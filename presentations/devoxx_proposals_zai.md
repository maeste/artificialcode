# Devoxx Belgium 2026 — CfP Proposals

- **Conference:** Devoxx Belgium 2026 (Antwerp) — https://devoxx.be/
- **Theme:** *FROM DEVELOPER TO BUILDER* (Agentic Engineering, AI Agents, MCP, Spec-Driven Development)
- **Format:** Talk, 50 min
- **Audience level:** Medium

## Tracks chosen

| Proposal | Track | Angle |
|---|---|---|
| A — AI & Open Source | Mind the Geek | Reflective, broad appeal, evidence-driven |
| B — Tailor-made harness | Agentic Engineering & Tooling | Technical, flagship track of 2026 |

> Strategy: two different tracks so the proposals do not cannibalize each other and acceptance odds are maximized.

---

## PROPOSAL A — AI & Open Source

### Fields at a glance

- **Presentation Title:** `The Good, the Bad and the Ugly: AI's Real Impact on Open Source`
- **Track:** Mind the Geek
- **Session type:** Talk (50 min)
- **Audience level:** Medium

### Presentation Description (≤1500 char, attendee-facing)

```
AI didn't just arrive in our IDEs, it walked straight into the heart of open source. In the past two years, large language models have started writing code, filing bug reports, hunting vulnerabilities, reviewing pull requests, and even opening merge requests, sometimes by the thousands. The result is a quiet revolution with a very loud fallout.

This talk takes an honest, evidence-driven walk through the Good, the Bad and the Ugly of the AI era in open source.

The Good: AI helps maintainers triage issues, generate docs and tests, onboard newcomers, and ship faster, while security tooling surfaces real CVEs at scale.

The Bad: a flood of AI-generated low-quality contributions, licensing contamination, homogenized code, and skills quietly atrophying.

The Ugly: maintainer burnout under waves of "vibe" pull requests (some projects now publicly ban AI PRs), hallucinated package names that attackers then register, and supply-chain attacks fabricated at machine speed.

Expect concrete cases and numbers, hype separated from harm, and practical principles to keep open source open, human, and trustworthy when the machines are contributing too.
```

### Elevator Pitch (reviewer-only)

```
Open source is the substrate of the entire software industry, and AI is reshaping who contributes to it and how fast. This is a deeply current, broadly relevant topic that touches security, supply chains, maintainer wellbeing and developer culture, yet it is rarely discussed with evidence instead of tribal takes. The speaker brings a practitioner's perspective with concrete cases (good and bad) and an opinionated, balanced framework the audience can act on. It fits the Devoxx 2026 "From Developer to Builder" narrative by asking the uncomfortable question the builder era creates: who maintains what the machines ship? Memorable, story-driven, broad appeal.
```

### Notes (reviewer-only)

```
This talk can alternatively fit the Security, Trust & Compliance track if the program committee sees a better fit there. Happy to adapt depth and emphasis. I will bring updated figures and concrete cases current to the conference date.
```

### Alternate titles

1. `The Good, the Bad and the Ugly: AI's Real Impact on Open Source` *(chosen)*
2. `The Good, the Bad and the Ugly of the AI Era in Open Source`
3. `When the Machines Contribute: The Good, the Bad and the Ugly of AI in OSS`

---

## PROPOSAL B — Tailor-made harness

### Fields at a glance

- **Presentation Title:** `Your Agent Harness Should Be Tailor-Made`
- **Track:** Agentic Engineering & Tooling
- **Session type:** Talk (50 min)
- **Audience level:** Medium

### Presentation Description (≤1500 char, attendee-facing)

```
Most agents today run inside someone else's harness. You install a framework, drop in a system prompt, wire a few tools, and ship. It works for a demo. Then it loops forever on a tricky task, edits the wrong files, invents tools that don't exist, or politely drifts off mission while burning tokens.

The problem isn't the model. It's the off-the-rack harness.

This talk argues that effective agents, coding or otherwise, deserve a bespoke harness: scaffolding tailored to the developer, the project, and the mission. James Bond doesn't wear a suit off the rack; Q tailors it for the mission (hidden compartment, right fit, built to move). Your agent's harness deserves the same care.

We'll dissect what a harness actually is (system prompt, tool boundaries, context and memory, loop control, stop conditions, guardrails, evals, budget) and why the generic defaults fail exactly where autonomy matters most. Through before/after examples, you'll see how encoding project constraints, a precise definition of "done", and tight loop guardrails turns a distracted agent into one that stays on target.

You'll leave with a practical blueprint for designing harnesses that are efficient, effective, and boringly reliable, plus the confidence to build your own instead of inheriting someone else's.
```

### Elevator Pitch (reviewer-only)

```
Devoxx 2026's "From Developer to Builder" theme is all about agents, but most builders inherit a generic harness and then hit the same wall: agents that loop, drift, and burn budget. This talk gives a memorable, actionable mental model (the bespoke suit) for the single highest-leverage decision in agentic engineering: how you scaffold your agent. It is framework-agnostic and model-agnostic, so it stays useful as the LLM-of-the-week changes. Includes concrete before/after examples of harness changes taming runaway loops, and a reusable blueprint the audience can apply Monday morning. Strong fit for Agentic Engineering & Tooling, the conference's flagship track this year.
```

### Notes (reviewer-only)

```
Can also work as a shorter session or accommodate a brief live before/after demo if the slot allows. Framework- and model-agnostic by design; the examples are illustrative rather than a tool pitch, so the content ages well as the ecosystem moves.
```

### Alternate titles

1. `Your Agent Harness Should Be Tailor-Made` *(chosen)*
2. `007 and the Tailored Harness: Why Off-the-Rack Agents Fail`
3. `Off-the-Rack vs Bespoke: Building the Harness Your Agent Deserves`
4. `Tailor Your Harness: Keeping Agents On-Mission and Out of Loops`

---

## Submission checklist (what is still needed)

Not blocking for saving the draft, but decisive for selection:

1. **Two supporting URLs** (effectively expected): one with public slides/material, one with a **video of an existing talk**. If no recent video exists, record a 3–5 min summary: it is the strongest signal the speaker can hold a stage.
2. **Proposal A:** pick 2–3 concrete cases with numbers (a well-known project that banned AI PRs, a maintainer-load figure, a real slopsquatting example). Without them, "balanced" risks reading as generic.
3. **Proposal B:** prepare **one real before/after** (same task with a generic harness that loops/drifts vs a tailor-made harness that stays on target). This is the single thing that sells the talk to the committee.

## TODO

- [ ] Fill supporting URLs for both proposals
- [ ] Collect 2–3 concrete cases for Proposal A
- [ ] Prepare one before/after demo for Proposal B
- [ ] Record a 3–5 min talk video (if no existing one)
