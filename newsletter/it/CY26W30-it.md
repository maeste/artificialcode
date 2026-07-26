# Harness, intelligenza e compositional generalization

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana in cui proseguo il filo dell'harness da dove l'avevo lasciato, ma scendo di un livello. La settimana scorsa avevo mostrato i numeri che dimostrano che l'harness conta più del modello. Questa volta vado a vedere cosa c'è dentro e perché funziona, incrociando due punti di vista che si completano. Addy Osmani mi dà il vocabolario: loop, harness, factory, e il comprehension debt come rischio quando perdi il controllo dell'outer loop. Alex Zhang mi dà la dimostrazione formale: la compositional generalization vive nell'harness, non nei pesi, e un RLM addestrato su task corti generalizza su task da 8 a 32 volte più lunghi. L'uno dice dove si rompe il sistema se automatizzi senza verificare, l'altro cosa guadagni quando l'harness è disegnato bene. Nei link trovi il routing multi-modello, i MoE aperti di Kimi K3, Gemini 3.6 Flash, Claude Opus 5 e Qwen-Image-3. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * Sabato è uscito "Quali skills usiamo davvero per i nostri agenti" (#64 Risorse Artificiali): le skill che usiamo con Claude Code, come le scegliamo e perché non si scrivono a mano ma si distillano da sessioni di lavoro. [Ascolta](https://www.youtube.com/watch?v=YW4gIaVKIxM&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep64_drop)

---

## L'intelligenza non sta solo nei pesi: Osmani e Zhang sull'harness

Due voci, questa settimana, che dicono la stessa cosa che ripeto da un po', e la dicono meglio di come la dicevo io. [Addy Osmani](https://addyo.substack.com/p/software-factories-light-and-dark) la dice col vocabolario di chi costruisce, [Alex Zhang](https://alexzhang13.github.io/blog/2026/harness/) la dimostra con gli esperimenti. Il punto in comune è il mio chiodo fisso: l'intelligenza non sta solo nei pesi del modello, sta sempre di più nell'harness, il software di contorno che lo governa.

Osmani parte da tre strati che vale la pena tenere a mente. Il **loop** è un singolo agente che fa una cosa e la ripete. L'**harness** sono le pareti attorno al loop: la sandbox, i tool, la memoria, i gate di verifica. La **factory** è molti loop nutriti da una coda e scaricati in produzione attraverso un gate di review. È una gerarchia pulita, e mi piace perché dà un nome a quello che facciamo tutti i giorni senza chiamarlo così.

Da qui Osmani ricava la regola che secondo me è la più importante di tutte, la **back pressure**: puoi delegare a un loop solo tanta autonomia quanta ne puoi verificare in modo economico e affidabile. La generazione è illimitata, la verifica è il collo di bottiglia. Non è un problema di volume, è un problema di surplus di PR cattive. È lo stesso punto che facevo la settimana scorsa con i numeri di Lilian Weng, e prima ancora citando Simone Basso: il modello è commodity, l'harness è l'asset.

Qui entra Zhang, e cambia piano. Osmani parla da ingegnere che ha visto le fabbriche; Zhang parla da ricercatore che vuole spiegare perché l'harness funziona. La sua tesi è forte: la compositional generalization, la capacità di risolvere problemi nuovi componendone di familiari, dovrebbe stare nell'harness, non nella rete neurale. Un buon harness prende uno stato complesso e lo riduce a osservazioni piccole, ognuna delle quali il modello gestisce localmente in-distribution, cioè dentro il suo territorio di competenza. Un problema sconosciuto diventa un problema già visto.

Il meccanismo concreto Zhang lo chiama Recursive Language Model, RLM, e si regge su due gambe. Il context offloading: il contesto specifico passa come variabile simbolica e il modello di root non lo vede direttamente. E le sub-agent call programmatiche: i sotto-agenti sono trattati come funzioni REPL, il cui output finisce in variabili che la root non deve leggere. Risultato, ogni singola chiamata al modello resta pulita, senza quel context rot che ammazza gli harness attuali tipo Claude Code o Codex.

I numeri di Zhang sono quelli che mi hanno convinto del tutto. Allena un RLM su task corti e lo valuta su task da 8 a 32 volte più lunghi, e generalizza. Lo allena su un dominio e lo prova su un dominio completamente diverso che condivide solo la struttura latente, e generalizza. Il Transformer base, sugli stessi task, resta piatto nonostante il reward di training cresca. Con Qwen3-30B-A3B e l'harness RLM arriva a sfiorare o battere GPT-5.5. È la dimostrazione formale di quello che Osmani intuisce dalla pratica: il design dell'harness sposta le prestazioni più di quanto dovremmo aspettarci.

Adesso metto le due voci una accanto all'altra e ci vedo la stessa leva da due lati. Osmani mi dice dove si rompe il sistema quando automatizzi senza verificare; Zhang mi dice cosa guadagni quando l'harness è disegnato bene, e mi dà la prova che la generalizzazione si compra lì, non nei pesi. Sono il rovescio e il diritto della stessa medaglia.

E il punto in cui si toccano è proprio l'outer loop. Osmani insiste: l'ingegnere deve tenersi l'outer loop, decidere se l'approccio è giusto, verificare la solidità, approvare i cambiamenti, portarsene le conseguenze. L'inner loop, investigare, fixare, testare, lo deleghi. È qui che si gioca il **comprehension debt**, il debito di comprensione, e lo voglio leggere nel modo che mi convince di più. Non è, o non solo, codice che nessuno legge. È la perdita di controllo sulla comprensione del sistema, e soprattutto su come è costruito l'outer loop, fatto di trigger, verifier e guardrail. Quando smetti di capire perché l'agente parte, cosa lo ferma, quali confini lo governano, il debito si accumula anche se i test restano verdi. Ed è esattamente la regola di governance che difendo: l'evaluator e il controllo dei permessi devono stare fuori dal loop che evolve l'harness, altrimenti rompi i confini di astrazione e apri la porta al reward hacking. Loop corti, 3-10 step, si verificano bene; oltre i 20 l'agente perde il filo. L'autonomia la guadagni col giudizio umano a monte, su design e architettura, non la deleghi e basta.

---

## I link che mi hanno colpito questa settimana

### [Quando il routing multi-modello è davvero utile](https://arxiv.org/abs/2607.09197)

Questo paper parla la mia lingua: quando ha senso fare routing tra più modelli invece di chiamare il più grosso? Serve diversità comportamentale reale e una policy stabile, e ne bastano pochi: meno di 10 agenti catturano quasi tutta la diversità disponibile, 4 in un benchmark. Non serve uno zoo, basta un gruppo curato e differenziato. Comporre sì, ma i router più accurati sono anche i più fragili.

### [Sparse by design: Kimi K3 e i MoE aperti](https://www.akashbajwa.co/p/sparse-by-design)

Torno su Kimi K3 per il trend dei MoE aperti. I parametri totali sono cresciuti venti volte da Mixtral, gli attivi sono quasi fermi, tra 17 e 49 miliardi da oltre due anni. La sparsity si paga in storage, economico, non in compute e banda. E c'è una mezza ammissione politica: quando i FLOP sono razionati dai controlli all'esportazione, si scala sull'asse che non toccano. Altra munizione per la polizza aperta.

### [Gemini 3.6 Flash e la famiglia Flash di Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)

Google spinge sui Flash e per me il tema è l'efficienza. Gemini 3.6 Flash butta il 17% di token in meno, il 65% in meno sul DeepSWE, e la Flash-Lite costa pochissimo. Nei sistemi multi-agente latenza e costo si sommano a ogni chiamata: ogni token risparmiato è una composizione in più che mi posso permettere. Non basta avere modelli diversi, devono essere economici abbastanza da combinarli.

### [Claude Opus 5: più capace, più comprehension debt](https://www.anthropic.com/news/claude-opus-5)

Opus 5 chiude il gap con Fable 5 a metà costo, con self-verification, minore varianza e due feature che parlano all'harness: cambio di tool a metà conversazione e fallback tra modelli. Resta la scatola nera di sempre, che limita quanto posso costruirci sopra. Collegamento diretto col deep dive: un modello che genera più codice sposta pressione sulla verifica. Più è capace, più comprehension debt rischio se non tengo l'outer loop.

### [Qwen-Image-3: la generazione immagini diventa pipeline](https://qwen.ai/blog?id=qwen-image-3.0)

Esco dal coding per un attimo. Qwen-Image-3 mi colpisce per il bersaglio, non per la qualità: layout complessi, testo a 10 pixel leggibile, formule LaTeX, griglie di infografiche in un passaggio, UI. Quando un componente diventa così componibile, smette di essere un giocattolo e diventa un pezzo di pipeline. È nei componenti componibili che il multi-modello trova senso: i pezzi si specializzano, chi sa montarli vince.
