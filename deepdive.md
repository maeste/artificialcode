# Deep-Dive: Ox Alpha, il modello senza nome

## Link principali
- [OpenRouter - Ox Alpha](https://openrouter.ai/stealth/ox-alpha) - pagina ufficiale: reasoning model per coding, agentic work, produzione. 1M context, 131k output, multimodale (testo+immagine+video), free durante la preview, rilasciato 20 ago 2026. Provider terzo anonimo, OpenRouter solo routing. Prompts/completions retained dal provider ma non usati per training (Stealth Model Terms).
- [opencode su X](https://x.com/i/status/2090544355824038300) - annuncio free week: 1M context, multimodal, Zero Data Retention, "capacity for 100T tokens per day". 13.8k like, 6.7M views.
- [OpenRouter su X](https://x.com/i/status/2090544970923184269) - "New stealth model": frontier model per efficient coding, sustained agentic work, real-world production.
- [NousResearch su X](https://x.com/i/status/2090899914700054780) - Ox Alpha gratis via Nous Portal, "capacity for 1 quadrillion tokens per day".
- [Fingerprint post r/singularity](https://www.reddit.com/r/singularity/comments/1vufbx1/) - 3 test black-box: (1) tokenizer identico a GLM-5.3 con offset costante +75 token (system prompt nascosto); Kimi/Qwen/MiMo/MiniMax divergono; (2) stringhe d'errore z.ai identiche ("[1210] This model always engages in thinking..."); (3) output temp-0 quasi word-for-word, stessi quirk markdown e LaTeX tedesco. Conclusione autore: è un modello GLM, variante vision di 5.3 o nuovo 5.5.
- [MTSlive thread](https://x.com/i/status/2090872472174522701) - 5° drop anonimo in 6 mesi; i precedenti 4 tutti rivendicati da lab cinesi: Zhipu, Xiaomi, Ant, Meituan. Su subset DeepSWE: Ox 80%, Fable 65%, GLM-5.3 62%, Sol 52%. Tokenizer identico a GLM. Citazione @theojaffee sul panico se fosse un "Flash model".
- [henryzhangumich reality check](https://x.com/i/status/2091066210721141009) - run completo del DeepSWE benchmark (113 task): NON 80% ma 58.4%, quasi identico a Claude Opus 4.8 (59%). Dettagli: ~21 ore a 4x concurrency con max reasoning, 66 task completati, 1.09B token input (96.1% cache hit), 6.98M output, ~9M in/62k out per task. Repo: github.com/MatchaOnMuffins/oxalpha
- [olam_labs Elo rating](https://x.com/i/status/2090930116138582224) - Ox Alpha #4 nel loro Elo, subito dietro GPT-5.6 Sol. "Primo modello genuinamente al frontier presumibilmente non di OpenAI o Anthropic". Domina nei social strategy games contro agenti e umani.
- [omarsar0 (Elvis Saravia)](https://x.com/i/status/2090820040073322733) - "Got confirmation on what the Ox Alpha model is. Can't disclose anything yet, but I can confirm it's a spectacular model. All I can say is that we all need to adjust our timelines."
- [TimJayas contro-test](https://x.com/i/status/2090872361096753524) - Ox Alpha vs Opus 5 one-shot su raptor engine three.js: Opus 5 nettamente meglio, tempi simili. Lato frontend/game dev dibattuto.
- [bridgemindai](https://x.com/i/status/2091129412926206032) - Ox Alpha batte GPT 5.6 Sol in un car game one-shot (physics, controls, UI). Guess dell'autore: Zhipu con GLM inedito o ByteDance, "capacità di serving troppo massiva per un lab piccolo".
- [Rumor Gemini](https://x.com/i/status/2091131444940742922) - voce non verificata che Ox Alpha sia Gemini 3.5 Pro in anteprima. Da menzionare solo come esempio del rumor mill.
- Hugging Face: nessun peso ufficiale. Solo placeholder (0xKitkat/Ox-Alpha-GGUF) che avvertono dai fake GGUF. Un hosted API model non può essere legittimamente quantizzato senza checkpoint autorizzato.

## Punti chiave
- Quinto modello stealth su OpenRouter in sei mesi; i primi quattro furono tutti rivendicati da lab cinesi (Zhipu, Xiaomi, Ant, Meituan)
- Lancio via harness (opencode, Cline, Codex picker, Pi harness), zero keynote, zero brand, free week come campagna di adozione
- Fingerprinting della community indica base GLM (Zhipu); nessuna conferma ufficiale
- Benchmark virali (80% subset) smentiti da run indipendente completo (58.4% = pari a Opus 4.8): lezione di benchmark hygiene
- Token economics da ingegnere: 96% cache hit, ~9M token input per task, il costo vero è nel contesto non nell'output
- Capacità di serving dichiarata (100T-1P token/giorno) implica infrastruttura da ipergiant: esclude i piccoli lab

## Note sparse
- Meta-narrazione: questa newsletter è co-scritta proprio con Ox Alpha dentro Hermes/OpenRouter. Trasparenza col lettore: il protagonista del pezzo è anche il co-autore.
- Collegamento con tesi W31: l'impalcatura conta più del modello. Qui il modello non ha nemmeno un nome, e funziona lo stesso.
- Angolo geopolitico: se le fingerprint sono giuste, la Cina ha un modello top-4 globale che regala token a manetta senza firmarlo. Il lancio anonimo come strategia competitiva: testi il mercato senza pagare il costo diplomatico/politico dell'annuncio.
- Contrasto con settimana stessa: OpenAI si ferma per misalignment, Anthropic va verso IPO da $2T+; intanto un fantasma entra nel top 4. Il mercato premia chi muove.
