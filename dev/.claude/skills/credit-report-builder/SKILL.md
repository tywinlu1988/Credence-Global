---
name: credit-report-builder
description: Use when turning a completed fixed-income credit analysis into a deliverable report — selecting the correct report template (Type 1–18), mapping findings to the L0/L1/L2 output tiers, rendering a multi-stakeholder dashboard, or assembling a layered credit report from an analysis artifact. Triggers on 'generate report', 'produce a credit approval report', 'build a dashboard', 'L0 signal card', or when a work-path sheet's templates must be produced. Requires an upstream analysis artifact; does not perform analysis itself.
---

## Path Resolution

See `dev/engine/agent-protocol.md` §1 — engine/ and templates/ paths resolve to the package root in both plugin-install and open-as-project modes.


## Purpose

**Engine version**: v0.1.0

**Non-Negotiables (see AGENTS.md)**: no report without a template from `dev/templates/` (never design ad-hoc HTML, dashboards, or layouts) · no numbers without a `doc §section` citation · no delivery without a QA Verdict.

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
4. **Render + CSS inline**: Use templates from `dev/templates/` to assemble the report; completeness lamp caliber follows output-layered-framework §8.4. After rendering each HTML file, make it **self-contained**: read `dev/templates/template-base.css`, inject its content into a `<style>` block in the report's `<head>`, and remove the `<link rel="stylesheet">` tag. This ensures reports render correctly when copied or forwarded — no missing CSS dependency.
5. **Naming convention**: Name rendered report files as `<issuer-slug>-type<NN>.html` where `<issuer-slug>` is a lowercase-hyphenated issuer name (e.g., `andritz-ag`) and `<NN>` is the two-digit template type number (e.g., `type01`, `type06`). This makes reports sortable and identifiable without opening them.
6. **Generate report index (when >1 reports)**: After all path reports are rendered, count the files in `rendered`. If the count (excluding `report-index.html` itself if already present) exceeds 1, generate a `report-index.html` navigation page from `dev/templates/report-index.html`. The index must:
   - Be self-contained (template-base.css inlined, same as reports — see step 4)
   - List every report file from `rendered` with: its file name, a relative-path link (e.g., `./andritz-ag-type01.html`), and a one-sentence description/summary of that report's content
   - Append `report-index.html` to the `rendered` list (NOT to `templates_used` — `templates_used` is reserved for per-path registry templates); use a relative path for portability
7. **Output Delivery Note**: Produce the Delivery Note per the schema below. All paths in `rendered` and `source_analysis` MUST be relative paths (no absolute paths) — the Delivery Note travels with the report files.

## Delivery Note Output

Template (schema single source of truth is `dev/engine/pipeline-contract.md` §2.3):

```yaml
path_id: ""                 # join key (inherited from Path Sheet, must not change)
depth: ""                   # L0|L1|L2|special (inherited from Path Sheet)
templates_used: []          # templates selected from the path's registry templates field
rendered: []                # actual report files produced (relative paths); includes report-index.html when >1 reports
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
  - ./issuer-name-type01.html
  - ./issuer-name-type06.html
  - ./report-index.html
tier_mapping:
  L0: Signal card (rating + outlook + key signals today + completeness lamp)
  L1: Snapshot (four-dimension radar + key anomalies + rating comparison)
  L2: Deep Report (pyramid layer-by-layer + dual-track cross-comparison + completeness report)
completeness_lamp: yellow (medium confidence, caliber per output-layered-framework §8.4)
source_analysis: ./analysis-artifact.yaml
```

## Chaining

- **Upstream**: `fixed-income-credit-analysis` skill — consumes its Analysis Artifact. Without an Analysis Artifact, this skill does not start (it does not perform analysis itself; go back upstream to complete analysis first).
- **REQUIRED NEXT SUB-SKILL**: `credit-qa-verifier` — after the Delivery Note is produced, hand off to the QA verification skill for pre-delivery final review (quality gates + mandatory checks); deliver only after QA passes.

## Guardrails

- **No analysis**: This skill only performs template selection, tier mapping, and assembly. It does not recalculate scores, fill in missing signals, or modify ratings. All analysis conclusions come from the upstream Analysis Artifact.
- **Do not replicate engine content**: Only reference path IDs, template names, and document sections; do not replicate any thresholds, layered time budgets, signal priority floors, or rating mappings. Tier semantics are based on `dev/engine/output-layered-framework.md`; template lists are based on `dev/engine/work-path-registry.md`.
- **Low density — no fabricated values**: Dimension scores set to null by the upstream Analysis Artifact due to insufficient density (`insufficient information to evaluate`) must retain that annotation in the report; do not fabricate values to make the report look complete.
- **Planned templates must be disclosed**: When a path's template is marked `planned`, must explicitly state "this template is under development" and provide alternative deliverable items available for that path; do not fabricate rendered output.
- **Report index rule — when >1 reports, auto-generate**: When a single engagement produces more than 1 report file, a `report-index.html` must be generated from `dev/templates/report-index.html`, linking to all reports with relative paths and descriptions. The index is appended to `rendered` only, not to `templates_used`.
- **CSS self-containment**: Every rendered HTML report must be self-contained. Read `dev/templates/template-base.css` and inline its content into each report's `<style>` block, replacing the `<link>` tag. Reports must render correctly when copied to any location or forwarded to others.
- **Relative paths only**: All file paths in the Delivery Note (`rendered`, `source_analysis`) must be relative paths. No absolute paths (e.g., a full Windows or Unix path starting with a drive letter or root slash). Reports travel together in one directory — use `./filename` not absolute paths.
- **Naming convention**: Report files follow `<issuer-slug>-type<NN>.html`. The index is `report-index.html`.

## References

- `references/report-mapping.md` — Path → template → tier mapping view (pointer only, no copied values)
- `dev/engine/pipeline-contract.md` — Four-stage chain I/O contract (artifact schema single source of truth)
- `dev/engine/work-path-registry.md` — Work path registry (`templates` field single source of truth)
- `dev/engine/output-layered-framework.md` — L0/L1/L2 tiered output (tier semantics single source of truth)
