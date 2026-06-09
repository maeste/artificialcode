# Hermes Agent in casa: l'assistente che decide da solo come parlarmi e farmi il sito

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana dedicata agli agenti, sotto vari aspetti. Nel deep dive vi racconto la mia esperienza con Hermes Agent, che da qualche settimana mi fa da assistente personale su una macchina dedicata in casa: come l'ho configurato, come ho lavorato sulla sicurezza, e due episodi concreti in cui ha preso iniziative che mi hanno davvero colpito e che mostrano cosa significa avere un agente con accesso reale ai propri dati. Nella sezione dei link trovate echi dello stesso tema da prospettive diverse: il repository di antirez per l'inferenza locale di DeepSeek V4, la nuova ricerca di Anthropic sull'explainability dei modelli, la modalità Dream dei Claude Managed Agents che porta una forma di self-improving in cloud, i rumor su Orbit (il futuro assistente proattivo di Anthropic), il claim di Subquadratic su una finestra da 12 milioni di token (da prendere con le pinze) e nove principi per scrivere skill davvero utili. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * È uscito l'episodio 51 di Risorse Artificiali, dentro c'è la storia di Hermes Agent in locale che decide da solo di renderizzare un HTML in foto.
  * Tesi che attraversa l'episodio: l'AGI non è più solo il modello, ma il sistema integrato (modello + inferenza ottimizzata + harness). [Episodio](https://www.youtube.com/watch?v=uqL22MeZFKI&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep51_drop)
  * Mercoledì uscirà una nuova intervista: Domenico Gagliardi (Founder e COO Kortix) spiega perché con l'AI nessun software è più difendibile, e dove resta il valore (infra + dati).
  * Ormai sapete del nostro repository su GitHub con tool e configurazioni per fare AI coding da terminale su Linux. Ora ha un suo sito con installazione a singolo script [Lince.sh](https://lince.sh)
  * Abbiamo rilasciato AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), che è un software per tradurre messaggi vocali in testo

Da solo:
  * Martedì sera sarò a Milano ad ascoltare Alessio che parla di Local AI all'[AI Meetup #14](https://www.eventbrite.it/e/biglietti-meetup-14-local-ai-1987537914405)
  * È stato pubblicato il video del talk che ho fatto con Alessio al [VoxxedDay Zurich](https://www.youtube.com/watch?v=DXEsG3Vo6F4)
  * Il 30 maggio avrò l'onore di essere uno dei [PyCon Italia speakers](https://2026.pycon.it/en/speakers)
  * Il 12 giugno sarò a Catania come speaker al [Coderful](https://www.coderful.io/)
  * Il 24 giugno sarò a Milano come speaker di [AIConf](https://www.aiconf.it/)

---

## Un mese con Hermes Agent: setup, sicurezza e iniziative autonome

Da qualche settimana ho installato [Hermes Agent](https://hermes-agent.nousresearch.com/) su una macchina dedicata in casa, e voglio raccontarvi la mia esperienza con un agente che mi fa costantemente da assistente. Chi mi legge da un po' sa che in passato avevo provato OpenClaw su una macchina virtuale, ma lo avevo lasciato perché era ancora acerbo e perché in quel momento avevo poco tempo da dedicargli per capire come sfruttarlo al meglio. Hermes Agent è sostanzialmente un'alternativa a OpenClaw: completamente open source, non legato a nessuna big tech, e con una grande attenzione alla sicurezza, dato che gli sviluppatori del sistema vengono dal mondo blockchain.

Per il setup ho preso un vecchio PC che avevo in casa e ci ho installato una versione di Ubuntu completamente nuova, dedicata solo a Hermes, in modo che non avesse contatto diretto con la mia macchina principale, anche se sta nella mia rete e ha accesso ad alcune delle mie risorse cloud. Avevo pensato di metterlo su un Raspberry, ma avendo questa macchina libera ho preferito dargli qualche risorsa in più. Come modello ho provato sia GLM-5.1 sia GLM-5-Turbo, e in questo momento sono stabile su 5-Turbo con il coding plan, mentre TTS e STT girano in locale sulla stessa macchina, in modo che la voce non lasci mai casa.

Gli ho dato accesso ai miei account privati (non quelli enterprise) sia su Google Workspace sia sui miei progetti su GitHub, ma con grande attenzione: sapete che il tema sandboxing mi sta a cuore. Token fine-grained per fargli vedere solo quello che voglio io, e soprattutto un hardening manuale delle [skill di Hermes](https://hermes-agent.nousresearch.com/docs/skills) per togliergli a livello di script tutte le operazioni che ritenevo pericolose, come cancellare o spedire email in autonomia. Non l'ho semplicemente istruito a non farle, queste cose: gliele ho proprio rimosse dagli script disponibili, perché un agente non può fare quello che non sa fare.

Detto questo, l'agente fa un sacco di cose per me: gestisce i dispositivi smart di casa, monitora l'andamento del [podcast](https://risorseartificiali.com), controlla la mail e prepara i draft di risposta (dopo l'hardening di cui sopra), tiene calendario e todo list con promemoria integrati, gestisce di notte la mia llm-wiki, fa PR review su [LINCE](https://lince.sh), riassume articoli e paper costruendo schemi e tabelle e leggendoli ad alta voce, e ha iniziato a curare i miei feed di informazioni. Mentre aspettavo mio figlio all'allenamento di basket, gli ho chiesto di rifarmi il sito personale, e il risultato è quello che trovate ora su [maeste.it](https://maeste.it).

La cosa più affascinante di questi agenti è che, quando hanno un numero discreto di informazioni sulle vostre conversazioni o sui dati a cui gli avete dato accesso, cominciano a prendere iniziative interessanti. Sul sito non solo mi ha proposto uno stile decisamente nelle mie corde, ma è andato a recuperare informazioni che io non gli avevo passato esplicitamente. Nel sito precedente, ad esempio, nell'elenco delle conferenze in cui sono stato speaker ne mancavano molte. Lui aveva accesso a questa newsletter, ha estratto le menzioni delle conferenze passate ed è andato a ricostruire l'elenco completo, mettendo tutto con tanto di citazione a slide e video collegati. Mi ha davvero colpito.

Un altro episodio. Mentre ero fuori a camminare, gli ho chiesto di approfondire un articolo per me e di farmene un riassunto. Quello che ha deciso di fare da solo è stato un riassunto in italiano (perché ha valutato che con attenzione bassa la lingua madre fosse più conveniente, anche se di solito ci parliamo in inglese), e me lo ha mandato come messaggio vocale su Telegram, generato dal TTS locale. Ma per alcuni concetti più visivi ha valutato che la sola voce non bastasse, e si è costruito un HTML al volo per rappresentarli al meglio. A quel punto si è accorto da solo che un HTML sarebbe stato scomodo da consultare dentro Telegram, soprattutto da smartphone, e quindi ha fatto degli screenshot adattati al formato dello schermo di un telefono, mandandomi quelli al posto del documento intero. Davvero impressionante.

Se siete ingegneri del software con una sensibilità per la sicurezza, è uno strumento che potete installare con un po' di attenzione e su cui c'è da divertirsi. Se invece non vi sentite forti su quel fronte, forse Hermes Agent è ancora troppo da smanettoni. Ma se uno smanettone lo siete, allora è territorio vostro.

---

## I link che mi hanno colpito questa settimana

### [ds4.c](https://github.com/antirez/ds4)

Ecco arrivato il repository di Salvatore Sanfilippo per l'inferenza di DeepSeek 4 su macchine Apple. Ne avevo già parlato nelle scorse settimane, raccontando che Salvatore stava lavorando a questa cosa, e finalmente ha iniziato a pubblicare il codice. È interessante la cosa in sé, il codice in sé, così come il trend sempre più forte dell'inferenza locale.

### [Natural Language Autoencoders](https://www.anthropic.com/research/natural-language-autoencoders)

Interessante ricerca di Anthropic, che come sempre è attenta all'explainability e in questo caso cerca di dare una spiegazione in natural language delle attivazioni interne di un modello.

### [Claude Managed Agents: Dreaming, Outcomes e Multiagent Orchestration](https://claude.com/blog/new-in-claude-managed-agents)

All'ultima conferenza di Anthropic uno degli annunci interessanti è stata la modalità Dream, che permette agli agenti in cloud di avere una sorta di self-improving riflettendo su come sono stati utilizzati e quali skill devono essere modificate o privilegiate.

### [Anthropic sta lavorando a Orbit](https://www.testingcatalog.com/anthropic-is-working-on-orbit-its-upcoming-proactive-assistant/)

Questo è poco più che un rumor, ma si dice che Anthropic stia lavorando a questo Orbit, una modalità in cloud che assomiglia agli agenti come OpenClaw ed Hermes Agent. Sopra trovate la mia esperienza concreta con un agente personale di questo tipo. Sembra che anche Anthropic sia interessata a questo mercato.

### [Subquadratic: una finestra di contesto da 12 milioni di token](https://thenewstack.io/subquadratic-12-million-context-window/)

Questo è esattamente l'articolo che mi sono fatto sintetizzare in una prima fase da Hermes Agent, che raccontavo sopra. L'articolo è in sé interessante e parla di una modalità evoluta di attention a diversi livelli che permette di far crescere la finestra di contesto fino a 12 milioni di token. L'esperienza però ci insegna che queste cose vanno prese con le pinze, perché già in passato si era parlato di ricerche che arrivavano a 100 milioni di token ma che non sono andate da nessuna parte. La cosa che più insospettisce nell'articolo e nel paper è che sono state fatte prove singole o poco più per ogni testa di inferenza: sono davvero troppo poche per urlare al miracolo.

### [9 Principles That Separate Useful Agent Skills From the Rest](https://generativeprogrammer.com/p/9-principles-that-separate-useful)

Un articolo molto interessante che sintetizza bene cosa siano veramente le skill e quando sono veramente utili e interessanti. Se state scrivendo dei sistemi che si appoggiano sulle skill come standard, agentskills.io oppure semplicemente quelle di Claude che sono la stessa cosa, è un articolo assolutamente da leggere.
