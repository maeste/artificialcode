# Campaign: lince-sandbox-3levels-en-v2

Reworded LinkedIn EN post after Buffer duplicate detection on the original.

## Post #1 — LinkedIn EN (reworded)
- channel: li_maeste
- date: 2026-05-06T14:00:00Z
- media: social/media/lince-sandbox-3levels.png

There's a difference between a sandbox and a wrapper: if the agent can read your API key from env and dial any host on the internet, you're running a wrapper.

LINCE just shipped a three-level sandbox model, paranoid / normal / permissive, across every agent we support: Claude Code, Codex, Gemini, OpenCode, Pi.

Two design decisions worth calling out, both from paranoid mode:

1. Kernel-enforced network isolation.
On Linux/bwrap, paranoid runs the agent inside a fresh network namespace (--unshare-net). The agent has its own loopback and no routes to anywhere, connect() to attacker.com is rejected by the kernel because there is no path to attacker.com. Not iptables-from-userspace. Not a userland wrapper the agent can shell out of.
On macOS/nono, the equivalent is Landlock LSM hooks on connect/bind plus the nono credential proxy.

2. The API key never enters the agent's process.
A credential proxy runs outside the sandbox and holds the key. The agent talks to it over a unix socket that's bind-mounted into the sandbox, and an in-sandbox socat bridge presents that socket as plain TCP localhost so any SDK that uses *_BASE_URL "just works." The proxy injects the auth header on the host side and forwards to the upstream API over HTTPS. It enforces an explicit host allowlist; anything off-list gets a 403. Cloud metadata endpoints (169.254.169.254 and friends) are blocked, no SSRF to your IAM role.

The combined effect: a prompt-injected agent in paranoid can't exfiltrate the key (it's not in the env, not in /proc/<pid>/environ, not in any tool the agent spawns) and can't make arbitrary outbound calls (the kernel won't route them and the proxy won't forward them). It can only do what it was hired to do, code, in your project directory.

Normal and permissive trade isolation for ergonomics, with the choice made explicit at install time, per agent.

Changelog: https://lince.sh/changelog/#2026-05-05
Security model + credential proxy details: https://lince.sh/documentation/sandbox/security-model

What's your team's threat model for agentic coding, sandboxing, wrapping, or trusting?

#AgenticCoding #AIAgents #SecurityEngineering #Sandbox #DevSecOps
