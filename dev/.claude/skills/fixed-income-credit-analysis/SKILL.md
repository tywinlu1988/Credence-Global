---
name: fixed-income-credit-analysis
description: Use when analyzing industries or companies for credit decisions in fixed income markets, building industry analysis frameworks for lending or bond investment, evaluating credit quality via dual-track methodology, constructing investment dashboards from public data, validating frameworks against historical defaults, or assessing cross-industry contagion, portfolio concentration, and systemic risk via the system-intelligence layer. Route vague needs to the credit-analysis-router skill.
---

## Invocation Protocol

When this Skill is invoked:

1. **Path-sheet-driven (preferred).** If the user message carries a Path Sheet produced by the `credit-analysis-router` skill, read the engine documents in the sheet's `engine_reading_order` order and validate against its `quality_gates`.
2. **Direct task, no path sheet.** If the user directly names a concrete task, read the core set — `dev/engine/engine-overview.md` + `dev/engine/dual-track-methodology.md` — plus any topic-specific doc the request names (e.g. `contagion-matrix.md`, `concentration-framework.md`, `external-support-framework.md`).
3. **Vague / unrouted need.** If the need is ambiguous and no path sheet exists, first route through the `credit-analysis-router` skill, or ask the Q1–Q4 questions (role / object / depth / data) yourself to pick a path from `dev/engine/work-path-registry.md`.
4. Use **only** thresholds, weights, rating mappings, and veto rules found in those documents.
5. For every quantitative judgment, cite the source document and section.
6. If a required threshold, weight, or mapping is missing from the engine documents, output `not defined in engine` and do not invent a value.
7. Do not invoke Mode B or generate external-data values unless the user has explicitly provided a CSV upload, API endpoint, or MCP server. Treat Mode B fields as data gaps until then.

# Fixed Income Credit Analysis Engine v0.0.4

## Overview

A systematic methodology for evaluating corporate credit quality in fixed income markets. The engine operates in three layers: (1) a **Mosaic Engine** that assembles fragmented public data into coherent signals; (2) a **Dual-Track Engine** combining industry-specific multi-layer analysis pyramids with market-based pricing signals; and (3) a **System-Intelligence Layer** that models cross-industry contagion, portfolio concentration, and a market-wide Systemic Risk Index (SRI). Combines multi-stakeholder perspectives into a unified assessment framework.

**Core principles:**
1. Traditional financial analysis systematically fails in policy-driven, technology-barrier, and asset-lease industries. The heaviest credit factor is rarely on the balance sheet.
2. External credit ratings consistently lag true credit deterioration by 17+ months.
3. **Mosaic theory:** Individual public data fragments are meaningless alone; assembled together they form coherent signals.
4. **Information completeness theory:** Data gaps are not defects — they are risk signals. "We don't have this data" itself tells the user something meaningful.

## When to Use

- Building an industry credit analysis framework from scratch
- Evaluating a specific company for lending or bond investment decisions
- Constructing a multi-dimensional investment dashboard (relative value + sector allocation fit + curve positioning + event calendar)
- Assembling fragmented public data into a coherent credit assessment using mosaic theory
- Retroactively validating analytical frameworks against historical defaults
- Evaluating sovereign-linked or government-supported credit → read `dev/engine/external-support-framework.md`
- Conducting ESG/governance risk scans and fraud detection → read `dev/engine/esg-framework.md` and `dev/engine/governance-fraud-risk.md`
- Performing LGD/recovery rate analysis for default scenarios → read `dev/engine/lgd-recovery-framework.md`
- Assessing external support (government, parent company) impact on creditworthiness → read `dev/engine/external-support-framework.md`
- Evaluating financial bonds → read `dev/engine/financial-bond-framework.md`
- Analyzing holding companies → read `dev/engine/holding-company-framework.md`
- Assessing cross-industry contagion risk from a stressed issuer or sector
- Evaluating portfolio concentration across industry, region, rating, tenor, and funding-channel dimensions
- Computing the Systemic Risk Index (SRI) and interpreting the four-level thermometer
- Mapping an industry to one of the six analytical paradigms (cyclical, defensive, growth, regulated-utility, financial, sovereign-linked)

## Mandatory Density Rules (mandatory)

- Critical dimension signal density **<20%** → MUST NOT output a numeric score for that dimension; state `insufficient information to evaluate` and list the missing signals.
- Weighted-average density across scored dimensions **<50%** → MUST NOT output a final letter rating; output a qualitative directional assessment plus a prioritized gap list.
- Density 50–80% → MAY rate but MUST label `medium confidence` and widen the implied interval by ±1 notch.
- The completeness report is mandatory for every analysis; omitting it is a protocol violation.

Full confidence/density model and gap-to-risk mapping: `references/mosaic-engine-architecture.md` (threshold single source: `dev/engine/mosaic-engine.md`).

## Mode B: External Data Source Adapter (Placeholder)

> **Mode B guardrail**: Unless the user explicitly provides a CSV upload, API endpoint, or MCP server, do not invoke Mode B interfaces or generate external data values. When Mode B is not active, all Mode B fields must be treated as data gaps.

Defined but not implemented. Adapter contract (`query_bond_analytics` / `query_market_data` / `query_industry_benchmark`) and connection priority (CSV > REST API > MCP > DB): `dev/engine/mosaic-engine.md`.

## Veto & Rating Ceiling (mandatory)

- **One-vote veto**: When any analysis layer triggers a one-vote veto condition, the issuer's rating **ceiling is locked at CCC** and may not be raised. Veto conditions for each layer: `dev/engine/industry-framework.md` §5.
- Rating mapping must use the official 12-notch table (`dev/engine/dual-track-methodology.md` §6); do not create custom notches.
- For sovereign-linked entities (P6): fiscal capacity and institutional strength govern, and support willingness determines the final notch (`dev/engine/external-support-framework.md`).

## Two-Track Parallel Structure (Core)

Track A (fundamental, qualitative+scoring, L1 heaviest → L4 lightest) and Track B (market pricing: credit spreads / volatility / fund flows / rating migration) run in parallel, then feed a Cross-Comparison Matrix. Consensus reinforces; divergence is the most valuable insight.

**When tracks diverge, prioritize Track A (auditable financial facts) over Track B (external ratings).**

Full pyramid weights, Track-B thresholds, and the cross-comparison matrix: `references/industry-scoring.md` and `dev/engine/dual-track-methodology.md`.

## System-Intelligence Layer

Aggregates issuer assessments into portfolio/market signals: cross-industry contagion (19×19 matrix), five-dimensional concentration, and the Systemic Risk Index `SRI = Σ(industry_risk_score × industry_weight_pct)` (scale 0–3+).

SRI thermometer: 🟢 normal (<0.5), 🟡 watch (0.5–1.0), 🟠 alert (1.0–1.8), 🔴 danger (≥1.8).

Full specification: `references/system-intelligence.md` and `dev/engine/systemic-warning-framework.md`.

## Key Design Principles

1. Financial analysis is NEVER the heaviest layer. The heaviest factor is structural/external.
2. Each industry has a different heaviest factor determined by 10-dimension scoring.
3. Don't jump layers. L1 must pass before L2 is meaningful.
4. L4 validates, never overrules. Poor financials with strong upper layers = may be investing through cycle. Strong financials with weak upper layers = MORE dangerous (peak cycle or fraud).
5. Public data is sufficient across the 13 covered industries.
6. Track B is independent, not subordinate. Divergence generates the most valuable questions.
7. When tracks clash, prioritize auditable financial facts over external ratings.
8. Data gaps are not defects — they are risk signals. Every analysis includes a completeness report.
9. The framework identifies structural unsustainability but cannot predict default timing or specific triggers.

## Chaining

- **Upstream**: `credit-analysis-router` — consumes its Path Sheet (see Invocation Protocol).
- **Output**: After analysis completes, output the Analysis Artifact (schema at `dev/engine/pipeline-contract.md` §2.2); `path_id` is inherited from the Path Sheet.
- **Downstream (REQUIRED NEXT SUB-SKILL)**: `credit-report-builder` — hand the Analysis Artifact to this skill for report assembly; this skill does not perform report assembly.

## References

Details have been moved to `references/` (single source of truth remains `dev/engine/` engine documents):

- `references/mosaic-engine-architecture.md` — Mosaic Engine Mode A: signal confidence / density assessment / gap mapping / completeness output
- `references/industry-scoring.md` — Track A industry pyramid · six paradigms (P1-P6) · D1-D10
- `references/system-intelligence.md` — Cross-industry contagion · five-dimensional concentration · SRI thermometer
- `references/stakeholder-paths.md` — Multi-stakeholder views · portfolio manager dashboard · Path Sheet consumption guide
- `dev/.claude/skills/credit-analysis-router/SKILL.md` — Requirement interpretation / routing layer, outputs Path Sheet
- `dev/engine/work-path-registry.md` — Work path registry (path sheet single source of truth)

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1.0 | 2026-07-07 | Initial release. 10-dim scoring, 4-layer pyramid, dual-track, 7 industries, solar forward-validated |
| 0.3.0 | 2026-07-08 | Mosaic engine architecture (Mode A+B). Multi-stakeholder coverage map. P0 bond investment dashboard. Signal confidence + density metrics. Completeness reporting. Mode B adapter interface (placeholder). |
| 0.4.0-alpha | 2026-07-08 | LGD/recovery, external support, outlook/monitoring, LGFV, ESG + governance/fraud, non-credit overlay, financial bond, holding company frameworks. Layered output. Multi-stakeholder coverage completed. |
| 0.7.0-alpha | 2026-07-13 | System-intelligence layer: contagion theory/matrix, five-dimensional concentration, systemic warning (SRI), 13-industry coverage, six analytical paradigms. |
| 0.7.1-release | 2026-07-15 | Dev-stack reorganization finalized; validation artifacts separated (root validation/, never in snapshots). Version headers promoted. |
| 0.7.4 | 2026-07-15 | SKILL.md slimmed to a navigator (≤150 lines); detail sunk to `references/` (mosaic / industry / system-intelligence / stakeholder). Invocation Protocol is now path-sheet-driven (`engine_reading_order`). LGV→LGFV naming unified. |
| v0.0.1 | 2026-07-18 | International release: 19-industry GICS contagion matrix, six international paradigms (P1-P6), six buy-side roles, S&P/Moody's/Fitch rating alignment, IFRS/US GAAP framework. LGFV framework retired (China-specific). |
| v0.0.2 | 2026-07-21 | Paradigm taxonomy unified on industry-framework P1-P6; references rebuilt (ghost LGFV/Corporate-Financing references removed); outlook migration matrix completed for all 18 tiers. |
