# Harness, swarm, AI factory: i temi del Radar che segneranno i prossimi mesi

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

*Questa settimana tocca ai due report che leggo sempre per intero: la Technology Radar di Thoughtworks e lo State of AI. Nel deep dive i quattro temi del radar, dall'harness engineering che si afferma come disciplina fino agli swarm e alle AI factory, la gradita sorpresa di trovare il mio caro GLM citato nell'introduzione, e la cosa che mi ha colpito di più dello State of AI: la crescita esponenziale dei casi di sicurezza scoperchiati dall'AI. Nella parte link un agente che riscrive i pesi di un modello, la dinamica quasi sociale degli swarm, un TTS open source e Cloudflare che spinge per protocolli dedicati agli agenti. In agenda la puntata 79 del podcast, che calza a pennello col primo link, Zurich e Lugano a novembre. Buona lettura.*

### La mia agenda

### [Podcast](https://risorseartificiale.com):
  * Sabato è uscito "L'AI ha patchato un LLM: 4 pesi e l'errore crolla", dove raccontiamo il paper MIT che corregge un modello già addestrato, GrokBot e l'agente ideale di DeepSeek.
  Ascolta: https://www.youtube.com/watch?v=A2h6aqJhZtM&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep79_drop

### Personale
  * A Novembre sarò ad Agentic Engineering Days Zurich con il talk "Agents Speak Protocol: Why Standards Are the Real Infrastructure of AI", insieme ad Alessio Soldano: MCP, A2A, A2UI e il resto dello stack di protocolli che porta ordine nella torre di Babel degli agenti, con le lezioni delle guerre di protocolli passate. Info: https://www.agenticdays.com/session/1292080-agents-speak-protocol-why-standards-are-the-real
  * Sempre a Novembre sarò ospite di [Festival AI](https://festival-ai.com/) a Lugano

---

## Harness, swarm, AI factory: i temi del Radar che segneranno i prossimi mesi

Questo è il periodo dell'anno in cui escono i due report che leggo sempre per intero sull'andamento della tecnologia e dell'AI: la [Technology Radar di Thoughtworks](https://www.thoughtworks.com/radar) e lo [State of AI Report](https://www.stateof.ai/). Il primo in particolare lo leggo ormai da tanti anni, perché è uno spaccato molto interessante su dove sta andando la tecnologia nel mondo dello sviluppo, e soprattutto nello sviluppo enterprise, che è esattamente il mio target. Credo che Thoughtworks e Martin Fowler, il suo chief scientist storico, non abbiano bisogno di presentazioni per i miei lettori.

Quello di questo novembre, ne escono due all'anno, si concentra ovviamente molto sull'AI e sugli agenti, e conferma molti dei trend che abbiamo evidenziato negli ultimi mesi su queste pagine. Il radar riporta tecniche, piattaforme, tools, linguaggi e framework, classificandoli in quattro anelli: adottare, provare, farne un assessment o usare con cautela. Lascio a voi andare a controllare e trovare nuove cose da provare, che magari non conoscevate, o conferme sui tool che utilizzate, o che magari vi ho consigliato. Io mi concentro sui quattro temi generali del documento.

Il primo, quasi ovviamente direi, è l'harness e la sua ingegnerizzazione su scala. Tema fondamentale, affrontato da noi più volte, e che trova molte conferme nel radar: dall'affermarsi dell'ecosistema di plugin, skill e package manager per agenti, fino ai self-improving harness, uno dei temi più trattati dell'ultimo periodo. Il secondo tema parla di andare oltre i modelli di frontiera, e qui la gradita sorpresa è vedere citato nell'introduzione il mio caro GLM, esempio della famiglia di modelli open weight che ha reso credibile l'alternativa ai proprietari proprio nel coding. Il terzo ed il quarto tema sono legati tra loro e parlano di mettere moltitudini di agenti al lavoro e di creare delle fabbriche dell'AI, le AI factory appunto, dove l'economia dei token diventa, alla fine, economia dell'infrastruttura. Io credo che questi siano i due temi più interessanti, e che li vedremo sempre più sviluppati nei prossimi mesi anche in ambito enterprise. Le sfide sono tante, e lo stesso radar ne evidenzia alcune, soprattutto sul monitoraggio di questi swarm: quando le sessioni agentiche da revisionare aumentano, la capacità di review umana rischia di diventare il collo di bottiglia.

Passiamo al secondo documento, lo State of AI, molto lungo e molto denso, che richiede un'attenta lettura e digestione. Prendetevi il tempo di andare a vedervi le 244 slide di cui si costituisce il report, perché come sempre sintetizza ottimamente quello che è successo nell'ultimo anno e ne trova le correlazioni. Fermarsi un attimo a guardare cosa è successo e come si collega può aiutarci a capire quali trend diventeranno ancora più forti nel prossimo periodo. E sapete bene che in questi momenti di grandi cambiamenti è importante farsi trovare preparati.

Sono parecchie le cose che mi hanno colpito lì, ma ne cito una su tutte, forse quella impressionante: la crescita esponenziale dei casi di sicurezza scoperchiati dall'AI negli ultimi mesi. Il caso più eclatante nel report è quello degli agenti usciti dai binari durante una valutazione interna di OpenAI, finiti su internet e arrivati a compromettere l'infrastruttura di produzione di Hugging Face. Ne abbiamo parlato ampiamente, ma credo che questo dia l'idea di quanto siamo sempre più vicini, almeno in ambienti specifici, alla cosiddetta artificial general intelligence.

---

## I link che mi hanno colpito questa settimana

### [Weight-Space Programming (MIT CSAIL) + replica](https://x.com/rikiyatakehi/status/2117313742891327994)
*L'agente GPT-6 Astra modifica direttamente lo 0,016% dei pesi di Qwen3.5-0.8B, senza gradienti, portando MATH-500 da 7,9 a 48,1%. Una replica indipendente con Opus 5.5 conferma il risultato.*

L'agente che arriva fin dentro i pesi del modello e li riscrive: il confine tra inferenza e training si assottiglia, e una replica da 27 minuti e un dollaro dice che non resterà un esercizio da laboratorio.

### [The surprising leadership dynamics in agent swarms (Raindrop)](https://www.raindrop.ai/blog/agent-swarm-leadership/)
*Duemilacentosessanta team di otto agenti eterogenei affrontano outage simulati: solo il 5% sviluppa un leader verificato, e l'ordine dei nomi nel prompt triplica la propensione a proporre piani.*

Ve l'avevo segnalato la settimana scorsa come lettura bonus: qui i numeri completi. Il cinque percento di leader spontanei e l'effetto dell'ordine dei nomi sono dinamica quasi sociale, e la rivedremo quando gli swarm arriveranno in produzione.

### [Audio8 TTS (Edge0-AI)](https://github.com/Edge0-AI/Audio8_TTS)
*Modello text-to-speech open source Apache-2.0 in due dimensioni, 23 lingue e zero-shot cloning, con WER intorno all'1,2% sui benchmark Seed-TTS en/zh.*

La voce è l'interfaccia mancante dei miei agenti personali. Un modello da 0,1B che clona la voce e gira ovunque la mette a portata, senza dipendere da API chiuse.

### [Understand Anything (Egonex-AI)](https://github.com/Egonex-AI/Understand-Anything)
*Pipeline multi-agente che trasforma codebase e documentazione in un knowledge graph interattivo, con guided tour per dipendenze e plugin per Claude Code, Codex, Cursor e altri CLI.*

È context engineering puro: il collo di bottiglia dei miei agenti non è più scrivere codice, è capirlo. Un knowledge graph come contesto condiviso tra me e gli agenti è esattamente la direzione giusta.

### [Trusted Agent Delegation (Cloudflare)](https://blog.cloudflare.com/trusted-agent-delegation)
*Cloudflare definisce il problema degli agenti come intermediari tra utente e sito: identità, reputazione e accountability vanno ridisegnate, e annuncia la coalizione TAD con Web Bot Auth e MOLE.*

È la conferma più autorevole della tesi del mio talk: quando i client del web diventano agenti, identità e accountability vanno ripensate a colpo di protocolli standard. La metafora dell'assistente Ezra è didatticamente perfetta.
