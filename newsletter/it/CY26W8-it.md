# CY26W8

Questa settimana voglio partire con quello che osservo ultimamente sui social. Stigmatizzarlo, probabilmente non mi farà nuovi amici, ma credo che quello che sta succedendo nel mondo degli ingegneri del software (ed affini) sia abbastanza evidente. C'è stata una prima fase, che collocherei fino a Natale circa, in cui la maggioranza degli "addetti ai lavori" del software postava cose tipo: "L'AI non può sostituire un buon ingegnere, fa troppi errori", "Fatemi vedere qualcosa che non sia un esempio in una PR", "Ma per favore, l'AI può scrivere solo boilerplate code". Insomma la negazione pura. Ora siamo invece in una seconda fase con post di questo tono: "Ma se l'AI ci dà più velocità mi spiegate perché io lavoro il doppio", "L'AI non ci toglie il lavoro, anzi ce lo incasina di più", "Bisogna diventare tutti architetti del software, dovevamo lavorare di meno e invece ci chiedono ancora di più". Ecco, date un'occhiata alla ben nota curva di accettazione del cambiamento di Kübler-Ross che riporto qui sotto... e preparatevi alla fase di depressione...

Prima di lasciarvi alla lettura delle notizie e delle mie analisi di cosa è successo in settimana, fatemi dire cosa è successo, sta per succedere o succederà nella mia agenda pubblica, per chi volesse seguire i miei interventi o volesse incontrarmi di persona (adoro scambiare opinioni con chiunque abbia voglia di farlo):

* [Podcast](https://risorseartificiali.com) con Alessio e Paolo:
  * Mercoledì è uscita una intervista con [Daniele Zonca](https://www.linkedin.com/in/daniele-zonca-9867807/) su AI nel mondo enterprise
  * Sabato è venuto a trovarci un vecchio amico, [Antonello Mantuano](https://www.linkedin.com/in/antonellomantuano/), per un'interessante chiacchierata
  * Il 12 Marzo saremo al JUG di Milano per registrare la nostra prima puntata live. [Non mancate](https://www.eventbrite.com/e/risorse-artificiali-appunti-e-spunti-dal-mondo-dellai-tickets-1983617212480?aff=oddtdtcreator)
  * Stiamo lavorando ad altre interviste e puntate con ospiti molto interessanti
* Da solo
  * Mi hanno intervistato di nuovo al podcast opensource. Stavolta parlo di agenti, AI, AGI. [Esce qui il 26](https://open.spotify.com/show/3EAhXkBUmHE1a8vFTH84Yg?si=bacd744b0f9c4a55). Ascoltatela e fatemi avere vostri commenti
  * Il 26 Febbraio sarò a [questo evento a Milano](https://www.eventbrite.it/e/biglietti-meetup-12-rag-night-1981586932859?aff=oddtdtcreator) (come uditore, ma volentieri scambio opinioni). E al di là di me l'evento vale la pena di essere seguito
  * Il 24 Marzo sarò al Voxxed Day a Zurigo. Io e Alessio [presentiamo un talk sull'AI assisted coding](https://vdz26.voxxeddays.ch/talk/?id=8057)
  * Il 30 Maggio avrò l'onore di essere uno dei PyCon Italia [speakers](https://2026.pycon.it/en/speakers)

## 🤖 Novità e ricerca nei modelli AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Sonnet 4.6 costa meno per token di Opus 4.5 ma ne usa ~2.5x di più: i modelli più piccoli compensano con più reasoning, e il confronto prezzo/prestazioni reale è meno lineare di quanto sembri.
- **Takeaway 2:** L'ingresso di Google con Lyria 3 nella musica generativa conferma che questo mercato è già concreto e in fase di consolidamento, dopo Suno e altri pionieri.
- **Takeaway 3:** La competizione sui modelli è globale e multimodale: Gemini 3.1 Pro (reasoning), Qwen 3.5 (visione, 201 lingue), PersonaPlex (voce real-time) — la frontiera avanza su più assi contemporaneamente.

- **Action Items:**
  - Confronta il TCO reale di Sonnet 4.6 vs Opus 4.5 nei tuoi use case, considerando il consumo totale di token.
  - Sperimenta PersonaPlex per l'interazione vocale con agenti di coding su Linux/open source.

### Cosa succede questa settimana?

Altro nuovo modello nella famiglia Gemini di Google: con Lyria 3 Big Blue si mette anche nel mercato della musica generata da AI, e lo fa come sempre in grande stile e con grande potenza. Ed è un mercato tutt'altro che secondario che già dai primi accordi di Suno e altre piattaforme sta muovendo un sacco di soldi, come probabilmente succederà anche alle produzioni video, ma quello della musica generata è già realtà ora.

Ma in casa Gemini il rilascio più rilevante è Gemini Pro 3.1, che non va confuso con Gemini 3.0 Deep Think della scorsa settimana: si tratta di una versione nuova del modello per tutti gli abbonati. E migliora sensibilmente i risultati in tutti i benchmark, su tutti un valore raddoppiato su ARC-AGI-2.

Anche Anthropic annuncia un rilascio importante con Sonnet 4.6 che nei benchmark e nei report interni di Anthropic pareggia, o quasi, Opus 4.5 a un prezzo per token molto più basso. Ma per farlo usa molti più token (stima 2.5x), quindi da un lato il costo totale è sì più basso di Opus 4.5 ma non incredibilmente più basso, dall'altro suggerisce che modelli SOTA più piccoli raggiungono performance più alte con più reasoning. Non inaspettato, ma interessante conferma indiretta.

Anche i cinesi sono tutt'altro che fermi, con Qwen che pubblica la versione 3.5 del loro modello di punta. Nativamente multimodale, con un'architettura ibrida interessante e il supporto a ben 201 lingue. Interessante anche l'arrivo sul mercato AI di DuckDuckGo con la loro politica di privacy portata anche sulla generazione di immagini.

Segnalo anche con grande interesse il modello conversazionale speech-to-speech di NVIDIA. Ci spenderò qualche ora prossimamente per capire se può aiutare a portare la modalità di interazione vocale con gli agenti (di coding e non) nel mondo open source (in particolare Linux), che tanto mi è caro.

### I link della settimana

- [Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/) — Google rilascia Gemini 3.1 Pro con punteggio raddoppiato su ARC-AGI-2, avanzamento significativo nel reasoning astratto.
- [DuckDuckGo AI Image Editing](https://9to5mac.com/2026/02/19/duckduckgo-rolls-out-ai-powered-image-editing-on-duck-ai/) — Editing immagini AI privacy-first su Duck.ai, senza account e senza memorizzazione dei dati.
- [Gemini Lyria 3](https://blog.google/innovation-and-ai/products/gemini-app/lyria-3/) — Generazione musicale AI integrata nell'app Gemini: brani di 30 secondi da testo o immagini.
- [Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) — Anthropic rilascia Sonnet 4.6 con context window da 1M token, preferito a Opus 4.5 nel 59% dei casi.
- [Qwen3.5](https://qwen.ai/blog?id=qwen3.5) — Vision-language model con 397B parametri (17B attivi), architettura ibrida e supporto a 201 lingue.
- [PersonaPlex](https://huggingface.co/nvidia/personaplex-7b-v1) — Modello NVIDIA speech-to-speech real-time full-duplex per conversazioni vocali interattive.

## 🕸️ Agentic AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** La sicurezza degli agenti AI è un problema architetturale, non risolvibile con soli prompt-based safeguard: servono sandboxing, permessi granulari e logging dedicato.
- **Takeaway 2:** L'harness engineering emerge come evoluzione di prompt e context engineering: cambiare dati, tool, MCP e skill può avere più impatto sulla performance degli agenti che cambiare il modello stesso.
- **Takeaway 3:** L'autonomia degli agenti cresce costantemente e gli utenti esperti passano dall'approvare singole azioni al monitoraggio strategico — un cambio di paradigma nell'interazione umano-agente.

- **Action Items:**
  - Rivedi l'architettura di sicurezza dei tuoi agenti: verifica sandboxing, scope dei permessi e logging delle azioni autonome.
  - Sperimenta con l'harness engineering: modifica tool, dati e context dei tuoi agenti prima di cambiare modello per migliorare i risultati.

### Cosa succede questa settimana?

Partiamo da qualcosa di cui abbiamo parlato settimana scorsa. Il creatore di OpenClaw alla fine ha deciso di joinare OpenAI. Sono certo che con il sostegno della società saprà portare altre idee di rottura in questo giovane mercato. Mi auguro fortemente che il suo lavoro possa continuare anche in community perché uno degli aspetti più interessanti di OpenClaw è stato di riportare l'Open Source al centro del dibattito.

Due i temi principali che voglio mettere in evidenza con i link che riporto in questa sezione. Il primo riguarda una crescente attenzione alla sicurezza degli agenti, con problemi architetturali da affrontare e le buone pratiche da spiegare e inculcare a sviluppatori ed utenti. La sicurezza è sempre stata un tema tanto centrale quanto trascurato, e con l'AI generativa diventa ancora più importante capire i rischi e come mitigarli.

Il secondo tema è quello della misurazione dei risultati e dell'autonomia degli agenti, dai benchmark di OpenAI e Anthropic fino a chi mostra come cambiare harness (cioè tutto quello con cui si estende un LLM: dati, tool, MCP, skill, ecc.) possa cambiare i risultati degli agenti. Tenete a mente la parola harness, perché sempre più spesso si parla di harness engineering, come evoluzione di context engineering e di prompt engineering.

### I link della settimana

- [Sandbox sicuro per agenti locali](https://cursor.com/blog/agent-sandboxing) — Cursor riduce le interruzioni degli agenti del 40% con sandboxing nativo per piattaforma (Seatbelt, Landlock, WSL2).
- [Harness Engineering per Deep Agents](https://x.com/Vtrivedy10/status/2023805578561060992) — L'agente LangChain passa dalla Top 30 alla Top 5 su Terminal Bench 2.0 con un solo cambio di harness.
- [EVMbench](https://openai.com/index/introducing-evmbench/) — Benchmark OpenAI per valutare agenti AI su vulnerabilità smart contract, uso difensivo e offensivo.
- [OpenClaw creator joins OpenAI](https://steipete.me/posts/2026/openclaw) — Il creatore di OpenClaw entra in OpenAI; il progetto resta open e indipendente in una nuova fondazione.
- [The problem isn't OpenClaw. It's the architecture.](https://www.vulnu.com/p/the-problem-isnt-openclaw-its-the-architecture) — Le vulnerabilità di OpenClaw rivelano rischi strutturali negli ecosistemi agenti: servono sandboxing e permessi ristretti.
- [Measuring AI Agent Autonomy](https://www.anthropic.com/research/measuring-agent-autonomy) — Anthropic analizza milioni di interazioni umano-agente: autonomia crescente, utenti verso monitoraggio strategico.

## 💻 AI Assisted Coding

### I Takeaways per gli AI Engineers

- **Takeaway 1:** L'open source nell'era degli agenti AI si trasforma: il valore non è più solo nel codice scritto, ma nella capacità di tradurre idee in software — e l'AI amplifica questa capacità.
- **Takeaway 2:** La configurazione degli agenti di coding (CLAUDE.md, skill, workflow) diventa una competenza chiave: file ben strutturati e il principio "less is more" fanno la differenza nella qualità dell'output.

- **Action Items:**
  - Rivedi e ottimizza il tuo CLAUDE.md (o AGENT.md) seguendo il principio "less is more": meno istruzioni, più mirate.
  - Esplora la guida ufficiale Anthropic sulle skill per creare workflow riutilizzabili nei tuoi agenti di coding.

### Cosa succede questa settimana?

Partiamo da un articolo di uno dei fondatori di Hugging Face su come cambia l'open source nell'era dell'agentic engineering. E cambia da tanti punti di vista che vale la pena esplorare nell'articolo. Io vi lascio solo una mia riflessione che ho riportato anche su [X](https://x.com/maeste) riguardo a quanto l'ego degli sviluppatori potesse contare in passato. Ma d'altra parte penso che gli sviluppatori open (ed il loro ego) si manifesti più nel mettere in codice delle idee, a volte geniali, ed in questo l'AI non può che aiutare a farlo.

Altri articoli di rilievo per chi fa AI Engineering questa settimana vengono da Anthropic con la loro guida per creare skill (articolo non nuovo nuovo, ma credo di non averlo mai segnalato) ed un interessante articolo su come scrivere meglio i vostri CLAUDE.md (o AGENT.md).

Date un'occhiata anche agli altri articoli, specie se volete usare al meglio la vostra subscription a OpenRouter o sperimentare con database vettoriali di nuova generazione.

### I link della settimana

- [Come cambia l'open source nell'era dell'agentic coding](https://x.com/maeste/status/2023688349484044659) — Riflessione sulla trasformazione dell'open source quando gli agenti AI contribuiscono autonomamente al codice.
- [ZVEC](https://github.com/alibaba/zvec) — Database vettoriale in-process di Alibaba, leggero e veloce, per ricerche di similarità senza dipendenze esterne.
- [Free Models Router](https://openrouter.ai/openrouter/free) — Meta-router OpenRouter che seleziona casualmente tra modelli gratuiti, utile per prototipazione e testing.
- [Complete Guide to Building Skills for Claude](https://claude.com/blog/complete-guide-to-building-skills-for-claude) — Guida ufficiale Anthropic alla creazione di skill riutilizzabili per agenti Claude, pattern "tiny CLI".
- [CLAUDE.md Masterclass](https://newsletter.claudecodemasterclass.com/p/claudemd-masterclass-from-start-to) — Guida completa su come ottimizzare i file CLAUDE.md per Claude Code, principio "less is more".

## 🏢 Business e società

### I Takeaways per gli AI Engineers

- **Takeaway 1:** L'AI come esoscheletro non solo potenzia, ma abilita lavori prima impensabili — la metafora va oltre il semplice amplificatore e ridefinisce cosa è possibile fare.
- **Takeaway 2:** GPT-5.2 che deriva un risultato originale in fisica teorica è un segnale concreto: l'AI sta già generando nuova conoscenza scientifica, indipendentemente dai tempi dell'AGI.
- **Takeaway 3:** Scegliere l'AI oggi non è più scegliere un modello: il framework di Mollick (Modelli, App, Harness) aiuta a navigare un ecosistema sempre più stratificato.

- **Action Items:**
  - Leggi l'articolo di Mollick e valuta quale layer (Modelli, App, Harness) ha più impatto sul tuo workflow attuale.
  - Rifletti su come l'AI stia trasformando il tuo lavoro: stai solo potenziando task esistenti o stai abilitando attività prima impensabili?

### Cosa succede questa settimana?

Dopo la presa di posizione forte di settimana scorsa sull'AGI, sui suoi tempi e i suoi impatti, in questa sezione ho volutamente cercato di portare spunti diversi e di riflessione su quelli che possono essere punti di vista opposti. Quindi qui troverete link su passi avanti significativi nell'uso dell'AI per la ricerca scientifica (fisica teorica), ma anche chi teorizza che l'AGI sia lontana. Il punto di vista che io preferisco è quello di chi la paragona a un esoscheletro, un modo di potenziare chi la usa, anche se pure su questo ci sarebbe bisogno di distinguere molto bene che cosa si intenda per non essere fraintesi. La mia visione è proprio quella dell'esoscheletro che non solo potenzia, ma abilita lavori prima impensabili o trasforma completamente la percezione di chi lo usa.

Interessante anche l'articolo di Ethan Mollick per aiutare a scegliere gli strumenti in questo momento così trasformativo.

### I link della settimana

- [A Guide to Which AI to Use in the Agentic Era](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the) — Ethan Mollick propone un framework a 3 layer (Modelli, App, Harness) per orientarsi nella scelta degli strumenti AI.
- [Why I don't think AGI is imminent](https://dlants.me/agi-not-imminent.html) — I Transformer attuali hanno limitazioni architetturali fondamentali; l'AGI richiederà probabilmente approcci radicalmente diversi.
- [GPT-5.2 Deriva un Nuovo Risultato in Fisica Teorica](https://openai.com/index/new-result-theoretical-physics/) — GPT-5.2 Pro propone una nuova formula per lo scattering dei gluoni, verificata da fisici di IAS, Harvard e Cambridge.
- [Stop Thinking of AI as a Coworker. It's an Exoskeleton](https://www.kasava.dev/blog/ai-as-exoskeleton) — L'AI come amplificatore delle capacità umane, non sostituzione: il modello esoscheletro è più realistico e produttivo.
- [ByteDance Building Out AI Team in US](https://www.bloomberg.com/news/articles/2026-02-19/bytedance-building-out-artificial-intelligence-team-in-us) — ByteDance assume quasi 100 dipendenti per la divisione AI negli USA, tra ricerca e generazione contenuti.
