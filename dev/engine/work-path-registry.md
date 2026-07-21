# Work Path Registry

**Version**: v0.0.5 | **Date**: 2026-07-18

This registry is the design baseline for the v0.0.1 skill architecture refactoring (requirement understanding -> path routing -> engine invocation -> report delivery, all fully controllable). It makes all 16 work paths explicit and machine-readable, serving as the single source of truth for the Intake Router (v0.0.5) routing and execution-layer skill decomposition (v0.0.5).

**Single Source of Truth Principle**: This registry only records "which engine documents a path uses, which templates it employs, and which quality gates it must pass." It does NOT copy any thresholds, weights, or rule text -- the rule text always resides in the engine documents referenced by `engine_sequence`.

## Table of Contents

1. [Path Status Definitions](#1-path-status-definitions)
2. [Full Path Overview](#2-full-path-overview)
3. [Path Schema Definition](#3-path-schema-definition)
4. [Path Details](#4-path-details)
5. [Chaining Rules (L0->L1->L2 Escalation and Monitoring Triggers)](#5-chaining-rules-l0-l1-l2-escalation-and-monitoring-triggers)
6. [Appendix: Development Backlog](#6-appendix-development-backlog)

## 1. Path Status Definitions

| Status | Marker | Definition |
|---|---|---|
| **active** | ✅ | Fully implemented: engine documents + templates + proven use cases available, end-to-end deliverable |
| **partial** | 🟡 | Partially implemented: components (engine or template) exist but not yet assembled into an explicit path (missing entry protocol or quality gates) |
| **planned** | 🔴 | To be developed: engine/paradigm/template missing, only role requirements defined |

## 2. Full Path Overview

| ID | Path Name | Role | Investigation Direction | Depth | Template | Status |
|---|---|---|---|---|---|---|
| WP-CS-01 | Credit Selector Single-Issuer Rating | credit-selector | Industry Pyramid -> Mosaic -> Dual Track -> Rating | L2 | Type 1 + Type 6 | ✅ active |
| WP-CS-02 | Credit Selector Add-On (LGD+External Support) | credit-selector | lgd-recovery + external-support | special | Type 8 + Type 9 | 🟡 partial |
| WP-PM-01 | Portfolio Manager Investment Dashboard | portfolio-manager | PM Four-Dimension (Relative Value/Covenants/Liquidity/Events) | L2 | Type 5 | ✅ active |
| WP-PM-02 | PM Comparative Analysis | portfolio-manager | Dual-Track Comparison + Differentiation Analysis | L2 | Type 2 | 🟡 partial |
| WP-AD-01 | Advisor Origination Assessment | advisor | Issuance Window + Investor Matching + Comps Pricing | special | none | 🔴 planned |
| WP-TR-01 | Trader Market Watch Signal Card | trader | L0 Signals + SRI Thermometer Linkage | L0 | L0 Spec | 🟡 partial |
| WP-RO-01 | Risk Officer Concentration Assessment | risk-officer | Five-Dimension Concentration | special | Type 14 | ✅ active |
| WP-RO-02 | Risk Officer Cross-Industry Contagion | risk-officer | Contagion Matrix + Contagion Theory | special | Type 13 | ✅ active |
| WP-RO-03 | Risk Officer Systemic Risk Reading | risk-officer | SRI + Thermometer | special | Type 15 | ✅ active |
| WP-RO-04 | Risk Officer Portfolio Stress Test | risk-officer | Stress Scenario + Financial Deep Dive Stress Section | special | Type 11 | 🟡 partial |
| WP-II-01 | Individual Investor Decision Support | individual-investor | Financing Channel Comparison + Timing | special | none | 🔴 planned |
| WP-X-01 | Black Swan Backtest Validation | meta | validation-methodology | special | Type 3 | ✅ active |
| WP-X-02 | Multi-Role Parallel Assessment | meta | M0/M1/M4 Parallel + Cross Matrix | L2 | Type 4 | ✅ active |
| WP-X-03 | Industry Framework Builder | meta | New Industry Pyramid + D1-D10 | special | Type 7 | ✅ active |
| WP-X-04 | ESG/Governance Risk Scan | meta | esg + governance-fraud | special | Type 10 | 🟡 partial |
| WP-X-05 | Outlook & Continuous Monitoring | meta | outlook-monitoring + migration matrix | special | Type 18 | ✅ active |

> Status distribution: ✅ active 9 paths / 🟡 partial 5 paths / 🔴 planned 2 paths. See [Appendix](#6-appendix-development-backlog) for the development backlog.

## 3. Path Schema Definition

Each path is registered as a ```yaml block in [Path Details](#4-path-details) with the following fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Unique path identifier, format `WP-(CS\|PM\|AD\|TR\|RO\|II\|X)-\d{2}` (CS=credit-selector, PM=portfolio-manager, AD=advisor, TR=trader, RO=risk-officer, II=individual-investor, X=meta/special-purpose paths) |
| `name` | string | yes | Path name in English |
| `status` | enum | yes | `active` \| `partial` \| `planned` (see [Path Status Definitions](#1-path-status-definitions)) |
| `role` | enum | yes | `credit-selector` \| `portfolio-manager` \| `advisor` \| `trader` \| `risk-officer` \| `individual-investor` \| `meta` |
| `trigger` | map | yes | Trigger conditions (for router matching), with two sub-fields: `user_intent` (user intent keyword array) and `object` (analysis object) |
| `trigger.user_intent` | string[] | yes | User intent keywords for router natural language matching |
| `trigger.object` | enum | yes | `single-issuer` \| `portfolio` \| `industry` \| `market` \| `meta` |
| `depth` | enum | yes | `L0` \| `L1` \| `L2` \| `special` (output depth tier, corresponding to the output-layered-framework three tiers + special) |
| `engine_sequence` | string[] | yes | Engine document call sequence (relative repository root paths; single source of truth, content not duplicated). May be empty `[]` for planned paths |
| `paradigm_selection` | string | yes | Paradigm selection note (six paradigms mapped by industry mapping table; use `n/a` with reason when not applicable) |
| `templates` | string[] | yes | Report templates (relative repository root paths) or one of the allowed token values below |
| `outputs` | string[] | yes | Deliverable list for this path |
| `quality_gates` | string[] | yes | Quality gates, format `rule-name (doc-path §section)`; may be empty `[]` for planned paths |

**Allowed non-file token values for `templates`** (other than actual template file paths, only the following two tokens are permitted for templates not yet implemented):

| Token | Meaning | Example |
|---|---|---|
| `planned` | Template to be developed (no file), used with planned/partial status | `planned` |
| `L0-spec: <spec-doc> §section` | No standalone template file; specification defined in the referenced engine document | `L0-spec: dev/engine/output-layered-framework.md §3` |

**`quality_gates` traceability convention**: The `rule-name` (the part before `(`) must be a keyword that actually exists in one of the referenced `engine_sequence` documents and can be traced by grep (test T2.7 enforces this for active paths). The `§section` is for human-reading navigation and is not machine-validated.

## 4. Path Details

### WP-CS-01 Credit Selector Single-Issuer Rating (✅ active)

The core path: A bank relationship manager / credit selector performs credit approval ratings on a single issuer. It follows the full chain of "Industry Pyramid qualitative scoring -> Mosaic Engine signal extraction and completeness assessment -> Dual-Track cross-validation -> Rating mapping," delivering a rating + signal and data completeness report. Proven with Yongmei, Ziguang, Brilliance Auto, and other cases.

```yaml
id: WP-CS-01
name: Credit Selector Single-Issuer Rating
status: active
role: credit-selector
trigger:
  user_intent: [credit approval, credit limit, lending decision, loan approval, credit rating]
  object: single-issuer
depth: L2
engine_sequence:
  - dev/engine/industry-framework.md
  - dev/engine/mosaic-engine.md
  - dev/engine/dual-track-methodology.md
paradigm_selection: Six paradigms (per industry mapping table)
templates:
  - dev/templates/template-type1.html
  - dev/templates/template-type6.html
outputs: [rating + signals, completeness report]
quality_gates:
  - "Signal Density (dev/engine/mosaic-engine.md §4.3)"
  - "Veto (dev/engine/industry-framework.md §5)"
  - "Cross-Validation (dev/engine/dual-track-methodology.md §4)"
```

### WP-CS-02 Credit Selector Add-On (LGD+External Support) (🟡 partial)

A specialized add-on package for credit selection: on top of the WP-CS-01 main rating, it adds Loss Given Default (LGD) and External Support modules for facility-level rating, credit enhancement assessment, and support uplift determination. Both engine documents are complete, but they have not yet been assembled into an explicit add-on path with entry protocol and quality gates.

```yaml
id: WP-CS-02
name: Credit Selector Add-On (LGD+External Support)
status: partial
role: credit-selector
trigger:
  user_intent: [loss given default, LGD, recovery rate, external support, government support, credit enhancement]
  object: single-issuer
depth: special
engine_sequence:
  - dev/engine/lgd-recovery-framework.md
  - dev/engine/external-support-framework.md
paradigm_selection: n/a (Special add-on module layered on main rating; no paradigm re-selection)
templates:
  - dev/templates/template-type8.html
  - dev/templates/template-type9.html
outputs: [LGD tier + recovery rate, external support adjustment recommendation]
quality_gates:
  - "LGD Five-Tier Classification (dev/engine/lgd-recovery-framework.md §2)"
  - "Support Capacity (dev/engine/external-support-framework.md §3)"
```

### WP-PM-01 Portfolio Manager Investment Dashboard (✅ active)

A bond investor's single-instrument investment decision framework: the PM four-dimension framework (Relative Value / Covenant Protection / Liquidity / Event Calendar) weighted scoring, producing investment recommendations. Proven in Longi vs. Yidao and other cases, paired with the Type 5 dashboard template.

```yaml
id: WP-PM-01
name: Portfolio Manager Investment Dashboard
status: active
role: portfolio-manager
trigger:
  user_intent: [bond analysis, relative value, investment dashboard, buy decision, fair pricing]
  object: single-issuer
depth: L2
engine_sequence:
  - dev/engine/multi-stakeholder.md
paradigm_selection: n/a (PM four-dimension framework evaluates by instrument type, not by industry paradigm)
templates:
  - dev/templates/template-type5.html
outputs: [four-dimension score, investment recommendation]
quality_gates:
  - "Four-Dimension (dev/engine/multi-stakeholder.md §2)"
  - "Relative Value (dev/engine/multi-stakeholder.md §2.2)"
```

### WP-PM-02 PM Comparative Analysis (🟡 partial)

An investment-perspective horizontal comparison of two bonds: uses the dual-track methodology for forward-looking comparison and differentiation analysis between two issuers, answering "which one to buy." Both dual-track and validation methodology (forward comparison / differentiation) are in place, but the path has not yet been formalized as an independent investment path.

```yaml
id: WP-PM-02
name: PM Comparative Analysis
status: partial
role: portfolio-manager
trigger:
  user_intent: [bond comparison, which is better, forward comparison, differentiation, choose between]
  object: single-issuer
depth: L2
engine_sequence:
  - dev/engine/dual-track-methodology.md
  - dev/engine/validation-methodology.md
paradigm_selection: Six paradigms (each target determined per industry mapping table)
templates:
  - dev/templates/template-type2.html
outputs: [comparison score, differentiation conclusion]
quality_gates:
  - "Forward Comparison (dev/engine/validation-methodology.md §4)"
  - "Differentiation (dev/engine/validation-methodology.md §4.2)"
```

### WP-AD-01 Advisor Origination Assessment (🔴 planned)

Underwriter perspective: assesses the feasibility of underwriting a bond issuance -- issuance window judgment, investor matching, and comparable pricing. **Engine missing**: The M2/Advisor framework engine document and Type 16 origination report template are both to be developed. See [Appendix](#6-appendix-development-backlog).

```yaml
id: WP-AD-01
name: Advisor Origination Assessment
status: planned
role: advisor
trigger:
  user_intent: [underwriting feasibility, issuance window, comparable pricing, investor matching, bookbuilding]
  object: single-issuer
depth: special
engine_sequence: []
paradigm_selection: TBD (To be determined after advisor framework development)
templates:
  - planned
outputs: [underwriting feasibility conclusion, pricing range]
quality_gates: []
```

### WP-TR-01 Trader Market Watch Signal Card (🟡 partial)

A lightweight market-watch tool from the trader perspective: L0 signal card (5-second summary: rating + outlook + key signals of the day) linked with the SRI systemic warning thermometer. The L0 specification and thermometer engine are complete, but the L0 signal card has no standalone template file (the specification is defined in output-layered-framework §3), and the M3/Trader trading framework still needs to be completed.

```yaml
id: WP-TR-01
name: Trader Market Watch Signal Card
status: partial
role: trader
trigger:
  user_intent: [market watch, trading signal, daily alert, signal card, intraday warning]
  object: single-issuer
depth: L0
engine_sequence:
  - dev/engine/output-layered-framework.md
  - dev/engine/systemic-warning-framework.md
paradigm_selection: n/a (L0 signal layer is cross-paradigm; directly reads single-issuer rating + system thermometer)
templates:
  - "L0-spec: dev/engine/output-layered-framework.md §3"
outputs: [L0 signal card, thermometer reading]
quality_gates:
  - "L0 Signal Card (dev/engine/output-layered-framework.md §3)"
  - "Thermometer (dev/engine/systemic-warning-framework.md §3)"
```

### WP-RO-01 Risk Officer Concentration Assessment (✅ active)

Portfolio risk control perspective: evaluates a bond portfolio across five concentration dimensions (industry/region/rating/tenor/funding channel), producing a concentration score and adjustment recommendations. The concentration-framework is fully implemented, paired with the Type 14 template.

```yaml
id: WP-RO-01
name: Risk Officer Concentration Assessment
status: active
role: risk-officer
trigger:
  user_intent: [portfolio concentration, industry exposure, regional concentration, concentration risk, portfolio diversification]
  object: portfolio
depth: special
engine_sequence:
  - dev/engine/concentration-framework.md
paradigm_selection: n/a (Portfolio dimension cross-paradigm aggregation, mapped by holdings industry distribution)
templates:
  - dev/templates/template-type14.html
outputs: [five-dimension concentration score, concentration adjustment recommendations]
quality_gates:
  - "Five-Dimensional Concentration (dev/engine/concentration-framework.md §1)"
  - "Threshold System (dev/engine/concentration-framework.md §2.2)"
```

### WP-RO-02 Risk Officer Cross-Industry Contagion (✅ active)

Portfolio risk control perspective: uses a 19x19 contagion matrix + contagion theory to analyze cross-industry transmission risk within a portfolio, identifying high-contagion chains and escalation factors, producing a contagion path map and adjustment recommendations. Paired with the Type 13 template.

```yaml
id: WP-RO-02
name: Risk Officer Cross-Industry Contagion
status: active
role: risk-officer
trigger:
  user_intent: [contagion, spillover risk, industry transmission, contagion matrix, risk spread]
  object: portfolio
depth: special
engine_sequence:
  - dev/engine/contagion-matrix.md
  - dev/engine/contagion-theory.md
paradigm_selection: n/a (Contagion matrix is cross-paradigm; transmitted by industry pairs)
templates:
  - dev/templates/template-type13.html
outputs: [contagion path map, contagion adjustment recommendations]
quality_gates:
  - "Contagion Matrix (dev/engine/contagion-matrix.md §2)"
  - "Escalation Factor (dev/engine/contagion-matrix.md §6.1)"
  - "Transmission Path (dev/engine/contagion-theory.md §3)"
```

### WP-RO-03 Risk Officer Systemic Risk Reading (✅ active)

Portfolio / full-market perspective: aggregates multi-source signals to calculate the SRI (Systemic Risk Index), producing a four-tier thermometer reading. The systemic-warning-framework is fully implemented (including historical backtesting), paired with the Type 15 template.

```yaml
id: WP-RO-03
name: Risk Officer Systemic Risk Reading
status: active
role: risk-officer
trigger:
  user_intent: [systemic risk, SRI, thermometer, market risk, broad market risk]
  object: market
depth: special
engine_sequence:
  - dev/engine/systemic-warning-framework.md
paradigm_selection: n/a (Systemic aggregation, cross-paradigm)
templates:
  - dev/templates/template-type15.html
outputs: [SRI reading, thermometer tier]
quality_gates:
  - "Signal Aggregation (dev/engine/systemic-warning-framework.md §2)"
  - "Four-Level Thermometer (dev/engine/systemic-warning-framework.md §3)"
```

### WP-RO-04 Risk Officer Portfolio Stress Test (🟡 partial)

Portfolio risk control perspective: applies stress scenarios (five-dimension threshold jumps + financial deep dive stress section) to a portfolio, evaluating losses under extreme conditions. The concentration-framework stress section and financial-deep-dive scenario sensitivity matrix are complete, but not yet assembled into an explicit stress test path.

```yaml
id: WP-RO-04
name: Risk Officer Portfolio Stress Test
status: partial
role: risk-officer
trigger:
  user_intent: [stress test, extreme scenario, portfolio stress, sensitivity, stress scenario]
  object: portfolio
depth: special
engine_sequence:
  - dev/engine/concentration-framework.md
  - dev/engine/financial-deep-dive.md
paradigm_selection: n/a (Stress scenarios are cross-paradigm)
templates:
  - dev/templates/template-type11.html
outputs: [stress scenario loss, threshold jump results]
quality_gates:
  - "Stress Test (dev/engine/concentration-framework.md §9)"
  - "Scenario Sensitivity (dev/engine/financial-deep-dive.md §E)"
```

### WP-II-01 Individual Investor Decision Support (🔴 planned)

Enterprise (issuer) perspective reverse application: compares financing channels (bond/loan/non-standard), judges financing timing and cost. **Engine missing**: The individual investor framework engine document and Type 17 advisory template are both to be developed. See [Appendix](#6-appendix-development-backlog).

```yaml
id: WP-II-01
name: Individual Investor Decision Support
status: planned
role: individual-investor
trigger:
  user_intent: [financing channels, bond vs loan, financing timing, financing cost, how to finance]
  object: single-issuer
depth: special
engine_sequence: []
paradigm_selection: TBD (To be determined after individual investor framework development)
templates:
  - planned
outputs: [financing channel comparison, timing recommendation]
quality_gates: []
```

### WP-X-01 Black Swan Backtest Validation (✅ active)

Meta-path (validation): uses historical default / black swan events for dual-timeline backtest validation, verifying whether the framework would have issued warning signals before the default, producing validation conclusions and framework improvement recommendations. The validation-methodology is fully implemented (Yongmei/Ziguang cases), paired with the Type 3 template.

```yaml
id: WP-X-01
name: Black Swan Backtest Validation
status: active
role: meta
trigger:
  user_intent: [backtest validation, historical default, black swan, framework effectiveness, ex-post testing]
  object: meta
depth: special
engine_sequence:
  - dev/engine/validation-methodology.md
paradigm_selection: n/a (Validation methodology reuses the paradigm selection of the path under validation)
templates:
  - dev/templates/template-type3.html
outputs: [validation conclusion, framework improvement recommendations]
quality_gates:
  - "Black Swan Back-Testing (dev/engine/validation-methodology.md §1)"
  - "Dual-Timepoint (dev/engine/validation-methodology.md §3)"
```

### WP-X-02 Multi-Role Parallel Assessment (✅ active)

Meta-path (comparison): performs parallel assessment of a single issuer from multiple role perspectives (credit-selector/portfolio-manager/risk-officer), building a cross-comparison matrix to identify consensus and divergence. Multi-stakeholder §3-4 defines the standard workflow (proven in the Brilliance Auto case), paired with the Type 4 template.

```yaml
id: WP-X-02
name: Multi-Role Parallel Assessment
status: active
role: meta
trigger:
  user_intent: [multi-perspective, multi-role, parallel assessment, cross-comparison, multi-stakeholder]
  object: single-issuer
depth: L2
engine_sequence:
  - dev/engine/multi-stakeholder.md
paradigm_selection: Six paradigms (determined by the target's industry mapping table)
templates:
  - dev/templates/template-type4.html
outputs: [multi-role score matrix, consensus/divergence report]
quality_gates:
  - "Multi-Role Parallel (dev/engine/multi-stakeholder.md §4)"
  - "Cross-Role Comparison (dev/engine/multi-stakeholder.md §3.2)"
```

### WP-X-03 Industry Framework Builder (✅ active)

Meta-path (construction): builds an analysis framework for new industries -- ten-dimension scoring (D1-D10) with weight assignment, paradigm classification, and industry pyramid construction. The industry-framework is fully implemented (seven-industry pyramid specifications + veto), paired with the Type 7 template.

```yaml
id: WP-X-03
name: Industry Framework Builder
status: active
role: meta
trigger:
  user_intent: [new industry, framework building, industry pyramid, ten-dimension scoring, industry analysis]
  object: industry
depth: special
engine_sequence:
  - dev/engine/industry-framework.md
paradigm_selection: Six paradigms (paradigm assignment determined during framework construction)
templates:
  - dev/templates/template-type7.html
outputs: [industry pyramid, D1-D10 scores]
quality_gates:
  - "Ten-Dimension (dev/engine/industry-framework.md §2)"
  - "Pyramid (dev/engine/industry-framework.md §4)"
  - "Veto (dev/engine/industry-framework.md §5)"
```

### WP-X-04 ESG/Governance Risk Scan (🟡 partial)

Specialized path: scans an issuer for ESG (Environmental/Social/Governance) and financial fraud / governance risk, producing ESG overlay adjustments and governance red-flag lists. The esg-framework and governance-fraud-risk are complete, but not yet assembled into an explicit specialized path.

```yaml
id: WP-X-04
name: ESG/Governance Risk Scan
status: partial
role: meta
trigger:
  user_intent: [ESG, governance risk, financial fraud, fraud, debt evasion]
  object: single-issuer
depth: special
engine_sequence:
  - dev/engine/esg-framework.md
  - dev/engine/governance-fraud-risk.md
paradigm_selection: n/a (ESG/governance is a cross-paradigm overlay layer)
templates:
  - dev/templates/template-type10.html
outputs: [ESG risk scan, governance red-flag list]
quality_gates:
  - "ESG (dev/engine/esg-framework.md §1)"
  - "Financial Fraud (dev/engine/governance-fraud-risk.md §1)"
  - "Debt Evasion (dev/engine/governance-fraud-risk.md §4)"
```

### WP-X-05 Outlook & Continuous Monitoring (✅ active)

Specialized path: provides a 12-24 month rating outlook, maintains a 90-day watchlist, and triggers continuous monitoring (including rating migration matrix). The outlook-monitoring-framework + Type 18 template + outlook_engine coding engine are fully implemented (activated in v0.0.1).

```yaml
id: WP-X-05
name: Outlook & Continuous Monitoring
status: active
role: meta
trigger:
  user_intent: [rating outlook, continuous monitoring, watchlist, migration matrix, rating action]
  object: single-issuer
depth: special
engine_sequence:
  - dev/engine/outlook-monitoring-framework.md
paradigm_selection: n/a (Outlook and monitoring are cross-paradigm mechanisms)
templates:
  - dev/templates/template-type18.html
outputs: [rating outlook, watchlist]
quality_gates:
  - "Rating Outlook (dev/engine/outlook-monitoring-framework.md §2)"
  - "Watchlist (dev/engine/outlook-monitoring-framework.md §3)"
  - "Rating Migration Matrices (dev/engine/outlook-monitoring-framework.md §5)"
```

## 5. Chaining Rules (L0->L1->L2 Escalation and Monitoring Triggers)

This section registers **escalation triggers** (when a shallow output should escalate to a deeper path) and **monitoring triggers** (when a portfolio risk control path should re-run). This section only defines "when to switch/re-run a path," not the semantics or values of any tier itself. The single sources of truth are as follows -- this section does NOT copy any values or add any new thresholds from them:

- Definition, consumption time, and information density of L0/L1/L2 outputs: [output-layered-framework](output-layered-framework.md) §2 (three-tier output system overview) is the single source of truth;
- L0 signal card semantics and red priority signals: [output-layered-framework](output-layered-framework.md) §3 (L0 signal card) is the single source of truth;
- Rating comparison and "notch" divergence semantics: [output-layered-framework](output-layered-framework.md) §4 (L1 Snapshot - Rating Comparison) is the single source of truth;
- Signal priority numerical filter thresholds: [output-layered-framework](output-layered-framework.md) §6 (Information Priority Sorting) is the single source of truth;
- SRI thermometer four-tier numerical ranges: [systemic-warning-framework](systemic-warning-framework.md) §3 (Four-Tier Thermometer) is the single source of truth.

### Escalation Triggers (Depth Upgrade)

| Escalation | Trigger Condition | Target Path (Example) | Source (Single Source of Truth) |
|---|---|---|---|
| **L0 -> L1** | L0 signal card shows **red (high-priority) signal** | WP-TR-01 -> WP-PM-01 | output-layered-framework §3, §4 |
| **L1 -> L2** | L1 snapshot internal rating differs from external rating by **>=2 notches** | WP-PM-01 -> WP-CS-01 | output-layered-framework §4 |

- **L0 -> L1 escalation**: The L0 signal card only answers "Does this bond require my attention today?" (§3). Once a red priority signal appears, there is a matter requiring focused attention, and escalation to an L1 snapshot is warranted, using the four-dimension radar chart and key anomaly list to locate risk points.
- **L1 -> L2 escalation**: When the L1 snapshot rating comparison shows an internal rating differing from the external rating by >=2 notches, there is a divergence between the engine's judgment and the market/rating agency that merits deep investigation. Escalation to an L2 deep-dive report is warranted, using pyramid layered analysis and dual-track cross-validation to support the credit/investment decision. (>=2 is the conservative upper bound: §4 marks <=2 notches as "substantially consistent / cross-validated"; here the conservative trigger is used to deep-dive early. The escalation trigger is a workflow judgment about "when to invest deeper analysis," a different coordinate from the §4 display label; semantic authority rests with §4.)

### Monitoring Triggers (Re-run Conditions)

Risk officer (RO) portfolio paths are not one-time outputs; they re-run under the following events. Thermometer tier semantics do not add new thresholds here; they directly reference the four-tier definitions and action recommendations in [systemic-warning-framework](systemic-warning-framework.md) §3.

| Trigger Source | Trigger Event | Re-run Paths | Source (Single Source of Truth) |
|---|---|---|---|
| **Monthly SRI Reading** | Monthly systemic risk thermometer reading; when tier rises | WP-RO-03 -> triggers WP-RO-01 / WP-RO-02 | systemic-warning-framework §3 |
| **Migration Matrix Outlook Change** | Continuous monitoring hits trigger condition (enters watchlist/outlook adjustment), or migration matrix shows outlook change | WP-X-05 -> triggers related RO portfolio paths for review | outlook-monitoring-framework §4, §5 |

- **Monthly SRI Reading**: Read the systemic risk thermometer monthly (WP-RO-03). When the thermometer tier rises, follow the action recommendations for the corresponding tier in systemic-warning-framework §3, re-running WP-RO-01 (concentration) and WP-RO-02 (contagion) for high-contagion/high-concentration industries in the portfolio. Tier ranges and action recommendations are governed by that document's §3.
- **Migration Matrix Outlook Change**: When the continuous monitoring trigger mechanism in [outlook-monitoring-framework](outlook-monitoring-framework.md) §4 is hit (e.g., entry into watchlist, outlook adjustment), or when the §5 migration matrix shows a rating outlook change, re-run WP-X-05 and trigger associated portfolio path reviews.

> **Single Source of Truth Declaration**: The tier semantics, signal thresholds, and thermometer ranges referenced in this section are ultimately governed by the corresponding sections of the three engine documents cited above. If any inconsistency arises between this section and those engine documents, the engine documents prevail.

## 6. Appendix: Development Backlog

The following 🔴 gaps are the development backlog for upcoming versions. Each entry marks the missing component and the affected path:

| # | Gap | Missing Component Type | Affected Path | Notes |
|---|---|---|---|---|
| 1 | Advisor (formerly M2) framework engine document | engine | WP-AD-01 | Issuance window + investor matching + comps pricing methodology |
| 2 | Individual Investor (formerly M5) framework engine document | engine | WP-II-01 | Financing channel comparison + timing methodology |
| 3 | Trader (formerly M3) framework completion | engine | WP-TR-01 | Trader-specific engine (currently only L0 spec + thermometer, partial) |
| 4 | Type 16 origination report template | template | WP-AD-01 | Origination feasibility conclusion + pricing range report |
| 5 | Type 17 individual investor advisory template | template | WP-II-01 | Financing channel comparison + timing recommendation report |
| 6 | Outlook monitoring template | template | WP-X-05 | ✅ Delivered (v0.0.1, template-type18.html) |

> Evolution tracking: each version release should update the status distribution in this table (🔴->🟡->✅) and record it in engine-overview.md §6 Version History.
