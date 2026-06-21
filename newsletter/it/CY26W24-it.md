# L'agente è un processo, e gira nel sistema operativo di secondo livello

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana in cui torno su un tema che mi accompagna da mesi e che con LINCE mi sono trovato a maneggiare da vicino: cosa è davvero un agente, dove iniziano e finiscono i suoi confini. Nel deep dive provo a mettere in fila come il concetto si è evoluto, dall'harness engineering al loop engineering, fino a una tesi che mi sta a cuore: harness e loop stanno diventando l'unità minima con cui accediamo agli agenti, più un processo che gira in un sistema operativo di secondo livello che un'app con un LLM infilato dentro. Lo leggo attraverso gli investimenti delle ultime settimane, da OpenAI che acquisisce Ona a Xiaomi con MiMo Code, fino alle sandbox di NVIDIA e LangChain. Nella sezione link trovate i temi che fanno da contorno: Google che spinge sul locale con DiffusionGemma e Gemma 4 QAT, la saga di Claude Fable 5 (lanciato, leakkato da Pliny e poi sospeso da una direttiva USA), e due applicazioni dell'AI alla ricerca scientifica, Claude chimico e Codex che simula i buchi neri. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * Nuova intervista: Roberto Stagi (Ratel AI) spiega perché il contesto degli agenti non si satura per colpa degli MCP server, ma perché l'indice dei tool resta nel modello. Open source, benchmark aperti. [Ascolta](https://youtu.be/DGWXwzw2ZoY?utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=stagi_drop). Dentro c'è anche la "agent anxiety": l'ansia di non avere un agente al lavoro mentre sei a pranzo al mare, più comune di quanto ammettiamo.
  * Sabato è uscito "Scrivere codice è una commodity: Fable e i workflow", dove do a Fable un task multilinguaggio e lo porto a casa in una notte con 40 agenti in parallelo, zero-shot. Da qui: loop engineering e l'articolo di Anthropic "When AI builds itself". [Episodio](https://youtu.be/YdSKoTPpuvk?utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep56_drop)
  * I nostri progetti [Lince.sh](https://lince.sh) e AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), ormai li conoscete bene.

Da solo:
  * Sono stato a Catania come speaker al [Coderful](https://www.coderful.io/), una delle conferenze meglio organizzate e con i migliori contenuti che mi sia capitato di vedere di recente. Le mie slide le trovate [qui](https://maeste.it/coderful2026); appena disponibile, lì troverete anche il video.
  * Il 24 giugno sarò a Milano come speaker di [AIConf](https://www.aiconf.it/).

---

## Harness e loop: la nuova unità minima dell'AI agentica

Parte del mio lavoro di questi mesi, soprattutto su [LINCE](https://lince.sh), è stato provare a dare una definizione di agente: dove inizia, dove finisce, dove passano i suoi confini. Non sono qui per raccontarvi il dettaglio di quel progetto, ma una cosa che quel lavoro mi ha costretto a fare è guardare da vicino come il concetto stesso di agente, e dei suoi confini, si sia evoluto negli ultimi mesi. È una storia che vale la pena raccontare, perché credo stia cambiando l'unità di base con cui ragioniamo quando parliamo di AI agentica.

Il punto di partenza è una cosa che dico da settimane: per fare agenti non bastano ottimi modelli e qualche tool. L'harness, cioè l'impalcatura attorno al modello, sta diventando il pezzo centrale, e come accoppi il modello all'harness conta quanto il modello stesso. Le competenze di chi lavora seriamente su questi sistemi si sono spostate di conseguenza: prima si parlava di harness engineering, e di recente la community (Boris, il creatore di Claude Code, in testa) ha cominciato a chiamarlo loop engineering. Dietro a questi due termini c'è un'idea precisa: oltre al contesto che dai all'LLM, c'è molto altro da curare.

L'harness engineering aggiunge alla cura del contesto la capacità di definire i limiti entro cui vogliamo che l'agente si muova, appunto l'imbracatura. Significa dargli una sandbox, degli evals, un modo di verificare il proprio lavoro. Aggiungendo questi confini, l'agente riesce a muoversi con più autonomia e a reggere compiti più lunghi e complessi. Il loop engineering va un passo oltre: se vogliamo un'autonomia ancora maggiore, dobbiamo definire anche i limiti del loop dentro cui l'harness cicla per arrivare al risultato. Un loop è fatto di uno stato iniziale, un evento che lo fa partire, un goal da raggiungere, una serie di comportamenti consolidati (le skill), uno stato di lavoro (la memoria) che tiene traccia di cosa è stato fatto e cosa resta da verificare, e di meccanismi di decisione per capire se continuare o se il goal è raggiunto.

La distinzione, se volete una bussola, è questa: l'harness definisce lo spazio in cui l'agente può muoversi, cosa gli è lecito fare e cosa no; il loop definisce il tempo e la decisione, quante volte ripetere e quando fermarsi.

Mettendo insieme le due cose, quello che chiamiamo agente comincia ad assomigliare sempre di più a un processo che gira dentro un sistema operativo agentico, una specie di sistema operativo di secondo livello, in cui l'harness definisce i limiti e il loop gestisce i processi. E questo legame tra LLM, harness e loop sta definendo una nuova entità minima: un'unità di lavoro che possiamo spostare sulla macchina, sulla rete, sul cloud. Non un microservizio come quelli web o rest a cui siamo abituati, ma qualcosa di più vicino a un pod.

Provo a spiegarmi con un'analogia che mi è cara. Quando mi interfaccio a un database con SQL, do per scontato che il logging, la scrittura su disco e la gestione delle transazioni li faccia il server, senza che io debba pluggarli ogni volta. Un database server scrive su disco e tiene le transazioni, punto. Allo stesso modo, quando mi interfaccio a un agente (cioè al suo harness e al suo loop), do per scontato che abbia delle skill, degli evals, una sandbox. Pensare a evals, sandbox o guardrail come pezzi da appiccicare sopra a del codice che parla con un LLM è una visione che regge sempre meno: quei pezzi sono parte integrante dell'unità con cui lavoriamo.

Ed è esattamente quello che raccontano gli investimenti di queste settimane. Non si costruisce più un'applicazione con l'LLM infilato dentro come un tool, che è quello che facevano LangChain, LlamaIndex e gli altri un paio di anni fa. Si costruisce sopra l'agente, inteso come LLM più harness più loop, trattandolo come il sistema in cui far vivere le proprie applicazioni AI native. OpenAI ha [acquisito Ona](https://openai.com/index/openai-to-acquire-ona/) (l'ex Gitpod) proprio per dare a Codex ambienti cloud sicuri e preconfigurati e orchestrare task persistenti a lunga durata. Xiaomi ha rilasciato [MiMo Code](https://venturebeat.com/technology/xiaomis-new-open-source-agentic-ai-coding-harness-mimo-code-beats-claude-code-at-ultra-long-200-step-tasks), un harness di coding open source che, a loro dire, regge sequenze oltre i 200 step con una memoria persistente affidata ai subagent (numeri autodichiarati, li prendo con le pinze, ma la direzione è quella). NVIDIA ha pubblicato [SkillSpector](https://github.com/NVIDIA/SkillSpector) per analizzare le skill degli agenti a caccia di vulnerabilità prima di installarle. E perfino [LangChain](https://www.langchain.com/blog/give-your-ai-agent-its-own-computer) oggi offre microVM isolate a livello hardware per dare a ogni agente il suo computer dedicato.

È un po' come scrivere la propria app in HTML5. Dietro ci sono livelli su livelli (il browser che fa rendering, il motore JavaScript, l'HTTP, il TCP/IP, le socket), ognuno con i suoi meccanismi di sicurezza, tracing e verifica, e ognuno lo diamo per scontato. Nessuno si plugga le socket a mano. L'harness e il loop stanno diventando quel tipo di livello: in una parola, sono la nuova entità minima con cui accediamo agli agenti.

---

## I link che mi hanno colpito questa settimana

### Il locale, anche in casa Google
- [DiffusionGemma: generazione testo 4x più veloce](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)
- [Gemma 4 QAT: compressione per mobile e laptop](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/)

*DiffusionGemma è un MoE da 26B che genera blocchi di testo in parallelo con la diffusione testuale, fino a 4x su GPU. Gemma 4 QAT porta checkpoint quantization-aware per girare su mobile e laptop senza perdere qualità.*

DiffusionGemma e Gemma 4 QAT confermano il trend del locale di cui parlavo già nelle scorse settimane: c'è sempre più attenzione ai modelli locali, anche da parte di Google. Le due notizie, tra l'altro, attaccano i due colli di bottiglia veri dell'inferenza in casa: la latenza, con la generazione di blocchi in parallelo, e la memoria, con la quantizzazione. Vanno ancora trovate le applicazioni giuste per i modelli più piccoli, ma la crescita dell'hardware porterà ad avere modelli sempre più potenti capaci di girare in locale. E visto che si cominciano a vedere governi, come quello americano, che interdicono l'uso di modelli potenti, credo che presto potremmo averne bisogno sul serio.

### La saga di Fable 5
- [Lancio di Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Accesso a Fable e Mythos sospeso](https://www.anthropic.com/news/fable-mythos-access)
- [Il leak del system prompt di Pliny](https://x.com/elder_plinius/status/2064478648057610422)
- [Anthropic fa marcia indietro sulla policy che "sabotava" i ricercatori](https://www.engadget.com/2192004/anthropic-walks-back-policy-sabotaging-research/)

*Anthropic lancia Fable 5 e Mythos 5, poi una direttiva di export control USA ne sospende l'accesso per un possibile jailbreak. Pliny ne leakka il system prompt, mentre Anthropic ritira la policy che degradava in sordina le richieste dei ricercatori.*

Fable 5 è, o meglio era, visto che il governo americano ne ha interdetto l'uso, una bomba. Ne parlo nel podcast di sabato scorso: le sue capacità di svolgere compiti molto complessi sono davvero incredibili. Avrei potuto farci il deep dive, su questo e sulle tante notizie che ha generato, dai ricercatori che si scagliano (giustamente) contro blocchi troppo stringenti per il lavoro sugli LLM, poi allentati da Anthropic che fa marcia indietro, fino al governo americano che ne interdice l'uso. Non ne ho fatto il deep dive volutamente, perché credo che vedremo ancora colpi di scena nei prossimi giorni e mi pare presto per tirare una sintesi. Intanto Pliny (nome noto nel mondo dell'hacking) ha fatto il leak del system prompt, e pare che usando quel system prompt su Opus si ottengano risultati migliori rispetto alla versione vanilla di Opus 4.8. Io non ho ancora provato, ma sembra un'ulteriore conferma di come la fase del cosiddetto in-context learning non sia più trascurabile: se un system prompt ben fatto sposta i risultati di un modello già potente come Opus 4.8, vuol dire che buona parte del valore non sta solo nei pesi, ma in come l'harness imposta il contesto. Ed è esattamente il filo del deep dive di questa settimana.

### L'AI entra nel laboratorio
- [Rendere Claude un chimico](https://www.anthropic.com/research/making-claude-a-chemist)
- [Codex per simulare i buchi neri](https://openai.com/index/using-codex-to-simulate-black-holes/)

*Claude predice gli spettri NMR eguagliando ChemDraw e MestReNova e propone strutture molecolari dai dati spettrali. L'astrofisico Chi-kwan Chan usa Codex per affinare le simulazioni di plasma e particelle attorno ai buchi neri.*

Sono entrambe applicazioni dell'AI alla ricerca scientifica computazionale, forse il prossimo fronte su cui vedremo gli agenti fare le prodezze che oggi vediamo sul codice. Non è un caso che il coding sia stato il primo dominio a esplodere: come il codice, anche la simulazione scientifica è un ambiente dove la verifica, per quanto non semplice, resta gestibile, perché un calcolo o torna con i dati o non torna. E chi mi legge da un po' avrà imparato che è proprio dove i risultati sono verificabili che gli agenti danno il meglio di sé.
