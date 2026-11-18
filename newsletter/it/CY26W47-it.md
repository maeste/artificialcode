# L'RSI esce dai laboratori: l'AI che accelera l'AI arriva nell'industria

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

*Questa settimana tutti quanti hanno parlato di Jensen Huang, del suo caso tra spie, tradimenti e dimissioni forzate da CEO di NVIDIA. Sono stato tentato di fare il deep dive su quello, perché piaccia o non piaccia ha impatti significativi sul mondo dell'AI, dato che NVIDIA è comunque l'azienda più capitalizzata del mondo, e che decisamente sta trainando non soltanto il mondo dei chip ma anche molte altre cose legate alle AI e all'AI open source, compresa la recente acquisizione di Hugging Face. Ma questa è una newsletter che si è sempre concentrata soprattutto, nell'ultimo periodo, sulle tecnologie e sui trend tecnologici all'interno del mondo dell'AI, e ho deciso di continuare. Quindi vi lascio alla lettura del deep dive, che oggi è sul recursive self-improvement. Buona lettura.*

### La mia agenda

### [Podcast](https://risorseartificiali.com):
  * Sabato è uscita la puntata 80, "Jensen è caduto in fallo, ma l'AI non si ferma": MiniMax H3 diventa image generator (16 megapixel in locale in 6 step), Thoughtworks Radar 40 e lo standard A2UI. Ascolta: https://www.youtube.com/watch?v=tVpIC_ABvHY&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep80_drop

### Personale
  * Settimana prossima sarò ad Agentic Engineering Days Zurich con il talk "Agents Speak Protocol: Why Standards Are the Real Infrastructure of AI", insieme ad Alessio Soldano: MCP, A2A, A2UI e il resto dello stack di protocolli che porta ordine nella torre di Babel degli agenti, con le lezioni delle guerre di protocolli passate. Info: https://www.agenticdays.com/session/1292080-agents-speak-protocol-why-standards-are-the-real
  * Sempre settimana prossima sarò ospite di [Festival AI](https://festival-ai.com/) a Lugano, e il mio intervento sarà tutto centrato sui temi che avete visto tante volte passare su questa newsletter, e che hanno fatto parte del deep dive della scorsa settimana: gli harness e il loro impatto sugli agenti AI di varia natura.

---

## L'RSI esce dai laboratori: l'AI che accelera l'AI arriva nell'industria

Ultimamente si continua a sentire parlare di recursive self-improvement (RSI), ovvero la capacità dei modelli, e più in generale, di migliorare se stessi durante il loro ciclo di vita. Ve ne ho parlato parecchie volte anch'io, con diverse definizioni o sfumature, menzionando ad esempio gli harness self-evolving, che abbiamo incontrato di nuovo proprio nello scorso numero tra i temi del Technology Radar. Questa settimana ci faccio il deep dive, perché è importante osservare che questa tecnica sta uscendo dai laboratori di ricerca puri: negli scorsi mesi abbiamo avuto tanti paper di ricerca sul recursive self-improvement e sui self-evolving harness, ma appunto, dicevo, sta uscendo dai laboratori di ricerca per andare a finire nell'industria.

E gli effetti sono già molto concreti, e dimostrano un'accelerazione impressionante nei tempi di consolidamento di nuove scoperte. Il documento che dà i numeri a questa sensazione è la [valutazione indipendente che METR ha condotto ad alto accesso dentro Anthropic](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/) tra agosto e ottobre: le capability sui task ben specificati progrediscono circa al doppio della velocità dell'anno precedente, 1,9x sull'indice AECI con intervallo 1,5-2,8, e gran parte dell'accelerazione, forse l'80%, è attribuibile all'IA che fa R&D. METR precisa anche che il salto non è spiegabile con la sola scala di compute di training. Parliamo di due anni di progressi in uno, con il personale che dichiara fino a 12x di uplift nel proprio lavoro quotidiano.

Questa cosa si vede molto bene sulla ricerca pura, vera e propria, quindi su materie di ricerca verificabili, come la matematica, altre scienze o la programmazione stessa. Ma la parte più interessante è un'altra: questa tecnica viene applicata sempre più alla ricerca specifica dell'intelligenza artificiale, andando a fare recursive self-improvement sia sui modelli, e qui intendo sull'architettura dei modelli oltre che sulle tecniche di training, sia sulle self-evolving AI. Le due vie sono esattamente quelle che racconta [Tom Mann](https://x.com/TomasMann1878/status/2119346730458038678) nel bilancio del suo primo anno come research engineer sul team RSI di Meta: aggiornare il modello fondazione, oppure migliorare l'impalcatura attorno a esso, fatta di prompt, tool e memoria. Insegnare agli agenti di ricerca, come scrive lui, a risolvere i problemi più difficili del mondo con token e compute. E il suo primo paper, Research Preference Models, serve proprio a questo: selezionare a basso costo gli esperimenti promettenti da provare.

È un trend molto importante, che spostandosi nell'industria e, piano piano ma sempre più concretamente, anche nel mondo enterprise rischia di cambiare ulteriormente le regole del gioco. E qui le letture si fanno serie. [Ajeya Cotra](https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai) stima che raddoppiare i progressi richieda un'accelerazione del lavoro di 4-9x, plausibile intorno a 10x oggi, e osserva che la soglia di accelerazione drammatica prevista dall'RSP di Anthropic è ormai alle spalle: senza colli di bottiglia, l'estrapolazione ingenua porta molto lontano in pochissimo tempo. La definisce la cosa più importante successa nell'AI risk negli ultimi anni. [Zvi Mowshowitz](https://thezvi.substack.com/p/ai-r-and-d-is-accelerating-towards) nota che il ritmo è già in anticipo di mesi sulla timeline dello scenario AI 2027, e che la situazione è grave, ma non è una sorpresa. Con le dovute cautele: METR stessa segnala incertezze ampie in entrambe le direzioni, Toby Ord nel pretrain Mythos vede un salto una tantum più che un cambio di pendenza, e Anthropic ha censurato gran parte delle evidenze più informative, chiedendoci in pratica un atto di fiducia.

Invito voi lettori affezionati di questa newsletter a non sottovalutarlo, e a prendervi il tempo di leggere gli articoli che propongo e di approfondire il tema.

---

## I link che mi hanno colpito questa settimana

### 🌍 Industria e geopolitica dell'IA

È impossibile ignorare la notizia di Jensen Huang di questa settimana. Ne abbiamo parlato in modo molto leggero durante il podcast, e qui vi riporto due link significativi che toccano NVIDIA da prospettive molto diverse.

#### [NVIDIA Announces CEO Transition](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition)
*Jensen Huang si dimette con effetto immediato, senza motivazione dichiarata. Colette Kress, CFO dal 2013, CEO ad interim; Harvey C. Jones primo chair del board. Risultati Q3 fissati per il 17 novembre.*

#### [Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs](https://unemploymentlabs.com/checkpoint-forensics)
*Forensics sui pesi pubblicati: DeepSeek, Moonshot, MiniMax e Ant avrebbero inizializzato sei modelli su GPU Blackwell soggette a export control. L'impronta prova l'inizializzazione, non il training.*

### 🚀 Nuovi modelli

Solo qualche settimana fa Amodei invocava un rallentamento nel rilascio dei modelli, e tutti gli altri importanti esponenti del mondo dell'AI gli davano ragione. A giudicare dalle notizie di queste settimane, non sembra che abbiano applicato quel metodo.

#### [Introducing Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)
*Il daily driver di Google per coding e workflow agentici: supera Argon sull'Artificial Analysis Index in modalità high, 2,5x più veloce di Gemini 3.8 Flash, $1,50/$7,50 per milione di token.*

#### [Introducing Claude Fable 5.2 and Claude Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2)
*Lo stesso modello in due versioni: Fable con salvaguardie cyber e bio per tutti, Mythos senza per organizzazioni verificate. 49,1% su FrontierCode 2.0, e oltre il 90% delle modifiche mergeate in Anthropic scritte da Claude.*

#### [Introducing Our Smallest, Most Efficient Model: Muse Ember](https://research.meta.ai/blog/muse-ember)
*Il modello più piccolo ed efficiente di Meta per il lavoro agente ad alto volume: tool call, routing, estrazione. Eguaglia i migliori punteggi di Haiku a un terzo del costo, $0,10/$0,50 per milione.*

### 🤖 Agentic AI

Tre notizie importanti nel mondo degli agenti, perché toccano tre aspetti diversi che li rendono più vicini al mondo enterprise. Da un lato si vede l'esigenza sempre più forte di avere agenti self-hosted, per un discorso di sicurezza e di pratica. Dall'altro l'importanza della memoria, e infine si cominciano a vedere nuove modalità di interagire con questi agenti, che non siano soltanto la conversazione e il linguaggio naturale.

#### [Operate Claude Managed Agents inside your security perimeter](https://claude.com/resources/articles/self-hosted-claude-managed-agents)
*Beta privata: l'intero servizio per agenti autonomi gira nel cloud del cliente, sessioni nel suo database, modelli via Anthropic, Bedrock o gateway interni. Credenziali fuori dalla sandbox, sessioni esportabili.*

#### [A2UI 1.0: Build delightful, fast, reliable, agentic experiences](https://developers.googleblog.com/a2ui-10-build-delightful-fast-reliable-agentic-experiences/)
*Versione stabile del protocollo open per la UI generativa: gli agenti rispondono con schermate interattive renderizzate dai componenti nativi di ogni app; i valori sensibili non raggiungono il modello.*

#### [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory)
*La gerarchia di memoria di Claude (transcript, note, wiki, contesto) con il dreaming, la riflessione offline che corregge e consolida. Le wiki alzano l'accuratezza dal 53% al 61% su un corpus di 420M di token.*

### 🔬 AI e scienza

Anche questo è un trend: l'AI che accelera la scienza, soprattutto nel mondo biologico. Da sempre DeepMind fa da traino su queste cose, e lo conferma con AlphaGenome.

#### [AlphaGenome 2: Deciphering how cells read DNA to better understand disease](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)
*Modello condizionale per predire gli effetti delle varianti genetiche per tipo e stato cellulare, condizionabile sui propri dati single-cell. Quasi il doppio del richiamo di varianti causali rispetto alla versione precedente.*
