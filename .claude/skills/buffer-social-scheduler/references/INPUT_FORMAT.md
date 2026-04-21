# Campaign Markdown Format

A campaign is a single markdown file describing one or more scheduled social posts.

## Structure

```markdown
# Campaign: <Campaign Name>

Optional free-text description. Ignored by the parser.

## Post #1 — Optional label (ignored)
- channel: <channel_alias>
- date: <ISO-8601 datetime in UTC>
- media: <local path OR public URL, optional>

Post body goes here.

Multiple paragraphs allowed. Hashtags at the end are fine.

#Hashtag1 #Hashtag2

## Post #2 — ...
- channel: <channel_alias>
- date: <ISO-8601 datetime in UTC>

Another post body.
```

## Rules

### Campaign header

- The first H1 `# Campaign: <name>` is required. `<name>` is used as the state file name (`.buffer/scheduled-<name>.json`), slugified.
- Any paragraph between the H1 and the first `## Post #` is ignored.

### Post headers

- Each post starts with `## Post #<N>` where `<N>` is a positive integer.
- Post numbers should be unique but do not need to be sequential.
- Anything after the post number on the same line (em dashes, labels, dates) is ignored by the parser.

### Post metadata

Immediately after the post header, put one metadata field per line, prefixed with `- `:

- **`channel`** (required): alias defined in `.buffer/channels.json`. Example: `li_en`, `x_maeste`.
- **`date`** (required): ISO-8601 datetime with timezone. Example: `2026-04-08T14:00:00Z` or `2026-04-08T14:00:00+00:00`. Always UTC.
- **`media`** (optional): either a path relative to the project root (e.g. `social/media/hero.png`) or an absolute `https://` URL.

Metadata stops at the first blank line or the first line not starting with `- `. The rest is the post body.

### Post body

- Everything after the metadata block until the next `## Post #` header or end of file.
- Leading and trailing blank lines are stripped.
- The body is posted as-is, preserving line breaks.

## Character limits

The scheduler enforces character limits based on the channel's service (resolved via `channels.json`):

| Service | Limit | Enforcement |
|---------|-------|-------------|
| twitter | 280 | Hard error |
| linkedin | 3000 | Warning above 3000, hard error above 8000 |
| facebook | 63206 | Warning |
| instagram | 2200 | Warning |

## Media handling

- If `media:` starts with `http://` or `https://`, it is used as-is.
- If it is a local path, the scheduler checks that it is committed and pushed to the GitHub remote of the current branch. If not, it stages and commits the file (grouped), then asks the user to push.
- The public URL is then computed as:
  `https://raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`

## Example

See the `campaign-example.md` output of a dry-run for a real example, or look at `social/campagna-finale-lince.md` in the project as a full-scale reference.

## Common mistakes

- **Missing timezone** on `date`: the parser rejects naive datetimes. Always include `Z` or an offset.
- **Channel alias typo**: if the alias is not in `channels.json`, the dry-run reports it. Check the alias file.
- **Metadata after blank line**: metadata must be contiguous lines immediately after the post header. A blank line ends metadata parsing.
- **Too similar posts**: Buffer's duplicate detection flags posts that share many words. The dry-run warns about high-similarity pairs on the same channel.
