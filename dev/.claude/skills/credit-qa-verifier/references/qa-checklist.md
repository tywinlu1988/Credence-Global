# QA Checklist

**Version**: v0.0.2

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

## Fail Conditions (not limited to)

- Missing completeness report (completeness is a required output for every analysis; rule source: `dev/engine/mosaic-engine.md` §5).
- Dimensions below the density floor outputting numeric scores, or insufficient weighted-average density yet a final letter rating is output.
- One-shot veto triggered but rating ceiling not locked.
- Mode B hallucination: external data values appearing when the user has not explicitly provided data sources.
- Fabricated thresholds/weights/rating mappings; engine-undefined quantities not truthfully annotated.
- The three artifacts' `path_id` are inconsistent or unresolvable in the registry.

> If any inconsistency arises between this checklist and the referenced engine documents, the engine documents prevail.
