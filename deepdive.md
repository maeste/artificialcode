# Deep-Dive: Le skills che uso tutti i giorni per fare building
## Link principali
https://github.com/RisorseArtificiali/skills
https://github.com/RisorseArtificiali/skills/blob/main/WORKFLOW.md
https://github.com/RisorseArtificiali/skills/blob/main/SKILLS-CHEATSHEET.md
https://lince.sh/

---

# Deep-Dive CY26W37: Personal AGI — la guerra è per l'harness, non per il modello

## Bozza definitiva

Questa settimana tutti parlano di [GPT-6 Astra](https://openai.com/index/safety-overview-gpt-6-astra/). Ne abbiamo parlato a lungo nel podcast: 99,9% su ARC-AGI-3, l'[annuncio](https://x.com/OpenAI/status/2095595741528125780) che in tre giorni ha accumulato centinaia di migliaia di like, e [la lettura di Chollet](https://x.com/fchollet/status/2095598451115614371) che lo definisce uno step-function change, con il modello che si costruisce al volo un proprio linguaggio simbolico per ragionare sui giochi. Alle prime prove è, per certi versi, incredibile. Eppure la notizia che mi ha colpito di più è arrivata dalla stessa OpenAI ma da un'altra porta: i [North Stars](https://openai.com/index/an-alien-mind/), il piano strategico pubblico scritto dal chief scientist Jakub Pachocki. Perché dentro c'è una parola che descrive la partita vera di questo momento: personal AGI.

OpenAI è l'unico ad averla messa nera su bianco. Tre obiettivi: il [ricercatore AI automatizzato](https://www.technologyreview.com/2026/03/20/1134438/openai-is-throwing-everything-into-building-a-fully-automated-researcher/), l'accelerazione economica, e il "personal AGI per ogni persona sulla Terra". Niente definizione formale. La versione operative è nel [job posting del team Personal AGI](https://openai.com/careers/research-engineerresearch-scientist-personal-agi-north-stars-san-francisco/): "evolvere ChatGPT da chatbot a superassistente infinitamente capace e personalizzato". [Brockman](https://gln75.com/en/blog/brockman-openai-superapp-path-agi) ci mette i numeri: AGI al "70-80%", la definizione non conta più, il pavimento sale troppo in fretta. E [il retweet](https://x.com/gdb/status/2093065379145019902) che ha fatto girare mezzo internet: ChatGPT Work che prenota da solo un taglio di capelli, "chatgpt is increasingly becoming your personal AGI". Poi febbraio: [Peter Steinberger, il creatore di OpenClaw](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/), l'harness open più diffuso al mondo, entra in OpenAI per guidare i personal AI agents. Leggetelo bene: il laboratorio con i modelli più desiderati del pianeta ha comprato in casa la persona che sa costruire l'esecuzione, non i pesi.

Ma la lettura di OpenAI resta centrata sul modello: il personal AGI è ChatGPT, un modello, avvolto dal loro harness nel loro cloud. Io la vedo diversa, e non sono l'unico. Nous Research non ha mai usato quella parola per [Hermes](https://hermes-agent.nousresearch.com/docs/), e non è un caso: il loro agente è self-improving, model-agnostic su venti provider, le skill le crea l'esperienza, il modello è una variabile di configurazione. L'harness è il prodotto.

E l'harness ha ormai la sua teoria. Il paper ["Stop Comparing LLM Agents Without Disclosing the Harness"](https://arxiv.org/abs/2605.23950) formalizza la Binding Constraint Thesis: nei task long-horizon la varianza di performance indotta dall'harness supera quella del modello, nel loro esperimento di sette volte. ["The Harness Effect"](https://arxiv.org/abs/2607.06906) fa l'esperimento pulito: stessi sei modelli, stessi task, cambia solo l'orchestrazione. Costo per task meno 41%, tempo meno 44%, token meno 38%.

La mia tesi è più semplice di qualunque paper: il personal AGI sarà una soluzione ingegneristica, non di modello. Un harness che orchestra agenti multipli, ognuno col modello giusto per il compito: uno locale per la privacy, uno in cloud per la capacità, uno economico per il batch. Non un supermodello al centro, un'orchestra dirette bene. Proprio come funziona il mio setup, dove l'agente personale gira sul mio server, col modello che scelgo io, e questa settimana l'ho messo a testare il sandbox che protegge gli altri.

Personal AGI significa una cosa sola: chi possiede l'harness possiede l'agente. Il resto è marketing.

## Link di riferimento (per la parte link della newsletter)
- [OpenAI — Safety overview: GPT-6 Astra](https://openai.com/index/safety-overview-gpt-6-astra/)
- [OpenAI su X — annuncio GPT-6 Astra](https://x.com/OpenAI/status/2095595741528125780)
- [François Chollet — Astra su ARC-AGI-3](https://x.com/fchollet/status/2095598451115614371)
- [OpenAI — "An Alien Mind" (i North Stars, Pachocki)](https://openai.com/index/an-alien-mind/)
- [MIT Technology Review — automated researcher](https://www.technologyreview.com/2026/03/20/1134438/openai-is-throwing-everything-into-building-a-fully-automated-researcher/)
- [OpenAI Careers — Personal AGI / North Stars](https://openai.com/careers/research-engineerresearch-scientist-personal-agi-north-stars-san-francisco/)
- [Brockman su Big Technology Podcast (sintesi)](https://gln75.com/en/blog/brockman-openai-superapp-path-agi)
- [gdb — "chatgpt is increasingly becoming your personal AGI"](https://x.com/gdb/status/2093065379145019902)
- [TechCrunch — Steinberger (OpenClaw) joins OpenAI](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/)
- [arXiv — Stop Comparing LLM Agents Without Disclosing the Harness (2605.23950)](https://arxiv.org/abs/2605.23950)
- [arXiv — The Harness Effect (2607.06906)](https://arxiv.org/abs/2607.06906)
- [Hermes Agent docs (Nous Research)](https://hermes-agent.nousresearch.com/docs/)
