Benvenuti alla newsletter di questa settimana. Tante novità importanti: OpenAI rilascia GPT-5.4 con performance notevoli, mentre Alibaba lancia la famiglia Qwen 3.5 con un modello da 9 miliardi di parametri che batte il GPT open source da 120 miliardi — la notizia della settimana sui modelli. Google risponde con Gemini 3.1 Flash-Lite, puntando su velocità e costi bassi. Sul fronte agenti, l'influenza di OpenClaw si fa sentire ovunque: dalle automazioni di Cursor alla tesi che MCP sia morto in favore delle CLI. Per il coding assistito, vi presentiamo LINCE, il nostro progetto open source, e discutiamo di come le code review tradizionali siano destinate a cambiare. Infine, nel business, lo scontro Anthropic-Pentagono si evolve, OpenAI raccoglie 110 miliardi di dollari e Amodei ci ricorda che il pensiero critico resta il nostro ultimo vero vantaggio.

Prima di lasciarvi alla lettura delle notizie e delle mie analisi di cosa è successo in settimana, fatemi dire cosa è successo, sta per succedere o succederà nella mia agenda pubblica, per chi volesse seguire i miei interventi o volesse incontrarmi di persona (adoro scambiare opinioni con chiunque abbia voglia di farlo):

* [Podcast](https://risorseartificiali.com) con Alessio e Paolo:
  * Il 12 marzo saremo al JUG di Milano per registrare la nostra prima puntata live. [Non mancate](https://www.eventbrite.com/e/risorse-artificiali-appunti-e-spunti-dal-mondo-dellai-tickets-1983617212480?aff=oddtdtcreator)
  * Sabato è uscita una puntata in cui torniamo a parlare diffusamente di AI coding, agenti, e tante novità
  * Stiamo lavorando ad altre interviste e puntate con ospiti molto interessanti
  * Abbiamo creato un repository su GitHub con tools e configurazioni per fare AI coding da terminale su Linux. Ovviamente open source, quindi dateci un'occhiata e contribuite: [LINCE - Linux Intelligent Native Coding Environment](https://github.com/RisorseArtificiali/lince)
* Da solo:
  * Mi hanno intervistato di nuovo al podcast Open Source. Stavolta parlo di agenti, AI, AGI. [Uscita qui il 26](https://open.spotify.com/show/3EAhXkBUmHE1a8vFTH84Yg?si=bacd744b0f9c4a55). Ascoltatela e fatemi avere i vostri commenti
  * Il 24 marzo sarò al Voxxed Day a Zurigo. Io e Alessio [presentiamo un talk sull'AI assisted coding](https://vdz26.voxxeddays.ch/talk/?id=8057)
  * Il 25 marzo sarò speaker in questo meetup a Milano sul [Vibe Coding e Agentic Engineering](https://www.eventbrite.it/e/biglietti-meetup-13-vibe-coding-1983538213191?aff=ebdssbcategorybrowse)
  * Il 30 maggio avrò l'onore di essere uno dei PyCon Italia [speakers](https://2026.pycon.it/en/speakers)

Ma partiamo dall'AI research, perché anche questa settimana ci sono novità rilevanti sul fronte dei modelli.

## 🧠 Novità e ricerca nei modelli AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** La competizione sui modelli si gioca su tre assi: prestazioni pure (GPT-5.4), efficienza/costo (Gemini 3.1 Flash-Lite) e modelli piccoli ad alte prestazioni (Qwen 3.5). Non c'è più un singolo vincitore.
- **Takeaway 2:** Qwen 3.5-9B che batte gpt-oss-120B dimostra che la dimensione del modello conta meno dell'architettura: i modelli cinesi open source ridefiniscono il rapporto prestazioni/parametri.
- **Takeaway 3:** NotebookLM con video cinematici segna il passaggio da "AI che riassume" a "AI che produce contenuti multimediali completi".

- **Action Items:**
  - Provare GPT-5.4 e Qwen 3.5-9B su un task concreto del proprio workflow per confrontare prestazioni e costi reali.
  - Sperimentare NotebookLM Cinematic Video Overviews per valutare se può sostituire strumenti di presentazione tradizionali.

### Cosa succede questa settimana?

Come sempre, tante novità nel mondo dei modelli. Incominciamo dal nuovo modello in casa OpenAI, GPT-5.4, che porta tante novità e delle performance davvero notevoli, sia per quanto leggo nei benchmark che per le prime opinioni che ho letto sui social. Questa sembra essere la risposta di OpenAI a quanto di buono sta facendo Anthropic con i suoi modelli Claude, sia Opus che Sonnet. Google risponde invece con Gemini 3.1 Flash-Lite, in cui punta soprattutto alla velocità e ai costi bassi: è il più piccolo e il più veloce della serie Gemini. Ma se parliamo di modelli piccoli e veloci, la notizia assolutamente della settimana (ma forse notizia della settimana in generale sui modelli) è l'uscita dei modelli Qwen 3.5. Come sempre per Qwen, si tratta di una famiglia di modelli nativamente multimodale e che ha diverse dimensioni, a partire da 0.8 miliardi di parametri fino a modelli molto grandi, mixture of experts, con grandi prestazioni. In particolare è interessante l'articolo che confronta la versione a 9 miliardi che batte per ragionamento e benchmark la versione GPT open source a 120 miliardi. Un risultato davvero notevole per i modelli cinesi, che viene proprio da Qwen, che ricordo essere fatto da Alibaba, quindi una delle grandi big tech mondiali e sicuramente la più grande in Cina. Infine, segnalo la nuova feature, per ora in prova riservata ad alcuni utenti, di NotebookLM che, usando Gemini 3 e Veo, è in grado di generare dei video che non sono più soltanto presentazioni di slide ma dei veri e propri documentari.

### I link della settimana

- [Introducing GPT-5.4](https://openai.com/index/introducing-gpt-5-4/) — GPT-5.4 con contesto 1M token, tool search, visione migliorata e 33% meno errori fattuali rispetto a GPT-5.2.
- [Deep Dive: Qwen 3.5](https://trilogyai.substack.com/p/deep-dive-qwen-35-brings-native-multimodality) — Qwen 3.5 con multimodalità nativa, contesto 262K token e architettura ibrida per deployment edge da 0.8B parametri.
- [Gemini 3.1 Flash-Lite](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) — Il modello più veloce e conveniente della serie Gemini 3, a partire da $0.25/M token in input.
- [Cinematic Video Overviews in NotebookLM](https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/) — NotebookLM genera video cinematici dalle fonti utente usando Gemini 3 e Veo 3.
- [Qwen3.5-9B Beats gpt-oss-120B](https://venturebeat.com/technology/alibabas-small-open-source-qwen3-5-9b-beats-openais-gpt-oss-120b-and-can-run) — Qwen3.5-9B supera gpt-oss-120B sui benchmark, disponibile open source con licenza Apache 2.0.

## 🤖 Agentic AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** L'influenza di OpenClaw è visibile ovunque: memoria persistente, automazione goal-driven e CLI come interfaccia per agenti stanno diventando pattern dominanti nel settore.
- **Takeaway 2:** La tesi "MCP è morto" trova conferma pratica nell'esplosione di CLI dedicate (Google Workspace CLI in testa): strumenti esistenti e ben documentati battono protocolli nuovi.
- **Takeaway 3:** GAM dimostra che la memoria agentica efficace non è solo "salvare tutto", ma sintetizzare on-demand con un approccio ispirato alla compilazione just-in-time.

- **Action Items:**
  - Esplorare Cursor Automations per costruire agenti ricorrenti nel proprio workflow di sviluppo.
  - Leggere il paper GAM per valutare come applicare l'approccio Memorizer/Researcher alla gestione della memoria nei propri agenti.

### Cosa succede questa settimana?

Nelle notizie di questa settimana relative agli agenti mi sembra abbastanza evidente intravedere un'influenza da parte di OpenClaw. Cerco di spiegarmi. Una delle caratteristiche di OpenClaw era sicuramente quella di avere un'automazione forte basandosi su quanto imparava dalla memoria. Questa caratteristica la ritroviamo sia nelle automazioni di Cursor — e qui il parallelo è abbastanza forte. Cursor Automations introduce agenti che girano su schedule, creano le proprie sandbox e soprattutto hanno accesso a un tool di memoria che permette di imparare dalle esecuzioni passate. È esattamente la logica della "fabbrica che produce il software" — un concetto che chi segue OpenClaw riconoscerà immediatamente. Lo ritroviamo anche nei test che sta facendo Google per quello che loro chiamano Learning Hub, dove gli agenti imparano autonomamente basandosi su obiettivi definiti. Queste due cose ricordano da vicino quello che OpenClaw fa in questo ambito. O quantomeno possiamo dire che, se non è un'influenza diretta, le stesse spinte che hanno portato allo sviluppo di OpenClaw stanno portando anche altri a fare ricerca nella stessa direzione. Un'altra delle caratteristiche di OpenClaw è quella di usare CLI al posto di MCP. In questo senso sono interessanti sia l'articolo che prende una posizione forte dicendo che MCP è morto, ma anche e soprattutto l'uscita di tantissime CLI nelle ultime settimane per fare le cose più svariate. Il punto chiave dell'articolo è semplice ma potente: gli LLM sono già bravi a capire le cose da soli, tutto ciò di cui hanno bisogno è una CLI e della documentazione. Non servono protocolli nuovi quando gli strumenti esistono già e funzionano bene sia per umani che per agenti. Ultimo ma non ultimo, quella da parte degli ingegneri di Google per interagire con tutto il Workspace, quindi da Gmail al calendario a Google Drive e tutto quanto relativo a Workspace. Infine, vi segnalo una ricerca chiamata General Agentic Memory via Deep Research che vale la pena di essere letta. Si tratta di un framework di memoria per agenti. Ci sono parecchie idee interessanti in questa ricerca e vi invito a leggerla, in particolare avendo attenzione per l'approccio che ricorda in qualche modo la compilazione just-in-time che troviamo in alcuni linguaggi, applicata però al contesto e al linguaggio naturale. In pratica, GAM usa due componenti — un Memorizer che mantiene riassunti leggeri e un Researcher che recupera e sintetizza informazioni rilevanti solo quando servono. È un'alternativa elegante al classico approccio "salva tutto in un vector store" che domina oggi il panorama agentico.

### I link della settimana

- [Cursor Automations](https://cursor.com/blog/automations) — Agenti always-on su schedule o eventi con sandbox cloud e memoria per imparare dalle esecuzioni passate.
- [Google Workspace CLI](https://github.com/googleworkspace/cli) — CLI unificata per tutti i servizi Google Workspace, progettata per umani e agenti AI con 100+ skills.
- [GAM: General Agentic Memory Via Deep Research](https://arxiv.org/abs/2511.18423) — Framework di memoria agentica con approccio JIT: Memorizer per riassunti leggeri e Researcher per sintesi on-demand.
- [Google Tests Learning Hub with Goal-Based Actions](https://www.testingcatalog.com/google-tests-new-learning-hub-powered-by-goal-based-actions/) — Gemini "Goal Scheduled Actions": l'AI aggiusta autonomamente i task verso obiettivi definiti.
- [MCP Is Dead. Long Live the CLI](https://ejholmes.github.io/2026/02/28/mcp-is-dead-long-live-the-cli.html) — Le CLI sono più pratiche di MCP per umani e agenti: strumenti esistenti, ben documentati e universali.

## 💻 AI Assisted Coding

### I Takeaways per gli AI Engineers

- **Takeaway 1:** LINCE dimostra che Linux e il terminale restano l'ambiente più naturale per lo sviluppo AI-assisted: sandbox, backlog e assistenza vocale integrati in un'unica sessione.
- **Takeaway 2:** Le code review tradizionali stanno diventando il collo di bottiglia dello sviluppo AI-assisted: servono nuovi modelli basati su intenzioni e criteri di accettazione, non ispezione riga per riga.
- **Takeaway 3:** L'introduzione degli evals nello skill-creator di Anthropic segna un cambio di paradigma: il contesto testato batte il contesto ridotto per migliorare le performance degli agenti di coding.

- **Action Items:**
  - Provare LINCE e contribuire al progetto open source con feedback, bug report o pull request.
  - Iscriversi al workshop Packt Publishing su refactoring AI con ast-grep e Claude Code (14 marzo 2026).

### Cosa succede questa settimana?

Partiamo da una cosa un po' autoreferenziale ma a cui tengo molto. Insieme agli altri ragazzi del podcast Risorse Artificiali abbiamo iniziato un progetto open source che abbiamo chiamato LINCE, che sta per Linux Intelligent Native Coding Environment. Un nome complicato per rendere pubblico quello che noi usiamo tutti i giorni. In pratica abbiamo messo insieme una serie di script, configurazioni e anche alcuni software che abbiamo sviluppato con l'aiuto di agenti intelligenti per aiutarci nel lavoro di tutti i giorni come AI-assisted developer. Si tratta in pratica di avere un'integrazione di Claude Code con un backlog, con un assistente vocale che abbiamo chiamato VoxCode e con una sandbox fatta tutta in user space Linux. So che probabilmente starete pensando che molte di queste cose esistono già nativamente in Claude Code, ma il punto è che la maggior parte di queste non funzionano o non funzionano bene all'interno di un sistema Linux. E noi crediamo che Linux possa essere invece il sistema in cui fare sviluppo all'interno del terminale, visto che è il sistema operativo che meglio integra il terminale di tutti quanti. Se vi va, andate a darci un'occhiata, provatelo, lasciateci commenti, feedback, aprite qualche baco se ne trovate o magari mandateci qualche pull request. Grazie.

Una delle cose a cui magari daremo un occhio è anche come automatizzare, o meglio rendere più semplici e più dirette, le code review. Perché le code review stanno diventando proprio il collo di bottiglia e forse anche una delle cose che avranno bisogno di essere riviste man mano che il codice generato dagli agenti intelligenti diventerà sempre maggiore. È molto interessante l'articolo che vi propongo, intitolato "How to Kill the Code Review", in cui appunto si discute come il metodo tradizionale di code review possa diventare insostenibile nell'era dell'AI e come invece ci si potrebbe focalizzare di più su altri criteri, tra cui l'accettazione delle cosiddette intenzioni di sviluppo. Leggetelo, ne vale la pena.

Così come vale la pena dare un'occhiata all'articolo che parla dell'importanza di aver inserito gli evals nella creazione delle skill da parte di Anthropic. Come l'articolo spiega bene, è un cambio di paradigma importante che vale la pena di essere approfondito.

Infine, vi segnalo un workshop di 90 minuti organizzato da Packt Publishing che copre gli aspetti del refactoring usando l'AI coding. Il formatore è anche l'autore di una libreria che si chiama ast-grep e usa proprio l'approccio AST per guidare Claude Code nella fase di refactoring, riducendo molto le regressioni e rendendo il processo di refactoring molto più lineare. Credo che approcci misti come questo possano essere assolutamente significativi per migliorare ulteriormente l'esperienza di coding assistito. Io sono già iscritto a quel workshop, se vi va dateci un'occhiata.

### I link della settimana

- [How to Kill the Code Review](https://www.latent.space/p/reviews-dead) — Le code review tradizionali sono insostenibili con l'AI: serve focalizzarsi su specifiche e criteri di accettazione.
- [LINCE - Linux Intelligent Native Coding Environment](https://github.com/RisorseArtificiali/lince) — Workstation agentica su terminale Linux con Claude Code sandboxed, task board e assistenza vocale.
- [Anthropic Brings Evals to Skill-Creator](https://tessl.io/blog/anthropic-brings-evals-to-skill-creator-heres-why-thats-a-big-deal/) — Evals integrate nello skill-creator di Anthropic per testare e validare skill AI automaticamente.
- [Safely Refactor Production Codebases with AI — Workshop](https://www.eventbrite.com/e/safely-refactor-production-codebases-with-ai-registration-1982005923070?aff=artificialcode) — Workshop (14 marzo 2026) su refactoring sicuro con ast-grep e Claude Code su codebase di produzione.

## 🏢 Business e società

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Amodei ribadisce che il pensiero critico è l'ultimo vero vantaggio competitivo umano, mentre il coding diventa commodity: un messaggio chiaro su dove investire le proprie competenze.
- **Takeaway 2:** Lo scontro Anthropic-Pentagono e il successivo accordo OpenAI-Dipartimento della Guerra sollevano domande irrisolte: le red line etiche sono reali vincoli o strumenti negoziali?
- **Takeaway 3:** OpenAI a $730B di valutazione e 900M di utenti settimanali dimostra che il mercato AI consumer è ormai mainstream, indipendentemente dal dibattito tecnico sui modelli.

- **Action Items:**
  - Leggere il paper Anthropic sugli impatti sul mercato del lavoro per capire dove l'AI sta già cambiando le dinamiche occupazionali nel proprio settore.
  - Guardare l'intervista integrale di Amodei a Bangalore per approfondire la sua visione sulla concentrazione di potere nell'AI.

### Cosa succede questa settimana?

Ormai lo avrete capito, quando Dario Amodei parla io non mi perdo di certo la sua intervista. Ne è uscita una nuova, un'intervista intera che ha rilasciato a Bangalore, in cui si concentra su come le competenze di coding siano in declino e quanto il pensiero critico possa essere il vantaggio competitivo da preservare per gli esseri umani. Parla anche di come la concentrazione del potere con le AI possa diventare un problema ancora più grande di quanto non sia stato in passato.

E in effetti, come ben sapete, in questo periodo Amodei e Anthropic hanno preso posizione rispetto al Dipartimento della Guerra degli Stati Uniti e il Pentagono, ritirandosi da un accordo milionario. Questa cosa ha avuto svariate evoluzioni: vi riporto l'ultima risposta da parte di Amodei e di Anthropic riguardo a questo scontro, in cui loro sono stati accusati di essere un rischio per la supply chain di sicurezza nazionale. Danno una risposta molto forte, che trovate nell'articolo che ho riportato. Ovviamente il Dipartimento americano non sta fermo e nel frattempo ha fatto altri accordi, nella fattispecie con OpenAI, i quali dichiarano di aver messo delle red line contro gli argomenti che hanno fatto discutere e che hanno spinto Anthropic a ritirarsi. Personalmente, a me sembra strano che Anthropic si sia ritirata perché quelle red line sono state superate e poi il Dipartimento della Guerra americano abbia firmato un accordo con un'altra compagnia rispettandole invece. Qualcosa non torna.

Nel frattempo OpenAI continua a fare il suo business e ha raccolto altri 110 miliardi di dollari, arrivando a una valutazione di 730 miliardi di dollari: 900 milioni di utenti attivi settimanali, 50 milioni di abbonati consumer e 9 milioni di abbonati business. Direi che l'azienda comunque sta andando bene, a dispetto di qualche dubbio che ha sollevato negli ultimi mesi rispetto ai concorrenti, che sembrano essere andati avanti più velocemente.

Concludo segnalandovi un altro paper da parte di Anthropic che analizza il mercato del lavoro e gli impatti reali che l'AI sta già avendo: diversi da quelli che forse ci si aspettava qualche mese fa, ma comunque estremamente interessanti da leggere.

### I link della settimana

- [Where Things Stand with the Department of War](https://www.anthropic.com/news/where-stand-department-war) — Anthropic risponde alla designazione come rischio per la supply chain di sicurezza nazionale, annuncia azione legale.
- [Labor Market Impacts of AI](https://www.anthropic.com/research/labor-market-impacts) — Nuovo framework Anthropic per misurare gli impatti reali dell'AI sui mercati del lavoro.
- [Dario Amodei — Full Interview](https://www.youtube.com/watch?v=68ylaeBbdsg) — Intervista integrale a Bangalore: coding in declino, pensiero critico come vantaggio umano, concentrazione di potere nell'AI.
- [OpenAI's Agreement with the Department of War](https://openai.com/index/our-agreement-with-the-department-of-war/) — Accordo classificato con red line contro sorveglianza di massa, armi autonome e decision-making automatizzato.
- [OpenAI Raises $110B at $730B Valuation](https://openai.com/index/scaling-ai-for-everyone/) — Round da $110B, 900M utenti settimanali, 50M abbonati consumer, 9M business paganti.

