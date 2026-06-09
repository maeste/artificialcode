La notizia della settimana, che sicuramente non vi sarete persi, è il leak del codice di Claude Code. Notizia senz'altro rilevante, ma di certo non l'unica cosa che segnalo in questa newsletter. Mi soffermo anche sull'uscita di Gemma 4, i modelli open weight di Google che soprattutto nelle versioni più piccole sembrano molto promettenti e hanno dei grandi risultati. Comunque non mancano gli approfondimenti sulle cose che abbiamo imparato guardando al codice di Claude Code, perché di certo ci sono cose da imparare, dato che rimane una delle migliori piattaforme di agentic coding in questo momento sul mercato. E la rete si è scatenata, sia scaricando i sorgenti, sia parlandone in articoli, sia creandone delle versioni in Rust e Python.

Prima di lasciarvi alla lettura, vi raccomando di non perdervi il podcast di Simon Willison, che mette l'accento sui rischi di burnout per gli sviluppatori, sempre più nel vortice dell'orchestrazione multiagentica durante le fasi di coding. E ovviamente non perdetevi anche il nostro podcast e tutte le iniziative che vi riassumo qui nella mia agenda.

### La mia agenda

[Podcast](https://risorseartificiali.com) con Alessio e Paolo:
  * È uscita una bella intervista a Gabriele Venturi fondatore di PandasAI e nerd vero :)
  * Stiamo lavorando ad altre interviste e puntate con ospiti molto interessanti.
  * Ormai sapete del nostro repository su GitHub con tool e configurazioni per fare AI coding da terminale su Linux. Ora ha un suo sito con installazione a singolo script [Lince.sh](https://lince.sh)
  * Abbiamo rilasciato AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), che è un software per tradurre messaggi vocali in testo

Da solo:
  * È stato pubblicato il video del talk che ho fatto con Alessio al [VoxxedDay Zurich](https://www.youtube.com/watch?v=DXEsG3Vo6F4)
  * Il 30 maggio avrò l'onore di essere uno dei [PyCon Italia speakers](https://2026.pycon.it/en/speakers)
  * Il 12 giugno sarò a Catania come speaker al [Coderful](https://www.coderful.io/)

---

## Novita e ricerca nei modelli AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** I modelli open weight piccoli come Gemma 4 stanno rendendo concreta un'architettura agentica a due livelli: locale per task semplici, cloud per orchestrazione complessa.
- **Takeaway 2:** Qwen dimostra che il ragionamento multimodale nativo (non solo multiformato in input) sta diventando realtà nei modelli open.
- **Takeaway 3:** Per i player europei come Mistral, la nicchia dei modelli specializzati e compatti potrebbe essere la strategia vincente rispetto alla competizione generalista.

- **Action Items:**
  - Provate Gemma 4 in locale per task di speech-to-text o processing leggero: i benchmark sono promettenti e la nostra esperienza con AntiVocale lo conferma.
  - Tenete d'occhio il leak su Mythos di Anthropic: se confermato, potrebbe ridefinire il benchmark di riferimento per i modelli frontier.

### Cosa succede questa settimana?

Le notizie relative ai modelli di questa settimana sono indubbiamente dominate dall'uscita di Gemma 4 da parte di Google, una nuova famiglia di modelli open weight relativamente piccoli che danno una grande spinta all'utilizzo di modelli anche in locale, perché forniscono prestazioni davvero notevoli. Sempre di più, guardando a quello che succede con i modelli open weight di piccole dimensioni, comincio a pensare che si stia delineando un'architettura per gli agenti che presto si baserà su due livelli: uno locale, con modelli relativamente piccoli per compiti più semplici o per metaprocessare le informazioni, per poi demandare a modelli state of the art l'orchestrazione e i compiti più complessi.

Ma tornando ai modelli di Google, come dicevo, i risultati dei benchmark sono davvero notevoli e in più si tratta di modelli completamente multimodali. In uno dei progetti open source che stiamo rilasciando con il gruppo di Risorse Artificiali, AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), che è un software per tradurre messaggi vocali in testo, abbiamo introdotto anche i Gemma 4 con buona soddisfazione. Da una prima prova, hanno prestazioni simili a Whisper per quanto riguarda lo speech-to-text, ma con un miglioramento sulla capacità di inferenziare la punteggiatura. Questa è la nostra esperienza diretta, però gli articoli che riporto sono molto interessanti, soprattutto quello che ne presenta in modo visuale l'architettura: vi raccomando di darci un'occhiata se siete curiosi di capire come un modello è fatto internamente.

Di certo i cinesi non stanno a guardare, perché Qwen ha rilasciato due modelli questa settimana: un omnimodale (quindi che supporta tutti i tipi di formato, dall'audio al testo al video in input) e uno invece denominato 3.6-Plus che ha un ragionamento avanzato di tipo multimodale. È da tempo che parlo di questa possibilità in questa newsletter, e finalmente, in maniera così esplicita, Qwen rilascia un modello con ragionamento basato su dati multimodali, che si genera in parte dei dati grafici per poi usarli all'interno della fase di reasoning.

È con piacere che parlo anche dell'Europa, perché Mistral ha rilasciato Voxtral TTS, un modello text-to-speech da soli 4 miliardi di parametri ma che sembra avere delle ottime prestazioni. Non l'ho ancora provato nel dettaglio, ma forse è proprio in questi modelli molto specializzati che Mistral può dire la sua: non certo può competere con i modelli state of the art generalisti, come ha già dimostrato in passato, ma su cose molto specifiche potrebbe essere la loro nicchia di mercato.

Chiudo parlando di un leak arrivato dal mondo Anthropic, e non mi riferisco al leak su Claude Code (di cui parlo nella sezione dei coding agent), ma invece sul fatto che stiano provando internamente un nuovo modello più grande di Opus che sembra avere prestazioni a dir poco impressionanti. Ovviamente si tratta di un leak, non si sa quanto orchestrato per farsi pubblicità, e va preso con le pinze. Ma di sicuro, considerando quanto Opus sia già in grado di fare, un modello più grande che arriva da Anthropic sarà qualcosa di interessante da provare.

### I link della settimana

- [Claude Mythos](https://m1astra-mythos.pages.dev/) — Nuovo tier di modelli Anthropic sopra Opus, con punteggi molto superiori in coding, ragionamento e cybersecurity.
- [A Visual Guide to Gemma 4](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4) — Guida visuale all'architettura dei modelli Gemma 4: attenzione locale/globale, p-RoPE, Mixture of Experts.
- [Gemma 4 Open Models](https://deepmind.google/models/gemma/gemma-4/) — Famiglia di modelli aperti Google DeepMind in 4 varianti, multilingue, multimodali, ottimizzati per uso locale.
- [Qwen3.5-Omni](https://qwen.ai/blog?id=qwen3.5-omni) — Modello omnimodale completo: testo, immagini, audio e video, con supporto per 113 lingue.
- [Qwen3.6-Plus](https://qwen.ai/blog?id=qwen3.6) — Ragionamento multimodale avanzato, tappa critica verso agenti multimodali nativi.
- [Mistral Voxtral TTS](https://mistral.ai/news/voxtral-tts) — Modello text-to-speech da 4B parametri, 9 lingue, espressivo, bassa latenza, open-source.

## Agentic AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** L'orchestrazione visuale degli agenti (come Cline Kanban) sta maturando, ma la complessità resta un trade-off da valutare rispetto a soluzioni più leggere.
- **Takeaway 2:** La memoria persistente è confermata come componente chiave degli agenti efficaci, dal leak di Claude Code fino a soluzioni dedicate come Engram.
- **Takeaway 3:** L'ottimizzazione degli agenti tramite reinforcement learning (Agent Lightning) e training loop strutturati sta passando dalla teoria ai framework utilizzabili.

- **Action Items:**
  - Valutate Cline Kanban se gestite workflow multi-agente complessi, ma confrontatelo con soluzioni più semplici come Backlog.md per i vostri casi d'uso.
  - Esplorate Agent Lightning di Microsoft se volete ottimizzare agenti esistenti senza riscrivere codice.

### Cosa succede questa settimana?

Questa settimana in questa categoria mi concentro su quattro link che cercano di individuare le tendenze di sviluppo e ricerca nell'ambito degli agenti nel mondo AI, e mi riferisco qui ad agenti generici, non necessariamente di codice.

Parto da Cline Kanban, che invece è nato proprio per gli agenti di coding ma che, guardandolo bene, si potrebbe facilmente applicare anche ad agenti più generici. Si tratta di un kanban in cui voi potete orchestrare in maniera grafica e intuitiva gli agenti, creandone dipendenze o workflow. Sicuramente interessante da guardare. Molto più evoluto, e a una prima impressione un pochino troppo complicato per i miei gusti rispetto a Backlog.md, ma di sicuro vale la pena esplorarlo per usi più complessi.

Poi un articolo sulla memoria, Engram Memory System. Da tempo parlo dell'importanza della memoria negli agenti, e questa cosa è stata dimostrata anche dall'attenzione all'uso della memoria nel codice trapelato di Claude Code. In questo caso si tratta di una memoria basata su vettori, che forse non è la cosa più flessibile di tutte quelle che ho visto, ma che è promettente per quanto sia in grado di migliorare il workflow.

Gli altri due articoli sono in qualche modo tra loro collegati. Uno è una ricerca, o meglio un framework di Microsoft, per ottimizzare gli agenti con reinforcement learning. L'altro invece è un articolo più teorico sul training loop intorno all'utilizzo dell'harness da parte dei modelli all'interno di un sistema di agenti.

### I link della settimana

- [The Model-Harness Training Loop](https://x.com/Vtrivedy10/status/2039872562662941118) — Ciclo di training per agenti basato su harness engineering, modelli open e infrastruttura accessibile.
- [Cline Kanban](https://cline.bot/blog/announcing-kanban) — App per orchestrare più agenti di codifica con visualizzazione kanban, gestione dipendenze e stato live.
- [Engram Memory System](https://weaviate.io/blog/engram-internal-use-case) — Sistema di memoria vettoriale per agenti, contesto persistente per migliorare i workflow.
- [Agent Lightning (Microsoft)](https://github.com/microsoft/agent-lightning) — Framework per ottimizzare agenti con RL, prompt optimization e fine-tuning, zero modifiche al codice.

## AI Assisted Coding

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Il leak di Claude Code conferma che il vantaggio competitivo degli agenti di coding non sta nel modello ma nell'harness: gestione della memoria, uso degli strumenti e orchestrazione dei subagent.
- **Takeaway 2:** L'approccio ibrido locale/cloud di Cursor 3 rappresenta un'alternativa architetturale interessante rispetto allo swarm di subagent via CLI.
- **Takeaway 3:** La revisione incrociata tra agenti diversi (Codex su Claude Code, [Lince.sh](https://lince.sh)) sta emergendo come pratica per migliorare la qualità del codice generato.

- **Action Items:**
  - Leggete i quattro articoli sul leak di Claude Code per estrarre pattern applicabili ai vostri agenti, in particolare su memoria e harness.
  - Guardate il diagramma di Karpathy sul suo workflow personale con agenti di coding come punto di partenza per ottimizzare il vostro.

### Cosa succede questa settimana?

Per quanto riguarda l'agentic coding, questa settimana è senza dubbio stata dominata dal leak del codice di Anthropic. Come molti di voi avranno visto, è successo che uno sviluppatore abbia pubblicato una versione di Claude che conteneva anche il codice a fini di debug, e immediatamente la rete si è scatenata. Ne abbiamo ampiamente parlato anche durante l'ultimo episodio del podcast di Risorse Artificiali, che se siete di lingua italiana vi consiglio di ascoltare.

Qui non mi voglio soffermare troppo su quelle che sono le lezioni apprese, perché sono tante e variegate. Anche se non c'è una ricetta magica, come era lecito aspettarsi se siete in questo mondo da un po' di tempo. È un insieme di buona pratica di uso dell'harness e della memoria: questo mi sento di condensare in una sola frase. Poi il codice è chiaramente cresciuto molto su se stesso, molto scritto con l'aiuto delle AI, e a tratti ha delle aree di possibile miglioramento con un buon refactoring. Ma non è questo il punto, perché Claude Code funziona molto bene grazie soprattutto a quei due aspetti che ho menzionato prima. Vi consiglio di leggere i quattro link che vi propongo, perché fanno un'analisi del codice in maniera accessibile ma sufficientemente approfondita per rendersi conto dello strumento e di come si adatti alle diverse necessità, e magari farvi venire qualche idea per i vostri agenti di coding e non.

Se state utilizzando agenti di coding, vi consiglio anche di non perdervi il tweet di Karpathy, soprattutto per il diagramma allegato che chiarisce quale sia il suo uso personale degli agenti di coding. Magari non è perfetto per il vostro use case, ma di sicuro può darvi dei consigli, come sempre Karpathy riesce a fare.

È un po' che non parliamo di Cursor, ma anche loro non stanno fermi. È uscita la versione 3 del loro IDE, riprogettato per uno sviluppo agent-driven e multi-repository. Quindi molto interessante. Integra agenti sia locali che cloud in parallelo, in un'orchestrazione ampia di tipo swarm vero e proprio. A loro va riconosciuto il coraggio e la capacità di provare soluzioni nuove, perché questo approccio ibrido locale e cloud è sicuramente diverso dall'approccio che tengono Claude Code e tutti gli altri CLI, che invece tendono a fare swarm di subagent.

Infine vi segnalo un plugin per Claude Code per utilizzare Codex all'interno del workflow di Claude. È curioso perché permette di fare una revisione di agenti incrociati e di utilizzare in parallelo due agenti diversi sullo stesso problema. Anche [Lince.sh](https://lince.sh), che è il progetto che sto sviluppando con gli altri ragazzi di Risorse Artificiali, vi permette di fare una cosa vagamente simile: utilizzare agenti multipli sullo stesso repository di codice e passare dall'uno all'altro in maniera molto veloce, il tutto stando nello stesso terminale. Se vi va, dateci un'occhiata e dateci i vostri feedback. Di [Lince.sh](https://lince.sh) parlerò sicuramente molto più diffusamente nella prossima newsletter, dopo che lo avremo lanciato ufficialmente su tutti i social, e magari gli dedicherò proprio una puntata intera di questa newsletter. Che ne dite?

### I link della settimana

- [Cursor 3](https://cursor.com/blog/cursor-3) — IDE riprogettato per sviluppo agent-driven, multi-repo, agenti locali e cloud in parallelo.
- [Inside the Claude Code source](https://gist.github.com/Haseeb-Qureshi/d0dc36844c19d26303ce09b42e7188c1) — Analisi del sorgente Claude Code: 500K righe TypeScript, architettura harness, divergenze da Codex.
- [Codex Plugin per Claude Code](https://x.com/reach_vb/status/2038670509768839458) — Plugin per integrare Codex nel workflow Claude Code, revisioni incrociate tra agenti.
- [AINews The Claude Code Source Leak](https://www.latent.space/p/ainews-the-claude-code-source-leak) — Leak del sorgente Claude Code via source map: orchestrazione, memoria, rischio sicurezza npm.
- [Practical Lessons From the Claude Code Leak](https://generativeprogrammer.com/p/practical-lessons-from-the-claude) — Lezioni architetturali dal leak: CLAUDE.md, subagenti, worktree, hook automatici.
- [Claude Code's Real Secret Sauce](https://x.com/rasbt/status/2038980345316413862) — L'harness software (Grep, Glob, LSP, subagenti) conta più del modello sottostante.
- [Karpathy su LLM e coding](https://x.com/karpathy/status/2039805659525644595) — Tweet di Karpathy con diagramma correlato sull'uso degli LLM nel coding.

## Business e societa

### I Takeaways per gli AI Engineers

- **Takeaway 1:** La corsa al compute tra OpenAI e Anthropic definirà il panorama AI del 2026-2027, con Google come terzo incomodo che ha colmato un gap enorme.
- **Takeaway 2:** L'economia della generative AI resta dominata dai semiconduttori (70% dei ricavi): chi vende le pale continua a guadagnare più di chi scava.
- **Takeaway 3:** Il burnout da orchestrazione di agenti multipli è un rischio reale e sottovalutato per gli sviluppatori, come evidenziato da Simon Willison.

- **Action Items:**
  - Leggete i due articoli economici (timelines e economics) per capire le forze di mercato che guidano le scelte tecnologiche che vi impattano quotidianamente.
  - Monitorate i vostri limiti cognitivi nell'uso di agenti multipli e adottate strumenti che riducano il context switching.

### Cosa succede questa settimana?

OpenAI raccoglie altri 122 miliardi di dollari di finanziamenti, con una valutazione monster che arriva oltre gli 800 miliardi. Nel frattempo, Anthropic, che al momento sta vincendo la sfida dei ricavi, ha raddoppiato la sua capacità di calcolo, pareggiando quasi quella di OpenAI stessa. Si preannuncia un 2026-2027 veramente serrato tra questi due competitor che stanno prendendo gran parte del mercato, senza dimenticare ovviamente Google, che ha fatto cose incredibili recuperando un gap enorme che aveva nel 2024 e diventando uno dei principali competitor allo stesso livello di questi due.

Proprio per questo motivo di grande competizione, è interessante leggere gli articoli sulla timeline update delle previsioni sull'intelligenza artificiale e anche come funziona l'economia della generative AI. Sono due articoli di tipo economico, ma che secondo me vale la pena approfondire per capire quali sono le spinte economiche che stanno dietro a questa rivoluzione industriale.

Simon Willison, in un podcast, parla di una cosa che ho spesso affrontato in queste righe e anche in italiano nel podcast Risorse Artificiali: cioè quanto nell'era degli agenti il burnout possa essere davvero un rischio per gli sviluppatori, che si trovano ad affrontare i loro limiti cognitivi nell'orchestrare agenti multipli. Come detto, con [Lince.sh](https://lince.sh) stiamo cercando di fornire uno strumento che limiti un pochino il context switching, tenendo quantomeno lo sviluppatore all'interno del terminale. Ma indubbiamente, aumentare il numero di agenti da coordinare è da un lato una necessità per aumentare la capacità di utilizzo di questi strumenti, ma dall'altro presenta dei grossi rischi. Simon è una delle penne che preferisco leggere, e si è rivelato un'ottima sorpresa anche nel podcast di Lenny.

### I link della settimana

- [Simon Willison su Lenny's Podcast](https://simonwillison.net/2026/Apr/2/lennys-podcast/) — AI state of the union: limiti cognitivi umani nell'era degli agenti, burnout, nuovi limiti personali.
- [Q1 2026 AI Timelines Update](https://blog.aifutures.org/p/q1-2026-timelines-update) — Previsioni Automated Coder anticipate a meta 2028, Claude Code a $2.5B di ricavi annualizzati.
- [Compute Wars: OpenAI vs Anthropic](https://x.com/petergostev/status/2038755953336836514) — Anthropic ha raddoppiato la capacita, quasi alla pari con OpenAI. Il 2027 sara una gara serrata.
- [OpenAI raccoglie $122B](https://openai.com/index/accelerating-the-next-phase-ai/) — $122 miliardi di nuovi finanziamenti, valutazione $852B, strategia su compute e enterprise.
- [The Economics of Generative AI](https://apoorv03.com/p/the-economics-of-generative-ai-two) — I semiconduttori catturano il 70% dei ricavi AI. La strategia piu profittevole resta vendere le pale.

