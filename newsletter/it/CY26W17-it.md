# Anthropic inciampa, OpenAI spinge, io guardo open

Settimana impegnativa per Anthropic, che ha dovuto ammettere tre grosse problematiche che hanno scatenato varie reazioni nella community. Nel frattempo OpenAI recupera terreno sia su di loro con Codex e GPT-5.5, sia su Google con la generazione di immagini di ChatGPT Images 2.0 che compete da vicino o forse supera NanoBanana. I cinesi non sono da meno con l'arrivo di DeepSeek versione 4 e Qwen 3.6, tutti open source. E io mi chiedo invece se non sia ora di concentrarmi su degli strumenti open source, ma leggetevi tutto nel mio deep dive.

### La mia agenda

[Podcast](https://risorseartificiali.com) con Alessio e Paolo:
  * Nell'ultimo episodio parliamo diffusamente di quanto discuto nel deep dive di questa settimana e facciamo vedere esempi di immagini
  * È uscita una bella intervista a Luigi Congedo che ci porta la sua esperienza nei VC americani e ci racconta le sue scelte coraggiose in Italia. Non perdetevela.
  * Stiamo cercando di curare meglio il formato audio/video e presentazione del podcast... ogni feedback è gradito
  * Mercoledì prossimo torna [Stefano Gatti](https://stefanogatti.substack.com/) in intervista. Ci racconterà la sua lettura attuale dell'intelligenza ibrida che aveva anticipato a ottobre, e questa settimana di resa dei conti è un buon contesto per riascoltarlo.
  * Ormai sapete del nostro repository su GitHub con tool e configurazioni per fare AI coding da terminale su Linux. Ora ha un suo sito con installazione a singolo script [Lince.sh](https://lince.sh)
  * Abbiamo rilasciato AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), che è un software per tradurre messaggi vocali in testo

Da solo:
  * È stato pubblicato il video del talk che ho fatto con Alessio al [VoxxedDay Zurich](https://www.youtube.com/watch?v=DXEsG3Vo6F4)
  * Il 30 maggio avrò l'onore di essere uno dei [PyCon Italia speakers](https://2026.pycon.it/en/speakers)
  * Il 12 giugno sarò a Catania come speaker al [Coderful](https://www.coderful.io/)
  * Altri talk ad altre conferenze in arrivo...

---

## Bug, modelli e la tentazione open source

Questa settimana a farla da padrone nelle news sono state sicuramente due cose. L'arrivo di GPT-5.5 e di ChatGPT Images 2.0, che hanno segnato un grande passo avanti per OpenAI sia nel mondo dell'intelligenza artificiale agentica e del coding sia in quello della generazione delle immagini. I risultati sono davvero notevoli per OpenAI, perché hanno recuperato i gap che fino a poco fa erano abbastanza evidenti con Anthropic per quanto riguarda la parte agentica e con Google per quanto riguarda la creazione delle immagini. GPT-5.5 ottiene risultati allo stato dell'arte su Terminal-Bench 2.0 (82,7%) e SWE-Bench Pro (58,6%), e per la prima volta un modello OpenAI sembra davvero in grado di tenere testa a Claude Code nel coding agente.

Ma parallelamente è scoppiato il caso di Anthropic, che ha ammesso di aver avuto tre bachi importanti in Claude Code che hanno inficiato le performance e la qualità dei risultati del suo modello di punta Opus. Il postmortem è dettagliato: il 4 marzo lo sforzo di reasoning predefinito è passato da alto a medio senza annuncio, il 26 marzo un bug nella gestione della cache ha azzerato il contesto di pensiero a ogni turno, e il 16 aprile un prompt di sistema per ridurre la verbosità ha compromesso la qualità del codice generato. Tutti e tre i problemi sono stati corretti entro il 20 aprile, e Anthropic sta reimpostando i limiti di utilizzo per tutti gli abbonati come gesto di riparazione. Questo ha confermato una sensazione già presente nella comunità, che ha scatenato varie reazioni, anche alcune forse eccessive, definendo questa cosa come inaccettabile e gravissima. Io sinceramente penso che i bachi nel mondo del software possano succedere e non sarà né il primo né l'ultimo. D'altra parte però capisco la posizione di alcuni che si sono lamentati del fatto che invece di avere così tanti rilasci e nuove feature, forse sarebbe il caso per Anthropic di concentrarsi sulla stabilità del loro sistema, perché sta diventando sempre più centrale per una grande massa di sviluppatori.

Ma se torniamo a dare un'occhiata in casa OpenAI, mantenere una velocità esagerata di rilascio di nuove feature sembra essere una necessità, perché altrimenti è un attimo trovarsi indietro o farsi sorpassare da qualche altra azienda. La buona notizia, se vogliamo vederla così, è che alcuni sviluppatori che hanno deciso di passare ad altri strumenti, Codex in particolare, per provare GPT-5.5, hanno certificato quanto l'utilizzo degli standard, e in particolare delle skill, permetta un facile approdo a strumenti diversi.

In questo senso sono contento di aver previsto l'utilizzo di diversi coding agent in [LINCE.sh](https://lince.sh), perché come si vede anche in questo caso legarsi in maniera indissolubile a un agente di coding e a un vendor potrebbe non essere una buona idea. Ed estendendo un pochino questo concetto, credo che sia giunto il tempo anche per me di cominciare a guardare qualche agent open source. Se i modelli state of the art non sono fattibili in locale o open source, o almeno non ancora, quello che possiamo fare come ingegneri AI è utilizzare quantomeno degli strumenti che siano completamente sotto il nostro controllo, e perché no, magari contribuire al loro miglioramento. Tra l'altro, la settimana dei modelli aperti è stata ricca: DeepSeek V4 con 1,6T di parametri e contesto da 1M di token in open source, e Qwen 3.6-27B, un modello denso da 27B parametri che batte il suo predecessore MoE da 397B su tutti i principali benchmark di coding, dimostrano che la distanza tra modelli proprietari e open source si sta assottigliando almeno sulle architetture.

C'è l'imbarazzo della scelta là fuori tra gli strumenti open source, tra cui ad esempio Goose oppure OpenCode, ma io credo che questa settimana proverò a concentrarmi su PI e su Hermes Agent. Due strumenti molto diversi, uno per fare coding e l'altro per fare agente generico, ma che hanno entrambi cose molto interessanti. Il primo è veramente minimale e cresce per estensioni, ed è stato utilizzato in maniera molto efficace anche per implementare l'autoresearch di Karpathy. Il secondo è interessante perché, facendo cose molto simili o identiche a OpenClaw, ha un'attenzione alla sicurezza e all'isolamento del codice generato ed eseguito dall'agente davvero notevole.

---

## I link che mi hanno colpito questa settimana

### [Aggiornamento di Anthropic sulla qualità di Claude Code](https://www.anthropic.com/engineering/april-23-postmortem)
*Postmortem ufficiale su tre bug separati che hanno degradato la qualità di Claude Code tra marzo e aprile 2026.*

Un postmortem che va letto, sicuramente è interessante vedere come Anthropic metta in luce i tre errori, ma è molto interessante anche leggere come sia stato difficile indagare la causa di questi errori. La complessità è veramente alta in questi sistemi e non soltanto per i modelli.

### Il grande passo avanti di OpenAI
- [OpenAI presenta GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [OpenAI presenta ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)
- [Segno del futuro: GPT-5.5 (Ethan Mollick)](https://www.oneusefulthing.org/p/sign-of-the-future-gpt-55)

*GPT-5.5 porta risultati allo stato dell'arte su Terminal-Bench 2.0 e SWE-Bench Pro, ChatGPT Images 2.0 genera immagini con testo di alta qualità, e Mollick testa le nuove capacità in modo approfondito.*

Dicevo anche nel deep dive di quanto siano stati significativi i passi avanti in casa OpenAI. Trovate qui gli annunci del nuovo modello GPT-5.5 e dello strumento collegato Codex che fanno veramente cose molto importanti, sia per quello che ho letto sia per le prove che ho fatto io direttamente. E c'è anche l'annuncio relativo alle immagini generate da ChatGPT Images 2.0. Se siete curiosi, andate a vedere le thumbnail del mio podcast che sono generate o corrette da ChatGPT Images. Non perdetevi assolutamente l'analisi dettagliata del professor Ethan Mollick: assolutamente un articolo da leggere, ed è divertente anche andare a vedere le sue simulazioni per rendersi conto di quale sia l'evoluzione dei modelli negli ultimi mesi.

### I cinesi non stanno a guardare
- [DeepSeek V4 Preview Release](https://api-docs.deepseek.com/news/news260424)
- [Qwen 3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b)

*DeepSeek V4 in open source con 1,6T di parametri e contesto da 1M di token, e Qwen 3.6-27B, un modello denso da 27B che batte il predecessore da 397B su tutti i benchmark di coding.*

I cinesi di certo non stanno fermi e arriva l'annuncio di DeepSeek V4 in preview. È un annuncio importante perché DeepSeek, vi ricorderete, circa un anno fa generò un vero e proprio terremoto dimostrando che anche i modelli open weight potevano competere con i modelli americani state of the art. Succede più o meno di nuovo la stessa cosa, ma quello che rende sempre interessanti i rilasci di DeepSeek sono i paper che rilasciano a corredo, che nel caso della versione precedente ha portato a concreti avanzamenti non soltanto per DeepSeek ma anche per tutta la comunità. Il paper di questa volta sembra molto interessante anche in questo caso, anche se forse meno disruptive, ma non ho ancora avuto modo di approfondirlo abbastanza per poterne fare un commento dettagliato. Magari ci tornerò. Nel frattempo anche Alibaba rilascia Qwen 3.6-27B in modalità completamente open, ed è un rilascio importante perché i benchmark sono davvero notevoli e molto migliori anche degli stessi Gemma 4 che tanto hanno fatto parlare di sé non più tardi di qualche settimana fa.

### [Google presenta Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform/)
*Piattaforma enterprise per costruire, scalare e governare agenti aziendali, con Agent Studio low-code, Agent Development Kit e oltre 200 modelli nel Model Garden.*

Vi ricorderete che un paio di settimane fa Anthropic ha annunciato la sua versione di piattaforma agentica. Ecco, Google è già arrivata anch'essa ad annunciare la sua, e questo identifica un trend abbastanza forte delle big tech che stanno iniziando a fornire delle piattaforme vere e proprie che semplifichino di molto lo sviluppo di agenti che girino in cloud. Stiamo forse vedendo l'affermarsi di un nuovo trend che sposta gli agenti, che oggi girano in locale sulle nostre macchine, verso il cloud. Non lo so, non ne sono ancora certo, perché parte del fascino degli agenti che girano sulle nostre macchine è quello di avere a che fare con i nostri dati, i nostri sistemi. Ma di sicuro nel momento in cui si va nel mondo enterprise vedremo piattaforme agentiche come quella di Google e quella di Anthropic affermarsi. Non so se siamo ancora pronti per il mondo enterprise.
