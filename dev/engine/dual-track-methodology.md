# Dual-Track Analysis Methodology

**Version**: v0.3.2 | **Date**: 2026-07-10

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

> **Reading guide**: §§1-4, §6 (Rating Mapping), §7 (EL integration), and §8
> (Decision Rules) contain the executable methodology — required reading before
> executing any work path that references this document. §7.7 (unrated /
> thinly-traded issuers) is required when the issuer lacks ratings or liquid
> market signals.
> §5 and §§9-11 (positioning summary, mitigation framework, worked examples)
> live in `appendix/dual-track-methodology-appendix.md` — read only when the
> analysis needs detailed justification or the user asks for methodological
> background.


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


> **Appendix**: §5 (Cash Flow Deep Dive positioning), §9 (Risk Mitigation), §10 (First Solar worked example), §11 (Lehman back-test) moved to `appendix/dual-track-methodology-appendix.md` — read on demand.

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

### 7.7 Unrated and Thinly-Traded Issuers

Approximately 30% of European mid-cap industrial companies and a significant share of
emerging-market issuers are unrated by the major agencies (S&P/Moody's/Fitch). These
issuers lack CDS contracts, have illiquid or no public bonds, and do not benefit from
the cross-validation framework that Track B provides for rated issuers. This section
defines the proxy-signal methodology for unrated issuers.

**Completeness expectation**: Unrated issuers will typically score below the 80% green
threshold on completeness density. This is expected and not a failure — the analysis
must document which signals are missing and which proxies are used.

**Proxy signals (in priority order)**:

| Proxy | Source | Strength | Limitation |
|---|---|---|---|
| **Equity-implied credit risk** | EV/EBITDA vs rated peers, equity volatility, short interest | Moderate | Equity markets price growth, not credit; can be misleading in distress |
| **Peer spread benchmarking** | Public bond spreads of nearest-rated comparable companies (industry, size, leverage) | Moderate | Rating, structure, and jurisdiction differences introduce noise |
| **Schuldschein / private placement data** | Issuer's own private-placement pricing if disclosed | Moderate | Limited public availability; terms vary widely |
| **Bank loan margin** | Syndicated loan pricing if disclosed in financial notes | Weak | Relationship pricing; not mark-to-market |
| **Altman Z-score / Merton model** | Public financials only | Weak | Book-value based; lags market signals |

**Confidence adjustment**: For unrated issuers, the default confidence cap is **medium**
(two levels below the standard "high" for fully-rated issuers with liquid CDS). The
QA review should verify that the analysis does not claim "high confidence" for an
unrated issuer without exceptional justification (e.g., public benchmark bond issued
within 6 months with observable secondary trading).

**Track B handling**: When Track B is absent or severely limited, the analysis defaults
to Track A-leading with a documented data gap. The cross-validation outcome is
`incomplete`, not `Track A strong` — the distinction matters for the QA verdict.

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

## Related Content

- [Engine Architecture Overview](engine-overview.md) -- Core philosophy, overall architecture, design principles
- [Industry Classification & Analysis Framework](industry-framework.md) -- 10-dimension scoring, industry types, pyramid specifications
- [Mosaic Engine](mosaic-engine.md) -- Signal extraction, assembly, completeness assessment, Mode B interface
