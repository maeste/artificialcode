Quattro mesi di newsletter settimanali senza saltare nemmeno una settimana. È stato un bel viaggio per me nel scriverle, ma soprattutto nel leggere il materiale che ha formato le mie opinioni e che ho cercato di condividere con voi per approfondimenti ulteriori. Penso sia arrivato il momento di fare una sosta in questo percorso per riflettere su quello che penso degli argomenti che abbiamo trattato, concentrandomi sulle mie opinioni e approfondendo gli aspetti che mi stanno più a cuore. Tornerò alle notizie la prossima settimana.

Questa non è la tua tipica rassegna settimanale di notizie. Invece, sto facendo un passo indietro per riflettere sui quattro principali trend che abbiamo seguito in questi mesi, condividendo quello che mi è rimasto più impresso e quello che sta attivamente influenzando il modo in cui lavoriamo nel software oggi. È qualcosa che prevedo di fare circa ogni trimestre, dando sia a me che a voi la possibilità di prendere fiato, riflettere e sperabilmente dare vita a discussioni preziose e scambi di opinioni.

Se volete approfondire uno qualsiasi di questi argomenti, li abbiamo discussi a lungo nel nostro podcast del sabato (solo in italiano) su [Youtube](https://www.youtube.com/channel/UCYQgzIby7QHkXBonTWk-2Fg) e [Spotify](https://open.spotify.com/show/16dTKEEtKkIzhr1JJNMmSF?si=900902f2dca8442e).

## 🛠️ AI Assisted Coding: Oltre l'Hype verso una Vera Trasformazione

### Le mie conclusioni dell'ultimo trimestre

Vibe coding versus AI assisted coding. Non posso iniziare a discutere dell'influenza dell'AI sul software senza riconoscere che questi sono due cose fondamentalmente diverse. Il vibe coding, come originariamente definito da Andrei Karpathy, è quell'esperienza magica di generare un'intera applicazione da un prompt ben costruito e lasciare che l'AI faccia la maggior parte del lavoro pesante, idealmente senza ulteriori interventi. È affascinante e incredibilmente attraente per chi si avvicina al coding, ma gli sviluppatori esperti sanno che questo funziona solo per applicazioni greenfield e specificamente per prototipi.

Quando parliamo di applicazioni complesse con migliaia o milioni di righe di codice e standard di qualità elevati, è quello che chiamo AI assisted coding il vero game changer. L'AI diventa un partner, mentre è lo sviluppatore esperto che comprende architettura e requisiti, sa come fare le richieste giuste, correggere la rotta quando l'agente di coding devia, suggerire correzioni, scrivere test ed eseguire verifiche esterne. Questa differenza fondamentale eleva l'AI assisted coding a un livello completamente diverso.

Non sto parlando solo di completamento intelligente del codice qui. Intendo un'esperienza completa di agente di coding come Cursor in modalità Agent, o vari CLI come Claude Code o Gemini CLI. Solo in questo modo si ottiene un'esperienza completa di AI assisted coding. Le interfacce CLI offrono i migliori risultati, anche se inizialmente potrebbe sembrare strano e una sorta di passo indietro abbandonare l'IDE, ma ti mantengono molto più concentrato nel fare squadra con l'AI dandogli istruzioni, direzioni e correzioni durante il ciclo di sviluppo. È poi abbastanza normale passare all'IDE per fare la tua parte, tornando al tuo partner AI in CLI quando necessario. Il mio preferito rimane Claude Code, seguito da vicino da Gemini CLI. Riguardo ai modelli, ammetto che questa settimana ho provato ChatGPT-5 per scrivere codice e i risultati sono innegabilmente vicini a quelli di Claude, anche se Claude ricade ancora la mia preferenza.

Il famoso boost di velocità 10x esiste in casi specifici, anche se forse non sempre. Ma la sensazione di lavorare almeno a velocità 5x è costante. Non dal primo giorno, ovviamente. Come in tutto, devi imparare, diventare esperto, sapere come costruire il prompt giusto, curare il contesto della conversazione scegliendo quali file e documenti l'AI può accedere in un momento specifico, e organizzare un workflow efficace. [Molti studi di ricerca che suggeriscono miglioramenti molto più piccoli](https://addyo.substack.com/p/the-reality-of-ai-assisted-software), non devono soprendere o condfondere in quanto si riferiscono al 2024 e a utenti che utilizzano principalmente il completamento del codice. Le cose sono cambiate radicalmente nel 2025, in particolare negli ultimi mesi. Confermo assolutamente la mia sensazione di un fattore di miglioramento tra 5 e 10 volte, nella mia esperienza personale quotidiana.

Il ruolo dello sviluppatore si sta trasformando radicalmente. Essere in grado di leggere codice e comprendere l'architettura del sistema diventa più importante che scrivere in modo impeccabile. Uno degli effetti collaterali più positivi è la capacità di essere poliglotti nei linguaggi. Se sei un buon architetto, impari in fretta a leggere un linguaggio e sai come usare questi strumenti, sei libero di usare il linguaggio che preferisci o che è più adatto al problema in questione.

La quantità di codice che viene sviluppato con l'assistenza dell'AI oggi è incredibile. Basta tenere d'occhio GitHub per vederlo. Il mio team e io spesso commentiamo scherzosamente tra noi le pull request dicendo "Cursor (o Claude) ha fatto un ottimo lavoro qui." Ma se volete qualcosa di concreto, date un'occhiata a questo [repository](https://github.com/a2aproject/a2a-tck). È totalmente scritto dall'AI? No, ma l'AI assisted coding è indubbiamente diventata una pratica normale e regolare per me.

Il lavoro dello sviluppatore sta scomparendo? Tutto il codice sarà scritto dall'AI? Non credo. Credo che presto il 95% del codice sarà scritto dall'AI, ma quel restante 5% sarà molto più del 100% del codice scritto a dicembre 2023\. Quello che intendo è che l'AI assisted coding sta sbloccando una quantità inaspettata di creazione di codice, risolvendo problemi per i quali scrivere codice era troppo costoso o scomodo. Inoltre, l'aumentata velocità di scrittura del codice aumenta il bisogno di buone architetture software e eccellenti ingegneri software che possano adattarsi a questa nuova modalità.

**Action items:**

* Inizia a usare agenti CLI di coding oggi.
* Padroneggia la cura del contesto.
* Concentrati sull'architettura più che sulla sintassi.

## 🧠 Agents: Quello che Devi Sapere

### Le mie conclusioni dell'ultimo trimestre

Il 2025 è indubbiamente l'anno degli agenti. Non per l'adozione, dovremo aspettare un po' di più per quello, ma certamente per il fermento nel mondo del software. Tutti hanno i loro agenti: ChatGPT Agent, Manus, Spark, Google AI Mode, e gli agenti di coding sono ovunque. Poi c'è l'esplosione di [MCP](https://modelcontextprotocol.io/docs/getting-started/intro) per aggiungere tools a un LLM per renderlo un agente, o l'avvento del protocollo [Agent2Agent](https://a2a-protocol.org/v0.3.0/specification/) per la comunicazione multi-agente.

Ma cos'è esattamente un agente e cosa sono i sistemi multi-agente o agentic? Non ci sono definizioni generali ampiamente accettate. Lascia che semplifichi il più possibile e ti dia le mie. **Un AI Agent è** un sistema intelligente, tipicamente alimentato da un modello, capace di percepire lo stato del sistema, intraprendere azioni, verificarle e memorizzarle per evolvere le sue capacità nel tempo. Analizziamo i vari punti toccati.

* Percepire e intraprendere azioni si traduce nell'accedere a tools, tipicamente via MCP, il che significa la capacità di chiamare servizi esistenti o sviluppati su misura per leggere stato o dati e intraprendere azioni per cambiare lo stato.
* L'auto-verifica avviene attraverso strumenti nati per valutare gli LLM e che sono perfetti per valutare risultati i un ambiente non deterministico. Sto parlando degli Evals.
* Infine, sull'evoluzione delle capacità non c'è ancora accordo completo, ma certamente richiede sia memoria a breve che a lungo termine.

**Un sistema agentic consiste** di più agenti che comunicano tra loro. Ma ecco la domanda spontanea: gli agenti stessi non sono tools dotati di intelligenza interna? [Risposta breve: No](https://discuss.google.dev/t/agents-are-not-tools/192812). L'articolo linkato dà una definizione formale, ma lascia che semplifichi di nuovo.

* Un tool è qualcosa che dà capacità aggiuntive a un particolare modello, usato direttamente dal modello per compiere un compito. Qualcosa che gestisco direttamente, controllando input, output e decidendo cosa farne.
* Un altro agente è qualcosa a cui delego un compito, che non controllo direttamente e di cui conosco solo le capacità astratte, la cui esecuzione è opaca per me, che esegue compiti che non posso soddisfare nemmeno con i migliori strumenti.

**Usiamo un'analogia per questo**: uno strumento è una chiave inglese che posso usare per molte cose come aggiustare la mia bicicletta, cosa che so come fare. Ma se il bagno perde, chiamo un idraulico. La chiave inglese non basta; ho bisogno di competenze diverse. Un altro motivo per la delega è l'opacità o la riservatezza dei dati usati per generare una risposta, dove non voglio avere più di quanto necessario. Infine, ci possono essere ragioni di economie di scala per usare un agente e non un tool. Pensa a una tipografia che stampa per te: teoricamente, potresti prendere i loro strumenti e farlo da solo, ma non è conveniente.

L'ultima distinzione che vorrei fare è tra **agenti orizzontali e verticali**. Gli agenti orizzontali come chatGPT agent, Manus e altri sono progettati per essere user-friendly, prendendo un ampio set di problemi e risolvendoli usando strumenti e strategie generiche (tipicamente implementando l'uso del computer). Tipicamente prendono una richiesta dell'utente e la risolvono al meglio. Gli agenti verticali sono più specifici, specificamente addestrati per risolvere un compito molto specifico con strumenti specializzati, conoscenza su misura, accesso a dati riservati. Sono tipicamente orchestrati per comporre diversi verticali e risolvere l'intero problema. Per rimanere nella mia analogia sopra, gli orizzontali sono il manutentore generalista o l'appassionato di fai-da-te, mentre i verticali sono una squadra di idraulici, elettricisti e muratori, orchestrati dal caposquadra.

Quindi dopo tutte queste definizioni, dove siamo? Gli agenti sono certamente l'argomento caldo degli ultimi mesi e certamente l'area di sviluppo più promettente per vedere l'AI applicata in contesti enterprise. Come AI Engineers, dobbiamo iniziare a pensare agli agenti come i componenti che costituiscono e costituiranno le future architetture AI. Ma dobbiamo anche tenere presente che i framework che stiamo sviluppando per costruire agenti non possono ignorare i componenti fondamentali che ho menzionato sopra e devono facilitarne l'uso da parte di chi sviluppere, distribuirà, monitorerà e personalizzerà gli agenti nelle aziende:

* L'LLM è il cervello dell'agente e non puoi farne a meno. Ottimizzare contesto e prompt non è più solo lavoro di un data scientist e lo sarà sempre meno. I framework devono aiutare gli ingegneri software in questo.
* Gli evals e i sistemi di tracing sono parte integrante del sistema. In un sistema intrinsecamente non deterministico, essere in grado di valutare il comportamento è più fondamentale che mai.
* I tools e i loro protocolli, MCP in questo caso, sono importanti, ma lo è anche il design degli strumenti e delle loro API per essere AI-friendly.
* La comunicazione tra agenti richiede protocolli come A2A, su cui sto scommettendo, ma anche la capacità di delegare e orchestrare agenti multipli è chiave.
* La memoria, sia a breve che a lungo termine, è così sottovalutata eppure così importante.

**Action items:**

* Sperimenta con gli strumenti MCP.
* Sperimenta con sistemi multi-agente e il protocollo A2A
* Progetta API AI-friendly.
* Implementa sistemi di eval e tracing appropriati.

## 🤖 Model Improvements: Superando Muri Impossibili

### Le mie conclusioni dell'ultimo trimestre

Potremmo parlare per ore solo del progresso dei modelli. In questi mesi abbiamo visto una gara continua tra i principali player OpenAI, Anthropic, Google, e un'esplosione di concorrenti open-source. Ma il punto su cui voglio concentrarmi, forse il più importante per noi nel mondo del software, è come questo rapido sviluppo non riguardi solo il miglioramento delle caratteristiche, ma come i modelli imparano a fare cose nuove e sempre più sofisticate che pensavamo impossibili fino a poco prima.

Come dice Dario Amodei in una [recente intervista](https://youtu.be/GcqQ1ebBqkc?list=TLGGndLmhjwsKA8xNjA4MjAyNQ), ci siamo abituati a pensare che ci fossero muri insormontabili riguardo alle capacità di questi modelli che abbiamo gradualmente accettato fossero superati: "non faranno mai discorsi coerenti" (pre-ChatGPT), "non simuleranno mai una voce umana," "non useranno mai le parole per ragionare," "non useranno mai strumenti," "non sapranno mai collaborare." In questi pochi anni e ancora di più negli ultimi mesi, abbiamo visto tutti questi muri crollare. I modelli diventano sempre più bravi a fare cose che pensavamo impossibili.

Un'altra intervista affascinante è con [Demis Hassabis](https://youtu.be/-HzgcbRXUK8?list=TLGGrx-9q6U0a80xNjA4MjAyNQ) che condivide molte intuizioni interessanti. Quello che mi ha colpito di più è la sua definizione chiara di come i modelli di reti neurali sono molto bravi a scendere una curva di gradiente d'errore, riuscendo a indovinare una struttura e poi imitarla, quando la complessità rende impossibile o molto difficile per noi formalizzare, anche se appare ovvio che una struttura esista. Questo è il motivo per cui i modelli sono stati recentemente in grado di fare protein folding, perché stiamo lavorando su strutture DNA con i modelli, o forme di montagne, o progressione degli uragani. Tutti elementi naturali dove è evidente che esista una struttura, ma quale sia questa struttura nel dettaglio ci sfugge.

Ma come si traduce questo in quello che vediamo quotidianamente? Iniziamo con una critica su cui molti hanno insistito recentemente sui social media riguardo ai video generati. Tutti si sono concentrati sugli aspetti del rendering finale del video, perfettamente legittimo se vuoi usare questi strumenti per produrre un video virale o qualcosa di professionale. Ma quello che non dovremmo perderci come ingegneri software è che quei video hanno imparato la fisica dei liquidi o la rifrazione della luce in un modo molto vicino o perfettamente aderente alla realtà. E l'hanno fatto solo osservando gli esempi forniti. Se hai idea di come scrivere l'equazione che rappresenta un'onda dell'oceano, assumendo che sia anche possibile, capisci quanto sia incredibile questo. Per non parlare dei world models che riproducono questa fisica in tempo reale.

Anche i modelli LLM hanno fatto progressi incredibili, specialmente nella gestione di contesti lunghi. Pochi mesi fa parlavamo di 64k token; ora sia Gemini che Claude raggiungono comodamente 1 milione di token. Questo è molto significativo nelle implicazioni pratiche come comprendere enormi basi di testo, e più importante per noi, codice. Guardando questo da un'altra prospettiva, è incredibile il progresso necessario nei meccanismi di attention per raggiungere questi risultati.

Non possiamo non citare lo sviluppo dei modelli piccoli e come il loro fine-tuning sta diventando più facile e più adottato per raggiungere performance simili a moelli più grandi, almeno in compiti molto specifici. Questo ci riporta ai sistemi multi-agente e agli agenti verticali che potrebbero decidere di usare un modello piccolo altamente specializzato ed economico per risolvere compiti specifici. La specializzazione dei modelli potrebbe essere un tema importante nei prossimi mesi, sicuramente per i modelli piccoli, ma anche i modelli grandi stanno specializzando sempre di più le loro capacità. Quindi vediamo Claude altamente specializzato nel coding, O3 nella scrittura creativa, Gemini in matematica e fisica, e questa specializzazione è ancora più pronunciata se guardiamo a diverse abilità come generazione video o elaborazione immagini. Più specializzazione per i modelli, potrebbe significare nel prossimo futuro più spazio per agenti verticali multi-agente orchestrati per risolvere problemi le cui complessità spaziano su multiple capacità. Alla fine, è come una squadra di esperti che spesso fa meglio di un singolo genio. O se preferisci, diverse aree del nostro cervello. L'AGI (Artificial General Intelligence) sta probabilmente arrivando nello spazio degli agenti, più che in un singolo modello: infatti GPT5, GROK4, Gemini DeepThink stanno già sperimentando con il loro pensiero "parallelo" (che sono multiple istanze dell'LLM usate in modo agentic)

Ma c'è altra fantascienza che diventerà presto realtà. Gli sviluppi attuali e del prossimo futuro, come dice anche Hassabis nella sua intervista, vanno verso l'embodiment, cioè la robotica. Per fare ulteriori passi nell'intelligenza, dice, i modelli hanno bisogno di esperienza fisica. Sta arrivando il "momento ChatGPT" per la robotica? Io scommetto sul sì.

**Action items:**

* Sfrutta le finestre di contesto lunghe.
* Preparati per l'AI embodied.
* Rimani aggiornato sulle capacità dei modelli.
* Guarda avanti verso l'AGI agentic

## 💼 Business and Society: Cavalcando la Quarta Rivoluzione Industriale

### Le mie conclusioni dell'ultimo trimestre

Gli impatti sulla società sono già significativi e continueranno ad esserlo. Molti chiamano questo momento la quarta rivoluzione industriale, e come tutte le rivoluzioni industriali, dovremo adattarci a nuovi modi di lavorare, studiare e fare business. Specialmente se sei o hai a che fare con giovani o giovanissimi, l'AI sarà per loro quello che internet è stato per noi, o forse di più, quello che la stampa è stata per i nostri trisnonni.

Sento spesso paragoni con la bolla delle dot-com. Se questa crescita dell'AI nei mercati sia speculazione finanziaria, non ho né le competenze né l'interesse per dirlo. Quello che posso dirvi è che la tecnologia è qui per restare, proprio come le dot-com erano una bolla, ma se mi stai leggendo è perché la tecnologia di quella bolla, internet, è qui e ha cambiato considerevolmente società, lavoro, studio e business.

Ma chiudiamo con noi. Cosa significa questo nuovo modo di fare business, dove tutto si muove così rapidamente? Anche per questo, il ruolo degli ingegneri software deve cambiare, la mentalità deve cambiare. Se prima eravamo abituati a sviluppare software per risolvere un problema che rimaneva piuttosto stabile nel tempo, l'adattamento richiesto oggi è proprio dover risolvere problemi che sono veri oggi ma potrebbero essere risolti dall'avanzamento dei modelli domani. Quindi ancora più di prima, ci è richiesto di essere agili, con una filosofia di prodotto estremamente lean, creando soluzioni che risolvono problemi molto specifici e sono sufficientemente minimali per andare sul mercato proprio ora. Fare l'API che esegue il compito X che un modello non può fare oggi è quello che dobbiamo fare. Ma deve essere minimale e pronta immediatamente, perché se ci prendiamo tempo per creare quell'API o framework perfetto ma nel frattempo il problema è già risolto, abbiamo appena sprecato lavoro. Inoltre la soluzione dovrebbe essere flessibile, progettata pensando all'AI e in grado di adattarsi alle nuove capacità LLM in arrivo. Sempre di più il nostro software deve essere progettato per l'internet degli agenti, non solo per utenti umani.

La capacità di adattarsi, essere veloci, grazie anche all'AI assisted coding, minimali e agili sia nelle decisioni che nell'esecuzione sono oggi le caratteristiche più importanti per muoversi in questo mercato frenetico e in costante cambiamento. E la mia sensazione è che siamo ancora nella curva dell'hype, lontani dalla stabilità nell'adozione o nella tecnologia se guardiamo all'AI nel suo insieme e non solo agli LLM (pensa a quello che è stato menzionato sopra riguardo all'AGI multi-agente e all'AI embodiment).

Quindi il futuro può essere luminoso, emozionante, ma decisamente impegnativo. E in paesaggi che cambiano rapidamente solo le creature più adattabili sopravvivono e prosperano.

**Action items:**

* Adotta la filosofia lean.
* Consegna soluzioni minimali praticabili.
* Rimani agile nell'esecuzione.
