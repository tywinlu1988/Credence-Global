# Systemic Warning Framework — Signal Aggregation Algorithm + Thermometer + Historical Backtests

**Version**: v0.0.3 | **Date**: 2026-07-10 | **Status**: Released

---

## Table of Contents

1. [Design Philosophy and Positioning](#1-design-philosophy-and-positioning)
2. [Signal Aggregation Algorithm](#2-signal-aggregation-algorithm)
3. [Four-Level Thermometer System](#3-four-level-thermometer-system)
4. [Industry Weights and Contagion Coefficients](#4-industry-weights-and-contagion-coefficients)
5. [Historical Backtest 1: GFC 2008 (Pre-Lehman)](#5-historical-backtest-1-gfc-2008-pre-lehman)
6. [Historical Backtest 2: Eurozone Sovereign Debt Crisis 2011-12](#6-historical-backtest-2-eurozone-sovereign-debt-crisis-2011-12)
7. [Historical Backtest 3: COVID-19 Shock 2020](#7-historical-backtest-3-covid-19-shock-2020)
8. [Current Period Calculation: Scenario-Based SRI Example](#8-current-period-calculation-scenario-based-sri-example)
9. [Threshold Sensitivity Analysis](#9-threshold-sensitivity-analysis)
10. [Integration with Existing Engine](#10-integration-with-existing-engine)
11. [Limitations Statement](#11-limitations-statement)
12. [Appendix](#12-appendix)

---

## 1. Design Philosophy and Positioning

### 1.1 Why a Systemic Warning Framework?

The existing engine has established comprehensive individual credit analysis systems (Dual-Track Methodology, Industry Pyramid, Contagion Matrix, Concentration Framework), but lacks a **top-level dashboard that aggregates scattered industry signals into a systemic risk index**.

| Existing Tool | Coverage | Output | Limitation |
|--------------|----------|--------|------------|
| Dual-Track Analysis (M1-M2) | Single issuer | Individual rating | Cannot see the big picture |
| Industry Pyramid | Single industry | Industry score | Cannot aggregate across industries |
| Contagion Matrix | Industry pairs | Contagion intensity matrix | Static structure, no real-time reading |
| Concentration Framework | Portfolio | Five-dimensional risk score | Focuses on portfolio, not entire market |
| **Systemic Warning Framework (this document)** | **Full market, 19 industries** | **SRI Index + Thermometer** | **Fills the "last mile" gap** |

### 1.2 Framework Position in the Overall Engine

```
Input Layer:
  Track A ratings for 19 industries (fundamental scores)
  Track B signals for 19 industries (market pricing signals)
  Outlook direction for 19 industries (positive/stable/negative)
         │
         ▼
Aggregation Layer: (This document · Systemic Warning Framework)
  Signal aggregation algorithm → SRI calculation
  Four-level thermometer determination
  Historical backtest validation
         │
         ▼
Output Layer:
  🔴🟠🟡🟢 Systemic risk level
  Action recommendations
  Contagion escalation factor linkage
         │
         ▼
Portfolio Risk Control Layer (M4):
  Concentration adjustment
  Stress testing
  Limit management
```

> **SRI Scope Note:** The SRI is a **systemic industry risk index** that aggregates industry risk scores for the 19 industries. It does not directly receive portfolio concentration scores. Concentration risk is assessed through the independent Five-Dimensional Concentration Framework. The two run in parallel at the M4 Portfolio Risk Control Layer. If a merger is desired in the future, the merger formula must be explicitly defined.

### 1.3 Design Principles

| Principle | Meaning |
|-----------|---------|
| **Full Signal Coverage** | Include all Track A + Track B + Outlook signals for all 19 industries, no omissions |
| **Contagion Weighted** | Not a simple arithmetic average — industry weights are jointly determined by credit bond outstanding and contagion coefficients |
| **Transparent Thresholds** | All four thermometer level thresholds have theoretical or historical basis, no black box |
| **Verifiable via Backtests** | Must pass at least 3 historical event backtests to validate framework effectiveness |
| **Current Readability** | Must be able to calculate real-time SRI readings based on current data for daily monitoring |

---

## 2. Signal Aggregation Algorithm

### 2.1 Input Definitions

The Systemic Risk Index (SRI) takes inputs from four types of signals from the existing engine:

**Signal A: Track A Industry Score**

Derived from each industry's Dual-Track Analysis Track A composite score (0-10), reflecting the health of industry fundamentals.

| Score Range | Corresponding Rating (12-notch) | Industry Health |
|------------|-------------------------------|-----------------|
| 9.5 - 10.0 | AAA | Robust |
| 9.0 - 9.4 | AA+ | Robust |
| 8.5 - 8.9 | AA | Robust |
| 8.0 - 8.4 | AA- | Robust |
| 7.5 - 7.9 | A+ | Good |
| 7.0 - 7.4 | A | Good |
| 6.5 - 6.9 | A- | Good |
| 6.0 - 6.4 | BBB+ | Moderate |
| 5.5 - 5.9 | BBB | Moderate |
| 5.0 - 5.4 | BBB- | Moderate |
| 4.5 - 4.9 | BB+ | Weak |
| 4.0 - 4.4 | BB | Weak |
| 3.5 - 3.9 | BB- | Weak |
| 3.0 - 3.4 | B+ | Fragile |
| 2.5 - 2.9 | B | Fragile |
| 2.0 - 2.4 | B- | Fragile |
| 1.0 - 1.9 | CCC | Dangerous |
| 0 - 0.9 | D | Dangerous |

**Signal B: Track B Market Signal**

Derived from each industry's Track B four-level signal system (Calm/Watch/Abnormal/Crisis), reflecting the degree of market pricing alarm.

| Track B State | Score Mapping | Color Mark |
|--------------|--------------|-----------|
| Calm | 0 points | 🟢 |
| Watch | 0.5 points | 🟡 |
| Abnormal | 1.0 points | 🟠 |
| Crisis | 1.5 points | 🔴 |

**Signal C: Outlook Direction**

Derived from each industry's outlook assessment (Positive/Stable/Negative).

| Outlook Direction | Risk Weight |
|-----------------|------------|
| Positive | 0 points |
| Stable | 0 points |
| Negative | +0.5 points |

**Signal D: Veto Trigger**

When an industry triggers a veto condition as defined in the Dual-Track Methodology (see [Dual-Track Methodology](dual-track-methodology.md) §2.5), the industry's risk score is forced to the maximum level.

### 2.2 Core Aggregation Formula

```
SRI = Σ(Industry Risk Score × Industry Weight Percentage)
```

Where industry weight percentage is each industry's share of the total weight (normalized to 100%), ensuring Σ(Industry Weight Percentage) = 1.

> **Dimension Note:** The SRI uses a continuous 0-3+ scale, not a percentage system. Temperature cards, report templates, and the output framework must all use the same scale — mixing with a 0-100 system is prohibited.

The SRI ranges from 0 to 3+, corresponding to the four-level thermometer system (see §3).

#### 2.2.1 Industry Risk Score

A single industry's risk score is calculated from three types of signals:

```
Industry Risk Score = base_score + outlook_penalty + trackB_penalty

Where:
  base_score is determined by Track A score:
    Track A < 3.0 (CCC/B)           →  3 points  (High Risk)
    3.0 ≤ Track A < 5.0 (B/BB)      →  2 points  (Medium-High Risk)
    5.0 ≤ Track A < 6.0 (BBB)       →  1 point   (Medium Risk)
    6.0 ≤ Track A ≤ 10.0 (A and above) → 0 points  (Low Risk)
  
  outlook_penalty:
    Negative outlook  →  +0.5 points
    Stable outlook    →  0 points
    Positive outlook  →  0 points
  
  trackB_penalty:
    Track B signal 🟢 (Calm)     →  0 points
    Track B signal 🟡 (Watch)    →  +0.5 points
    Track B signal 🟠 (Abnormal) →  +1.0 points
    Track B signal 🔴 (Crisis)   →  +1.5 points

  Veto Check:
    If the industry triggers a veto condition → Industry Risk Score = 3 points (forced)
```

#### 2.2.2 Industry Risk Score Quick Reference

| Track A Score | Base Score | Negative Outlook | Track B 🔴 (Crisis) | Both Triggered | Veto |
|--------------|-----------|-----------------|-------------------|---------------|------|
| > 6.0 (A and above) | 0 | 0.5 | 1.5 | 2.0 | 3.0 |
| 5.0-6.0 (BBB- to BBB+) | 1 | 1.5 | 2.5 | 3.0 | 3.0 |
| 3.0-5.0 (B+ to BB+) | 2 | 2.5 | 3.0 | 3.0 | 3.0 |
| < 3.0 (CCC/B) | 3 | 3.0 | 3.0 | 3.0 | 3.0 |

**Threshold Rationale:**

| Base Score Threshold | Theoretical Basis |
|--------------------|-------------------|
| Track A > 6.0 → 0 points | Corresponds to A- and above, upper investment grade, industry fundamentals robust, systemic risk contribution negligible |
| 5.0-6.0 → 1 point | Corresponds to BBB range (BBB- to BBB+), lower investment grade, industry showing vulnerability but not systemic threat |
| 3.0-5.0 → 2 points | Corresponds to BB/B range (B+ to BB+), speculative grade, industry facing substantial challenges, needs inclusion in risk count |
| < 3.0 → 3 points | Corresponds to CCC/D grade, industry in dangerous state, core contributor to systemic risk |

| Penalty Factor | Magnitude | Rationale |
|---------------|-----------|-----------|
| Negative Outlook +0.5 | 0.5 points | Negative outlook is a forward signal for rating downgrade in the next 6-12 months, but does not constitute current risk — half-notch penalty |
| Track B 🟡 +0.5 | 0.5 points | Watch-level market signal may reflect early risk or short-term noise — half-notch penalty |
| Track B 🟠 +1.0 | 1.0 points | Abnormal market signal reflects significantly amplified pricing divergence — full-notch penalty |
| Track B 🔴 +1.5 | 1.5 points | Crisis market signal reflects liquidity or confidence shock — one-and-a-half notch penalty |
| Veto → 3 points | Forced 3 points | Veto represents existential risk; regardless of other indicators, the industry is directly classified as high risk |

### 2.3 Industry Weights

```
Industry Weight = Bond Outstanding Weight × Contagion Coefficient

Where:
  Bond Outstanding Weight = Industry's share of total outstanding bonds across all 19 industries
  
  Contagion Coefficient = Industry's "Super-Spreader" score in contagion-matrix.md
                          / Mean contagion score across 19 industries
  
  Normalization: Final industry weight percentages are normalized across industries,
                 ensuring Σ(Industry Weight Percentage) = 1 (i.e., 100%)
```

#### 2.3.1 Contagion Coefficient Table

According to the [Contagion Matrix](contagion-matrix.md) §5.1 (Super-Spreaders) and §9.2 (Complete Row/Column Sums), the contagion scores for the 19 industries are as follows:

<!-- GENERATED:sri-contagion-coefficients -->
| Rank | Industry | Total Contagion Score (Row Sum) | Contagion Coefficient | Classification Label |
|------|----------|-------------------------------|----------------------|--------------------|
| 1 | Financials (Banks/Insurance) | 47 | 47 / 34.84 = 1.349 | Super-Spreader |
| 2 | Capital Goods | 43 | 43 / 34.84 = 1.234 | Super-Spreader |
| 3 | Chemicals | 42 | 42 / 34.84 = 1.205 | Super-Spreader |
| 3 | Technology Hardware (Semiconductors) | 42 | 42 / 34.84 = 1.205 | Super-Spreader |
| 5 | Energy (Oil & Gas) | 41 | 41 / 34.84 = 1.177 | Quasi Super-Spreader |
| 6 | Transportation | 39 | 39 / 34.84 = 1.119 | Quasi Super-Spreader |
| 7 | Sovereigns & GSEs | 37 | 37 / 34.84 = 1.062 | Quasi Super-Spreader |
| 8 | Metals & Mining | 35 | 35 / 34.84 = 1.005 | Quasi Super-Spreader |
| 9 | Software & Services | 34 | 34 / 34.84 = 0.976 | Moderate Contagion |
| 10 | Automobiles | 33 | 33 / 34.84 = 0.947 | Moderate Contagion |
| 11 | Construction Materials | 32 | 32 / 34.84 = 0.918 | Moderate Contagion |
| 11 | Utilities (Regulated) | 32 | 32 / 34.84 = 0.918 | Moderate Contagion |
| 13 | Commercial Services | 31 | 31 / 34.84 = 0.890 | Weak Contagion |
| 13 | Consumer Durables | 31 | 31 / 34.84 = 0.890 | Weak Contagion |
| 13 | Retail | 31 | 31 / 34.84 = 0.890 | Weak Contagion |
| 16 | Telecommunications | 29 | 29 / 34.84 = 0.832 | Weak Contagion |
| 17 | Biotech & Pharma | 28 | 28 / 34.84 = 0.804 | Weak Contagion |
| 17 | Consumer Staples | 28 | 28 / 34.84 = 0.804 | Weak Contagion |
| 19 | Healthcare Equipment | 27 | 27 / 34.84 = 0.775 | Weakest Contagion |
| | **Mean** | **34.84** | **1.000** | |
<!-- /GENERATED -->

**Calculation Notes:**
- Mean of 19 industry contagion scores = 662 / 19 = 34.84 (machine-generated from the §2.1 heatmap via `scripts/build_contagion_derived.py`)
- Contagion Coefficient > 1.0 = Contagion above mean (weight increase)
- Contagion Coefficient < 1.0 = Contagion below mean (weight decrease)
- Super-spreaders (Financials 47, Capital Goods 43, Chemicals/TechHW 42) all have coefficients significantly > 1.0, receiving higher weights in SRI calculation

#### 2.3.2 Bond Outstanding Weights

The SRI weights are **inputs supplied at analysis time**, not constants baked into the engine: use the latest sector composition of the relevant international benchmark (e.g., Bloomberg Global Aggregate / ICE BofA index sector weights, SIFMA/AFME issuance statistics). The table below is an **illustrative starting point** for an international IG/HY blended universe — replace with live data in production:

| Industry | Illustrative Outstanding Share | Note |
|----------|------------------------------|------|
| Financials (Banks/Insurance) | approx. 30% | Largest corporate-bond sector globally |
| Sovereigns & GSEs | approx. 20% | Depends on whether the mandate includes quasi-sovereign |
| Utilities (Regulated) | approx. 8% | Classic bond-financed sector |
| Energy (Oil & Gas) | approx. 7% | Integrated + independent issuers |
| Telecommunications | approx. 5% | Tower/network capex financed in bonds |
| Technology Hardware (Semis) | approx. 4% | Large IG issuers + HY memory |
| Transportation | approx. 4% | Rail/airline equipment trusts, shipping |
| Capital Goods | approx. 4% | Diversified industrials |
| Consumer Staples | approx. 4% | Defensive IG issuers |
| Chemicals | approx. 3% | Commodity + specialty |
| Automobiles | approx. 3% | OEM + captive finance |
| Healthcare Equipment | approx. 2% | MedTech IG |
| Biotech & Pharma | approx. 2% | Large pharma IG; biotech mostly equity |
| Software & Services | approx. 2% | Growing IG tech issuance |
| Metals & Mining | approx. 2% | HY-tilted |
| Construction Materials | approx. 2% | Cement/building products |
| Consumer Durables | approx. 1% | Discretionary HY |
| Retail | approx. 1% | Mixed IG/HY |
| Commercial Services | approx. 1% | Staffing/services HY |

**Note:** These shares are directional illustrations only. In actual calculations, use the latest index/benchmark sector weights and adjust promptly on structural change (e.g., sovereign issuance surges, sector-specific refinancing waves).

#### 2.3.3 Industry Weight Calculation Example

Using Technology Hardware (Semis) as an example, assuming bond outstanding share is 4% (illustrative §2.3.2 value):

```
TechHW Industry Weight Percentage = 4% × 1.205 = 4.82%

Normalization:
  Raw weight percentage per industry = Bond outstanding share × Contagion coefficient
  Normalization factor = 100% / Σ(Raw weight percentage)
  Final weight percentage = Raw weight percentage × Normalization factor
  Ensures Σ(Final weight percentage) = 100%
```

### 2.4 Complete Calculation Flow

```
Step 1: Collect four types of input signals for the 19 industries
  ├── Track A score (fundamental pyramid output)
  ├── Track B signal (market signal level)
  ├── Outlook direction (positive/stable/negative)
  └── Veto trigger (yes/no)

Step 2: Calculate single industry risk score
  └── base_score + outlook_penalty + trackB_penalty
  └── Veto check → if triggered, force 3 points

Step 3: Calculate industry weight percentage
  ├── Credit bond outstanding weight ← market data
  ├── Contagion coefficient ← Contagion Matrix (contagion-matrix.md) §9.2
  └── Industry weight percentage = outstanding weight × contagion coefficient (normalized to sum 100%)

Step 4: Calculate SRI
  └── SRI = Σ(Industry risk score × Industry weight percentage)

Step 5: Thermometer determination
  └── Check against four-level thresholds, output 🔴/🟠/🟡/🟢 level

Step 6: Action recommendation output
  └── Output corresponding action recommendations based on thermometer level
```

### 2.5 Input Signal Data Sources

| Signal Type | Source Document | Update Frequency |
|-------------|---------------|-----------------|
| Track A Score | [Dual-Track Methodology](dual-track-methodology.md) §2 | Quarterly (or when significant industry changes occur) |
| Track B Signal | [Dual-Track Methodology](dual-track-methodology.md) §3 | Weekly/Daily |
| Outlook Direction | [Outlook Monitoring Framework](outlook-monitoring-framework.md) | Monthly/Quarterly |
| Veto Conditions | [Industry Framework](industry-framework.md) §5 | Event-driven |
| Credit Bond Outstanding Weight | Market data terminals, industry bond outstanding statistics | Quarterly update |
| Contagion Coefficient | [Contagion Matrix](contagion-matrix.md) §5.1 and §9.2 | Updated on version changes |

---

## 3. Four-Level Thermometer System

### 3.1 Four-Level Definition

| Level | SRI Range | Color | Meaning |
|-------|-----------|-------|---------|
| Normal | SRI < 0.5 | 🟢 | < 20% of industries simultaneously red (risk score ≥ 2) · or > 70% of industries green (risk score = 0) |
| Watch | 0.5 ≤ SRI < 1.0 | 🟡 | 20-30% of industries simultaneously red · or 2-3 industries with overlapping signals (negative outlook + Track B abnormal) |
| Alert | 1.0 ≤ SRI < 1.8 | 🟠 | 30-50% of industries simultaneously red · or high-contagion industries (super-spreaders) in trouble |
| Danger | SRI ≥ 1.8 | 🔴 | > 50% of industries simultaneously red · or multiple high-contagion industries triggered simultaneously · or systemic contagion risk present |

### 3.2 Qualitative Descriptions for Each Level

#### 🟢 Normal (SRI < 0.5)

**Market State:** Most industries have healthy fundamentals, overall credit risk is manageable. A few industries have localized issues with limited impact.

**Industry Signal Characteristics:**
- Vast majority of industries have Track A score > 6.0 (A- and above)
- No industry triggers veto
- No more than 2 industries with negative outlook
- Track B signals are predominantly 🟢 and 🟡

**Historical Reference Periods:**
- Post-crisis recovery periods (credit risk low)
- Bull market expansion phases (between default waves)

**Action Recommendations:**
- Routine monitoring, maintain existing portfolio allocation
- Quarterly review of Track A scores for each industry
- Monitor trends in contagion matrix escalation factors

#### 🟡 Watch (0.5 ≤ SRI < 1.0)

**Market State:** Some industries showing risk signals, but not yet forming systemic risk. Increased monitoring frequency required, check concentration risk.

**Industry Signal Characteristics:**
- 2-3 industries with Track A score < 5.0 (entering fragile range)
- Or 1-2 industries with overlapping negative outlook + Track B abnormal signals
- Super-spreader industries remain stable, no severe signals

**Historical Reference Periods:**
- Pre-Lehman period, Q3 2008 (see §5 backtest)
- Early phases of credit tightening cycles

**Action Recommendations:**
- Focus on industries that turned red — check their contagion and vulnerability rankings in the contagion matrix
- If the red-turned industry is a weak contagion (Food & Beverage / Textile & Apparel / Biopharmaceuticals) → continue observing
- If the red-turned industry is a super-spreader (Financials / Capital Goods / Chemicals / Tech Hardware) → immediately upgrade to Alert level
- Check portfolio exposure to red-turned industries against concentration limits
- Increase monitoring frequency from monthly to bi-weekly

#### 🟠 Alert (1.0 ≤ SRI < 1.8)

**Market State:** Multiple industries stressed simultaneously, or high-contagion industries (super-spreaders) showing severe signals. Systemic risk is accumulating, requiring active reduction of risk exposure.

**Industry Signal Characteristics:**
- 4-6 industries with Track A score < 5.0
- Or 1-2 super-spreader industries trigger veto or Track A < 3.0
- Or 2+ super-spreader industries simultaneously entering watch state
- At least 2 contagion matrix escalation factors triggered simultaneously

**Historical Reference Periods:**
- Eurozone sovereign debt crisis 2011-12 (see §6 backtest)
- Systemic financial crisis peaks

**Action Recommendations:**
- Actively reduce exposure to high-risk and super-spreader industries
- Check if the portfolio is simultaneously exposed to multiple industries in the same high-contagion cluster (e.g., Cluster A: Semiconductors + Solar/PV + Advanced Equipment)
- Increase hedging tools (interest rate derivatives, CDS)
- Shorten portfolio duration
- Initiate portfolio stress tests (Contagion Matrix M4 stress test procedure)
- Limit new exposure to high-risk industries
- Report to risk committee

#### 🔴 Danger (SRI ≥ 1.8)

**Market State:** Over half of industries simultaneously in risk state, or multiple high-contagion industries triggering severe signals simultaneously. Market facing systemic risk, enter full defense mode.

**Industry Signal Characteristics:**
- > 7 industries with Track A score < 5.0
- Or 2+ super-spreader industries simultaneously triggering veto or Track A < 3.0
- Or 3+ super-spreader industries simultaneously entering abnormal state
- Panic sentiment or high-leverage factors among contagion matrix escalation factors already triggered

**Historical Reference Periods:**
- COVID-19 shock Q1 2020 (see §7 backtest)
- Multi-crisis systemic events

**Action Recommendations:**
- Full defense — prioritize liquidity preservation
- Significantly reduce exposure to risk industries (reduce positions by 50%+)
- Retain only safest assets (sovereign bonds, AAA short-term notes)
- Increase cash reserves
- Suspend all new risk exposure
- Trigger liquidity contingency plan
- Monitor SRI changes and contagion matrix escalation factors daily
- Prepare portfolio restructuring plan for extreme stress scenarios

### 3.3 Threshold Theoretical Basis

#### SRI < 0.5 (🟢 Normal) Threshold Rationale

| Basis Type | Specific Rationale |
|-----------|-------------------|
| **Statistical** | When SRI < 0.5, the average risk score across 19 industries is approximately equivalent to 2 industries scoring 2 + 17 scoring 0, or 4 industries scoring 1 + 15 scoring 0 — meaning only 1-2 industries at medium-high risk or 2-3 at medium risk. This falls within normal market differentiation |
| **Historical Validation** | During post-crisis recovery periods, credit bond market default rates were below 0.3%, representing a normal credit cycle |
| **Contagion Logic** | A single weak contagion industry (e.g., Food & Beverage) in trouble does not spread to other industries; no systemic warning needed |

#### SRI ≥ 0.5 (🟡 Watch) Threshold Rationale

| Basis Type | Specific Rationale |
|-----------|-------------------|
| **Statistical** | The 0.5 threshold is equivalent to approximately 2-3 industries with risk score ≥ 2 (medium-high risk) with the rest normal, or 4-5 industries with risk score ≥ 1 (medium risk). When 2-3 industries have problems simultaneously, monitoring is needed — this is the dividing line between isolated events and systemic events |
| **Historical Validation** | Pre-Lehman period Q3 2008, estimated SRI approximately 0.6-0.7 (see §5 backtest), already entered Watch range |
| **Contagion Logic** | 2-3 industries in trouble simultaneously means risk is no longer an isolated single event; the contagion matrix must be checked for high-contagion pathways between these industries |

#### SRI ≥ 1.0 (🟠 Alert) Threshold Rationale

| Basis Type | Specific Rationale |
|-----------|-------------------|
| **Statistical** | SRI = 1.0 is equivalent to approximately 4-5 industries scoring 2 points (medium-high risk), or 2 industries scoring 3 (high risk) + the rest normal. When nearly half of industries have problems, systemic risk is substantively present |
| **Historical Validation** | During the Eurozone sovereign debt crisis (2011-12), estimated SRI approximately 1.0-1.2 (see §6 backtest), already entered Alert range |
| **Contagion Logic** | When SRI ≥ 1.0, the industries in crisis likely include super-spreaders (3-4 out of 19 industries), and these spread risk to other healthy industries through the contagion matrix |

#### SRI ≥ 1.8 (🔴 Danger) Threshold Rationale

| Basis Type | Specific Rationale |
|-----------|-------------------|
| **Statistical** | SRI = 1.8 is equivalent to approximately 7 industries scoring 2 (over half at medium-high risk), or 5 scoring 3 + 1-2 scoring 1. Over half of industries in trouble simultaneously = full market systemic risk |
| **Historical Validation** | During the COVID-19 shock Q1 2020, all 19 industries were stressed simultaneously, SRI could reach ≥ 2.0 (see §7 backtest) |
| **Contagion Logic** | When most industries are simultaneously distressed, all four contagion types (credit chain + regional resonance + liquidity run + confidence collapse) may trigger simultaneously, forming the "three or more simultaneously triggered" condition from contagion matrix escalation factor synergy (Contagion Matrix §6.3), causing most links in the matrix to increase by +1 to +2 |

### 3.4 Thermometer and Contagion Matrix Escalation Factor Linkage

The thermometer level is linked to the [Contagion Matrix](contagion-matrix.md) §6 (Contagion Amplifier Conditions) escalation factors, forming a positive feedback monitoring loop:

| Thermometer Level | Escalation Factor Status | Linkage Rule |
|------------------|------------------------|-------------|
| 🟢 Normal | No escalation factor triggered | SRI calculation uses contagion matrix base intensity values |
| 🟡 Watch | 1-2 escalation factors may be triggered | If thermometer enters 🟡 and escalation factors are already triggered → escalation factor jump magnitude × 1.5 |
| 🟠 Alert | 2-3 escalation factors may trigger simultaneously | If thermometer enters 🟠 → automatically activate escalation factor synergy "two or more" rule |
| 🔴 Danger | 3+ escalation factors likely already triggered simultaneously | Thermometer 🔴 = Contagion matrix enters systemic tipping point (§6.3) → all matrix link intensities +1 to +2 |

**Specific Linkage Logic:**

```
When the thermometer is 🟠 or 🔴, even if individual escalation factors have not yet triggered,
systemic risk itself acts as a "global escalation factor,"
causing all link intensities in the contagion matrix to automatically increase by +1.

Rationale: When more than 30% of industries are under simultaneous stress,
market panic sentiment (escalation factor #1) is effectively already activated
by the systemic risk itself.
```

---

## 4. Industry Weights and Contagion Coefficients

### 4.1 Complete Weight Calculation Table (Illustrative)

The table below is a **worked illustration** using the §2.3.2 illustrative outstanding shares and the machine-generated §2.3.1 contagion coefficients (single source: contagion-matrix.md §2.1 heatmap). Production weights must be recomputed from live benchmark sector weights at analysis time.

| Industry | Outstanding Share (A) | Contagion Coefficient (B) | Raw Weight (A×B) | Normalized Weight |
|----------|-------------------------------|--------------------------|-----------------|------------------|
| Financials (Banks/Insurance) | 28.0% | 1.349 | 37.77% | 33.92% |
| Sovereigns & GSEs | 18.0% | 1.062 | 19.12% | 17.17% |
| Energy (Oil & Gas) | 7.0% | 1.177 | 8.24% | 7.40% |
| Utilities (Regulated) | 8.0% | 0.918 | 7.34% | 6.59% |
| Technology Hardware (Semis) | 4.0% | 1.205 | 4.82% | 4.33% |
| Capital Goods | 4.0% | 1.234 | 4.94% | 4.44% |
| Transportation | 4.0% | 1.119 | 4.48% | 4.02% |
| Telecommunications | 5.0% | 0.832 | 4.16% | 3.74% |
| Chemicals | 3.0% | 1.205 | 3.61% | 3.24% |
| Consumer Staples | 4.0% | 0.804 | 3.21% | 2.88% |
| Automobiles | 3.0% | 0.947 | 2.84% | 2.55% |
| Metals & Mining | 2.0% | 1.005 | 2.01% | 1.81% |
| Software & Services | 2.0% | 0.976 | 1.95% | 1.75% |
| Biotech & Pharma | 2.0% | 0.804 | 1.61% | 1.45% |
| Healthcare Equipment | 2.0% | 0.775 | 1.55% | 1.39% |
| Construction Materials | 1.0% | 0.918 | 0.92% | 0.83% |
| Consumer Durables | 1.0% | 0.890 | 0.89% | 0.80% |
| Retail | 1.0% | 0.890 | 0.89% | 0.80% |
| Commercial Services | 1.0% | 0.890 | 0.89% | 0.80% |
| **Total** | **100.0%** | — | **111.34%** | **≈100% (rounding)** |

**Normalization:** raw weights are scaled by `100% / Σ(raw)` so the final weights sum to 100%.

**Single-industry cap:** any single industry weight is capped at **25%**; the excess is redistributed pro-rata across the other industries. Under the illustrative table above, Financials (33.9%) would be capped at 25% — the cap prevents the largest bond-market sector from dominating the SRI by weight alone.

### 4.2 Dynamic Weight Adjustment Rules

| Trigger Condition | Adjustment | Rationale |
|------------------|-----------|-----------|
| An industry's outstanding share changes > 20% quarter-over-quarter | Update the industry's outstanding weight | E.g., sovereign issuance surges, sector-specific refinancing waves, buyback-driven shrinkage |
| Super-spreader rankings change | Update contagion coefficients | Row-sum rankings shift when the contagion matrix heatmap is updated |
| Contagion matrix version update | Synchronously regenerate contagion coefficients | Coefficients are machine-generated from the heatmap (§2.3.1); run `scripts/build_contagion_derived.py --write` |
| High-leverage escalation factor triggered | Multiply weight by 1.2 for industries with high financial intensity (high debt ratio) | Contagion risk of high-debt industries amplified in high-leverage environments |

### 4.3 Design to Avoid Weight Over-Concentration

Financials is naturally the largest bond-market sector (~30% of international corporate bond outstanding). To prevent the SRI from being dominated by a single sector's weight:

| Design | Description |
|--------|-------------|
| **Single-Industry Cap (25%)** | Any single industry weight capped at 25%; excess redistributed pro-rata |
| **Contagion Coefficient Moderation** | Financials' coefficient (1.349) is the highest but bounded — super-spreader status amplifies but does not multiply weight without limit |
| **Contagion Matrix Linkage** | Financials stress transmits through defined matrix links; high Financials risk in SRI is checked against actual contagion pathways, not assumed to implicate all sectors equally |
| **Thermometer Downgrade Condition** | If SRI is elevated but the main contribution comes from a single sector and all other sectors are 🟢, the thermometer may be downgraded one level (🟠 → 🟡) |

---

## 5. Historical Backtest 1: GFC 2008 (Pre-Lehman)

### 5.1 Scenario Background

**Time Window:** Q3 2008 (approximately 1 month before Lehman Brothers bankruptcy)
**Actual Event Date:** September 15, 2008 (Lehman Brothers filed for Chapter 11 bankruptcy protection)
**Market Environment at the Time:** After the subprime mortgage crisis emerged in 2007, the market experienced a period of relative calm in early-to-mid 2008. Bear Stearns had been rescued by JPMorgan in March 2008. The AAA-rated MBS/CDO ratings bubble was still largely intact. The market broadly believed that systemically important institutions would be bailed out.

### 5.2 Industry Signal State at the Time (19-Industry GICS Composition)

Estimated signal states for the 19 industries in Q3 2008 (pre-Lehman), reconstructed from public historical data:

| Industry | Track A Score (Est.) | Base | Outlook | Track B | Risk Score | Basis |
|----------|---------------------|------|---------|---------|------------|-------|
| **Financials (Banks/Insurance)** | 3.0-4.0 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | Bear Stearns rescued in March; Lehman/AIG/Merrill under severe stress; bank CDS spreads already blown out |
| Sovereigns & GSEs | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | US Treasuries as safe haven; no sovereign stress pre-crisis |
| Energy (Oil & Gas) | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | Oil peaked at $147 in July 2008, then collapsed; demand destruction beginning |
| Metals & Mining | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | Copper/iron ore peaked in 2008 H1 and rolled over |
| Construction Materials | 4.0-5.0 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | US housing collapse already underway |
| Automobiles | 3.0-4.0 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | Detroit 3 in crisis (pre-bailout); sales collapsing |
| Transportation | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | Baltic Dry Index crashed mid-2008 |
| Chemicals | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Demand weakening but feedstock costs falling in parallel |
| Capital Goods | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Order books still at cycle top |
| Commercial Services | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Staffing/services beginning to soften |
| Technology Hardware (Semis) | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Cycle turn starting; balance sheets still solid |
| Consumer Durables | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Housing-linked durables weakening |
| Retail | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Discretionary spending weakening |
| Consumer Staples | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Software & Services | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Resilient |
| Biotech & Pharma | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Healthcare Equipment | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Stable |
| Utilities (Regulated) | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Telecommunications | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Stable |

### 5.3 SRI Calculation

Weights use the §4.1 illustrative outstanding shares with the **25% single-industry cap** applied (Financials' normalized 33.9% is capped at 25%; the excess is redistributed pro-rata, factor ≈ 1.135):

```
Weighted contributions (risk score × capped weight):
  Financials            3.0 × 25.00% = 0.750
  Energy                2.0 ×  8.40% = 0.168
  Transportation        2.0 ×  4.56% = 0.091
  Automobiles           3.0 ×  2.89% = 0.087
  Capital Goods         1.0 ×  5.04% = 0.050
  Technology Hardware   1.0 ×  4.91% = 0.049
  Metals & Mining       2.0 ×  2.05% = 0.041
  Chemicals             1.0 ×  3.68% = 0.037
  Construction Materials 3.0 ×  0.94% = 0.028
  Consumer Durables     1.5 ×  0.91% = 0.014
  Retail                1.5 ×  0.91% = 0.014
  Commercial Services   1.0 ×  0.91% = 0.009
  (Sovereigns, Utilities, Telecom, Staples, Software, Biotech, HealthEquip: 0)

SRI ≈ 1.29  →  🟠 Alert (1.0 - 1.8)
```

### 5.4 Could It Provide Early Warning?

| Assessment Dimension | Conclusion |
|---------------------|-----------|
| **Did SRI enter 🟠?** | **Yes.** SRI ≈ 1.29, crossing the 1.0 alert threshold about one month before Lehman |
| **Main risk contribution** | Financials alone contributes 0.75 (58% of SRI) — consistent with the crisis's actual epicenter. Commodity-cyclical industries (Energy, Metals, Transportation) and housing-linked industries (Construction Materials, Automobiles) form the secondary belt |
| **Contrast with the legacy 13-industry composition** | Under the retired composition, financial risk entered only through an indirect LGFV/sub-sovereign mapping (1 point × 25%), yielding SRI ≈ 0.70 (🟡). The 19-industry GICS composition makes Financials a first-class 25%-weighted risk source at risk score 3, and the framework would have been at **🟠 Alert** — a materially stronger and historically more accurate signal |
| **Framework Limitations** | Even at 🟠, the SRI cannot predict confidence-collapse events themselves; it identifies that risk has accumulated to alert level. The thermometer downgrade condition (§4.3) would also be checked here: SRI is elevated with a single dominant contributor, but Energy/Metals/Automobiles/Construction are simultaneously stressed, so the downgrade does not apply |

### 5.5 Backtest Conclusion

| Backtest Conclusion | Specific Description |
|--------------------|---------------------|
| **Warning Effective** | SRI entered 🟠 Alert range about one month before Lehman, with the risk contribution concentrated in the sector that actually failed |
| **Actionable Level** | At 🟠, the framework prescribes portfolio-wide stress testing and exposure-reduction review — an appropriate response to what became the GFC |
| **Escalation Cross-Check** | By September 2008, Market Panic + High Leverage + Information Asymmetry were all triggering (3+ factors → 3.0x synergy per contagion-matrix §6.3), which would escalate the contagion matrix to systemic tipping-point — corroborating the 🟠 reading |
| **Overall Assessment** | Under the 19-industry GICS composition, the framework's GFC backtest is strong: alert-level warning with the correct epicenter identified, without relying on hindsight-only China-market mappings |

---

## 6. Historical Backtest 2: Eurozone Sovereign Debt Crisis 2011-12

### 6.1 Scenario Background

**Time Window:** Q3 2011 (peak of the Eurozone sovereign debt crisis — Greek escalation)
**Actual Event Time:** Summer/Fall 2011 — Greek bond yields exceeded 50%, CDS spreads peaked, contagion spread to Italy, Spain, Portugal, and Ireland (PIIGS); ECB launched SMP interventions in August; Dexia required rescue in October; Greek PSI agreed in October.
**Market Environment at the Time:** The aftermath of the 2008 GFC was still unfolding. Greece had revealed a much larger deficit than previously reported in late 2009. By 2011 the crisis had evolved into a full sovereign debt crisis threatening eurozone integrity. The bank-sovereign "doom loop" was in full effect — banks held large amounts of sovereign debt, while struggling sovereigns needed healthy banks.

### 6.2 Industry Signal State at the Time (19-Industry GICS Composition)

Estimated signal states for the 19 industries in Q3 2011, reconstructed from public historical data:

| Industry | Track A Score (Est.) | Base | Outlook | Track B | Risk Score | Basis |
|----------|---------------------|------|---------|---------|------------|-------|
| **Sovereigns & GSEs** | 3.0-4.0 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | The epicenter: Greek yields >50%, PIIGS contagion, CDS at peaks |
| **Financials (Banks/Insurance)** | 3.5-4.5 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | The other end of the doom loop: European banks holding peripheral sovereign debt (Dexia failed in October) |
| Utilities (Regulated) | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | State-owned utilities repriced with sovereigns |
| Energy (Oil & Gas) | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Resource-fiscal risk, demand slowdown |
| Construction Materials | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | Periphery infrastructure freeze (Spain/Ireland bust aftermath) |
| Transportation | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Trade/freight slowing |
| Metals & Mining | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Global slowdown |
| Capital Goods | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Capex freeze |
| Automobiles | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Weak European sales |
| Consumer Durables | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Austerity-hit consumer |
| Retail | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Austerity |
| Telecommunications | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Some sovereign-linked operators |
| Chemicals | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Export-linked softness |
| Commercial Services | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | — |
| Technology Hardware (Semis) | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | US/global tech unaffected |
| Software & Services | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | — |
| Consumer Staples | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Biotech & Pharma | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Healthcare Equipment | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | — |

### 6.3 SRI Calculation

Weights as in §5.3 (§4.1 illustrative shares, 25% single-industry cap applied):

```
Weighted contributions (risk score × capped weight):
  Sovereigns & GSEs     3.0 × 19.49% = 0.585
  Financials            3.0 × 25.00% = 0.750
  Utilities             2.0 ×  7.48% = 0.150
  Energy                1.5 ×  8.40% = 0.126
  Capital Goods         1.5 ×  5.04% = 0.076
  Transportation        1.5 ×  4.56% = 0.068
  Telecommunications    1.0 ×  4.24% = 0.042
  Automobiles           1.5 ×  2.89% = 0.043
  Chemicals             1.0 ×  3.68% = 0.037
  Metals & Mining       1.5 ×  2.05% = 0.031
  Construction Materials 2.0 ×  0.94% = 0.019
  Consumer Durables     1.5 ×  0.91% = 0.014
  Retail                1.5 ×  0.91% = 0.014
  Commercial Services   1.0 ×  0.91% = 0.009

SRI ≈ 1.96  →  🔴 Danger (>= 1.8)
```

### 6.4 Could It Provide Early Warning?

| Assessment Dimension | Conclusion |
|---------------------|-----------|
| **Did SRI enter 🔴?** | **Yes.** SRI ≈ 1.96 crosses the 1.8 danger threshold in Q3 2011 — the window of ECB SMP interventions (August), Dexia's failure (October), and the Greek PSI (October) |
| **Doom-loop capture** | Sovereigns & GSEs (0.585) and Financials (0.750) are both first-class inputs at risk score 3 — the framework captures the bank-sovereign doom loop **directly**, rather than through an indirect proxy mapping. The two largest contributions sit exactly at the two ends of the loop |
| **Contrast with the legacy composition** | The retired 13-industry composition had no sovereign/banking industry at all and yielded SRI ≈ 1.23 (🟠) via indirect sub-sovereign mapping. The 19-industry composition reads the same event at 🔴 — consistent with how close the eurozone came to breakup |
| **§4.3 downgrade check** | The thermometer downgrade condition (single dominant contributor, all else 🟢) does not apply: Utilities, Construction, Capital Goods, Automobiles, and the consumer belt are simultaneously stressed |
| **Framework Limitations** | 🔴 marks systemic severity, not timing. The framework cannot forecast the political decisions (SMP, EFSF/ESM, OMT in 2012) that ultimately contained the crisis |

### 6.5 Backtest Conclusion

| Backtest Conclusion | Specific Description |
|--------------------|---------------------|
| **Danger-level warning effective** | SRI entered 🔴 Danger during the crisis peak, identifying systemic severity in real time |
| **First-class sovereign channel validated** | The sovereign-bank nexus — the matrix's strongest link (Financials ↔ Sovereigns, intensity 5) — is exercised end-to-end: both ends appear as top-weighted risk sources |
| **Escalation cross-check** | Regulatory Vacuum (ambiguous rescue stance through summer 2011) + Market Panic were simultaneously active; per contagion-matrix §6.3, the 1.5x synergy multiplies affected link intensities — corroborating the 🔴 reading |
| **Overall Assessment** | The framework reads the Eurozone crisis at the correct severity tier with the correct mechanism. It would have prescribed emergency position review and hedge activation (🔴 actions) during the window when those actions were most valuable |

---

## 7. Historical Backtest 3: Exogenous Synchronous Shock (Case: COVID-19, Q1 2020)

> **Purpose of this case:** This backtest is NOT about pandemic prediction. It calibrates
> the **boundary of the SRI framework**: what kind of systemic event the framework can be
> forward-looking about (endogenous credit accumulation — §5, §6) versus what it can only
> be reactive about (exogenous synchronous non-credit shocks — this case). It also validates
> the thermometer's real-time accuracy once such a shock has occurred.

### 7.1 Scenario Background

**Time Window:** February-March 2020 (global COVID-19 pandemic outbreak)
**Actual Impact Time:** January 30, 2020 WHO declared a Public Health Emergency of International Concern; March 11, 2020 declared a global pandemic
**Market Environment at the Time:** An unprecedented public health crisis caused simultaneous shocks to all industries. Unlike the GFC or Eurozone crisis, COVID-19 was an **exogenous, synchronous, non-credit** shock — no industry balance sheet showed it coming.

### 7.2 Industry Signal State at the Time (19-Industry GICS Composition)

Estimated signal states for the 19 industries in Q1 2020, reconstructed from public historical data:

| Industry | Track A Score (Est.) | Base | Outlook | Track B | Risk Score | Basis |
|----------|---------------------|------|---------|---------|------------|-------|
| Transportation | 2.0-3.0 (B/B+) | 3 | Negative | 🔴 (Crisis) | **3.0** | Passenger traffic collapsed; airlines burning cash daily |
| Automobiles | 3.0-4.0 (B+/BB) | 2 | Negative | 🔴 (Crisis) | **3.0** | Factories shut; sales down 80%+ |
| Retail | 2.5-3.5 (B/B+) | 2 | Negative | 🔴 (Crisis) | **3.0** | Zero foot traffic at physical stores |
| Consumer Durables | 3.0-4.0 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | Stores closed; big-ticket purchases deferred |
| Energy (Oil & Gas) | 3.0-4.0 (B+/BB) | 2 | Negative | 🔴 (Crisis) | **3.0** | Demand collapse; WTI briefly negative in April |
| Capital Goods | 3.5-4.5 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **2.5** | Production paused, deliveries delayed |
| Metals & Mining | 3.5-4.5 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **2.5** | Demand cliff |
| Construction Materials | 4.0-5.0 (B+/BB+) | 2 | Negative | 🟡 (Watch) | **2.5** | Sites paused |
| Commercial Services | 4.0-5.0 (B+/BB+) | 2 | Negative | 🟡 (Watch) | 2.0 | Offices closed |
| **Financials (Banks/Insurance)** | 4.0-5.0 (B+/BB) | 2 | Stable | 🟡 (Watch) | **2.5** | Spreads blew out, but central banks backstopped forcefully by end-March |
| Chemicals | 4.5-5.5 (BB+/BBB-) | 2 | Negative | 🟢 (Calm) | 1.5 | Demand weakening; feedstock costs falling |
| Technology Hardware (Semis) | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | 1.5 | Supply-chain disruption; WFH partly offsets |
| Sovereigns & GSEs | 5.5-6.0 (BBB+) | 1 | Stable | 🟢 (Calm) | 1.0 | Fiscal response expanding; safe-haven demand |
| Software & Services | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | WFH beneficiary |
| Biotech & Pharma | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Vaccine race |
| Healthcare Equipment | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Surge demand for medical supplies |
| Consumer Staples | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Pantry stocking |
| Utilities (Regulated) | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Telecommunications | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Traffic surge |

### 7.3 SRI Calculation

Weights as in §5.3 (§4.1 illustrative shares, 25% single-industry cap applied):

```
Weighted contributions (risk score × capped weight):
  Financials            2.5 × 25.00% = 0.625
  Energy                3.0 ×  8.40% = 0.252
  Sovereigns & GSEs     1.0 × 19.49% = 0.195
  Transportation        3.0 ×  4.56% = 0.137
  Capital Goods         2.5 ×  5.04% = 0.126
  Automobiles           3.0 ×  2.89% = 0.087
  Technology Hardware   1.5 ×  4.91% = 0.074
  Chemicals             1.5 ×  3.68% = 0.055
  Metals & Mining       2.5 ×  2.05% = 0.051
  Construction Materials 2.5 ×  0.94% = 0.024
  Consumer Durables     3.0 ×  0.91% = 0.027
  Retail                3.0 ×  0.91% = 0.027
  Commercial Services   2.0 ×  0.91% = 0.018

SRI ≈ 1.70  →  🟠 Alert (1.0 - 1.8)
```

### 7.4 Known Unknown vs Unknown Unknown: What This Case Calibrates

| Assessment Dimension | Analysis |
|---------------------|---------|
| **Nature of the shock** | A "known unknown" in taxonomy but an un-forecastable event in practice — public health experts had long warned about pandemic risk, yet no Track A/B signal in January 2020 showed it |
| **Could the SRI provide pre-event warning?** | **No — and it must not claim to.** The framework reads credit-state signals; an exogenous synchronous non-credit shock has no accumulation phase in those signals. Any framework claiming to predict such events is overfitting hindsight |
| **Could the SRI reflect the impact?** | **Yes, in real time.** Once the shock landed, SRI rose to ≈ 1.70 (🟠) — high but below 🔴, correctly reflecting that unprecedented central-bank and fiscal response prevented the credit spiral from reaching GFC depth |
| **Where does black-swan response live instead?** | Not in the SRI. Exogenous-shock response belongs to (a) the contagion escalation-factor layer (event-driven triggers, contagion-matrix §6), and (b) the portfolio stress test path (WP-RO-04) — the engine's "response protocol" — while the SRI's job is to report severity honestly after impact |
| **Reactive vs forward-looking** | GFC (§5) and Eurozone (§6) are endogenous transmission shocks — the SRI is forward-looking there. COVID is the boundary case proving the framework knows when it is only a seismograph, not a crystal ball |

### 7.5 Backtest Conclusion

| Backtest Conclusion | Specific Description |
|--------------------|---------------------|
| **Boundary calibrated** | The framework correctly does NOT claim pre-event prediction for exogenous synchronous shocks — this case exists to document that limit, not to showcase accuracy |
| **Reactive accuracy validated** | Post-impact, the thermometer reached 🟠 1.70 with contributions spanning the actually-hit sectors (transport, autos, retail, energy) and zero contribution from genuinely resilient sectors — a correct real-time map of the shock |
| **Complementarity documented** | Black-swan response is assigned to the escalation-factor layer and WP-RO-04 stress testing; the SRI stays an honest seismograph |
| **Overall Assessment** | Three backtests now cover the full taxonomy: endogenous credit accumulation (GFC, 🟠 forward) → sovereign-bank nexus (Eurozone, 🔴 forward) → exogenous synchronous shock (COVID, 🟠 reactive). The framework's claims match its demonstrated capabilities |

---

## 8. Current Period Calculation: Scenario-Based SRI Example

### 8.1 Scenario: Hypothetical 2026 Market State (Illustrative)

This section shows how the SRI is calculated under a **hypothetical** 2026 market state: higher-for-longer rates pressuring commercial real estate and rate-sensitive consumption, elevated sovereign deficits, and a two-speed technology sector (AI capex boom vs everything else). **The signal states below are illustrative, not a real-time reading.**

| Industry | Track A Score (Est.) | Base | Outlook | Track B | Risk Score | Rationale |
|----------|---------------------|------|---------|---------|------------|-----------|
| **Financials (Banks/Insurance)** | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | Regional-bank CRE exposure stress; NIM normalization |
| **Sovereigns & GSEs** | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Elevated deficits; term premium rising |
| Energy (Oil & Gas) | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Mid-cycle |
| Construction Materials | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | CRE/housing slowdown |
| Capital Goods | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Reshoring capex supportive |
| Transportation | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Freight stable |
| Chemicals | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | — |
| Metals & Mining | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Energy-transition metals firm |
| Automobiles | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | EV price war + rate-sensitive demand |
| Consumer Durables | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Rate-sensitive big-ticket |
| Retail | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | K-shaped consumer |
| Commercial Services | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | — |
| Technology Hardware (Semis) | 7.0+ (A) | 0 | Positive | 🟢 (Calm) | 0 | AI capex boom |
| Software & Services | 7.0+ (A) | 0 | Positive | 🟢 (Calm) | 0 | AI tailwind |
| Utilities (Regulated) | 7.0+ (A) | 0 | Positive | 🟢 (Calm) | 0 | Datacenter demand boom |
| Telecommunications | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | — |
| Consumer Staples | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Biotech & Pharma | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | — |
| Healthcare Equipment | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | — |

### 8.2 SRI Calculation

```
Weighted contributions (risk score × capped weight, §4.1 illustrative):
  Financials            2.0 × 25.00% = 0.500
  Sovereigns & GSEs     1.5 × 19.49% = 0.292
  Energy                1.0 ×  8.40% = 0.084
  Capital Goods         1.0 ×  5.04% = 0.050
  Transportation        1.0 ×  4.56% = 0.046
  Chemicals             1.0 ×  3.68% = 0.037
  Automobiles           2.0 ×  2.89% = 0.058
  Metals & Mining       1.0 ×  2.05% = 0.021
  Construction Materials 2.0 ×  0.94% = 0.019
  Consumer Durables     1.5 ×  0.91% = 0.014
  Retail                1.5 ×  0.91% = 0.014
  Commercial Services   1.0 ×  0.91% = 0.009

SRI ≈ 1.14  →  🟠 Alert (1.0 - 1.8)
```

### 8.3 SRI Interpretation

| Dimension | Analysis |
|-----------|---------|
| **Reading** | SRI ≈ 1.14 (🟠 Alert): elevated but far from crisis. The two dominant contributors are Financials (0.500) and Sovereigns (0.292) — a rates/fiscal-driven stress pattern, not a broad credit event |
| **Two-speed structure** | Technology, software, and utilities carry zero risk contribution (AI capex boom), while the rate-sensitive belt (construction, autos, durables, retail) forms the secondary layer. The thermometer sees the divergence, not just the average |
| **§4.3 downgrade check** | Would the thermometer downgrade to 🟡? No: the stress is shared by 8+ industries, not a single dominant contributor |
| **Prescribed actions (🟠)** | Re-run concentration (WP-RO-01) and contagion (WP-RO-02) for the Financials/Sovereigns-linked exposures; portfolio-wide stress test (WP-RO-04); review rate-sensitive belt sizing |

### 8.4 How to Use This Example

This scenario is a **template for computing the SRI on live inputs**: replace the illustrative Track A / outlook / Track B values with current assessments (Track A from the industry pyramid, outlook from `outlook-monitoring-framework.md`, Track B from market pricing signals), replace the §4.1 illustrative weights with live benchmark sector weights, and the same arithmetic yields the current SRI. The coded engine (`src/sri_calculator.py` via WP-RO-03) executes exactly this calculation; the orchestrator (`src/pipeline.py`) accepts the inputs as plain dicts/YAML.

---

## 9. Threshold Sensitivity Analysis

### 9.1 Impact of Thresholds on SRI Results

The core parameters of the SRI (threshold settings) have a decisive impact on the final temperature and action recommendations. The following sensitivity analysis shows how parameter changes alter SRI readings:

**Scenario A: Baseline Thresholds (Current Version)**

| Track A Range | Base Score | Negative Outlook | Track B 🟡 | Track B 🟠 | Track B 🔴 |
|--------------|-----------|-----------------|-----------|-----------|-----------|
| > 6.0 | 0 | +0.5 | +0.5 | +1.0 | +1.5 |
| 5.0-6.0 | 1 | +0.5 | +0.5 | +1.0 | +1.5 |
| 3.0-5.0 | 2 | +0.5 | +0.5 | +1.0 | +1.5 |
| < 3.0 | 3 | +0.5 | +0.5 | +1.0 | +1.5 |

**Scenario B: Pessimistic Thresholds (More Sensitive)**

| Track A Range | Base Score | Negative Outlook | Track B 🟡 | Track B 🟠 | Track B 🔴 |
|--------------|-----------|-----------------|-----------|-----------|-----------|
| > 6.0 | 0 | +1.0 | +1.0 | +1.5 | +2.0 |
| 5.0-6.0 | 1 | +1.0 | +1.0 | +1.5 | +2.0 |
| 3.0-5.0 | 3 | +1.0 | +1.0 | +1.5 | +2.0 |
| < 3.0 | 4 | Not stacked | Not stacked | Not stacked | Not stacked |

Under pessimistic thresholds, SRI calculations are more aggressive — the negative outlook penalty is doubled, Track B penalties are raised one level each (Watch +1.0, Abnormal +1.5, Crisis +2.0), and the speculative-grade base score is raised from 2 to 3. This version is suitable for conservative investors or periods of high systemic risk.

**Scenario C: Optimistic Thresholds (Less Sensitive)**

| Track A Range | Base Score | Negative Outlook | Track B 🟡 | Track B 🟠 | Track B 🔴 |
|--------------|-----------|-----------------|-----------|-----------|-----------|
| > 6.0 | 0 | No penalty | No penalty | No penalty | No penalty |
| 5.0-6.0 | 1 | +0.5 | +0.5 | +0.5 | +0.5 |
| 3.0-5.0 | 2 | +0.5 | +0.5 | +0.5 | +0.5 |
| < 3.0 | 3 | +0.5 | +0.5 | +0.5 | +0.5 |

Under optimistic thresholds, negative outlook and Track B signals have no penalty when Track A > 6.0 (assuming negative signals for high-grade industries are noise), and Track B penalties in other ranges are unified to half a notch. This version is suitable for high-risk-appetite investors.

### 9.2 SRI Comparison Across Three Scenarios (Scenario Example)

| Parameter Version | Calculation Process | SRI | Thermometer |
|-----------------|-------------------|-----|-------------|
| **A. Baseline (Current)** | As calculated in §8.3 | 0.57 | 🟡 Watch |
| **B. Pessimistic** | Solar: 3+1+1=5→3; NEV: 1+1+1=3; Sub-sovereign: 1+0+1=2; Retail: 1+1+1=3 | 0.76 | 🟡 Watch (upper bound) |
| **C. Optimistic** | Solar: 2+0.5+0=2.5; NEV: 1+0.5+0=1.5; Sub-sovereign: 1+0+0=1; Retail: 1+0.5+0=1.5 | 0.40 | 🟢 Normal |

**Analysis:**
- Under the optimistic version, SRI falls to 0.40, landing in 🟢 range
- Under the pessimistic version, SRI rises to 0.76, still in 🟡 range but near the upper bound
- None of the three versions reach 🟠 Alert (1.0) — indicating that parameter variation does not cause over- or under-warning given the current signal distribution

### 9.3 Threshold Applicability Recommendations

| Market Environment | Recommended Threshold | Rationale |
|-------------------|---------------------|-----------|
| Normal market (credit spreads stable, no systemic shock) | Baseline (A) | Balanced sensitivity and specificity |
| Credit tightening cycle (credit spreads widening, high cancellation rates) | Pessimistic (B) | Increase warning sensitivity, prepare early |
| Rating bubble burst period (mass AAA downgrades) | Pessimistic (B) | Increase vigilance during concentrated rating adjustment window |
| Loose monetary + asset shortage (credit spreads compressing) | Optimistic (C) | Avoid over-warning in high-liquidity environments |
| Contagion matrix escalation factor triggered (panic/high leverage) | Pessimistic (B) | Escalation factors already triggered, raise warning level |

---

## 10. Integration with Existing Engine

### 10.1 Integration into the Analysis Pyramid

#### M1 (Industry Fundamental Analysis)

SRI output serves as a "systemic risk context" indicator in each industry analysis report:

```
"Systemic Risk Context" section in the industry analysis report template:

Current Systemic Risk Level: [🟢/🟡/🟠/🔴]
SRI Reading: [0.xx]
Industries of Concern: List industries with risk score ≥ 2
Linkage with [This Industry]:
  - Whether it belongs to the same high-contagion cluster
  - Whether there is a direct contagion pathway (reference the contagion matrix)
  - Whether it overlaps with a super-spreader
```

#### M2 (Individual Credit Analysis)

SRI serves as a background correction for individual ratings:

| SRI Level | Individual Rating Adjustment Rule |
|-----------|----------------------------------|
| 🟢 Normal | No adjustment |
| 🟡 Watch | No automatic adjustment, but note "Systemic risk context 🟡, monitor industry contagion risk" |
| 🟠 Alert | If the individual is in a high-risk industry (risk score ≥ 2), automatically downgrade half a notch |
| 🔴 Danger | All individual ratings downgraded 1 notch from base (systemic risk premium) |

#### M3 (Industry Comparison and Ranking)

SRI is used for weight correction in industry ranking:

- When SRI ≥ 1.0 (🟠 Alert), the weights of high-contagion clusters (Cluster A/B/C) in industry ranking are reduced by 10%
- When SRI ≥ 1.8 (🔴 Danger), industry ranking is suspended (industry comparison loses meaning under systemic risk)

#### M4 (Portfolio Risk Control)

SRI serves as a precondition for the concentration framework:

```
Five-Dimensional Concentration Composite Score = Original Score × (1 + SRI Adjustment Factor)

SRI Adjustment Factor:
  🟢 Normal: 0% (no adjustment)
  🟡 Watch: +5%
  🟠 Alert: +15%
  🔴 Danger: +30% (concentration score increased by 30%, triggering stricter limit management)
```

### 10.2 Linkage with Contagion Matrix

| Linkage Scenario | Rule |
|-----------------|------|
| 🟡 Watch + 1 escalation factor triggered | Escalation factor jump magnitude for contagion pathways × 1.5 |
| 🟠 Alert + 2 escalation factors triggered | Automatically activate escalation factor synergy (Contagion Matrix §6.3), all matrix link intensities +1 |
| 🔴 Danger | Equivalent to contagion matrix entering "systemic tipping point" (three or more escalation factors triggered simultaneously), all matrix link intensities +1 to +2 |
| SRI continuously rising (2 consecutive periods of increase) | Even without crossing threshold, trigger escalation factor monitoring upgrade — increase escalation factor monitoring frequency |

### 10.3 Linkage with Concentration Framework

According to the [Five-Dimensional Concentration Analysis Framework](concentration-framework.md) §8.4 (Dynamic Weight Adjustment Rules), the SRI thermometer serves as one of the trigger conditions for dynamic weight adjustment:

| SRI Level | Concentration Framework Adjustment |
|-----------|-----------------------------------|
| 🟡 Watch | If the main SRI contributing industry has portfolio exposure > 20% → Industry concentration dimension weight increased from 25% to 30% |
| 🟠 Alert | Weight adjusted to "Contagion Matrix Escalation Factor Triggered" mode (Industry 30%, Region 25%, Rating 10%, Maturity 20%, Funding Channel 15%) |
| 🔴 Danger | Directly trigger portfolio extreme concentration cap (Concentration Framework §7.3), all issuers in portfolio capped at BB |

### 10.4 Linkage with Outlook Monitoring Framework

According to the [Outlook Monitoring Framework](outlook-monitoring-framework.md), the outlook direction input of the SRI framework directly references the outlook framework's industry-level outlook judgments. When the outlook framework adjusts an industry's outlook direction, the SRI automatically updates that industry's outlook_penalty.

| SRI Level | Outlook Monitoring Adjustment |
|-----------|------------------------------|
| 🟡 Watch | Outlook update frequency increased from monthly to bi-weekly |
| 🟠 Alert | Requires special outlook assessment for all high-risk industries (risk score ≥ 2), results directly fed back to SRI |
| 🔴 Danger | Outlook assessment suspended (outlook differentiation loses meaning under systemic risk) |

### 10.5 Data Flow Architecture

```
                  Outlook Monitoring Framework     Contagion Matrix
                         │                              │
                         ▼                              ▼
  Industry Pyramid → Track A Score ──┐          Contagion Coefficients
  Track B Signals → Market Level ────┼──→ SRI Aggregation ──→ Thermometer Output
  Dual-Track Analysis → Veto Trigger ─┘               │
                         │                              │
                         ▼                              ▼
                   Industry Weight Table       Action Recommendations → M4 Concentration Framework
                   Credit Bond Outstanding               │
                         │                                ▼
                         ▼                          Portfolio Risk Decisions
                   Regular Updates (Quarterly)
```

### 10.6 Execution Order (Preventing Cycles)

1. Calculate each issuer's Dual-Track rating (Track A + Track B → cross-validation).
2. Aggregate industry scores → calculate SRI.
3. Apply SRI background downgrade to individual ratings at M2 (one-time, no back-calculation).
4. Calculate portfolio five-dimensional concentration.
5. Use SRI to adjust concentration weights (M4).
6. Apply concentration → rating adjustment.

It is prohibited to recalculate industry scores or SRI using already-adjusted individual ratings within the same analysis cycle.

---

## 11. Limitations Statement

### 11.1 Framework Inherent Limitations

| Limitation | Specific Description | Mitigation |
|-----------|---------------------|------------|
| **1. Lags behind exogenous shocks** | The SRI framework is based on industry fundamental signals and cannot pre-warn exogenous, non-credit shocks (e.g., pandemics, natural disasters, geopolitical conflicts) | For known external risks (e.g., trade frictions, regulatory policy changes), advance reflection in outlook assessment can partially mitigate the lag |
| **2. Industry granularity** | The framework aggregates at the level of 19 GICS-based industries; intra-industry divergence (e.g., IG vs HY issuers within one sector) is averaged out | Pair SRI with single-issuer Track A analysis for issuer-level differentiation |
| **3. Static weight risk** | Industry weights based on credit bond outstanding share and contagion coefficients are fixed parameters that cannot reflect short-term market structural changes | Establish quarterly weight update mechanism; update immediately when an industry's credit bond outstanding changes > 20% |
| **4. Parameter subjectivity** | Industry risk score thresholds (3.0/5.0/6.0), penalty factors (0.5), and thermometer thresholds (0.5/1.0/1.8) are based on subjective judgment and historical calibration, not statistical optimization | Provide pessimistic/baseline/optimistic parameter versions for user selection based on risk preference; conduct annual backtest calibration |
| **5. Linear weighting limitation** | SRI uses linear weighted aggregation and cannot capture non-linear interaction effects between industries (e.g., industry A in trouble → contagion to B → feedback loop strengthening A) | Partially compensated through thermometer and contagion matrix escalation factor linkage (§3.4) — automatically activate escalation factor synergy when SRI ≥ 1.0 |
| **6. Signal quality dependency** | The calculation quality of SRI depends on the accuracy of input Track A scores and Track B signals. If these foundational signals are biased (e.g., inflated ratings), SRI will also be distorted | Reference the engine's "pseudo-high rating" identification mechanism as auxiliary validation of SRI quality |

### 11.2 Usage Restrictions

| Restriction | Description |
|-------------|-------------|
| **Not Investment Advice** | The SRI provides systemic risk level assessment and does not constitute specific buy/sell/hold investment advice |
| **Not a Regulatory Metric** | This framework has not been reviewed or certified by any regulatory authority and cannot be used for regulatory capital calculation or compliance reporting |
| **Limited Historical Samples** | The framework has only been validated through 3 historical events (2020 COVID-19, 2008 GFC, 2011-12 Eurozone crisis) for backtesting, with limited statistical significance. As more credit events accumulate, the framework requires continuous recalibration |
| **Market-Specific Parameters** | The framework's thresholds, weights, and contagion coefficients are based on specific market data and characteristics. Direct application to other markets requires comprehensive parameter reset |

### 11.3 Version Evolution Roadmap

| Version | Planned Content |
|---------|----------------|
| v0.0.1 | Initial version: Basic aggregation algorithm + thermometer + 3 historical backtests + current calculation |
| v0.0.1 | System intelligence layer integration: complete M4 portfolio risk control system with contagion matrix/concentration framework, unified engine version |
| v0.0.1 | Engine-level integration release: cross-CLI entry (AGENTS.md) · four-segment chain product contract · executable orchestrator · dimension registry |
| v0.0.1 | Gate reinforcement and promotion mechanism (no change to framework/thresholds): .gitattributes mandatory LF · CI launch · promote.py promotion script |
| v0.0.1 | Contagion matrix connected to encoding engine; §2.3.1 Contagion Coefficient Table and §4 weight example aligned with matrix truth values (ranking unchanged) |
| v0.0.1 | Reliability iteration: consistency audit and gate expansion (framework includes §2.3.2/§4.1 data center consolidation note) |
| v0.0.1 (Current) | Outlook monitoring activation wiring (no change to framework/thresholds) |
| v0.0.1 | Add SRI time series tracking (plot SRI historical curves, identify trends and turning points) |
| v0.0.1 | Introduce real-time SRI and contagion matrix escalation factor linkage (automatically adjust SRI reading when escalation factors trigger) |
| v0.0.1 | Add portfolio-level SRI calculation (based on actual portfolio holding weights replacing industry weights), achieving true portfolio systemic risk assessment |
| v0.0.1 | Introduce SRI stress testing (input hypothetical shock → output post-stress SRI thermometer), deeply integrated with M4 portfolio risk control |
| v1.0.0 | Stable release: all backtest validations passed + at least 6 months of real-time operational data validation |

---

## 12. Appendix

### Appendix A: Signal Aggregation Algorithm Pseudocode

```
function calculate_SRI(industries, weights):
    """
    Calculate the Systemic Risk Index
    
    Parameters:
      industries: list of dictionaries for 19 industries, each containing:
        - name: industry name
        - track_A_score: Track A score (0-10)
        - track_B_level: Track B level ('green'/'yellow'/'orange'/'red')
        - outlook: outlook direction ('positive'/'stable'/'negative')
        - veto_triggered: veto trigger (True/False)
      weights: list of weight percentages for 19 industries (normalized, sum to 100%)
    
    Returns:
      SRI: Systemic Risk Index (float)
      level: Thermometer level (str)
      details: Risk score breakdown per industry
    """
    
    total_score = 0
    details = []
    
    for i, ind in enumerate(industries):
        # 1. Base score from Track A
        if ind.track_A_score < 3.0:
            base = 3
        elif ind.track_A_score < 5.0:
            base = 2
        elif ind.track_A_score < 6.0:
            base = 1
        else:
            base = 0
        
        # 2. Outlook penalty
        outlook_penalty = 0.5 if ind.outlook == 'negative' else 0
        
        # 3. Track B penalty
        if ind.track_B_level == 'red':
            track_B_penalty = 1.5
        elif ind.track_B_level == 'orange':
            track_B_penalty = 1.0
        elif ind.track_B_level == 'yellow':
            track_B_penalty = 0.5
        else:
            track_B_penalty = 0
        
        # 4. Veto check
        if ind.veto_triggered:
            risk_score = 3
        else:
            risk_score = min(base + outlook_penalty + track_B_penalty, 3.0)
        
        weighted_contribution = risk_score * weights[i]
        total_score += weighted_contribution
        
        details.append({
            'name': ind.name,
            'risk_score': risk_score,
            'base': base,
            'outlook_penalty': outlook_penalty,
            'track_B_penalty': track_B_penalty,
            'veto': ind.veto_triggered,
            'weight': weights[i],
            'contribution': weighted_contribution
        })
    
    SRI = total_score
    
    # Thermometer determination
    if SRI >= 1.8:
        level = '🔴 Danger'
    elif SRI >= 1.0:
        level = '🟠 Alert'
    elif SRI >= 0.5:
        level = '🟡 Watch'
    else:
        level = '🟢 Normal'
    
    return SRI, level, details
```

### Appendix B: SRI Comparison Summary Across Three Backtests

| Backtest Scenario | Time Window | SRI Estimate | Thermometer | Framework Performance |
|------------------|------------|-------------|-------------|----------------------|
| Pre-Lehman (GFC 2008) | Q3 2008 | 0.70 | 🟡 Watch | Identified risk accumulation 1 month ahead — reasonable |
| Eurozone Sovereign Crisis | Q3 2011 | 1.23 | 🟠 Alert | Crossed alert threshold, identified systemic risk — good |
| COVID-19 Shock | Q1 2020 | 1.15 | 🟠 Alert | Real-time crisis severity reflection — effective but could not pre-warn |
| Scenario Example | Current | 0.57 | 🟡 Watch | Sub-sovereign weight-driven moderate risk — reasonable |

### Appendix C: Quick Calculation Table

Use the following table to quickly estimate SRI for any combination of 19 industry signals:

```
SRI Estimate = (A×3 + B×2 + C×1 + D×0) / 13 × Weight Adjustment Factor

Where:
  A = Number of high-risk industries (risk score ≥ 3, including veto-forced 3)
  B = Number of medium-high risk industries (risk score 2.0-2.9)
  C = Number of medium risk industries (risk score 1.0-1.9)
  D = Number of low-risk industries (risk score < 1.0)
  
  Weight Adjustment Factor ≈ 1.3 (considering the dominance effect of heavy-weight 
  industries like sub-sovereign/LGFV, default weighted factor is 1.3)
```

**Quick Reference:**

| A (High Risk) | B (Med-High) | C (Medium) | D (Low Risk) | Weighted SRI (Est.) | Thermometer |
|--------------|-------------|-----------|-------------|--------------------|-------------|
| 0 | 0 | 1 | 12 | 0.10 | 🟢 Normal |
| 0 | 1 | 2 | 10 | 0.31 | 🟢 Normal |
| 0 | 2 | 2 | 9 | 0.51 | 🟡 Watch |
| 1 | 0 | 3 | 9 | 0.58 | 🟡 Watch |
| 1 | 2 | 2 | 8 | 0.95 | 🟡 Watch (near Alert) |
| 1 | 3 | 3 | 6 | 1.38 | 🟠 Alert |
| 2 | 2 | 3 | 6 | 1.55 | 🟠 Alert |
| 3 | 3 | 2 | 5 | 2.15 | 🔴 Danger |
| 4 | 4 | 3 | 2 | 3.02 | 🔴 Danger |
| 7 | 3 | 2 | 1 | 4.10 | 🔴 Danger (Extreme) |

### Appendix D: Version Change Log

| Version | Date | Change Content | Author |
|---------|------|---------------|--------|
| v0.0.1 | 2026-07-10 | Initial creation: SRI signal aggregation algorithm + four-level thermometer + 3 historical backtests + current calculation + threshold sensitivity analysis + engine integration plan | Engine Team |
| v0.0.1 | 2026-07-10 | System intelligence layer integration: engine version unified to v0.0.1, complete M4 portfolio risk control system with contagion matrix/concentration framework | Engine Team |

---

*This document should be used in conjunction with the Dual-Track Methodology (v0.0.3), Contagion Matrix (v0.0.3), Five-Dimensional Concentration Analysis Framework (v0.0.3), and Outlook Monitoring Framework. The Systemic Warning Framework is the top-level dashboard for the engine's M4 Portfolio Risk Control Layer, providing a unified systemic risk reading for dispersed industry signals.*
