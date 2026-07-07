# Amodei contro l'open source, come Gates contro Linux. Mi sembra un errore

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana in cui parto da una frase che mi ha fatto drizzare i peli: Dario Amodei che dichiara che i modelli open source sono pericolosi e vanno limitati o bloccati. Chi mi segue da un po' sa quanto l'open source conti per me, e nel deep dive spiego perché resto basito, deluso e preoccupato: la mossa mi ricorda Bill Gates che, alla fine degli anni Novanta, diceva che Linux era un sistema pericoloso. La mia tesi, da cittadino europeo, è che non vedo alternative agli open weight, e che il nostro contributo viaggia su due strade: l'inferenza locale, come fa antirez con DS4, e l'ottimizzazione degli harness e del software di contorno, che è dove mi sto giocando tutto, con GLM, Ollama e OpenRouter, e che mi riporta al vecchio chiodo fisso dei modelli multipli. Tanto che sul podcast ho tagliato il 90% del mio abbonamento Anthropic. Nella sezione link trovate i temi di contorno: Fable 5 che torna dopo gli export control, il nuovo Sonnet 5, Nano Banana 2 Lite e gli interaction model di Thinking Machines, il drug discovery di Anthropic e DSpark di DeepSeek. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * Sabato è uscito "La politica USA su AI e open source mi fa drizzare i peli": ho tagliato il 90% del mio abbonamento Anthropic dopo la mossa su Fable e le parole di Dario Amodei. [Ascolta](https://youtu.be/iB9MxO5jn6E?utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep60_drop)
  * I nostri progetti [Lince.sh](https://lince.sh) e AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), ormai li conoscete bene. Date un'occhiata anche ad [Agent ready skills](https://github.com/RisorseArtificiali/agent-ready-skill) di cui ho parlato il 24 giugno ad AIConf.
  * Stiamo pensando di fare delle live su YouTube e X, brevi, una volta a settimana, all'ora di pranzo o lì attorno, per raccontarvi e farvi vedere cose pratiche sui nostri progetti, sugli agenti personali e su usi diversi dell'AI.

Da solo:
  * Finalmente un periodo tranquillo per le mie uscite pubbliche. In fondo è arrivata l'estate, ma stiamo già lavorando a settembre.
  * Appena escono i video delle conferenze degli scorsi mesi ve li segnalo, perché vorrei vostro feedback.

---

## Open source come pericolo? La tesi di Amodei, e perché non la condivido

Chi mi segue sul podcast sa che l'ho già affrontato anche lì, ma davvero non posso non aprire questa edizione dalle parole di Dario Amodei, che [ha dichiarato che i modelli open source sono pericolosi, non possono essere lasciati liberi e vanno limitati o bloccati](https://memeburn.com/amodei-says-open-source-ai-is-becoming-too-dangerous-to-stay-unrestricted/). Chi mi conosce, di persona o perché mi segue da un po', sa quanto l'open source sia importante per me. E benché veda i problemi e le pericolosità di dare una tecnologia così potente in mano a tutti senza regolamentazione, non posso che restare basito, deluso e preoccupato da chi vuole mettere un limite all'open source.

L'ho detto in podcast e lo ripeto qui: questa affermazione mi ricorda in modo impressionante Bill Gates che, alla fine degli anni Novanta, diceva che Linux era un sistema pericoloso per la sicurezza informatica e la sicurezza in generale.

Capisco anche quando Amodei osserva che i modelli open weight sono solo parzialmente una versione open source, perché non ci dicono tutto dei modelli. Ma è meglio sapere qualcosa e poter controllare qualcosa, piuttosto che avere a che fare con la scatola nera dei modelli completamente closed source come quelli di Anthropic.

Se a questo aggiungiamo la politica americana, sempre più invadente e predominante nella scelta di quali modelli possano essere "esportati", per usare le loro parole, quindi utilizzabili al di fuori dei cittadini statunitensi, credo sia doveroso, da cittadino europeo, cominciare a pensare a come l'Europa e il resto del mondo possano tutelarsi. Non vedo alternative, da questo punto di vista, all'uso di modelli open weight. E credo sia importante che ricercatori e sviluppatori europei si chiedano che contributo possono dare al mondo open source.

È difficile, oggi, dare un contributo nella generazione di nuovi modelli: serve capitale e una pianificazione di lungo periodo in cui l'Europa, purtroppo, è molto indietro, ad eccezione forse di Mistral, che comunque resta decisamente più indietro dei modelli cinesi.

Le strade possibili, quindi, pur usando modelli di stampo cinese, sono due. La prima è quella che sta facendo antirez, e altri con lui: ottimizzare l'inferenza locale. Il suo progetto [DS4](https://github.com/antirez/ds4) è molto promettente e sta diventando famoso nella comunità di chi vuole fare inferenza locale, ma richiede un hardware che non tutti hanno.

C'è poi un secondo contributo possibile: ottimizzare gli harness e tutto il software di contorno a questi modelli, usandoli però in inferenza remota. Oggi mi sto affidando a GLM e a [Ollama](https://ollama.com) in cloud, oltre che a [OpenRouter](https://openrouter.ai/). GLM è un modello estremamente potente, e probabilmente quello tra gli open weight che, sul coding, più si avvicina alle prestazioni dei modelli closed source come Anthropic e OpenAI; come early adopter ho un [invito con sconto](https://z.ai/subscribe?ic=DWTQHGMFKV) per provarlo. Ollama e OpenRouter, d'altro canto, ti lasciano usare e provare tanti modelli diversi.

Perché poter usare modelli diversi è importante? Chi ha letto la newsletter della settimana scorsa sa che ho parlato di usare modelli multipli per ottenere risultati simili o migliori dei monolitici più grandi. È un'idea che mi affascina dai tempi del [PoC wise-agents](https://github.com/wise-agents/wise-agents), e che oggi ritrovo in progetti come [Fugu di Sakana](https://sakana.ai/fugu/) o [Mixture of Agents (MoA) di Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/mixture-of-agents).

Nelle prossime settimane e mesi dedicherò molta della mia esperienza a capire se e quanto mischiare più modelli possa essere una strada percorribile a livello ingegneristico. Da me, come al solito, saprete tutto: ne parlerò qui e pubblicherò open source il software che produrrò.

---

## I link che mi hanno colpito questa settimana

### [Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5)

È il collegamento più diretto col deep dive di oggi. Fable era stato interdetto proprio dalla politica di export control che citavo, e ora torna, con un classificatore di sicurezza aggiornato e un framework condiviso con Amazon, Microsoft e Google per classificare la gravità dei jailbreak. Bene che l'accesso sia rientrato. La lezione, però, resta: se un modello può sparire per decisione politica, la polizza open weight non è un'opzione, è una necessità.

### [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)

Sonnet 5 chiude il gap con Opus 4.8 a prezzi molto più bassi, e si sente. La famiglia Sonnet ha aperto l'era agentica, e questa versione fa un salto netto su planning, tool use e coding. Lo uso ogni giorno, e come modello è ottimo. Mi resta il dubbio del deep dive: è una scatola nera chiusa, e questo limita quanto posso costruirci sopra in modo davvero mio.

### [Nano Banana 2 Lite](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)

Google spinge sull'acceleratore della generazione multimediale a basso costo: Nano Banana 2 Lite genera immagini in pochi secondi a pochissimi centesimi, e Omni Flash porta l'editing video conversazionale a prezzi accessibili. Il tema per me è un altro: quando i componenti diventano così economici e veloci, ha sempre più senso comporre pipeline multi modello, il filone di cui parlavo nel deep dive e a cui dedicherò le prossime settimane.

### [Inside Thinking Machines' Interaction Models](https://blog.bytebytego.com/p/inside-thinking-machines-interaction)

Questo lo trovo proprio affascinante, e attacca a due temi miei. Lo schema a due modelli, uno veloce per la conversazione e uno lento per il reasoning, è il pattern fast path e slow path di cui parlavo. E poi spostano l'interattività dentro il modello invece di appiccicarla fuori con un harness di componenti piccoli. È una direzione che si allinea a dove penso stia andando l'agentico.

### [Anthropic lancia il programma AI di drug discovery](https://www.cnbc.com/2026/06/30/anthropic-launches-ai-drug-discovery-program-claude-science.html)

Anthropic entra nella scoperta di farmaci, e lo fa concentrandosi su malattie neglette che il mercato ignora. Come storia fa simpatia. E rientra in un filone che mi convince: la ricerca scientifica è terreno fertile per gli agenti, perché una molecola o funziona o non funziona, ed è dove i risultati sono verificabili che l'AI dà il meglio. L'ironia, dopo il deep dive, è che è proprio Anthropic, la scatola nera per eccellenza.

### [DeepSeek open source DSpark](https://venturebeat.com/orchestration/deepseek-open-sources-dspark-a-new-framework-to-speed-up-llm-inference-by-up-to-85)

Chiudo con un link che parla dritto al deep dive. DSpark è speculative decoding open source di DeepSeek, e accelera l'inferenza fino all'85% senza cambiare l'output del modello. È esattamente il tipo di contributo di cui parlavo: non generare nuovi modelli, ma ottimizzare il software di contorno, gli harness, l'inferenza. Che venga da DeepSeek, e in open source, rafforza il punto: l'ecosistema aperto sta lavorando proprio sui pezzi che contano.
