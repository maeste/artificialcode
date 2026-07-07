# Guerra fredda dell'AI: gli open weight non sono un ripiego, sono l'assicurazione

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

Settimana in cui prendo finalmente di petto la saga di Fable, che nei numeri scorsi avevo lasciato volutamente in sospeso aspettando che la polvere si posasse. Ora la polvere si è posata, e non nel modo che speravo: la Casa Bianca ha interdetto l'accesso a Fable e Mythos, e per noi europei il messaggio è pesante. Nel deep dive parto da qui per arrivare alla mia tesi: in un mondo dove i modelli di frontiera americani possono esserci tolti per decisione politica, i modelli open weight diventano molto più di un'alternativa tecnica, sono l'unica forma di indipendenza che ci resta. DeepSeek, MiniMax, GLM e Kimi sono in forma smagliante, e vi racconto perché GLM 5.2 è da mesi il mio preferito per esperienza d'uso. Nella sezione link trovate i temi che fanno da contorno: OpenAI che prepara GPT-5.6 tagliando i prezzi mentre Anthropic è nei guai, Midjourney che a sorpresa costruisce uno scanner ecografico full-body, Factory 2.0 e le software factory, l'agente di ricerca autonomo Sakana Marlin, il percorso verso l'ASI secondo DeepMind, e il loop-driven development che mette nero su bianco il filo del mio deep dive della settimana scorsa. Buona lettura.

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * Nuovo episodio di Risorse Artificiali: Paolo clona la sua voce in locale e gratis, e da oggi non si fida più di un messaggio vocale. [Ascolta](https://youtu.be/Z-srn-RNf5s?utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep57_drop).
  * Nella stessa puntata: il ritiro di Fable, Codex 5.5 vs Opus 4.8 e perché ormai non guardiamo più il codice che scriviamo con gli agenti.
  * I nostri progetti [Lince.sh](https://lince.sh) e AntiVocale ([Google Play](https://play.google.com/store/apps/details?id=com.antivocale.app), [GitHub](https://github.com/RisorseArtificiali/anti-vocale)), ormai li conoscete bene.

Da solo:
  * Sono stato a Catania come speaker al [Coderful](https://www.coderful.io/), una delle conferenze meglio organizzate e con i migliori contenuti che mi sia capitato di vedere di recente. Le mie slide le trovate [qui](https://maeste.it/coderful2026); appena disponibile, lì troverete anche il video.
  * Il 24 giugno sarò a Milano come speaker di [AIConf](https://www.aiconf.it/).

---

## Quando la frontiera è ostaggio della politica

La saga di Fable, che seguo da un paio di settimane e di cui finora non avevo voluto fare il deep dive perché mi pareva presto per tirare le somme, è arrivata al punto che temevo. La Casa Bianca ha interdetto l'accesso a Fable e Mythos, e la cosa grave non è tanto il blocco in sé, quanto l'intenzione che ci sta dietro: a quanto pare lo si voleva bannare solo per i cittadini non americani. Poi, nella difficoltà di distinguerli uno per uno, [Anthropic ha finito per chiudere i rubinetti a tutti](https://www.anthropic.com/news/fable-mythos-access). Se la lettura è questa, il messaggio è pesante, soprattutto per noi europei: il divario con gli Stati Uniti, invece di assottigliarsi, rischia di diventare ancora più marcato.

E allora la domanda diventa una sola: se i modelli di frontiera americani possono esserci tolti da un giorno all'altro per decisione politica, su cosa costruiamo? La mia risposta, in questo momento, è netta: i modelli open source, o per essere precisi open weight. Mi sembrano l'alternativa migliore, e forse perfino l'unica, visto che sul fronte europeo Mistral resta parecchio lontana dallo stato dell'arte. Il bello degli open weight è proprio questo: i pesi li hai tu, nessuna direttiva te li può revocare con un tratto di penna.

La buona notizia è che l'alternativa esiste davvero, ed è in forma smagliante. DeepSeek, MiniMax, GLM, Kimi sono tutte ottime opzioni, e nelle ultime settimane hanno rilasciato versioni nuove una dietro l'altra. [DeepSeek ha appena chiuso un round da 7,4 miliardi](https://techfundingnews.com/deepseek-raises-7-4b-at-50b-valuation-in-first-ever-external-funding-round/) che la incorona startup AI più preziosa della Cina, e [Kimi K2.7 Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code) spinge sul coding agentico con un MoE da un trilione di parametri. Sono ottimi anche per l'inferenza locale, di cui parlo spesso, ma restano interessanti come modelli a prescindere da dove li fate girare.

E qui si chiude un cerchio che avevo lasciato aperto giusto un paio di settimane fa. Quando parlavo del trend del locale e delle architetture ibride, avevo buttato lì una previsione: visto che si cominciavano a vedere governi che interdicono l'uso dei modelli più potenti, presto avremmo potuto averne bisogno sul serio. Ecco, ci siamo. Avere modelli di questo livello che girano anche sulle nostre macchine non è più soltanto una questione di costi o di privacy, è una forma di indipendenza tecnologica.

In mezzo a tutti, quello su cui voglio spendere due parole è GLM. La versione [5.2 è stata definita "Opus level"](https://z.ai/blog/glm-5.2), SOTA insomma. Non il migliore in assoluto, quel posto resta per ora di GPT-5.5, ma con un distacco davvero risicato, e comunque un modello capace di reggere compiti lunghi e complessi. Per me è già il modello primario di Hermes Agent e il fallback per il coding, anche se sospetto che presto diventerà uno dei primari pure lì. Mi piace particolarmente usarlo con un harness minimale ed estensibile come Pi.

Lo uso fin da novembre scorso, e l'ho sempre trovato tra i migliori modelli open source. Attenzione, non parlo di innovazione: lì DeepSeek resta di gran lunga il più interessante in termini di ricerca, sia nella versione 3 che nella 4. Parlo di esperienza d'uso, e su quella GLM per me è in cima da mesi. Non sono il solo a pensarla così: [anche antirez lo sta integrando in DS4](https://x.com/antirez/status/2068723687990108312). Un'ultima nota pratica, come early adopter ho un [link con il 10% di sconto sull'abbonamento](https://z.ai/subscribe?ic=DWTQHGMFKV), ed è ancora valido se volete provarlo.

Tornando al punto di partenza: finché l'accesso ai modelli di frontiera dipenderà da una direttiva che può cambiare dall'oggi al domani, gli open weight non sono un ripiego, sono la nostra polizza assicurativa. E per fortuna, oggi, è una polizza che copre quasi tutto.

---

## I link che mi hanno colpito questa settimana

### [OpenAI prepara i modelli GPT-5.6](https://www.testingcatalog.com/openai-prepares-gpt-5-6-models-for-the-upcoming-release/)

Il dettaglio che salta all'occhio, soprattutto dopo il deep dive, è il timing: OpenAI taglia i prezzi in modo aggressivo per insidiare Anthropic proprio mentre Fable è impantanata nei guai regolatori americani. Sono ancora rumor, quindi numeri e date li prendo con le pinze, ma la finestra da 1,5 milioni di token e la spinta sul coding long-horizon dicono dove si gioca la partita.

### [Midjourney costruisce uno scanner ecografico full-body](https://www.engadget.com/2196998/midjourney-full-body-ultrasonic-scanner/)

Questa è la notizia che non c'entra niente con le altre, e proprio per questo me la tengo. Che un'azienda nata per generare immagini si metta a costruire scanner ecografici full-body, con tanto di spa, è un salto che fatico a inquadrare. I 60 secondi contro l'ora e mezza di una risonanza fatico a crederli finché non vedo dati veri, ma se confermati è physical AI da tenere d'occhio.

### [Factory 2.0: dalle coding agent alle software factory](https://factory.ai/news/software-factory)

Qui ritrovo, quasi parola per parola, la tesi del deep dive della settimana scorsa: l'ingegnere che smette di scrivere software e comincia a costruire le fabbriche che lo costruiscono. Mi colpisce soprattutto il pilastro dell'indipendenza dai modelli e dell'intelligenza sovrana, che si lega dritto al discorso open weight di oggi. Il rischio, come sempre, è che resti più manifesto che prodotto.

### [Sakana Marlin](https://sakana.ai/marlin-release/)

Un agente che lavora in autonomia fino a otto ore e sforna report di strategia da cento pagine è il tipo di compito lungo che mi affascina. Resto però fedele al mio chiodo fisso: gli agenti danno il meglio dove il risultato è verificabile, e l'analisi strategica è terreno ben più scivoloso del codice. La domanda vera è come Marlin verifica le proprie conclusioni.

### [Google DeepMind e il percorso verso l'ASI](https://arxiv.org/abs/2606.12683)

Quello che apprezzo di questo paper è la sobrietà: niente singolo momento magico in cui l'AGI diventa superintelligenza, ma una serie di trasformazioni progressive, con colli di bottiglia e attriti messi nero su bianco. È un inquadramento che condivido, e che fa da contrappeso ai toni da rivoluzione imminente. Quaranta minuti abbondanti, ma se vi interessa il lungo periodo sono spesi bene.

### [Da test-driven a loop-driven development](https://generativeprogrammer.com/p/from-test-driven-to-loop-driven-development)

Se avete letto il deep dive della scorsa settimana, qui vi sembrerà di guardarvi allo specchio: trigger, goal, harness, verifier e stato attorno al loop dell'agente sono quasi gli stessi ingredienti con cui provavo a definire il loop engineering. Il punto centrale è quello che ripeto sempre, più autonomia concedi al loop, più forti devono diventare i controlli. Fa piacere vedere il concetto consolidarsi nella community.
