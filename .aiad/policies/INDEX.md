# AIAD Policies — rejstřík doktrín

> Zdroj pravdy pro doktríny vynucované napříč všemi AI nástroji (Claude Code, Codex/AGENTS,
> Gemini CLI, Zed) i člověkem. Per-tool rules soubory (CLAUDE.md, AGENTS.md, GEMINI.md,
> `.rules`) na tyto policy **odkazují**, neduplikují je. Mechanické vynucení: `.githooks/pre-commit`.

| Policy | ID | Enforcement | Stav |
|---|---|---|---|
| [Flowbite/Tailwind Stack](flowbite-stack.policy.md) | `flowbite-stack` | pre-commit Gate 5 (block + warn) | STRICT |

## Další (zatím nekodifikované jako samostatný soubor, ale platné)

- **CZE — Czech-Language Excellence**: čeština bez strojových překlepů; viz globální
  `~/.claude/CLAUDE.md` a pre-commit Gate 2 (advisory).
- **Brand voice & tagline**: `messaging/`, kanonický tagline „Myslíme na hvězdy, jednáme vědecky."
- **No secrets / metadata hygiene / merge markers**: pre-commit Gate 1/3/4.

## Jak přidat novou doktrínu

1. Vytvoř `*.policy.md` zde (formát viz `flowbite-stack.policy.md`).
2. Přidej řádek do tabulky výše.
3. Pokud má být mechanicky vynucená, přidej Gate do `.githooks/pre-commit`.
4. Doplň krátký pointer do `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.rules` a `README.md`.
