# CLI, AI e un rover che non andava dritto: la robotica vista da un Software Engineer

Questa settimana nel deep dive vi racconto della mia esperienza con l'hackathon di Cyberwave che ho fatto insieme a Paolo, l'altro co-host di Risorse Artificiali. È stato molto interessante giocare con un robot e con la piattaforma di Cyberwave per fare la nostra prima vera esperienza di Physical AI, ed è stata un'esperienza molto formativa anche se non così straightforward come ci saremmo aspettati, ma di tutto questo trovate il dettaglio nel deep dive. Nella sezione dei link, invece, vi segnalo un po' di cose interessanti successe questa settimana, da DeepSeek V4 fino a GLM-5V-Turbo, passando per altre notizie e punti di vista inaspettati. Ma lascio a voi la lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com) con Alessio e Paolo:
  * Sabato è uscita la puntata 50 di Risorse Artificiali. Tre modelli cinesi open weight, DeepSeek V4 che taglia il 78% di compute sulla KV cache, e il mio deep-dive su Hermes Agent (gira da solo con GLM-5.1 e mi gestisce mail e calendario, di cui racconterò in dettaglio settimana prossima qui in newsletter). [Ascolta](https://www.youtube.com/watch?v=qKl4Vkb6BMw&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep50_drop)
  * Mercoledì è uscita la nuova intervista a [Stefano Gatti](https://stefanogatti.substack.com/), seconda volta da noi dopo essere stato il primo ospite della serie. Tesi forte del finale: l'AI oggi non è un equalizzatore, amplifica chi è nel top 10%. [Ascoltatelo qui](https://www.youtube.com/watch?v=c2Xpixk2LXw&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=gatti_drop)
  * Ormai sapete del nostro repository su GitHub con tool e configurazioni per fare AI coding da terminale su Linux. Ora ha un suo sito con installazione a singolo script [Lince.sh](https://lince.sh)
  * Abbiamo rilasciato AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), che è un software per tradurre messaggi vocali in testo

Da solo:
  * È stato pubblicato il video del talk che ho fatto con Alessio al [VoxxedDay Zurich](https://www.youtube.com/watch?v=DXEsG3Vo6F4)
  * Il 30 maggio avrò l'onore di essere uno dei [PyCon Italia speakers](https://2026.pycon.it/en/speakers)
  * Il 12 giugno sarò a Catania come speaker al [Coderful](https://www.coderful.io/)
  * Il 24 giugno sarò a Milano come speaker di [AIConf](https://www.aiconf.it/)

---

## Hackathon Cyberwave: la robotica vista da due ingegneri del software

Nelle ultime settimane io e Paolo, uno dei due co-host con me del podcast Risorse Artificiali, abbiamo avuto l'opportunità di partecipare al cohort di [Cyberwave](https://cyberwave.com/) dedicato a esperimenti sulla robotica. Cyberwave è un'interessante startup italiana che si occupa di robotica, ha appena chiuso un round seed ed è in cerca di feedback dagli sviluppatori: per questo ha creato un hackathon di quattro settimane aperto a un gruppo di sperimentatori. Potevamo farcelo mancare? Certo che no, soprattutto perché uno dei founder, Simone di Somma, lo avevamo già intervistato a Risorse Artificiali e la cosa ci aveva incuriositi parecchio.

La [piattaforma di Cyberwave](https://docs.cyberwave.com/get-started) è cloud e permette di lavorare con i robot fisici creando un gemello virtuale all'interno del loro ambiente di simulazione 3D, con l'obiettivo di semplificare l'esperienza di sviluppo nel mondo della robotica. Data la nostra esperienza nell'ingegneria del software siamo partiti abbastanza tranquilli, oserei dire anche un po' presuntuosi, convinti di riuscire a coprire un caso d'uso piuttosto evoluto. Ma la robotica, abbiamo scoperto, è qualcosa di completamente diverso dall'ingegneria del software, e molto più di quanto ce l'aspettassimo. Tanto per cominciare i robot vanno calibrati appena arrivano: quando aprite la scatola e iniziate a programmarli, vi stupirete di scoprire che non è detto che vadano dritti, e quindi serve un lavoro di calibrazione e di studio dei dettagli hardware del sistema che avete in mano. Il debug, poi, è fisico, complicato e talvolta rischioso per l'incolumità del rover stesso.

Detto questo, da smanettoni quali siamo non ci siamo demoralizzati. Abbiamo cominciato a esplorare sia il robot, un [UGV Beast](https://www.waveshare.com/wiki/UGV_Beast) di Waveshare, sia la piattaforma, scoprendo le cose innovative che ci offriva e gli inevitabili bug di un prodotto così giovane. Due geek del software che devono andare a caccia di bachi, discuterli su Discord con i founder e contribuire alla loro soluzione con delle PR: due bambini in un negozio di caramelle. Alla fine, invece di un caso d'uso complicato, abbiamo messo insieme una sorta di quickstart per lavorare con Cyberwave e con il rover UGV: una serie di [Jupyter Notebook](https://github.com/RisorseArtificiali/jupyter-rover) che permettono anche ai neofiti come noi di capire tutte le possibilità che un robot e la piattaforma offrono per sviluppare.

Lavorandoci ci siamo accorti che alcune considerazioni assomigliavano molto a quelle di un'architettura software tradizionale: cosa mettere nel cloud e cosa sull'edge ricorda da vicino la separazione backend/frontend, e i fallback per gli errori di comunicazione devono essere progettati in modo che il robot continui a funzionare anche se la rete cade. Altre cose invece sono nuove. L'AI di base (riconoscimento immagini, persone, ostacoli) ormai è una commodity, ma per rendere un robot davvero autonomo c'è ancora tanto da fare: un conto è riconoscere un ostacolo, un altro è riconoscere spigoli e ombre, come ha fatto un altro concorrente dell'hackathon. E ogni robot è diverso: il form factor condiziona la progettazione e rende difficile costruire librerie di alto livello davvero portabili.

Abbiamo poi vinto l'hackathon, e mi fa piacere perché premia proprio lo spirito di creare qualcosa di utile ad altri sviluppatori. Ma la cosa importante è un'altra: ci siamo divertiti tantissimo e abbiamo avuto la conferma che the next big thing è la robotica. Il mio aha moment è arrivato quando ho implementato una CLI per il rover e l'ho data in pasto a Claude Code: poter conversare con il robot in linguaggio naturale, dirgli cosa fare e dove guardare e vederlo eseguire, è davvero un game changer. È una finestra sul futuro, quello in cui anche chi non è esperto potrà avere in mano strumenti ben testati e piattaforme come Cyberwave per un'esperienza più snella di quanto non sia oggi. Resta un punto critico, e non va sottovalutato: l'allineamento dei modelli AI, sia generativi che di riconoscimento, è imprescindibile quando si manda un oggetto fisico in giro a prendere iniziative. Tutto è ancora early stage, ma il senso si vede chiaramente, e se siete giovani e dovete decidere dove investire il vostro tempo, forse è lì che dovete guardare.

---

## I link che mi hanno colpito questa settimana

### [Speculative Decoding](https://aladinodigitale.it/2026/04/28/speculative-decoding.html)

Parto citando l'altro co-host di Risorse Artificiali, Alessio, che ha scritto un bellissimo articolo sullo speculative decoding, una tecnica per ottenere migliori risultati nella fase di decoding dei transformer, molto molto utile quando fate inferenza locale.

### DeepSeek V4 e l'inferenza locale
- [DeepSeek Unveils Flagship AI Model a Year After Breakthrough](https://www.bloomberg.com/news/articles/2026-04-24/deepseek-unveils-newest-flagship-a-year-after-ai-breakthrough)
- [antirez su DeepSeek v4, KV cache e SSD](https://x.com/antirez/status/2050982689696588013)

DeepSeek ha annunciato la versione 4 del suo Large Language Model in versione preview. Che cosa significa la versione preview? È che non è finito completamente il Reinforcement Learning, quindi alcuni dei benchmark non sono brillanti come forse ci si aspettava dalla nuova versione di DeepSeek, ma probabilmente miglioreranno molto per la final. Cito però anche un ottimo lavoro di Salvatore Sanfilippo (antirez), che sulla base di questo modello ha cominciato a spendere tempo nell'ottimizzare l'inferenza locale. Fa tante cose con DeepSeek versione 4, compresa una quantizzazione ibrida a 2 e 8 bit, ma la cosa che mi ha colpito di più è quest'ultima, di cui cito il link al post: la capacità di utilizzare la KV cache su un disco SSD invece che in memoria. Come ho commentato su X, questo può essere un vero e proprio game changer per l'inferenza locale e non solo. Poter utilizzare una memoria di lungo termine come un disco SSD invece che la RAM potrebbe abbassare molto i costi di inferenza o aprire un'intera nuova strada alle soluzioni locali.

### [Sunsetting Roo Code Extension, Cloud and Router](https://roocode.com/blog/sunsetting-roo-code-extension-cloud-and-router)

Roo Code, uno dei primi agenti integrati in VS Code, chiude i battenti. Ma non è tanto questa la notizia: succede, con i progetti open source, che a un certo punto si interrompano. La cosa che mi ha colpito è la dichiarazione del founder, che ha detto che non è più tempo per gli IDE. Lascio a voi la riflessione, io ho già la mia, che ai miei lettori credo sia ben nota visto che da tempo non uso più un IDE ma una CLI con agenti multipli in [LINCE](https://lince.sh).

### Karpathy e Hassabis: due interviste da non perdere
- [Andrej Karpathy: From Vibe Coding to Agentic Engineering](https://www.youtube.com/watch?v=96jN2OCOfLs)
- [Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough](https://www.youtube.com/watch?v=JNyuX1zoOgU)

I miei lettori sanno benissimo che quando Karpathy o Demis Hassabis parlano, io li ascolto. E questa settimana l'hanno fatto entrambi, in due interviste molto interessanti. Lascio a voi l'ascolto e i giudizi.

### [Google vende le sue TPU](https://finance.yahoo.com/markets/stocks/article/google-to-sell-tpu-chips-to-select-customers-in-latest-shot-at-nvidia-214900221.html)

Interessante news da un punto di vista business di Google, che inizia a vendere TPU. La compagnia di Mountain View, dopo essere diventata la principale concorrente di OpenAI per quanto riguarda le soluzioni consumer, sembra volersi mettere anche nel mercato hardware, diventando una concorrente diretta di Nvidia.

### [GLM-5V-Turbo](https://docs.z.ai/guides/vlm/glm-5v-turbo)

Chi mi legge da un po' o mi ascolta su Risorse Artificiali sa che sono un utilizzatore di GLM come alternativa a Claude, e che da tempo ho il loro abbonamento Max, anche perché è molto conveniente. Va anche detto che GLM ha fatto grandi passi in avanti, avvicinandosi moltissimo ai modelli state of the art. Con la serie 5 dei loro modelli esce questa nuova versione 5V-Turbo, che ha benchmark veramente molto interessanti. Al momento è disponibile solo come API oppure per un sottoinsieme di tester nell'abbonamento di coding. Ovviamente sono già in lista.
