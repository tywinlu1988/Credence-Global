# Quantitative Analysis Methodology — Fixed Income Credit Analysis Engine

**Version**: v0.0.1 | **Date**: 2026-07-10
**Positioning**: Deep quantitative layer of Track B (Market Pricing) · Quantitative analysis specification in the dual-track framework

> **Honest Statement**: The statistical correction methods defined in this document (confidence intervals / ADF test / B-P test / FDR correction) are methodological documentation and have not yet been verified through code implementation.

---

## 1. Positioning of Quantitative Analysis

### 1.1 Role in the Dual-Track Framework

In the dual-track analysis framework, Track B (market pricing signals) was originally defined as a four-level signal system (Calm / Attention / Abnormal / Crisis). Here, quantitative analysis is the **deepening layer of Track B** — performing precise quantitative dissection of each signal type on top of the four-level classification.

```
Track B (Original Four-Level Signals)     Quantitative Analysis (Deepening Layer)
   ├── Credit Spread                         ├── L0.1 Market Data Benchmarking
   ├── Volatility                             ├── L0.2 Statistical Signal Detection
   ├── Capital Flow Direction                 ├── L0.3 Quantitative Factor Model
   └── Rating Migration                        └── Stress Testing & Scenario Analysis
```

| What it does | What it does not do |
|--------|---------|
| Extract quantitative signals from market public data | Substitute for fundamental analysis (Track A) |
| Convert market signals into structured scores | Predict exact default dates |
| Detect abnormal volatility and pricing deviations | Provide financial audit conclusions |
| Provide quantitative inputs for the cross-validation matrix | Substitute for external ratings (external ratings themselves are one of the inputs) |
| Quantify the deviation between pricing and fundamentals | Provide trading advice (only provides analytical framework) |

### 1.2 Three Levels of Quantitative Analysis

| Level | Name | Description | Data Requirements | Computational Complexity |
|------|------|------|----------|-----------|
| **L0.1** | Market Data Benchmarking | Clean, align, and compare available raw market data — "what it is" | Low: public market data | Low: basic statistics |
| **L0.2** | Statistical Signal Detection | Build statistical models on top of L0.1 to detect anomalies — "where is the problem" | Medium: requires historical series | Medium: statistical tests |
| **L0.3** | Quantitative Factor Model | Multi-factor decomposition and stress testing to explain pricing — "why, what if" | High: requires panel data and benchmarks | High: regression / simulation |

**Implementation Priority: L0.1 > L0.2 > L0.3**. Under public data constraints, L0.1 and L0.2 steps are the core of most analyses. L0.3 is only fully feasible after paid data is supplemented.

### 1.3 Data Availability Constraints (Honest Statement)

This engine **does not require paid terminals such as Wind/Bloomberg as prerequisites**. The following is a hard constraint list of what can and cannot be done in a zero-paid-terminal environment:

| Indicator | Availability | Source/Alternative | Quality |
|------|---------|--------------|------|
| Yield-to-Maturity (YTM) | Available | Exchange quotes / China Money Network / Hexun bond data | Relatively high — may deviate for inactive bonds |
| Z-spread | **Not available** | Requires cash flow modeling engine from professional terminals | Unavailable — can only approximate |
| OAS | **Not available** | Requires option-embedded pricing model | Unavailable — can only approximate |
| Modified Duration | Partially available | Approximate calculation based on coupon/maturity/yield (MacCaulay/1+YTM) | Medium — does not include option-adjusted adjustments |
| Convexity | **Not available** | Requires precise cash flow pricing | Unavailable |
| Historical yield series | Available (limited) | Exchange public quotes, missing for inactive bonds | Medium — sparse data |
| Bid-ask spread | **Not available** | China bond market is opaque; no such data without professional terminals | Unavailable — approximate with turnover rate |
| Implied Volatility | **Not available** | No standardized options market for China credit bonds/convertible bonds | Unavailable — use historical volatility |
| Stock price/volatility | Available | Free quote APIs / financial websites | Relatively high |
| Trading volume/turnover rate | Partially available | Exchange public data, but data is sparse for very illiquid bonds | Medium |
| Credit rating migration | Available | Rating agency announcements | Relatively high — but has lag |
| Capital flow direction / Northbound capital flow | Available | Exchange/HKEX daily disclosures | Relatively high — but insufficient granularity |

**Core conclusion: Without relying on paid terminals, we can perform trend analysis, anomaly detection, and relative value ranking based on public market data, but cannot conduct fine-grained analysis requiring precise cash flow discount models and option pricing models.**

---

## 2. Credit Spread Analysis

### 2.1 Spread Indicator Definitions

Under the hard constraint of being unable to obtain Z-spread and OAS, this engine uses the following spread approximation system:

| Indicator | Formula | Application Scenario | Limitations |
|------|------|---------|--------|
| **YTM Spread** | YTM_bond - YTM_same-maturity CDB bond | General — most basic credit spread approximation | Does not account for term structure differences; large deviation for option-embedded bonds |
| **YTM-Benchmark Rate Approximate Z-spread** | Same as above + linear interpolation adjustment | When remaining maturity deviates from benchmark maturity | Medium effectiveness — directionally correct but biased in magnitude |
| **Industry Spread** | YTM spread - same-rating industry average | For cross-industry comparison, removes industry beta | Requires sufficient sample to compute industry average |
| **Individual Bond-Industry Deviation** | Individual bond YTM spread - Industry YTM spread median | Identify bonds above/below peers within the same industry | Median unstable when sample insufficient |

**Z-spread Alternative Handling Rules:**

```
When Z-spread is needed but unavailable:
  1. First choice: YTM - same-maturity CDB bond yield (linear interpolation)
  2. Annotate: "Z-spread unavailable, using YTM spread approximation — analysis error may increase with duration and option-embedded features"
  3. Annotate separately for option-embedded bonds: "Option-embedded pricing depends on OAS model, cannot be precisely calculated"
  4. Use ranking rather than absolute values in conclusions — "Spread level higher than 80% of peers" is better than "Spread is 235bp"
```

### 2.2 Three-Dimensional Spread Comparison Framework

The credit spread of each analysis subject must be compared across three dimensions:

```
Three-Dimensional Spread Analysis
  ├── Horizontal: Spread distribution of same-industry/same-rating enterprises
  │    ├── Goal: Identify relative pricing — which enterprises are overvalued or undervalued by the market
  │    ├── Output: Quantile position of individual bond within industry spread distribution
  │    └── Example: Intra-industry comparison of 5 solar PV convertible bonds (see 2.5)
  │
  ├── Vertical: Enterprise's own historical spread quantile
  │    ├── Goal: Determine whether current pricing is high or low relative to own history
  │    ├── Window: 6 months / 1 year / 3 years (depending on data availability)
  │    ├── Quantile ranges: 0-20% compressed / 20-80% normal / 80-100% expanded
  │    └── Rule: 3 consecutive months at >80% quantile → marked as "persistent spread widening"
  │
  └── Cross-Sectional: Inter-rating spread compensation
       ├── Goal: Determine whether market's risk premium across different ratings is reasonable
       ├── Indicators: AAA-BBB spread differential, BBB-B spread differential
       ├── Normal range: AAA-BBB spread differential at 80-150bp (historical median)
       └── Abnormal scenarios:
            ├── Inter-rating spread differential narrowing → market not distinguishing ratings, potential undervaluation risk
            └── Inter-rating spread differential widening sharply → market panic, liquidity premium dominates
```

### 2.3 Spread Anomaly Detection Rules

| Anomaly Type | Quantitative Definition | Signal Level | Possible Meaning |
|---------|---------|---------|---------|
| **Jump** | Single-day spread change > 50bp | Red Abnormal | Sudden credit event / rating adjustment / price error |
| **Trend** | Cumulative spread widening > 50bp over 20+ consecutive trading days | Yellow Attention | Gradual credit quality deterioration / industry headwinds |
| **Divergence from Fundamentals** | Fundamental score stable but spread widening > 1 standard deviation | Orange Divergence | Market pricing disconnected from fundamentals → divergence signal |
| **Divergence from Industry** | Industry spread stable but individual bond spread independently widening > 30bp | Orange Divergence | Enterprise-specific risk exposure |
| **Liquidity Compression** | Simultaneous sharp drop in trading volume + spread widening | Red Abnormal | Precursor to liquidity crisis |

**Anomaly Detection Processing Flow:**

```
1. Obtain spread time series from L0.1
2. Calculate historical mean and standard deviation (window = 60 trading days)
3. Detection conditions:
   a) Single-day change > Mean + 3σ → Jump anomaly
   b) 20-day cumulative change > Mean + 2σ → Persistent anomaly
   c) Spread quantile > 90% for 15 consecutive days → High-water mark warning
4. Cross-validation: Simultaneously check whether trading volume/turnover rate is abnormal
5. Output: Anomaly signal + possible explanatory hypothesis + suggested action
```


### 2.3.1 Confidence Interval Specification for Spread Statistics [Statistical Correction v0.0.1]

**Bootstrap confidence interval for spread mean estimation:**
```
Spread Mean 95% Bootstrap Confidence Interval
├── Method: Non-parametric Bootstrap, 1000 resamples
├── Calculation Steps:
│   1. Resample N times with replacement from the original spread series (N observations) → Bootstrap sample
│   2. Calculate the spread mean of this sample
│   3. Repeat steps 1-2 for a total of 1000 times → obtain 1000 Bootstrap means
│   4. Take the 2.5% and 97.5% quantiles of these 1000 means → 95% confidence interval
├── Output: "Spread Mean: 185bp [95% CI: 172bp–198bp]"
└── Prerequisite: Bootstrap only executable when N≥30; when N<30 annotate "Sample size insufficient, Bootstrap unreliable, using t-distribution approximation"
```

**Spread Anomaly Detection Rules Revision (replacing original 50bp subjective threshold):**
```
Anomaly Type: Jump
Old rule: Single-day spread change > 50bp
New rule: Single-day spread change > upper bound of 95% Bootstrap confidence interval of historical rolling mean (60d)
        → Current value > μ̂_boot_97.5% → Mark as anomaly
        → Annotate: "Bootstrap 95% CI upper bound = XX bp, current change exceeds this range"

Anomaly Type: Trend
Old rule: Cumulative spread widening > 50bp over 20+ consecutive trading days
New rule: 20-day cumulative change > upper bound of 95% Bootstrap confidence interval of historical rolling mean (60d)
        → Annotation method same as above, annotate "Corrected via Bootstrap CI"

Anomaly Type: Divergence from Fundamentals
Old rule: Fundamental score stable but spread widening > 1 standard deviation
New rule: Fundamental score stable but spread widening exceeds 95% Bootstrap confidence interval of rolling mean
```

**Confidence Interval Visualization Specification:**
- All spread time-series charts must include a 95% confidence interval band (shaded area)
- Annotate whether the current value falls within the confidence interval
- 5 consecutive trading days exceeding the interval upper bound → escalate signal level

### 2.3.2 Multiple Hypothesis Testing Correction (FDR) [Statistical Correction v0.0.1]

**Problem Background:** Simultaneously monitoring N subjects × K detection rules = a large number of parallel hypothesis tests; the false positive rate inflates with the number of tests. For example, simultaneously monitoring 3 anomaly types for 100 bonds = 300 parallel tests. Even if all bonds are normal, approximately 15 false positive signals would be generated (300 × 0.05).

```
FDR Correction Specification (Benjamini-Hochberg Procedure):
├── Set FDR control level: q = 0.05 (i.e., allow 5% of significant signals to be false positives)
├── Applicable Scenarios:
│   ├── Spread anomaly detection: simultaneously detect M anomaly types for N bonds
│   ├── Volatility anomaly detection: simultaneously detect K volatility patterns for N stocks
│   └── Any scenario involving multiple comparisons
├── BH Procedure Steps:
│   1. Sort p-values of all m parallel tests: p₁ ≤ p₂ ≤ ... ≤ pₘ
│   2. Find the largest k such that pₖ ≤ (k/m) × q
│   3. Reject H₀ for the first k tests corresponding to this criterion → these are "significant after FDR correction"
│   4. The remaining m-k tests, although raw p<0.05, are not significant after correction → annotate "not significant after correction"
├── Output Specification:
│   ├── "Number of triggered warnings today: 15"
│   ├── "Number of significant signals after FDR correction: 8"
│   ├── "Number of uncorrected raw signals: 15"
│   └── "False positive risk note: among the 15 warnings triggered today, statistically approximately 0-7 could be false positives"
└── Annotation Rules:
    ├── Signals still significant after correction → annotate "Significant after FDR correction"
    ├── Signals not significant after correction → annotate "Raw p<0.05 but not significant after FDR correction"
    └── Global annotation: "FDR correction: Benjamini-Hochberg procedure, q=0.05"
```

### 2.4 Convertible Bond Spread Analysis (Special Handling)

Credit spread analysis for convertible bonds differs from plain bonds due to their option-embedded nature:

| Aspect | Convertible Bond Treatment | Reason |
|------|--------------|------|
| YTM Calculation | Standard YTM + separation of conversion option value | Plain bond portion and conversion right need separate pricing |
| Credit Spread Benchmark | Plain bond value vs same-rating credit bonds | Analysis of bond floor after stripping conversion option premium |
| Yield-to-Maturity | Typically negative — plain bond portion usually significantly discounted | Conversion option value offsets credit risk premium |
| More Relevant Indicators | Conversion premium + Pure bond premium | Credit risk is more subtle in convertible bonds |

### 2.5 Example: Cross-Comparison of 5 Solar PV Convertible Bond Spreads

**Analysis Date:** 2026-07-01 | **Data Source:** Exchange public quotes + CDB bond yield-to-maturity curve

**Sample Pool:** 5 solar PV industry convertible bonds

| CB | Underlying Stock | Price (CNY) | YTM (%) | YTM Spread (bp) | Conversion Premium (%) | Rating |
|--------|---------|---------|-------------|-----------|------------|------|
| LONGi 22 CB | LONGi Green Energy | 105.80 | 0.52 | 95 | 74 | AAA |
| Tongwei 22 CB | Tongwei Co. | 98.20 | 2.15 | 258 | 45 | AAA |
| Trina 23 CB | Trina Solar | 101.50 | 1.80 | 223 | 52 | AA |
| Jinko CB | Jinko Energy | 103.40 | 1.35 | 178 | 38 | AA |
| JA Solar CB | JA Solar Technology | 96.80 | 2.45 | 288 | 61 | AA |

**Three-Dimensional Analysis Results:**

| Dimension | Analysis | Findings |
|------|------|------|
| **Horizontal Comparison** | Industry spread median = 223bp (around Tongwei 22 / Trina 23) | LONGi 22 has the lowest spread (95bp) — AAA rating + industry leader premium |
| | | JA Solar has the highest spread (288bp) — market has additional concerns about its credit quality |
| | LONGi 22 vs JA Solar spread differential = 193bp | Extreme divergence within the same industry — validating rating differentiation |
| **Vertical Comparison** | LONGi 22 YTM spread 95bp → historical quantile approx. 55% | Close to historical average, not abnormal |
| | Tongwei 22 YTM spread 258bp → historical quantile approx. 78% | Above historical average, consistent with 2025 loss expectations |
| **Cross-Sectional Comparison** | AAA spread median ≈ 95-258bp (small sample) | High divergence within AAA — rating signal is coarse |
| | AA spread median ≈ 178-288bp | Similarly divergent within AA — enterprise individuality outweighs rating commonality |

**Core Conclusions:**
- LONGi 22's spread is significantly lower than peers — AAA rating + industry leader position provides a "safety premium," but the 74% conversion premium indicates very conservative valuation of the plain bond portion
- JA Solar has the highest spread — the market has already priced in its declining profitability and rising debt ratio
- Spread differential within the same industry reaches 193bp — **driven by fundamental differences**, not systemic market sentiment

**Data Quality Annotations:**
- YTM spread calculation based on closing clean price; inactive bonds may have a 1-2 day lag
- Z-spread unavailable, assuming term-matching error within ±15bp
- When convertible bond YTM is negative, the practical meaning of spread analysis diminishes — focus should shift to conversion premium

---

## 3. Volatility Analysis

### 3.1 Volatility Indicators and Availability

| Volatility Type | Definition | Data Availability | Significance for Credit Analysis |
|-----------|------|-----------|-----------------|
| **Historical Volatility (HV)** | Standard deviation of past N-day stock/yield returns (annualized) | Available for listed companies (free quotes) | Reflects uncertainty in enterprise value |
| **Implied Volatility (IV)** | Derived inversely from option market prices | Not available — China credit bond/CDS option market does not exist | N/A |
| **Realized Volatility (RV)** | Daily volatility calculated from high-frequency trading data | Only available for highly liquid stocks (minute-level quotes are paid) | Substitute with daily HV |
| **Idiosyncratic Volatility** | Residual volatility after stripping market factors | Can be estimated from free data via regression | Reflects enterprise-specific risk |

**Hard Constraint:** Non-listed companies have no stock price data; volatility analysis is completely unavailable. This is one of the core limitations of Track B for non-listed enterprises.

### 3.2 Historical Volatility Calculation Specification

```
Basic Parameters:
├── Data Source: Free quote APIs / financial websites (Sina Finance, East Money, etc.)
├── Price Type: Closing price (adjusted)
├── Return Calculation: ln(P_t / P_{t-1}) × 100%
├── Annualization Factor: √252 (number of trading days)
└── Calculation Windows: 20-day / 60-day / 120-day (output simultaneously)

HV Formula:
  HV = σ(r) × √252
  where σ(r) = standard deviation of daily returns over the window period

Output Format:
  HV_20d: 35.2%  (Short-term — reflects uncertainty over the past month)
  HV_60d: 28.7%  (Medium-term — reflects uncertainty over the past quarter)
  HV_120d: 32.1% (Long-term — reflects uncertainty over the past half year)
  HV_Trend: "Rising" | "Declining" | "Stable" (determined via 20-day moving average)
```

### 3.3 Volatility Decomposition Framework

Under data constraints, a simplified decomposition approach is used — approximating systematic and idiosyncratic volatility decomposition through single-factor regression:

```
Step 1: Obtain industry index / market index returns
  Market proxy: CSI 300 (000300.SH)
  Industry proxy: Solar PV industry index (931151.CSI) / CSI industry indices

Step 2: Rolling regression (window = 120 trading days)
  R_i = α + β × R_m + ε
  where R_i = daily return of individual stock
        R_m = daily return of the index
        ε = residual (idiosyncratic return)
        β = systematic factor exposure

Step 3: Volatility decomposition
  Total volatility (V_total) = β² × V_m + V_ε
  Systematic proportion = β² × V_m / V_total × 100%
  Idiosyncratic proportion = V_ε / V_total × 100%

Step 4: Output
  ├── Systematic volatility proportion: 65% (industry risk dominates)
  ├── Idiosyncratic volatility proportion: 35% (enterprise-specific risk)
  ├── Systematic volatility trend (vs industry): "Above industry average, and the gap is widening"
  └── Idiosyncratic volatility trend: "Rising — reflecting increased enterprise-specific risk"
```

**Limitations Annotated:**
- Simplified single-factor model does not account for time-varying industry beta
- Assumes beta is stable within the 120-day window — a weak assumption in volatile markets
- This analysis is unavailable for non-listed companies

### 3.4 Volatility Jumps and Warning Signals

| Volatility Pattern | Detection Method | Credit Implication | Suggested Action |
|-----------|---------|---------|---------|
| **Volatility Spike** | HV > historical mean + 3σ | Sudden credit event | Check contemporaneous news/announcements — may be rating downgrade, litigation, technical issues |
| **Persistent Volatility Increase** | HV_20d > HV_60d > HV_120d for 5 consecutive days | Systematic increase in uncertainty | Watch — leads spread widening by 6-12 weeks |
| **Volatility + Spread Dual Rise** | Both breach thresholds simultaneously | Confirmation of credit quality deterioration | Strong signal — market is repricing in both dimensions simultaneously |
| **Sudden Spike Under Low Volatility** | Previous HV < mean, suddenly jumps to > mean + 2σ | Risk exposed after being underestimated | Most dangerous signal — the market had previously ignored accumulated risk |
| **Divergence Between Volatility and Fundamentals** | Fundamentals stable but volatility surges | Market has concerns not captured by the framework | Divergence signal — need to investigate hidden risks |

**Volatility Jump Rating Rules:**

| HV_20d Change Magnitude | Rating Adjustment | Explanation |
|----------------|---------|------|
| < 10% and trend stable | No change | Normal volatility |
| 10-30% increase | Track B signal upgrade → Attention | Uncertainty increasing, needs attention |
| 30-50% increase | Track B signal upgrade → Abnormal | Significant change, recommend investigating cause |
| > 50% increase | Track B signal upgrade → Crisis | Violent fluctuation, may trigger Cross-Validation Divergence A |
| > 20% decline | No change/downgrade | Uncertainty narrowing — neutral or positive signal |


### 3.4.1 Confidence Interval Specification for Volatility Statistics [Statistical Correction v0.0.1]

**95% Confidence Interval for Historical Volatility (Based on Chi-Square Distribution):**
```
95% CI Formula for HV (assuming returns approximately normally distributed):
  [(n-1) × HV² / χ²₀.₀₂₅(n-1),  (n-1) × HV² / χ²₀.₉₇₅(n-1)]

Where:
├── n = number of observations in the window (e.g., 20-day window n=20)
├── HV = Historical Volatility (annualized)
├── χ²₀.₀₂₅(n-1) = 2.5% quantile of chi-square distribution with n-1 degrees of freedom
├── χ²₀.₉₇₅(n-1) = 97.5% quantile of chi-square distribution with n-1 degrees of freedom
└── Degrees of freedom note: the mean return is estimated, consuming 1 degree of freedom

Calculation Example (n=20, HV=35.2%):
  χ²₀.₀₂₅(19) = 8.907
  χ²₀.₉₇₅(19) = 32.852
  CI = [19 × 0.352² / 32.852,  19 × 0.352² / 8.907]
     = [19 × 0.1239 / 32.852,  19 × 0.1239 / 8.907]
     = [0.0716, 0.2643]
     = [26.8%, 51.4%] (annualized volatility)

Output: "HV_20d: 35.2% [95% CI: 26.8%–51.4%]"
```

**Volatility Jump Detection Rules Revision:**
```
Old rule: HV > historical mean + 3σ → Volatility spike
New rule: Current HV > upper bound of 95% CI of rolling window HV → Mark as volatility jump
        → Annotate: "Current HV = XX%, exceeds upper bound of rolling window HV 95% CI (YY%)"

Old rule: HV_20d > HV_60d > HV_120d for 5 consecutive days → Persistent volatility increase
New rule: HV_20d > HV_60d > HV_120d AND HV_20d exceeds the 95% CI upper bound of HV_60d
        → Confirms the trend is statistically significant

Old rule: Sudden spike under low volatility (previous HV < mean, suddenly jumps to > mean + 2σ)
New rule: Previous HV within 95% CI, suddenly jumps to exceed 95% CI upper bound
        → Most dangerous signal — risk exposed after being underestimated
```

### 3.4.2 Volatility Multiple Hypothesis Testing Correction (FDR) [Statistical Correction v0.0.1]

```
Volatility FDR Correction (shares the same framework as Spread FDR Correction):
├── Sources of parallel tests:
│   ├── N stocks × 3 volatility patterns (spike / persistent increase / dual rise)
│   └── 3 volatility windows (20-day / 60-day / 120-day) can be selectively combined
├── BH Procedure: Consistent with Section 2.3.2 → use Benjamini-Hochberg to control FDR at q=0.05
├── Output Specification:
│   ├── "Volatility warnings today: 12"
│   ├── "Number of significant signals after FDR correction: 7"
│   └── "False positive risk note: among 12 warnings, statistically approximately 0-5 could be false positives"
└── Annotation Rules: Consistent with Section 2.3.2
```

### 3.5 Example: Shuangliang Energy Volatility Deteriorated Before Rating Downgrade

**Case Background:** Shuangliang Energy (600481) — solar PV equipment + polysilicon reduction furnace manufacturer
**Key Timeline:**

| Time | Event |
|------|------|
| 2025-Q4 | Polysilicon prices continued to decline, Shuangliang's reduction furnace order demand fell |
| 2026-01 | Shuangliang earnings pre-announcement: expected loss for 2025 |
| 2026-03 | An external rating agency downgraded Shuangliang's rating outlook to negative |
| 2026-05 | Rating downgrade (AAA to AA) |

**Volatility Analysis (Retrospective to 2025-Q3):**

| Window | HV_20d | HV_60d | HV Trend | Signal |
|------|--------|--------|--------|------|
| 2025-Q3 (Jul-Sep) | 22.3% | 24.1% | Stable | Blue Normal |
| 2025-Q4 (Oct) | 28.7% | 25.8% | Rising | Yellow HV_20d MoM +29% |
| 2025-Q4 (Nov) | 35.2% | 28.4% | Rapidly rising | Orange HV_20d breached mean + 2σ |
| 2025-Q4 (Dec) | 42.8% | 34.1% | Persistently rising | Red High volatility — leading rating by approximately 3 months |
| 2026-01 (Earnings pre-announcement) | 51.3% | 39.5% | Spike | Red Confirmation of volatility + spread dual rise |
| 2026-03 (Negative outlook) | 45.2% | 41.8% | High-level oscillation | Red Volatility already high for 3 months |
| 2026-05 (Rating downgrade) | 48.6% | 44.2% | Persistently high | Red Market pricing already reflected before rating downgrade |

**Key Findings:**
1. HV_20d began rising in October 2025 (leading the rating downgrade by approximately 7 months)
2. HV breached the "mean + 2σ" threshold in December 2025 (leading by approximately 5 months)
3. Yield volatility reacted before spreads and ratings — **volatility is a leading indicator**
4. By the time of the rating downgrade, volatility had been at high levels for 5 months — rating lag was quantitatively confirmed

**Signal Detection Rule Trigger Records:**

```
2025-10-15  HV_20d MoM +29%          → Triggered "Persistent Volatility Increase"    → Signal: Yellow
2025-11-20  HV_20d breached mean + 2σ → Triggered "Volatility Spike"                   → Signal: Orange
2025-12-10  HV_20d > HV_60d > HV_120d for 5 days → Triggered "Persistent Increase"    → Signal: Red
2025-12-15  Spread concurrently widened 25bp → Triggered "Volatility + Spread Dual Rise" → Signal: Red (Confirmed)
```

**Framework Judgment:**
Volatility signals provided clear warnings 5 months before the rating downgrade, validating the leading nature of volatility analysis in credit early warning. The quantitative rules for this signal can be directly encoded as inference logic for an AI Agent.

### 3.6 Core Limitations of Volatility Analysis

| Limitation | Explanation | Impact Level |
|------|------|---------|
| **Not applicable to non-listed companies** | No stock price/quotes data; volatility analysis cannot be conducted at all | High — approximately 50% of bond issuers are non-listed companies |
| **Window period selection bias** | Different windows may give conflicting signals | Medium — should output multiple windows simultaneously, prioritize trends over absolute values |
| **Market noise false alarms** | Increased volatility does not necessarily represent credit deterioration — could be sector rotation, liquidity shock | Medium — must be cross-validated with spreads + trading volume |
| **Historical volatility lags behind implied volatility** | HV is a backward-looking statistic; IV is forward-looking | Medium — but IV is unavailable, can only use HV for directional approximation |
| **Correlation convergence in extreme markets** | All volatility rises synchronously during stress periods, reducing differentiation | Low — should switch to multi-factor analysis in such cases |

---

## 4. Multi-Factor Risk Exposure

### 4.1 Factor Decomposition Framework

Under public data constraints, a **simplified linear factor model** is used to decompose the drivers of corporate credit spreads:

```
Target Variable: Enterprise YTM spread (weekly data)
Model Structure:
  Spread_i(t) = α_i + β_macro × F_macro(t) + β_ind × F_ind(t) 
                + β_region × F_region(t) + ε_i(t)
  
  Where:
  ├── F_macro(t) = Macro factors (interest rate level / term spread / credit spread index)
  ├── F_ind(t)   = Industry factor (industry spread mean / industry index return)
  ├── F_region(t)= Regional factor (regional spread mean — applicable only to SOEs/LGFVs)
  ├── α_i        = Idiosyncratic alpha — pricing of enterprise's own credit quality
  ├── β_*        = Exposure coefficients for each factor
  └── ε_i(t)     = Residual — part not explained by factors (model error + idiosyncratic shocks)
```

### 4.2 Simplified Single-Factor Regression (Feasible Approach Under Public Data Constraints)

Due to sparse data on Chinese corporate bonds (especially inactive issues), the feasibility of multi-factor panel data is low. The following is a feasible simplification under **limited data constraints**:

| Factor | Proxy Variable | Data Source | Applicability |
|------|---------|-------|--------|
| **Macro Interest Rate** | 10-year government bond yield (monthly average) | Central Bank (PBOC) / public market data | Universal |
| **Macro Credit** | AAA corporate bond yield curve level | CCDC free disclosure (monthly) | Universal (but CCDC valuation curve has lower precision) |
| **Industry Beta** | Median change in industry spread | Equal-weighted average of industry sample enterprises | Requires ≥3 sample enterprises |
| **Regional Beta** | Regional SOE spread mean (if applicable) | Equal-weighted average of regional sample enterprises | Only for SOEs/LGFVs — private enterprises have no regional beta |
| **Liquidity** | Turnover rate (average daily trading volume / outstanding scale) | Exchange public data | Data sparse for low-liquidity bonds |
| **Idiosyncratic Alpha** | Residual term — alpha from rolling 6-month regression | Model-endogenous | Requires sufficient weekly observations (≥24 weeks) |

**Regression Technical Specification:**

```
Regression Type: Rolling OLS (window = 24 weeks, approximately 6 months)
Frequency: Weekly
Minimum Observations: 12 weeks (do not output factor decomposition if insufficient)
Constraint: Do not calculate industry beta when sample enterprises < 3

Output Format:
  ├── R²: 0.65 (macro + industry factors explain 65% of spread variation)
  ├── β_macro: 0.42 (sensitivity of spread to macro interest rates)
  ├── β_ind: 0.38 (for every 10bp widening in industry spread, individual bond spread widens 3.8bp)
  ├── α: +25bp (positive idiosyncratic alpha — market demands an additional 25bp premium for this enterprise)
  └── Residual standard deviation: 18bp (unexplained part — as a measure of uncertainty)

Model Diagnostics:
  ├── Durbin-Watson statistic: 1.85 (no significant autocorrelation)
  ├── VIF: < 3 (no multicollinearity)
  └── Residual normality test: p > 0.05 (passed)
```


### 4.2.1 Confidence Interval Specification for Factor Regression [Statistical Correction v0.0.1]

**Regression Coefficient Confidence Intervals (Newey-West Robust Standard Errors):**
```
Output format revision for all beta coefficients (replacing original point estimates without confidence intervals):

Old output format:
  β_macro: 0.42 (sensitivity of spread to macro interest rates)
  β_ind: 0.38

New output format (with 95% confidence interval and significance annotation):
  β_macro: 0.42  [95% CI: 0.28–0.56]  ✅ p=0.003 (significant)
  β_ind  : 0.38  [95% CI: 0.22–0.54]  ✅ p=0.012 (significant)
  α      : +25bp [95% CI: -8bp–+58bp] ❌ p=0.124 (not significant)

Calculation Specification:
├── Standard Error Type: Newey-West heteroskedasticity and autocorrelation consistent standard errors (HAC)
├── Lag truncation parameter: auto-selected per Newey-West (1994), or floor(4×(T/100)^(2/9))
├── Confidence Interval: β̂ ± t₀.₀₂₅(df) × SE_HAC
└── Significance Annotation:
    ├── p<0.05 → annotate "✅ p=XX (significant)"
    └── p≥0.05 → annotate "❌ p=XX (not significant)"
```

**Confidence Interval for Regression R²:**
```
R² Confidence Interval (via F-distribution transformation):
├── Method: R² → F-statistic → F-distribution confidence interval → convert back to R² confidence interval
├── Formula: F = (R²/k) / ((1-R²)/(n-k-1))
├── Output: "R²: 0.65 [95% CI: 0.52–0.76]"
└── Prerequisite: n ≥ 30, and residuals approximately normal (otherwise use Bootstrap instead)
```

### 4.2.2 Statistical Precondition Testing Specification [Statistical Correction v0.0.1]

Before conducting factor regression, the following three preconditions must be tested sequentially. If any test fails, processing must follow the prescribed rules before proceeding.

**Test 1: Stationarity Test (ADF)**
```
ADF Test (Augmented Dickey-Fuller):
├── Test Object: All time series — target variable (spread) and all factor variables
├── Null Hypothesis H₀: Series has a unit root (non-stationary)
├── Decision Criteria:
│   ├── p ≤ 0.05 → Reject H₀ → Series is stationary ✅
│   └── p > 0.05 → Cannot reject H₀ → Series is non-stationary ❌
├── Handling Rules:
│   1. Non-stationary series → perform first differencing (ΔX_t = X_t - X_{t-1})
│   2. Re-run ADF test after differencing
│   3. If p ≤ 0.05 after differencing → use differenced series for regression
│   4. If still p > 0.05 after first differencing → annotate "data does not satisfy stationarity assumption", skip this factor
├── Output Format:
│   ├── "Spread series: ADF statistic = -3.82, p=0.004 → Stationary ✅"
│   ├── "Macro factor: ADF statistic = -2.15, p=0.22 → Non-stationary ❌ → p=0.001 after first differencing ✅"
│   └── "Industry factor: ADF p=0.08 after first differencing → Still non-stationary ❌ → Factor unavailable, skipped"
└── Annotation Location: Top of regression output
    "All series have passed ADF stationarity test (or have been differenced)"
```

**Test 2: Heteroskedasticity Test (Breusch-Pagan)**
```
Breusch-Pagan Test:
├── Test Object: Residuals of the regression model
├── Null Hypothesis H₀: Residual variance is constant (homoskedasticity)
├── Decision Criteria:
│   ├── p > 0.05 → Cannot reject H₀ → Homoskedastic ✅ (ordinary standard errors are acceptable)
│   └── p ≤ 0.05 → Reject H₀ → Heteroskedasticity present ❌
├── Handling Rules:
│   ├── If heteroskedasticity present → Must use Newey-West HAC standard errors
│   └── Annotate in regression output: "Using HAC standard errors to correct for heteroskedasticity"
├── Relationship with Beta Confidence Intervals:
│   └── Regardless of Breusch-Pagan result, beta confidence intervals uniformly use Newey-West standard errors
│       (HAC standard errors are consistent under both heteroskedasticity and autocorrelation, do not depend on test result)
└── Output Format:
    "Breusch-Pagan test: BP statistic = 18.5, p=0.002 → Heteroskedasticity present ✅ HAC standard errors used"
```

**Test 3: Multicollinearity Test (VIF)**
```
VIF (Variance Inflation Factor):
├── Test Object: All independent variables (factor variables)
├── Calculation: For each factor, regress it against all other factors; VIF_j = 1/(1-R²_j)
├── Decision Criteria:
│   ├── VIF < 5 → No significant collinearity ✅
│   ├── 5 ≤ VIF < 10 → Moderate collinearity ⚠️
│   │   └── annotate "VIF=XX, moderate collinearity — factor weight has been reduced"
│   └── VIF ≥ 10 → Severe collinearity ❌
│       └── annotate "VIF=XX, severe collinearity — this factor heavily overlaps with another, merged/deleted"
├── Handling Rules:
│   ├── VIF ≥ 10 → identify overlapping factor pairs, merge or delete one, then recalculate VIF
│   ├── Merging method: take the equal-weighted average of two factors as a new factor
│   └── Record the handling process for traceability
├── Output Format:
│   ├── "VIF test: Macro factor=2.8, Industry factor=3.2, Regional factor=1.5 → All <5 ✅"
│   └── "VIF test: Industry factor=8.5 ⚠️ (moderate collinearity, weight reduced)"
└── Annotation Location: Regression diagnostics section
```

**Integrated Output Specification for the Three Tests:**
```
Statistical Precondition Test Report:
├── ADF Stationarity Test: All series have passed (or passed after differencing) ✅
├── Breusch-Pagan Heteroskedasticity Test: BP=18.5, p=0.002 → Heteroskedasticity present
│   └── Handling: Newey-West HAC standard errors used
└── VIF Multicollinearity Test: Maximum VIF=3.2 → No significant collinearity ✅
```

### 4.3 Time-Varying Characteristics of Factor Exposure

Factor exposure is not static — when market conditions change or enterprise fundamentals shift, factor betas drift. Detection rules are as follows:

| Signal | Detection Method | Meaning |
|------|---------|------|
| **β_macro Rising** | 24-week rolling beta + trend regression | Enterprise pricing increasingly driven by macro factors — credit quality drifting toward macro-sensitive type |
| **β_ind Declining** | Same as above | Market no longer pricing by industry label — idiosyncratic risk becoming prominent |
| **α Turning from Negative to Positive** | Alpha window breaching ±2σ | Market starting to demand additional premium from the enterprise — credit perception deteriorating |
| **Residual Standard Deviation Expanding** | Rolling 24-week residual sigma trending up | Model explanatory power declining — factors exist that the framework has not captured (hidden risks) |
| **R² Sharply Declining** | Weekly R² dropping from >0.6 to <0.3 | Pricing logic has undergone structural change — factor model needs reset |

**Rule Application:** When time-varying signals are detected, the AI Agent should output in the following format:

```
Factor Model Stability Warning:
├── Detected: β_macro increased from 0.35 to 0.52 (+49%) over the last 12 weeks
├── Implication: Enterprise pricing shifting from "industry-driven" to "macro-driven"
├── Possible Cause: Industry beta is breaking down — the market no longer prices the enterprise as "one of the industry"
├── Suggestion: Check for enterprise-specific risks (financial deterioration / governance issues / potential rating downgrade)
└── Confidence: Medium (24-week window is relatively short, time-varying detection may have lag)
```

### 4.4 Example: Factor Decomposition of Solar PV Enterprise Credit Spreads

**Analysis Subject:** LONGi Green Energy (601012) vs JA Solar Technology (002459)
**Analysis Date:** 2026-07-01
**Data Window:** 2026-01 to 2026-06 (26 weeks)
**Data Source:** Exchange public quotes + CCDC free data

| Factor | LONGi Green Energy | JA Solar Technology | Industry Average | Interpretation |
|------|---------|---------|---------|------|
| β_macro | 0.38 | 0.52 | 0.45 | JA is more sensitive to macro interest rates — higher debt ratio leads to greater duration exposure |
| β_ind | 0.45 | 0.32 | 0.40 | LONGi is still priced as "industry leader"; JA's declining industry beta indicates the market is differentiating pricing |
| α | -15bp | +42bp | 0bp | LONGi receives a market premium (negative alpha means below-industry spread); JA demands an additional 42bp — reflecting earnings decline and debt ratio concerns |
| R² | 0.72 | 0.58 | 0.65 | Factor model explains LONGi better — JA has idiosyncratic factors not captured by the model |
| Residual σ | 12bp | 22bp | 15bp | JA's pricing uncertainty is higher — information asymmetry or insufficient liquidity |

**Timeline: Factor Drift Detection (JA Solar Technology)**

| Month | β_macro | β_ind | α(bp) | Signal |
|------|---------|-------|-------|------|
| 2026-01 | 0.48 | 0.38 | +18 | Baseline |
| 2026-02 | 0.46 | 0.37 | +22 | Stable |
| 2026-03 | 0.50 | 0.35 | +28 | Alpha uptrend initiated |
| 2026-04 | 0.51 | 0.33 | +35 | Alpha breached +2σ threshold |
| 2026-05 | 0.53 | 0.31 | +40 | β_ind continuously declining — industry beta weakening |
| 2026-06 | 0.52 | 0.32 | +42 | Confirmed: pricing logic shifting from "industry-driven" to "macro + idiosyncratic driven" |

**Conclusions:**
- JA Solar Technology's factor model underwent structural change from January to June 2026: declining industry beta, rising alpha, expanding residual sigma
- Signals collectively point to: **the market is implementing "de-industry-labeling" pricing for JA Solar** — JA is no longer uniformly priced as a "solar PV enterprise" but is individually priced as a "risky solar PV enterprise"
- This signal preceded the actual rating adjustment (as of the analysis date, JA's rating remained AA/stable)

**Data Quality Annotations:**
- Regression based on weekly data (26 observations), statistical power is limited
- Z-spread unavailable, using YTM spread as target variable — spreads of option-embedded vs non-option-embedded bonds are not comparable
- Industry factor average based on 5 sample enterprises — stability will improve with sample expansion

### 4.5 Applicable Conditions and Boundaries of Factor Analysis

| Condition | Requirement | Handling When Not Met |
|------|------|--------------|
| Minimum observations | ≥12 weeks (weekly data) | Annotate "insufficient observations, factor decomposition unreliable" |
| Minimum sample enterprises (industry beta) | ≥3 enterprises in same industry | Skip industry beta calculation, output only macro beta and alpha |
| Bond activity | Weeks with trading ≥ 50% of total weeks | For inactive bonds, spread data may be distorted — annotate low quality |
| Same-bond duration stability | Remaining maturity should not change significantly during analysis period | Bonds approaching maturity have abnormal spread behavior — exclude or analyze separately |
| Non-option-embedded preference | YTM volatility of option-embedded bonds affected by option value | Handle option-embedded bonds separately — or exclude (prioritize plain bonds/MTNs) |

---

## 5. Correlation Analysis

### 5.1 Correlation Indicator Definitions

| Indicator | Definition | Calculation Method | Signal Meaning |
|------|------|---------|---------|
| **Spread Correlation ρ** | Correlation of weekly YTM spread changes between two enterprises | Pearson correlation coefficient (window = 24 weeks) | Degree of co-movement |
| **Tail Correlation** | Probability of co-directional change under extreme conditions | Proportion of co-decline when below the 5th percentile | Linkage under stress scenarios |
| **Cross-sectional σ** | Cross-sectional standard deviation of industry spreads | Weekly standard deviation of all individual bond spreads within an industry | Degree of intra-industry divergence |
| **Correlation Heatmap** | Matrix displaying all pairwise ρ values | N × N matrix | Systemic risk structure |

### 5.2 Intra-Industry Enterprise Spread Correlation Matrix

**Purpose:** Determine whether credit spreads of enterprises within the same industry move synchronously — high correlation indicates industry systemic risk dominance; low correlation indicates enterprise-specific risk dominance.

**Example: Correlation Matrix of 5 Solar PV Convertible Bond Spreads (2026-01 to 2026-06)**

| Correlation ρ | LONGi 22 CB | Tongwei 22 CB | Trina 23 CB | Jinko CB | JA Solar CB |
|-----------|---------|---------|---------|---------|---------|
| **LONGi 22 CB** | 1.00 | 0.62 | 0.55 | 0.48 | 0.35 |
| **Tongwei 22 CB** | 0.62 | 1.00 | 0.72 | 0.61 | 0.52 |
| **Trina 23 CB** | 0.55 | 0.72 | 1.00 | 0.68 | 0.58 |
| **Jinko CB** | 0.48 | 0.61 | 0.68 | 1.00 | 0.65 |
| **JA Solar CB** | 0.35 | 0.52 | 0.58 | 0.65 | 1.00 |

**Analysis:**
- Industry average ρ = 0.576 (moderate correlation — not fully synchronous within the industry)
- LONGi and JA Solar have the lowest spread correlation (ρ=0.35) — the two extremes of pricing have the lowest correlation
- Tongwei and Trina have the highest correlation (ρ=0.72) — both AA-rated, loss-making enterprises, spreads move in sync
- Cross-sectional standard deviation σ_cross expanded from 35bp to 62bp over 6 months — intra-industry divergence intensifying

**Conclusion:** The solar PV industry is **no longer "in the same boat"** — the credit pricing of different enterprises is diverging, and industry systemic risk is being replaced by individual risk. Industry beta is declining.

### 5.3 Cross-Industry Default Correlation (Jump Under Stress)

Cross-industry default correlation is typically low in normal periods but rises sharply during systemic stress — this is a quantitative signal of "risk diversification failure."

| Stress Event | Cross-Industry Correlation Change | Jump Magnitude | Recovery Time |
|---------|----------------|---------|---------|
| 2020-11 Yongcheng Coal Default | Coal → Steel → Chemical → Construction | ρ rose from 0.3 to 0.7+ | Approximately 6 months |
| 2024-05 Real Estate Shock | Real Estate → Banking → LGFV → Construction | ρ rose from 0.4 to 0.8+ | Still ongoing (as of 2026) |
| 2018-10 Private Enterprise Default Wave | Inter-private enterprise correlation rose from 0.2 to 0.6 | Private enterprises as a whole were "re-labeled" | Approximately 12 months |

**Detection Rules:**

```
Cross-Industry Correlation Jump Detection:
  1. Select samples spanning 5 industries (≥3 bond issuers per industry)
  2. Calculate correlation matrix between industry-mean spreads (window = 12 weeks, rolling)
  3. Detect weekly change in average cross-industry ρ
  4. Trigger thresholds:
     ├── Normal: cross-industry average ρ < 0.4
     ├── Warning: cross-industry average ρ > 0.5 and rising trend lasting 4 weeks
     └── Crisis: cross-industry average ρ > 0.7 (systemic risk transmission)

Output Format:
  Cross-industry average correlation: 0.38 (+0.05 vs 4 weeks ago)
  Highest-correlation industry pair: Coal-Steel (ρ=0.55) — energy industry chain linkage
  Fastest-rising correlation industry pair: Real Estate-Banking (ρ from 0.42 to 0.51) — watch credit transmission
  Status: Yellow Mild increase — systemic risk slowly accumulating
```

### 5.4 Regional Correlation: Yongcheng Coal Default Case Study

**Event:** 2020-11-10, Yongcheng Coal & Electricity Holding Group default
**Transmission Path:** Yongcheng Coal default → Coal credit spreads widen → Henan SOE spreads widen → Shanxi/Hebei SOE spreads widen → Weak SOEs broad-based widening

**Quantitative Analysis:**

| Time | Henan Province SOE Spread Mean | Shanxi Province SOE Spread Mean | Hebei Province SOE Spread Mean | Full Market SOE Spread Mean |
|------|-----------------|-----------------|-----------------|-----------------|
| 2020-11-01 (Pre-default) | 125bp | 110bp | 118bp | 105bp |
| 2020-11-10 (Default date) | 142bp | 118bp | 122bp | 112bp |
| 2020-11-17 (Default + 1 week) | **285bp** | **195bp** | **188bp** | **165bp** |
| 2020-12-01 (Default + 3 weeks) | 242bp | 172bp | 165bp | 148bp |
| 2021-02-01 (Default + 3 months) | 158bp | 132bp | 135bp | 118bp |

**Correlation Changes:**

| Period | Henan-Shanxi (ρ) | Henan-Hebei (ρ) | National SOE Cross-sectional σ | Signal |
|------|------------|------------|-------------|------|
| 12 weeks pre-default | 0.25 | 0.28 | 22bp | Low correlation — normal regional divergence |
| 4 weeks post-default | **0.72** | **0.68** | **58bp** | High correlation — market treats "weak SOEs" as a whole |
| 12 weeks post-default | 0.45 | 0.42 | 35bp | Regressing — but not back to pre-default level |

**Rule:** A jump in regional spread correlation after a stress event is **quantitative evidence of systemic risk transmission**. When spreads of non-related regions are observed widening synchronously, systemic risk is spreading.

### 5.5 Correlation Jump as Systemic Risk Warning

| Warning Type | Detection Condition | Signal Level | Suggested Action |
|---------|---------|---------|---------|
| **Intra-Industry Correlation Surge** | ρ jumps from <0.4 to >0.7 (Δ>0.3, period ≤4 weeks) | Red Systemic | Industry systemic risk exposure — all enterprises treated "equally" |
| **Cross-Industry Correlation Breaching Threshold** | Cross-industry average ρ rises from <0.4 to >0.6 | Red Systemic | Risk transmitting across industries — portfolio diversification failing |
| **Cross-sectional Standard Deviation Compression** | Industry σ_cross drops from >60bp to <30bp | Orange Attention | Market no longer distinguishing good/bad enterprises — pricing signals distorted |
| **Regional Labeling** | Non-event region spreads follow event region spreads synchronously widening | Red Systemic | Market is labeling by "region + ownership" — fundamental analysis broken |
| **Tail Correlation Rising** | Co-decline proportion at the 5th percentile rises from <20% to >40% | Red Systemic | "Everything falls together" under extreme conditions — tail risk concentrated |

**AI Agent Inference Rules (Correlation Module):**

```
Input: Industry selection + time window
1. Pull sample enterprise spread time series
2. Calculate correlation matrix (window = 24 weeks, rolling step = 1 week)
3. Detection rules:
   a) Weekly change in mean_ρ > 0.1 and rising for 4 consecutive weeks → Warning
   b) Any ρ jump > 0.3 (single week) → Check for stress event
   c) σ_cross < 30bp and mean_ρ > 0.6 → Labeling risk
4. Output: Correlation status + topological structure + trend + suggestion
```

---


### 5.5.1 Confidence Interval Specification for Correlation Statistics [Statistical Correction v0.0.1]

**Confidence Interval for Pearson Correlation Coefficient (Fisher Z Transformation):**
```
Fisher Z Transformation to calculate the 95% confidence interval for the correlation coefficient:
├── Step 1: Convert Pearson r to Fisher Z
│   Z = 0.5 × ln((1+r)/(1-r))
├── Step 2: Standard error of Z
│   SE_Z = 1 / √(n-3)
│   where n = number of observations in the window (e.g., 24 weeks)
├── Step 3: 95% confidence interval for Z
│   CI_Z = [Z - 1.96 × SE_Z,  Z + 1.96 × SE_Z]
├── Step 4: Convert CI_Z back to the correlation coefficient scale
│   CI_r = [(e^(2×CI_Z_low)-1)/(e^(2×CI_Z_low)+1),
│           (e^(2×CI_Z_high)-1)/(e^(2×CI_Z_high)+1)]

Calculation Example (r=0.62, n=24):
  Z = 0.5 × ln((1+0.62)/(1-0.62)) = 0.5 × ln(4.263) = 0.725
  SE_Z = 1 / √(21) = 0.218
  CI_Z = [0.725 - 1.96×0.218,  0.725 + 1.96×0.218] = [0.298, 1.152]
  CI_r = [0.290, 0.818]

Output: "ρ = 0.62 [95% CI: 0.29–0.82], n=24"
```

**Correlation Jump Detection Rules Revision:**
```
Old rule: Weekly change in mean_ρ > 0.1 and rising for 4 consecutive weeks → Warning
New rule: Absolute difference between current correlation and rolling window correlation > 2 × SE_Fisher
        → Mark as correlation jump
        → Where SE_Fisher = √(1/(n₁-3) + 1/(n₂-3)) (combined standard error of the two windows)

Output Format Revision:
  Old: mean_ρ = 0.38 (+0.05 vs 4 weeks ago)
  New: mean_ρ = 0.38 [95% CI: 0.25–0.51] (Δ=+0.05, |Δ| < 2×SE=0.12 → Not reaching jump threshold ✅)
```

**Confidence Interval Annotation for Correlation Matrix:**
```
Each ρ value in the correlation matrix should be accompanied by a confidence interval:
  LONGi 22 - Tongwei 22: ρ=0.62 [95% CI: 0.29–0.82]  n=24
  Tongwei 22 - Trina 23: ρ=0.72 [95% CI: 0.44–0.88]  n=24
  LONGi 22 - JA Solar: ρ=0.35 [95% CI: -0.07–0.66] n=24 ← CI spans 0, not significant

Annotation Rules:
├── CI does not include 0 → annotate "Significant correlation ✅"
└── CI includes 0 → annotate "Not significant — may be sampling error ❌"
```

**Preconditions:**
- n ≥ 10 (minimum sample size requirement, otherwise Fisher Z transformation is unstable)
- When n < 10, annotate "sample size insufficient, correlation estimate unreliable — directional reference only"

## 6. Stress Testing and Scenario Analysis

### 6.1 Stress Testing Methodology Overview

| Stress Test Type | Definition | Data Requirements | Engine Feasibility |
|------------|------|---------|-----------|
| **Single-Factor Sensitivity** | Impact of a single risk factor change on bond value | Low — duration approximation is sufficient | ✅ Fully feasible |
| **Multi-Factor Scenario** | Multiple factors changing simultaneously (historical replay / hypothetical) | Medium — requires correlation matrix | ⚠️ Partially feasible (simplified as weighting) |
| **Tail Risk** | Loss distribution under extreme scenarios | High — requires Monte Carlo simulation or extreme value theory | ❌ Not feasible (simulation depends on professional terminals) |
| **Reverse Stress Testing** | "What scenario would lead to default?" | Medium — requires enterprise financial structure | ✅ Basically feasible (using financial ratios) |

### 6.2 Single-Factor Sensitivity Analysis

Under the constraint of being unable to obtain modified duration and convexity, **approximate duration** is used:

```
Approximate Duration Calculation (MacCaulay Duration):
  D_mac = Σ(t × CF_t / (1+YTM)^t) / Bond_Price
  
Simplified version (for fixed-rate, non-option-embedded, non-zero-coupon):
  D_approx ≈ Remaining years / (1 + YTM)
  
Price Change Approximation:
  ΔP / P ≈ -D_approx × ΔYTM

Example:
  Bond: 3-year MTN, YTM=3.5%
  D_approx ≈ 3 / (1.035) = 2.90
  If yield rises 100bp → Price change ≈ -2.90 × 1% = -2.90%
```

**Single-Factor Sensitivity Template:**

```
Stress Factor: Risk-free rate increases 100bp / 200bp
Applicable Sensitive Bonds: All fixed-rate non-option-embedded plain bonds
Analysis Objective: Impact of interest rate increase on bond market value

| Bond | Remaining Maturity (Years) | YTM (%) | Approx Duration | Rate +100bp Impact | Rate +200bp Impact |
|------|------------|--------|---------|--------------|--------------|
| Bond A | 2.0 | 2.80 | 1.95 | -1.95% | -3.90% |
| Bond B | 3.5 | 3.20 | 3.39 | -3.39% | -6.78% |
| Bond C | 5.0 | 3.80 | 4.81 | -4.81% | -9.62% |

Limitations Annotated:
  1. The above is a linear approximation, without convexity correction — the larger the rate change, the larger the error
  2. Option-embedded features are not considered — convertible bonds cannot use this method
  3. Duration of option-embedded bonds is adjusted by the option — actual sensitivity is lower than the approximation
```

**Supported Sensitivity Factors (by priority):**

| Factor | Standard Shock Magnitude | Analysis Method | Data Availability |
|------|------------|---------|-----------|
| Risk-free rate parallel shift | +50bp / +100bp / +200bp | Duration approximation | ✅ |
| Credit spread widening | +50bp / +100bp / +200bp | Duration approximation | ✅ |
| Rating downgrade (1-2 notches) | Depends on historical migration matrix | Spread model | ⚠️ Requires rating migration data |
| Liquidity shock | Trading volume shrinks to 10% | Qualitative — cannot quantify into precise loss | ❌ Cannot quantify |

### 6.3 Multi-Factor Scenario Analysis

Under the constraint of being unable to implement Monte Carlo simulation, the **scenario weighting method** is used:

```
Method: Calculate impact independently for each factor, assuming independence between factors (simplifying assumption)
Formula: ΔP_total = Σ(ΔP_i × S_i)
  where ΔP_i = price change under the shock of factor i
        S_i = probability of that factor occurring in the scenario (0-1)

Deficiency: Ignores factor correlation — under stress scenarios, factor correlation systematically increases
       → Annotate: "Independence assumption may underestimate total impact, error approximately 10-20%"
```

**Standard Scenario Template:**

| Scenario Name | Risk-Free Rate | Credit Spread | Rating | Liquidity | Estimated Statistical Probability |
|---------|-----------|---------|------|--------|--------------|
| **Mild Stress** | +50bp | +50bp | Stable | Normal | Historical probability approx. 20% |
| **Moderate Stress** | +100bp | +100bp | Negative outlook / 1-notch downgrade | Trading volume halved | Historical probability approx. 10% |
| **Severe Stress** | +200bp | +200bp | 2-notch downgrade | Trading highly inactive | Historical probability approx. 3% |
| **Extreme Tail** | +300bp | +400bp | Multi-notch downgrade to CCC | Liquidity dried up | Historical probability approx. 1% |

**Quantitative Estimation for Multi-Factor Scenario Combinations:**

```
Take a 3-year MTN (YTM=3.5%, Approx Duration=2.90) as an example:

| Scenario | Rate Shock | Spread Shock | Total YTM Shock | Estimated Price Impact |
|------|---------|---------|----------|------------|
| Mild Stress | +50bp | +50bp | +100bp | -2.90% |
| Moderate Stress | +100bp | +100bp | +200bp | -5.80% |
| Severe Stress | +200bp | +200bp | +400bp | -11.60% |
| Extreme Tail | +300bp | +400bp | +700bp | -20.30% |

Limitations:
  1. The independence assumption for rates + spreads does not hold under stress — actual impact may be larger
  2. Convexity not considered — convexity provides protection during large rate changes | Directionally correct but magnitude biased
  3. Counterparty risk, margin calls, and other non-linear effects not considered
```

### 6.4 Tail Risk Scenario Construction

The goal of tail risk scenarios is not "prediction," but **exposing the portfolio's vulnerability to specific extreme events**. In quantitative credit analysis, tail risk is constructed through the following 3 methods:

| Construction Method | Description | Example | Feasibility |
|---------|------|------|-------|
| **Historical Replay** | Select the most severe credit shock events from history | "2015 stock market crash + bond market crash" / "2020 Yongcheng Coal shock" | ✅ High (data available) |
| **Hypothetical Worst Case** | The worst imaginable situation for this enterprise | "Core client bankruptcy + refinancing freeze + rating downgrade to D" | ✅ High (depends on industry judgment) |
| **Stress Factor Superposition** | Multiple low-probability factors occurring simultaneously | "Rates 200bp + Spreads 400bp + Stock price down 50%" | ⚠️ Medium (factor correlation unknown) |

**Tail Risk Scenario Documentation Specification:**

```
Scenario Name: [Scenario name — concise description of core risk]
Scenario Type: [Historical Replay / Hypothetical / Factor Superposition]
Construction Basis: [Why this scenario is reasonable — based on history or industry logic]

Factor Settings:
├── Factor 1: [Name] → [Shock Magnitude] — [Basis]
├── Factor 2: [Name] → [Shock Magnitude] — [Basis]
└── Factor 3: [Name] → [Shock Magnitude] — [Basis]

Exposed Exposure:
├── Bond A: [Impact description]
├── Bond B: [Impact description]
└── Portfolio Total Impact: [%]

Trigger Conditions (what would trigger this scenario):
├── Observable leading signal 1
├── Observable leading signal 2
└── Observable leading signal 3

Historical Reference Events: List if there are similar historical events
```

### 6.5 Example: Loss Estimation for Brilliance China Auto Under Three Scenarios

**Analysis Subject:** 17 Huaqi 05 (corporate bond issued by Brilliance China Auto Group Holding Co., Ltd.)
**Analysis Date:** 2018-12-31 (T-22 months — retrospective verification case)
**Data Source:** 2018 annual report + public market data

**Basic Bond Information:**
- Bond Type: Corporate bond (unsecured)
- Issuance Amount: CNY 1 billion
- Term: 3+2 years (option-embedded — issuer's right to adjust coupon rate + investor's right to put)
- Interest Start Date: 2017-11
- Current YTM (2018-12-31): approximately 7.5%
- Approximate Duration (simplified option-embedded handling): approximately 2.5 years

**Special Annotation for Option-Embedded Bonds in Output:**
> Note: Duration and spread analysis precision for option-embedded bonds is lower than for plain bonds. The following analysis is based on a "assuming no exercise" plain bond framework; actual risk exposure may be less than estimated (because investors have the right to put).

**Loss Estimates for Three Scenarios:**

| Scenario | Description | Core Trigger Logic | YTM Shock | Price Impact | Put Likelihood | Comprehensive Rating |
|------|------|------------|---------|---------|-----------|---------|
| **Scenario 1: Mild Scenario** | Rate increase 50bp + industry spread widening 50bp | Monetary policy normalization + auto industry cyclical downturn | 7.5% → 8.5% | -2.5% (approx. -2.5M per 100M) | Low | A |
| **Scenario 2: BMW Spin-off Scenario** | BMW confirmed stake increase + parent company credit independent assessment | 2018-10-11 BMW already announced stake increase plan | 7.5% → 12.0% | -10.8% (approx. -10.8M per 100M) | Medium — put right is protection | CCC |
| **Scenario 3: Default Scenario** | Parent company default — recovery rate 40% (assumed) | Core asset spin-off completed + refinancing frozen | Recovery rate scenario | -60% (approx. -60M per 100M) | High | D |

**Detailed Construction of Scenario 2:**

```
Scenario Name: Credit Repricing of Parent Company After BMW Spin-off
Scenario Type: Hypothetical (based on 2018-10-11 announcement)
Construction Basis: BMW's announcement to increase its stake in BMW Brilliance to 75% has been released —
          once the transaction is completed, BMW Brilliance will no longer be consolidated,
          and the parent company loses its core cash flow source

Factor Settings:
├── Risk-free rate: +50bp (monetary policy normalization assumption)
├── Credit spread: +400bp (risk repricing after core asset spin-off)
│   ├── Basis: Tracking rating agency maintained AAA/stable after BMW Brilliance announcement
│   ├── But the market had already begun repricing — Brilliance China (01114.HK) stock price had fallen 24.54%
│   └── Parallel case: China Hongqiao (01378.HK) credit spread widened approximately 350bp after being shorted
├── Stock price scenario: Brilliance China continued to fall — further weakening the parent company's refinancing ability
└── Rating scenario: Expected rating downgrade to BB or lower within 1-2 years (actual: default after 22 months)

Exposed Exposure:
├── 17 Huaqi 05 (1 billion): -10.8% (if put before default, losses significantly reduced)
├── Other outstanding bonds of the parent company: similar impact
└── Portfolio total impact: depends on holdings

Trigger Condition Monitoring:
├── Progress of BMW stake increase (most critical — completed in 2022, real-world timeline)
├── Parent company's separate financial statements continued to deteriorate (requires quarterly tracking)
├── Refinancing encountering obstacles (new bond issuance failed or rates rose significantly)
└── Stock price continued to fall (Brilliance China's stock performance is a leading indicator)
```

**Retrospective Verification (Actual Results):**

| Prediction | Actual Result | Deviation |
|------|---------|------|
| Parent company risk exposure after BMW spin-off | First default in 2020-10 — accurate | Time-wise 22 months |
| Rating would be downgraded | AAA to BB after default — accurate | But rating severely lagged |
| Recovery rate ~40% | Bankruptcy reorganization, unsecured creditor recovery rate approx. 30-40% | Basically accurate |
| Scenario 2 YTM=12% | Actual YTM on secondary market before default reached 20%+ | Underestimated panic level — liquidity premium not fully accounted for |

**Lessons from Scenario Analysis:**
1. Scenario analysis can **identify risk direction**, but typically **underestimates non-linear amplification under extreme conditions**
2. The absence of liquidity premiums is the largest systematic underestimation factor in scenario analysis
3. The put right on option-embedded bonds is an important risk mitigation tool — but cannot assume the counterparty will be able to exercise it
4. Correlation jumps under stress (all bonds falling together) cannot be captured through single-bond scenario analysis

### 6.6 Hard Constraints of Stress Testing

| Constraint | Impact | Handling Method |
|------|------|---------|
| No precise pricing model for convertible bonds + option-embedded bonds | Larger error in stress testing for option-embedded bonds | Annotate as "option-embedded bond approximation" — recommend analyzing only the plain bond portion |
| No CDS/CRMW market data | Cannot test hedge effectiveness | Annotate "CDS products absent in China market — hedging not feasible" |
| No Bid-ask spread | Liquidity shocks cannot be precisely quantified | Use trading volume shrinkage percentage as approximation — annotate "approximate estimate" |
| No full-market portfolio data | Cannot compute portfolio-level VaR/ES | Limit to single-bond/single-enterprise level stress testing |
| Cannot simulate non-linear derivative effects | Option clauses (put/call) can only be qualitatively analyzed | Annotate "option-embedded bonds require professional terminal for precise pricing" |

---

## 7. Market Implied Signal Extraction

### 7.1 Signal Framework Overview

Market implied signals are credit clues extracted from the **price behavior of non-credit-bond assets**. Although these signals do not come directly from credit spreads, they are an important complement to Track B in a public data environment.

```
Signal Source Matrix:
  ┌─────────────────────────────────────────────────┐
  │                 Asset Type                        │
  │       Bond    │   Stock    │  Convertible  │ Fund Flow│
  ├──┼──────────┼──────────┼───────────┼─────────┤
  │Cr│ YTM Spread│ Beta Change │ Bond Floor    │ Northbound│
  │ed│ Z-spread  │ Volatility  │ Pure Bond Prem│ Financing │
  │it│ Turnover  │ Cum Return  │ Conv Premium  │ Intra-ind │
  │Si│ Issue Rate│ Abnormal Trd│ Option Value  │ Affiliat │
  │gn│           │             │               │           │
  └──┴──────────┴──────────┴───────────┴─────────┘
```

### 7.2 Convertible Bond Conversion Premium → Credit Concerns

The conversion premium of convertible bonds measures not only option value but also implies credit information:

**Core Logic:** When the market becomes concerned about the issuer's credit quality, the "bond floor protection" value of convertible bonds rises, pushing the conversion premium higher — even if the stock price is unchanged, the discount on the plain bond portion causes the conversion premium to expand.

| Conversion Premium Range | General Meaning | Interpretation in Credit Analysis |
|---------------|---------|-------------------|
| 0-20% | Deep in-the-money — close to conversion | Low credit risk — market willing to convert |
| 20-40% | Mildly out-of-the-money — normal range | Normal credit pricing |
| 40-60% | Moderately out-of-the-money — watch signal | Bond floor discount exists — market has implicit credit concerns |
| **60-80%** | **Highly out-of-the-money — needs investigation** | **Credit risk premium is starting to dominate pricing — plain bond portion already discounted** |
| >80% | Extremely out-of-the-money — strong signal | Almost no conversion possibility — bond priced at default risk |

**Limitations Annotated:**
- Conversion premium is affected by multiple factors: underlying stock price, remaining maturity, volatility, interest rate levels — a high premium is not always a credit issue
- Quality of bond floor protection (put clauses) varies greatly across convertible bonds — requires case-by-case analysis of protection clauses
- When analyzing credit signals from convertible bonds, the underlying stock price trend must also be examined to exclude interference from "anomalous premium caused solely by a large stock price increase"

### 7.3 Example: LONGi 22 CB Premium 74%

**Analysis Date:** 2026-07-01
**Data:** LONGi 22 CB price 105.80 CNY, LONGi Green Energy stock price 18.23 CNY, conversion price 19.85 CNY, YTM=0.52%

| Indicator | Value | Meaning |
|------|------|------|
| Conversion Value | 18.23 / 19.85 × 100 = 91.84 CNY | Conversion loss of approximately 8.16 CNY per bond |
| Conversion Premium | (105.80 - 91.84) / 91.84 = **15.2%** | Actual calculated value — lower than market perception |
| **Pure Bond Value** | Discounting future cash flows at 3.5% discount rate ≈ 92.5 CNY | |
| **Pure Bond Premium** | (105.80 - 92.5) / 92.5 = **14.4%** | Trading above bond floor — has some safety cushion |
| **Market-Reported Conversion Premium** | Typically calculated as **74%** | Note: this value is calculated based on **face value of 100 CNY**, not conversion value |

**Important Clarification (Data Misuse Risk):**

> **Key Finding:** The commonly used conversion premium in the market (e.g., 74%) is a simplified calculation based on face value of 100 CNY rather than conversion value. In credit analysis, the **conversion value premium** = (CB price - conversion value) / conversion value should be used. LONGi 22's actual conversion premium is 15.2%, suggesting limited credit concerns. The 74% figure is an industry convention quoting indicator and does not directly reflect credit risk.

**Credit Signals Extracted from LONGi 22 CB:**

| Signal | Value | Credit Meaning | Signal Direction |
|------|------|---------|---------|
| Conversion Value Premium | 15.2% | Fairly neutral — market pricing close to conversion value | Normal |
| Pure Bond Premium | 14.4% | Bond floor has some protection — not default concern | Positive |
| YTM | 0.52% (significantly lower than same-rating credit bonds ~3.5%) | Market has confidence in LONGi's credit quality | Positive |
| Bond Floor Discount | 105.80 vs pure bond value 92.5 | Premium trading — plain bond portion not discounted | Positive |

**Conclusion:** LONGi 22 CB's credit signals are generally positive — the market perceives LONGi's credit risk as low. The 74% premium (calculated on face value) is a **calculation basis difference** and should not be misinterpreted as a credit concern.

**Inference Annotation for AI Agents:**
> When processing convertible bond conversion premiums, a distinction must be made between "face-value-based premium" and "conversion-value-based premium" — the former is used for trading scenarios, the latter for credit analysis. Using face-value premium for credit judgment produces misleading conclusions.

### 7.4 Issuance Rate Changes → Market Repricing

The issuance rate of newly issued bonds is the **most real-time, cleanest pricing signal** of the market's view of the issuer's credit — because it is not affected by secondary market liquidity.

| Signal Type | Detection Rule | Credit Meaning |
|---------|---------|---------|
| **Same-issuer new issuance rate jump** | New issue rate > previous issue + 50bp (same maturity) | Market's credit assessment of the issuer deteriorating |
| **Issuance rate vs market valuation** | Issue rate > CCDC valuation + 20bp | Primary market more pessimistic than secondary market — watch |
| **Issuance failure/cancellation** | Announcement of cancellation or postponement | Severe signal — market does not accept current pricing |
| **Issuance rate crossing rating lines** | New issue rate > market average for lower 1-2 rating tiers | Market believes actual credit quality is below nominal rating |
| **Same-industry new issuance rate trend** | Industry average new issuance rate rising consecutively | Entire industry bearing higher financing costs |

**Example: Tongwei Co. Short-term Bill Issuance Rate Changes (2025-2026)**

| Issue Date | Type | Term | Issue Rate | Change vs Previous | Signal |
|---------|------|------|---------|-----------|------|
| 2025-03 | Short-term bill | 270 days | 2.60% | — | Baseline |
| 2025-06 | Short-term bill | 270 days | 2.30% | -30bp | Spread compression — monetary easing |
| 2025-09 | Short-term bill | 270 days | 2.02% | -28bp | Continued compression |
| 2026-01 | Short-term bill | 270 days | 2.15% | **+13bp** | Orange **Turning point — trend reversal** |
| 2026-04 | Short-term bill | 270 days | 2.45% | +30bp | Orange **Continued widening — trend confirmed** |

**Analysis:** The continuous decline in rates during 2025 reflected the monetary easing environment (market-wide rate decline). However, the turning point in January 2026 (+13bp) cannot be explained by macro interest rates — money market rates were stable in early 2026. This indicates **credit premium is rising independently** — even with the AAA rating maintained, the market has begun repricing Tongwei's credit risk.

### 7.5 Persistent Stock Price Decline + Volatility Amplification → Leading the Bond Market

The stock market is more sensitive to credit quality changes than the bond market — reasons: higher liquidity, more diverse trader types, faster information transmission.

**Detection Rules:**

```
Signal Combination: Persistent stock price decline + volatility amplification
Detection Conditions:
  1. Stock price: cumulative decline > 20% over the past 60 trading days
  2. Volatility: HV_20d > HV_60d and HV_60d above the historical 80th percentile
  3. Trading volume: average daily volume > historical average (exclude false signals from liquidity drain)
  4. Orange All conditions met → Credit warning signal

Signal Meaning:
  ├── The equity market is already "voting with its feet" reflecting credit concerns
  ├── The bond market typically lags by 2-6 weeks (for targeted information) or 6-12 weeks (for systemic information)
  └── Signal strength increases with the number of conditions met

Cross-Validation:
  ├── Check concurrent: rating actions / earnings warnings / refinancing events
  ├── Intra-industry comparison: whether other enterprises in the same industry are also declining → exclude industry-wide systemic decline
  └── Fundamental confirmation: whether Track A supports the "credit deterioration" judgment
```

**Validation Case: Brilliance China Auto (After 2018-10-11 Announcement)**

| Signal | Value | Credit Meaning |
|------|------|---------|
| Brilliance China (01114) single-day decline | -24.54% | Extremely negative — core asset value impaired |
| Cumulative decline 1 month after announcement | -35% | Decline persisted — market confidence not restored |
| HV_20d (pre-announcement) | 28% | Normal volatility |
| HV_20d (post-announcement) | 65% | More than doubled — uncertainty surged |
| Bond market reaction (within 2 weeks) | Spread widened approximately 35bp | **Bond market reaction was lagging and muted — stock market led by approximately 8-12 weeks** |

### 7.6 Northbound Capital Flow / Margin Balance → Institutional Sentiment

| Signal | Data Source | Availability | Indication for Credit Analysis |
|------|-------|--------|-----------------|
| **Northbound Capital (Stock Connect) holdings change** | HKEX daily disclosure | ✅ Free | Foreign institutions' ongoing attitude toward the stock — indirectly reflects views on credit quality |
| **Margin balance change** | Exchange daily disclosure | ✅ Free | Risk appetite of leveraged investors — rapid withdrawal may be a warning |
| **Block trade premium/discount** | Exchange disclosure | ⚠️ Partially free | Large trader's judgment of fair value — but typically viewed as institutional rebalancing |
| **Major shareholder pledge ratio change** | Corporate announcements | ✅ Public | Major shareholder funding tightness — associated risk at the company level |

**Method for Using Northbound Capital Flow in Credit Analysis:**

```
Signal Extraction:
  1. Obtain Stock Connect holdings data for the target enterprise (if listed) (daily)
  2. Calculate holding market value change = current day holding market value - previous day holding market value
  3. Decompose into: price effect + actual buying/selling
     Actual buying/selling = holding market value change - (holding volume × stock price change)
  4. Detection:
     ├── Net selling for 5 consecutive days (actual buying/selling negative) → Yellow Foreign capital reducing holdings
     ├── Weekly holding proportion decline > 10% → Orange Foreign sentiment clearly cooling
     └── Northbound holding proportion at 3-month low → Red Institutional confidence insufficient

Limitations Annotated:
  ├── Only applicable to Shanghai-Hong Kong Stock Connect / Shenzhen-Hong Kong Stock Connect targets — not all bond-issuing enterprises have northbound data
  ├── Northbound buying/selling may have non-credit reasons (portfolio rebalancing, sector rotation, FX hedging)
  └── Northbound capital accounts for approximately 3-5% of China A-shares — signal strength is limited
```

### 7.7 Comprehensive Signal Assessment Table

| Market Implied Signal | Data Source | Lead Over Bond Market Window | Reliability | Availability | 
|------------|-------|------------|-------|-------|
| Conversion premium (conversion value basis) | Convertible bond public quotes | 0-4 weeks | Medium | ✅ |
| Issuance rate change (primary market) | Issuance announcement / China Money Network | 0-2 weeks (immediate) | High | ✅ |
| Cumulative stock price decline + volatility amplification | Free quote APIs | 2-12 weeks | Medium-High | ✅ (Listed companies) |
| Northbound capital persistent reduction | HKEX | 4-12 weeks | Medium | ⚠️ (Shanghai-Hong Kong Stock Connect targets only) |
| Margin balance withdrawal | Exchange | 1-4 weeks | Medium | ⚠️ (Margin trading targets only) |
| Major shareholder pledge ratio increase | Corporate announcements | 8-24 weeks | Medium | ✅ |

---

## 8. Output Standards and Limitations

### 8.1 Output Specification for Each Indicator

**Every indicator** in quantitative analysis must be accompanied by the following elements when output:

```
[Indicator Name]
├── Current Value: [Value]
├── Data Source: [Source description]
├── Calculation Window: [Time window / Number of observations]
├── Quality Annotation: [High quality / Medium / Low quality / Alternative]
├── Trend: [Rising / Declining / Stable / N/A]
├── Threshold Judgment: [Normal / Attention / Abnormal / Crisis]
├── Historical Quantile: [% — if sufficient historical data available]
└── Qualitative Association: [What the change in this indicator means qualitatively]
```

**Quality Annotation Rules:**

| Quality Level | Annotation Condition | Representation in Report |
|---------|---------|--------------|
| **High Quality** | Data from authoritative source, complete series, no alternative assumptions in calculation | ✅ No annotation |
| **Medium** | Data from public but less authoritative source, series has few gaps | ⚠️ Accompanied by "Medium Quality" annotation |
| **Low Quality** | Calculated via alternative method, significant gaps in series, insufficient activity | ⚠️ Accompanied by "Low Quality — For Reference Only" annotation |
| **Alternative** | Precise indicator unavailable, using approximate substitute | Accompanied by alternative description and expected error range |
| **Unavailable** | Completely inaccessible or requires paid terminal | ❌ Clearly annotate "Unavailable" with reason |

**Output Example (Full Annotation):**

```
Indicator: YTM Spread
Current Value: 223bp
Data Source: Exchange closing clean price + CCDC government bond yield curve (linear interpolation)
Calculation Window: 2026-01-01 to 2026-07-01 (126 trading days)
Quality Annotation: ⚠️ Medium quality — Z-spread unavailable, YTM spread does not consider term structure
Trend: Last 20 days +18bp (rising)
Threshold Judgment: Orange Abnormal — exceeds 80th percentile of industry history
Historical Quantile: 82% (vs own past 1 year)
Qualitative Association: The persistent widening of YTM spread is consistent with the timeline of the company's
          2025 loss pre-announcement; the market has been repricing credit risk
```

### 8.2 Data Quality Matrix Summary

| Indicator | Quality Level | Core Limitation | Recommended Alternative / Handling |
|------|---------|---------|-------------|
| YTM Spread | Medium | Price distortion for inactive bonds; no option adjustment | Use only for active bonds (≥1 trade per week) |
| Z-spread | ❌ Unavailable | Requires professional terminal cash flow modeling | Use YTM spread + term approximation + annotate error |
| OAS | ❌ Unavailable | Requires option-embedded pricing model | Abandon — or use Z-spread approximation for plain bonds |
| Modified Duration | Medium | Approximate calculation does not include option adjustment | Feasible for fixed-rate plain bonds; not applicable for CBs / option-embedded bonds |
| Convexity | ❌ Unavailable | Requires precise cash flow pricing | Annotate "Convexity unavailable" — do not estimate |
| Historical Volatility (HV) | Medium-High | Lagging indicator; not applicable to non-listed companies | Cross-validate with spread trend |
| Implied Volatility | ❌ Unavailable | China credit bond / convertible bond options market absent | Use HV for directional approximation |
| Bid-ask spread | ❌ Unavailable | China bond market opaque | Use turnover rate / trading frequency as liquidity proxy |
| Northbound capital holdings | Medium-High | Only available for Shanghai/Shenzhen Stock Connect targets | Mark "No data" for non-Stock Connect enterprises |
| Margin balance | Medium | Only available for margin trading targets | Mark "No data" for non-margin-targets |
| Issuance rate | Medium-High | Only available when new issuance occurs | Secondary market spread as continuous substitute |
| Rating migration | Medium | Significant lag | Use Track A for forward-looking validation rather than reliance |
| Trading volume / turnover rate | Medium | Data sparse for inactive bonds | Changes in trading volume for active bonds are more meaningful than absolute levels |

### 8.3 Summary of Core Public Data Limitations

This section consolidates all data limitations annotated throughout the document as a single reference point:

| Limitation Category | Specific Content | Impact on Analysis | Solvable Through Data Source Upgrade |
|---------|---------|-------------|-------------------------|
| **Z-spread/OAS missing** | Unable to obtain any professional terminal spread decomposition data | Cannot finely decompose credit risk, interest rate risk, and option risk | ✅ Solvable by accessing Wind/Bloomberg |
| **Bid-ask spread missing** | China bond market opaque, market maker quotes unavailable | Cannot assess real transaction costs and liquidity | ⚠️ Partial — possibly after accessing CFETS data |
| **Non-listed companies have no stock price** | 50%+ of bond issuers are non-listed companies | Volatility analysis, stock price signals completely unavailable | ❌ Structural — non-listed entities have no public stock price |
| **Convertible bond pricing model missing** | Cannot calculate pure bond value, option value, theoretical pricing | Credit signal extraction for convertible bonds limited to simplified calculations | ✅ Solvable by accessing professional terminals + QuantLib |
| **China CDS market absent** | Credit default swaps virtually nonexistent in China | Cannot extract credit risk premium from credit derivatives | ❌ Market infrastructure issue — not data acquisition |
| **ESG/ETL data non-standardized** | No standardized ESG scores, carbon emissions data (public) | Cannot incorporate ESG factors into quantitative models | ⚠️ Partial — can access third-party ESG scores |
| **High-frequency data missing** | Minute-level/tick-by-tick data requires payment | Cannot perform high-frequency volatility, microstructure analysis | ✅ Solvable by accessing paid data |
| **Inactive bond data sparse** | Many bonds have no trading for days | Spread calculation distorted — benchmark method not applicable | ❌ Market liquidity issue — not data acquisition |
| **Parent-subsidiary data isolation** | Consolidated statements mask parent company risk (validation cases have repeatedly confirmed) | The "enterprise" granularity in factor analysis needs to be precise to the bond issuing entity | ⚠️ Requires manual identification of the issuing entity — data source upgrade cannot fully resolve |
| **Covenant data non-standardized** | Bond covenants scattered in prospectuses | Cannot batch process option-embedded analysis | ⚠️ Partial — can be structured after LLM extraction of covenants |

### 8.4 Alternative Methods Summary Table

When precise indicators are unavailable, alternative methods and their effectiveness ratings:

| Unavailable Indicator | Alternative Method | Effectiveness Rating | Applicable Conditions | Error Range |
|------------|---------|---------|---------|---------|
| Z-spread | YTM - same-maturity CDB bond (linear interpolation) | ⭐⭐⭐ Medium | Plain bonds, non-option-embedded, active bonds | ±15-30bp |
| OAS | No alternative — annotate as unavailable | ❌ | N/A | N/A |
| Modified Duration | Macaulay Duration approximation (D/(1+YTM)) | ⭐⭐⭐ Medium | Plain bonds, fixed rate | Error increases with YTM |
| Convexity | No alternative — annotate as unavailable | ❌ | N/A | N/A |
| Implied Volatility | Historical Volatility (HV_20d) | ⭐⭐ Low | Directional reference only | Lagging + insufficient precision |
| Bid-ask spread | Average daily trading volume + turnover rate | ⭐⭐ Low | Directional liquidity judgment | Cannot quantify transaction costs |
| Individual stock high-frequency data | Daily closing price + daily return | ⭐⭐⭐ Medium | Daily analysis sufficient | Cannot do microstructure |
| Non-listed company financials | Prospectus + judicial + bidding + hiring + commercial registry | ⭐⭐⭐ Medium | Multi-source cross-validation | Depends on data richness |
| Northbound capital (non-target) | No alternative | ❌ | N/A | N/A |
| Tail Risk (VaR/ES) | Scenario weighting method (see Chapter 6) | ⭐⭐ Low | Directional exposure judgment | No statistical precision guarantee |

### 8.5 Output Checklist

Before each quantitative analysis output, the AI Agent must execute the following checks:

```
[ ] Is each indicator accompanied by a data source annotation?
[ ] Is each indicator accompanied by a quality annotation?
[ ] Has the unavailable status been annotated for all inaccessible indicators?
[ ] Has the error range been annotated for alternative methods?
[ ] Has Z-spread/OAS been annotated as unavailable?
[ ] For non-listed enterprises, has volatility/stock price signal unavailability been annotated?
[ ] For convertible bonds, has the option-embedded issue been annotated in model limitations?
[ ] Has the time window been explicitly annotated?
[ ] Is there a distinction between "available but low quality" and "unavailable"?
[ ] Is a qualitative association explanation included (what this value/change is saying)?
[ ] If an alternative method was used, has the expected error range been annotated?
[ ] Has signal consistency been checked (avoid misjudgment from a single indicator)?
```

### 8.6 Mapping from Track B Quantitative Analysis to Track A

The final output of quantitative analysis needs to be mapped to Track B's four-level signal system and enter the cross-validation matrix:

```
L0.1 + L0.2 + L0.3 → Track B Four-Level Signals → Cross-Validation → Comprehensive Rating

Quantitative Layer (This Document)        Four-Level Signal Layer        Dual-Track Collision Layer
├── YTM Spread Level                      ├── Spread Calm                ├── Consensus
├── Volatility Status                     ├── Spread Attention           ├── Divergence A (A good, B bad)
├── Factor Drift Detection                ├── Spread Abnormal            └── Divergence B (A bad, B good)
├── Correlation Structure                 └── Spread Crisis
├── Stress Testing
├── Market Implied Signals
└── Data Quality Annotations

Four-Level Signal Decision Rules (One-Click Mapping):
  Spread stable or narrowing + Low volatility + Factor stable         → Calm
  Spread widening 20-50bp + Volatility rising                        → Attention
  Spread jump >50bp or persistent widening + Large volatility increase → Abnormal
  Curve inversion / Liquidity drying up + Extreme spread widening    → Crisis
```

---

## Appendixes

### A. Standard Time Window Configuration

| Analysis Type | Recommended Window | Minimum Window | Optimal Frequency |
|---------|---------|---------|---------|
| Spread Trend Analysis | 60 trading days | 20 trading days | Weekly update |
| Volatility Analysis | 20/60/120 days (triple window) | 20 days | Weekly update |
| Factor Regression | 24 weeks | 12 weeks | Monthly update |
| Correlation Matrix | 24 weeks | 12 weeks | Monthly update |
| Stress Testing | N/A | N/A | Quarterly update or event-driven |
| Market Implied Signals | Varies widely | Depends on signal type | Event-driven |

### B. Terminology Table

| Term | Definition/Notes |
|------|-----------------|
| Yield-to-Maturity (YTM) | Calculated based on exchange closing clean price |
| Credit Spread | YTM - same-maturity government/CDB bond yield |
| Z-spread | Not available, using YTM spread as substitute |
| OAS | Not available |
| Duration | Using Macaulay Duration approximation |
| Historical Volatility | Annualized daily return standard deviation |
| Beta | Single-factor rolling regression |
| Alpha | Factor model residual — idiosyncratic pricing of the enterprise |
| R-squared | Proportion of spread variation explained by factors |
| Cross-sectional Sigma | Cross-sectional dispersion of spreads within industry/rating at same period |
| Tail Correlation | Probability of co-decline under extreme scenarios |

### C. Document Version History

| Version | Date | Changes |
|------|------|---------|
| v0.0.1 | 2026-07-08 | Initial release: complete eight-chapter quantitative analysis methodology |
| — | — | Contents: Credit Spread, Volatility, Multi-Factor, Correlation, Stress Testing, Market Implied Signals, Output Standards |
| — | — | Examples: 5 solar PV convertible bonds, Shuangliang Energy, Brilliance China Auto, LONGi 22 CB, Yongcheng Coal regional transmission |

### D. Statistical Method Usage Checklist [Statistical Correction v0.0.1]

Before each quantitative analysis run, the AI Agent must confirm each of the following statistical preconditions item by item. Each confirmation result (✅ / ⚠️ / ❌) must be explicitly annotated in the output and must not be omitted.

```
□ Has the time series been tested for stationarity (ADF)?
   → Annotate "ADF p=X.XXX → Stationary/Non-stationary (differenced/skipped)"

□ Have the regression residuals been tested for heteroskedasticity (Breusch-Pagan)?
   → Annotate "BP p=X.XXX → Homoskedastic/Heteroskedastic (HAC standard errors used)"

□ Has the multi-factor model been tested for multicollinearity (VIF)?
   → Annotate "Max VIF=X.X → No collinearity/Moderate collinearity weight reduced/Severe collinearity merged"

□ Is the correlation estimate accompanied by a confidence interval (Fisher Z transformation)?
   → Annotate "ρ=X.XX [95% CI: X.XX–X.XX]"

□ Is the volatility estimate accompanied by a confidence interval (chi-square distribution)?
   → Annotate "HV=X.X% [95% CI: X.X%–X.X%]"

□ Is the spread estimate accompanied by a confidence interval (Bootstrap)?
   → Annotate "Spread Mean=X [95% CI: X–X]"

□ Has FDR correction (Benjamini-Hochberg) been applied for multiple hypothesis testing?
   → Annotate "Raw signal count=X, Significant after FDR correction count=X, q=0.05"

□ Is the sample size ≥ 30 (minimum regression sample size)?
   → If n<30, annotate "Sample size insufficient (n=X) — regression results for directional reference only"

□ Is the tail probability annotated as a "ranking tool" rather than an "exact probability"?
   → Annotate "Tail probability is a ranking tool, not a precise statistical probability"

□ Does the test include false positive rate and false negative rate (not just successful cases)?
   → Annotate "False positive rate estimate: X% (after FDR correction), False negative rate estimate: X% (based on test power)"
```

**Usage Rules:**
1. At the end of each quantitative analysis output, the completion status of this checklist must be attached
2. Items that did not pass must be accompanied by a handling explanation — "not done" and "done but failed" have different annotations
3. This checklist acts as a quality control gate — only when all items are ✅ may the analysis proceed to Track B four-level signal mapping
4. If any item is ❌, the analysis must be annotated as "Statistical preconditions not fully satisfied — conclusion confidence limited"
