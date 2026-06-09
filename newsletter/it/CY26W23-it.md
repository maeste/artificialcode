# Locale o cloud è la domanda sbagliata: l'AI sarà ibrida

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana in cui torno su un tema che mi sta a cuore da tempo: come stiamo ottimizzando l'AI per farla girare in locale, e dove ci sta portando tutto questo. Nel deep dive provo a mettere in fila i pezzi, dal lavoro su modelli piccoli, quantizzazione e harness minimali fino all'hardware, con Apple che al momento vince a man bassa e NVIDIA che prova a rispondere con l'RTX Spark. La mia tesi è che il futuro non sia locale contro cloud, ma un'architettura ibrida in cui i due si completano: far girare in casa quello che si può, e chiamare il cloud solo quando serve davvero. Nella sezione link trovate i temi che fanno da contorno e completano il quadro: un tool per confrontare modelli Ollama in locale, Anthropic sul recursive self-improvement, il paradigma Sleep di Google per i modelli che imparano da soli, il vero collo di bottiglia degli agenti enterprise (i permessi, non il modello), il dreaming nella memoria di ChatGPT, Open Code Review e il nuovo Nemotron-3-Ultra di NVIDIA, con i suoi pesi e dataset aperti. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * Sabato è uscita la puntata 55 di Risorse Artificiali, "Workflow dinamici: l'AI che si scrive gli harness": con Opus 4.8 ogni agente si genera al volo il proprio tool custom in JavaScript, e parliamo di cosa significa per sicurezza e sandboxing. [Ascolta](https://www.youtube.com/watch?v=A7y6dQdqaIo&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep55_drop)
  * Nella stessa puntata: perché i benchmark non sono comparabili (conta l'harness, non solo il modello), MiniMax M3 e l'intervista di Hassabis col doppiaggio automatico di YouTube.
  * I nostri progetti [Lince.sh](https://lince.sh) e AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), ormai li conoscete bene.

Da solo:
  * Sono stato a [PyCon Italia come speaker](https://2026.pycon.it/en/speakers): trovate tutti i contenuti dei miei due interventi, come sempre, su [maeste.it](https://maeste.it) nella sezione dedicata ai talk. Metterò lì anche i video non appena disponibili.
  * Il 12 giugno sarò a Catania come speaker al [Coderful](https://www.coderful.io/)
  * Il 24 giugno sarò a Milano come speaker di [AIConf](https://www.aiconf.it/)

---

## Architetture ibride: l'AI gira in locale, il cloud lo chiami solo quando serve

Da qualche tempo vedo un trend che si fa sempre più netto: ottimizzare tutto per far girare l'AI in locale. Lo si vede su più fronti contemporaneamente, e messi insieme raccontano una direzione precisa. C'è il lavoro sull'inferenza, ci sono i modelli piccoli, ci sono i modelli quantization aware, cioè pensati fin dall'addestramento per reggere bene la riduzione di precisione, e c'è soprattutto un enorme lavoro di quantizzazione, comprese le quantizzazioni asimmetriche che provano a spremere ogni bit senza perdere qualità. Stanno arrivando architetture nuove che tolgono l'encoder o alcune fasi del decoding, e harness disegnati in modo minimale, penso a Pi, oppure pensati per girare a braccetto con l'inferenza, come il [DS4 di antirez](https://github.com/antirez/ds4), fino a sistemi come [Unsloth](https://unsloth.ai/docs/new/studio) che sulla stessa macchina ti permettono di fare inferenza e anche fine tuning. L'idea di fondo sembra una sola: avere sempre più sistemi che girano in casa, e non solo per giocarci.

In tutto questo l'hardware conta, e conta tantissimo. Al momento Apple sta vincendo a man bassa grazie alla stabilità della sua architettura ARM con RAM condivisa: se su tanti altri fronti Apple arranca, sull'hardware per far girare le cose in locale ha tra le mani un punto di svolta. NVIDIA e Microsoft provano a rispondere con un sistema concorrente, l'[RTX Spark](https://www.nvidia.com/it-it/products/rtx-spark/), perché il DGX Spark resta troppo specifico per la maggior parte di noi.

Prima di arrivare al mio pensiero forte, voglio togliere un possibile equivoco. Tutto questo lavoro sul locale non è in contrasto con la spinta dei laboratori di frontiera a concentrare sempre più intelligenza nei modelli SOTA, anzi. Le due cose si completano a vicenda, e proprio dalla loro somma esce l'architettura ibrida di cui parlo. Da una parte i grandi laboratori continueranno a spostare in alto l'asticella di cosa un modello sa fare, dall'altra cresce un ecosistema che porta una parte di quella capacità sulle nostre macchine. Non è una gara tra i due fronti, è una divisione del lavoro che si va componendo.

Ed eccomi al mio pensiero forte. Al momento, per fare sul serio inferenza locale, bisogna avere o un hardware di un certo livello, per esempio per far girare DeepSeek con DS4, oppure casi d'uso abbastanza specifici. Anche se gli ultimi modelli piccoli, penso a Gemma 4 12B, aprono la strada pure alle schede RTX e ADA con 16 GB di RAM, e nel frattempo gli open weight crescono in capacità: [MiniMax M3](https://www.implicator.ai/minimax-promises-m3-weights-after-1m-context-model-launch/) conferma la voglia di portare avanti, sulla scia di DeepSeek V4, coding di frontiera, multimodalità nativa e una finestra da un milione di token, e per giunta a prezzi via API molto bassi. Io però vedo un futuro diverso, fatto di architetture ibride: far girare in locale alcune delle operazioni, magari su modelli finetunati apposta, e delegare al cloud solo quando serve davvero. Un po' quello che abbiamo visto con "/advisor" in Claude Code, ma ribaltato: il modello principale è quello locale, e l'advisor in cloud lo richiami solo nei momenti che contano. È una direzione simile a quella che propone Perplexity, che non a caso intitola un suo pezzo [The data center moves to your machine](https://www.perplexity.ai/hub/blog/the-data-center-moves-to-your-machine).

E qui arrivo alla parte che mi intriga di più, perché è ancora tutta da scrivere. A sensazione, una delle ottimizzazioni ingegneristiche di cui avremo bisogno è la capacità di fare il loading dei modelli in memoria in modo molto più veloce e dinamico, così da poter caricare al volo versioni specifiche o con fine tuning dedicati a seconda del compito che abbiamo davanti. Oggi è una sfida per cui non ci sono ancora soluzioni chiare, ed è proprio per questo che vale la pena tenerci gli occhi aperti: è uno di quei problemi che, quando verrà risolto bene, cambierà l'economia di tutto il resto.

---

## I link che mi hanno colpito questa settimana

### [Ollama Model Tester (GitHub Repo)](https://github.com/ulyssestenn/omt)

Uno strumento piccolo ma furbo, proprio nello spirito del deep dive di questa settimana. Se stai sperimentando con l'inferenza locale, poter lanciare lo stesso prompt su più modelli e confrontare le risposte affiancate ti fa risparmiare un sacco di tempo. Di tool così ne serviranno sempre di più.

### [When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement)

Anthropic che parla apertamente di recursive self-improvement fa sempre un certo effetto. Il dato degli otto volte più codice per ingegnere lo prendo con le pinze, come tutti i benchmark interni, ma la direzione è quella e vale la pena leggere come la raccontano loro.

### [Sleep for Continual Learning](https://arxiv.org/abs/2606.03979)

Qui Google prova a dare ai modelli una specie di sonno: una fase in cui consolidano la conoscenza di breve termine nei parametri, con tanto di stadio di Dreaming via reinforcement learning per generarsi curricula da soli. È esattamente il filone dei modelli che migliorano da soli che mi interessa da tempo. Tenetelo a mente, perché più sotto, con Open Code Review, torna lo stesso schema: l'AI che lavora sul lavoro dell'AI.

### [The AI agent bottleneck isn't model performance, it's permissions](https://venturebeat.com/orchestration/the-ai-agent-bottleneck-isnt-model-performance-its-permissions)

Questo pezzo dice una cosa che ripeto da mesi: il collo di bottiglia degli agenti enterprise non è quanto è bravo il modello, ma i permessi e la governance. Ed è esattamente uno dei problemi che con [Lince.sh](https://lince.sh) proviamo ad aiutare a risolvere, lavorando su sandboxing e su cosa un agente può o non può fare. Leggetelo, perché inquadra bene il problema.

### [OpenAI introduce il "dreaming" nella memoria di ChatGPT](https://openai.com/index/chatgpt-memory-dreaming/)

Dopo i Memory Files di Anthropic di cui parlavo la settimana scorsa, anche OpenAI mette mano alla memoria, con un sistema in background che trasforma le chat passate in un profilo organizzato per categorie. Il tema memoria è diventato uno dei terreni di scontro veri tra gli harness, e qui si vede bene dove sta andando la partita.

### [Open Code Review (GitHub Repo)](https://github.com/alibaba/open-code-review)

Ed eccoci al gancio che vi avevo lasciato sopra con il paper sul Sleep. Qui siamo sul concreto: una CLI che legge il diff di git e produce review puntuali riga per riga, con la filosofia di mettere insieme ingegneria deterministica e agente, lasciando a ciascuno quello che sa fare meglio. È la stessa idea di divisione del lavoro del deep dive, applicata alla qualità del codice: l'AI che rivede e migliora ciò che l'AI stessa produce, ma con un'ossatura deterministica a tenere la barra.

### [NVIDIA Nemotron-3-Ultra](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/)

Chiudo con un modello che parla dritto al deep dive: 550 miliardi di parametri ma solo 55 attivi, grazie a un MoE ibrido Mamba-Attention, con un milione di token di contesto. La cosa che mi fa drizzare le orecchie è che NVIDIA pubblica checkpoint, versioni quantizzate e pure i dataset: è proprio il tipo di apertura che alimenta l'ecosistema locale di cui parlavo.
