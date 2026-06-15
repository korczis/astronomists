# Agent Registry — Astronomists

> Trimmed registry. Injected via `/inject` (Core bootstrap) from Prismatic Platform AIAD.
> Full platform registry (552 agents) was **not** injected — only universal core agents.

## Injected agents

| Agent | Spec | Roles | Účel |
|---|---|---|---|
| `commit-coordinator` | [`.aiad/agents/commit-coordinator.agent.md`](../.aiad/agents/commit-coordinator.agent.md) | git, commit, coordination | Conventional commits + co-author footer, koordinace commit workflow |
| `session-context-synthesizer` | [`.aiad/agents/session-context-synthesizer.agent.md`](../.aiad/agents/session-context-synthesizer.agent.md) | session-context, synthesis, documentation | Syntéza session kontextu do `.claude/session-context/` |

## Protocols

Viz [`.claude/protocols/`](protocols/):

- `CONTEXT-MANAGEMENT-PROTOCOL.md`
- `claim-verification.protocol.md`
- `AGENT-CREATION-PROTOCOL.md`
- `crisis-response-protocols.md`

## Rozšíření

Další agenty lze doinjektovat ze zdroje:

```bash
/inject /Users/korczis/dev/astronomists --components agents --scope standard
```

---

**Injected:** 2026-06-15 · **Strategy:** preserve · **Source:** prismatic-platform
