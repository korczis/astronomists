# Astronautisté

Brand & web pro hnutí **Astronautisté** — „Myslíme na hvězdy, jednáme vědecky."
Veřejný web: **[astronautiste.cz](https://astronautiste.cz)**.

## Stack

**Zola** (static site generator) + **Tailwind CSS `^3.4.17`** + **Flowbite `^2.5.2`** + **Alpine.js** + Playwright (E2E).

```bash
bash scripts/build.sh      # Tailwind CSS → vendor JS → zola build → zola check
```

Build z větve `gh-pages` přes CI. Repozitář layout viz [`AGENTS.md`](AGENTS.md).

## AI tooling & vynucené doktríny

Tento repo je řízen **doktrínami**, které se vynucují **automaticky a vždy** napříč všemi
AI nástroji i člověkem. Jeden zdroj pravdy, mechanická brána, per-tool ukazatele.

### Zdroj pravdy
- **[`.aiad/policies/`](.aiad/policies/INDEX.md)** — kanonické policy (AIAD). Rejstřík: `INDEX.md`.

### Per-tool konfigurace (každý nástroj si načítá svůj soubor)

| Nástroj | Soubor | Načítání |
|---|---|---|
| **Claude Code** (Anthropic) | [`CLAUDE.md`](CLAUDE.md) | auto |
| **OpenAI Codex** / obecné agenty | [`AGENTS.md`](AGENTS.md) | auto (`AGENTS.md` konvence) |
| **Gemini CLI** (Google) | [`GEMINI.md`](GEMINI.md) | auto |
| **Zed editor** | [`.rules`](.rules) | auto |
| Všichni / člověk | [`README.md`](README.md) + `.aiad/policies/` | — |

Per-tool soubory na policy **odkazují**, neduplikují text → žádný drift.

### Mechanické vynucení (skutečné „always enforced")
Git **pre-commit** brána — [`.githooks/pre-commit`](.githooks/pre-commit). Aktivace (jednou):

```bash
git config core.hooksPath .githooks
```

Gaty: metadata hygiene · CZE jazyk (advisory) · secrets · merge markery ·
**Gate 5: Flowbite/Tailwind stack** (block + advisory warn).

### Klíčová doktrína — Flowbite v2 / Tailwind v3 (STRICT)
Projekt je **Flowbite `v2` / Tailwind `v3`** (JS config). Generovaný kód **MUSÍ** používat
`tailwind.config.js` (`darkMode:'class'`, `require('flowbite/plugin')`,
`@tailwind base/components/utilities`) a **NESMÍ** používat Tailwind-v4 / Flowbite-v4
CSS-first syntax (`@custom-variant`, `@plugin "flowbite"`, `@import "tailwindcss"`, `@theme {}`).

> ⚠️ `flowbite.com` `llms.txt` / `llms-full.txt` jsou už pro **v4** → **neaplikovat sem.**

Detail: [`.aiad/policies/flowbite-stack.policy.md`](.aiad/policies/flowbite-stack.policy.md).

## Licence / kontakt
Public repo `korczis/astronomists`. Kontakt přes web.
