# This Week in AI - CY26W4

## Introduzione

Da oggi si cambia il modo di scrivere questa newsletter. Chi mi conosce bene sa che io nella comfort zone sono irrequieto e quando una cosa inizia a prendere una routine mi piace fermarmi un attimo, guardare indietro e mettermi in discussione. E complice i miei colleghi di [podcast](https://risorseartificiali.com) ho deciso di rivedere il mio processo creativo della newsletter perché fosse un po' più human-driven o human-centric. Che non significa che io non usi più l'AI nel mio processo creativo, ma la uso in un modo diverso, perché oggi escludere l'AI dalla propria produzione intellettuale è quantomeno irragionevole (Antirez docet, vedi il capitolo su AI assisted coding), ma l'uso che se ne fa è tanto migliorativo del risultato finale quanto è consapevole e controllato.

Ma prima di raccontarvi come ho cambiato questa cosa, lasciatemi commentare l'immagine di copertina (che stavolta non è generata, ma su questo nessuna promessa). Il libro che vedete lì, vicino a una montagna di arachidi, è [Agentic Design Pattern di Antonio Gulli](https://amzn.eu/d/e01u45q). Come dicevo nel mio [post LinkedIn](https://www.linkedin.com/posts/maeste_ognuno-ha-le-sue-metriche-per-il-gradimento-activity-7420382061892546560-pGXK?utm_source=share&utm_medium=member_desktop&rcm=ACoAAADPXZoBb_9NISS3o9qVhN7rHVKEQx81fWk) da cui ho preso l'immagine, ognuno ha le sue metriche per misurare il gradimento di un libro... il mio sono il numero di arachidi che mangio durante la lettura... e quelle della foto sono solo una piccola parte. Consiglio spassionato, se state progettando un sistema ad agenti o se li volete anche solo usare, compratelo, leggetelo e tenetelo sul comodino.

Torniamo alla newsletter. Il processo di creazione fino ad oggi era più o meno questo:

* Raccolta link e lettura articoli
* Organizzazione dei link più significativi
* Aggiunta di miei commenti per ogni sezione in forma di lista di punti
* AI... scrivi (con un formato e uno stile preparato in precedenza)

Poi ieri, stimolato dai commenti di Paolo e Alessio mi sono fermato a farmi delle domande (tecnica 3 whys):

* Perché ho iniziato a scrivere una newsletter? Per condividere le cose che leggo in settimana... ok... ma soprattutto perché mi è sempre piaciuto scrivere e scrivere è il mio modo di rielaborare e memorizzare informazioni. Ma di fatto non sto più scrivendo...
* Perché ho sentito l'esigenza di passare all'AI i miei punti e farle fare un testo per gli altri? Due motivi, perché ho poco tempo, e perché voglio un testo più lungo e discorsivo. Ma questo presuppone che i miei lettori abbiano più tempo di me... hmmm forse non è né vero né pagato.
* Perché un'ennesima newsletter può avere senso? Per elaborare meglio il mio pensiero e condividerlo con gli altri. E siamo tornati ad uno dei motivi per cui scrivere, elaborare il mio pensiero ed aggiungere il mio punto di vista. Ma un elenco per punti rielaborato dall'AI fa questa cosa? Solo in parte.

Quindi ho invertito le parti, lasciando che l'AI facesse da ufficio di redazione (pulizia link, sintesi dei testi che comunque io avevo già letto) e correttore di bozze, lasciando a me l'onore e l'onere di unire i puntini e creare il testo.

Quello che troverete nei capitoli qui sotto ha un formato leggermente diverso dalle precedenti newsletter (assomigliando un po' di più ai primi numeri in realtà), in cui l'unica parte scritta dall'AI è l'elenco di link e il loro riassunto. Il testo di "Cosa succede questa settimana?", Takeaways e Action Items sono tutti miei, con l'AI che fa da editor e da ufficio di redazione per controllare correttezza e coerenza.

Altra piccola modifica, una più rigorosa selezione dei link forniti, riducendoli di numero e cercando di trasferirvi quelli più significativi. Lasciatemi un commento con un vostro sincero feedback di cosa ne pensate.

Sono certo che qualcuno non ci crederà... dato che Paolo e Alessio mi hanno accusato di aver scritto "troppo con l'AI" anche il post LinkedIn di commento al libro sopra... e giuro che invece l'ho scritto tutto a mano, anche dopo una birra di troppo :)

Se siete curiosi di come ho impostato questo processo con l'AI che diventa davvero un co-worker con l'uso di un CLI e di skills specifiche, lasciate anche questo in un commento e ve lo racconto in uno dei prossimi numeri della newsletter... o magari in un'edizione straordinaria ;)

---

## 🧠 Novità e ricerca nei modelli AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** La ricerca sui modelli reasoning è tutt'altro che ferma e stiamo scoprendo nuove strade per far pensare i modelli
- **Takeaway 2:** Pensare per immagini è uno strumento potente per gli uomini, lo diventerà per i modelli e per i robot
- **Takeaway 3:** Strumenti come Cowork cambieranno il modo di lavorare davanti ad uno schermo

- **Action Items:**
  - Tenete un occhio sulle ricerche in arxiv.org
  - Provate a implementare flussi di lavoro (non codice) con Claude Code o Claude Cowork

### Cosa succede questa settimana?

Il paper del primo link che propongono (DASD) ha degli impatti immediati ed altri meno evidenti. Su questi ultimi mi voglio concentrare un attimo per darvi una visione di insieme di dove sta andando la ricerca in questo campo. Il paper parla tra l'altro del problema dell'overthinking che in sostanza rende molto più lunghe le chain of thoughts. DASD è proprio (una delle) proposta di soluzione a questo problema. Perché è fondamentale? Perché chain più corte permettono a parità di contesto di esplorare soluzioni multiple (multiple chains) ed in sostanza ottenere risultati migliori.

Il secondo link è di nuovo un paper, che esplora il ragionamento visuale. Chi mi segue sa che ne ho parlato spesso sia qui in newsletter che in [podcast](https://risorseartificiali.com), perché ritengo che sia una delle prossime significative evoluzioni nei modelli di reasoning. Se ci pensate quante volte vi siete fatti uno schizzo o un diagramma per ragionare meglio su un problema? Eccolo ora che modelli come Nanoban e altri sono bravissimi a creare questi schizzi o diagrammi, perché non usare le capacità multimodali di interpretazione di immagini complesse anche nella fase di reasoning? Abbiamo fatto lo stesso per i tools, che dapprima non entravano nel reasoning (ma ora lo fanno un po' tutti da ChatGPT 5.x, a Gemini 3 passando per modelli cinesi come Minimax e GLM) e con ottimi risultati. Io personalmente mi aspetto grandi cose dal ragionamento visuale.

Infine una novità che sta arrivando da Anthropic che potrebbe cambiare radicalmente il modo di lavorare sui nostri PC, Cowork fa quello che Claude Code già fa per i più tecnici e promette di caricare contesti dinamici per qualunque tipo di documento...come fa Claude Code con il codice (e altro). Il mio suggerimento è di non perdere di vista cosa sta succedendo nel mondo Claude, perché arriverà presto sulla vostra scrivania. E se vi fidate di me, avete già tutto questo in Claude Code, se solo vi volete "sporcare le mani" usando un terminale.

### I link della settimana

**[Distribution-Aligned Sequence Distillation (DASD)](https://arxiv.org/abs/2601.09088)**

Nuovo pipeline di distillazione per modelli di ragionamento compatti che affronta l'overthinking tramite distillazione selettiva su token CoT. DASD-4B-Thinking è completamente open-source e supera modelli molto più grandi.

**[Render-of-Thought: Visualizing Reasoning Chains](https://arxiv.org/abs/2601.14750)**

Framework che converte passaggi di ragionamento testuali in rappresentazioni visuali usando VLM, raggiungendo compressione 3-4x mantenendo prestazioni competitive.

**[Anthropic works on Knowledge Bases for Claude Cowork](https://www.testingcatalog.com/anthropic-works-on-knowledge-bases-for-claude-cowork/)**

Anthropic prepara un aggiornamento fondamentale a Claude con modalità Cowork e Knowledge Bases: repository persistenti consultabili per contesto rilevante, aggiornabili incrementalmente.

## 🤖 Agentic AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** La personal intelligence di Google può cambiare ulteriormente il panorama degli agenti. Il fatto che proattivamente attinga a risorse è il cambiamento fondamentale, da tenere in conto anche per i vostri sviluppi. Non più RAG (pull) ma context push.
- **Takeaway 2:** La sicurezza è una priorità sempre. Ancora di più con la GenAI, sia perché il linguaggio naturale sembra più innocuo, sia perché fa sentire anche i non-programmatori in grado di programmare
- **Takeaway 3:** Evals come fondamento dell'Agentic AI: Gli evals sono sia strumenti di sviluppo (Eval Driven Development) che sistemi di monitoraggio continuo in produzione, necessari per gestire l'indeterminismo dei sistemi agentic AI

- **Action Items:**
  - Provate il plugin Claude per Chrome per sperimentare l'agentic browsing e confrontate le vostre esperienze con le future integrazioni Gemini-Chrome
  - Implementate una strategia di evals completa: Eval Driven Development in sviluppo + monitoring continuo in produzione per i vostri agenti

### Cosa succede questa settimana?

Settimana scorsa abbiamo parlato di Personal intelligence di Google (e l'ho fatto anche in [podcast](https://risorseartificiali.com)) che porta l'intelligenza di Gemini a cercare in modo proattivo informazioni nei vostri documenti, fotografie, impegni, luoghi visitati...insomma in tutti quei dati che ogni giorno date (anzi diamo) a Google. La potenzialità è enorme, anche se come diceva lo zio di Peter Parker "da un grande potere deriva una grande responsabilità". Google ha annunciato questa settimana che questa onnipotenza non sarà data solo all'app di Gemini, ma anche ad AI mode nella normale ricerca Google. Tenetelo presente. Parallelamente si fa un gran parlare, ma ancora non si è visto niente, di una integrazione di Gemini in Chrome. Avendo provato (e usando sempre più spesso) il plugin per Chrome di Claude, mi aspetto grandi cose da quella integrazione, perché far agire un agente su una delle pagine aperte, con licenza di navigare per voi è realmente mindblowing. Se potete provatelo e fatemi sapere cosa ne pensate.

Ma come dicevamo ci sono le grandi responsabilità e la sicurezza è una di quelle. Un articolo di quelli selezionati parla nello specifico di sicurezza delle [skills](https://agentskills.io) che essendo puro testo possono sembrare innocue e invece vi si possono nascondere worms che sfruttano proprio l'intelligenza dei modelli per essere ancora più pericolosi e dannosi. Un altro articolo parla invece più in generale della necessità di un runtime (sistema operativo se volete spingervi oltre) per gli agenti. Un'idea del genere, presente in numerosi paper di ricerca e articoli negli ultimi mesi, ha parecchi impatti anche sulla sicurezza. Parlerò proprio di sicurezza legata alla Generative AI, in un [panel al Voxxed Day Ticino ad inizio febbraio](https://vdt26.voxxeddays.ch/talk/?id=5409), magari ci vediamo lì.

Gli Evals in AI generativa, specialmente nel mondo degli agenti sono una risorsa fondamentale che ogni AI Engineer dovrebbe conoscere bene. L'articolo che propongo questa settimana si focalizza sul loro uso per monitorare eventuali cause che fanno degradare le performance (intese come bontà delle risposte e non come velocità). Ma gli evals sono fondamentali anche in fase di sviluppo e sempre di più si sente parlare di evals driven development, come una evoluzione nel mondo degli agenti del test driven development. E se ci pensate non può che essere così: in un mondo dove il software ha risultati indeterministici e valutati per percentuale di successo anche i test devono essere sostituiti con qualcosa che segua la stessa filosofia. Gli evals per l'appunto.

### I link della settimana

**[AI Engineering Has a Runtime Problem](https://mikemason.ca/writing/ai-coding-agents-jan-2026/)**

Il 57% delle aziende esegue agenti AI in produzione, ma manca un runtime standardizzato per gestire stato, streaming, isolamento e scaling.

**[Thoughts on Evals](https://www.raindrop.ai/blog/thoughts-on-evals)**

Monitoring in produzione genera miliardi di label mensili, offrendo insight real-world superiori alle eval statiche.

**[Supply-chain risk of agentic AI - infecting infrastructures via skill worms](https://blog.lukaszolejnik.com/supply-chain-risk-of-agentic-ai-infecting-infrastructures-via-skill-worms/)**

Le "skill worms" sono un rischio emergente: codice malevolo può diffondersi attraverso la supply chain degli skill AI.

**[Google brings Personal Intelligence to AI Mode in Search](https://blog.google/products-and-platforms/products/search/personal-intelligence-ai-mode-search/)**

Google introduce "Personal Intelligence" in AI Mode nella Ricerca, permettendo l'accesso a Gmail e Photos per risposte personalizzate.

## 💻 AI Assisted Coding

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Il pragmatismo vince sul pregiudizio: Anche un creatore di Redis scettico come Antirez riconosce che l'AI-assisted coding è ormai troppo efficace per ignorarlo. L'AI non sostituisce il programmatore esperto, ma lo potenzia (Antirez++).
- **Takeaway 2:** Dai copilot agli agenti: Il passo successivo al code completion è l'agentic coding con contesto, pianificazione e capacità di gestire progetti complessi. Claude Code 2.0 e tool come Devin rappresentano questa evoluzione.
- **Takeaway 3:** I nuovi colli di bottiglia: Con il coding più veloce, i problemi si spostano su specifiche, gestione task, code review e sicurezza. Tool come Devin Review e Tasks in Claude Code affrontano questi aspetti.

- **Action Items:**
  - Leggete l'articolo di Antirez e provate a fare il salto dal code completion all'agentic coding con Claude Code o altri tool simili
  - Implementate processi di code review AI-assisted (Devin Review o simili) e sistemi di task management (backlog.md, Tasks in Claude Code) per gestire il flusso accelerato

### Cosa succede questa settimana?

Non posso che partire dall'articolo di Salvatore Sanfilippo (Antirez) che mi ha molto colpito. In passato e anche nell'articolo stesso, Antirez (creatore di Redis, che di certo non ha bisogno di presentazioni), non si definisce un fan dell'AI anzi ha espresso anche critiche sull'argomento. Ma in questo articolo arriva a dire che "ora è chiaro che per la maggior parte dei progetti, scrivere il codice tu stesso non ha più senso, se non per divertimento" spiegando come l'AI assisted coding possa dare un boost nella produttività anche di un programmatore top come lui. È pragmatico e chiaro nel dire che oggi non ha nessun senso essere negazionisti, come anche Kent Beck ha più volte sottolineato. Salvatore dice che con l'aiuto di un coding agent è riuscito a completare 4 task molto complessi con una certa facilità. Aggiungo una mia nota: il fatto che ci fosse lui al timone di quell'agente fa tutta la differenza del mondo. Non tutti diventano Antirez con l'AI, ma diciamo che Antirez diventa Antirez++ e questo vale per tutti i programmatori e professionisti che vogliano approfondire questo strumento.

Non vi siete ancora avvicinati all'agentic coding e magari siete rimasti al completamento di codice evoluto con l'AI. Il secondo articolo merita una lettura perché parla proprio di come fare quel passo (verso Claude Code nella fattispecie) con successo.

A chi mi chiede dove si stanno spostando i problemi e i colli di bottiglia con tutto questo coding più veloce ed "aiutato" rispondo sempre: specifiche, gestione dei task per l'agente, code review, sicurezza. Di sicurezza ho parlato nella sezione precedente. Nei link di questa sezione potete trovare la risposta che Devin cerca di dare alla code review, molto interessante perché non si limita ad aggiungere AI in quella fase (che sposta solo un po' più là il problema), ma usa l'AI per rendere più semplice ed efficace il processo aggiungendo tool per aiutare gli umani a capire e gestire le PR. La gestione dei task sta arrivando nativamente in Claude Code che come sempre è attento alle iniziative community. Il mio goto per questa cosa resta [backlog.md](https://backlog.md) ma sono curioso di vedere cosa porteranno quelli di Anthropic.

Di gestione dei task e di spec-driven development parlerò al [Voxxed Day in un altro panel](https://vdt26.voxxeddays.ch/talk/?id=10201), dove farò da moderatore con quattro ospiti che si occupano proprio di quello. Vi racconterò in una delle prossime newsletter o nel podcast cosa avrò imparato.

### I link della settimana

**[Don't fall into the anti-AI hype](https://antirez.com/news/158)**

Salvatore "Antirez" Sanfilippo, creatore di Redis, sostiene che per la maggior parte dei progetti scrivere il codice da soli non ha più senso, se non per divertimento.

**[I was a top 0.01% Cursor user. Here's why I switched to Claude Code 2.0](https://blog.silennai.com/claude-code)**

Guida completa ai 5 pilastri dell'agentic coding: context management, planning, closing the loop, verifiability e debugging sistematico.

**[Devin Review: AI to Stop Slop](https://cognition.ai/blog/devin-review)**

Tool di code review AI-powered che affronta i colli di bottiglia con comprensione AI del codice, CLI, organizzazione intelligente dei diffs e flagging bug.

**[We're turning Todos into Tasks in Claude Code](https://www.threads.net/@boris_cherny/post/DT15_lHjmWS)**

Anthropic aggiorna Todos a Tasks: nuova primitiva per tracciare progetti complessi con dipendenze, collaborazione cross-session e persistenza nel filesystem.

## 🏢 Business e società

### I Takeaways per gli AI Engineers

- **Takeaway 1:** OpenAI e la necessità economica: Nonostante ricavi in crescita, OpenAI cerca $50B di nuovi fondi e introduce ads nel tier Go. La pubblicità diventa necessaria per sostenere l'infrastruttura AI e competere con Google.
- **Takeaway 2:** L'inferenza è il nuovo motore economico: Mentre il training di modelli richiede investimenti enormi, l'inferenza ottimizzata (vLLM, Inferact) sta diventando il vero generatore di ricavi nell'ecosistema AI.
- **Takeaway 3:** Allineamento e trasparenza: Anthropic pubblica la nuova costituzione di Claude, evidenziando l'importanza di allineare i modelli AI con valori umani man mano che acquisiscono più autonomia decisionale.

- **Action Items:**
  - Valutate attentamente i trade-off tra costo e privacy nelle vostre scelte di tool AI (tier con ads vs tier senza)
  - Leggete la costituzione di Claude per capire come l'allineamento dei modelli impatterà i sistemi AI autonomi del futuro

### Cosa succede questa settimana?

Questa settimana OpenAI protagonista di questa sezione. Da un lato Altman incontra investitori per un'altra GROSSA iniezione di fondi nella società. Nonostante il 2025 abbia visto un grande incremento dei ricavi, OpenAI ha ancora bisogno di ingenti investimenti per mantenere il passo che si è data nel portare l'AI anche nel consumer e sostenere il confronto con un gigante come Google. Contemporaneamente lancia un abbonamento light (chiamato Go) a soli 8$ al mese, ma sostenuto da annunci pubblicitari mostrati all'utente durante il suo utilizzo. Il link ufficiale e l'autorevole opinione di Simon Willison (una delle voci che più stimo nel panorama AI) spiegano quali sono le promesse di OpenAI di chiara separazione tra contenuti ed ads. Staremo a vedere, nel frattempo Google giura che Gemini non avrà mai pubblicità...appunto staremo a vedere.

Nel frattempo osserviamo una startup fatta da alcuni dei creatori di vLLM che erano di recente stati acquisiti e che ri-tentano l'avventura imprenditoriale. Non so se anche stavolta avranno gli stessi successi, ma di certo in questo momento l'inferenza è il motore dei soldi molto più del creare modelli.

Anthropic conferma la loro attenzione all'allineamento di Claude. L'articolo merita una lettura anche per capire bene cosa sia l'allineamento e quanto questo potrebbe impattare nell'uso dell'AI in futuro, specie dandole sempre più autonomia decisionale.

### I link della settimana

**[OpenAI's long-rumored introduction of ads to ChatGPT](https://simonwillison.net/2026/Jan/16/chatgpt-ads/)**

Simon Willison analizza l'introduzione degli ads su ChatGPT per i tier Free e Go, con implicazioni significative per il modello di business di OpenAI.

**[OpenAI plans to introduce ads in ChatGPT](https://openai.com/index/our-approach-to-advertising-and-expanding-access/)**

OpenAI annuncia ufficialmente la pubblicità su ChatGPT per supportare l'accesso più ampio all'AI, garantendo privacy e separazione tra ads e risposte.

**[Claude's new constitution](https://www.anthropic.com/news/claude-new-constitution)**

Anthropic pubblica la nuova costituzione di Claude: documento dettagliato sulla visione, valori e allineamento del modello AI.

**[OpenAI's Altman Meets Mideast Investors for $50 Billion Round](https://www.bloomberg.com/news/articles/2026-01-21/openai-s-altman-meets-mideast-investors-for-50-billion-round)**

Sam Altman cerca finanziamenti per un round da almeno $50 miliardi che valuterebbe OpenAI tra $750-830 miliardi per infrastrutture AI e data center.

**[Inference startup Inferact lands $150M to commercialize vLLM](https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/)**

Inferact, startup del team vLLM, raccoglie $150M per commercializzare il motore di inference open-source, evidenziando il passaggio dal training all'inferenza.

## 🤖 Robotica e Physical AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Physical AI: il prossimo frontier. La robotica è solo una parte della Physical AI, che unisce percezione, ragionamento e azione nel mondo fisico. Player come Nvidia, OpenAI e startup come Cyberwave stanno investendo pesantemente in questo spazio.
- **Takeaway 2:** L'ecosistema si sta muovendo: Dai modelli VLA di Nvidia alle interfacce cervello-computer di Merge Labs (finanziate da OpenAI), l'industria sta creando l'infrastruttura per l'AI fisica. È il "momento Android" per la robotica.
- **Takeaway 3:** Opportunità concrete per i developer: Programmi come Cyberwave Builders offrono hardware gratuito e supporto per sviluppare physical AI reale. È il momento di sperimentare con robotica e sistemi fisici.

- **Action Items:**
  - Iscrivetevi al Cyberwave Builders Program per ottenere accesso gratuito ad hardware robotico e sviluppare progetti di physical AI
  - Esplorate le tecnologie VLA di Nvidia e le risorse su embodied AI per capire come integrare percezione visiva, linguaggio e azione nei vostri progetti

### Cosa succede questa settimana?

Parto segnalandovi l'iniziativa di Cyberwave, startup italiana nel mondo della robotica: un builders program con cohort di 4 settimane focalizzati alla creazione di physical AI. E se siete selezionati vi forniscono il robot gratuitamente per fare il vostro sviluppo. Per me che considero la robotica "the next big thing" (ehm...non sono l'unico), un'occasione da non perdere. Infatti sono già iscritto, e vi consiglio di fare lo stesso seguendo il link fornito sotto. Se volete sapere di più di Cyberwave ho [intervistato in podcast il founder Simone Di Somma](https://open.spotify.com/episode/7gnSOUip21E41RVFWCn8iZ?si=aadf90f7884346ac). Un'intervista densa e molto interessante sia per Cyberwave che per le esperienze e la vision di Simone.

E a testimoniare che non sono l'unico a pensare alla robotica, o meglio alla physical AI di cui la robotica è solo una parte, come il prossimo momento di svolta, gli altri due link vi parlano delle ricerche e degli investimenti in questo campo di niente meno che OpenAI e Nvidia, due delle aziende che stanno trascinando la rivoluzione dell'AI.

### I link della settimana

**[Nvidia Speeds up AI Reasoning with Fast-ThinkAct](https://www.otherworldsai.com/blog/nvidias-android-moment-for-robotics-inside-the-ces-2026-physical-ai-revolution)**

Fast-ThinkAct: framework vision-language-action con inferenza 9.3x più veloce. Nvidia presenta Isaac GR00T N1.6, modello VLA per applicazioni robotiche.

**[Investing in Merge Labs](https://openai.com/index/investing-in-merge-labs/)**

OpenAI guida un round da $252M in Merge Labs, startup di interfacce cervello-computer non invasive che usano ultrasuoni per leggere/scrivere nel cervello.

**[Launching the Cyberwave Builders Program](http://cyberwave.com/blog/builders-program)**

Cyberwave lancia un builders program di 4 settimane per physical AI con hardware robotico gratuito (bracci SO101, rover UGV) e supporto del team.
