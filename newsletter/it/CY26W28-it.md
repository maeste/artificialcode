# Siamo al ChatGPT moment dell'harness, e quasi nessuno se ne accorge

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana in cui la sezione link è piena di nuovi modelli di frontiera, e mi sono trovato a fare una scelta di campo. Avrei potuto fare il deep dive su uno di quelli, e ne avevo voglia, invece ho preferito concentrarmi sull'importanza dell'harness, l'impalcatura di software attorno al modello. Non perché i modelli non contino: anzi. Le due cose non si escludono, ed entrambe sono decisive per il futuro agentico. Ma c'è una differenza che mi sembra fondamentale. Sui modelli stiamo vivendo la rincorsa al modello più incredibile di tutti, ed è una cosa che, per quanto spettacolare, ci aspettiamo: ogni settimana c'è un nuovo SOTA, e abbiamo imparato a non sorprenderci più di tanto. Sull'ingegneria del software dietro agli agenti, invece, siamo al ChatGPT moment: qualcosa sta cambiando così in fretta, e così sotto gli occhi di tutti, che tra un anno ci sembrerà scontato e oggi facciamo ancora fatica a nominarlo.

Nel deep dive lo dimostro con i numeri, perché questa volta i numeri ci sono. Due grafici dicono la stessa cosa: a parità di modello, cambiare harness sposta il risultato più di quanto dovremmo aspettarci. E Lilian Weng, con un post che ho divorato, ci mette la definizione e la direzione di marcia. La mia tesi resta la solita, ma ora ha l'appoggio della ricerca e dei dati: che tu usi un modello chiuso o uno open weight, la vera leva è l'harness, ed è dove mi sto giocando tutto, con Lince.

Nella sezione link trovate proprio i modelli di frontiera di cui parlavo: la nuova famiglia GPT-5.6 e GPT-Live di OpenAI, Muse Spark 1.1 e Muse Image di Meta, Grok 4.5, Hy3 di Tencent, Seedream di ByteDance e Gemma 4 di Google. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * Sabato è uscita la nuova puntata: Fable è un altro livello e la gente lo usa per ottimizzare l'harness e insegnare a Opus.
  * Poi i costi reali dei modelli, la guerra fredda AI Cina-USA e LongCat su chip Huawei. [Ascolta](https://youtu.be/Xsmd-qbtgVA?utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep61_drop)
  * I nostri progetti [Lince.sh](https://lince.sh) e AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), ormai li conoscete bene. Date un'occhiata anche ad [Agent ready skills](https://github.com/RisorseArtificiali/agent-ready-skill) di cui ho parlato il 24 giugno ad AIConf.
  * Stiamo pensando di fare delle live su YouTube, X e magari LinkedIn, brevi, una volta a settimana, all'ora di pranzo o lì attorno, per raccontarvi e farvi vedere cose pratiche sui nostri progetti, sugli agenti personali e su usi diversi dell'AI. Primo esperimento questo giovedì, [seguiteci sui social per saperne di più](https://risorseartificiali.com)

Da solo:
  * Finalmente un periodo tranquillo per le mie uscite pubbliche. In fondo è arrivata l'estate, ma stiamo già lavorando a settembre.
  * Appena escono i video delle conferenze degli scorsi mesi ve li segnalo, perché vorrei un vostro feedback.

---

## L'harness conta più del modello: ora ci sono anche i numeri a dimostrarlo

Parto da due figure che mi hanno tenuto incollato allo schermo. La prima: stesso task, stesso modello, e cambiando solo l'harness il costo per task crolla da 0,21 a 0,12 dollari, il tempo da 48 a 27 secondi, i token da 14.200 a 8.800. Meno 41%, meno 44%, meno 38%, senza toccare un solo peso.

![[Pasted image 20260712213349.png]]

La seconda è ancora più cattiva. Nel grafico costo contro pass-rate, lo stesso Opus 4.8 passa dall'87 al 90 per cento solo perché a cambiare è l'harness e il livello di effort, a parità di spesa.

![[Pasted image 20260712213536.png]]

Sono due immagini che dicono la stessa cosa, ed è esattamente il mio chiodo fisso. Chi mi segue da qualche settimana lo sa: dalla newsletter in cui sostenevo che l'agente è un processo che gira in un sistema operativo di secondo livello, a quella in cui citavo Simone Basso, "il modello è commodity, l'harness è l'asset". Adesso a metterlo nero su bianco, con tanto di definizione, è [Lilian Weng in un post che vi consiglio davvero](https://lilianweng.github.io/posts/2026-07-04-harness/). Per lei l'harness è il sistema attorno al modello che orchestra l'esecuzione: decide come pensa e pianifica, come chiama i tool e agisce, come percepisce e gestisce il contesto, come conserva gli artifact e valuta i risultati. E la sua previsione sul breve periodo è netta: il recursive self-improvement non parte da un modello che riscrive i propri pesi, ma proprio dall'harness engineering. L'analogia che usa è quella con il sistema operativo, la stessa a cui ero arrivato io. Fa piacere.

Il punto che mi interessa di più lo mettono a fuoco due articoli usciti quasi in parallelo su X, e convergono su una classificazione a tre livelli: modello, harness, artifact. [Shilong Liu la racconta così](https://x.com/Shilong_Liu_AI/status/2074800880017342665): l'evoluzione può avvenire dentro il modello, dentro l'harness, o negli artifact che l'agente produce. [pirroh di Replit](https://x.com/pirroh/status/2074118901143679414) arriva allo stesso punto chiamando il terzo livello "contesto", ma la sostanza non cambia. E qui arriva la parte che mi tocca da vicino. pirroh è esplicito: alla frontiera, con modelli come Fable 5 o GPT 5.6, non possiedi i pesi e non puoi fare fine-tuning. Quello che controlli davvero è l'harness, cioè migliorare codice, tool e istruzioni minando le tracce di produzione, e il contesto, personalizzando per agente, utente e organizzazione.

È il riflesso speculare della tesi che difendo da cittadino europeo sugli open weight. Che tu usi un modello chiuso o uno aperto, la vera leva resta l'harness: solo che nel chiuso è l'unica che ti rimane, nell'aperto ce l'hai tutta. Ed è una leva che compone, la spedisci ogni giorno e migliora a ogni interazione.

Attenzione, però, c'è un caveat che non voglio nascondere. Weng riporta un vecchio risultato di STOP, un esperimento di self-improvement ricorsivo che con GPT-4 migliorava le prestazioni ma con modelli più deboli come GPT-3.5 e Mixtral le degradava. La struttura ricorsiva da sola non basta: il modello base deve essere abbastanza capace da migliorare il meccanismo. Migliorare l'harness ti fa ottenere di più dallo stesso modello, ma l'intelligenza resta il nucleo. E poi c'è la regola di design più importante di tutte, quella su cui sto lavorando con [Lince](https://lince.sh): l'evaluator e il controllo dei permessi devono stare fuori dal loop che evolve l'harness. Se lasci che il programma si modifichi da solo dentro l'anello, rompi i confini di astrazione e apri la porta al reward hacking. È governance, di nuovo.

E qui torno alla cosa che ripeto sempre. Tutti questi loop di self-improvement danno il meglio dove i risultati sono verificabili. Lo dice Weng, i loop funzionano meglio quando le metriche sono misurabili e oggettive; lo sintetizza Shilong con tre domande perfette, cosa evolve, che feedback lo guida, dove si chiude il loop; e lo pratica pirroh con ViBench, il suo benchmark per il vibe coding. Se il loop si chiude sul codice o su un eval, hai qualcosa di solido a cui aggrapparti; se si chiude sul marketing, stai ottimizzando verso il nulla.

Chiudo con [Matei Zaharia](https://x.com/matei_zaharia/status/2074943612631273730), che ha misurato i coding agent sui task veri di Databricks: ci sono sorprendenti opportunità di abbassare i costi e alzare la qualità, e i modelli open source sono ormai davvero competitivi. Non è un caso. La leva non è aspettare il prossimo modello di punta. È l'harness, ed è lì che mi sto giocando tutto.

---

## I link che mi hanno colpito questa settimana

### Meta: reasoning agentic e immagini
- [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/)
- [Muse Image](https://about.fb.com/news/2026/07/introducing-muse-image-meta-ai/)

*Spark 1.1 è il modello multimodale di reasoning di Meta Superintelligence Labs, pensato per compiti agentic, con contesto gestito attivamente fino a un milione di token e orchestrazione multi-agente. Muse Image è il primo modello di image generation del laboratorio, con testo leggibile nell'immagine e editing diretto da sketch.*

Meta fa sul serio sull'agentic. Di Spark mi interessa che il contesto attivo a un milione di token e l'orchestrazione multi-agente siano nativi: parla il linguaggio dell'harness, non del chatbot. E Muse Image con il testo leggibile tocca un punto dove i vecchi generatori sbagliavano sempre.

### OpenAI: la nuova frontiera e la voce
- [GPT-5.6](https://openai.com/index/gpt-5-6/)
- [GPT-Live](https://openai.com/index/introducing-gpt-live/)

*GPT-5.6 in tre livelli, Sol, Terra e Luna. Sol è il nuovo flagship, SOTA su coding, cybersecurity e scienza, e su Agents' Last Exam batte Claude Fable 5 di oltre 13 punti a circa un quarto del costo, con agenti paralleli in modalità "ultra". GPT-Live è la nuova generazione di modelli vocali full-duplex, che ascolta e parla insieme.*

Sol è il nuovo riferimento, ma il numero che conta non è il +13 su Fable, è il costo a un quarto: la frontiera si compra sempre più a rate. Di GPT-Live mi incuriosisce il pattern, delegare in background al reasoning mentre la voce resta viva: è orchestrazione, ancora.

### [Hy3 di Tencent](https://simonwillison.net/2026/Jul/6/hy3/)

*MoE open source Apache 2.0 da 295 miliardi di parametri, 21 attivi, contesto a 256K, che compete con flagship open da due a cinque volte i suoi parametri.*

Questo rafforza dritto la mia tesi europea. Un MoE cinese aperto che regge il confronto con modelli molto più grossi significa che l'alternativa alla frontiera esiste, ed è la polizza di cui parlavo. Da provare gratis su OpenRouter fino al 21 luglio.

### [Grok 4.5](https://x.ai/news/grok-4-5)

*Modello di xAI addestrato con Cursor, 80 token al secondo, efficienza di token circa doppia, default in Grok Build, in Cursor e via API. Non ancora in UE, atteso a metà luglio.*

Due note. Gli 80 token al secondo sono musica per i sistemi multi-agente, dove la latenza tra le chiamate si somma. E l'UE tagliata fuori, ancora: ogni modello che arriva tardi da noi è un'altra spinta verso gli open weight.

### [Seedream 5.0 Pro di ByteDance](https://www.testingcatalog.com/bytedance-debuts-seedream-5-0-pro-with-advanced-reasoning/)

*Modello multimodale di creazione immagini pensato per il production design: layout complessi, editing di precisione per regione, separazione in livelli, testo nativo in 14 lingue.*

Non mi colpisce la qualità dell'immagine, mi colpisce il bersaglio. Editing per regione e livelli sono funzioni da pipeline, non da chatbot: quando i componenti diventano componibili, ha più senso montarli in un sistema multi-modello.

### [Gemma 4](https://arxiv.org/abs/2607.02770)

*Nuova generazione di LLM open weight multimodali, dense e MoE da 2,3 a 31 miliardi, modalità "thinking", efficienza su contesto lungo, modello 12B unificato che processa audio e immagini grezze. Apache 2.0.*

Google continua a spingere sull'aperto e sul locale, e il 12B unificato che ingerisce audio e immagini grezze senza encoder è il pezzo più interessante. Open weight, Apache 2.0: altra munizione per la polizza.
