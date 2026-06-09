# Estrazione link dalle ultime 25 edizioni della newsletter

Temi: memoria a lungo termine per LLM/agenti, continuous learning, agenti auto-evolutivi, sistemi di auto-miglioramento (auto-research).

---

## Memoria a lungo termine per LLM e agenti

### Hermes Agent
https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching
https://hermes-agent.nousresearch.com/docs/developer-guide/session-storage
https://hermes-agent.nousresearch.com/docs/developer-guide/memory-provider-plugin
https://hermes-agent.nousresearch.com/docs/developer-guide/context-engine-plugin

- Descrizione: Hermes Agent è un'alternativa open source a OpenClaw. Mi ha colpito perché c'è molta più attenzione alla sicurezza, ma soprattutto per il suo sistema di memoria pluggable ed estremamente avanzato. Vale la pena darci un'occhiata anche solo per capire come utilizzano il sistema di memoria.
- Fonte: CY26W15-it.md

### Engram Memory System
- URL: https://weaviate.io/blog/engram-internal-use-case
- Descrizione: Sistema di memoria vettoriale per agenti, contesto persistente per migliorare i workflow. Da tempo parlo dell'importanza della memoria negli agenti, e questa cosa è stata dimostrata anche dall'attenzione all'uso della memoria nel codice trapelato di Claude Code.
- Fonte: CY26W14-it.md

### Google Always On Memory Agent
- URL: https://venturebeat.com/orchestration/google-pm-open-sources-always-on-memory-agent-ditching-vector-databases-for
- Descrizione: Sistema open source per memoria persistente degli agenti, senza database vettoriale, sotto licenza MIT.
- Fonte: CY26W11-it.md

### Memex(RL): Scaling Agenti LLM a Lungo Orizzonte via Memoria Indicizzata
- URL: https://arxiv.org/abs/2603.04257
- Descrizione: Memoria indicizzata con RL per agenti a lungo orizzonte, superando i limiti delle finestre di contesto finite.
- Fonte: CY26W11-it.md

### GAM: General Agentic Memory Via Deep Research
- URL: https://arxiv.org/abs/2511.18423
- Descrizione: Framework di memoria agentica con approccio JIT: Memorizer per riassunti leggeri e Researcher per sintesi on-demand.
- Fonte: CY26W10-it.md

### Claude Code Auto-Memory
- URL: https://x.com/trq212/status/2027109375765356723
- Descrizione: Claude salva autonomamente contesto tra le sessioni: CLAUDE.md per le istruzioni dell'utente, MEMORY.md taccuino aggiornato autonomamente da Claude ad ogni sessione.
- Fonte: CY26W9-it.md

### Claude-Mem
- URL: https://github.com/thedotmack/claude-mem
- Descrizione: Plugin memoria persistente per Claude Code con web viewer e ricerca ibrida
- Fonte: CY26W7-it.md

### DeepSeek Engram
- URL: https://rewire.it/blog/engram-how-deepseek-added-second-brain-to-llm/
- Descrizione: Con l'introduzione di DeepSeek Engram, hanno affrontato il problema dell'efficienza computazionale dei Transformer in modo laterale. Invece di far processare ogni singolo pattern ripetitivo alla rete neurale, il sistema utilizza tabelle di lookup per schemi comuni. Questo secondo cervello permette al modello di recuperare informazioni statiche istantaneamente, liberando cicli di calcolo preziosi per il ragionamento logico puro.
- Fonte: CY26W3-it.md


### GraphSense
- URL: https://github.com/faraazahmad/graphsense
- Descrizione: Il suo strumento GraphSense open-source dimostra che applicando tecniche consolidate di computer science (vector embedding per la similarità semantica e database a grafo per il tracking delle dipendenze) possiamo rendere gli assistenti AI per coding molto più pratici e cost-effective.
- Fonte: W37-it.md

### Approccio di Factory alla compressione del contesto
- URL: https://www.factory.ai/news/compressing-context
- Descrizione: Introduce tecniche innovative per gestire workflow di agenti estesi. Usano "riassunti ancorati" che si aggiornano incrementalmente. Punta verso sistemi di "gestione proattiva della memoria" dove gli agenti decidono intelligentemente quando comprimere informazioni.
- Fonte: W30-it.md

### Memories.ai, modello che ricorda a scala sovrumana
- URL: https://www.testingcatalog.com/memories-ai-introduces-a-new-model-that-remembers-at-superhuman-scale/
- Descrizione: Il nuovo modello di Memories.ai dimostra questa evoluzione, processando video a scala sovrumana mantenendo una comprensione persistente attraverso interi archivi.
- Fonte: W30-it.md

### Cognee
- URL: https://www.cognee.ai/
- Descrizione: Cognee trasforma dati grezzi in memorie strutturate, usando knowledge graph per identificare connessioni nascoste e supportare più backend store per sistemi di memoria semantica flessibili.
- Fonte: W30-it.md

### Reflection AI, Asimov (agente di ricerca codice con memoria del team)
- URL: https://reflection.ai/blog/introducing-asimov/
- Descrizione: Reflection AI ha lanciato Asimov, un agente di ricerca codice che indicizza intere codebase e conoscenze del team per rispondere a domande di ingegneria con citazioni. Promette di diventare un membro del team, imparando convenzioni e best practices dal team.
- Fonte: W29-it.md

### Context Engineering Series
- URL: https://jxnl.co/writing/2025/08/28/context-engineering-index/
- Descrizione: Esplora come agenti di coding come Claude Code e Cursor performano "context engineering" progettando portfolio di strumenti, comandi slash e architetture di sotto-agenti per aiutare i sistemi AI a scoprire le informazioni di cui hanno bisogno per performare ottimalmente.
- Fonte: W36-it.md

### Context engineering per agenti
- URL: https://rlancemartin.github.io/2025/06/23/context_engineering/
- Descrizione: L'arte e la scienza di fornire agli agenti le informazioni giuste ad ogni step. Comporta fornire istruzioni appropriate, conoscenza e strumenti per ottimizzare l'output riducendo l'uso di token. I quattro approcci comuni sono: scrivere contesto, selezionare contesto, comprimere contesto e isolare contesto.
- Fonte: W31-it.md

---

## Continuous learning e apprendimento continuo

### Momento GPT-3 dell'RL (continuous learning / adattamento)
- URL: https://www.mechanize.work/blog/the-upcoming-gpt-3-moment-for-rl/
- Descrizione: Ci stiamo avvicinando al momento GPT-3 dell'RL. Il campo si sposterà presto verso training massicci attraverso migliaia di ambienti diversi, producendo modelli con forti abilità di adattarsi rapidamente a task completamente nuovi.
- Fonte: W29-it.md

### Imparare la bitter lesson
- URL: https://rlancemartin.github.io/2025/07/30/bitter_lesson/
- Descrizione: Ci ricorda che la filosofia di design delle applicazioni AI è ancora nascente. Possiamo predire che i modelli miglioreranno drasticamente, quindi progettare applicazioni per sfruttare questo miglioramento è cruciale. Comprendi la struttura della tua applicazione, ri-valuta man mano che i modelli migliorano.
- Fonte: W31-it.md

---

## Agenti che evolvono autonomamente

### Autogenesis, A Self-Evolving Agent Protocol (arXiv)
- URL: https://arxiv.org/abs/2604.15034
- Descrizione: Avrete sicuramente sentito parlare dell'autoresearch di Karpathy. Qui metto un articolo e un repository che vengono da Shopify per dimostrare quanto autoresearch possa essere potente anche usata fuori dal caso d'uso base di Karpathy, che era il training dei modelli. Stiamo davvero andando verso agenti capaci di migliorarsi da soli?
- Fonte: CY26W16-it.md

### Measuring AI Agent Autonomy
- URL: https://www.anthropic.com/research/measuring-agent-autonomy
- Descrizione: Anthropic analizza milioni di interazioni umano-agente: autonomia crescente, utenti verso monitoraggio strategico.
- Fonte: CY26W8-it.md

### Dr. Zero (Meta Superintelligence Labs)
- URL: https://arxiv.org/abs/2601.07055
- Descrizione: Questo framework permette agli agenti di ricerca di evolversi senza dati di training umani, utilizzando un ciclo di feedback tra un modulo che genera domande difficili e uno che impara a risolverle tramite web search. Questo approccio di auto-evoluzione per il ragionamento multi-hop è esattamente ciò che serve per superare i limiti dei modelli supervisionati tradizionali.
- Fonte: CY26W3-it.md

### Self-Evolving Agents Survey
- URL: https://arxiv.org/abs/2412.12498
- Descrizione: Lettura essenziale per comprendere come gli agent possano evolversi con accesso a memoria, strumenti ed esperienza. Inquadra l'auto-evoluzione come un passo chiave verso l'Artificial Super Intelligence (ASI).
- Fonte: W32-it.md

### projnanda
- URL: https://projnanda.github.io/projnanda/#/
- Descrizione: NANDA è profondamente investita nello sviluppo di agent. Il lavoro mostra framework per l'interoperabilità e coordinazione degli agent che formano le fondamenta dell'emergente Agentic Web, una mesh di agent e protocolli interoperabili.
- Fonte: W34-it.md


---

## Sistemi di auto-miglioramento e auto-research

### Autoresearch isn't just for training models (Shopify Engineering)
- URL: https://shopify.engineering/autoresearch
- Descrizione: Avrete sicuramente sentito parlare dell'autoresearch di Karpathy. Qui metto un articolo e un repository che vengono da Shopify per dimostrare quanto autoresearch possa essere potente anche usata fuori dal caso d'uso base di Karpathy, che era il training dei modelli.
- Fonte: CY26W16-it.md

### davebcn87/pi-autoresearch (GitHub)
- URL: https://github.com/davebcn87/pi-autoresearch
- Descrizione: Repository citato insieme all'articolo di Shopify per dimostrare quanto autoresearch possa essere potente anche usata fuori dal caso d'uso base di Karpathy, che era il training dei modelli. Stiamo davvero andando verso agenti capaci di migliorarsi da soli?
- Fonte: CY26W16-it.md

### Agent Lightning (Microsoft)
- URL: https://github.com/microsoft/agent-lightning
- Descrizione: Framework per ottimizzare agenti con RL, prompt optimization e fine-tuning, zero modifiche al codice. L'ottimizzazione degli agenti tramite reinforcement learning e training loop strutturati sta passando dalla teoria ai framework utilizzabili.
- Fonte: CY26W14-it.md

### The Model-Harness Training Loop
- URL: https://x.com/Vtrivedy10/status/2039872562662941118
- Descrizione: Ciclo di training per agenti basato su harness engineering, modelli open e infrastruttura accessibile. Articolo teorico sul training loop intorno all'utilizzo dell'harness da parte dei modelli all'interno di un sistema di agenti.
- Fonte: CY26W14-it.md

### AutoResearch di Karpathy
- URL: https://github.com/karpathy/autoresearch
- Descrizione: Loop di ricerca guidati da AI per migliorare iterativamente il training di modelli su singola GPU.
- Fonte: CY26W11-it.md

### AutoHarness: Sintesi Automatica di Code Harness per Agenti LLM
- URL: https://arxiv.org/abs/2603.03329
- Descrizione: Generazione automatica di strutture protettive per agenti tramite raffinamento iterativo con feedback ambientale.
- Fonte: CY26W11-it.md

### KARL: Agenti di Conoscenza via Reinforcement Learning
- URL: https://arxiv.org/abs/2603.05218
- Descrizione: Agenti di ricerca enterprise addestrati con RL, con performance Pareto-ottimali rispetto a Claude 4.6 e GPT 5.2.
- Fonte: CY26W11-it.md

### LLM Daydreaming (auto-miglioramento tramite connessioni background)
- URL: https://gwern.net/ai-daydreaming
- Descrizione: I modelli attuali mancano di processi background per formare connessioni tra argomenti apparentemente non correlati. La soluzione proposta coinvolge sistemi che stimolano gli LLM a recuperare fatti casuali, generare connessioni innovative e usare modelli critici per filtrare insight genuinamente preziosi.
- Fonte: W29-it.md

### Reinforcement Learning Teachers di Sakana AI (auto-miglioramento dei modelli)
- URL: https://sakana.ai/rlt/
- Descrizione: Usando modelli "teacher" che spiegano soluzioni piuttosto che risolvere problemi da zero, un piccolo modello da 7B parametri ha superato i 671B parametri di DeepSeek R1. Questi teacher ricevono in anticipo sia domande che risposte corrette e sono addestrati solo a generare spiegazioni chiare che aiutano i modelli studenti a capire.
- Fonte: W26-it.md
