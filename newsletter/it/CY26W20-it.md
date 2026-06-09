# Thinking Machines e OpenAI riscrivono la voce: la traduzione simultanea non è più walkie-talkie

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana importante per l'interazione vocale, con due rilasci a pochi giorni l'uno dall'altro che ho deciso di trattare insieme nel deep dive: i modelli GPT Real Time di OpenAI, usciti il 7 maggio, e gli Interaction Models di Thinking Machines, la startup di Mira Murati, presentati in pompa magna l'11 maggio. Vi racconto cosa cambia davvero rispetto alla modalità vocale a cui siamo abituati, perché un anno fa avevamo identificato la traduzione simultanea come uno dei lavori a rischio e oggi quel rischio è diventato concreto. Nella sezione link trovate temi che fanno da contorno: Gemini agentico che si installa nel sistema operativo di Android, due lavori sui modelli piccoli e modulari (i Recursive LMs e EMO di Allen AI), il framework SkillOS di Google per agenti che imparano dall'esperienza, e la tesi di Garry Tan sulla personal AI come operating system. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * È uscito [l'episodio 52 di Risorse Artificiali](https://risorseartificiali.com/2026/05/16/l-ai-un-anno-dopo/), un anno esatto di podcast senza saltare una settimana. Nell'episodio proviamo a chiederci cosa è cambiato nell'AI nell'arco di quest'anno mentre noi cercavamo di raccontarla ai nostri amici italiani.
  * Mercoledì è uscita una nuova intervista: [Domenico Gagliardi](https://risorseartificiali.com/2026/05/13/con-lai-nessun-software-e-difendibile/) (Founder e COO Kortix) spiega perché con l'AI nessun software è più difendibile, e dove resta il valore (infra + dati).
  * Ormai sapete del nostro repository su GitHub con tool e configurazioni per fare AI coding da terminale su Linux. Ora ha un suo sito con installazione a singolo script [Lince.sh](https://lince.sh)
  * Abbiamo rilasciato AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), che è un software per tradurre messaggi vocali in testo

Da solo:
  * Martedì sera sarò a Milano per partecipare [all'evento di AI Socratic Milano](https://luma.com/4vviqrs5). Se ci sarà modo presenterò anche lo stato attuale di [Lince](https://lince.sh)
  * È stato pubblicato il video del talk che ho fatto con Alessio al [VoxxedDay Zurich](https://www.youtube.com/watch?v=DXEsG3Vo6F4)
  * Il 30 maggio avrò l'onore di essere uno dei [PyCon Italia speakers](https://2026.pycon.it/en/speakers)
  * Il 12 giugno sarò a Catania come speaker al [Coderful](https://www.coderful.io/)
  * Il 24 giugno sarò a Milano come speaker di [AIConf](https://www.aiconf.it/)

---

## La voce in tempo reale: Thinking Machines, OpenAI e la fine del botta-e-risposta

Nell'arco di pochi giorni sono arrivati due rilasci che hanno spostato sul serio l'asticella dell'interazione vocale con i modelli. Il primo, il 7 maggio, è arrivato da OpenAI con [i modelli GPT Real Time](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/): tre nuovi modelli nell'API, GPT-Realtime-2 con ragionamento da GPT-5 e contesto esteso a 128K token, GPT-Realtime-Translate per la traduzione live da oltre 70 lingue verso 13, e GPT-Realtime-Whisper per la trascrizione in streaming. Quattro giorni dopo, in pompa magna, è arrivata la risposta di [Thinking Machines](https://thinkingmachines.ai/blog/interaction-models/), la startup di Mira Murati, che ha presentato gli Interaction Models in research preview: non ancora disponibili in Europa, almeno non in maniera facile, ma i video che ho visto sono francamente impressionanti. Se devo descriverli in una frase, sono la modalità vocale di ChatGPT con gli steroidi. Si tratta di modelli che rispondono alla voce in maniera realmente interattiva, costruiti da zero con un design multi-stream pensato per la responsività in tempo reale, in modo da eliminare per progettazione il limite del turno classico botta-e-risposta. Il timing di OpenAI ha forse tolto un po' di spinta al lancio di Thinking Machines, perché parte delle capacità mostrate erano già coperte dalla loro nuova API.

C'è però un dettaglio che mi ha colpito a favore di Thinking Machines: il loro modello è relativamente piccolo, 273 milioni di parametri mi pare. Vi ricordo che, rumors perché non li hanno mai pubblicati, sia Claude Opus che GPT 5.5 dovrebbero aggirarsi intorno ai 2 trillion di parametri in configurazione Mixture of Experts. Un ordine di grandezza di meno, in pratica. E i risultati sono comunque impressionanti: ci sono video di persone che parlano in maniera estremamente naturale, come se stessero parlando con un'altra persona. Il modello interrompe chi sta parlando, aspetta, riprende il filo. Chi ha provato ChatGPT vocale sa che, ad oggi, era già l'esperienza migliore in giro, molto meglio di quella di Claude, ma hai comunque la sensazione che il modello aspetti che tu faccia una pausa per capire che hai finito la frase e poi ti risponda. È sensato, dato che internamente funziona così: prende il contesto, lo spezzetta in sotto sezioni e comincia a preparare la risposta a turno.

Quello di Thinking Machines, e con buona probabilità anche il nuovo GPT Real Time, funziona invece in modo diverso. Vengono chiamati appunto real time perché riescono ad avere una comprensione al secondo di tutto quello che è il contesto fino a quel momento, rielaborandolo continuamente. Il paper non è ancora uscito, sono curioso di leggerlo, ma i rumors danno come idea che internamente stiano usando i [recursive language models](https://www.alphaxiv.org/blog/reinforcement-learning-for-rlms), qualcosa che Google ha già provato in altri contesti. E questa cosa permette una naturalezza pazzesca, tra cui la traduzione simultanea.

Ho visto un filmato di GPT Real Time ieri sera e l'effetto è esattamente questo: una persona parla in francese, la traduzione in inglese parte un paio di secondi dopo e prosegue in parallelo, come quando ascolti un traduttore simultaneo professionista. Funziona così: il modello aspetta di capire che è passato il verbo principale della frase, perché è quello a determinare la direzione semantica del discorso, e a quel punto inizia a tradurre. Thinking Machines mostra video equivalenti, e per chi sviluppa [il cookbook di OpenAI](https://developers.openai.com/cookbook/examples/voice_solutions/realtime_translation_guide) propone già tre architetture pronte all'uso (browser, Twilio, LiveKit) per traduzione broadcast, customer service e meeting multilingua.

Tra l'altro, dicevamo un anno fa, su queste stesse pagine, che la traduzione simultanea era uno dei lavori a rischio. Ecco, rischio concreto, ci siamo, siamo lì. Se prima la traduzione automatica ricordava un walkie-talkie, adesso non più. E vale anche con più lingue che si intervallano una con l'altra, perché a quel punto, una volta che hai il sistema, una lingua vale l'altra.

---

## I link che mi hanno colpito questa settimana

### [Gemini arriva su Android in versione agentica](https://techcrunch.com/2026/05/12/google-brings-agentic-ai-and-vibe-coded-widgets-to-android/)
*Google porta Gemini su Android con azioni multi-step tra app, browsing autonomo, form-filling, dictation Rambler su Gboard e widget generati in linguaggio naturale (vibe-coding). Debutto su Samsung Galaxy e Pixel quest'estate.*

Il pezzo che mi interessa qui non è tanto il widget vibe-coded, più una vetrina che altro, ma il fatto che Google stia spingendo sull'agentic direttamente sul sistema operativo mobile, con accesso reale alle app e al web. È un'altra conferma del trend che vede gli agenti uscire dalla chat e diventare ospiti dei nostri device. Resta da vedere quanto bene venga gestita la sicurezza in scenari così aperti, perché lì si gioca tutta la partita.

### [Reinforcing Recursive Language Models](https://www.alphaxiv.org/blog/reinforcement-learning-for-rlms)
*Articolo che spiega come usare il reinforcement learning per fine-tunare modelli da 4B come Recursive Language Models in produzione, eguagliando Claude Sonnet 4.6 a costi e dimensioni molto inferiori.*

Tema che mi sta a cuore da tempo: modelli piccoli, addestrati bene per compiti specifici e ricorsivamente collaborativi, possono pareggiare con i grandi. Il dato in linea con Sonnet 4.6 è notevole, soprattutto se confermato fuori dai test sintetici. Ho citato lo stesso lavoro nel deep dive come architettura plausibile dietro agli Interaction Models di Thinking Machines, perché credo che il trend dei modelli piccoli ricorsivi sia uno dei filoni più interessanti da seguire.

### [SkillOS: skill curation per agenti che imparano dall'esperienza](https://arxiv.org/abs/2605.06614)
*Paper Google su un framework RL che separa l'agent executor (frozen) da un skill curator (trainable), che gestisce un repository di skill riutilizzabili evolute dall'esperienza accumulata.*

Filone parallelo a quello di Dream nei Managed Agents di Anthropic, di cui parlavamo qualche settimana fa: gli agenti che migliorano da soli rileggendo le proprie sessioni. Qui Google formalizza la cosa con un curator dedicato e dimostra che le skill prodotte generalizzano tra modelli e domini diversi. Per chi sta costruendo sistemi agentici a lungo termine, è la direzione giusta da osservare.

### [EMO: modularità emergente nei Mixture of Experts](https://allenai.org/blog/emo)
*Allen AI rilascia EMO, un MoE da 128 esperti dove la modularità emerge naturalmente in pretraining usando i boundary dei documenti come weak supervision. Performance quasi piene con solo il 12.5% degli esperti attivi.*

Il dato che mi fa drizzare le orecchie è proprio quel 12.5%. Se davvero si tiene su task reali e non solo sui benchmark, vuol dire che si può fare deploy di sottoinsiemi specializzati di un modello e ridurre drasticamente memoria e compute. Per l'inferenza locale, di cui parliamo spesso, sarebbe un game changer. Vale la pena seguire il filone, soprattutto in chiave open weight.

### [Garry Tan: la personal AI come operating system](https://x.com/garrytan/status/2053127519872614419)
*Garry Tan (YC) presenta GBrain, sistema open source MIT che trasforma note markdown in un knowledge graph auto-organizzato, base per agenti personali con cron job autonomi.*

Quello che mi piace della tesi di Tan è l'inquadramento: la personal AI non è una chat, è un sistema operativo con harness sottile, skill grosse, codice grosso e un data layer grosso. È esattamente lo schema mentale con cui sto lavorando con [Hermes Agent](https://hermes-agent.nousresearch.com/) in casa. Il fatto che GBrain sia MIT, open source e basato su markdown è un bel manifesto: stare sopra la linea dell'API, non sotto. Da approfondire.
