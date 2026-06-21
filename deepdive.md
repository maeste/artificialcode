
## L'harness e i loop nuovi cardini dell'AI agentica

* Più passa il tempo e più diventa chiaro che per fare agenti non bastano solo ottimi modelli e qualche tool Gli harness stanno diventando centrali e come accoppiare il modello all'harness è dfondamentale
* Lo skill per gli utilizzatori evoluti sono cambiate e oggi bisogna più che mai si parla di harness engineering che di recente è evoluto in loop engineering
* Questi due termini significa che oltre al contesto che si da all'LLm bisogna saper curare molto di più. 
* Intuitivamente l'harness engineering aggiunge alla cura del contsto la capacità definire anche i limiti all'interno dei quali vogliamo che l'agente si muova, appunto l'ibracatura. Si tratta quindi di definire una sandbox, degli evals, e un modo di verificare il lavoro. Aggiungendo questi confini l'agente è in grado di muoversi con maggiore autonomia e per compiti più lunghi e complessi
* Ma se vogliamo un livello di autonimia e delle capacià agentiche ancora maggiori dobbiamo saper definire anche i limiti del loop all'interno del quale vogliamo che l'harness cicli per portare a termine il suo compito. E un loop è composto da uno stato iniziale, un evento che fa iniziare il loop, Un goal da portare a termine, una serie di funzionalità o behaviour consolidati (le skills) uno stato di lavoro (memoria) che permetta di tener traccia dei compiti fatti e di cosa verificare, dei sistemi di decisione per decidere se continuare il loop o se il goal è raggiunto. 
* Osservando quello che succede è sempre più chiaro che quelli che chiamiamo agenti (di coding e non) sempre di più assomigliano a dei processi che girano all'interno di un sistema operativo agentico (una sorta di sistema operativo di secondo livello), in cui sono appunto definiti i limit (con l'harness) e la gestione dei processi (con i loop)
* E questo legame tra LLM, agenti, harness e loop sta definendo delle nuove entità minime che possano essere considerate come unità operative o appunto processi da poter spostare sulla macchina, sulla rete, sul clooud. Ma non sono microservizi che assomigliano a quelli web o rest, ma invece delle unità di lavoro più simili ad un pod. Pensare gli evals, o le sandbox o ui guardrails come entità da pluggare sopra un sistema che contine del codice che si interfaccia agli LLM è sempre meno realistico. Tutti quei pezzetto di software di base che costituiscono l'harness o il loop ssono parte integrante dell'unità con cui ci interfacciamo e con cui il programmatore (o colui che sviluppa nuove skills o skills di livello applicativo). Se mi interfaccio ad un database cn SQL, mi aspetto che per me il logging, la scrittura su disco, la gestione della memoria siano fatte dal server di database, eventualmente interrogati da mie estensioni, ma che non necessitano di essere pluggati ogni volta. Un server di database scrive su disco, lo do per scontato. Un server di database tiene le transazioni, lo do per scontato. Quando mi interfaccio ad un agente (ovvero al suo harness/loop) do per scontato che abbia delle skill, che abbia degli evals, che abbia una sandbox ecc ecc. 
* I link di supporto servono a dimostrare quanto investimento ci sia su harness (o estensioni dell'harness per supportare loop) da parte di tutti, perchè ormai il servizio non è più un AI infused application (quello che faceva langchain e simili 2 anni fa per permettere allo sviluppatore di aggiunger un LLm come un tool nel suo codice), ma un sitema che vede gli agenti (LLM+Harness+Loop) come il servizio in cui deployare cose nuove e in cui far viivere le proprie applicazione AI native
* E' un po' come scrivere la propria app in HTML5. Dietro ci sono tanti livelli (a titlo esemplificativo in ordine: Il browser che fa rendering e il motore javascript, l'http, il tcp/ip, le socket) ma ognuno di questi livelli è dato per scontato ed ha i suoi meccanismi di eval/sicurezza/tracing che sono implementati e dati per scontati
* In una parola: l'harness+loop è la nuova entità minima con cui accedere agli agenti.
* Nei link, parlando di sandbox citiamo anche Lince.sh

## Link a supporto


### [OpenAI acquisisce Ona](https://openai.com/index/openai-to-acquire-ona/)

OpenAI ha annunciato l'acquisizione di Ona, la startup tedesca di cloud development già nota come Gitpod, che fornisce ambienti cloud sicuri e preconfigurati per gli agenti AI. La tecnologia di orchestrazione di Ona permetterà a Codex di eseguire task persistenti e a lunga durata, continuando a lavorare nel cloud del cliente anche a laptop chiuso. Il team Ona confluirà in OpenAI sul progetto Codex. Termini economici non divulgati.

---

### [MiMo Code di Xiaomi batte Claude Code sui task ultra-lunghi](https://venturebeat.com/technology/xiaomis-new-open-source-agentic-ai-coding-harness-mimo-code-beats-claude-code-at-ultra-long-200-step-tasks)

Xiaomi ha rilasciato MiMo Code, harness di coding agentico open source (licenza MIT). Secondo i benchmark dell'azienda, con MiMo-V2.5-Pro supera Claude Code su SWE-bench Verified, SWE-bench Pro e Terminal Bench 2, gestendo sequenze oltre i 200 step dove Claude entrava in loop di allucinazione. Introduce un sistema di memoria persistente affidato a subagent. Da notare: i numeri sono autodichiarati e non verificati in modo indipendente.

---

### [SkillSpector (repo GitHub)](https://github.com/NVIDIA/SkillSpector)

SkillSpector, sviluppato da NVIDIA, analizza le skill degli agenti AI alla ricerca di vulnerabilità di sicurezza prima dell'installazione, aiutando a individuare comportamenti rischiosi nelle estensioni di terze parti.

### [Dai al tuo agente il suo computer](https://www.langchain.com/blog/give-your-ai-agent-its-own-computer)

LangSmith introduce Sandboxes, microVM virtualizzate a livello hardware che offrono agli agenti AI un ambiente di calcolo dedicato e sicuro, rispondendo ai rischi dell'esecuzione di codice non fidato. Queste sandbox permettono agli agenti di eseguire task dinamici, gestire stato persistente e far girare workflow complessi senza compromettere l'infrastruttura di produzione.
