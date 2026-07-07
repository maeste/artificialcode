# Sembra un modello, è una squadra: la svolta multi agente dell'AI

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana in cui torno su un'idea che inseguo da anni, da quando due anni fa ci provavo con un PoC chiamato wise-agents: far lavorare insieme più modelli, piccoli e specializzati, invece di affidare tutto a un unico cervellone. Allora era troppo presto, oggi la ritrovo dappertutto. Nel deep dive metto in fila le tappe, dal council di Karpathy al Fusion Router di OpenRouter, fino a Sakana Fugu, che si presenta come un modello ma sotto è un sistema multi agente. La mia tesi è che l'unità di misura si sia spostata dal singolo modello alla squadra e a chi la dirige, e che con un buon harness multi-modello gran parte di quei risultati siano già alla nostra portata. Non a caso Simone Basso, nell'intervista che trovate in agenda, lo dice meglio di me: il modello è commodity, l'harness è l'asset. Nella sezione link i temi di contorno: la Casa Bianca che frena GPT-5.6 (e qui torna la frontiera ostaggio della politica), il modellino on-device di Liquid AI, il chip Jalapeño di OpenAI, il computer use su Gemini Flash, il fine-tuning dei MoE con NVIDIA, i rincari di Apple sulla RAM e Mercury 2 che genera mille token al secondo. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * Nuova [intervista a Simone Basso (CTPO WeRoad)](https://www.youtube.com/watch?v=gTB3Q0_LXiM&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=basso_drop): perché "il modello è commodity, l'harness è l'asset" e come lo applicano davvero a scala europea. Dentro anche le 150 licenze AI date a tutta l'azienda (non solo ai dev) e il ROI reale dei coding agent, l'8x di Anthropic visto da chi lo misura.
  * Sabato è uscito "Physical AI: VLA contro World Model": con Vittorio di Cyberwave abbiamo capito perché un agente software lo costruisci in due ore e uno fisico in due anni. [Ascoltala qui](https://www.youtube.com/watch?v=8Dlsukidue4&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep58_drop).
  * I nostri progetti [Lince.sh](https://lince.sh) e AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), ormai li conoscete bene. Date un'occhiata anche ad [Agent ready skills](https://github.com/RisorseArtificiali/agent-ready-skill), di cui ho parlato il 24 giugno ad AIConf.

Da solo:
  * Il 24 giugno sono stato a Milano come speaker di [AIConf](https://www.aiconf.it/). Grazie a tutti quelli che hanno partecipato e mi hanno dato feedback sul mio talk. Trovate le slide, il form di feedback e tutti i link [qui](https://maeste.it/speaking/aiconf2026.html), e presto aggiungerò anche il video dell'intervento.
  * Martedì 30 alle 20 farò una [live su X e su YouTube con Ivan Fioravanti](https://x.com/dom_gag_96/status/2069706343401857183?s=46). Argomento: gli agenti personali, Hermes e GBrain. Seguiteci... potrebbero esserci sorprese.

---

## Sistemi multi modello e multi agente: due anni fa era troppo presto, adesso ci siamo

Due anni fa mettevo le mani su un PoC che si chiamava [wise-agents](https://github.com/wise-agents/wise-agents). L'idea che inseguivo era questa: un sistema multi agente in cui tanti modelli piccoli si dividono il compito e si orchestrano tra loro per risolvere problemi complessi, invece di affidare tutto a un unico modello gigante. Funzionava a sprazzi, ed era evidentemente troppo presto, i modelli di allora non reggevano il gioco. Ma l'intuizione, a distanza di due anni, la ritrovo dappertutto.

Il primo a renderla popolare, mesi fa, è stato Karpathy con [llm-council](https://github.com/karpathy/llm-council): tu fai una domanda, l'intero consiglio risponde, ogni modello legge le risposte anonimizzate degli altri e le ordina per qualità, e un chairman sintetizza la risposta finale. Anonimizzate apposta, così nessun modello tifa per il proprio brand. Lui stesso dice che non lo supporterà ("il codice ormai è effimero"), ma il giocattolo ha fatto scuola, e da lì sono nate parecchie implementazioni in giro, più o meno professionali.

Poi è arrivata OpenRouter a portarla in produzione con il suo [Fusion Router](https://openrouter.ai/docs/guides/routing/routers/fusion-router): fino a otto modelli rispondono in parallelo con accesso al web, un judge confronta le risposte (le confronta, non le fonde: consenso, disaccordi, lacune, punti ciechi) e il tuo modello sintetizza. È solido, ma con un limite che mi sento di sottolineare, è stato pensato e testato soprattutto, forse solo, sulla deep research. Fuori da quel caso d'uso resta ancora terreno da esplorare.

E infine arriva [Sakana Fugu](https://arxiv.org/abs/2606.21228), che è la mossa più interessante perché ribalta la prospettiva. Fugu si presenta come un modello, lo usi come fosse un singolo LLM, ma sotto il cofano è un sistema multi agente: un orchestratore che capisce la richiesta, costruisce al volo lo scaffold agentico e smista il lavoro a un team di modelli specializzati. E i numeri ci sono, SOTA su SWE-Bench Pro, Terminal Bench, LiveCodeBench, GPQA, perfino Humanity's Last Exam. Esiste già anche la riproduzione open, [OpenFugu](https://github.com/trotsky1997/OpenFugu), che definisce il cuore del sistema con una formula che mi è rimasta in testa, "a policy over models", una policy sopra i modelli, e misura +107% rispetto al miglior singolo worker.

Il punto che voglio mettere a fuoco è proprio questo. Si parla tanto di orchestrazione, ed è giusto, l'orchestrazione è il concetto che tiene insieme Karpathy, OpenRouter e Fugu. Ma sotto sotto sono tutti sistemi multi agente: non un modello più bravo, ma più agenti, spesso modelli diversi, che si dividono il lavoro e ne ricompongono i pezzi. È un cambio di unità di misura: l'oggetto interessante non è più il singolo modello, ma la squadra e chi la dirige.

E qui torno al mio chiodo fisso, l'harness. Perché se ci pensate, gran parte di questo risultato è possibile se si usa un buon harness, supportando modelli e vendor diversi per agenti e sub agenti. Per questo di recente la mia attenzione si è spostata sugli harness e su come avere il giusto contesto e i tool per supportare flussi e loop di lavoro avanzati, multi agente e con goal di lungo termine ben definiti. È l'orchestrazione, l'impalcatura attorno ai modelli, a fare la differenza, non solo il modello, specie quando il risultato che misuriamo non è quello di un'interazione da chatbot, ma un compito complesso che viene assolto in ore di lavoro.

Da ultimo, sottolineo di nuovo che questi sistemi danno il meglio dove le risposte sono confrontabili e verificabili. Dove c'è un verifier, sul codice o sulla matematica, il judge ha qualcosa di solido a cui aggrapparsi. Su terreni più sfumati il guadagno c'è, ma è meno garantito. Non è un difetto, è solo il perimetro entro cui oggi conviene di più.

Due anni fa era troppo presto. Adesso l'idea è matura, i modelli reggono il gioco, e la domanda non è più quale modello scegliere, ma come farli lavorare in squadra.

---

## I link che mi hanno colpito questa settimana

### [La Casa Bianca chiede a OpenAI di rallentare il rilascio di GPT-5.6](https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/)

Qui ritrovo, quasi fotocopiato, il discorso della settimana scorsa su Fable e Mythos. La frontiera che diventa ostaggio di una decisione politica, con tanto di approvazione governativa cliente per cliente, non è più un caso isolato, è un pattern. E ogni volta che succede, la mia tesi sugli open weight come polizza assicurativa si rafforza.

### [Liquid AI rilascia LFM2.5-230M](https://www.liquid.ai/blog/lfm2-5-230m)

Un modello da 230 milioni di parametri che gli stessi autori sconsigliano per il reasoning pesante, ma che vola su instruction following, estrazione e tool use. È esattamente il tipo di worker specializzato di cui parlavo nel deep dive: non il tuttofare, ma il pezzo giusto per un compito preciso dentro un sistema multi agente, e per giunta on-device.

### [Jalapeño: il nuovo chip di OpenAI](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)

Due cose mi colpiscono. La prima è l'integrazione verticale completa, dai prodotti ai modelli fino al silicio: OpenAI vuole controllare tutto lo stack. La seconda, ancora più interessante, è il tape-out in nove mesi accelerato dai loro stessi modelli, che riporta dritto al tema del recursive self-improvement. I numeri sul perf-per-watt però li aspetto su silicio vero.

### [Computer Use arriva su Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/)

Che il computer use entri in un modello piccolo e veloce come Flash è già notevole, ma la parte che guardo davvero è un'altra: conferma utente sulle azioni sensibili e stop automatico in caso di prompt injection. È il problema di permessi e governance che ripeto da mesi, e su cui lavoriamo con Lince. Senza quei controlli, il computer use long-horizon in produzione non ce lo metti.

### [Accelerare il fine-tuning con NVIDIA NeMo AutoModel](https://huggingface.co/blog/nvidia/accelerating-fine-tuning-nvidia-nemo-automodel)

Rendere il fine-tuning dei MoE accessibile con una sola riga di import, e portare in portata modelli prima fuori scala, è il genere di lavoro poco appariscente che però alimenta tutto il resto. Se vogliamo davvero sistemi multi agente con worker finetunati apposta per il loro pezzo, ci servono esattamente strumenti così, che abbassano la soglia d'ingresso.

### [Apple aumenta i prezzi di Mac e iPad per la carenza di chip di memoria](https://www.pbs.org/newshour/economy/apple-increases-prices-for-macs-and-ipads-blaming-memory-chip-shortage-fueled-by-ai)

Notizia in apparenza noiosa, ma c'è un cortocircuito che mi fa riflettere. La RAM unificata è proprio ciò che rende Apple la macchina migliore per l'inferenza locale, e ora è la carenza di chip di memoria, spinta dall'AI, a far salire i prezzi. Il boom dell'AI rende più caro l'hardware che serve a portarsela in casa, un attrito sul futuro ibrido di cui parlo spesso.

### [Mercury 2 di Inception Labs batte DiffusionGemma di Google](https://decrypt.co/371722/inception-labs-mercury-2-ai-beats-googles-diffusiongemma)

Chiudo con un modello che parla dritto al deep dive. Il titolo è la velocità, mille token al secondo grazie alla diffusione, ma il dettaglio che mi fa drizzare le orecchie è che viene proposto esplicitamente per i sistemi multi agente. Ha senso: quando moltiplichi le chiamate tra agenti, la latenza si somma, e un worker così veloce cambia cosa diventa fattibile.
