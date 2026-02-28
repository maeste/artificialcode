In questo numero della newsletter esprimo un paio di opinioni forti. La prima è essenzialmente contenuta in uno degli action items dell'ultima sezione:

> "Quando leggi di licenziamenti a causa dell'AI, cerca sempre il secondo comunicato: il contesto business spesso racconta una storia molto diversa"

Ovviamente mi riferisco ai recenti 4.000 licenziamenti di Block e all'AI washing che si è osservato intorno alla notizia e agli annunci della stessa.

La seconda opinione, che viene soprattutto dal mio uso quotidiano dell'AI assisted coding, è che Claude Code sia ad oggi la scelta più naturale in quel campo, nonostante Codex ed altri avanzino nel numero di utilizzatori, restano a varie lunghezze. A questo aggiungo che le novità che arrivano da parte di Anthropic sembrano sempre molto ben ragionate per migliorare l'esperienza e le performance degli sviluppatori. Secondo me il motivo sta nel fatto che anche per gli sviluppi interni di Anthropic, Claude Code sia il principale contributor.

Prima di lasciarvi alla lettura delle notizie e delle mie analisi di cosa è successo in settimana, fatemi dire cosa è successo, sta per succedere o succederà nella mia agenda pubblica, per chi volesse seguire i miei interventi o volesse incontrarmi di persona (adoro scambiare opinioni con chiunque abbia voglia di farlo):

* [Podcast](https://risorseartificiali.com) con Alessio e Paolo:
  * Il 12 Marzo saremo al JUG di Milano per registrare la nostra prima puntata live. [Non mancate](https://www.eventbrite.com/e/risorse-artificiali-appunti-e-spunti-dal-mondo-dellai-tickets-1983617212480?aff=oddtdtcreator)
  * Sabato è uscita una puntata in cui torniamo a parlare diffusamente di AI coding, agenti, e tante novità
  * Stiamo lavorando ad altre interviste e puntate con ospiti molto interessanti
* Da solo:
  * Mi hanno intervistato di nuovo al podcast opensource. Stavolta parlo di agenti, AI, AGI. [Uscita qui il 26](https://open.spotify.com/show/3EAhXkBUmHE1a8vFTH84Yg?si=bacd744b0f9c4a55). Ascoltatela e fatemi avere i vostri commenti
  * Il 24 Marzo sarò al Voxxed Day a Zurigo. Io e Alessio [presentiamo un talk sull'AI assisted coding](https://vdz26.voxxeddays.ch/talk/?id=8057)
  * Il 25 Marzo sarò speaker in questo meetup a Milano sul [Vibe Coding e Agentic Engineering](https://www.eventbrite.it/e/biglietti-meetup-13-vibe-coding-1983538213191?aff=ebdssbcategorybrowse)
  * Il 30 Maggio avrò l'onore di essere uno dei PyCon Italia [speakers](https://2026.pycon.it/en/speakers)

Ma partiamo dall'AI research, perché anche questa settimana ci sono novità rilevanti sul fronte dei modelli.

---

## 🔬 Novità e ricerca nei modelli AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** La competizione AI si è spostata dall'asse quantità-rilasci verso l'innovazione architettonica: DeepSeek V4 con Engram e Qwen3.5 con MoE ottimizzato mostrano che la frontier si sposta anche attraverso efficienza, non solo potenza bruta
- **Takeaway 2:** Google consolida la strategia multifront: dopo Gemini 3.x sugli LLM, Nano Banana 2 copre la generazione immagini con capacità native di riconoscimento e coerenza — non più modelli separati ma ecosistema integrato
- **Takeaway 3:** La voce come interfaccia naturale con i modelli è una tendenza in accelerazione: strumenti come Wispr Flow segnalano un cambio di paradigma nell'interazione uomo-macchina che va oltre la semplice trascrizione

- **Action Items:**
  - Testa Nano Banana 2 su image generation con focus su testo e coerenza
  - Monitora il rilascio di DeepSeek V4 e l'architettura Engram

### Cosa succede questa settimana?

Una settimana di relativa calma nel mondo dei modelli...o quasi. Certo non ci sono 3 SOTA o 5 rilasci di nuovi modelli cinesi come nelle ultime settimane, ma ci sono almeno un paio di cose molto rilevanti ed altre che comunque confermano il panorama dell'AI sempre in grande fermento per quanto concerne l'incremento di performance (in termini di qualità e potenza) dei modelli di linguaggio e non solo. Partiamo dall'annuncio principale della settimana che è l'arrivo sul mercato di Nano Banana 2, il nuovo modello di generazione di immagini di Google. Chiaramente è parte della strategia di Google di portare avanti la loro offerta su tutti i fronti, così dopo l'annuncio di Gemini 3.1 di settimana scorsa sul fronte degli LLM, ecco arrivare il modello stable diffusion (anche se forse definirlo "solo" stable diffusion è limitativo). Cosa c'è di nuovo? Tanto: ovviamente ottima qualità, soprattutto nelle figure umane e nel testo, grande coerenza tra una immagine e l'altra e capacità di editing dell'immagine. Ma non solo, nativa capacità di riconoscere le immagini generate e quella che i creatori definiscono "una grande conoscenza del mondo" per generare ambientazioni realistiche a partire da semplici prompt. La seconda notizia da sottolineare è il rilascio da parte di Alibaba della nuova famiglia di modelli Qwen 3.5 (di cui vi ho già accennato settimana scorsa, ma che merita un approfondimento). Come sempre una famiglia di modelli, non solo uno con benchmark notevoli su tutti i fronti. Insomma la big tech più big della Cina non sta certo a guardare né gli US né la concorrenza interna che viene da startup come Moonshot, Z.ai o Deepseek. Proprio parlando di Deepseek, ci sono insistenti rumors di un imminente rilascio di Deepseek V4. Al di là di polemiche su presunte distillazioni usando i modelli SOTA americani (onestamente un po' sterili da chi ha usato dati e testi protetti da diritto d'autore per trainare i propri modelli), quello che voglio sottolineare da un punto di vista tecnico è che si tratterebbe del primo modello ad usare una architettura Engram. Ci vorrebbe un articolo intero per discutere come Engram riduce la complessità quadratica della sparse attention e quindi l'uso di VRAM per la KV cache ed è oltre lo scopo di questa newsletter. Però è l'ennesima conferma di quanto Deepseek stia puntando sull'innovazione più che sulla forza bruta.

Chiudiamo con una nota su una tendenza trasversale: si cominciano a vedere sempre più frequentemente proposte di interazione vocale con il PC e con i modelli — Wispr Flow ne è un esempio concreto. Credo che sia una tendenza significativa, solida e molto interessante.

### I link della settimana

- [Nano Banana 2](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) — Il nuovo modello di generazione immagini di Google: alta qualità su figure umane e testo, coerenza multi-immagine e "conoscenza del mondo" per ambientazioni realistiche.
- [DeepSeek V4: Rumors vs Reality for the Next Big Coding Model](https://blog.kilo.ai/p/deepseek-v4-rumors-vs-reality-for) — Analisi dei rumors su DeepSeek V4: architettura Engram, contesto 1M+ token e prezzi ~$0.27/M token, in un mercato già molto competitivo.
- [Anthropic: Detecting and Preventing Distillation Attacks](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks) — Anthropic rivela campagne industriali di distillazione illecita su Claude da parte di DeepSeek, Moonshot e MiniMax tramite circa 24.000 account fraudolenti.
- [Wispr Flow](https://wisprflow.ai/) — App voice-to-text AI per qualsiasi app e dispositivo, con auto-edit, supporto 100+ lingue e accesso gratuito illimitato durante il lancio Android.
- [Qwen3.5: Towards Native Multimodal Agents](https://qwen.ai/blog?id=qwen3.5) — Alibaba rilascia Qwen3.5, famiglia MoE con 397B parametri (17B attivi), contesto 256K, 201 lingue, 19× più veloce di Qwen3-Max, licenza Apache 2.0.

---

## 🤖 Agentic AI

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Guardrail architetturali, non solo nel prompt: la compressione del contesto può far perdere istruzioni critiche — serve sicurezza infrastrutturale indipendente dall'LLM
- **Takeaway 2:** Autonomia e capacità decisionale degli agenti sono la variabile critica per il successo in produzione — misurarle è prioritario, non opzionale
- **Takeaway 3:** Agenti su UI umane: come i robot umanoidi, l'inefficienza dell'interfaccia è accettabile perché l'infrastruttura esiste già

- **Action Items:**
  - Verifica che i tuoi guardrail agentici siano architetturali, non solo nel prompt
  - Leggi la ricerca Anthropic sull'autonomia degli agenti

### Cosa succede questa settimana?

Partiamo da un post su X che ha fatto molto parlare di sé: quello di Summer Yue. Per chi non lo sapesse, lei è responsabile di Safety & Alignment nel laboratorio di Superintelligence di Meta. Il post racconta di come si sia lasciata sfuggire di mano OpenClaw che stava per cancellare tutta la sua posta elettronica (pare che sia riuscita a sventare il disastro). Al di là delle considerazioni sul suo ruolo o su OpenClaw che lasciato troppo libero può fare disastri, a me piace sottolineare che lei aveva dato una istruzione nel system prompt di non farlo, ma (pare per compressione del contesto) è andata persa. Alla fine io dico brava ad averlo postato invece di tenerselo per sé, speriamo che serva a far capire a tutti (e al mondo enterprise) che servono guardrail forti e fuori dal controllo degli LLM se e quando si fanno fare cose potenzialmente rischiose.

Gli altri due link ci parlano invece di agenti con sempre maggiori capacità, capaci di emulare l'uso umano del computer e con una indipendenza e capacità decisionale in crescita. Vi invito a leggere la ricerca di Anthropic perché appunto questa indipendenza e capacità decisionale sono le chiavi del successo o insuccesso degli agenti e di una economia degli agenti.

Il nuovo agente di Perplexity invece l'ho citato per mostrarvi che, esattamente come accade per la robotica con form factor umanoide, a volte sia più conveniente fare in modo che gli agenti usino interfacce disegnate per gli umani, nettamente più inefficienti di quelle fatte per interazione tra macchine. Perché? Semplicemente perché quelle UI ci sono già.

### I link della settimana

- [Anthropic Research: Measuring AI Agent Autonomy in Practice](https://x.com/anthropicai/status/2024210053369385192) — Framework Anthropic per valutare indipendenza e capacità decisionale degli agenti AI in diversi scenari di deployment, nel contesto della sicurezza agenti.
- [Introducing Perplexity Computer](https://www.perplexity.ai/hub/blog/introducing-perplexity-computer) — Lavoratore digitale general-purpose che unifica le capacità AI in un unico sistema, opera interfacce umane autonomamente e può girare per ore o mesi.
- [Summer Yue su X — OpenClaw inbox incident](https://x.com/summeryue0/status/2025774069124399363) — La responsabile Safety di Meta Superintelligence racconta come OpenClaw stesse per cancellare la sua inbox: 9.8 milioni di visualizzazioni, lezione pratica sui guardrail agentici.

---

## 💻 AI Assisted Coding

### I Takeaways per gli AI Engineers

- **Takeaway 1:** La durata di un task autonomo portato a successo è un KPI fondamentale per misurare la maturità degli agenti: i 25 ore di Codex e il 30% di PR autonome di Cursor sono i nuovi benchmark di riferimento
- **Takeaway 2:** L'auto-memory di Claude Code è la forma più pragmatica di apprendimento continuo verticale disponibile oggi: imperfetta ma concettualmente potente — trasforma ogni sessione in esperienza persistente
- **Takeaway 3:** La sicurezza del codice generato da AI sta diventando una specializzazione a sé: agenti come Claude Code Security Research non sono opzionali ma infrastruttura necessaria in un mondo dove il codice è sempre più generato

- **Action Items:**
  - Configura e sperimenta Claude Code auto-memory nel tuo progetto principale
  - Leggi l'articolo di Thariq su come modellare l'action space degli agenti

### Cosa succede questa settimana?

Tante notizie in quella che è la categoria più in fermento degli ultimi mesi, quella sull'AI assisted coding. Partiamo dall'evoluzione degli agenti autonomi in casa Cursor ed OpenAI. I primi dichiarano che circa il 30% delle loro PR arrivano da agenti autonomi, con un intervento umano minimo. I secondi riportano un impressionante task completato da Codex in circa 25 ore di lavoro: come ho già detto tante volte, la lunghezza di un task autonomo portato a successo è uno dei parametri fondamentali per valutare l'evoluzione degli agenti.

Per quanto riguarda le novità, Claude Code la fa da padrone in questo ambito, come è sempre stato negli ultimi mesi. Il passo di novità in casa Anthropic per gli AI Engineer è davvero difficile da tenere, ma le novità di questa settimana richiedono e meritano un approfondimento. Il concetto di auto-memory, in cui Claude capisce cosa di quanto accaduto in una sessione può essere significativo come memoria di lungo termine, è un concetto potente. Probabilmente ancora imperfetto, ma è quanto più si può avvicinare ad una versione light di apprendimento continuo, almeno in un verticale. La sicurezza è un tema fondamentale in un mondo in cui gran parte del codice è generato, e quindi agenti specializzati come "Claude Code Security Research" diventeranno un fondamentale supporto per gli sviluppatori e anche un aiuto per chi si occupa primariamente di sicurezza.

Concludo menzionando l'interessante articolo di uno dei creatori di Claude Code che ci insegna come modellare i nostri flussi e le skills per ottimizzare l'interazione tra uomo e macchina, e anche l'articolo che prova a spiegare perché Claude è ad oggi la scelta primaria tra gli agenti di coding per la stragrande maggioranza degli AI engineer (anche se Codex ha dichiarato un grosso incremento di utilizzatori, resta a notevole distanza).

### I link della settimana

- [Claude Code Security Research Preview](https://www.anthropic.com/news/claude-code-security) — Anthropic lancia un'anteprima AI per identificare vulnerabilità nel codice come farebbero i ricercatori umani, con verifica multi-stadio, severity rating e approvazione obbligatoria degli sviluppatori.
- [GPT-5 Codex: 25-Hour Coding Sprint](https://developers.openai.com/cookbook/examples/codex/long_horizon_tasks) — GPT-5.3-Codex completa autonomamente un progetto da 25 ore, generando ~30.000 righe di codice con memoria strutturata in markdown e verifica qualità ad ogni milestone.
- [Why Developers Keep Choosing Claude Over Every Other AI](https://www.bhusalmanish.com.np/blog/posts/why-claude-wins-coding.html) — Analisi del perché Claude Code è la scelta primaria: editing senza corrompere il codice circostante, lettura dei file corretti, task multi-step senza perdere il filo.
- [Claude Code Auto-Memory](https://x.com/trq212/status/2027109375765356723) — Claude salva autonomamente contesto tra le sessioni: CLAUDE.md per le istruzioni dell'utente, MEMORY.md taccuino aggiornato autonomamente da Claude ad ogni sessione.
- [Lessons from Building Claude Code: Seeing like an Agent](https://x.com/trq212/status/2027463795355095314) — Framework per modellare l'action space degli agenti: strumenti calibrati sulle capacità del modello, uso strategico di AskUserQuestion, scelta tool generici vs. specializzati.
- [Cursor Agent Computer Use](https://cursor.com/blog/agent-computer-use) — Cursor lancia agenti cloud in VM isolate: più del 30% delle PR interne ora create autonomamente da agenti, con monitoraggio via video e controllo remoto del desktop.

---

## 🏢 Business e società

### I Takeaways per gli AI Engineers

- **Takeaway 1:** Il fenomeno dell'"AI washing" nei licenziamenti è reale e va riconosciuto: quando un titolo sale del 20% annunciando tagli "a causa dell'AI" mentre il CEO ammette crescita disorganica post-COVID, i segnali d'allarme sono evidenti
- **Takeaway 2:** La posizione di Amodei sul Dipartimento della Difesa è un caso raro di coerenza etica in campo AI: rinunciare a un contratto governativo per principio, in un settore dove la pressione economica è enorme, merita attenzione come modello
- **Takeaway 3:** L'arrivo degli Apple smart glasses segnerebbe una svolta nell'adozione consumer dell'AI embodied: la UI Liquid Glass suggeriva da tempo che Apple si stesse preparando a questo form factor

- **Action Items:**
  - Quando leggi di licenziamenti "a causa dell'AI", cerca sempre il secondo comunicato: il contesto business spesso racconta una storia molto diversa
  - Monitora gli annunci Apple su smart glasses: potrebbero ridefinire il mercato consumer dell'AI wearable

### Cosa succede questa settimana?

Non si può che partire dai licenziamenti di Block. Il 40% dei dipendenti, circa 4.000. Annunciato internamente e su X, dicendo che è a causa dell'AI. Ed il titolo che balza di oltre +20% in un periodo nero per tutta la borsa statunitense. Se non è AI washing questo... e in effetti lo stesso Dorsey ammette in un tweet successivo (a borse chiuse) che Block era cresciuta troppo in fretta ed in modo disorganico durante il periodo COVID. A cui andrebbero aggiunte anche considerazioni sul mercato dei pagamenti online (principale business di Block) in chiara difficoltà.

Sia ben chiaro, non sono certo io la persona che nega gli impatti dell'AI su società e lavoro: basta che leggiate la newsletter di due settimane fa per capire quanto sia preoccupato e ritenga fondamentale non farsi trovare impreparati da questa rivoluzione. Però dico anche che è più facile, comodo e redditizio in borsa, dare la colpa all'AI invece che a scelte imprenditoriali sbagliate.

Di tutt'altro tenore la notizia legata alla presa di posizione forte di Anthropic e del suo CEO Dario Amodei sull'uso di Claude da parte del dipartimento della difesa americano. Coerente e forte. A me è piaciuto molto...certo sono certo che presto il dipartimento della difesa americana troverà un altro fornitore, anzi lo ha già trovato in OpenAI...speriamo rispettando i paletti che Altman dice di aver avuto come garanzia, anche se immagino siano un filo più morbidi di quelli posti da Amodei per cui è saltato il precedente accordo.

Chiudo con una notizia di tutt'altro tenore, ovvero i rumors sull'arrivo di smart glasses in casa Apple. Sinceramente è da quando ho visto la UI tutta in trasparenza "Liquid Glass" che dico che urla "occhiali!!"

### I link della settimana

- [Statement from Dario Amodei on discussions with the Department of War](https://www.anthropic.com/news/statement-department-of-war) — Amodei rifiuta le condizioni del Dipartimento della Difesa USA su sorveglianza di massa e armi autonome, mantenendo le salvaguardie etiche di Anthropic nonostante le pressioni.
- [Jack Dorsey annuncia i licenziamenti di Block](https://x.com/jack/status/2027129697092731343?s=20) — Dorsey annuncia il licenziamento del 40% della forza lavoro di Block (~4.000 persone), attribuendolo all'AI e ai nuovi modelli di lavoro con team più snelli.
- [Jack Dorsey — secondo post](https://x.com/jack/status/2027290756793135253?s=20) — In un post successivo (a borse chiuse), Dorsey ammette che Block era cresciuta troppo velocemente e in modo disorganico durante il periodo COVID.
- [Apple AI Smart Glasses](https://9to5mac.com/2026/02/21/apple-ai-smart-glasses-rumors-sounding-more-exciting/) — Apple accelera lo sviluppo di occhiali smart AI con due fotocamere integrate, puntando a rivaleggiare con i Meta Ray-Bans nel mercato emergente dei wearable AI.
