# Systemic Warning Framework — Signal Aggregation Algorithm + Thermometer + Historical Backtests

**Version**: v0.3.1 | **Date**: 2026-07-10 | **Status**: Released

---

## Table of Contents

1. [Design Philosophy and Positioning](#1-design-philosophy-and-positioning)
2. [Signal Aggregation Algorithm](#2-signal-aggregation-algorithm)
3. [Four-Level Thermometer System](#3-four-level-thermometer-system)
4. [Industry Weights and Contagion Coefficients](#4-industry-weights-and-contagion-coefficients)
10. [Integration with Existing Engine](#10-integration-with-existing-engine)
12. [Appendix](#12-appendix)

---

> **Reading guide**: §§1-4 contain the executable methodology — signal
> aggregation, the four-level thermometer, industry weights, and contagion
> coefficients. These sections are required reading before executing any work
> path that references this document.
> §§5-9, §11, and §12 Appendices B-C (backtests, worked example, sensitivity,
> only when the analysis needs detailed justification.


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

### Appendix D: Version Change Log

| Version | Date | Change Content | Author |
|---------|------|---------------|--------|
| v0.0.1 | 2026-07-10 | Initial creation: SRI signal aggregation algorithm + four-level thermometer + 3 historical backtests + current calculation + threshold sensitivity analysis + engine integration plan | Engine Team |
| v0.0.1 | 2026-07-10 | System intelligence layer integration: engine version unified to v0.0.1, complete M4 portfolio risk control system with contagion matrix/concentration framework | Engine Team |

---

*This document should be used in conjunction with the Dual-Track Methodology (v0.3.1), Contagion Matrix (v0.3.1), Five-Dimensional Concentration Analysis Framework (v0.3.1), and Outlook Monitoring Framework. The Systemic Warning Framework is the top-level dashboard for the engine's M4 Portfolio Risk Control Layer, providing a unified systemic risk reading for dispersed industry signals.*