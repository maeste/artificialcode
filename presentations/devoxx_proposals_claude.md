# Devoxx Belgium — CfP Proposals

Conference: [Devoxx Belgium](https://devoxx.be/)
Session type: Conference talk (50 min)
Audience level: Medium

> **TODO:** replace the `[BIO: ...]` placeholders in each "Message to the program committee" with your real bio/credentials before submitting.

---

## Proposal A

**Title:** The Good, the Bad and the Ugly of AI in Open Source
**Track:** Development Practices
**Session type:** Conference talk (50 min)
**Audience level:** Medium

### Abstract

Open source has always run on an implicit contract: contributing takes effort, and that effort signals intent. AI just tore up that contract. Today, generating a plausible pull request, a bug report, or even a CVE-grade vulnerability claim costs almost nothing. Reviewing it, triaging it, and deciding whether to trust it costs exactly what it always did, or more. That is the asymmetry, and it is quietly reshaping the open source we all depend on.

This talk looks at the AI era through the eyes of the people who keep open source running: the maintainers. The Good: AI lowers the barrier to contribution, accelerates fixes, and turns fuzzing and triage into superpowers. The Bad: a flood of low-quality, confidently-wrong contributions that drain reviewer attention. The Ugly: fabricated security reports, automated slop, and trust attacks that exploit the very openness that makes the ecosystem work. We walk through real, public cases and what they teach us.

Then we get practical. If the bottleneck has moved from writing code to trusting code, how do we rebalance? We look at concrete defenses: contribution policies for the AI era, triage strategies, where to point AI so it actually helps, and how to protect maintainer attention as the scarcest resource in open source.

### Key takeaways

- Why the "cost to generate vs cost to review" asymmetry is the real story behind AI in open source
- A tour of real public incidents (AI slop PRs, fabricated vulnerability reports, trust attacks) and what actually went wrong
- Where AI genuinely helps maintainers: fuzzing, triage, first-pass review, documentation
- Practical policies and workflows to protect reviewer attention and keep projects trustworthy
- A mental model for evaluating AI-assisted contributions without becoming the bottleneck yourself

### Message to the program committee

The developer conversation is stuck on "AI writes code faster." Almost nobody is talking about the downstream cost on the people who have to review and trust that code. This talk reframes the debate around maintenance economics, which is where the pain actually lands: fabricated vulnerability reports, AI slop contributions, and trust attacks are already hitting high-profile projects. [BIO: I am an active open source maintainer working at the intersection of AI agents and OSS (smolagents / agent tooling), and I have handled AI-generated issues and contributions first-hand.] The talk is balanced and evidence-based, not hype and not doom. No live coding: narrative plus real public cases plus a practical closing framework. Audience level Medium, no security specialism required, but attendees leave with something to apply on Monday.

### Tags

`open-source` · `ai` · `software-supply-chain` · `developer-experience` · `maintainership`

---

## Proposal B

**Title:** Tailor-Made Agents: Building the Harness Your Project Actually Needs
**Track:** Agentic Engineering & Tooling
**Session type:** Conference talk (50 min)
**Audience level:** Medium

### Abstract

Everyone is building agents. Almost nobody is building the harness. The model gets all the attention, but the model is just the body. The harness (everything around it: the context you feed, the tools you expose, the control loop, the guardrails, the evals) is the suit. And an off-the-rack suit on James Bond looks exactly as wrong as an off-the-rack harness on your project: it technically "fits", but it bunches in the loops, wanders off on tangents, and never quite does the job.

This talk makes the case that a good harness is tailor-made, not to the model, but to the developer and the project it serves. We define what a harness actually is, in plain terms, for coding agents and generic agents alike, then show why one-size-fits-all harnesses waste tokens, drift off task, and spiral in loops. Using bespoke tailoring as the through-line, we break down the dimensions you can actually cut to measure: what context to include and exclude, which tools to expose and which to hide, how to shape the control loop, where to place constraints so the agent stays on task, and how to tell when your harness is too loose or too tight.

You leave with a practical way to design your own harness, so your agents stop performing and start delivering.

### Key takeaways

- A clear, jargon-free definition of an agent "harness", and why it (not the model) decides whether agents ship
- Why generic harnesses fail: token waste, task drift, and loop spirals, with concrete failure patterns
- The dimensions you can tailor (context, tools, control loop, guardrails, evals) mapped to real decisions
- The signals that tell you your harness is too loose or too tight, and how to adjust
- A transferable method to design a bespoke harness for your own project or developer workflow, coding and beyond

### Message to the program committee

The industry has crossed from "can an agent do this?" to "why does my agent keep going off the rails?" The answer is almost always the harness, not the model, yet the harness is treated as throwaway glue code and rarely gets a design vocabulary. This talk gives it one, and is deliberately model-agnostic and framework-agnostic: the principles apply to coding agents and generic ones. [BIO: I build agent harnesses in practice (Hermes Agent, Openclaw, smolagents), and draw on them as concrete examples without turning the talk into a product pitch.] The James Bond bespoke-suit metaphor keeps an abstract topic vivid and memorable for a Medium audience. Concept-driven, light on live code, heavy on transferable method. Fits 50 min with Q&A.

### Tags

`ai-agents` · `agentic-engineering` · `tooling` · `llm` · `developer-experience`
