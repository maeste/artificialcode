# LINCE Launch: Social Media Campaign (English)

---

## Part 1: LinkedIn EN Posts

---

### Angle 1: Sandbox YOLO (Security + Fearless Agent Execution)

#### Alt A

I let AI agents run wild on my codebase last night. No permission prompts. No anxiety. I slept like a baby.

Here's why.

Most coding agents interrupt you every 30 seconds: "Can I write this file?" "Can I run this command?" You end up babysitting instead of building.

LINCE flips this. It wraps every agent in kernel-level sandboxing (bubblewrap on Linux, nono on Linux/macOS) with zero performance overhead. The agent can do whatever it wants inside the sandbox, including deleting files, running arbitrary commands, modifying configs. Nothing escapes.

And if something goes wrong? Snapshots. One command to roll back everything.

At Voxxed Day Ticino I said: "The attack surface is you, not your software." LINCE is built on that principle. The real risk isn't your code, it's the developer clicking "approve" on autopilot at 2am.

So we removed the approve button entirely. You don't need it when the sandbox is real.

Open source, MIT license, terminal-native.

Try it: lince.sh
GitHub: github.com/RisorseArtificiali/lince

#OpenSource #DevTools #AIAgents #CodingWorkstation #TerminalTools

> **Media note**: Attach a short GIF or screen recording showing an agent running freely inside a sandboxed session, then a snapshot rollback in action.

---

#### Alt B

"Are you sure you want to allow this action?"

If you use AI coding agents, you've clicked that dialog hundreds of times. Maybe thousands.

And let's be honest: after the first fifty, you stop reading. You just click approve. Which means the permission system isn't protecting you. It's just slowing you down while giving you a false sense of security.

LINCE takes a different approach. Every agent runs inside a kernel-level sandbox (bubblewrap/nono). Zero overhead. The agent has full freedom inside its container, and nothing leaks out. If the agent does something destructive, you roll back with a snapshot.

No permission fatigue. No false sense of control. Real isolation.

This isn't a theoretical improvement. It changes how you work with agents. You stop babysitting and start trusting the process, because the safety net is structural, not behavioral.

Open source, MIT licensed, built by the Risorse Artificiali team.

lince.sh | github.com/RisorseArtificiali/lince

#DevTools #AIAgents #OpenSource #Security #TerminalFirst

> **Media note**: Attach a screenshot of a sandboxed agent session with the LINCE dashboard visible, highlighting the absence of permission prompts.

---

#### Alt C

The most dangerous moment in AI-assisted coding isn't when the agent makes a mistake.

It's when you approve that mistake without reading the prompt.

Permission fatigue is real. After hours of coding with agents, "approve" becomes a reflex. That's when things break. The attack surface isn't your software. It's you.

LINCE eliminates this problem at the architecture level. Kernel-level sandboxing (zero overhead, bubblewrap on Linux, nono on Linux/macOS) means agents run in full YOLO mode. No permission dialogs. No interruptions. Nothing escapes the sandbox.

Made a mess? Snapshot rollback, one command, done.

We built this because we were tired of pretending that clicking "yes" 200 times a day was a security model.

MIT license. Open source. Terminal-native.

lince.sh | github.com/RisorseArtificiali/lince

#CodingSecurity #AIAgents #OpenSource #DevTools #Sandbox

> **Media note**: Attach a diagram or infographic showing the sandbox architecture (agent inside bubble, system outside) with a "no permission prompts" callout.

---

### Angle 2: Context Switch Killer (Multi-Agent Orchestration)

#### Alt A

Running one AI coding agent is powerful. Running five at the same time is chaos.

Unless you have a dashboard for it.

LINCE is a terminal-based workstation that lets you run 8+ agents in parallel. A Rust/WASM dashboard plugin (under 900KB) shows you which agents are working, which ones need input, and lets you switch between them with single keystrokes.

The sweet spot we've found is 3-5 agents working simultaneously. One refactoring a module, one writing tests, one fixing CI, one reviewing docs. You become the conductor, not the musician.

Here's the shift: the bottleneck is no longer generation. Agents generate code fast. The bottleneck is verification. LINCE lets you spend your attention where it matters, reviewing and steering, instead of waiting for one agent to finish before starting another.

Minimal context switching. Maximum throughput. All from your terminal.

Open source, MIT license.

lince.sh | github.com/RisorseArtificiali/lince

#MultiAgent #DevProductivity #AIAgents #OpenSource #TerminalTools

> **Media note**: Attach a screenshot or GIF of the Zellij dashboard showing multiple agent panes running simultaneously, with the status indicators visible.

---

#### Alt B

The biggest lie about AI coding assistants: "Just use one at a time."

I run 3 to 5 agents in parallel. Every day. Here's how.

LINCE gives you a terminal dashboard (a tiny Rust/WASM plugin, ~900KB) built on Zellij. Each agent gets its own pane. The dashboard tells you which agents are busy, which are stuck, and which need your input. One keystroke to switch.

This changes the economics of coding with AI. Instead of a linear workflow (prompt, wait, review, prompt again), you run parallel workflows. Agent A refactors while Agent B writes tests while Agent C updates documentation. You rotate between them, reviewing output, giving direction, moving on.

The bottleneck shifts from "how fast can the agent generate code" to "how fast can I verify and steer." That's a much better problem to have.

Vendor-independent too. Claude Code, Codex, Gemini, Aider, OpenCode, or your own custom agent via a TOML config.

lince.sh | github.com/RisorseArtificiali/lince

#DevTools #AIAgents #Productivity #OpenSource #CodingWorkflow

> **Media note**: Attach a short screen recording showing the workflow of switching between multiple agent panes using keystrokes, with visible status indicators.

---

#### Alt C

What if the real productivity gain from AI agents isn't faster code generation, but parallel code generation?

One agent is useful. Five agents running simultaneously, each on a different task, with a dashboard telling you exactly which one needs your attention? That's a workflow transformation.

LINCE makes this practical. It's a terminal-based multi-agent workstation with a lightweight dashboard (Rust/WASM, ~900KB) that runs on Zellij. You see all your agents at a glance. Switch with a keystroke. No tab switching, no window juggling, no lost context.

We've tested this extensively. The sweet spot is 3-5 agents. Below that, you don't need the orchestration. Above that, verification becomes the bottleneck (which, honestly, it should be, that means you're using agents correctly).

Works with any agent: Claude Code, Codex, Gemini, Aider, OpenCode, or define your own in TOML.

MIT license. Open source. Built for developers who want to multiply, not just assist.

lince.sh | github.com/RisorseArtificiali/lince

#MultiAgent #TerminalTools #AIEngineering #OpenSource #DevProductivity

> **Media note**: Attach an annotated screenshot of the dashboard with callouts explaining the status indicators and keystroke navigation.

---

### Angle 3: Terminal-Only (No IDE, No Browser, No Extra Apps)

#### Alt A

I deleted my IDE. Then my browser. Then every extra app I used for coding.

I now work entirely in the terminal. And I'm more productive than ever.

LINCE is a terminal-native multi-agent workstation. Zellij as your window manager. No VS Code. No Chrome. No Slack integration. No Electron apps eating your RAM. Just your shell, your agents, and your code.

Why does this matter?

Because every app you open is a context switch. Every tab is a decision. Every notification is an interruption. The terminal eliminates all of that. One environment. One set of keybindings. One mental model.

LINCE adds multi-agent orchestration to this setup: a Rust/WASM dashboard plugin (~900KB), sandboxed execution, session persistence, voice input via local Whisper. All without leaving the terminal.

Minimal dependencies. Maximum focus.

Open source, MIT license. Built for developers who want less software, not more.

lince.sh | github.com/RisorseArtificiali/lince

#TerminalFirst #MinimalDev #DevTools #OpenSource #AIAgents

> **Media note**: Attach a full-screen screenshot of a LINCE terminal session showing the complete workflow (agents, code, dashboard) with no other applications visible.

---

#### Alt B

Your coding setup has 47 open tabs, 3 IDE windows, a chat app, and a monitoring dashboard.

Mine has a terminal.

LINCE is a terminal-only multi-agent coding workstation. Everything you need, agent orchestration, sandboxed execution, session persistence, voice input, lives inside your shell. Zellij handles window management. A tiny Rust/WASM plugin (~900KB) provides the dashboard.

No IDE required. No browser tabs. No Electron apps consuming 2GB of RAM to display a text editor.

This isn't minimalism for aesthetics. It's minimalism for performance. Fewer context switches means deeper focus. Fewer tools means fewer things that break. Fewer dependencies means faster setup on any machine.

VoxCode (local Whisper integration) even handles voice input for those of us who find dictation useful but hate browser-based tools. Especially handy on Linux where audio tooling can be... challenging.

MIT license. Open source. Terminal-native by conviction, not by limitation.

lince.sh | github.com/RisorseArtificiali/lince

#TerminalTools #MinimalSetup #DevProductivity #OpenSource #AIAgents

> **Media note**: Attach a side-by-side comparison image: left side shows a cluttered desktop with multiple apps, right side shows a clean LINCE terminal session.

---

#### Alt C

The best developer tool is the one you already have: your terminal.

Every layer you add on top of it (IDE, browser, desktop app, integration platform) adds latency, cognitive load, and failure modes. LINCE strips it all away.

It's a multi-agent coding workstation that lives entirely in your terminal. Zellij for window management. A Rust/WASM dashboard plugin (~900KB) for agent orchestration. Bubblewrap/nono for sandboxing. Local Whisper for voice input. Session persistence built in.

No external dependencies to manage. No heavy IDE to keep updated. No browser tabs to organize. SSH into a remote machine, start LINCE, and you have your full multi-agent workstation.

This is particularly powerful for teams working across different environments. Same tool on your laptop, your workstation, your cloud VM. Same keybindings, same workflow, same mental model everywhere.

Open source. MIT license. Built by the Risorse Artificiali team.

lince.sh | github.com/RisorseArtificiali/lince

#TerminalNative #DevTools #RemoteDev #OpenSource #AIWorkstation

> **Media note**: Attach a GIF showing LINCE running via SSH on a remote machine, demonstrating the portable terminal-native workflow.

---

### Angle 4: Open Source Launch (Personal Story)

#### Alt A

A couple of months ago, I stood on stage at Voxxed Day Ticino and said: "The attack surface is you, not your software."

The audience laughed. Then they thought about it. Then they stopped laughing.

We were all having the same experience: running AI coding agents, clicking "approve" on autopilot, pretending we were reviewing each action when we were really just rubber-stamping. The security model was theatrical, not structural.

In the weeks that followed, we built LINCE.

It's a terminal-based multi-agent coding workstation. Open source, MIT license. Kernel-level sandboxing so agents run freely without permission dialogs. A lightweight dashboard to orchestrate multiple agents in parallel. Session persistence. Voice input. Vendor-independent (Claude Code, Codex, Gemini, Aider, OpenCode, custom agents via TOML).

Built by the Risorse Artificiali team, born from a real frustration with how the current tooling works.

This isn't a product launch. It's a contribution. We built what we needed, and we're sharing it because we think others need it too.

Star the repo, try it out, tell us what's broken. That's how open source works.

lince.sh | github.com/RisorseArtificiali/lince

#OpenSource #AIAgents #DevTools #CodingWorkstation #Community

> **Media note**: Attach a photo from the Voxxed Day Ticino talk (if available) or a screenshot of the LINCE GitHub repo page. Consider a short video introduction from the author.

---

#### Alt B

Every tool I've built started the same way: I got frustrated enough to stop complaining and start coding.

LINCE started at Voxxed Day Ticino a couple of months ago, during a talk about AI agent security. I was explaining how permission-based security in coding agents is fundamentally broken, how developers become the weakest link by clicking "approve" without reading.

Someone in the audience asked: "So what's the alternative?"

Good question. In the weeks that followed, we went and built it.

LINCE is an open-source, terminal-based multi-agent workstation. Kernel-level sandboxing (not permission dialogs). Multi-agent dashboard (not tab switching). Terminal-native (not IDE-dependent). Vendor-independent (not locked to one provider).

The Risorse Artificiali team put this together over a few intense weeks of iteration. We use it daily. It changed how we work with agents, from cautious single-agent sessions to confident multi-agent workflows.

MIT license. Everything is on GitHub. We want contributors, critics, and collaborators.

If you've felt the same frustration with current agent tooling, give it a try.

lince.sh | github.com/RisorseArtificiali/lince

#OpenSource #DevCommunity #AIAgents #BuildInPublic #TerminalTools

> **Media note**: Attach a carousel of images: (1) conference photo or slide, (2) LINCE terminal screenshot, (3) GitHub repo stats/stars.

---

#### Alt C

Today we're open-sourcing LINCE, and I want to tell you why it exists.

The Risorse Artificiali team and I have been working with AI coding agents for over a year. We noticed three things:

1. Permission-based security is broken. You click "approve" on autopilot. The attack surface is you.
2. Running multiple agents is powerful but chaotic. You need orchestration, not just more terminal tabs.
3. Every new tool adds complexity. We wanted to subtract, not add.

LINCE is our answer to all three:

Kernel-level sandboxing (bubblewrap/nono) so agents run in full YOLO mode. No permission prompts, real isolation, snapshot rollback.

A Rust/WASM dashboard (~900KB) on Zellij for running 3-8 agents in parallel with single-keystroke switching.

Terminal-native architecture. No IDE, no browser, no external dependencies.

Plus: vendor-independent agent support, VoxCode voice input via local Whisper, session persistence, MIT license.

We're not building a company around this. We're building a tool for developers, by developers.

lince.sh | github.com/RisorseArtificiali/lince

#OpenSource #LINCE #AIAgents #DevTools #MITLicense

> **Media note**: Attach a 60-90 second video walkthrough of LINCE features, or a polished screenshot with feature callouts annotated.

---

## Part 2: X.com (Twitter) EN Posts/Threads

---

### Angle 1: Sandbox YOLO

#### Thread Alt A

**Tweet 1 (standalone hook):**
I run AI coding agents with zero permission prompts. No approvals, no interruptions, no anxiety. They can delete files, run commands, do whatever they want. And my system is perfectly safe.

**Tweet 2:**
The secret: kernel-level sandboxing.

LINCE wraps every agent in bubblewrap (Linux) or nono (Linux/macOS). Zero overhead. The agent has full freedom inside the container. Nothing escapes.

Permission prompts aren't security. They're theater.

**Tweet 3:**
Think about it: after clicking "approve" 200 times in a day, are you really reading the prompts? Or are you just rubber-stamping?

The attack surface isn't your software. It's you at 2am clicking "yes" on autopilot.

**Tweet 4:**
LINCE fixes this architecturally. No human in the approval loop means no human error in the approval loop.

Something went wrong? Snapshot rollback. One command. Done.

**Tweet 5:**
Open source, MIT license, terminal-native.

Built by @RisorseArtificiali

lince.sh
github.com/RisorseArtificiali/lince

> **Media note**: Tweet 1: no media (maximize reach). Tweet 2: diagram of sandbox architecture. Tweet 4: GIF of snapshot rollback. Tweet 5: screenshot of GitHub repo.

---

#### Thread Alt B

**Tweet 1 (standalone hook):**
"Are you sure you want to allow this action?"

If you use AI coding agents, you've seen this dialog 10,000 times. And you stopped reading it after the first 50. That's not security. That's a liability.

**Tweet 2:**
We built LINCE to eliminate permission fatigue entirely.

Every agent runs in a kernel-level sandbox (bubblewrap/nono). Zero overhead. Full isolation. The agent has complete freedom inside the container. Your system stays untouched.

**Tweet 3:**
No permission prompts means:
- No interruptions to your flow
- No false sense of security
- No 2am "approve everything" mistakes
- No babysitting agents

Just real, structural isolation.

**Tweet 4:**
And if an agent makes a mess inside the sandbox? Snapshot rollback. One command. Clean slate.

The safety net is architectural, not behavioral. That's the whole point.

**Tweet 5:**
LINCE: open source, MIT license, terminal-native multi-agent workstation.

lince.sh
github.com/RisorseArtificiali/lince

> **Media note**: Tweet 1: no media. Tweet 2: infographic comparing permission-based vs sandbox-based security. Tweet 3: screenshot showing clean agent execution without prompts. Tweet 5: repo screenshot.

---

#### Thread Alt C

**Tweet 1 (standalone hook):**
At Voxxed Day Ticino I told a room full of developers: "The attack surface is you, not your software."

Nobody disagreed. Because we all know we click "approve" without reading. So we built a tool that doesn't ask.

**Tweet 2:**
LINCE sandboxes every AI coding agent at the kernel level. Bubblewrap on Linux, nono on Linux/macOS. Zero overhead.

Agents run in full YOLO mode. No permissions, no dialogs, no interruptions. Nothing escapes the sandbox.

**Tweet 3:**
Why is this better than permission prompts?

Because permission prompts assume you'll read them. You won't. Not after hour 3. Not at 11pm. Not on the 500th prompt of the day.

Sandboxing doesn't assume anything about your behavior. It just works.

**Tweet 4:**
Snapshot rollback means mistakes are cheap. Roll back with one command. Try again. No drama.

This changes how you relate to agents. You stop being cautious and start being productive.

**Tweet 5:**
Open source. MIT license. Terminal-native.

lince.sh
github.com/RisorseArtificiali/lince

Star it, break it, tell us what's wrong. That's how we improve.

> **Media note**: Tweet 1: photo from the conference (if available). Tweet 2: architecture diagram. Tweet 4: GIF of rollback in action. Tweet 5: repo page screenshot.

---

### Angle 2: Context Switch Killer

#### Thread Alt A

**Tweet 1 (standalone hook):**
I run 5 AI coding agents simultaneously. One refactors, one writes tests, one fixes CI, one updates docs, one reviews security. I switch between them with single keystrokes.

**Tweet 2:**
LINCE is a terminal-based multi-agent workstation built on Zellij. A tiny Rust/WASM dashboard plugin (~900KB) shows you all your agents at a glance.

Which ones are working. Which ones are stuck. Which ones need your input.

**Tweet 3:**
The insight that changed everything for us: the bottleneck isn't generation anymore. Agents generate code fast.

The bottleneck is verification. LINCE lets you spend your attention where it actually matters.

**Tweet 4:**
Sweet spot: 3-5 agents in parallel.

Below that, you don't need orchestration.
Above that, verification becomes overwhelming.

3-5 is where you get the multiplier effect without losing control.

**Tweet 5:**
Works with any agent: Claude Code, Codex, Gemini, Aider, OpenCode, or define your own in TOML.

Vendor lock-in is not a feature.

lince.sh
github.com/RisorseArtificiali/lince

> **Media note**: Tweet 1: no media. Tweet 2: GIF of the dashboard with multiple agents running. Tweet 4: screenshot showing 4 agents in different states. Tweet 5: TOML config snippet screenshot.

---

#### Thread Alt B

**Tweet 1 (standalone hook):**
The way most developers use AI agents: prompt one agent, wait, review, prompt again. Linear. Slow. One at a time.

There's a better way. You just need a dashboard.

**Tweet 2:**
LINCE runs multiple AI agents in parallel inside your terminal. A Rust/WASM dashboard (~900KB) on Zellij tells you what each agent is doing.

Switch between agents with a keystroke. No tab juggling. No lost context. No "wait, which terminal was that?"

**Tweet 3:**
We tested different configurations extensively:

- 1 agent: useful but linear
- 2 agents: marginal improvement
- 3-5 agents: the sweet spot (multiplier effect)
- 8+ agents: possible but verification becomes the limit

The constraint shifts from generation to verification. That's progress.

**Tweet 4:**
Vendor-independent: Claude Code, Codex, Gemini, OpenCode, Aider, or any custom agent defined in TOML.

Mix and match. Use the best agent for each task. No lock-in.

**Tweet 5:**
Open source, MIT license. Built by @RisorseArtificiali.

lince.sh
github.com/RisorseArtificiali/lince

> **Media note**: Tweet 1: no media. Tweet 2: screen recording of agent switching. Tweet 3: simple chart showing productivity vs number of agents. Tweet 5: repo page screenshot.

---

#### Thread Alt C

**Tweet 1 (standalone hook):**
Hot take: running one AI coding agent at a time is like having a team of 5 engineers and only letting one work while the others watch.

Multi-agent orchestration isn't a luxury. It's the obvious next step.

**Tweet 2:**
LINCE makes multi-agent practical. Terminal-native dashboard on Zellij (Rust/WASM, ~900KB). Run 3-8 agents in parallel. See their status at a glance. Switch with a keystroke.

You become the conductor. The agents are the orchestra.

**Tweet 3:**
Key insight from months of daily use: the bottleneck shifts.

Single agent: you wait for generation.
Multi-agent: you focus on verification.

Verification is where your expertise matters most. Generation is what agents are good at. Let each do what they're best at.

**Tweet 4:**
Sandboxed execution means you don't worry about agents stepping on each other. Each one is isolated. Snapshot rollback if anything goes sideways.

Parallel execution without parallel anxiety.

**Tweet 5:**
LINCE: open source, MIT license, vendor-independent.

Works with Claude Code, Codex, Gemini, Aider, OpenCode, custom agents via TOML.

lince.sh
github.com/RisorseArtificiali/lince

> **Media note**: Tweet 1: no media. Tweet 2: dashboard GIF with multiple agents. Tweet 3: simple before/after workflow diagram. Tweet 5: repo screenshot with star count.

---

### Angle 3: Terminal-Only

#### Thread Alt A

**Tweet 1 (standalone hook):**
My entire coding setup: one terminal window. No IDE. No browser. No Electron apps. No 16GB of RAM consumed by a text editor pretending to be an operating system.

**Tweet 2:**
LINCE is a terminal-native multi-agent coding workstation. Zellij as window manager. Rust/WASM dashboard plugin (~900KB). Kernel-level sandboxing. Voice input via local Whisper. Session persistence.

All inside your terminal.

**Tweet 3:**
Why terminal-only matters:

- Same setup on laptop, workstation, cloud VM
- SSH in, start LINCE, full workstation
- No dependency hell from GUI toolkits
- One set of keybindings everywhere
- Fewer context switches, deeper focus

**Tweet 4:**
VoxCode (voice input via local Whisper) is a game-changer for Linux users. If you've ever tried dictation tools on Linux, you know the pain. Local processing, no cloud dependency, works inside the terminal.

**Tweet 5:**
Open source. MIT license. Minimal dependencies.

lince.sh
github.com/RisorseArtificiali/lince

> **Media note**: Tweet 1: no media. Tweet 2: full-screen terminal screenshot. Tweet 3: screenshot of LINCE via SSH on remote machine. Tweet 4: GIF of VoxCode voice input. Tweet 5: repo screenshot.

---

#### Thread Alt B

**Tweet 1 (standalone hook):**
Controversial opinion: your IDE is slowing you down. Not because it's slow. Because it's one more thing to manage, configure, update, and context-switch into.

The terminal is all you need.

**Tweet 2:**
LINCE: terminal-based multi-agent workstation.

- Zellij for window management
- Rust/WASM dashboard (~900KB) for agent orchestration
- Bubblewrap/nono for sandboxing
- Local Whisper for voice input
- Session persistence built in

No external dependencies.

**Tweet 3:**
The power of terminal-native: I SSH into a cloud VM, start LINCE, and I have my full multi-agent workstation. Same keybindings. Same workflow. Same mental model.

Try doing that with VS Code + 47 extensions.

**Tweet 4:**
"But I need my IDE for..." 

Code completion? Agents do that.
File navigation? Terminal tools.
Debugging? Terminal debuggers.
Git? Git was always terminal-native.

The IDE solved problems from 2015. The terminal (with agents) solves problems from 2026.

**Tweet 5:**
LINCE: open source, MIT license. Built for developers who want fewer tools, not more.

lince.sh
github.com/RisorseArtificiali/lince

> **Media note**: Tweet 1: no media. Tweet 2: clean LINCE terminal screenshot with feature labels. Tweet 3: split-screen showing local vs SSH session. Tweet 5: repo screenshot.

---

#### Thread Alt C

**Tweet 1 (standalone hook):**
What if the next evolution of developer tools isn't adding more features to the IDE, but removing the IDE entirely?

That's the bet we're making with LINCE.

**Tweet 2:**
LINCE is a terminal-only multi-agent coding workstation. Zellij handles windows. A Rust/WASM plugin (~900KB) handles the dashboard. Bubblewrap/nono handle sandboxing. Whisper handles voice.

Total footprint: minimal. Total capability: everything you need.

**Tweet 3:**
The terminal advantage most people overlook: composability.

Every terminal tool works with every other terminal tool. Pipes. Scripts. Automation. Your workflow is programmable by default.

IDEs give you plugins. The terminal gives you Unix.

**Tweet 4:**
LINCE adds to this composability:
- Any AI agent that runs in a terminal works with LINCE
- Configure custom agents via TOML
- Session persistence means your multi-agent setup survives reboots
- Vendor-independent by design

**Tweet 5:**
Open source. MIT license. Terminal-native by conviction.

lince.sh
github.com/RisorseArtificiali/lince

> **Media note**: Tweet 1: no media. Tweet 2: annotated terminal screenshot. Tweet 3: diagram showing Unix composability with LINCE in the pipeline. Tweet 5: repo screenshot.

---

### Angle 4: Open Source Launch

#### Thread Alt A

**Tweet 1 (standalone hook):**
Today we're open-sourcing LINCE, a terminal-based multi-agent coding workstation. Let me tell you why we built it and why we're giving it away.

**Tweet 2:**
It started at Voxxed Day Ticino. I was talking about AI agent security and said: "The attack surface is you, not your software."

Everyone nodded. We all know we click "approve" without reading after the 50th prompt. The security model is broken.

**Tweet 3:**
So the @RisorseArtificiali team built what we needed:

- Kernel-level sandboxing (no more permission theater)
- Multi-agent dashboard (3-8 agents in parallel)
- Terminal-native (no IDE, no browser)
- Vendor-independent (any agent, via TOML)
- Voice input (local Whisper)
- MIT license (no strings)

**Tweet 4:**
We use LINCE daily. It changed how we work with agents.

From cautious single-agent sessions with constant permission clicking, to confident multi-agent workflows where we focus on verification instead of babysitting.

**Tweet 5:**
This is a real open source launch. We want contributors, bug reports, feature requests, criticism.

Star it. Clone it. Break it. Tell us what's wrong.

lince.sh
github.com/RisorseArtificiali/lince

> **Media note**: Tweet 1: no media. Tweet 3: feature overview image with icons. Tweet 4: screenshot of daily usage. Tweet 5: GitHub repo page with contributing guidelines visible.

---

#### Thread Alt B

**Tweet 1 (standalone hook):**
We spent the last few weeks building a tool that makes AI coding agents actually usable. Today we're releasing it for free. Here's the story.

**Tweet 2:**
Problem 1: Permission fatigue. You click "approve" 200x/day. You stop reading. The security is fake.

Solution: kernel-level sandboxing. Zero overhead. Agents run free inside the container. Nothing escapes. Snapshot rollback when needed.

**Tweet 3:**
Problem 2: One agent at a time is a bottleneck. But running multiple agents is chaotic.

Solution: Rust/WASM dashboard on Zellij (~900KB). See all agents at a glance. Switch with a keystroke. Sweet spot: 3-5 agents in parallel.

**Tweet 4:**
Problem 3: Every new tool adds complexity. IDE plugins, browser extensions, desktop apps.

Solution: terminal-only. Zellij for windows. Everything in one environment. SSH anywhere, start LINCE, full workstation.

**Tweet 5:**
LINCE. Open source. MIT license. Vendor-independent.

Built by @RisorseArtificiali because we needed it and figured others would too.

lince.sh
github.com/RisorseArtificiali/lince

> **Media note**: Tweet 1: no media. Tweets 2-4: one screenshot/diagram per tweet illustrating each problem/solution. Tweet 5: repo page screenshot.

---

#### Thread Alt C

**Tweet 1 (standalone hook):**
"The attack surface is you, not your software."

I said this at a conference a couple of months ago. Then we spent the following weeks building a tool based on that idea. Today it's open source.

**Tweet 2:**
LINCE is a terminal-based multi-agent coding workstation. The core idea: stop trusting humans to click the right button 200 times a day. Start trusting architecture.

Kernel-level sandboxing. Zero overhead. Agents run freely. You sleep well.

**Tweet 3:**
But LINCE isn't just about security. It's about multiplying what agents can do for you.

Run 3-5 agents in parallel. Dashboard shows their status. Switch with a keystroke. The bottleneck shifts from generation to verification, which is exactly where your expertise belongs.

**Tweet 4:**
Terminal-native. No IDE required. No browser required. Works over SSH. ~900KB dashboard plugin. Session persistence. Voice input via local Whisper. Vendor-independent (Claude Code, Codex, Gemini, Aider, OpenCode, custom agents).

Minimal software. Maximum capability.

**Tweet 5:**
MIT license. Open source. Built by @RisorseArtificiali.

We want your feedback, your PRs, your issues, your ideas.

lince.sh
github.com/RisorseArtificiali/lince

> **Media note**: Tweet 1: no media (conference quote as hook). Tweet 2: sandbox architecture diagram. Tweet 3: dashboard GIF. Tweet 4: feature list as clean graphic. Tweet 5: repo screenshot.

---

## Part 3: Publication Plans

---

### Plan 1: 7-Day Blitz (Security-First Narrative)

Leads with the strongest differentiator (sandbox/YOLO), builds through multi-agent orchestration, closes with community launch.

| Day | Platform | Post (Angle/Alt) | Rationale |
|-----|----------|-------------------|-----------|
| Day 1 (Mon) | X.com | Angle 1 / Alt C (Sandbox YOLO, conference quote) | Start with a provocative hook on X where virality is key. The conference quote works as a standalone first tweet. |
| Day 1 (Mon) | LinkedIn | Angle 1 / Alt A (Sandbox YOLO, "slept like a baby") | Strong opening on LinkedIn same day. Different alt so audiences on both platforms get fresh content. |
| Day 2 (Tue) | X.com | Angle 2 / Alt A (Context switch killer, "5 agents") | Follow security with productivity angle while momentum is building. |
| Day 3 (Wed) | LinkedIn | Angle 2 / Alt B (Context switch killer, "better way") | Mid-week LinkedIn post when professional engagement peaks. |
| Day 4 (Thu) | X.com | Angle 3 / Alt A (Terminal-only, "one terminal window") | Terminal-only angle appeals to X's technical audience. |
| Day 5 (Fri) | LinkedIn | Angle 3 / Alt B (Terminal-only, "IDE slowing you down") | Friday thought-provoker for weekend reading. |
| Day 7 (Sun) | X.com | Angle 4 / Alt A (Open source launch story) | Sunday evening thread for Monday morning visibility. |

---

### Plan 2: 7-Day Blitz (Story-First Narrative)

Leads with the personal/conference story, unfolds the "why" before the "what."

| Day | Platform | Post (Angle/Alt) | Rationale |
|-----|----------|-------------------|-----------|
| Day 1 (Mon) | LinkedIn | Angle 4 / Alt A (Open source launch, personal story) | LinkedIn loves founder stories. Set the narrative context first. |
| Day 1 (Mon) | X.com | Angle 4 / Alt C (Open source launch, conference quote) | Mirror the story on X with more punch. |
| Day 2 (Tue) | X.com | Angle 1 / Alt B (Sandbox YOLO, permission fatigue) | Now that people know the story, explain the core innovation. |
| Day 3 (Wed) | LinkedIn | Angle 1 / Alt C (Sandbox YOLO, "most dangerous moment") | Deepen the security narrative on LinkedIn. |
| Day 4 (Thu) | X.com | Angle 2 / Alt C (Context switch killer, "hot take") | Provocative multi-agent take for X engagement. |
| Day 5 (Fri) | LinkedIn | Angle 2 / Alt A (Context switch killer, "conductor") | Professional multi-agent pitch for LinkedIn. |
| Day 7 (Sun) | X.com | Angle 3 / Alt B (Terminal-only, "IDE slowing you down") | Weekend controversial take to spark debate. |

---

### Plan 3: 7-Day Blitz (Alternating Platforms)

Strict daily alternation between platforms, covering all angles evenly.

| Day | Platform | Post (Angle/Alt) | Rationale |
|-----|----------|-------------------|-----------|
| Day 1 (Mon) | LinkedIn | Angle 4 / Alt C (Open source launch, feature overview) | Launch announcement on the professional network. |
| Day 2 (Tue) | X.com | Angle 1 / Alt A (Sandbox YOLO, "run wild") | Technical depth for X's developer audience. |
| Day 3 (Wed) | LinkedIn | Angle 1 / Alt B (Sandbox YOLO, permission fatigue) | Security angle resonates with LinkedIn's risk-aware audience. |
| Day 4 (Thu) | X.com | Angle 2 / Alt A (Context switch killer, "5 agents") | Productivity hook for maximum X engagement. |
| Day 5 (Fri) | LinkedIn | Angle 2 / Alt C (Context switch killer, "obvious next step") | Forward-looking perspective for Friday reflection. |
| Day 6 (Sat) | X.com | Angle 3 / Alt C (Terminal-only, "removing the IDE") | Weekend debate fuel for developers. |
| Day 7 (Sun) | LinkedIn | Angle 3 / Alt A (Terminal-only, "deleted my IDE") | Bold personal story for Sunday evening engagement. |

---

### Plan 4: 14-Day Sustained Campaign (Narrative Arc)

Two-week build from story to features to community, with rest days for organic engagement.

| Day | Platform | Post (Angle/Alt) | Rationale |
|-----|----------|-------------------|-----------|
| Day 1 (Mon) | LinkedIn | Angle 4 / Alt A (Open source launch, personal story) | Set the narrative. People need to know WHY before WHAT. |
| Day 1 (Mon) | X.com | Angle 4 / Alt C (Conference quote launch) | Dual-platform launch day for maximum initial reach. |
| Day 3 (Wed) | LinkedIn | Angle 1 / Alt A (Sandbox YOLO, "slept like a baby") | Core differentiator on LinkedIn, after story has set context. |
| Day 4 (Thu) | X.com | Angle 1 / Alt B (Sandbox YOLO, permission fatigue) | Security deep-dive for X's technical audience. |
| Day 6 (Sat) | X.com | Angle 3 / Alt A (Terminal-only, "one terminal window") | Weekend content for developer browsing. |
| Day 7 (Sun) | LinkedIn | Angle 2 / Alt A (Context switch killer, "conductor") | Sunday read about productivity for Monday morning. |
| Day 8 (Mon) | X.com | Angle 2 / Alt C (Context switch killer, "hot take") | Week 2 opens with provocative multi-agent angle. |
| Day 9 (Tue) | LinkedIn | Angle 3 / Alt B (Terminal-only, "IDE slowing you down") | Thought leadership piece mid-week. |
| Day 11 (Thu) | X.com | Angle 1 / Alt C (Sandbox, conference quote) | Resurface security angle for people who missed week 1. |
| Day 12 (Fri) | LinkedIn | Angle 4 / Alt B (Open source, "got frustrated enough") | Circle back to personal story with new angle. |
| Day 13 (Sat) | X.com | Angle 3 / Alt C (Terminal-only, "removing the IDE") | Weekend debate content. |
| Day 14 (Sun) | LinkedIn | Angle 2 / Alt C (Context switch killer, "obvious next step") | Close with forward-looking vision for the new week. |

---

### Plan 5: 14-Day Sustained Campaign (Feature Spotlight)

Each feature gets dedicated spotlight days across both platforms.

| Day | Platform | Post (Angle/Alt) | Rationale |
|-----|----------|-------------------|-----------|
| Day 1 (Mon) | LinkedIn | Angle 4 / Alt C (Launch announcement, feature overview) | Comprehensive launch post covering all features. |
| Day 1 (Mon) | X.com | Angle 4 / Alt B (Launch story, "weeks of building") | Complementary launch thread with story angle. |
| Day 2 (Tue) | X.com | Angle 1 / Alt A (Sandbox deep-dive) | Sandbox spotlight day 1: technical details on X. |
| Day 3 (Wed) | LinkedIn | Angle 1 / Alt C (Sandbox, "most dangerous moment") | Sandbox spotlight day 2: business case on LinkedIn. |
| Day 5 (Fri) | X.com | Angle 2 / Alt B (Multi-agent, "better way") | Multi-agent spotlight day 1: workflow change. |
| Day 6 (Sat) | LinkedIn | Angle 2 / Alt A (Multi-agent, "conductor metaphor") | Multi-agent spotlight day 2: leadership angle. |
| Day 8 (Mon) | X.com | Angle 3 / Alt B (Terminal-only, "IDE slowing you down") | Terminal spotlight day 1: provocative take. |
| Day 9 (Tue) | LinkedIn | Angle 3 / Alt C (Terminal-only, "composability") | Terminal spotlight day 2: technical depth. |
| Day 10 (Wed) | X.com | Angle 1 / Alt C (Sandbox, revisited with conference quote) | Resurface top differentiator mid-campaign. |
| Day 11 (Thu) | LinkedIn | Angle 2 / Alt B (Multi-agent, "dashboard" focus) | Revisit multi-agent with fresh angle. |
| Day 12 (Fri) | X.com | Angle 2 / Alt C (Multi-agent, "hot take") | End of week provocation for engagement. |
| Day 13 (Sat) | X.com | Angle 3 / Alt A (Terminal-only, "one terminal window") | Weekend minimal setup appeal. |
| Day 14 (Sun) | LinkedIn | Angle 4 / Alt A (Open source, personal story, full circle) | Close the campaign by returning to the origin story. |

---

### Plan 6: 14-Day Sustained Campaign (Engagement-Optimized)

Optimized around platform-specific peak engagement times and content types.

| Day | Platform | Post (Angle/Alt) | Rationale |
|-----|----------|-------------------|-----------|
| Day 1 (Mon) | LinkedIn | Angle 4 / Alt A (Personal story launch) | Monday 8-10am: highest LinkedIn engagement window. Founder stories perform well at week start. |
| Day 2 (Tue) | X.com | Angle 1 / Alt C (Conference quote, sandbox) | Tuesday morning: X developer audience is active. Provocative security hook maximizes retweets. |
| Day 3 (Wed) | LinkedIn | Angle 1 / Alt B (Permission fatigue, sandbox) | Wednesday 9am: second-best LinkedIn day. Security angle resonates with senior devs/managers. |
| Day 4 (Thu) | X.com | Angle 2 / Alt A (5 agents simultaneously) | Thursday: numbers-driven posts perform well on X. Concrete "5 agents" claim drives curiosity. |
| Day 5 (Fri) | LinkedIn | Angle 3 / Alt B (IDE controversial take) | Friday afternoon: thought-provoking content for weekend consideration. High save/share rate. |
| Day 7 (Sun) | X.com | Angle 4 / Alt A (Open source launch story) | Sunday 6pm: developers browse X before the week. Story threads get high engagement. |
| Day 8 (Mon) | LinkedIn | Angle 2 / Alt A (Multi-agent conductor) | Monday: fresh week, fresh angle. Productivity content peaks on Monday/Tuesday. |
| Day 9 (Tue) | X.com | Angle 3 / Alt C (Removing the IDE) | Tuesday: controversial takes drive engagement early in the week. |
| Day 10 (Wed) | LinkedIn | Angle 4 / Alt B (Got frustrated enough) | Wednesday: second personal story angle for people who missed Day 1. |
| Day 11 (Thu) | X.com | Angle 2 / Alt C (Hot take multi-agent) | Thursday: opinionated content performs well mid-week on X. |
| Day 12 (Fri) | LinkedIn | Angle 2 / Alt C (Obvious next step) | Friday: forward-looking content for weekend reflection. |
| Day 13 (Sat) | X.com | Angle 3 / Alt A (One terminal window) | Saturday: minimalist/lifestyle content resonates with weekend browsing. |
| Day 14 (Sun) | LinkedIn | Angle 1 / Alt A (Slept like a baby, sandbox) | Sunday evening: strong closer that circles back to core differentiator before new week. |

---

*Campaign created for LINCE launch by Risorse Artificiali. All posts ready for review and scheduling.*
