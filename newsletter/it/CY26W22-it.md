# Il README è morto, viva l'onboarding: documentare nell'era degli agenti

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana di ritorno dalla PyCon Italia, e con il deep dive di questo numero parto da una provocazione che mi porto dietro da quei giorni: nessuno legge più la documentazione, né gli sviluppatori né gli utenti finali. Vi racconto perché succede e quali strade sto esplorando per rimediare, tra README come punto di ingresso, wizard nel terminale, help gerarchici e skill di onboarding per gli agenti, con esempi concreti presi da LINCE e dal DS4 di antirez. Nella sezione link trovate i temi della settimana: l'enciclica di Papa Leone XIV sull'AI, il nuovo benchmark DeepSWE che incorona Codex sul coding, i Memory Files di Anthropic e Claude Opus 4.8 con i Dynamic Workflows, la guerra dei prezzi riaccesa da DeepSeek, e Reasonix, un coding agent pensato per i modelli open weight. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * Mercoledì è uscita la conversazione con Andrea Saltarello (Improove, AIConf, Politecnico di Milano): perché l'AI adoption in azienda è un problema culturale prima che tecnologico, e come formare i junior nell'era degli agenti. [Ascolta](https://www.youtube.com/watch?v=2GQGi8R4j_0&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=saltarello_drop)
  * Sabato è uscito "Il Papa ha capito gli LLM meglio di noi": l'enciclica di Leone XIV apre, poi benchmark saturi, DeepSeek V4 e contesto append-only, harness a microkernel e Claude vs Codex. [Episodio](https://www.youtube.com/watch?v=4EdfeDpMk-Q&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep54_drop)
  * Ormai sapete del nostro repository su GitHub con tool e configurazioni per fare AI coding da terminale su Linux. Ora ha un suo sito con installazione a singolo script [Lince.sh](https://lince.sh)
  * Abbiamo rilasciato AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), che è un software per tradurre messaggi vocali in testo

Da solo:
  * Sono stato a [PyCon Italia come speaker](https://2026.pycon.it/en/speakers): trovate tutti i contenuti dei miei due interventi, come sempre, su [maeste.it](https://maeste.it) nella sezione dedicata ai talk. Metterò lì anche i video non appena disponibili
  * Il 12 giugno sarò a Catania come speaker al [Coderful](https://www.coderful.io/)
  * Il 24 giugno sarò a Milano come speaker di [AIConf](https://www.aiconf.it/)

---

## Chi legge davvero la documentazione? Dal README alle skill di onboarding

Nessuno legge più la documentazione. Lo dico soprattutto degli sviluppatori, ma forse vale un po' per tutti, utenti finali compresi. È una cosa che mi è apparsa evidente parlando con tante persone alla PyCon Italia, da cui sono appena tornato e dove ho avuto due talk. Uno in particolare era un [workshop](https://maeste.it/pycon2026-workshop/) che si occupava esattamente di questo: come fornire il giusto setup a un progetto, open source o no, perché gli agenti possano codificare bene, cioè avere tutte le informazioni di cui hanno bisogno. La mia provocazione durante il workshop è stata proprio quella: spesso gli agenti sbagliano, ma non perché sono stupidi, bensì perché ignorano le basi del progetto.

La stessa cosa succede con gli utenti finali, siano essi sviluppatori o utenti del progetto che stiamo rilasciando, perché davvero nessuno legge più la documentazione. In questo periodo di overload informativo, dovuto anche all'AI, nessuno si prende più la briga di farlo: i progetti sono talmente tanti, e le cose che si vogliono provare così tante, che la documentazione resta lì, non letta. Ci aggiungo un'altra cosa: il fatto di essere tornati al terminale, di cui parlo spesso, da un lato è bellissimo per molti motivi, ma dall'altro rende l'interfaccia un po' meno intuitiva, almeno per una certa fetta di utenti.

È un po' che mi riscervello sulla soluzione, perché un utente che non legge la documentazione probabilmente non userà al meglio il nostro progetto, e rischia di stufarsi presto: non perché il progetto non funzioni, ma perché non è riuscito a farlo funzionare per quello che gli serviva. Ed è un peccato, perché è del tutto evitabile.

Le soluzioni che ho esplorato, in [LINCE](https://lince.sh) e di recente con una [pull request per il DS4 di antirez](https://github.com/antirez/ds4/pull/310), spaziano su più fronti. Il primo è rendere l'interfaccia del terminale un po' più a finestre, o guidata da wizard, come fa Lince con il [wizard di creazione degli agenti](https://lince.sh/documentation/#/dashboard/usage-guide?id=agent-creation-wizard) (la "N" maiuscola), o come la dashboard stessa di LINCE, che riporta icone e finestre dentro il terminale. Il secondo è ripensare il README: il README come documento unico ed esaustivo è morto, e deve diventare invece un punto di ingresso iniziale, una sorta di TLDR. La documentazione di dettaglio può stare altrove, ma facendo lo scraping del solo README l'utente capisce subito a cosa serve il progetto e cosa può farci. Ovviamente deve contenere anche l'invito a leggere il resto. Sullo stesso filone, anche i file di configurazione dovrebbero essere il più possibile autodocumentati, e dovrebbe essere semplicissimo crearne versioni aderenti alle esigenze di chi li usa: è quello che proviamo a fare con il [learning mode](https://lince.sh/documentation/#/sandbox/cli-reference?id=learn) di Lince.sh.

Ma c'è un modo che in questo momento mi piace più di tutti: creare delle skill di onboarding per gli agenti stessi. L'utente, anziché leggersi la documentazione riga per riga, arriva nel progetto, lancia la skill e comincia a conversare con il proprio agente, istruito per attenersi soltanto alla documentazione e all'help dei comandi. Ottiene così tutta l'informazione di cui ha bisogno in un modo che è ormai diventato l'abitudine, la conversazione, ma resta ancorato a quello che voi avete effettivamente documentato. È esattamente lo spirito della skill che ho proposto ad antirez per DS4 e di quella che abbiamo già in Lince.sh.

Per fare questo, però, anche gli help dei comandi devono essere organizzati bene, e qui torniamo al punto di partenza: vanno resi usabili dagli agenti, anche quando non saranno gli agenti a usarli direttamente, ma li useranno solo per costruire l'onboarding. Un buon esempio sono i comandi di Lince, ma soprattutto quelli di [DS4](https://github.com/antirez/ds4), dove [antirez](https://x.com/antirez/status/2060677906032906452?s=20) ha fatto un ottimo lavoro sugli help gerarchici, a cui cercherò di ispirarmi anche per Lince.

E poi, ultimo ma non ultimo, servono sempre di più contenuti diversi e un po' più umani, per evitare l'effetto AI slop. È anche per questo che ho un podcast, e che scrivo questa newsletter: come sapete non è più AI generated, l'AI mi fa da editor ma quello che leggete lo scrivo io. Lo stesso vale per i video che spiegano certe funzionalità. Ecco, quello per Lince.sh non l'ho ancora fatto abbastanza, e mi interessa davvero sapere se è una cosa che gradireste.

---

## I link che mi hanno colpito questa settimana

### [Notes on Pope Leo XIV's encyclical on AI](https://simonwillison.net/2026/May/25/encyclical-on-ai/)

Dell'enciclica papale ho parlato a lungo nel podcast di questa settimana, e credo che si possa condensare così: il Papa ha capito i Large Language Model molto meglio di Bernie Sanders e Walter Veltroni.

### [DeepSWE: il nuovo benchmark del coding](https://venturebeat.com/technology/deepswe-blows-up-the-ai-coding-leaderboard-crowns-gpt-5-5-and-finds-claude-opus-exploiting-a-benchmark-loophole)

Un nuovo benchmark si è affacciato nel mondo dell'AI, in particolare dei coding agent, ed è significativo proprio perché è molto nuovo e molto curato, e quindi non ancora saturo. I risultati sono impressionanti e confermano l'impressione che, in questo momento, Codex sia migliore di qualunque altro agent e di qualunque altro modello nelle attività di coding.

### [Anthropic plans Claude memory update with new Memory Files](https://www.testingcatalog.com/anthropic-plans-claude-memory-update-with-new-memory-files/)

Però Anthropic non si ferma e sta lavorando molto sugli aspetti di memoria del suo harness. Un link sicuramente interessante da leggere.

### [Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)

E a conferma che di certo Anthropic non sta ferma, è uscito Claude Opus 4.8, che porta un miglioramento di tipo incrementale rispetto alla 4.7. Forse la cosa più significativa è che dalla 4.8 sono disponibili i Dynamic Workflows, che assomigliano molto agli swarm di agenti che Google ha già lanciato con Antigravity. Ed esattamente come gli swarm di Antigravity, sono estremamente dispendiosi: prima di cominciare a usarli, fate qualche test su attività piccole per capire quanto impatto possono avere sul vostro portafoglio.

### [DeepSeek made its 75% discount permanent](https://thenextweb.com/news/deepseek-v4-pro-75-percent-price-cut-permanent)

La guerra dei prezzi è ufficialmente iniziata, e DeepSeek detta il ritmo. Quella che prima era una promozione diventa il prezzo base di DeepSeek V4: ridotto a un quarto del prezzo inizialmente annunciato.

### [Reasonix](https://esengine.github.io/DeepSeek-Reasonix/)

Reasonix è un coding agent DeepSeek-native per il terminale. La cosa interessante è che è stato ottimizzato per fare leva sui meccanismi di caching di DeepSeek, andando praticamente solo in append: una cosa che ci si può permettere avendo un milione di token, e che riduce drasticamente i costi. Ma in generale è interessante che si comincino a vedere harness pensati e sviluppati per sfruttare al meglio le capacità dei modelli open weight. Una cosa che di certo Anthropic, OpenAI e Google stanno già facendo con i loro harness, ottimizzati per i loro modelli.
