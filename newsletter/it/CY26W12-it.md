Se devo trovare un tema ricorrente all'interno di questa newsletter, ma forse anche in quelle delle ultime settimane, credo che indubbiamente il tema sia l'agentic coding e forse più in generale lo sviluppo di sistemi agentici. Ma per ora non distribuiti in rete come forse si poteva pensare all'inizio di questo sviluppo, bensì molto centrati sulla macchina dell'utente. È probabilmente una cosa che cambierà nel tempo e, come abbiamo visto tante volte, cicli e ricicli all'interno dell'informatica: spesso è successo in passato che una soluzione centralizzata andasse a finire sulle macchine dei singoli utenti per poi tornare a soluzioni distribuite.

Provate a pensarci: siamo passati dai mainframe ai personal computer per poi tornare al cloud, ma questo è solo uno dei tanti esempi che potrei fare di questa traiettoria, ed è quello che un po' sta succedendo anche nel mondo dell'AI. Siamo passati dai chatbot, centralizzati e completamente controllati dal vendor, per arrivare ai coding agent o comunque agli agenti personali (pensate non solo a Claude Code, ma anche a OpenClaw o a Claude Work), e poi forse in futuro vedremo agenti distribuiti nel cloud. Quest'ultima non è una cosa che sia ancora fatta, ma ci sono tutte le premesse perché possa succedere. Quindi tenete gli occhi aperti, continuate a leggere la newsletter e abbiate sempre un vostro pensiero critico su quello che sta succedendo. Sporcatevi le mani provando un po' delle cose che vi propongo e fate di tutto per saltare su questo treno in folle corsa.

Prima di lasciarvi alla lettura delle notizie e delle mie analisi di cosa è successo in settimana, fatemi dire cosa è successo, sta per succedere o succederà nella mia agenda pubblica, per chi volesse seguire i miei interventi o volesse incontrarmi di persona (adoro scambiare opinioni con chiunque abbia voglia di farlo):

* [Podcast](https://risorseartificiali.com) con Alessio e Paolo:
  * Mercoledì è uscita la mia intervista a Massimo Re Ferré, PM di AWS Kiro.
  * Stiamo lavorando ad altre interviste e puntate con ospiti molto interessanti.
  * Ormai sapete del nostro repository su GitHub con tool e configurazioni per fare AI coding da terminale su Linux. Questa settimana abbiamo rilasciato una dashboard completa... quasi un IDE per agenti, ma tutto da terminale: [LINCE - Linux Intelligent Native Coding Environment](https://github.com/RisorseArtificiali/lince)
* Da solo:
  * Il 24 marzo sarò al Voxxed Day a Zurigo. Io e Alessio [presentiamo un talk sull'AI assisted coding](https://vdz26.voxxeddays.ch/talk/?id=8057)
  * Il 25 marzo sarò speaker in questo meetup a Milano sul [Vibe Coding e Agentic Engineering](https://www.eventbrite.it/e/biglietti-meetup-13-vibe-coding-1983538213191?aff=ebdssbcategorybrowse)
  * Il 30 maggio avrò l'onore di essere uno dei [PyCon Italia speakers](https://2026.pycon.it/en/speakers)
  * Il 12 giugno sarò a Catania come speaker al [Coderful](https://www.coderful.io/)

## Novità e ricerca nei modelli AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Il contesto da 1M di token di Anthropic cambia qualitativamente il lavoro con gli agenti di coding, eliminando il collo di bottiglia della gestione del contesto
- **Takeaway 2:** I vendor cinesi convergono su modelli ottimizzati per scenari agentici (MiniMax M2.7, GLM-5-Turbo): l'agentic AI è il campo di battaglia competitivo del momento
- **Takeaway 3:** Se DeepMind sta costruendo metriche per l'AGI, è perché la distanza percepita si sta riducendo concretamente

- **Action Items:**
  - Provate Claude Code con il contesto da 1M su un task complesso multi-file
  - Leggete il paper di DeepMind sul framework cognitivo per l'AGI per calibrare le aspettative su dove siamo realmente

### Cosa succede questa settimana?

Partiamo da una novità rilevante che viene da Anthropic, che ha portato la lunghezza del contesto sia del modello Opus che del modello Sonnet a un milione di token. Avere un milione di token cambia molto l'esperienza di utilizzo di Claude Code, specialmente perché vi permette di fare operazioni molto lunghe e molto complesse senza la necessità di ripulire il contesto o di tenere traccia in modo alternativo di queste operazioni. È sicuramente una funzionalità da provare.

Di sicuro anche i vendor cinesi di modelli non stanno a guardare. MiniMax lancia il suo modello M2.7, che ha ottimi risultati nei benchmark soprattutto per la funzione agentica. Lo stesso si dica per GLM-5-Turbo, a sua volta ottimizzato per scenari agentici. Entrambi i modelli sono consigliati per essere utilizzati con OpenClaw, che è, o almeno sembra, il vero punto di riferimento in questo momento per i modelli cinesi. Nell'utilizzo pratico per quanto riguarda il coding, avevo detto nelle settimane scorse che l'esperienza con Claude è comunque superiore. Ma devo ammettere che anch'io uso uno di questi modelli.

Molto interessanti invece le notizie che vengono dalla ricerca, a partire dai World Model che fanno progredire sempre di più l'AI simulando la complessità del mondo reale. Ma anche un'interessante ricerca di DeepSeek per usare un indice all'interno dell'attenzione, catturando meglio il senso semantico della frase che sta trattando.

Ultimo ma non ultimo, in ambito di ricerca, un framework cognitivo rilasciato da Google DeepMind per misurare il progresso verso l'AGI. Al di là del paper, che è molto interessante da leggere e vi consiglio, mi piace rimarcare il fatto che se DeepMind, con la visibilità che ha sull'evoluzione dei modelli, sta disegnando un framework per misurare il progresso verso l'AGI, è perché ci stiamo avvicinando sempre di più a quel punto.

### I link della settimana

- [1M di contesto ora disponibile per Opus 4.6 e Sonnet 4.6](https://claude.com/blog/1m-context-ga) — Finestra di contesto da 1M di token a prezzo standard per Claude Opus 4.6 e Sonnet 4.6, incluso Claude Code
- [World Models: Calcolare l'Incalcolabile](https://www.notboring.co/p/world-models) — I World Model simulano la complessità del mondo reale per abilitare previsioni e pianificazione tramite reti neurali
- [Misurare il progresso verso l'AGI: un framework cognitivo](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/) — Google DeepMind propone una tassonomia cognitiva con 10 abilità chiave per misurare il progresso verso l'AGI
- [MiniMax lancia il modello M2.7](https://www.testingcatalog.com/minimax-launches-m2-7-model-on-minimax-agent-and-apis/) — Modello M2.7 disponibile via API con capacità di debugging autonomo e harness per agenti di ricerca
- [GLM-5-Turbo](https://docs.z.ai/guides/llm/glm-5-turbo) — Modello fondazionale di Z.ai ottimizzato per scenari agentici con contesto da 200K e supporto MCP
- [Attenzione Sparsa più Veloce con IndexCache](https://github.com/THUDM/IndexCache) — Patch per SGLang e vLLM che elimina fino al 75% dei calcoli nell'attenzione sparsa di DeepSeek

## Agentic AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** OpenAI sta costruendo un ecosistema completo per il coding agentico: modello (GPT 5.4), monitoraggio della sicurezza e subagent in un'unica strategia coordinata
- **Takeaway 2:** I subagent sono ormai un pattern consolidato cross-piattaforma (Claude Code, Codex): chi non li usa sta lasciando performance sul tavolo
- **Takeaway 3:** Il context engineering è la disciplina chiave per far funzionare bene i sistemi agentici, e l'articolo di SwirlAI ne mappa i cinque pattern fondamentali

- **Action Items:**
  - Leggete l'articolo "State of Context Engineering in 2026" come guida pratica per ottimizzare il contesto nei vostri agenti
  - Provate i subagent in Codex o Claude Code per sperimentare il pattern di delega agentica su un task reale

### Cosa succede questa settimana?

OpenAI dimostra di avere sviluppato grandi interessi per il coding e si pone come seria alternativa, secondo qualcuno anche migliore, a Claude Code. Questa settimana vi invito a porre la vostra attenzione sui tre articoli che riporto da parte di OpenAI, perché sono tutti e tre significativi in questa strategia.

GPT 5.4 è stato un grande passo avanti soprattutto nella sua usabilità agentica all'interno di Codex ed è il primo modello e agente, insieme a Codex, da parte di OpenAI che sembra davvero in grado di gestire una grande varietà di task, sia di codice che non. Inoltre OpenAI ha rilasciato un sistema di monitoraggio per gli agenti di coding autonomi, progettato per rilevare i rischi di disallineamento e studiarne il comportamento, che sottolinea ancora di più il loro interesse per questo mercato. Lo stesso si dica del fatto che Codex da questa settimana supporta i subagent, un pattern largamente usato nel mondo Anthropic e non solo, che permette di lanciare agenti secondari autonomi gestiti dall'agente principale risparmiando il contesto e ottimizzando il lavoro.

Allontanandoci dal mondo di OpenAI, segnalo in questo settore OpenShell, un runtime sicuro fatto da NVIDIA per far girare agenti autonomi. Sostanzialmente si tratta di una soluzione basata su Kubernetes con delle policy dichiarative scritte in YAML. Davvero una soluzione avanzata che va ben al di là, probabilmente, della sola scrittura di codice.

Da ultimo vi segnalo un interessantissimo articolo riguardo al contesto, che si chiama "State of Context Engineering", che contiene davvero quattro o cinque spunti molto interessanti. Secondo me è un must read in questo periodo per capire a fondo come gestire efficacemente il contesto nei vostri sistemi agentici. Si va dalle skill e la loro progressive disclosure alla compressione del contesto, al routing intelligente, ma anche a discorsi relativi a RAG o agli strumenti esterni come tool o MCP server.

### I link della settimana

- [GPT 5.4 è un grande passo avanti per Codex](https://www.interconnects.ai/p/gpt-54-is-a-big-step-for-codex) — Primo agente OpenAI con vera usabilità agentica, istruzioni precise e capacità di gestire task diversificati
- [Monitoraggio degli Agenti di Coding Autonomi](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/) — Sistema di monitoraggio OpenAI per rilevare rischi di disallineamento negli agenti di coding interni
- [Subagent e agenti personalizzati in Codex](https://simonwillison.net/2026/Mar/16/codex-subagents/) — Codex rilascia i subagent in GA con supporto per agenti custom definiti tramite file TOML
- [OpenShell](https://github.com/NVIDIA/OpenShell) — Runtime sicuro NVIDIA per agenti autonomi con sandbox e policy YAML dichiarative su Kubernetes
- [Stato del Context Engineering nel 2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026) — Cinque pattern chiave per gestire il contesto: progressive disclosure, compressione, routing, RAG e MCP

## AI Assisted Coding

### I Takeaways per gli AI Engineers

- **Takeaway 1:** OpenAI acquisisce Astral (uv, Ruff, ty) e promette di mantenerli open source: la parola "open" nel nome potrebbe finalmente avere senso almeno per gli strumenti
- **Takeaway 2:** Le skill sono il punto di estensione più ad alto impatto per i coding agent: chi non le usa sta sottoutilizzando il proprio agente
- **Takeaway 3:** Il mercato dei coding agent si frammenta con alternative serie (Cursor Composer 2, Codex) che sfidano Claude Code su prezzo e performance

- **Action Items:**
  - Leggete l'articolo di Anthropic sulle skill e cominciate ad aggiungerne ai vostri coding agent
  - Provate LINCE Dashboard per gestire agenti multipli in parallelo dal terminale

### Cosa succede questa settimana?

L'acquisizione di Astral da parte di OpenAI la dice veramente lunga su quanto OpenAI abbia sviluppato interesse per il mercato del coding. Per chi non conoscesse, Astral è l'azienda dietro a tre dei principali strumenti di sviluppo open source per Python. Mi riferisco a uv, Ruff e ty, che entrano a far parte dell'ecosistema di Codex. Così come aveva fatto per OpenClaw, OpenAI promette di mantenere i progetti completamente open source, che se confermato darebbe un senso alla parola "open" all'interno del loro nome, visto che con i modelli hanno una politica completamente diversa.

Cursor invece, che sembrava essere un po' dimenticato, rilascia il primo suo modello di coding veramente di frontiera. Composer 2, a un prezzo piuttosto basso, ha dei sostanziali miglioramenti di performance che secondo il vendor supererebbero addirittura quelle di Claude.

Da casa Google viene annunciato un nuovo strumento di design chiamato Stitch, che avevamo già visto in realtà affacciarsi nel Google Labs, e che trasformerà il modo di lavorare e di collaborare con l'AI nell'ambiente 3D e 2D, con la capacità di generare applicazioni React funzionali a partire dal solo design, quindi non dal codice ma dal design dell'applicazione stessa.

Uno degli sviluppatori interni di Anthropic ha scritto un bellissimo articolo su come vengono usate le skill internamente in casa Anthropic e come sono state sviluppate. Vi consiglio fortemente la lettura di questo articolo se state aggiungendo skill ai vostri arnesi per il vostro coding agent. E se non lo state facendo, dovreste. Quindi leggete quell'articolo, imparate come fare e cominciate a valutare l'aggiunta di skill tra le cose che usate per migliorare l'esperienza di coding con i coding agent.

Infine una segnalazione che viene dal fronte personale. Insieme agli altri ragazzi di Risorse Artificiali, questa settimana abbiamo reso disponibile su GitHub uno strumento per utilizzare agenti multipli in maniera efficiente ed efficace all'interno del terminale Linux. LINCE Dashboard ha il supporto per la persistenza delle sessioni e anche la capacità di input vocale. Nel frattempo Anthropic ha reso disponibile l'input vocale anche su Linux, ma credetemi, il nostro funziona molto meglio. LINCE Dashboard si configura come un ambiente unico dove potete utilizzare molteplici agenti anche su directory diverse e quindi progetti diversi in parallelo, senza perdervi mai la richiesta di input da parte di uno di questi mentre lavorate in parallelo con altro. Inoltre ogni agente viene sandboxato per garantire sicurezza sul vostro sistema, che non mi stancherò mai di ripetere è una delle cose fondamentali quando usate un agente di coding o non di coding.

### I link della settimana

- [Lezioni dalla Costruzione di Claude Code: Come Usiamo le Skill](https://x.com/trq212/status/2033949937936085378) — Come Anthropic usa le skill internamente: cartelle funzionali, progressive disclosure e sezioni "Gotchas" ad alto impatto
- [Cursor Composer 2](https://cursor.com/blog/composer-2) — Modello di coding frontier a prezzo competitivo con miglioramenti sostanziali su CursorBench e SWE-bench
- [OpenAI acquisisce Astral](https://openai.com/index/openai-to-acquire-astral/) — uv, Ruff e ty entrano nell'ecosistema Codex; OpenAI promette di mantenerli open source
- [Anteprima del nuovo strumento di design di Google](https://www.testingcatalog.com/exclusive-early-look-at-upcoming-vibe-design-tool-from-google/) — Stitch: spazio di lavoro 3D con AI che genera applicazioni React funzionali dai design
- [LINCE Dashboard](https://github.com/RisorseArtificiali/lince/tree/main/lince-dashboard) — Plugin Zellij per gestire multiple istanze Claude Code con persistenza sessioni e input vocale

## Business e società

### I Takeaways per gli AI Engineers

- **Takeaway 1:** OpenAI punta all'IPO trasformando ChatGPT in strumento di produttività enterprise: il passaggio da novità consumer a revenue sostenibile è il vero segnale
- **Takeaway 2:** La Cina sta democratizzando l'AI con programmi di adozione di massa che non hanno equivalenti in Occidente
- **Takeaway 3:** L'open source nell'era dell'AI ha bisogno di nuovi framework di mentorship per gestire il rumore dei contributi generati automaticamente

- **Action Items:**
  - Formate la vostra opinione leggendo i quattro link e condividetela nei commenti
  - Valutate come il framework delle "3 C" può applicarsi ai vostri progetti open source che ricevono contributi AI

### Cosa succede questa settimana?

In questa sezione vi invito a leggere i quattro link che vi propongo senza darvi troppo la mia lettura, perché credo sia importante che abbiate una vostra opinione e un vostro spirito critico sui link che propongo. Sono felice di discutere di eventuali opinioni nei commenti, ma credo che i quattro link, pur non essendo da prima pagina, siano molto significativi per capire in che direzione sta andando il mondo dell'AI, tra Stati Uniti e Cina a fare da padroni dei trend che condizionano il mercato.

### I link della settimana

- [OpenAI si prepara all'IPO entro fine anno](https://www.cnbc.com/2026/03/17/openai-preps-for-ipo-in-2026-says-chatgpt-must-be-productivity-tool.html) — OpenAI punta alla quotazione in borsa entro il 2026, ChatGPT deve diventare strumento di produttività enterprise
- [Come la Cina sta portando tutti su OpenClaw](https://www.cnbc.com/2026/03/18/china-openclaw-baidu-tencent-ai.html) — Baidu e Tencent promuovono OpenClaw con campagne di adozione di massa su tutte le fasce demografiche
- [Ripensare il mentorship open source nell'era dell'AI](https://github.blog/open-source/maintainers/rethinking-open-source-mentorship-in-the-ai-era/) — Il framework delle "3 C" per fare mentorship strategico contro il rumore dei contributi generati dall'AI
- [Personal Intelligence di Google si espande a tutti gli utenti USA](https://techcrunch.com/2026/03/17/googles-personal-intelligence-feature-is-expanding-to-all-us-users/) — L'assistente Google accede a Gmail e Photos per risposte personalizzate, ora disponibile per tutti
