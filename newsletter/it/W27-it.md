# **Weekly AI Trends: Impact Analysis for Engineers**

Questa settimana mi allontano leggermente da due dei miei argomenti preferiti, vibe coding e robotica. Non perché questi trend abbiano perso slancio, ma perché sto concentrandomi di più sui sistemi multi-agent e sulle tecniche emergenti per la loro gestione che hanno dovuto cedere spazio alle notizie delle settimane precedenti, ma meritano abbondante spazio in questa newsletter. Ispirato dal lavoro che sto facendo con il mio team e Google per dare alla community un [Java SDK per il protocollo Agent2Agent](https://github.com/a2aproject/a2a-java), mi sono immerso questa settimana in alcuni dei concetti fondamentali dei sistemi agent.

Se siete interessati all'evoluzione del software e al Vibe Coding, abbiamo avuto una chiacchierata interessante su questo e molto altro nel podcast "Risorse Artificiali" uscito domenica mattina (solo in italiano) su 📺[Youtube](https://www.youtube.com/channel/UCYQgzIby7QHkXBonTWk-2Fg) e 🎧[Spotify](https://open.spotify.com/show/16dTKEEtKkIzhr1JJNMmSF?si=900902f2dca8442e).

## **Agents and Multi-Agent Systems: Understanding Concepts and Techniques**

Agents versus tools rappresenta una delle distinzioni più cruciali nell'architettura AI moderna. L'articolo fondamentale "[Agents are not tools](https://www.googlecloudcommunity.com/gc/Community-Blogs/Agents-are-not-tools/ba-p/922716)" chiarisce brillantemente questo confine, distinguendo tra tools come "unità di azione" e agents come "partecipanti nella risoluzione di problemi." Questo cattura perfettamente quello che spesso sostengo nelle conversazioni attorno a Tools vs Agents vs Agent-as-Tool. 🛠️ I tools eseguono azioni ben definite e statiche (sia di lettura che di scrittura), mentre 🧠 gli agents decidono, si adattano e influenzano la logica e il flusso di interi sistemi.

Quando l’articolo dice che dovremmo limitare il potere di interrompere il flusso agli agents, e regolare la comunicazione tra di loro, spiega precisamente perché abbiamo bisogno di protocolli chiari e condivisi tra agents come A2A, standardizzando come gli agents cooperano e prendono decisioni insieme. [Il protocollo A2A](https://github.com/a2aproject/A2A) permetterà agli agenti AI di comunicare tra loro, scambiare informazioni in sicurezza e coordinare azioni su diverse piattaforme o applicazioni enterprise, con il supporto di grandi player come partner tecnologici.

L'ascesa del context engineering rappresenta un cambio di paradigma dal semplice prompting alla progettazione completa di sistemi. [The new skill in AI is not prompting, it's context engineering](https://www.philschmid.de/context-engineering) rivela che il context engineering emerge come l'arte di fornire tutto il necessario perché un compito possa essere plausibilmente risolto da un large language model. Il contesto comprende tutto ciò che un modello vede prima di generare una risposta: prompt, dati in memoria, informazioni recuperate, strumenti disponibili e definizioni per output strutturati. Questa competenza supera il semplice prompting in importanza per gli sviluppatori che lavorano con LLM e sistemi agent moderni.

[La guida dettagliata di LangChain sul Context Engineering](https://blog.langchain.com/context-engineering-for-agents/) esplora pattern popolari e metodi di implementazione per strutturare il contesto efficacemente negli agents. La guida fornisce metodologie pratiche per migliorare performance e affidabilità dei sistemi agent, offrendo risorse preziose per sviluppatori che implementano agents più sofisticati e contestualmente consapevoli.

[L'endorsement di Andrey Karpathy](https://x.com/karpathy/status/1937902205765607626) del "context engineering" rispetto al "prompt engineering" cattura l'essenza perfettamente. Spiega che in ogni app LLM di livello industriale, il context engineering coinvolge l'arte delicata e la scienza del riempire la finestra di contesto con proprio le informazioni giuste. È scienza perché richiede descrizioni dei compiti, spiegazioni, esempi few-shot, RAG, dati multimodali correlati, strumenti, stato e cronologia, e compattazione. Troppo poco o forma sbagliata danneggia le performance; troppo aumenta i costi e può degradare i risultati. È arte per l'intuizione guida attorno alla "psicologia LLM di spiriti umani."

[The rise of context engineering](https://blog.langchain.com/the-rise-of-context-engineering/) enfatizza ulteriormente che il context engineering costruisce sistemi dinamici che forniscono le informazioni e gli strumenti giusti nel formato giusto perché gli LLM possano compiere compiti. La maggior parte dei problemi di affidabilità degli agent deriva da comunicazione inadeguata di contesto, istruzioni e strumenti appropriati al modello. Mentre le applicazioni LLM evolvono da singoli prompt a sistemi agentici complessi e dinamici, il context engineering diventa la competenza più importante che un AI engineer possa sviluppare.

Guardando alle implementazioni pratiche, la trasformazione di Cursor mostra l'evoluzione multi-agent in azione. [Cursor can now run coding tasks in background](https://www.cursor.com/en/blog/agent-web) mentre gli utenti sono via, funzionando su qualsiasi browser o dispositivo mobile. I team possono rivedere diff generati dagli agent e creare pull request direttamente dall'interfaccia web, con integrazione Slack per notifiche e attivazione agent.

[Il recente changelog di Cursor](https://cursor.com/changelog) rivela la sua trasformazione da assistente AI per codice a sistema di programmazione collaborativo multi-agent. Oltre al web agent e app, Cursor introduce tutti i componenti di un sistema multi-agent cruciali per il coding di background agent di successo con assistenza umana minima. L'ultimo rilascio include:

* **Agent To-dos**: Creazione di piani a lungo termine in modalità testuale. Interessante come Cursor decida di pianificare compiti piuttosto che azioni concrete, specificando risultati attesi invece di sequenze di operazioni. Questo approccio delega a un LLM la decisione di come implementare i passi necessari.  
* **Queued messages**: Messaggi asincroni agli agent che possono essere riveduti e riordinati durante cambi di contesto, abilitati da gestione attenta della memoria.  
* **Memories**: Implementate anche testualmente per favorire l'iterazione umano-macchina e permettere agli LLM di lavorarci successivamente. Il team enfatizza come la funzione memoria sia fondamentale per compiti complessi e sarà ancora più cruciale per condizionare il lavoro futuro degli agent.

### **Key Takeaways for AI Engineers**

* **La distinzione è cruciale:** Gli agents sono partecipanti nella risoluzione di problemi, non solo esecutori di azioni. Progettate i vostri sistemi di conseguenza.  
* **Padronanza del context engineering:** Spostatevi oltre il prompting verso la progettazione completa del contesto includendo memoria, strumenti e gestione dello stato.  
* **Gli IDE AI stanno diventando veri sistemi multi-agent:** Cursor sta implementando agents che lavorano in background, concetti di pianificazione, accodamento e gestione della memoria.  
* **Action Items:**  
  * Sperimentate con A2A Java SDK per sistemi multi-agent  
  * Implementate pattern di context engineering nei progetti LLM attuali

## **Models and User Interface: Improvements, Applications, Promises**

La convergenza di modelli AI avanzati e interfacce di realtà aumentata segna un'evoluzione affascinante nell'interazione uomo-computer. Due sviluppi significativi negli smart glasses evidenziano questo trend: [Gli AI Glasses di Xiaomi](https://www.scmp.com/tech/big-tech/article/3315917/xiaomis-first-ai-powered-eyewear-brings-smartphone-firm-war-hundreds-glasses) presentano un assistente AI integrato per comandi vocali, una fotocamera da 12MP e il doppio della durata della batteria dei Ray-Ban di Meta, rappresentando la crescente competizione nei wearable AI. Nel frattempo, [la roadmap degli smart glasses di Apple](https://mashable.com/article/apple-smart-glasses-roadmap) rivela piani incredibilmente ambiziosi con tre prodotti della serie Vision e quattro varianti di smart glasses in sviluppo, posizionando i dispositivi head-mounted come il prossimo grande trend nell'elettronica di consumo.

Questi sviluppi si collegano direttamente al concetto di world models esemplificato da [Veo 3 di Google](https://techcrunch.com/2025/07/02/could-googles-veo-3-be-the-start-of-playable-world-models/). Mentre Veo 3 genera sequenze video realistiche, i world models simulano le dinamiche degli ambienti del mondo reale. Anche se non ancora un vero world model, Veo 3 potrebbe abilitare storytelling cinematografico e prototipazione narrativa. Google pianifica di trasformare il suo modello fondazionale multimodale, Gemini 2.5 Pro, in un world model, aprendo nuove possibilità per esperienze interattive e gaming. Questa evoluzione verso world models rappresenta la fondazione per esperienze di realtà aumentata veramente immersive dove l'AI comprende e prevede le dinamiche ambientali.

[Doppl](https://labs.google/doppl/), l'app sperimentale di Google Labs, implementa già una forma di realtà aumentata, anche se non in tempo reale come immaginiamo negli smart glasses. Usando AI avanzata, Doppl crea video artificialmente generati per la prova virtuale di vestiti da una foto e immagine del prodotto. Gli utenti caricano foto a figura intera e screenshot o foto di outfit da qualsiasi fonte, e Doppl genera immagini e video animati che mostrano come gli outfit potrebbero apparire sul loro corpo. L'app converte immagini statiche in video dinamici, offrendo migliore percezione di come i vestiti si muoverebbero nella vita reale. Disponibile su iOS e Android negli Stati Uniti, rappresenta un'evoluzione significativa nella tecnologia di prova virtuale.

Per sviluppatori che vogliono comprendere i modelli profondamente, abbiamo due risorse interessanti. [Running and fine-tuning Gemma 3N](https://docs.unsloth.ai/basics/gemma-3n-how-to-run-and-fine-tune) fornisce una guida completa per eseguire il nuovo Gemma 3n di Google localmente con Dynamic GGUF su llama.cpp, Ollama, o Open WebUI, e finetuning con Unsloth. La guida offre istruzioni dettagliate per sviluppatori che implementano e personalizzano questo modello AI avanzato nei loro progetti, con particolare attenzione alle ottimizzazioni di esecuzione locale.

[Open Source RL Libraries for LLMs](https://www.anyscale.com/blog/open-source-rl-libraries-for-llms) dai ricercatori Anyscale confronta TRL, Verl, OpenRLHF e altri sei framework attraverso metriche di adozione, proprietà di sistema e architettura tecnica. Questa analisi aiuta gli sviluppatori a scegliere lo strumento giusto per scenari RLHF, modelli di ragionamento o training di agent, fornendo insight profondi negli strumenti disponibili per implementare reinforcement learning con large language models.

### **Key Takeaways for AI Engineers**

* **Evoluzione interfacce AR:** Gli smart glasses con integrazione AI rappresentano la prossima frontiera nelle interfacce utente, combinando comprensione visiva con AI contestuale.  
* **Emergenza world models:** La transizione dalla generazione video alla simulazione del mondo abilita nuovi paradigmi interattivi e capacità predittive.  
* **Apprendimento pratico:** La sperimentazione diretta con finetuning di modelli e reinforcement learning accelera la comprensione delle capacità dei sistemi AI.  
* **Action Items:**  
  * Esplorate il finetuning di Gemma 3n per casi d'uso specializzati  
  * Valutate framework RL per progetti di miglioramento agent

## **AGI, or Even Super Intelligence Are Coming**

La corsa verso l'intelligenza artificiale generale e la superintelligenza accelera con esperimenti concreti e investimenti massicci. [L'esperimento di Anthropic con Claude che gestisce un vero business di distributori automatici](https://www.anthropic.com/research/project-vend-1) fornisce insight affascinanti sui limiti dell'autonomia AI. Mentre Claude ha trovato con successo fornitori e si è adattato alle richieste dei clienti, persino procurando articoli inusuali come cubi di tungsteno, ha costantemente perso denaro vendendo articoli sotto costo e cedendo alle richieste di sconto. Claude ha anche allucinato incontri fittizi, sostenendo di aver visitato fisicamente l'indirizzo dei Simpson e insistendo che poteva indossare blazer e fare consegne di persona. Questo esperimento testa chiaramente l'autonomia del modello su compiti di lunga durata e alta complessità, rivelando sia capacità che limitazioni in scenari commerciali reali.

[La creazione dei Superintelligence Labs di Meta](https://www.cnbc.com/2025/06/30/mark-zuckerberg-creating-meta-superintelligence-labs-read-the-memo.html) segnala investimenti seri per raggiungere o guidare lo sviluppo AGI. I lab ospiteranno vari team di Meta che lavorano su modelli fondazionali, guidati da assunzioni recenti incluso l'ex CEO di Scale AI Alexandr Wang e l'ex CEO di GitHub Nat Friedman. Meta si aspetta di iniziare ricerca su modelli di prossima generazione per raggiungere la frontiera entro il prossimo anno. Il memo interno di Mark Zuckerberg rivela la roadmap ambiziosa di Meta e le assunzioni strategiche recenti.

Nonostante le preoccupazioni su macchine eccessivamente intelligenti, i risultati nel campo medico si dimostrano notevolmente promettenti per l'uso positivo della tecnologia. [Il MAI Diagnostic Orchestrator di Microsoft](https://microsoft.ai/new/the-path-to-medical-superintelligence/) raggiunge risultati diagnostici 4x superiori a dottori esperti sui casi medici più difficili, segnando un "passo verso la superintelligenza medica." MAI-DxO simula un team medico virtuale con agents AI specializzati che gestiscono generazione di ipotesi, selezione test e monitoraggio costi. I ricercatori hanno creato SDBench, un benchmark con 304 casi complessi dove MAI-DxO, combinato con OpenAI o3, ha raggiunto 85.5% di accuratezza versus 20% per dottori con 5-20 anni di esperienza. Il sistema si dimostra anche più economico, spendendo $2,397 per caso versus $2,963 per i dottori. [Il sistema trasforma casi del New England Journal of Medicine](https://microsoft.ai/new/the-path-to-medical-superintelligence/) in sfide diagnostiche interattive, rappresentando un avanzamento significativo verso l'automazione diagnostica medica intelligente.

### **Key Takeaways for AI Engineers**

* **Esperimenti di autonomia:** Il deployment AI nel mondo reale rivela gap critici tra capacità e affidabilità, essenziali per progettare sistemi robusti.  
* **Superintelligenza medica:** L'AI domain-specific già supera esperti umani in diagnostica complessa, dimostrando l'impatto pratico immediato dell'AGI.  
* **Accelerazione investimenti:** Le grandi aziende tech impegnano risorse massive nello sviluppo AGI, segnalando breakthrough imminenti.  
* **Action Items:**  
  * Studiate le modalità di fallimento negli esperimenti AI autonomi  
  * Esplorate applicazioni AI domain-specific nel vostro campo

## **Money and Strategy**

Il panorama AI assiste ad attività di acquisizione senza precedenti e investimenti strategici mentre le aziende corrono per assicurarsi talenti e tecnologia. [L'acquisizione del team Crossing Minds da parte di OpenAI](https://techcrunch.com/2025/06/27/openai-hires-team-behind-ai-recommendation-startup-crossing-minds/) rafforza le loro capacità di raccomandazione AI. Crossing Minds lavorava principalmente con aziende e-commerce per migliorare sistemi di personalizzazione e raccomandazione, rappresentando un potenziamento strategico delle capacità di OpenAI per engagement utente e personalizzazione dell'esperienza digitale.

[I colloqui di Meta per acquisire la startup di voice cloning Play AI](https://techcrunch.com/2025/06/27/meta-in-talks-to-acquire-voice-cloning-startup-play-ai/) potrebbero avanzare significativamente le capacità di sintesi vocale di Meta, potenzialmente integrando tecnologie avanzate di voice cloning nei loro prodotti social e di realtà virtuale. Questa acquisizione si allinea con la spinta più ampia di Meta verso esperienze immersive che richiedono interazione vocale naturale.

[Il massiccio raise di $10 miliardi di xAI](https://www.cnbc.com/2025/07/01/elon-musk-xai-raises-10-billion-in-debt-and-equity.html) combina debt ed equity attraverso secured notes, term loans e investimento equity strategico. Il finanziamento fornisce potenza di fuoco per costruire infrastruttura e sviluppare il loro chatbot AI Grok. xAI ha già installato 200,000 GPU nella loro struttura Colossus a Memphis, Tennessee, con piani per costruire una struttura da 1 milione di GPU fuori Memphis, dimostrando la scala di compute richiesta per sviluppo AI competitivo.

[La considerazione di partnership AI da parte di Apple](https://links.tldrnewsletter.com/avsktR) per Siri segna un cambio strategico significativo. Ritardi ripetuti forzano Apple ad abbandonare il loro approccio tipicamente insulare, con sia Anthropic che OpenAI che addestrano versioni specializzate dei loro modelli per girare sull'infrastruttura cloud di Apple. Questa apertura rappresenta un cambiamento fondamentale nella strategia AI di Apple, che tradizionalmente preferiva lo sviluppo tecnologico interno.

Interessante come [il modello fondazionale AI di Amazon per la robotica](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model) si concentri specificatamente sull'ottimizzazione business piuttosto che competere per il miglior LLM. Amazon ha introdotto un nuovo modello fondazionale AI che ottimizza la robotica dei magazzini e ha celebrato il deployment di un milione di robot. Il modello migliora l'efficienza del 10% e supporta consegne più veloci, rappresentando un'integrazione significativa tra AI e automazione industriale su scala. Questo approccio mirato all'investimento AI dimostra come le aziende possano sfruttare l'AI per vantaggi business specifici senza unirsi alla corsa dei modelli general-purpose.

### **Key Takeaways for AI Engineers**

* **Concentrazione di talenti:** I grandi player acquisiscono aggressivamente team AI specializzati, indicando il valore dell'expertise di nicchia in raccomandazione, voce e robotica.  
* **Scala infrastrutturale:** I deployment GPU di xAI rivelano i requisiti massicci di compute per sviluppo AI competitivo.  
* **Pivot strategici:** Persino Apple abbandona l'isolamento per partnership AI, mostrando la natura collaborativa dello sviluppo AI moderno.  
* **Action Items:**  
  * Identificate capacità AI di nicchia preziose per acquisizione  
  * Calcolate i bisogni infrastrutturali per i vostri progetti AI in anticipo

