---
name: buffer-social-scheduler
description: Schedule social media campaigns via Buffer GraphQL API with automatic media pipeline via GitHub. Supports LinkedIn, X/Twitter, and other channels. Dry-run by default, duplicate detection, character limit validation, delete/reschedule workflow. Use when user says "schedule social campaign", "schedule buffer posts", "programma campagna social", or "buffer scheduling".
metadata:
  author: codiceartificiale
  version: "1.0"

scripts:
  - path: scripts/init_channels.py
    name: init_channels
    description: Fetch Buffer channels and save aliases for the project
  - path: scripts/schedule.py
    name: schedule
    description: Schedule a campaign from a markdown file (dry-run by default)
  - path: scripts/delete.py
    name: delete
    description: Delete posts previously scheduled for a campaign
---

# Buffer Social Scheduler

Schedule social media campaigns via Buffer GraphQL API. Each campaign is described in a single markdown file. The skill handles validation, media upload to GitHub for public URLs, and the actual scheduling.

## Trigger Phrases

- "schedule social campaign" / "programma campagna social"
- "schedule buffer posts" / "programma post buffer"
- "buffer scheduling"
- "pubblica campagna social"

## Prerequisites

Before first use:

1. **Buffer API key**: export as `BUFFER_API_KEY` environment variable. Get it from https://publish.buffer.com/settings/api
2. **Git repository with GitHub remote**: required for auto media upload
3. **Python 3.8+**: uses stdlib only

## Workflow

### Step 0: Initialize Channels (once per project)

Ask the user to run:
```bash
python3 .claude/skills/buffer-social-scheduler/scripts/init_channels.py
```

This fetches the Buffer channels and prompts the user to assign an alias to each. Result saved to `.buffer/channels.json` in the project root.

Skip this step if `.buffer/channels.json` already exists. Check first.

### Step 1: Campaign Markdown

Ask the user for the path to the campaign markdown file, or help them create one.

See [references/INPUT_FORMAT.md](references/INPUT_FORMAT.md) for the exact format.

### Step 2: Dry-Run (always first)

Run:
```bash
python3 .claude/skills/buffer-social-scheduler/scripts/schedule.py <campaign.md>
```

The script runs in dry-run mode by default. It:
- Parses the campaign file
- Validates each post (channels exist, char limits, dates, media files)
- Detects potential duplicates between posts on the same channel
- Reports media files that need to be committed and pushed
- Shows a full summary of what would be scheduled

Report the output to the user. If there are errors or warnings, help the user fix them before proceeding.

### Step 3: Media Upload (if needed)

If dry-run reports uncommitted or unpushed media files:

1. Stage and commit the media files on behalf of the user
2. Ask the user to run `git push` (do NOT push automatically)
3. Wait for the user to confirm the push is done
4. Verify the files are accessible at their GitHub raw URLs

See [references/MEDIA_PIPELINE.md](references/MEDIA_PIPELINE.md) for details.

### Step 4: Confirm and Schedule

Once dry-run is clean and media is accessible, run:
```bash
python3 .claude/skills/buffer-social-scheduler/scripts/schedule.py <campaign.md> --confirm
```

This actually schedules the posts via Buffer API. After success, the Buffer post IDs are saved to `.buffer/scheduled-<campaign-name>.json` for later deletion or rescheduling.

Report the result, including which posts failed (duplicate detection, etc.) and suggest fixes.

### Step 5: Delete / Reschedule (separate)

To cancel all posts for a campaign:
```bash
python3 .claude/skills/buffer-social-scheduler/scripts/delete.py <campaign.md>
```

This reads the state file, lists the scheduled posts, asks for confirmation, and deletes them via API.

To reschedule: delete, then schedule again with updated markdown.

## Important Rules

1. **Dry-run first, always.** Never skip the dry-run. It catches char limit violations, missing channels, and duplicate content that Buffer would reject.

2. **One commit per media batch.** When uploading media, stage all missing files and create a single commit. Do not create separate commits per file.

3. **Never push automatically.** Always ask the user to run `git push` themselves after the commit. Verify URLs are reachable before scheduling.

4. **Respect character limits.** Twitter/X hard limit is 280 by default (the script enforces). LinkedIn warns above 3000.

5. **Buffer gotchas:** Always use `User-Agent` header. Duplicate detection is aggressive. LinkedIn page mentions (`@[Page Name]`) do not work via API and must be edited manually after publication.

6. **State file as source of truth.** Never manually edit `.buffer/scheduled-*.json`. Use `delete.py` to remove posts, then `schedule.py` to add new ones.

## When Things Go Wrong

- **HTTP 403 with code 1010**: Missing or wrong User-Agent header. The script sets it automatically; this should not happen unless the API endpoint changes.
- **"it looks like you've posted that one recently"**: Buffer's duplicate detection. Reword the post substantially (first line is the most sensitive). Also happens after multiple failed creation attempts on the same channel (cooldown of several minutes).
- **403 on media URL**: The file is not accessible. Verify `git push` completed and the URL resolves with `curl -I`.
- **Channel not found**: `.buffer/channels.json` alias does not match. Re-run `init_channels.py` or edit the campaign file.

See [references/BUFFER_API.md](references/BUFFER_API.md) for the full list of Buffer API quirks.

## Success Criteria

- Campaign markdown parsed without errors
- All posts validated (channels, chars, dates, media)
- Media files committed and pushed to GitHub with public URLs reachable
- Dry-run output reviewed and approved by user
- Posts scheduled successfully via Buffer API
- State file saved for later deletion/rescheduling
- Post IDs reported back to the user with scheduled dates
