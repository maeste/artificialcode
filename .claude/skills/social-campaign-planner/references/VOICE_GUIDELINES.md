# Voice Guidelines

Platform-specific rules for generating post alternatives. These are hard constraints, not style suggestions.

## Universal rules

- **No em dashes (—)**. Use commas or parentheses instead. This is a project-wide preference.
- **URLs include `https://`**. Do not abbreviate as `lince.sh` in final posts. Use `https://lince.sh`.
- **No placeholder text**. Every alternative must be publishable as-is after the user confirms.
- **Preserve explicit quotes**. If the brief cites exact phrasing, reproduce it verbatim in quotes.

## LinkedIn (personal account)

- **Pronoun**: first-person singular ("I", "io")
- **Length**: 800-1500 characters is the sweet spot. Up to 3000 is acceptable for deep content. Above 3000 triggers a warning from the scheduler.
- **First line**: only first line is visible before "...see more". Make it provocative, specific, or a hook that forces a click.
- **Paragraph breaks**: use blank lines between paragraphs. LinkedIn renders them well.
- **Hashtags**: 3-5 at the end, relevant and searched. Avoid generic tags like `#AI` alone.
- **Mentions**: `@[Page Name]` syntax is for the Buffer UI; tagging will NOT work via API. Document this for the user and suggest they edit after publication.
- **Style**: narrative, personal, opinionated. Share a specific anecdote, a contrarian take, or a concrete number. Avoid corporate marketing tone.

## LinkedIn (company page)

All rules above, plus:

- **Pronoun**: first-person plural ("we", "noi"). Refer to individual team members by first name when relevant ("il nostro Stefano ha detto..."). Never "I" on a company page.
- **Style**: slightly more formal than personal, but still human. Avoid third-person corporate speak ("LINCE is a product that..."). Prefer "abbiamo costruito...", "ci siamo accorti...".

## X / Twitter (personal)

- **Pronoun**: first-person singular
- **Length**: hard limit 280 characters (default tier). If the user has X Premium, up to 25,000 is technically possible but not recommended for reach. Default to 280.
- **URL handling**: URLs count as 23 characters regardless of actual length. Count against the 280 budget.
- **First line / standalone value**: the first and only tweet must deliver value by itself. No cliffhangers.
- **Hashtags**: omit on X. Research in 2024-2026 consistently shows hashtags reduce reach on X. Exception: occasionally a single, highly relevant hashtag works for discovery.
- **Link placement**: at the end, separated by a blank line. Buffer handles this correctly.
- **Style**: punchy, direct, often provocative. A concrete claim, a counter-intuitive observation, or a sharp opinion. Avoid questions as openers (engagement-bait pattern performs poorly now).

## X / Twitter (company)

Same as above, with "we" instead of "I". Rarely used for companies at Codice Artificiale; the main X account is personal.

## Instagram (any)

- **Length**: up to 2200 characters
- **Hashtags**: 5-15, mix of popular and niche
- **Style**: visual-first. Text is caption; media is the primary communication.
- **Call-to-action**: explicit (e.g., "link in bio")

## Threads

- **Length**: 500 characters
- **Style**: casual, conversational. Less polished than LinkedIn.
- **Hashtags**: sparingly, 1-3.

## Bluesky

- **Length**: 300 characters hard limit
- **Style**: similar to early Twitter, developer-friendly
- **Hashtags**: 1-2 at most

## Mastodon

- **Length**: 500 characters (default instance setting)
- **Style**: community-oriented, more technical depth welcomed
- **Content warnings**: use CW for off-topic or sensitive content
- **Hashtags**: important for federated discovery, 2-5

## Company vs personal voice in practice

When writing alternatives, maintain these patterns:

**Personal**: "I built...", "Ho costruito...", "When I tried...", "Quando ho provato..."

**Company**: "We built...", "Abbiamo costruito...", "Our team found that...", "Il nostro team..."

**Never mix**: do not use "I" on a company page even when referring to a team member's action. Instead, reference them: "Our colleague Stefano said at Voxxed Day...".
