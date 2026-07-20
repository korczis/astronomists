# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> 🇨🇿 CZ rationale + EN technical body. Originally injected from Prismatic Platform AIAD
> (`/inject`, Core bootstrap) — 2026-06-15; corrected 2026-07-20 (build pipeline now exists).

## Project type

**Static site** for the Astronautisté brand (`astronautiste.cz`): **Zola** + **Tailwind CSS
`^3.4.17`** + **Flowbite `^2.5.2`** + **Alpine.js** + **p5.js**, tested with **Playwright**.
Content is brand mythology, pillars, campaign copy, and audience pages, rendered through Zola
templates. (Older docs in this repo call it a "docs-only, no build pipeline" repo — that was
true historically but is no longer accurate; treat `package.json`/`scripts/` as authoritative.)

Deploys to **astronautiste.cz** via `gh-pages` (built by CI, not the raw repo docs). `master`
and `gh-pages` are separate branches — `gh-pages` is force-orphan-published by
`.github/workflows/deploy.yml` on push to `master`, never edited directly.

## Commands

```bash
npm install                 # JS deps (also requires the `zola` binary on PATH, not npm-managed)
git config core.hooksPath .githooks   # activate portable pre-commit doctrine gate (once)

bash scripts/serve.sh       # npm run serve|dev — zola serve + Tailwind watch, http://127.0.0.1:1111
bash scripts/build.sh       # npm run build — Tailwind → vendor JS → zola build → zola check
bash scripts/check.sh       # post-build sanity gate (required outputs, no unrendered Tera, key copy present)
bash scripts/check-doctrines.sh   # CI mirror of pre-commit Gate 5, scans the whole tracked tree

npm run test:e2e             # Playwright against a full local build (webServer builds to public-test)
npx playwright test tests/kampan.spec.ts        # single spec file
npx playwright test -g "some test name"         # single test by name
npm run test:e2e:mobile      # mobile-chrome project only
npm run test:e2e:live        # tests-live/ against the deployed site (LIVE_URL to override)
```

`BASE_URL` and `OUTPUT_DIR` env vars override `scripts/build.sh`'s Zola base URL / output dir
(used for local preview builds and Playwright's `public-test` output). Never deploy with a
dirty working tree or a failing `zola check` — use the `/deploy` skill rather than pushing to
`master` manually; it gates on both.

## Architecture

- **Content → template flow (Zola):** each `content/<section>/_index.md` defines a section
  (nav item); individual pages set `template = "..."` in TOML front matter to pick one of
  `templates/{index,hub,detail,page,section,social-kit,carousel-bg}.html`. Page-specific copy
  lives under `[extra]` front matter (`eyebrow`, `lead`, `image`, `og_image`, `illustration`,
  `illustration_alt`, `anchor`, ...) and is pulled into templates via Tera — check an existing
  page in the same section (e.g. `content/proc/*.md`) before adding a new one, front matter
  shape isn't identical across sections.
- **Sections map 1:1 to site IA:** `proc/` (pillars), `pro-koho/` (audiences: rodiče/studenti/
  učitelé/vědci), `kampan/` (25 numbered campaign pieces), `manifest/`, `motivy/`, `pridej-se/`,
  `docs/`, `brand/`.
- **`templates/base.html`** is the shared shell: `<html class="dark">` (site is dark-only, no
  light mode), includes `partials/{head,nav,footer}.html`, then loads vendored JS in a fixed
  order that matters — p5 → `starfield.js` → alpine-intersect → alpine → `enhance.js` →
  flowbite, all `defer`, no external CDN.
- **`static/js/`** mixes vendored and hand-written files: `flowbite.min.js`, `p5.min.js`,
  `alpine.min.js`, `alpine-intersect.min.js` are copied from `node_modules` by
  `build.sh`/`serve.sh` (gitignored, don't hand-edit) — `starfield.js` (p5 hero backdrop,
  respects `prefers-reduced-motion`) and `enhance.js` (progressive-enhancement fallback if
  Alpine fails to load) are hand-written source, tracked in git.
- **Doctrine enforcement is duplicated by design:** `.aiad/policies/` (index `INDEX.md`) is the
  single source of truth for cross-tool rules; `CLAUDE.md`/`AGENTS.md`/`GEMINI.md`/`.rules`
  each point at it rather than restating it. It's mechanically enforced twice — locally via
  `.githooks/pre-commit` Gate 5 (staged-diff scan) and in CI via `scripts/check-doctrines.sh`
  (full tracked-tree scan, invoked from `deploy.yml`). The two carry the same "V4 syntax"
  regex independently — keep them in sync if you touch either.
- **Brand source of truth lives outside `content/`:** design tokens in
  `design-system/astronautiste-design-system.json` (mirrored into `tailwind.config.js`), brand
  voice in `messaging/ASTRONAUTISTE_MESSAGING_FRAMEWORK.md`, mythology/pillars in
  `brand-book/`. Copy changes in `content/` should stay consistent with these, not just
  internally consistent with themselves.

## Design tokens (quick reference)

| Token | Hex | Use |
|---|---|---|
| Void Black | `#0a0a0a` | primary background |
| Presence White | `#f8f8f8` | typography, content |
| Signal Red | `#e63946` | emphasis, action |
| Prague Gold | `#d4a574` | warmth accent (dark surfaces only) |
| Space Blue | `#1d3557` | depth, credibility |
| Growth Green | `#06a77d` | positive outcome |

Fonts: `Inter` (sans), `Georgia` (serif). Full token set:
`design-system/astronautiste-design-system.json`.

## Communication style

- Direct, concise, technical. Žádné zbytečné zdvořilosti.
- **Default jazyk odpovědí: čeština (cs-CZ)**; mirror the user.
- **Vždy English**: code identifiers, conventional commit prefixes
  (`feat:`/`fix:`/`docs:`/`chore:`/`refactor:`), package names, log tokens.
- Brand tagline a copy zůstávají v originále (CZ): *„Myslíme na hvězdy, jednáme vědecky."*

## Stack & enforced doctrines (MANDATORY)

- **Flowbite/Tailwind stack** (STRICT — `.aiad/policies/flowbite-stack.policy.md`): project is
  Flowbite **v2** / Tailwind **v3** (`tailwind.config.js`, `darkMode:'class'`,
  `require('flowbite/plugin')`, `@tailwind base/components/utilities`). **DO NOT** use
  Tailwind-v4 / Flowbite-v4 CSS-first syntax (`@custom-variant`, `@plugin "flowbite"`,
  `@import "tailwindcss"`, `@theme {}`) — pre-commit **Gate 5 blocks this**. Note:
  `flowbite.com`'s `llms.txt`/`llms-full.txt` are already v4 — **do not apply them here**.
  Interactivity via data-attributes (`data-collapse-toggle`, ...) + a11y attributes
  (`aria-controls`, `aria-expanded`, `aria-hidden`, `sr-only`).
- Other gates: Apple metadata hygiene (block), CZE language tells (advisory), secrets (block),
  unresolved merge markers (block).

## Protocols (`.claude/protocols/`)

Injected mandatory protocols — apply where relevant to this repo's docs/site work:

- `CONTEXT-MANAGEMENT-PROTOCOL.md` — context and session-context management.
- `claim-verification.protocol.md` — verify claims, don't state unsupported facts.
- `AGENT-CREATION-PROTOCOL.md` — standard for creating agents.
- `crisis-response-protocols.md` — relevant to brand crisis messaging.

## Agents (`.aiad/agents/`)

- `commit-coordinator` — commit coordination (conventional format + co-author footer).
- `session-context-synthesizer` — synthesizes session context into `.claude/session-context/`.

Catalog: `.claude/AGENT_REGISTRY.md`.

## Git workflow

- Conventional commits: `type(scope): description` + Claude co-author footer.
- Branches: `feature/`, `fix/`, `refactor/` prefixes.
- Never `--no-verify`; after a hook failure, create a NEW commit (don't amend).
- `git config core.hooksPath .githooks` activates the portable pre-commit hook.
- Pushing to `master` triggers production deploy (see Architecture above) — prefer the
  `/deploy` skill over a manual push.

---

**Originally injected by:** `/inject` (aiad-injection-coordinator) · Prismatic Platform AIAD
**Scope:** Core bootstrap · **Strategy:** preserve · **Date:** 2026-06-15
