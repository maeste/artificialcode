
## Ottimizzare per una achitettura ibrida locale /remoto

* Si vede sempre più ottimizzare per girare in locale
	* inferenza
	* Modelli piccoli
	* Modelli quantization aware
	* Quantizzazioni assimmetriche e grande lavoro di quantizzazione
	* Architetture nuove che tolgono encoder o alcune asi di decoding
	* Harness disegnati in modo minimale (Pi) o pensati per girare a braccetto con inferenza (DS4-agent), sistemi come quello di unsloth per fare inferena e anche fine tuning
	* 
* L'idea sembra quella di avere più sistemi che girano in locale
* Importanza dell'hardware per cui Apple al momento sta vincendo a man bassa grazie alla stabilità della sua architettura arm con ram condivisa. Se Apple ha difficotà su tutto il resto l'hw per far girare cos ein locale è un punto di svolta. NVIDIA e microsoft provano a lanciar eun sistema concorrent (RTX spark), perchè DGX spark è troppo specifico
* Mio pensiero forte: al momento bisogna avere o hw di un certo livello (ad esempio per far girare deepseek con DS4) o casi d'uso abbastanza specifici, anche se gli ultimi modelli piccoli come Gemma 4 12B aprono la strada anche alle schede RTX ed ADA con 16Gb di ram. Io vedo un futuro con architetture ibride, facendo giare in locale alcune delle operazioni su modelli locali, magari finetunati, deleggando a modelli in cloud quando necessario. Un po' quello che abbiamo visto con "/advisor" in claude cde, ma dove il modello principale è locale e l'advisor in cloud richiamato solo quando necessario. Qualcosa di simile a quanto propone perplexity. A sensazione una delle ottimizzazioni ingegneristiche di cui abbiamo bisogno potrebbe essere la capacità di fare il loading dei modelli in memoria in modo più veloce e dinamico per poter caricare velocemente versioni specifiche o con fine tuninig specifici. Una sfida per la quale al momento non ci sono ancora soluzioni chiare, ma per la quale vale la pena tenere gli occhi aperti.

## Link a supporto
[**MiniMax promises M3 weights after 1M-context model launch (2 minute read)**](https://tracking.tldrnewsletter.com/CL0/https:%2F%2Fwww.implicator.ai%2Fminimax-promises-m3-weights-after-1m-context-model-launch%2F%3Futm_source=tldrai/1/0100019e8db2ce27-ebfc9d5d-e7a5-43d1-9960-fe14f34affbb-000000/fD5H5ePwfXiXY7b2DbK8mzhZ4kR_Mq__nd1Bi5YDJBc=452)  
  
MiniMax will release the model weights and a technical report for its M3 model within the next 10 days. The new model is currently available through MiniMax Code, token plans, and an API. It has a 1M-token context window and a guaranteed 512,000-token minimum for API use. The model is the first open-weight model to combine frontier coding, native multimodality, and a 1M-token context window. MiniMax lists standard API pricing up to 512,000 input tokens at $0.60 per million input and $2.40 per million output.

https://www.perplexity.ai/hub/blog/the-data-center-moves-to-your-machine?utm_source=tldrai


https://github.com/antirez/ds4

https://unsloth.ai/docs/new/studio

https://www.nvidia.com/it-it/products/rtx-spark/
