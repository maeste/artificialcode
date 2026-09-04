# Il 2026 è l'anno delle review assistite: vi apro la cassetta degli attrezzi

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

*Questa settimana apro il cassetto degli attrezzi. La domanda che mi fate più spesso, sui social e nei commenti, ha finalmente una risposta: un repository GitHub aperto, con le skill che uso tutti i giorni, il workflow che le concatena e il cheatsheet per orientarsi. È un deep dive più corto del solito proprio perché il grosso sta lì, e perché il vero protagonista è pr-walkthrough, la skill con cui faccio le review assistite. Nella parte link c'è il finale del giallo: Ox Alpha era davvero GLM-5.3-Flash, e Z.ai lo conferma con i numeri. Poi Qwen anticipa l'architettura della versione 4, MiniMax-H3 spiega perché gli open weight contano, Sopro V2 porta il TTS on-device e AutoSaddler di Microsoft ottimizza l'harness analizzando i trace, che secondo me è il futuro. In agenda la puntata 69 del podcast sul caso Ox Alpha, AI Salon Milano a settembre e Zurich a novembre. Buona lettura.*

### La mia agenda

[Podcast](https://risorseartificiali.com):
  * Sabato è uscito "Era stealth, era GLM: 5.3 Flash e i numeri da giganti", dove smontiamo il modello comparso come Ox Alpha: 6 miliardi di parametri attivi, benchmark da colosso, 138 dollari la suite. Ascolta: https://www.youtube.com/watch?v=_C22mIG9LZs&utm_source=codiceartificiale&utm_medium=newsletter&utm_campaign=ep69_drop

Da solo:
* Il 14 settembre sarò ospite di [AI Salon Milano](https://luma.com/aisalon?e=evt-qhXFEh6vFAzCIxz) per una chiacchierata con [Yuri Mariotti](https://www.linkedin.com/in/yurimariotti/)
* Il 20 novembre sarò uno degli speaker, insieme ad [Alessio Soldano](https://aladinodigitale.it/), ad [Agentic Engineering Days Zurich](https://www.agenticdays.com/) con un talk sugli standard nel mondo degli agenti
* Anche per il 10 ottobre qualcosa bolle in pentola sullo stesso tema... ma non annuncio finché non esce l'agenda... magari qualcuno attento alle conferenze e ai developer group ha capito :)

---

## La mia cassetta degli attrezzi per agenti adesso è open source

In tanti mi avete chiesto, a più riprese attraverso i social, i commenti e altro, di spiegare come lavoro con i miei agenti di coding. Ed è esattamente quello che voglio fare in questo deep dive. È un deep dive particolare, perché sarà un po' più corto del solito: il grosso della lettura e delle informazioni lo trovate, come mia abitudine, in un repository GitHub, [RisorseArtificiali/skills](https://github.com/RisorseArtificiali/skills).

Prima di spiegarvi come il repository è strutturato e come leggerlo, lasciate che vi precisi una cosa: i progetti in cui sono coinvolto sono progetti molto grandi. Il mio lavoro è sviluppare framework e piattaforme di sviluppo su cui i programmatori dei clienti costruiscono grossi sistemi enterprise, ovviamente con tanta AI di mezzo, sia nello sviluppo dei framework sia in quello che supportano per i clienti. Il workflow è nato lì, su progetti con più di dieci contributor attivi e oltre cinquanta persone coinvolte. Non per questo non funziona su progetti più piccoli, ma lì va adattato.

Il repository è una collezione di skill. Alcune sono prese da altri autori, tra i più famosi [Matt Pocock](https://github.com/mattpocock/skills) e [Addy Osmani](https://github.com/addyosmani/agent-skills), e usate così come sono, direttamente come le trovate nei loro repository. Per poche di queste ho preferito fare delle piccole personalizzazioni perché si adattassero meglio al mio caso d'uso: grilling, ad esempio, l'ho riscritta per fare una domanda alla volta invece dei round in batch. Altre sono interamente sviluppate da me, ovviamente con l'aiuto del mio agente di fiducia, per i miei casi d'uso. A corredo trovate un [workflow](https://github.com/RisorseArtificiali/skills/blob/main/WORKFLOW.md) che spiega come le uso nella mia quotidianità: la pipeline parte da brainstorming e grilling, passa dalla PRD e dai piani di implementazione, e finisce nella review avversaria prima del merge, con i gate in cui decide l'umano, cioè io. E un [cheatsheet](https://github.com/RisorseArtificiali/skills/blob/main/SKILLS-CHEATSHEET.md) che vi dà tutto l'elenco delle skill e quando ha senso usarle. Nel repository trovate citati anche i tre server MCP che uso d'abitudine: Serena, Backlog.md e qmd.

Come dico anche nel repository, sentitevi liberi di adattare le skill e il workflow al vostro caso. Il mio consiglio è quello di partire con le skill così come sono, visto che sono state da me testate negli ultimi mesi, e adattare eventualmente il vostro workflow, cercando di essere sempre voi a governare gli agenti e le skill, in base a quello che vi serve.

Due note finali, che trovate anche nel repository: io lavoro sempre con agenti multipli in parallelo, tipicamente cinque su un paio di progetti contemporaneamente, e spesso non digito le mie istruzioni ma le detto. Come faccio a fare queste cose su Linux? Ovviamente con l'altro progetto che cito spesso, [Lince](https://lince.sh/), e una delle sue costole, VoxCode, che trascrive in locale con Whisper: nessun audio lascia la macchina.

Se volete sapere, di tutte le skill da me prodotte, quale è quella che mi piace di più: sicuramente pr-walkthrough, perché mi permette di revisionare pull request molto complesse attraverso un processo iterativo che produce anche degli artefatti che comprendono visualizzazioni grafiche degli impatti e dei cambi architetturali, mappe before/after e blast radius a colpo d'occhio. Ho parlato spesso, sia qui che nel podcast, del fatto che il 2026 è già, o sta diventando, l'anno in cui non si fa più pull request review al modo in cui la facevamo prima: se il 2025 è stato l'anno del coding assistito, sicuramente il 2026 è l'anno delle review assistite. E credo che questa skill dia una grossa mano proprio perché vi permette di non aumentare il vostro debito tecnico ma di restare sempre in controllo di quello che sta succedendo nel vostro repository, da un punto di vista degli impatti e dell'architettura, senza dover leggere necessariamente una riga per volta.

Fatemi sapere che cosa ne pensate e soprattutto contribuite al progetto con le vostre pull request: di sicuro le rivedrò con una di quelle skill che vi ho presentato.

---

## I link che mi hanno colpito questa settimana

### [Qwen3.8-Flash-Next](https://qwen.ai/blog?id=qwen3.8-flash-next)
La cosa che mi ha colpito di più qui è il fatto che Qwen decida di anticipare l'architettura della versione 4: sia per quanto è sparsa, sia per quanto funzioni bene la sparse attention.

### [GLM-5.3-Flash / Ox Alpha: l'annuncio di Z.ai](https://z.ai/blog/glm-5.3-flash) + [l'analisi economica di The Deep View](https://www.thedeepview.com/articles/what-z-ai-s-ox-alpha-reveals-about-ai-economics)
È stato il deep dive di settimana scorsa: andatevelo a leggere se volete. La conferma è arrivata ufficiale: Ox Alpha è GLM-5.3-Flash. Quello che supera le mie aspettative è che sia una versione più piccola di GLM-5.3, soltanto 320 miliardi con 6 miliardi attivi. Ma le prestazioni, sia da benchmark che dalle mie impressioni, sono notevoli: sulla parte di puro testo, soprattutto quella agentica e coding, sia per quanto riguarda la parte multimodale.

### [MiniMax-H3 su 8×H200](https://www.lmsys.org/blog/2026-08-27-minimax-h3-h200) + [H3 Max di fal](https://blog.fal.ai/introducing-h3-max-by-fal/)
Con MiniMax-H3 si vede quanto sia importante avere modelli open, perché quello che è successo in settimana è che le versioni fine-tuned, o comunque rimaneggiate, del modello di base sono ancora meglio di esso.

### [Sopro V2: TTS privato, veloce e on-device](https://research.haloneuro.ai/posts/sopro-v2)
Un altro TTS piccolo e veloce che gira on-device o comunque sulla CPU. Non vedo l'ora di darlo al mio Hermes Agent. Se funziona meglio di quello che sto usando adesso ve lo farò sapere qui o in podcast.

### [Gemini Omni 1.1 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)
Nuova versione omnimodale di Gemini che promette meraviglie. Io l'ho provata poco per ora, ma mi riprometto di farlo molto di più nei prossimi giorni.

### [AutoSaddler](https://github.com/microsoft/AutoSaddler)
Il progetto è nato da un interessantissimo paper di ricerca degli ultimi tempi da parte di Microsoft. L'idea è quella di ottimizzare l'harness, inteso come prompt, skills, tools e tutto quanto, analizzando il trace di un'esecuzione di un agente. Sicuramente challenging ma estremamente affascinante: torneremo di sicuro a parlarne, di questo o di altri modi di ottimizzare gli harness analizzando i loro trace, perché credo che questo sia il futuro in questo settore particolare.
