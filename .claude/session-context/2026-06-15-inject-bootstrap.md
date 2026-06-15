# 2026-06-15 — AIAD inject bootstrap + gh-pages deploy

## Co se dělalo

1. **GitHub Pages deploy** — brand package publikován jako Jekyll site na větvi
   `gh-pages`, live na https://korczis.github.io/astronomists/. On-brand layout
   (Void Black / Prague Gold / Signal Red, Inter), render přes GH Pages supported
   pluginy (optional-front-matter, default-layout, titles-from-headings, relative-links).
2. **`/inject` Core bootstrap** — z Prismatic Platform AIAD injektována core
   infrastruktura (strategie `preserve`):
   - `CLAUDE.md` (tailored pro docs/brand repo)
   - `.aiad/manifest.toml` + 2 agenti (commit-coordinator, session-context-synthesizer)
   - `.claude/protocols/` (4× verbatim), `.claude/AGENT_REGISTRY.md` (trimmed)
   - `.githooks/pre-commit` (portable, bez mix — docs gates)
   - `.claude/session-context/` (tento starter)

## Klíčová rozhodnutí

- **Core bootstrap, ne full mirror** — zdroj má 552 agentů / 11 GB `.claude`; injektován
  jen univerzální core.
- **pre-commit přegenerován jako portable** — originál vázaný na `mix check.precommit`
  a `apps/prismatic_osint_core/...`, v docs repu by padal.
- **Pages publikuje jen brand-facing dirs** — `injection-config/`, reporty, backupy vyřazeny.

## Co zbývá / možná navázat

- Aktivovat hook: `git config core.hooksPath .githooks`.
- Commitnout inject artefakty na master (zatím untracked).
- Volitelně: Standard AIAD scope (víc agentů/commands/workflows).
