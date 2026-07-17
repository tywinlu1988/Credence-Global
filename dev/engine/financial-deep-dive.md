# Financial Deep Dive Sub-Module

**Version**: v0.0.1 | **Date**: 2026-07-17 | **Status**: Published

---

> **Note:** This module is a deep-dive sub-module of the L4 Financial Layer within the Dual-Track Methodology (dual-track-methodology.md). It provides detailed calculation specifications for the financial layer indicators across all 7 industries in the industry framework (industry-framework.md). The module is structured as three-statement linkage + four-dimensional deep analysis + three-scenario sensitivity matrix, with additional extensions for sovereign and banking sector analysis.

---

## Table of Contents

- [A. Three-Statement Linkage Core Logic](#a-three-statement-linkage-core-logic)
- [B. Working Capital Efficiency Analysis](#b-working-capital-efficiency-analysis)
- [C. Debt Maturity Scheduling](#c-debt-maturity-scheduling)
- [D. FCF Generation Capacity](#d-fcf-generation-capacity)
- [E. Scenario Sensitivity Matrix](#e-scenario-sensitivity-matrix)
- [F. Sovereign-Specific Metrics](#f-sovereign-specific-metrics)
- [G. Bank CAMELS Framework](#g-bank-camels-framework)
- [Appendix: Data Account Reconciliation (IFRS/US GAAP)](#appendix-data-account-reconciliation-ifrsus-gaap)

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

## F. Sovereign-Specific Metrics

### F.1 Scope and Purpose

This section extends financial deep-dive analysis to sovereign borrowers. Sovereign credit analysis requires metrics beyond corporate financial statements, covering fiscal sustainability, external vulnerability, and institutional strength.

### F.2 Core Sovereign Credit Metrics

| Dimension | Metric | Formula | Interpretation | Data Source |
|-----------|--------|--------|---------------|-------------|
| **Fiscal Sustainability** | General Government Debt / GDP | Total government gross debt / nominal GDP | <40%: low; 40-70%: moderate; 70-100%: elevated; >100%: high risk (thresholds vary by institutional strength) | IMF WEO; national statistical agencies |
| | Fiscal Balance / GDP | (Revenue - Expenditure) / GDP | >0%: surplus; 0% to -3%: manageable; -3% to -6%: concerning; <-6%: risky | Same as above |
| | Primary Balance / GDP | Fiscal balance excluding net interest payments | Positive primary balance: debt-stabilizing; Negative: debt may be on unsustainable path | Same as above |
| | Interest / Revenue | Interest expense / total government revenue | <5%: low burden; 5-10%: moderate; 10-15%: elevated; >15%: severe constraint | Budget execution reports |
| **External Vulnerability** | External Debt / GDP | Total external debt (public + private) / GDP | <50%: low; 50-100%: moderate; >100%: elevated | World Bank IDS; IIF |
| | Foreign Exchange Reserves / Short-Term External Debt | Greenspan-Guidotti rule | >100%: adequate coverage of short-term external debt | IMF IFS; central bank data |
| | Reserves / Imports (months) | Gross reserves / monthly imports | >6 months: strong; 3-6 months: adequate; <3 months: vulnerable | Same as above |
| | Current Account Balance / GDP | (Exports - Imports + Net Income + Net Transfers) / GDP | Surplus: net external creditor; deficit >5%: potentially vulnerable to sudden stops | IMF WEO |
| **Debt Structure** | Average Maturity (years) | Weighted average maturity of government debt | Longer = lower rollover risk | National debt management reports |
| | Foreign Currency Debt Share | Foreign currency debt / total debt | Higher share = greater vulnerability to exchange rate depreciation | Public debt bulletins |
| | Concessional Debt Share | Concessional / total external debt | Higher = lower financing cost and more stable creditor base | World Bank IDS |
| | Holders' composition | Share held by residents vs. non-residents; central bank vs. banks vs. non-banks | Higher domestic institutional holding = more stable investor base | National central bank financial accounts |

### F.3 Sovereign Rating Drivers and Thresholds

Indicator thresholds for sovereign creditworthiness depend on a country's institutional strength and income level. The following framework uses a composite sovereign risk score:

| Indicator | Very Strong (100-80) | Strong (80-60) | Medium (60-40) | Weak (40-20) | Very Weak (20-0) |
|-----------|---------------------|---------------|---------------|-------------|-----------------|
| Debt / GDP | <30% | 30-55% | 55-75% | 75-100% | >100% |
| Fiscal Balance / GDP | >+2% | 0% to +2% | -3% to 0% | -6% to -3% | <-6% |
| Primary Balance / GDP | >+3% | +1% to +3% | -1% to +1% | -3% to -1% | <-3% |
| Interest / Revenue | <3% | 3-7% | 7-12% | 12-18% | >18% |
| Reserves / ST External Debt | >200% | 150-200% | 100-150% | 50-100% | <50% |
| Current Account / GDP | >+3% | 0% to +3% | -3% to 0% | -6% to -3% | <-6% |
| GDP per Capita Growth (3yr avg) | >5% | 3-5% | 1-3% | 0-1% | <0% |
| Inflation (CPI, annual avg) | <2% | 2-4% | 4-8% | 8-15% | >15% |
| Rule of Law (WGI percentile) | >90th | 75-90th | 50-75th | 25-50th | <25th |
| Political Stability (WGI percentile) | >80th | 60-80th | 40-60th | 20-40th | <20th |

### F.4 Sovereign Debt Stress Test Scenarios

The following sovereign-specific scenarios supplement the general corporate scenario framework:

| Scenario Type | Key Variables | Typical Shock Magnitude | Transmission Channels |
|--------------|--------------|------------------------|---------------------|
| **Interest Rate Shock** | Financing cost increase; bond yield spike | +200bp to +500bp (depending on current spread) | Higher interest expense -> wider fiscal deficit -> higher debt -> adverse debt dynamics |
| **GDP Growth Shock** | Real GDP growth decline | -3pp to -5pp (recession stress) | Lower revenue -> wider deficit -> higher debt/GDP (denominator effect) |
| **Exchange Rate Shock** | Currency depreciation against USD | -15% to -30% (emerging markets) | Higher FX debt service -> wider fiscal deficit; imported inflation -> central bank response |
| **Commodity Price Shock** | Export commodity price decline | -20% to -40% (for commodity exporters) | Lower export revenue -> wider current account deficit -> FX reserve depletion |
| **Contingent Liability Shock** | Materialization of SOE or banking sector contingent liabilities | 10-30% of GDP (banking crisis; SOE bailout) | One-time increase in debt level; may shift debt trajectory |
| **Sudden Stop Shock** | Capital flow reversal; loss of market access | Complete loss of access for 3-12 months | Forced adjustment; potential balance-of-payments crisis; potential sovereign default |

### F.5 Sovereign Stress Test Output Template

| Metric | Base | Bear | Severe | Assessment |
|--------|------|------|--------|------------|
| Debt / GDP | XX% | XX% (+Δ) | XX% (+Δ) | G/Y/O/R |
| Fiscal Balance / GDP | XX% | XX% | XX% | G/Y/O/R |
| External Debt Service / Reserves | XX% | XX% | XX% | G/Y/O/R |
| Gross Financing Need / GDP | XX% | XX% | XX% | G/Y/O/R |
| Sovereign Spread (bp) | XX | XX | XX | G/Y/O/R |

**Key Threshold Levels:**

| Risk Level | Debt/GDP (EM) | Debt/GDP (DM) | Interest/Revenue | Gross Financing Need / GDP |
|-----------|--------------|--------------|-----------------|--------------------------|
| Robust | <40% | <60% | <5% | <10% |
| Moderate | 40-60% | 60-90% | 5-10% | 10-15% |
| Elevated | 60-80% | 90-120% | 10-15% | 15-20% |
| High Risk | >80% | >120% | >15% | >20% |

---

## G. Bank CAMELS Framework

### G.1 Scope and Purpose

This section extends financial deep-dive analysis to banking institutions using the CAMELS supervisory framework. CAMELS is the internationally recognized framework (adopted by the U.S. Federal Reserve, FDIC, OCC, and adapted by banking regulators worldwide) for assessing bank financial condition and identifying potential solvency and liquidity issues.

### G.2 CAMELS Dimensions

| Component | Full Name | Weight (Supervisory) | Focus |
|-----------|-----------|---------------------|-------|
| **C** | Capital Adequacy | 20% | Ability to absorb losses; regulatory capital ratios |
| **A** | Asset Quality | 20% | Quality of loans, securities, and other assets; credit risk profile |
| **M** | Management | 25% | Board and management capability; strategic planning; governance |
| **E** | Earnings | 15% | Profitability; sustainability of earnings; earnings quality |
| **L** | Liquidity | 10% | Ability to meet cash flow obligations; funding stability |
| **S** | Sensitivity to Market Risk | 10% | Exposure to interest rate, foreign exchange, and other market risks |

**Total Score:** Composite 1 (strongest) to 5 (weakest)

### G.3 Capital Adequacy (C)

**Regulatory Framework:** Basel III (as implemented by local jurisdiction)

| Metric | Formula | Strong (1) | Adequate (2) | Watch (3) | Weak (4-5) | Data Source |
|--------|--------|-----------|-------------|-----------|------------|-------------|
| **CET1 Ratio** | Common Equity Tier 1 / Risk-Weighted Assets | >12% | 10.5-12% | 8-10.5% | <8% (below regulatory minimum) | Pillar 3 disclosures; regulatory filings |
| **Tier 1 Ratio** | Tier 1 Capital / RWA | >13% | 11.5-13% | 9-11.5% | <9% | Same as above |
| **Total Capital Ratio** | Total Capital / RWA | >15% | 13-15% | 10.5-13% | <10.5% | Same as above |
| **Leverage Ratio** | Tier 1 Capital / Total Exposure | >5% | 4-5% | 3-4% | <3% (below Basel III minimum of 3%) | Same as above |
| **Capital Conservation Buffer** | CET1 above minimum requirement | >2.5% (buffer fully met) | 1.5-2.5% | 0-1.5% | <0% (buffer breached) | Same as above |
| **TLAC / MREL (G-SIBs)** | Total Loss-Absorbing Capacity / RWA | >20% | 18-20% | 16-18% | <16% (below minimum) | Resolution authority disclosures |
| **Tangible Common Equity / Tangible Assets** | (Common Equity - Intangibles) / (Total Assets - Intangibles) | >8% | 6-8% | 4-6% | <4% | Balance sheet |

### G.4 Asset Quality (A)

| Metric | Formula | Strong (1) | Adequate (2) | Watch (3) | Weak (4-5) | Data Source |
|--------|--------|-----------|-------------|-----------|------------|-------------|
| **NPL Ratio** | Non-Performing Loans / Gross Loans | <1% | 1-3% | 3-5% | >5% | Financial statements; regulatory filings |
| **NPL Coverage Ratio (LLR/NPL)** | Loan Loss Reserves / NPLs | >150% | 100-150% | 70-100% | <70% | Same as above |
| **Provisioning Coverage Ratio** | Total provisions / NPLs | >100% | 80-100% | 60-80% | <60% | Same as above |
| **Net Charge-Off (NCO) Ratio** | Net charge-offs / Average Loans | <0.5% | 0.5-1.0% | 1.0-2.0% | >2.0% | Same as above |
| **Loan Growth (3yr CAGR)** | CAGR of gross loans | 5-15% (measured growth) | 15-20% or 0-5% | 20-25% or negative | >25% (too fast) or < -5% (contracting) | Same as above |
| **Sector Concentration (CRE, C&I, Consumer)** | Share of loans in each highly cyclical sector | <20% in any single cyclical sector | 20-30% | 30-40% | >40% | Segment reporting |
| **Geographic Concentration** | Share of loans in any single stressed region | <15% | 15-25% | 25-35% | >35% | Geographic segment data |
| **Forbearance Ratio** | Forborne loans / Gross loans | <1% | 1-3% | 3-5% | >5% | IFRS 9 / CECL disclosures |
| **Stage 2 / Stage 3 Ratio (IFRS 9)** | (Stage 2 + Stage 3) / Total Loans | <10% | 10-20% | 20-30% | >30% | IFRS 9 disclosure notes |

### G.5 Management (M)

Management assessment is inherently qualitative but can be guided by structural and performance indicators:

| Indicator | Strong (1) | Adequate (2) | Watch (3) | Weak (4-5) | Data Source |
|-----------|-----------|-------------|-----------|------------|-------------|
| **Management Stability** | Stable team; average tenure >5 years | Some recent changes but orderly | CFO/CEO departed in last 12 months | Multiple key departures; no succession plan | Annual report; regulatory filings |
| **Regulatory History** | No enforcement actions in 5+ years | Minor regulatory findings addressed | Current regulatory MOU / formal agreement | Cease-and-desist order; PCA prompt corrective action | Regulator websites |
| **Strategic Clarity** | Clear, measurable strategic plan; consistent execution | Reasonable strategy with minor pivots | Unclear strategy; frequent changes | No coherent strategy; reactive decisions | Investor presentations; annual reports |
| **Risk Management Framework** | Independent CRO; board risk committee; ERM framework | Adequate risk governance | Risk management gaps identified | Material risk management failures | Pillar 3 disclosures; regulatory reports |
| **Internal Audit** | Independent IA; direct board reporting | IA exists but not fully independent | IA under-resourced or constrained | No effective IA function | Annual report (corporate governance section) |
| **Board Oversight** | Majority independent directors; financial expertise | Complies with independence requirements | Board lacks relevant expertise | Board dominated by management or insiders | Proxy statements; governance reports |
| **Succession Planning** | Documented plan for all key roles | Informal but adequate | No clear successor for CEO/CFO | Key person risk; no plan | Engagement with IR; governance disclosures |

### G.6 Earnings (E)

| Metric | Formula | Strong (1) | Adequate (2) | Watch (3) | Weak (4-5) | Data Source |
|--------|--------|-----------|-------------|-----------|------------|-------------|
| **ROAA** | Net Income / Average Total Assets | >1.2% | 0.8-1.2% | 0.4-0.8% | <0.4% or negative | Income statement + balance sheet |
| **ROAE** | Net Income / Average Common Equity | >12% | 8-12% | 4-8% | <4% | Same as above |
| **Net Interest Margin (NIM)** | Net Interest Income / Average Earning Assets | >3.5% | 2.5-3.5% | 1.5-2.5% | <1.5% | Same as above |
| **Efficiency Ratio** | Non-Interest Expense / (Net Interest Income + Non-Interest Income) | <55% | 55-65% | 65-75% | >75% | Income statement |
| **Cost of Risk** | Provision Expense / Average Gross Loans | <0.5% | 0.5-1.0% | 1.0-2.0% | >2.0% | Income statement + balance sheet |
| **Non-Interest Income / Total Revenue** | Non-interest Income / Total Income | 20-40% (diversified) | 15-20% or 40-50% | 10-15% or >50% (excessive reliance) | <10% or >60% | Income statement |
| **Earnings Volatility** | Standard deviation of quarterly ROAA over 3 years | <10% of mean ROAA | 10-20% | 20-30% | >30% | Quarterly financial data |
| **Dividend Payout Ratio** | Dividends / Net Income | 30-50% (sustainable) | 20-30% or 50-60% | 0-20% or 60-80% | >80% (excessive) or negative payout | Cash flow statement |

### G.7 Liquidity (L)

| Metric | Formula | Strong (1) | Adequate (2) | Watch (3) | Weak (4-5) | Data Source |
|--------|--------|-----------|-------------|-----------|------------|-------------|
| **LCR** | Liquidity Coverage Ratio: High-Quality Liquid Assets / Net Cash Outflows over 30 days | >150% (well above 100% minimum) | 120-150% | 100-120% | <100% (below minimum) | Pillar 3 disclosures |
| **NSFR** | Net Stable Funding Ratio: Available Stable Funding / Required Stable Funding | >120% | 110-120% | 100-110% | <100% (below minimum) | Same as above |
| **Loan-to-Deposit Ratio** | Gross Loans / Total Deposits | 70-90% (traditional banking) | 60-70% or 90-100% | 50-60% or 100-110% | <50% or >110% | Balance sheet |
| **Deposit Concentration** | Top 20 depositor share of total deposits | <10% | 10-20% | 20-30% | >30% | Regulatory filings (limited public disclosure) |
| **Wholesale Funding Dependence** | (Wholesale deposits + market funding) / Total Liabilities | <15% | 15-25% | 25-35% | >35% | Funding disclosure notes |
| **Core Deposits / Total Deposits** | Insured/stable retail deposits / total deposits | >70% | 60-70% | 50-60% | <50% | Same as above |
| **Liquid Assets / Total Assets** | Cash + government securities / total assets | >15% | 10-15% | 5-10% | <5% | Balance sheet |
| **Undrawn Committed Lines / Total Assets** | Confirmed undrawn credit lines / total assets | >5% | 3-5% | 1-3% | <1% | Regulatory filings |

### G.8 Sensitivity to Market Risk (S)

| Metric | Formula | Strong (1) | Adequate (2) | Watch (3) | Weak (4-5) | Data Source |
|--------|--------|-----------|-------------|-----------|------------|-------------|
| **EVE / Economic Value of Equity Sensitivity** | Change in EVE for +/- 200bp parallel interest rate shock | <10% of Tier 1 capital | 10-20% | 20-30% | >30% | Regulatory filings; Pillar 3 |
| **Net Interest Income Sensitivity** | Change in NII for +/- 200bp over 12 months | <5% of NII | 5-10% | 10-15% | >15% | Same as above |
| **Trading Book VaR (99%, 1-day)** | Value at Risk as % of Tier 1 capital | <0.5% | 0.5-1.0% | 1.0-2.0% | >2.0% | Pillar 3; annual report risk section |
| **FX Exposure** | Net open FX position / Tier 1 capital | <5% | 5-15% | 15-25% | >25% | Regulatory filings |
| **Derivatives / Total Assets (notional)** | Derivative notional / Total assets | <100% | 100-300% | 300-500% | >500% | Annual report; derivatives note |
| **Counterparty Credit Risk** | Peak positive exposure / Tier 1 capital | <20% | 20-50% | 50-100% | >100% | Regulatory filings |

### G.9 CAMELS Composite Score and Credit Implications

| Composite Score | Rating | Description | Credit Implication |
|----------------|--------|-------------|-------------------|
| **1** | Strong | Well-managed; resistant to external shocks; all dimensions satisfactory | Minimal default risk; strong credit quality |
| **2** | Satisfactory | Fundamentally sound; minor weaknesses correctable | Low default risk; investment grade compatible |
| **3** | Watch | Moderate weaknesses requiring attention; vulnerable to adverse conditions | Moderate default risk; may correspond to lower IG or HY |
| **4** | Weak | Serious weaknesses; inadequate risk management; vulnerable without corrective action | High default risk; likely HY |
| **5** | Critically Deficient | Extremely weak; immediate corrective action needed; probable failure | Imminent default risk |

### G.10 Bank-Specific Stress Test Parameters

For banks, the following stress parameters supplement the general corporate scenario framework:

| Parameter | Base | Bear | Severe | Source |
|-----------|------|------|--------|--------|
| NPL Ratio increase | Unchanged | +2pp | +5pp | Historical bank crisis data |
| Provisioning Cost (bps of loans) | Current level | Current + 100bp | Current + 200bp | Basel calibration studies |
| Net Interest Margin compression | Unchanged | -20bp | -50bp | Central bank stress test scenarios |
| Loan Growth | Current trend | -50% of trend | 0% (no growth) | Macro downturn scenarios |
| Market shock (govt bond yield increase) | Unchanged | +100bp (parallel shift) | +200bp (bear flattener) | Historical market stress events |
| Deposits outflow (% of total) | 0% | 3% over 30 days | 10% over 30 days | Historical bank run/stress scenarios |

---

## Appendix: Data Account Reconciliation (IFRS/US GAAP)

### Cash Flow Statement Accounts

| Analysis Metric | Cash Flow Statement Line Item | IFRS/US GAAP Note |
|----------------|------------------------------|-------------------|
| CFO (Cash from Operations) | Net cash provided by operating activities | IFRS: may include interest and dividends paid/received at discretion; US GAAP: interest paid and dividends received are operating, dividends paid are financing |
| Capital Expenditure (Capex) | Purchases of property, plant, equipment, and intangible assets | Excludes M&A-related payments |
| Interest Expense | Interest paid (cash flow) OR interest expense (income statement) | IFRS: interest paid can be in CFO or CFF; US GAAP: interest paid is CFO. For cross-border comparison, use income statement interest expense consistently |
| FCF | CFO - Capex | Simplified; excludes interest tax shield adjustment |
| Dividends Paid | Dividends paid | IFRS: can be operating or financing; US GAAP: financing |

### Balance Sheet Accounts

| Analysis Metric | Balance Sheet Line Items | Note |
|----------------|-------------------------|------|
| Trade Receivables | Trade receivables + Notes receivable (current) | IFRS 9: expected credit loss allowance deducted; US GAAP: CECL allowance deducted. Remove allowance for comparability |
| Inventory | Inventory (raw materials + WIP + finished goods) | IFRS: LIFO prohibited; US GAAP: LIFO permitted. If US company uses LIFO, adjust for LIFO reserve |
| Trade Payables | Trade payables + Notes payable (current) | Include accrued expenses only if they represent trade payables |
| Short-term Borrowings | Short-term borrowings / Bank overdrafts | IFRS: overdrafts often netted against cash (unlike US GAAP). Reclassify if needed |
| Current Portion of Non-Current Liabilities | Current portion of long-term debt / bonds payable / lease liabilities | IFRS 16: all leases included; US GAAP: operating lease liabilities classified as current portion of operating leases |
| Bonds Payable | Bonds payable (non-current) | IFRS: amortized cost or fair value; US GAAP: generally amortized cost |
| Long-term Borrowings | Long-term borrowings (non-current) | By maturity date |
| Lease Liabilities (Non-current) | Non-current lease liabilities | IFRS: all leases; US GAAP: finance leases only (operating leases presented separately) |
| Undrawn Committed Lines | Off-balance-sheet disclosure: "Bank Credit Facilities" / "Committed Lines of Credit" | Disclosed in notes; not on balance sheet |

### Income Statement Accounts

| Analysis Metric | Income Statement Line Item | Note |
|----------------|--------------------------|------|
| Revenue | Revenue / Net Sales | IFRS 15 / ASC 606: five-step model. Revenue is net of returns, discounts, and allowances |
| Cost of Revenue | Cost of sales / Cost of revenue | IFRS: includes cost of inventory sold; US GAAP: same, but LIFO may affect COGS |
| Gross Margin | (Revenue - Cost of Revenue) / Revenue | Compare within accounting framework; adjust for IFRS vs US GAAP differences (leases, stock compensation) |
| Interest Expense (Income Statement) | Interest expense (within finance costs) | IFRS: finance costs include all borrowing costs; US GAAP: interest expense classification varies |
| Depreciation and Amortization (D&A) | Depreciation + Amortization (PP&E + intangible assets) | IFRS: depreciation of ROU asset included; US GAAP: operating lease expense is a single line (no separate D&A). Adjust for comparability |
| EBITDA | Net Income + Tax + Interest + D&A | **IFRS vs US GAAP adjustment:** For US GAAP reporters with operating leases add back implied D&A component; IFRS lessees already have D&A in EBITDA. This can cause 5-15% EBITDA differences for lease-intensive companies. |
| Non-recurring / Exceptional Items | Restructuring charges, impairment losses, gains/losses from asset sales | IFRS: "exceptional items" classification is not specifically defined but used in practice; US GAAP: "unusual and/or infrequent" items classified separately in non-operating section |

### IFRS vs US GAAP: Key Adjustment Table for Cross-Border Analysis

| Metric | IFRS Treatment | US GAAP Treatment | Adjustment for Comparability |
|--------|---------------|------------------|---------------------------|
| **Lease-adjusted EBITDA** | EBITDA includes D&A of ROU asset (IFRS 16) | EBITDA excludes operating lease expense (operating lease is single line in operating expenses) | Add back 2/3 of operating lease expense to US GAAP EBITDA (approximation: 2/3 = implicit D&A component; 1/3 = implicit interest) |
| **Pre-provision Net Revenue (PPNR) — Banks** | Net interest income + non-interest income - operating expenses (before provisions) | Same concept; classification differences in fee income may apply | Adjust for specific line item classification differences |
| **Tangible Common Equity (TCE)** | Common equity - goodwill - intangible assets (excluding servicing rights) | Common equity - goodwill - intangible assets (excluding mortgage servicing rights) | Generally comparable; check whether capitalized development costs (IFRS) should be excluded for TCE |
| **Loan Loss Provision** | IFRS 9 ECL: 12-month (Stage 1) or lifetime (Stage 2/3) expected losses | ASC 326 CECL: lifetime expected losses at origination | CECL provision is typically larger than IFRS 9. When comparing, note the methodology difference |
| **Risk-Weighted Assets (RWA)** | Basel III standardized or IRB approaches | Basel III standardized or IRB (US modifications) | US implementation may differ from EU implementation; compare within same regime |

---

## Related Content

- [Industry Classification and Framework](industry-framework.md) — L4 financial layer specifications and thresholds by industry
- [Dual-Track Methodology](dual-track-methodology.md) — Cash flow deep-dive linkage to rating mapping
- [Engine Architecture Overview](engine-overview.md) — Core concepts and overall architecture
- [LGD Recovery Framework](lgd-recovery-framework.md) — Loss given default estimation
- [External Support Framework](external-support-framework.md) — Sovereign, multilateral, and group support assessment
