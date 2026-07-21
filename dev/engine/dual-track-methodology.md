# Dual-Track Analysis Methodology

**Version**: v0.0.4 | **Date**: 2026-07-10

---

## 1. Dual-Track Parallel Architecture

The core of the analysis engine consists of **two independent parallel analysis tracks** that converge through a cross-validation matrix to produce a final judgment.

```
Input: Industry + Entity + Analysis Date
           |
      +----+--------+
      |              |
Track A:            Track B:
Fundamentals        Market Pricing
(Qualitative +      (Quantitative
 Scoring)           Signals)
      |              |
 L1 (Heaviest)     Credit Spreads
 L2                 Volatility
 L3                 Fund Flows
 L4 (Lightest)      Rating Migration
      |              |
      +------+-------+
             v
  Cross-Validation Matrix
  Consensus -> Mutual reinforcement
  Divergence -> Most valuable insight
```

### Design Philosophy of the Two Tracks

| Feature | Track A: Fundamentals | Track B: Market Pricing |
|---|---|---|
| Data Sources | Industry data, corporate filings, policy documents, procurement results | Bond yields, stock prices, trading volumes, rating events |
| Update Frequency | Quarterly/Annual (filing cycles) | Daily/Weekly (continuous) |
| Objectivity | Higher (based on public facts) | Affected by market sentiment |
| Lag | Filing lag exists | Real-time reflection |
| Core Value | Identify structural unsustainability | Capture market pricing errors |

---

## 2. Track A: Fundamental Pyramid Scoring

### 2.1 Scoring Logic

Each layer is independently scored (0-10), with weights determined by industry type.

```
Composite Score = Sigma(Layer Score x Layer Weight)
Layer Score = Sigma(Indicator Score x Indicator Weight)
Indicator Score = f(Raw Value, Threshold, Direction)
```

### 2.2 Standard Four-Layer Pyramid

| Industry Type | L1 (Heaviest) | L2 | L3 | L4 (Lightest) |
|---|---|---|---|---|
| **Policy-Driven** | 35% Policy/Macro | 30% Technology | 20% Supply Chain | 15% Financial |
| **Technology-Moat** | 20% Policy | 35% Technology/IP/Regulatory | 25% Operations | 20% Financial |
| **Zero-Sum Game** | 25% Survival Position | 20% Technology | 30% Profit Fortress | 25% Financial |
| **Asset Lease** | 15% Policy | 20% Technology | 35% Client/Lease | 30% Financial |

> **Authoritative Source Reference**: The authoritative definition of the four-layer pyramid weight templates is available in [Industry Classification & Analysis Framework](industry-framework.md) Section 3.2. This table is a copy; in case of discrepancies, industry-framework.md takes precedence.

### 2.3 Special Pyramid Structures

| Industry | Layers | Layer Structure and Weights |
|---|---|---|
| **Semiconductor** | 5 layers | L1 Geopolitics 30-35%, L2 Technology 25-30%, L3 Market 15-20%, L4 Policy/Capital 10-15%, L5 Financial 5-10% |
| **NEV - OEM** | 5 layers | L1 Survival Position 25%, L2 Technology 20%, L3 Operations 20%, L4 Financial 15%, L5 Policy/Export 10% |
| **NEV - Supply Chain** | 5 layers | L1 Profit Fortress 30%, L2 Technology 20%, L3 Client Quality 22%, L4 Financial 17%, L5 Policy/Export 8% |
| **Medical Devices** | 5 layers | L1 Policy 15%, L2 Regulatory Certificates 22%, L3 Channel 25%, L4 Financial 20%, L5 External Support 8% |
| **Biotech/Pharma** | 5 layers | L1 Policy 15%, L2 Pipeline 25%/15%, L3 BD 20%/25%, L4 Financial 20%/15%, L5 External Support 10%/- |

### 2.4 Layer Scoring Examples (Solar Industry)

| Layer | Scoring Dimension | High Score (8-10) Characteristics | Low Score (0-3) Characteristics |
|---|---|---|---|
| L1 Policy | Policy direction alignment | Receives national subsidies and tax incentives | Core products restricted by policy |
| L2 Technology | Efficiency gap vs leader | Efficiency lead >2% above industry average | Capacity dominated by obsolete technology |
| L3 Supply Chain | Customer concentration | Diversified customer base | Single customer >50% |
| L4 Financial | Cash/Short-term debt ratio | >1.5x | Sustained negative FCF + high short-term debt |

### 2.5 Progressive Layer Principle

1. **L1 must pass before proceeding meaningfully to L2.** If there is fatal risk at the policy/macro level, lower-layer analysis is meaningless.
2. **L4 (Financial Layer) is a validation layer, not a judgment layer.**
   - Good financials but poor upper layers = **More dangerous** (may indicate financial fraud or cyclical peak)
   - Poor financials but strong upper layers = flagged risk but does not overturn rating
3. **One-Vote Veto**: If any layer triggers a one-vote veto condition, the composite rating ceiling is locked at CCC.

---

## 3. Track B: Market Pricing Signals

### 3.1 Four-Level Market Signal System

| Level | Credit Spread | Volatility | Fund Flows | Rating Events |
|---|---|---|---|---|
| **Calm** | Stable/narrowing | <3% daily volatility | Stable/inflow | Rating stable |
| **Watch** | Widening 20-50bp | 3-5% | Moderate outflow | Negative outlook |
| **Abnormal** | >50bp jump or sustained widening | >5% sustained | Accelerating outflow | Watch list |
| **Crisis** | Curve inversion/frozen | >8% or liquidity dry-up | Net liquidation outflow | Downgrade |

### 3.2 Track B Scoring Mapping

| Market State | Track B Score | Meaning |
|---|---|---|
| All four levels at Calm | 8-10 | Market has no concern about credit quality |
| 1-2 dimensions enter Watch | 5-7 | Market shows caution signals |
| 1-2 dimensions enter Abnormal | 3-4 | Market pricing reflects material risk |
| Any dimension enters Crisis | 0-2 | Market pricing reflects default expectations |

---

## 4. Cross-Validation Matrix

### 4.1 Four-Quadrant Cross-Validation

```
                         | Track B: Calm       |  Track B: Abnormal/Crisis
                         | (Score 8-10)        |  (Score 0-4)
-------------------------+---------------------+-----------------------------
Track A: Strong          |  Consensus           |  Divergence A
Score 6-10               |  Mutual reinforcement|  What is the market panicking
                         |  High rating confidence|  about? Overreaction?
                         |                      |  Or framework blind spot?
-------------------------+---------------------+-----------------------------
Track A: Weak            |  Divergence B        |  Consensus
Score 0-5                |  What is the market  |  Mutual validation
                         |  ignoring? Is the    |  Risk fully priced
                         |  framework too       |  High rating confidence
                         |  aggressive? Or      |
                         |  hidden risk?        |
```

### 4.2 Divergence Handling Rules

| Divergence Type | Trust Priority | Rationale |
|---|---|---|
| **Divergence A** (A strong + B weak) | **Track A** | Market may be overreacting; need to check for external negative factors not captured by framework |
| **Divergence B** (A weak + B strong) | **Track A** | External rating lag is a known problem (verified 17+ months lag); market may be seduced by narrative |

**Core Principle: When the two tracks diverge, trust Track A (auditable public financial facts) over Track B (external ratings and market prices).**

### 4.3 Deviation Score (Suggested Addition)

Deviation score (0-10): Measures consistency between Track A and Track B.

| Deviation | Meaning | Action Recommendation |
|---|---|---|
| 0-3 | Highly consistent | Auto-output, no human intervention needed |
| 4-6 | Moderate deviation | Auto-trigger review reminder |
| 7-10 | Severe deviation | Manual analyst intervention required |

---

## 5. Cash Flow Deep Dive

> **Authoritative Source Reference**: The complete FCF calculation specification (including classification standards, Ponzi detection, and working capital linkage) is available in [Financial Deep Dive](financial-deep-dive.md) Section D. This section is a positioning summary within the dual-track architecture.

### 5.1 Core Formula

Free Cash Flow (FCF) is the core measure of a company's true cash-generating capacity and serves as a validation input in L4 financial layer scoring:

```
FCF = Operating Cash Flow - Capital Expenditure
FCF/Revenue = FCF / Operating Revenue
FCF/Interest = FCF / Interest Expense
```

Data source: Annual cash flow statement (operating cash flow, capex, interest/dividend payments).

### 5.2 FCF Generation Capacity Classification

| FCF/Revenue | FCF/Interest | Classification | Meaning |
|---|---|---|---|
| >5% | >3x | Strong cash generation | Operating cash flow abundant, can cover both investment and debt service, low credit risk |
| 0-5% | 1-3x | Maintenance operations | Can only sustain existing operations and basic debt service, expansion depends on external financing |
| <0 | <1x | Dependent on external financing | Operating cash flow insufficient, requires ongoing financing support -- short-term tolerable, long-term unsustainable |
| Any value | <0 (persistent >2 years) | Ponzi financing suspicion | FCF persistently negative and cannot cover interest expense -- a common characteristic across historical default cases |

### 5.3 Link to Rating Mapping

FCF analysis results do not directly change the Track A composite score but serve as a **validity correction input** for L4 financial layer:

- **FCF/Revenue > 5% and FCF/Interest > 3x**: L4 score ceiling may increase by +1 point above the standard ceiling (credit quality reinforcement confirmation)
- **FCF/Revenue < 0 and FCF/Interest < 1x**: L4 score ceiling locked at 4 (out of 10), meaning the financial layer cannot exceed 4 regardless of other indicators
- **FCF/Interest persistently <0 for over 2 years**: Trigger "Ponzi financing suspicion" risk warning, composite rating ceiling locked at B (regardless of other layers)

### 5.4 Working Capital Linkage

FCF quality must be cross-validated with working capital efficiency (DSO/DIO/DPO/CCC):

| FCF Characteristic | Working Capital Characteristic | Joint Judgment |
|---|---|---|
| FCF positive | CCC normal or improving | True cash generation, FCF credible |
| FCF positive | CCC deteriorating (DSO rising/DIO accumulating) | FCF quality questionable, profit may be eroded by working capital consumption |
| FCF negative | CCC naturally deteriorating | Fundamental operational deterioration, monitor cash runway |
| FCF negative | CCC improving (by squeezing payables) | Short-term window dressing, unsustainable |

---

## 6. Rating Mapping

Rating granularity expanded from 6 tiers to 12 tiers, adding AA+/AA-/A+/A-/BBB+/BBB-/BB+/BB-/B+/B- intermediate grades. Each tier has a width of 0.5 points, aligned with international rating agency granularity (S&P/Moody's/Fitch).

| Score Range | Rating | Meaning |
|---|---|---|
| 9.5 - 10.0 | AAA | Extremely low risk |
| 9.0 - 9.4 | AA+ | |
| 8.5 - 8.9 | AA | Low risk |
| 8.0 - 8.4 | AA- | |
| 7.5 - 7.9 | A+ | Medium-low risk |
| 7.0 - 7.4 | A | |
| 6.5 - 6.9 | A- | |
| 6.0 - 6.4 | BBB+ | Medium risk |
| 5.5 - 5.9 | BBB | |
| 5.0 - 5.4 | BBB- | |
| 4.5 - 4.9 | BB+ | Medium-high risk |
| 4.0 - 4.4 | BB | |
| 3.5 - 3.9 | BB- | |
| 3.0 - 3.4 | B+ | High risk |
| 2.5 - 2.9 | B | |
| 2.0 - 2.4 | B- | |
| 1.0 - 1.9 | CCC | Extremely high risk |
| 0 - 0.9 | D | Default/imminent |

**Special Rules**: When a one-vote veto is triggered, the composite rating ceiling is locked at CCC (score range 1.0-1.9 in the 12-tier system).

---

## 7. EL Expected Loss Integration

New integration layer combining PD rating with LGD framework to enable quantitative EL (Expected Loss) estimation.

### 7.1 Core Formula

```
EL = PD x LGD x EAD

Where:
  PD  = Annualized default probability mapped from PD rating (interval midpoint as point estimate)
  LGD = Loss Given Default mapped from five-level LGD classification
  EAD = Principal + Accrued Interest (simplified, without Credit Conversion Factor CCF)
```

### 7.2 PD to Default Probability Mapping

PD ratings map to annualized default probability intervals, referencing Moody's global historical default rate statistics:

| PD Rating | Corresponding Annualized PD Range |
|---|---|
| AAA | < 0.01% |
| AA+/AA/AA- | 0.01% - 0.05% |
| A+/A/A- | 0.05% - 0.15% |
| BBB+/BBB/BBB- | 0.15% - 0.50% |
| BB+/BB/BB- | 0.50% - 2.0% |
| B+/B/B- | 2.0% - 8.0% |
| CCC | 8.0% - 30% |
| D | > 30% |

**Honesty Label**: The above PD intervals are based on Moody's global statistics from "Corporate Default and Recovery Rates, 1920-2023." These PD intervals are for ranking reference only and should not be used for regulatory capital calculations.

### 7.3 LGD Loss Rate Mapping

LGD grade definitions are available in [LGD & Recovery Analysis Framework](lgd-recovery-framework.md) Section 2; loss rate intervals summarized below:

| LGD Grade | Loss Rate Interval | Recovery Rate Interval |
|---|---|---|
| LGD1 | < 20% | > 80% |
| LGD2 | 20% - 40% | 60% - 80% |
| LGD3 | 40% - 60% | 40% - 60% |
| LGD4 | 60% - 80% | 20% - 40% |
| LGD5 | > 80% | < 20% |

### 7.4 Output Example (Generic Template)

```
Rating: BB+
Annualized PD: 0.5%-2.0% (midpoint 1.0%)
LGD: LGD2 (20-40%, high-quality collateral coverage)
EAD: Principal $100M + Accrued Interest $0.2M = $100.2M (coupon ~0.8%)
EL: 1.0% x 30% x $100.2M = $300,600
    (Expected loss rate of 0.30% x principal)
```

### 7.5 EL Calculation Example: Ford Motor Company

The following demonstrates the complete PD x LGD x EAD calculation chain using Ford Motor Company (analysis date: 2023-09).

**Step 1: Map PD from Rating**

Ford Motor Company Track A Composite Score 5.75 -> Rating mapping BB+ (5.5-5.9 interval, medium-high risk)

| PD Rating | Annualized PD Range | Midpoint Used (Point Estimate) |
|---|---|---|
| BB+ | 0.5% - 2.0% | **1.0%** |

Data source: Section 7.2 PD mapping table, based on Moody's global default rate statistics.

**Step 2: Assess LGD**

Ford's outstanding bonds are senior unsecured:

| LGD Factor | Assessment | Notes |
|---|---|---|
| Debt priority | Senior Unsecured | No specific collateral coverage |
| Industry recovery benchmark | Auto manufacturing | Heavy asset industry, equipment has residual value but technology cycles short |
| Collateral/guarantee | None | Unsecured bond |
| LGD Rating | **LGD3** | Loss rate interval 40%-60%, midpoint 50% |

Data source: LGD & Recovery Analysis Framework Section 2, five-level LGD classification system.

**Step 3: Determine EAD**

Using a Ford Motor Company 5-year note issued in 2022:

| EAD Component | Value | Notes |
|---|---|---|
| Principal | $500M | Face value |
| Accrued interest (3 months) | $7.5M | Coupon rate ~6.0% |
| **EAD Total** | **$507.5M** | Simplified calculation, CCF not considered |

**Step 4: Calculate EL**

```
EL = PD x LGD x EAD

PD  = 1.0% (BB+ rating midpoint)
LGD = 50% (LGD3 midpoint, unsecured bond)
EAD = $507.5M

EL = 1.0% x 50% x $507.5M
   = 0.005 x $507.5M
   = **$2.5375M**

Expected loss rate = 0.50% of principal (1.0% PD x 50% LGD)
```

**Step 5: Comparative Interpretation -- Rating vs. EL**

| Analysis Tool | Conclusion | Precision |
|---|---|---|
| **Rating only (BB+)** | "Medium-high risk, overall credit quality acceptable" | Qualitative description, cannot quantify loss |
| **EL (0.50% of principal)** | "Expected loss ~0.50% of principal, i.e., $5,000 expected loss per $1M exposure" | **Quantitative precision, cross-bond comparable** |

**Why EL is more precise than rating alone:**

1. **Distinguishes within the same rating**: Two BB+ companies -- one with high-quality collateral (LGD2) and one unsecured (LGD3) -- have EL differing by roughly 2x. Rating alone cannot reflect this.
2. **Converts PD and LGD changes into a consistent metric**: Ratings rank from a "probability of loss" perspective, EL ranks from an "expected loss amount" perspective. For portfolio managers, the latter is more actionable.
3. **EL aggregates at portfolio level**: Summing EL across all positions yields portfolio-level expected loss, useful for provisioning and risk budget allocation.

**Important Limitations**:

| Limitation | Impact on this Case |
|---|---|
| PD intervals not calibrated to automotive sector | Actual default rate may differ from Moody's global baseline |
| LGD is a simplified estimate | Actual recovery rate in a default scenario may deviate from 40%-60% |
| EL is a ranking tool | $2.5375M is a ranking reference, not a precise forecast |

### 7.6 Important Limitations

1. **PD mapping is a ranking tool, not a measurement tool**: This framework's EL estimation is used to compare credit risk rank-ordering across different bonds and cannot replace Basel II/III framework regulatory capital measurement.
2. **LGD is a simplified estimate**: LGD intervals are framework set values, not based on market historical recovery rate statistics. See [lgd-recovery-framework.md](lgd-recovery-framework.md) for the honesty statement.
3. **EAD simplified treatment**: Off-balance-sheet credit conversion factors are not considered, as the engine's current analysis targets are credit bonds (principal + interest exposure is explicit).

---

## 8. Decision Rules

| Scenario | Rule | Explanation |
|---|---|---|
| **Both tracks aligned** | Direct rating output | Mutual reinforcement, high confidence |
| **Divergence A (A strong + B weak)** | Downside protection, output B+, annotate "market has additional concerns" | Need to check for risks not captured by framework |
| **Divergence B (A weak + B strong)** | Downside protection, output A-, annotate "rating lag highly likely" | Refer to lessons from historical divergence cases (Lehman 2007-2008, Wirecard 2019-2020) |
| **Insufficient data (e.g., private company, no Track B)** | Output Track A only, annotate "Track B data unavailable" | Data gap itself is a risk signal |
| **One-vote veto triggered** | Ceiling locked at CCC | Survival risk triggered, financial analysis moot |

---

## 9. Risk Mitigation Recommendation Framework

> **Note**: Risk mitigation recommendations are an integral part of the dual-track output; refer to the risk mitigation section below.
> **Note**: The existing engine output stops at "risk identification" and "risk assessment," lacking specific "what to do" guidance. This framework does not provide investment advice ("should we buy or sell"), but helps select the most appropriate mitigation path on the premise that the user has decided to reduce risk.

### 9.1 Design Principles

1. **Not investment advice**: This framework does not answer "should we buy or sell," only "if we want to reduce risk, what options are available"
2. **Scenario matching**: Each mitigation path is annotated with applicable scenarios and costs, avoiding one-size-fits-all
3. **Honesty labeling**: Certain risks (e.g., systemic risk) cannot be mitigated through portfolio adjustments alone -- this must be clearly stated
4. **Integration with existing analysis**: Mitigation recommendations are based on the engine's completed credit analysis conclusions (rating, scenario stress testing, concentration analysis, etc.), not duplicate analysis

### 9.2 Mitigation Path Menu

| # | Mitigation Path | Applicable Scenario | Effectiveness | Cost/Trade-off | Implementation Difficulty |
|---|---|---|---|---|---|
| 1 | **Shorten duration** | Credit quality uncertain, rising rate risk | High | May lose carry income (short-end yields lower) | Easy -- sell long bonds, buy short bonds |
| 2 | **Increase collateral/credit enhancement** | Single entity credit quality weak but still room for mitigation | High | Affects financing cost (issuer may demand compensation) | Medium -- requires renegotiation of terms |
| 3 | **Diversify across regions** | Regional concentration too high (single region exposure >20%) | Medium-high | Transaction costs + new region research costs | Medium -- requires finding new investment targets |
| 4 | **Diversify across industries** | Industry concentration too high (single industry exposure >30%) | Medium-high | Cross-industry research threshold | Medium -- requires understanding new industry logic |
| 5 | **Purchase CDS** | Large single-name credit risk exposure, but do not want to sell outright | Medium | Premium cost (can reference credit spread pricing) | Medium -- market depth limited, requires counterparty |
| 6 | **Reduce single-name exposure** | Single entity concentration too high (>10% of portfolio) | Highest | Trading commissions + liquidity impact (if holding large position) | Easy -- gradual reduction in secondary market |
| 7 | **Increase repo capacity** | Insufficient liquidity reserves, need to strengthen liquidity | Medium | Collateral tie-up, leverage increases | Medium -- requires account/credit line setup |
| 8 | **Add interest rate hedging** | Large duration exposure, rising rate risk | Medium | Hedge cost (futures/IRS) | Medium -- requires derivatives trading capability |
| 9 | **Add covenant protection** | New investments or existing bonds with amendable terms | Medium-high | May reduce issuance spread (stronger protection -> lower coupon) | Medium -- applies only to primary market or bondholder meetings |
| 10 | **Liquidate/exit** | One-vote veto triggered or score <3 | Highest | Transaction costs + opportunity costs + possible market reputation impact | Easy (when market liquidity is good) |

### 9.3 Mitigation Path Recommendation Rules

Automatically generate mitigation recommendations based on engine output:

| Engine Finding | Recommended Mitigation Paths | Priority Ranking |
|---|---|---|
| **A. Single entity credit quality deterioration** (rating below B) | (1) Reduce single-name exposure (2) Shorten duration (3) Purchase CDS (4) Increase collateral requirements | 1>3>2>4 |
| **B. Industry concentration too high** (single industry >30%) | (1) Diversify across industries (2) Reduce exposure to high-risk entities in the industry (3) Purchase industry index CDS (if available) | 1>2>3 |
| **C. Regional concentration too high** (high-risk region >10%) | (1) Diversify across regions (2) Reduce high-risk region exposure (3) Monitor regional debt resolution progress | 1>2>3 |
| **D. Pseudo-high-grade proportion too high** (>15%) | (1) Review each pseudo-high-grade bond individually (2) Reduce bonds with score <5 (3) Require additional collateral | 1>2>3 |
| **E. Liquidity risk prominent** (cash runway <6 months) | (1) Shorten duration (2) Increase repo capacity (3) Maintain cash reserves | 2>1>3 |
| **F. Bear scenario failure** (interest coverage <1.5x) | (1) Significantly reduce exposure (2) Purchase CDS (3) Require additional collateral | 1>3>2 |
| **G. Severe scenario failure** (interest coverage <1.0x) | (1) Liquidate/exit (2) Or require full guarantee (3) Shorten to ultra-short duration | 1 (if exit possible) >3 (if exit not possible) |
| **H. High governance risk** (governance signal triggered) | (1) Reduce exposure to <0.5% (2) Require cross-default clause (3) Arrange acceleration | 1>2>3 |
| **I. Default intent suspicion** (repayment willingness score <-50) | (1) Liquidate/exit only (2) No acceptable alternative mitigation path | 1 (mandatory) |

### 9.4 Mitigation Recommendation Output Template

```
## Risk Mitigation Recommendations

### Core Mitigation Path (Required)
1. **[Path Name]**: [Specific operation description]
   - Applicable conditions: [Preconditions required]
   - Expected effect: [Estimated risk reduction after implementation]
   - Estimated cost: [Transaction cost / Liquidity cost / Opportunity cost]

### Optional Supplementary Paths
2. **[Path Name]**: [Specific operation description]
   - Applicable conditions: [...]
   - Expected effect: [...]
   - Estimated cost: [...]

### Non-Mitigable Risks (Honesty Label)
- **[Risk type]**: This risk cannot be effectively mitigated through portfolio adjustments. Reason: [...]
  Recommendation: [How to manage through other means -- e.g., systemic risk requires reducing overall risk budget]

### Mitigation Priority Ranking
  1. [Highest priority path] -- Lowest cost / Best effect
  2. [Second priority path] -- As supplement
  3. [Alternative path] -- Backup plan when implementation conditions are not met
```

### 9.5 Important Limitations and Disclaimers

**Mitigation limitations that must be annotated**:

| Limitation | Explanation |
|---|---|
| **Systemic risk cannot be mitigated by single-name instruments** | Macro recession, liquidity crisis, sudden regulatory change -- these risks cannot be resolved by adjusting individual bond exposure; only overall risk budget reduction or macro hedging tools can help |
| **CDS market depth is limited** | The credit derivatives market is still at an early stage of development; most individual bonds lack corresponding CDS availability -- the "purchase protection" path requires verifying actual market accessibility |
| **Portfolio adjustments have costs** | Rebalancing must consider transaction costs (commissions + impact costs) + tax costs + opportunity costs (missing potential price recovery after selling) |
| **Liquidity constraints** | During market stress, large-scale reduction may cause greater price losses -- the actual effect of the "reduce position" path during a crisis may be far below model estimates |
| **Missing data affects mitigation effectiveness judgment** | If the engine analysis itself has low data completeness, the confidence level of mitigation recommendations will be correspondingly reduced |
| **Principal-agent issues** | Different roles (fund manager vs. credit underwriter vs. trader) have different cost tolerance for the same mitigation path -- a fund manager's tolerance for yield reduction differs from a credit underwriter's |

### 9.6 Link to Cross-Validation Matrix

Mitigation recommendation intensity should be linked to cross-validation divergence status:

| Cross-Validation Status | Mitigation Recommendation Intensity | Explanation |
|---|---|---|
| **Consensus (A strong + B strong, or A weak + B weak)** | Standard recommendations | Sufficient confidence, standard template output |
| **Divergence (A strong + B weak, or A weak + B strong)** | Enhanced recommendations + directional guidance | Uncertainty exists -> recommend implementing "irreversible" mitigation paths (e.g., reduce exposure) over "reversible" paths (e.g., shorten duration) |
| **Insufficient data** | Conservative recommendations | Key data missing -> prioritize "information-insensitive" paths (e.g., increase collateral) |

---

## 10. Complete Reasoning Example: First Solar vs SunPower (5-Step Reasoning)

### Background
- Analysis date: 2025-06
- Industry: Solar (Policy-Driven)
- Targets: First Solar (FSLR, listed, bonds outstanding) vs SunPower (SPWR, listed, high yield profile)

### Step 1: Industry Classification and Weight Determination

- 10-dimension scoring result: Policy-Driven (D3=5, D4=4)
- Weight template: L1 Policy 35%, L2 Technology 30%, L3 Supply Chain 20%, L4 Financial 15%

### Step 2: Layer-by-Layer Scoring

#### First Solar

| Layer | Key Signals | Score | Weight |
|---|---|---|---|
| L1 Policy | IRA (Inflation Reduction Act) support for domestic solar manufacturing, Section 45X credits | 8 | 35% |
| L2 Technology | CdTe thin-film efficiency leader, Series 6+/7 module production | 8 | 30% |
| L3 Supply Chain | Vertically integrated, dominant US market share, multi-year contracted backlog | 7 | 20% |
| L4 Financial | Cash reserves $2.1B, positive operating cash flow, low debt/equity | 7 | 15% |

**Composite = 8x35% + 8x30% + 7x20% + 7x15% = 2.80 + 2.40 + 1.40 + 1.05 = 7.65**

#### SunPower

| Layer | Key Signals | Score | Weight |
|---|---|---|---|
| L1 Policy | IRA benefits apply but less direct as distributor/installer focused | 5 | 35% |
| L2 Technology | Relies on Maxeon (spinoff) for panel supply, limited proprietary technology | 2 | 30% |
| L3 Supply Chain | High customer concentration, distribution model lacks pricing power | 2 | 20% |
| L4 Financial | Debt/equity elevated, negative FCF, cash runway concerns | 1 | 15% |

**Composite = 5x35% + 2x30% + 2x20% + 1x15% = 1.75 + 0.60 + 0.40 + 0.15 = 2.90**

**One-Vote Veto Check**: SunPower debt/equity ratio exceeds danger threshold but does not trigger an explicit technology elimination condition. Rating ceiling not locked. Composite score 2.90 -> B.

### Step 3: Track B Analysis

#### First Solar

| Signal Dimension | Status | Notes |
|---|---|---|
| Credit spread | Watch | Some industry-wide concerns |
| Volatility | Calm | Normal equity market fluctuations |
| Fund flows | Calm | Stable institutional interest |
| Rating events | Stable | Ratings maintained |

**Track B Score**: 7 (Watch/Calm mix)

#### SunPower

| Signal Dimension | Status | Notes |
|---|---|---|
| Credit spread | Abnormal | High-yield bonds reflecting distress |
| Volatility | Watch | Elevated stock volatility |
| Fund flows | Watch | Institutional outflows |
| Rating events | Negative | Outlook negative / potential downgrade |

**Track B Score**: 3 (Abnormal/Watch mix)

### Step 4: Cross-Validation

| Comparison | First Solar | SunPower |
|---|---|---|
| Track A Score | 7.65 (A-) | 2.90 (B) |
| Track B Score | 7 (Watch/Calm) | 3 (Abnormal/Watch) |
| Cross-Validation Status | **Consensus (A strong + B moderate)** | **Consensus (A weak + B abnormal)** |
| Framework Judgment | Mutual reinforcement, high confidence | Mutual validation, risk fully priced |
| Final Rating | A- (High confidence) | B (Medium confidence) |
| Score Gap | **4.75 points -- framework clearly distinguishes strong vs weak** | |

### Step 5: Output and Completeness Report

**First Solar:**
- Composite Rating: A- (High confidence)
- Core Finding: CdTe technology leadership + IRA beneficiary + strong backlog
- Key Risk: Industry-wide capacity oversupply may pressure margins
- Data Completeness: L2 Technology lacks yield data for competitor comparison (score +/-1.0 uncertainty)

**SunPower:**
- Composite Rating: B (Medium confidence)
- Core Finding: Technology transition challenges + elevated debt + FCF negative
- Key Risk: High-yield bond market could close if fundamentals deteriorate further
- Data Completeness: Track B data available but high yield market less liquid than investment grade

---

## 11. Back-Test Validation Example: Lehman Brothers Dual-Track Analysis

### T1 Timepoint (2007-03-31, T-18 months)

| Track | Signal | Status |
|---|---|---|
| **A - Leverage ratio 31:1** | Extreme leverage | Red |
| **A - Subprime mortgage exposure ~$85B** | Excessive concentration | Red |
| **A - Short-term funding >60% of liabilities** | Maturity mismatch | Yellow |
| **A - Commercial real estate 28% of portfolio** | Concentration risk | Yellow |
| **A - Q1 2007 net income flat, provisions rising** | Earnings deterioration | Yellow |
| **B - External rating A2/A (Moody's/S&P) Stable** | Excellent (but misleading) | Green |
| **B - CDS spread ~60bp** | Normal financing cost | Green |
| **B - Investment banking industry robust** | Industry tailwind | Green |

**Cross-Validation Status: Divergence B (A weak + B strong) -- Track A 3 reds + 2 yellows, Track B entirely green misleading.**

**Framework Judgment**: Trust Track A -> Output high-risk rating, "recommend continued monitoring."

**Actual Outcome**: T+4.5 months (T2) Track A deteriorated to 5 reds, Track B began showing yellow signals (convergence toward Track A). T+18 months bankruptcy.

> **Validation Methodology**: This back-test case follows the dual-timepoint validation standard process defined in [Validation Methodology](validation-methodology.md).

---

## Related Content

- [Engine Architecture Overview](engine-overview.md) -- Core philosophy, overall architecture, design principles
- [Industry Classification & Analysis Framework](industry-framework.md) -- 10-dimension scoring, industry types, pyramid specifications
- [Mosaic Engine](mosaic-engine.md) -- Signal extraction, assembly, completeness assessment, Mode B interface
