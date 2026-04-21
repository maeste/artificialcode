---
name: social-campaign-planner
description: Collaborative design of multi-post social media campaigns. Reads source documents (newsletter, README, product docs) plus a brief, proposes strategic angles, generates platform-specific alternatives, drafts publication plans, and materializes a campaign markdown file compatible with the buffer-social-scheduler skill. Use when user says "pianifica campagna social", "social campaign planning", "design social campaign", or "progetta campagna".
metadata:
  author: codiceartificiale
  version: "1.0"
---

# Social Campaign Planner

Collaborative, step-by-step design of a social media campaign. Produces a markdown file in the format consumed by `buffer-social-scheduler` (see that skill's `INPUT_FORMAT.md`). This skill is conversational and does not execute code; it guides the user through strategic decisions.

## Trigger Phrases

- "pianifica campagna social" / "plan social campaign"
- "progetta campagna" / "design social campaign"
- "social campaign planning"
- "campaign planner"

## Relationship with buffer-social-scheduler

This skill is **separate** and **upstream**. Its only output is a campaign markdown file. The user then passes that file to `buffer-social-scheduler/scripts/schedule.py` for validation and actual scheduling.

Do NOT invoke Buffer API calls from this skill. If the user wants to schedule, tell them to run the scheduler skill.

## Workflow

### Step 0: Source materials

Ask the user for source documents that describe what is being promoted. Examples: a newsletter article, a project README, a product landing page, a deep-dive markdown. Read them with the Read tool.

If the user says "no docs, just a brief", proceed to Step 1 without source materials.

Check if `.buffer/channels.json` exists in the project. If yes, read it and note the available channels, services, and account names. This will inform default voice and platform choices in later steps.

### Step 1: Brief intake

Ask the user for the brief. Accept either a path to a `brief.md` (see [references/BRIEF_FORMAT.md](references/BRIEF_FORMAT.md)) or collect the information interactively. Required fields:

- **Campaign objective**: what success looks like (e.g., "drive stars on the GitHub repo", "grow newsletter subscribers")
- **Audience**: who you want to reach
- **Core message**: the single most important idea (one sentence)
- **Platforms and accounts**: which channels from `.buffer/channels.json` (or explicit names), and which voice each uses (personal vs team)
- **Duration**: start date, end date
- **Frequency per channel**: e.g., "LinkedIn EN 2/week, LinkedIn IT 2/week, X 3/week"
- **Constraints**: blackout dates, time preferences, existing posts that conflict
- **Key references**: specific phrases, facts, or anecdotes the user wants to keep (e.g., conference quotes, concrete numbers)

If the user uses speech-to-text, apply the same STT proofreading rules as other conversational skills in this project (punctuation, capitalization, filler removal). Do not change content.

### Step 2: Propose strategic angles

Based on source materials and brief, propose 3 to 5 narrative angles. Each angle is a distinct "story" to tell about the subject. For each angle provide:

- **Name**: short label
- **Hook**: the punchy idea that opens posts on this angle
- **Why it works**: rationale (what it triggers in the audience)
- **Best platform fit**: where this angle performs best (LinkedIn vs X)

Present as a table or list. **Do NOT generate post text yet.** Wait for the user to select which angles to use (typically 3-4 out of 5).

If the user proposes an additional angle or rejects some, iterate.

### Step 3: Generate alternatives per angle per platform

For each selected angle and each platform (LinkedIn personal, LinkedIn company, X, others), generate **3 alternatives**. Each alternative is a complete, ready-to-post text.

Apply platform voice rules strictly. See [references/VOICE_GUIDELINES.md](references/VOICE_GUIDELINES.md) for:
- LinkedIn personal: first-person "I", 800-1500 chars, strong first line visible before "...see more", 3-5 hashtags, narrative style
- LinkedIn company: first-person plural "we/noi", same length, reference founder/team by name when appropriate
- X/Twitter: under 280 chars, punchy first line, link at end, no hashtags (they reduce reach on X in 2026)
- Others: see VOICE_GUIDELINES.md for Instagram, Threads, Mastodon, Bluesky

Process one angle at a time. Present the 3 alternatives for each platform, wait for user selection (or iteration), then move to the next angle. Keep track of selected alternatives for Step 5.

Rules:
- Preserve key references from the brief (conference quotes, concrete numbers, specific terminology) across alternatives
- Do NOT use em dashes anywhere (project-wide preference)
- Ensure posts on the same channel are substantially different (Buffer rejects near-duplicates on the same queue)
- Include `https://` in all URLs explicitly

### Step 4: Publication plans

Propose 2 to 3 alternative publication plans covering the whole duration. Each plan is a table with columns: `Day | Date | Platform | Angle/Alt | Rationale`.

Plan shapes to consider:
- **Burst / sprint**: high frequency in first week, lighter second week
- **Sustained**: even cadence across the whole period
- **Narrative arc**: story first, features next, CTA last
- **Community-driven**: fewer posts but spaced out for engagement

For each plan apply:
- Respect the frequency declared in the brief
- Respect blackout dates and conflicting posts
- Day-of-week awareness: Mon/Tue/Wed/Thu peak for LinkedIn; Sat good for provocative dev content on X; Fri more casual
- Base times: Italian posts default 10:00 local (08:00 UTC); English posts default 16:00 local (14:00 UTC); override per brief

Wait for the user to choose a plan or request modifications.

### Step 5: Optional Marp previews

Ask the user if they want a Marp slide-deck per plan, where each slide = one scheduled day (platform + opening hook + rationale). If yes, write the Marp files in the same directory as the output campaign, named `plan-<id>.md`.

This step is optional. Default to skipping unless the user asks.

### Step 6: Materialize the campaign markdown

Output a single markdown file in the format expected by `buffer-social-scheduler`. See [references/OUTPUT_FORMAT.md](references/OUTPUT_FORMAT.md) for the exact structure.

File layout:
```markdown
# Campagna: <name>

Optional description.

## Post #1 — <label>
- channel: <alias>
- date: <YYYY-MM-DDTHH:MM:SSZ>
- media: <local path OR https URL, optional>

<body of the post>
```

Rules:
- Use channel aliases from `.buffer/channels.json` when available; otherwise use descriptive placeholders and warn the user
- Dates in ISO-8601 UTC with `Z` suffix
- One post per selected alternative per slot in the chosen plan
- Post numbers sequential starting from 1
- Order posts chronologically
- Include media paths if media was discussed; otherwise omit

After writing the file, tell the user:
1. The path of the generated campaign file
2. That the next step is `python3 .claude/skills/buffer-social-scheduler/scripts/schedule.py <path>` for dry-run
3. Any LinkedIn page mentions (`@[Page]`) are NOT supported via API and must be edited manually after scheduling

## Important Rules

1. **Conversational, not autonomous.** Wait for user confirmation between steps. Do not materialize until angles, alternatives, and plan are all confirmed.

2. **One output file.** At the end, produce exactly one markdown file compatible with buffer-social-scheduler. No intermediate files unless the user asks (e.g., Marp presentations).

3. **Voice discipline.** Platform voice rules in VOICE_GUIDELINES.md are hard constraints, not suggestions. Never use "I" on a company account. Never exceed 280 on X. Never use em dashes anywhere.

4. **Preserve user content.** When the brief cites specific quotes, numbers, or anecdotes, every generated alternative must use them correctly. Do not paraphrase away from a user's chosen phrasing.

5. **Respect cross-channel similarity.** Between posts on the same channel queue, ensure opening lines differ substantially. Buffer rejects near-duplicates.

6. **Link the scheduler, don't invoke it.** This skill produces input for `buffer-social-scheduler`. It never calls the Buffer API or schedules anything.

## Success Criteria

- Source materials and brief gathered
- 3-5 angles proposed, subset selected by user
- 3 alternatives per angle per platform generated and curated
- 2-3 publication plans proposed, one chosen
- Optional: Marp previews generated
- Final campaign markdown file written in buffer-social-scheduler format
- User informed of next step (scheduler invocation) and manual-edit caveats (LinkedIn page mentions)
