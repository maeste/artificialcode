#!/usr/bin/env python3
"""Schedule a campaign of social posts via Buffer API.

Usage:
    python3 schedule.py <campaign.md>                  # dry-run (default)
    python3 schedule.py <campaign.md> --confirm        # actually schedule

The script:
    1. Parses the campaign markdown.
    2. Validates channels, char limits, dates, media, plan limits, duplicates.
    3. Prepares media (GitHub upload pipeline for local paths).
    4. In --confirm mode, schedules each post via Buffer API and saves state.
"""

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from buffer_client import BufferClient, BufferError


CONFIG_DIR = Path(".buffer")
CHANNELS_FILE = CONFIG_DIR / "channels.json"
OPTIONAL_CONFIG_FILE = CONFIG_DIR / "config.json"

CHAR_LIMITS = {
    "twitter": (280, "hard"),
    "linkedin": (3000, "warn"),
    "facebook": (63206, "warn"),
    "instagram": (2200, "warn"),
    "threads": (500, "warn"),
    "mastodon": (500, "warn"),
    "bluesky": (300, "hard"),
}

PLAN_LIMIT_PER_CHANNEL = 10
SIMILARITY_WARN_THRESHOLD = 0.5


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def run(cmd, check=True, capture=True):
    result = subprocess.run(
        cmd,
        capture_output=capture,
        text=True,
        check=False,
    )
    if check and result.returncode != 0:
        raise RuntimeError(
            f"Command failed: {' '.join(cmd)}\nstderr: {result.stderr.strip()}"
        )
    return result


def parse_campaign(path):
    """Parse a campaign markdown file into a dict.

    Returns:
        {
            "name": str,
            "slug": str,
            "posts": [ {id, channel, date, media, text, raw_header}, ... ],
        }
    """
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()

    # Campaign name from the first H1
    name = None
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            m = re.match(r"^#\s+(?:Campaign:|Campagna:)\s*(.+?)\s*$", stripped, re.IGNORECASE)
            name = m.group(1) if m else stripped[2:].strip()
            break
    if not name:
        raise ValueError("Campaign markdown must start with '# Campaign: <name>' or '# Campagna: <name>'")

    # Split on post headers
    post_header_re = re.compile(r"^##\s+Post\s+#(\d+)\b(.*)$", re.IGNORECASE)
    posts = []
    current = None
    in_metadata = True
    body_lines = []

    for line in lines:
        m = post_header_re.match(line)
        if m:
            if current is not None:
                current["text"] = "\n".join(body_lines).strip()
                posts.append(current)
            current = {
                "id": int(m.group(1)),
                "raw_header": line.strip(),
                "channel": None,
                "date": None,
                "media": None,
                "text": "",
            }
            in_metadata = True
            body_lines = []
            continue

        if current is None:
            continue

        if in_metadata:
            stripped = line.strip()
            if not stripped:
                # Blank line: if no metadata collected yet, keep looking
                if current["channel"] is not None or current["date"] is not None or current["media"] is not None:
                    in_metadata = False
                continue
            md_match = re.match(r"^-\s+(\w+)\s*:\s*(.+?)\s*$", stripped)
            if md_match:
                key = md_match.group(1).lower()
                value = md_match.group(2).strip()
                if key in ("channel", "date", "media"):
                    current[key] = value
                    continue
            # Non-metadata line: start of body
            in_metadata = False
            body_lines.append(line)
        else:
            body_lines.append(line)

    if current is not None:
        current["text"] = "\n".join(body_lines).strip()
        posts.append(current)

    return {"name": name, "slug": slug(name), "posts": posts}


def parse_iso(value):
    """Parse an ISO-8601 datetime with timezone into a datetime object."""
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    try:
        parsed = dt.datetime.fromisoformat(value)
    except ValueError as e:
        raise ValueError(f"Invalid date format '{value}': expected ISO-8601 with timezone") from e
    if parsed.tzinfo is None:
        raise ValueError(f"Date '{value}' has no timezone. Use 'Z' or an offset.")
    return parsed


def format_due_at(parsed):
    """Return the exact format Buffer expects: YYYY-MM-DDTHH:MM:SS.000Z (UTC)."""
    utc = parsed.astimezone(dt.timezone.utc)
    return utc.strftime("%Y-%m-%dT%H:%M:%S.000Z")


def load_channels():
    if not CHANNELS_FILE.exists():
        raise FileNotFoundError(
            f"{CHANNELS_FILE} not found. Run init_channels.py first."
        )
    return json.loads(CHANNELS_FILE.read_text())


def load_optional_config():
    if OPTIONAL_CONFIG_FILE.exists():
        return json.loads(OPTIONAL_CONFIG_FILE.read_text())
    return {}


def jaccard(a, b):
    tokens_a = set(re.findall(r"\w+", a.lower()))
    tokens_b = set(re.findall(r"\w+", b.lower()))
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def github_url_for(path, config):
    """Return the raw.githubusercontent.com URL for a local path."""
    override_owner = config.get("github_owner")
    override_repo = config.get("github_repo")
    override_branch = config.get("github_branch")

    if override_owner and override_repo and override_branch:
        owner, repo, branch = override_owner, override_repo, override_branch
    else:
        remote = run(["git", "remote", "get-url", "origin"], check=False)
        if remote.returncode != 0:
            raise RuntimeError(
                "No git remote 'origin' found. Add a GitHub remote or set github_owner/github_repo/github_branch in .buffer/config.json"
            )
        url = remote.stdout.strip()
        m = re.match(r"(?:https://github\.com/|git@github\.com:)([^/]+)/([^/.]+)(?:\.git)?/?$", url)
        if not m:
            raise RuntimeError(
                f"Remote '{url}' is not a GitHub URL. Set github_owner/github_repo/github_branch in .buffer/config.json as fallback."
            )
        owner, repo = m.group(1), m.group(2)
        branch_result = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], check=False)
        if branch_result.returncode != 0:
            raise RuntimeError("Unable to determine current git branch")
        branch = override_branch or branch_result.stdout.strip()

    # Ensure path is forward slashes and not absolute
    rel = Path(path)
    if rel.is_absolute():
        try:
            repo_root = Path(run(["git", "rev-parse", "--show-toplevel"]).stdout.strip())
            rel = rel.relative_to(repo_root)
        except Exception as e:
            raise RuntimeError(f"Path {path} is absolute and outside the repo: {e}")
    rel_str = str(rel).replace("\\", "/")
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{rel_str}"


def media_status(path):
    """Return one of: 'missing', 'untracked', 'modified', 'committed-unpushed', 'pushed'."""
    if not Path(path).exists():
        return "missing"
    tracked = run(["git", "ls-files", "--error-unmatch", path], check=False)
    if tracked.returncode != 0:
        return "untracked"
    diff = run(["git", "diff", "--quiet", "--", path], check=False)
    if diff.returncode != 0:
        return "modified"
    # Check if HEAD is ahead of origin on the current branch
    branch_result = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], check=False)
    if branch_result.returncode != 0:
        return "committed-unpushed"
    branch = branch_result.stdout.strip()
    ahead = run(
        ["git", "rev-list", f"origin/{branch}..HEAD", "--count"],
        check=False,
    )
    if ahead.returncode != 0:
        return "committed-unpushed"
    # If ahead > 0, maybe. But we also want to know if the file's last commit is in the pushed set.
    last_commit = run(["git", "log", "-n", "1", "--format=%H", "--", path], check=False)
    if last_commit.returncode != 0 or not last_commit.stdout.strip():
        return "committed-unpushed"
    sha = last_commit.stdout.strip()
    contains = run(
        ["git", "branch", "-r", "--contains", sha],
        check=False,
    )
    if contains.returncode != 0 or not contains.stdout.strip():
        return "committed-unpushed"
    return "pushed"


def url_reachable(url):
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "buffer-social-scheduler/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return 200 <= resp.status < 400
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return False


def validate(campaign, channels):
    """Return (errors, warnings, resolved_posts)."""
    errors = []
    warnings = []
    resolved = []
    seen_ids = set()
    by_channel = {}

    for post in campaign["posts"]:
        pid = post["id"]
        if pid in seen_ids:
            errors.append(f"Post #{pid}: duplicate post number")
        seen_ids.add(pid)

        if not post["channel"]:
            errors.append(f"Post #{pid}: missing 'channel' metadata")
            continue
        if post["channel"] not in channels:
            errors.append(
                f"Post #{pid}: channel alias '{post['channel']}' not in .buffer/channels.json"
            )
            continue
        channel_info = channels[post["channel"]]
        service = channel_info["service"]

        if not post["date"]:
            errors.append(f"Post #{pid}: missing 'date' metadata")
            continue
        try:
            parsed_date = parse_iso(post["date"])
        except ValueError as e:
            errors.append(f"Post #{pid}: {e}")
            continue
        if parsed_date <= dt.datetime.now(dt.timezone.utc):
            errors.append(
                f"Post #{pid}: date {post['date']} is not in the future"
            )

        if not post["text"]:
            errors.append(f"Post #{pid}: body is empty")

        # Char limits
        limit, mode = CHAR_LIMITS.get(service, (None, None))
        if limit is not None:
            length = len(post["text"])
            if length > limit:
                msg = f"Post #{pid}: text is {length} chars, exceeds {service} limit of {limit}"
                if mode == "hard":
                    errors.append(msg)
                else:
                    warnings.append(msg)

        by_channel.setdefault(channel_info["id"], []).append((pid, post["text"]))

        resolved.append(
            {
                "id": pid,
                "channel_alias": post["channel"],
                "channel_id": channel_info["id"],
                "service": service,
                "date": format_due_at(parsed_date),
                "media": post["media"],
                "text": post["text"],
            }
        )

    # Plan limit
    for cid, items in by_channel.items():
        if len(items) > PLAN_LIMIT_PER_CHANNEL:
            warnings.append(
                f"Channel id {cid}: {len(items)} posts scheduled, Buffer free plan allows max {PLAN_LIMIT_PER_CHANNEL} in queue"
            )

    # Similarity
    for cid, items in by_channel.items():
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                sim = jaccard(items[i][1], items[j][1])
                if sim >= SIMILARITY_WARN_THRESHOLD:
                    warnings.append(
                        f"Posts #{items[i][0]} and #{items[j][0]} on same channel: similarity {sim:.2f} (Buffer may reject as duplicate)"
                    )

    return errors, warnings, resolved


def prepare_media(resolved, config, confirm_mode):
    """For each post with local media, ensure it is committed and pushed.

    Modifies resolved[i]['media_url'] in place.
    Returns (needs_commit, needs_push) lists of paths.
    """
    needs_commit = []
    needs_push = []

    for post in resolved:
        if not post["media"]:
            post["media_url"] = None
            continue
        raw = post["media"]
        if raw.startswith("http://") or raw.startswith("https://"):
            post["media_url"] = raw
            post["media_source"] = "url"
            continue
        status = media_status(raw)
        post["media_source"] = "local"
        if status == "missing":
            post["media_url"] = None
            post["media_error"] = f"file not found: {raw}"
            continue
        if status in ("untracked", "modified"):
            needs_commit.append(raw)
        elif status == "committed-unpushed":
            needs_push.append(raw)
        try:
            post["media_url"] = github_url_for(raw, config)
        except RuntimeError as e:
            post["media_url"] = None
            post["media_error"] = str(e)

    return needs_commit, needs_push


def commit_media(files, campaign_name):
    run(["git", "add", "--"] + files)
    msg = f"Add media for {campaign_name} social campaign"
    run(["git", "commit", "-m", msg])


def print_dry_run(campaign, resolved, errors, warnings, needs_commit, needs_push):
    print(f"=== Campaign: {campaign['name']} ===")
    print(f"Slug: {campaign['slug']}")
    print(f"Posts: {len(resolved)}")
    print()

    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  - {e}")
        print()
    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"  - {w}")
        print()

    if needs_commit:
        print("MEDIA TO COMMIT:")
        for f in needs_commit:
            print(f"  - {f}")
        print()
    if needs_push:
        print("MEDIA TO PUSH:")
        for f in needs_push:
            print(f"  - {f}")
        print()

    print("PREVIEW:")
    for post in resolved:
        print(f"  #{post['id']}  {post['date']}  {post['channel_alias']} ({post['service']})")
        first_line = post["text"].splitlines()[0][:80] if post["text"] else "<empty>"
        print(f"    {len(post['text'])} chars: {first_line}")
        if post.get("media_url"):
            print(f"    media: {post['media_url']}")
        elif post.get("media_error"):
            print(f"    media ERROR: {post['media_error']}")
        print()


def save_state(campaign_slug, entries):
    CONFIG_DIR.mkdir(exist_ok=True)
    path = CONFIG_DIR / f"scheduled-{campaign_slug}.json"
    existing = []
    if path.exists():
        try:
            existing = json.loads(path.read_text()).get("posts", [])
        except Exception:
            existing = []
    existing.extend(entries)
    path.write_text(json.dumps({"posts": existing}, indent=2) + "\n")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("campaign", help="Path to the campaign markdown file")
    parser.add_argument("--confirm", action="store_true", help="Actually schedule (otherwise dry-run)")
    parser.add_argument("--skip-url-check", action="store_true", help="Skip HEAD check of media URLs before scheduling")
    args = parser.parse_args()

    campaign = parse_campaign(args.campaign)
    channels = load_channels()
    config = load_optional_config()

    errors, warnings, resolved = validate(campaign, channels)
    needs_commit, needs_push = prepare_media(resolved, config, confirm_mode=args.confirm)

    print_dry_run(campaign, resolved, errors, warnings, needs_commit, needs_push)

    if errors:
        print("Errors found. Fix them and re-run.")
        sys.exit(2)

    if not args.confirm:
        print("Dry-run complete. Re-run with --confirm to schedule.")
        sys.exit(0)

    # --- Confirm mode ---

    if needs_commit:
        print(f"\nCommitting {len(needs_commit)} media file(s)...")
        commit_media(needs_commit, campaign["name"])
        # After commit they still need push
        needs_push.extend(needs_commit)

    if needs_push:
        print("\nThe following media commits have not been pushed to origin:")
        for f in needs_push:
            print(f"  - {f}")
        print("\nRun 'git push' in another terminal, then press Enter here to continue.")
        input()

    if not args.skip_url_check:
        print("\nVerifying media URLs are reachable...")
        unreachable = []
        for post in resolved:
            if post.get("media_url"):
                if not url_reachable(post["media_url"]):
                    unreachable.append((post["id"], post["media_url"]))
        if unreachable:
            print("ERROR: the following media URLs are not reachable:")
            for pid, url in unreachable:
                print(f"  Post #{pid}: {url}")
            print("Check 'git push' completed and the repo is public. Aborting.")
            sys.exit(3)
        print("  All media URLs reachable.")

    try:
        client = BufferClient()
    except BufferError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"\nScheduling {len(resolved)} post(s)...")
    successes = []
    failures = []
    for post in resolved:
        try:
            res = client.create_post(
                text=post["text"],
                channel_id=post["channel_id"],
                due_at=post["date"],
                image_url=post.get("media_url"),
            )
            print(f"  OK   #{post['id']}  id={res['id']}  due={res['due_at']}")
            successes.append({
                "post_num": post["id"],
                "buffer_id": res["id"],
                "due_at": res["due_at"],
                "channel_alias": post["channel_alias"],
                "channel_id": post["channel_id"],
            })
        except BufferError as e:
            print(f"  FAIL #{post['id']}  {e}")
            failures.append({"post_num": post["id"], "error": str(e)})

    if successes:
        state_path = save_state(campaign["slug"], successes)
        print(f"\nSaved {len(successes)} post id(s) to {state_path}")

    print(f"\nDone: {len(successes)} scheduled, {len(failures)} failed")
    if failures:
        print("\nFailed posts can be retried after rewording (duplicate detection) or after a cooldown.")
        sys.exit(4)


if __name__ == "__main__":
    main()
