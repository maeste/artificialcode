# Gli agenti migliorano da soli, ma chi verifica l'harness che si riscrive?

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana in cui torno sul mio chiodo fisso, ma da un'angolazione che non avevo ancora battuto: il self-improvement continuo degli agenti. È un tema delicato, che si guarda da almeno due punti di vista, e nel deep dive li tengo separati apposta. Da una parte il modello, con i pesi che smettono di essere congelati al training e cominciano a evolvere durante l'uso, come sta sperimentando Qwen. Dall'altra l'harness e la memoria, che migliorano da fuori, e su cui vedo tre strade diverse: Prime Intellect, Meta e ancora Qwen. Nel mezzo ci metto anche qualcosa che la ricerca ha dimostrato non funzionare, la self-reflection, e la chiave che uso per orientarmi: l'HOW marcisce, il WHAT si apprezza. La conclusione è quella che mi porto dietro da mesi e che qui diventa scomoda: puoi delegare solo l'autonomia che riesci a verificare a basso costo, e il caso in cui verificare è più difficile è proprio l'harness che riscrive sé stesso. Nei link trovate Muse Code, i 10.000 miliardi di parametri di ByteDance, DiffusionGemma e AnyDoc. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * Sabato è uscita la puntata 66 di Risorse Artificiali, "L'AI fa 10 scoperte matematiche in una settimana", con Alessandro Maserati: cosa resta quando l'AI risolve le dimostrazioni, security, prompting 2026 ed economia dei token. [Ascolta](https://www.youtube.com/watch?v=YXGBwrwfpkU&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep66_drop)

---

## Self-improvement continuo: cosa evolve nei pesi, cosa evolve nell'harness

Ci sono due modi di far migliorare un agente, e lavorano su scale di tempo completamente diverse. Uno passa dai pesi e si misura in settimane. L'altro passa dall'harness e si misura in turni. È la stessa dicotomia della [survey con Schmidhuber](https://arxiv.org/abs/2607.13104) che linkavo tre settimane fa, dove il self-improvement viene formalizzato come un operatore che aggiorna i pesi oppure lo scaffold. E lo scaffold, lo dicevo allora, sono i miei harness chiamati con un altro nome.

Da una parte c'è il modello, e il modello ha diversi modi di evolvere. Il primo, forse il più naturale che viene in mente, è l'evoluzione dei pesi. Oggi si fa in fase di training, ma sempre di più la si sperimenta in modo continuo: significa fare degli snapshot di quello che funziona e applicare piccole evoluzioni con metodi tipo LoRA. Dwarkesh Patel ha appena messo in fila [otto previsioni per l'era del continual learning](https://www.dwarkesh.com/p/era-of-continual-learning), e una mi resta addosso: se i pesi si aggiornano ogni giorno dalle sessioni di lavoro, le safety eval fatte prima del rilascio perdono senso.

Ho trovato più interessante, però, leggere in queste settimane come [Qwen stia approcciando lo stesso problema](https://qwen.ai/blog?id=qwen3.8) con tecniche di self-evolving basate sui feedback. È una ricerca interessante, già applicata in Qwen3.8-Max, e i risultati sembrano molto promettenti: nel caso oh-my-cli il modello ha lavorato sedici giorni in autonomia producendo 265 commit e 127 PR, e in un benchmark e-commerce da 365 giorni ha imparato a spuntare prezzi più bassi round dopo round. Di sicuro va studiato molto più a fondo, e non mi è chiaro quanto queste tecniche di feedback continuo, che fanno evolvere i pesi con piccole variazioni raccolte durante le sessioni di inferenza, possano essere davvero scalabili. Al momento sono state provate su 3.8-Max ma in versione di laboratorio. Vediamo se si riesce a portarle sull'inferenza vera e propria.

Dall'altra parte c'è l'approccio di far evolvere gli agenti in una maniera completamente diversa, cioè da fuori, non dal modello. Se diamo per scontato che il modello è la base dell'intelligenza degli agenti, è anche vero che la base del loro comportamento la forma l'harness. Far evolvere l'harness, e la memoria collegata all'harness, che in qualche modo ne fa parte a seconda di dove uno decide di tagliare, può essere estremamente promettente. Lo vediamo in queste settimane su tre progetti, con tre modalità diverse. [Prime Intellect](https://www.primeintellect.ai/blog/prime-agent) usa un comando `/refine` che legge la traiettoria e applica la più piccola modifica CRUD che migliora l'harness: 95,5% su ARC-AGI-3 con Opus 5, sopra la baseline dell'esperto umano. [Meta con Muse Code](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) fa co-training tra harness e modello, con Spark 1.1 che genera ambienti e valuta i candidati per Spark 1.2. Qwen, di nuovo, l'harness se lo produce da solo.

Poi c'è la memoria, e anche lì almeno quattro paradigmi diversi, ognuno da capire e ragionare per sé: cristallizzare le tracce in skill eseguibili come fa [MSCE](https://arxiv.org/abs/2607.16621), codificarla come programma da interrogare con grep come [PRO-LONG](https://arxiv.org/abs/2607.20064), che vale 18 punti su ARC-AGI-3, lasciare che sia l'agente a decidere cosa ricordare come nell'auto-memory di Claude 5, oppure pre-strutturarla in un grafo deterministico senza LLM come [Zero-Mem](https://arxiv.org/abs/2607.29377).

Mi interessa però citarvi anche qualcosa che la ricerca ha dimostrato non funzionare. È uscito un paper che si intitola ["Sample More, Reflect Less"](https://arxiv.org/abs/2607.28576) e che fa vedere molto bene, pur su modelli piccoli dall'1,5 ai 7 miliardi di parametri, come la self-reflection di un agente, cioè chiedere all'agente stesso di raffinare i propri risultati, non porti a risultati significativi. Self-Refine e Reflexion perdono contro il semplice repeated sampling a parità di budget di token. È un po' come chiedere a uno studente di rileggere il compito in classe sperando che trovi tutti gli errori, soprattutto se non era sufficientemente preparato.

Questa cosa non va confusa con la reflection fatta con modelli diversi, che invece dà buoni risultati. Ma molto spesso, soprattutto nei grandi laboratori, si vede la tendenza a sedersi e usare sempre lo stesso modello. Probabilmente i modelli più grandi sono più capaci di autocorreggersi, e questa ricerca è importante proprio perché fa vedere che sui modelli piccoli non funziona: per estensione possiamo desumere che anche quando funziona sui grandi lo faccia perché non sono stati messi completamente sotto stress su tutto quello che potevano esplorare. Ovvero: se al primo passaggio esploriamo completamente lo spazio delle soluzioni che il modello è in grado di esplorare, una reflection non ci darà nessun miglioramento.

All'interno del miglioramento continuo degli harness, e degli agenti in generale, mi piace sottolineare che ci sono due prospettive diverse da cui guardare il possibile miglioramento: l'HOW e il WHAT. La distinzione la prendo da [Daniel Miessler](https://danielmiessler.com/blog/the-answer-to-the-harness-question). L'HOW sono le istruzioni operative, lo step by step: più il modello è intelligente, più le micro-istruzioni diventano inutili, ed è per questo che il post-training sul come comportarsi può diventare importante, proprio per scartarle e far focalizzare il ragionamento, e quindi i token di reasoning, in maniera più efficiente ed efficace. Il WHAT invece è materia dell'harness: il contesto, gli intenti, l'identità, i criteri di qualità e soprattutto i criteri di verifica, tutte quelle cose che creano il loop e lo chiudono. Miessler lo dice bene: l'HOW marcisce col Bitter Lesson, perché prima o poi i lab te lo addestrano dentro. Il WHAT no: il tuo contesto nessun laboratorio può post-trainarlo al posto tuo.

E proprio sui loop voglio tornare, perché una delle cose fondamentali nel self-improvement di un agente è trovarsi in uno spazio di risultati verificabili. Questa verifica deve essere prima di tutto a basso costo, per poter girare ad alta frequenza, e non deve essere facilmente falsificabile, perché ci crediate o no ai modelli piace tantissimo barare, e se possono ci proveranno. Infine, non è meno importante concentrarsi su loop corti, corti nel senso di un numero di step non grande, diciamo sotto i dieci prima di ogni verifica. Questo consente una chiusura del loop più stretta e un miglioramento continuo più alto. È la back pressure di [Addy Osmani](https://addyo.substack.com/p/software-factories-light-and-dark) di cui parlavo due settimane fa: puoi delegare solo l'autonomia che riesci a verificare a basso costo e ad alta frequenza. Ed è qui che si vede la tensione vera, perché il caso in cui la back pressure è più difficile da esercitare è esattamente quello dell'harness che riscrive sé stesso.

Una risposta parziale, però, l'ho già data qualche settimana fa, ed è la regola di governance su cui sto lavorando con [Lince](https://lince.sh): l'evaluator e il controllo dei permessi devono stare fuori dal loop che evolve l'harness. Se lasci che il programma si modifichi da solo dentro l'anello, rompi i confini di astrazione e apri la porta al reward hacking. Vale per l'harness esattamente come vale per i pesi.

---

## I link che mi hanno colpito questa settimana

### [Meta Muse Code e Spark 1.2: l'harness co-addestrato col modello](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)

*Background agent asincroni attivi per tutta la sessione, event log locale di ogni chiamata e tool run, e Spark 1.2 co-addestrato con l'harness.*

È il collegamento più diretto col deep dive di oggi, dove Muse Code è uno dei tre modi in cui l'harness migliora sé stesso. Qui aggiungo il pezzo che là non entrava: i background agent restano attivi per tutta la sessione invece di nascere e morire su ogni task, e ogni chiamata al modello, ogni tool run e ogni approvazione finiscono in un event log locale. Anche Meta si lancia nel mondo degli harness, ormai un asset importante tanto quanto il modello.

### [ByteDance verso i 10.000 miliardi di parametri](https://www.kucoin.com/news/flash/bytedance-training-10-trillion-parameter-ai-model-aiming-for-global-leadership)

*Secondo il Financial Times, che cita tre fonti informate, ByteDance starebbe addestrando un modello da circa 10.000 miliardi di parametri, più di tre volte Kimi K3.*

10T è un numero incredibile, ma visto che la legge di scalabilità sembra perfettamente intatta e più parametri significa più intelligenza, questo modello potrebbe diventare un punto di rottura. O confutarla. Prendetelo con le pinze, però: la notizia rimbalza da un aggregatore all'altro, e alla base ci sono insider anonimi.

### [DiffusionGemma: Google porta la diffusione sul testo](https://arxiv.org/abs/2608.00146)

*Circa 20 token per forward pass e 1.500 al secondo su una singola H100, raffinando blocchi da 256 token in parallelo. Base Gemma 4 MoE.*

Un paper assolutamente da leggere. Se la qualità delle risposte non eguaglia ancora i modelli autoregressivi, la velocità è impressionante, e i ricercatori di Google sono andati oltre la semplice generazione di testo mantenendo anche il reasoning in un modello diffusion. Abbiamo parlato tante volte della necessità di andare oltre il paradigma autoregressivo: questa non è necessariamente l'unica direzione, ma certamente una da esplorare.

### [AnyDoc: da qualunque documento a markdown senza spendere un token](https://www.firecrawl.dev/blog/anydoc-and-pdf-inspector)

*Libreria Rust open source di Firecrawl che converte 14 formati in markdown, con 81 punti di qualità su 100 contro i 70 della migliore alternativa e 4,4 millisecondi mediani.*

Markdown è il formato elettivo per i modelli, e un progetto che converte praticamente qualunque formato in MD senza spendere un solo token cambia le regole del gioco. Fino ad ora questo lavoro lo si è fatto con un modello dedicato, magari piccolo, con i costi in token correlati. Qui invece è puro Rust: nessun modello ML, nessun servizio esterno. Il benchmark è fatto in casa, ma la direzione mi sembra quella giusta.
