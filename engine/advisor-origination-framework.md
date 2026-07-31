# Advisor Origination Assessment Framework

**Version**: v0.1.1 | **Date**: 2026-07-29 | **Status**: Published

**Module**: Fixed Income Credit Analysis Engine · Multi-Stakeholder Layer

---

> This document is the single source of truth for WP-AD-01 (Advisor Origination Assessment).
> It defines the methodology for assessing whether a bond issuance is feasible — issuance
> window judgment, investor matching, and comparable pricing. All thresholds, weights, and
> decision rules in this document are the canonical reference; downstream skills and templates
> reference them by section number.

---

> **Reading guide**: §§1-4 contain the executable methodology — thresholds,
> weights, scoring rules, and decision frameworks. These sections are required
> reading before executing any work path that references this document.
> §§5-6 contain the decision framework and quality gates — read when
> assembling the origination conclusion — read only when the analysis needs detailed justification
> or the user asks for methodological background.


## Table of Contents

- [1. Positioning in the Engine](#1-positioning-in-the-engine)
- [2. Issuance Window Assessment](#2-issuance-window-assessment)
- [3. Investor Matching](#3-investor-matching)
- [4. Comparable Pricing](#4-comparable-pricing)
- [5. Origination Feasibility Conclusion](#5-origination-feasibility-conclusion)
- [6. Quality Gates](#6-quality-gates)

---

## 1. Positioning in the Engine

### 1.1 Role

The advisor (underwriter) perspective asks: *"Can this bond be issued, at what price, to whom?"*
It is a **forward-looking origination assessment**, not a credit rating. It layers on top
of a completed credit analysis (WP-CS-01 or equivalent) and adds market-access, demand-side,
and pricing-feasibility dimensions.

### 1.2 Relationship to Other Paths

| Path | Relationship |
|---|---|
| WP-CS-01 (Single-Issuer Rating) | **Prerequisite** — origination assessment requires a completed credit rating |
| WP-PM-01 (Investment Dashboard) | Supplements demand-side assessment with relative-value context |
| WP-RO-03 (SRI Reading) | Macro conditions feed issuance-window judgment |
| WP-TR-01 (Signal Card) | Short-term market signals inform window timing |
| WP-II-01 (Financing Channel) | Complements — AD-01 assesses underwriting feasibility, II-01 recommends the issuer's optimal channel |

---

## 2. Issuance Window Assessment

### 2.1 Three Dimensions

The issuance window is assessed on three independent dimensions. Each dimension is scored
1-10; the composite determines the window grade.

| Dimension | Weight | Key Indicators |
|---|---|---|
| **Market Conditions** | 40% | Benchmark rate trend (rising/flat/falling), credit spread environment (tightening/stable/widening), primary market volume (YoY change), central bank posture |
| **Issuer-Specific Timing** | 35% | Rating outlook (stable/positive = tailwind), recent news flow (earnings/reorganization), sector rotation (in/out of favor), refinancing urgency |
| **Investor Demand Signals** | 25% | Recent comparable deal performance (oversubscription ratio), fund flow data (fixed-income inflows), investor survey sentiment, roadshow feedback if available |

### 2.2 Scoring Framework

| Score Range | Window Grade | Description |
|---|---|---|
| 8.0-10.0 | **Open** | Conditions strongly favour issuance; tight spreads, strong demand, tailwinds |
| 6.0-7.9 | **Conditional** | Issuance viable but window-sensitive; launch if no adverse events in 2 weeks |
| 4.0-5.8 | **Narrow** | Window closing; only issuers with strong demand visibility should proceed |
| 0.0-3.9 | **Closed** | Adverse conditions; recommend delay unless refinancing is urgent |

### 2.3 Market Conditions Sub-Indicators

| Indicator | Source | Scoring |
|---|---|---|
| Benchmark rate trend (3-month) | Central bank forward guidance + futures-implied path | Falling → 8-10; Flat → 5-7; Rising → 1-4 |
| Credit spread environment (IG index OAS) | Bloomberg/ICE BofA | Tightening >10bp QoQ → 8-10; Stable ±10bp → 5-7; Widening >10bp → 1-4 |
| Primary market volume (YoY) | Dealogic/Bloomberg league tables | >+20% YoY → 8-10; ±20% → 4-7; <−20% → 1-3 |
| Central bank posture | Policy rate path, QE/QT status, liquidity operations | Easing → 8-10; On hold → 5-7; Tightening → 1-4 |

### 2.4 Refinancing Urgency Override

When the issuer faces a maturity within 6 months and has no committed backup facilities,
the window grade is downgraded by one tier (e.g., Conditional → Narrow). This override
acknowledges that refinancing necessity can force issuance in suboptimal windows.

---

## 3. Investor Matching

### 3.1 Investor Segmentation

Map the proposed bond's characteristics to investor demand pools:

| Investor Type | Typical Allocation | Key Decision Factors |
|---|---|---|
| **IG Institutional** (insurance, pension) | 50-70% of IG book | Rating ≥ BBB-, duration match, ESG screen, regulatory capital treatment |
| **Total Return Funds** | 15-25% | Relative value vs. index, carry, spread-tightening potential |
| **Bank Treasury** | 5-15% | HQLA eligibility, risk-weight, internal rating alignment |
| **Retail / Private Banking** | 5-10% | Recognisable name, minimum denomination, tax treatment |
| **ETF / Passive** | Variable | Index inclusion, market-value weight, liquidity screen |

### 3.2 Matching Score

For each investor type, score 0-2:
- **2**: Strong match — bond characteristics align with decision factors
- **1**: Partial match — some characteristics align but one or two concerns
- **0**: No match — structural misalignment (rating below floor, tenor mismatch, ESG exclusion)

**Matching Composite** = sum of investor-type scores (max 10). Normalise to a 0-10 scale.

| Matching Score | Demand Assessment |
|---|---|
| 7.0-10.0 | **Broad Demand** — multiple investor types strongly aligned |
| 5.0-6.9 | **Adequate Demand** — sufficient base to fill book, but not universally attractive |
| 3.0-4.8 | **Narrow Demand** — requires targeted marketing; price concession likely |
| 0.0-2.9 | **Insufficient Demand** — high risk of failed syndication |

### 3.3 ESG Exclusion Overlay

If the issuer (or its industry) appears on the exclusion lists of major ESG-screened indices
(MSCI ESG Leaders, FTSE4Good, STOXX ESG), deduct 2 points from the matching composite.
This is a structural demand headwind independent of credit quality.

---

## 4. Comparable Pricing

### 4.1 Comparable Selection

Select 3-5 comparable bonds issued within the last 12 months. Comparables must match on:
- Industry (same GICS industry group or adjacent per contagion-matrix §1.2)
- Rating (within 2 notches on the internal scale)
- Tenor (within ±2 years of proposed issuance tenor)
- Currency and jurisdiction (same market, same governing law)

### 4.2 Pricing Adjustments

Start from the median comparable spread at issuance, then adjust:

| Adjustment Factor | Direction | Magnitude |
|---|---|---|
| Rating differential (per notch) | ±5-8bp | Linear interpolation between comparable rating and issuer rating |
| Tenor differential (per year) | ±2-3bp | Term premium per additional year |
| Size differential (>2x or <0.5x median comp size) | ±5-10bp | Liquidity premium for small issues; scarcity premium for large benchmarks |
| Market condition drift (since comp pricing date) | ± current index OAS change | Re-price comps to current market |
| Issuer-specific premium/discount | −10 to +15bp | Based on news-flow, recent deal performance, sector rotation |

### 4.3 Final Pricing Range

Recommended range: **[adjusted-median − 5bp, adjusted-median + 10bp]**.

The range is asymmetric (wider upper bound) reflecting the underwriter's conservative bias:
it is cheaper to tighten guidance than to widen it after launch.

---

## 5. Origination Feasibility Conclusion

### 5.1 Three-Outcome Framework

| Outcome | Conditions | Recommendation |
|---|---|---|
| **Go** | Window Open + Demand ≥ Adequate + Pricing range acceptable to issuer | Proceed to bookbuilding; recommended spread within range |
| **Conditional** | Window Conditional OR Demand Narrow, but not both | Launch subject to: wait for event X (e.g., earnings, FOMC), or pre-sound 2 anchor investors |
| **No-Go** | Window Closed OR Demand Insufficient OR Pricing range > issuer's maximum acceptable | Recommend delay; specify minimum conditions to revisit |

### 5.2 Sensitivity Table

For each outcome, produce a sensitivity table showing:
- **Bull case**: Window improves + demand strengthens → 10-15bp tighter pricing
- **Base case**: Current assessment
- **Bear case**: Window deteriorates + demand weakens → 15-25bp wider pricing, Conditional drops to No-Go

---

## 6. Quality Gates

The following quality gates are defined for WP-AD-01 and are the single source of truth
for QA verification:

- **Issuance Window (${CLAUDE_PLUGIN_ROOT}/engine/advisor-origination-framework.md §2)** — three-dimension window assessment with sub-indicator scoring and refinancing-urgency override
- **Investor Matching (${CLAUDE_PLUGIN_ROOT}/engine/advisor-origination-framework.md §3)** — five-segment investor matching with ESG exclusion overlay
- **Comparable Pricing (${CLAUDE_PLUGIN_ROOT}/engine/advisor-origination-framework.md §4)** — 3-5 comparable selection, five-factor pricing adjustment, asymmetric range

---

## Related Content

- [Engine Architecture Overview](engine-overview.md) — Core philosophy, overall architecture
- [Work Path Registry](work-path-registry.md) — WP-AD-01 path definition and routing
- [Dual-Track Methodology](dual-track-methodology.md) — Track B market pricing signals (feeds comparables)
- [Systemic Warning Framework](systemic-warning-framework.md) — SRI thermometer (macro conditions feed window assessment)
- [Quantitative Analysis](quantitative-analysis.md) — §7.4 issuance rate changes (market repricing signals)
- [Industry Framework](industry-framework.md) — P1-P6 paradigm classification (industry matching for comparables)
