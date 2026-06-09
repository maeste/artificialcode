# Campagna LINCE - Post Definitivi

## Calendario

**Nota:** Il 14 aprile e' lunedi', non mercoledi'. Ho assunto che l'intervista esca mercoledi' 16 aprile ed evito quel giorno. Se la data e' diversa, segnalalo e adeguo.

| # | Data | Giorno | Piattaforma | Account | Angolo |
|---|------|--------|-------------|---------|--------|
| 1 | 8 apr | Mar | LinkedIn EN | Personale | Launch story |
| 2 | 8 apr | Mar | X.com | Personale | Sandbox YOLO |
| 3 | 9 apr | Mer | LinkedIn IT | Risorse Artificiali | Launch story (team) |
| 4 | 10 apr | Gio | LinkedIn IT | Risorse Artificiali | Sandbox YOLO (team) |
| 5 | 10 apr | Gio | X.com | Personale | Multi-agent |
| 6 | 11 apr | Ven | LinkedIn EN | Personale | Sandbox YOLO |
| 7 | 12 apr | Sab | X.com | Personale | Terminal-only |
| 8 | 14 apr | Lun | X.com | Personale | VoxCode / Linux |
| 9 | 15 apr | Mar | LinkedIn EN | Personale | Multi-agent |
| 10 | 15 apr | Mar | LinkedIn IT | Risorse Artificiali | Multi-agent (team) |
| 11 | 17 apr | Gio | LinkedIn EN | Personale | Terminal-only |
| 12 | 17 apr | Gio | X.com | Personale | Sandbox revisit |
| 13 | 18 apr | Ven | LinkedIn IT | Risorse Artificiali | Terminal + VoxCode (team) |
| 14 | 19 apr | Sab | X.com | Personale | Closer / CTA |

**Conflitti evitati:**
- Sab 12 e 19 apr: nessun post LinkedIn IT (post podcast RA alle 13:00)
- Mer 16 apr: nessun post (intervista alle 17:00)

**Note sui giorni:**
- Martedi'/mercoledi'/giovedi': picco engagement LinkedIn, ideali per contenuto tecnico e annunci
- Venerdi': tono leggermente piu' rilassato, buono per riflessioni
- Sabato: contenuto "provocatorio" o lifestyle su X, dove il pubblico dev scorre nel weekend
- Lunedi': ripresa settimana, buono per contenuto di nicchia

---

## Post #1 — Mar 8 apr — LinkedIn EN (Personale)
**Angolo: Launch story**

A couple of months ago, I stood on stage at Voxxed Day Ticino and said: "The attack surface is you, not your software."

The audience laughed. Then they thought about it. Then they stopped laughing.

We were all having the same experience with AI coding agents: clicking "approve" on autopilot, pretending we were reviewing each action when we were really just rubber-stamping. The security model was theatrical, not structural.

In the weeks that followed, together with the @[Risorse Artificiali] team, we built LINCE.

It's a terminal-based multi-agent coding workstation. Open source, MIT license. Kernel-level sandboxing so agents run freely without permission dialogs. A lightweight Rust/WASM dashboard (~900KB) to orchestrate multiple agents in parallel. Session persistence. Voice input via local Whisper. Vendor-independent: Claude Code, Codex, Gemini, OpenCode, Aider, or any custom agent via TOML.

This isn't a product launch. It's a contribution. We built what we needed, and we're sharing it because we think others need it too.

Star the repo, try it out, tell us what's broken. That's how open source works.

https://lince.sh | https://github.com/RisorseArtificiali/lince

#OpenSource #AIAgents #DevTools #CodingWorkstation #TerminalFirst

> **Media:** `social/media/dashboard-detail.png`

---

## Post #2 — Mar 8 apr — X.com (Personale)
**Angolo: Sandbox YOLO**

I run AI coding agents with zero permission prompts. Kernel-level sandboxing, zero overhead, snapshot rollback. The attack surface isn't your software. It's you clicking "approve" on autopilot. LINCE fixes that.

https://lince.sh

> **Media:** `social/media/lince-demo.gif`

---

## Post #3 — Mer 9 apr — LinkedIn IT (Risorse Artificiali)
**Angolo: Launch story (voce team)**

Un paio di mesi fa al Voxxed Day Ticino, il nostro Stefano ha detto una frase durante un panel sulla sicurezza che ci e' rimasta in testa: "La superficie d'attacco sei tu, non il software che produci."

Non era una provocazione. Era una frustrazione condivisa da tutto il team. Lavoravamo tutti i giorni con agenti AI di coding e vedevamo lo stesso schema: l'agente chiede permesso, approvi. Chiede ancora, approvi ancora. Dopo un po' approvi senza leggere. E quello e' il momento in cui sei vulnerabile.

Nelle settimane successive abbiamo costruito LINCE.

E' una workstation multi-agente che vive interamente nel terminale. Sandbox a livello kernel (bubblewrap su Linux, nono su macOS) con zero overhead. Dashboard in Rust/WASM per orchestrare 3-5 agenti in parallelo e sapere sempre chi ha bisogno di input. VoxCode per comandi vocali con Whisper locale (una benedizione per chi su Linux ha sempre lottato con l'audio). Supporto per Claude Code, Codex, Gemini, OpenCode, Aider e agenti custom via TOML.

Non ci siamo legati a nessun vendor. E' open source, licenza MIT.

Provatelo, aprite issue, mandateci PR. Lo trovate qui: https://lince.sh

#OpenSource #LINCE #RisorseArtificiali #AIEngineering #DevTools

> **Media:** `social/media/dashboard-detail.png`

---

## Post #4 — Gio 10 apr — LinkedIn IT (Risorse Artificiali)
**Angolo: Sandbox YOLO (voce team)**

Il pattern piu' pericoloso nello sviluppo con agenti AI non e' un prompt injection.

E' lo sviluppatore che clicca "approva" per la centesima volta senza leggere cosa sta approvando.

Lo vediamo continuamente nel team. Parti con le migliori intenzioni, controlli ogni richiesta. Dopo mezz'ora con 3 agenti in parallelo, il cervello si arrende e approvi tutto a occhi chiusi.

Per questo in LINCE abbiamo ribaltato il problema. Invece di chiedere permessi, mettiamo tutto dentro una sandbox a livello kernel. Bubblewrap su Linux, nono su macOS. Zero overhead sulle prestazioni. L'agente opera liberamente perche' il danno massimo e' confinato. E se qualcosa va storto, snapshot e rollback in un attimo.

Non e' YOLO nel senso di "ce ne freghiamo". E' YOLO nel senso di "l'ambiente e' sicuro, quindi l'agente puo' lavorare libero e noi possiamo concentrarci sulla verifica".

Provatelo: https://lince.sh | https://github.com/RisorseArtificiali/lince

#DevSecurity #CodingAgents #OpenSource #LINCE #AIEngineering

> **Media:** `social/media/lince-sandbox.png`

---

## Post #5 — Gio 10 apr — X.com (Personale)
**Angolo: Multi-agent orchestration**

5 AI agents in parallel. One refactors, one tests, one fixes CI. I switch between them with a keystroke. The bottleneck isn't generation anymore, it's verification. LINCE makes multi-agent practical.

https://lince.sh

> **Media:** `social/media/dashboard-full.png`

---

## Post #6 — Ven 11 apr — LinkedIn EN (Personale)
**Angolo: Sandbox YOLO**

"But aren't you afraid to let agents run without any controls?"

I get this question every time. The answer: it depends on where they run.

The real problem with AI coding agents isn't that they make mistakes (they do, constantly). The problem is they ask permission for every single operation. And after the twentieth popup, you start approving everything without reading.

That's the real security flaw. It's you.

LINCE uses kernel-level sandboxing with bubblewrap and nono. No overhead. The agent operates in a fully isolated environment, it can do whatever it wants without asking. If it causes a disaster, you roll back from a snapshot.

It's not YOLO as in "I don't care." It's YOLO as in "the environment is safe, so the agent can work freely."

Built with the @[Risorse Artificiali] team. Open source, MIT.

https://lince.sh | https://github.com/RisorseArtificiali/lince

#DevTools #CodingAgents #OpenSource #Sandbox #AIEngineering

> **Media:** `social/media/lince-sandbox.png`

---

## Post #7 — Sab 12 apr — X.com (Personale)
**Angolo: Terminal-only**

My entire coding setup: one terminal. No IDE. No browser. No Electron eating 16GB of RAM. LINCE is a terminal-native multi-agent workstation. Sandbox, dashboard, voice input, session persistence. Minimal dependencies.

https://lince.sh

> **Media:** `social/media/lince-hero.png`

---

## Post #8 — Lun 14 apr — X.com (Personale)
**Angolo: VoxCode / Linux audio**

Linux + voice dictation + coding agents = pain. PulseAudio, PipeWire, daemons that don't talk. We built VoxCode: local Whisper, routed to your active agent, no audio config needed. Part of LINCE.

https://github.com/RisorseArtificiali/lince/tree/main/voxcode

> **Media:** `social/media/dashboard-detail.png` (ha VoxCode visibile)

---

## Post #9 — Mar 15 apr — LinkedIn EN (Personale)
**Angolo: Multi-agent orchestration**

The bottleneck of AI coding agents is no longer code generation. It's verification.

You can launch 8 agents in parallel. The problem is knowing which one needs input, which one finished, which one got stuck. With current tools you jump from window to window, lose the thread, forget what the third agent was doing.

LINCE solves this with a dashboard written in Rust/WASM (a Zellij plugin, about 900KB). From a single panel you see all active agents, their status, who needs you. You switch with a single keystroke.

The sweet spot we've found is 3-5 agents in parallel. Enough to multiply productivity, few enough to maintain control.

The result: less context switching, more time verifying the work that matters. Because as Addy Osmani writes, the real shift is from being the musician to being the conductor.

Built with @[Risorse Artificiali]. Open source, MIT: https://lince.sh

#DevProductivity #AIEngineering #OpenSource #MultiAgent #TerminalFirst

> **Media:** `social/media/lince-demo.webm` (video) oppure `social/media/dashboard-full.png`

---

## Post #10 — Mar 15 apr — LinkedIn IT (Risorse Artificiali)
**Angolo: Multi-agent (voce team)**

Qual e' il numero giusto di agenti AI da far lavorare in parallelo?

Dopo settimane di test la nostra risposta e': 3-5. Non di piu'.

Con 1-2 agenti non sfrutti il potenziale del parallelismo. Con 8+ perdi piu' tempo a gestirli che a beneficiare del loro lavoro. Lo sweet spot e' nel mezzo.

Ma anche con 3-5 agenti, senza gli strumenti giusti e' un caos. Devi sapere in ogni momento chi sta facendo cosa, chi si e' bloccato, chi ha bisogno di input.

Per questo abbiamo costruito la dashboard di LINCE: un plugin Rust/WASM per Zellij (circa 900KB, leggero come deve essere). Vedi tutto in un colpo d'occhio, navighi con singoli tasti. Il tuo lavoro non e' piu' lanciare agenti. E' verificare il loro output.

Perche' il collo di bottiglia reale non e' mai stato la generazione. E' sempre stata la verifica.

Funziona con qualsiasi agente: Claude Code, Codex, Gemini, OpenCode, Aider, o il vostro agente custom via configurazione TOML. Nessun vendor lock-in.

https://lince.sh | https://github.com/RisorseArtificiali/lince

#MultiAgent #AIEngineering #OpenSource #LINCE #Productivity

> **Media:** `social/media/lince-demo.gif`

---

## Post #11 — Gio 17 apr — LinkedIn EN (Personale)
**Angolo: Terminal-only**

No IDE. No browser. No extra apps. Just the terminal.

It sounds like a limitation. It's a deliberate design choice.

Every program you add to your workflow is one more context switch. One more window to manage, one more interface to remember, one more update that breaks something.

LINCE transforms your shell into a multi-agent engineering workstation. Zellij as window manager. The dashboard plugin (Rust/WASM, ~900KB) orchestrates everything. VoxCode gives you voice input with local Whisper. Kernel-level sandboxing for YOLO mode.

Minimal dependencies. If you have a terminal, you have everything you need.

It's vendor-independent: works with Claude Code, Codex, Gemini, OpenCode, Aider. Want to add a custom agent? A TOML file and you're set.

The terminal is the most composable, portable, scriptable environment we have. LINCE builds on that, it doesn't replace it.

Open source, MIT license. Built by the @[Risorse Artificiali] team.

https://lince.sh

#TerminalFirst #DevTools #OpenSource #AIEngineering #MinimalSetup

> **Media:** `social/media/lince-hero.png`

---

## Post #12 — Gio 17 apr — X.com (Personale)
**Angolo: Sandbox revisit**

The most dangerous pattern in AI coding isn't prompt injection. It's the developer clicking "approve" for the 100th time without reading. LINCE doesn't ask. Kernel-level sandbox, zero overhead, snapshot rollback. It protects you from yourself.

https://lince.sh

> **Media:** `social/media/lince-why.png`

---

## Post #13 — Ven 18 apr — LinkedIn IT (Risorse Artificiali)
**Angolo: Terminal + VoxCode (voce team)**

Niente IDE. Niente browser. Niente app extra. Solo il terminale.

Sembra una limitazione, ma e' una scelta progettuale precisa. Ogni programma che aggiungi al tuo flusso di lavoro e' un context switch in piu'. Un'altra finestra da gestire, un'altra interfaccia da ricordare, un altro aggiornamento che rompe qualcosa.

LINCE trasforma la shell in una workstation di ingegneria multi-agente. Zellij fa da window manager. Il plugin dashboard (Rust/WASM, ~900KB) orchestra tutto.

E per chi su Linux ha sempre lottato con l'audio (sappiamo che siete in tanti), abbiamo sviluppato VoxCode: input vocale con Whisper in locale. Niente cloud, niente latenza, niente configurazioni audio da incubo. Funziona e basta, direttamente nel terminale, integrato con la dashboard e la sandbox.

In queste due settimane dal lancio abbiamo ricevuto feedback che ci ha confermato di essere sulla strada giusta. Se non lo avete ancora provato, fateci sapere cosa ne pensate.

Dipendenze minime. Se hai un terminale, hai tutto.

https://lince.sh | https://github.com/RisorseArtificiali/lince

#TerminalLife #Linux #DevTools #OpenSource #LINCE

> **Media:** `social/media/lince-demo.webm` (video per LinkedIn)

---

## Post #14 — Sab 19 apr — X.com (Personale)
**Angolo: Campaign closer / CTA**

Two weeks in: LINCE is an open-source, terminal-native multi-agent workstation. Kernel sandbox, Rust/WASM dashboard, voice input, vendor-independent. What devs told us they wanted: real isolation, fewer tools, no permission theater.

https://lince.sh

> **Media:** `social/media/dashboard-full.png`
