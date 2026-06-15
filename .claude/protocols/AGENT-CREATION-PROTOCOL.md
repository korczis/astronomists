# Agent Creation Protocol

**Version**: 1.0.0
**Created**: 2025-11-09
**Classification**: AIES (AI Ecosystem) Standard Protocol
**Authority**: PLATFORM-WIDE - All AI Tools

---

## Overview

This protocol defines the standardized 7-phase methodology for creating new agents in the Prismatic Platform ecosystem. Based on successful ARCHER SUPREME missions demonstrating revolutionary agent development patterns.

**Success Rate**: 100% (Code Reconnaissance Specialist, Regression Prevention System)
**Expected Benefits**: 50% faster agent creation, seamless integration, zero disruption

---

## Prerequisites

Before starting agent creation:
- [ ] Load latest session context from `.claude/session-context/`
- [ ] Review existing agents in `.claude/AGENT_REGISTRY.md`
- [ ] Analyze platform pain points and capability gaps
- [ ] Verify user requirements are clear and actionable

---

## Phase 1: Requirement Clarification

**Duration**: 10-20 minutes
**Goal**: Crystal-clear understanding of agent requirements

### Checklist

- [ ] **Gather User Requirements**: Document initial agent concept
- [ ] **Identify Domain and Scope**: Determine tactical/strategic/supreme classification
- [ ] **Clarify Integration Points**: MCP protocol, quality gates, command registry
- [ ] **Define Success Criteria**: Measurable outcomes and validation metrics
- [ ] **Iterate Until Clear**: Ask clarifying questions until zero ambiguity

### Questions to Answer

1. What specific problem does this agent solve?
2. Which domain does it belong to? (LLM, OSINT, Quality, Infrastructure, etc.)
3. What authority level does it need? (Tactical, Strategic, Supreme)
4. How does it integrate with existing systems?
5. What are the expected benefits and impact?

### Output

- **Agent Concept Document**: Clear description of agent purpose and capabilities
- **Integration Requirements**: List of systems and protocols needed
- **Success Metrics**: Quantifiable outcomes

---

## Phase 2: Platform Analysis

**Duration**: 15-30 minutes
**Goal**: Understand current platform state and identify integration opportunities

### Checklist

- [ ] **Load Session Context**: Review `.claude/session-context/` for latest state
- [ ] **Analyze Pain Points**: Identify current platform challenges
- [ ] **Review Existing Agents**: Check `.claude/AGENT_REGISTRY.md` for 187+ agents
- [ ] **Identify Capability Gaps**: Where does this agent fill a need?
- [ ] **Map Integration Points**: MCP, quality gates, command registry, coordination

### Analysis Tasks

```bash
# Review platform statistics
cat .claude/AGENT_REGISTRY.md | grep "Total Agents"
cat .claude/COMMAND_REGISTRY.md | grep "Total Commands"

# Analyze codebase size
find apps/*/lib -name "*.ex" | wc -l
find apps/*/lib -name "*.ex" | xargs wc -l | tail -1

# Check quality state
mix quality.gates

# Review recent sessions
ls -lt .claude/session-context/*.md | head -5
```

### Output

- **Platform State Report**: Current statistics and quality metrics
- **Pain Point Analysis**: Documented challenges this agent will address
- **Capability Gap Assessment**: Clear justification for new agent

---

## Phase 3: Agent Design

**Duration**: 30-60 minutes
**Goal**: Comprehensive agent specification with tactical classification

### Checklist

- [ ] **Define Agent Classification**: Tactical Intelligence / Strategic Command / Supreme Authority
- [ ] **Specify Core Capabilities**: Detailed list of agent functions
- [ ] **Design Integration Interfaces**: MCP protocol, quality gates, command integration
- [ ] **Plan Coordination Protocols**: How agent communicates with others
- [ ] **Document Authority Levels**: What decisions can agent make autonomously

### Agent Specification Template

```markdown
# [Agent Name]

**Classification**: [TACTICAL INTELLIGENCE | STRATEGIC COMMAND | SUPREME AUTHORITY]
**Domain**: [Primary domain(s)]
**Authority**: [HIGH | MEDIUM | LOW]
**Coordination**: [MCP | Direct | Hybrid]

## Core Capabilities

1. [Primary capability with description]
2. [Secondary capability with description]
3. [Additional capabilities...]

## Integration Points

- **MCP Protocol**: [How it uses MCP]
- **Quality Gates**: [Integration with quality infrastructure]
- **Command Registry**: [Slash commands it provides]
- **Agent Coordination**: [Which agents it coordinates with]

## Success Metrics

- **Immediate Impact**: [What happens right away]
- **Short-term (1-2 months)**: [Expected improvements]
- **Long-term (3-6 months)**: [Strategic value]
```

### Output

- **Agent Specification Document**: `.claude/agents/[agent-name].md`
- **Core Capabilities List**: Detailed functionality description
- **Integration Plan**: How agent fits into ecosystem

---

## Phase 4: Implementation

**Duration**: 60-180 minutes
**Goal**: Working agent implementation with core engine

### Checklist

- [ ] **Create Agent Definition File**: `.claude/agents/[agent-name].md`
- [ ] **Implement Core Engine**: `apps/prismatic/lib/[domain]/[agent_name].ex`
- [ ] **Add Validation Logic**: Verify agent operations and outputs
- [ ] **Include Error Handling**: Graceful failure and recovery
- [ ] **Write Comprehensive Documentation**: @moduledoc, @doc, @spec

### Implementation Patterns

**GenServer Pattern** (for stateful agents):
```elixir
defmodule Prismatic.[Domain].[AgentName] do
  use GenServer
  require Logger

  @moduledoc """
  [Comprehensive agent description]

  ## Capabilities
  - [Capability 1]
  - [Capability 2]

  ## Usage
      {:ok, pid} = [AgentName].start_link([])
      [AgentName].perform_task(pid, params)
  """

  def start_link(opts) do
    GenServer.start_link(__MODULE__, opts, name: __MODULE__)
  end

  @impl true
  def init(opts) do
    state = %{...}
    {:ok, state}
  end

  # Client API...
  # Server callbacks...
end
```

**Mix Task Pattern** (for command-line tools):
```elixir
defmodule Mix.Tasks.[Domain].[TaskName] do
  use Mix.Task

  @shortdoc "[Brief description]"

  @moduledoc """
  [Comprehensive task description]

  ## Usage
      mix [domain].[task_name]
  """

  @impl Mix.Task
  def run(args) do
    # Implementation...
  end
end
```

### Output

- **Core Engine**: Working implementation file(s)
- **Validation Tests**: Basic validation that agent works
- **Comprehensive Documentation**: All public functions documented

---

## Phase 5: Command Integration

**Duration**: 30-60 minutes
**Goal**: Slash commands with AIAD (AI-Assisted Development) integration

### Checklist

- [ ] **Create Slash Commands**: `.claude/commands/[command-name].md`
- [ ] **Update Command Registry**: Add to `.claude/COMMAND_REGISTRY.md`
- [ ] **Test Command Execution**: Verify commands work as expected
- [ ] **Document Usage Patterns**: Examples and common workflows
- [ ] **AIAD Integration**: Claude Code workflow enhancement

### Command Specification Template

```markdown
# /[command-name] - [Brief Description]

**Category**: [Development | Intelligence | Operations | etc.]
**Priority**: [High | Medium | Low]
**Authority**: [Strategic | Tactical | Operational]

## Synopsis

```bash
/[command-name] [SUBCOMMAND] [OPTIONS]
```

## Description

[Detailed command description]

## Usage Examples

```bash
# Basic usage
/[command-name]

# With options
/[command-name] --option value

# Advanced usage
/[command-name] subcommand --complex-option value
```

## AIAD Integration

[How this command enhances AI-assisted development workflows]
```

### Output

- **Slash Commands**: `.claude/commands/[command-name].md`
- **Command Registry Updates**: Entry in `.claude/COMMAND_REGISTRY.md`
- **Usage Documentation**: Comprehensive examples

---

## Phase 6: Ecosystem Registration

**Duration**: 20-30 minutes
**Goal**: Agent fully integrated into platform ecosystem

### Checklist

- [ ] **Update Agent Registry**: Add to `.claude/AGENT_REGISTRY.md`
- [ ] **Compile and Test**: `mix compile --warnings-as-errors --force`
- [ ] **Verify Integration**: Run quality gates `mix quality.gates`
- [ ] **Update Platform Statistics**: Agent count, command count
- [ ] **Test MCP Coordination**: Verify agent can coordinate with others

### Registration Updates

**`.claude/AGENT_REGISTRY.md`**:
```markdown
## [Domain] Specialists

- [Existing Agent 1](./agents/existing-agent-1.md)
- [New Agent](./agents/new-agent.md)  # NEW
- [Existing Agent 2](./agents/existing-agent-2.md)
```

**Platform Statistics**:
```markdown
**Total Agents**: 188 (+1)  # Update count
**Total Commands**: 52 (+2)  # Update count
```

### Validation Commands

```bash
# Compilation test
mix compile --warnings-as-errors --force

# Quality gates
mix quality.gates

# MCP coordination test
mix mcp.status

# Agent discovery test
grep -r "NewAgent" .claude/
```

### Output

- **Registry Entry**: Agent listed in `.claude/AGENT_REGISTRY.md`
- **Compilation Success**: Zero warnings, all tests pass
- **Quality Gates Pass**: Score ≥ 95/100

---

## Phase 7: Validation & Documentation

**Duration**: 15-30 minutes
**Goal**: Comprehensive mission archive with restoration instructions

### Checklist

- [ ] **Run Quality Gates**: `mix quality.gates` (must pass)
- [ ] **Create Session Context**: `.claude/session-context/YYYY-MM-DD-[agent]-session.md`
- [ ] **Document Learnings**: `.claude/learnings/YYYY-MM-DD-[topic].md`
- [ ] **Plan Next Steps**: What comes after this agent?
- [ ] **Validate Restoration**: Can future session load this context?

### Session Context Template

```markdown
# ARCHER SUPREME - [Agent Name] Creation Mission Complete

**Mission Date**: YYYY-MM-DD
**Commander**: ARCHER SUPREME
**Status**: ✅ MISSION ACCOMPLISHED

## Mission Executive Summary

[High-level summary of what was accomplished]

## Revolutionary Deliverables

1. **Agent Definition**: [Description]
2. **Core Engine**: [Description]
3. **Commands**: [Description]
4. **Integration**: [Description]

## Success Metrics

- ✅ [Metric 1]
- ✅ [Metric 2]
- ✅ [Metric 3]

## Next Steps

1. [Next step 1]
2. [Next step 2]
3. [Next step 3]

## Restoration Commands

```bash
# View agent
cat .claude/agents/[agent-name].md

# Run agent
mix [task]

# Test integration
mix quality.gates
```
```

### Output

- **Session Context**: Complete mission archive
- **Learning Document**: Insights for future improvements
- **Next Steps Plan**: Clear path forward

---

## Success Criteria

An agent creation mission is successful when ALL of the following are true:

✅ **Agent fully documented** in `.claude/agents/[agent-name].md`
✅ **Core implementation complete** with comprehensive @moduledoc
✅ **Slash commands created** in `.claude/commands/`
✅ **Registered in ecosystem** via `.claude/AGENT_REGISTRY.md`
✅ **Zero compilation warnings** (`mix compile --warnings-as-errors`)
✅ **Quality gates pass** (`mix quality.gates` score ≥ 95)
✅ **MCP integration verified** (can coordinate with other agents)
✅ **Session context saved** for future restoration
✅ **Learnings documented** for continuous improvement

---

## Common Pitfalls & Solutions

### Pitfall 1: Unclear Requirements
**Problem**: Starting implementation before requirements are crystal clear
**Solution**: Phase 1 iteration - ask questions until zero ambiguity

### Pitfall 2: Skipping Platform Analysis
**Problem**: Creating agent that duplicates existing functionality
**Solution**: Phase 2 thorough review of `.claude/AGENT_REGISTRY.md`

### Pitfall 3: Poor Integration Design
**Problem**: Agent doesn't fit into ecosystem properly
**Solution**: Phase 3 comprehensive integration planning with MCP

### Pitfall 4: Incomplete Documentation
**Problem**: Future sessions can't understand or maintain agent
**Solution**: Phase 7 comprehensive session context with restoration instructions

### Pitfall 5: No Quality Validation
**Problem**: Agent works but violates quality standards
**Solution**: Phase 6 mandatory quality gates before considering complete

---

## Continuous Improvement

After each agent creation:
1. **Review** what went well and what could improve
2. **Document** learnings in `.claude/learnings/`
3. **Update** this protocol with improvements
4. **Share** insights with team and AI ecosystem

---

## AIES Integration

This protocol is part of the **AI Ecosystem (AIES)** and should be accessible to:
- Claude Code (`.claude/`)
- Gemini Integration (`.gemini/`)
- Future AI tools (standardized format)

**Cross-AI Compatibility**: This protocol uses standard Markdown and can be referenced by any AI tool accessing the codebase.

---

**Protocol Version**: 1.0.0
**Last Updated**: 2025-11-09
**Success Rate**: 100%
**Next Review**: 2025-12-09

---

## Connect & Contribute

**Created by [Tomáš Korcak (korczis)](https://github.com/korczis)** | Open Source under [GHL](https://github.com/korczis/prismatic-platform/blob/main/LICENSE)

- [GitHub](https://github.com/korczis/prismatic-platform) | [GitLab](https://gitlab.com/korczis/prismatic-platform) | [LinkedIn](https://linkedin.com/in/korczis) | [Contact](mailto:korczis@gmail.com)
- [Developer Portal](/developers/) | [Architecture](/architecture/) | [Meet the Creator](/about/author/)
