---
name: credit-qa-verifier
description: Use when verifying a fixed-income credit report or analysis — checking a work path's quality gates, enforcing the mandatory signal-density rules (no numeric score below the density floor), the one-shot-veto CCC ceiling, Mode B anti-hallucination guardrails, and single-source-of-truth compliance (no invented thresholds). Triggers on 'QA check', 'review this report', 'check for issues', 'quality gate', or as the final step after report generation. Reads engine documents as the rule source; never relaxes a gate.
---

## Purpose

**Engine version**: v0.0.3

QA layer — final stage of the four-stage chain. Responsibility: perform pre-delivery review of the Delivery Note and its upstream Analysis Artifact and Path Sheet, producing a QA Verdict. This skill uses engine documents as the rule source and **never relaxes a gate**: if any quality gate or mandatory check fails, the verdict is `fail` and must be sent back for remediation; do not lower standards for delivery. This skill does not replicate any thresholds/rating mappings; rule content uses the referenced engine documents as the single source of truth.

## Inputs

- **Delivery Note**: produced by `credit-report-builder` (field shape at `dev/engine/pipeline-contract.md` §2.3).
- **Analysis Artifact**: produced by `fixed-income-credit-analysis`, for reviewing density/veto/completeness (§2.2).
- **Path Sheet `quality_gates`**: produced by `credit-analysis-router`, serving as the checklist source for gate-by-gate review; `path_id` is the join key throughout — all three artifacts must be consistent.

## Output

- **QA Verdict** — final stage artifact, field shape at `dev/engine/pipeline-contract.md` §2.4. `verdict` takes one of `pass` | `pass-with-findings` | `fail`.

## Verification Protocol

1. **Join key consistency**: The `path_id` in all three artifacts must be identical and resolvable in the registry. Inconsistency → `fail`.
2. **Gate-by-gate review**: Review each quality gate in the Path Sheet's `quality_gates` list, producing `gate_results` (each with `status` + `evidence`, evidence citing engine document sections).
3. **Four mandatory checks**: See below. Any failure → `fail`.
4. **Produce verdict**: All pass → `pass`; pass but with findings that should be noted → `pass-with-findings`; any failure → `fail` with `remediation`.

## Mandatory Checks (rule source is engine documents)

- **Signal density rule `density_rule`**: Dimensions below the density floor must not output numeric scores and must be annotated as `insufficient information to evaluate`; when weighted-average density is insufficient, must not output a final letter rating. Rule source: `dev/engine/mosaic-engine.md` §4.3.
- **One-shot veto ceiling `veto_ceiling`**: Issuers triggering a one-vote veto have their rating ceiling locked at CCC, may not be raised. Rule source: `dev/engine/industry-framework.md` §5.
- **Mode B anti-hallucination `mode_b`**: Unless the user explicitly provides data sources (CSV/API/MCP), no Mode B external data values may appear; all Mode B fields must be treated as data gaps. Rule source: `dev/engine/mosaic-engine.md` §6.
- **Single source of truth `single_source`**: Reports/analyses must not fabricate thresholds, weights, or rating mappings; quantities not defined in the engine must be annotated as `not defined in engine`. Rule source: all referenced engine documents.

## QA Verdict Output

Template (schema single source of truth is `dev/engine/pipeline-contract.md` §2.4):

```yaml
path_id: ""                 # join key (all three artifacts must be consistent)
verdict: ""                 # pass|pass-with-findings|fail
gate_results:               # gate-by-gate review results
  - gate: ""                # "rule name (dev/engine/<doc>.md §section)" (inherited from Path Sheet quality_gates)
    status: ""              # pass|fail
    evidence: ""            # review evidence (citing engine document sections, not copying values)
mandatory_checks:           # four mandatory checks
  density_rule: ""
  veto_ceiling: ""
  mode_b: ""
  single_source: ""
remediation: []             # remediation suggestions for failed items
```

Example (Credit Selector single target WP-CS-01, three gates all pass, mandatory checks all pass, one finding to note):

```yaml
path_id: WP-CS-01
verdict: pass-with-findings
gate_results:
  - gate: "Signal Density (dev/engine/mosaic-engine.md §4.3)"
    status: pass
    evidence: Dimensions below density floor are set to null and annotated insufficient information to evaluate (mosaic-engine §4.3)
  - gate: "Veto (dev/engine/industry-framework.md §5)"
    status: pass
    evidence: No one-vote veto triggered; rating ceiling rule verified (industry-framework §5)
  - gate: "Cross-Validation (dev/engine/dual-track-methodology.md §4)"
    status: pass
    evidence: Track divergence presented and interpreted in report (dual-track-methodology §4)
mandatory_checks:
  density_rule: pass
  veto_ceiling: pass
  mode_b: pass
  single_source: pass
remediation: []
```

## Chaining (Final Stage)

- **Upstream (REQUIRED)**: `credit-report-builder` — consumes its Delivery Note and upstream artifacts.
- **Final stage**: This skill is the last of the four-stage chain; no downstream. When verdict is `fail`, return to the appropriate stage per `remediation` (density/veto issues → return to analysis; template/assembly issues → return to report) for remediation and re-review.

## Guardrails

- **Never relaxes a gate**: Quality gates and mandatory checks only have pass/fail outcomes; no discretionary pass. Missing completeness report, outputting numeric scores below density floor, fabricating thresholds, Mode B hallucination — all result in `fail`.
- **Do not replicate engine content**: Only reference rule names and document sections; do not replicate any thresholds, SRI tiers, layered time budgets, or rating mappings. Numerical judgments are based on the referenced engine documents.
- **Engine documents as rule source**: Every gate rule name must be grep-able in the referenced engine document (traceability at `references/qa-checklist.md`); do not fabricate rules.

## References

- `references/qa-checklist.md` — QA checklist (gate rule name → engine document traceability, pointer only)
- `dev/engine/pipeline-contract.md` — Four-stage chain I/O contract (artifact schema single source of truth)
- `dev/engine/mosaic-engine.md` — Signal density / completeness / Mode B guardrail (density_rule, mode_b rule source)
- `dev/engine/industry-framework.md` — One-shot veto rating ceiling (veto_ceiling rule source)
- `dev/engine/work-path-registry.md` — Work path registry (quality gate list traceability)
