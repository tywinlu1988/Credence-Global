# Loss Given Default (LGD) and Recovery Analysis Framework — Appendix

> Appendix to `lgd-recovery-framework.md` — version tracks the parent document; reference
> material (worked examples, derivations, historical validation) moved here in
> the 2026-07 restructure. Read on demand.

---

## 4. Standard LGD Assessment Process

```
Step 1: Identify obligation type (secured/unsecured senior/subordinated/junior)
    |   Input: Prospectus "Terms of the Bonds" section
    |   Output: Seniority classification + Base_LGD benchmark
    v
Step 2: Assess credit enhancement (collateral quality / guarantor credit)
    |   Input: Prospectus collateral and guarantee sections
    |   Output: Delta_Collateral + Delta_Guarantee
    v
Step 3: Reference industry recovery rate benchmarks
    |   Input: Industry asset characteristics analysis
    |   Output: Delta_Industry
    v
Step 4: Assess recovery path under default scenario
    |   Input: Issuer jurisdiction legal environment, comparable default cases
    |   Output: Delta_RecoveryPath + Delta_Legal
    v
Step 5: Comprehensive output — LGD grade + expected recovery range
    |   Output: LGD grade + recovery range + confidence assessment
    v
Step 6: (Optional) Merge with PD rating for EL expected loss assessment
    |   Output: EL range + risk capital charge estimate
```

### 4.1 Data Requirements by Step

| Step | Data Required | Publicly Available? | Alternative Approach |
|------|--------------|-------------------|---------------------|
| Step 1 | Prospectus "Bond Terms" section | **Yes** (exchange/regulator filings) | -- |
| Step 1 | Issue credit rating from rating agencies | **Yes** (rating agency websites) | Note: external ratings may lag |
| Step 2 | Collateral type and coverage ratio | **Partial** (prospectus descriptions, no independent appraisal) | Qualitative judgment on coverage adequacy by collateral type |
| Step 2 | Guarantor credit rating and financials | **Yes** (if guarantor is publicly rated or listed) | Unrated guarantors require public information inference |
| Step 3 | Industry asset structure data | **Yes** (industry research, financial statement footnotes) | Typical fixed-asset/total-asset ratios, etc. |
| Step 4 | Default case recovery rate data | **Limited** (public reporting only) | Reference Section 9 historical case compilation |
| Step 4 | Issuer litigation and enforcement records | **Yes** (court databases, public records) | -- |
| Step 5+6 | Issuer PD rating | **Yes** (engine output) | -- |

---


---

## 5. Debt Priority and Credit Enhancement Evaluation

### 5.1 International Debt Instrument Seniority Classification

| Bond Type | Legal Seniority | Typical LGD Grade Range | Notes |
|-----------|---------------|------------------------|-------|
| **Senior Secured Bonds** | Highest priority among creditors; backed by specific collateral | LGD1 - LGD3 | Depends on collateral type and coverage multiple |
| **Senior Unsecured Notes** | Unsecured but senior to subordinated debt | LGD3 - LGD4 | Recovery depends on issuer's unencumbered asset pool |
| **Senior Unsecured Bonds (MTN/Public)** | Pari passu with other unsecured senior debt | LGD3 - LGD4 | Typical unsecured corporate bond |
| **Convertible Bonds** | Senior unsecured (debt prior to conversion) | LGD3 - LGD4 | Embedded equity optionality; put/call provisions may affect actual LGD |
| **Exchangeable Bonds** | Secured (by pledged equity of the underlying company) | LGD1 - LGD3 | Depends on coverage multiple and quality of underlying shares |
| **Asset-Backed Securities — Senior Tranche** | Senior (structured waterfall) | LGD1 - LGD3 | Depends on underlying asset quality and credit enhancement |
| **Asset-Backed Securities — Junior/Equity** | Junior/equity tranche | LGD5 | First-loss piece, very high LGD |
| **Subordinated Notes** | Subordinate to senior creditors | LGD4 - LGD5 | Lower priority in liquidation waterfall |
| **Perpetual/Hybrid Securities** | Unsecured, deep subordination, deferrable coupons | LGD4 - LGD5 | May rank below conventional subordinated debt; coupon deferral risk |
| **Secured Bank Loans (Term Loans A/B)** | Senior secured, typically first lien | LGD1 - LGD3 | Covenants and collateral monitoring provide additional protection |

**Data Sources:** Legal priority of claims references international insolvency frameworks discussed in Section 10. LGD ranges are **framework baseline values**, not precise statistics.

### 5.2 Issue Rating vs. Issuer Rating: Notching Relationship

Rating agencies determine issue ratings by "notching" from the issuer rating:

| Credit Enhancement | Moody's Notching | S&P Notching | This Engine LGD Grade Adjustment |
|-------------------|-----------------|-------------|----------------------------------|
| Unsecured debenture | 0 notch (baseline) | 0 notch (recovery rating 3-4) | LGD3 - LGD4 |
| Secured (guarantee, same credit quality as issuer) | +0 notch | +0 notch (recovery rating 2-3) | LGD3 (substantially unchanged) |
| Secured (guarantor stronger than issuer) | +1 notch | +1 notch (recovery rating 1-2) | LGD2 |
| Secured (high-quality collateral, ample coverage) | +1 to +2 notches | +1 to +2 notches | LGD1 - LGD2 |
| Subordinated | -1 to -2 notches | Recovery rating 5 | LGD4 - LGD5 |

**Data Sources:** Moody's *Notching Criteria* (2018); S&P *Issue Credit Rating Methodology* (2017). This framework references the notching logic but does not employ quantitative notching, as precise quantification is not feasible under public data constraints.

---


---

## 6. Collateral Classification and Valuation Framework

### 6.1 Recovery Value Assessment by Collateral Type

#### 6.1.1 Cash and Cash Equivalents Pledge

| Assessment Dimension | Indicator | Data Source | Precision |
|--------------------|----------|-------------|----------|
| Pledge ratio | Typically 95%-100% | Prospectus pledge terms | **Precise** |
| Value volatility | Very low | -- | -- |
| Enforcement difficulty | Low (freeze + transfer) | Legal practice | **Qualitative** |
| LGD adjustment | Delta_Collateral = -20pp to -25pp | -- | **Simplified Estimate** |

**Typical Scenario:** Cash collateral accounts in structured products, margin deposits.

#### 6.1.2 Government/ Treasury Bond Pledge

| Assessment Dimension | Indicator | Data Source | Precision |
|--------------------|----------|-------------|----------|
| Pledge ratio | Typically 95%-100% | Pledge agreement terms | **Precise** |
| Value volatility | Very low (limited interest rate risk) | Public market data | **Precise** |
| Enforcement difficulty | Low (standardized repo mechanism) | -- | **Qualitative** |
| LGD adjustment | Delta_Collateral = -20pp to -25pp | -- | **Simplified Estimate** |

#### 6.1.3 Listed Equity Pledge

**Key Risk Indicators:**

| Assessment Dimension | Indicator | Safe Threshold | Danger Threshold | Data Source |
|--------------------|----------|--------------|-----------------|-------------|
| Loan-to-Value (LTV) | Loan amount / pledged equity market value | <50% | >70% | Prospectus guarantee terms |
| Maintenance margin ratio | Pledged equity value / loan balance | >150% | <130% (margin call triggered) | Periodic filings |
| Stock price volatility | 30-day annualized volatility | <30% | >50% | Public market data |
| Pledged equity liquidity | Average daily turnover rate | >1% | <0.3% | Public market data |
| Concentration risk | Shares pledged / total shares outstanding | <30% | >50% (large liquidation impact) | Exchange/regulatory filings |
| Pledgor identity | Controlling shareholder vs. other | Controlling shareholder can negotiate; non-controlling easier to liquidate | -- | Beneficial ownership filings |

**LGD Adjustment Calculation (Simplified Estimate):**

```
Delta_Collateral (Equity Pledge) =
  -20pp  IF (LTV<50% AND vol<30% AND turnover>1%)
  -15pp  IF (LTV 50-60% AND vol<40%)
  -10pp  IF (LTV 60-70% AND vol<50%)
  -5pp   IF (LTV 70-80% AND maintenance margin>150%)
  0pp    IF (LTV>80% OR maintenance margin<130%)
  +5pp   IF (concentration>50% OR pledgor is controlling shareholder in legal dispute)
```

**Data Note:** The above assignments are **experience-based benchmarks**, not regression results. International research (e.g., Moody's *Equity Pledge LGD* 2018) indicates equity pledge recovery rates are highly dependent on LTV and underlying stock volatility. Recovery rates may be lower in markets where enforcement is subject to legal uncertainty and block-trade discounts.

#### 6.1.4 Real Estate / Property Collateral

| Assessment Dimension | Safe | Watch | Danger | Data Source |
|--------------------|------|-------|--------|-------------|
| LTV ratio | <50% | 50-70% | >70% | Prospectus (if disclosed) or property appraisal summary |
| Property type | Prime city office/residential | Secondary city residential | Tertiary/industrial/special-purpose | Property market data |
| Liquidity | Absorption cycle <6 months | Absorption cycle 6-12 months | Absorption cycle >12 months | Third-party market data (consulting firms) |
| Auction discount | Typically 70-80% of market value | 60-70% | <60% | Court auction historical data |

**LGD Adjustment Calculation (Simplified Estimate):**

```
Delta_Collateral (Real Estate) = (LTV% x Auction Discount Factor) - 60%

Auction Discount Factors: Prime metro 0.75, Secondary city 0.65, Tertiary 0.55

Example: LTV 60%, secondary city -> 60% x 0.65 - 60% = -21% -> Delta_Collateral = -15pp
Example: LTV 80%, tertiary city -> 80% x 0.55 - 60% = -16% -> Delta_Collateral = -10pp
Example: LTV 90%, tertiary city -> 90% x 0.55 - 60% = -10.5% -> Delta_Collateral = -5pp
```

**Data Source:** Judicial auction discount rates reference court auction platform data and distressed asset market practice. Residential auction transaction prices typically range from 70-80% of market value; industrial properties trade at steeper discounts.

#### 6.1.5 Accounts Receivable Pledge

| Assessment Dimension | Safe Characteristics | Danger Characteristics | Data Source |
|--------------------|---------------------|----------------------|-------------|
| Diversification | Many small receivables, diversified obligors | Single large obligor (concentration >50%) | Prospectus receivable schedule |
| Obligor quality | Investment-grade/large cap/sovereign | Sub-investment-grade/distressed | Obligor public credit information |
| Aging | <1 year | >1 year | Prospectus aging schedule |
| Perfection of security interest | Properly filed/registered | Not perfected | Public filing registry |

**LGD Adjustment:** Delta_Collateral (Receivables) adjustment range -5pp to +5pp. Receivables recovery is generally more challenging than real estate collateral but offers better recovery than unsecured debt.

**Note:** The actual credit enhancement value of receivables pledges varies significantly by market. In several jurisdictions, even perfected receivables pledges have realized substantially less than book value in reorganization proceedings.

#### 6.1.6 Machinery and Equipment Collateral

| Assessment Dimension | General-purpose Equipment | Specialized Equipment | Data Source |
|--------------------|-------------------------|----------------------|-------------|
| Equipment type | Machine tools, injection molds, HVAC | Solar ingot furnaces, lithography machines, pharmaceutical fermenters | Prospectus collateral schedule |
| Secondary market | Active secondary market exists | Very narrow or nonexistent secondary market | Industry equipment trading platforms |
| Depreciation rate | 10-20 year straight-line | Rapid technological obsolescence, may become zero | Equipment useful life + tech refresh cycle |
| Removal/transport cost | Low | High (may exceed residual value) | Industry practice by equipment type |

**LGD Adjustment:** Delta_Collateral (Equipment) adjustment range -5pp to +10pp. General-purpose equipment typically has higher recovery value; specialized equipment carries significant recovery uncertainty under default scenarios and may require a penalty rather than a credit.

### 6.2 Collateral Assessment Constraints Summary

| Assessment Dimension | Precision Determination | Reason |
|--------------------|----------------------|--------|
| Collateral type identification | **Precise** | Prospectus typically discloses collateral type |
| Collateral value | **Simplified Estimate** | Appraisal values in prospectus may be optimistic; value at default may differ materially from issuance |
| LTV ratio | **Partially Precise** | Computable when loan amount and appraisal value are both disclosed; but appraisal may be stale and value at default uncertain |
| Collateral realization discount | **Simplified Estimate** | Depends on market conditions and judicial enforcement efficiency at default — cannot be precisely forecast |
| Seniority of enforcement costs | **Simplified Estimate** | Insolvency law provisions on treatment of enforcement expenses vary by jurisdiction |

---


---

## 10. International Bankruptcy and Insolvency Frameworks

### 10.1 Framework Overview

LGD assessment must account for the legal and insolvency framework governing the issuer's jurisdiction. The three most influential international frameworks are:

| Framework | Jurisdiction | Key Features | Impact on LGD |
|-----------|-------------|-------------|--------------|
| **Chapter 11 (U.S. Bankruptcy Code)** | United States | Debtor-in-possession; automatic stay; exclusivity period; cram-down provisions; 363 sales | Generally higher unsecured recovery due to going-concern preservation; DIP financing priority |
| **Scheme of Arrangement (UK Companies Act)** | United Kingdom / Common Law jurisdictions | Court-sanctioned compromise between company and creditors; no automatic stay; requires class voting | Flexible but no automatic protection; pre-pack schemes are common; recovery depends on class composition |
| **EU Insolvency Regulation (Recast)** | EU Member States (cross-border) | Main proceeding in COMI jurisdiction; automatic recognition across member states; secondary proceedings permitted | Harmonized framework reduces cross-border uncertainty; secondary proceedings can complicate recovery waterfall |
| **CCAA (Companies' Creditors Arrangement Act)** | Canada | Similar to Chapter 11 with stay and plan of arrangement; more court involvement | Intermediate recovery outcomes; relatively efficient restructuring process |
| **Civil Law Insolvency (France, Germany, Japan)** | Civil law jurisdictions | Typically more creditor-protective than debtor-protective; administrator-driven rather than DIP | Generally lower unsecured recovery rates than Chapter 11; faster but potentially less value-maximizing |

### 10.2 Chapter 11 (United States)

**Key LGD Implications:**

| Feature | Description | LGD Impact |
|---------|-----------|-----------|
| Automatic Stay | Immediately halts all collection efforts upon filing | Preserves asset pool; gives debtor breathing room; potentially higher recovery |
| Debtor-in-Possession | Existing management retains control unless cause is shown | Incentivizes timely filing; may preserve value; risk of management entrenchment |
| Exclusivity Period | Debtor has exclusive right to propose plan for 120 days (extendable) | Provides negotiation leverage to debtor; may delay resolution |
| Cram-Down | Court can confirm plan over dissenting creditor class if fair-and-equitable test met | Protects against holdout creditors; facilitates restructuring |
| 363 Sale | Sale of assets outside a plan; free and clear of liens | Increasingly used; can achieve higher value through market-tested sale |
| Priority Waterfall | Secured claims -> administrative expenses -> DIP financing -> unsecured priority -> general unsecured -> subordinated -> equity | Clear hierarchy reduces negotiation cost |
| DIP Financing | Super-priority financing to fund operations during bankruptcy | Provides liquidity; existing secured creditors may be primed |

**Recovery Data (U.S.):** Moody's reports that U.S. senior unsecured bond recovery rates average ~40-50% under Chapter 11 (depending on industry cycle). The UCLA-LoPucki Bankruptcy Research Database shows median time to plan confirmation of ~18 months for large public companies.

### 10.3 Scheme of Arrangement (United Kingdom and Commonwealth)

**Key LGD Implications:**

| Feature | Description | LGD Impact |
|---------|-----------|-----------|
| No Automatic Stay | No statutory moratorium; interim court order can provide limited protection | Less breathing room; creditor action continues unless the court intervenes |
| Class Voting | Creditors divided into classes; each class votes by majority in value (75%) and majority in number (50%) | Minority creditors can be crammed down; but class composition is litigated frequently |
| Cross-Class Cram-Down | UK does not have cross-class cram-down (unlike Chapter 11); all impaired classes must approve | More difficult to bind dissenting classes; may reduce restructuring success rate |
| Pre-Pack Administration | Company enters administration with a pre-negotiated sale of business pre-arranged | Very fast (can complete in days); maximizes going-concern value; creditors limited to reviewing deal |
| Administration | Equivalent to Chapter 11 moratorium but administrator-controlled rather than DIP | Administrator has duty to act in interests of all creditors |

**Recovery Data (UK):** Pre-pack administration typical recovery for unsecured creditors is low (often <20%) because the business is sold free of liabilities. Scheme of arrangement recoveries vary widely but are generally comparable to Chapter 11 for senior classes.

### 10.4 EU Insolvency Regulation (Recast)

**Key LGD Implications:**

| Feature | Description | LGD Impact |
|---------|-----------|-----------|
| Main Proceeding | Opened in the jurisdiction of the debtor's COMI (center of main interests) | Determines which insolvency law governs the main proceeding |
| Secondary Proceeding | Can be opened in any member state where the debtor has an establishment | Creates coordination challenges; assets in secondary proceedings are administered separately |
| Automatic Recognition | Main proceeding and its judgments recognized across all EU member states (except Denmark) | Reduces cross-border legal uncertainty; critical for LGD assessment of multi-jurisdictional entities |
| Group Coordination | Provisions for coordinating insolvency proceedings of group members | Relevant for parent/subsidiary LGD analysis across EU |

**Recovery Data (EU):** European Banking Authority reports that recovery rates vary significantly by member state, with German and Dutch proceedings typically yielding higher unsecured recoveries than Southern European counterparts.

### 10.5 Framework Comparison and LGD Calibration

| Framework | Typical Secured Recovery | Typical Unsecured Recovery | Avg. Duration | Predictability of Outcome |
|-----------|------------------------|---------------------------|---------------|--------------------------|
| **Chapter 11 (US)** | 50-80% | 20-50% | 12-24 months | Moderate — court has wide discretion |
| **Scheme / Administration (UK)** | 50-80% | 15-35% | 6-12 months (pre-pack); 12-18 months (scheme) | Moderate — pre-pack outcomes predictable, schemes less so |
| **EU Insolvency (varies)** | 30-70% (varies by MS) | 5-30% (varies by MS) | 12-36 months | Low — significant variation by member state |
| **Civil Law (Japan)** | 60-80% | 20-40% | 6-12 months | Moderate — civil rehabilitation and liquidation procedures well-defined |

**Delta_Legal Adjustment by Framework:**

| Jurisdiction/Framework | Delta_Legal Adjustment | Rationale |
|----------------------|----------------------|-----------|
| Chapter 11 (US) — predictable application | -5pp to 0pp | Established jurisprudence; generally efficient |
| Chapter 11 (US) — unpredictable outcome | 0pp to +5pp | Some districts have inconsistent outcomes |
| UK Scheme / Administration | -5pp to 0pp | Efficient process; pre-pack provides value preservation |
| EU MS — efficient (Germany, Netherlands) | -5pp to 0pp | Effective administration and legal certainty |
| EU MS — less efficient (selected Southern European) | +5pp to +10pp | Longer timelines; lower unsecured recovery |
| Civil Law — predictable (Japan, Korea) | 0pp to -5pp | Efficient and creditor-protective |
| Emerging market — untested framework | +5pp to +10pp | No track record of large-scale insolvencies |
| Emerging market — tested and weak | +10pp to +15pp | Documentation indicates low recovery expectations |

---


---

## 11. Collateral Valuation: International Standards

### 11.1 International Valuation Standards (IVS)

The International Valuation Standards Council (IVSC) provides the globally recognized framework for collateral valuation. The relevant standards for LGD assessment:

| IVS Standard | Subject | Relevance to LGD |
|-------------|---------|-----------------|
| **IVS 101 — Scope of Work** | Defines the valuation assignment, basis of value, and assumptions | All collateral valuations used in LGD should reference the applicable basis of value |
| **IVS 102 — Investigation and Compliance** | Requires valuer to collect sufficient data and comply with standards | Due diligence on valuer qualifications and methodology is critical for LGD reliability |
| **IVS 103 — Reporting** | Specifies content of valuation report | LGD framework should require that collateral valuations meet IVS 103 reporting standards |
| **IVS 104 — Bases of Value** | Market Value, Mortgage Lending Value (MLV), Fair Value, Investment Value | MLV is most relevant for LGD because it reflects long-term sustainable value, excluding speculative elements |
| **IVS 105 — Valuation Approaches** | Market approach, Income approach, Cost approach | Different approaches yield different value conclusions; the forced-sale/liquidation value is most relevant for default scenarios |
| **IVS 400 — Real Property Interests** | Valuation of real estate for secured lending | Core standard for real estate collateral — the most common collateral type in corporate lending |
| **IVS 410 — Development Property** | Valuation of development and construction property | Relevant for project finance and real estate development LGD |
| **IVS 500 — Financial Instruments** | Valuation of financial instruments (equity, bonds, derivatives) | Relevant for equity and financial instrument pledges |

### 11.2 Valuation Bases for LGD Assessment

| Basis of Value | Definition | Appropriate Use for LGD | Typical Discount from Market Value |
|---------------|-----------|------------------------|-----------------------------------|
| **Market Value** | Estimated amount for which an asset should exchange on the valuation date between a willing buyer and a willing seller in an arm's-length transaction | Baseline reference; not appropriate for forced-sale scenarios | 0% (by definition, market value is benchmark) |
| **Mortgage Lending Value (MLV)** | Value of property determined by prudent assessment of its future marketability, ignoring speculative elements | **Recommended for LGD** — long-term sustainable value | 10-25% below market value depending on property type and market |
| **Fair Value** | IFRS 13 / ASC 820 — price that would be received to sell an asset in an orderly transaction between market participants | Useful where mark-to-market is applied; "orderly transaction" assumption may not hold in default | Varies; depends on assumptions about "orderly" nature of sale |
| **Liquidation / Forced Sale Value** | Estimated amount when insufficient marketing period, typically in a distressed context | **Most appropriate for LGD default scenario** | 20-50% below market value depending on asset type and market conditions |
| **Orderly Liquidation Value (OLV)** | Estimated gross amount that could be received from a sale with reasonable marketing period | Intermediate between market value and forced sale | 10-20% below market value |
| **Salvage Value** | Net amount expected to be realized at end of useful life | Less relevant for LGD (typically post-default is before end of useful life) | Not directly comparable |

### 11.3 LTV (Loan-to-Value) Standards by Asset Class

| Asset Class | Prudent LTV (Senior Secured) | Conservative LTV | Margin of Safety | Source Standards |
|------------|------------------------------|-----------------|-----------------|----------------|
| **Prime Residential Real Estate** | <60% | <45% | 40-55% | EBA Guidelines on LTV limits; Basel CRE guidance |
| **Commercial Real Estate (Prime Office)** | <55% | <40% | 45-60% | Basel III CRE risk weights; IPF valuation guidelines |
| **CRE — Secondary / Tertiary** | <45% | <30% | 55-70% | Higher volatility; larger auction discounts |
| **Industrial Property** | <50% | <35% | 50-65% | Greater specialization; narrower buyer pool |
| **Listed Equity (Liquid, Blue Chip)** | <50% | <35% | 50-65% | Haircuts per ECB/EBA margination practices |
| **Listed Equity (Small Cap / Illiquid)** | <30% | <20% | 70-80% | Higher volatility; larger liquidation impact |
| **Treasury Bonds (OECD Sovereign)** | <95% | <90% | 5-10% | Standard repo haircuts per Basel; ECB collateral framework |
| **Corporate Bonds (IG)** | <85% | <75% | 15-25% | Based on haircuts applied by central banks for liquidity operations |
| **Corporate Bonds (HY)** | <60% | <45% | 40-55% | Higher default correlation; lower secondary market liquidity |
| **Aircraft (Modern Narrow-body)** | <65% | <50% | 35-50% | ISTAT appraisals; semi-annual value decline; specific to aircraft type |
| **Ships (Large Bulk/Cargo)** | <60% | <45% | 40-55% | Baltic Exchange indices; freight rate volatility |
| **Inventory (Generic)** | <50% | <35% | 50-65% | Valuation subject to obsolescence; physical inspection challenges |
| **Accounts Receivable (Diversified)** | <75% | <60% | 25-40% | Advance rate based on obligor quality and aging |

### 11.4 Real Estate Collateral Valuation — International Methodologies

| Valuation Method | Description | Data Requirements | Reliability in Default |
|-----------------|-----------|------------------|----------------------|
| **Comparable Sales Approach** | Value = adjusted comparable property sales | Active market with transaction data | High in active markets; low in distressed or illiquid markets |
| **Income Capitalization Approach** | Value = net operating income / capitalization rate | Rental income and cap rate data | Moderate to high for income-producing property; cap rates subject to judgment |
| **Discounted Cash Flow Approach** | Value = PV of projected cash flows | Long-term lease and market data | Moderate — assumptions become more speculative under default scenario |
| **Cost Approach** | Value = replacement cost - depreciation | Construction cost data | Lower — cost may not reflect market value; more relevant for specialized assets |
| **Automated Valuation Model (AVM)** | Statistical model based on public data | Large transaction database | Low to moderate — reliant on data quality; less accurate for unique properties |
| **Forced Sale / Auction Value** | Estimated price under time-constrained sale | Historical auction data | Most relevant for LGD — typically 20-50% below market value |

**Honesty Statement:** Property valuation for LGD purposes is inherently uncertain. Even professional appraisals prepared under IVS standards carry a typical margin of error of +/-10-15% for standard property types in active markets, and significantly wider for specialized or illiquid assets. Valuation becomes more uncertain at the point of default, which may coincide with a market downturn.

---
