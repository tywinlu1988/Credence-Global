# Loss Given Default (LGD) and Recovery Analysis Framework

**Version**: v0.3.0 | **Date**: 2026-07-17 | **Status**: Published

**Module**: Fixed Income Credit Analysis Engine — Expected Loss (EL) Framework Supplement

---

> **Honesty Statement:** The LGD estimation methods in this framework constitute **simplified estimates** rather than precise measurements. Accurate LGD requires internal collateral valuation data, historical default-and-recovery databases, and workout process tracking — data that belongs to institutional internal records and is unavailable through public channels across most markets. This framework aims to provide *discriminating LGD rankings* under public-data constraints, not precise loss-given-default predictions. Sections are annotated to indicate which parts are "precise indicators" (computable values with public data support), which are "simplified estimates" (inferences based on covenants and industry benchmarks), and which draw on international recovery studies.

---

> **Reading guide**: §§1-3 contain the executable methodology — LGD tiers,
> influencing factors, and classification rules. §§7-9 and §§12-15 cover
> guarantees, industry recovery rates, recovery paths, public-data estimation,
> and integration — required reading for the LGD add-on path.
> §§4-6 and §§10-11 (assessment process, collateral valuation detail,
> — read on demand.


## Table of Contents

- [1. LGD Positioning in the Engine](#1-lgd-positioning-in-the-engine)
- [2. Five-Tier LGD Classification](#2-five-tier-lgd-classification)
- [3. Key Factors Influencing LGD](#3-key-factors-influencing-lgd)
- [7. Guarantee and Credit Enhancement Assessment](#7-guarantee-and-credit-enhancement-assessment)
- [8. Industry Characteristics and Recovery Rates](#8-industry-characteristics-and-recovery-rates)
- [9. Post-Default Recovery Path Analysis](#9-post-default-recovery-path-analysis)
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