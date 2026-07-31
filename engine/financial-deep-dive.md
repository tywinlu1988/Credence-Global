# Financial Deep Dive Sub-Module

**Version**: v0.3.0 | **Date**: 2026-07-17 | **Status**: Published

---

> **Note:** This module is a deep-dive sub-module of the L4 Financial Layer within the Dual-Track Methodology (dual-track-methodology.md). It provides detailed calculation specifications for the financial layer indicators across all 7 industries in the industry framework (industry-framework.md). The module is structured as three-statement linkage + four-dimensional deep analysis + three-scenario sensitivity matrix, with additional extensions for sovereign and banking sector analysis.

---

> **Reading guide**: §§A-D contain the executable methodology — three-statement
> linkage, working capital, debt scheduling, and FCF capacity. §E (scenario
> sensitivity) is required for stress-test paths.
> §F, §G, and the Appendix (sovereign metrics, bank CAMELS, IFRS/GAAP


## Table of Contents

- [A. Three-Statement Linkage Core Logic](#a-three-statement-linkage-core-logic)
- [B. Working Capital Efficiency Analysis](#b-working-capital-efficiency-analysis)
- [C. Debt Maturity Scheduling](#c-debt-maturity-scheduling)
- [D. FCF Generation Capacity](#d-fcf-generation-capacity)
- [E. Scenario Sensitivity Matrix](#e-scenario-sensitivity-matrix)

---

## A. Three-Statement Linkage Core Logic

### A.1 Core Flow Diagram

The three financial statements form a closed-loop linkage through cash flows:

```
Income Statement                    Cash Flow Statement                    Balance Sheet
---------------                     -----------------                    ----------------
Revenue                              Cash Flow from Operations (CFO)      Cash & Equivalents
  - Cost of Revenue                    = Net Income                       (Beginning Balance)
  - Operating Expenses                   + D&A                               |
  - Interest Expense                     - Working Capital Changes           | CFO Inflow
  - Income Tax                           - Interest/Taxes Paid              | Capex Outflow
  = Net Income                           + Other Adjustments                | Debt Service Outflow
    |                                                                       | Financing Inflow
    |        Add back D&A                                                  | Dividend Outflow
    |        Subtract working capital changes            CF from Investing     v
    |        Subtract capex                  = -Capital Expenditures      Cash & Equivalents
    |                                   -----------------                (Ending Balance)
    +--------------------------------> FCF = CFO - Capex
                                         |
                                         +-- Debt service: interest + maturing debt
                                         +-- Investment: new projects / M&A
                                         +-- Dividends: shareholder returns
```

### A.2 Three-Statement Reconciliation

| Reconciliation | Formula | Verification Method |
|---|---|---|
| Cash Change Verification | Ending Cash - Beginning Cash = CFO + CFI + CFF | Sum of three cash flow sections should equal balance sheet cash change |
| FCF Verification | FCF = Net Income + D&A - Working Capital Changes - Capex | Indirect calculation from income statement validates CFO |
| Debt Service Verification | FCF should be >= Interest Expense + Next 12-Month Debt Maturities | Cash remaining after debt service is true free cash flow |
| Working Capital Verification | Working Capital Change = Delta AR + Delta Inventory - Delta AP | Should match balance sheet working capital changes |

### A.3 IFRS vs. US GAAP Reconciliation Notes

Analysts should be aware of key differences between IFRS and US GAAP that affect financial deep-dive calculations:

| Item | IFRS | US GAAP | Impact on Analysis |
|------|------|---------|-------------------|
| **Revenue Recognition** | IFRS 15 (same as US GAAP ASC 606 after convergence) | ASC 606 | Largely converged; differences may arise in interim reporting and specific industry guidance |
| **Lease Accounting** | IFRS 16: lessees recognize right-of-use (ROU) asset and lease liability; single classification | ASC 842: similar ROU model but dual classification (finance vs. operating leases in P&L) | EBITDA different: IFRS classes all lease as finance (D&A + interest); US GAAP operating lease expense recorded as single operating expense. Adjust for comparability. |
| **Inventory Costing** | LIFO prohibited | LIFO permitted | For US companies using LIFO, DSO/DIO calculations must adjust for LIFO reserve |
| **Development Costs** | Capitalization required if criteria met | Capitalization generally prohibited (expensed as incurred) | R&D-intensive companies: IFRS balance sheet includes capitalized development costs; US GAAP generally does not. Affects asset base and D&A. |
| **Borrowing Costs** | Capitalization required for qualifying assets | Capitalization required for qualifying assets (substantially similar) | Generally comparable; subtle differences in what qualifies |
| **Impairment (Long-lived Assets)** | Single-step: compare carrying amount to recoverable amount (higher of FVLCD and VIU) | Two-step: test recoverability (undiscounted cash flows), then measure impairment (fair value) | US GAAP impairment less frequent (higher threshold). For LGD analysis, IFRS impairment may be more timely. |
| **Financial Instruments (Impairment)** | IFRS 9: expected credit loss (ECL) model — 12-month ECL (Stage 1); lifetime ECL if credit risk increased significantly (Stage 2); lifetime ECL + interest on net carrying (Stage 3) | ASC 326 (CECL): lifetime expected losses recognized upon origination or purchase | CECL is more conservative (larger upfront allowance); affects book value and regulatory capital. Important for bank analysis. |
| **Statement of Cash Flows** | Interest paid can be classified as operating or financing; dividends paid as operating or financing | Interest paid must be operating; dividends paid must be financing | FCF calculation may treat interest differently; adjust for cross-border comparability |
| **Extraordinary Items** | Prohibited | Prohibited (since 2016) | Largely converged |

**Adjustment Note for Cross-Border Comparisons:** When comparing financial metrics across companies reporting under IFRS vs. US GAAP, analysts should identify the key reconciling items (leases, development costs, impairment methodology) and make pro-forma adjustments to ensure comparability. For purposes of this engine, IFRS-based metrics are the default baseline; for US GAAP reporters, adjust the following as noted in individual line items.

---

## B. Working Capital Efficiency Analysis

### B.1 Four Core Metrics

| Metric | Full Name | Formula | Data Source (IFRS/US GAAP Accounts) | Meaning |
|--------|-----------|--------|--------------------------------------|---------|
| DSO | Days Sales Outstanding | Trade Receivables / (Revenue / 365) | Balance Sheet: Trade Receivables (incl. notes receivable); Income Statement: Revenue | Average days to collect from customers |
| DIO | Days Inventory Outstanding | Inventory / (Cost of Revenue / 365) | Balance Sheet: Inventory (raw materials/WIP/finished goods); Income Statement: Cost of Revenue | Average days inventory is held before sale |
| DPO | Days Payables Outstanding | Trade Payables / (Cost of Revenue / 365) | Balance Sheet: Trade Payables (incl. notes payable); Income Statement: Cost of Revenue | Average days to pay suppliers |
| CCC | Cash Conversion Cycle | DSO + DIO - DPO | Calculated from the above three | Complete cycle days from cash out to cash in |

### B.2 General Thresholds

| Metric | Healthy | Watch | Danger | Data Source |
|--------|---------|-------|--------|-------------|
| DSO | <60 days | 60-90 days | >90 days (>180 days severe) | Annual report receivables note |
| DIO | Industry-dependent (see below) | Industry-dependent | Industry-dependent | Inventory note (raw/WIP/finished) |
| DPO | 30-90 days | <30 or >90 without reasonable explanation | >120 days (may indicate distress) | Payables note (aging analysis) |
| CCC | <100 days | 100-150 days | >150 days | Calculated from above |

### B.3 Seven-Industry Differentiated DSO/DIO/DPO/CCC Thresholds

| Industry | DSO Healthy | DSO Danger | DIO Healthy | DIO Danger | DPO Reference | CCC Reference | Notes |
|----------|------------|-----------|------------|-----------|--------------|--------------|-------|
| **Solar/Energy Storage** | <60 days | >90 days | <45 days | >60 days triggers impairment test; >120 days high concern | 30-90 days | >150 days watch | Module prices decline weekly; inventory depreciation very fast |
| **Semiconductor/IC** | Fabless <45d; Foundry <60d | >90d (sanctioned customers separate) | Fabless <60d; Foundry <90d | >120 days | 30-60 days | <100d healthy | Check DSO by customer; sanctioned entity payment channels may be restricted |
| **Capital Equipment / Machine Tools** | <180 days (long acceptance cycles) | >365 days | <120 days (incl. WIP) | WIP accumulation + payable contraction = order cancellations | 30-120 days | >200d watch | DSO naturally long; distinguish contractual milestones vs. actual collections |
| **Biopharma — Pharma** | <90 days | >120 days | <60 days | >90 days | 30-90 days | >120d watch | Biotech focuses on cash runway; working capital less relevant |
| **Medical Devices** | Distributor <90d; Direct <180d | Distrib >120d; Direct >240d | <90 days | >120d channel stuffing | 30-90 days | >150d watch | Public hospital payment cycles are long; analyze by channel |
| **NEV — OEM** | <45 days | >90 days | <45 days | >60 days faces price-cut risk | 30-120 days | <100d | Includes subsidy/credit receivables; separate these out |
| **NEV — Supply Chain** | <90 days | >120 days | <60 days | >90 days | Squeezed by OEMs; 30-60d | >180d watch | OEM payment pressure significant |
| **Data Centers** | <30 days (prepaid model) | DSO rising trend | N/A (no physical inventory) | N/A | N/A | CCC naturally negative; positive CCC indicates operational issue | Prepaid rental model; negative CCC is normal |

### B.4 Working Capital Spike Detection Rules

| Spike Signal | Detection Condition | Possible Meaning | Response |
|---|---|---|---|
| DSO single-quarter jump >30 days | Current quarter DSO - prior quarter DSO > 30 days | Customer payment deterioration or aggressive revenue recognition | Check Top 5 customer aging; verify revenue recognition policy |
| DIO single-quarter jump >30 days | Current DIO - prior DIO > 30 days | Product obsolescence or inventory mismatch | Check finished goods aging; assess impairment provision adequacy |
| DPO single-quarter jump >45 days | Current DPO - prior DPO > 45 days | Supplier relationship deterioration or cash pressure | Check supplier payment terms changes; investigate liquidity pressure |
| CCC deterioration >50 days | Current CCC - prior CCC > 50 days | Overall working capital cycle efficiency decline | Comprehensive three-statement linkage; assess cash runway |
| Payable growth far exceeding revenue growth | Delta AP growth rate - Delta Revenue growth rate > 20pp | Paying suppliers late to preserve cash | Unsustainable short-term optimization; subsequent retaliatory payment pressure |

---

## C. Debt Maturity Scheduling

### C.1 Maturity Distribution Construction Method

Core philosophy: **The relevant metric is not "short-term debt ratio" (static snapshot), but the dynamic debt maturity profile over the next 12/24/36 months.**

Data source path (annual report note extraction):

```
Short-term borrowings            -> Note: "Short-term borrowings" details
  +-- Credit borrowings           -> By maturity
  +-- Secured/pledged borrowings -> By maturity
  +-- Discounted / factoring     -> By maturity

Current portion of long-term debt -> Note: "Current portion of non-current liabilities"
  +-- Current portion of long-term borrowings -> By maturity
  +-- Current portion of bonds payable        -> By maturity
  +-- Current portion of lease liabilities    -> By maturity

Bonds payable                    -> Note: "Bonds payable"
  +-- Maturing this period       -> By maturity
  +-- Maturing next 12 months    -> By maturity
  +-- 12-36 month maturity       -> By maturity

Long-term borrowings             -> Note: "Long-term borrowings"
  +-- 1-2 years                  -> By maturity
  +-- 2-3 years                  -> By maturity
  +-- 3+ years                   -> By maturity
```

### C.2 Maturity Profile Construction

Summarize the above data into quarterly/ monthly maturity buckets:

| Maturity Window | Short-term Borrowings | Current Portion of LTD | Bonds Payable | Long-term Borrowings (Installments) | Total | Cumulative % |
|----------------|----------------------|----------------------|--------------|-----------------------------------|-------|-------------|
| Next 1-3 months | A1 | B1 | C1 | D1 | S1 | S1/Total Debt |
| Next 4-6 months | A2 | B2 | C2 | D2 | S2 | (S1+S2)/Total Debt |
| Next 7-12 months | A3 | B3 | C3 | D3 | S3 | (S1+S2+S3)/Total Debt |
| 13-24 months | A4 | B4 | C4 | D4 | S4 | (S1..S4)/Total Debt |
| 25-36 months | A5 | B5 | C5 | D5 | S5 | (S1..S5)/Total Debt |
| >36 months | A6 | B6 | C6 | D6 | S6 | 100% |

### C.3 Danger Classification

| Level | Condition | Assessment | Reference Cases |
|-------|-----------|-----------|-----------------|
| Smooth | Next 12M maturities < 30% of total debt | Even distribution; low refinancing pressure | -- |
| Watch | Next 12M maturities 30-50% | Need to confirm committed credit lines are sufficient | -- |
| High Risk | Next 12M maturities 50-70% | May not roll in adverse market conditions | -- |
| Extreme Risk | Next 12M maturities >70% or single-month concentration >20% | **Maturity wall** — same pattern observed in multiple corporate defaults globally | Enron (2001): significant near-term debt; Lehman (2008): short-term funding mismatch; many others |

### C.4 Committed Credit Line Coverage Ratio

```
Committed Credit Line Coverage = Undrawn committed credit facilities / Next 12M maturing debt
```

| Ratio | Assessment |
|-------|-----------|
| >2.0x | Ample — sufficient committed capacity to cover maturities |
| 1.0-2.0x | Adequate — need to monitor the match between facility expiry and debt maturity |
| 0.5-1.0x | Insufficient — part of maturing debt relies on operating cash flow or new financing |
| <0.5x | Dangerous — high concentration of near-term maturities with insufficient backup liquidity |

---

## D. FCF Generation Capacity

### D.1 Core Ratios

| Metric | Formula | Data Source | Meaning |
|--------|--------|-------------|---------|
| FCF | CFO - Capital Expenditures | Cash flow statement: CFO - capex (purchases of PP&E + intangible assets) | True discretionary cash flow |
| FCF / Revenue | FCF / Revenue x 100% | Cash flow statement + income statement | Cash conversion per dollar of revenue |
| FCF / Interest | FCF / Interest Expense | Cash flow statement: interest paid (or income statement: interest expense) | FCF coverage of interest |
| FCF / Total Debt | FCF / Total Interest-bearing Debt | FCF / (short-term borrowings + current portion LTD + LTD + bonds payable + lease liabilities) | FCF repayment capacity for total debt |

### D.2 FCF Classification Matrix

| FCF/Revenue | FCF/Interest | FCF/Total Debt | Classification | Industry Typical |
|------------|-------------|---------------|---------------|-----------------|
| >10% | >5x | >15% | Strong cash generator | Data centers (stable rental), mature Pharma |
| 5-10% | 3-5x | 8-15% | Healthy | Medical devices, capital equipment leaders |
| 0-5% | 1-3x | 3-8% | Maintenance | Solar manufacturing, semiconductor foundries |
| -5%-0% | 0-1x | 0-3% | Fragile | NEV early stage, Biotech |
| <-5% | <0x | <0% | Bleeding | Persistent loss-making; potential Ponzi financing |

### D.3 Seven-Industry FCF Characteristics

| Industry | FCF Profile | FCF/Revenue Typical Range | Special Notes |
|----------|------------|--------------------------|---------------|
| **Solar/Energy Storage** | Highly cyclical; often negative during capacity expansion | -5% to 8% | Negative FCF during capacity expansion is not necessarily dangerous; assess expansion ROI |
| **Semiconductor/IC** | Fabless lighter asset, FCF usually positive; Foundry heavy capex, FCF volatile | Fabless: 5-15%; Foundry: -10% to 10% | Capex cadence drives FCF; distinguish maintenance vs. growth capex |
| **Capital Equipment** | Order-based production; FCF concentrated in Q4 deliveries | -5% to 10% | Watch Q4 concentration seasonality; annualize |
| **Biotech (Pre-revenue)** | No commercial revenue; deeply negative FCF | -50% to -20% | Negative FCF is normal; focus on cash runway, not FCF |
| **Pharma (Revenue-stage)** | Mature blockbuster products generate stable FCF | 10-25% | Patent cliff may cause FCF discontinuity |
| **Medical Devices** | Consumables: stable FCF; capital equipment: volatile | 10-20% | "Device + consumable" lock-in provides more predictable FCF |
| **NEV — OEM** | Large early-stage investment; deeply negative FCF | -20% to 5% | Positive FCF is often a profitability inflection signal |
| **NEV — Supply Chain** | Squeezed by OEM margin pressure; FCF usually 0-8% | 0-8% | Monitor receivable turnover deterioration |
| **Data Centers** | Stable rental income; strong FCF | 15-30% | Maintenance capex is high proportion; distinguish maintenance vs. expansion |

---

## E. Scenario Sensitivity Matrix

> **Source:** Risk Management Standards Audit (G2 — Stress Testing Rigor Assessment)
> **Modification Note:** Shock magnitudes upgraded to meet Basel "severe but plausible" standard; Severe scenario introduced with industry historical calibration anchors; Reverse stress testing module added; Second-order feedback loop effects incorporated

### E.1 Three-Scenario Parameter Settings

| Parameter | Base | Bear | Severe |
|-----------|------|------|--------|
| Revenue change | Baseline | -10% | -30% (calibrated to industry historical maximum drawdown) |
| Gross margin change | Baseline | -5 ppts | -15 ppts |
| Financing cost change | Baseline | +100bp | +200bp |

**Scenario Design Principles (Risk Management Audit G2):**
- **Base:** Baseline scenario using most recent financial data
- **Bear:** Moderate deterioration scenario for conventional margin-of-safety assessment
- **Severe:** "Severe but historically precedented" — not the absolute worst possible, but a magnitude of shock that the industry has actually experienced in history
  - Calibration anchor: each industry's "historical maximum drawdown" (the actual shock magnitude experienced in the industry's most severe historical recession)
  - Severe parameters should not exceed historical maximum drawdown but should approach it

**Seven-Industry Severe Scenario Calibration Anchors (Based on Historical Data):**

| Industry | Historical Shock Event | Max Revenue Decline | Max Gross Margin Compression | Severe Calibration Rationale |
|----------|----------------------|-------------------|---------------------------|-----------------------------|
| **Solar/Storage** | 531 Policy Shift (2018 China); Overcapacity Cycle (2023-2024 Global) | -35% | -20pp | Post-531 industry revenue fell ~30% on average; leader LONGi revenue -25% |
| **Semiconductor/IC** | Downcycle (2022-2023); US Export Controls Escalation | -25% | -12pp | Memory chip revenue down 40% in 2022; foundry down 15-20% |
| **Capital Equipment** | Manufacturing investment downturn (2015-2016 Global) | -25% | -10pp | Cyclical downturn typically 20-25% revenue decline |
| **Pharma** | VBP/Procurement Shock (2020-2022 China); Patent Cliff (various) | -30% | -18pp | Core product included in procurement: gross margin compression 15-20pp possible |
| **Medical Devices** | Procurement + FF Management (2021-2023); Reimbursement cuts (various markets) | -25% | -15pp | Coronary stent VBP cut >90% historically extreme; mid-range shock selected |
| **NEV — OEM** | Subsidy Phase-out (2019-2020, various markets); Price War (2024) | -30% | -15pp | 2024 price war compressed industry gross margin >10pp |
| **Data Centers** | Supply glut cycle (2023-2024); Hyperscaler demand pause | -15% | -10pp | Asset-light model provides stronger shock resistance |

> **Note:** Severe parameters should be recalibrated semi-annually based on latest industry historical data. Sources: WIND / CITIC industry indices or equivalent industry index providers for each market.

### E.2 Scenario Transmission Path

```
Revenue Change --> Revenue Change --> Net Income Change --> CFO Change --> FCF Change
Gross Margin Change --> Gross Profit Change --> Net Income Change --> CFO Change --> FCF Change
Financing Cost Change --> Interest Expense Change --> Net Income Change --> FCF/Interest Change

Second-order effects (feedback loop under stress):
  Financing cost increase --> Finance charge increase --> Net income decrease
    --> Internal cash flow reduction
    --> External financing dependence increases --> Leverage rises
    --> Rating downgrade pressure
    --> Financing cost further increases (negative feedback; Severe scenario only)

Asset impairment feedback (Severe scenario):
  Revenue decline + Gross margin compression --> Inventory write-down
    --> Asset impairment loss --> Net equity decline
    --> Debt-to-asset ratio increases --> Cross-default clause trigger risk
```

### E.3 Scenario Calculation Logic

**Note:** Calculation logic is a simplified linear model. Severe scenario requires second-order effect corrections (see E.7).

| Calculation Item | Formula | Notes |
|-----------------|---------|-------|
| Adjusted Revenue | Base Revenue x (1 + Revenue Change Rate) | -- |
| Adjusted Gross Profit | Adjusted Revenue x (Base Gross Margin + Gross Margin Change) | Severe scenario must layer on asset impairment |
| Adjusted Net Income (Simplified) | (Adjusted Gross Profit - Base Operating Expenses) x (1 - Tax Rate) | -- |
| Adjusted CFO (Simplified) | Adjusted Net Income + D&A (assumed unchanged) | Severe scenario: consider WC deterioration |
| Adjusted FCF | Adjusted CFO - Capex (assumed unchanged) | Severe scenario: capex may be cut |
| Adjusted Interest Expense | Base Interest Expense x (1 + Financing Cost Change) | Severe scenario: second-order financing cost increase |
| Adjusted Interest Coverage | Adjusted EBITDA / Adjusted Interest Expense | -- |
| Adjusted FCF/Interest | Adjusted FCF / Adjusted Interest Expense | -- |

### E.4 Scenario Output Template

| Scenario | Metric | Base Value | Scenario Value | Change | Safety |
|----------|--------|-----------|---------------|--------|--------|
| **Base** | Interest Coverage | X | X | -- | G/Y/O/R |
| | FCF/Interest | Y | Y | -- | G/Y/O/R |
| | Cash Runway (months) | Z | Z | -- | G/Y/O/R |
| **Bear** | Interest Coverage | X | X_down | -Delta | -- |
| | FCF/Interest | Y | Y_down | -Delta | -- |
| | Cash Runway | Z | Z_down | -Delta | -- |
| **Severe** | Interest Coverage | X | X_severe | -Delta_severe | -- |
| | FCF/Interest | Y | Y_severe | -Delta_severe | -- |
| | Cash Runway | Z | Z_severe | -Delta_severe | -- |
| **Reverse** | Critical Revenue Decline | -- | X_crit | -- | -- |
| | Critical Gross Margin Compression | -- | Y_crit | -- | -- |
| | Critical Financing Cost Increase | -- | Z_crit | -- | -- |

### E.5 Margin of Safety Criteria

| Safety Level | Bear Interest Coverage | Bear FCF/Interest | Bear Cash Runway | Assessment |
|-------------|----------------------|------------------|-----------------|------------|
| Robust | >3.0x | >2.0x | >18 months | Safe even under severe deterioration |
| Resilient | 1.5-3.0x | 1.0-2.0x | 12-18 months | Moderate deterioration absorbable |
| Fragile | 1.0-1.5x | 0.5-1.0x | 6-12 months | Near default under Bear scenario |
| Dangerous | <1.0x | <0.5x | <6 months | Certain default under Bear scenario |

**Severe Scenario Supplementary:** If any metric falls into the Dangerous range under Severe scenario, the entity would certainly default under extreme shock; this should trigger a "tail risk warning" flag in the composite rating output, but not an automatic downgrade (Severe is not the base case).

### E.6 Critical Point Identification

Identify the level of deterioration that would trigger debt service difficulty:

```
Debt Service Difficulty Trigger:
  (Bear Scenario Interest Coverage < 1.0x) OR
  (Bear Scenario FCF/Interest < 0.5x and sustained) OR
  (Bear Scenario Cash Runway < 6 months AND no undrawn committed credit facilities)

Critical Deterioration Magnitude:
  Maximum tolerable revenue decline = X% (beyond which interest coverage <1.0x)
  Maximum tolerable gross margin compression = Y ppts
  Maximum tolerable financing cost increase = Z bp
```

**Reverse Stress Test** (Risk Management Audit G2): Calculate the shock magnitude that would cause interest coverage = 1.0x — "How much deterioration can the entity absorb before it defaults?"

```
Critical Revenue Decline:
  Let (Adjusted EBITDA / Adjusted Interest Expense) = 1.0x
  Solve: Adjusted Revenue = Adjusted Interest Expense / (Base Gross Margin + Margin Adjustment)
  Output: Critical Revenue Decline = (Base Revenue - Adjusted Revenue) / Base Revenue

Critical Gross Margin Compression:
  Let (Adjusted EBITDA / Adjusted Interest Expense) = 1.0x
  Solve: Critical Gross Margin = Adjusted Interest Expense / Adjusted Revenue + Expense Ratio
  Output: Critical Gross Margin Compression = Base Gross Margin - Critical Gross Margin

Reverse Output:
  "This entity can tolerate a revenue decline of approximately X% or gross margin compression
   of approximately Y ppts without triggering interest coverage <1.0x"
```

### E.7 Second-Order Effects and Feedback Loops (Severe Scenario Only)

Under Severe scenario, apply the following second-order effects to correct the simplified linear model:

| Second-Order Effect | Trigger Condition | Correction Logic |
|--------------------|-----------------|-----------------|
| **Inventory Write-Down** | Revenue decline >20% AND gross margin compression >10pp | Inventory write-down = Inventory balance x 10% (assumed impairment rate); additional reduction in net income |
| **Working Capital Freeze** | Revenue decline >25% | DSO passively extends 20 days (customer payment delays); DIO extends 30 days (obsolescence); additional WC consumption |
| **Financing Cost Second-Order Increase** | Severe scenario assumes 1-2 notch rating downgrade | Financing cost increases further 50-100bp on top of +200bp (reflecting credit spread widening from rating migration) |
| **Capex Reduction** | FCF negative AND cash runway <12 months | Entity actively cuts 50% of non-essential capex; alleviates FCF pressure |
| **Asset Impairment — Net Equity Erosion** | Sustained losses >2 years | Net equity decline -> Debt-to-asset ratio increases -> Triggers additional collateral requirements or cross-default |

### E.8 Industry Calibration Factors

Scenario parameters differ systematically by industry. The table below provides industry-specific calibration factors:

| Industry | Bear Revenue Factor | Severe Revenue Factor | Bear GM Factor | Severe GM Factor | Notes |
|----------|-------------------|---------------------|---------------|-----------------|-------|
| **Solar/Energy Storage** | 1.0x | 1.2x | 1.0x | 1.3x | Strong cyclicality; GM compression faster than revenue decline |
| **Semiconductor — Fabless** | 0.8x | 0.9x | 0.8x | 1.0x | Fabless slightly more counter-cyclical |
| **Semiconductor — Foundry** | 1.0x | 1.1x | 1.0x | 1.1x | Heavy fixed depreciation; high revenue sensitivity |
| **Capital Equipment** | 0.9x | 1.0x | 0.9x | 0.9x | Long order cycles; lagging revenue fluctuation |
| **Biotech (Pre-revenue)** | N/A | N/A | N/A | N/A | No stable revenue; use cash runway stress test instead |
| **Pharma** | 0.8x | 1.0x | 0.8x | 1.2x | Procurement shock severe; revenue relatively stable |
| **Medical Devices** | 0.9x | 0.9x | 1.0x | 1.0x | Consumables model counter-cyclical; capital equipment volatile |
| **NEV — OEM** | 1.0x | 1.2x | 1.0x | 1.0x | Price war pressures GM; revenue relatively resilient |
| **NEV — Supply Chain** | 1.1x | 1.3x | 1.0x | 1.1x | Dual pressure from OEM squeeze and order fluctuation |
| **Data Centers** | 0.6x | 0.7x | 0.8x | 0.8x | Rental model shock-resistant; monitor renewal rates |

**Usage:** Multiply the default scenario parameters (Bear: -10% / +100bp; Severe: -30% / +200bp) by the industry-specific factor. For example, Solar Severe revenue factor 1.2x -> actual revenue decline = -30% x 1.2 = -36%.

> **Note:** Calibration factors are based on historical event back-analysis. Update quarterly based on latest industry macro data.

---



## Related Content

- [Industry Classification and Framework](industry-framework.md) — L4 financial layer specifications and thresholds by industry
- [Dual-Track Methodology](dual-track-methodology.md) — Cash flow deep-dive linkage to rating mapping
- [Engine Architecture Overview](engine-overview.md) — Core concepts and overall architecture
- [LGD Recovery Framework](lgd-recovery-framework.md) — Loss given default estimation
- [External Support Framework](external-support-framework.md) — Sovereign, multilateral, and group support assessment