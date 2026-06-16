# Policy: Flowbite/Tailwind Stack Doctrine

> 🇨🇿 Závazná doktrína pro jakoukoli AI/člověka pracující v tomto repu.
> EN technical body. Enforced automaticky přes `.githooks/pre-commit` (Gate 5).
> **Level: STRICT** — porušení ve zdrojových souborech blokuje commit.

| | |
|---|---|
| **ID** | `flowbite-stack` |
| **Scope** | celý repo (build source: CSS, JS, config, HTML templaty) |
| **Enforcement** | `.githooks/pre-commit` Gate 5 (block + advisory warn) |
| **Owner** | brand/site maintainer |
| **Last verified** | 2026-06-16 |

## Rationale (CZ)

Web `astronautiste.cz` běží na **Flowbite `^2.5.2` + Tailwind CSS `^3.4.17`** (JS config:
`tailwind.config.js`). Živá `flowbite.com` dokumentace a její `llms.txt` / `llms-full.txt`
jsou ale už pro **Flowbite v4 + Tailwind v4** (CSS-first config). Když AI nakrmíš aktuální
Flowbite LLM rules, vygeneruje v4/Tailwind-v4 syntax, která **rozbije náš build**.
Tato doktrína drží generovaný kód na naší verzi.

Zdroj: https://flowbite.com/docs/getting-started/llm/ ·
`llms.txt`: https://raw.githubusercontent.com/themesberg/flowbite/refs/heads/main/llms.txt

## MUST (v2 / Tailwind v3)

- Tailwind config v `tailwind.config.js`: `darkMode: 'class'`,
  `content` glob obsahuje `./node_modules/flowbite/**/*.js`,
  `plugins: [require('flowbite/plugin')]`.
- CSS entry (`styles/input.css`): `@tailwind base; @tailwind components; @tailwind utilities;`.
- JS: UMD `flowbite.min.js` (vendorováno `scripts/build.sh` z `node_modules`), načtené
  v `templates/base.html` s `defer` → v2 auto-inituje data-attribute komponenty na
  `DOMContentLoaded`. Po dynamické změně DOM volej `initFlowbite()`.
- Interaktivita přes **data-attributes**: `data-collapse-toggle`, `data-dropdown-toggle`,
  `data-modal-target/-toggle`, `data-drawer-*`, `data-accordion` …
- A11y (povinné): `aria-controls` + `aria-expanded` na toggle,
  `aria-hidden="true"` na dekorativní SVG, `sr-only` text na icon-only buttonech.
- Dark mode: web je **dark-only** → `<html class="dark">`, žádný theme toggle /
  `localStorage('color-theme')`. Flowbite v2 dark variant funguje přes plugin.

## MUST NOT (Tailwind v4 / Flowbite v4 — rozbije build)

Tyto vzory jsou ve zdroji **zakázané** (pre-commit je blokne):

- `@custom-variant dark (...)`   ← v4 dark mode (my používáme `darkMode: 'class'`)
- `@plugin "flowbite"` / `@plugin 'flowbite'`   ← v4 CSS-first plugin
- `@import "tailwindcss"`   ← v4 entry (my používáme `@tailwind base/components/utilities`)
- `@theme { ... }`   ← v4 theme config (my používáme `theme.extend` v `tailwind.config.js`)

## Upgrade na v4 (vědomé rozhodnutí, ne omylem)

Bump `flowbite` na `^3`/`^4` nebo `tailwindcss` na `^4` je **breaking** (CSS-first config,
`@custom-variant`, `@plugin`, odstranění `tailwind.config.js`). Pre-commit na to **WARN**.
Pokud se k upgradu rozhodneš: udělej ho jako samostatný PR, přepiš tuto policy i všechny
per-tool rules a aktualizuj `.githooks/pre-commit` Gate 5.

## Související doktríny

- CZE — Czech-Language Excellence (viz globální `~/.claude/CLAUDE.md`, pilíř #19).
- Brand voice — `messaging/ASTRONAUTISTE_MESSAGING_FRAMEWORK.md`.
- Brand tagline (kanonický): „Myslíme na hvězdy, jednáme vědecky."
