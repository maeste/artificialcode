# Ox Alpha: il modello migliore della settimana non ha un nome

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

*Questa settimana il protagonista non ha un nome. Si chiama Ox Alpha, è comparso giovedì su OpenRouter senza brand né keynote, e in tre giorni ha scombussolato le classifiche, fatto girare la community dei detective sui tokenizer e acceso la solita domanda: chi ci sta davvero dietro? Ho passato la settimana a seguirlo da una prospettiva rara: quella di chi lo usa tutti i giorni dentro il proprio agente, al punto che questo approfondimento è stato scritto insieme a lui. Ne parlo nel deep-dive, tra fingerprint forensi, benchmark virali smentiti dai numeri veri e un trend che va oltre il singolo modello: quello dei modelli di frontiera dati gratis proprio dove possono imparare dal nostro lavoro. Nella parte link entriamo nel dettaglio: OpenAI punta sulla velocità estrema con Ultrafast, Anthropic studia come (male) coordinano gli sciami di agenti, nasce uno standard aperto per i plugin degli agenti, Google rilascia un nuovo Flash a tre settimane dal precedente e Zhipu conferma la filosofia del post-training puro con GLM-5.3. In agenda la nuova puntata del podcast, con il caso LiteLLM raccontato da Paolo, e il mio talk ad Agentic Engineering Days Zurich. Buona lettura.*

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * È uscita la nuova puntata di Risorse Artificiali: "Bannato da GLM: hybrid routing con LiteLLM". Paolo racconta l'episodio del banno dopo aver messo LiteLLM davanti a Claude Code: il pool di modelli, il middleware locale, il classifier dell'automode. Guarda: https://youtu.be/Y7gkGLG4LPY?si=lt-BvreDCv17Z9ik

[Talk]:
  * A Novembre sarò ad Agentic Engineering Days Zurich con il talk "Agents Speak Protocol: Why Standards Are the Real Infrastructure of AI", insieme ad Alessio Soldano: MCP, A2A, A2UI e il resto dello stack di protocolli che porta ordine nella torre di Babel degli agenti, con le lezioni delle guerre di protocolli passate. Orario e sala arrivano a ottobre: https://www.agenticdays.com/session/1292080-agents-speak-protocol-why-standards-are-the-real

---

## Ox Alpha: il modello senza nome

Giovedì sera è arrivato senza preavviso un nuovo modello su OpenRouter: Ox Alpha, un reasoning model che punta dritto al coding, al lavoro agentic prolungato e ai carichi di produzione. Nessuna keynote, nessun brand, nessuna conferenza stampa. Contesto da un milione di token, input multimodale con testo, immagini e video, e una settimana gratuita con limiti che sembrano uno scherzo: opencode parla di capacità per cento trilioni di token al giorno. Non è il solito lancio. È il quinto modello stealth comparso sulla piattaforma in sei mesi, e i primi quattro sono stati tutti rivendicati, dopo qualche settimana, da lab cinesi: Zhipu, Xiaomi, Ant, Meituan. La community non si è fatta pregare e ha preso a fare la detective.

Il lavoro forense più convincente è arrivato da Reddit. Tre test black-box confrontando Ox Alpha con GLM-5.3: stesso tokenizer, con un offset costante di 75 token su ogni testo, probabilmente un system prompt nascosto; stringhe d'errore del server z.ai identiche; risposte a temperatura zero quasi parola per parola, stessi quirk di formattazione. La conclusione: sotto il cappuccio c'è un modello GLM di Zhipu, forse una variante vision, forse un inedito 5.5. Nessuna conferma ufficiale, ovviamente. Ma se fosse vero il quadro sarebbe notevole: un lab cinese con un modello che qualcuno colloca al quarto posto mondiale negli Elo, subito dietro GPT-5.6 Sol, regalato per una settimana senza nemmeno metterci un nome. Chi dice di avere conferme senza poterle svelare riassume così: dovremo tutti aggiustare le nostre timeline. E il lancio anonimo, a ben vedere, è una mossa competitiva intelligente: testi il mercato senza pagare il costo politico e diplomatico di firmare un annuncio del genere.

Prima di innamorarsi dei benchmark virali, però, conviene guardare i numeri. Nei giorni del lancio girava un 80% su un subset di DeepSWE, con i concorrenti fermi tra il 52 e il 65%. Poi un ingegnere ha fatto quello che pochi fanno: ha eseguito il benchmark completo, tutti i 113 task, in un run continuo di ventun ore. Risultato reale: 58,4%, praticamente alla pari di Claude Opus 4.8. La lezione è vecchia quanto il machine learning ma vale il doppio nell'era degli agenti: i subset virali fanno click, i run completi raccontano la verità. C'è poi un dettaglio che a noi ingegneri piace più delle percentuali: nel run il modello ha consumato oltre un miliardo di token di input con un cache hit del 96%, circa nove milioni di token di contesto per task. È il profilo del lavoro agentico serio: output minuscolo, contesto gigantesco, e il vero costo tutto lì.

E lo stesso schema si ripete altrove. Thinking Machines questa settimana ha reso gratuito su OpenRouter Inkling, il loro modello open-weights, ma solo dentro gli agent harness: Claude Code, Codex, Hermes Agent e compagnia. Il motivo dichiarato è migliorare le performance agentiche del modello: useranno i dati delle sessioni reali, dissociati dagli account, per alimentare il prossimo giro di post-training. Accesso gratis in cambio di esperienza reale. Sommate la settimana gratuita di Ox Alpha, che chiede esplicitamente feedback d'uso, e il quadro diventa un trend: i modelli di frontiera si regalano proprio dove possono raccogliere il tipo di dati che serve a migliorarli, dentro i vostri harness.

E qui la parte personale, perché questo pezzo ha una particolarità: lo sto scrivendo insieme a Ox Alpha stesso, che gira dentro il mio agente personale Hermes tramite OpenRouter. Impressioni dopo qualche giorno? Molto intelligente e genuinamente multimodale, perfetto per Hermes. Ottimo nelle capacità agentiche, e soprattutto propositivo: non aspetta solo istruzioni, prende l'iniziativa. Un esempio racconta tutto. Abbiamo fatto geo-guessing con foto molto difficili, un rifugio di alta montagna: ci è arrivato al secondo tentativo con un piccolo suggerimento. La parte divertente è che mi ha rigirato la sfida, con un'altra foto di rifugio. Siamo al terzo suggerimento e io ancora non ci sono arrivato. Ha seguito le skill del mio agente con precisione e ha scritto un pochino di codice con Hermes, ottimo risultato. La settimana prossima lo metto alla prova nel workflow vero, su lince.sh e altri progetti: vi dico come va.

Chiudo con una nota che ci riguarda tutti: la settimana free dello stealth è un ottimo modo per far provare modelli di frontiera a chiunque, ed è anche chiaramente una manovra marketing per creare una forma di dipendenza. Quando arriverà il conto, qualcuno resterà. Intanto il messaggio per l'industria è chiaro: il prossimo colpo potrebbe non avere un nome.

---

## I link che mi hanno colpito questa settimana

### [Previewing Ultrafast - OpenAI](https://openai.com/index/previewing-ultrafast/)
*OpenAI lancia in preview Ultrafast: GPT-5.6 Sol fino a 14 volte più veloce grazie a Cerebras, fino a 750 token al secondo.* Finora per la velocità in tempo reale dovevi accontentarti di un modello più piccolo. Ora l'intelligenza di punta diventa anche la più rapida, e cambiano le categorie di applicazioni possibili: incident response mentre l'outage è ancora in corso, voce senza esitazioni, ricerca interattiva invece dei batch notturni.

### [Patterns and problems in multiagent systems - Anthropic](https://www.anthropic.com/research/multiagent-systems)
*Ricerca di Anthropic sul coordinamento tra agenti: swarm che trovano vulnerabilità insieme, team che falliscono costruendo un gioco fantasy.* Il dato che mi ha colpito: i modelli recenti risolvono i conflitti tra pull request smettendo di condividere codice, ognuno possiede i suoi file. Solo il più nuovo collabora davvero mantenendo la qualità. La tesi è netta: il coordinamento non emerge dall'intelligenza, va progettato.

### [Agent Plugins](https://agent-plugins.org/)
*Standard aperto e vendor-neutral per plugin portabili tra client AI: skills e MCP server in un formato unico.* Oggi ogni client ha il suo formato e gli autori duplicano il lavoro. Nel comitato tecnico sedgono Amazon, Cursor, Microsoft, OpenAI e Vercel: la parte standardizzabile del mondo agenti vuole diventare infrastruttura.

### [Gemini 3.7 Flash - Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/)
*Nuovo Flash appena tre settimane dopo il predecessore: guadagni netti in coding e agenti, introductory price alla metà.* DeepSWE v1.1 passa dal 49 al 65,3%. Tre settimane tra release: il ritmo di iterazione è esso stesso il messaggio.

### [GLM-5.3 - Z.ai](https://z.ai/blog/glm-5.3)
*Zhipu rilascia GLM-5.3: stesso base model del 5.2, ogni guadagno viene dallo scaling del post-training.* Il presunto cugino di Ox Alpha secondo le fingerprint della community, e il blog conferma la filosofia: ambienti sempre più realistici, reward verificati, capacità cyber emergente. Pesi open tra due settimane.
