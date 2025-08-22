# Weekly AI Trends: Impact Analysis for Engineers

*Questa settimana ci regala significativi insights dalla ricerca di MIT NANDA sull'AI enterprise che ha fatto parlare molto sui social media, anche se spesso per le ragioni sbagliate. Mentre i titoli urlano sui fallimenti dell'AI nelle aziende, la ricerca effettiva racconta una storia molto più sfumata sulle sfide e opportunità della trasformazione. Ho passato tempo considerevole ad analizzare in profondità il State of AI in Business 2025 Report, e quello che ho trovato conferma molti dei trend di cui abbiamo discusso qui per settimane. Il report non mostra fallimenti; mostra evoluzione. Evidenzia il gap tra progetti pilota e deployment in produzione, l'importanza critica dei sistemi di memoria degli agent, e l'infrastruttura emergente che permetterà la vera trasformazione enterprise. Oltre a questa ricerca fondamentale, stiamo vedendo sviluppi affascinanti dall'audace offerta di Perplexity per Chrome alla strategia di pricing aggressiva di OpenAI con GPT-5, e la continua maturazione delle architetture agentic. Per chi fosse interessato ad approfondire questi argomenti, li ho discussi a lungo nell'episodio podcast di sabato su [Youtube](https://www.youtube.com/channel/UCYQgzIby7QHkXBonTWk-2Fg) e [Spotify](https://open.spotify.com/show/16dTKEEtKkIzhr1JJNMmSF?si=900902f2dca8442e).*

## Business and Society

### Key Takeaways for AI Engineers

- **Enterprise Reality Check:** MIT NANDA rivela che solo il 5% delle organizzazioni vede ritorni trasformativi da investimenti GenAI di $30-40B, ma la "shadow AI economy" mostra il 90% di adozione individuale  
- **Memory is Everything:** I deployment di agent di successo dipendono da sistemi di memoria sofisticati e context engineering, non solo dalle capacità grezze del modello  
- **Environmental Impact:** I nuovi studi di Google e Mistral mostrano che l'impronta energetica dell'AI è gestibile con l'ottimizzazione appropriata  
- **Action Items:**  
  - Studia il report completo di MIT NANDA per i pattern di implementazione enterprise  
  - Valuta architetture memory-first per i tuoi sistemi di agent

### What's been going on this week?

Iniziamo con l'elefante nella stanza: il [State of AI in Business 2025 Report](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) di MIT NANDA. I social media si sono scatenati con questo, estrapolando la statistica che solo il 5% delle organizzazioni sta vedendo ritorni trasformativi dai loro investimenti AI. Ma questa è una lettura pericolosamente incompleta di quello che è in realtà un documento affascinante che ogni practitioner di AI enterprise dovrebbe studiare per intero.

Devo riconoscere che NANDA non è un osservatore neutrale qui. Sono profondamente investiti nello sviluppo di agent ([dai un'occhiata al loro lavoro](https://projnanda.github.io/projnanda/#/)), il che certamente influnza la loro prospettiva. Tuttavia, anche con questa premessa, la loro analisi conferma trend che sto seguendo da mesi. Il report mostra effettivamente che nonostante alti tassi di adozione (principalmente pilot), c'è una trasformazione minima in corso. Ma ecco quello che gli scettici non vi stanno dicendo: il report spiega accuratamente perché e offre soluzioni concrete.

La ricerca rivela che i chatbot superano le soluzioni custom o basate su agent, ma attribuisce questo all'immaturità delle piattaforme agent piuttosto che a limitazioni fondamentali. Più criticamente, enfatizza che le aziende hanno disperatamente bisogno di guidance esperta e framework. Le aziende che tentano implementazioni solo senza consulenza appropriata o metodologie falliscono a tassi significativamente più alti. Il fattore chiave di successo che emerge ripetutamente è la memoria degli agent e le capacità di apprendimento. Il report martella questo punto: i pilot di successo che si laureano alla produzione presentano invariabilmente sistemi di memoria sofisticati e usano quella memoria per context engineering e condizionamento comportamentale.

Il Capitolo 4 delinea brillantemente quello di cui i clienti enterprise hanno effettivamente bisogno: *"Un vendor di cui ci fidiamo; Comprensione profonda del nostro workflow; Interruzione minima agli strumenti attuali; Confini dati chiari; La capacità di migliorare nel tempo; Flessibilità quando le cose cambiano."* In altre parole, hanno bisogno di agenti e di un buon vendor che fornisca loro un framework su cui costruirli. Il Capitolo 5 fornisce la ricetta di NANDA per trasformare i pilot in successi, e mentre il loro bias verso lo sviluppo agentic è chiaro, la loro visione è convincente. Il mio passaggio preferito cattura la trasformazione che ci aspetta: "*L'infrastruttura per supportare questa transizione sta emergendo attraverso framework come Model Context Protocol (MCP), Agent-to-Agent (A2A), e NANDA, che abilitano l'interoperabilità e coordinazione degli agent. Questi protocolli creano competizione di mercato ed efficienze di costo permettendo agli agent specializzati di lavorare insieme piuttosto che richiedere sistemi monolitici. E questi framework formano le fondamenta dell'emergente Agentic Web, una mesh di agent e protocolli interoperabili che sostituisce le applicazioni monolitiche con layer di coordinazione dinamici."*

Il panorama enterprise AI si sta scaldando in altri modi affascinanti. [L'audace offerta di Perplexity di $34.5 miliardi per Chrome](https://finance.yahoo.com/news/perplexity-ai-offers-34-5-153658141.html) rappresenta una mossa coraggiosa per controllare la distribuzione mentre Google affronta procedimenti antitrust. Si impegnano a mantenere Chromium open source, investire $3 miliardi nel progetto, e mantenere Google come ricerca predefinita. Nel frattempo, [Sam Altman sta delineando la roadmap da trilioni di dollari di OpenAI](https://link.mail.beehiiv.com/ss/c/u001.KT4rQsO6sHS_v2VASG2xukYrcBLmr-VWvDqpbYLTfcSTlKShOIF6oP8VsdYbadggQmWzSZXRPycAyzidsNqxDEdjBB1Ihf-GCOncldzNWOGEeMJQtsLDRHutTG6qCZhEwKbZ_dubtmszshAys9W6ZQBYmRBX0p6j7uj-rxo66SGjobLHVIcbjBw22ppbHqF6ggRzrKHM45jhokmnUW1HBbFEPKlTCETDemWCMQgsFSOTubHOe-n_x0mjd8HHm2DjUuKi9QfvdymmZrnRQMNUNeWSjp6rkMXKMawGZlRcRfpgY559T1OUgt5bhBlMGsUL) con investimenti massicci in infrastrutture nei data center e chip specializzati per lo sviluppo AGI.

Sul fronte geopolitico, [i commenti di Altman sulle capacità AI della Cina](https://www.tomshardware.com/tech-industry/openai-ceo-sam-altman-says-that-export-controls-alone-wont-hold-back-chinas-ai-ambitions-my-instinct-is-that-doesnt-work) suggeriscono che gli US potrebbero sottovalutare il progresso cinese. Il suo scetticismo sui controlli alle esportazioni da soli per contenere le ambizioni della Cina si allinea con [lo sviluppo di Nvidia di nuovi chip specifici per la Cina](https://links.tldrnewsletter.com/RHSndm) che supererebbero l'attuale H20, approfittando della recente apertura di Trump a vendite di chip più avanzati.

La conversazione ambientale sta finalmente ottenendo dati seri. [L'analisi di Google dell'impronta ambientale di Gemini](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference) rivela che ogni query di testo usa energia equivalente a guardare la TV per nove secondi, con il modello che diventa 33x più efficiente energeticamente e riduce l'output di carbonio di 44x nell'ultimo anno. Una query Gemini consuma 0.24 Wh, leggermente sotto la media di 0.34 Wh di ChatGPT. [Il contributo di Mistral agli standard ambientali](https://mistral.ai/news/our-contribution-to-a-global-environmental-standard-for-ai) enfatizza la responsabilità collettiva attraverso la catena del valore AI per affrontare gli impatti ambientali mentre l'AI si integra più profondamente nella nostra economia.

Una nota intrigante dal settore finanziario: [la ricerca sul trading con ChatGPT](https://marginalrevolution.com/marginalrevolution/2025/08/trading-with-chatgpt.html) mostra numeri significativi di investitori che usano AI per decisioni di trading, potenzialmente impattando la volatilità del mercato e la formazione dei prezzi. Interessante l'ironia che i professionisti della finanza dichiarano di non usare GPT mentre i volumi di trading che crollano durante i malfunzionamenti di ChatGPT suggeriscono il contrario.

## 🤖 Agentic AI

### Key Takeaways for AI Engineers

- **Declarative Agent Design:** Le definizioni di agent basate su YAML dimostrano che natorual language e LLM prompting sono più importanti di Python o qualunque altro linguaggio per il buon funzionamento degli agenti  
- **Context Engineering \> RAG:** Focus sulla gestione intelligente della finestra di contesto piuttosto che sul retrieval tradizionale  
- **Production Reality:** Gli sviluppatori stanno discutendo nelle conferenze e online, trovando nuove ricette per questo nuovo mondo. Quelle vecchie non si applicano al nuovo mondo.  
- **Action Items:**  
  - Esplora i framework di agent basati su YAML come ADK 1.12.0  
  - Implementa architetture a due livelli con subagent stateless

### What's been going on this week?

Gli agent e i sistemi multi-agent stanno emergendo come la chiave per muovere l'AI enterprise oltre i semplici chatbot verso una genuina trasformazione dei processi. Il trend verso la composizione dichiarativa di agent sta accelerando, come dimostrato dal [nuovo supporto YAML di ADK 1.12.0](https://github.com/google/adk-python/releases/tag/v1.12.0). Il mio team ha sperimentato con questo approccio oltre un anno fa, e il ragionamento è chiaro: i componenti in linguaggio naturale che interagiscono con gli LLM sono il vero core di un agent dalla prospettiva dello sviluppatore finale. **Tutto il resto come protocolli di comunicazione, registry, discovery, monitoring e sicurezza dovrebbe essere gestito dal framework. Idem per le tecniche di context engineering avanzate dove i framework devono facilitare molto la vita degli sviluppatori.**

l [wrap-up di reAgent dal GitHub HQ](https://jonturow.substack.com/p/reagent-wrap-up-what-150-builders) ha riunito 150+ builder di agent e ha evidenziato il gap significativo tra hype mediatico e realtà di produzione.

Il design di tool per agent richiede di ripensare gli approcci tradizionali. [L'analisi di Reilly Wood dei tool MCP](https://www.reillywood.com/blog/apis-dont-make-good-mcp-tools/) spiega perché l'auto-conversione di API esistenti a tool MCP fallisce: gli agent lottano con grandi numeri di tool, le API possono far esplodere le finestre di contesto, e le API non sfruttano le capacità uniche degli agent. La soluzione implica progettare tool specificamente per il consumo degli agent da zero.

La frontiera della ricerca continua ad avanzare con [il toolkit completo di OpenCUA](https://arxiv.org/pdf/2508.09123) per agent computer-use, con 22K traiettorie di dimostrazione umana attraverso tre sistemi operativi e 200+ applicazioni. Il loro ragionamento "reflective long Chain-of-Thought" aiuta gli agent a identificare e recuperare dagli errori durante task multi-step. Nel frattempo, [Manus Wide Research](https://manus.im/blog/introducing-wide-research) si posiziona non solo come un AI ma come una piattaforma di cloud computing personale unica, definendo la categoria General AI Agents.

Forse in modo più provocatorio, [il founder di Chroma dichiara "RAG is Dead, Context Engineering is King"](https://www.latent.space/p/chroma). L'argomento: RAG bundla male tre concetti quando il vero lavoro è context engineering, determinare cosa appartiene alla finestra di contesto per ogni generazione LLM. I team top ora usano un approccio a due fasi: il retrieval di prima fase riduce 10.000 candidati a 300, poi gli LLM ri-rankano quelli ai 20-30 finali. Questo shift dal retrieval alla gestione intelligente del contesto rappresenta un ripensamento fondamentale di come alimentiamo informazioni ai language model.

Anche i player stabiliti stanno abbracciando approcci agentic. [I nuovi agent AI di Grammarly](https://link.mail.beehiiv.com/ss/c/u001.dSnm3kaGd0BkNqLYPjeMf2eV4n7e3bJOirn74G3ZyF1BAQt0YUbg1eq2UM6VoBL7RXr2npck1f6vrRi-nC_-rnFhvKiliAMrPWKkwakVzHILlRqKPVYFNqTJUkMU7y1C6-Y2CRj5F4LEyeHbhIQKfljpd2wAuWqscI93S5eCppICgOfV8y_mazcvGk_s-Sh8Oqadq8Be3j01l4VrXwW4CDogoHIlbD_3qL5NOHTPlXm6Yd1jkblq7SNc1b5yM3YzplGA5MNr0CAGgeqAJJuMclXrAJPqZyOaRJHeeX_2P4RO-6IY8R2Ur_vtdIa2peTP0JPJSWTFObSYO0Ws2FpkyVaBUrniE2rFerqxjaHxnPWTYzLK4aSsd74QZhYBMmJ8EPHywi7KZqLnGzZ475i7dB8jYVzqrv1Glm0Axl_oo2w) vanno oltre la correzione grammaticale per assistere con la strutturazione del contenuto e la personalizzazione del tono, rappresentando un'evoluzione verso assistenti di scrittura più intelligenti e contestuali.

## 🛠️ AI Assisted Coding

### Key Takeaways for AI Engineers

- **GPT-5 Coding Performance:** Uguaglia Claude Sonnet con prompting basato su tag appropriato  
- **Context Expansion:** Il supporto di 1M token di Sonnet abilita l'analisi completa del codebase  
- **Vibe Coding Mainstream:** Microsoft integra il coding in linguaggio naturale direttamente nelle celle Excel  
- **Action Items:**  
  - Mastera l'API verbosity e il sistema tag di GPT-5  
  - Testa il contesto 1M di Sonnet per task di codebase grandi

### What's been going on this week?

Sto testando GPT-5 per la generazione di codice, ed è quasi al livello di Claude, almeno eguagliando Sonnet mentre Opus rimane leggermente superiore. Il gap è minimo e probabilmente colmabile con prompting più attento dato che ogni modello ha il suo stile di prompting. OpenAI ha investito pesantemente nella customizzazione comportamentale basata su tag per GPT-5, quindi probabilmente ha bisogno di una migliore utilizzazione rispetto ai miei tentativi iniziali. La [GPT-5 Prompting Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide) rivela funzionalità innovative come il parametro verbosity API che controlla la lunghezza della risposta indipendentemente dalla profondità del ragionamento, e l'API Responses che mantiene il contesto di ragionamento tra le chiamate tool. Il [cheat sheet dei consigli di coding](https://cdn.openai.com/API/docs/gpt-5-for-coding-cheatsheet.pdf) fornisce consigli pratici su come strutturare le richieste per una qualità del codice superiore e sfruttare le capacità di ragionamento del modello per debugging complesso.

[Claude Sonnet 4 ora supporta il contesto di 1M token](https://www.anthropic.com/news/1m-context) in beta pubblica sull'API di Anthropic e Amazon Bedrock, con il supporto Vertex AI pianificato. Questa massiva espansione della finestra di contesto è eccellente per contesti di programmazione lunghi con codice esteso o problemi multipli da analizzare. La validazione di Apple delle capacità di coding di Claude arriva attraverso [l'integrazione nativa di Claude in Xcode 26 beta 7](https://9to5mac.com/2025/08/18/apple-preps-native-claude-integration-on-xcode), permettendo agli sviluppatori iOS e macOS l'accesso diretto alle capacità di Claude dall'interno dell'IDE.

Ho detto ripetutamente che il Vibe Coding sostituirà i fogli di calcolo per molti casi d'uso. Bene, Microsoft sta correndo per adattarsi [mettendo vibe coding direttamente nelle celle Excel](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-ai-to-your-formulas-with-the-copilot-function-in-excel/4443487). La nuova funzione COPILOT permette agli utenti di inserire prompt in linguaggio naturale direttamente nelle celle per task come riassumere, categorizzare, o generare dati, trasformando Excel in uno strumento AI-native accessibile agli utenti non tecnici.

L'industria del gaming sta abbracciando l'AI su scala massiva secondo report recenti, integrando l'intelligenza artificiale in ogni aspetto dello sviluppo dei giochi dalla generazione di contenuto alla creazione di NPC intelligenti. [Gli sviluppatori di giochi stanno scoprendo](https://link.mail.beehiiv.com/ss/c/u001.wvWEU4waUFueFnw9YIT64guTdqFaMgjcLXsEe42LDMgLBOJfHPoh83zGeqi38QqeBYustYhWXHBrNPv94iliXxK38qE1YMeS4Qr1adafhrUMzxwelaBdH1_2q0bde1nKXxm-VvVkqWFsVE7kx-vfLgD8s36fV3fcjt-hFp7LErVY-zjFODdvRac4Dz2oMblRSlfLTdzamxpm03g8kcNRDUteerhwAU_35Qo-OMHvrx4M4GEOxBiH_OpFlnu9JDsA7chOKPZTu9QCoJJGla3Wnsux6n5nWDszYRZwCYd8n_HNji2oz_ckM9xvUOJEcZ76ZokFbZWQ_rYjkKKyTf9oBkpCPRdtWSU6JNAgUtWXkGnfw7EO9Q9v5gev1vmhQeWax2DHKVF9324_Vd2rq0dMmg) che l'AI può rivoluzionare non solo la creazione di asset ma intere esperienze di gameplay, abilitando interazioni giocatore più immersive e personalizzate.

## 📈 AI Models and Releases

### Key Takeaways for AI Engineers

- **Price War Incoming:** Il pricing aggressivo di GPT-5 di OpenAI sottoquota significativamente i competitor  
- **User Experience Matters:** OpenAI riporta indietro GPT-4o dopo le lamentele degli utenti su GPT-5  
- **Chinese Competition:** DeepSeek V3.1 raggiunge la parità con i modelli occidentali a 685B parametri  
- **Action Items:**  
  - Benchmarka GPT-5 vs modelli attuali per i tuoi casi d'uso  
  - Valuta DeepSeek V3.1 per alternative open-source

### What's been going on this week?

Le mosse di OpenAI questa settimana rivelano sia avanzamento tecnico che strategia di mercato. [Il pricing di GPT-5 a $1.25 per milione di token input e $10 per milione di token output](https://techcrunch.com/2025/08/08/openai-priced-gpt-5-so-low-it-may-spark-a-price-war) sottoquota drammaticamente Claude Opus 4.1 di Anthropic e eguaglia la baseline di Gemini 2.5 Pro di Google. Questo pricing aggressivo potrebbe scatenare una guerra dei prezzi in tutto il settore. Interessante, [OpenAI sta riportando indietro GPT-4o come opzione](https://www.theverge.com/news/756980/openai-chatgpt-users-mourn-gpt-5-4o) dopo che gli utenti si sono lamentati della mancanza della sua percepita personalità e flessibilità. L'impegno di Sam Altman per affrontare le preoccupazioni sulle performance mostra la responsività di OpenAI al feedback degli utenti.

Il breakthrough tecnico dietro l'efficienza di GPT-5 viene dal [nuovo tipo di dato MXFP4 di OpenAI](https://www.theregister.com/2025/08/10/openai_mxfp4), che promette risparmi computazionali massicci rispetto ai tipi di dato tradizionali. Questa innovazione permette di far stare un modello da 120 miliardi di parametri in una GPU con solo 80GB di VRAM, potenzialmente riducendo i costi di inference del 75%.

Google sta avanzando su fronti multipli. [La nuova funzionalità di memoria automatica di Gemini](https://www.theverge.com/news/758624/google-gemini-ai-automatic-memory-privacy-update) ricorda i dettagli delle conversazioni senza prompt, personalizzando l'output basato su interazioni passate. L'azienda sta anche [espandendo AI Mode per la ricerca conversazionale globalmente](https://blog.google/products/search/ai-mode-agentic-personalized), aggiungendo capacità agentic per prenotazioni ristoranti negli US per abbonati AI Ultra. Sul lato efficienza, [Gemma 3 270M](https://developers.googleblog.com/en/introducing-gemma-3-270m) offre strong instruction-following in un pacchetto tiny da 270 milioni di parametri, usando solo lo 0.75% di batteria per 25 conversazioni su un Pixel 9 Pro.

Lo sviluppo AI cinese continua ad accelerare. [DeepSeek V3.1 è uscito silenziosamente](https://links.tldrnewsletter.com/XLCW5L) con 685 miliardi di parametri, raggiungendo punteggi di benchmark che rivalleggiano i sistemi proprietari di OpenAI e Anthropic. Il modello rappresenta una sfida significativa al dominio AI occidentale. [L'imminente lancio di DeepSeek-R2](https://www.huaweicentral.com/huawei-ai-chip-powered-deepseek-r2-tipped-to-launch-this-month) sui chip AI di Huawei promette un'architettura Mixture-of-Experts avanzata che potenzialmente raddoppia i parametri di R1. ByteDance non sta nemmeno ferma, rilasciando [Seed-OSS-36B](https://links.tldrnewsletter.com/P4UlNL) con contesto di 512K token, progettato per ragionamento avanzato con varianti sia sintetiche che non-sintetiche.

## 🦾 Robotics and AI of things

### Key Takeaways for AI Engineers

- **Reality Check:** I giochi robotici cinesi mostrano limitazioni attuali ma commitment di investimento massiccio  
- **Video as Policy:** Usare la generazione video come proxy per le policy di controllo robot  
- **Home Integration:** Gemini sostituisce Google Assistant attraverso i dispositivi Nest questo autunno  
- **Action Items:**  
  - Studia le tecniche di transfer video-to-policy  
  - Preparati per il surge del deployment robotico consumer

### What's been going on this week?

I [Humanoid Robot Games a Pechino](https://links.tldrnewsletter.com/NUH3Fo) hanno offerto una finestra affascinante sullo stato attuale della robotica. Con 280+ team da 16 paesi che competevano in calcio, sprint e kickboxing, i robot cadevano frequentemente, rivelando l'immaturità della tecnologia. Ma questo è esattamente il punto. Questi eventi servono scopi multipli per lo sviluppo robotico cinese: costruzione dell'accettazione pubblica, dimostrazione del progresso, e più criticamente, raccolta dati del mondo reale. [Il commento di Azeem Azhar](https://substack.com/@exponentialview/note/c-146641930) nota che nonostante le cadute frequenti, il progresso in locomozione e equilibrio dimostra il rapido avanzamento della Cina nella robotica umanoide.

L'investimento massiccio della Cina nella robotica non è solo per orgoglio nazionale. È una mossa strategica per il dominio manifatturiero e per affrontare le sfide demografiche. Queste dimostrazioni pubbliche, mentre mostrano le limitazioni attuali, rivelano anche la traiettoria e il livello di commitment. Ogni caduta genera dati preziosi, ogni calcio riuscito fa avanzare il campo. La volontà di mostrare pubblicamente tecnologia imperfetta dimostra fiducia nel percorso di sviluppo.

La frontiera della ricerca sta esplorando approcci innovativi al controllo robot. Il paper ["Video Generators are Robot Policies"](https://arxiv.org/abs/2508.00795v1) propone di usare la generazione video come proxy per imparare policy robot, affrontando sia la generalizzazione sotto shift di distribuzione che la limitazione dei dati di dimostrazione umana. Questo approccio potrebbe accelerare drammaticamente l'apprendimento robotico sfruttando i dataset massicci usati per la generazione video.

La robotica consumer sta prendendo un percorso diverso attraverso l'integrazione smart home. [Google sta sostituendo Assistant con Gemini attraverso speaker e display Nest](https://blog.google/products/gemini/gemini-live-updates-august-2025) questo autunno, portando AI conversazionale avanzata, Gemini Live, e consapevolezza multi-dispositivo al controllo smart home. Questo rappresenta un passo significativo verso l'integrazione dell'AI conversazionale nella vita domestica quotidiana, potenzialmente preparando il terreno per un'integrazione robotica domestica più sofisticata.
