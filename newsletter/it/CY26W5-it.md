Questo numero della newsletter non è particolarmente lungo, ma denso. I link e le storie che riporto sotto meritano un'attenta lettura e qualche approfondimento. Ma prima di evidenziarvi le mie tre storie top discusse sotto, lasciate che vi consigli di approfondire l'argomento a mio avviso più rilevante della settimana e forse di tutto il mese di gennaio.

Come l'anno scorso al World Economic Forum c'è stato un panel/confronto tra Demis Hassabis e Dario Amodei parlando di AGI (Artificial General Intelligence), o più precisamente del mondo dopo l'AGI. Vi consiglio di spendere 30 minuti sul [Video YouTube](https://www.youtube.com/watch?v=02YLwsCKUww) completo perché la portata delle cose che dicono dovrebbe interessare chiunque, non solo AI Engineers, ma anche economisti e politici. Noi ne abbiamo parlato nel [podcast Risorse Artificiali](https://risorseartificiali.com) sabato, se vi va di sentire la nostra opinione e di ragionarne un po'.

Come estensione di questo, vi consiglio di mettervi comodi e leggere l'articolo annuale di Amodei (che è quasi un libro, ma ne vale la pena) su questi temi: [The Adolescence of Technology - Dario Amodei Essay](https://www.darioamodei.com/essay/the-adolescence-of-technology).

Tornando ai link e temi trattati sotto, mi permetto di evidenziarne tre:

- L'avvento di OpenClaw... interessante soprattutto come finestra sul futuro di quello che (quest'anno) gli agenti fanno e faranno per noi. Un assaggio di AGI che vi fa capire perché i discorsi di Hassabis e Amodei siano fondamentali da affrontare ORA!
- L'agentic coding è il cambio di paradigma nello sviluppo del codice più importante degli ultimi 20 anni. Andrej Karpathy dixit.
- Google sta allargando la sua sfera di influenza sull'AI: Gemini in tutti i telefoni, in Chrome, TPU prodotte in autonomia, clienti "rubati" a OpenAI.


Buona lettura! Ogni feedback è più che gradito, sempre, se volete anche di persona se Venerdi prossimo siete al Voxxed Day a  Lugano (o giovedi sera per una birra): Parlerò di [sicurezza legata alla Generative AI in un panel](https://vdt26.voxxeddays.ch/talk/?id=5409), e di gestione dei task e di spec-driven development parlerò al [Voxxed Day in un altro panel](https://vdt26.voxxeddays.ch/talk/?id=10201), dove farò da moderatore.

---

## Novità e ricerca nei modelli AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Il 2026 segna l'affermazione di due trend paralleli: capacità di ragionamento visivo integrato nella CoT e processi agentici multi-agente sia interni che esterni ai modelli
- **Takeaway 2:** I modelli visivi stanno evolvendo verso un "pensare con immagini" simile agli esseri umani, che utilizzano schemi e diagrammi per supportare il ragionamento
- **Takeaway 3:** La robotica sta per raggiungere il suo "aha moment" nei prossimi 18 mesi, guidata dalla convergenza di hardware come Helix 02 e world model come Genie

- **Action Items:**
  - Sperimenta con Genie in Google Labs per comprendere le potenzialità dei world model interattivi
  - Studia come integrare il ragionamento visivo nei processi di sviluppo AI della tua organizzazione

### Cosa succede questa settimana?

C'è un filo conduttore nelle prime tre notizie relative ai modelli di questa settimana: la capacità visiva come parte integrante del ragionamento è il trend che si sta evidenziando in questo inizio anno e che può segnare una ulteriore svolta per gli LLM multimodali. Penso infatti che il 2026 vedrà due grandi trend affermarsi:

- I processi agentici sia interni che esterni ai modelli: sia Kimi K2.5 che Gemini spingono verso le capacità di orchestrare e parallelizzare in agenti multipli
- La multimodalità dei modelli usata anche nella CoT, ovvero nei processi di pensiero. Se ci pensate è una evoluzione naturale alla CoT basata solo su token, esattamente come a noi capita di farci uno schema o un diagramma per aiutarci a pensare, così iniziano a fare e faranno sempre di più i modelli

C'è un terzo trend evidente questa settimana nella ricerca e nella pratica. Un trend che avrà presto il suo "aha moment", diciamo nei prossimi 18 mesi. Sto parlando della robotica e questa settimana lo vediamo sia con l'hardware con l'impressionante Helix 02 che nel software con i world model che la fanno da padroni nei papers di ricerca degli ultimi mesi. Ma Google va oltre permettendoci di provare il loro Genie, un world model state of the art disponibile in Google Labs. Fatevi un giro.

### I link della settimana

- **[Kimi K2.5: Visual Agentic Intelligence](https://www.kimi.com/blog/kimi-k2-5.html)** - Moonshot AI introduce il più potente modello open-source con 15T token visivo-testuali, agent swarm fino a 100 sub-agenti e riduzione tempi fino a 4.5x.
- **[Google launches Agentic Vision in Gemini 3 Flash](https://www.testingcatalog.com/google-launches-agentic-vision-in-gemini-3-flash/)** - Approccio iterativo Think-Act-Observe con esecuzione codice per zoom automatico, annotazione immagini e parsing tabelle complesse.
- **[Visual Models for Reasoning Like Humans](https://github.com/thuml/Reasoning-Visual-World)** - Modello multimodale unificato che usa generazione visiva come parte del chain-of-thought per ragionamento simile agli esseri umani.
- **[Introducing Helix 02: Full-Body Autonomy](https://www.figure.ai/news/helix-02)** - Singolo sistema neurale che controlla l'intero corpo dai pixel, autonomia loco-manipolativa in cucina completa per 4 minuti senza intervento umano.
- **[Google DeepMind's Project Genie Now Live](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/)** - Prototipo world-building interattivo disponibile per abbonati Google AI Ultra, crea ambienti virtuali con comprensione fisica e dinamiche reali.

---

## Agentic AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** OpenClaw rappresenta la frontiera degli agenti general-purpose capaci di operare su qualsiasi task desktop, ma richiede cautela estrema: sandboxing in VM e account isolati sono essenziali
- **Takeaway 2:** Le big tech stanno implementando l'agentic AI con approcci più controllati: Anthropic con app MCP integrate in Claude, Google con Gemini in Chrome
- **Takeaway 3:** Il trend verso agenti autonomi è inarrestabile, ma la sicurezza rimane il collo di bottiglia: da un grande potere deriva una grande responsabilità

- **Action Items:**
  - Valuta l'adozione di agenti AI nel tuo flusso di lavoro partendo da approcci controllati come le app MCP di Claude
  - Se sperimenti con agenti general-purpose come OpenClaw, crea sempre un ambiente isolato con VM e account dedicati

### Cosa succede questa settimana?

Questa settimana non si può che iniziare questa sezione parlando di OpenClaw, già noto come Clawd.bot e molt.bot (vedi [qui](https://openclaw.ai/blog/introducing-openclaw) la storia del come e perché hanno cambiato nome 3 volte al progetto in 10 giorni). Di cosa si tratta? Di un agente simile per certi versi agli agenti di coding come claude-code e Codex, ma in grado di svolgere qualunque compito e parlare con voi attraverso Telegram o WhatsApp. E quando dico qualunque compito intendo praticamente qualunque cosa possiate fare con il vostro PC.

Io l'ho provato e sono stato in grado di mandargli richieste (su Telegram mentre ero fuori casa) tipo: "controlla la mia mail, prendi quelle che arrivano da questa newsletter e producimi un documento riassuntivo con tutti i link che sono li menzionati. Poi cerca nel web quali sono le notizie/link più discussi e crea una sezione nel documento con le 5 notizie più rilevanti e le 5 più controverse. Quando hai finito mandami una sintesi su Telegram"... e wow, dopo 5 minuti aveva fatto tutto.

Al momento non è uno strumento per tutti (da un grande potere deriva una grande responsabilità diceva lo zio più famoso dell'industria del comics americano): è un tool per smanettoni e soprattutto per chi sa cosa sta facendo, perché per fare tutte queste cose gli dovete dare accesso alla vostra mail, al vostro intero computer, ai vostri tool... e lui lavora non controllato potendo fare potenzialmente grandi danni o esponendovi al rischio di prompt injection di malintenzionati. Io ho fatto girare tutto su una macchina virtuale isolata, accedendo ad account che ho creato solo per il test. Ma l'esperimento è affascinante, e fa capire quello che sarà entro breve con una delega di una parte significativa del lavoro agli agenti, come sa bene chi sta usando estensivamente gli agenti di coding non solo per il coding (di questo parleremo settimana prossima nel [podcast](https://risorseartificiali.com).

D'altra parte le big tech stanno andando in questa direzione, con più cautela per evitare i rischi menzionati sopra: Anthropic con le app MCP in Claude, Google con l'integrazione stretta di Gemini in Chrome (vedi link sotto).

Chiudo questa parte con una promessa: se qualcuno dimostra interesse con commenti o via social, scriverò un articolo passo passo per configurare una macchina virtuale per isolare il più possibile OpenClaw.

### I link della settimana

- **[Anthropic Integrates Interactive MCP Apps into Claude](https://www.testingcatalog.com/anthropic-integrates-interactive-mcp-apps-into-claude/)** - App MCP interattive per Asana, Slack, Figma e Box direttamente in Claude con esperienze live integrate e standard aperti.
- **[Kimi Agent SDK](https://github.com/MoonshotAI/kimi-agent-sdk)** - Interfaccia programmatica per Kimi CLI con client nativi, automazione conversazioni multi-turno e strumenti personalizzati.
- **[Chrome: The browser you love, reimagined with AI](https://blog.google/products-and-platforms/products/chrome/chrome-reimagined-with-ai/)** - Nuova visione di Chrome con AI nativi, automazione intelligente e comprensione contestuale avanzata.
- **[Google begins rolling out Chrome's "Auto Browse" AI agent today](https://arstechnica.com/google/2026/01/google-begins-rolling-out-chromes-auto-browse-ai-agent-today/)** - Agente di navigazione autonoma in split-screen, modifica immagini con Nano Banana e manipolazione pagine con AI.
- **[OpenClaw AI](https://openclaw.ai/)** - Piattaforma emergente per agenti AI autonomi con orchestrazione avanzata e integrazione multi-sistema.

---

## AI Assisted Coding

### I Takeaways per gli AI Engineers

- **Takeaway 1:** L'agentic coding rappresenta il più grande cambio di paradigma degli ultimi 20 anni nello sviluppo software, superando il semplice code completion verso una vera espansione delle capacità
- **Takeaway 2:** Con gli agenti di coding si parla più di espansione che di accelerazione: delegando all'AI si finisce per fare più cose, non solo le stesse cose più velocemente
- **Takeaway 3:** L'isolamento dell'ambiente di lavoro diventa cruciale: sandbox locali come `/sandbox` di Claude-code e soluzioni cloud isolate sono la risposta alle esigenze di sicurezza

- **Action Items:**
  - Se non usi ancora un agente di coding, crea una sandbox isolata e prova: è un cambiamento di paradigma dal quale non si torna indietro
  - Valuta soluzioni cloud per ambienti di sviluppo isolati quando la sandbox locale non è sufficiente per le tue esigenze

### Cosa succede questa settimana?

Mi riaggancio a quello che dicevo prima parlando di OpenClaw: con gli agenti, che siano general purpose o di puro coding, sta diventando sempre più importante isolare l'ambiente di lavoro. E se in locale sandbox che isolano il filesystem (ad esempio claude-code ha un comando `/sandbox` nativo per questo) e development context siano una buona soluzione, stanno prendendo piede anche soluzioni per creare ambienti di sviluppo isolati in cloud. Personalmente non ne ho ancora sentito una forte esigenza, ma l'articolo che riporto sotto mi ha fatto "prudere le mani" in questo senso.

L'altro link che voglio evidenziare è l'articolo/lungo tweet di Andrej Karpathy, che come sapete è una delle mie voci preferite nel mondo dell'AI. Karpathy dice tante cose significative che vi invito a leggere (bastano 3 minuti), ma quelle che mi hanno colpito di più e che sottoscrivo in pieno, avendo avuto esperienze identiche:

- L'agentic coding (attenzione non il code completion AI o cose minori, parla proprio di agentic coding con cose tipo claude-code o Codex o simili) è il più grande cambio di paradigma nello sviluppo del codice che abbiamo sperimentato negli ultimi 20 anni. Nulla da aggiungere.
- Più che di accelerazione si può parlare di espansione. Ovvero delegando e velocizzando molti task all'AI si finisce per fare più cose e non semplicemente le cose di prima più velocemente
- Con gli agenti di coding (specie quando si usano anche per altri task, aggiungo io) si ha la sensazione di cosa sarà l'AGI

Voi non usate ancora un agente di coding? Coraggio, fatevi la vostra sandbox e provateci, come dice Karpathy è il più grande cambio di paradigma degli ultimi 20 anni, e dal quale non si torna indietro.

### I link della settimana

- **[The surprising attention on sprites, exe.dev, and shellbox](https://lalitm.com/trying-sprites-exedev-shellbox/)** - Nuovi servizi VPS Linux ottimizzati per Claude Code, gestiscono sharing servizi web e stack end-to-end senza configurare VM, container o certificati.
- **[Agent Trace: Capturing the Context Graph of Code](https://cognition.ai/blog/agent-trace)** - Specifica aperta vendor-neutral per registrare contributi AI con autorialità umana, rende lo sviluppo leggibile e abilita dashboard management data-driven.
- **[Management as AI superpower](https://www.oneusefulthing.org/p/management-as-ai-superpower)** - La delega efficace all'AI dipende da tempo baseline, probabilità successo e tempo processo: con GPT-5.2 Thinking/Pro, successo medio 72% su GDPval.
- **[Andrej Karpathy Tweet](https://x.com/karpathy/status/2015883857489522876)** - Karpathy commenta agentic coding come più grande cambio paradigma degli ultimi 20 anni: espansione più che accelerazione, sensazione di cosa sarà l'AGI.

---

## Business e società

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Gli ultimi 12-18 mesi mostrano la rincorsa e conquista di Google su tutti i fronti: quota traffico da ChatGPT a Gemini (+315%), accordo Apple per copertura 100% smartphone, produzione TPU con Samsung
- **Takeaway 2:** L'industria AI si sta muovendo verso cicli di supporto molto più brevi: il costo elevato di mantenere modelli vecchi spinge a ritiri rapidi come GPT-4o, aprendo opportunità per soluzioni on-premise enterprise
- **Takeaway 3:** Le mosse di Apple (Q.ai, accordo Gemini) suggeriscono una strategia focalizzata sull'interazione AI-uomo, mentre Amazon copre metà del round da 100 miliardi di OpenAI, potenzialmente portando GPT su Alexa

- **Action Items:**
  - Valuta soluzioni on-premise per stabilizzare i modelli AI nelle tue implementazioni enterprise, dato i cicli di supporto sempre più brevi
  - Monitora l'evoluzione dell'ecosistema Google (Gemini, TPU Samsung, integrazioni) che sta rapidamente erodendo la dominanza di OpenAI su più fronti

### Cosa succede questa settimana?

Sempre tanti soldi che si muovono in Silicon Valley. L'acquisizione di Apple di Q.ai (che fa sistemi vocali), insieme all'accordo con Google per l'uso di Gemini di cui parlavamo settimana scorsa potrebbe rivelare la strategia di Cupertino di concentrarsi sull'interazione AI-uomo. Staremo a vedere.

Amazon che, onestamente, sembra un po' in ritardo (anche se forse il suo focus è sul cloud che fa girare l'AI, sul quale sono tutt'altro che indietro), pare possa essere uno dei principali investitori coprendo la metà del prossimo round di OpenAI da 100 miliardi di dollari. Il che potrebbe essere interessante anche per OpenAI che, dopo aver perso Siri, potrebbe vedere sbarcare il suo modello vocale su Alexa.

Intanto OpenAI taglia qualche costo dismettendo GPT-4o e modelli più vecchi. Su questo è importante notare come il costo elevato di mantenere in vita i modelli più vecchi stia spingendo l'industria a cicli di supporto molto più brevi rispetto alle tecnologie precedenti. L'esigenza di avere modelli più stabili, una volta raggiunte le performance desiderate, potrebbe spingere il mercato enterprise a valutare soluzioni on-premise.

Concludo questa sezione con l'analisi di quanto gli ultimi 12-18 mesi siano stati una grande rincorsa e poi conquista di Google su tutti i fronti: tantissimi punti percentuali del traffico dei chatbot si sposta da ChatGPT a Gemini, accordo con Apple porta Gemini (ovviamente già presente su Android) su praticamente il 100% degli smartphone, l'accordo con Samsung per la produzione delle TPU li toglie dalla concorrenza con Nvidia per avere slot produttivi di TSMC accelerando anche su quel fronte. E di questi giorni è l'indiscrezione che sarà presto possibile importare in Gemini le conversazioni avute con ChatGPT (in realtà lo è già, ma richiede di essere un po' smanettoni... ora diventa un bottone), con l'intento di abbattere anche l'ultima resistenza degli utenti ad abbandonare "il primo arrivato" per non perdersi la storia delle proprie chat.

### I link della settimana

- **[Amazon could invest up to $50 billion in OpenAI in coming weeks, source says](https://www.cnbc.com/2026/01/29/amazon-openai-investment-jassy-altman.html)** - Amazon in trattativa per 50 miliardi in OpenAI, potenziale uso chip AI Amazon, nonostante precedenti investimenti in Anthropic.
- **[Apple Acquires Q.ai](https://techcrunch.com/2026/01/29/apple-buys-israeli-startup-q-ai-as-the-ai-race-heats-up/)** - Apple acquisisce startup israeliana Q.ai specializzata in audio AI per avanzare riconoscimento vocale sussurrato e enhancement per AirPods e Vision Pro.
- **[Google Trusting Samsung for AI TPU Manufacturing](https://www.sammyfans.com/2025/12/25/google-trusting-samsung-for-ai-tpu-manufacturing/)** - Google affida a Samsung produzione chip TPU per AI, partnership strategica nel settore semiconduttori ML e diversificazione supply chain.
- **[Retiring GPT-4o and Older Models](https://openai.com/blog/retiring-gpt-4o)** - GPT-4o, GPT-4.1, GPT-4.1 mini ritirati il 13 febbraio per semplificare capacità e transizione verso GPT-5, nessun cambiamento API simultaneo.
- **[ChatGPT Traffic Analysis: Lead Shrinks as Gemini Surges](https://ppc.land/chatgpts-lead-shrinks-as-gemini-surges-in-ai-traffic-war/)** - ChatGPT scesa dall'86.6% al 64.6% in 12 mesi (-22 pp), Gemini esplosa dal 5.3% al 22% (+315%), inversione trend mercato AI.

