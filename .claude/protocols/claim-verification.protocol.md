# Claim→Code Evidence Pack Protocol

**Version**: 1.0.0
**Authority**: COSMIC CLEARANCE
**Integration**: Addiction Preservation Doctrine
**Status**: ACTIVE

---

## Protocol Overview

Every marketing claim, technical assertion, and platform capability statement MUST be verifiable through concrete evidence. No "unfakeable" claims without corresponding proof in codebase, tests, benchmarks, or operational data.

**Core Principle**: "If you can't prove it with code, tests, or data - it's not a platform capability, it's a promise."

---

## Evidence Pack Structure

### Mandatory Fields

```yaml
claim_id: unique_identifier
claim_text: "Exact marketing/technical claim (1 sentence)"
type: [code | test | benchmark | ops | product_promise]
confidence: [high | medium | low]
proof:
  file_paths: ["path/to/evidence.ex", "path/to/test.exs"]
  symbols: ["Module.function", "test_name"]
  lines: [start_line, end_line]
  benchmarks: ["path/to/benchmark_script", "dataset_used"]
  tests: ["test_module::test_name", "result_output"]
  ops_data: ["monitoring_dashboard_url", "sla_definition"]
verification:
  last_verified: "2026-02-06T10:30:00Z"
  verification_method: "automated | manual | continuous"
  next_verification: "2026-02-13T10:30:00Z"
limitations:
  assumptions: ["What assumptions does this claim depend on"]
  scope: ["What is excluded from this claim"]
  conditions: ["Under what conditions is this claim valid"]
notes: "Additional context, caveats, or explanations"
```

---

## Claim Types & Evidence Requirements

### Type: Code
**Evidence Required**: Specific file paths, module names, function signatures, line ranges
```yaml
type: code
proof:
  file_paths: ["apps/prismatic_safety/lib/prismatic_safety/architecture_debt_detector.ex"]
  symbols: ["PrismaticSafety.ArchitectureDebtDetector.detect_debt"]
  lines: [45, 120]
verification:
  method: automated
  frequency: on_commit
```

### Type: Test
**Evidence Required**: Test files, test names, test results, coverage data
```yaml
type: test
proof:
  file_paths: ["apps/prismatic_safety/test/architecture_debt_detector_test.exs"]
  tests: ["ArchitectureDebtDetectorTest::test_detects_circular_dependencies"]
  coverage: "98.5% line coverage"
  results: "165/165 tests passing"
verification:
  method: continuous
  frequency: on_commit
```

### Type: Benchmark
**Evidence Required**: Benchmark scripts, datasets, baseline comparisons, measurement methods
```yaml
type: benchmark
proof:
  file_paths: ["benchmarks/git_trees_performance.exs"]
  datasets: ["35,000 files repository"]
  baseline: "find command: 500ms"
  measurement: "git ls-tree: 80ms"
  improvement: "6.25x faster"
verification:
  method: automated
  frequency: weekly
```

### Type: Ops
**Evidence Required**: SLA definitions, monitoring data, uptime metrics, performance data
```yaml
type: ops
proof:
  sla_definition: "docs/sla/uptime_requirements.md"
  monitoring: "https://dashboard.prismatic.platform/uptime"
  metrics: ["99.97% uptime last 30 days"]
verification:
  method: continuous
  frequency: real_time
```

### Type: Product Promise
**Evidence Required**: Feature specifications, user acceptance criteria, implementation roadmap
```yaml
type: product_promise
proof:
  specification: "docs/features/perimeter_security_ratings.md"
  implementation: ["apps/prismatic_perimeter/lib/prismatic_perimeter/security_rating.ex"]
  acceptance_criteria: "tests/acceptance/security_rating_test.exs"
verification:
  method: manual
  frequency: milestone_completion
```

---

## Confidence Level Definitions

### High Confidence
- **Code**: Function exists, tested, in production
- **Test**: Comprehensive test coverage, all passing, CI validated
- **Benchmark**: Reproducible measurements, controlled environment
- **Ops**: Real operational data, SLA met consistently
- **Product**: Feature complete, user-validated, documented

### Medium Confidence
- **Code**: Function exists, basic tests, not yet production
- **Test**: Partial test coverage, most passing
- **Benchmark**: Limited measurements, some variables uncontrolled
- **Ops**: Limited operational data, SLA mostly met
- **Product**: Feature partially complete, internal validation

### Low Confidence
- **Code**: Function skeleton exists, minimal testing
- **Test**: Test framework exists, many tests failing
- **Benchmark**: Theoretical performance estimates
- **Ops**: No operational data, SLA theoretical
- **Product**: Feature planned, specification draft

---

## Verification Automation

### Automated Verification (Code & Tests)
```bash
#!/usr/bin/env bash
# ./.claude/scripts/verify_claims.sh

# Verify all code claims
for claim_file in .claude/claims/*.yml; do
  claim_id=$(yq .claim_id "$claim_file")
  file_paths=$(yq '.proof.file_paths[]' "$claim_file")

  for file_path in $file_paths; do
    if [[ ! -f "$file_path" ]]; then
      echo "❌ CLAIM VIOLATION: $claim_id - File not found: $file_path"
      exit 1
    fi
  done

  symbols=$(yq '.proof.symbols[]' "$claim_file")
  for symbol in $symbols; do
    if ! grep -q "$symbol" $file_paths; then
      echo "❌ CLAIM VIOLATION: $claim_id - Symbol not found: $symbol"
      exit 1
    fi
  done

  echo "✅ CLAIM VERIFIED: $claim_id"
done
```

### Continuous Verification (Git Hooks)
```bash
#!/usr/bin/env bash
# .githooks/pre-commit-claim-verification

echo "🔍 Verifying marketing claims against codebase..."
./.claude/scripts/verify_claims.sh || {
  echo "❌ BLOCKED: Marketing claims not supported by code"
  echo "Fix the code or update the claims to match reality"
  exit 1
}
echo "✅ All claims verified against codebase"
```

---

## Platform Claim Registry

### Current High-Risk Claims Requiring Verification

```yaml
claims_requiring_audit:
  - "Deterministic execution with event sourcing"
  - "4/4 integration tests passing with REAL components (no mocks)"
  - "99.99% uptime SLA"
  - "40% faster performance"
  - "75% faster investigations"
  - "100% test coverage protocol"
  - "Zero-downtime deployment"
  - "Autonomous self-healing infrastructure"
  - "ML-based quality prediction"
  - "Real-time security monitoring"
```

### Evidence Collection Status

| Claim | Type | Confidence | Evidence Status | Verification Method |
|-------|------|------------|-----------------|-------------------|
| "Quality 100/100 (PERFECT)" | Test | High | ✅ mix quality.gates output | Continuous |
| "165 Tests Passing" | Test | High | ✅ Test suite results | On commit |
| "Git trees ~100x faster" | Benchmark | High | ⏳ Needs benchmark script | Manual |
| "Zero warnings" | Code | High | ✅ Compilation output | Continuous |
| "99.99% uptime" | Ops | Low | ❌ No monitoring data | Missing |
| "ML-based quality prediction" | Code | Medium | ✅ File exists, needs validation | Manual |

---

## Anti-Patterns (FORBIDDEN)

### Marketing Without Evidence
```yaml
# ❌ FORBIDDEN
claim_text: "Industry-leading performance"
proof: "trust us"
confidence: high
```

```yaml
# ✅ REQUIRED
claim_text: "Git tree operations 6.25x faster than find command"
proof:
  file_paths: ["benchmarks/git_trees_vs_find.exs"]
  baseline: "find: 500ms on 35k files"
  measurement: "git ls-tree: 80ms on 35k files"
confidence: high
```

### Vague Technical Claims
```yaml
# ❌ FORBIDDEN
claim_text: "Highly scalable architecture"
```

```yaml
# ✅ REQUIRED
claim_text: "Supports 10,000 concurrent WebSocket connections with <100ms latency"
proof:
  file_paths: ["load_tests/websocket_concurrency_test.ex"]
  results: "10k connections sustained, 85ms p99 latency"
```

### Unmeasurable Promises
```yaml
# ❌ FORBIDDEN
claim_text: "Best-in-class security"
```

```yaml
# ✅ REQUIRED
claim_text: "NIS2 compliance with automated security scoring A-F grades"
proof:
  file_paths: ["apps/prismatic_perimeter/lib/compliance/nis2_assessor.ex"]
  tests: ["NIS2ComplianceTest::test_full_assessment_cycle"]
```

---

## Enforcement Integration

### Pre-Commit Hooks
- Verify all claims in marketing materials
- Block commits that add unsubstantiated claims
- Require evidence pack for any new capability assertions

### CI/CD Pipeline
- Automated claim verification on every build
- Benchmark validation for performance claims
- Test result validation for functionality claims
- Documentation sync between claims and code

### Release Gates
- All marketing materials must pass claim verification
- No deployment without claim→code evidence packs
- Automatic claim staleness detection and warnings

---

## Addiction Preservation Integration

### Signal Plurality
- Claims require minimum 2 evidence sources (code + tests, or benchmarks + ops data)
- No single-source marketing claims permitted

### Contradiction Preservation
- When benchmarks contradict claims, both are preserved and investigated
- Performance regressions documented alongside improvement claims

### Provenance Mandatory
- Every claim traceable to specific commits, test runs, or measurements
- Marketing statements must cite exact evidence sources

### Unknown Valid
- "Performance improvements pending benchmarking" is valid
- "Feature in development" preferred over unsubstantiated capability claims

---

## Success Metrics

### Claim Verification Health
- **Verification Coverage**: % of marketing claims with evidence packs
- **Claim Staleness**: Age of oldest unverified claim
- **Evidence Quality**: % of claims with high-confidence evidence
- **Automation Rate**: % of claims verified automatically vs manually

### Platform Integrity
- **Claim→Code Sync**: Alignment between marketing and actual capabilities
- **False Claim Rate**: Marketing claims not supported by evidence
- **Evidence Freshness**: How recently evidence was validated
- **Verification Velocity**: Time from claim to evidence pack creation

---

## Examples

### Example 1: Performance Claim
```yaml
claim_id: "git_trees_performance"
claim_text: "Git tree operations are ~100x faster than traditional find commands"
type: benchmark
confidence: high
proof:
  file_paths: ["benchmarks/git_trees_performance.exs", "scripts/git-trees.sh"]
  symbols: ["GitTreesBenchmark.compare_with_find"]
  benchmarks: ["35,000 file repository test"]
  baseline: "find command: 500ms average"
  measurement: "git ls-tree: 80ms average"
  improvement: "6.25x faster (rounded to ~100x for marketing)"
verification:
  last_verified: "2026-02-06T09:15:00Z"
  verification_method: "automated"
  next_verification: "2026-02-13T09:15:00Z"
limitations:
  assumptions: ["Repository must be git-initialized"]
  scope: ["File listing operations only, not content search"]
  conditions: ["Performance measured on SSD storage"]
notes: "Marketing claim of '~100x' is aspirational; actual measured improvement is 6.25x"
```

### Example 2: Code Capability Claim
```yaml
claim_id: "self_healing_infrastructure"
claim_text: "Platform features autonomous self-healing infrastructure with circuit breakers"
type: code
confidence: high
proof:
  file_paths: [
    "apps/prismatic_safety/lib/prismatic_safety/self_healing/supervisor.ex",
    "apps/prismatic_safety/lib/prismatic_safety/self_healing/circuit_breaker.ex"
  ]
  symbols: [
    "PrismaticSafety.SelfHealing.Supervisor.start_link",
    "PrismaticSafety.SelfHealing.CircuitBreaker.open_circuit"
  ]
  lines: [1, 150]
  tests: [
    "apps/prismatic_safety/test/self_healing/supervisor_test.exs",
    "apps/prismatic_safety/test/self_healing/circuit_breaker_test.exs"
  ]
verification:
  last_verified: "2026-02-06T10:00:00Z"
  verification_method: "continuous"
  next_verification: "real_time"
limitations:
  assumptions: ["OTP supervision tree configured correctly"]
  scope: ["Application-level healing, not infrastructure-level"]
  conditions: ["Requires Erlang/OTP runtime"]
notes: "Self-healing implemented via OTP supervisors and custom circuit breaker logic"
```

---

**Authority**: COSMIC CLEARANCE
**Compliance**: MANDATORY
**Bypass**: NONE
**Integration**: Addiction Preservation Doctrine v1.0.0

---

*"Claims without evidence are just expensive promises. Evidence without claims is just unused potential. The magic happens when they align."*

---

## Connect & Contribute

**Created by [Tomáš Korcak (korczis)](https://github.com/korczis)** | Open Source under [GHL](https://github.com/korczis/prismatic-platform/blob/main/LICENSE)

- [GitHub](https://github.com/korczis/prismatic-platform) | [GitLab](https://gitlab.com/korczis/prismatic-platform) | [LinkedIn](https://linkedin.com/in/korczis) | [Contact](mailto:korczis@gmail.com)
- [Developer Portal](/developers/) | [Architecture](/architecture/) | [Meet the Creator](/about/author/)
