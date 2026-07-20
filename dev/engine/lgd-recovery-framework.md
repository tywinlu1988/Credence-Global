# Loss Given Default (LGD) and Recovery Analysis Framework

**Version**: v0.0.2 | **Date**: 2026-07-17 | **Status**: Published

**Module**: Fixed Income Credit Analysis Engine — Expected Loss (EL) Framework Supplement

---

> **Honesty Statement:** The LGD estimation methods in this framework constitute **simplified estimates** rather than precise measurements. Accurate LGD requires internal collateral valuation data, historical default-and-recovery databases, and workout process tracking — data that belongs to institutional internal records and is unavailable through public channels across most markets. This framework aims to provide *discriminating LGD rankings* under public-data constraints, not precise loss-given-default predictions. Sections are annotated to indicate which parts are "precise indicators" (computable values with public data support), which are "simplified estimates" (inferences based on covenants and industry benchmarks), and which draw on international recovery studies.

---

## Table of Contents

- [1. LGD Positioning in the Engine](#1-lgd-positioning-in-the-engine)
- [2. Five-Tier LGD Classification](#2-five-tier-lgd-classification)
- [3. Key Factors Influencing LGD](#3-key-factors-influencing-lgd)
- [4. Standard LGD Assessment Process](#4-standard-lgd-assessment-process)
- [5. Debt Priority and Credit Enhancement Evaluation](#5-debt-priority-and-credit-enhancement-evaluation)
- [6. Collateral Classification and Valuation Framework](#6-collateral-classification-and-valuation-framework)
- [7. Guarantee and Credit Enhancement Assessment](#7-guarantee-and-credit-enhancement-assessment)
- [8. Industry Characteristics and Recovery Rates](#8-industry-characteristics-and-recovery-rates)
- [9. Post-Default Recovery Path Analysis](#9-post-default-recovery-path-analysis)
- [10. International Bankruptcy and Insolvency Frameworks](#10-international-bankruptcy-and-insolvency-frameworks)
- [11. Collateral Valuation: International Standards](#11-collateral-valuation-international-standards)
- [12. Simplified LGD Estimation Under Public Data Constraints](#12-simplified-lgd-estimation-under-public-data-constraints)
- [13. LGD Integration with Existing Frameworks](#13-lgd-integration-with-existing-frameworks)
- [14. LGD Assessment Template and Output Specifications](#14-lgd-assessment-template-and-output-specifications)
- [15. Version History and Roadmap](#15-version-history-and-roadmap)

---

## 1. LGD Positioning in the Engine

### 1.1 From PD-Only to PD x LGD Two-Dimensional Framework

The engine's current rating output is a single-dimensional probability-of-default ranking (AAA to D). Major rating agencies (Moody's, S&P, Fitch) all employ a PD + LGD two-dimensional framework. Risk differences between different obligations of the same issuer can span 2-4 notches — determined entirely by collateral, guarantee, and seniority structure.

**The LGD module does not replace existing PD ratings. It operates as an independent dimension alongside PD ratings:**

```
PD Rating (Existing)        LGD Rating (New)
AAA to D                    LGD1 to LGD5
    |                            |
    +-------------+-------------+
                  |
          Integrated Credit Assessment
     (Expected Loss: EL = PD x LGD)
```

### 1.2 Expected Loss Matrix

The complete expression of integrated credit risk is Expected Loss (EL):

| PD Rating | LGD Rating | Expected Loss Rate (EL) | Meaning |
|-----------|-----------|------------------------|---------|
| AAA (low PD) | LGD1 (low LGD) | <0.2% | Very low risk, double protection |
| AAA (low PD) | LGD5 (high LGD) | ~4% | High-quality issuer but weak covenant protection |
| CCC (high PD) | LGD1 (low LGD) | ~10% | Near-default but ample collateral |
| CCC (high PD) | LGD5 (high LGD) | ~80%+ | Worst combination, near total loss expected |

**Data Note:** EL = PD x LGD is a **conceptual framework formula**. Precise EL calculation requires quantitative PD and LGD estimates, not ordinal grades. The engine currently uses PD grades (AAA to D) and LGD grades (LGD1 to LGD5); the EL matrix employs interval mapping.

### 1.3 Benchmarking Against International Rating Agencies

| Rating Agency | PD Dimension | LGD Dimension | Notation | Notes |
|-------------|-------------|--------------|---------|-------|
| Moody's | Rating (Aaa-C) | Loss Grade (1-6) | Aaa.lgd1 | Loss grades based on historical recovery rates |
| S&P | Rating (AAA-D) | Recovery Rating (1+ to 5) | AAA/1+ | Recovery rating specific to each obligation |
| Fitch | Rating (AAA-D) | Recovery Rating (RR1-RR6) | AAA(RR1) | Recovery ratings map to recovery rate ranges |
| **This Engine** | **PD Rating (AAA to D)** | **LGD Grade (LGD1-LGD5)** | **BBB/LGD2** | **Output as two independent lines** |

**Data Sources:** Moody's *Loss Given Default (LGD) and Recovery Rate Metrics* Methodology (2017); S&P *Recovery Ratings* Criteria (2019); Fitch *Recovery Ratings and Notching Criteria* (2020). These public methodology documents describe the LGD framework structure but do not disclose underlying recovery rate benchmarks or internal models.

### 1.4 When to Use the LGD Module

| Scenario | LGD Analysis Depth | Rationale |
|---------|-------------------|-----------|
| Issuer-only credit quality assessment (generic rating) | Not needed | Issuer rating does not consider obligation-specific differences |
| Specific bond credit risk assessment | Full LGD analysis | Secured vs. unsecured bonds of the same issuer have materially different risk profiles |
| Convertible/exchangeable bond assessment | Simplified LGD analysis | Bond protection mechanisms become more important as conversion value declines |
| Structured product seniority analysis | Full LGD analysis | Seniority tranching drives LGD differences |
| Portfolio stress testing in risk management | LGD parameter inputs required | Portfolio loss under default scenarios depends on each obligation's LGD estimate |
| Relative value comparison | LGD required as pricing input | Bonds with same PD rating but different LGD should exhibit yield spread differences |

---

## 2. Five-Tier LGD Classification

### 2.1 LGD Grade Definitions

| LGD Grade | Expected Loss Rate | Expected Recovery Rate | Typical Scenario |
|-----------|-------------------|----------------------|-----------------|
| LGD1 | <20% | >80% | Cash/treasury collateral covering 100%+, investment-grade sovereign guarantees, highest-seniority structured tranches |
| LGD2 | 20%-40% | 60%-80% | High-quality collateral with adequate coverage (LTV<50%), listed equity pledge with margin ratio >150%, confirmed irrevocable standby letters of credit from major international banks |
| LGD3 | 40%-60% | 40%-60% | General collateral coverage (LTV 50-70%), guaranteed but guarantor correlated with issuer, senior unsecured bonds |
| LGD4 | 60%-80% | 20%-40% | Subordinated bonds, unsecured debentures (no collateral, no guarantee), secured bonds where guarantor credit quality is weaker than issuer |
| LGD5 | >80% | <20% | Junior tranches, deep subordination, structured product equity tranches, bonds already in default with no effective credit enhancement |

**Data Note:** The LGD/recovery rate ranges in this framework reference Moody's *Corporate Default and Recovery Rates* (2020) global recovery statistics, S&P's *Recovery Rating Scale* classification logic, and Altman's seminal research on bond recovery rates.

### 2.2 LGD Grade and PD Rating Interaction Constraints

| PD Rating | Achievable LGD Grade Range | Constraint Rationale |
|-----------|---------------------------|---------------------|
| AAA - AA | LGD1 - LGD4 | High issuer quality cannot alter covenant-level LGD ceiling |
| A - BBB | LGD1 - LGD5 | Medium-quality issuers can reach LGD1 through superior credit enhancement; unsecured debentures at LGD3-LGD4 |
| BB - B | LGD2 - LGD5 | Low-quality issuers may be unable to reach LGD1 even with collateral due to enforcement difficulties |
| CCC - D | LGD3 - LGD5 | Near-default/defaulted issuers — recovery depends on liquidation values rather than expected enhancement effectiveness |

**Constraint Logic:** PD rating affects the LGD ceiling because — as an issuer's credit quality deteriorates to a certain point — some credit enhancement measures lose effectiveness (e.g., correlated guarantors deteriorate simultaneously, collateral enforcement is impeded by the issuer's legal entanglements).

---

## 3. Key Factors Influencing LGD

### 3.1 Factor Overview

| Factor Category | Specific Factor | Effect on LGD | Data Source | Calculation Precision |
|----------------|----------------|--------------|-------------|----------------------|
| **Debt Seniority** | Secured/Unsecured Senior/Subordinated/Junior | Higher seniority = lower LGD | Offering memorandum/prospectus (public) | **Precise** — terms usually clearly defined |
| **Collateral Quality** | Collateral type, value coverage multiple, liquidity | Higher quality/more coverage = lower LGD | Prospectus collateral clauses (public) | **Simplified Estimate** — no independent collateral appraisal report; relies on covenant descriptions and industry benchmarks |
| **Guarantee Enhancement** | Guarantor credit quality, guarantee ratio, legal enforceability | Stronger guarantor/higher ratio = lower LGD | Guarantor public credit information (public) | **Simplified Estimate** — requires independent assessment of guarantor credit quality |
| **Industry Characteristics** | Asset-heavy vs. asset-light, asset specificity | Higher asset recoverability = lower LGD | Industry research, historical recovery cases (public) | **Simplified Estimate** — relies on industry benchmarks and case inference |
| **Default Path** | Reorganization/Liquidation/Out-of-court restructuring | Liquidation value typically below reorganization value | Historical cases, legal environment analysis (public) | **Simplified Estimate** — depends on specific case legal proceedings and negotiations |
| **Legal/Judicial Environment** | Bankruptcy law completeness, judicial efficiency | Higher efficiency/predictability = higher recovery (lower LGD) | Legal environment reports, historical cases (public) | **Qualitative Assessment** — depends on jurisdiction-specific judicial analysis |

### 3.2 Factor Decomposition Formula (Simplified Estimate)

```
LGD Estimate = Base_LGD - Adjustments

Where:
  Base_LGD   = f(Debt Seniority, Economic Cycle Phase)
  Adjustments = Delta_Collateral + Delta_Guarantee + Delta_Industry
                + Delta_RecoveryPath + Delta_Legal

Base_LGD Benchmark (seniority only):
  - Secured Senior:          Base_LGD = 45%  (i.e., ~55% recovery)
  - Unsecured Senior:        Base_LGD = 60%  (i.e., ~40% recovery)
  - Subordinated:            Base_LGD = 75%  (i.e., ~25% recovery)
  - Junior/Equity Tranche:   Base_LGD = 90%  (i.e., ~10% recovery)

Adjustments (Delta):
  - Delta_Collateral:  Collateral quality adjustment, range -25pp to +10pp
  - Delta_Guarantee:   Guarantee enhancement adjustment, range -15pp to +5pp
  - Delta_Industry:    Industry recovery characteristics, range -5pp to +10pp
  - Delta_RecoveryPath: Default path adjustment, range -5pp to +10pp
  - Delta_Legal:       Legal environment adjustment, range -5pp to +10pp
```

**Honesty Statement:** The coefficients above (e.g., Base_LGD = 45% for secured senior) are **simplified benchmarks** based on global historical recovery rate data. Moody's 2019 data shows global weighted-average recovery rates: secured senior 55.1% (LGD=44.9%), unsecured senior 39.8% (LGD=60.2%), subordinated 23.5% (LGD=76.5%). Altman and Eberhart (1994) documented similar patterns across U.S. corporate bonds. These benchmarks serve as starting points but should be calibrated to specific market contexts where local data is available.

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

## 7. Guarantee and Credit Enhancement Assessment

### 7.1 Guarantor Credit Quality Assessment

The core logic of guarantee-based credit enhancement: **the guarantor's independent credit quality determines the actual enhancement effect.** Related-party guarantees (parent for subsidiary, sibling company cross-guarantees) provide far less enhancement than independent third-party guarantees.

**Guarantee Enhancement Dual Scoring Matrix:**

| Issuer Credit Quality | Guarantor Significantly Stronger | Guarantor Similar | Guarantor Weaker |
|---------------------|--------------------------------|------------------|-----------------|
| High (AA and above) | No additional value from guarantee | No additional value from guarantee | Negative value (adds correlation risk) |
| Medium (A-BBB) | LGD improves by 1-2 grades | LGD improves by 0-1 grades | LGD unchanged or increases |
| Low (BB and below) | LGD improves by 1 grade | LGD unchanged | LGD increases by 1 grade |

**Data Source:** Guarantor credit ratings (if available) from rating agency websites; guarantor financial data (if listed) from public financial statements.

### 7.2 International Guarantee/Enhancement Types

| Guarantee Type | Enhancement Effectiveness | Typical LGD Adjustment | Typical Examples/Institutions | Notes |
|---------------|-------------------------|----------------------|------------------------------|-------|
| **Sovereign/Government Guarantee** | Strongest | Delta=-15pp to -20pp | Explicit sovereign guarantee backed by full faith and credit; typically requires parliamentary appropriation | Effectiveness depends on sovereign credit quality |
| **Multilateral Development Bank Guarantee** | Very Strong | Delta=-15pp | World Bank (IBRD) guarantees, regional development banks (ADB, AfDB, EBRD) | Preferred creditor status; very low historical loss rates |
| **Export Credit Agency Guarantee** | Strong | Delta=-10pp to -15pp | US EXIM, UKEF, EDC (Canada), Euler Hermes (Germany), Sinosure | Country risk + agency-specific assessment |
| **Monoline Financial Guarantee** | Strong (pre-crisis); Moderate (post-2008) | Delta=-10pp to -15pp | Assured Guaranty, Ambac (legacy), MBIA (legacy) | Post-2008 financial guarantor capacity is more constrained |
| **Parent/Group Guarantee (Independent Credit)** | Moderate to Strong | Delta=-5pp to -15pp | Strong parent guaranteeing subsidiary debt | Requires assessment of parent's independent credit quality |
| **Parent/Group Guarantee (Related Party)** | Weak | Delta=0pp to -5pp | Subsidiary debt guaranteed by parent; consolidated group | Legal validity but limited incremental credit benefit — parent and subsidiary are already economically integrated |
| **Personal Guarantee (Controlling Shareholder)** | Weak to Moderate | Delta=0pp to -5pp | Founder/controlling shareholder personal guarantee | Legally valid but enforcement depends on personal asset recoverability and jurisdictional asset-protection laws |
| **Standby Letter of Credit / Bank Guarantee** | Strong (depending on issuing bank) | Delta=-10pp to -15pp | Major international banks | Enhancement depends on issuing bank credit rating |
| **Keepwell Agreement / Support Letter** | Very Weak | Delta=0pp | Agreement to maintain ownership/liquidity support | Limited legal enforceability in most jurisdictions |
| **Debt Service Reserve Account** | Moderate to Strong | Delta=-5pp to -10pp | Cash reserve account typically 6-12 months of debt service | Most effective when reserve is fully funded and subject to perfected security interest |
| **Excess Cash Flow Sweep** | Moderate | Delta=-5pp | Mandatory prepayment from excess cash flow | Effectiveness depends on the definition of excess cash flow and sweep percentage |

**Data Source:** Guarantor rating data from rating agency public information. Analysis of guarantee types references international bond market practice and regulatory guidance on credit enhancement.

### 7.3 Related-Party Guarantee Special Risks

Related-party guarantees are among the most common guarantee forms in many markets, but also carry the **lowest information content** regarding incremental credit enhancement.

| Related-Party Type | Risk Characteristics | Identification Method | Output Adjustment |
|-------------------|---------------------|---------------------|------------------|
| Subsidiary issuing + parent guarantee | Parent and subsidiary are consolidated; intra-group credit risk is highly correlated | Check whether issuer and guarantor are within the same group | LGD adjustment halved (e.g., standard guarantee Delta=-10pp becomes Delta=-5pp) |
| Parent issuing + subsidiary guarantee | Subsidiary financial contribution is already part of parent's credit assessment | Check whether the subsidiary is effectively providing asset backing for parent debt | LGD adjustment not applicable (enhancement is circular under consolidation) |
| Cross guarantees among sibling companies | Guarantee chain may form a loop; default of one may propagate | Check whether the guarantee chain forms a closed loop | LGD adjustment halved or eliminated |
| Controlling shareholder guarantee | Effective at legal level, difficult at enforcement level | Check whether guarantee agreement is notarized and perfected | Adjustment only if the guarantor has identifiable and enforceable independent core assets |

**Honesty Statement:** Quantitative adjustment of related-party guarantees is a **highly subjective qualitative judgment**. This framework does not provide precise Delta formulas but only directional guidance.

### 7.4 GSE and Implicit Guarantee Framework

Government-Sponsored Enterprises (GSEs) and entities with implicit government backing present a unique assessment challenge:

| Entity Type | Implicit Guarantee Strength | Assessment Approach | Historical Reference |
|------------|---------------------------|---------------------|---------------------|
| **Fannie Mae / Freddie Mac (GSEs)** | Very Strong (U.S. federal conservatorship since 2008) | Conservative assumption: effective sovereign backing during crisis | 2008 conservatorship demonstrated willingness to support; senior and subordinated debt treated differently |
| **Federal Home Loan Banks (FHLB)** | Strong (joint and several liability among 11 banks) | Senior debt: near-sovereign; no guarantee of standalone debt | Never defaulted; access to U.S. Treasury as lender of last resort is statutory |
| **European Union Institutions** | Strong (EU budget + member state backing) | EIB, ESM, EU Commission bonds trade near sovereign levels | EU budget guarantee; ECB backstop mechanisms |
| **State-Owned Enterprises (Investment Grade)** | Varies by ownership, legal framework, strategic importance | Separate capacity vs. willingness assessment | Explicit guarantee vs. implicit assumption must be distinguished |
| **Systemically Important Financial Institutions (SIFIs)** | Conditional (resolution frameworks post-2008) | TLAC/MREL instruments are bail-in-able; senior opco debt may retain implicit support | Post-crisis resolution regimes have materially reduced implicit expectations |

---

## 8. Industry Characteristics and Recovery Rates

### 8.1 Industry Asset Recoverability Classification

**Core Logic:** Different industries have different asset structures and asset characteristics, which determine recovery value after default.

| Industry Type | Asset Characteristics | Recovery Rate Reference Range | Examples |
|--------------|----------------------|------------------------------|----------|
| **Asset-Heavy — General Equipment** | Fixed assets ratio >40%, equipment widely usable across industries | 40%-60% | Traditional manufacturing, general equipment manufacturing, chemicals |
| **Asset-Heavy — Specialized Equipment** | Fixed assets ratio >40%, equipment is highly specialized | 20%-40% | Solar cell manufacturing (specialized furnaces), semiconductor manufacturing (lithography — secondary market exists), advanced battery production |
| **Asset-Light — Core IP** | Intangible assets dominate (patents/IP/software), low book value | 10%-30% | Chip design (fabless), biotech (pipeline value hard to assess), software companies |
| **Asset-Light — Platform** | Core assets are data and user relationships, minimal book assets | 5%-20% | Internet platforms, fintech companies |
| **Contractual/Concession Assets** | Core assets are long-term contracts/concessions, cash flow predictable | 50%-70% | Data centers (long-term power + customer contracts), toll roads (concession agreements) |
| **Real Estate Intensive** | Property/land dominates balance sheet | 50%-75% | Commercial real estate, industrial parks, logistics property |

**Data Sources:** Industry fixed-asset/total-asset ratios from listed company financial statement footnotes. Equipment secondary market liquidity from industry-specific trading platforms. Recovery ranges reference Moody's *Industry Recovery Rate Study* (2018) and Altman's recovery rate database.

### 8.2 Key Industry Delta_Industry Adjustments

| Industry | Delta_Industry | Rationale | Data Support |
|---------|---------------|-----------|-------------|
| **Solar Manufacturing** | +5pp | Asset-heavy but equipment highly specialized; rapid technology cycles (PERC to TOPCon to BC); older production lines have minimal recovery value | Equipment trading data shows near-zero recovery for technology that is three generations obsolete |
| **Semiconductor — Foundry** | -5pp | Asset-heavy with highly specialized equipment, but lithography/etch equipment has international secondary market; recovery reasonably supported | Secondary semiconductor equipment market (e.g., SurplusGlobal) shows residual value rates of 30-50% |
| **Semiconductor — Fabless** | +10pp | Asset-light; IP monetization highly uncertain; core asset (engineering team) disperses after default | Case study inference; no systematic public data |
| **Biotechnology** | +5pp to +10pp | Pipeline value extremely uncertain — late-stage assets may be sold but at steep discounts; early-stage pipeline essentially zero | BioPharma M&A and bankruptcy asset sale cases |
| **Data Centers** | -5pp | Power contracts and customer leases are salable; assets continue generating cash flows | Data center M&A shows efficient, high-PUE assets can trade at premiums |
| **Electric Vehicle Manufacturing** | +10pp | Inventory depreciates rapidly (market prices drop weekly); specialized production lines costly to retool; battery recovery value limited | EV market pricing data; battery recycling market still immature |
| **Medical Devices** | 0pp | Generally asset-light but channel value convertible; regulatory registrations have independent value | Registration certificates can be separately priced in M&A transactions |

**Honesty Statement:** Delta_Industry adjustment parameters are **framework-set values**, not empirically regressed results. Historical real recovery rates by industry are typically not available in systematic form across most markets.

### 8.3 Industry Concentration Indirect Effects on Recovery

| Industry Concentration Characteristic | Effect on LGD | Logic |
|--------------------------------------|-------------|-------|
| Highly concentrated (oligopoly, CR3>70%) | LGD may decrease | Quality assets may be acquired by competitors, creating "buyer's market" for recovery |
| Highly fragmented (CR3<20%) | LGD may increase | Limited specialized operational capacity among asset buyers; larger disposal discounts |
| Severe overcapacity | LGD significantly increases | Idle equipment has virtually no secondary buyers during industry-wide overcapacity |

**Data Sources:** Industry concentration metrics (CR3/CR5) from industry research reports. This adjustment is primarily qualitative.

---

## 9. Post-Default Recovery Path Analysis

### 9.1 Three Post-Default Resolution Paths

| Path | Definition | Average Recovery (Global Reference) | Typical Application |
|------|-----------|-----------------------------------|-------------------|
| **Reorganization (Chapter 11 / Administration)** | Court-supervised restructuring under bankruptcy protection; going-concern preservation | 40-60% (secured creditors); 5-30% (unsecured creditors) | Preferred path for larger enterprises with going-concern value |
| **Liquidation (Chapter 7 / Winding-up)** | Enterprise ceases operations; assets sold and distributed per priority | 20-40% (secured creditors); 0-20% (unsecured creditors) | Main path for SMEs; unsecured creditors typically experience very low recoveries |
| **Out-of-Court Restructuring (Scheme of Arrangement / London Approach)** | Consensual debt restructuring outside formal insolvency proceedings | Highly variable; no reliable global average | Increasingly common; lacks automatic stay, execution risk varies |

**Data Sources:** Global recovery rates reference Moody's *Annual Default and Recovery Rate Report* and S&P *Global Recovery Rates*. U.S. Chapter 11 data from UCLA-LoPucki Bankruptcy Research Database; European data from the European Banking Authority.

### 9.2 International Reorganization Case Recovery Rate References

| Case | Year | Jurisdiction | Industry | Unsecured Creditor Recovery | Key Features |
|------|------|-------------|---------|---------------------------|-------------|
| **Enron** | 2001 | United States (Chapter 11) | Energy/Trading | ~20% (initial plan); ~52% (final distribution after years of litigation) | Complex structured entities; off-balance-sheet liabilities inflated recovery uncertainty |
| **WorldCom** | 2002 | United States (Chapter 11) | Telecommunications | ~36% (unsecured bonds); ~100% (bank debt) | Largest U.S. bankruptcy at the time; asset sales to Verizon |
| **General Motors** | 2009 | United States (Chapter 11 — 363 Sale) | Automotive | ~10-25% (unsecured bonds); New GM equity offered as partial compensation | Pre-packaged restructuring via Section 363 sale; government-backed rescue |
| **Lehman Brothers** | 2008 | United States (Chapter 11) | Financial | Varies by entity and jurisdiction; senior unsecured ~21-34% (depending on legal entity) | Largest bankruptcy in history; cross-border complexity (over 80 legal entities across jurisdictions) |
| **Nortel Networks** | 2009 | US (Chapter 11) / Canada (CCAA) | Telecom Equipment | Variable; total recovery pool was ultimately ~$7B vs. initial estimates of $2-3B | Cross-border coordination between U.S. and Canadian proceedings; 7-year process |
| **MF Global** | 2011 | United States (Chapter 11) | Financial Brokerage | ~100% recovery of customer segregated funds (after extensive recovery efforts) | Segregation rules and commodity customer protection |
| **Abengoa** | 2016 | Spain (Pre-concurso) | Energy/Infrastructure | ~50% (restructuring agreement with creditors) | Complex multi-jurisdictional pre-insolvency restructuring |
| **Thomas Cook** | 2019 | United Kingdom (Compulsory Liquidation) | Travel/Tourism | Unsecured creditors received near zero; ATOL-bond protected package holiday customers | Comprehensive compulsory liquidation with government-backed repatriation |
| **Wirecard** | 2020 | Germany (Insolvency) | Fintech/Payments | Expected <5% for unsecured creditors | Fraud-driven insolvency; missing trust account balances |
| **Greensill Capital** | 2021 | United Kingdom (Administration) | Supply Chain Finance | Expected 35-65% depending on asset type | Complex structured credit; single-buyer concentration |
| **Credit Suisse (AT1) Write-down** | 2023 | Switzerland (Finma-orchestrated) | Banking | Additional Tier 1 (AT1) bonds: 100% write-down; senior bonds: 0.59-7.52% (risk-adjusted) | Regulatory resolution; contractual write-down mechanism triggered; shareholder value zero |

**Data Sources:** Recovery rates from court-approved plans, court filings, and public media reports. These are **case-specific statistics**, not weighted industry averages.

**Important Notes:** The above unsecured creditor recovery rates should be considered indicative only. Actual recovery rates are affected by:
1. **Claim size**: Smaller claims often receive proportionally higher recovery (e.g., U.S. Chapter 11 small-claim priority treatment)
2. **Reorganization duration**: Typical cycles of 1-5 years; time value of money is not reflected in stated recovery rates
3. **Debt-to-equity swap value**: Many reorganization plans include equity; the actual sale price and timing of equity disposition determine the ultimate recovery
4. **Post-reorganization survival**: Some reorganized entities subsequently default (e.g., the "Chapter 22" phenomenon)
5. **Cross-border complexity**: Multi-jurisdictional legal entities compound recovery uncertainty

### 9.3 Out-of-Court Restructuring Special Risks

| Characteristic | Out-of-Court Restructuring | Formal Insolvency Proceeding | Effect on LGD |
|---------------|--------------------------|------------------------------|--------------|
| Legal binding force | Weak (requires high consensus threshold) | Strong (court-ordered, majority binds minority) | Out-of-court may require multiple renegotiations; high time cost |
| Information transparency | Low | High (court-appointed administrator + creditor committee) | Out-of-court places smaller creditors at greater information disadvantage |
| Debt relief magnitude | Smaller (typically extensions + rate reductions) | Larger (principal may be discounted) | Out-of-court has higher nominal recovery but longer actual recovery cycle |
| Liquidation threat | Optional (proceeds to formal process if no deal) | The ultimate outcome if no going-concern plan | -- |

**Honesty Statement:** Recovery rate data for out-of-court restructurings is not systematically available in any major market. The above analysis is based on practitioner reporting and case descriptions, constituting qualitative judgment.

### 9.4 Delta_RecoveryPath Adjustment Reference

| Scenario | Delta Adjustment | Applicable Conditions |
|---------|----------------|---------------------|
| Expected reorganization, issuer asset quality acceptable | -5pp | Going-concern value exists; business can be preserved through restructuring |
| Expected reorganization, issuer assets already hollowed out | 0pp | Unsecured creditor recovery very low even after reorganization |
| Expected liquidation | +5pp to +10pp | Liquidation discounts exceed reorganization; longer duration |
| Expected out-of-court restructuring with strong issuer bargaining power | +5pp | Issuer may use flexibility of out-of-court process to suppress recovery |

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

## 12. Simplified LGD Estimation Under Public Data Constraints

### 12.1 Data Constraint Summary

| Data Needed But Unavailable | Why Unavailable | Alternative Approach |
|---------------------------|----------------|---------------------|
| Precise collateral appraisal reports | Internal data (available only to banks or rating agencies) | Tier classification based on prospectus collateral descriptions and industry benchmarks |
| Historical default recovery database | No publicly available systematic recovery database in most markets | Global benchmarks + case-specific adjustment; reference Moody's/S&P public data |
| Real-time collateral valuation | Collateral value fluctuates with markets; continuous tracking required | Annotate "collateral value as of assessment date" and update monthly/quarterly |
| Precise inter-creditor priority among same-issuer obligations | Not fully public (cross-default / cross-guarantee complexity) | Most likely priority ranking based on bond terms |
| Reorganization/liquidation timeline | Highly case-specific | Qualitative reference using historical average restructuring cycles |
| Post-default creditor negotiation dynamics | Non-public | Not included; annotated as "not considering negotiation dynamics" |

### 12.2 Simplified LGD Estimation Process (Public Data Version)

```
Input: Bond ISIN/ticker + Analysis Date
    |
    +-- Step 1: Extract debt seniority from prospectus
    |     Output: Seniority type (secured/unsecured senior/subordinated/junior)
    |
    +-- Step 2: Extract credit enhancement from prospectus covenants
    |    +-- Collateral type and description
    |    +-- Guarantor name
    |    +-- Guarantee percentage
    |     Output: Enhancement type and quality (high/medium/low/none)
    |
    +-- Step 3: Infer industry LGD benchmark from issuer industry and asset structure
    |     Output: Industry LGD baseline adjustment
    |
    +-- Step 4: Reference historical comparable cases for the industry/jurisdiction
    |     Output: Comparable case recovery range
    |
    +-- Step 5: Comprehensive estimate
          Output: LGD grade + recovery range + confidence level
```

### 12.3 Estimation Accuracy Classification

| Input Dimension | Estimation Accuracy | Explanation |
|----------------|-------------------|-------------|
| **Debt seniority classification** | **High** | Prospectus clearly states priority |
| **Whether secured** | **High** | Prospectus clearly states collateral/guarantee |
| **Collateral type** | **High** | Prospectus clearly describes collateral |
| **Guarantor identity** | **High** | Prospectus clearly identifies guarantor |
| **Guarantor credit quality** | **Medium** | If public rating exists, directly available; unrated requires public information inference |
| **Collateral coverage multiple** | **Medium-Low** | Prospectus may not disclose market value of collateral, only book value |
| **Current collateral value** | **Low** | Post-issuance value changes; requires industry index/market price estimation |
| **Industry recovery benchmark** | **Medium** | Global data available but may not directly apply to specific markets; local case sample insufficient |
| **Default path prediction** | **Low** | Depends on multiple unpredictable factors (issuer, creditors, court, government dynamics) |
| **Actual recovery rate** | **Very Low** | Interaction of all above factors makes precise prediction nearly impossible |

### 12.4 Statistical Uncertainty Range of LGD Estimates

| LGD Grade | Recovery Median (Global Reference) | 90% Confidence Interval (Global) | Cross-Market Adjusted Range |
|-----------|-----------------------------------|-------------------------------|---------------------------|
| LGD1 | 85% | 70% - 98% | 65% - 98% (jurisdictional enforcement efficiency reduces lower bound) |
| LGD2 | 70% | 50% - 85% | 45% - 80% (legal uncertainty depresses lower bound) |
| LGD3 | 50% | 30% - 70% | 25% - 65% (restructuring recovery rates may fall below global median in less efficient jurisdictions) |
| LGD4 | 25% | 10% - 45% | 10% - 40% (subordinated bonds lack dedicated cross-market statistics) |
| LGD5 | 8% | 2% - 20% | 2% - 15% (structured product equity tranches can approach 0%) |

**Data Sources:** Global statistics reference Moody's *Corporate Default and Recovery Rates, 1920-2019* (February 2020), pp. 26-30, and Altman & Hotchkiss *Corporate Financial Distress and Bankruptcy* (2019). Cross-market adjustments are qualitative judgments based on observed case patterns.

### 12.5 Limitations of ML/AI for LGD Prediction

Various machine learning approaches have been proposed for LGD prediction. Their applicability depends on data availability:

| Method | Limitations Across Most Markets | Feasibility |
|--------|-------------------------------|------------|
| Statistical regression on large historical database | Default sample sizes are typically insufficient (many markets have fewer than 200 corporate default observations) | **Not currently feasible** |
| Time-series models on default recovery data | Default events span a short history in most emerging markets; recovery data is not systematically disclosed | **Not currently feasible** |
| Covenant-driven expert system / rule engine | Does not rely on training data; based on public terms and industry benchmark rules | **Viable approach** (method adopted by this framework) |
| Transfer learning (global data pre-training + local data fine-tuning) | Market structure differences (state ownership, legal frameworks, government coordination) limit transfer learning effectiveness | **Academically possible but unproven** |

**Conclusion:** Under current data constraints across most markets, the **rule-engine approach** based on covenants and industry benchmarks is the only viable LGD estimation method. ML/AI approaches can only surpass rule engines when sufficient local market default and recovery data becomes available — a condition unlikely to be met in the near to medium term for most markets.

---

## 13. LGD Integration with Existing Frameworks

### 13.1 Integration with Dual-Track Methodology

Adding an LGD dimension to the rating mapping in dual-track-methodology.md:

**Current (Pre-Modification):**

| Composite Score Range | Rating | Meaning |
|---------------------|--------|---------|
| 9.5 - 10.0 | AAA | Very low risk, extremely high credit quality |
| ... | ... | ... |
| 0.0 - 0.9 | D | Default or material default |

**Proposed Extension (Post-Modification):**

| Composite Score Range | PD Rating | LGD Additional Output | Full Rating Notation |
|---------------------|----------|---------------------|--------------------|
| 9.5 - 10.0 | AAA | LGD1 - LGD5 | AAA/LGD2 |
| 8.5 - 8.9 | AA | LGD1 - LGD5 | AA/LGD3 |
| 7.5 - 7.9 | A+ | LGD1 - LGD5 | A+/LGD3 |
| ... | ... | ... | ... |

**Recommendation:** LGD should be output as an independent module rather than embedded in the rating string, for the following reasons:
1. Maintains backward compatibility with the existing PD rating framework
2. LGD is an obligation-level attribute, not an issuer-level attribute — different bonds of the same issuer may have different LGD
3. The dual-track methodology's core output (rating + signal + completeness report) can attach LGD information at each bond level

### 13.2 Integration with Multi-Stakeholder Decision Matrix

In multi-stakeholder.md, LGD considerations are added to the decision matrix for each role:

| Role | Use of LGD | Decision Impact |
|------|-----------|----------------|
| **M0 Credit Underwriting** | Collateral LGD analysis is a core input to underwriting decisions | Secured loans have lower LGD than unsecured; affects loan pricing and tenor |
| **M1 Bond Investment** | Add LGD assessment under "Covenant Protection (M1.2)" dimension | Between two bonds with the same PD rating, the one with lower LGD offers better investment value |
| **M3 Market Trading** | Consider LGD risk adjustment in carry analysis | High carry but high LGD may not represent genuine value opportunity |
| **M4 Portfolio Risk Control** | LGD parameter determines loss severity in stress testing | Portfolio expected loss = sum(each bond's PD x LGD x exposure) |

### 13.3 Integration with Financial Deep Dive

In the scenario sensitivity matrix of financial-deep-dive.md, a "Recovery Rate Shock" scenario is added:

**Proposed Addition:**
- **Scenario 4: Recovery Rate Shock** — assumes collateral value declines 30% (e.g., real estate price decline) or collateral enforcement cycle extends

| Scenario Variable | Base | Bull | Bear | Recovery Shock |
|-----------------|------|------|------|---------------|
| Revenue change | Baseline | +10% | -10% | Baseline |
| Gross margin change | Baseline | +5pp | -5pp | Baseline |
| Interest rate change | Baseline | -100bp | +100bp | Baseline |
| **Collateral value change** | -- | -- | -- | **-30%** |
| **Recovery rate change** | -- | -- | -- | **-15pp** |
| Adjusted LGD grade | -- | -- | -- | **May rise 1-2 grades** |

---

## 14. LGD Assessment Template and Output Specifications

### 14.1 Single Bond LGD Assessment Output Template

```
=========================================================
LGD Assessment Report
=========================================================

Basic Information
----------------------------------------
Bond Name/ISIN: XX Bond / XS1234567890
Issuer: XX Corporation
Issue Amount/Outstanding: USD 1,000M / USD 800M
Analysis Date: 2026-07-17

Debt Seniority and Enhancement
----------------------------------------
Seniority Category: Senior Unsecured
Enhancement Type: Guarantee
Guarantor: XX Group Limited (Parent Guarantee)
Guarantee Ratio: 100%

Collateral Details
----------------------------------------
Collateral Type: None (guarantee only)
Collateral Coverage Multiple: N/A
Non-Collateral Enhancement: Full unconditional and irrevocable
  joint-and-several liability guarantee from parent

LGD Estimation Results
----------------------------------------
LGD Grade: LGD3
Expected Loss Rate Range: 40% - 60% (LGD3)
Expected Recovery Rate Range: 40% - 60%
Base Confidence: Medium-Low

Estimation Process
----------------------------------------
Base_LGD (Unsecured Senior): 60%                  <- Global benchmark
Delta_Collateral: 0pp (no collateral)              <- High confidence
Delta_Guarantee: -5pp (parent guarantee,           <- Medium confidence
                    related-party halving adjustment)
Delta_Industry: 0pp (industrial equipment)         <- Medium confidence
Delta_RecoveryPath: 0pp (assumed reorganization)   <- Low confidence
Delta_Legal: +5pp (issuer jurisdiction has         <- Low confidence
                   untested insolvency framework)
LGD Estimate: 60% - 5% + 0% + 0% + 5% = ~60%      <- Medium-low confidence

Notes: Although the parent provides a full guarantee, the parent
and subsidiary are related parties with highly correlated credit
risk. The jurisdiction's insolvency framework is not well tested
for large corporate restructurings. Independent assessment of the
guarantor's credit quality is recommended.

Comparative Analysis
----------------------------------------
Same issuer secured bond (XX Secured): LGD2 (expected recovery 50-70%)
Same issuer unsecured bond (this issue): LGD3
This bond vs. same-industry same-rating median: LGD3 vs. LGD3 (median)

Key Risk Notes
----------------------------------------
1. Related-party guarantee provides limited incremental enhancement
2. Legal environment in issuer's jurisdiction may affect enforcement
3. No collateral coverage; full dependence on guarantor credit

Data Gaps and Uncertainties
----------------------------------------
[] Guarantor independent credit rating  -> Parent external rating available
[] Guarantor financial condition         -> Parent is unlisted; financial data incomplete
[] Historical guarantee enforcement      -> No data
[] Current collateral value              -> N/A (no collateral)
```

### 14.2 PD + LGD Integrated Credit Assessment Template

```
=========================================================
Integrated Credit Assessment (PD + LGD Two-Dimension)
=========================================================

I. Issuer Information
   ...

II. PD Rating (Dual-Track Methodology Output)
   PD Rating: [AAA-D]
   Track A Score: [X.X/10]
   Track B Status: [Calm / Watch / Anomaly / Crisis / No Data]
   Cross-Validation Status: [Consensus / Divergence-A / Divergence-B]
   Data Completeness: [X%]

III. LGD Rating (This Report Subject)
   LGD Grade: [LGD1 - LGD5]
   Expected Recovery Range: [X% - X%]
   Estimation Confidence: [High / Medium / Low]

IV. Expected Loss (EL) Composite Assessment
   PD x LGD Matrix Integrated Judgment:
   +---------------------+--------------------+
   | PD Rating           | [AAA-D]            |
   | LGD Grade           | [LGD1-LGD5]        |
   | EL Range            | [Low/Medium/High]  |
   | Risk Classification  | [IG / HY / Default]|
   +---------------------+--------------------+

V. Key Drivers
   1. PD Driver: [Issuer-level core credit factor summary]
   2. LGD Driver: [Obligation-level enhancement and recovery path summary]

VI. Cross-Bond Comparison
   +-----------+-----------+-----------+-----------+
   | Bond      | PD Rating | LGD Grade | EL Status |
   +-----------+-----------+-----------+-----------+
   | Bond A    | [Rating]  | [LGD]     | [EL]      |
   | Bond B    | [Rating]  | [LGD]     | [EL]      |
   | Bond C    | [Rating]  | [LGD]     | [EL]      |
   +-----------+-----------+-----------+-----------+
```

---

## 15. Version History and Roadmap

### 15.1 Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-07-17 | Initial international release: Five-tier LGD classification, international bankruptcy frameworks (Chapter 11, Scheme of Arrangement, EU Insolvency Regulation), IVS-based collateral valuation, five-sector recovery benchmarks from Moody's/Altman studies, global case library |

### 15.2 Roadmap (by Priority)

| Priority | Item | Description | Dependencies |
|---------|------|-------------|-------------|
| **P0** | LGD module integration with mosaic engine | Integrate LGD assessment signals into the mosaic-engine.md signal extraction pipeline | Mosaic engine pattern extension |
| **P0** | Historical default recovery database (compilation) | Compile and organize default case recovery rates by industry/jurisdiction/debt type from published sources | Public information collection |
| **P1** | Implement LGD assessment template | Implement the Section 14 template as an operational engine module | Framework stabilization |
| **P1** | Add LGD dimension to POC validation | Test LGD module discrimination in existing case back-testing | P0 completion |
| **P2** | Issue rating notching quantification | Develop simplified notching rules based on rating agency methodologies | -- |
| **P2** | Perpetual/hybrid LGD special rules | Research the settlement priority and legal standing of perpetuals | -- |
| **P3** | Structured product/ABS LGD treatment | Develop separate framework for ABS senior/junior tranche LGD assessment | -- |
| **P3** | LGD-to-bond-pricing quantitative model | PD x LGD -> credit spread mapping; requires sufficient market data | -- |

### 15.3 Related Content

- [Engine Architecture Overview](engine-overview.md) — Core concepts, overall architecture, design principles
- [Dual-Track Methodology](dual-track-methodology.md) — Track A + Track B, cross-validation, rating mapping
- [Multi-Stakeholder Framework](multi-stakeholder.md) — Decision matrix for each role
- [Financial Deep Dive Module](financial-deep-dive.md) — Three-statement linkage, scenario sensitivity matrix
- [Mosaic Engine](mosaic-engine.md) — Signal extraction, mosaic assembly, completeness assessment
