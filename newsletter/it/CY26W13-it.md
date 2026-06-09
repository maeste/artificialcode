Benvenuti alla newsletter di questa settimana, in cui vi cerco di parlare dell'esigenza di sicurezza che hanno gli agenti da un lato, ma anche della crescente autonomia che si cerca di dare loro per diventare sempre più utili. Le due cose non sono in netto contrasto, ma il mio è un invito a tenere sempre presente la necessità di avere sandbox e guardrail che limitino i problemi che si possono creare da una grande libertà lasciata agli agenti in fase di ideazione, che è però necessaria per dare loro l'autonomia di cui hanno bisogno per diventare ancora più potenti. Non mancano novità sul fronte dei modelli e su ricerche molto interessanti, soprattutto nell'ottimizzazione della memoria. Probabilmente non un caso, vista la crescente difficoltà nel reperimento della memoria stessa e quindi l'aumento dei prezzi. La sezione Business e società si divide tra scelte forti di OpenAI e un senatore americano che investe l'intelligenza artificiale di un ruolo, quello dell'oracolo, che forse non le è proprio. Prima di lasciarvi alla lettura, vi ricordo tutte le occasioni in cui potete incontrarmi dal vivo per scambiare opinioni e arricchirci a vicenda.

* [Podcast](https://risorseartificiali.com) con Alessio e Paolo:
  * Stiamo lavorando ad altre interviste e puntate con ospiti molto interessanti.
  * Ormai sapete del nostro repository su GitHub con tool e configurazioni per fare AI coding da terminale su Linux. Questa settimana abbiamo rilasciato una dashboard completa... quasi un IDE per agenti, ma tutto da terminale: [LINCE - Linux Intelligent Native Coding Environment](https://github.com/RisorseArtificiali/lince)
* Da solo:
  * Il 30 maggio avrò l'onore di essere uno dei [PyCon Italia speakers](https://2026.pycon.it/en/speakers)
  * Il 12 giugno sarò a Catania come speaker al [Coderful](https://www.coderful.io/)

## Novità e ricerca nei modelli AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** ARC-AGI-3 conferma che l'AGI richiede capacità agentiche di adattamento ad ambienti senza regole predefinite, non solo pattern matching.
- **Takeaway 2:** La compressione della KV cache (TurboQuant) potrebbe abilitare sia modelli più grandi in locale sia contesti enormemente più lunghi sui modelli di frontiera.
- **Takeaway 3:** Mistral potrebbe trovare la sua nicchia nei modelli specializzati (come Voxtral TTS) piuttosto che competere sui large language model di frontiera.

- **Action Items:**
  - Provare a quantizzare un modello locale seguendo la guida "quantizzazione dalle basi" per valutare il trade-off qualità/dimensione sulla propria macchina.
  - Testare Voxtral TTS per casi d'uso multilingue, approfittando delle 9 lingue supportate e della bassa latenza.

### Cosa succede questa settimana?

La novità principale da segnalare nel mondo dei modelli è sicuramente l'uscita del nuovo benchmark ARC-AGI-3, in cui i modelli di frontiera risolvono appena l'1% degli enigmi. C'era un grande bisogno di un nuovo benchmark che testasse l'AGI perché il precedente ARC-AGI-2 ormai non era più sfidante per i modelli di frontiera. Andando a guardare come il benchmark è stato scritto, è interessante vedere come le capacità che si testano di più sono quelle agentiche, e in particolare quelle che permettono di adattarsi a un ambiente in cui le regole non sono definite a priori. Questo suggerisce che si comincia a pensare, come in tanti hanno suggerito in passato, che per arrivare all'AGI si debba necessariamente passare dalle capacità di un robot che si muove in un ambiente senza regole definite a priori, ma che possono essere derivate dai feedback ricevuti dall'ambiente. Sicuramente interessante il nuovo approccio da parte di chi ha scritto il benchmark.

L'altra notizia importante nel mondo dei modelli è sicuramente l'uscita di TurboQuant, un modo nuovo di comprimere e quantizzare la KV cache. L'articolo e il paper sono da parte dei ricercatori di Google e promettono un'efficienza estrema per quanto riguarda la compressione della KV cache e quindi, in ultima istanza, del contesto. Quello che potrebbe succedere a breve sono due cose. La prima è la capacità di poter far girare modelli anche più grandi e complessi con un contesto decente in locale. La seconda è che i modelli di frontiera otterranno la capacità di avere contesti ancora più lunghi di quelli a cui siamo abituati adesso, e come sappiamo contesti più lunghi significano quello che normalmente viene chiamato in-context learning.

Vi propongo anche un articolo che spiega molto bene la quantizzazione rivista dalle basi. Si parla di quantizzazione dei modelli e non di KV cache come nel caso precedente, ma credo che sia una lettura utile per chi si chiede come questa tecnica funzioni.

Un'altra riflessione interessante è quella portata dall'articolo che spiega bene perché il fine-tuning è meno chiacchierato che in passato, soprattutto per motivi di costo e di mantenimento.

Infine, da non perdere il nuovo lancio di Mistral Voxtral, un modello text-to-speech veramente piccolo che ha ottimi risultati in ben nove lingue. Forse è in queste nicchie che Mistral può tornare a dire la sua, visto che di certo i suoi modelli non possono competere con quelli di frontiera, almeno per quanto riguarda i large language model.

### I link della settimana

- [ARC-AGI-3 è uscito](https://threadreaderapp.com/thread/2036861192619384989.html) — Nuovo benchmark per intelligenza agentiva: i modelli frontier risolvono meno dell'1% degli ambienti interattivi.
- [TurboQuant: ridefinire l'efficienza AI con compressione estrema](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) — Tecnica Google per comprimere la KV cache preservando le relazioni geometriche utili al modello.
- [La quantizzazione dalle basi](https://ngrok.com/blog/quantization) — Guida completa che spiega come funziona la quantizzazione dei modelli e i suoi effetti sulla qualità.
- [Mistral lancia il modello Voxtral TTS](https://mistral.ai/news/voxtral-tts) — Modello text-to-speech da 4B parametri, multilingue in 9 lingue con bassa latenza.
- [Perché non facciamo più fine-tuning?](https://www.natemeyvis.com/why-arent-we-fine-tuning-more/) — I prompt oggi bastano per la maggior parte dei casi d'uso, rendendo il fine-tuning meno necessario.

## Agentic AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** L'uso del computer "come un umano" da parte degli agenti è la chiave per riutilizzare l'enorme ecosistema di tool già esistenti senza riscriverli.
- **Takeaway 2:** La sicurezza degli agenti autonomi sta emergendo come categoria a sé: sandbox, scoring delle dipendenze e isolamento kernel sono le tre direzioni principali.
- **Takeaway 3:** Gli agenti sempre disponibili (via Channels, OpenClaw) cambiano il paradigma da "strumento on-demand" a "collaboratore persistente".

- **Action Items:**
  - Valutare Nono o Brin per isolare i propri coding agent, soprattutto se si lavora con agenti autonomi su codebase sensibili.
  - Provare Claude Code Channels con Telegram o iMessage per sperimentare il modello di agente sempre raggiungibile dal telefono.

### Cosa succede questa settimana?

Due i trend principali da evidenziare in questa sezione. Il primo è come sempre di più si vada verso agenti in grado di utilizzare il computer come esseri umani per svolgere i loro compiti. Il senso di questa cosa va ricercato nella capacità di riutilizzare tool esistenti disegnati per gli esseri umani. Un po' come quando si parla dei robot umanoidi che possono riutilizzare facilmente tutti quegli strumenti che abbiamo costruito per noi, dalla maniglia alla padella. Allo stesso modo, l'utilizzo del computer fatto come lo fa un essere umano permette di riutilizzare una serie di tool e programmi che altrimenti andrebbero riscritti o pesantemente adattati. Insieme a questo, la tendenza avviata da esperienze come quella di OpenClaw a rendere questi agenti sempre disponibili si sta diffondendo: attraverso quelli che Claude Code ha chiamato Channels, ad esempio, si ottiene un effetto molto simile a quello che OpenClaw ha reso possibile per primo.

La seconda tendenza è in qualche modo correlata a questo nuovo modo di utilizzare gli agenti, sempre presenti sui nostri computer e con sempre più capacità di interagire con quello che trovano sul computer e con tutti i nostri account. Quello di cui parlo è la tendenza a sviluppare tool che isolino gli agenti e non gli permettano di fare cose dannose, sia a livello di veri e propri sandbox, sia in modi più creativi di pensiero laterale al problema. In questo senso vi segnalo tre progetti che si chiamano Starpod, Brin e Nono, che meritano di essere guardati. Come sapete, insieme alle altre persone che con me condividono il podcast, sto lavorando a un progetto simile che abbiamo chiamato LINCE, e che integra appunto questi concetti di sandboxing e isolamento dei coding agent posti in una dashboard per un rapido coordinamento di agenti multipli, al fine di averli sempre presenti e sempre attivi. I progetti che vi segnalo mi sono piaciuti così tanto che abbiamo già integrato Nono come sandbox alternativa alla nostra sandbox nativa Linux, e stiamo ragionando anche sull'integrazione di Brin. Starpod risolve un problema leggermente diverso, ma è sicuramente qualcosa che va preso in considerazione per ambienti enterprise.

### I link della settimana

- [Claude Code e Cowork possono ora usare il tuo computer](https://www.engadget.com/ai/claude-code-and-cowork-can-now-use-your-computer-210000126.html) — Computer Use disponibile per abbonati Pro e Max su macOS.
- [Perplexity testa lo strumento Market Research per Perplexity Computer](https://www.testingcatalog.com/perplexity-tests-market-research-agent-for-perplexity-computer/) — Ricerca di mercato con fonti premium via sistema agentivo multi-modello.
- [Claude Code Channels: inviare eventi in una sessione attiva](https://code.claude.com/docs/en/channels) — Push di eventi da Telegram, Discord e iMessage nelle sessioni Claude Code.
- [Starpod](https://starpod.sh/) — Piattaforma per il deployment di agenti AI multi-tenant su larga scala.
- [Brin](https://brin.sh/) — Servizio di scoring delle dipendenze esterne per la sicurezza degli agenti AI.
- [Nono](https://nono.sh/) — Sandbox open-source con isolamento a livello kernel per agenti AI su macOS e Linux.

## AI Assisted Coding

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Le acquisizioni di Astral (OpenAI) e Bun (Anthropic) confermano che il coding è il campo di battaglia principale per i leader dell'AI.
- **Takeaway 2:** Modelli cinesi come GLM-5.1 stanno colmando il divario di qualità nel coding a prezzi aggressivi, aumentando la pressione competitiva.
- **Takeaway 3:** Claude Auto Mode è un passo avanti nei permessi automatici, ma non sostituisce una sandbox vera e propria.

- **Action Items:**
  - Esplorare Cline Kanban come possibile alternativa o complemento a Backlog.md per l'orchestrazione dei coding agent.
  - Testare GLM-5.1 su un progetto di coding non critico per verificare il rapporto qualità/prezzo rispetto ai modelli di frontiera.

### Cosa succede questa settimana?

OpenAI che acquisisce Astral fa il paio con Anthropic che qualche mese fa aveva acquisito la società che sta dietro a Bun. I due grandi nomi dell'AI si stanno focalizzando sicuramente sullo sviluppo software e si contendono le aziende che producono i sistemi di gestione delle dipendenze più interessanti nel mondo Python e TypeScript. È sicuramente una cosa da segnalare e che fa capire quanto il coding sia centrale in questo momento per queste aziende.

Un'altra notizia che mi piace segnalare è l'uscita di GLM-5.1, che ha risultati di coding che si avvicinano a quelli di Claude Opus. Come probabilmente vi ricorderete, GLM è il modello di punta di un'azienda cinese che si chiama Z.ai e che sta cercando di fare concorrenza ai modelli di frontiera per il coding con dei prezzi molto aggressivi. Benché la velocità di esecuzione non sia quella dei modelli di frontiera, l'accuratezza si sta avvicinando sempre di più.

Da segnalare di sicuro anche il nuovo Auto Mode di Claude, che permette dei permessi automatici un po' meno aggressivi rispetto a disabilitare tutti i controlli rischiosi. C'è un'opzione per farlo in Claude Code, ma va assolutamente gestita all'interno di una sandbox. Di sandbox parlo nella sezione precedente e mi ci sto molto focalizzando con il progetto LINCE. Claude Auto Mode limita un po' quei rischi, anche se le sandbox sono assolutamente sempre consigliate.

Cline Kanban è un progetto interessante e in qualche modo concorrente con Backlog.md, che tante volte ho segnalato sia qui che in podcast come uno dei miei strumenti di base per lo sviluppo agentico. Di sicuro conviene darci un'occhiata più approfondita. Io non ho ancora avuto il tempo di farlo, ma mi riprometto di farlo questa settimana. Se qualcuno ha qualche opinione forte su questo, vi prego di segnalarmelo nei commenti.

Lascio a voi la lettura del link su Cursor Composer 2 costruito su Kimi 2.5 e le questioni di trasparenza che lì sono segnalate.

### I link della settimana

- [OpenAI acquisisce Astral](https://openai.com/index/openai-to-acquire-astral/) — Acquisizione dei tool Python Ruff e uv per integrarli in Codex.
- [Cursor Composer 2 costruito su Kimi 2.5](https://techcrunch.com/2026/03/22/cursor-admits-its-new-coding-model-was-built-on-top-of-moonshot-ais-kimi/) — Modello Cursor basato su Kimi open-source di Moonshot AI, questioni di trasparenza.
- [Cline Kanban: orchestrazione multi-agente](https://cline.bot/blog/announcing-kanban) — Kanban board CLI-agnostica per gestire più coding agent in parallelo.
- [GLM-5.1 Coding: si avvicina a Claude Opus 4.6](https://help.apiyi.com/en/glm-5-1-coding-plan-claude-opus-alternative-api-guide-en.html) — 94,6% delle capacità di Opus a $3/mese da Z.ai.
- [Claude Auto Mode](https://claude.com/blog/auto-mode) — Permessi automatici in Claude Code con classificatore di sicurezza integrato.

## Business e società

### I Takeaways per gli AI Engineers

- **Takeaway 1:** La chiusura di Sora e il focus sul ricercatore automatizzato confermano il pivot di OpenAI dal consumer all'enterprise, lasciando Google quasi solo sul mercato consumer.
- **Takeaway 2:** Il collasso dell'accordo Disney da $1B rivela quanto i costi della generazione video AI siano ancora insostenibili, anche per OpenAI.
- **Takeaway 3:** Il video di Sanders con Claude solleva la questione di quanto potere e autorità stiamo conferendo all'AI nelle decisioni che contano.

- **Action Items:**
  - Guardare il video di Bernie Sanders con Claude e leggere il commento di Paolo Gervasi su LinkedIn per farsi un'opinione propria sul tema.
  - Leggere l'overview completa di Claude 2026 per mappare quali delle nuove funzionalità (Channels, Auto Mode, Computer Use) sono già utilizzabili nel proprio workflow.

### Cosa succede questa settimana?

Partiamo da due notizie su OpenAI che, anche se non sembra, sono strettamente collegate. La prima è che OpenAI annuncia in fretta e furia la chiusura di Sora. Vi ricorderete che Sora era il loro modello e tutto quello che ci girava attorno per creare video realistici, un po' come Veo per Google e tanti altri. Loro lo avevano impostato molto come un social e comunque come qualcosa da dare agli utenti consumer, e si vociferava da tempo che i costi fossero troppo elevati per essere sostenibili. Ma la notizia dentro la notizia è che sulla base di Sora, qualche mese fa, OpenAI aveva chiuso un accordo di scambio di azioni con Disney del valore di un miliardo di dollari, che con questa chiusura del progetto salta completamente. Evidentemente i costi erano veramente troppo alti per essere sostenuti, se Sam Altman decide di rinunciare a un miliardo di dollari da parte di Disney.

L'altra notizia arriva dall'interno di OpenAI: l'azienda punta tutto sulla costruzione di un ricercatore completamente automatizzato, per arrivare a un sistema multi-agente entro il 2028. In che modo questa cosa è collegata con la chiusura di Sora? Perché testimonia quanto OpenAI si stia focalizzando sul mercato enterprise e il business-to-business, lasciando un po' indietro quello consumer per una scelta di mercato. Se vi ricordate, anche tutti gli investimenti evidenti che sono stati fatti su Codex per tornare competitivi con Claude vanno in questa direzione. E chi resta sul mercato consumer in Occidente? Praticamente soltanto Google. Ma di certo Google nel mercato consumer è abituato a sguazzare.

Non so se avete visto il video del senatore Bernie Sanders che discute l'impatto dell'AI con Claude. Io mi allineo molto all'opinione che ho letto su LinkedIn di [Paolo Gervasi](https://futuripreferibili.substack.com/), che ne fa una fotografia estremamente accurata e dissacrante, paragonandolo agli antichi greci che andavano dall'oracolo a chiedere il suo giudizio, dandogli in questo modo il valore di divinità che forse l'oracolo non aveva. Lascio a voi le riflessioni su questa cosa. Ne ho parlato anche in podcast con i miei colleghi, se volete andare ad ascoltarci.

Vi saluto con un articolo che cerca, a fatica, di mettere insieme tutte le novità in casa Anthropic nel 2026. Chat, Cowork, Code, Projects: tutte le novità di Claude Code. Avrei potuto mettere questo articolo in una qualunque delle sezioni precedenti. Sta qui in Business e società perché la velocità di rilascio di nuove feature su Claude Code, e in generale in questo mondo, stanno ridisegnando il modo di fare business e gli impatti che stanno avendo sulla società. Buona lettura.

### I link della settimana

- [OpenAI punta tutto sulla costruzione di un ricercatore completamente automatizzato](https://www.technologyreview.com/2026/03/20/1134438/openai-is-throwing-everything-into-building-a-fully-automated-researcher/) — Obiettivo "intern AI" entro settembre, sistema multi-agente entro 2028.
- [OpenAI chiude Sora, crolla l'accordo da 1 miliardo con Disney](https://www.theguardian.com/technology/2026/mar/24/openai-ai-video-sora) — Shutdown di Sora e collasso del deal Disney da $1B per focus su IPO e AGI.
- [Il senatore Bernie Sanders discute l'impatto dell'AI su privacy e democrazia con Claude](https://www.youtube.com/watch?v=h3AtWdeu_G0) — Conversazione su raccolta dati, pubblicità mirata e garanzie legali.
- [Claude 2026: tutto ciò che è stato rilasciato e come usarlo](https://x.com/kloss_xyz/status/2036356467629162772) — Overview completa di Claude 4.6: Chat, Cowork, Code, Projects.
