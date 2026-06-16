# GEMINI.md — Astronautisté (astronautiste.cz)

> Auto-načítáno Gemini CLI. Závazné pro generování kódu v tomto repu.
> Zdroj pravdy doktrín: `.aiad/policies/` (rejstřík `.aiad/policies/INDEX.md`).

## Stack
**Zola** (static site) + **Tailwind CSS `^3.4.17`** + **Flowbite `^2.5.2`** + Alpine.js.
Build: `scripts/build.sh`. Default jazyk odpovědí: **čeština**; code identifiers anglicky.

## STRICT doktrína — Flowbite v2 / Tailwind v3 (`.aiad/policies/flowbite-stack.policy.md`)

Projekt je Flowbite **v2** / Tailwind **v3** (JS config):
- ✅ `tailwind.config.js` · `darkMode: 'class'` · `require('flowbite/plugin')` ·
  `@tailwind base; @tailwind components; @tailwind utilities;`
- ✅ interaktivita přes data-attributes (`data-collapse-toggle` …) + a11y
  (`aria-controls`, `aria-expanded`, `aria-hidden`, `sr-only`); web je **dark-only** (`<html class="dark">`)
- ❌ **NEPOUŽÍVEJ** Tailwind-v4 / Flowbite-v4 CSS-first syntax:
  `@custom-variant`, `@plugin "flowbite"`, `@import "tailwindcss"`, `@theme {}`
  — pre-commit **Gate 5 to blokne** (`.githooks/pre-commit`).

⚠️ `flowbite.com` `llms.txt` / `llms-full.txt` jsou už pro **v4** → **neaplikuj je sem**.

## Brand
Kanonický tagline: „Myslíme na hvězdy, jednáme vědecky." · značka vždy **Astronautisté** /
doména **astronautiste.cz** (ne „austronautiste"). Brand voice: `messaging/`.
