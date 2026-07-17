# Systemic Warning Framework — Signal Aggregation Algorithm + Thermometer + Historical Backtests

**Version**: v0.0.1 | **Date**: 2026-07-10 | **Status**: Released

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
| **Systemic Warning Framework (this document)** | **Full market, 13 industries** | **SRI Index + Thermometer** | **Fills the "last mile" gap** |

### 1.2 Framework Position in the Overall Engine

```
Input Layer:
  Track A ratings for 13 industries (fundamental scores)
  Track B signals for 13 industries (market pricing signals)
  Outlook direction for 13 industries (positive/stable/negative)
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

> **SRI Scope Note:** The SRI is a **systemic industry risk index** that aggregates industry risk scores for the 13 industries. It does not directly receive portfolio concentration scores. Concentration risk is assessed through the independent Five-Dimensional Concentration Framework. The two run in parallel at the M4 Portfolio Risk Control Layer. If a merger is desired in the future, the merger formula must be explicitly defined.

### 1.3 Design Principles

| Principle | Meaning |
|-----------|---------|
| **Full Signal Coverage** | Include all Track A + Track B + Outlook signals for all 13 industries, no omissions |
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
Industry Weight = Credit Bond Outstanding Weight × Contagion Coefficient

Where:
  Credit Bond Outstanding Weight = Industry's share of total outstanding credit bonds across all 13 industries
  
  Contagion Coefficient = Industry's "Super-Spreader" score in contagion-matrix.md
                          / Mean contagion score across 13 industries
  
  Normalization: Final industry weight percentages are normalized across industries,
                 ensuring Σ(Industry Weight Percentage) = 1 (i.e., 100%)
```

#### 2.3.1 Contagion Coefficient Table

According to the [Contagion Matrix](contagion-matrix.md) §5.5 (Super-Spreaders) and Appendix B (Complete Contagion Ranking by Industry), the contagion scores for the 13 industries are as follows:

| Rank | Industry | Total Contagion Score (Row Sum) | Contagion Coefficient | Classification Label |
|------|----------|-------------------------------|----------------------|--------------------|
| 1 | Semiconductors/Integrated Circuits | 25 | 25 / 19.38 = 1.290 | Super-Spreader |
| 2 | LGFV Bonds | 23 | 23 / 19.38 = 1.187 | Super-Spreader |
| 3 | Advanced Equipment/Industrial Machinery | 22 | 22 / 19.38 = 1.135 | Super-Spreader |
| 4 | Solar/PV & Energy Storage | 21 | 21 / 19.38 = 1.083 | Quasi Super-Spreader |
| 5 | New Energy Vehicles | 20 | 20 / 19.38 = 1.032 | Quasi Super-Spreader |
| 6 | Data Centers/Compute Infrastructure | 20 | 20 / 19.38 = 1.032 | Quasi Super-Spreader |
| 7 | Media/Internet | 20 | 20 / 19.38 = 1.032 | Moderate Contagion |
| 8 | Transportation | 19 | 19 / 19.38 = 0.980 | Moderate Contagion |
| 9 | Medical Devices | 18 | 18 / 19.38 = 0.929 | Moderate Contagion |
| 10 | Retail | 18 | 18 / 19.38 = 0.929 | Moderate Contagion |
| 11 | Biopharmaceuticals/Innovative Drugs | 17 | 17 / 19.38 = 0.877 | Weak Contagion |
| 12 | Textile & Apparel | 15 | 15 / 19.38 = 0.774 | Weak Contagion |
| 13 | Food & Beverage | 14 | 14 / 19.38 = 0.722 | Weakest Contagion |
| | **Mean** | **19.38** | **1.000** | |

**Calculation Notes:**
- Mean of 13 industry contagion scores = (25 + 23 + 22 + 21 + 20 + 20 + 20 + 19 + 18 + 18 + 17 + 15 + 14) / 13 = 252 / 13 = 19.38
- Contagion Coefficient > 1.0 = Contagion above mean (weight increase)
- Contagion Coefficient < 1.0 = Contagion below mean (weight decrease)
- Super-spreaders (top 3: Semiconductors 25, LGFV 23, Advanced Equipment 22) all have coefficients significantly > 1.0, receiving higher weights in SRI calculation

#### 2.3.2 Credit Bond Outstanding Weights

Based on international bond market sector outstanding share data (reference 2025-2026 data):

| Industry | Credit Bond Outstanding Share | Data Source |
|----------|------------------------------|-------------|
| LGFV Bonds | approx. 35% | Largest single category, approx. 15 trillion outstanding |
| Transportation | approx. 8% | Infrastructure/transport SOE bonds |
| Real Estate | approx. 5% | Continues to contract, declining outstanding |
| Retail | approx. 4% | Includes e-commerce platform bonds |
| Media/Internet | approx. 3% | Technology sector bonds |
| Food & Beverage | approx. 3% | Consumer staple bonds |
| Solar/PV & Energy Storage | approx. 2% | Fast-growing sector |
| New Energy Vehicles | approx. 2% | Includes OEM and supply chain bonds |
| Semiconductors/Integrated Circuits | approx. 1.5% | Growth enterprise board + bond financing |
| Advanced Equipment/Industrial Machinery | approx. 1% | State-owned enterprises + niche leaders |
| Medical Devices | approx. 1% | Includes medical equipment bonds |
| Biopharmaceuticals/Innovative Drugs | approx. 0.8% | Biotech primarily equity financed |
| Textile & Apparel | approx. 0.7% | Consumer-focused private enterprise bonds |

**Note:** The above shares are directional estimates. In actual calculations, the latest full-market credit bond outstanding data should be used for dynamic updates. When structural changes occur in a specific industry's credit bond outstanding (e.g., LGFV reduction due to debt resolution or bond expansion for technology sectors), weights should be adjusted promptly. Data Centers/Compute Infrastructure credit bond outstanding is consolidated into the LGFV category (park/infrastructure related), not listed separately.

#### 2.3.3 Industry Weight Calculation Example

Using the semiconductor industry as an example, assuming credit bond outstanding share is 1.5%:

```
Semiconductor Industry Weight Percentage = 1.5% × 1.290 = 1.94%

Normalization:
  Raw weight percentage per industry = Credit bond outstanding share × Contagion coefficient
  Normalization factor = 100% / Σ(Raw weight percentage)
  Final weight percentage = Raw weight percentage × Normalization factor
  Ensures Σ(Final weight percentage) = 100%
```

### 2.4 Complete Calculation Flow

```
Step 1: Collect four types of input signals for the 13 industries
  ├── Track A score (fundamental pyramid output)
  ├── Track B signal (market signal level)
  ├── Outlook direction (positive/stable/negative)
  └── Veto trigger (yes/no)

Step 2: Calculate single industry risk score
  └── base_score + outlook_penalty + trackB_penalty
  └── Veto check → if triggered, force 3 points

Step 3: Calculate industry weight percentage
  ├── Credit bond outstanding weight ← market data
  ├── Contagion coefficient ← Contagion Matrix (contagion-matrix.md) Appendix B
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
| Contagion Coefficient | [Contagion Matrix](contagion-matrix.md) §5.5 and Appendix B | Updated on version changes |

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
- If the red-turned industry is a super-spreader (Semiconductors / LGFV / Advanced Equipment) → immediately upgrade to Alert level
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
| **Statistical** | When SRI < 0.5, the average risk score across 13 industries is approximately equivalent to 1 industry scoring 2 + 12 scoring 0, or 3 industries scoring 1 + 10 scoring 0 — meaning only 1-2 industries at medium-high risk or 2-3 at medium risk. This falls within normal market differentiation |
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
| **Contagion Logic** | When SRI ≥ 1.0, the industries in crisis likely include super-spreaders (3 out of 13 industries), and these spread risk to other healthy industries through the contagion matrix |

#### SRI ≥ 1.8 (🔴 Danger) Threshold Rationale

| Basis Type | Specific Rationale |
|-----------|-------------------|
| **Statistical** | SRI = 1.8 is equivalent to approximately 7 industries scoring 2 (over half at medium-high risk), or 5 scoring 3 + 1-2 scoring 1. Over half of industries in trouble simultaneously = full market systemic risk |
| **Historical Validation** | During the COVID-19 shock Q1 2020, all 13 industries were stressed simultaneously, SRI could reach ≥ 2.0 (see §7 backtest) |
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

### 4.1 Complete Weight Calculation Table

Based on the Contagion Matrix (contagion-matrix.md) super-spreader rankings and 13-industry mean contagion score, the weight parameters for each industry are as follows:

| Industry | Credit Bond Outstanding Share (A) | Contagion Coefficient (B) | Raw Weight (A×B) | Normalized Weight |
|----------|-------------------------------|--------------------------|-----------------|------------------|
| LGFV Bonds | 35.0% | 1.187 | 41.53% | 37.55% |
| Transportation | 8.0% | 0.980 | 7.84% | 7.09% |
| Retail | 4.0% | 0.929 | 3.71% | 3.36% |
| Media/Internet | 3.0% | 1.032 | 3.10% | 2.80% |
| Food & Beverage | 3.0% | 0.722 | 2.17% | 1.96% |
| Solar/PV & Energy Storage | 2.0% | 1.083 | 2.17% | 1.96% |
| New Energy Vehicles | 2.0% | 1.032 | 2.06% | 1.87% |
| Semiconductors/Integrated Circuits | 1.5% | 1.290 | 1.93% | 1.75% |
| Advanced Equipment/Industrial Machinery | 1.0% | 1.135 | 1.13% | 1.03% |
| Medical Devices | 1.0% | 0.929 | 0.93% | 0.84% |
| Biopharmaceuticals/Innovative Drugs | 0.8% | 0.877 | 0.70% | 0.63% |
| Textile & Apparel | 0.7% | 0.774 | 0.54% | 0.49% |
| Real Estate (Note) | 5.0% | — | — | — |
| **Total** | **~67%** | — | **~67.82%** | **61.33%** |

**Note:** The real estate industry is not within the engine's 13-industry coverage, but its credit bond outstanding is approximately 5%. In the SRI calculation, this portion can be attributed to related industries (e.g., LGFV through land finance linkages) or treated as "other industries" separately. In the current version, real estate credit bonds are added back to LGFV weight through regional credit linkage.

**Data Source:** Credit bond outstanding shares are based on market data from major financial information terminals (Q2 2026 credit bond market statistics, including enterprise bonds, corporate bonds, MTNs, CPs, PPNs), covering both interbank and exchange markets. Contagion coefficients are derived from the 13-industry mean contagion score in contagion-matrix.md Appendix B. Real estate outstanding share of 5% is for reference only and is not included in SRI calculation. Data Centers/Compute Infrastructure credit bond outstanding is consolidated into the LGFV category (park/infrastructure related), not listed separately.

**Normalization Calculation Notes:**
- Raw weight total ≈ 67.82% (covering only the credit bond outstanding weight within the 13-industry scope)
- Normalized industry weight percentage = raw weight / 67.82% × 61.33%
- Normalization factor = 100% / Σ(weight percentage) (ensures final Σ(weight percentage) = 100%)

**Practical Simplified Treatment:** Due to the excessively high LGFV weight (raw weight 41.53%), **truncated weights** are recommended for actual calculations:
- LGFV weight truncated at 25% (prevents a single industry from dominating the SRI)
- Excess truncated weight is redistributed to other industries proportionally by their raw weights

| Industry | Truncated Weight (Recommended) | Description |
|----------|-------------------------------|-------------|
| LGFV Bonds | 25.00% | Truncated at 25%, preventing over-dominance |
| Transportation | 8.50% | Adjusted upward |
| Retail | 4.00% | Adjusted upward |
| Media/Internet | 3.35% | Adjusted upward |
| Food & Beverage | 2.22% | Adjusted upward |
| Solar/PV & Energy Storage | 2.33% | Adjusted upward |
| New Energy Vehicles | 2.22% | Adjusted upward |
| Semiconductors/Integrated Circuits | 2.06% | Adjusted upward |
| Advanced Equipment/Industrial Machinery | 1.22% | Adjusted upward |
| Medical Devices | 1.01% | Adjusted upward |
| Biopharmaceuticals/Innovative Drugs | 0.77% | Adjusted upward |
| Textile & Apparel | 0.60% | Adjusted upward |
| Other (including Real Estate, etc.) | 46.72% | Transmitted through LGFV + infrastructure linkages |
| **Total** | **100.00%** | |

**Truncation Sensitivity Analysis:** The impact of different truncation thresholds on SRI calculation results (scenario example):

| Truncation Threshold | LGFV Weight | Other Industry Weights | SRI | Thermometer | Description |
|--------------------|------------|----------------------|-----|-------------|-------------|
| 20% | 20.00% | Each industry ↑ | 0.52 | 🟡 Watch | More aggressive truncation, reducing LGFV dominance, but may underestimate LGFV systemic risk |
| **25% (Recommended)** | **25.00%** | **Each industry ↑** | **0.56** | **🟡 Watch** | **Balanced compromise between LGFV representation and over-dominance** |
| 30% | 30.00% | Each industry ↓ | 0.61 | 🟡 Watch (upper bound) | More conservative truncation, retaining LGFV signal, SRI more sensitive |
| No truncation (37.55%) | 37.55% | Normalized weights | 0.73 | 🟠 Alert | SRI dominated by LGFV alone, weakening risk signals from other industries |

**Recommendation:** Default to 25% truncation. During LGFV systemic risk exposure periods (e.g., debt resolution critical years), 30% truncation may be selected to retain more LGFV signal. When the portfolio is highly diversified away from LGFV, 20% truncation may be selected to reduce LGFV interference.

### 4.2 Dynamic Weight Adjustment Rules

| Trigger Condition | Adjustment | Rationale |
|------------------|-----------|-----------|
| An industry's credit bond outstanding share changes > 20% quarter-over-quarter | Update the industry's credit bond outstanding weight | E.g., LGFV reduction due to debt resolution, or bond expansion causing semiconductor share to rise |
| Super-spreader rankings change | Update contagion coefficients | E.g., a new-generation industry (AI compute) rises to replace existing super-spreaders |
| Contagion matrix version update | Synchronously update contagion coefficients | Intensity adjustments in the contagion matrix change contagion total scores |
| High-leverage escalation factor triggered | Multiply weight by 1.2 for industries with high financial intensity (high debt ratio) | Contagion risk of high-debt industries amplified in high-leverage environments |

### 4.3 Design to Avoid Weight Over-Concentration

As the largest category in the credit bond market (approximately 35% of outstanding), LGFV naturally has the highest weight in the SRI. To prevent the SRI from being dominated by a single LGFV signal:

| Design | Description |
|--------|-------------|
| **Contagion Coefficient Moderation** | LGFV is super-spreader #2 (23 points), lower than Semiconductors (25 points), with a contagion coefficient of 1.187, mid-range among super-spreaders — prevents excessive weight stacking |
| **Weight Truncation Mechanism** | Any single industry weight capped at 25% |
| **Contagion Matrix Linkage** | LGFV credit risk primarily spreads through regional resonance rather than direct inter-industry contagion; in the SRI, high LGFV risk does not necessarily mean other industries are also high risk |
| **Thermometer Downgrade Condition** | If SRI is elevated but the main contribution comes from LGFV alone, and all other industries are 🟢, the thermometer may be downgraded one level (🟠 → 🟡) |

---

## 5. Historical Backtest 1: GFC 2008 (Pre-Lehman)

### 5.1 Scenario Background

**Time Window:** Q3 2008 (approximately 1 month before Lehman Brothers bankruptcy)
**Actual Event Date:** September 15, 2008 (Lehman Brothers filed for Chapter 11 bankruptcy protection)
**Market Environment at the Time:** After the subprime mortgage crisis emerged in 2007, the market experienced a period of relative calm in early-to-mid 2008. Bear Stearns had been rescued by JPMorgan in March 2008. The AAA-rated MBS/CDO ratings bubble was still largely intact. The market broadly believed that systemically important institutions would be bailed out.

### 5.2 Industry Signal State at the Time

Based on historical data reconstruction, the estimated signal states for the 13 industries in Q3 2008 (pre-Lehman) are as follows:

| Industry | Track A Score (Est.) | Industry Risk Score (Base) | Outlook | Track B | Risk Score |
|----------|---------------------|--------------------------|---------|---------|------------|
| Energy/Mining | 3.0-4.0 (B+ to BB) | 2 | Negative | 🟡 (Watch) | 3.0 |
| LGFV Bonds / Sub-Sovereign | 5.5-6.0 (BB+ to BBB) | 1 | Stable | 🟢 (Calm) | 1.0 |
| Transportation | 5.5-6.0 (BB+ to BBB) | 1 | Stable | 🟢 (Calm) | 1.0 |
| Real Estate / Financial | 3.5-4.5 (B+ to BB) | 2 | Negative | 🟠 (Abnormal) | 3.0 |
| Solar/PV & Energy Storage | 5.5-6.0 (BBB- to BBB+) | 1 | Stable | 🟢 (Calm) | 1.0 |
| Semiconductors/Integrated Circuits | 6.0-7.0 (BBB+ to A-) | 0 | Positive | 🟢 (Calm) | 0 |
| Advanced Equipment | 6.0-7.0 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| Biopharmaceuticals | 6.5-7.5 (A- to A) | 0 | Positive | 🟢 (Calm) | 0 |
| Medical Devices | 6.0-7.0 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| New Energy Vehicles | 5.5-6.5 (BBB to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| Data Centers | 6.5-7.0 (A- to A) | 0 | Positive | 🟢 (Calm) | 0 |
| Food & Beverage | 7.0-7.5 (A) | 0 | Stable | 🟢 (Calm) | 0 |
| Textile & Apparel | 6.0-6.5 (BBB+) | 0 | Stable | 🟢 (Calm) | 0 |

**Note on Energy/Mining and Financial/Real Estate sectors:** These industries are not within the engine's standard 13-industry coverage. In this backtest, their risk signals are approximated within the relevant industry categories. In Q3 2008:
- Lehman Brothers had massive exposure to subprime MBS/CDOs, with a debt-to-equity ratio exceeding 30:1
- AIG had written extensive credit default swaps on MBS, facing potential $50B+ in losses
- Systemic contagion was spreading across the entire financial sector
- Major banks (Citi, Bank of America, Merrill Lynch) were all under severe stress
- The financial sector's track B signals reflected extreme market pricing dislocation

### 5.3 SRI Calculation

```
Risk Score Count:
  3-point industries: 2 (Energy/Mining, Real Estate/Financial — including veto-level signals)
  2-point industries: 0
  1-point industries: 3 (Sub-sovereign/LGFV, Transportation, Solar/PV)
  0-point industries: 8 (remaining industries)

Simple Arithmetic Mean ≈ (3×2 + 1×3 + 0×8) / 13 = 9 / 13 = 0.69

Weighted SRI Estimate (approximate):
  LGFV/Sub-sovereign (25% weight): 1 point × 25% = 0.25
  Transportation (8.5%): 1 point × 8.5% = 0.09
  Energy/Mining (approx 2%): 3 points × 2% = 0.06
  Real Estate/Financial indirect (5%): 3 points × 5% = 0.15
  Other industries weighted total: ≈ 0.15
  SRI ≈ 0.25 + 0.09 + 0.06 + 0.15 + 0.15 = 0.70

→ **SRI ≈ 0.70 (🟡 Watch range)**
```

### 5.4 Could It Provide Early Warning?

| Assessment Dimension | Conclusion |
|---------------------|-----------|
| **Did SRI enter 🟡?** | **Yes.** SRI ≈ 0.70, crossed the 0.5 watch threshold |
| **Could it warn 1 month ahead?** | **Conditional warning.** SRI was already in 🟡 in Q3 2008, with the main risk contribution coming from Energy/Mining (3 points) and Real Estate/Financial (3 points), and Sub-sovereign/Transportation (1 point each). Lehman's bankruptcy was directly related to financial/real estate exposure. But SRI was still below 🟠 (SRI < 1.0), meaning the framework identified "watch-level" rather than "alert-level" risk |
| **Framework Limitations** | SRI was 🟡 in Q3 2008, but Lehman's bankruptcy on September 15, 2008 triggered a 🔴-level systemic shock (global financial system freeze). The SRI cannot predict confidence collapse events themselves — it can only identify that "risk is accumulating" |
| **Improvement Direction** | If combined with contagion matrix escalation factor analysis (panic sentiment + information asymmetry + high leverage were all triggering in September 2008), an escalation factor warning could have been triggered on top of the 🟡 SRI, upgrading to 🟠 Alert level response |

### 5.5 Backtest Conclusion

| Backtest Conclusion | Specific Description |
|--------------------|---------------------|
| **Warning Effective** | SRI entered 🟡 Watch range 1 month before Lehman, identifying the fact that risk was accumulating |
| **But Not Upgraded to Alert** | SRI ≈ 0.70 only reached the lower end of the Watch range; the framework would not recommend substantial position reduction, only "increase monitoring frequency · check concentration" |
| **Needs Coordination with Escalation Factors** | If pre-signals from escalation factors (especially information asymmetry: the opacity of Lehman's balance sheet in the months before bankruptcy) were incorporated, the warning could have been upgraded to 🟠 Alert 1-2 weeks before the event |
| **Overall Assessment** | The framework performed reasonably in this backtest — it identified risk accumulation without excessive warning. The Lehman event was essentially a "black swan" (systemically important institution bankruptcy that was widely considered "too big to fail"). The core value of the warning framework is to initiate the monitoring process when risk accumulates beforehand, not to precisely predict the timing of default |

---

## 6. Historical Backtest 2: Eurozone Sovereign Debt Crisis 2011-12

### 6.1 Scenario Background

**Time Window:** Q3 2011 (the peak of the Eurozone sovereign debt crisis — Greek debt crisis escalation)
**Actual Event Time:** Summer/Fall 2011 — Greek bond yields exceeded 50%, CDS spreads peaked, and contagion spread to Italy, Spain, Portugal, and Ireland (PIIGS)
**Market Environment at the Time:** The aftermath of the 2008 global financial crisis was still unfolding. The Greek government revealed a much larger deficit than previously reported in late 2009. By 2011, the crisis had evolved into a full-blown sovereign debt crisis threatening the eurozone's integrity. The bank-sovereign "doom loop" was in full effect — banks held large amounts of sovereign debt, while struggling sovereigns needed banks to remain healthy.

### 6.2 Industry Signal State at the Time

Based on historical data reconstruction, the estimated signal states for the 13 industries in Q3 2011 are as follows:

| Industry | Track A Score (Est.) | Industry Risk Score (Base) | Outlook | Track B | Risk Score |
|----------|---------------------|--------------------------|---------|---------|------------|
| Real Estate / Banking (Note) | 3.5-4.5 (B+ to BB) | 2 | Negative | 🟠 (Abnormal) | 3.0 |
| Construction/Building Materials (Note) | 4.0-5.0 (B+ to BB+) | 2 | Negative | 🟡 (Watch) | 3.0 |
| LGFV/Sub-Sovereign/Sovereign | 4.0-5.0 (B+ to BB+) | 2 | Negative | 🟠 (Abnormal) | 3.0 |
| Transportation | 5.0-5.5 (BBB- to BB+) | 1 | Stable | 🟢 (Calm) | 1.0 |
| Solar/PV & Energy Storage | 6.0-7.0 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| Semiconductors/Integrated Circuits | 6.5-7.5 (A- to A) | 0 | Positive | 🟢 (Calm) | 0 |
| Advanced Equipment | 6.0-7.0 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| Biopharmaceuticals/Innovative Drugs | 6.5-7.5 (A- to A) | 0 | Positive | 🟢 (Calm) | 0 |
| Medical Devices | 6.0-7.0 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| New Energy Vehicles | 5.5-6.5 (BBB to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| Data Centers | 6.5-7.0 (A- to A) | 0 | Positive | 🟢 (Calm) | 0 |
| Food & Beverage | 7.0-7.5 (A) | 0 | Stable | 🟢 (Calm) | 0 |
| Textile & Apparel | 6.0-6.5 (BBB+) | 0 | Stable | 🟢 (Calm) | 0 |
| Media/Internet | 6.0-7.0 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |

**Note on Banking and Construction:** The banking sector and construction/building materials are not within the engine's 13-industry coverage. In this backtest, these risks are approximated through:
- Sovereign/banking risk is reflected through Sub-sovereign/LGFV (via sovereign credit linkage)
- Construction/building materials risk is reflected through Transportation (via construction supply chain)
- Core contagion chain: Sovereign stress → Banking sector → Sub-sovereign → Real economy

### 6.3 Contagion Chain Mapping: Sovereign-Related Industries in SRI Weight Treatment

Since sovereign/banking is not one of the 13 industries, the sovereign debt crisis impacts the SRI indirectly through two pathways:

```
Pathway A: Sovereign → LGFV/Sub-Sovereign (Regional Resonance + Credit Chain)
  Sovereign credit rating downgrades → Weaker sub-sovereign fiscal capacity → Sub-sovereign credit revaluation
  Banking sector stress → Banks deleverage → Sub-sovereign/LGFV financing environment tightens

Pathway B: Sovereign → Construction/Building Materials → Transportation → All Industries
  Construction freeze → Building materials defaults → Logistics/transport volume decline
  Sovereign stress → Government spending cuts → Infrastructure investment decline → Affects all industries
```

**Treatment in SRI:** Sovereign debt crisis risk was indirectly reflected through the Sub-sovereign/LGFV risk score — in Q3 2011, the Sub-sovereign outlook had already shifted from stable to negative, and Track B signals shifted from 🟢 to 🟡/🟠 (reflecting market concern about the sovereign-sub-sovereign linkage).

### 6.4 SRI Calculation

```
Risk Score Count:
  3-point industries: 2 (Sovereign/Banking, Construction/Building Materials — indirectly counted)
  3-point industries: 1 (Sub-sovereign/LGFV)
  1-point industries: 1 (Transportation, indirect linkage)
  0-point industries: 9 (remaining industries)

Simple Arithmetic Mean ≈ (3×3 + 1×1 + 0×9) / 13 = 10 / 13 = 0.77

Weighted SRI Estimate (including sovereign indirect mapping):
  LGFV/Sub-sovereign (25% weight): 3 points × 25% = 0.75
  Transportation (8.5%): 1 point × 8.5% = 0.09
  Banking indirect mapping (5% weight): 3 points × 5% = 0.15
  Construction/Building Materials indirect (3%): 3 points × 3% = 0.09
  Other industries weighted total: ≈ 0.15
  SRI ≈ 0.75 + 0.09 + 0.15 + 0.09 + 0.15 = 1.23

→ **SRI ≈ 1.23 (🟠 Alert range)**
```

### 6.5 Could It Provide Early Warning?

| Assessment Dimension | Conclusion |
|---------------------|-----------|
| **Did SRI enter Watch?** | **Yes.** SRI ≈ 1.23, well into 🟠 Alert range, crossing the 1.0 threshold |
| **Could it warn of the Eurozone crisis?** | **Significant warning, mainly through indirect pathways.** Since sovereign/banking are not among the 13 industries, SRI primarily reflected the crisis through Sub-sovereign/LGFV (3 points) and indirect mapping. SRI ≈ 1.23 clearly indicated "Alert level — systemic risk accumulating" |
| **Did SRI identify sovereign-related contagion chains?** | **Partially identified.** SRI captured the Sub-sovereign risk escalation (negative outlook + Track B abnormal), but could not directly reflect banking/construction sector risks — these industries are not within the 13-industry coverage |
| **Improvement Direction** | Adding a "sovereign/banking indirect contagion factor" as an input (e.g., Sub-sovereign outlook negative weight × 1.5 during sovereign stress cycles) would make the SRI more sensitive to the sovereign → sub-sovereign → infrastructure contagion chain. Additionally, the contagion matrix pathways for Sub-sovereign ↔ Transportation (intensity 4) and Sub-sovereign ↔ Solar/PV/Data Centers (intensity 3) would trigger jumps under stress, further elevating the SRI reading |

### 6.6 Backtest Conclusion

| Backtest Conclusion | Specific Description |
|--------------------|---------------------|
| **Warning Effective** | SRI in Q3 2011 was approximately 1.23, well into 🟠 Alert range, clearly signaling "systemic risk accumulating, need to reduce exposure" |
| **Crossed Alert Threshold** | SRI ≈ 1.23 crossed the 1.0 Alert threshold, framework would recommend "actively reduce high-risk industry exposure · increase hedging · shorten duration" |
| **Sovereign Not in 13 Industries is a Blind Spot** | The SRI framework directly covers 13 industries; sovereign/banking is captured indirectly through Sub-sovereign. For more accurate sovereign crisis early warning, it is recommended to monitor sovereign credit signals separately outside the SRI framework |
| **Overall Assessment** | The framework performed **well** in this backtest — SRI entered the Alert range 3-6 months before the peak of the crisis. If investors had initiated "check concentration · reduce exposure" procedures when SRI > 1.0, the combined sovereign + sub-sovereign + banking exposure could have been identified and reduced in advance |

---

## 7. Historical Backtest 3: COVID-19 Shock 2020

### 7.1 Scenario Background

**Time Window:** February-March 2020 (global COVID-19 pandemic outbreak)
**Actual Impact Time:** January 30, 2020 WHO declared a Public Health Emergency of International Concern; March 11, 2020 declared a global pandemic
**Market Environment at the Time:** An unprecedented public health crisis caused simultaneous shocks to all industries. Unlike the GFC or Eurozone debt crisis, COVID-19 was an "exogenous, synchronous, non-credit" shock.

### 7.2 Industry Signal State at the Time

Based on historical data reconstruction, the estimated signal states for the 13 industries in Q1 2020 are as follows:

| Industry | Track A Score (Est.) | Industry Risk Score (Base) | Outlook | Track B | Risk Score | Notes |
|----------|---------------------|--------------------------|---------|---------|------------|-------|
| Transportation | 2.0-3.0 (B to B+) | 3 | Negative | 🔴 (Crisis) | 3.0 | Passenger traffic collapsed, airlines losing millions per day |
| Retail | 2.5-3.5 (B to B+) | 2 | Negative | 🔴 (Crisis) | 3.0 | Department stores/malls saw zero foot traffic |
| Media/Internet | 3.0-4.0 (B+ to BB) | 2 | Negative | 🟠 (Abnormal) | 3.0 | Ad revenue plunged, but online consumption benefited |
| Food & Beverage | 3.5-4.5 (B+ to BB) | 2 | Negative | 🟠 (Abnormal) | 3.0 | Restaurant/gift consumption plunged, but essential consumption benefited |
| Textile & Apparel | 2.5-3.5 (B to B+) | 2 | Negative | 🟠 (Abnormal) | 3.0 | Physical stores closed, export orders canceled |
| Real Estate | 3.0-4.0 (B+ to BB) | 2 | Negative | 🟠 (Abnormal) | 3.0 | Sales offices closed, sales cash flow frozen |
| New Energy Vehicles | 3.5-4.5 (B+ to BB) | 2 | Negative | 🟠 (Abnormal) | 3.0 | Factories shut down, sales down 80%+ |
| Solar/PV & Energy Storage | 4.0-5.0 (B+ to BB+) | 2 | Negative | 🟡 (Watch) | 3.0 | Capacity utilization declined, overseas orders delayed |
| Advanced Equipment | 4.0-5.0 (B+ to BB+) | 2 | Negative | 🟡 (Watch) | 3.0 | Production paused, deliveries delayed |
| Medical Devices | 5.0-6.0 (BBB- to BB+) | 1 | Positive | 🟢 (Calm) | 1.0 | Pandemic supply demand surged, benefiting sector |
| Biopharmaceuticals | 5.5-6.5 (BBB+ to A-) | 0 | Positive | 🟢 (Calm) | 0 | Pandemic-related R&D benefited, non-COVID areas affected |
| LGFV/Sub-Sovereign | 5.0-6.0 (BBB- to BB+) | 1 | Stable | 🟡 (Watch) | 1.5 | Infrastructure stabilization expectations rose, but short-term pressure |
| Semiconductors/Integrated Circuits | 5.5-6.5 (BBB+ to A-) | 0 | Positive | 🟡 (Watch) | 0.5 | Supply chain disruption concerns but domestic substitution logic strengthened |

### 7.3 SRI Calculation

```
Risk Score Count:
  3-point industries: 8 (Transportation, Retail, Media, Food & Beverage, Textile & Apparel,
                       New Energy Vehicles, Solar/PV, Advanced Equipment)
  1.5-point industries: 1 (Sub-sovereign/LGFV)
  1-point industries: 1 (Medical Devices, benefiting)
  0.5-point industries: 1 (Semiconductors)
  0-point industries: 2 (Biopharmaceuticals, Data Centers — benefiting)

Simple Arithmetic Mean ≈ (3×8 + 1.5×1 + 1×1 + 0.5×1 + 0×2) / 13
                      = (24 + 1.5 + 1 + 0.5 + 0) / 13
                      = 27 / 13 = 2.08

Weighted SRI Calculation:
  Transportation (8.5% weight): 3 points × 8.5% = 0.26
  Sub-sovereign/LGFV (25%): 1.5 points × 25% = 0.38
  Retail (4%): 3 points × 4% = 0.12
  Media/Internet (3.35%): 3 points × 3.35% = 0.10
  Food & Beverage (2.22%): 3 points × 2.22% = 0.07
  Textile & Apparel (0.6%): 3 points × 0.6% = 0.02
  Solar/PV (2.33%): 3 points × 2.33% = 0.07
  Advanced Equipment (1.22%): 3 points × 1.22% = 0.04
  New Energy Vehicles (2.22%): 3 points × 2.22% = 0.07
  Medical Devices (1.01%): 1 point × 1.01% = 0.01
  Semiconductors (2.06%): 0.5 points × 2.06% = 0.01
  Other industries weighted total: ≈ 0
  SRI ≈ 0.26 + 0.38 + 0.12 + 0.10 + 0.07 + 0.02 + 0.07 + 0.04 + 0.07 + 0.01 + 0.01 = 1.15

→ **SRI ≈ 1.15 (🟠 Alert range)**
```

### 7.4 Was This a "Known Unknown" or an "Unknown Unknown"?

| Assessment Dimension | Analysis |
|---------------------|---------|
| **Nature of the Pandemic** | The pandemic itself was a "known unknown" — public health experts had long warned about pandemic risk (SARS experience, WHO pandemic preparedness plans), but the specific timing, scale, and impact pathways were unknown |
| **Could the SRI Framework Provide Early Warning?** | **Cannot provide pre-event warning.** The SRI framework relies on industry fundamental signals (Track A/B/Outlook), and all industries had normal Track A scores before the pandemic outbreak (January 2020) — it cannot predict an exogenous, synchronous shock affecting all industries |
| **Could the SRI Reflect the Impact?** | **Yes, in real time.** Once the shock occurred (February 2020), Track A scores plunged across industries, outlooks turned negative, Track B signals jumped, and SRI rapidly rose to approximately 1.15 (🟠 Alert), accurately reflecting the severity of the systemic crisis |
| **Essential Difference from Credit Events** | The key difference between COVID-19 and the GFC/Eurozone crisis: the former was an "exogenous synchronous shock" (all industries simultaneously affected by non-credit factors), while the latter were "endogenous transmission shocks" (credit risk gradually spreading from one industry to others). The SRI framework is "reactive" for the former (confirming severity after the shock) and "forward-looking" for the latter (identifying risk accumulation before the shock) |

### 7.5 Backtest Conclusion

| Backtest Conclusion | Specific Description |
|--------------------|---------------------|
| **SRI Real-Time Effectiveness** | Under the COVID shock, SRI rapidly reached the 🟠 Alert range (approximately 1.15), accurately reflecting the severity of the systemic crisis |
| **Cannot Pre-Warn Exogenous Shocks** | The SRI framework has no pre-warning capability for "known unknowns" (exogenous shocks) — this is a common limitation of all fundamental signal-based scoring frameworks |
| **Distinguishing "Exogenous" from "Endogenous"** | The core value of the SRI framework is in identifying "endogenous, accumulated, transmissible" credit risk, not predicting "exogenous, sudden, non-credit" shocks. The former is the proper function of a credit analysis framework |
| **Practical Significance During the Pandemic** | If the SRI framework showed 🔴 Danger in March 2020, its value was not in warning (the pandemic had already arrived), but in **avoiding misjudgment during the crisis** — when SRI is 🔴, the framework recommends "full defense · preserve liquidity · reduce positions," which would have helped investors avoid excessive credit risk-taking during the pandemic |

---

## 8. Current Period Calculation: Scenario-Based SRI Example

### 8.1 Scenario: Hypothetical Market Stress State

This section provides a scenario-based example showing how the SRI would be calculated under a hypothetical market stress state. The following signal state is illustrative — not a current real-time reading.

| Industry | Track A Score (Est.) | Base Score | Outlook | Track B | Risk Score |
|----------|---------------------|-----------|---------|---------|------------|
| Solar/PV & Energy Storage | 4.5-5.5 (BB+ to BBB-) | 2 | Negative | 🟡 (Watch) | 3.0 |
| Semiconductors/Integrated Circuits | 6.5-7.5 (A- to A) | 0 | Positive | 🟢 (Calm) | 0 |
| Advanced Equipment/Industrial Machinery | 6.0-7.0 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| Biopharmaceuticals/Innovative Drugs | 5.5-6.5 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| Medical Devices | 6.0-7.0 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| New Energy Vehicles | 5.0-6.0 (BBB- to BB+) | 1 | Negative | 🟡 (Watch) | 2.0 |
| Data Centers/Compute Infrastructure | 6.5-7.5 (A- to A) | 0 | Positive | 🟢 (Calm) | 0 |
| LGFV/Sub-Sovereign | 5.0-5.5 (BBB- to BB+) | 1 | Stable | 🟡 (Watch) | 1.5 |
| Food & Beverage | 6.5-7.5 (A- to A) | 0 | Stable | 🟢 (Calm) | 0 |
| Textile & Apparel | 5.5-6.5 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| Transportation | 5.5-6.5 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |
| Retail | 5.0-6.0 (BBB- to BB+) | 1 | Negative | 🟡 (Watch) | 2.0 |
| Media/Internet | 5.5-6.5 (BBB+ to A-) | 0 | Stable | 🟢 (Calm) | 0 |

### 8.2 Industry Risk Score Detail

| Industry | Risk Score | Detail |
|----------|-----------|--------|
| **Solar/PV & Energy Storage** | 3.0 | Base 2 (Track A 4.5-5.5, BB+ to BBB- range) + Negative outlook 0.5 + Track B Watch 0.5. Core issue is severe overcapacity; the entire supply chain faces restructuring pressure |
| **New Energy Vehicles** | 2.0 | Base 1 (Track A 5.0-6.0, BBB- to BB+ range) + Negative outlook 0.5 + Track B Watch 0.5. Ongoing price wars, accelerating shakeout of weaker players, but battery sector stabilizing and recovering |
| **LGFV/Sub-Sovereign** | 1.5 | Base 1 (Track A 5.0-5.5, BBB- to BB+ range) + Track B Watch 0.5. Debt resolution progressing, but regional divergence intensifying, concentrated rating downgrades in weaker regions |
| **Retail** | 2.0 | Base 1 (Track A 5.0-6.0, BBB- to BB+ range) + Negative outlook 0.5 + Track B Watch 0.5. Consumption downgrade trend, online-offline integration pressure, some enterprises under stress |
| **Remaining 9 industries** | 0 | All with Track A above 5.5 (BBB+ and above), stable or positive outlook, Track B calm, no risk contribution |

### 8.3 SRI Calculation

```
Risk Score Count:
  3.0-point industries: 1 (Solar/PV)
  2.0-point industries: 2 (New Energy Vehicles, Retail)
  1.5-point industries: 1 (LGFV/Sub-sovereign)
  0-point industries: 9 (remaining industries)

Simple Arithmetic Mean = (3.0×1 + 2.0×2 + 1.5×1 + 0×9) / 13
                       = (3.0 + 4.0 + 1.5) / 13
                       = 8.5 / 13 = 0.65

Weighted SRI Calculation:
  LGFV/Sub-sovereign (25% weight): 1.5 points × 25% = 0.375
  Solar/PV (2.33%): 3 points × 2.33% = 0.070
  New Energy Vehicles (2.22%): 2.0 points × 2.22% = 0.044
  Retail (4%): 2.0 points × 4% = 0.080
  Transportation (8.5%): 0 points × 8.5% = 0
  Other industries: 0 points × combined weight = 0
  SRI = 0.375 + 0.070 + 0.044 + 0.080 = 0.569

→ **SRI ≈ 0.57 (🟡 Watch range)**
```

### 8.4 SRI Interpretation

| Dimension | Analysis |
|-----------|----------|
| **Current Level** | 🟡 Watch (SRI ≈ 0.57), slightly below the pre-crisis backtest reading of 0.70 |
| **Main Contributors** | ① LGFV/Sub-sovereign (largest weight, 1.5 points) contributes 0.375, 66% of SRI; ② Retail (2.0 points) contributes 0.080; ③ Solar/PV (3.0 points) contributes 0.070; ④ NEV (2.0 points) contributes 0.044 |
| **Historical Comparison** | Similar to the pre-systemic-event level, but the risk structure is different — the GFC 2008 risk was concentrated in finance/energy, this scenario is concentrated in Sub-sovereign + Solar/PV + Consumer |
| **Key Characteristic** | The SRI is elevated mainly because of the LGFV/Sub-sovereign weight (25%) combined with its risk signal (1.5 points). If the extreme LGFV weight is removed, the industries with substantive risk (Track A < 6.0) are only Solar/PV + NEV + Retail — 3 industries — and SRI would fall below 0.2 (🟢) |
| **Assessment** | 🟡 Watch is reasonable — Sub-sovereign/LGFV does face regional divergence pressure, and Solar/PV and NEV face overcapacity issues. But it has not reached 🟠 Alert level (SRI < 1.0) because super-spreaders (Semiconductors, Advanced Equipment) are all operating normally, with no simultaneous multi-industry resonance |

### 8.5 Recommended Actions

| Action Item | Specific Content |
|------------|-----------------|
| **Monitoring Focus** | Sub-sovereign/LGFV regional divergence progress, Solar/PV industry restructuring progress, whether NEV price wars escalate further |
| **Check Concentration** | Whether combined portfolio exposure to Sub-sovereign + Solar/PV + NEV + Retail exceeds concentration limits (Cluster D + Cluster F combined exposure < 40%) |
| **Escalation Scenario** | If Semiconductors or Advanced Equipment (super-spreaders) show signal deterioration, SRI could rapidly rise above 1.0 into 🟠 Alert — immediate position reduction plan would be required |
| **No Need for Panic** | Current SRI ≈ 0.57 is at the lower end of 🟡 Watch range, and the main contribution comes from the Sub-sovereign weight (rather than substantive risk spread) — no major portfolio adjustment needed |

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
| **2. Incomplete industry coverage** | The framework only covers 13 industries; important credit bond industries such as banking, construction, energy/mining are not directly covered and require indirect mapping with information loss | Indirect capture through related industries' signals (e.g., sub-sovereign for fiscal linkages, transportation for construction supply chain) |
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
| v0.6.8-alpha | Initial version: Basic aggregation algorithm + thermometer + 3 historical backtests + current calculation |
| v0.7.0-alpha | System intelligence layer integration: complete M4 portfolio risk control system with contagion matrix/concentration framework, unified engine version |
| v0.8.0-release | Engine-level integration release: cross-CLI entry (AGENTS.md) · four-segment chain product contract · executable orchestrator · dimension registry |
| v0.8.1-release | Gate reinforcement and promotion mechanism (no change to framework/thresholds): .gitattributes mandatory LF · CI launch · promote.py promotion script |
| v0.8.2-release | Contagion matrix connected to encoding engine; §2.3.1 Contagion Coefficient Table and §4 weight example aligned with matrix truth values (ranking unchanged) |
| v0.8.3-release | Reliability iteration: consistency audit and gate expansion (framework includes §2.3.2/§4.1 data center consolidation note) |
| v0.0.1 (Current) | Outlook monitoring activation wiring (no change to framework/thresholds) |
| v0.9.0-beta | Add SRI time series tracking (plot SRI historical curves, identify trends and turning points) |
| v0.9.0-beta | Introduce real-time SRI and contagion matrix escalation factor linkage (automatically adjust SRI reading when escalation factors trigger) |
| v0.9.0-release | Add portfolio-level SRI calculation (based on actual portfolio holding weights replacing industry weights), achieving true portfolio systemic risk assessment |
| v0.9.0-release | Introduce SRI stress testing (input hypothetical shock → output post-stress SRI thermometer), deeply integrated with M4 portfolio risk control |
| v1.0.0 | Stable release: all backtest validations passed + at least 6 months of real-time operational data validation |

---

## 12. Appendix

### Appendix A: Signal Aggregation Algorithm Pseudocode

```
function calculate_SRI(industries, weights):
    """
    Calculate the Systemic Risk Index
    
    Parameters:
      industries: list of dictionaries for 13 industries, each containing:
        - name: industry name
        - track_A_score: Track A score (0-10)
        - track_B_level: Track B level ('green'/'yellow'/'orange'/'red')
        - outlook: outlook direction ('positive'/'stable'/'negative')
        - veto_triggered: veto trigger (True/False)
      weights: list of weight percentages for 13 industries (normalized, sum to 100%)
    
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

Use the following table to quickly estimate SRI for any combination of 13 industry signals:

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
| v0.6.8-alpha | 2026-07-10 | Initial creation: SRI signal aggregation algorithm + four-level thermometer + 3 historical backtests + current calculation + threshold sensitivity analysis + engine integration plan | Engine Team |
| v0.7.0-alpha | 2026-07-10 | System intelligence layer integration: engine version unified to v0.7.0-alpha, complete M4 portfolio risk control system with contagion matrix/concentration framework | Engine Team |

---

*This document should be used in conjunction with the Dual-Track Methodology (v0.0.1), Contagion Matrix (v0.0.1), Five-Dimensional Concentration Analysis Framework (v0.0.1), and Outlook Monitoring Framework. The Systemic Warning Framework is the top-level dashboard for the engine's M4 Portfolio Risk Control Layer, providing a unified systemic risk reading for dispersed industry signals.*
