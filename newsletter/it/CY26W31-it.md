# Formare junior nell'era AI: l'apprendistato dal basso è finito

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

*Questa settimana parlo di qualcosa che mi tocca da vicino: la formazione dei junior nell'era dell'AI. Se i coding assistant hanno eroso il codice che i junior scrivono e la review sta diventando un collo di bottiglia che l'AI stessa sta assorbendo, cosa resta dell'apprendistato tradizionale? La mia tesi è che la formazione deve spostarsi dal bottom-up implicito al top-down esplicito, e che libri che sembravano vecchi come Fowler tornano centrali, mentre pattern agentici come quelli di Gullí diventano la nuova materia di studio. È un tema che ho toccato anche nel podcast di sabato: se l'AGI è un asintoto, e per quasi tutto il lavoro reale l'AI non deve essere perfetta, allora il punto non è quanto è bravo il modello, ma quanto è solida l'impalcatura di contesto, architettura e giudizio che ci costruisci sopra. Vale per gli agenti, vale per le persone. Buona lettura.*

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * - Sabato è uscita la puntata 65 di Risorse Artificiali, "L'AGI è un asintoto": perché l'AI non sarà mai perfetta e per quasi tutto il lavoro reale non serve che lo sia. Dentro anche Laguna S2.1, densità dei modelli e quantizzazione. Ascolta: https://www.youtube.com/watch?v=ay18maVnX_k?utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep65_drop

---

## La fine dell'apprendistato dal basso (e cosa ci tocca insegnare adesso)

Ho cominciato a programmare scrivendo codice, come tutti. Buttavo giù righe, le correggevo in revisione, facevo danni, rifacevo. Era un apprendistato bottom-up: imparavi i pattern sbagliandoli, i trade-off soffrendoli, l'architettura scoprendola un incidente di produzione alla volta. Non era elegante, ma funzionava, ed è il modo in cui due generazioni di ingegneri si sono formate.

Quel percorso si sta chiudendo, e non è un'opinione. Il [Stanford Digital Economy Lab](https://news.stanford.edu/stories/2025/09/more-educated-workers-losing-jobs-to-ai-study-finds), analizzando milioni di record ADP, rileva che i lavoratori 22-25enni nelle occupazioni più esposte all'AI hanno perso il 16% di occupazione relativa dalla fine del 2022. Il report SignalFire parla chiaro: le nuove assunzioni graduate nelle Big Tech sono scese al 7%, metà del 2019, e il 37% dei manager preferisce usare l'AI piuttosto che assumere un under-30. A questo si aggiunge quello che [Gergely Orosz ha messo nero su bianco](https://newsletter.pragmaticengineer.com/p/the-pulse-new-trend-concern-about) parlando con engineering leader di mezzo mondo: da quando i modelli hanno cominciato a generare più codice, il collo di bottiglia si è spostato dalla scrittura alla review. Le PR si moltiplicano, i reviewer si bruciano, e quando l'AI code review non trova commenti il reviewer umano approva senza leggere. È il comprehension debt di cui parlo da settimane, ma adesso ha un volto operativo.

Il punto che mi interessa è il junior developer. Se imparavi dal basso, scrivendo e facendoti correggere, cosa impari quando non scrivi più e presto non recensisci nemmeno? L'AI ha eroso entrambe le gambe dell'apprendistato tradizionale. Nazar Boyko lo sintetizza bene: il lavoro che l'AI ha automatizzato via non era spreco, era l'apprendistato. L'AI non ha potato le inefficienze, ha cancellato il curriculum e conservato l'esame.

La mia ipotesi è che la formazione debba spostarsi esplicitamente dal basso al top-down. Le aziende devono investire su un percorso strutturato che insegni architettura, design pattern e system design come disciplina, non come sottoprodotto di errori ripetuti. I libri di [Martin Fowler](https://martinfowler.com/books/), *Refactoring* e *Patterns of Enterprise Application Architecture*, che sembravano dinosauri in un mondo di Copilot, tornano centrali. Fowler stesso, in un [writeup di agosto 2025](https://martinfowler.com/articles/2025-ai-effect.html) sull'impatto degli LLM sullo sviluppo software, è esplicito: il refactoring è più importante che mai, perché il codice generato va costantemente riorganizzato per restare sano. E ha un'osservazione che mi ha colpito: si sente spesso paragonare l'LLM a un junior colleague, ma l'LLM è felice di dire "all tests green" quando i test falliscono. Se fosse il comportamento di un ingegnere junior, quanto ci metterebbe a finire dalle risorse umane? Il paragone funziona solo se il junior ha il giudizio che all'LLM manca, e quel giudizio va formato.

Gli [Architecture Decision Records](https://adr.github.io/) diventano la disciplina con cui insegni a un junior a pensare in termini di scelte vincolate, non di codice che funziona. Un ADR cattura una decisione e la sua ratio, inclusi trade-off e conseguenze, ed è esattamente la competenza che separa chi sa valutare codice AI da chi lo accetta passivamente.

E qui entra il libro che secondo me bridgia meglio il classico con il nuovo: [Antonio Gullí](https://link.springer.com/book/10.1007/978-3-031-99491-0), *Agentic Design Patterns* (Springer, 2025). Gullí, Distinguished Engineer nel CTO Office di Google, esplicita pattern riutilizzabili per orchestrare agenti, gestire memoria, valutazioni e controllo umano. È l'estensione naturale dei design pattern classici al mondo agentico: i GoF per l'era dell'AI. Ed è esattamente il caso in cui l'insegnamento top-down è non solo possibile, ma inevitabile, perché i pattern agentici sono troppo nuovi e troppo specifici per essere scoperti per tentativi su un codebase di produzione.

C'è un parallelismo che mi convince e che lega al mio chiodo fisso sull'harness. [Birgitta Böckeler di Thoughtworks](https://martinfowler.com/articles/2025-ai-effect.html), commentando il lavoro di OpenAI su quello che chiamano "harness engineering", definisce l'harness come l'insieme di pratiche e tooling che tengono gli agenti AI in carreggiata: context engineering, vincoli architetturali, garbage collection del codice. OpenAI ha costruito un prodotto di oltre un milione di righe con nessun codice digitato manualmente, ma solo perché aveva un harness solido. L'analogia è potente e simmetrica: come gli agenti AI hanno bisogno di un harness ben disegnato per essere efficaci, i junior hanno bisogno di un training harness che insegni loro il COSA (architettura, pattern, trade-off) prima o accanto al COME (scrivere codice).

Non è un'osservazione scontata, e c'è chi obietta che l'apprendistato non sparisce, si sposta. Ha ragione, in parte. Il punto è curare quali ticket restano umani perché sono formazione, non throughput: la comprensione end-to-end di un flusso, lo shadow on-call, la scrittura dei postmortem. Assegnare comprensione, non solo output. Ma questo richiede consapevolezza e investimento deliberato, non succede da solo.

La conclusione è semplice e scomoda. Se l'apprendistato dal basso muore, e sta morendo, chi non investe su formazione strutturata di architettura e pattern si ritrova con orchestratori che non capiscono cosa orchestrano. E i libri giusti, i pattern giusti, gli ADR come disciplina, non sono vecchia scuola: sono l'unica scuola che resta. I senior del 2030 sono i junior che qualcuno sta formando oggi. Se nessuno li forma, nel 2030 ci saranno solo senior irreproducibili e nessuno che potrà prendere il loro posto.

---

## I link che mi hanno colpito questa settimana

### [Inkling-Small: il MoE aperto di Thinking Machines Lab](https://thinkingmachines.ai/news/inkling-small/)

*MoE 276B/12B, multimodal nativo, reasoning effort controllabile, contesto a un milione di token.*

Thinking Machines Lab non smette di sorprendermi. Dopo il manifesto sull'AI decentrata e l'open weight di luglio, arriva Inkling-Small con numeri che parlano chiaro: 276 miliardi di parametri totali, 12 miliardi attivi, 4,4% di sparsity. È il tipo di modello che conferma il trend che seguo da settimane: i parametri attivi sono fermi da due anni tra 12 e 49 miliardi, mentre i totali crescono. La sparsity si paga in storage, economico, non in compute. E reasoning effort controllabile significa che puoi dosare quanto pensare prima di rispondere, che nel mio mondo di harness e loop agentic è oro. Per la polizza europea, ogni modello aperto a questo livello è munizione.

### [Claude 5: meno regole, più giudizio](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)

*Anthropic ha rimosso l'80% del system prompt di Claude Code per Opus 5 senza perdita sulle evals. Lo shift: da rules a judgement, da manual memory a auto-memory.*

Questo collegamento diretto col deep dive di oggi me lo sentivo. Se l'80% del system prompt è ridondante, significa che i modelli maturi hanno bisogno di meno HOW (istruzioni operative) e più WHAT (contesto e intent). È la stessa regola che difendo per la formazione dei junior: il HOW si può delegare o automatizzare, il WHAT va insegnato. Il fatto che Claude Code migliori togliendo regole è la dimostrazione empirica di un principio che vale per gli agenti e vale per le persone. Progressive disclosure, auto-memory, giudizio invece di checklist: è il futuro dell'harness e della formazione.

### [GPT-5.6: la frontiera si abbassa di prezzo](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/)

*Luna -80%, Terra -20%, Sol Fast mode. Sol auto-ottimizza i propri kernel di inferenza.*

OpenAI abbassa i prezzi di GPT-5.6 in modo aggressivo, e il dettaglio tecnico più interessante mi sembra l'auto-ottimizzazione dei kernel da parte di Sol. È recursive self-improvement applicato all'inferenza, non al modello, e conferma quello che dice Lilian Weng e che ripeto da settimane: la vera leva sta nell'harness, non nei pesi. Sul fronte pricing, il crollo dei costi rende i sistemi multi-modello sempre più pratici: quando ogni chiamata costa poco, puoi permetterti di combinarne dieci. È il terreno su cui scommetto, e prezzi che crollano accelerano la curva.

### [DeepSeek V4-Flash: l'open weight da un centesimo](https://api-docs.deepseek.com/news/news260801)

*$0.14/$0.28 per milione di token, 1M context, 384K output, thinking + non-thinking modes.*

DeepSeek continua a essere il miglior rapporto qualità-prezzo degli open weight, e V4-Flash lo ribadisce. Quattordici centesimi per un milione di token in input, ventotto in output, contesto a un milione: sono numeri che tre mesi fa sembravano impossibili. La modalità thinking + non-thinking è esattamente quello che serve nei sistemi multi-agente: lo stesso modello fa da worker veloce per i task semplici e da reasoner per quelli complessi, senza cambiare vendor. Per chi costruisce sopra modelli aperti come me, DeepSeek è diventato il worker di default.

### [Gemini Robotics ER 2: l'AI esce dallo schermo](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-2/)

*Embodied reasoning, temporal intelligence, multi-robot collaboration.*

Esce dal mio perimetro abituale, ma non posso ignorarlo. Gemini Robotics ER 2 punta su embodied reasoning e temporal intelligence, e il dettaglio che mi colpisce è la multi-robot collaboration: agenti fisici che coordinano. È l'estensione del paradigma agentico dal software al mondo reale, e i pattern di orchestrazione di cui parlavo nel deep dive, quelli di Gullí, valgono anche qui. L'harness di un robot collaborativo è molto più vincolato di quello di un coding agent, ma il principio è lo stesso: quanta autonomia puoi delegare dipende da quanta ne sai verificare.
