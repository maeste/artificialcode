# Personal AGI: la guerra è per l'harness, non per il modello

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

*Questa settimana tutti parlano di GPT-6 Astra, e per una volta l'hype è quasi giustificato: 99,9% su ARC-AGI-3 e benchmark da record su tutta la linea. Ma la notizia che mi ha colpito di più non è il modello, è il piano: nei North Stars OpenAI mette nero su bianco il "personal AGI per ogni persona sulla Terra". Da lì è partito questo deep dive, perché quella parola descrive una partita che riguarda da vicino chi costruisce agenti: è una guerra per l'harness, non per il modello. OpenAI ha il modello al centro, Nous Research guarda all'harness, e io sto con questi ultimi: la mia tesi è che il personal AGI sarà una soluzione ingegneristica, un'orchestra di agenti multipli con modelli locali e in cloud, non un supermodello solo. Con i numeri dei paper che lo dimostrano. Nella parte link: Anthropic segmenta i safeguards come variabile di prodotto, Google sfodera il terzo Flash in sei settimane e porta il video generativo a pipeline, NVIDIA compra Hugging Face e Laycock spiega perché la code review è il nuovo collo di bottiglia. In agenda la puntata 70 del podcast sul caso benchmark di Astra, AI Salon Milano e Zurich. Buona lettura.*

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * È uscita la nuova puntata di Risorse Artificiali: "99,9% nel benchmark, 61 nell'indice: il caso GPT-6 Astra". OpenAI rilascia GPT-6 Astra con numeri da record: 99,9% su ARC-AGI-3 che nessun modello sfiora, ma un benchmark maxato, cioè mostrato al modello in addestramento, vale ancora qualcosa? E perché l'indice di Artificial Analysis gli dà 61, lo stesso punteggio di GLM 5.3 Max? Con Stefano, Paolo e Alessio: costi per intelligent task, pesi dell'indice, Qwen 3.8 Flash Next, Waymo su TPU, Nvidia che compra Hugging Face e GLM su 100 mila chip Huawei. Guarda: https://www.youtube.com/watch?v=y79Nb91Akto

[Talk]:
  * A Novembre sarò ad Agentic Engineering Days Zurich con il talk "Agents Speak Protocol: Why Standards Are the Real Infrastructure of AI", insieme ad Alessio Soldano: MCP, A2A, A2UI e il resto dello stack di protocolli che porta ordine nella torre di Babel degli agenti, con le lezioni delle guerre di protocolli passate. Orario e sala arrivano a ottobre: https://www.agenticdays.com/session/1292080-agents-speak-protocol-why-standards-are-the-real

[Eventi]:
  * Il 14 Settembre sarò ospite di [AI Salon Milano](https://luma.com/aisalon?e=evt-qhXFEh6vFAzCIxz) per una chiacchierata con [Yuri Mariotti](https://www.linkedin.com/in/yurimariotti/)
  * Anche per il 10 ottobre qualcosa bolle in pentola sullo stesso tema...ma non annuncio finchè non esce l'agenda...magari qualcuno attento alle conferenze e developer groups ha capito :)

---

## Personal AGI: la guerra è per l'harness, non per il modello

Questa settimana tutti parlano di [GPT-6 Astra](https://openai.com/index/safety-overview-gpt-6-astra/). Io pure ne ho scritto nel podcast: 99,9% su ARC-AGI-3, l'[annuncio](https://x.com/OpenAI/status/2095595741528125780) che in tre giorni ha accumulato centinaia di migliaia di like, e [la lettura di Chollet](https://x.com/fchollet/status/2095598451115614371) che lo definisce uno step-function change, con il modello che si costruisce al volo un proprio linguaggio simbolico per ragionare sui giochi. Alle prime prove è, per certi versi, incredibile. Eppure la notizia che mi ha colpito di più è arrivata dalla stessa OpenAI ma da un'altra porta: i [North Stars](https://openai.com/index/an-alien-mind/), il piano strategico pubblico scritto dal chief scientist Jakub Pachocki. Perché dentro c'è una parola che descrive la partita vera di questo momento: personal AGI.

OpenAI è l'unico ad averla messa nera su bianco. Tre obiettivi: il [ricercatore AI automatizzato](https://www.technologyreview.com/2026/03/20/1134438/openai-is-throwing-everything-into-building-a-fully-automated-researcher/), l'accelerazione economica, e il "personal AGI per ogni persona sulla Terra". Niente definizione formale. La versione operative è nel [job posting del team Personal AGI](https://openai.com/careers/research-engineerresearch-scientist-personal-agi-north-stars-san-francisco/): "evolvere ChatGPT da chatbot a superassistente infinitamente capace e personalizzato". [Brockman](https://gln75.com/en/blog/brockman-openai-superapp-path-agi) ci mette i numeri: AGI al "70-80%", la definizione non conta più, il pavimento sale troppo in fretta. E [il retweet](https://x.com/gdb/status/2093065379145019902) che ha fatto girare mezzo internet: ChatGPT Work che prenota da solo un taglio di capelli, "chatgpt is increasingly becoming your personal AGI". Poi febbraio: [Peter Steinberger, il creatore di OpenClaw](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/), l'harness open più diffuso al mondo, entra in OpenAI per guidare i personal AI agents. Leggetelo bene: il laboratorio con i modelli più desiderati del pianeta ha comprato in casa la persona che sa costruire l'esecuzione, non i pesi.

Ma la lettura di OpenAI resta centrata sul modello: il personal AGI è ChatGPT, un modello, avvolto dal loro harness nel loro cloud. Io la vedo diversa, e non sono l'unico. Nous Research non ha mai usato quella parola per [Hermes](https://hermes-agent.nousresearch.com/docs/), e non è un caso: il loro agente è self-improving, model-agnostic su venti provider, le skill le crea l'esperienza, il modello è una variabile di configurazione. L'harness è il prodotto.

E l'harness ha ormai la sua teoria. Il paper ["Stop Comparing LLM Agents Without Disclosing the Harness"](https://arxiv.org/abs/2605.23950) formalizza la Binding Constraint Thesis: nei task long-horizon la varianza di performance indotta dall'harness supera quella del modello, nel loro esperimento di sette volte. ["The Harness Effect"](https://arxiv.org/abs/2607.06906) fa l'esperimento pulito: stessi sei modelli, stessi task, cambia solo l'orchestrazione. Costo per task meno 41%, tempo meno 44%, token meno 38%.

La mia tesi è più semplice di qualunque paper: il personal AGI sarà una soluzione ingegneristica, non di modello. Un harness che orchestra agenti multipli, ognuno col modello giusto per il compito: uno locale per la privacy, uno in cloud per la capacità, uno economico per il batch. Non un supermodello al centro, un'orchestra dirette bene. Proprio come funziona il mio setup, dove l'agente personale gira sul mio server, col modello che scelgo io, e questa settimana l'ho messo a testare il sandbox che protegge gli altri.

Personal AGI significa una cosa sola: chi possiede l'harness possiede l'agente. Il resto è marketing.

---

## I link che mi hanno colpito questa settimana

### [Anthropic — Introducing Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)

Anthropic rilascia due versioni dello stesso modello con livelli diversi di safeguards. Fable 5.1 è GA su API, AWS, GCP e Azure: 55,8% su Terminal-Bench 4.0, cache read a $0.25/M (-75%), safeguards ridotte di un fattore enorme nei falsi positivi. Mythos 5.1, la versione più permissiva, resta gated alle organizzazioni USA verificate (CVP e LSVP). Un modello, tanti prodotti: la segmentazione dei safeguard diventa variabile di prodotto.

### [Google — Introducing Gemini 3.8 Flash and 3.8 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)

Terzo Flash in sei settimane. La tesi: 3.8 Flash "works harder", più passi di ragionamento e più tool call agli stessi prezzo e velocità del 3.7. Prezzo introduttivo $0.75/$3.75 per milione con scadenza 31 dicembre 2026, poi il doppio: la guerra dei Flash si sposta sull'economia unitaria. Accanto, Gemini 3.8 Flash Cyber specializzato in patching (pass@1 47,2% su CWE-Bench), accesso gated al Fairwind Program.

### [Google — Gemini Omni 1.1 Flash lets you build with more control](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Google porta il modello video Omni a 1.1 production-ready: analisi fino a 10 secondi di filmato precedente per coerenza visiva, scene extension fino a 40 secondi cumulativi, controllo dei keyframe per transizioni e loop, video reference in input per la consistenza dei personaggi. Le preview draft 360p costano un terzo del 720p. Runway, Figma e Adobe tra i clienti citati: il video generativo diventa pipeline, non demo.

### [NVIDIA — NVIDIA to Acquire Hugging Face](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/)

NVIDIA acquisisce Hugging Face per $12.930.300.000, la cifra scritta con la precisione del centesimo. In cambio: 18M+ sviluppatori, 3M+ modelli, 500K dataset. Le garanzie nel post di Jensen Huang: la piattaforma resta aperta, il compute NVIDIA non sarà richiesto per build o deploy, supporto multi-cloud e brand 🤗 mantenuto. L'hub neutrale dell'open weights ha un padrone: la promessa di neutralità è da leggere come posizionamento del compratore.

### [Rachel Laycock — rachels-ramblings: code review](https://martinfowler.com/rachels-ramblings/code-review.html)

La CTO di Thoughtworks risponde a Brian Houck (DX) dopo un disaccordo nato a Code Remix: "we've been using code review to solve the wrong problems". La review faceva da quality gate, security check, mentoring e knowledge sharing tutte insieme, sempre in ritardo. Con l'AI che genera più codice di quanto gli umani possano ispezionare (a Meta +106% di LOC per diff in un anno), imporre review umana su ogni cambiamento crea un collo di bottiglia: non abbiamo creato organizzazioni 10x, abbiamo creato un backlog. La proposta: spostare il giudizio a sinistra (pair/mob, fitness function) e review umana solo per eccezione.
