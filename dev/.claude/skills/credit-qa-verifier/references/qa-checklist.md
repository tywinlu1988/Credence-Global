# QA Checklist

**Version**: v0.0.7

> This checklist is the review basis for `credit-qa-verifier`: four mandatory checks + common path quality gates. Every **rule name must be grep-able in the referenced engine document** (same traceability standard as the registry quality gates), and no rules may be fabricated. Rule content and values use the referenced engine documents as the single source of truth; this checklist does not copy any thresholds, SRI tiers, layered time budgets, or rating values.

## Four Mandatory Checks (mandatory_checks)

Any failure results in `fail`:

| Check | Rule Name (grep keyword) | Rule Source |
|---|---|---|
| density_rule | Signal Density | dev/engine/mosaic-engine.md §4.3 |
| density_rule | Insufficient data to evaluate | dev/engine/mosaic-engine.md §4.3 |
| veto_ceiling | Veto | dev/engine/industry-framework.md §5 |
| veto_ceiling | locked at CCC | dev/engine/industry-framework.md §5 |
| mode_b | Mode B | dev/engine/mosaic-engine.md §6 |
| mode_b | data gaps | dev/engine/mosaic-engine.md §6 |
| single_source | single source of truth | dev/engine/work-path-registry.md |

## Common Path Quality Gates (gate_results)

Gate-by-gate review follows the Path Sheet's `quality_gates` list; the complete quality gate inventory uses each path's `quality_gates` field in `dev/engine/work-path-registry.md` as the single source of truth. The following are common quality gate rule names for active paths and their traceability:

| Rule Name (grep keyword) | Rule Source |
|---|---|
| Cross-Validation | dev/engine/dual-track-methodology.md §4 |
| Five-Dimension | dev/engine/concentration-framework.md §1 |
| Thermometer | dev/engine/systemic-warning-framework.md §3 |
| Contagion Matrix | dev/engine/contagion-matrix.md §2 |
| Deep-Dive Frameworks | dev/engine/multi-stakeholder.md §2 |

## Process-Compliance Checks (anti-drift; process_compliance)

Any failure results in `fail`:

| Check | Rule Name (grep keyword) | Rule Source |
|---|---|---|
| template_compliance | templates | dev/engine/work-path-registry.md |
| citation_compliance | engine_undefined | AGENTS.md |
| dimension_compliance | Ten-Dimension Scoring | dev/engine/industry-framework.md |
| dimension_compliance | Six International Paradigms | dev/engine/industry-framework.md |
| dimension_compliance | Contagion Matrix | dev/engine/contagion-matrix.md |
| chain_compliance | Path Sheet | dev/engine/pipeline-contract.md |

**What each check verifies:**

- **template_compliance**: Every rendered report file maps to a template in the path's registry `templates` field (or a declared marker) — no ad-hoc layouts. Manifest: `dev/templates/index.yaml`.
- **citation_compliance**: Every numeric claim (threshold, weight, score, tier, rating) carries a `doc §section` citation or is marked `engine_undefined`.
- **dimension_compliance**: All analysis dimensions/metrics use engine vocabulary only (industry-framework D1-D10 + paradigm pyramids; concentration-framework five dimensions; contagion-matrix 19 industries; P1-P6 paradigms) — no invented dimensions, industries, or paradigms.
- **chain_compliance**: A Path Sheet exists for the `path_id`, and this QA Verdict is produced before delivery — analysis never ships without it.

## Fail Conditions (not limited to)

- Missing completeness report (completeness is a required output for every analysis; rule source: `dev/engine/mosaic-engine.md` §5).
- Dimensions below the density floor outputting numeric scores, or insufficient weighted-average density yet a final letter rating is output.
- One-vote veto triggered but rating ceiling not locked.
- Mode B hallucination: external data values appearing when the user has not explicitly provided data sources.
- Fabricated thresholds/weights/rating mappings; engine-undefined quantities not truthfully annotated.
- The three artifacts' `path_id` are inconsistent or unresolvable in the registry.
- A rendered report file that does not map to any template in the path's registry `templates` field (ad-hoc layout).
- Numeric claims without a `doc §section` citation that are not marked `engine_undefined`.
- Dimensions, industries, metrics, or paradigms not present in the engine vocabulary.
- Analysis delivered without a passing QA Verdict.

> If any inconsistency arises between this checklist and the referenced engine documents, the engine documents prevail.
