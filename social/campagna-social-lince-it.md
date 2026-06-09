# Campagna Social LINCE - Lancio Open Source

## Parte 1: Post LinkedIn in Italiano

---

### Angolo 1: Sandbox YOLO - "Lancia agenti senza approvare permessi, dormi tranquillo"

#### Alternativa 1A

Lancio 5 agenti AI in parallelo e non approvo nemmeno un permesso.

Sembra un incubo di sicurezza? In realta' e' il contrario.

Quando lavori con agenti di coding, il flusso standard e' questo: l'agente vuole scrivere un file, tu approvi. Vuole eseguire un comando, tu approvi. Vuole cancellare qualcosa, tu approvi. Moltiplica per 5 agenti e il tuo lavoro diventa cliccare "si'" tutto il giorno.

Con LINCE abbiamo ribaltato il problema. Invece di chiedere permessi, mettiamo tutto dentro una sandbox a livello kernel (bubblewrap su Linux, nono su Linux/macOS). Zero overhead. L'agente puo' fare quello che vuole, perche' il danno massimo e' confinato.

E se qualcosa va storto? Snapshot e rollback in un attimo.

Al Voxxed Day Ticino ho detto una cosa che ripeto spesso: la superficie d'attacco sei tu, non il software che produci. LINCE nasce da questa idea.

Open source, licenza MIT: lince.sh

**Allegato consigliato**: GIF o breve video che mostra un agente in YOLO mode dentro la sandbox, con il rollback da snapshot.

#OpenSource #AIEngineering #DevTools #CodingAgents #TerminalLife

---

#### Alternativa 1B

"Ma non hai paura a far girare agenti senza controllo?"

Me lo chiedono ogni volta. La risposta e': dipende da dove girano.

Il vero problema degli agenti di coding non e' che sbagliano (sbagliano, eccome). Il problema e' che ti chiedono il permesso per ogni singola operazione. E tu, dopo il ventesimo popup, inizi ad approvare tutto senza leggere.

Ecco, quella e' la vera falla di sicurezza. Sei tu.

LINCE usa sandboxing a livello kernel con bubblewrap e nono. Nessun overhead. L'agente opera in un ambiente isolato, puo' fare quello che vuole senza chiederti nulla. Se combina un disastro, fai rollback dallo snapshot.

Non e' YOLO nel senso di "me ne frego". E' YOLO nel senso di "l'ambiente e' sicuro, quindi l'agente puo' lavorare libero".

Lo abbiamo costruito con il team di Risorse Artificiali. Open source, MIT.

lince.sh | github.com/RisorseArtificiali/lince

**Allegato consigliato**: Screenshot della dashboard con agenti attivi in sandbox, evidenziando l'indicatore di isolamento.

#DevTools #CodingAgents #OpenSource #Sandbox #AIEngineering

---

#### Alternativa 1C

Il pattern piu' pericoloso nello sviluppo con agenti AI non e' un prompt injection.

E' lo sviluppatore che clicca "approva" per la centesima volta senza leggere cosa sta approvando.

Lo vedo continuamente. Parti con le migliori intenzioni, controlli ogni richiesta. Dopo mezz'ora con 3 agenti in parallelo, il tuo cervello si arrende e approvi tutto a occhi chiusi.

Con LINCE abbiamo eliminato il problema alla radice. Sandboxing a livello kernel (bubblewrap su Linux, nono su Linux/macOS), zero overhead sulle prestazioni. Gli agenti operano in modalita' YOLO perche' l'ambiente e' confinato. Se qualcosa va storto, rollback da snapshot.

La superficie d'attacco non e' il software. Sei tu. E LINCE ti protegge da te stesso.

Progetto open source del team Risorse Artificiali, licenza MIT.

lince.sh

**Allegato consigliato**: Video breve (30-60s) che mostra il confronto tra il flusso classico con approvazioni continue e il flusso YOLO in sandbox.

#AIEngineering #OpenSource #DevSecurity #CodingAgents #LINCE

---

### Angolo 2: Context Switch Killer - "Agenti multipli senza impazzire"

#### Alternativa 2A

Il collo di bottiglia degli agenti AI non e' la generazione. E' la verifica.

Puoi lanciare 8 agenti in parallelo. Il problema e' capire quale ha bisogno di input, quale ha finito, quale si e' bloccato. Con gli strumenti attuali salti da una finestra all'altra, perdi il filo, dimentichi cosa stava facendo il terzo agente.

LINCE risolve questo con una dashboard scritta in Rust/WASM (un plugin per Zellij, circa 900KB). Da un unico pannello vedi tutti gli agenti attivi, il loro stato, chi ha bisogno di te. Passi da uno all'altro con un singolo tasto.

Lo sweet spot che abbiamo trovato e' 3-5 agenti in parallelo. Abbastanza per moltiplicare la produttivita', pochi abbastanza per mantenere il controllo.

Il risultato: meno context switching, piu' tempo a verificare il lavoro che conta.

Open source, MIT: lince.sh

**Allegato consigliato**: Screenshot o GIF della dashboard LINCE con 4-5 agenti attivi, evidenziando gli indicatori di stato e la navigazione con tasti.

#DevProductivity #AIEngineering #OpenSource #MultiAgent #TerminalLife

---

#### Alternativa 2B

Tre agenti che lavorano in parallelo. Uno genera test, uno refactora, uno scrive documentazione.

Bello in teoria. Nella pratica, dopo 10 minuti stai saltando tra finestre come un matto cercando di capire chi ha bisogno di cosa.

Questo e' il problema che ci ha spinto a costruire LINCE. Non serviva un altro modo per lanciare agenti. Serviva un modo per orchestrarli senza perdere la testa.

La dashboard e' un plugin Rust/WASM per Zellij, pesa circa 900KB. Ti mostra tutti gli agenti attivi, chi e' in attesa di input, chi ha finito. Navighi con un singolo tasto. Niente mouse, niente tab del browser, niente alt-tab compulsivo.

Il punto chiave: il collo di bottiglia non e' far generare codice agli agenti. E' verificare quello che producono. LINCE minimizza il tempo perso nel context switching cosi' puoi concentrarti sulla verifica.

Progetto del team Risorse Artificiali. Open source, MIT.

lince.sh | github.com/RisorseArtificiali/lince

**Allegato consigliato**: GIF animata che mostra il passaggio rapido tra agenti nella dashboard con un singolo keystroke.

#CodingAgents #DevTools #Productivity #OpenSource #AIEngineering

---

#### Alternativa 2C

Qual e' il numero giusto di agenti AI da far lavorare in parallelo?

Dopo mesi di test la risposta e': 3-5. Non di piu'.

Con 1-2 agenti non sfrutti il potenziale del parallelismo. Con 8+ perdi piu' tempo a gestirli che a beneficiare del loro lavoro. Il sweet spot e' nel mezzo.

Ma anche con 3-5 agenti, senza gli strumenti giusti e' un caos. Devi sapere in ogni momento chi sta facendo cosa, chi si e' bloccato, chi ha bisogno di input.

Per questo abbiamo costruito la dashboard di LINCE: un plugin Rust/WASM per Zellij (circa 900KB, leggero come deve essere). Vedi tutto in un colpo d'occhio, navighi con singoli tasti. Il tuo lavoro non e' piu' lanciare agenti. E' verificare il loro output.

Perche' il collo di bottiglia reale non e' mai stato la generazione. E' sempre stata la verifica.

Open source, MIT. Costruito con il team di Risorse Artificiali.

lince.sh

**Allegato consigliato**: Infografica che mostra la curva di produttivita' rispetto al numero di agenti (sweet spot 3-5), con screenshot della dashboard.

#MultiAgent #AIEngineering #DevTools #OpenSource #Productivity

---

### Angolo 3: Terminal-Only - "Niente IDE, niente browser, solo terminale"

#### Alternativa 3A

Niente IDE. Niente browser. Niente app extra. Solo il terminale.

Sembra una limitazione, ma e' una scelta progettuale precisa.

Ogni programma che aggiungi al tuo flusso di lavoro e' un context switch in piu'. Un'altra finestra da gestire, un'altra interfaccia da ricordare, un altro aggiornamento che rompe qualcosa.

LINCE trasforma la tua shell in una workstation di ingegneria multi-agente. Zellij fa da window manager. Il plugin dashboard (Rust/WASM, ~900KB) orchestra tutto. VoxCode ti da' input vocale con Whisper locale (una benedizione per chi su Linux ha sempre lottato con l'audio).

Dipendenze minime. Se hai un terminale, hai tutto quello che serve.

E' vendor-independent: funziona con Claude Code, Codex, Gemini, OpenCode, Aider. Vuoi aggiungere un agente custom? Un file TOML e sei a posto.

Progetto open source del team Risorse Artificiali, licenza MIT.

lince.sh

**Allegato consigliato**: Screenshot a schermo intero della workstation LINCE nel terminale con piu' agenti attivi, nessun altro programma visibile.

#TerminalLife #DevTools #OpenSource #AIEngineering #Linux

---

#### Alternativa 3B

L'ultima volta che ho aperto un IDE per lavoro non me lo ricordo.

Non per snobismo. E' che quando hai agenti AI che scrivono codice, la parte "editor" diventa quasi irrilevante. Quello che conta e' orchestrare, verificare, iterare. E per quello il terminale basta e avanza.

LINCE nasce da questa convinzione. E' una workstation multi-agente che vive interamente nel terminale. Zellij come window manager, una dashboard Rust/WASM da 900KB per orchestrare tutto, VoxCode per input vocale con Whisper locale.

Zero dipendenze esterne. Niente Electron che mangia 2GB di RAM. Niente browser con 47 tab aperte. Solo il terminale.

Supporta Claude Code, Codex, Gemini, OpenCode, Aider e qualsiasi agente custom via configurazione TOML. Non ti lega a nessun vendor.

Costruito con il team di Risorse Artificiali. Open source, MIT.

lince.sh | github.com/RisorseArtificiali/lince

**Allegato consigliato**: Video breve (30-45s) che mostra l'avvio di LINCE da un terminale pulito fino alla workstation completa con agenti attivi.

#TerminalLife #OpenSource #DevTools #CodingAgents #MinimalSetup

---

#### Alternativa 3C

Se usi Linux e hai mai provato a far funzionare la dettatura vocale, sai di cosa parlo.

E' uno dei piccoli problemi che nessuno risolve perche' non e' abbastanza "sexy". Ma quando lavori con agenti AI, poter dare istruzioni a voce mentre verifichi il codice e' un game changer.

VoxCode in LINCE usa Whisper in locale. Niente cloud, niente latenza, niente privacy concerns. Funziona e basta.

Ma VoxCode e' solo una delle feature. LINCE e' una workstation multi-agente interamente basata su terminale. Niente IDE, niente browser, niente app extra.

Zellij come window manager. Dashboard Rust/WASM (~900KB) per orchestrare gli agenti. Sandboxing a livello kernel per la modalita' YOLO. Supporto per Claude Code, Codex, Gemini, OpenCode, Aider e agenti custom via TOML.

Se hai un terminale, hai tutto.

Open source, MIT. Progetto del team Risorse Artificiali.

lince.sh

**Allegato consigliato**: Video demo di VoxCode in azione: l'utente da' un'istruzione vocale e l'agente nel terminale la esegue.

#Linux #VoiceInput #DevTools #OpenSource #AIEngineering

---

### Angolo 4: Lancio Open Source - "Dal palco alla tastiera"

#### Alternativa 4A

Al Voxxed Day Ticino ho detto una frase che mi e' rimasta in testa: "La superficie d'attacco sei tu, non il software che produci."

Non era una battuta. Era una frustrazione reale.

Lavoravo con agenti AI tutti i giorni e vedevo sempre lo stesso schema: l'agente chiede permesso, tu approvi. Chiede ancora, approvi ancora. Dopo un po' approvi senza leggere. E quello e' il momento in cui sei vulnerabile.

Da quella frustrazione e' nato LINCE. Lo abbiamo costruito con il team di Risorse Artificiali partendo da un'idea semplice: se metti l'agente in una sandbox a livello kernel, non ha bisogno di chiedere permessi. Puo' lavorare libero, tu puoi concentrarti sulla verifica.

Poi abbiamo aggiunto l'orchestrazione multi-agente con una dashboard minimale (Rust/WASM, ~900KB), il supporto per qualsiasi agente via TOML, l'input vocale con Whisper locale. Tutto nel terminale.

Oggi lo rilasciamo open source, licenza MIT. Perche' un tool di sicurezza chiuso non ha senso.

lince.sh | github.com/RisorseArtificiali/lince

**Allegato consigliato**: Foto dal palco del Voxxed Day Ticino (se disponibile) oppure screenshot del repository GitHub con le prime stelle.

#OpenSource #LINCE #AIEngineering #DevTools #RisorseArtificiali

---

#### Alternativa 4B

Un paio di mesi fa ho parlato di sicurezza degli agenti AI al Voxxed Day Ticino. Quello che ho detto mi e' rimasto in testa, e a quanto pare non solo a me.

Usavo agenti AI per scrivere codice ogni giorno. E ogni giorno perdevo tempo in tre modi: approvando permessi che non leggevo piu', saltando tra finestre per seguire agenti diversi, e tenendo aperti programmi che non mi servivano davvero.

La reazione della community dopo la conferenza mi ha convinto che il problema non era solo mio.

Cosi' nelle settimane successive, con il team di Risorse Artificiali, abbiamo iniziato a costruire. La prima decisione e' stata: tutto nel terminale, sandbox a livello kernel, nessun compromesso. Da li' sono venute la dashboard in Rust/WASM per Zellij, il supporto multi-vendor (Claude Code, Codex, Gemini, OpenCode, Aider), VoxCode per l'input vocale con Whisper locale, la configurazione agenti via TOML.

Oggi lo rilasciamo con licenza MIT. Non e' perfetto, ma funziona. E con la community puo' diventare molto meglio.

lince.sh

**Allegato consigliato**: Carosello LinkedIn con 3-4 slide: il problema, la soluzione, la demo, il link al repo.

#OpenSource #LINCE #BuildInPublic #AIEngineering #DevCommunity

---

#### Alternativa 4C

Rilasciare un progetto open source fa sempre un po' paura.

Hai lavorato per settimane, sai tutti i limiti, conosci ogni workaround. E poi lo metti fuori e il mondo lo giudica per quello che e', non per quello che sara'.

LINCE e' un toolkit che trasforma il terminale in una workstation multi-agente. Sandbox a livello kernel per la modalita' YOLO (bubblewrap e nono, zero overhead). Dashboard Rust/WASM per orchestrare 3-5 agenti senza impazzire. Input vocale locale. Supporto per Claude Code, Codex, Gemini, OpenCode, Aider e agenti custom.

E' nato da un'idea che ho condiviso al Voxxed Day Ticino: la superficie d'attacco degli agenti AI non e' il software, sei tu. LINCE ti protegge mettendo tutto in sandbox, cosi' puoi lavorare in YOLO mode senza rischi.

Lo abbiamo costruito con il team di Risorse Artificiali. Da oggi e' su GitHub con licenza MIT.

Non e' perfetto. Ma e' reale, funziona, e ora e' vostro.

lince.sh | github.com/RisorseArtificiali/lince

**Allegato consigliato**: Video breve (60-90s) di walkthrough completo: avvio LINCE, lancio agenti in sandbox, dashboard, input vocale.

#OpenSource #LINCE #RisorseArtificiali #CodingAgents #AIEngineering

---

## Parte 2: Piani di Pubblicazione

### Legenda Angoli e Alternative
- **A1a/A1b/A1c** = Angolo 1 (Sandbox YOLO), Alternative A/B/C
- **A2a/A2b/A2c** = Angolo 2 (Context Switch Killer), Alternative A/B/C
- **A3a/A3b/A3c** = Angolo 3 (Terminal-Only), Alternative A/B/C
- **A4a/A4b/A4c** = Angolo 4 (Lancio Open Source), Alternative A/B/C

---

### Piano 1: Sprint 7 giorni, focus tecnico

Strategia: partire con l'angolo tecnico piu' forte (sandbox), costruire verso il lancio.

| Giorno | Piattaforma | Post | Razionale |
|--------|-------------|------|-----------|
| Lun | LinkedIn | A1a (Sandbox YOLO) | Apertura forte con il differenziante tecnico principale. Il lunedi' il pubblico tech e' attivo e ricettivo. |
| Mar | LinkedIn | A2a (Context Switch) | Consolidare con il secondo punto di forza. Chi ha visto il post di lunedi' approfondisce. |
| Mer | LinkedIn | A3a (Terminal-Only) | Meta' settimana, angolo piu' "lifestyle". Attira chi non ha reagito ai post tecnici. |
| Gio | LinkedIn | A4a (Lancio Open Source) | Storia personale dopo tre post tecnici. Crea connessione emotiva e contestualizza il progetto. |
| Ven | LinkedIn (commento) | Riepilogo settimana | Commento sul post di giovedi' con link a tutti i post precedenti e al repo. |
| Sab | - | Pausa | Nessuna pubblicazione. |
| Dom | LinkedIn | A1b (Sandbox, alt B) | Ripresa del tema piu' forte con angolo diverso. La domenica sera LinkedIn ha buon traffico. |

---

### Piano 2: Sprint 7 giorni, focus narrativo

Strategia: partire dalla storia personale, poi svelare le feature una alla volta.

| Giorno | Piattaforma | Post | Razionale |
|--------|-------------|------|-----------|
| Lun | LinkedIn | A4b (Lancio, alt B) | Apertura con la storia "un paio di mesi fa al Voxxed Day Ticino". Crea curiosita' e connessione. |
| Mar | LinkedIn | A1b (Sandbox YOLO, alt B) | Rivelare il cuore tecnico del progetto. Chi ha letto la storia vuole capire il "come". |
| Mer | - | Pausa | Dare tempo alla community di reagire e commentare. |
| Gio | LinkedIn | A2b (Context Switch, alt B) | Secondo pilastro tecnico. Angolo produttivita' per chi non e' interessato alla sicurezza. |
| Ven | LinkedIn | A3c (Terminal, VoxCode) | Chiusura settimana con la feature piu' "sorprendente" (input vocale su Linux). |
| Sab | - | Pausa | Nessuna pubblicazione. |
| Dom | LinkedIn | A4c (Lancio, alt C) | Chiusura con il post "ora e' vostro". Call to action per il weekend quando la gente ha tempo di provare. |

---

### Piano 3: Sprint 7 giorni, alta frequenza

Strategia: massima visibilita' con pubblicazione quasi quotidiana, alternando angoli.

| Giorno | Piattaforma | Post | Razionale |
|--------|-------------|------|-----------|
| Lun | LinkedIn | A4a (Lancio Open Source) | Annuncio ufficiale a inizio settimana. Massima visibilita'. |
| Mar | LinkedIn | A1a (Sandbox YOLO) | Feature principale il giorno dopo il lancio. Chi ha visto l'annuncio vuole dettagli. |
| Mer | LinkedIn | A2c (Context Switch, alt C) | Angolo "numeri" (sweet spot 3-5 agenti). Contenuto condivisibile. |
| Gio | LinkedIn | A3b (Terminal-Only, alt B) | Angolo provocatorio ("non apro un IDE da..."). Genera discussione nei commenti. |
| Ven | LinkedIn | A1c (Sandbox, alt C) | Ritorno sul tema sicurezza con angolo "approval fatigue". Venerdi' post piu' riflessivo. |
| Sab | LinkedIn | A3c (VoxCode/Linux) | Post di nicchia nel weekend per la community Linux. |
| Dom | LinkedIn | A2a (Context Switch, alt A) | Chiusura con tema produttivita'. Prepara la settimana successiva. |

---

### Piano 4: Campagna 14 giorni, a onde

Strategia: due settimane con intensita' crescente. Prima settimana semina, seconda settimana raccolto.

| Giorno | Piattaforma | Post | Razionale |
|--------|-------------|------|-----------|
| Lun (S1) | LinkedIn | A4a (Lancio Open Source) | Annuncio ufficiale. Tono personale per generare condivisioni. |
| Mar (S1) | - | Pausa | Lasciare che l'annuncio raccolga reazioni organiche. |
| Mer (S1) | LinkedIn | A1a (Sandbox YOLO) | Prima feature deep-dive. Chi ha messo like al lancio vuole sapere di piu'. |
| Gio (S1) | - | Pausa | Consolidamento. Rispondere ai commenti sui post precedenti. |
| Ven (S1) | LinkedIn | A2a (Context Switch) | Seconda feature. Chiusura della prima settimana con tema produttivita'. |
| Sab-Dom (S1) | - | Pausa | Weekend di riflessione. |
| Lun (S2) | LinkedIn | A3a (Terminal-Only) | Riapertura seconda settimana con angolo "filosofico" (solo terminale). |
| Mar (S2) | LinkedIn | A1b (Sandbox, alt B) | Ritorno sulla sicurezza con angolo fresco. Approfondimento per chi e' arrivato tardi. |
| Mer (S2) | - | Pausa | Rispondere ai commenti, interagire con la community. |
| Gio (S2) | LinkedIn | A2c (Context Switch, alt C) | Angolo numeri (sweet spot 3-5). Contenuto che invita alla discussione. |
| Ven (S2) | LinkedIn | A3c (VoxCode/Linux) | Feature di nicchia per il venerdi'. Attira una community specifica. |
| Sab (S2) | - | Pausa | Weekend. |
| Dom (S2) | LinkedIn | A4c (Lancio, alt C) | Chiusura campagna con "ora e' vostro". Call to action forte nel weekend. |
| Lun (S3) | LinkedIn (commento) | Riepilogo | Commento riepilogativo con metriche delle prime due settimane e ringraziamenti. |

---

### Piano 5: Campagna 14 giorni, tematica

Strategia: settimana 1 dedicata alla sicurezza, settimana 2 alla produttivita'. Due narrative distinte.

| Giorno | Piattaforma | Post | Razionale |
|--------|-------------|------|-----------|
| Lun (S1) | LinkedIn | A4a (Lancio Open Source) | Annuncio ufficiale con tutti i temi. Stabilisce il contesto. |
| Mar (S1) | LinkedIn | A1a (Sandbox YOLO) | Inizio settimana sicurezza. Il differenziante principale. |
| Mer (S1) | - | Pausa | Consolidamento tema sicurezza. |
| Gio (S1) | LinkedIn | A1b (Sandbox, alt B) | Approfondimento sicurezza con angolo "approval fatigue". |
| Ven (S1) | LinkedIn | A1c (Sandbox, alt C) | Terza variante sicurezza. "Il pattern piu' pericoloso..." |
| Sab-Dom (S1) | - | Pausa | Weekend. |
| Lun (S2) | LinkedIn | A2a (Context Switch) | Inizio settimana produttivita'. Transizione dal tema sicurezza. |
| Mar (S2) | LinkedIn | A3a (Terminal-Only) | Produttivita' attraverso la semplicita'. Solo terminale. |
| Mer (S2) | - | Pausa | Consolidamento. |
| Gio (S2) | LinkedIn | A2c (Context Switch, alt C) | Sweet spot 3-5 agenti. Contenuto data-driven. |
| Ven (S2) | LinkedIn | A3c (VoxCode/Linux) | Produttivita' vocale. Chiusura della narrativa produttivita'. |
| Sab (S2) | - | Pausa | Weekend. |
| Dom (S2) | LinkedIn | A4b (Lancio, alt B) | Chiusura con la storia personale. Retrospettiva a due settimane dal lancio. |

---

### Piano 6: Campagna 14 giorni, community-driven

Strategia: pubblicazioni distanziate per massimizzare l'interazione. Focus sulla costruzione della community.

| Giorno | Piattaforma | Post | Razionale |
|--------|-------------|------|-----------|
| Lun (S1) | LinkedIn | A4b (Lancio, alt B) | Apertura narrativa. "Un paio di mesi fa al Voxxed Day Ticino." Invita alla conversazione. |
| Mar (S1) | - | Interazione | Giornata dedicata a rispondere a ogni commento e condivisione. |
| Mer (S1) | LinkedIn | A1a (Sandbox YOLO) | Feature principale. Chiedere nei commenti: "Come gestite voi i permessi degli agenti?" |
| Gio-Ven (S1) | - | Interazione | Rispondere, ringraziare chi condivide, interagire con i profili rilevanti. |
| Sab (S1) | LinkedIn | A3b (Terminal, alt B) | Post weekend provocatorio ("non apro un IDE da..."). Genera dibattito. |
| Dom (S1) | - | Interazione | Alimentare la discussione nei commenti del sabato. |
| Lun (S2) | LinkedIn | A2b (Context Switch, alt B) | Ripresa con tema orchestrazione. Chiedere: "Quanti agenti usate in parallelo?" |
| Mar-Mer (S2) | - | Interazione | Community building. Condividere risposte interessanti. |
| Gio (S2) | LinkedIn | A3c (VoxCode/Linux) | Feature di nicchia. Taggare community Linux rilevanti. |
| Ven (S2) | - | Interazione | Consolidamento. |
| Sab (S2) | LinkedIn | A1c (Sandbox, alt C) | "Il pattern piu' pericoloso..." Post riflessivo per il weekend. |
| Dom (S2) | - | Interazione | Rispondere ai commenti finali. |
| Lun (S3) | LinkedIn | A4c (Lancio, alt C) | Chiusura: "ora e' vostro". Riepilogo con metriche della community (stelle GitHub, download, commenti ricevuti). |

---

## Note Operative

### Orari di Pubblicazione Consigliati
- **LinkedIn**: 8:00-9:00 oppure 17:30-18:30 (ora italiana). Il martedi', mercoledi' e giovedi' hanno il miglior engagement. Il lunedi' mattina e' forte per gli annunci.

### Risposta ai Commenti
- Rispondere entro 1 ora dalla pubblicazione per alimentare l'algoritmo.
- Fare domande di follow-up nei commenti per generare discussione.
- Ringraziare chi condivide con un commento personalizzato (non generico).

### Media Consigliati (Priorita')
1. **GIF della dashboard** con agenti attivi (massimo impatto visivo, basso costo di produzione)
2. **Screenshot a schermo intero** della workstation LINCE (facile da produrre, forte impatto)
3. **Video breve 30-60s** di demo (massimo impatto ma richiede piu' lavoro)
4. **Carosello 3-4 slide** per i post narrativi (buon engagement su LinkedIn)

### Metriche da Monitorare
- Impression e click-through sui post
- Stelle GitHub e fork dopo ogni pubblicazione
- Commenti qualitativi (domande tecniche = segnale positivo)
- Condivisioni da parte di profili con >1000 follower
