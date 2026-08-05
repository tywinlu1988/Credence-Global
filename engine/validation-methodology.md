# Validation Methodology

**Version**: v0.3.1 | **Date**: 2026-07-10
**Source**: Fixed-Income Credit Analysis Skill Pack v0.0.10.3.0 . Black Swan Back-Testing Cases
**Date**: 2026-07-08
**Nature**: Structured Archive -- extracted and organized from existing skill packs and validation cases

---

## 1. Black Swan Back-Testing Overview

### 1.1 Validation Design Principles

1. **Strict time point limitation**: All data must be limited to publicly available information as of the analysis date -- no ex-post information or backward reasoning
2. **Dual timepoint design**: T1 at 17-18 months before default (tests medium-term warning capability), T2 at 4-5 months before default (tests short-term escalation capability)
3. **Cross-risk-genotype validation**: Cover different types of default causes -- fraud, acquisition bubble, governance failure, leverage crisis
4. **Track A + Track B independent dual-track validation**: Simultaneously validate both fundamental and market pricing paths
5. **External rating as control baseline**: Framework warning timeliness must be measured against the lag of external rating migrations

### 1.2 Core Findings (Cross-Case Summary)

- **External rating lag >17 months**: Across all validation cases, external ratings remained at AAA/A or equivalent 17-22 months before default
- **Public data sufficient for warning**: All cases showed clearly identifiable risk signals from public data at the T1 timepoint
- **Track A leads Track B**: Fundamental signals (Track A) issued warnings 6-12 months ahead of market pricing (Track B)
- **Data gaps themselves are signals**: Certain missing data (e.g., no market pricing for private entities) are themselves important risk signals

---

> **Reading guide**: §§1-5 contain the executable methodology — the 6-step
> backtest process, dual-timepoint protocol, forward-looking comparison, and
> mosaic completeness in validation. These sections are required reading
> before executing any work path that references this document.
> §§6-7 (completed case summaries, improvement record) live in


## 2. Black Swan Back-Testing Standard Process (6 Steps)

```
Step 1: Select Validation Target
  +-- Entity that experienced material default / bankruptcy
  +-- External rating >= A prior to default (tests rating lag)
  +-- Public data available before default
  +-- Output: Target declaration + default date + pre-default rating

Step 2: Determine Analysis Timepoints
  +-- T1: 17-18 months before default (tests medium-term warning)
  +-- T2: 4-5 months before default (tests short-term escalation, optional)
  +-- Timepoint selection criteria: Data availability (annual/half-year reports published)
  +-- Output: T0 analysis base date + supporting public data set list

Step 3: Reconstruct Data Environment at Analysis Timepoint
  +-- Use only information publicly available at that timepoint
  +-- Precise to documents/reports/announcements published by that date
  +-- Do not consult any ex-post information
  +-- Output: Complete data inventory for that timepoint

Step 4: Run Framework Assessment
  +-- Track A: Industry pyramid layer-by-layer (L1 to L4, no skipping)
  |   +-- Each layer score + one-vote veto check
  |   +-- Composite score + rating mapping
  +-- Track B: Market pricing four-level signals (if data available)
  |   +-- Credit spreads / Volatility / Fund flows / Rating migration
  |   +-- Four-level segmentation (Calm/Watch/Abnormal/Crisis)
  +-- Cross-validation: Four-quadrant matrix
  +-- Output: Framework assessment at T0

Step 5: Compare Against Actual Outcome
  +-- Framework conclusion vs. actual default outcome
  +-- Framework rating vs. contemporaneous external rating
  +-- Warning window length (months from T0 to default)
  +-- Output: Comparison summary

Step 6: Record Framework Findings and Improvements
  +-- What the framework got right (successful warnings)
  +-- What the framework could not have known (data limitations)
  +-- Framework improvement suggestions (weight adjustments / new indicators / new veto conditions)
  +-- Output: Framework improvement record
```

---

## 3. Dual-Timepoint Validation Method

### 3.1 Timepoint Selection Principles

| Timepoint | Time Window | Data Baseline | Validation Objective |
|---|---|---|---|
| **T1** | 17-18 months pre-default | Most recent full fiscal year annual report (published ~3-4 months before T1) | Test medium-term warning -- can risk accumulation be identified when "everything seems normal"? |
| **T2** | 4-5 months pre-default | Most recent quarterly / half-year report (published ~1-2 months before T2) | Test short-term escalation -- has risk fully materialized? Has signal density increased? |

### 3.2 T1 Assessment Key Points

```
Detection Focus:
+-- Are there structural qualitative changes? (Governance defects / Core asset divestiture / Policy shift)
+-- Degree of divergence between parent standalone vs. consolidated statements
+-- Are 2+ layers simultaneously flashing red in Track A?
+-- Is Track B showing abnormal spread widening? (>50bp jump or sustained widening trend)
+-- Is the cross-validation quadrant in "divergence"? (Track A weak but Track B strong -> market ignoring risk)
```

**T1 Acceptable Outcomes**:
- Framework identifies risk but cannot predict exact default date -> **Pass**
- Framework rating significantly lower than external rating (e.g., BBB vs AAA) -> **Framework outperforms external rating**
- Framework says "needs continued monitoring" rather than "immediately avoid" -> **Normal** (precise default prediction 17 months out is unrealistic)

### 3.3 T2 Assessment Key Points

```
Detection Focus:
+-- Have T1 signals fully escalated? (More red flags / Consistent deterioration direction)
+-- Is Track B beginning to converge with Track A? (Market finally reflecting fundamentals)
+-- Are there irreversible fatal signals? (Insolvency / Cash flow completely depleted / Core asset divestiture completed)
+-- Have any one-vote veto conditions been triggered?
```

**T2 Acceptable Outcomes**:
- Framework rating further downgraded (e.g., from BBB to CCC) -> **Pass**
- Framework issues "strongly recommend avoid/reduce position" -> **Pass**
- One-vote veto condition triggered -> **Pass**

### 3.4 Dual-Timepoint Signal Density Comparison

Compare signal density changes from T1 to T2 for each dimension:

| Dimension | T1 Signal Density | T2 Signal Density | Direction | Meaning |
|---|---|---|---|---|
| L1 Policy/Macro | 60% | 70% | Up | Policy risk signals further strengthened |
| L2 Technology/Competition | 75% | 85% | Up | Competitive disadvantage further confirmed |
| L3 Supply Chain/Operations | 45% | 65% | Up | Operational deterioration signals fully exposed |
| L4 Financial/Debt Service | 70% | 90% | Up | Financial deterioration signals fully exposed |
| Track B Market Pricing | 40% | 65% | Up | Market beginning to respond (from lag to convergence) |

---

## 4. Forward-Looking Comparison Method

### 4.1 Design Purpose

Test the framework's **differentiation capability** within the same industry -- can the framework clearly distinguish "relatively strong" from "relatively weak" entities and produce differentiated ratings before the weaker entity defaults or crashes?

### 4.2 Validation Framework: Gilead Sciences vs. Valeant Pharmaceuticals

| Item | Content |
|---|---|
| **Analysis Date** | 2015-06 (real-time, not back-testing) |
| **Industry** | Biopharmaceuticals |
| **Target A** | Gilead Sciences (GILD) -- HIV/HCV leader, massive cash flow, strong IP portfolio |
| **Target B** | Valeant Pharmaceuticals -- acquisition-driven, extremely high leverage, unsustainable pricing strategy |
| **Data Source** | 100% public data (SEC filings, clinical trial results, pricing data, rating reports) |

### 4.3 Comparative Assessment Results

| Comparison Dimension | Gilead Sciences | Valeant Pharmaceuticals |
|---|---|---|
| **Composite Score** | 7.50 | 2.00 |
| **Rating** | A- | B |
| **Rating Gap** | -- | **5.5 points** |
| **Track B** | Normal (market efficient) | Abnormal (CDS spreads widening sharply) |
| **L1 Policy/Regulatory** | Stable patent framework, favorable pricing environment for breakthrough therapies | Regulatory investigations into price hikes, political pressure on specialty pharma -> 2 pts |
| **L2 Technology/IP** | Industry-leading HIV/HCV franchise, strong pipeline -> 0 pts | No internal R&D, relies entirely on acquired products -> 2 pts |
| **L3 Operations** | High margins, established commercial infrastructure | Philidor pharmacy relationship opaque, channel risk -> 1 pt |
| **L4 Financial** | $15B cash, near-zero net debt, massive FCF | Debt/EBITDA >6x, negative FCF after interest, leverage covenant pressure -> 0 pts |

### 4.4 Unique Value of Forward-Looking Validation

| Feature | Description |
|---|---|
| **Extreme differentiation** | 5.5-point gap far exceeds any known threshold -- framework has strong discriminatory power in this industry |
| **Works without market data** | Even if Track B is unavailable for non-listed entities, the framework still functions |
| **Assesses private companies too** | IPO filings (even if withdrawn), court records, clinical trial data -> sufficient structured signals |
| **Warning timeliness** | Framework anticipates material credit events 8-24 months ahead (depending on market environment and trigger events) |

---

## 5. Mosaic Completeness in Validation

### 5.1 Signal Density Assessment per Validation Case

During validation, output signal density for each stakeholder role/dimension:

| Role/Dimension | Signal Density | Available Signal Levels | Key Gaps | Confidence |
|---|---|---|---|---|
| Credit Underwriting (M0) | 72% | L5x2, L4x4, L3x3 | Parent-subsidiary cash pooling agreement, equity pledge details | Medium-High |
| Bond Investment (M1) | 73% | L5x3, L4x5, L3x2 | Z-spread/OAS, modified duration, trade price series | Medium-High |
| Trading + Risk (M3+M4) | 58% | L4x3, L3x3, L2x3 | Bid-ask spread, CDS products (may not exist), RWA data | Medium |

### 5.2 Data Gap Treatment Principles in Validation

1. **Missing data does not mean "cannot analyze" -- it means "make judgment with available data"**
2. **Substitute signal rule**: When precise data is unavailable, use publicly available proxy indicators
3. **Annotation rule**: All substitute-signal-based judgments must be annotated as "substitute signal source" in the output
4. **Market infrastructure gaps vs. data gaps**: Market-specific data gaps (e.g., bid-ask spread not disclosed, CDS products unavailable) should be annotated as "market infrastructure gap, not a system limitation"

### 5.3 Substitute Signal Mapping Table (Validation-Proven)

| Missing Data | Substitute | Effectiveness |
|---|---|---|
| Z-spread / OAS | YTM + same-rating spread comparison | Medium -- cannot decompose finely, but sufficient for ranking |
| Modified duration + convexity | Tenor structure substitute | Medium -- precision reduced but direction correct |
| Bid-ask spread | Average daily volume + turnover rate | Medium -- cannot assess transaction cost, but can assess activity level |
| Precise trade price series | Issuance rate + spread trend | Medium-High -- trend signals more meaningful than price points |
| Private company financials | IPO filings (if available) + court records + hiring activity | Medium -- requires multi-source cross-validation |
| CDS/CRMW pricing | Issuance spread changes + stock price (if listed) | Low -- cannot precisely hedge |

---



## Related Content

- [Engine Architecture Overview](engine-overview.md) -- Core philosophy, overall architecture, design principles
- [Dual-Track Analysis Methodology](dual-track-methodology.md) -- Track A + Track B, cross-validation, rating mapping
- [Mosaic Engine](mosaic-engine.md) -- Signal extraction, assembly, completeness assessment, Mode B interface
