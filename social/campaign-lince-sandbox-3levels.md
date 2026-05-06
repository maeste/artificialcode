# Campaign: lince-sandbox-3levels

Three-level sandbox model rollout (paranoid / normal / permissive) across all supported agents in LINCE. LinkedIn IT + LinkedIn EN + X/Twitter EN.

## Post #1 — LinkedIn IT
- channel: li_maeste
- date: 2026-05-06T12:00:00Z
- media: social/media/lince-sandbox-3levels.png

Se il tuo agent di coding AI ha la tua API key nelle env vars e accesso di rete senza vincoli, non hai una sandbox. Hai un wrapper.

LINCE ha appena rilasciato un modello sandbox a tre livelli, paranoid / normal / permissive, su tutti gli agent supportati: Claude Code, Codex, Gemini, OpenCode, Pi.

Due scelte di design vale la pena evidenziare, entrambe in modalità paranoid:

1. Isolamento di rete imposto nel kernel.
Su Linux/bwrap, paranoid esegue l'agent dentro un network namespace fresco (--unshare-net). L'agent ha solo il proprio loopback e nessuna route verso l'esterno, la connect() verso attacker.com viene rifiutata dal kernel perché non esiste alcun percorso verso attacker.com. Niente iptables in userspace. Niente wrapper da cui l'agent possa scappare con una shell.
Su macOS/nono, l'equivalente sono gli hook LSM di Landlock su connect/bind più il credential proxy di nono.

2. L'agent non vede mai la tua API key.
Un credential proxy gira fuori dalla sandbox e custodisce la chiave. L'agent ci parla tramite uno unix socket bind-mountato dentro la sandbox, e un bridge socat interno presenta quel socket come localhost TCP, così qualunque SDK che usa *_BASE_URL funziona out-of-the-box. Il proxy inietta l'header di autenticazione lato host e inoltra verso l'API upstream in HTTPS. Applica un'allowlist esplicita di host; tutto ciò che è fuori lista riceve 403. Gli endpoint metadata cloud (169.254.169.254 e simili) sono bloccati, niente SSRF verso il tuo ruolo IAM.

Effetto combinato: un agent con prompt injection in paranoid non può esfiltrare la chiave (non c'è nell'env, non in /proc/<pid>/environ, non in nessun tool che spawna) e non può fare chiamate uscenti arbitrarie (il kernel non le instrada e il proxy non le inoltra). Può fare solo ciò per cui è stato ingaggiato, scrivere codice, nella tua project directory.

Normal e permissive scambiano isolamento per ergonomia, con la scelta esplicita a install time, per agent.

Changelog: https://lince.sh/changelog/#2026-05-05
Security model + dettagli credential proxy: https://lince.sh/documentation/sandbox/security-model

Qual è il threat model del tuo team per l'agentic coding, sandbox, wrapper, o fiducia?

#AgenticCoding #AIAgents #SecurityEngineering #Sandbox #DevSecOps

## Post #2 — LinkedIn EN
- channel: li_maeste
- date: 2026-05-06T14:00:00Z
- media: social/media/lince-sandbox-3levels.png

If your AI coding agent has your API key in its env vars and unrestricted outbound network, you don't have a sandbox. You have a wrapper.

LINCE just shipped a three-level sandbox model, paranoid / normal / permissive, across every agent we support: Claude Code, Codex, Gemini, OpenCode, Pi.

Two design decisions worth calling out, both from paranoid mode:

1. Network isolation enforced in the kernel.
On Linux/bwrap, paranoid runs the agent inside a fresh network namespace (--unshare-net). The agent has its own loopback and no routes to anywhere, connect() to attacker.com is rejected by the kernel because there is no path to attacker.com. Not iptables-from-userspace. Not a userland wrapper the agent can shell out of.
On macOS/nono, the equivalent is Landlock LSM hooks on connect/bind plus the nono credential proxy.

2. The agent never sees your API key.
A credential proxy runs outside the sandbox and holds the key. The agent talks to it over a unix socket that's bind-mounted into the sandbox, and an in-sandbox socat bridge presents that socket as plain TCP localhost so any SDK that uses *_BASE_URL "just works." The proxy injects the auth header on the host side and forwards to the upstream API over HTTPS. It enforces an explicit host allowlist; anything off-list gets a 403. Cloud metadata endpoints (169.254.169.254 and friends) are blocked, no SSRF to your IAM role.

The combined effect: a prompt-injected agent in paranoid can't exfiltrate the key (it's not in the env, not in /proc/<pid>/environ, not in any tool the agent spawns) and can't make arbitrary outbound calls (the kernel won't route them and the proxy won't forward them). It can only do what it was hired to do, code, in your project directory.

Normal and permissive trade isolation for ergonomics, with the choice made explicit at install time, per agent.

Changelog: https://lince.sh/changelog/#2026-05-05
Security model + credential proxy details: https://lince.sh/documentation/sandbox/security-model

What's your team's threat model for agentic coding, sandboxing, wrapping, or trusting?

#AgenticCoding #AIAgents #SecurityEngineering #Sandbox #DevSecOps

## Post #3 — Twitter EN
- channel: x_maeste
- date: 2026-05-06T14:00:00Z
- media: social/media/lince-sandbox-3levels.png

API key in env + open network = wrapper, not sandbox.

LINCE paranoid: Linux netns isolation (--unshare-net) + credential proxy holds the key over a unix socket.

https://lince.sh/changelog
