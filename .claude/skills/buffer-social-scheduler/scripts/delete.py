#!/usr/bin/env python3
"""Delete posts previously scheduled for a campaign.

Usage:
    python3 delete.py <campaign.md>                 # interactive confirmation
    python3 delete.py <campaign.md> --yes           # skip confirmation
"""

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from buffer_client import BufferClient, BufferError


CONFIG_DIR = Path(".buffer")


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def campaign_slug_from_file(path):
    text = Path(path).read_text(encoding="utf-8")
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            m = re.match(r"^#\s+(?:Campaign:|Campagna:)\s*(.+?)\s*$", stripped, re.IGNORECASE)
            name = m.group(1) if m else stripped[2:].strip()
            return slug(name)
    raise ValueError("Campaign name not found in markdown")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("campaign", help="Path to the campaign markdown file")
    parser.add_argument("--yes", action="store_true", help="Skip interactive confirmation")
    args = parser.parse_args()

    camp_slug = campaign_slug_from_file(args.campaign)
    state_file = CONFIG_DIR / f"scheduled-{camp_slug}.json"
    if not state_file.exists():
        print(f"No state file at {state_file}. Nothing to delete.")
        sys.exit(0)

    state = json.loads(state_file.read_text())
    posts = state.get("posts", [])
    if not posts:
        print(f"No posts recorded in {state_file}.")
        sys.exit(0)

    print(f"Campaign slug: {camp_slug}")
    print(f"State file: {state_file}")
    print(f"Posts to delete: {len(posts)}\n")
    for p in posts:
        print(f"  #{p['post_num']}  {p['due_at']}  {p['channel_alias']}  buffer_id={p['buffer_id']}")

    if not args.yes:
        confirm = input("\nDelete all of the above? [y/N]: ").strip().lower()
        if confirm != "y":
            print("Aborted.")
            sys.exit(0)

    try:
        client = BufferClient()
    except BufferError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    remaining = []
    deleted = 0
    for p in posts:
        try:
            ok = client.delete_post(p["buffer_id"])
            if ok:
                print(f"  DELETED #{p['post_num']} ({p['buffer_id']})")
                deleted += 1
            else:
                print(f"  UNEXPECTED #{p['post_num']} ({p['buffer_id']}) - response not DeletePostSuccess")
                remaining.append(p)
        except BufferError as e:
            print(f"  FAIL #{p['post_num']} ({p['buffer_id']}): {e}")
            remaining.append(p)

    if remaining:
        state_file.write_text(json.dumps({"posts": remaining}, indent=2) + "\n")
        print(f"\n{len(remaining)} post(s) could not be deleted; state file kept.")
        sys.exit(4)
    else:
        state_file.unlink()
        print(f"\nDeleted {deleted} post(s). State file removed.")


if __name__ == "__main__":
    main()
