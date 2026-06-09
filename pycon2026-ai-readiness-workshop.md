# Measuring AI-Readiness: A Hands-On Audit of Your Own Codebase

**Event:** PyCon Italia 2026 — Workshop (120 minutes)
**Audience level:** Intermediate
**Language:** English

## Elevator pitch

Your AI coding agent burns tokens, takes wrong turns, and breaks things. Not because the model is weak, but because your repository was written for humans, not for agents. In this 2-hour workshop you won't watch slides about a framework. You'll bring your own codebase and walk out with a measured AI-Readiness score, a ranked list of fixes, and the scripts to repeat the measurement in CI.

## Abstract

AI agents fail inside real repositories for reasons that static lint rules and architecture diagrams don't capture: context layouts that waste tokens, structures that hide intent, validation loops that never close. "AI-Readiness" is a measurable property of a codebase, and like any measurable property you can audit it, improve it, and track it over time.

This workshop is **not** a tour of a pre-packaged scoring framework. It is a working session in which you learn a repeatable four-stage process and apply it, live, to a repository you actually care about.

### The process you will learn

You will work on **your own repository** through four stages:

1. **Scan.** Run a diagnostic on your codebase across a set of weighted dimensions (agent instructions, project navigability, testing and validation, CI/CD, spec-driven workflow, skills and tooling, documentation, agent-specific configuration). Output: a 0-100 baseline score and a per-dimension breakdown that shows exactly where the repo is leaking agent effort.

2. **Report.** Turn the raw scan into a prioritized roadmap. Which dimensions cost the most tokens? Which fixes have the best ROI per hour of engineering work? What is invisible to an agent today that a small change would surface?

3. **Fix.** Apply targeted interventions. Some are auto-generated (missing CLAUDE.md, environment templates, CI scaffolding, assertion messages); others require human judgment (restructuring a spec workflow, rewriting an architecture overview). You will do both, live, on your repo.

4. **Diff.** Re-run the scan and measure the delta. Quantify the improvement, identify what is left, and wire the scan into CI so AI-Readiness becomes a tracked metric, not a one-off audit.

The three-axis model from the original research (efficiency, navigability, verifiability) still anchors the analysis, but you will work with it through instruments rather than slides.

### What you take home

- A **scored AI-Readiness baseline** for your repository.
- A **prioritized intervention plan** with expected impact per fix.
- The **measurement scripts** (open-source) to re-run the audit on demand or in CI.
- A **reusable protocol** you can hand to your team or apply to other repos.

### Prerequisites

- Laptop with Python 3.10+ and Docker.
- A repository you can run locally, ideally one your team actually uses, even if small.
- API credits for one supported LLM provider (Anthropic, OpenAI, GLM, MiniMax, or Kimi).
- Comfort with the command line and reading Python.

### Why a process, not a framework

Pre-packaged scores tell you *that* something is wrong. A process tells you *how to find out what is wrong in code you didn't write*, which is your own. By the end of the workshop you should be able to onboard a new repository to AI-Readiness measurement without me in the room.
