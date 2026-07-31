# Financial Deep Dive Sub-Module — Appendix

> Appendix to `financial-deep-dive.md` — version tracks the parent document; reference
> material (worked examples, derivations, historical validation) moved here in
> the 2026-07 restructure. Read on demand.

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
