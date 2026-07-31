# Governance and Financial Fraud Risk Analysis Module — Appendix

> Appendix to `governance-fraud-risk.md` — version tracks the parent document; reference
> material (worked examples, derivations, historical validation) moved here in
> the 2026-07 restructure. Read on demand.

---

## 3. Related-Party Transaction Anomaly Detection

### 3.1 Related-Party Transaction Volume Detection

| Detection Item | Threshold | Signal Intensity | Data Source |
|--------------|----------|-----------------|-------------|
| **Related-party revenue / Total revenue > 20%** | Annual related-party transaction amount / Total revenue > 20% | High | Annual report related-party summary |
| **Related-party revenue / Total revenue > 50%** | Entity is dependent on related parties for more than half its revenue | High | Same as above |
| **Related-party gross margin anomaly** | Related-party transaction margin +/- Independent transaction margin > 10pp | High | Segment reporting / related-party details note |
| **Related-party sales growth too fast** | Related-party revenue growth rate > total revenue growth rate x 3 | Medium | Annual / quarterly report |
| **Related-party procurement concentration** | Top 5 related-party suppliers account for >80% of all related-party purchases | Medium | Supplier disclosure |

### 3.2 Related-Party Fund Occupation Detection

| Detection Item | Threshold | Signal Intensity | Data Source |
|--------------|----------|-----------------|-------------|
| **"Other receivables" from related parties** | Related-party other receivables / Total assets > 3% (or > equivalent USD 50M) | High | Other receivables note |
| **"Prepayments" to related parties** | Related-party prepayments with aging >1 year (substance is fund occupation) | High | Prepayments note |
| **Related-party fund occupation audit report** | External audit identifies non-operational fund occupation | High | Fund occupation special audit report |
| **Intercompany netting anomaly** | Same related party has large receivable and large payable simultaneously (possible circular trade for revenue inflation) | Medium | Receivable/payable related-party details |

**International Context — Related-Party Fraud:**
- **Wirecard (2020):** The most egregious modern related-party fraud. Related-party transactions with third-party acquirers (Al Alam Solutions, Senjo Group) accounted for the majority of reported revenue in the alleged fraud. Cash balances held at trustee accounts were entirely fictitious; related-party relationships were used to create the appearance of legitimate payment processing operations that did not exist.
- **Satyam (2009):** Founder Ramalinga Raju fabricated revenue by creating fictitious customer contracts and generating false invoices through related parties. The company had ~USD 1bn in fictitious cash on the balance sheet.
- **Luckin Coffee (2020):** Fabricated ~$310M in revenue through a related-party supply chain. The company used related entities controlled by the Chairman to create fake purchase orders, supply chain transactions, and sales receipts.

### 3.3 Related-Party Guarantee Detection

| Detection Item | Threshold | Signal Intensity | Data Source |
|--------------|----------|-----------------|-------------|
| **External guarantees / Net Equity > 50%** | Guarantee balance to third parties / net equity > 50% (excluding wholly-owned subsidiaries) | High | Guarantee disclosure |
| **Large guarantee to single related party** | Guarantee to single related party > 50% of that party's net equity | High | Related-party guarantee details |
| **Guarantee balance exceeding net equity** | Total external guarantees / net equity > 100% (material guarantee exposure) | High | Same as above |
| **Cross-guarantee chain / guarantee circle** | Multiple entities guaranteeing each other (guarantee network; regional financial contagion risk) | Medium | Annual report + regional guarantee network analysis |

### 3.4 Related-Party Transaction Analytical Logic

```
Step 1: Identify all related parties
  +-- Extract related-party list from annual report "Related-party Relationships" section
  +-- Include: ultimate controller, subsidiaries, associates/JVs, key management and their close family

Step 2: Quantify related-party transaction volume
  +-- Total related-party transactions / Revenue -> if >20%, trigger red flag
  +-- Related-party receivables / Total assets -> if >5%, verify each significant item
  +-- Related-party guarantees / Net equity -> if >50%, trigger red flag

Step 3: Anomaly pattern detection
  +-- Compare related-party transaction margin vs. independent transaction margin
      -> Deviation >10pp = potential tunneling / self-dealing indicator
  +-- Same related party with large receivable and payable simultaneously
      -> Potential circular trade indicator
  +-- Quarter-end / year-end concentrated increase
      -> Potential window-dressing transaction

Step 4: Cash flow tracing
  +-- Trace changes in "Other receivables - related parties" (year-over-year change)
  +-- If related-party other receivables persistently growing without plausible explanation
      -> Confirm fund occupation

Output:
  Related-party transaction risk level = Normal / Watch / High
  Specific risk items (at least 1-3 most dangerous signals)
```

---


---

## 5. Quantitative Screening Tools

### 5.1 Benford's Law

**Concept:** In naturally occurring numerical data sets, the leading digit distribution follows a predictable pattern: digit 1 appears ~30.1% of the time, digit 2 ~17.6%, down to digit 9 at ~4.6%. Significant deviations from this distribution may indicate data manipulation.

| Application | Method | Threshold | Interpretation |
|------------|--------|-----------|---------------|
| **Revenue digits** | Compare first-digit distribution of quarterly/monthly revenue figures to Benford's distribution | Chi-square test or MAD (Mean Absolute Deviation) > 0.015 | Significant deviation suggests possible revenue fabrication |
| **Expense digits** | Same analysis on expense line items | Same | Fabricated expenses tend to deviate from natural distribution |
| **Balance sheet items** | Same analysis on accounts receivable, inventory, fixed assets | Same | Certain patterns of manipulation are detectable at aggregate level |
| **Journal entry level** | Most powerful at transaction level (underlying journal entries) | -- | Limited by data availability; most effective for internal auditors |

**Limitations:**
1. Not all manipulated data fails Benford's Law — sophisticated fraud may be constructed to conform to Benford's distribution
2. Benford's Law is less reliable for small data sets (fewer than 100 observations)
3. Certain accounting items may legitimately deviate from Benford's distribution (e.g., thresholds, regulatory limits)
4. Benford's Law is a preliminary screening tool, not a conclusive fraud detection method

### 5.2 Beneish M-Score

**Concept:** The M-Score is a mathematical model using 8 financial ratios to detect earnings manipulation. Developed by Professor Messod Beneish, the model identifies companies most likely to have manipulated their earnings.

| Variable | Ratio | Formula | Weight |
|----------|-------|---------|--------|
| **DSRI** | Days Sales in Receivables Index | (Receivables_t / Revenue_t) / (Receivables_t-1 / Revenue_t-1) | 0.920 |
| **GMI** | Gross Margin Index | ((Revenue_t-1 - COGS_t-1) / Revenue_t-1) / ((Revenue_t - COGS_t) / Revenue_t) | -0.528 |
| **AQI** | Asset Quality Index | (1 - (Current Assets_t + PPE_t) / Total Assets_t) / (1 - (Current Assets_t-1 + PPE_t-1) / Total Assets_t-1) | 0.404 |
| **SGI** | Sales Growth Index | Revenue_t / Revenue_t-1 | 0.892 |
| **DEPI** | Depreciation Index | (Depreciation_t-1 / (PPE_t-1 + Depreciation_t-1)) / (Depreciation_t / (PPE_t + Depreciation_t)) | -0.115 |
| **SGAI** | Sales, General & Admin Index | SG&A_t / Revenue_t / (SG&A_t-1 / Revenue_t-1) | 0.172 |
| **LVGI** | Leverage Index | (LTD_t + Current Liabilities_t) / Total Assets_t / ((LTD_t-1 + Current Liabilities_t-1) / Total Assets_t-1) | -0.327 |
| **TATA** | Total Accruals to Total Assets | (Net Income_t - CFO_t) / Total Assets_t | 4.679 |

**M-Score = -4.84 + 0.920(DSRI) + 0.528(GMI) + 0.404(AQI) + 0.892(SGI) + 0.115(DEPI) + 0.172(SGAI) - 0.327(LVGI) + 4.679(TATA)**

| M-Score | Interpretation |
|---------|---------------|
| **> -2.22** | Potential manipulator (approximately 3-5% of public companies flagged, of which ~40-50% are actual manipulators per Beneish research) |
| **< -2.22** | Non-manipulator (but not a guarantee — some manipulators score below threshold) |

**Data Requirements:** 2 years of financial data (current and prior period). All inputs are publicly available from financial statements.

**Limitations:**
1. The M-Score was developed and tested on US public companies; effectiveness in other markets may vary
2. The -2.22 threshold may need recalibration for specific industries or markets
3. The model produces false positives (flags non-manipulators) and false negatives (misses manipulators)
4. Best used as a screening tool, not a standalone fraud detection system

### 5.3 Dechow F-Score

**Concept:** Developed by Dechow, Ge, Larson, and Sloan (2011), the F-Score predicts the likelihood of material misstatement based on financial statement data.

| Component | Variable | Description |
|-----------|----------|-------------|
| **RSST_ACC** | Accruals Quality | (WC accruals_t + NCO_t + FIN_t) / Avg Total Assets |
| **CHG_REC** | Change in Receivables | Delta Receivables / Delta Revenue |
| **CHG_INV** | Change in Inventory | Delta Inventory / Delta Revenue |
| **SOFT_ASSETS** | Soft Assets | (Total Assets - PPE - Cash and Securities) / Total Assets |
| **CHG_CS** | Change in Cash Sales | Delta (Revenue - Delta Receivables) |
| **CHG_ROA** | Change in Return on Assets | ROA_t - ROA_t-1 |
| **ISSUE** | Actual Issuance | Indicator if company issued equity or debt in the prior 12 months |
| **CHG_MARGIN** | Change in Gross Margin | Gross Margin_t - Gross Margin_t-1 |
| **CHG_TURN** | Change in Asset Turnover | (Revenue_t / Avg Total Assets) - (Revenue_t-1 / Avg Total Assets_t-1) |
| **CHG_EMPLOY** | Change in Number of Employees | Delta Employees / Employees_t-1 |
| **LEASE_REC** | Lease Receivables | Indicator if company reports material lease receivables |
| **DLW** | Debt / Equity Issuance | Change in equity or long-term debt > 10% |

**F-Score Interpretation:**

| F-Score Range | Misstatement Probability Rank | Interpretation |
|---------------|------------------------------|---------------|
| **< 1.00** | Low | Below-average probability of misstatement |
| **1.00 - 1.50** | Moderate | Above-average probability; further analysis warranted |
| **1.50 - 2.00** | Elevated | Materially above-average probability; strong signal for investigation |
| **> 2.00** | High | Significant misstatement risk; priority for detailed review |

**Limitations:**
1. F-Score is more complex than M-Score and requires more data inputs
2. The model was calibrated on US SEC enforcement actions; effectiveness varies internationally
3. Firms may have legitimate reasons for F-Score signals (e.g., restructuring, mergers, accounting changes)
4. Best used as a complement to M-Score and other screening tools

### 5.4 Combined Quantitative Screening Approach

| Screening Layer | Tool / Method | Output | Decision Rule |
|----------------|--------------|--------|--------------|
| **Layer 1: First-Pass Screen** | Benford's Law on revenue and expense | Flag if MAD > threshold | Ensure sufficient data points; apply to quarterly data for at least 3 years |
| **Layer 2: Statistical Model** | Beneish M-Score | M-Score value; flagged if > -2.22 | Cross-reference with F-Score; conflicting signals require manual review |
| **Layer 3: Cross-Validation** | Dechow F-Score | F-Score value; flagged if > 1.50 | Combined M-Score > -2.22 AND F-Score > 1.50 = Strong suspicion |
| **Layer 4: Qualitative Overlay** | Red flag checklist (Sections 1-4) | Count of active red flags | 3+ active high-intensity red flags + positive M/F Score = Material concern |
| **Layer 5: Expert Judgment** | Manual review of signals | Composite fraud risk assessment | Final override if qualitative factors contradict quantitative results |

---


---

## 6. Historical Validation: Major International Fraud Cases

### 6.1 Enron (2001) — Off-Balance-Sheet Entities

**Fraud Genotype:** Off-balance-sheet debt concealment + Related-party self-dealing + Fictitious revenue

| Red Flag | Present? | Earliest Warning | Lead Time |
|---------|---------|-----------------|-----------|
| (1) SPE debt not consolidated | Yes | T0 (3+ years before bankruptcy) | >3 years |
| (2) CFO personally interested in SPEs (conflict of interest) | Yes | T0 (disclosed in related-party notes) | >3 years |
| (3) Related-party transactions with SPEs for revenue inflation | Yes | T0 | >3 years |
| (4) Revenue growth without commensurate CFO | Yes | T0 | >3 years |
| (5) Complex, opaque business model and financial reporting | Yes | T0 (no one understood the financial statements) | >3 years |
| (6) Aggressive mark-to-market accounting on illiquid assets | Yes | T0 | >3 years |
| (7) Stock-based compensation incentivizing earnings manipulation | Yes | T0 | >3 years |
| (8) Audit committee approval of related-party transactions | Yes (but ineffective) | T0 | Approved despite obvious conflict |

**Earliest Warning:** Related-party transactions with SPEs, and CFO's personal interest in those SPEs, were publicly disclosed for years before the bankruptcy. The warnings were not acted upon because Enron's financial structure was too complex for analysts and regulators to understand.

**Key Lesson:** Off-balance-sheet entities require fundamental economic analysis beyond legal form. If a related-party transaction lacks business purpose beyond financial reporting, it is a strong red flag regardless of the accounting treatment approved by auditors.

### 6.2 WorldCom (2002) — Capitalization of Operating Expenses

**Fraud Genotype:** Expense capitalization + Earnings manipulation

| Red Flag | Present? | Earliest Warning | Lead Time |
|---------|---------|-----------------|-----------|
| (1) Line costs (operating expense) capitalized as PP&E (USD 11bn) | Yes | T0 (fixed asset additions dwarfed peers) | >2 years |
| (2) PP&E growth rate >> CFO growth rate | Yes | T0 | >2 years |
| (3) EBITDA inflated by reclassifying operating expense as capex | Yes | T0 | >2 years |
| (4) FCF reliability compromised (CFO inflated by same reclassification) | Yes | T0 | >2 years |
| (5) Aggressive revenue targets from CEO | Yes | T0 | >2 years |
| (6) Internal audit identified issues but was overruled by management | Yes | T1 (June 2002) | <1 month before filing |

**Earliest Warning:** Fixed asset additions growing at a rate completely inconsistent with industry capacity deployment and business growth. Ratio of capex/revenue was far above competitors. Any analyst comparing the company's capex intensity to competitors would have identified the anomaly.

**Key Lesson:** Capital expenditure analysis is a powerful fraud detection tool. When a company's capex / revenue or capex / depreciation ratios deviate significantly from industry peers without a plausible explanation (e.g., major network build or acquisition integration), the quality of reported earnings should be questioned.

### 6.3 Wirecard (2020) — Fictitious Revenue + Missing Cash

**Fraud Genotype:** Fictitious revenue through third-party acquirers + Missing cash balances + Related-party fraud

| Red Flag | Present? | Earliest Warning | Lead Time |
|---------|---------|-----------------|-----------|
| (1) Third-party acquirer relationships generating majority of revenue without independent verification | Yes | T0 (multiple years of FT reporting) | 3+ years |
| (2) Cash balances held in trustee accounts that could not be independently verified | Yes | T0 | 3+ years |
| (3) Related-party transactions (Al Alam, Senjo) lacking business substance | Yes | T0 | 3+ years |
| (4) Total revenues and profits reported from high-risk jurisdictions | Yes | T0 (Singapore, Philippines, Dubai) | 3+ years |
| (5) Short-seller reports identifying red flags (Zatarra Research, 2016; FT, 2019) | Yes | T0 (2016) | 4+ years |
| (6) Auditor (EY) unable to verify cash: Bank confirmations not returned | Yes | T1 (2020) | <1 year |
| (7) COO Jan Marsalek with unexplained operating role and offshore interests | Yes | T0 | 3+ years |
| (8) Growth entirely through M&A; organic growth unclear | Yes | T0 | 3+ years |

**Earliest Warning:** Multiple years of critical reporting by the Financial Times (2015-2019) and short-seller research (2016) identified the core red flag: third-party acquirer relationships that generated the majority of reported revenue could not be independently verified, and cash balances in "trustee accounts" were not confirmed by independent third parties.

**Key Lesson:** When revenue is concentrated in a few relationships that are opaque and cannot be independently verified, the burden of proof should shift: the company must demonstrate the revenue is real. The failure of auditors, regulators, and investors to demand independent verification for 4+ years is the cautionary tale.

### 6.4 Toshiba (2015) — Earnings Management and Management Pressure

**Fraud Genotype:** Systematic earnings overstatement across multiple business units driven by management pressure

| Red Flag | Present? | Earliest Warning | Lead Time |
|---------|---------|-----------------|-----------|
| (1) Unrealistic profit targets known as "challenge" — managers pressured to meet them | Yes | T0 (internal culture issue) | Multiple years |
| (2) Periodic earnings manipulation across multiple business units (3 presidents involved) | Yes | T0 (pattern observable) | Multiple years |
| (3) Infrastructure systems (PC, semiconductors) and energy divisions involved | Yes | T0 | Multiple years |
| (4) External investigation revealed ~JPY 224bn overstated profit | Yes | T1 (2015 investigation launched) | ~2 years |
| (5) Outside directors and audit committee failed to detect | Yes | T0 | Systemic governance failure |

**Earliest Warning:** The earnings pattern was consistent across multiple business units — a sustained pattern of meeting or just beating targets despite underlying industry headwinds. Disproportionate focus on "challenge" targets was a cultural indicator.

**Key Lesson:** Management "tone from the top" and cultural indicators matter. When a company consistently meets aggressive targets across all business units despite adverse industry conditions, analyst skepticism is warranted.

### 6.5 Overall Evidence Strength

| Signal Category | Historical Validation Cases | Average Lead Time | Conclusion |
|----------------|---------------------------|------------------|------------|
| Revenue quality signals | 4/4 (Enron, WorldCom, Wirecard, Toshiba all involved revenue/earnings quality issues) | 2-3+ years | Receivable / CFO divergence and complex revenue recognition captured 2+ years in advance |
| Management / governance signals | 3/4 (Enron CFO conflict, Wirecard COO opacity, Toshiba management pressure) | 2-3+ years | Governance signals are often the earliest but require qualitative interpretation |
| Related-party transaction signals | 3/4 (Enron SPEs, Wirecard acquirers, WorldCom vendor relationships) | 2-3+ years | Related-party signals are the most stable early warning category |
| Balance sheet / asset quality | 3/4 (WorldCom capex, Wirecard cash, Enron SPEs) | 1-3 years | Balance sheet manipulation often leaves clear footprints in asset ratios |
| Quantitative screening (M-Score / F-Score) | Applicable to all (would have flagged Enron, WorldCom, Wirecard) | 2+ years | M-Score and F-Score are effective screening tools when applied consistently over time |

**Core Conclusion:** Governance and related-party signals are the earliest leading indicators across major fraud cases (average 2-3+ years lead time), yet these are the dimensions that traditional financial analysis covers least effectively. This module fills that gap.

---


---

## 8. Operational Risk Extension: IT Systems and Business Continuity

### 8.1 Background and Positioning

> **Source:** Risk Management Standards Audit (G3 — Operational Risk / Governance Deficiency Coverage). The existing governance-fraud-risk.md module has validated effective detection of financial fraud, management governance, related-party transactions, and manipulation. However, operational risk extends beyond fraud — systems risk, compliance risk, and key person risk are equally important to credit quality.

### 8.2 IT Systems Failure / Business Interruption Credit Transmission

```
Core system failure / material business interruption
    |
    +-- Short-term (1-7 days)
    |     +-- Business halt -> immediate revenue loss
    |     +-- Data loss/corruption -> difficulty restoring operations
    |     +-- Customer complaints / churn -> reputational damage
    |     +-- Regulatory attention -> inquiry / on-site inspection
    |
    +-- Medium-term (1-6 months)
    |     +-- Revenue loss (interruption + recovery period)
    |     +-- IT system rebuild / RTO costs (increased capex)
    |     +-- Insurance claims insufficient (deductibles + exclusions)
    |     +-- Customer trust decline -> market share loss
    |     +-- Data breach follow-up compensation / litigation
    |
    +-- Long-term (6-24 months)
          +-- Financing cost increase (investors reassess IT governance)
          +-- Business license / qualification restrictions
          +-- Compliance costs permanently increase
```

### 8.3 IT Systems Red Flags

| Red Flag | Detection Condition | Signal Intensity | Observability |
|---------|-------------------|-----------------|--------------|
| **Core system material outage** | Media/company confirms core system outage >4 hours | Medium-High | Observable — major news coverage |
| **Data center catastrophic failure** | Fire/power outage/network interruption affecting multiple services | High | Observable — industry bulletins |
| **Cybersecurity event (ransomware/DDoS)** | Ransomware encryptions critical systems; or DDoS causing service unavailability | Medium-High | Observable — company disclosure obligation |
| **Personal data breach >1M records** | Confirmed data breach involving >1M users (GDPR / equivalent disclosure triggers) | High | Observable — regulatory notification obligations |
| **Extended planned system downtime** | Core system downtime >24 hours scheduled maintenance | Medium | Observable — maintenance notices |
| **IT investment well below industry median** | IT capex consistently <50% of industry median for 3+ years | Low-Medium | Partially observable |
| **Single-vendor critical system dependency** | Core systems provided by single vendor without replacement option | Low-Medium | Partially observable |

**Data Limitation Note:** IT systems and business continuity risks are among the most difficult operational risk types to detect:
1. Entities have **no obligation to disclose** system architecture robustness
2. Digital-transformation different stages create very different risk exposures
3. Cybersecurity event disclosure is selective — small events may not be reported
4. This framework's IT systems detection is **inherently reactive** — only detectable after public events occur

---


---

## 9. Operational Risk Extension: Regulatory Compliance

### 9.1 Compliance Violation Credit Transmission

```
Compliance violation event
    |
    +-- Regulatory Penalty
    |     +-- Fine (direct financial loss)
    |           +-- Antitrust: up to 1-10% of annual revenue (e.g., EC fines)
    |           +-- Financial regulation: fines up to millions / billions
    |           +-- Securities regulation: disgorgement + penalties
    |     +-- Business Restriction
    |           +-- Business suspension / license suspension
    |           +-- New business application hold
    |           +-- Industry access restricted
    |     +-- Credit Transmission
    |           +-- Penalty directly impacts net income -> capital accumulation weakened
    |           +-- Business restriction reduces revenue -> FCF decline
    |           +-- Investor trust decline -> credit spread widening -> financing cost increase
    |
    +-- Legal/Regulatory Escalation
    |     +-- Investigation -> business uncertainty
    |     +-- Shareholder class action / securities litigation
    |     +-- Controller/executive under criminal process -> management vacuum
    |     +-- Compliance costs permanently increase
    |
    +-- Market Reaction
          +-- Stock/bond price decline (same day reaction)
          +-- Rating agency may adjust
          +-- Banks tighten credit lines
          +-- Suppliers demand prepayment / shorter terms -> WC pressure
```

### 9.2 Compliance Violation Signal Classification

| Signal Category | Specific Signal | Signal Intensity | Data Source |
|---------------|----------------|-----------------|-------------|
| **Securities / Market Regulator** | Formal investigation (SEC/ FCA/ ESMA/ equivalent) | High | Regulator announcements |
| | Penalty for fraudulent financial reporting | High | SEC AAER / equivalent |
| | Insider trading sanction | High | Regulator publications |
| **Antitrust / Competition** | Merger blocked or subject to remedies | Medium-High | Competition authority announcements |
| | Antitrust fine (>1% of revenue) | High | Same as above |
| | Abuse of dominance finding | High | Same as above |
| **Financial Services** | License suspension / revocation | High | Financial regulator |
| | Material fine for AML/KYC breaches | Medium-High | Same as above |
| | Breach of prudential requirements | Medium | Same as above |
| **Data Protection / Privacy** | GDPR / equivalent material fine | Medium-High | Data protection authority |
| | Data breach with regulatory action | Medium | Same as above |
| **Tax** | Tax evasion / fraud finding | High | Tax authority |
| | Material transfer pricing adjustment | Medium-High | Same as above |
| **Anti-Bribery / Corruption** | FCPA / UK Bribery Act / equivalent enforcement | High | DOJ/SEC; SFO; equivalent |
| | Compliance monitor appointment | High | Same as above |

### 9.3 Compliance Risk Composite Assessment

| Assessment | Condition |
|-----------|----------|
| **No Signal** | No regulatory penalty / investigation in last 3 years |
| **Weak Signal** | Minor penalty (< equivalent USD 1M) and resolved |
| **Medium Signal** | (1) Material fine or (2) Business restricted but not suspended or (3) Investigation initiated |
| **Strong Signal** | (1) Fraud investigation or (2) Material penalty > USD 100M or (3) Core business suspended or (4) Multiple medium signals |
| **Extreme Signal** | Controller/executive held criminally liable + core license revoked (linked to one-vote veto) |

---


---

## 10. Operational Risk Extension: Key Person Risk

### 10.1 Key Person Definition — Beyond Existing Coverage

The existing module (Section 2) covers CEO/CFO turnover. This extension adds:

| Person Type | Existing Coverage (Section 2) | This Extension |
|------------|-----------------------------|---------------|
| CEO/General Manager | Change frequency / tenure / mass resignation | Add: sudden departure cause analysis; successor quality; credit impact of star CEO departure |
| CFO/Finance Director | Change frequency / relationship with Chairman | Add: special credit meaning of finance head departure (fraud indicator) |
| CTO/Chief Scientist | Not covered | **New** — critical for technology/biotech/semiconductor entities |
| Chairman/Controller | Covered (Section 2.1) | Add: controller unreachable/investigated credit impact |
| Business Unit Head | Not covered | **New** — for sales-driven or project-based businesses |
| Compliance / Risk Officer | Not covered | **New** — critical for financial entities |
| Company Secretary | Change frequency | Maintain existing |

### 10.2 Key Person Risk Credit Transmission

```
Key person sudden change
    |
    +-- CEO/General Manager departure
    |     +-- Strategy execution interrupted; new CEO may change direction
    |     +-- Investor confidence decline (especially if performance was adequate)
    |     +-- Core team follow (CEO often brings team)
    |     +-- Credit impact: management uncertainty -> financing cost increase
    |
    +-- CFO/Finance Director departure
    |     +-- Financial reporting quality at risk
    |     +-- Auditor may reassess internal control effectiveness
    |     +-- Financing plans may be delayed
    |     +-- Special signal: CFO leaving before earnings release -> High red flag
    |
    +-- CTO/Chief Scientist departure
    |     +-- R&D pipeline may be interrupted (especially biotech)
    |     +-- Core technical talent continuity lost
    |     +-- IP/patent maintenance affected
    |
    +-- Controller unreachable / investigated
    |     +-- Entity may fall into governance vacuum
    |     +-- Bank credit freezes (compliance)
    |     +-- Suppliers demand prepayment / stop credit terms
    |     +-- Credit impact: catalytic event — can turn liquidity pressure into default in days
    |
    +-- Core management mass resignation
          +-- Indicates material undisclosed issue
          +-- Most severe: independent director mass resignation -> internal control effectively collapsed
          +-- Credit impact: directly triggers one-vote veto assessment
```

### 10.3 Key Person Risk Red Flags

| Red Flag | Detection Condition | Signal Intensity | Observability |
|---------|-------------------|-----------------|--------------|
| **Controller unreachable / investigated / detained** | Company announcement confirms inability to contact controller, or confirmation of detention/investigation | High | Observable — regulatory filing required |
| **CEO abnormal resignation** | CEO resigns before term and before retirement age with "personal reasons" not explained | High | Observable — company announcement |
| **CFO resignation within 30 days before earnings** | CFO resigns within 30 days before scheduled earnings release | High | Observable — timing comparison |
| **CTO/Chief Scientist departure (technology firm)** | Semiconductor R&D VP / Biotech Chief Scientific Officer / Software CTO departure | Medium-High | Partially observable |
| **Auditor / Internal Audit head sudden resignation** | Auditor resigns outside normal rotation | High | Observable |
| **Core team mass departure** | 3+ core members in same department depart simultaneously/sequentially | Medium-High | Partially observable |
| **Compliance / Risk head departure (financial entity)** | Bank CRO / Compliance Director leaving before or after regulatory action | Medium | Observable |
| **Multiple key executives selling simultaneously** | 3+ executives concentrated selling within 30 days | Medium-High | Observable — insider trading filings |
| **Star CEO / Founder stepping back from operations** | Founder / long-serving CEO exits day-to-day management | Medium | Observable |

### 10.4 Controller Risk Signal Timeline

```
Signal intensity from low to high:

[Early Signals] (T-12 to T-24 months)
  +-- Controller frequently traveling / long absences (not observable)
  +-- Controller starting to sell personal assets (not observable)
  +-- Controller reducing involvement in daily decision-making (partially observable)

[Mid Signals] (T-6 to T-12 months)
  +-- Controller high-pledge ratio + stock price declining (Section 2.1 covered)
  +-- Controller's personal assets/other companies under financial stress

[Late Signals] (T-3 to T-6 months)
  +-- Controller's shares frozen by court (observable)
  +-- Controller listed as dishonest person / restricted from high consumption (observable)
  +-- Controller resigning from all positions (observable)

[Catalytic Signals] (T-0 to T-3 months)
  +-- Controller unreachable (observable)
  +-- Controller taken by regulatory/prosecutorial authority (observable)
  +-- Controller filing / applying for entity insolvency (observable)
```

---
