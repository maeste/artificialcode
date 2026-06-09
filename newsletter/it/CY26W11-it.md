La solita settimana intensa tra Meta, che rimanda ulteriormente il rilascio dei nuovi modelli LLM, mentre acquisisce Moltbook, certificando di fatto che stiamo andando verso un'economia basata sugli agenti. Anche il professor Ethan Mollick, che tante volte ho citato in questa newsletter e che stimo molto, scrive di come il mondo dell'AI stia già passando da quella che lui chiama co-intelligence a un modello in cui gli esseri umani utilizzano la propria intelligenza per orchestrare agenti multipli che fanno il grosso del lavoro. È un cambio significativo e in un certo senso epocale, soprattutto scritto da chi ha sempre teorizzato fortemente il concetto di co-intelligence.

Ma ci sono tante altre notizie e tanti altri nuovi tool di cui parliamo in questa newsletter, oltre al fatto che ho reinserito per questo numero una sezione in cui discuto i principali paper di ricerca relativi ai trend che ho sottolineato prima. È un'altra cosa che ho pensato nelle ultime settimane, ovvero la memoria persistente, le skill, lo sviluppo degli harness e come si guardi agli agenti come entità su cui fare reinforcement learning, al di là del modello singolo che utilizzano, ma come entità dispositive.

Prima di lasciarvi alla lettura delle notizie e delle mie analisi di cosa è successo in settimana, fatemi dire cosa è successo, sta per succedere o succederà nella mia agenda pubblica, per chi volesse seguire i miei interventi o volesse incontrarmi di persona (adoro scambiare opinioni con chiunque abbia voglia di farlo):

* [Podcast](https://risorseartificiali.com) con Alessio e Paolo:
  * Il 12 marzo siamo stati al JUG di Milano per registrare la nostra prima puntata live.
  * Stiamo lavorando ad altre interviste e puntate con ospiti molto interessanti
  * Abbiamo creato un repository su GitHub con tools e configurazioni per fare AI coding da terminale su Linux. Ovviamente open source, quindi dateci un'occhiata e contribuite: [LINCE - Linux Intelligent Native Coding Environment](https://github.com/RisorseArtificiali/lince)
* Da solo:
  * Il 19 marzo sarò all'[AI aperitivo](https://luma.com/lwn6x7b2?tk=yQaOfJ), non so ancora se facendo una demo di Lince... ma in ogni caso ne possiamo parlare :)
  * Il 24 marzo sarò al Voxxed Day a Zurigo. Io e Alessio [presentiamo un talk sull'AI assisted coding](https://vdz26.voxxeddays.ch/talk/?id=8057)
  * Il 25 marzo sarò speaker in questo meetup a Milano sul [Vibe Coding e Agentic Engineering](https://www.eventbrite.it/e/biglietti-meetup-13-vibe-coding-1983538213191?aff=ebdssbcategorybrowse)
  * Il 30 maggio avrò l'onore di essere uno dei PyCon Italia [speakers](https://2026.pycon.it/en/speakers)

## Novità e ricerca nei modelli AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Il valore competitivo si sposta dal modello al prodotto integrato.
- **Takeaway 2:** Meta conferma le difficoltà post-Llama 4: il ritardo di Avocado segnala un gap crescente.
- **Takeaway 3:** La generazione di codice evolve verso la generazione di prodotti completi.

- **Action Items:**
  - Valuta quanto i tuoi workflow dipendono da modelli isolati vs. prodotti integrati.
  - Esplora le nuove integrazioni di Gemini in Google Workspace e Maps per capire il livello di maturità raggiunto.

### Cosa succede questa settimana?

Nelle novità in tema di modelli di questa settimana (o meglio, più che di modelli, di prodotti) mi concentro su aspetti leggermente diversi da quelli in cui pongo normalmente la mia attenzione. In genere guardo molto le novità sui modelli, mentre questa settimana l'unica novità è piuttosto negativa: Meta ritarda ulteriormente il lancio dei nuovi modelli Avocado e in generale di quelli che di fatto sono i Llama 5. Questo rilascio è ritardato almeno fino a maggio, e quello che trapela sono problemi di performance e di accuratezza. Davvero Meta non sta facendo una bella figura sul mercato da Llama 4 in avanti.

Le altre novità invece si focalizzano su quella che è una tendenza piuttosto forte: il passaggio da sistemi isolati a sistemi molto più integrati, in cui i modelli collaborano direttamente con i prodotti. In questo senso sono da notare le novità in casa Google, sia per quanto riguarda Maps che per quanto riguarda gli aggiornamenti a Workspace, in cui i modelli Gemini si integrano fortemente con i prodotti di Google.

Ultimo ma non ultimo, la citazione di Replit Agent 4, che cito qui e non nella sezione AI Assisted Coding perché credo che sia significativo come il passaggio sia dalla generazione di codice puro alla generazione di un'intera suite di prodotti in maniera collaborativa.

### I link della settimana

- [Come stiamo ripensando Maps con Gemini](https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/) — Ask Maps di Google usa Gemini per risposte personalizzate e raccomandazioni in tempo reale sulle destinazioni.
- [Claude ora crea grafici, diagrammi e visualizzazioni interattive](https://claude.com/blog/claude-builds-visuals) — Imagine with Claude genera e modifica grafici, diagrammi e visualizzazioni interattive direttamente nella conversazione.
- [Meta ritarda il rilascio del nuovo modello AI per problemi di performance](https://www.bloomberg.com/news/articles/2026-03-11/meta-delays-new-ai-model-rollout-after-performance-concerns) — Il modello Avocado di Meta non compete con i leader; rilascio posticipato almeno a maggio per problemi di performance.
- [Aggiornamenti Gemini Workspace](https://blog.google/products-and-platforms/products/workspace/gemini-workspace-updates-march-2026/) — Nuove funzionalità Gemini integrate in Docs, Sheets, Slides e Drive per produttività e collaborazione potenziate.
- [Replit Agent 4](https://replit.com/blog/agent-4) — Canvas di design infinito e agenti AI paralleli per costruire backend, frontend e slide deck in un unico ambiente integrato.

## Agentic AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Il protocollo A2A v1.0 segna il passaggio da agenti isolati a ecosistemi multi-agente interoperabili e pronti per la produzione.
- **Takeaway 2:** AutoResearch di Karpathy mostra agenti che migliorano iterativamente i modelli: un passo concreto verso il self-improvement autonomo.
- **Takeaway 3:** Tre pattern architetturali si consolidano per gli agenti: memoria persistente, skill programmabili e harness come infrastruttura di autonomia.

- **Action Items:**
  - Studia i tre pattern (memoria, skill, harness) e valuta quali sono già presenti nella tua architettura agentica.
  - Esplora il protocollo A2A v1.0 e le sue Agent Card per capire come abilitare la comunicazione cross-platform tra i tuoi agenti.

### Cosa succede questa settimana?

In questa sezione c'è veramente l'imbarazzo della scelta su quali notizie focalizzarsi, ma non posso che partire dall'annuncio del protocollo A2A in versione 1.0, dato che ho partecipato attivamente a questo lavoro insieme al mio team, curando anche Java SDK e TCK per tutto il protocollo.

Ma lasciando da parte le cose più personali, una menzione d'onore va all'AutoResearch di Karpathy, che da circa due settimane tiene banco nella community. Si tratta di utilizzare degli agenti in un loop di ricerca guidato per migliorare il training di un modello. L'ho già detto tante volte, sia qui che in podcast, che vedere dei modelli capaci di migliorare se stessi fa pensare molto da vicino all'AGI. È per me quello uno dei punti di svolta. Forse non ci siamo ancora, ma vedere miglioramenti iterativi, gestiti completamente da un agente, fa sicuramente impressione.

Ci sono poi tre trend che sottolineo da qualche tempo. La memoria persistente per gli agenti, le skill come modo di estendere gli agenti e di programmarne i comportamenti, e infine un trend che sottolineo da qualche settimana: quello degli harness. Per harness si intendono tutti quegli artefatti (tool, agenti, memoria o qualunque altra cosa possa essere utilizzata dall'LLM) per comportarsi in maniera il più possibile autonoma e decisionale, per diventare un agente. Riporto un articolo per ognuno di questi trend, che ritengo significativi come bagaglio culturale di qualunque AI engineer.

Infine, Perplexity dimostra che l'idea di far utilizzare un computer direttamente agli agenti è qualcosa di realistico e non è solo un giocattolo fatto dalla community come OpenClaw. In fondo è un po' come quando parliamo di robot umanoidi che hanno quel form factor per poter utilizzare tutti gli strumenti che noi abbiamo disegnato per il form factor umano. Allo stesso modo, gli agenti capaci di utilizzare software già esistenti, anche se disegnati per essere usati da umani, possono avere il vantaggio competitivo di riutilizzare una grandissima base di strumenti già disponibili.

### I link della settimana

- [Agent Skills: Progressive Disclosure come Pattern di System Design](https://www.newsletter.swirlai.com/p/agent-skills-progressive-disclosure) — Pattern a tre livelli (discovery, activation, execution) per gestire il contesto degli agenti in modo efficiente.
- [A2A Protocol v1.0: Comunicazione Agente Standardizzata](https://a2a-protocol.org/latest/announcing-1.0/) — Protocollo aperto per scoperta, comunicazione e coordinamento tra agenti AI su diverse piattaforme e organizzazioni.
- [L'Anatomia di un Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/) — I modelli contengono l'intelligenza, l'harness la rende utile: componenti core per trasformare LLM in agenti.
- [Google Always On Memory Agent](https://venturebeat.com/orchestration/google-pm-open-sources-always-on-memory-agent-ditching-vector-databases-for) — Sistema open source per memoria persistente degli agenti, senza database vettoriale, sotto licenza MIT.
- [AutoResearch di Karpathy](https://github.com/karpathy/autoresearch) — Loop di ricerca guidati da AI per migliorare iterativamente il training di modelli su singola GPU.
- [Il Personal Computer di Perplexity](https://www.theverge.com/2026/3/11/perplexity-personal-computer-mac-mini-ai-agents) — Agenti AI che gestiscono task delegando ad altre AI su un Mac Mini, come un project manager automatico.

## AI Assisted Coding

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Il 2026 si profila come l'anno in cui gli LLM entrano nelle code review: Claude Code Review è il primo segnale concreto.
- **Takeaway 2:** L'ecosistema di estensioni per Claude Code sta maturando rapidamente, con progetti come Everything Claude Code e SuperClaude che arricchiscono l'esperienza agentica.
- **Takeaway 3:** Chrome DevTools MCP apre le funzionalità del browser a qualunque agente, non solo quelli di coding, con il supporto ufficiale di Google.

- **Action Items:**
  - Prova Claude Code Review sulle tue PR per valutare la qualità delle revisioni automatiche rispetto al processo manuale.
  - Configura Chrome DevTools MCP nel tuo ambiente di sviluppo per esplorare le possibilità di debugging agentico.

### Cosa succede questa settimana?

Ci sono meme in community che parlano di come vai a letto, ti svegli e ogni mattina trovi una novità di Claude, e rispecchiano abbastanza la verità. Solo questa settimana ci sono almeno tre grandi novità da segnalare nel mondo Anthropic. La prima e più importante è che hanno rilasciato in preview per clienti Team ed Enterprise una nuova funzionalità di Claude Code chiamata Review per gestire le pull request review. Proprio settimana scorsa parlavo di come l'utilizzo degli LLM si stia spostando dalla pura generazione di codice anche ad altre fasi. Il 2026 potrebbe essere l'anno in cui vediamo gli LLM entrare a far parte dei tool utilizzati per fare le code review in maniera importante. Questo mi sembra il primo segnale.

Il secondo link che segnalo per Claude è chiamato Everything Claude Code ed è interessante perché è uno dei vincitori dell'hackathon di Anthropic. Si tratta di una serie di agenti, comandi e skill fatti per migliorare l'esperienza di utilizzo di Claude Code, qualcosa di molto simile a SuperClaude di cui ho già parlato spesso in passato. È nella mia to-do list di questa settimana provarlo estensivamente per capire se l'esperienza è realmente migliorativa rispetto a SuperClaude e altri progetti già disponibili.

Invece in casa Google annunciano i Chrome DevTools come MCP, ed è un annuncio importante perché al di là del discorso di sviluppo vero e proprio permette di aprire la funzionalità del browser a qualunque agente, di coding e non. Qualcosa che sicuramente abbiamo già visto succedere in OpenClaw, ma che questa volta ha il supporto pieno di Google.

### I link della settimana

- [Claude Code Review](https://claude.com/blog/code-review) — Sistema di code review automatizzato con team multi-agente per analisi approfondita delle pull request, disponibile per Team ed Enterprise.
- [Everything Claude Code](https://github.com/affaan-m/everything-claude-code) — 16 agenti specializzati, 65+ skill e 40+ comandi slash per ottimizzare i flussi di lavoro di Claude Code.
- [Documentazione Modalità Interattiva Claude, /btw](https://code.claude.com/docs/en/interactive-mode) — Domande laterali durante il lavoro attivo senza interrompere i task né aggiungere alla cronologia.
- [Come i Coding Agent stanno ridefinendo Engineering, Product e Design](https://www.reforge.com/blog/coding-agents-reshaping-engineering) — Il collo di bottiglia si sposta dalla scrittura alla revisione del codice; i generalisti ottengono il massimo vantaggio.
- [Chrome DevTools MCP](https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session) — Connessione diretta a sessioni browser attive per debugging agentico, senza estensioni né browser headless.

## Business e società

### I Takeaways per gli AI Engineers

- **Takeaway 1:** L'acquisizione di Moltbook da parte di Meta conferma l'interesse delle grandi aziende tech a un'economia basata sugli agenti.
- **Takeaway 2:** L'Anthropic Institute segnala che le sfide legali, economiche e di governance dell'AI stanno diventando priorità strategiche al pari dello sviluppo tecnico.
- **Takeaway 3:** Ethan Mollick ridefinisce il rapporto con l'AI: da co-intelligence (AI che aiuta l'umano) a gestione dell'AI (l'umano che orchestra agenti autonomi).

- **Action Items:**
  - Leggi l'articolo completo di Ethan Mollick "The Shape of the Thing" per approfondire il passaggio da co-intelligence a gestione dell'AI.
  - Osserva la strategia di acquisizioni open source di OpenAI come indicatore di quali tool diventeranno standard di piattaforma.

### Cosa succede questa settimana?

In questa sezione partiamo di nuovo da Meta, che ha acquisito, o meglio, assunto la persona che ha creato Moltbook, dato che si tratta di un'acquisizione di un'azienda fatta da una singola persona. Per chi non se lo ricordasse, Moltbook è un social network per agenti che sembra essere esattamente nel business principale di Meta, ma che conferma anche l'interesse da parte delle grandi aziende a un'economia basata sugli agenti.

Nel frattempo OpenAI continua con le sue acquisizioni di piattaforme open source. Così come era successo per OpenClaw, almeno nell'acquisire piattaforme open source e mantenerle tali sta confermando il suo nome che inizia con Open, cosa che non ha mai fatto, o quasi, con i modelli.

E mentre anche Nvidia investe sulla startup di Mira Murati con una partnership pluriennale, io preferisco concentrarmi su due articoli. Uno di Anthropic, che presenta l'Anthropic Institute, un istituto fondato per concentrarsi sugli aspetti legali, economici e di governance globale dell'AI. E uno invece del professor Ethan Mollick, che esamina il passaggio dell'AI da quella che lui ha sempre chiamato co-intelligence, cioè l'intelligenza aumentata dagli esseri umani attraverso l'utilizzo dell'AI, verso invece un'intelligenza che deve essere usata dall'essere umano per la gestione dell'AI e dei tanti agenti che si possono utilizzare in parallelo per svolgere compiti completi. Vi consiglio di leggere con attenzione questo articolo perché il professor Ethan Mollick sicuramente esprime questo concetto meglio di me, e non voglio certo mettermi a sintetizzarlo quando penso che una lettura completa e approfondita sia fondamentale.

### I link della settimana

- [The Shape of the Thing](https://www.oneusefulthing.org/p/the-shape-of-the-thing) — Ethan Mollick esamina il passaggio dalla co-intelligence alla gestione dell'AI e degli agenti autonomi.
- [Presentazione dell'Anthropic Institute](https://www.anthropic.com/news/the-anthropic-institute) — Istituto dedicato agli aspetti legali, economici e di governance globale dell'AI, guidato da Jack Clark.
- [Nvidia investe nel Thinking Machines Lab di Mira Murati](https://www.theinformation.com/articles/nvidia-invests-in-mira-muratis-thinking-machines-lab) — Partnership pluriennale con almeno un gigawatt di chip per addestramento e serving di modelli frontier.
- [Promptfoo entra in OpenAI](https://www.promptfoo.dev/blog/promptfoo-joining-openai/) — Piattaforma open source di sicurezza e valutazione AI acquisita da OpenAI, rimarrà open source.
- [Meta ha acquisito Moltbook](https://techcrunch.com/2026/03/10/meta-acquired-moltbook-the-ai-agent-social-network-that-went-viral-because-of-fake-posts/) — Meta acquisisce il social network per agenti AI basato sul framework OpenClaw.

## Paper di ricerca

### I Takeaways per gli AI Engineers

- **Takeaway 1:** I paper confermano il trend degli agent harness: skill, tool e memoria sono le infrastrutture che trasformano l'AI da informativa a dispositiva.
- **Takeaway 2:** Il reinforcement learning applicato agli agenti (non solo agli LLM) apre la strada ad agenti enterprise addestrati per casi d'uso specifici.
- **Takeaway 3:** SkillNet propone un modello aperto per skill riutilizzabili e componibili, un riferimento utile per chi progetta architetture agentiche.

- **Action Items:**
  - Leggi SkillNet per trarre ispirazione su come strutturare e connettere le skill nei tuoi agenti.
  - Approfondisci la distinzione tra RL sugli LLM e RL sugli agenti introdotta da KARL per capire le implicazioni sul design dei tuoi sistemi.

### Cosa succede questa settimana?

Una sezione sui paper di ricerca che mancava un po' a questa newsletter. La reintroduco per riportarvi quattro paper molto significativi che ho letto nelle ultime settimane e che confermano i trend evidenziati nelle sezioni precedenti: l'esigenza di una memoria di lungo orizzonte (Memex(RL)), con un reinforcement learning che permetta di farla utilizzare meglio agli agenti, ma anche tutto il trend che si sta sviluppando attorno agli agent harness (AutoHarness), ovvero le skill, i tool e tutto quello che è il raffinamento iterativo degli strumenti che gli agenti possono utilizzare per passare da un'intelligenza artificiale informativa a una dispositiva.

Nella stessa direzione va SkillNet, un paper che definisce un'infrastruttura aperta per delle skill AI riutilizzabili, con una valutazione multidimensionale e delle connessioni tra di loro. Merita comunque di essere letto anche solo per avere idee su come scrivere meglio e collegare meglio le proprie skill.

Il paper KARL parla di agenti di conoscenza via reinforcement learning. È interessante per quanto dimostri che attraverso il reinforcement learning gli agenti, in particolare di ricerca ma non solo, possano essere addestrati per casi specifici enterprise come entità distinte per i clienti. Qui si parla di utilizzare il reinforcement learning sugli agenti, quindi sulla parte di reasoning e action, e non soltanto sulla parte degli LLM. È una distinzione importante.

### I link della settimana

- [AutoHarness: Sintesi Automatica di Code Harness per Agenti LLM](https://arxiv.org/abs/2603.03329) — Generazione automatica di strutture protettive per agenti tramite raffinamento iterativo con feedback ambientale.
- [SkillNet: Creazione, Valutazione e Connessione di Skill AI](https://arxiv.org/abs/2603.04448) — Infrastruttura aperta per skill AI riutilizzabili con valutazione multidimensionale e 200.000+ skill nel repository.
- [KARL: Agenti di Conoscenza via Reinforcement Learning](https://arxiv.org/abs/2603.05218) — Agenti di ricerca enterprise addestrati con RL, con performance Pareto-ottimali rispetto a Claude 4.6 e GPT 5.2.
- [Memex(RL): Scaling Agenti LLM a Lungo Orizzonte via Memoria Indicizzata](https://arxiv.org/abs/2603.04257) — Memoria indicizzata con RL per agenti a lungo orizzonte, superando i limiti delle finestre di contesto finite.
