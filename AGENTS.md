# AGENTS.md — Astronomists (Astronautisté Brand)

> 🇨🇿 Konfigurace projektu pro práci s Codex. CZ rationale + EN technical body.
> Injektováno z Prismatic Platform AIAD (`/inject`, Core bootstrap) — 2026-06-15.

## Project type

**Docs / brand package** — žádný build language (no `mix.exs`/`package.json`/`Cargo.toml`).
Obsah: brand mytologie, vizuální design systém, messaging framework. Publikováno jako
GitHub Pages site (větev `gh-pages`, https://korczis.github.io/astronomists/).

Toto **není** code repo — neexistuje `mix`/`npm`/`cargo` pipeline. Quality gates jsou
dokumentační (links, language, metadata hygiene), ne kompilace/testy.

## Communication style

- Direct, concise, technical. Žádné zbytečné zdvořilosti.
- **Default jazyk odpovědí: čeština (cs-CZ)**; mirror the user.
- **Vždy English**: code identifiers, conventional commit prefixes
  (`feat:`/`fix:`/`docs:`/`chore:`/`refactor:`), package names, log tokens.
- Brand tagline a copy zůstávají v originále (CZ): *„Myslíme na hvězdy, jednáme vědecky."*

## Repository layout

```
astronomists/
├── brand-book/       # mytologie, pilíře, narativní architektura
├── design-system/    # barvy, typografie, komponenty, accessibility, design tokens (JSON)
├── messaging/        # tone of voice, copy templates, playbook
├── motifs/           # vizuální motivy
├── assets/           # asset inventory
├── injection-config/ # interní deployment dokumentace (NEpublikuje se na Pages)
├── .aiad/            # AIAD infrastruktura (agents, manifest)
├── .claude/          # protocols, session-context, agent registry
└── .githooks/        # portable pre-commit (docs quality gates)
```

## Design tokens (zdroj pravdy)

`design-system/astronautiste-design-system.json`. Klíčová paleta:

| Token | Hex | Použití |
|---|---|---|
| Void Black | `#0a0a0a` | primární pozadí |
| Presence White | `#f8f8f8` | typografie, content |
| Signal Red | `#e63946` | emphasis, action |
| Prague Gold | `#d4a574` | warmth accent (jen na tmavém) |
| Space Blue | `#1d3557` | depth, credibility |
| Growth Green | `#06a77d` | positive outcome |

Fonty: `Inter` (sans), `Georgia` (serif).

## Working agreements

- **Read before edit.** U markdownu zachovávej existující strukturu nadpisů a hustotu.
- **Brand voice je závazný** — viz `messaging/ASTRONAUTISTE_MESSAGING_FRAMEWORK.md`.
- **Žádné secrets v repu.** Public repo (`korczis/astronomists`).
- **GitHub Pages:** site se staví z větve `gh-pages` (root). Master a gh-pages jsou
  oddělené; obsah na Pages se synchronizuje vědomě, ne automaticky z master.

## Stack & enforced doctrines (MANDATORY)

Web `astronautiste.cz`: **Zola** (static site) + **Tailwind CSS `^3.4.17`** + **Flowbite `^2.5.2`** + Alpine.js.
Build: `scripts/build.sh` (Tailwind → vendor JS → `zola build` → `zola check`).
(Pozn.: „není code repo" výše je historické — site build dnes existuje.)

Doktríny jsou **automaticky vynucené** přes `.githooks/pre-commit` (`git config core.hooksPath .githooks`).
Zdroj pravdy: **`.aiad/policies/`** (rejstřík `.aiad/policies/INDEX.md`). Tento soubor jen odkazuje.

- **Flowbite/Tailwind stack** (STRICT — `.aiad/policies/flowbite-stack.policy.md`):
  projekt je Flowbite **v2** / Tailwind **v3** (`tailwind.config.js`, `darkMode:'class'`,
  `require('flowbite/plugin')`, `@tailwind base/components/utilities`). **NEPOUŽÍVEJ**
  Tailwind-v4 / Flowbite-v4 CSS-first syntax (`@custom-variant`, `@plugin "flowbite"`,
  `@import "tailwindcss"`, `@theme {}`) — pre-commit **Gate 5 to blokne**.
  `flowbite.com` `llms.txt` je už v4 → **neaplikovat sem**. Web je **dark-only**.
- Další gaty: metadata hygiene, CZE jazyk (advisory), secrets, merge markery.

## Protocols (`.claude/protocols/`)

Injektované mandatorní protokoly — aplikuj relevantně k docs práci:

- `CONTEXT-MANAGEMENT-PROTOCOL.md` — správa kontextu a session-context.
- `claim-verification.protocol.md` — ověřuj tvrzení, neuváděj nepodložená fakta.
- `AGENT-CREATION-PROTOCOL.md` — standard pro tvorbu agentů.
- `crisis-response-protocols.md` — relevantní k brand crisis messaging.

## Agents (`.aiad/agents/`)

- `commit-coordinator` — koordinace commitů (conventional format + co-author footer).
- `session-context-synthesizer` — syntéza session kontextu do `.claude/session-context/`.

Katalog: `.claude/AGENT_REGISTRY.md`.

## Git workflow

- Conventional commits: `type(scope): description` + Codex co-author footer.
- Branches: `feature/`, `fix/`, `refactor/` prefixy.
- Nikdy `--no-verify`; po selhání hooku vytvoř NOVÝ commit (neamenduj).
- `git config core.hooksPath .githooks` aktivuje portable pre-commit.

---

**Injected by:** `/inject` (aiad-injection-coordinator) · Prismatic Platform AIAD
**Scope:** Core bootstrap · **Strategy:** preserve · **Date:** 2026-06-15
