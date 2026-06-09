---
marp: true
theme: default
paginate: true
backgroundColor: white
class: lead
style: |
  section {
    font-size: 0.8
    5rem;
  }
  pre {
    font-size: 0.7rem;
  }
  h1 {
    font-size: 1.8rem;
  }
  h2 {
    font-size: 1.2rem;
  }
  h3 {
    font-size: 1rem;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.6rem;
  }
  .columns-3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.6rem;
  }
  section.lead h1 {
    font-size: 2rem;
    color: #2563eb;
  }
  section.lead h2 {
    font-size: 1.4rem;
    color: #4b5563;
  }
  .text-center {
    text-align: center;
  }
  .bg-light {
    background-color: #f3f4f6;
    padding: 0.6rem;
    border-radius: 0.5rem;
  }
  .small {
    font-size: 0.65rem;
  }
  .highlight {
    background-color: #dbeafe;
    padding: 0.4rem;
    border-radius: 0.25rem;
    font-size: 0.8rem;
  }
  .warning {
    background-color: #fef3c7;
    padding: 0.4rem;
    border-radius: 0.25rem;
    font-size: 0.8rem;
  }
  .danger {
    background-color: #fee2e2;
    padding: 0.4rem;
    border-radius: 0.25rem;
    font-size: 0.8rem;
  }
  .success {
    background-color: #d1fae5;
    padding: 0.4rem;
    border-radius: 0.25rem;
    font-size: 0.8rem;
  }
  .grid-content {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.6rem;
    margin-top: 0.6rem;
  }
  ul, ol {
    padding-left: 1.2rem;
    margin: 0.4rem 0;
  }
  p {
    margin: 0.4rem 0;
  }
  .big-emoji {
    font-size: 3rem;
    text-align: center;
    margin: 0.5rem 0;
  }
  .quote {
    border-left: 4px solid #2563eb;
    padding-left: 1rem;
    font-style: italic;
    color: #4b5563;
  }
  .evolution-arrow {
    font-size: 2rem;
    text-align: center;
    color: #2563eb;
  }
---

<!-- _class: lead -->

<div class="columns">
<div>

## Stefano Maestri

**maeste.it**

**Podcast:** risorseartificiali.com

**Newsletter:** codiceartificiale.substack.com
artificialcode.substack.com

**Backlog.md** → github.com/MrLesk/Backlog.md
**LINCE** → github.com/RisorseArtificiali/lince

</div>
<div class="text-center">

![w:280](maeste-qr.png)

**maeste.it**

</div>
</div>

---

<!-- _class: lead -->
# From Vibe to Agentic
## The Coding You Didn't Know You Wanted

<div class="highlight text-center">
The silent revolution in software development
</div>

<!--
**IT:** Benvenuti! Oggi parliamo di una transizione che sta avvenendo sotto i nostri occhi: dal "vibe coding" all'agentic engineering. Non e' solo un cambio di strumenti, e' un cambio di mentalita'. E vi faro' vedere due tool concreti che rendono questa transizione pratica e reale: Backlog.md per le specifiche e LINCE per l'orchestrazione multi-agente.

**EN:** Welcome! Today we'll talk about a transition happening right before our eyes: from "vibe coding" to agentic engineering. It's not just a tool change, it's a mindset shift. And I'll show you two concrete tools that make this transition practical and real: Backlog.md for specs and LINCE for multi-agent orchestration.
-->

---

# What is Vibe Coding?

<div class="quote">
"You just see stuff, say 'run', and it works. You can feel the code." - Andrej Karpathy
</div>

<div class="columns" style="margin-top: 1rem;">
<div class="bg-light">

### The Approach
- Write a prompt, get code back
- Accept suggestions on instinct
- Iterate by describing what's wrong
- "It compiles? Ship it."
- Trust the AI output without deep review

</div>
<div class="bg-light">

### Where It Works
- Prototyping, MVPs, hackathons
- Learning new languages/frameworks
- One-off scripts and automation
- **10x faster** for throwaway code
- Perfect when **correctness is not critical**

</div>
</div>

<!--
**IT:** Il termine "vibe coding" e' stato coniato da Andrej Karpathy. L'idea e' semplice: descrivi quello che vuoi, l'AI genera il codice, ti sembra giusto (il "vibe"), e lo accetti. Ha un valore enorme per prototyping e learning. Il problema non e' il vibe coding in se', e' quando lo usiamo per cose serie.

**EN:** The term "vibe coding" was coined by Andrej Karpathy. The idea is simple: you describe what you want, the AI generates code, it feels right (the "vibe"), and you accept it. It has enormous value for prototyping and learning. The problem isn't vibe coding itself, it's when we use it for serious things.
-->

---

# Where Vibe Coding Breaks

<div class="grid-content">
<div class="danger">

### Security
AI-generated code often has vulnerabilities. SQL injection, XSS, hardcoded secrets. The "vibe" doesn't catch CVEs.

</div>
<div class="danger">

### Maintainability
Code that "vibes" right today becomes legacy debt tomorrow. No architecture, no patterns, no consistency.

</div>
<div class="danger">

### Correctness
"It works on my machine" scaled to "It works in the chat window". Edge cases, race conditions, data integrity.

</div>
<div class="danger">

### Reliability
~50% agent task success rate without structure. Half the time the agent produces something broken or off-spec.

</div>
</div>

<div class="warning text-center" style="margin-top: 0.6rem;">
The core issue: <b>poor task specification</b>, not poor model capability.
</div>

<!--
**IT:** Ecco dove il vibe coding crolla. Ma il dato piu' importante e' quello in basso a destra: senza struttura, il tasso di successo degli agenti AI e' circa il 50%. Meta' delle volte producono qualcosa di rotto o fuori specifica. Il problema non e' il modello, e' che non gli diamo specifiche chiare. Ed e' qui che cambia tutto.

**EN:** Here's where vibe coding collapses. But the most important data point is bottom-right: without structure, the AI agent success rate is around 50%. Half the time they produce something broken or off-spec. The problem isn't the model, it's that we don't give it clear specs. And that's where everything changes.
-->

---

# The Evolution

<div class="columns-3">
<div class="danger">

### Vibe Coding

"Make me a website"

AI generates code.
You hope it works.

**~50% success rate**

No constraints
</div>
<div class="warning">

### Prompt Engineering

"Create a React app with TypeScript, use Next.js App Router, add error boundaries"

**~70% success rate**

Prompt constraints
</div>
<div class="success">

### Agentic Engineering

"Here are the specs, the harness, the tests. The agent operates within these guardrails."

**~95% success rate**

System constraints
</div>
</div>

<div class="highlight text-center" style="margin-top: 0.5rem;">
The leap isn't in the model. It's in <b>the system surrounding the model</b>.
</div>

<!--
**IT:** Vediamo l'evoluzione con i numeri. Nel vibe coding, circa 50% di successo. Col prompt engineering saliamo al 70%. Ma con l'agentic engineering, con specifiche chiare, harness strutturati, e feedback loop, arriviamo al 95%. Il salto non e' nel modello, e' nel sistema che circonda il modello.

**EN:** Let's see the evolution with numbers. In vibe coding, about 50% success. With prompt engineering we get to 70%. But with agentic engineering, with clear specs, structured harnesses, and feedback loops, we reach 95%. The leap isn't in the model, it's in the system surrounding the model.
-->

---

# From Prompt to Harness Engineering

<div class="columns">
<div>

### Prompt Engineering
- Crafting the perfect prompt
- Context stuffing
- One interaction at a time
- The human is the orchestrator
- Knowledge lives in your head

</div>
<div>

### Harness Engineering
- Designing the operating environment
- Project rules (`CLAUDE.md`)
- Spec-driven task breakdown
- Automated validation & feedback loops
- Knowledge lives in the system

</div>
</div>

<div class="evolution-arrow">
📝 → 🏗️
</div>

<div class="highlight text-center">
A good prompt helps for one turn. A good harness helps <b>permanently</b>.
</div>

<!--
**IT:** La distinzione chiave: il prompt engineering e' per-interazione, l'harness engineering e' un investimento permanente. Crei l'ambiente una volta, e ogni agente eredita quelle regole. Ma l'harness da solo non basta: serve un modo per spezzare il lavoro in task con specifiche chiare. Ed e' qui che entra Backlog.md.

**EN:** The key distinction: prompt engineering is per-interaction, harness engineering is a permanent investment. You create the environment once, and every agent inherits those rules. But the harness alone isn't enough: you need a way to break work into tasks with clear specs. And that's where Backlog.md comes in.
-->

---

# The Missing Piece: Spec-Driven Development

<div class="bg-light">

### The problem with "just implement feature X"
The agent doesn't know **what "done" looks like**. No acceptance criteria, no scope boundaries, no testable outcomes. It fills the gaps with assumptions.

</div>

<div class="columns" style="margin-top: 0.6rem;">
<div class="danger">

### Without specs
```
You: "Add user search"
Agent: builds something...
  - Wrong search algorithm?
  - Missing pagination?
  - No error handling?
  - Touches unrelated files?

WHO KNOWS. No spec = no way
to validate the output.
```

</div>
<div class="success">

### With specs
```
Task: "Add user search"
Acceptance Criteria:
  ✓ Full-text search on name/email
  ✓ Results paginated (20/page)
  ✓ Returns 404 on empty results
  ✓ Response time < 200ms
  ✓ Unit tests for all paths
Scope: only src/users/
```

</div>
</div>

<!--
**IT:** Ecco il pezzo mancante. Dire all'agente "implementa la ricerca utenti" e' vibe coding mascherato. L'agente non sa cosa significa "fatto". Senza criteri di accettazione, senza confini di scope, senza outcome testabili, riempie i vuoti con assunzioni. A destra vedete la differenza: specifiche chiare con criteri testabili. Questo e' l'approccio spec-driven che ci porta al 95% di successo.

**EN:** Here's the missing piece. Telling the agent "implement user search" is vibe coding in disguise. The agent doesn't know what "done" means. Without acceptance criteria, scope boundaries, or testable outcomes, it fills the gaps with assumptions. On the right you see the difference: clear specs with testable criteria. This is the spec-driven approach that gets us to 95% success.
-->

---

# Backlog.md: Specs for Agents

<div class="bg-light">

**Backlog.md** is an open-source, markdown-native task manager designed for human-AI collaboration. Tasks live as `.md` files in your repo. No SaaS, no external tools, 100% Git-native.

</div>

<div class="columns" style="margin-top: 0.6rem;">
<div class="bg-light">

### The 3-Phase Loop

**1. Task Creation** (Spec-Driven)
- Break work into atomic tasks
- Each task has acceptance criteria
- Written as "work order for a stranger"

**2. Task Execution** (Plan-First)
- Agent drafts plan before coding
- Human approves plan
- Only then: implement

**3. Task Finalization** (DoD)
- Verify all acceptance criteria
- Write PR-style summary
- Propose (don't create) follow-ups

</div>
<div class="bg-light">

### Why It Works

- **One task per session, one PR per task**
- The creating agent is NOT the executing agent
- All context is self-contained in the task
- Human-in-the-loop at critical checkpoints
- Git-native audit trail

### Key Rule

<div class="warning">
"Write every task as a work order for a stranger who knows nothing about your conversation."
</div>

This forces completeness and eliminates assumptions.

</div>
</div>

<!--
**IT:** Backlog.md e' il tool che risolve il problema delle specifiche. E' un task manager markdown-native: i task sono file .md nel vostro repo, versionati con Git. Il loop e' in tre fasi: creazione con specifiche e criteri di accettazione, esecuzione con piano approvato, e finalizzazione con verifica. La regola chiave: ogni task va scritto come un ordine di lavoro per uno sconosciuto. Questo forza la completezza e elimina le assunzioni.

**EN:** Backlog.md is the tool that solves the specs problem. It's a markdown-native task manager: tasks are .md files in your repo, versioned with Git. The loop is three phases: creation with specs and acceptance criteria, execution with approved plan, and finalization with verification. The key rule: every task must be written as a work order for a stranger. This forces completeness and eliminates assumptions.
-->

---

# Backlog.md in Action

<div class="bg-light small">

```markdown
# Task: Add Core Search Functionality

## Status: In Progress

## Description
Implement full-text search for users by name and email in the users API module.

## Acceptance Criteria
- [ ] GET /users/search?q=<query> endpoint
- [ ] Full-text search on name and email fields
- [ ] Results paginated (20 per page, configurable)
- [ ] Returns empty array (not 404) for no results
- [ ] Search is case-insensitive
- [ ] Response time < 200ms for 10k users
- [ ] Unit tests cover: valid search, empty result, pagination, special characters

## Scope
- ONLY modify files in src/users/
- Do NOT change database schema

## Implementation Plan (approved ✓)
1. Add search repository method with SQL ILIKE
2. Create search endpoint in routes.py
3. Add pagination helper
4. Write test suite
```

</div>

<div class="highlight text-center">
The agent reads this, implements exactly what's specified, and checks off criteria as it goes.
</div>

<!--
**IT:** Ecco un task Backlog.md reale. Guardate la struttura: descrizione, criteri di accettazione con checkbox, scope esplicito con confini chiari, e il piano di implementazione approvato dall'umano. L'agente legge questo file, implementa esattamente quello che e' specificato, e spunta i criteri man mano che li completa. Nessuna assunzione, nessuna deriva di scope. Questo e' il cambio dal 50% al 95% di successo.

**EN:** Here's a real Backlog.md task. Notice the structure: description, acceptance criteria with checkboxes, explicit scope with clear boundaries, and the implementation plan approved by the human. The agent reads this file, implements exactly what's specified, and checks off criteria as it goes. No assumptions, no scope drift. This is the change from 50% to 95% success.
-->

---

# But One Agent Is Not Enough

<div class="bg-light">

Real projects need **parallel work streams**:
backend API, frontend UI, tests, documentation, security review...

</div>

<div style="margin-top: 0.6rem;">

### The orchestration problem

```
Agent 1: working on backend API          → needs monitoring
Agent 2: working on frontend components  → needs monitoring
Agent 3: writing integration tests       → needs monitoring
Agent 4: updating documentation          → needs monitoring

Developer: ALT-TABbing between 4 terminals, losing sanity
```

</div>

<div class="warning text-center" style="margin-top: 0.6rem;">
Agentic engineering at scale requires <b>multi-agent orchestration</b>.
You need a command center, not a pile of terminal tabs.
</div>

<!--
**IT:** Ma un singolo agente non basta per progetti reali. Servono stream di lavoro paralleli: backend, frontend, test, documentazione. E qui nasce il problema dell'orchestrazione: come monitorate 4 agenti che lavorano in parallelo? Alt-Tab tra terminali? Non scala. Serve un centro di comando. Ed e' qui che entra LINCE.

**EN:** But a single agent isn't enough for real projects. You need parallel work streams: backend, frontend, tests, documentation. And here's the orchestration problem: how do you monitor 4 agents working in parallel? Alt-tabbing between terminals? Doesn't scale. You need a command center. And that's where LINCE comes in.
-->

---

# LINCE: The Agent Command Center

<div class="bg-light">

**LINCE** (Linux Intelligent Native Coding Environment) is a TUI dashboard for managing multiple Claude Code agents simultaneously. A Zellij WASM plugin built in Rust.

</div>

<div class="columns" style="margin-top: 0.6rem;">
<div class="bg-light">

### Core Features
- **Multiple agents** in one terminal
- Real-time status: Running, INPUT, Idle
- Token usage tracking per agent
- Active tool display (what is each agent doing?)
- Subagent count tracking
- Focus/hide agent panes with one key
- Session persistence (save & restore)

</div>
<div class="bg-light">

### The Safety Layer
- Every agent runs in a **bubblewrap sandbox**
- Full write access to project directory
- **Zero access** to SSH keys, cloud credentials, home directory
- Enables `--dangerously-skip-permissions` safely
- Full autonomy within strict boundaries

### Bonus
- **Voice control** via local Whisper
- Speak commands, routed to focused agent

</div>
</div>

<!--
**IT:** LINCE e' una dashboard TUI per gestire piu' agenti Claude Code contemporaneamente. E' un plugin Zellij scritto in Rust. Potete avere fino a 8 agenti, ognuno con stato in tempo reale, tracking dei token, e display del tool attivo. Ogni agente gira in un sandbox bubblewrap: accesso completo al progetto, zero accesso a credenziali e SSH key. Questo vi permette di dare piena autonomia agli agenti senza rischi reali. E c'e' pure il controllo vocale con Whisper locale.

**EN:** LINCE is a TUI dashboard for managing multiple Claude Code agents simultaneously. It's a Zellij plugin written in Rust. You can have up to 8 agents, each with real-time status, token tracking, and active tool display. Every agent runs in a bubblewrap sandbox: full project access, zero access to credentials and SSH keys. This lets you give agents full autonomy without real risk. And there's even voice control with local Whisper.
-->

---

# The Full Stack: Backlog.md + LINCE

```
┌─────────────────────────────────────────────────────────┐
│                    DEVELOPER                            │
│          (Defines specs, reviews, approves)             │
├─────────────────────────────────────────────────────────┤
│                   BACKLOG.MD                            │
│   Spec-driven tasks with acceptance criteria & DoD      │
├─────────────────────────────────────────────────────────┤
│                 LINCE DASHBOARD                         │
│    Multi-agent orchestration, monitoring, sandboxing    │
├────────────┬────────────┬────────────┬──────────────────┤
│  Agent 1   │  Agent 2   │  Agent 3   │    Agent 4       │
│  Backend   │  Frontend  │   Tests    │    Docs          │
│  🟢 Running │  🟡 INPUT  │  🟢 Running │   🔵 Idle        │
├────────────┴────────────┴────────────┴──────────────────┤
│                     HARNESS                             │
│   CLAUDE.md + Linters + Tests + CI + Pre-commit hooks   │
└─────────────────────────────────────────────────────────┘
```

<div class="highlight text-center">
Specs (Backlog.md) + Orchestration (LINCE) + Guardrails (Harness) = <b>Agentic Engineering</b>
</div>

<!--
**IT:** Ecco lo stack completo. In cima lo sviluppatore che definisce le specifiche e fa review. Poi Backlog.md che struttura il lavoro in task con criteri di accettazione. LINCE che orchestra piu' agenti in parallelo con monitoring e sandboxing. Gli agenti che lavorano autonomamente su stream diversi. E alla base l'harness: CLAUDE.md, linter, test, CI. Questa e' l'agentic engineering completa: specifiche, orchestrazione, e guardrail.

**EN:** Here's the complete stack. At the top, the developer defining specs and reviewing. Then Backlog.md structuring work into tasks with acceptance criteria. LINCE orchestrating multiple agents in parallel with monitoring and sandboxing. The agents working autonomously on different streams. And at the base, the harness: CLAUDE.md, linters, tests, CI. This is complete agentic engineering: specs, orchestration, and guardrails.
-->

---

# Demo: The Agentic Workflow

<div class="bg-light small">

```
STEP 1 - SPEC (Backlog.md)
$ claude "Break down the user management feature into tasks"
→ Agent creates 4 tasks in backlog/ with acceptance criteria and scope

STEP 2 - REVIEW
Developer reviews tasks, adjusts scope, approves plans

STEP 3 - ORCHESTRATE (LINCE)
$ lince-dashboard
┌─────────────────────────────────────────────────┐
│ LINCE Dashboard           Agents: 3 | Tokens: 45k │
├─────────────────────────────────────────────────┤
│ 🟢 agent-backend  │ Running │ Edit src/users  │ 12k │
│ 🟢 agent-tests    │ Running │ pytest          │ 8k  │
│ 🟡 agent-frontend │ INPUT   │ waiting...      │ 25k │
└─────────────────────────────────────────────────┘

STEP 4 - VALIDATE
Each agent runs tests, checks acceptance criteria, creates PR
Agent-frontend asks: "Should search be client-side or server-side?"
Developer answers, agent continues autonomously
```

</div>

<!--
**IT:** Ecco la demo in azione. Step 1: con Backlog.md l'agente spezza la feature in 4 task con specifiche. Step 2: lo sviluppatore fa review e approva i piani. Step 3: con LINCE lanciamo 3 agenti in parallelo. La dashboard mostra lo stato in tempo reale. L'agente backend sta modificando codice, l'agente test sta runnando pytest, l'agente frontend ha bisogno di input. Step 4: ogni agente valida il proprio lavoro contro i criteri di accettazione e crea una PR. L'intero flusso e' strutturato, monitorato, e sandboxed.

**EN:** Here's the demo in action. Step 1: with Backlog.md the agent breaks the feature into 4 tasks with specs. Step 2: the developer reviews and approves plans. Step 3: with LINCE we launch 3 agents in parallel. The dashboard shows real-time status. The backend agent is editing code, the test agent is running pytest, the frontend agent needs input. Step 4: each agent validates its work against acceptance criteria and creates a PR. The entire flow is structured, monitored, and sandboxed.
-->

---

# Patterns vs Anti-Patterns

<div class="columns">
<div class="success">

### What Works

**Spec-first development**
Write the task spec before any code

**One task, one agent, one PR**
Atomic, verifiable units of work

**Plan-then-execute**
Agent drafts plan, human approves

**Sandboxed autonomy**
Full freedom within strict boundaries

**Feedback loops**
Tests + linting + CI as teacher

**Scope containment**
"Only modify files in src/auth/"

</div>
<div class="danger">

### What Doesn't Work

**The Mega-Prompt**
Stuffing everything into one prompt

**YOLO Mode**
"Just do it, I trust the AI"

**Micromanagement**
Dictating every step to the agent

**No Feedback Loop**
Agent produces output, nobody checks

**Scope-Free Agents**
No boundaries = unpredictable changes

**One-Shot Thinking**
Expecting perfection on first try

</div>
</div>

<!--
**IT:** Riassumiamo i pattern e gli anti-pattern. A sinistra, quello che funziona: spec-first, un task per agente per PR, piano prima dell'esecuzione, autonomia sandboxed, feedback loop, e contenimento dello scope. A destra, quello che non funziona: mega-prompt, YOLO mode, micromanagement, nessun feedback, agenti senza confini, e aspettarsi perfezione al primo colpo. Backlog.md e LINCE implementano i pattern di sinistra strutturalmente, non come buone intenzioni.

**EN:** Let's summarize patterns and anti-patterns. On the left, what works: spec-first, one task per agent per PR, plan before execute, sandboxed autonomy, feedback loops, and scope containment. On the right, what doesn't: mega-prompt, YOLO mode, micromanagement, no feedback, boundaryless agents, and expecting first-try perfection. Backlog.md and LINCE implement the left-side patterns structurally, not as good intentions.
-->

---

# The Developer's New Role

<div class="columns">
<div class="bg-light">

### What You Stop Doing
- Writing boilerplate code
- Manual formatting and syntax
- Being the human compiler
- Alt-tabbing between terminals
- Holding context in your head

</div>
<div class="bg-light">

### What You Start Doing
- Writing specs and acceptance criteria
- Designing harnesses and guardrails
- Reviewing agent plans and output
- Orchestrating parallel work streams
- Being the system architect

</div>
</div>

<div style="margin-top: 0.6rem;">

| Before | After |
|--------|-------|
| "I can write React" | "I can write specs that agents implement correctly" |
| "I know Python syntax" | "I can design validation pipelines" |
| "I debug by reading code" | "I debug by improving guardrails" |
| "I manage my TODO list" | "I manage a fleet of sandboxed agents" |

</div>

<!--
**IT:** Il ruolo dello sviluppatore cambia. Non scrivete piu' boilerplate, non fate Alt-Tab tra terminali, non tenete il contesto in testa. Invece, scrivete specifiche e criteri di accettazione, progettate harness, fate review di piani e output, orchestrate stream paralleli. La tabella in basso mostra il cambio di skill: da "so scrivere React" a "so scrivere spec che gli agenti implementano correttamente".

**EN:** The developer's role changes. You stop writing boilerplate, alt-tabbing between terminals, holding context in your head. Instead, you write specs and acceptance criteria, design harnesses, review plans and output, orchestrate parallel streams. The table below shows the skill shift: from "I can write React" to "I can write specs that agents implement correctly".
-->

---

# What This Means For You Today

<div class="columns-3">
<div class="bg-light">

### Start Now

- Add `CLAUDE.md` to your projects
- Install **Backlog.md**: specs for every task
- Write acceptance criteria, not vague requests
- Set up pre-commit hooks

</div>
<div class="bg-light">

### Level Up

- Try **LINCE** for multi-agent work
- Design feedback loops (tests as teachers)
- Practice the plan-then-execute loop
- Sandbox your agents

</div>
<div class="bg-light">

### Think Ahead

- Learn system design, not just syntax
- Practice declarative thinking
- Embrace constraint-driven design
- Build agent-friendly codebases

</div>
</div>

<div class="highlight text-center" style="margin-top: 1rem;">
<b>backlog.md</b> → github.com/MrLesk/Backlog.md | <b>lince</b> → github.com/RisorseArtificiali/lince
</div>

<!--
**IT:** Cosa potete fare da oggi? Iniziate con CLAUDE.md e Backlog.md: scrivete specifiche per ogni task, non richieste vaghe. Poi salite di livello con LINCE per il lavoro multi-agente, sandbox, e feedback loop. Pensate avanti: imparate system design, pensiero dichiarativo, constraint-driven design. I link ai due tool sono in basso.

**EN:** What can you do starting today? Start with CLAUDE.md and Backlog.md: write specs for every task, not vague requests. Then level up with LINCE for multi-agent work, sandboxing, and feedback loops. Think ahead: learn system design, declarative thinking, constraint-driven design. Links to both tools are at the bottom.
-->

---

<!-- _class: lead -->

# Key Takeaways

<div style="margin-top: 1rem;">

### 1. Vibe coding: ~50% success. Spec-driven agentic: ~95%.
### 2. The new skill is **harness engineering**, not prompt engineering
### 3. **Backlog.md**: write specs as work orders for strangers
### 4. **LINCE**: orchestrate multiple sandboxed agents in parallel
### 5. Constraints make agents **more reliable**, not less capable

</div>

<div class="highlight text-center" style="margin-top: 1.5rem;">
The coding you didn't know you wanted is the coding where you <b>design the system</b> instead of writing the code.
</div>

<!--
**IT:** Cinque takeaway. Uno: dal 50% al 95% di successo con l'approccio spec-driven. Due: la nuova skill e' l'harness engineering. Tre: Backlog.md per scrivere specifiche come ordini di lavoro per sconosciuti. Quattro: LINCE per orchestrare agenti sandboxed in parallelo. Cinque: i vincoli rendono gli agenti piu' affidabili, non meno capaci. Il coding che non sapevate di volere e' quello dove progettate il sistema invece di scrivere il codice.

**EN:** Five takeaways. One: from 50% to 95% success with spec-driven approach. Two: the new skill is harness engineering. Three: Backlog.md for writing specs as work orders for strangers. Four: LINCE for orchestrating sandboxed agents in parallel. Five: constraints make agents more reliable, not less capable. The coding you didn't know you wanted is the one where you design the system instead of writing the code.
-->

---

<!-- _class: lead -->

# Thank You

<div class="columns">
<div>

## Stefano Maestri

**maeste.it**

**Podcast:** risorseartificiali.com

**Newsletter:** codiceartificiale.substack.com
artificialcode.substack.com

**Backlog.md** → github.com/MrLesk/Backlog.md
**LINCE** → github.com/RisorseArtificiali/lince

</div>
<div class="text-center">

![w:280](maeste-qr.png)

**maeste.it**

</div>
</div>

<div class="highlight text-center" style="margin-top: 0.5rem;">
Questions?
</div>

<!--
**IT:** Grazie a tutti! Trovate tutto su maeste.it, il QR code vi porta direttamente li'. Il podcast Risorse Artificiali e le newsletter Codice Artificiale e Artificial Code per restare aggiornati. Backlog.md e LINCE su GitHub. Domande?

**EN:** Thank you all! You can find everything at maeste.it, the QR code takes you right there. The Risorse Artificiali podcast and the Codice Artificiale / Artificial Code newsletters to stay updated. Backlog.md and LINCE on GitHub. Questions?
-->
