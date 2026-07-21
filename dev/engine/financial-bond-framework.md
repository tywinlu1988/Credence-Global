# Financial Bond Credit Analysis Framework

**Version**: v0.0.5 | **Date**: 2026-07-10 | **Status**: Published

**Module**: Fixed Income Credit Analysis Engine - Financial Industry Analysis Track (Parallel to Corporate Bond Pyramid)

---

> **Honesty Statement:** This framework is specifically designed for credit analysis of financial enterprises (banks, securities firms, insurance companies, financial leasing companies). The credit logic of financial enterprises is fundamentally different from corporate enterprises -- there is no "inventory turnover," "accounts receivable aging," or "gross margin," which are core indicators for corporate analysis. For financial enterprises, the "raw material" is funding, the "product" is loans and investments, and the "cost" is risk. This framework aims to fill the gap in the engine regarding financial bonds, but does not replace the specialized regulatory frameworks for each sub-type (such as the Basel Accords, Solvency II, etc.).

---

## Table of Contents

- [1. Positioning of Financial Bonds in the Engine](#1-positioning-of-financial-bonds-in-the-engine)
- [2. Financial Industry Analysis Track Design](#2-financial-industry-analysis-track-design)
- [3. Bank Sub-Framework (CAMELS)](#3-bank-sub-framework-camels)
- [4. Securities Sub-Framework](#4-securities-sub-framework)
- [5. Insurance Sub-Framework](#5-insurance-sub-framework)
- [6. Financial Leasing Sub-Framework](#6-financial-leasing-sub-framework)
- [7. Cross-Sub-Type General Indicators](#7-cross-sub-type-general-indicators)
- [8. Financial Bond Public Data Quality Assessment](#8-financial-bond-public-data-quality-assessment)
- [9. Special Risks in Financial Bond Analysis](#9-special-risks-in-financial-bond-analysis)
- [10. Cross-Validation Linkage Between Financial and Corporate Bonds](#10-cross-validation-linkage-between-financial-and-corporate-bonds)
- [11. Scoring Output Template](#11-scoring-output-template)
- [12. Version History and To-Do Items](#12-version-history-and-to-do-items)

---

## 1. Positioning of Financial Bonds in the Engine

### 1.1 Financial Bond Market Scale

In the global credit bond market (as of end-2025), financial bonds (including commercial bank bonds, securities company bonds, insurance company bonds, and financial leasing bonds) account for a significant portion of total credit bond outstanding.

| Financial Bond Sub-Type | Outstanding Scale Estimate | Issuer Characteristics |
|---|---|---|
| Commercial bank bonds (including Tier 2 capital bonds, perpetual bonds) | Significant | State-owned banks + joint-stock banks + city/rural commercial banks, most comprehensive regulatory disclosure |
| Securities company bonds (including short-term notes) | Notable | Primarily listed securities firms, heavily influenced by market conditions |
| Insurance company bonds (including capital supplementary bonds) | Moderate | Life insurance > property insurance, long duration, interest rate sensitive |
| Financial leasing bonds | Smaller | Primarily bank-affiliated leasing companies, asset-side highly linked to industrial cycle |

### 1.2 Financial Bonds vs Corporate Bonds: Fundamental Differences

| Dimension | Corporate Enterprises | Financial Enterprises |
|---|---|---|
| Core assets | Inventory, equipment, plant, IP | Loan portfolios, investment portfolios, customer relationships |
| Revenue source | Product/service sales | Net interest income, fees, investment income |
| Primary risks | Demand/competition/cost | Credit risk (loan default), market risk (asset price volatility), liquidity risk |
| Leverage characteristics | Debt-to-asset ratio 40-70% | Naturally high leverage (banks > 90% liability ratio is normal) |
| Regulatory density | Industry regulation + environmental etc. | Strict financial institution regulation (capital/liquidity/related party hard constraints) |
| Data quality | Variable, poor for non-listed enterprises | Mandatory disclosure, data quality far better than corporate bonds |
| Risk exposure speed | Gradual deterioration (> 12 months) | Can erupt suddenly (bank run / market freeze) |
| Government support | Some SOEs have implicit guarantees | Systemically important financial institutions have explicit + implicit support |

### 1.3 Why Financial Bonds Need an Independent Analysis Track

The existing engine's corporate bond pyramids (cyclical / defensive / growth / regulated-utility types) are completely unsuitable for financial enterprises:

- **L1 Policy Layer**: Still important for financial enterprises (monetary policy / regulatory policy), but weights and indicators are completely different
- **L2 Technology Layer**: Financial enterprises have no "technology moat" concept (except fintech)
- **L3 Supply Chain Layer**: A financial enterprise's "supply chain" is fund sources (deposits / interbank / bond issuance) and fund deployment (loans / investments)
- **L4 Financial Layer**: Financial indicators are completely different (capital adequacy ratio vs debt-to-asset ratio, NIM vs gross margin)

---

## 2. Financial Industry Analysis Track Design

### 2.1 Track Design Principles

Financial bonds do not establish a separate independent pyramid scoring system, but instead add a **"Financial Industry Analysis Track"** within the existing dual-track architecture, running parallel to the corporate bond pyramid.

```
Input: Industry + Enterprise + Analysis Date
           │
      ┌────┴────┐
      │ Industry  │
      │ Judgment │
      └────┬────┘
           │
      ┌────┴─────────────────────┐
      │                          │
      Corporate                   Financial
      Enterprises                 Enterprises
      (Corporate Pyramid)        (Financial Analysis Track)
      · Policy-driven            · Bank -> CAMELS
      · Technology-moat          · Securities -> Capital+Leverage+Proprietary
      · Zero-sum                 · Insurance -> Solvency+Spread
      · Asset-lease              · Leasing -> NPL+Provisions+Spread
           │                          │
      └────┴─────────────────────┘
           │
           Enter Dual-Track Cross-Validation (Track A+B)
```

### 2.2 Standardized Scoring Structure of the Financial Analysis Track

Financial enterprises do not use the four-layer pyramid weighting logic (policy/technology/supply chain/financial) used for corporates, but instead adopt a **"Five-Dimension Risk Score"** structure, uniformly applicable to all financial sub-types, with specific indicators and weights adjusted per sub-type.

```
Financial Five-Dimension Score = Sum(Dimension Score x Sub-Type Weight)
Dimension Score = Sum(Indicator Score x Indicator Weight)

Five Dimensions:
  C - Capital Adequacy
  A - Asset Quality
  L - Liquidity & Funding
  E - Earnings & Profitability
  S - Sensitivity & Risk (Market/Operational/Concentration)

Weights adjusted by sub-type:
  Bank:      C25% A30% L20% E15% S10%
  Securities: C20% A20% L20% E20% S20%
  Insurance:  C30% A20% L10% E20% S20%
  Leasing:    C20% A35% L15% E15% S15%
```

### 2.3 Linkage with the Corporate Pyramid

The five-dimension score generated by the financial analysis track maps to the existing engine's **12-notch rating system** (AAA -> D), with scoring range definitions entirely consistent with corporate bonds:

| Five-Dimension Score Range | Corresponding Rating | Meaning |
|---|---|---|
| 9.5 - 10.0 | AAA | Extremely low risk |
| 8.0 - 9.4 | AA+/AA/AA- | Low risk |
| 6.5 - 7.9 | A+/A/A- | Medium-low risk |
| 5.0 - 6.4 | BBB+/BBB/BBB- | Medium risk |
| 3.5 - 4.9 | BB+/BB/BB- | Medium-high risk |
| 2.0 - 3.4 | B+/B/B- | High risk |
| 1.0 - 1.9 | CCC | Extremely high risk |
| 0 - 0.9 | D | Default/Imminent |

> **Important**: The same rating corresponds to different risk logic. Bank AA and corporate AA both mean "low risk," but the risk sources differ -- for banks, the risk is asset quality deterioration and liquidity crisis; for corporates, it is competitive landscape deterioration and cash flow exhaustion.

### 2.4 Market Signals for the Financial Analysis Track (Track B Access)

Track B signals for financial enterprises are consistent with corporate enterprises, using a four-level market signal system:

| Signal Dimension | Bank/Securities Special Considerations |
|---|---|
| Credit spreads | Bank Tier 2 capital / perpetual bond spreads reflect market views on capital quality; securities short-term note spreads reflect liquidity pressure |
| Stock price volatility | Listed bank/securities/insurance stock price volatility (listed financial enterprise coverage > 90%) |
| Fund flows | Interbank CD issuance rate/volume -> reflects bank financing accessibility |
| Rating events | Rating downgrade impact on banks is greater than for corporates (affects interbank credit lines, may trigger liquidity crisis) |

---

## 3. Bank Sub-Framework (CAMELS)

### 3.1 CAMELS Six-Dimension Framework

Bank credit analysis adopts the internationally recognized CAMELS framework, with adjustments for market characteristics.

| Dimension | Meaning | Weight | Core Indicators | Data Source |
|---|---|---|---|---|
| **C - Capital Adequacy** | Capital adequacy | 25% | CET1 ratio, Tier 1 capital ratio, Capital adequacy ratio, Leverage ratio | Annual/quarterly reports |
| **A - Asset Quality** | Asset quality | 30% | NPL ratio, Special-mention loan ratio, Provision coverage ratio, Loan loss provision ratio, 90+ days past due / NPL divergence | Annual/quarterly reports |
| **M - Management** | Management quality | 10% | Equity structure stability, management track record, related transaction scale, regulatory penalty record | Business information platforms / regulatory announcements |
| **E - Earnings** | Profitability | 15% | ROA, ROE, Net interest margin (NIM), Cost-to-income ratio, Non-interest income ratio | Annual/quarterly reports |
| **L - Liquidity** | Liquidity | 15% | LCR, NSFR, Loan-to-deposit ratio, Interbank liability ratio | Annual/quarterly reports (some require estimation) |
| **S - Sensitivity** | Market risk sensitivity | 5% | Interest rate risk, FX risk exposure, Trading book ratio, Derivatives size/capital | Annual reports + estimation |

### 3.2 C - Capital Adequacy Score (25%)

| Indicator | Calculation | Strong (8-10) | Adequate (4-7) | Weak (0-3) | Weight |
|---|---|---|---|---|---|
| CET1 ratio | CET1 / Risk-weighted assets | > 12% | 9-12% | < 9% (regulatory minimum) | 35% |
| Tier 1 capital ratio | Tier 1 capital / Risk-weighted assets | > 13% | 10-13% | < 10% (regulatory buffer) | 25% |
| Capital adequacy ratio | Total capital / Risk-weighted assets | > 15% | 12-15% | < 12% (< 10.5% triggers regulatory action) | 25% |
| Leverage ratio | Tier 1 capital / Total assets (no risk weighting) | > 6% | 4-6% | < 4% (regulatory minimum) | 15% |

**Bank Capital Regulatory Minimums:**
- CET1 minimum requirement: 5% (D-SIB/G-SIB add 1%-2.5% surcharge)
- Tier 1 capital minimum requirement: 6%
- Capital adequacy minimum requirement: 8%
- **In practice, capital below regulatory requirement + buffer triggers restrictions -- do not wait for hard minimum**

**Scoring Adjustment:**
- Capital quality (including other Tier 1 / Tier 2 capital composition) -- high proportion of TLAC-eligible instruments +1 point
- TLAC (Total Loss-Absorbing Capacity) compliance -- systemically important banks need to monitor TLAC shortfall

### 3.3 A - Asset Quality Score (30%)

| Indicator | Calculation | Strong (8-10) | Adequate (4-7) | Weak (0-3) | Weight |
|---|---|---|---|---|---|
| NPL ratio | Non-performing loans / Total loans | < 1.0% | 1.0-2.5% | > 2.5% (> 5% severely weak) | 30% |
| Special-mention loan ratio | Special-mention loans / Total loans | < 2.0% | 2.0-5.0% | > 5.0% | 20% |
| Provision coverage ratio | Loan loss provisions / NPLs | > 300% | 150-300% | < 150% (< 120% triggers regulatory attention) | 20% |
| Loan loss provision ratio | Loan loss provisions / Total loans | > 3.5% | 2.5-3.5% | < 2.5% | 15% |
| 90+ days past due / NPL divergence | Loans 90+ days past due / NPLs | < 100% | 100-130% | > 130% (signal of hidden NPLs) | 15% |

**Bank Asset Quality Core Focus Areas:**

1. **Divergence ratio is the mirror of asset quality.** 90+ days past due / NPL divergence > 100% means the bank is hiding NPLs -- this is the most important leading indicator in bank asset quality analysis. A failed mid-sized bank (2019) had divergence > 150% for an extended period before regulatory takeover.

2. **Special-mention loans are a leading signal.** An increase in the special-mention loan ratio precedes an increase in the NPL ratio by 6-12 months, making it the most important forward warning of asset quality deterioration.

3. **The quality of the NPL ratio depends on divergence.** For banks with divergence > 130%, the disclosed NPL ratio is essentially unreliable; the true NPL ratio needs to be estimated by adding 1-3 percentage points to the disclosed value.

4. **Industry concentration is a hidden risk.** Concentration exposure to real estate / LGFVs / overcapacity industries is not directly reflected in NPLs, but will be concentrated during economic downturns.

**Industry Exposure Concentration Adjustment (Corrected Score):**

| Single Industry Exposure / Net Capital | Score Correction |
|---|---|
| > 50% (real estate) | -1 point (special attention) |
| > 100% (LGFVs) | -2 points (highly concentrated) |
| Top 3 industries combined > 200% | -1 point (industry concentration risk) |

### 3.4 M - Management Quality Score (10%)

| Indicator | Calculation | Strong (8-10) | Adequate (4-7) | Weak (0-3) | Weight |
|---|---|---|---|---|---|
| Equity structure stability | Major shareholder changes in 3 years | Stable | Changes but no control dispute | Frequent changes or equity pledge disputes | 25% |
| Management stability | Chairman/president changes in 3 years | 0-1 times | 2-3 times | > 3 times or abnormal changes | 20% |
| Related transaction scale | Related transactions / Net assets | < 10% | 10-30% | > 30% or suspected benefit transfer to major shareholder | 25% |
| Regulatory penalty record | Major penalties in 3 years | 0 | 1-2 minor fines | > 2 major penalties or taken over/placed under receivership | 30% |

**Special Attention Signals (Triggering Veto-Level Concern):**
- Major shareholder equity frozen by court order
- Chairman/president under investigation or missing
- Related loans not deducted from capital
- Large volume of non-standard business transactions with shareholders

### 3.5 E - Earnings Score (15%)

| Indicator | Calculation | Strong (8-10) | Adequate (4-7) | Weak (0-3) | Weight |
|---|---|---|---|---|---|
| ROA | Net profit / Average total assets | > 1.0% | 0.5-1.0% | < 0.5% (< 0% sustained losses) | 25% |
| ROE | Net profit / Average net assets | > 12% | 6-12% | < 6% (< 0% sustained losses) | 25% |
| NIM | Net interest income / Average interest-earning assets | > 2.2% | 1.8-2.2% | < 1.8% (< 1.5% stressed) | 25% |
| Cost-to-income ratio | Operating expenses / Operating income | < 30% | 30-40% | > 40% (> 50% inefficient) | 15% |
| Non-interest income ratio | Non-interest income / Operating income | > 25% | 15-25% | < 15% (over-reliant on spread) | 10% |

**Bank Earnings Analysis Key Points:**

1. **NIM trend is more important than absolute value.** In an interest rate down-cycle, industry NIM may compress from 2.2% to below 1.6%. Banks with rapid NIM decline typically have fragile asset-liability structures (sticky deposit costs, weak loan pricing power).

2. **Non-interest income needs decomposition:** Fee income (wealth management, investment banking, settlement) is relatively stable; investment income (bond price gains, fund dividends) is volatile. High non-interest income ratio but primarily investment income -> sustainability questionable.

3. **Credit cost is the biggest drag on earnings.** Bank reported profit = Net interest income + Non-interest income - Operating expenses - Credit impairment losses - Tax. Credit impairment losses are the largest profit adjustment item -- may be understated when NPLs are high.

### 3.6 L - Liquidity Score (15%)

| Indicator | Calculation | Strong (8-10) | Adequate (4-7) | Weak (0-3) | Weight |
|---|---|---|---|---|---|
| LCR | High-quality liquid assets / Net cash outflows over 30 days | > 150% | 100-150% | < 100% (non-compliant) | 30% |
| NSFR | Available stable funding / Required stable funding | > 120% | 100-120% | < 100% (non-compliant) | 25% |
| Loan-to-deposit ratio | Total loans / Total deposits | < 75% | 75-85% | > 85% (> 100% extremely high risk) | 20% |
| Interbank liability ratio | Interbank liabilities / Total liabilities | < 15% | 15-25% | > 25% (> 33% regulatory cap) | 15% |
| High-quality liquid assets | Cash + government bonds + policy bank bonds / Total assets | > 10% | 5-10% | < 5% | 10% |

**Bank Liquidity Core Focus Areas:**

1. **High interbank liability dependence is a fragility signal.** A failed mid-sized bank had interbank liability ratio exceeding 40% before takeover, far above the 33% regulatory cap. Liquidity crises for small and medium banks often start with interbank financing tightening.

2. **LCR and NSFR public disclosure is limited.** Most banks only disclose LCR and NSFR at the large bank level in annual reports; city/rural commercial banks may not disclose. Non-disclosure itself is a negative signal.

3. **Loan-to-deposit ratio > 100% means the bank is extremely "borrowing short, lending long."** If combined with a high interbank liability ratio, liquidity risk is extremely high.

### 3.7 S - Market Risk Sensitivity Score (5%)

| Indicator | Calculation | Strong (8-10) | Adequate (4-7) | Weak (0-3) | Weight |
|---|---|---|---|---|---|
| Trading book ratio | Trading securities / Total assets | < 5% | 5-15% | > 15% | 30% |
| Bond investment / Capital | Bond investment size / Net capital | < 300% | 300-500% | > 500% | 25% |
| Derivatives notional / Capital | Derivatives notional / Net capital | < 500% | 500-2000% | > 2000% | 20% |
| FX exposure / Capital | FX risk exposure / Net capital | < 10% | 10-30% | > 30% | 25% |

**Note:** Banks' market risk exposure is typically small (mainly hold-to-maturity bonds), but some joint-stock banks have high trading book ratios, and interest rate fluctuations have a greater impact on their capital.

### 3.8 Bank Veto Conditions (Score Capped at CCC)

Triggering any of the following conditions caps the bank's composite rating at CCC:

1. **CET1 ratio < regulatory minimum (including buffer)** -- capital deficiency has triggered regulatory restrictions
2. **NPL ratio > 8%** -- severe asset quality deterioration
3. **Provision coverage ratio < 100%** -- insufficient provisions, effectively insolvent
4. **Taken over, placed under receivership, or systemic risk resolution mechanism triggered**
5. **Interbank liability ratio > 33% (regulatory cap) AND loan-to-deposit ratio > 100%**
6. **Chairman/president placed under investigation or missing**

### 3.9 Bank Size Tier Reference

Banks of different tiers have different scoring baselines:

| Bank Type | Examples | CET1 Ratio Baseline | NPL Baseline | ROE Baseline | Special Considerations |
|---|---|---|---|---|---|
| State-owned banks | Major global banks | > 12% | < 1.5% | > 10% | TLAC compliance, G-SIB surcharge |
| Joint-stock banks | National commercial banks | > 10% | < 1.8% | > 8% | Interbank liability ratio, non-standard exposure |
| City commercial banks | Regional leading banks | > 10% | < 1.5% | > 10% | Regional economic concentration, LGFV exposure |
| Rural commercial banks | Regional leading banks | > 11% | < 2.0% | > 8% | Agricultural exposure, SME credit risk |
| Foreign banks | International banks (local subsidiaries) | > 15% | < 0.5% | > 5% | Parent bank support is key, local business share small |
| Community banks | -- | > 10% | < 3.0% | Unstable | Very small scale, fragile liquidity |

---

## 4. Securities Sub-Framework

### 4.1 Special Characteristics of Securities Firm Credit Analysis

Securities firms are fundamentally different from banks:
- **Asset side**: Primarily financial assets (stocks/bonds/funds/derivatives), not loans
- **Liability side**: Leveraged operations but leverage ratio subject to regulatory constraints
- **Revenue**: Highly dependent on market conditions (brokerage/IB/proprietary/asset management)
- **Risk**: Market risk > credit risk, highly correlated with secondary market conditions

### 4.2 Securities Firm Five-Dimension Score

| Dimension | Weight | Core Indicators | Data Source |
|---|---|---|---|
| **C - Capital Adequacy** | 20% | Net capital, Risk coverage ratio, Capital leverage ratio | Annual reports / monthly operating data |
| **A - Asset Quality** | 20% | Proprietary investment returns, Bond investment rating distribution, Stock pledge repo default rate | Annual reports + estimation |
| **L - Liquidity & Funding** | 20% | LCR, Short-term financing ratio, Financing channel diversity | Annual reports |
| **E - Earnings** | 20% | ROE, Brokerage market share, IB IPO underwriting ranking, Proprietary income ratio | Financial data platforms / industry associations |
| **S - Sensitivity** | 20% | Leverage ratio, Derivatives notional/net capital, Proprietary equity ratio, Single client concentration | Annual reports |

### 4.3 Securities Firm Key Indicator Scoring

| Indicator | Calculation | Strong (8-10) | Adequate (4-7) | Weak (0-3) | Weight |
|---|---|---|---|---|---|
| **C - Risk coverage ratio** | Net capital / Total risk capital reserves | > 300% | 200-300% | < 200% (< 100% triggers regulatory action) | 50% |
| **C - Capital leverage ratio** | Core net capital / Total on- and off-balance sheet assets | > 15% | 10-15% | < 10% (< 8% triggers regulatory action) | 50% |
| **A - Stock pledge default rate** | Default pledge size / Total pledge size | < 5% | 5-15% | > 15% | 40% |
| **A - Proprietary investment leverage** | Proprietary size / Net capital | < 200% | 200-400% | > 400% | 30% |
| **E - ROE** | Net profit / Average net assets | > 8% | 4-8% | < 4% or loss-making | 35% |
| **E - Brokerage stability** | Std dev / mean of brokerage revenue over 3 years | < 15% | 15-30% | > 30% | 25% |
| **L - Short-term note ratio** | Short-term financing / Total liabilities | < 20% | 20-35% | > 35% | 40% |
| **L - Financing channel diversity** | Number of available financing channels (corp bonds / short-term notes / revenue certificates / borrowing / repo / refinancing) | > 5 types | 3-5 types | < 3 types | 30% |
| **S - Leverage ratio (regulatory)** | Total assets / Net assets | < 3x | 3-5x | > 5x (> 6x regulatory cap) | 40% |
| **S - Proprietary equity ratio** | Equity proprietary / Net capital | < 50% | 50-100% | > 100% | 30% |

### 4.4 Securities Firm Credit Analysis Key Points

1. **Proprietary business is a key variable.** Securities firm operations are divided into "asset-light" (brokerage/IB/asset management) and "asset-heavy" (proprietary/market making). Higher proprietary ratio = greater performance volatility = credit risk fluctuating with markets.

2. **Stock pledge repo is a unique risk.** The 2018 stock pledge margin call wave caused many securities firms to book large impairment provisions, with some small and medium firms facing default on repurchase agreements. Firms with large pledge businesses and weak risk control require extra attention.

3. **Brokerage business is stable but being compressed.** Commission rates have been declining. Brokerage as a profit pillar is weakening. The progress of wealth management transformation (fund distribution / advisory service revenue share) needs attention.

4. **IB business depends on regulatory cycles.** IPO pace is heavily influenced by policy regulation. IB revenue cannot be used as a credit quality baseline at peak levels.

5. **Leading vs small/medium securities firms:** Leading firms have significantly superior financing channels, client bases, and regulatory standing compared to small/medium firms; credit differentiation is evident.

### 4.5 Securities Firm Veto Conditions

1. **Risk coverage ratio < 100%** (net capital insufficient to cover risk exposure)
2. **Capital leverage ratio < 8%** (regulatory red line)
3. **Stock pledge default rate > 20% AND size > 50% of net capital**
4. **Proprietary equity ratio > 200%** (exceeds regulatory cap)
5. **Subject to business restriction measures or risk resolution by securities regulator**

---

## 5. Insurance Sub-Framework

### 5.1 Special Characteristics of Insurance Credit Analysis

Core logic of insurance company credit analysis:
- **Liability side**: Premium income is "collect now, pay later" -- naturally high cash flow business, but long-term liabilities (life insurance) have interest rate risk
- **Asset side**: Most funds invested in bonds/non-standard fixed income assets, some in equities
- **Core risks**: **Spread loss** (liability cost > investment return), **insufficient solvency**, **equity investment volatility**

### 5.2 Insurance Five-Dimension Score

| Dimension | Weight | Core Indicators | Data Source |
|---|---|---|---|
| **C - Solvency Adequacy** | 30% | Composite solvency ratio, Core solvency ratio, Actual capital / Minimum capital | Solvency reports (quarterly) |
| **A - Asset Quality** | 20% | Fixed income ratio, Credit bond rating distribution, Non-standard asset ratio, Default asset ratio | Annual reports |
| **L - Liquidity & Liabilities** | 10% | Lapse ratio, LCR, Short-term debt ratio | Annual / solvency reports |
| **E - Earnings** | 20% | ROE, Composite investment yield, Net investment yield, Underwriting profit/loss, Spread | Annual reports |
| **S - Sensitivity** | 20% | Equity investment ratio, Interest rate sensitivity (duration gap), Concentration risk | Annual / solvency reports |

### 5.3 Insurance Key Indicator Scoring

| Indicator | Calculation | Strong (8-10) | Adequate (4-7) | Weak (0-3) | Weight |
|---|---|---|---|---|---|
| **C - Composite solvency ratio** | Actual capital / Minimum capital | > 200% | 120-200% | < 120% (< 100% triggers regulatory action) | 50% |
| **C - Core solvency ratio** | Core capital / Minimum capital | > 150% | 75-150% | < 75% (< 50% triggers regulatory action) | 30% |
| **C - Actual capital / Premium income** | Actual capital / Annual premiums | > 30% | 15-30% | < 15% | 20% |
| **E - Composite investment yield** | (Investment income + FV changes) / Average invested assets | > 5% | 3-5% | < 3% for 2 consecutive years | 30% |
| **E - Spread** | Composite investment yield - Average liability cost | > 1.5% | 0-1.5% | < 0% (negative spread) | 30% |
| **E - ROE** | Net profit / Average net assets | > 10% | 5-10% | < 5% or loss-making | 20% |
| **E - Underwriting profit margin** | Underwriting profit / Earned premiums | > 3% | 0-3% | < 0% sustained | 20% |
| **S - Equity investment ratio** | (Stocks + equity funds + equity assets) / Total invested assets | < 15% | 15-25% | > 25% (> 30% regulatory cap) | 35% |
| **S - Interest rate duration gap** | Asset duration - Liability duration | Gap < 1 year | Gap 1-3 years | Gap > 3 years | 30% |
| **S - Top 5 counterparty concentration** | Top 5 counterparty risk exposure / Total assets | < 10% | 10-20% | > 20% | 20% |
| **L - Lapse ratio** | Lapse benefits / Earned premiums | < 3% | 3-8% | > 8% | 40% |

### 5.4 Insurance Credit Analysis Key Points

1. **Negative spread is the biggest chronic risk for life insurers.** In an interest rate down-cycle, long-term government bond yields may decline from 3%+ to below 2%, while the adjustment of life insurance policy pricing rates lags. Policies sold at peak pricing rates face continuously declining asset reinvestment returns -> negative spread accumulates. This represents a major systemic risk source.

2. **Solvency ratio is a regulatory red line but not a leading indicator.** The solvency ratio reflects "current" capital levels. Solvency deterioration is typically the result of asset-side problems (investment losses/defaults) that have already occurred, not a forward predictor.

3. **Combine short and long-term perspectives:**
   - **Short-term leading indicators**: Rising lapse ratio, declining new business value (NBV) -> cash flow pressure
   - **Medium-term core indicators**: Negative spread trend, duration gap -> sustained profitability deterioration
   - **Long-term structural indicators**: Solvency ratio, equity investment ratio -> capital safety margin

4. **Listed vs non-listed:** Listed insurance companies have the most complete information disclosure and high data reliability. Non-listed insurers (especially small and medium life insurers) have varying levels of public information -- many do not disclose investment yields and duration gaps.

5. **With-profits / universal life guarantee pressure:** If investment returns fall below customer expected returns, insurers need to subsidize from own funds -- this accelerates capital consumption in a low-rate environment.

### 5.5 Insurance Veto Conditions

1. **Composite solvency ratio < 100%** (solvency non-compliant, mandatory regulatory action triggered)
2. **Core solvency ratio < 50%** (severely insufficient)
3. **Sustained negative spread for 3 consecutive years (composite investment yield < liability cost) and gap widening**
4. **Equity investment ratio > 30%** (exceeds regulatory cap)
5. **Taken over/placed under receivership or business scope restricted by financial regulator**

---

## 6. Financial Leasing Sub-Framework

### 6.1 Special Characteristics of Financial Leasing Credit Analysis

Financial leasing enterprises have "bank-like" characteristics:
- **Asset side**: Primarily lease assets (equipment/aircraft/ships/vehicles etc.) -- both financial and physical assets
- **Liability side**: Highly dependent on bank borrowing and bond issuance -- financing channels are core
- **Risk characteristics**: Credit risk (lessee default) + asset risk (lease asset value decline / disposal difficulty) + maturity mismatch risk
- **High correlation with banks**: Most financial leasing companies are bank subsidiaries -- parent bank support is a key variable

### 6.2 Leasing Five-Dimension Score

| Dimension | Weight | Core Indicators | Data Source |
|---|---|---|---|
| **C - Capital Adequacy** | 20% | Capital adequacy ratio, Leverage multiple (total assets / net assets) | Annual reports / regulatory disclosures |
| **A - Asset Quality** | 35% | Non-performing lease asset ratio, Provision coverage ratio, Special-mention lease asset ratio, Industry concentration | Annual reports |
| **L - Liquidity & Funding** | 15% | Financing channel diversity, Asset-liability maturity matching, Short-term debt ratio | Annual reports |
| **E - Earnings** | 15% | ROA, ROE, Net interest spread, Non-interest income ratio | Annual reports |
| **S - Sensitivity** | 15% | Single client concentration, Industry concentration (aircraft/shipping/equipment), Regional concentration | Annual reports + estimation |

### 6.3 Leasing Key Indicator Scoring

| Indicator | Calculation | Strong (8-10) | Adequate (4-7) | Weak (0-3) | Weight |
|---|---|---|---|---|---|
| **C - Capital adequacy ratio** | Net capital / Risk-weighted assets | > 15% | 10-15% | < 10% (< 8% triggers regulatory action) | 50% |
| **C - Leverage multiple** | Total assets / Net assets | < 5x | 5-8x | > 8x (> 10x extreme) | 50% |
| **A - Non-performing lease asset ratio** | Non-performing lease assets / Total lease assets | < 0.5% | 0.5-2.0% | > 2.0% (> 5% severe) | 30% |
| **A - Provision coverage ratio** | Lease asset loss provisions / Non-performing lease assets | > 250% | 150-250% | < 150% | 20% |
| **A - Special-mention lease asset ratio** | Special-mention lease assets / Total lease assets | < 2% | 2-5% | > 5% | 15% |
| **A - Industry concentration (largest industry)** | Largest industry exposure / Total lease assets | < 20% | 20-35% | > 35% | 15% |
| **E - Net interest spread** | Lease yield - Funding cost rate | > 2.5% | 1.5-2.5% | < 1.5% | 30% |
| **E - ROE** | Net profit / Average net assets | > 10% | 6-10% | < 6% | 25% |
| **E - ROA** | Net profit / Average total assets | > 1.2% | 0.8-1.2% | < 0.8% | 25% |
| **L - Asset-liability maturity mismatch** | Weighted asset duration - Weighted liability duration | < 1 year | 1-3 years | > 3 years | 35% |
| **L - Bank borrowing ratio** | Bank borrowing / Total liabilities | < 50% | 50-70% | > 70% | 30% |
| **S - Single client concentration** | Largest single client exposure / Net capital | < 15% | 15-30% | > 30% | 40% |
| **S - Top 3 industry concentration** | Top 3 industry exposure / Total lease assets | < 40% | 40-60% | > 60% | 30% |

### 6.4 Financial Leasing Credit Analysis Key Points

1. **Parent bank support is the lifeline.** Most financial leasing companies are bank subsidiaries. Credit quality is highly dependent on the parent bank -- if the parent bank is willing and able to support during difficulties, the leasing company's liquidity and asset quality risks are manageable. But if the parent bank itself has difficulties (e.g., city commercial bank-affiliated leasing), risks compound.

2. **Industry concentration determines cyclical risk exposure.**
   - Aviation leasing (aircraft): Affected by global aviation cycles, severely impacted during COVID, but recovery value relatively high (aircraft easily monetizable)
   - Ship leasing: Strongly cyclical, greatly affected by global trade indicators
   - Equipment leasing (construction machinery / manufacturing equipment): Linked to fixed asset investment cycle
   - Vehicle leasing: Affected by new energy vehicle transition (residual value risk)

3. **Lease asset quality assessment is challenging.**
   - Unlike bank loans which have standardized five-category classification
   - Recovery rates for leased assets (especially specialized equipment) are highly uncertain
   - Lessee credit primarily comprises SMEs and private enterprises, risk higher than various enterprise clients of banks

4. **Maturity mismatch is a structural risk.** Lease assets typically have longer terms (3-8 years), while liabilities are mainly bank borrowings and short-term notes within 1 year. If the financing market tightens, the liquidity risk of short-term borrowing funding long-term assets is immediately exposed.

### 6.5 Leasing Veto Conditions

1. **Capital adequacy ratio < 8%** (regulatory red line)
2. **Non-performing lease asset ratio > 5%**
3. **Provision coverage ratio < 100%**
4. **Leverage multiple > 10x** (excessive leverage)
5. **Parent bank credit rating downgraded to below investment grade AND parent bank declares no further support**

---

## 7. Cross-Sub-Type General Indicators

### 7.1 Government Support and Systemic Importance Assessment

| Indicator | Description | Applicable Sub-Type |
|---|---|---|
| Systemically important financial institution (D-SIB/G-SIB) list | Included in central bank systemic importance list -> clear capital requirements but also stronger support expectations | Banks |
| Central/local government shareholding ratio | Higher state ownership -> stronger implicit government support expectation | All |
| Employee size / branch coverage | Employees > 100K / nationwide branch network -> "too big to fail" | Banks |
| Listing status | Listed financial enterprises have higher transparency and financing channels | All |
| Whether part of "financial holding company" pilot | FHCs subject to stricter regulation but also access policy support | All |

**Government Support Score Correction:**

| Condition | Score Correction |
|---|---|
| Listed as D-SIB/G-SIB + state-controlled | +1.0 (five-dimension score final value) |
| State-controlled but non-D-SIB/G-SIB | +0.5 |
| Local state-owned (city commercial banks etc.) | +0.3 (depends on local fiscal strength) |
| Private-controlled + low systemic importance | +0 (no additional support) |
| Private + high-risk asset structure | -0.5 (government may not support) |

### 7.2 Related Party Risk

Equity/business interconnections between financial enterprises are an important contagion channel for systemic risk:

| Linkage Type | Risk | Scenarios Requiring Attention |
|---|---|---|
| Bank -> Leasing | Leasing risks transmit back to parent bank | Leasing NPL ratio rising + parent bank capital deficiency |
| Bank -> Insurance | Insurer default causes bank investment losses | Bank holds insurance subordinated debt or negotiated deposits |
| Securities -> Bank | Securities firm financial bonds held by banks | Securities proprietary losses -> banks holding bonds disposed |
| Financial holding group internal | Internal transactions and risk isolation effectiveness | Case examples: subsidiary risk isolation failure |

### 7.3 ESG Factors (Financial Bond Specialization)

| ESG Dimension | Banks | Securities | Insurance | Leasing |
|---|---|---|---|---|
| **E - Green Finance** | Green credit/green bond ratio | Green IB business scale | Green investment ratio | Green lease asset ratio |
| **S - Inclusive Finance** | SME lending | Investor education/protection | Inclusive insurance coverage | SME leasing ratio |
| **G - Governance Risk** | Related transactions / insider control | Practitioner integrity | Sales compliance / lapse disputes | Violation lending / compliance penalties |

---

## 8. Financial Bond Public Data Quality Assessment

### 8.1 Data Accessibility

| Data Type | Accessibility | Coverage | Update Frequency | Reliability |
|---|---|---|---|---|
| Capital adequacy ratio | Mandatory disclosure | All licensed financial institutions | Quarterly | High (banking/securities regulator co-regulated) |
| NPL ratio | Mandatory disclosure | All licensed banks | Quarterly | Medium-high (consistent statistical definitions, but may be hidden) |
| Solvency ratio | Mandatory disclosure | All licensed insurers | Quarterly | High (strict solvency reporting system) |
| Net capital / leverage ratio | Mandatory disclosure | Securities firms | Monthly | Medium-high |
| Provision coverage ratio | Mandatory disclosure | Banks | Quarterly | Medium (provision adjustment flexibility) |
| Investment yield | Partial disclosure | Insurance / some banks | Annual | Medium (definition differences) |
| LCR | Large banks / joint-stock banks disclose | Only listed companies | Semi-annual | Medium-high |
| Related transactions | Mandatory disclosure | Listed companies / bond issuers | Annual | Medium |
| Equity structure | Publicly searchable | All | Real-time | High |
| Regulatory penalties | Publicly searchable | All | Real-time | High (regulatory announcements) |

### 8.2 Data Quality Comparison with Corporate Bonds

| Comparison Item | Financial Bonds | Corporate Bonds |
|---|---|---|
| Mandatory disclosure system | Yes (banking/securities/central bank regulators etc.) | Partial industries have (e.g., environmental/safety) |
| Key indicator standardization | High (uniform regulatory definitions) | Low (large variance across industries) |
| Audit quality | High (primarily Big 4) | Medium (some private enterprise audit quality questionable) |
| Forward-looking data | Low (regulation focuses more on current period) | Medium (industry forward data relatively rich) |
| **Summary** | **Data quality far better than corporate bonds, but real risks are often off-balance-sheet** |

### 8.3 "Good Data but Risk Harder to Capture" Paradox

**Financial bond analysis faces a special contradiction:**

- **Financial enterprises have the best public data quality among all bond issuers** -- regulatory mandatory, uniform definitions, strict auditing, high frequency
- **But the real risks are often not in this data** -- a failed mid-sized bank showed all disclosed data as "compliant" before takeover, with NPL ratio only 1.5% and capital adequacy ratio 12.5%
- **Key risks are hidden in:**
  1. **Off-balance-sheet assets**: Wealth management products / interbank CDs / channel business -- accounting for 10-30% of total bank assets, disclosure extremely non-transparent
  2. **Asset quality divergence**: Average NPL ratio of 1.5% masks the fact that NPL ratios for real estate/LGFV/overcapacity industry exposure may be > 5%
  3. **Related transactions**: Major shareholders channeling funds through related loans / non-standard instruments -- data not public
  4. **Maturity mismatch**: The extent of borrowing short and lending long cannot be directly read from the balance sheet
  5. **Concentration**: Actual exposure to single industry / single client / single region has limited disclosure

**Core Principle: In financial bond analysis, "data absence" itself is the most important risk signal.**

---

## 9. Special Risks in Financial Bond Analysis

### 9.1 Systemic Risk and Contagion Risk

Risk correlation among financial enterprises is far higher than among corporate enterprises:
- **Interbank risk**: One bank experiencing risk -> interbank lending/CD market contraction -> all financial institutions dependent on interbank funding come under pressure
- **Asset price linkage**: Interest rate/credit spread increase -> all banks/insurers/securities firms holding large bond portfolios simultaneously suffer losses
- **Run risk**: Market confidence collapse -> deposits/wealth management products/premiums flow out simultaneously -> liquidity crisis
- **Regulatory policy shifts**: Such as new asset management regulations impacting bank wealth management, de-shadow banking effects on asset management scale

**Analysis Recommendation:** Analysis of a single financial enterprise must be paired with an overall market environment assessment; indicators cannot be viewed in isolation.

### 9.2 Off-Balance-Sheet Risk (Implicit Leverage)

| Off-Balance-Sheet Item | Scale Estimate | Risk Type | Disclosure Transparency |
|---|---|---|---|
| Bank wealth management products (guaranteed/non-guaranteed) | Significant | Break of implicit guarantee + asset impairment | Low (underlying assets not transparent) |
| Interbank CDs | Significant | Rollover risk + interest rate volatility | Medium (aggregate data available but no look-through) |
| Channel business / trust beneficiary rights | Notable (peak already compressed) | Underlying asset quality + compliance risk | Extremely low |
| Stock pledge repo | Moderate (securities firm side) | Stock price decline forced margin call | Medium |
| Insurance "universal life" accounts | Moderate | Asset-liability mismatch + negative spread | Low |

**Off-balance-sheet risk assessment cannot rely on the analyzed entity's own disclosure, and requires:**
1. Industry aggregate off-balance-sheet trends (central bank / financial regulator publications)
2. Public bank wealth management annual reports (partial)
3. Third-party statistical data from interbank market / exchange
4. Comparing the off-balance-sheet / on-balance-sheet ratio of similar institutions -- abnormally high means risk

### 9.3 Interest Rate Environment Impact

Financial enterprises (especially banks and insurers) are highly sensitive to the interest rate environment:

| Interest Rate Scenario | Impact on Banks | Impact on Insurers | Impact on Securities Firms |
|---|---|---|---|
| Rates continuously declining | NIM compression -> earnings pressure; bond holdings gain price appreciation (hedge) | Negative spread widening -> long-term toxicity accumulation; bond holdings gain valuation uplift | Bond proprietary benefits; brokerage/IB neutral |
| Rates rapidly rising | NIM improvement; bond holdings suffer losses (interest rate risk) | Liability cost increase lags -> short-term improvement but lapse ratio may rise | Bond proprietary losses; trading volume increases |
| Inverted yield curve (short > long) | Negative carry -> asset-liability management difficulty | Short-term reinvestment yield below long-term average funding cost | Funding operations loss-making |
| Prolonged low rates | NIM compressed to limit -> bank earnings model under pressure | Negative spread continuously accumulating -> some companies may become insolvent | Proprietary yield decline |

### 9.4 Fintech Impact

| Impact Type | Method | Affected Entities |
|---|---|---|
| Payment disintermediation | Digital payment platforms capturing deposits | Banks (especially those with high retail deposit ratios) |
| Lending disintermediation | Internet consumer/SME lending diverting | Banks (credit card / consumer lending) |
| Wealth management disintermediation | Money market funds replacing bank liquidity products | Banks / Insurance |
| Digital cost reduction | AI replacing human advisors / customer service | Securities / Insurance |

---

## 10. Cross-Validation Linkage Between Financial and Corporate Bonds

### 10.1 Financial Analysis Track Entering the Dual-Track Architecture

After generating the "five-dimension score," the financial analysis track enters the dual-track cross-validation workflow alongside corporate bond scoring:

```
Financial Five-Dimension Score
    │
    ▼
Financial Rating Mapping (AAA -> D)
    │
    ├──> Track A: Fundamental Score ──────────┐
    │                                         │
    ├──> Track B: Market Signals              ├──> Cross-Validation -> Final Rating
    │        (spreads/volatility/             │
    │         fund flows/rating events)        │
    │                                         │
    └──> Data Completeness Report ────────────┘
```

### 10.2 Special Handling of Validation Differences

The weight of Track B signals should be adjusted between financial and corporate enterprises:

| Validation Status | Corporate Enterprise Handling | Financial Enterprise Handling |
|---|---|---|
| Divergence A (A good + B bad) | Trust A preferentially | **Also trust A preferentially, but need to investigate:** Is the market worried about off-balance-sheet risk or systemic contagion? |
| Divergence B (A bad + B good) | Trust A preferentially | **Also trust A preferentially, but need to investigate:** Is pricing elevated due to government support expectations? |
| Consensus (all good) | Confirm | **Note systemic risk superposition:** Individual financial enterprise may be sound but if the industry as a whole is deteriorating, industry trends may overwhelm individual quality |
| Consensus (all bad) | Confirm | **Confirm but need to add:** Financial enterprise rating downgrades may trigger chain reactions (interbank credit tightening -> liquidity deterioration) |

### 10.3 Assessment Involving Financial Enterprises as External Support

When corporate credit analysis needs to assess external support from banks/securities/insurance (such as bank credit support in the external support framework), the five-dimension score from this framework can serve as the basis for assessing the supporting entity's credit quality.

---

## 11. Scoring Output Template

```
+=========================================================+
|          Financial Credit Analysis Report                |
|          [Sub-Type: Bank / Securities / Insurance / Leasing] |
+=========================================================+
| Composite Score: [0-10]                                  |
| Rating: [AAA -> D]                                      |
| Analysis Date: [YYYY-MM-DD]                             |
| Confidence: [High/Medium/Low]                            |
+=========================================================+
| Five-Dimension Score Detail:                             |
|   C - Capital Adequacy: [0-10] x [Weight] = [Score]     |
|   A - Asset Quality:   [0-10] x [Weight] = [Score]     |
|   L - Liquidity:       [0-10] x [Weight] = [Score]     |
|   E - Earnings:        [0-10] x [Weight] = [Score]     |
|   S - Sensitivity:     [0-10] x [Weight] = [Score]     |
+=========================================================+
| Core Findings:                                          |
|  [3-5 line core analysis conclusion]                    |
+=========================================================+
| Key Risks:                                              |
|  1. [Risk 1] - [Severity] - [Mitigation Suggestion]     |
|  2. [Risk 2] - [Severity] - [Mitigation Suggestion]     |
|  3. [Risk 3] - [Severity] - [Mitigation Suggestion]     |
+=========================================================+
| Data Completeness: [Signal density percentage]           |
|  Data Gaps: [List key existing gaps]                    |
|  Gap Impact: [Impact on rating confidence]              |
+=========================================================+
| Cross-Validation: [Consensus / Divergence A / Divergence B]|
|  Track B Signals: [Spreads/Volatility/Fund Flows/Rating Events]|
|  [If divergent] What is the market concerned about: [Analysis] |
+=========================================================+
| Veto Check: [Passed / Triggered (list triggered items)] |
+=========================================================+
```

---

## 12. Version History and To-Do Items

### v0.0.1 (2026-07-09) -- Initial Release

- Financial industry analysis track design (parallel to corporate bond pyramid)
- CAMELS bank sub-framework (C/A/M/E/L/S six dimensions, with market-specific adjustments)
- Securities firm sub-framework (five dimensions + specialized indicators + stock pledge risk)
- Insurance sub-framework (five dimensions + negative spread + solvency)
- Financial leasing sub-framework (five dimensions + parent bank support + industry concentration)
- Cross-sub-type general indicators (government support / related parties / ESG)
- Financial bond public data quality assessment
- Special risk analysis for financial bonds (off-balance-sheet / contagion / interest rates / fintech)

### To-Do Items

| # | Item | Priority | Description |
|---|---|---|---|
| 1 | **Forward-looking validation of financial bonds** | High | Select 1-2 banks/securities firms for forward validation, similar to corporate bond case studies |
| 2 | **Backward-looking validation of financial bonds** | High | Validate historical cases of failed banks and other distressed financial institutions |
| 3 | **Systemically important bank list update** | Medium | Track D-SIB/G-SIB list changes and additional capital requirements |
| 4 | **Solvency II Phase 2 impact assessment** | Medium | Impact of updated solvency regulations on solvency ratios |
| 5 | **Financial leasing parent bank support scoring refinement** | Medium | Design sub-framework for assessing parent bank support willingness and capability |
| 6 | **TLAC gap analysis** | Low | Add TLAC compliance analysis for systemically important banks |
| 7 | **Off-balance-sheet risk quantification method** | Low | Develop methodology for estimating off-balance-sheet risk scale based on public data |
| 8 | **Fintech impact quantification** | Low | Quantify the degree of fintech impact on different types of financial institutions |

---

## Related Content

- [Dual-Track Analysis Methodology](dual-track-methodology.md) -- Track A+B architecture, rating mapping, cross-validation matrix
- [Mosaic Engine](mosaic-engine.md) -- Signal extraction, assembly, completeness assessment
- [External Support Framework](external-support-framework.md) -- Government/group/strategic investor support analysis for financial institutions
- [LGD and Recovery Rate Framework](lgd-recovery-framework.md) -- Recovery rate assessment for financial bonds (particular attention to subordinated debt and capital instruments)
- [Industry Classification and Analysis Framework](industry-framework.md) -- Ten-dimension scoring, industry type judgment
