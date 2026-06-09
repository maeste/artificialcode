# Internet degli agenti: i big posano le rotaie, OpenClaw e Hermes ci corrono già sopra

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana di pezzi grossi sul fronte degli agenti, con annunci paralleli da Google, OpenAI e Anthropic che, messi insieme, raccontano qualcosa di più grande dei singoli prodotti. Nel deep dive provo a metterli in fila e a leggerli come parti di un'unica infrastruttura, quella che la community ha cominciato a chiamare l'internet degli agenti: Spark e UCP da Google, Codex per quasi tutto e OpenClaw da OpenAI, Managed Agents 24 ore in cloud da Anthropic. E, sul versante open source, il dato che a me ha colpito di più: Hermes Agent diventato l'arnese che ha consumato più token su OpenRouter nell'ultima settimana, davanti a tutti. Nella sezione link trovate temi che fanno da contorno e completano il quadro: il maxi deal Anthropic-SpaceX da quasi $45 miliardi sul compute, che si lega ai numeri impressionanti di crescita dei ricavi di Anthropic, la marcia di OpenAI verso l'IPO di settembre dopo la fine della causa con Musk, qualche nota in più su Gemini 3.5 Flash, l'arrivo di Andrej Karpathy in Anthropic e la riflessione di Anthropic stessa su perché HTML batte Markdown come formato di ingestion per gli agenti di coding. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * Sabato nuova puntata di Risorse Artificiali sul Google I/O 2026: Gemini 3.5 Flash omnimodale a 1500 token/sec, Antigravity che inghiotte Gemini CLI, e una lunga storia su Demis Hassabis (mossa 37, AlphaFold, cellula virtuale). [Episodio](https://www.youtube.com/watch?v=OQ3y4FUZGwQ&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep53_drop)
  * Ormai sapete del nostro repository su GitHub con tool e configurazioni per fare AI coding da terminale su Linux. Ora ha un suo sito con installazione a singolo script [Lince.sh](https://lince.sh)
  * Abbiamo rilasciato AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), che è un software per tradurre messaggi vocali in testo

Da solo:
  * Martedì sera sarò a Milano per partecipare [all'evento di AI Socratic Milano](https://luma.com/4vviqrs5). Se ci sarà modo presenterò anche lo stato attuale di [Lince](https://lince.sh)
  * È stato pubblicato il video del talk che ho fatto con Alessio al [VoxxedDay Zurich](https://www.youtube.com/watch?v=DXEsG3Vo6F4)
  * Il 30 maggio avrò l'onore di essere uno dei [PyCon Italia speakers](https://2026.pycon.it/en/speakers)
  * Il 12 giugno sarò a Catania come speaker al [Coderful](https://www.coderful.io/)
  * Il 24 giugno sarò a Milano come speaker di [AIConf](https://www.aiconf.it/)

---

## Spark, Codex, Managed Agents (e Hermes #1): la settimana che ha posato le rotaie dell'internet degli agenti

Lo dico da settimane, e settimana dopo settimana mi sembra di vedere un puzzle che si compone: l'era degli agenti è arrivata, e non è più una questione di un singolo prodotto annunciato qua o là, ma di un'infrastruttura che i big stanno costruendo in parallelo. Sempre di più si intravede quella che vari osservatori cominciano a chiamare l'internet degli agenti. Questa settimana è stata particolarmente densa, perché Google, OpenAI e Anthropic hanno mosso pezzi importanti contemporaneamente, e a fianco la community open source ha piazzato un colpo che a me ha fatto particolarmente impressione.

Partiamo da Google, che ha annunciato [Spark](https://gemini.google/overview/agent/spark/), un agente personale 24/7 costruito su Gemini 3.5 Flash e Antigravity, pensato per girare in background sul vostro workspace e prendere iniziative su email, calendario, organizzazione. Non più una chat che apri quando vi serve qualcosa, ma un assistente che vive con voi. Ma il pezzo che mi ha incuriosito ancora di più è l'aggiornamento dello [Universal Commerce Protocol](https://blog.google/products-and-platforms/products/shopping/ucp-updates/), UCP, lo standard aperto su cui Google sta lavorando con il resto dell'industria per permettere agli agenti di parlare direttamente con i merchant. Carrelli multi-item, accesso real time al catalogo, identity linking per mantenere i benefici fedeltà. Se Spark è il commensale, UCP è la rotaia su cui lo si fa viaggiare.

OpenAI risponde su due fronti. Il primo è [Codex per quasi tutto](https://openai.com/index/codex-for-almost-everything/), che porta Codex molto al di là del coding e lo trasforma in un agente generalista capace di intervenire su compiti eterogenei. Il secondo è il continuo investimento su OpenClaw, che resta il loro tassello open source di riferimento e mantiene un ritmo di rilascio forsennato. Nella community si discute però sempre di più della governance del progetto, ed è una discussione legittima: basterebbe il numero di star fatte su GitHub per definirlo come fenomeno, non come un esperimento di nicchia. Quando un progetto open source diventa così centrale, la domanda su chi decide la roadmap pesa, e pesa parecchio.

Anthropic, dal canto suo, ha doppiato il proprio bet sull'enterprise con i [Managed Agents](https://platform.claude.com/docs/it/managed-agents/overview): agenti gestiti, in cloud, attivi 24 ore. È la versione hosted del concept che molti di noi stiamo testando in locale (io con Hermes Agent in casa, di cui ho parlato qualche settimana fa), pensata per aziende che vogliono una flotta di agenti in background senza occuparsi dell'infrastruttura. La modalità Dream qui trova il suo ambiente naturale.

E poi c'è il dato che mi ha colpito di più: [Hermes Agent è diventato l'arnese che ha consumato più token in assoluto su OpenRouter](https://www.reddit.com/r/singularity/comments/1t9hh33/hermes_agent_is_now_1_most_used_globally_in_past/) nell'ultima settimana. Numero uno, davanti a tutto. È un segnale potente: gli sviluppatori non stanno solo guardando agli agenti, li stanno mettendo in produzione, e quando hanno scelta non gravitano automaticamente verso il marchio più grande.

Mettendo insieme i pezzi, lo schema diventa chiaro: gli agenti escono dalla chat e si installano nei sistemi operativi (Android la settimana scorsa, i workspace desktop adesso con Spark), parlano con i merchant (UCP), girano 24 ore in cloud (Managed Agents, Spark) e arrivano fino al terminale dello sviluppatore (Codex, OpenClaw, Hermes). L'internet degli agenti non è più una metafora di marketing: è un'infrastruttura che si sta posando sotto i nostri occhi, mattone dopo mattone. E come per ogni infrastruttura, conta dove vi posizionate mentre la si costruisce.

---

## I link che mi hanno colpito questa settimana

### [Anthropic to Pay SpaceX Nearly $45 Billion for Computing Deal](https://www.bloomberg.com/news/articles/2026-05-20/anthropic-to-pay-spacex-nearly-45-billion-for-computing-deal?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc3OTM0MDE0MywiZXhwIjoxNzc5OTQ0OTQzLCJhcnRpY2xlSWQiOiJURkNUNldLSUpISUkwMCIsImJjb25uZWN0SWQiOiJBOEExRDhFQTI5OTc0OTRGQTQ1QUE2REJBMjAwNTM3MSJ9.7GmTLgNTHuRQhQxgg38WqTvHCpZXe6DAGkd4qH3ckIA)
*Anthropic firma un accordo da quasi $45 miliardi con SpaceX per ottenere 300+ megawatt di compute dal datacenter Colossus 1 di Memphis su tre anni.*

Anthropic continua a stupire, e questa è la conferma che il compute è la materia prima della partita. $1.25 miliardi al mese, con uscita a 90 giorni, raccontano due cose insieme: il livello di domanda che Anthropic prevede di dover servire, e la volontà di non dipendere da un singolo fornitore. Diversificare oltre AWS parla anche al mercato: oggi il vincolo è la capacità, non i contratti.

### [OpenAI Reportedly Moves Toward IPO](https://techcrunch.com/2026/05/20/openai-barrels-toward-ipo-that-may-happen-in-september/)
*OpenAI prepara la sua IPO per settembre 2026, con Goldman Sachs e Morgan Stanley come underwriter principali dopo la chiusura della causa di Musk.*

L'ostacolo legale è stato rimosso e OpenAI può finalmente puntare al mercato pubblico. È un passaggio enorme, perché chiude il capitolo aperto dalla controversa ristrutturazione del 2025 e segna l'addio definitivo al mito della non-profit. Da qui in poi le decisioni di prodotto e di modello si misureranno anche contro un mercato finanziario poco paziente, e cambieranno più cose di quanto sembri.

### [Mind-Blowing Growth Is About to Propel Anthropic Into Its First Profitable Quarter](https://www.wsj.com/tech/ai/mind-blowing-growth-is-about-to-propel-anthropic-into-its-first-profitable-quarter-7edbf2f4?st=rMpJ6a&reflink=desktopwebshare_permalink)
*Anthropic verso $10.9 miliardi di ricavi nel Q2, raddoppiati rispetto al trimestre precedente; crescita più veloce di Google e Facebook prima delle rispettive IPO.*

Mettete insieme questo numero con il deal SpaceX qui sopra e vedete il quadro: ricavi che esplodono e una macchina di spesa che si gonfia in proporzione. La crescita più veloce di Google e Facebook pre-IPO è una statistica notevole, ma la profittabilità sull'anno completo è tutt'altro che scontata, proprio per la fame di compute. Bet rischioso, ma se la traiettoria tiene, il payoff è di un ordine diverso.

### [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)
*Google lancia Gemini 3.5 Flash con 76.2% su Terminal-Bench 2.1, output 4x più veloce dei competitor e nuove capacità multimodali e agentiche.*

Ne ho già parlato nel deep dive come motore di Spark, ma il modello da solo merita una nota. Il 76.2% su Terminal-Bench 2.1 lo mette vicino al frontier sul coding agente, e la velocità 4x cambia l'economia dell'inferenza per workflow lunghi. Google si sta riposizionando seriamente, e questo è il pezzo che lo dimostra.

### [Karpathy Joins Anthropic](https://x.com/karpathy/status/2056753169888334312)
*Andrej Karpathy annuncia il passaggio ad Anthropic per dedicarsi alla R&D sulla frontiera LLM, lasciando in pausa l'attività didattica.*

Sapete che quando Karpathy parla, io ascolto. Questa volta non parla, agisce. Il rientro full-time in un grande laboratorio dopo anni da indipendente è un segnale forte sui prossimi due-tre anni: i grandi salti, dice in pratica, succederanno qui dentro. La scelta di Anthropic, e non di OpenAI o Google da cui era passato, dice altrettanto.

### [Using Claude Code: The Unreasonable Effectiveness of HTML](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html)
*Anthropic spiega perché HTML, non Markdown, è il formato di ingestion del contesto più efficace per Claude Code in specs, prototipi e interfacce custom.*

Discussione che ha attraversato il podcast e la community nelle ultime settimane, e che mi sembra cruciale per chi costruisce workflow agentici reali. La ricchezza strutturale di HTML, con layout, tabelle, elementi interattivi, dà al modello una densità informativa che il Markdown non riesce a esprimere. Lo capite davvero quando provate a far ingerire una spec lunga a un agente.
