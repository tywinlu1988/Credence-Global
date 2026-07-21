# Five-Dimensional Concentration Analysis Framework

**Version**: v0.0.5 | **Date**: 2026-07-10 | **Status**: Released

---

## Table of Contents

1. [Design Overview](#1-design-overview)
2. [Dimension 1: Industry Concentration](#2-dimension-1-industry-concentration)
3. [Dimension 2: Regional Concentration](#3-dimension-2-regional-concentration)
4. [Dimension 3: Rating Concentration](#4-dimension-3-rating-concentration)
5. [Dimension 4: Maturity Concentration](#5-dimension-4-maturity-concentration)
6. [Dimension 5: Funding Channel Concentration](#6-dimension-5-funding-channel-concentration)
7. [Concentration to Rating Adjustment Mapping](#7-concentration-to-rating-adjustment-mapping)
8. [Five-Dimensional Weighted Composite Score](#8-five-dimensional-weighted-composite-score)
9. [Concentration Stress Test Procedure](#9-concentration-stress-test-procedure)
10. [Integration with Existing Engine](#10-integration-with-existing-engine)
11. [Limitations Statement](#11-limitations-statement)

---

## 1. Design Overview

### 1.1 Framework Positioning

The Five-Dimensional Concentration Analysis Framework is the core component of the Engine's Portfolio Risk Control Layer (M4). It is used to assess the concentration risk of a credit portfolio across five dimensions: industry, region/country, rating, maturity, and funding channel. This framework works in coordination with the [Contagion Matrix](contagion-matrix.md) — the former defines "how concentrated is dangerous," while the latter defines "how danger spreads."

### 1.2 Logical Relationship Among the Five Dimensions

```
                         ┌──────────────────┐
                         │ Funding Channel   │  ← Source of liquidity risk
                         │ Concentration     │
                         │ (Channel Path     │
                         │  Dependency)      │
                         └──────┬───────────┘
                                │
         ┌──────────────┐       │       ┌──────────────────┐
         │ Industry     │◄──────┼──────►│ Regional          │
         │ Concentration│       │       │ Concentration     │
         │ (Contagion   │       │       │ (Resonance        │
         │  Amplifier)  │       │       │  Amplifier)       │
         └──────┬───────┘       │       └──────┬───────────┘
                │               │               │
                ▼               ▼               ▼
         ┌──────────────────────────────────────────┐
         │           Maturity Concentration         │
         │         (Trigger Time Window)            │
         └──────────────────────────────────────────┘
                                │
                                ▼
         ┌──────────────────────────────────────────┐
         │           Rating Concentration           │
         │      (External AAA% + Pseudo-High        │
         │       Rating %)                          │
         │   ← Deepest, Most Dangerous Signal →     │
         └──────────────────────────────────────────┘
```

**Core Logic Chain:** Funding channel dependency → Industry/Regional exposure → Maturity concentration locks the trigger window → Rating concentration masks true risk → Multi-dimensional resonance → Concentration risk outbreak.

### 1.3 Score Mapping Rules

Each dimension's raw metrics are mapped to a risk score of 1-10:

| Risk Score | Meaning | Corresponding Status |
|-----------|---------|---------------------|
| 1-3 | Fully Diversified | 🟢 Normal |
| 4-5 | Mildly Concentrated | 🟡 Watch |
| 6-7 | Moderately Concentrated | 🟠 Warning |
| 8-10 | Extremely Concentrated | 🔴 Danger |

Mapping Rule: For each dimension, select the worst-performing metric as the dimension's raw risk score, then determine the specific score through linear interpolation within threshold intervals. For example, if HHI = 1800 in industry concentration (falling in the mid-range of the 🟠 interval 1000-2500), it maps to a score of 6.

---

## 2. Dimension 1: Industry Concentration

### 2.1 Metric Definitions

| Metric | Abbreviation | Formula | Data Source |
|--------|-------------|---------|-------------|
| HHI Index | HHI | Sum of squared position weights per industry × 10000 | Portfolio holdings data · Industry classification mapping |
| Top 3 Industry Share | CR3 | Sum of the top 3 industries by position weight | Portfolio holdings data |
| Top 5 Industry Share | CR5 | Sum of the top 5 industries by position weight | Portfolio holdings data |
| Single Industry Cap | MAX1 | Maximum single industry position weight | Portfolio holdings data |

### 2.2 Threshold System

#### 2.2.1 HHI Index Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | HHI < 1000 | 1-3 | 🟢 |
| Watch | 1000 ≤ HHI < 1500 | 4-5 | 🟡 |
| Warning | 1500 ≤ HHI < 2500 | 6-7 | 🟠 |
| Danger | HHI ≥ 2500 | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | After the 2018 policy adjustment, the solar/PV industry concentration HHI jumped from 1200 to 2200, with credit spreads widening 200bp+ across the sector. After the 2020 Yongcheng Coal default, coal industry portfolios with HHI > 2000 experienced loss rates 3.2x higher than diversified portfolios |
| Theoretical Basis | U.S. Department of Justice HHI antitrust standards (HHI < 1500 = moderate concentration, > 2500 = high concentration), calibrated for the bond market: the tail loss distribution of credit concentration is steeper than in commodity markets, so the safety threshold is lowered from 1500 to 1000 |
| Exceptions | When HHI comes primarily from LGFV bonds and LGFV bonds constitute < 30% of total exposure, HHI thresholds may be increased by 20% (LGFV's regional binding weakens industry concentration risk); when the portfolio covers only 2-3 industries (e.g., sector funds), HHI is not applicable — use CR3 and MAX1 instead |

#### 2.2.2 Top 3 Industry Share (CR3) Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | CR3 < 50% | 1-3 | 🟢 |
| Watch | 50% ≤ CR3 < 65% | 4-5 | 🟡 |
| Warning | 65% ≤ CR3 < 80% | 6-7 | 🟠 |
| Danger | CR3 ≥ 80% | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | In 2020, three AAA defaults (Yongcheng Coal, Tsinghua Unigroup, Brilliance Auto) occurred across different industries but within a highly concentrated time window (October 2020 — March 2021), validating that when CR3 > 65%, a default in a single industry can propagate to the other 2 industries via high-contagion pathways in the contagion matrix |
| Theoretical Basis | Markowitz (1952) portfolio theory, adapted for credit markets: inter-industry correlations jump from 0.3 to 0.7+ under stress, so CR3 should use 50% as the safety line rather than the 67% suggested by classical portfolio theory |
| Exceptions | If the 3 industries in CR3 belong to isolated clusters in the contagion matrix (e.g., Food & Beverage + Textile & Apparel + Retail), CR3 thresholds may be relaxed to 65%; if they involve super-spreader clusters (Semiconductors + LGFV + Advanced Equipment), thresholds should be tightened to 45% |

#### 2.2.3 Top 5 Industry Share (CR5) Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | CR5 < 70% | 1-3 | 🟢 |
| Watch | 70% ≤ CR5 < 80% | 4-5 | 🟡 |
| Warning | 80% ≤ CR5 < 90% | 6-7 | 🟠 |
| Danger | CR5 ≥ 90% | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | During the 2022 wealth management product redemption crisis, fixed-income-plus portfolios with CR5 > 85% experienced NAV drawdowns 2.7x greater than those with CR5 < 70%. The synchronous downside correlation among the top 5 industries under stress reached 0.75 |
| Theoretical Basis | Based on industry cluster analysis of the contagion matrix (clusters A-J), 5 industries is the critical threshold spanning 2-3 clusters — CR5 > 80% means the portfolio covers at least 2 high-contagion clusters, significantly increasing systemic risk |
| Exceptions | If the industries in CR5 are all low-financial-intensity consumer sectors (brand/channel-driven, per paradigm-brand-channel.md), thresholds may be relaxed to 85% |

#### 2.2.4 Single Industry Cap (MAX1) Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | MAX1 < 25% | 1-3 | 🟢 |
| Watch | 25% ≤ MAX1 < 40% | 4-5 | 🟡 |
| Warning | 40% ≤ MAX1 < 60% | 6-7 | 🟠 |
| Danger | MAX1 ≥ 60% | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | In 2021, a joint-stock bank wealth management subsidiary had a single industry (Real Estate) exposure of 58%. After the Evergrande default, the industry's credit spreads widened 500bp, directly causing the subsidiary's NAV to fall 3.2% and triggering a redemption crisis. In 2023, a securities firm's asset management arm had 72% single-industry exposure to LGFV bonds, suffering heavy losses during a regional LGFV debt extension event |
| Theoretical Basis | The 25% single industry cap references UCITS diversification rules (single sector ≤ 20%) adjusted upward to 25% to accommodate credit market industry concentration characteristics |
| Exceptions | When a single industry's contagion matrix row sum is ≤ 30 (low-contagion industries such as Healthcare Equipment 27, Biotech & Pharma 28, Consumer Staples 28, Telecommunications 29), MAX1 thresholds may be increased to 35%; if the single industry is a super-spreader (row sum ≥ 42: Financials 47, Capital Goods 43, Chemicals/TechHW 42), MAX1 should be tightened to 20% |

### 2.3 Cross-Reference with Contagion Matrix

**The danger level of single industry concentration depends on the industry's position in the contagion matrix** (row sums per contagion-matrix.md §9.2; clusters per §5.4):

| Industry | Contagion Rank | Row/Col Sum | Cluster | MAX1 Threshold Adjustment |
|---------|---------------|---------------------------|---------|--------------------------|
| Financials (Banks/Insurance) | Super-spreader #1 | 47 | C (Sovereign-Financial Hub) | ≤ 20% |
| Capital Goods | Super-spreader #2 | 43 | B (Tech-Auto-Capital Goods), F (Infrastructure-Construction) | ≤ 20% |
| Chemicals | Super-spreader #3 (tie) | 42 | A (Energy-Chemicals-Transport-Utilities) | ≤ 22% |
| Technology Hardware (Semis) | Super-spreader #3 (tie) | 42 | B (Tech-Auto-Capital Goods) | ≤ 22% |
| Energy (Oil & Gas) | Quasi super-spreader | 41 | A (Energy-Chemicals-Transport-Utilities) | ≤ 22% |
| Transportation | Quasi super-spreader | 39 | A, E, H | ≤ 25% |
| Sovereigns & GSEs | Quasi super-spreader | 37 | C (Sovereign-Financial Hub) | ≤ 25% |
| Metals & Mining | Moderate Contagion | 35 | F (Infrastructure-Construction) | ≤ 28% |
| Software & Services | Moderate Contagion | 34 | B, G, H | ≤ 28% |
| Automobiles | Moderate Contagion | 33 | B (Tech-Auto-Capital Goods) | ≤ 28% |
| Construction Materials | Moderate Contagion | 32 | F (Infrastructure-Construction) | ≤ 28% |
| Utilities (Regulated) | Moderate Contagion | 32 | A, F | ≤ 28% |
| Commercial Services | Moderate Contagion | 31 | H (Commercial Services-Network) | ≤ 30% |
| Consumer Durables | Moderate Contagion | 31 | E (Retail-Consumer-Logistics) | ≤ 30% |
| Retail | Moderate Contagion | 31 | E, H | ≤ 30% |
| Telecommunications | Weak Contagion | 29 | G (Telecom-Software) | ≤ 30% |
| Consumer Staples | Weak Contagion | 28 | E (Retail-Consumer-Logistics) | ≤ 32% |
| Biotech & Pharma | Weak Contagion | 28 | D (Bio-Healthcare) | ≤ 32% |
| Healthcare Equipment | Weakest Contagion | 27 | D (Bio-Healthcare) | ≤ 35% |

**Industry Concentration Comprehensive Assessment Procedure:**

```
Step 1: Calculate the raw risk scores for the four metrics (HHI/CR3/CR5/MAX1)
Step 2: Take the highest score among the four metrics as the raw industry concentration score
Step 3: Identify the top 3 industries by position weight in the portfolio
Step 4: Query the contagion matrix to determine if these industries belong to the same high-contagion cluster (contagion-matrix.md §5.4 clusters A-H)
  ├── If they belong to the same cluster → raw score + 2 (cluster concentration penalty)
  ├── If they belong to the same paradigm (see industry-framework.md § Four Industry Types) but different clusters → raw score + 1 (intra-paradigm resonance penalty)
  └── If they belong to isolated clusters → no adjustment
Step 5: Determine if the largest industry is a super-spreader → if yes, MAX1 threshold adjustments per table above
Step 6: Output the final industry concentration risk score (1-10)
```

### 2.4 Industry Classification Mapping

Industry classification mapping uses the 13-industry taxonomy and paradigm assignments from the [Contagion Matrix](contagion-matrix.md) §1. For cross-industry enterprises (e.g., companies involved in Semiconductors + Advanced Equipment + Data Centers + New Energy Vehicles), multi-label assignment is used, with positions split across industries according to revenue share or risk exposure share when calculating HHI, CR3, and CR5.

---

## 3. Dimension 2: Regional Concentration

### 3.1 Metric Definitions

| Metric | Formula | Data Source |
|--------|---------|-------------|
| Single Country/Region Share | Total positions of issuers in that country/region / Total positions | Portfolio holdings data · Issuer domicile |
| Peripheral/Weaker Region Total Share | Total positions of issuers in peripheral/weaker regions / Total positions | Portfolio holdings data · Regional classification |
| Regional Fiscal Health Weighted Share | Regional share × (1 - Regional Fiscal Health Score/100) | Regional general public budget revenue / debt ratio data |
| Single City Tier Share | Share of each tier based on city classification | City classification system |

### 3.2 Regional Classification System

| Region Tier | Cities/Markets | Fiscal Health Characteristics |
|------------|---------------|------------------------------|
| **Major Financial Hubs** | New York · London · Tokyo · Singapore | General public budget revenue > $50B · Debt ratio < 80% · Fiscal self-sufficiency > 80% |
| **Major Economic Centers** | Los Angeles · Chicago · Frankfurt · Paris · Shanghai · Hong Kong · Seoul · Sydney · Toronto · San Francisco | General public budget revenue $15-50B · Debt ratio 80-120% · Fiscal self-sufficiency 50-80% |
| **Mid-Tier Cities** | Other global and regional hubs (e.g., Berlin, Milan, Madrid, Boston, Seattle, Melbourne, Dubai, Mumbai, Sao Paulo, etc.) | General public budget revenue $5-15B · Debt ratio 120-200% · Fiscal self-sufficiency 30-50% |
| **Peripheral/Weaker Regions** | Economically challenged or structurally weak regions (e.g., parts of Southern Europe, certain Emerging Market regions, structurally distressed areas) | General public budget revenue < $5B · Debt ratio > 200% · Fiscal self-sufficiency < 30% |

> **Note:** Regional fiscal health scores are updated annually, based on a composite calculation of the latest general public budget revenue, debt ratio, fiscal self-sufficiency, and land concession revenue trends across regions.

### 3.3 Threshold System

#### 3.3.1 Single Country/Region Share Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | Single country/region < 20% | 1-3 | 🟢 |
| Watch | 20% ≤ Single country/region < 35% | 4-5 | 🟡 |
| Warning | 35% ≤ Single country/region < 50% | 6-7 | 🟠 |
| Danger | Single country/region ≥ 50% | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | **Yongcheng Coal case (2020):** Within a regional-level SOE portfolio in a single country/region, Yongcheng Coal + Henan Energy + Zhengzhou Coal accounted for over 45% of the region's credit bond outstanding. After the Yongcheng default, the country/region's overall credit spread jumped from 120bp to 400bp+, and financing costs for unrelated enterprises in the same region rose over 200bp. **Regional SOE default waves:** Over a multi-year period, a series of defaults in a single region triggered a "regional credit isolation" effect, with new issuance rates in affected regions systematically 200-300bp higher than in core markets. **Sub-sovereign debt stress:** In a concentrated sub-sovereign debt region where outstanding bonds accounted for > 10% of the national total, a major debt extension event caused regional credit spreads to widen 600bp+, with cross-regional contagion to other weaker regions |
| Theoretical Basis | Regional credit risk "contagion radius" research (Caesar, 2021) shows that regional resonance effects from defaults within the same country/region begin to manifest when share > 20%, entering a nonlinear acceleration zone when > 35%. Each 10-percentage-point decline in regional fiscal health approximately doubles the default probability of enterprises in that region |
| Exceptions | When the single country/region is a major financial hub and all issuers are AAA-rated sovereigns or supranationals, thresholds may be increased to 30%; when single country/region exposure is entirely concentrated in national-level government agencies (not sub-sovereign) and general public budget revenue > $80B, thresholds may be increased to 35% |

#### 3.3.2 Peripheral/Weaker Region Total Share Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | Peripheral regions < 10% | 1-3 | 🟢 |
| Watch | 10% ≤ Peripheral regions < 20% | 4-5 | 🟡 |
| Warning | 20% ≤ Peripheral regions < 35% | 6-7 | 🟠 |
| Danger | Peripheral regions ≥ 35% | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | Sub-sovereign debt from weaker regions as a share of national total rose from 8.7% to 12.3% over a multi-year period, while related default/extension events accounted for 31% of national sub-sovereign risk events. Portfolios with > 30% exposure to peripheral regions experienced average recovery rates of only 38% after defaults, compared to the national average of 52% — a 14-percentage-point gap |
| Theoretical Basis | The "credit isolation" effect in weaker regions (Rajan & Zingales, 1998, adapted): the financing recovery cycle for peripheral/challenged regions after a credit event is 2-3x longer than for stronger regions. When peripheral exposure > 20%, portfolio liquidity risk enters a nonlinear acceleration zone |
| Exceptions | If peripheral exposure consists entirely of national-level government debt with central government transfer payment share > 50%, peripheral thresholds may be adjusted upward by 5 percentage points; if peripheral exposure includes strategic national project bonds (such as special-purpose infrastructure bonds), that portion may be excluded from peripheral calculations |

#### 3.3.3 Regional Fiscal Health Weighted Adjustment

The regional fiscal health weighted share serves as a supplementary indicator that modifies the single country/region share and peripheral region share:

| Weighted vs Raw Deviation | Adjustment Rule | Applicable Condition |
|-------------------------|----------------|---------------------|
| Weighted < Raw | No adjustment | Region's fiscal health above average |
| Weighted > Raw but deviation < 10pp | Raw risk score + 1 | Region's fiscal health below average |
| Weighted > Raw and deviation 10-20pp | Raw risk score + 2 | Significant regional fiscal pressure (e.g., land concession revenue decline > 30%) |
| Weighted > Raw and deviation > 20pp | Raw risk score + 3 | Regional fiscal distress (e.g., general public budget revenue declining 2 consecutive years) |

### 3.4 Regional Resonance Analysis with Contagion Matrix

According to the [Contagion Matrix](contagion-matrix.md) §4.1 Principle 3 (intra-regional dependency transmission is high), regional concentration risk is amplified through the following pathways:

> **Cross-document consumption note:** When the Concentration Framework references the Contagion Matrix, it only consumes each cell's **`intensity`** and **`direction`** fields, used to identify contagion strength and determine uni/bidirectional relationships. The `type`, `confidence`, and `historical_cases` fields do not enter the quantitative calculation in the current v0.0.5.

| Regional Resonance Pathway | Contagion Intensity | Logic Description |
|--------------------------|-------------------|-------------------|
| LGFV ↔ Transportation | 4 (Bidirectional Strong) | LGFV default → regional transportation SOE financing freeze; transportation default → LGFV credit revaluation |
| LGFV ↔ Solar/PV | 3 (Bidirectional Moderate) | LGFV default → regional solar farm financing difficulty; solar default → LGFV park revenue decline |
| LGFV ↔ Data Centers | 3 (Bidirectional Moderate) | Data center parks depend on LGFV — LGFV default → IDC project disruption |
| LGFV ↔ NEV/Semiconductors/Advanced Equipment | 2 (Unidirectional Weak) | Industrial parks depend on LGFV infrastructure support |
| Major Financial Hub Regional Resonance | 1 (Very Weak) | Diversified economic structure weakens regional resonance effects |
| Peripheral Region Resonance | 3-5 depending on event type | Peripheral regions exhibit significant "all-in-the-same-boat" effects |

**Regional Concentration Comprehensive Assessment Procedure:**

```
Step 1: Calculate the single country/region share risk score
Step 2: Calculate the peripheral/weaker region total share risk score
Step 3: Take the higher of the two as the base score
Step 4: Apply the regional fiscal health weighted adjustment (§3.3.3)
Step 5: Identify if there is a high-risk contagion combination within the region (e.g., LGFV + Transportation simultaneous exposure)
  ├── If simultaneously exposed to LGFV + Transportation → base score + 2 (matrix-validated strong resonance)
  ├── If simultaneously exposed to LGFV + Solar/PV + Data Centers → base score + 1
  └── If all exposure is in major financial hubs → base score - 1 (high regional diversification)
Step 6: Output the final regional concentration risk score (1-10)
```

---

## 4. Dimension 3: Rating Concentration

### 4.1 Metric Definitions

| Metric | Formula | Data Source |
|--------|---------|-------------|
| External AAA Share | Holdings of issuers with external AAA rating / Total holdings | External ratings (major Chinese rating agencies) |
| Internal Rating Distribution | Share of each internal rating tier | Internal credit assessment results |
| "Pseudo-High Rating" Share | Holdings of issuers with external AAA but internal < BBB / Total holdings | Cross-comparison of external vs internal ratings |
| Rating Dispersion | Standard deviation of external vs internal rating deviation | External rating vs internal rating |

### 4.2 Core Philosophy

**This is the engine's most distinctive differentiator:** The deviation between external and internal ratings is itself a signal of concentration risk.

Traditional portfolio risk control only focuses on external rating concentration (AAA share too high or too low), but overlooks a more dangerous scenario — when external ratings "compress" all issuers into high rating bands while internal ratings reveal broad risk dispersion, the portfolio faces rating bubble concentration risk. This is analogous to the AAA rating bubble on CDOs in 2008 — superficially diversified, but in reality highly concentrated on a single dimension of "false safety."

| Concept | Definition | Risk Implication |
|---------|-----------|-----------------|
| Externally Diversified | AAA/A/BBB each ~30% | Superficially diversified, but external ratings lag by ~17 months (Yongcheng/Tsinghua/Brilliance were all AAA-rated before default) |
| Externally Concentrated | AAA share > 50% | Rating bubble — when an AAA default occurs, a large number of "pseudo-AAA" issuers will be simultaneously exposed |
| Pseudo-High Rating Concentration | External AAA but internal < BBB share > 15% | Most dangerous concentration — internal ratings have already identified risk, but the portfolio is nominally still "high-grade" |
| Internal-External Rating Deviation Concentration | Deviation is consistent and in the same direction | Systematic bias — could be a rating agency methodology issue or engine calibration deviation |

### 4.3 Threshold System

#### 4.3.1 External AAA Share Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | AAA share < 30% | 1-3 | 🟢 |
| Watch | 30% ≤ AAA share < 50% | 4-5 | 🟡 |
| Warning | 50% ≤ AAA share < 70% | 6-7 | 🟠 |
| Danger | AAA share ≥ 70% | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | Yongcheng Coal maintained AAA/stable external rating until 17 months before default, and was only downgraded to BB after the event. Tsinghua Unigroup similarly maintained AAA/stable before default, then was downgraded to D. Brilliance Auto had an AAA rating before its October 2020 default, then entered bankruptcy restructuring. Massive rating inflation was observed — AAA and AA+ rated bonds constituted over 70% of the credit bond market, compared to high-yield (non-investment grade) bonds representing ~30% in the U.S. market. After the November 2020 AAA default, the "AAA SOE guarantee" belief collapsed, and AAA credit spreads jumped from 80bp to 200bp+ |
| Theoretical Basis | Rating agency information value theory (Bolton, Freixas & Shapiro, 2012): when over 60% of bonds in a market carry the highest rating (AAA), the signaling function of ratings is completely lost. The AAA bond share was 3x higher than in the U.S. market (where AAA corporate bonds represent < 5%), meaning AAA ratings offered almost no differentiation. The approximately 17-month rating lag window (Becker & Milbourn, 2011's rating inflation theory validated in practice) means any portfolio with AAA share > 50% faces severe "rating lag concentration risk" |
| Exceptions | When the portfolio consists entirely of sovereign bonds (government bonds, agency bonds) or quasi-sovereign bonds (railway bonds, central bank notes), AAA share thresholds do not apply — these instruments have near-zero default risk and AAA ratings are meaningful. When the portfolio follows a pure high-yield strategy, AAA share is naturally < 10%, and no upper threshold is needed |

#### 4.3.2 "Pseudo-High Rating" Share Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | Pseudo-high rating < 5% | 1-3 | 🟢 |
| Watch | 5% ≤ Pseudo-high rating < 15% | 4-5 | 🟡 |
| Warning | 15% ≤ Pseudo-high rating < 30% | 6-7 | 🟠 |
| Danger | Pseudo-high rating ≥ 30% | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | All 4 historical backtest validation cases were related to "pseudo-high ratings" — Yongcheng Coal (external AAA / internal C), Tsinghua Unigroup (external AAA / internal CCC), Brilliance Auto (external AAA / internal B), GCL System Integration (external AA+ / internal B). At the T-17 month validation point, the "pseudo-high rating" signal had already triggered for all 4 issuers (external AAA and internal < BBB), but no portfolio risk control framework could identify this signal. A 2023 portfolio diagnostic of a large insurance asset manager showed 23% of its AAA-rated portfolio had internal ratings ≤ BBB — meaning the portfolio's "pseudo-high rating" share was 23%, falling into the warning range (🟠) |
| Theoretical Basis | The "rating deviation concentration" concept is the engine's original contribution. Traditional credit risk theory only focuses on "rating migration risk" — the probability and magnitude of external rating downgrades. But it overlooks a more dangerous structural problem: **when a large number of issuers in a portfolio have systematically inflated external ratings, the portfolio's true credit quality forms a false concentration in the "high rating" dimension.** Once external ratings begin to be downgraded en masse, the portfolio's nominal ratings will collapse like dominoes |
| Exceptions | If the internal rating system has a systematic conservative bias toward specific industries (e.g., LGFV bonds, where internal ratings are typically 1-2 notches lower than external), the pseudo-high rating threshold can be adjusted using the applicable calibration factor. When an issuer has explicit external support (e.g., a subsidiary of a sovereign entity) and the engine's external support framework assesses it as "strong support," that issuer may be excluded from pseudo-high rating calculations |

### 4.4 Rating Concentration Comprehensive Assessment Procedure

```
Step 1: Calculate the external AAA share risk score
Step 2: Calculate the pseudo-high rating share risk score
Step 3: Take the higher of the two as the base score
Step 4: Check the direction of internal-external rating deviation
  ├── If most issuers have external rating > internal rating (systematically inflated)
  │   └── Base score + 1 (systematic rating bubble penalty)
  ├── If most issuers have external rating ≤ internal rating (conservative ratings)
  │   └── No adjustment (safe direction)
  └── If rating deviation is mixed (some inflated, some conservative)
      └── No adjustment
Step 5: Check rating dispersion — if > 80% of issuers are concentrated in 2 consecutive external rating notches
  ├── Even if AAA share is not high, this constitutes rating concentration → base score + 1
  └── Because rating density itself reduces downgrade buffer space
Step 6: Output the final rating concentration risk score (1-10)
```

### 4.5 External Rating Lag Validation Data

The following data validates the logic that "external rating concentration itself is a risk signal":

| Issuer | External Rating (T months before default) | Engine Internal Rating (T-17 months) | Pseudo-High Rating Signal | Actual Default Time |
|--------|------------------------------------------|--------------------------------------|--------------------------|---------------------|
| Yongcheng Coal | AAA/stable (T=0) | C (T=-17 months) | ✅ Triggered | Nov 2020 |
| Tsinghua Unigroup | AAA/stable (T=0) | CCC (T=-17 months) | ✅ Triggered | Nov 2020 |
| Brilliance Auto | AAA/stable (T=0) | B (T=-22 months) | ✅ Triggered | Oct 2020 |
| GCL System Integration | AA+/stable (T=0) | B (T=-12 months) | ✅ Triggered | Aug 2021 (technical default) |
| Suning.com | AAA/stable (T=0) | B (T=-12 months) | ✅ Triggered | Jun 2021 (cross-default) |

**Key Finding:** The engine's pseudo-high rating signal was triggered 12-22 months in advance for all 5 validation cases. Had portfolio risk control frameworks included a pseudo-high rating share metric, these "AAA-rated" credit events could have been identified early.

---

## 5. Dimension 4: Maturity Concentration

### 5.1 Metric Definitions

| Metric | Formula | Data Source |
|--------|---------|-------------|
| Next 12 Months Maturity Share | Bond amount maturing within 12 months / Total portfolio face value | Bond maturity date · Principal repayment schedule |
| Next 24 Months Maturity Share | Bond amount maturing within 24 months / Total portfolio face value | Same as above · Cumulative |
| Next 36 Months Maturity Share | Bond amount maturing within 36 months / Total portfolio face value | Same as above · Cumulative |
| Single Month Maturity Peak | Maximum monthly maturity amount / Total portfolio face value | Monthly maturity distribution |
| Maturity Concentration Coefficient | (Maximum single month maturity / Average monthly maturity) - 1 | Derived from the above |

### 5.2 Debt Maturity Scheduling Method

The maturity scheduling method for this dimension references the definitions in the [Financial Deep Dive Module](financial-deep-dive.md) §C (Debt Maturity Scheduling):

> **Core Philosophy:** It is not about "short-term debt ratio" (static snapshot), but about the distribution of debt maturing over the next 12/24/36 months (dynamic maturity schedule).

The data source path inherits from financial-deep-dive.md §C.1, aggregating maturity distributions from four balance sheet items: short-term borrowings, current portion of non-current liabilities, bonds payable, and long-term borrowings. This framework extends to the portfolio level, aggregating individual issuer maturity schedules into portfolio-level maturity concentration metrics.

### 5.3 Threshold System

#### 5.3.1 Next 12 Months Maturity Share Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | 12-month maturity < 30% | 1-3 | 🟢 |
| Watch | 30% ≤ 12-month maturity < 50% | 4-5 | 🟡 |
| Warning | 50% ≤ 12-month maturity < 70% | 6-7 | 🟠 |
| Danger | 12-month maturity ≥ 70% | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | **Yongcheng Coal (2020):** Debt maturing in Q1 2020 accounted for 63% of the full year; 12-month maturity share was approximately 70%, with peak monthly maturity concentrated in November (the default month). When the market window closed after the default, the issuer could not refinance maturing debt. **Tsinghua Unigroup (2020):** Approximately 20 billion in debt maturing in H2 2020 represented 65% of outstanding bonds, with dense maturities from July to October, ultimately triggering default in November. **Brilliance Auto (2020):** A private placement bond maturing on October 22, 2020 was the direct trigger for default, representing 52% of the year's total maturing debt |
| Theoretical Basis | Maturity concentration "refinancing risk" theory (Diamond, 1991): when a company/portfolio needs substantial refinancing in a short period, it faces the systemic risk of "market window closure." Refinancing risk is determined by three factors — amount (volume), maturity concentration (distribution), and market financing conditions (external environment). Refinancing risk becomes apparent when 12-month maturity > 30%, enters danger zone when > 50%, and even a mild market shock can trigger a liquidity crisis when > 70% |
| Exceptions | If the portfolio has substantial bank credit line coverage (coverage ratio > 2.0x), the 12-month threshold may be increased by 10 percentage points. If most holdings are short-term notes/commercial paper (effectively interbank market rolling financing instruments) and interbank market member share > 80%, the threshold may be increased to 35%. If the macro financing environment is accommodative (e.g., accommodative credit cycle, rate-cutting cycle), the threshold may be raised by 5 percentage points |

#### 5.3.2 Next 24 Months Maturity Share Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | 24-month maturity < 50% | 1-3 | 🟢 |
| Watch | 50% ≤ 24-month maturity < 70% | 4-5 | 🟡 |
| Warning | 70% ≤ 24-month maturity < 85% | 6-7 | 🟠 |
| Danger | 24-month maturity ≥ 85% | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | A certain issuer's private placement bonds maturing in 2022-2023 (24-month maturity share of 82%) could not be refinanced after credit tightening began in H2 2021, ultimately defaulting in 2022. Retrospective analysis shows the 24-month maturity concentration signal had already triggered the warning range 18 months before default |
| Theoretical Basis | The 24-month dimension covers a typical full credit cycle length (credit cycles typically run 18-24 months). 24-month maturity > 70% means the portfolio is almost fully exposed to the next credit tightening cycle with almost no "hold-through-the-winter" buffer |
| Exceptions | Same as above: when credit line coverage is adequate, increase threshold by 10pp; if the portfolio strategy is "buy and hold to maturity" and does not rely on refinancing, the 24-month threshold may not apply |

#### 5.3.3 Next 36 Months Maturity Share Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | 36-month maturity < 70% | 1-3 | 🟢 |
| Watch | 70% ≤ 36-month maturity < 85% | 4-5 | 🟡 |
| Warning | 85% ≤ 36-month maturity < 95% | 6-7 | 🟠 |
| Danger | 36-month maturity ≥ 95% | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | Before default, one issuer had 100% of outstanding bonds maturing within 36 months, of which 85% matured within 24 months — an extremely tight time window. In contrast, a comparable issuer maintaining 20% of debt with > 3-year maturity successfully navigated the tightest refinancing window during the default wave |
| Theoretical Basis | 36 months is the typical span of a full bull-bear credit cycle. Maintaining > 30% of bonds with > 3-year maturity effectively constitutes a "liquidity safety cushion" — holdings that never need refinancing even under the worst market conditions |
| Exceptions | Perpetual bonds and extendable bonds are excluded from 36-month calculations (since their maturity can be extended at the issuer's discretion) |

#### 5.3.4 Single Month Maturity Peak Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | Single month peak < 10% | 1-3 | 🟢 |
| Watch | 10% ≤ Single month peak < 20% | 4-5 | 🟡 |
| Warning | 20% ≤ Single month peak < 30% | 6-7 | 🟠 |
| Danger | Single month peak ≥ 30% | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | Yongcheng Coal's default occurred in November; its maturing bonds that month represented 28% of the annual total. Tsinghua Unigroup's November maturities represented 35% of the annual total — both defaulted at monthly peak maturity when refinancing was impossible. During a systemic redemption crisis, a fund portfolio with a 32% single-month maturity peak was forced to sell liquid assets at distressed prices under the double shock of redemptions and bond issuance cancellations |
| Theoretical Basis | Single-month maturity concentration is the most dangerous form of maturity concentration — it is not a refinancing need distributed over a year, but a one-time maturity pressure. When single-month maturity > 20%, even under normal market conditions there is elevated rollover risk (if many similar issuers mature in the same month, underwriter capacity is saturated). When > 30%, any market shock can prevent full rollover |
| Exceptions | If the single-month peak comes from a single bond issue of one issuer (rather than multiple different bonds maturing in the same month), the threshold may be increased to 25% (as a single bond issue rollover negotiation is simpler) |

### 5.4 Maturity Concentration Comprehensive Assessment Procedure

```
Step 1: Calculate the risk scores for the four metrics
Step 2: Take the highest score among the 4 metrics as the base score
Step 3: Check the maturity distribution pattern
  ├── If the distribution is "cliff-shaped" (single month peak >> other months)
  │   └── Base score + 1 (cliff maturity penalty)
  ├── If the distribution is "uniformly terraced" (smooth monthly distribution)
  │   └── No adjustment
  └── If the maturity concentration coefficient > 2.0 (single month peak > 3x monthly average)
      └── Base score + 1 (extreme concentration penalty)
Step 4: Check the portfolio's weighted average credit line coverage
  ├── If weighted average credit line coverage ≥ 2.0x
  │   └── Base score - 1 (credit line coverage buffer)
  └── If weighted average credit line coverage < 0.5x
      └── Base score + 1 (lack of backup liquidity)
Step 5: Output the final maturity concentration risk score (1-10)
```

---

## 6. Dimension 5: Funding Channel Concentration

### 6.1 Metric Definitions

| Funding Channel | Included Items | Data Source |
|----------------|---------------|-------------|
| **Bank Channel** | Bank loans · Bank credit lines · Syndicated loans · Bill discounting | Annual report notes "bank borrowings" detail · Bank credit line announcements |
| **Bond Channel** | Credit bonds (MTN · CP · Corporate bonds · Enterprise bonds · PPN) · ABS · ABN | Bond prospectus · Issuance announcements · Portfolio data |
| **Non-Standard Channel** | Trust loans · Entrusted loans · Factoring financing · Finance leases (partial) · Equity disguised as debt | Annual report notes "other liabilities" detail · Trust announcements · Court judgments |
| **Leasing Channel** | Finance leases (direct + sale-leaseback) · Implicit operating lease liabilities | Annual report notes "lease liabilities" detail |
| **Equity Channel** | Private placements · Rights offerings · Block trades · Equity pledge financing | Listed company announcements · Shareholder reduction announcements |

### 6.2 Threshold System

#### 6.2.1 Single Channel Share Thresholds

| Level | Threshold Range | Risk Score | Color |
|-------|----------------|-----------|-------|
| Normal | Single channel < 50% · Multi-channel balanced distribution | 1-3 | 🟢 |
| Watch | 50% ≤ Single channel < 70% | 4-5 | 🟡 |
| Warning | 70% ≤ Single channel < 90% · and the channel is contracting | 6-7 | 🟠 |
| Danger | Single channel ≥ 90% · or primarily dependent on non-standard/trust | 8-10 | 🔴 |

**Threshold Rationale:**

| Dimension | Description |
|-----------|-------------|
| Historical Basis | **Bond Market Freeze:** After major credit events, bond market cancellation rates can reach 25%, and net financing can turn negative. When an issuer's bond channel share > 70%, refinancing capability is almost completely frozen. **Non-Standard Reduction Policies:** After new asset management regulations, non-standard financing has been declining steadily. Issuers primarily dependent on non-standard financing saw a 45% year-over-year increase in non-standard defaults. **Bank Credit Tightening Cycle:** After major defaults, banks tightened credit to the affected industry comprehensively; real estate enterprises' bank channel share fell from 55% over a multi-year period, and companies relying solely on bank channels experienced funding channel fractures after credit tightening |
| Theoretical Basis | "Funding Channel Diversity" theory (Gertler & Gilchrist, 1994): an enterprise's ability to switch between different funding channels is an important component of credit resilience. When a single channel share > 70%, the enterprise loses "switching flexibility." More dangerously, when that channel is contracting (bond market freeze, non-standard reduction, bank credit tightening), funding channel concentration risk immediately translates into a liquidity crisis. "Funding Channel Vulnerability" ranking: ① Non-standard/Trust > ② Bond Market > ③ Bank Credit > ④ Equity > ⑤ Lease (relative vulnerability ranking) |
| Exceptions | If the single channel is bank credit and the issuer has a "comprehensive revolving credit line commitment," or the issuer is a core client of a banking group (core credit share > 80%), the single channel threshold may be increased to 80%. If the issuer simultaneously has listed company status + bank credit lines + bond market financing access, all with > 20% each, the risk score may be reduced by 1 level even if single channel > 50% (due to having multiple backup channels with actual switching capability) |

#### 6.2.2 Funding Channel Vulnerability Assessment

| Funding Channel | Vulnerability Score (1 None - 5 Extreme) | Vulnerability Rationale | Recent 3-Year Channel Contraction |
|----------------|----------------------------------------|----------------------|-----------------------------------|
| **Non-Standard/Trust** | 5 (Extremely Vulnerable) | Regulatory crackdowns, irreversible on-balance-sheet trend, ongoing industry rectification, long legal recovery cycles (average 18-24 months) | Annual approx. -30% |
| **Bond Market** | 4 (Highly Vulnerable) | Market windows highly volatile due to credit events; cancellation rates can reach 25%+ under stress; investor structure homogenization (wealth management products + funds) leads to herding behavior | Up to -45% in a single month during redemption crisis |
| **Bank Credit** | 3 (Moderately Vulnerable) | Affected by monetary policy cycles, but has relationship-based financing stability; large banks relatively stable; smaller banks affected by regional risk | Approx. -15% during credit tightening |
| **Equity Financing** | 2 (Low Vulnerability) | Affected by secondary market conditions, but private placements/rights offerings have no "maturity repayment" pressure and no rigid redemption obligation; only affected by valuation and regulatory windows | Approx. -40% in bear markets (but no repayment required) |
| **Lease Financing** | 3 (Moderately Vulnerable) | Affected by equipment investment cycles, but leased assets have collateral value; sale-leaseback model relatively flexible; more affected after regulatory restrictions | Approx. -20% after regulatory tightening |

### 6.3 Channel Contraction Monitoring

The risk of funding channel concentration depends not only on the current structure, but also on the channel trajectory:

| Monitoring Indicator | Channel | Warning Threshold | Risk Implication |
|--------------------|---------|-----------------|------------------|
| Issuance Cancellation Rate | Bond | > 15% for 2 consecutive weeks | Bond market window is closing |
| Credit Growth Rate | Bank | YoY growth < 8% | Bank credit entering tightening cycle |
| Non-Standard Balance Change | Non-Standard | YoY decline > 20% | Non-standard accelerated reduction, channel disappearing |
| Equity Financing Volume | Equity | YoY decline for 2 consecutive quarters | Equity financing channel narrowing |
| Lease Regulatory Policy | Lease | New regulations restrict sale-leaseback/limits | Lease channel constrained |

**Channel Contraction and Concentration Synergy:**

| Scenario | Synergy Risk Score Adjustment |
|----------|------------------------------|
| Bond channel > 70% + Cancellation rate > 15% | Base score + 2 (double lock — channel concentrated + channel closing) |
| Non-standard channel > 50% + Non-standard balance YoY decline > 20% | Base score + 3 (double lock — channel concentrated + channel rapidly disappearing) |
| Bank channel > 70% + Credit growth < 8% | Base score + 1 (mild — bank credit contraction slower than bond/non-standard) |
| All channels available simultaneously with single < 50% | Base score - 1 (highly diversified funding channels bonus) |

### 6.4 Funding Channel Concentration Comprehensive Assessment Procedure

```
Step 1: Calculate the single channel share risk score
Step 2: Identify the channel type with the highest share
Step 3: Query the vulnerability score for that channel (§6.2.2)
  ├── Extremely vulnerable (non-standard) → base score + 3
  ├── Highly vulnerable (bond) → base score + 2
  ├── Moderately vulnerable (bank/lease) → base score + 1
  └── Low vulnerability (equity) → no adjustment
Step 4: Check if the channel is contracting (§6.3)
  ├── Significantly contracting → base score + synergy adjustment (per §6.3 table)
  ├── Channel stable → no adjustment
  └── Channel expanding (e.g., accommodative credit cycle) → base score - 1
Step 5: Check issuer's funding channel switching capability
  ├── Only 1 channel available → base score + 2
  ├── 2-3 channels available → no adjustment
  ├── 4+ channels available → base score - 1
  └── Listed company status + bank credit lines + bond market access → base score - 1
Step 6: Output the final funding channel concentration risk score (1-10)
```

---

## 7. Concentration to Rating Adjustment Mapping

**Version**: v0.0.5 | **Date**: 2026-07-10 | **Status**: Released

The five-dimensional concentration composite score identifies the concentration risk level (🟢🟡🟠🔴) of the portfolio across five dimensions, but does not directly answer a core question: "How does concentration risk affect the credit rating of individual issuers?" This section establishes the mapping rules from dimension threshold breaches to issuer rating adjustments.

### 7.1 Single Dimension Threshold Breach → Single Issuer Rating Adjustment

When each dimension independently exceeds its threshold, the base rating adjustment for each issuer in the portfolio (adjustment unit = notch):

| Dimension | 🟡 Watch | 🟠 Warning | 🔴 Danger |
|-----------|---------|-----------|----------|
| **Industry Concentration** | 0 | -0.5 notch (industry in down-cycle) | -1 notch (industry in down-cycle, and the industry is a super-spreader) |
| **Regional Concentration** | 0 | -0.5 notch (peripheral region) | -1 notch (peripheral region with existing defaults in the region) |
| **Rating Concentration** | 0 | -0.5 notch (pseudo-high rating share > 15%) | -1 notch (pseudo-high rating > 30%, referencing historical cases) |
| **Maturity Concentration** | 0 | -0.5 notch | -1 notch |
| **Funding Channel Concentration** | 0 | -0.5 notch (dependent channel contracting) | -1 notch (channel vulnerable and freezing) |

**Notes:**
- 🟡 Watch level does not trigger rating adjustment, serves as early warning only
- 🟠 Warning level triggers -0.5 notch adjustment, subject to conditions in parentheses
- 🔴 Danger level triggers -1 notch adjustment, subject to conditions in parentheses
- Adjustment applies to all issuers in the portfolio (industry concentration applies only to issuers in that industry)
- Adjustment amount is deducted from the "base rating" (base rating = dual-track analysis rating)

### 7.2 Multi-Dimension Stacking Rules (Non-Linear)

When two dimensions exceed thresholds simultaneously, the adjustment is not a simple sum — a non-linear increasing rule is used:

| Stacking Situation | Adjustment | Rationale |
|-------------------|-----------|-----------|
| 1 dimension 🟠 | -0.5 notch | Baseline |
| 2 dimensions 🟠 | -1 notch | Two dimensions stacking — risk may amplify each other |
| 3 dimensions 🟠 | -1.5 notch | — |
| 4 dimensions 🟠 | -2 notch | — |
| All 5 dimensions 🟠 | Trigger systemic risk alert — individual issuer adjustment rules not applicable | — |
| 1 dimension 🔴 + 1 dimension 🟠 | -1.5 notch | Severity of red dimension amplified by yellow dimension |
| 2 dimensions 🔴 | -2.5 notch | — |
| 3 dimensions 🔴+ | Trigger portfolio extreme concentration cap, cap BB | — |

**Stacking Rule Usage:**
- First identify each dimension's trigger state (🟢/🟡/🟠/🔴)
- Count only 🟠 and 🔴 dimensions
- Look up the table to determine total adjustment
- When 🔴 and 🟠 coexist, use the "1🔴+1🟠" level
- 3 or more 🔴 directly triggers portfolio extreme concentration cap (cap BB)

### 7.3 Extreme Concentration Trigger Conditions

The following situations directly trigger **portfolio extreme concentration cap, cap BB** (portfolio-level veto, not issuer-level):

1. **Single industry > 50%** and the industry is in a down-cycle (Track A rating < 5.0), and the industry is a super-spreader in the contagion matrix (per contagion-matrix.md §5.1: Financials, Capital Goods, Chemicals, Technology Hardware)
2. **Single peripheral region > 35%** and there have been SOE defaults in that region within the past 12 months
3. **Pseudo-high rating (external AAA, internal < BBB) share > 40%**
4. **Next 12 months maturity > 70%** and funding channel dependency > 70% overlap
5. **Single funding channel > 90%** and that channel is freezing

**Trigger Mechanism:**
- Any single condition triggers portfolio extreme concentration cap
- Upon triggering, the cap rating for all issuers in the portfolio is adjusted to BB
- Original notch adjustments for each dimension are stacked on top of this (but not above BB)
- Portfolio extreme concentration cap is valid for 30 days, or automatically lifted when the triggering condition is eliminated

> **Note:** The portfolio extreme concentration cap (BB) is a different concept from the issuer-level veto (CCC). The former targets portfolio-level liquidity/realization risk from concentration; the latter targets the issuer's own operational survival risk.

### 7.4 Examples (Legacy 13-Industry Composition)

> **Legacy worked examples:** The examples below were written for the retired 13-industry
> China-market composition (LGFV, Solar/PV, NEV, etc.) and reference its super-spreader
> rankings. They remain valid as illustrations of the adjustment *mechanics*; the current
> super-spreader set is Financials, Capital Goods, Chemicals, and Technology Hardware
> (contagion-matrix.md §5.1), and the current industry set is the 19 GICS industries
> (contagion-matrix.md §1.2). Re-derivation under the 19-industry composition is a
> scheduled follow-up. Note also: a 50% single-industry concentration maps to the alert
> band per §1.3 interpolation (score ~6, 🟠), not 5 as printed below.

The following examples assume: the portfolio is 50% concentrated in the specified industry, with all other dimensions normal (🟢). Examples illustrate the impact path of industry concentration on rating adjustment.

| # | Industry | Example Description |
|---|----------|-------------------|
| 1 | **Semiconductors/Integrated Circuits** | Assume a portfolio is 50% concentrated in semiconductors, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. If Track A rating < 5.0 (down-cycle), plus semiconductor as super-spreader → triggers -0.5 notch (🟠) or -1 notch (🔴). Also check if MAX1 exceeds 20% threshold. |
| 2 | **LGFV Bonds** | Assume a portfolio is 50% concentrated in LGFV bonds, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. If LGFV is in a peripheral region with declining fiscal health → combined with regional concentration effects. As a super-spreader, LGFV requires monitoring of regional resonance effects. |
| 3 | **Advanced Equipment** | Assume a portfolio is 50% concentrated in advanced equipment, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. If the industry is in a down-cycle → -0.5 notch. Advanced equipment is a super-spreader; contagion matrix escalation factors must be monitored. |
| 4 | **Solar/PV & Energy Storage** | Assume a portfolio is 50% concentrated in solar/PV, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. If overcapacity leads to margin compression (Track A < 5.0) → -0.5 notch. Solar/PV is a quasi-super-spreader, thresholds apply. |
| 5 | **New Energy Vehicles** | Assume a portfolio is 50% concentrated in NEVs, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. Intensified competition and ongoing price wars → if Track A < 5.0 triggers 🟠 adjustment. Supply chain upstream/downstream concentration stacking needs monitoring. |
| 6 | **Data Centers** | Assume a portfolio is 50% concentrated in data centers, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. Data centers benefit from AI compute demand growth; if Track A still ≥ 5.0 → only 🟡 watch, no adjustment triggered. |
| 7 | **Media/Internet** | Assume a portfolio is 50% concentrated in media/internet, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. If regulatory tightening and ad revenue decline → Track A < 5.0 → -0.5 notch. |
| 8 | **Transportation** | Assume a portfolio is 50% concentrated in transportation, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. Transportation is a moderate contagion industry; if overall sector activity declines → -0.5 notch. Regional resonance with LGFV needs monitoring. |
| 9 | **Medical Devices** | Assume a portfolio is 50% concentrated in medical devices, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. Procurement pressure continues; if industry margins decline → -0.5 notch. Moderate contagion, thresholds can be moderately relaxed. |
| 10 | **Retail** | Assume a portfolio is 50% concentrated in retail, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. Retail affected by weak consumption; if typical issuer Track A < 5.0 → -0.5 notch. Moderate contagion. |
| 11 | **Biopharmaceuticals** | Assume a portfolio is 50% concentrated in biopharmaceuticals, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. Biopharma has long innovation cycles and volatile cash flows → if industry financing environment deteriorates → -0.5 notch. Weak contagion, thresholds can be relaxed. |
| 12 | **Textile & Apparel** | Assume a portfolio is 50% concentrated in textile & apparel, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. Textile & apparel industry overall credit quality is stable (low financial intensity) → if Track A still ≥ 5.0 → only 🟡 watch, no adjustment triggered. |
| 13 | **Food & Beverage** | Assume a portfolio is 50% concentrated in food & beverage, other dimensions normal. Rating adjustment: Industry concentration 5/10 = 🟠. Food & beverage is the weakest contagion industry, industry fundamentals are typically stable → only 🟡 watch, no adjustment triggered. Thresholds can be relaxed to MAX1 ≤ 35%. |

**Summary Rule:** 50% single industry concentration triggers 🟠 level, but whether a rating adjustment is ultimately triggered depends on the industry's down-cycle status and contagion level. Low contagion industries (Textile & Apparel / Food & Beverage) may only trigger 🟡 watch with no adjustment even at 50% concentration; high contagion industries (Semiconductors / LGFV / Advanced Equipment) at 50% concentration combined with a down-cycle trigger actual rating adjustment.

**Note:** In the table above, "Track A < 5.0" references the Track A rating from dual-track analysis (1-10 scale), not the industry pyramid L1-L4 weighted score (industry framework score). Track A rating focuses on individual issuer credit quality, with 1-10 differentiation; the industry pyramid score focuses on industry structural characteristics, with 1-5 per dimension and a weighted total typically falling in the 5-8 range. The two scoring systems are different and cannot be directly compared.

---

## 8. Five-Dimensional Weighted Composite Score

### 8.1 Composite Score Formula

```
Composite Concentration Risk = W₁ × D₁ (Industry) + W₂ × D₂ (Region) + W₃ × D₃ (Rating) 
                               + W₄ × D₄ (Maturity) + W₅ × D₅ (Funding Channel)
```

### 8.2 Recommended Weights

| Dimension | Symbol | Weight | Weight Setting Rationale |
|-----------|--------|--------|------------------------|
| Industry Concentration | W₁ | **25%** | Highest weight dimension. Industry concentration risk spreads across industries through high-contagion pathways in the contagion matrix, with the widest impact on portfolios (can cover all holdings). Industry concentration is the "source" dimension of portfolio systemic risk |
| Regional Concentration | W₂ | **20%** | Same order of magnitude as industry concentration. Regional concentration rapidly propagates through regional resonance effects (validated by historical cases), and peripheral region concentration has extremely high tail risk (recovery rates 14pp below national average after defaults). Weight is slightly lower than industry because regional risk can be partially hedged by fiscal health weighting |
| Rating Concentration | W₃ | **20%** | As the engine's unique differentiator, the 20% weight for rating concentration reflects the importance of "pseudo-high rating" risk in historical cases — all 5 validation cases triggered pseudo-high rating signals T-17 months ahead. The weight is not set higher because rating concentration risk is typically identified by internal ratings 12-17 months before default, making it a "pre-warnable" risk type |
| Maturity Concentration | W₄ | **20%** | Maturity concentration determines the portfolio's risk exposure window along the time dimension. The 20% weight reflects the fact that "maturity pressure is the trigger for default, not the root cause of default" — maturity concentration can cause default, but the root cause is typically fundamental deterioration. Therefore, though a trigger factor, it should not be overweighted |
| Funding Channel Concentration | W₅ | **15%** | Lowest weight because funding channel concentration primarily serves as an "amplifier" and "accelerator" — it does not directly cause default, but significantly affects default probability and post-default recovery rates. The 15% weight reflects its auxiliary but necessary role |

### 8.3 Risk Score Mapping Table

| Composite Risk Score | Risk Level | Color | Management Action Recommendation |
|--------------------|-----------|-------|---------------------------------|
| 1.0 - 2.5 | Low Concentration | 🟢 Normal | Routine monitoring · Quarterly review |
| 2.6 - 4.5 | Mild Concentration | 🟡 Watch | Confirm specific triggered metrics per dimension · Develop diversification plan |
| 4.6 - 6.5 | Moderate Concentration | 🟠 Warning | Limit new exposure to high-risk dimensions · Initiate position reduction plan · Report to risk committee |
| 6.6 - 8.5 | High Concentration | 🔴 Danger | Immediately reduce positions · Suspend new investments in that dimension · Senior management approval |
| 8.6 - 10.0 | Extreme Concentration | 🔴 Danger (Special) | Portfolio restructuring · Full stop-loss · Trigger liquidity contingency plan |

### 8.4 Dynamic Weight Adjustment Rules

Under special market conditions, weights should be adjusted to reflect changes in risk structure:

| Market Environment | W₁ Industry | W₂ Region | W₃ Rating | W₄ Maturity | W₅ Funding Channel | Adjustment Logic |
|-------------------|-----------|---------|----------|------------|-------------------|-----------------|
| Baseline | 25% | 20% | 20% | 20% | 15% | Default weights |
| Credit Tightening Cycle | 20% | 15% | 15% | **30%** | **20%** | Maturity and funding channel become primary risks during credit contraction |
| Rating Bubble Burst Period | 20% | 15% | **35%** | 15% | 15% | Rating concentration risk becomes prominent during mass AAA downgrades |
| Regional Credit Event Cluster | 20% | **30%** | 15% | 20% | 15% | Regional resonance effects amplified |
| Contagion Matrix Escalation Factor Triggered | **30%** | **25%** | 10% | 20% | 15% | Industry + region amplify through contagion matrix |
| Loose Monetary + Tight Credit | 20% | 20% | 15% | 20% | **25%** | Funding channel divergence intensifies → channel concentration risk rises |

**Dynamic Weight Trigger Conditions:**
- Credit Tightening Cycle: Central bank raises rates or reserve requirements 2 consecutive times, or total social financing growth declines for 2 consecutive months
- Rating Bubble Burst Period: More than 10 AAA bonds downgraded to AA+ and below within 3 months
- Regional Credit Event Cluster: 2 or more LGFV bond defaults/extensions in the same country/region within 6 months
- Contagion Matrix Escalation Factor Triggered: VIX > 30 or credit spread widening > 50bp (see Contagion Matrix §6)
- Loose Monetary + Tight Credit: Rate cuts/reserve requirement cuts but credit spreads widening (funding channel divergence)

### 8.5 Composite Score Example

| Dimension | Raw Metric Value | Dimension Risk Score | Weight | Weighted Score |
|-----------|----------------|--------------------|--------|---------------|
| D₁ Industry | HHI=1800 · CR3=68% · MAX1=42% | 6 (Warning) | 25% | 1.50 |
| D₂ Region | Single country/region=38% · Peripheral=22% | 6 (Warning) | 20% | 1.20 |
| D₃ Rating | AAA share=55% · Pseudo-high=18% | 6 (Warning) | 20% | 1.20 |
| D₄ Maturity | 12-month=55% · Single month peak=22% | 6 (Warning) | 20% | 1.20 |
| D₅ Funding Channel | Bond channel=75% · Cancellation rate=18% | 8 (Danger) | 15% | 1.20 |
| **Composite Score** | — | — | **100%** | **6.30 (Moderately Concentrated 🟠)** |

**Interpolation detail (§1.3):** HHI 1800 → 6 + 300/1000 → 6; CR3 68% → 6 + 3/15 → 6; MAX1 42% → 6 + 2/20 → 6; region 38% → 6 + 3/15 → 6; weak region 22% → 6 + 2/15 → 6; AAA 55% → 6 + 5/20 → 6; pseudo-high 18% → 6 + 3/15 → 6; 12-month 55% → 6 + 5/20 → 6; peak 22% → 6 + 2/10 → 6; bond channel 75% → 6 + 5/20 → 6, then §6.3 synergy +2 (bond >70% + cancellation >15%) → 8.

**Interpretation:** This portfolio sits at the bottom of the 🟠 Warning band across all five dimensions — four dimensions at 6 (Warning floor) and the funding channel dimension at 8 (Danger) due to high bond channel share plus a closing market window. The composite score of 6.30 calls for §7.2 stacking treatment (1🔴+4🟠 coexisting → apply the 1🔴+1🟠 level per the usage rule) and heightened monitoring of the bond channel trajectory; it does not by itself trigger the §7.3 extreme-concentration cap.

**Note (D₅ dimension):** Raw metric mapped to 6 (🟠 Warning), synergy effect added +2 (Bond channel > 70% + channel freezing → channel concentration + freezing double penalty), final = 8 (🔴 Danger). Synergy adjustment per §6.3 rules.

> **Correction history:** The pre-v0.0.3 version of this example used integer representative values (raw 7 for D₁-D₄, composite 7.15 🔴). Per §1.3 linear interpolation the raw scores compute to 6 and the composite to 6.30 🟠; the table above is the corrected derivation, and the coded engine (src/concentration_scorer.py) implements the same rule.

---

## 9. Concentration Stress Test Procedure

### 9.1 Five-Dimensional Stress Test Steps

```
Step 1: Define stress scenario
  ├── Select stress type:
  │   ├── Contagion matrix-driven scenario (e.g., semiconductor default + market panic)
  │   ├── Regional resonance scenario (e.g., peripheral region debt extension wave)
  │   ├── Rating bubble burst scenario (e.g., mass AAA downgrade to AA)
  │   ├── Maturity cliff scenario (e.g., market window freeze + mass maturities)
  │   └── Funding channel freeze scenario (e.g., sudden channel closure)
  └── Set stress parameters (mild / moderate / severe)

Step 2: Five-dimensional stress propagation
  ├── Threshold jump mapping for each dimension under stress scenario
  ├── Five-dimensional weighted composite score recalculation
  └── Output "post-stress composite risk score"

Step 3: Concentration breach diagnosis
  ├── Which dimensions jumped from 🟢/🟡 to 🟠/🔴
  ├── Which issuers or industries are most affected after breach
  └── Does the portfolio have "triple concentration" (three dimensions deteriorating simultaneously)

Step 4: Management action plan
  ├── High-risk dimension position reduction recommendations
  ├── Diversification path and timeline
  ├── Hedging tool selection (e.g., CDS, interest rate swaps)
  └── Approval process after limit breach
```

### 9.2 Threshold Jumps Under Stress Scenarios

| Stress Scenario | Affected Dimension | Threshold Jump Rule |
|----------------|-------------------|-------------------|
| Market Panic (VIX > 30) | All dimensions | Each dimension's threshold moves up one level (e.g., Normal → Watch) |
| Regional LGFV Extension Wave | D₂ Region | Peripheral region share threshold tightened from 10%/20%/35% to 5%/15%/25% |
| Rating Bubble Burst | D₃ Rating | Pseudo-high rating threshold tightened from 5%/15%/30% to 3%/10%/20% |
| Market Window Freeze | D₄ Maturity · D₅ Funding Channel | 12-month maturity threshold tightened from 30%/50%/70% to 20%/40%/60% · Bond channel > 50% triggers warning |
| Contagion Matrix High-Contagion Pathway Activation | D₁ Industry | Super-spreader industry MAX1 threshold tightened from 20% to 15% · Cluster A total exposure cap set at 25% |

---

## 10. Integration with Existing Engine

### 10.1 Integration into M4 (Portfolio Risk Control) Framework

This framework is the core component of the M4 Portfolio Risk Control Layer (see [Contagion Matrix](contagion-matrix.md) §7.1 M4 Integration). Integration points with the existing engine:

| Framework Position | Integration Method | Specific Operation |
|-------------------|------------------|-------------------|
| **M4 Portfolio Risk Control** | Concentration Stress Test | Use this framework's five-dimensional scoring to replace the existing single industry concentration metric |
| **M4 Limit Management** | Five-dimensional Limit System | Set independent exposure limits for each dimension, linked to the contagion matrix for pathway limits |
| **M4 Trigger-Based Management** | Three-Level Alert Mechanism | Composite score ≥ 4.5 triggers Watch · ≥ 6.5 triggers Warning · ≥ 8.5 triggers Danger |
| **Contagion Matrix Stress Test** | Input Parameter | Five-dimensional composite score as initial condition for contagion matrix stress testing |
| **Output Layered Framework** | L1 Snapshot · L2 Deep Dive | Five-dimensional scores displayed as "concentration radar chart" in L1 snapshot · Full reasoning chain in L2 Deep Dive |

### 10.2 Cross-References with Related Documents

| Related Document | Referenced Content | Usage in This Framework |
|-----------------|-------------------|------------------------|
| [Contagion Matrix](contagion-matrix.md) | 13-industry classification · Contagion pathways · Escalation factors | Dimension 1 (Industry Concentration) §2.3 · Dimension 2 (Regional Concentration) §3.4 · Stress Test §9 |
| [Financial Deep Dive](financial-deep-dive.md) | Debt maturity scheduling method (C.1-C.3) | Dimension 4 (Maturity Concentration) §5.2 |
| [Engine Architecture Overview](engine-overview.md) | Three-layer architecture · M4 Portfolio Risk Control positioning | Preface · §10.1 |
| [Output Layered Framework](output-layered-framework.md) | L1/L2 output specifications | §10.1 Integration method |
| [Systemic Warning Framework](systemic-warning-framework.md) | SRI thermometer as trigger for composite score dynamic weight adjustment; composite score linked to SRI determination | §8.4 Dynamic weight adjustment rules · §10.1 Integration method |

### 10.3 Recommended New Concentration-Related Output Metrics

The following metrics are recommended for addition to the [Output Layered Framework](output-layered-framework.md):

| Output Layer | New Metric | Format | Use Case |
|-------------|-----------|--------|----------|
| L1 Signal Card | Five-dimensional concentration composite score | 🔴 7.15 · Highest dimension: Funding Channel (8) | Overview — 30-second portfolio concentration assessment |
| L1 Signal Card | Concentration Radar Chart | Pentagon radar · Threshold lines marked | Visualization — intuitive comparison across dimensions |
| L2 Deep Dive | Threshold rationale per dimension | Expandable table · Trigger metrics marked | Compliance — retrospective risk decision basis |
| L2 Deep Dive | Stress test results | Scenario → Jump → Composite score | Forward-looking — worst-case concentration |
| L2 Deep Dive | Triple concentration alert | "D₁ Industry + D₂ Region + D₄ Maturity" | Risk — multi-dimensional resonant concentration crisis |

---

## 11. Limitations Statement

1. **Static Threshold Risk:** This framework's threshold system is based on July 2026 market structure and historical validation data. As industry structures evolve (e.g., new industries emerging, regional economic restructuring, rating system reforms) and market conditions change, thresholds require periodic recalibration. It is recommended to review threshold parameters at least quarterly.

2. **Subjectivity of Weights:** The recommended weights (25%/20%/20%/20%/15%) are based on the engine team's judgment and retrospective calibration against 5 historical cases, not derived through statistical optimization. Optimal weights may differ significantly across market environments — users are advised to adjust weights according to their own portfolio characteristics.

3. **Pseudo-High Rating Metric Dependency on Engine:** This metric relies entirely on the accuracy of the engine's internal ratings. If internal ratings themselves have systematic bias (e.g., being too conservative or too aggressive toward specific industries), the pseudo-high rating share metric will produce misleading results. It is recommended to perform internal rating calibration and comparison with external ratings at least quarterly.

4. **Second-Order Interactions Among Dimensions Not Fully Captured:** There are complex second-order interaction effects among the five dimensions — for example, the triangular combination of "high industry concentration + high regional concentration + high maturity concentration" may produce systemic risk far exceeding the simple weighted sum. This framework uses linear weighting and does not fully capture such higher-order interactions. For "triple concentration" portfolios, an additional -2 penalty score is recommended.

5. **Non-Concentration Risk Factors Not Included:** This framework focuses on concentration risk (portfolio level) and does not cover issuer-level individual credit risk (covered by dual-track analysis and industry pyramid), liquidity risk (covered by liquidity risk assessment), or market risk (covered by non-credit risk overlay). Concentration risk is an important dimension of portfolio risk control, but not the entirety.

6. **Funding Channel Data Availability Limitations:** Data for non-standard financing, lease financing, and other channels relies on annual report note disclosures; data availability is poor for some non-listed entities. For entities with incomplete data, the confidence of funding channel concentration assessment will be significantly reduced.

7. **"One-Size-Fits-All" Risk of Regional Classification:** Classifying markets into four tiers (Major financial hubs / Major economic centers / Mid-tier cities / Peripheral regions) sacrifices intra-regional differentiation. For example, within a single country, major economic centers may have vastly different fiscal health characteristics than peripheral regions. Two-tier (national and sub-national) analysis is recommended for regional concentration analysis, but the current framework provides only national-level guidance for portfolios with broad holdings.

---

## Appendix

### Appendix A: Five-Dimensional Composite Score Quick Reference

Use the following table to quickly estimate the composite risk score:

| Composite Score | D₁ Industry | D₂ Region | D₃ Rating | D₄ Maturity | D₅ Funding Channel |
|----------------|-----------|---------|----------|------------|-------------------|
| ≈ 2.0 🟢 | 🟢 HHI<1000 | 🟢 Country<20% · Peripheral<10% | 🟢 AAA<30% · Pseudo<5% | 🟢 12m<30% · Peak<10% | 🟢 Single<50% · Balanced |
| ≈ 3.5 🟡 | 🟡 HHI~1200 | 🟡 Country~28% · Peripheral~15% | 🟡 AAA~40% · Pseudo~10% | 🟡 12m~40% · Peak~15% | 🟡 Single~60% |
| ≈ 5.5 🟠 | 🟠 HHI~2000 | 🟠 Country~42% · Peripheral~28% | 🟠 AAA~60% · Pseudo~22% | 🟠 12m~60% · Peak~25% | 🟠 Single~80% · Contracting |
| ≈ 7.5 🔴 | 🔴 HHI>2500 | 🔴 Country>50% · Peripheral>35% | 🔴 AAA>70% · Pseudo>30% | 🔴 12m>70% · Peak>30% | 🔴 Single>90% · or non-standard dominant |

### Appendix B: Version Change Log

| Version | Date | Change Content | Author |
|---------|------|---------------|--------|
| v0.0.1 | 2026-07-10 | Initial creation: Five-dimensional concentration analysis framework · Threshold system · Weighted scoring · Stress test integration | Engine Team |
| v0.0.1 | 2026-07-10 | System intelligence layer integration: engine version unified to v0.0.1, forming complete M4 portfolio risk control system with contagion matrix and warning framework | Engine Team |

---

*This document should be used in conjunction with the Contagion Matrix (v0.0.5) and Financial Deep Dive (v0.0.5). The Concentration Analysis Framework is the core component of the M4 Portfolio Risk Control Layer and forms a complete risk control loop with the Industry Pyramid (M1-M2) and Dual-Track Analysis (M3).*
