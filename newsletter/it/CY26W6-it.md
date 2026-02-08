Settimana dominata dagli annunci di Anthropic con Claude Opus 4.6 e OpenAI con GPT-5.3-Codex poche ore dopo. E come troverete nel testo, entrambi portano significativi miglioramenti su varie metriche, ma soprattutto sul coding e sulla capacità di sviluppare codice in task lunghi, multi-agente e con pianificazioni complesse.

Le prime impressioni che ne ho avuto da qualche test diretto e leggendo articoli di developer di cui ho grande stima (e che riporto in questa newsletter) sono notevoli e mi hanno perfino fatto scrivere che su questo settore specifico i modelli si avvicinano molto al concetto di AGI. Lo so che di AGI, in cui la G sta proprio per "general", non ha senso parlare in un ambito specifico, ma avete credo capito quello che voglio dire. Vedere un modello che scrive/migliora se stesso (Codex) o scrive da zero un compilatore C in grado di compilare il Kernel Linux (Opus)... fa tremare i polsi anche a chi ne ha viste parecchie nell'informatica, o forse proprio a noi.

Ho detto AGI, e di AGI in senso più proprio e di futuri possibili, preferibili o evitabili ho parlato lungamente in intervista ad [Alessandro Maserati](https://www.linkedin.com/in/alessandromaserati/) mercoledì nel podcast [Risorse Artificiali](http://risorseartificiali.com). Sabato invece nella puntata con i miei co-host Alessio e Paolo abbiamo parlato di agenti di coding e del loro uso. Ascoltate entrambe e fatemi avere i vostri commenti.

---

## Novità e ricerca nei modelli AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Il rilascio simultaneo di Claude Opus 4.6 e GPT-5.3 segnala un cambio di paradigma: i modelli non sono più solo "più intelligenti", ma diventano vere entità agentiche capaci di pianificare e delegare task complessi su lunghi orizzonti temporali.

- **Takeaway 2:** L'evoluzione dei benchmark dal semplice pattern matching alla valutazione di capacità generative complesse (Banana) e strategiche (Kaggle Game Arena) riflette la necessità di misurare ciò che ora conta: capacità di ragionamento a lungo termine e interazione sociale.

- **Takeaway 3:** Il contesto da 1M token e i miglioramenti nell'interfaccia uomo-macchina (speech-to-text, OCR avanzato) non sono feature accessorie: sono gli abilitatori fondamentali che rendono possibile l'uso pratico di queste capacità agentiche.

- **Action Items:**
  - Sperimenta con Claude Opus 4.6 su task di lunga durata per verificare la persistenza del task.
  - Guarda i modelli giocare su Kaggle. Attenzione può diventare addictive :)

### Cosa succede questa settimana?

Come dicevo nell'introduzione le notizie della settimana più importanti sono indiscutibilmente i rilasci dei nuovi modelli di Anthropic e OpenAI. Rilasciati a poche ore di distanza introducono passi avanti rilevanti in tutte le loro abilità, soprattutto nella scrittura del codice e nella capacità di eseguire task lunghi in maniera agentica. Inoltre Anthropic sperimenta con una finestra di contesto molto più grande (fino a 1M di token), che anche se non è una novità assoluta è una cosa molto importante perché è al momento uno dei limiti principali. Il miglioramento che vediamo sui benchmark è, seppur significativo, non eclatante come poteva accadere nei rilasci di 12/18 mesi fa, ma questa è una cosa naturale almeno per quanto riguarda il modo in cui i benchmark misurano le performance di questi modelli. I risultati che vediamo sul campo sono anche più significativi perché questi modelli stanno acquisendo capacità evolute che gli permettono di scomporre e pianificare task lunghi e di assegnarli ad agenti multipli. Ci tornerò anche nel capitolo relativo all'AI Assisted Coding.

E proprio questo evolversi nei comportamenti e nelle capacità di frazionare il problema porta alla necessità di testare le risposte di questi modelli in modo diverso. Molto interessanti in questo senso sia il nuovo benchmark denominato Banana Benchmark (che sostanzialmente misura la capacità dei modelli di svolgere compiti complessi e lunghi in termini di tempo) che l'idea di far giocare i modelli a dei videogame strategicamente complessi di Kaggle. Su quest'ultima cosa immagino che molti di voi siano andati con la mente alla finale di "War Games", quando fanno giocare il computer contro se stesso a tic-tac-toe. Al di là della citazione cinematografica l'idea in sé è interessante e merita di essere approfondita, sia su Kaggle per i modelli che magari anche tra agenti, per meglio capire fino a dove oggi si può spingere la capacità di pianificazione e strategia di questi modelli.

Qualche novità anche dall'Europa e dalla Cina, sull'interfaccia uomo-macchina con un modello speech-to-text ed un modello OCR. Forse sono meno impressionanti, ma se siete attenti lettori di questa newsletter sapete che l'interfaccia uomo-macchina è una dei principali componenti dell'esperienza di uso finale e quindi passi avanti in questa area sono sempre rilevanti.

### I link della settimana

**[Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)** (12 min)
Nuovo flagship di Anthropic con agentic coding migliorato, persistenza task più lunga e finestra di contesto da 1M token in beta. Risultati SOTA su ragionamento e coding.

**[Mistral Introduces Voxtral Transcribe 2](https://mistral.ai/news/voxtral-transcribe-2)** (3 min)
Modello speech-to-text di nuova generazione con pesi aperti, latenza sub-200ms e trascrizione accurata in 13 lingue a basso costo.

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)** (Hugging Face)
Modello OCR multimodale per documenti complessi con encoder visivo CogViT e connettore leggero per efficient token downsampling.

**[Banana Benchmark](https://dwzhu-pku.github.io/PaperBanana/)**
Nuovo benchmark dell'Università di Pechino per valutare LLM su task generativi aperti (scrittura creativa, riassunti, dialogo) con annotazioni umane.

**[Kaggle Game Arena Updates](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/kaggle-game-arena-updates/)** (7 min)
Google DeepMind espande Game Arena con Werewolf e poker per testare dinamiche sociali e gestione rischio. Gemini 3 Pro e Flash dominano la leaderboard scacchi.

---

## Agentic AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** La battaglia degli agenti in azienda è ufficialmente iniziata: dopo Claude Cowork di Anthropic, OpenAI lancia Frontier. Entrambi puntano sull'integrazione con i sistemi esistenti (no replatforming) e sulla collaborazione tra agenti (protocollo A2A), ma il vero vincitore sarà chi risolve prima il problema della sicurezza.

- **Takeaway 2:** Il "context rot" è inevitabile con i modelli attuali: l'approccio dei subagenti (e MCP come protocollo) è la soluzione pragmatica migliore, che abbraccia le limitazioni dei modelli invece di combatterle.

- **Takeaway 3:** Come per l'e-commerce, l'ecosistema degli agenti ha bisogno di uno stack di sicurezza: ogni livello gestisce ciò che gli altri non possono. Le aziende che costruiranno questa infrastruttura avranno opportunità enormi.

- **Action Items:**
  - Prova il Model Council di Perplexity per confrontare approcci strategici tra modelli.
  - Valuta la tua stack di sicurezza per gli agenti: cosa succede se un agente viene compromesso?

### Cosa succede questa settimana?

Dopo il lancio di qualche settimana fa di Claude Cowork di Anthropic anche OpenAI fornisce la sua ricetta per portare gli agenti in azienda. Come Cowork integra l'uso dell'AI con i sistemi già in uso nel lavoro di tutti i giorni. In più con la promessa di essere maggiormente distribuito nella rete aziendale favorendo la collaborazione tra agenti, un po' come il protocollo A2A. Questi sistemi vanno provati (al momento non è disponibile a tutti, ma solo a un set limitato di utenti), perché cambieranno radicalmente il modo di lavorare in azienda, almeno tanto quanto lo hanno fatto i PC rispetto alla carta.

Context rot e sicurezza sono due temi fondamentali quando si parla degli agenti. Riporto due articoli su questi argomenti che valgono la lettura. Ne ho parlato anche in un panel al Voxxed Days Ticino settimana scorsa. Ricordate che "da un grande potere deriva una grande responsabilità"... anche se non siete Spiderman.

Il Model Council di Perplexity è la versione di produzione dell'esperimento di Karpathy di cui parlavamo a dicembre. Come dissi allora, ci sono nicchie in cui può essere utile, quindi bene che un vendor abbia deciso di renderlo accessibile a tutti.

### I link della settimana

**[OpenAI introduced Frontier](https://openai.com/index/introducing-openai-frontier)** (8 min)
Piattaforma enterprise per costruire, deployare e gestire agenti AI. Condivide contesto tra sistemi aziendali, onboarding, learning e permessi chiari.

**[Clawdbot's Missing Layers](https://robdodson.me/posts/clawdbots-missing-layers/)** (7 min)
Come l'e-commerce, gli agenti necessitano di uno stack di sicurezza. Ogni livello gestisce ciò che gli altri non possono. Opportunità per infrastrutture.

**[Context Management and MCP](https://cra.mr/context-management-and-mcp/)** (10 min)
Il context rot è inevitabile: la soluzione migliore sono i subagenti. Approccio pragmatico che abbraccia le limitazioni dei modelli invece di combatterle.

**[Perplexity Model Council](https://www.perplexity.ai/hub/blog/introducing-model-council)** (6 min)
Multi-model research che esegue query su più frontier AI simultaneamente, sintetizzando gli output in una risposta unificata. Disponibile per Perplexity Max.

---

## AI Assisted Coding

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Claude ha scritto un compilatore C in Rust e OpenAI dichiara che 5.3-Codex ha sviluppato se stesso. Le capacità di coding degli agenti hanno raggiunto livelli che sfidano anche il scetticismo più radicale.

- **Takeaway 2:** Gli "agent teams" di Claude Code danno a ogni agente scope ristretto e context pulito: miglior ragionamento, check quality indipendenti e checkpoint naturali. È l'architettura che risolve il limite dei sistemi single-agent.

- **Takeaway 3:** Il coding è il campo di battaglia principale: Anthropic, OpenAI, Alibaba, Apple tutti puntano qui. Chi vince sul coding vince sull'agentic AI.

- **Action Items:**
  - Abilita `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in Claude Code e prova i team di agenti specializzati.
  - Leggi l'articolo di Addy Osmani sugli agent teams: la documentazione più chiara su come funziona l'architettura a swarms.

### Cosa succede questa settimana?

Lo dicevo nel primo capitolo, i modelli rilasciati da Anthropic ed OpenAI hanno fatto grandi passi avanti su tutte le metriche, ma è chiaro che le grandi compagnie si focalizzino almeno in questo momento sul coding e sulla capacità di pianificare. E da qui escono notizie che sembrano davvero fantascienza: Claude che crea un compilatore C scritto in Rust in grado di compilare un Kernel Linux. Oppure OpenAI che dichiara che 5.3-Codex è stato sviluppato da una versione preliminare di se stesso. Prendendo per buone queste notizie e dichiarazioni (ma ovviamente i negazionisti vi diranno che sono solo inventate per fare hype), siamo davanti a delle capacità di sviluppo di questi modelli/agenti assolutamente impensabili fino a pochi mesi fa. A livello di AGI in questo specifico campo. Se leggete bene la notizia sul compilatore C vedrete che ha dei limiti, inefficienze e dipendenze che potrebbe (e forse non dovrebbe avere)... ma se ci penso bene delle persone che conosco quelle in grado di scrivere una cosa del genere le conto sulle dita di una mano... e vi garantisco che di sviluppatori Open Source di livello altissimo ne conosco tanti in giro per il mondo. Ah e nessuno di quelli sulla mia mano lo avrebbe fatto da solo in quei tempi... scettici o meno, pensateci.

Andando più sul pratico se usate Claude Code per sviluppare, vi invito a leggere bene l'articolo di Addy Osmani, perché gli agent teams sono la novità principale in casa Anthropic a mio avviso e approfondirne il funzionamento non può che migliorare il vostro workflow.

Quanto il coding sia il focus principale di tutte le grandi aziende tecnologiche in questo momento lo si vede anche dalla (rin)corsa dei cinesi proprio sui modelli di coding da un lato, e l'adozione di modelli SOTA da parte di Apple nel suo strumento di sviluppo.

### I link della settimana

**[Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler)** (13 min)
Istanze Claude multiple in parallelo hanno costruito un compilatore C in Rust per il kernel Linux 6.9. Sforzo da $20K e 2000 sessioni con supervisione umana ridotta.

**[Claude in Xcode](https://www.anthropic.com/news/apple-xcode-claude-agent-sdk)** (1 min)
Xcode 26.3 introduce supporto nativo per Claude Agent SDK: subagenti, task in background e plugin direttamente nell'IDE di Apple.

**[GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex)** (11 min)
Modello di coding agentic più veloce che combina performance di GPT-5.2-Codex con ragionamento e conoscenza professionale. Usato per trovare bug nei propri training run.

**[Claude Code Swarms - Agent Teams](https://addyosmani.com/blog/claude-code-agent-teams/)** (15 min)
Agenti che lavorano in parallelo con scope ristretto e context pulito: miglior ragionamento, check quality indipendenti e checkpoint naturali. Abilita con `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

**[Qwen3-Coder-Next for Agentic Coding](https://qwen.ai/blog?id=qwen3-coder-next)** (5 min)
Modello open-weight di Alibaba ottimizzato per coding agenti. Architettura MoE ibrida con forte performance su executable synthesis e interazione RL-based.

---

## Business e società

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Il Super Bowl come termometro culturale: Anthropic ha fatto un advertisement durante l'evento più seguito d'America. Mentre in Europa ci si interroga se l'AI sia una bolla, negli Stati Uniti è già parte del tessuto culturale, al livello di Coca-Cola e McDonald's.

- **Takeaway 2:** L'adozione dell'AI è senza precedenti nella storia: ChatGPT ha raggiunto 100 milioni di utenti in due mesi. Nessuna tecnologia — cellulari, internet — ha mai avuto un uptake così rapido.

- **Takeaway 3:** Claude rimane ad-free: Anthropic dichiara che non mostrerà pubblicità nelle conversazioni. Una presa di posizione interessante sulla fiducia e l'integrità, che contrasta con l'aggressiva presenza al Super Bowl.

- **Action Items:**
  - Leggi l'articolo con i 10 grafici sull'era AI: in pochi minuti ti dà una fotografia chiara della velocità di affermazione di questa tecnologia.
  - Leggi l'articolo di Hugging Face sull'ecosistema open source per capire la traiettoria post-DeepSeek e come l'open artifact sharing sta guidando il momentum.

### Cosa succede questa settimana?

Riporto qui alcuni link per dare una finestra sugli impatti di business che l'AI sta avendo e continua ad avere. Al di là del sorriso che mi ha strappato la pubblicità di Anthropic per il Super Bowl... il dato significativo per me è che mentre in Europa ci si chiede se queste aziende sono solo una bolla (e in fondo un po' qualcuno lo spera), una o più di queste fanno un Ad al Super Bowl. E non è solo una questione di costi, ma anche quanto quell'evento sia popolare e parte della cultura di un paese... di cui l'AI fa parte se non quanto la Coca-Cola o McDonald's, almeno abbastanza da fare pubblicità in un Super Bowl.

E a confermarlo anche i dati di adozione di OpenAI. Ma se volete provare a capire in pochi minuti non perdetevi l'articolo con i 10 grafici più significativi sull'argomento, vi danno una bella fotografia di quanto rapidamente questa tecnologia si stia affermando.

### I link della settimana

**[Claude Will Remain Ad-Free](https://www.anthropic.com/news/claude-is-a-space-to-think)** (3 min)
Anthropic annuncia che Claude non mostrerà pubblicità o contenuti sponsorizzati nelle conversazioni, per preservare fiducia e integrità nelle interazioni AI.

**[10 Charts That Explain the AI Era](https://debliu.substack.com/p/10-charts-that-explain-the-ai-era)** (7 min)
ChatGPT ha raggiunto 100M utenti in due mesi, evidenziando un'adozione senza precedenti rispetto a tecnologie passate come cellulari e internet.

**[Open Source AI Ecosystem](https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment-blog-3)** (9 min)
Esplora la traiettoria dell'open source AI dal "momento DeepSeek", evidenziando strategie a lungo termine e forecasting di momentum sostenuto.

**[xAI Joins SpaceX](https://www.spacex.com/updates#xai-joins-spacex)** (2 min)
xAI si unisce a SpaceX, integrando ricerca AI avanzata con ingegneria aerospaziale. Merger strategico tra sviluppo AI e iniziative hardware/esplorazione spaziale.
