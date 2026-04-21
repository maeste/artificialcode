# Brief Format (optional)

A `brief.md` file is an optional structured way to provide campaign intake. If present, it replaces interactive questioning in Step 1. If absent, the planner asks the same questions conversationally.

## Template

```markdown
# Brief: <campaign-name>

## Objective
<One sentence describing what success looks like. Example: "drive GitHub stars on the lince repo" or "convert newsletter readers to podcast listeners".>

## Audience
<Who you want to reach. Be specific: seniority, role, prior knowledge, pain points.>

## Core message
<The single most important idea, in one sentence. If you can't compress it to one sentence, the campaign is unfocused.>

## Platforms and accounts
- LinkedIn (personal account `maeste`): voice "I"
- LinkedIn (company page `risorseartificiali`): voice "we/noi"
- X (personal account `maeste`): voice "I"

## Duration
- Start: 2026-04-08
- End: 2026-04-19

## Frequency per channel
- LinkedIn EN: 2 posts/week
- LinkedIn IT: 2 posts/week
- X EN: 3 posts/week

## Constraints
- No LinkedIn IT on Saturdays (podcast post at 13:00)
- No posts on Wednesday April 16 (interview publication at 17:00)
- Italian posts at 10:00 CEST (08:00 UTC)
- English posts at 16:00 CEST (14:00 UTC)

## Key references
- Conference quote: "The attack surface is you, not your software."
- Numbers: sweet spot 3-5 agents in parallel
- Vendor event: Anthropic blocked third-party subscription access on April 4

## Sources
- newsletter/it/CY26W15-it.md
- https://lince.sh
- https://github.com/RisorseArtificiali/lince
```

## Fields

| Field | Required | Notes |
|-------|----------|-------|
| Objective | yes | Drives angle selection |
| Audience | yes | Drives tone and technical depth |
| Core message | yes | Must appear (explicitly or implicitly) in every post |
| Platforms | yes | Must match `.buffer/channels.json` aliases if using the scheduler |
| Duration | yes | Used to build publication plans |
| Frequency | yes | Constrains plan shape |
| Constraints | no | Blackouts, conflicts, time preferences |
| Key references | no | Quotes, numbers, anecdotes to preserve across alternatives |
| Sources | no | Documents to read for context (paths or URLs) |

## Voice overrides

If a channel should use a non-default voice, specify it explicitly:

```markdown
## Platforms and accounts
- LinkedIn (`risorseartificiali`): voice "I" (founder-led, exception to team default)
```

Without overrides, the planner applies defaults:
- LinkedIn company pages: "we/noi"
- LinkedIn personal: "I/io"
- X, Instagram, Threads, Bluesky personal: "I/io"
- Organization-level accounts on any platform: "we/noi"
