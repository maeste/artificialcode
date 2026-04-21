# Output Format

The final artifact produced by this skill is a single markdown file consumed by `buffer-social-scheduler/scripts/schedule.py`. The format below is the minimum required; consult `.claude/skills/buffer-social-scheduler/references/INPUT_FORMAT.md` for the authoritative spec.

## Skeleton

```markdown
# Campagna: <campaign name>

Optional one-paragraph description. Not parsed; useful for humans reviewing the file.

## Post #1 — <optional label, ignored by parser>
- channel: <alias from .buffer/channels.json>
- date: <ISO-8601 in UTC, e.g. 2026-04-08T14:00:00Z>
- media: <path relative to repo root OR https URL>

<post body>

## Post #2 — <...>
- channel: <...>
- date: <...>
- media: <...>

<post body>
```

## Rules

1. **Campaign header**: first H1 starts with `# Campagna:` (Italian) or `# Campaign:` (English), followed by the name. The name is slugified by the scheduler to create `.buffer/scheduled-<slug>.json`.

2. **Post headers**: `## Post #<N>` where `<N>` is a positive integer. Anything after the number on the same line is ignored by the parser but useful as a human label.

3. **Metadata block**: contiguous lines immediately after the post header, each `- key: value`. Keys: `channel`, `date`, `media`. A blank line or a non-`- ` line ends the metadata.

4. **Date format**: ISO-8601 with timezone. Use `Z` for UTC. Example: `2026-04-08T14:00:00Z`. Always convert from the user's local time to UTC before writing.

5. **Channel aliases**: must match the ones in `.buffer/channels.json`. If the file does not exist, use descriptive placeholders like `linkedin_personal` and warn the user that they must either create `.buffer/channels.json` or rename aliases before scheduling.

6. **Media**:
   - Omit the line entirely if the post has no media.
   - If media is a local path, use a path relative to the repository root (e.g. `social/media/foo.png`). The scheduler will compute the GitHub raw URL.
   - If media is already a public URL, use it directly with `https://` prefix.
   - Do not invent media. If the user has not supplied media, either omit `media:` or leave a comment like `<!-- media TBD -->` inside the markdown for human review.

7. **Post body**: everything after the metadata block until the next `## Post #` header or end of file. Leading and trailing blank lines are stripped by the scheduler.

8. **Ordering**: write posts in chronological order by `date`. The parser accepts any order but human review is easier chronologically.

## Time zone conventions

Italian timezone (Europe/Rome) during DST is UTC+2:
- 10:00 local → `08:00:00Z`
- 16:00 local → `14:00:00Z`

Italian timezone in winter (standard time) is UTC+1:
- 10:00 local → `09:00:00Z`
- 16:00 local → `15:00:00Z`

Confirm with the user whether posts are in DST window before computing UTC offsets. The default assumption in this project is Europe/Rome.

## Common mistakes to avoid

- **Naive datetime**: `2026-04-08T14:00:00` without a timezone is rejected by the scheduler. Always include `Z` or an offset.
- **Unresolved mentions**: do not leave `@[Page Name]` as a placeholder to be filled later. Include the mention in the text as-is; the user will edit it in Buffer UI after publication (LinkedIn API does not support page mentions).
- **Duplicate first lines**: posts on the same channel with near-identical openings will be rejected by Buffer. Vary opening sentences substantially.
- **Over limit**: X/Twitter posts over 280 chars will hard-fail in the scheduler. LinkedIn over 3000 will warn. Respect the limits in VOICE_GUIDELINES.md.
