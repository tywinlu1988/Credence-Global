---
name: credit-report-builder
description: Use when turning a completed fixed-income credit analysis into a deliverable report — selecting the correct report template (Type 1–18), mapping findings to the L0/L1/L2 output tiers, rendering a multi-stakeholder dashboard, or assembling a layered credit report from an analysis artifact. Triggers on 'generate report', 'produce a credit approval report', 'build a dashboard', 'L0 signal card', or when a work-path sheet's templates must be produced. Requires an upstream analysis artifact; does not perform analysis itself.
---

## Purpose

**Engine version**: v0.0.5

Assembly layer — **this skill does not perform analysis**. Responsibility is two steps: map the Analysis Artifact produced by the upstream `fixed-income-credit-analysis` skill to L0/L1/L2 output tiers and select the correct template → assemble into a deliverable report and produce a Delivery Note. This skill does not replicate any engine thresholds/layered time budgets/rating mappings; template selection and tier semantics are always determined by engine documents as the single source of truth.

## Inputs

- **Path Sheet**: produced by the router, providing `path_id` / `depth` / `quality_gates`. `path_id` is the join key through the four-stage chain; this skill inherits it as-is and must not change it.
- **Analysis Artifact**: produced by fixed-income, providing findings / completeness / veto / system_readouts / mode_b_gaps (field shape at `dev/engine/pipeline-contract.md` §2.2).

## Outputs

- **Deliverable Report**: rendered from `dev/templates/` (template single source of truth — this skill does not carry template copies). Which template to use is determined by the `templates` field in `dev/engine/work-path-registry.md` for that path; do not substitute arbitrarily.
- **Delivery Note**: structured YAML, field shape at `dev/engine/pipeline-contract.md` §2.3.

## Assembly Protocol

1. **Read join key**: Take `path_id` from both the Path Sheet and the Analysis Artifact; verify it points to a registered path in the registry. If inconsistent, stop and report.
2. **Select templates**: Based on `path_id`, retrieve the template list from the registry's `templates` field (Type 1–18 or allowed marker values `planned` / `L0-spec:`). Marker value meanings are defined in registry §schema; when hitting `planned`, must explicitly state "template under development" and not fabricate rendered output.
3. **Map tiers**: Map the Analysis Artifact to L0 Signal Card / L1 Snapshot / L2 Deep Report tiers. The definitions, consumption time, and information density of the three tiers use `dev/engine/output-layered-framework.md` §2 (three-tier overview) / §3 (L0 Signal Card) / §5 (L2 Deep Report) as the single source of truth; this skill does not redefine them.
4. **Render**: Use templates from `dev/templates/` to assemble the report; completeness lamp caliber follows output-layered-framework §8.4.
5. **Output Delivery Note**: Produce the Delivery Note per the schema below.

## Delivery Note Output

Template (schema single source of truth is `dev/engine/pipeline-contract.md` §2.3):

```yaml
path_id: ""                 # join key (inherited from Path Sheet, must not change)
depth: ""                   # L0|L1|L2|special (inherited from Path Sheet)
templates_used: []          # templates selected from the path's registry templates field
rendered: []                # actual report files produced (from dev/templates/)
tier_mapping:               # Analysis Artifact → L0/L1/L2 tiers
  L0: ""
  L1: ""
  L2: ""
completeness_lamp: ""       # completeness lamp status
source_analysis: ""         # upstream analysis artifact reference (traceability)
```

Example (Credit Selector single target L2 Deep Report, path WP-CS-01 with Type 1 + Type 6):

```yaml
path_id: WP-CS-01
depth: L2
templates_used:
  - dev/templates/template-type1.html
  - dev/templates/template-type6.html
rendered:
  - dev/templates/template-type1.html
  - dev/templates/template-type6.html
tier_mapping:
  L0: Signal card (rating + outlook + key signals today + completeness lamp)
  L1: Snapshot (four-dimension radar + key anomalies + rating comparison)
  L2: Deep Report (pyramid layer-by-layer + dual-track cross-comparison + completeness report)
completeness_lamp: yellow (medium confidence, caliber per output-layered-framework §8.4)
source_analysis: Upstream Analysis Artifact (findings/completeness/veto, see pipeline-contract §2.2)
```

## Chaining

- **Upstream**: `fixed-income-credit-analysis` skill — consumes its Analysis Artifact. Without an Analysis Artifact, this skill does not start (it does not perform analysis itself; go back upstream to complete analysis first).
- **REQUIRED NEXT SUB-SKILL**: `credit-qa-verifier` — after the Delivery Note is produced, hand off to the QA verification skill for pre-delivery final review (quality gates + mandatory checks); deliver only after QA passes.

## Guardrails

- **No analysis**: This skill only performs template selection, tier mapping, and assembly. It does not recalculate scores, fill in missing signals, or modify ratings. All analysis conclusions come from the upstream Analysis Artifact.
- **Do not replicate engine content**: Only reference path IDs, template names, and document sections; do not replicate any thresholds, layered time budgets, signal priority floors, or rating mappings. Tier semantics are based on `dev/engine/output-layered-framework.md`; template lists are based on `dev/engine/work-path-registry.md`.
- **Low density — no fabricated values**: Dimension scores set to null by the upstream Analysis Artifact due to insufficient density (`insufficient information to evaluate`) must retain that annotation in the report; do not fabricate values to make the report look complete.
- **Planned templates must be disclosed**: When a path's template is marked `planned`, must explicitly state "this template is under development" and provide alternative deliverable items available for that path; do not fabricate rendered output.

## References

- `references/report-mapping.md` — Path → template → tier mapping view (pointer only, no copied values)
- `dev/engine/pipeline-contract.md` — Four-stage chain I/O contract (artifact schema single source of truth)
- `dev/engine/work-path-registry.md` — Work path registry (`templates` field single source of truth)
- `dev/engine/output-layered-framework.md` — L0/L1/L2 tiered output (tier semantics single source of truth)
