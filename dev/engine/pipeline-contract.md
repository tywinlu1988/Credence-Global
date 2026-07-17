# Four-Stage Pipeline I/O Contract (Pipeline Contract)

**Version**: v0.8.4-release | **Date**: 2026-07-18

This contract is the **single source of truth** for the v0.8.0 skill architecture four-stage pipeline (intake -> analysis -> report -> qa). It defines the structure of four artifacts passed between the four stages, as well as the chaining edges that drive stage transitions and re-runs. The four artifacts are carried by four skills respectively:

| Stage | Artifact | Carrying Skill | Upstream | Downstream |
|---|---|---|---|---|
| S1 intake | Path Sheet | `credit-analysis-router` | -- | S2 |
| S2 analysis | Analysis Artifact | `fixed-income-credit-analysis` | S1 | S3 |
| S3 report | Delivery Note | `credit-report-builder` | S2 | S4 |
| S4 qa | QA Verdict (terminal state) | `credit-qa-verifier` | S1+S2+S3 | -- (terminal) |

**Single Source of Truth Principle**: This contract only defines the **field shapes** of the artifacts and the **structure** of the chaining edges. It does not define or copy any thresholds, SRI tiers, layered time budgets, or rating mapping values. Any numerical semantics are ultimately governed by the referenced engine document sections (see [§4](#4-single-source-of-truth-declaration)).

## 1. Four-Stage Pipeline Overview and Join Key

The four artifacts are linked by the **`path_id`** join key: `path_id` must be a work path ID registered in [work-path-registry.md](work-path-registry.md). S1 selects it via the router; S2/S3/S4 inherit it unchanged. If any stage's artifact `path_id` cannot be resolved against the registry, it constitutes a referential integrity violation (enforced by the join-key check in `scripts/consistency_check.py`).

- S1 selects `path_id`, `engine_reading_order`, and `quality_gates`, determining "which path to follow, which engines to read, which gates to pass."
- S2 executes analysis per `engine_reading_order`, producing an analysis artifact with the same `path_id`.
- S3 assembles the analysis artifact into a delivery report, producing a delivery note with the same `path_id`.
- S4 performs terminal QA on the delivery for that `path_id`, producing a QA verdict.

## 2. Artifact Schemas

The following four schemas define the field shapes in yaml fence blocks (`path_id` left empty as template placeholder). Field semantics note their single-source-of-truth sections; schemas contain no numerical values.

### 2.1 S1->S2 Path Sheet

Produced by the router. The machine-readable single source of truth for the schema is `src/path_sheet.py` (fields aligned with [work-path-registry.md](work-path-registry.md) §3).

```yaml
role: ""                    # credit-selector|portfolio-manager|advisor|trader|risk-officer|individual-investor|meta
object: ""                  # single-issuer|portfolio|industry|market|meta
depth: ""                   # L0|L1|L2|special
mode: ""                    # A=public data only / B=user explicitly provides external data sources
path_id: ""                 # join key: registered work path ID
engine_reading_order: []    # engine document sequence registered for this path (single source of truth)
quality_gates: []           # "rule-name (dev/engine/<doc>.md §section)"
notes: ""
```

### 2.2 S2->S3 Analysis Artifact

Produced by fixed-income-credit-analysis. Density/completeness semantics are governed by [mosaic-engine.md](mosaic-engine.md) §4.3/§5 as single source of truth; veto semantics by [industry-framework.md](industry-framework.md) §5; systemic reading semantics by [systemic-warning-framework.md](systemic-warning-framework.md) §3 and [concentration-framework.md](concentration-framework.md).

```yaml
path_id: ""                 # join key (inherited from path sheet, must not change)
mode: ""                    # A|B (inherited from path sheet)
findings:                   # one group of findings per engine document / paradigm
  - engine_doc: ""          # dev/engine/<doc>.md (rule source for this finding group)
    paradigm: ""            # One of six paradigms, or n/a
    signals: []             # Extracted signals (priority semantics per output-layered-framework §6)
    scores: []              # Dimension scores; dimensions below density threshold are set to null -> insufficient information for assessment
completeness:               # Completeness (scope per mosaic-engine §4.3/§5)
  density_pct: ""           # Signal density (threshold not copied; see mosaic-engine §4.3)
  confidence: ""            # High|Medium|Low
  data_gaps: []             # Gap list (gap-to-risk mapping per mosaic-engine §5.2)
veto:                       # Veto (scope per industry-framework §5)
  triggered: false
  ceiling: ""               # Rating ceiling when triggered (tier value not copied)
system_readouts:            # Systemic intelligence layer readings; only valued for risk-officer / market paths, null otherwise
  sri:
    value: ""               # SRI reading (range per systemic-warning-framework §3)
    thermometer: ""         # Thermometer tier (four-tier definition per systemic-warning-framework §3)
  concentration:
    score: ""               # Five-dimension concentration score (scope per concentration-framework)
    adjustment: ""          # Concentration adjustment to rating (per concentration-framework)
    bb_cap: ""              # Concentration cap (per concentration-framework)
mode_b_gaps: []             # External data gaps when Mode B is not activated (guardrails per mosaic-engine §6)
```

### 2.3 S3->S4 Delivery Note

Produced by credit-report-builder. Template selection is governed by the path's `templates` field in [work-path-registry.md](work-path-registry.md). L0/L1/L2 layered semantics are governed by [output-layered-framework.md](output-layered-framework.md) §2/§3/§5.

```yaml
path_id: ""                 # join key (inherited from path sheet, must not change)
depth: ""                   # L0|L1|L2|special (inherited from path sheet)
templates_used: []          # Templates selected from the path's registry templates field (single source of truth)
rendered: []                # Actually produced report files (from dev/templates/)
tier_mapping:               # Analysis artifact -> L0/L1/L2 tier (semantics per output-layered-framework §2/§3/§5)
  L0: ""
  L1: ""
  L2: ""
completeness_lamp: ""       # Completeness indicator (scope per output-layered-framework §8.4)
source_analysis: ""         # Upstream analysis artifact reference (traceability)
```

### 2.4 S4 QA Verdict (Terminal State)

Produced by credit-qa-verifier, the terminal state of the four-stage pipeline. Each quality gate is re-checked from the path sheet's `quality_gates`. The rule sources for four mandatory checks are found in the referenced engine document sections.

```yaml
path_id: ""                 # join key (inherited from path sheet, must not change)
verdict: ""                 # pass|pass-with-findings|fail
gate_results:               # Per-gate re-check results
  - gate: ""                # "rule-name (dev/engine/<doc>.md §section)" (inherited from path sheet quality_gates)
    status: ""              # pass|fail
    evidence: ""            # Re-check evidence (references engine document sections, does not copy values)
mandatory_checks:           # Mandatory checks (rule sources per respective engine documents)
  density_rule: ""          # Signal density rule (mosaic-engine §4.3)
  veto_ceiling: ""          # Veto rating ceiling (industry-framework §5)
  mode_b: ""                # Mode B hallucination guardrail (mosaic-engine §6)
  single_source: ""         # Single source of truth compliance (do not fabricate thresholds)
remediation: []             # Remediation recommendations for non-passing items
```

## 3. Chaining Edges (Machine-Readable)

The following edges are the machine-readable representation of [work-path-registry.md](work-path-registry.md) §5 chaining rules, with fields `id` / `from` / `to` / `trigger` / `source_doc_ref`. This contract only codifies the topology of **when to switch/re-run paths**; all numerical trigger semantics are ultimately governed by the engine document sections referenced in `source_doc_ref` and are not copied here.

- Escalation triggers (depth upgrade): L0->L1, L1->L2 tier semantics per [output-layered-framework.md](output-layered-framework.md) §2/§3/§4.
- Monitoring triggers (re-run conditions): Risk officer portfolio paths re-run under thermometer / migration matrix events; tier semantics per [systemic-warning-framework.md](systemic-warning-framework.md) §3 and [outlook-monitoring-framework.md](outlook-monitoring-framework.md) §4/§5.

```yaml
chaining_edges:
  - id: edge-l0-to-l1-upgrade
    from: WP-TR-01
    to: [WP-PM-01]
    trigger: L0 signal card shows red (high-priority) signal
    source_doc_ref: dev/engine/output-layered-framework.md §3, §4
  - id: edge-l1-to-l2-upgrade
    from: WP-PM-01
    to: [WP-CS-01]
    trigger: L1 snapshot internal rating differs from external rating by >=2 notches
    source_doc_ref: dev/engine/output-layered-framework.md §4
  - id: edge-ro-monthly-sri-rerun
    from: WP-RO-03
    to: [WP-RO-01, WP-RO-02]
    trigger: Monthly SRI thermometer tier rises; re-run concentration and contagion for high-contagion/high-concentration industries in portfolio
    source_doc_ref: dev/engine/systemic-warning-framework.md §3
  - id: edge-migration-matrix-rerun
    from: WP-X-05
    to: []            # Open set: registry §5 does not enumerate, only states "related RO portfolio paths", so not hard-coded here
    to_ref: dev/engine/work-path-registry.md §5
    trigger: Continuous monitoring hits trigger condition (watchlist/outlook adjustment), or migration matrix shows outlook change; re-run WP-X-05 and trigger related portfolio path review
    source_doc_ref: dev/engine/outlook-monitoring-framework.md §4, §5
```

> **Topology Note**: `from`/`to` are work path IDs from the registry. `to` as a **list** indicates an enumerated closed set (e.g., `edge-ro-monthly-sri-rerun`, where registry §5 explicitly specifies "WP-RO-01 / WP-RO-02"). `to` as an **empty list + `to_ref`** indicates an open set not enumerated in the registry; the specific set is governed by the registry section referenced by `to_ref` (e.g., `edge-migration-matrix-rerun` -> §5 "related RO portfolio paths"). A monitoring trigger's "re-run" includes self-reference (e.g., `edge-migration-matrix-rerun` also re-runs WP-X-05 itself).

## 4. Single Source of Truth Declaration

- This contract defines the field shapes of four artifacts and the topology of chaining edges. It is the **sole authoritative definition** for the four-stage pipeline I/O; each skill document references this contract and does not re-define artifact structures independently.
- This contract **does not copy** any thresholds, SRI thermometer tiers, L0/L1/L2 tier time budgets, signal priority thresholds, or rating mapping values. The single sources of truth for these values are respectively: [mosaic-engine.md](mosaic-engine.md) (signal density/completeness), [industry-framework.md](industry-framework.md) §5 (veto ceiling), [systemic-warning-framework.md](systemic-warning-framework.md) §3 (SRI thermometer), [output-layered-framework.md](output-layered-framework.md) §2/§3/§5/§6 (tiering and priority), [dual-track-methodology.md](dual-track-methodology.md) §6 (rating mapping), and [concentration-framework.md](concentration-framework.md) (five-dimension concentration).
- If any inconsistency arises between this contract and the above engine documents, the engine documents prevail. Path topology (16 paths' status / `templates` / `engine_sequence` / `quality_gates`) is governed by [work-path-registry.md](work-path-registry.md) as the single source of truth.
