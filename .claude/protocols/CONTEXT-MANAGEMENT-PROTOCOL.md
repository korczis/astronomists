# Context Management Protocol
**Version**: 1.0.0
**Status**: MANDATORY - STRICTLY ENFORCED
**Priority**: P0 (Highest - System Critical)
**Last Updated**: 2025-10-31

## Overview

The Context Management Protocol ensures **100% session continuity** across all agent operations, user sessions, and development work through **automatic context saving and loading**.

**Purpose**: Eliminate context loss, enable seamless session resumption, preserve decision history, maintain project memory.

**Scope**: ALL agents, ALL sessions, ALL development work - NO EXCEPTIONS.

---

## 🚨 CRITICAL REQUIREMENTS

### Mandatory Context Operations

**EVERY agent operation MUST**:
1. Load context BEFORE starting work
2. Maintain context DURING execution
3. Save context AFTER major milestones
4. Save final context AT END of session

**NO EXCEPTIONS** - This is not optional, this is mandatory infrastructure.

---

## Context Loading Protocol

### When to Load Context

**ALWAYS load context**:
- ✅ At session start (first action of any session)
- ✅ Before deploying any agent
- ✅ When user says "proceed" (resume from checkpoint)
- ✅ When starting multi-session tasks
- ✅ After any interruption or error

### Context Sources (Priority Order)

1. **`.claude/session-context/`** - Latest session context files
   - Most recent matching session
   - **MANDATORY FORMAT**: `YYYY-MM-DD-HH-MM-SS-mmm-{relevant-keyword}-session.md`
   - Example: `2025-12-05-17-02-32-439-archer-supreme-complete-session.md`
   - **TIMESTAMP VALIDATION**: Pre-commit hook enforces exact format (.githooks/validate-session-context-timestamps)
   - **AUTOMATIC GENERATION**: Use `date '+%Y-%m-%d-%H-%M-%S'` + milliseconds for proper format

2. **`.claude/reports/ARCHER-SUPREME-MISSION-ARCHIVE/`** - Mission archives
   - Complete mission documentation
   - Full context for major initiatives
   - Official records with COSMIC CLEARANCE

3. **`.claude/todos/YYYY/MM/DD/`** - Recent TODO contexts
   - Current work-in-progress
   - Active task tracking
   - Session continuity markers

4. **MCP Blackboard `context` frame** - Live session context
   - Real-time coordination
   - Multi-agent shared state
   - Dynamic context updates

### Context Loading Procedure

```bash
# Step 1: Check for latest context
ls -lt .claude/session-context/ | head -10

# Step 2: Load most recent relevant context
cat .claude/session-context/YYYY-MM-DD-{relevant}-session.md

# Step 3: Review context sections
# - Mission objectives
# - Current state
# - Last actions taken
# - Next steps
# - Open issues/blockers

# Step 4: Confirm understanding
# "Loaded context from YYYY-MM-DD session. Resuming from: {checkpoint}"
```

### Context Loading Best Practices

- **Read ENTIRE context file** - Don't skip sections
- **Understand decisions** - Know why choices were made
- **Identify checkpoint** - Know exact resumption point
- **Check for blockers** - Address any open issues
- **Verify file integrity** - Ensure complete load

---

## Context Saving Protocol

### When to Save Context

**Auto-save triggers** (mandatory):
- ✅ After every major phase completion
- ✅ Every 30 minutes of active work (set timer)
- ✅ Before deploying another agent
- ✅ Before switching tasks
- ✅ On error or unexpected termination
- ✅ At user request ("save context")
- ✅ **AT SESSION END (absolutely mandatory)**

### Context File Requirements

#### Mandatory Content

**EVERY context file MUST include**:

1. **Session Metadata**
   - Date and timestamp
   - Mission/task name
   - Agent(s) involved
   - User objectives
   - Session classification (if applicable)

2. **Complete Task Description**
   - What was requested
   - Why it was needed
   - Success criteria
   - Constraints and requirements

3. **All Actions Taken** (with timestamps)
   - Commands executed
   - Files modified/created
   - Agents deployed
   - Decisions made
   - Reasoning for decisions

4. **All Files Modified/Created**
   - Full file paths
   - Nature of changes
   - Line counts
   - Purpose of changes

5. **All Deliverables Produced**
   - Reports created
   - Code written
   - Tests added
   - Documentation updated
   - Features delivered

6. **Verification Results**
   - Compilation status
   - Test results
   - Quality gate results
   - Deployment status
   - Performance metrics

7. **TODO Tickets Created**
   - Ticket IDs (PLAT-####)
   - Ticket descriptions
   - Priority levels
   - Categories

8. **Key Decisions and Rationale**
   - Strategic choices made
   - Alternatives considered
   - Reasons for selection
   - Trade-offs accepted

9. **Next Steps and Recommendations**
   - Immediate next actions
   - Medium-term priorities
   - Long-term roadmap
   - Blocked items needing resolution

10. **Restoration Instructions**
    - How to resume from this checkpoint
    - Prerequisites for continuation
    - Critical files to review
    - Commands to verify state

#### File Naming Convention

**MANDATORY FORMAT** (STRICTLY ENFORCED):
```
.claude/session-context/YYYY-MM-DD-HH-MM-SS-mmm-{agent-name}-{mission-type}-session.md
.claude/session-context/YYYY-MM-DD-HH-MM-SS-mmm-{agent-name}-{mission-type}-context.json

Examples:
.claude/session-context/2025-12-05-17-02-32-439-archer-supreme-complete-session.md
.claude/session-context/2025-12-05-14-23-15-789-qa-testing-llm-coverage-session.md
.claude/session-context/2025-12-05-09-45-22-123-ui-dashboard-delivery-session.md
```

**Format Specification**:
- `YYYY-MM-DD`: Date (4-digit year, 2-digit month, 2-digit day)
- `HH-MM-SS`: Time (24-hour format, 2 digits each)
- `mmm`: Milliseconds (3 digits)
- `{agent-name}`: Agent identifier (lowercase-with-hyphens)
- `{mission-type}`: Mission descriptor (lowercase-with-hyphens)
- `session.md`: File extension

**Enforcement**: Pre-commit hooks BLOCK commits with incorrect timestamp format.

#### File Format

**Markdown structure**:
```markdown
# {Mission Name} - Session Context
**Date**: YYYY-MM-DD
**Agent**: {agent-name}
**Status**: {complete|in-progress|blocked}

## Session Overview
[High-level summary]

## Objectives
[What needed to be achieved]

## Actions Taken
### Phase 1: {phase-name}
- [timestamp] Action 1
- [timestamp] Action 2

### Phase 2: {phase-name}
- [timestamp] Action 3

## Files Modified
1. `path/to/file1.ex` - Description of changes (123 lines)
2. `path/to/file2.md` - Description (456 lines)

## Deliverables
- Report: path/to/report.md
- Code: path/to/code.ex (tests: path/to/test.exs)
- Feature: Description

## Verification Results
- Compilation: ✅ PASS (0 warnings)
- Tests: ✅ PASS (650+ passing)
- Quality Gates: ✅ PASS (98/100)

## TODO Tickets
- PLAT-2034: Description [priority:high]
- PLAT-2035: Description [priority:medium]

## Key Decisions
1. **Decision**: What was decided
   **Rationale**: Why it was decided
   **Alternatives**: What else was considered
   **Trade-offs**: What was sacrificed

## Next Steps
### Immediate (Next Session)
- Action 1
- Action 2

### Medium-term (Next Week)
- Action 3

### Long-term (Next Month)
- Action 4

## Restoration Instructions
To resume from this checkpoint:
1. Load this context file
2. Review sections: {list critical sections}
3. Verify state: {commands to run}
4. Resume from: {specific checkpoint}

## Mission Status
**Status**: {complete|85% complete|blocked}
**Confidence**: {100%|high|medium}
**Blockers**: {none|list blockers}
```

### Context Saving Procedure

```bash
# Step 1: Compile context from session
# (gather all information from sections above)

# Step 2: Write context file with proper timestamp
TIMESTAMP=$(date '+%Y-%m-%d-%H-%M-%S-%3N')
cat > .claude/session-context/${TIMESTAMP}-{mission}-session.md <<'EOF'
[Complete context content]
EOF

# Step 3: Verify file written
ls -lh .claude/session-context/${TIMESTAMP}-{mission}-session.md

# Step 4: Confirm completeness
# - All mandatory sections present
# - All files/actions documented
# - Restoration instructions clear
# - Timestamp format: YYYY-MM-DD-HH-MM-SS-mmm

# Step 5: Announce save
echo "✅ Context saved: .claude/session-context/${TIMESTAMP}-{mission}-session.md"
```

### Context Saving Best Practices

- **Be comprehensive** - Don't summarize too much, capture details
- **Include timestamps** - Enables chronological reconstruction
- **Document reasoning** - Future sessions need to understand "why"
- **Test restoration** - Can you resume from this context alone?
- **Version large contexts** - If context grows huge, create incremental saves

---

## MCP Integration

### Context Sharing via MCP Blackboard

**Context Frame Structure**:
```elixir
%{
  type: :context,
  scope: :session,
  data: %{
    session_id: "session-uuid",
    agent: "archer-supreme",
    mission: "platform-transformation",
    checkpoint: %{
      phase: "warning-elimination",
      status: "85% complete",
      next_action: "fix-remaining-typing-violations"
    },
    files_modified: ["path1.ex", "path2.md"],
    decisions: [
      %{decision: "chose-option-a", rationale: "complete-elimination"}
    ],
    context_file: ".claude/session-context/2025-10-31-archer-supreme-session.md"
  },
  timestamp: ~U[2025-10-31 12:00:00Z]
}
```

### Broadcasting Context Updates

```bash
# Register context update
POST /api/mcp/exec
Body: {
  "tool": "context.save",
  "args": {
    "checkpoint": "phase-3-complete",
    "files": ["file1.ex", "file2.md"],
    "next": "phase-4-start"
  }
}

# Broadcast to coordination topic
Phoenix.PubSub.broadcast(Prismatic.PubSub, "mcp:coordination", {
  :context_checkpoint,
  %{agent: "current-agent", checkpoint: "phase-3-complete"}
})
```

### Multi-Agent Context Coordination

**When multiple agents coordinate**:
1. Parent agent saves context before deploying child agent
2. Child agent loads parent context + adds own context
3. Child agent saves combined context with its contributions
4. Parent agent loads child's context after completion
5. Parent agent merges and saves final comprehensive context

**Context Chain**:
```
Session Start
  └─> Load: previous-session-context.md
  └─> Agent A deploys
      └─> Save: agent-a-checkpoint-1.md
      └─> Agent B deploys (reads agent-a-checkpoint-1.md)
          └─> Save: agent-b-checkpoint-1.md
      └─> Agent A resumes (reads agent-b-checkpoint-1.md)
      └─> Save: agent-a-checkpoint-2.md
  └─> Final save: complete-session-context.md
```

---

## Enforcement and Compliance

### Automatic Enforcement

**Pre-session hook**:
- Check for latest context
- Prompt to load if available
- Block session start until context reviewed

**Post-session hook**:
- Verify context saved
- Block session end until context written
- Validate context file completeness

### Compliance Verification

**Context save verification checklist**:
- [ ] File created in `.claude/session-context/`
- [ ] Filename follows convention (YYYY-MM-DD-HH-MM-SS-mmm-{name}-session.md)
- [ ] Timestamp includes hours, minutes, seconds, milliseconds
- [ ] All mandatory sections present
- [ ] All files modified documented
- [ ] All decisions documented with rationale
- [ ] Next steps clearly defined
- [ ] Restoration instructions complete
- [ ] File size > 1KB (minimum for meaningful context)

**Audit trail**:
- All context operations logged to MCP audit trail
- Timestamp of save/load operations
- Agent responsible
- Context file path
- Verification status

### Non-Compliance Consequences

**Missing context save**:
- ⚠️ Warning: "Session ending without context save - UNACCEPTABLE"
- 🚫 Block: Cannot proceed to next session until current saved
- 📊 Metric: Track context save compliance rate (target: 100%)

**Incomplete context**:
- ⚠️ Warning: "Context missing mandatory sections"
- 🔄 Retry: Prompt for completion before accepting
- 📝 Template: Provide template for missing sections

---

## Context Management Tools

### Context Discovery

```bash
# Find latest contexts
find .claude/session-context -name "*.md" -mtime -7 -type f

# Search context by keyword
rg -i "archer supreme" .claude/session-context/

# List contexts by date
ls -lt .claude/session-context/ | head -20
```

### Context Validation

```bash
# Validate context file structure
cat .claude/session-context/YYYY-MM-DD-{name}-session.md | grep -E "^##"

# Check context completeness (required sections)
for section in "Session Overview" "Objectives" "Actions Taken" "Files Modified" "Deliverables" "Verification Results" "Next Steps" "Restoration Instructions"; do
  echo -n "Checking $section: "
  grep -q "## $section" .claude/session-context/YYYY-MM-DD-{name}-session.md && echo "✅" || echo "❌"
done

# Verify file size (should be substantial)
du -h .claude/session-context/YYYY-MM-DD-{name}-session.md
```

### Context Merge (for multi-session tasks)

```bash
# Merge related contexts into comprehensive context
cat .claude/session-context/2025-10-31-phase-1-session.md \
    .claude/session-context/2025-10-31-phase-2-session.md \
    .claude/session-context/2025-10-31-phase-3-session.md \
    > .claude/session-context/2025-10-31-complete-mission-session.md
```

---

## Examples and Templates

### Example: Archer Supreme Session Context

See: `.claude/session-context/2025-12-05-17-02-32-439-archer-supreme-complete-session.md`

**Key features**:
- Complete mission timeline (6 phases)
- All agents coordinated (6 specialists)
- All deliverables (30+ reports, 4,600+ LOC)
- All achievements quantified
- All decisions documented
- Complete restoration instructions

### Template: Quick Session Context

```markdown
# {Task Name} - Quick Session Context
**Date**: YYYY-MM-DD
**Duration**: {X hours}
**Status**: ✅ COMPLETE

## What Was Done
- Objective: {what needed to be achieved}
- Approach: {how it was tackled}
- Result: {what was delivered}

## Files Modified
1. `file1.ex` - {description}
2. `file2.md` - {description}

## Verification
- Compilation: {status}
- Tests: {status}
- Quality: {status}

## Next Steps
1. {immediate next action}
2. {follow-up action}

## Restoration
To continue: Load this context, verify {key files}, then {next action}.
```

### Template: Long-Running Mission Context

```markdown
# {Mission Name} - Complete Mission Context
**Date**: YYYY-MM-DD
**Classification**: {COSMIC CLEARANCE|CONFIDENTIAL|PUBLIC}
**Status**: {COMPLETE|IN-PROGRESS|BLOCKED}

## Mission Overview
[Comprehensive description]

## Complete Timeline
### Phase 0: {name}
**Status**: ✅
**Duration**: {time}
**Agent**: {agent-name}
[Details]

### Phase 1: {name}
**Status**: ✅
[Details]

[...all phases...]

## Quantified Achievements
[Metrics, before/after, ROI, etc.]

## Complete File Inventory
[All files modified with full paths and descriptions]

## Strategic Decisions Log
[All major decisions with full context]

## Mission Archive
- Location: {archive-path}
- Contents: {list of deliverables}
- Size: {total size}

## Restoration Instructions
[Detailed step-by-step restoration guide]
```

---

## Best Practices

### Context Writing Best Practices

1. **Write for your future self** - Assume you'll forget everything
2. **Document the "why"** - Decisions without rationale are useless
3. **Include verification steps** - How to validate state
4. **Be specific with paths** - Full absolute paths, not relative
5. **Timestamp everything** - Enables chronological reconstruction
6. **Link to artifacts** - Point to actual deliverables
7. **Assume context loss** - Could this context stand alone?

### Context Loading Best Practices

1. **Read completely** - Don't skim, read every section
2. **Understand before acting** - Know why things were done
3. **Verify state matches** - Context says X, does system actually have X?
4. **Ask questions** - If context unclear, clarify before proceeding
5. **Update context** - If you find context wrong, update it

### Context Maintenance

1. **Archive old contexts** - Move >30 days to `.claude/session-context/archive/`
2. **Consolidate related contexts** - Merge multi-session contexts periodically
3. **Index important contexts** - Maintain index of major mission contexts
4. **Version control contexts** - Commit to git for backup
5. **Review periodically** - Check contexts are being used and useful

---

## FAQ

### Q: How much detail is too much?
**A**: There is no "too much" for context. Err on the side of comprehensive. Storage is cheap, lost context is expensive.

### Q: What if session ends unexpectedly?
**A**: Auto-save every 30 minutes mitigates this. If crash occurs, latest auto-save provides recovery point.

### Q: Do I save context for tiny tasks?
**A**: If task is <5 minutes and completely self-contained, optional. If task is part of larger work or might need resumption, mandatory.

### Q: Can I skip context for exploratory work?
**A**: NO. Exploratory work often leads to insights that need preservation. Save context explaining what was explored and what was learned.

### Q: What if I don't know what to write?
**A**: Use templates. Fill in what you know. Leave placeholders for unknowns. Partial context is better than no context.

### Q: How do I handle sensitive information in context?
**A**: Use classification markers (COSMIC CLEARANCE, CONFIDENTIAL). Store sensitive contexts in secure location. Redact before sharing.

### Q: What about context for failed sessions?
**A**: ESPECIALLY important. Document what was attempted, why it failed, what was learned. Prevents repeating failures.

---

## Protocol Version History

**Version 1.0.0** (2025-10-31):
- Initial protocol definition
- Mandatory enforcement rules
- Complete examples and templates
- Integration with AGENT_REGISTRY.md and CLAUDE.md

---

## References

- **Main Documentation**: `CLAUDE.md` Section 1 - Context Management Protocol
- **Agent Integration**: `AGENT_REGISTRY.md` Section "MANDATORY CONTEXT MANAGEMENT PROTOCOL"
- **Example Contexts**: `.claude/session-context/2025-10-31-archer-supreme-complete-session.md`
- **Archive Standard**: `.claude/reports/ARCHER-SUPREME-MISSION-ARCHIVE/`
- **MCP Integration**: `.claude/mcp/MCP-USAGE-GUIDE.md`

---

**Status**: ACTIVE - STRICTLY ENFORCED
**Authority**: P0 (Highest Priority)
**Compliance**: 100% Required - No Exceptions
**Last Updated**: 2025-10-31

---

_This protocol ensures zero context loss and 100% session continuity across all Prismatic Platform development work._

---

## Connect & Contribute

**Created by [Tomáš Korcak (korczis)](https://github.com/korczis)** | Open Source under [GHL](https://github.com/korczis/prismatic-platform/blob/main/LICENSE)

- [GitHub](https://github.com/korczis/prismatic-platform) | [GitLab](https://gitlab.com/korczis/prismatic-platform) | [LinkedIn](https://linkedin.com/in/korczis) | [Contact](mailto:korczis@gmail.com)
- [Developer Portal](/developers/) | [Architecture](/architecture/) | [Meet the Creator](/about/author/)
