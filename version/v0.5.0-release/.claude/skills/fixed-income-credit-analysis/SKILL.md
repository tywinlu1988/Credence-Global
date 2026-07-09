---
name: fixed-income-credit-analysis
description: Use when analyzing industries or companies for credit decisions in Chinese fixed income markets, building industry-specific analysis frameworks for bank lending or bond investment, evaluating corporate credit quality through a systematic dual-track methodology, constructing multi-dimensional investment dashboards from fragmented public data, or retroactively validating analytical frameworks against historical default events
---

# Fixed Income Credit Analysis Engine v0.5.0-release

## Overview

A systematic methodology for evaluating corporate credit quality in China's fixed income markets. The engine operates in two modes: (A) a **Mosaic Engine** that assembles fragmented public data into coherent signals, and (B) an extensible external data source adapter (architected, not yet implemented). Combines industry-specific multi-layer analysis pyramids, market-based pricing signals, and multi-stakeholder perspectives into a unified assessment framework.

**Expanded capabilities (v0.4.0+):** LGD/recovery rate framework, external support assessment, structured outlook/monitoring system, LGV (local government financing vehicle / 城投债) framework, ESG + governance/fraud detection, non-credit risk overlay, financial bond framework, holding company framework, false positive/negative testing, and layered output system with graduated confidence levels.

**Core principles:**
1. Traditional financial analysis systematically fails in policy-driven, technology-barrier, and asset-lease industries. The heaviest credit factor is rarely on the balance sheet.
2. External credit ratings consistently lag true credit deterioration by 17+ months across all validated cases.
3. **Mosaic theory:** Individual public data fragments are meaningless alone; assembled together they form coherent signals.
4. **Information completeness theory:** Data gaps are not defects — they are risk signals. "We don't have this data" itself tells the user something meaningful.

## When to Use

- Building an industry credit analysis framework from scratch
- Evaluating a specific company for lending or bond investment decisions
- Constructing a multi-dimensional investment dashboard (relative value + terms protection + liquidity + event calendar)
- Assembling fragmented public data into a coherent credit assessment using mosaic theory
- Retroactively validating analytical frameworks against historical defaults
- Designing a commercial credit intelligence product
- Evaluating LGFV (城投债) credit quality through the LGV framework
- Conducting ESG/governance risk scans and fraud detection
- Performing LGD/recovery rate analysis for default scenarios
- Assessing external support (government, parent company) impact on creditworthiness

## Mosaic Engine Architecture (Mode A — Primary)

### Signal Confidence Levels

| Level | Type | Meaning |
|---|---|---|
| L5 | Multi-source cross-validated | Same fact confirmed by >=2 independent sources |
| L4 | Single-source direct | One reliable source explicitly states |
| L3 | Derived/inferred | Assembled from multiple fragments through reasoning |
| L2 | Directional weak | Direction known, magnitude unknown |
| L1 | Missing (gap) | Data that should exist but is absent — risksignal |

### Signal Density Assessment

For each analysis dimension, compute signal density = obtained signals / expected signals.

| Density | Meaning | Impact on Scoring |
|---|---|---|
| >80% | Sufficient | High confidence, direct scoring |
| 50-80% | Moderate | Medium confidence, score +/-1 interval |
| 20-50% | Insufficient | Low confidence, directional only, mark "needs supplement" |
| <20% | Severely lacking | Cannot score, mark "insufficient data" |

### Data Gap-to-Risk Mapping

Common gaps and their risk implications:

| Gap Type | Typical Missing Data | Information Risk | Substitute Signal |
|---|---|---|---|
| Competitive data | Exact cost comparison across firms | Over/under-estimate cost advantage | SOE bidding prices (market-accepted premium) |
| Financial data | Non-listed company financials | Cannot assess financial health | Enforcement records, judicial disputes, hiring trends |
| Market pricing | No stock/bond data for non-listed firms | Track B completely unavailable | Public financing events, equity transfer prices |
| Terms data | Duration/Z-spread (no Wind terminal) | Cannot do precise rate risk analysis | YTM approximation, same-rating spread comparison |
| Liquidity data | Bid-ask spread (not disclosed in China) | Cannot assess true trading cost | Daily volume, turnover rate, abnormal volume events |

### Completeness Report Output

Every analysis MUST include a completeness report structured as:
1. Per-dimension signal density bar
2. Gaps list (prioritized by impact on conclusion)
3. Gap-to-risk mapping
4. Confidence interval on scores
5. User-actionable suggestion (e.g., "If you need precise relative value ranking, connect Wind/Choice via Mode B")

## Mode B: External Data Source Adapter (Placeholder)

Standardized interface for users to connect their own data. Defined but not implemented.

**Adapter contract:**
- `query_bond_analytics(bond_code, fields)` — duration, convexity, Z-spread, OAS, bid-ask
- `query_market_data(instrument, data_type, date_range)` — price history, volume, volatility, fund flow
- `query_industry_benchmark(industry, metric, date)` — credit spread, default rate, rating migration

**Connection methods (priority order):** CSV upload (P1) > REST API (P1) > MCP Server (P2) > Database (P3)

Full architecture specification: `references/mosaic-engine-architecture.md`

## Multi-Stakeholder Coverage

| # | Stakeholder | Core Question | Status |
|---|---|---|---|
| M0 | Credit Approval (Bank) | Can we lend? At what price? | Covered (Track A+B) |
| M1 | Bond Investment | Cheap or expensive? Terms protective? Liquid? | P0 Complete |
| M2 | Bond Underwriting (DCM) | Can we sell this? To whom? Best window? | 完成 |
| M3 | Market Trading | Rate/credit/liquidity environment? | 完成 |
| M4 | Portfolio Risk | Concentration? Stress scenario? | 完成 |
| M5 | Corporate Finance | How to finance? Which channel? When? | 完成 |

## Two-Track Parallel Structure (Core)

```
Input: Industry + Company + Analysis Date
        |
    +-------+-----------+
    |                   |
Track A: Fundamental  Track B: Market Pricing
(qualitative+scoring) (quantitative signals)
    |                   |
  L1 (Heaviest)       Credit spreads
  L2                   Volatility
  L3                   Fund flows
  L4 (Lightest)        Rating migration
    |                   |
    +-------+-----------+
            |
    Cross-Comparison Matrix
    Consensus -> reinforced
    Divergence -> most valuable insight
```

**When tracks diverge, prioritize Track A (auditable financial facts) over Track B (external ratings).**

## Track A: Industry Analysis Pyramids

Each industry type has a different heaviest factor. Weights determined by 10-dimension scoring.

| Industry Type | Conditions | L1 (Heaviest) | L2 | L3 | L4 (Lightest) |
|---|---|---|---|---|---|
| Policy-Driven | D3>=4, D4>=3 | 35% Policy/Macro | 30% Technology | 20% Supply Chain | 15% Financial |
| Tech-Barrier | D7>=3, D9>=3 | 20% Policy | 35% Tech/IP/Registration | 25% Operations | 20% Financial |
| Consolidation | D2<=3, D10>=3 | 25% Survival | 20% Technology | 30% Profit Fortress | 25% Financial |
| Asset-Lease | D5>=4, D8>=3 | 15% Policy | 20% Technology | 35% Client/Lease | 30% Financial |

**Semiconductor uses a 5-layer pyramid** (L1 Geopolitics 30-35% / L2 Technology 25-30% / L3 Market 15-20% / L4 Policy 10-15% / L5 Financial 5-10%).

**NEV uses dual-track** (OEM survival model vs supply chain profit fortress model — completely separate frameworks).

Each layer scores 0-10. Each layer has one-shot veto conditions (see `references/industry-pyramids.md`).

## Ten-Dimension Industry Scoring (D1-D10)

| # | Dimension | Definition |
|---|---|---|
| D1 | Market Size | Current domestic market size (not projected) |
| D2 | Growth Trajectory | Growth certainty over next 3-5 years |
| D3 | Policy Support | Clarity and continuity of national-level policy support |
| D4 | Policy Volatility | Frequency of policy change, risk of abrupt pivots |
| D5 | Capital Sustainability | Diversity and longevity of capital sources |
| D6 | Livelihood Linkage | Direct relationship to social stability and basic welfare |
| D7 | External Dependency | Dependence on foreign technology, equipment, materials, markets |
| D8 | Supply Chain Power Concentration | Bargaining power distribution in the value chain |
| D9 | Industry Lifecycle | Stage of industry development |
| D10 | Cyclicality | Sensitivity to macro/inventory/price cycles |

## Industry Selection Filters (C1-C4)

| Condition | Meaning | Hard Gate? |
|---|---|---|
| C1 Transaction Volume | Sufficient lending + bond/equity issuance | Yes |
| C2 Analytical Barrier | "Can't understand it just from financials" | Yes |
| C3 Practitioner Pain | Professionals actively seeking capability | No |
| C4 Data Credibility | Public data is fundamentally reliable | **Yes — hard gate** |

## Track B: Market Pricing Signals

| Level | Credit Spreads | Volatility | Fund Flows | Rating Events |
|---|---|---|---|---|
| Calm | Stable/narrowing | <3% daily | Stable/inflow | Stable |
| Watch | Widened 20-50bp | 3-5% | Moderate outflow | Outlook negative |
| Abnormal | >50bp jump or persistent | >5% sustained | Accelerated outflow | Watchlist |
| Crisis | Curve inversion/freeze | >8% or liquidity dry-up | N-bound clearing | Downgraded |

## Cross-Comparison Matrix

| | Track B: Calm | Track B: Abnormal/Crisis |
|---|---|---|
| **Track A: Good (6-10)** | Consensus | Divergence: What is market panicking about? |
| **Track A: Poor (0-5)** | Divergence: What is market ignoring? | Consensus |

## M1: Bond Investment Dashboard (P0)

Four dimensions for evaluating individual bonds:

1. **Relative Value (30%):** YTM, conversion premium, Z-spread (if available), same-industry peer comparison, same-rating comparison
2. **Terms Protection (25%):** Conversion price adjustment history, put option triggers, cross-default clauses, redemption terms
3. **Liquidity (20%):** Daily volume, turnover rate, abnormal volume events, bid-ask spread (if available)
4. **Event Calendar (25%):** Next 3 months of macro events, industry events, company events, terms triggers

Output: Integrated ranking table + individual bond assessment + data gap report.

## Data Source Architecture

**Hard constraint: Zero internal bank data. Zero non-public data. Zero paid data sources (for POC).**

| Data Layer | Source | Method |
|---|---|---|
| Macro Policy | Government official sites | WebSearch + LLM parsing |
| Industry Data | Trade associations, broker reports | WebSearch |
| Supply Chain Prices | Free data (PVInfoLink/TrendForce/SMM) | WebSearch |
| Enterprise Records | NEEQ, judgment docs, enforcement records | WebSearch |
| Bidding/Tender | Provincial procurement platforms | WebSearch |
| Bond Data | Exchange announcements, China Money | WebSearch |

**Before any analysis, verify data accessibility across 4 categories:** policy, enterprise risk, industry data, market pricing.

## Scoring Engine

```
Composite Score = Sigma(Layer Score * Layer Weight)
Layer Weight = f(Industry 10-Dimension Score)
Layer Score = Sigma(Indicator Score * Indicator Weight)
Indicator Score = f(Raw Value, Threshold, Direction)
```

**Rating Map:** 9.0-10.0 AAA | 7.5-8.9 AA/A | 6.0-7.4 BBB/BB | 4.0-5.9 B | 2.0-3.9 CCC | 0-1.9 D

## Black-Swan Retrospective Validation

Two-time-point methodology (T1: 17-18 months, T2: 4-5 months before default). All data must have been publicly available AS OF the analysis point. See `references/validation-cases.md`.

## Validated Industries & Cases

| Industry | Forward Test | Retrospective Test |
|---|---|---|
| Solar/PV | 完成 | 完成 |
| Semiconductor | 完成 | 完成 |
| Biomedicine | 完成 | 完成 |
| High-End Equipment | 完成 | 完成 |
| Medical Devices | 完成 | 完成 |
| NEV | 完成 | 完成 |
| Data Center | 完成 | 完成 |
| Coal/SOE | 完成 | 完成 |

## Key Design Principles

1. Financial analysis is NEVER the heaviest layer. The heaviest factor is structural/external.
2. Each industry has a different heaviest factor determined by 10-dimension scoring.
3. Don't jump layers. L1 must pass before L2 is meaningful.
4. L4 validates, never overrules. Poor financials with strong upper layers = may be investing through cycle. Strong financials with weak upper layers = MORE dangerous (peak cycle or fraud).
5. Public data is sufficient. POC validated across 3 black-swan cases and 3 industries.
6. Track B is independent, not subordinate. Divergence generates the most valuable questions.
7. When tracks clash, prioritize auditable financial facts over external ratings.
8. Data gaps are not defects — they are risk signals. Every analysis includes a completeness report.
9. The framework identifies structural unsustainability but cannot predict default timing or specific triggers.

## Supporting Files

- `references/industry-pyramids.md` — Complete pyramid specs for 7 industries
- `references/validation-cases.md` — Detailed case data for 3 validated defaults
- `references/mosaic-engine-architecture.md` — Full mosaic engine architecture specification
- `references/non-credit-risk-overlay.md` — Non-credit risk overlay framework
- `references/esg-framework.md` — ESG + governance/fraud detection framework
- `references/financial-bond-framework.md` — Financial bond analysis framework
- `references/holding-company-framework.md` — Holding company credit analysis framework
- `references/lgv-framework.md` — LGFV (城投债) credit analysis framework
- `references/false-positive-negative-testing.md` — False positive/negative testing methodology
- `references/output-layered-framework.md` — Layered output system specification
- `templates/report-template.html` — HTML report template (dark theme)

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1.0 | 2026-07-07 | Initial release. 10-dim scoring, 4-layer pyramid, dual-track, 7 industries, solar forward-validated |
| 0.2.0 | 2026-07-07 | Retrospective validation methodology. Yongmei (2 time points, 17-month) + Tsinghua Unigroup (17-month). Framework effective across risk genotypes. Semiconductor 5-layer pyramid. |
| 0.3.0 | 2026-07-08 | Mosaic engine architecture (Mode A+B). Multi-stakeholder coverage map. P0 bond investment dashboard (relative value + terms + liquidity + event calendar). Signal confidence levels + signal density metrics. Data gap-to-risk mapping. Completeness reporting. External data source adapter interface (placeholder). |
| 0.4.0-alpha | 2026-07-08 | LGD/recovery rate framework. External support assessment. Structured outlook/monitoring system. LGV (城投债) framework. ESG + governance/fraud detection. Non-credit risk overlay. Financial bond framework. Holding company framework. False positive/negative testing methodology. Layered output system. Multi-stakeholder coverage completed (P1/P2). All 8 industries fully validated. |
| 0.5.0-release | 2026-07-09 | Release stabilization. Complete supporting documentation for all expanded capabilities. Production-ready layered output system. Full 8-industry, 30-document, 12-template coverage. |
