# ESG Risk Assessment Framework (Applicable to Global Fixed Income Markets)

**Version**: v0.0.2 | **Date**: 2026-07-10 | **Status**: Published | **Type**: Non-Credit Risk Overlay Sub-Module

---

> **Design Intent**: This framework is not a standalone ESG rating system, but rather an ESG-to-credit transmission assessment tool designed for the global credit bond market. ESG risks are ultimately mapped to credit impact -- assessing whether and how ESG events affect an issuer's debt servicing capacity or access to financing.
>
> **Overlay Attribute**: Consistent with non-credit-risk-overlay.md, this framework serves as an overlay layer, not altering base ratings, with a maximum +/-1 notch adjustment. ESG signals feed into the "Reputational Risk" and "Operational Risk" dimensions of the non-credit-risk-overlay.

---

## Table of Contents

- [1. ESG Market Specificities and Framework Design Principles](#1-esg-market-specificities-and-framework-design-principles)
- [2. E (Environmental) Risk Assessment](#2-e-environmental-risk-assessment)
- [3. S (Social) Risk Assessment](#3-s-social-risk-assessment)
- [4. G (Governance) Risk Assessment](#4-g-governance-risk-assessment)
- [5. ESG-to-Credit Mapping](#5-esg-to-credit-mapping)
- [6. Overlay Adjustment Rules](#6-overlay-adjustment-rules)
- [7. Data Availability Honest Labeling](#7-data-availability-honest-labeling)
- [8. Integration with Existing Frameworks](#8-integration-with-existing-frameworks)
- [Appendix A: Industry ESG Sensitivity Cross-Reference](#appendix-a-industry-esg-sensitivity-cross-reference)
- [Appendix B: Public Data Source List](#appendix-b-public-data-source-list)

---

## 1. ESG Market Specificities and Framework Design Principles

### 1.1 Key Differences Between Emerging and Mature ESG Markets

| Dimension | Mature Markets (EU/US) | Emerging Markets | Impact on Credit Analysis |
|---|---|---|---|
| **ESG Information Disclosure Coverage** | Listed companies + large non-listed enterprises generally disclose (~90%) | Only listed + bond-issuing enterprises mandatory disclosure (~30-40%), sub-national LGFVs / non-listed SMEs rarely disclose | **Severe data insufficiency** -- unable to perform forward-looking ESG scoring, can only conduct negative event screening |
| **Regulatory Environment** | ESG regulation moving from voluntary to mandatory (CSRD/ISSB) | Primarily driven by carbon neutrality / dual carbon goals; ESG disclosure guidelines are non-mandatory (sustainability reporting guidelines published by major exchanges in recent years but still in transition) | **High policy volatility** -- ESG-themed investing often influenced by policy direction shifts |
| **ESG Rating Agencies** | MSCI, Sustainalytics, Bloomberg ESG and other international institutions dominate | Domestic ESG rating agencies (e.g., SinoCarbon, SynTao Green Finance, Harvest) show low rating consistency (inter-agency correlation coefficient < 0.5) | **Ratings unreliable** -- domestic ESG ratings are not directly cited as credit judgment inputs |
| **ESG Event Disclosure** | Environmental/social events actively exposed by media and NGOs | Environmental penalties officially published by environmental protection authorities; social event disclosure insufficient (labor disputes / supply chain issues reporting may be limited) | **Severe information asymmetry** -- some ESG negative events barely visible in the public domain |
| **Investor Attention** | Large asset owners integrate ESG into investment decisions | Credit bond investors show low ESG attention (primarily in equity markets), but ESG factors have been confirmed to have material credit impact in some default cases | **Market has not yet fully priced ESG risk** -- ESG arbitrage opportunities exist |

### 1.2 Design Principles

| # | Principle | Implication |
|---|---|---|
| 1 | **Event-driven primary, forward-looking assessment secondary** | Current phase centers on "negative event detection" (environmental penalties / safety accidents / product quality scandals that are already externalized events), rather than "forward-looking ESG scoring" (due to insufficient data coverage) |
| 2 | **ESG-to-credit transmission path must be explicit** | Every ESG signal must correspond to a clear credit transmission path (cash flow / financing channels / debt service capacity); indicators with "ESG significance only but no credit impact" are not included |
| 3 | **+/-1 notch adjustment cap** | Consistent with non-credit-risk-overlay.md, ESG overlay adjustments do not exceed +/-1 notch (unless a veto condition is triggered) |
| 4 | **Asymmetric adjustment** | ESG signals are predominantly downward (negative) -- because ESG events almost always carry negative credit implications. Rare upward adjustments (e.g., financing cost reduction from green finance support) |
| 5 | **Industry differentiation** | High-carbon industries (coal/steel/chemicals) have high environmental weight; consumer-facing enterprises (food/pharma/retail) have high social weight; technology enterprises (semiconductor/software) have high governance weight |
| 6 | **Do not replicate international ESG ratings** | Does not adopt MSCI/Sustainalytics ESG scoring systems -- specifically designed for credit bond market characteristics |

### 1.3 Position of This Framework in the Engine Architecture

```
Standard Analysis Workflow (with ESG Overlay):

Step 1: Industry Classification -> Select Pyramid Template
Step 2: Pyramid Scoring -> L1-L4/L5 Layer-by-Layer Scoring -> Weighted Composite Score -> Base Credit Grade
Step 3: External Support Assessment (if needed) -> Upgrade Base Rating (0-3 notches)
Step 4: Non-Credit Risk Overlay (including ESG)
   ├── 4a: Market Risk Assessment
   ├── 4b: Operational Risk Assessment (including governance ESG signals)
   ├── 4c: Reputational Risk Assessment (including environmental + social ESG signals)
   ├── 4d: ★ ESG Specialized Assessment (this framework)
   │     ├── E: Environmental Event Scan + Transition Risk Assessment
   │     ├── S: Social Event Scan + Stakeholder Conflict Assessment
   │     └── G: Governance Structure Assessment (linked with governance-fraud-risk.md)
   └── 4e: Liquidity Risk Assessment
Step 5: Overlay Adjustment -> Base Rating +/-0~+/-1 notch
Step 6: Track B Market Pricing Cross-Validation
Step 7: Output Composite Rating + ESG Annotation
```

---

## 2. E (Environmental) Risk Assessment

### 2.1 Environmental Risk Classification System

| Category | Sub-Category | Credit Impact Intensity | Applicable Industries | Data Observability |
|---|---|---|---|---|
| **High-Carbon Industry Transition Risk** | Carbon emission cost / carbon allowance gap | High (long-term cumulative) | Coal/Steel/Chemicals/Cement/Power/Aluminum | **Partially observable** (requires carbon allowance cost estimation) |
| **Environmental Penalty Risk** | Excessive emissions / construction without approval / solid waste violations | Medium-High (short-term shock) | Manufacturing/Chemicals/Mining/Pulp & Paper | **Observable** (environmental protection authority disclosures) |
| **Production Suspension Risk** | Ordered suspension/production curtailment due to environmental inspection | High (direct cash flow interruption) | Chemicals/Steel/Cement/Mining | **Observable** (environmental protection authority announcements) |
| **Environmental Accident Risk** | Chemical leakage / explosion / environmental pollution incidents | High (compensation + suspension + remediation) | Chemicals/Mining/Transportation/Petrochemicals | **Observable** (major events covered by media + official notifications) |
| **Green Transition Opportunity** | Green finance support / carbon reduction revenue | Low-Medium (positive, requires actual implementation) | Renewable Energy/Energy Efficiency/EV | **Observable** (green bond issuance / carbon trading data) |

### 2.2 High-Carbon Industry Transition Risk (E1)

#### 2.2.1 Carbon Allowance Cost Transmission Path

```
Carbon Allowance Cost Transmission (National carbon market launched 2021, industry expansion 2025+):

Carbon allowance price increase
  ├── Covered industries (Power -> Steel -> Cement -> Aluminum -> Chemicals, phased expansion)
  │     ├── Carbon allowance deficit enterprises -> Must purchase allowances -> Operating cost increases
  │     │     ├── Can carbon cost be passed to customers? -- Yes -> Gross margin stable but terminal demand may decline
  │     │     └── Cannot pass through -- Gross margin compressed -> EBITDA reduction -> FCF reduction
  │     └── Carbon allowance surplus enterprises -> Sell allowances for additional revenue (e.g., power companies achieving surplus through efficiency upgrades)
  │
  ├── Non-covered industries (no direct carbon cost in short term, but face supply chain pass-through)
  │     └── Upstream supplier carbon cost increase -> Pass-through to procurement prices -> Indirect cost increase
  │
  └── Policy acceleration risk
        └── Free carbon allowance allocation ratio declining year by year (free allocation ratio for power sector declining ~1-2pp annually)
              -> Carbon cost rising year by year, and irreversible
```

#### 2.2.2 Industry Carbon Cost Impact Assessment

| Industry | Carbon Emission Intensity (tCO2/CNY 10K revenue, est.) | Free Allowance Coverage (2025 est.) | Carbon Cost/EBITDA (Carbon price CNY 100/ton scenario) | Credit Impact Rating |
|---|---|---|---|---|
| **Thermal Power** | 8-12 | 95%-97% (declining 1-2pp annually) | 2%-5% | **Low-Medium** (current free allowances sufficient, rising long-term) |
| **Steel (long process)** | 4-6 | 90%-93% | 3%-8% | **Medium** (free allowance declining + carbon price rising) |
| **Cement** | 5-7 | 90%-92% | 4%-10% | **Medium-High** (industry loss-making high, carbon cost sensitive) |
| **Chemicals (coal chemicals)** | 6-10 | 85%-90% | 5%-15% | **High** (carbon intensive + low product differentiation) |
| **Electrolytic Aluminum** | 3-5 | 85%-90% | 3%-8% | **Medium** (power cost already includes indirect carbon) |
| **Pulp & Paper** | 2-4 | 90%-95% | 1%-4% | **Low-Medium** |

**Data Limitation Note**: Industry carbon allowance coverage and free allocation ratios need tracking of national carbon market announcements and allowance allocation plans (published annually). Enterprise-level carbon allowance surplus/deficit is only partially disclosed in listed company ESG reports or CDP reports -- non-listed enterprises almost never disclose.

#### 2.2.3 Transition Risk Red Flag Signal List

| Red Flag Signal | Detection Condition | Signal Strength | Data Source |
|---|---|---|---|
| **Product carbon footprint > 2x industry average** | Enterprise-disclosed per-unit carbon emissions (e.g., ton CO2/ton steel) > industry average x 2 | Medium | ESG report / CDP disclosure (only some enterprises disclose) |
| **No clear carbon reduction plan or target** | Enterprise does not mention carbon reduction targets / carbon neutrality pathway in annual report or ESG report | Medium | Annual report ESG section / Sustainability report |
| **Major product carbon cost ratio > 5% and deteriorating** | Estimated carbon cost (carbon price x emissions) / EBITDA > 5% | Medium-High | Annual report EBITDA + industry emission coefficient estimation |
| **Carbon allowance gap widening (2 consecutive years)** | Enterprise actual emissions > free allowances, purchased allowance volume increasing YoY | Medium-High | Enterprise carbon allowance settlement announcement (national carbon market) |
| **Carbon market compliance overdue or default** | Failure to settle carbon allowances in full and on time (environmental protection authority disclosure) | **Strong** | Environmental protection authority "Carbon Emissions Trading" section |
| **Slow improvement after being listed as key emission entity** | Carbon emission intensity not declining or rising for 2 consecutive years | Medium | Enterprise carbon emission report (national carbon market) |

**Honest Labeling**: Enterprise-level carbon emission data coverage is extremely low. The national carbon market only covers the power generation sector (gradually expanding to steel/cement/aluminum from 2021-2025), and only key emission entities are required to report -- carbon data for SMEs is almost unobtainable. Therefore, the signal density for high-carbon industry transition risk assessment is significantly lower than for environmental penalties.

### 2.3 Environmental Penalties and Production Suspension (E2)

#### 2.3.1 Environmental Penalty -> Credit Transmission Path

```
Environmental penalty event
  │
  ├── Administrative penalty (fine)
  │     └── Fine amount directly reduces profit
  │           Amount <= 10K -- Financial impact negligible (no credit adjustment triggered)
  │           Amount > 1M -- Significant financial impact (especially for small enterprises)
  │           Amount > 5% of net profit -- Material financial impact (needs to be included in assessment)
  │
  ├── Ordered business suspension / production halt (most severe environmental penalty)
  │     ├── No revenue during suspension -- Cash flow interruption (daily loss = daily revenue x gross margin)
  │     ├── Restart requires remediation investment -- Additional capital expenditure
  │     ├── Customers may switch suppliers (especially for tight downstream supply) -- Permanent revenue loss
  │     └── Bank/bond investor attention -- Financing channels may tighten
  │
  ├── Supervised rectification (environmental protection authority)
  │     ├── Listed as key supervision target -- Future regulatory costs increase
  │     └── Public attention -- Reputational damage + financing cost increase
  │
  └── Criminal prosecution (environmental pollution crime)
        ├── Directly responsible personnel sentenced -- Management stability affected
        └── Enterprise listed as environmental dishonesty blacklist -- Affects bank credit / government project bidding
```

#### 2.3.2 Environmental Penalty Red Flag Signal List

| Red Flag Signal | Detection Condition | Signal Strength | Data Source |
|---|---|---|---|
| **Single fine > 1M** | Fine amount in administrative penalty decision issued by environmental protection authority > 1M | Medium | Environmental protection authority website "Administrative Penalties" section |
| **Ordered production suspension / business halt** | Penalty decision includes "ordered production suspension," "production curtailment," "business halt" etc. | **Strong** | Same as above |
| **Listed for supervised rectification** | Listed on environmental protection authority "Supervised Rectification" list | **Strong** | Environmental protection authority website "Supervised Rectification" section |
| **Regional approval restriction by provincial environmental authority** | Project environmental impact assessment approval restricted or suspended | Medium-Strong | Provincial environmental authority announcements |
| **Same enterprise repeatedly penalized (3+ times in 3 years)** | Cumulative environmental penalty records >= 3 (even if individual amounts are small) | Medium | Environmental protection authority historical penalty records |
| **Listed as environmental dishonesty enterprise** | Environmental credit rating "poor" or "severely poor" | Medium-Strong | Enterprise environmental credit evaluation system (established in some jurisdictions) |
| **Pollution monitoring data falsification** | Tampering/falsifying automatic monitoring data confirmed | **Strong** | Environmental protection authority "Environmental Monitoring Data Fraud" section |
| **Reported by central environmental inspection** | Central environmental protection inspection team publishes typical cases | **Strong** | Central environmental inspection team announcements |

**Data Limitation Note**:
- Environmental penalty data comes from proactive disclosure by environmental protection authorities at various levels, with relatively comprehensive coverage (administrative penalty decisions required to be published online).
- However, the following situations may be unobservable:
  1. Small fines (< 5K) may only be posted on local environmental authority websites, and some jurisdictions' disclosure systems have poor timeliness and searchability
  2. Actual implementation of production suspension (whether truly suspended, how long) -- penalty decisions only state "ordered suspension," but actual restart dates are not disclosed
  3. Severity of environmental penalties requires professional judgment: a "fine of 200K" is insignificant for an enterprise with 1B annual profit but material for an SME with 10M annual profit

### 2.4 Environmental Accidents and Ecological Remediation (E3)

| Red Flag Signal | Detection Condition | Signal Strength | Data Source |
|---|---|---|---|
| **Major environmental pollution accident** | Chemical leakage / toxic substance discharge causing environmental damage, widely reported by media or officially notified | **Strong** | Media reports + environmental protection authority notification + company announcement |
| **Soil/groundwater pollution remediation** | Listed in soil pollution remediation registry (must bear remediation costs) | Medium-High | Environmental protection authority "Soil Pollution Prevention" section |
| **Ecological environmental damage compensation** | Subject to ecological environmental damage compensation lawsuit (may involve substantial compensation) | Medium-High | Court judgment database + environmental protection authority disclosure |
| **Biodiversity impact controversy** | Project location involving nature reserves / ecological red lines, project halted | Medium | Environmental protection authority EIA disclosure + media reports |

### 2.5 Green Transition Opportunity (E4) -- Positive Signals

| Positive Signal | Detection Condition | Signal Strength | Credit Impact |
|---|---|---|---|
| **Issuance of green bonds / sustainability-linked bonds** | Successfully issued green bonds / ESG bonds / sustainability-linked bonds (SLBs) | Medium | Financing channels broadened, interest rates may have preferential treatment (green bond rate advantage currently ~10-30bp) |
| **Products/technology with clear carbon reduction benefits** | Solar PV components / wind power / EVs directly contribute to carbon emission reduction, downstream demand inelastic | Medium-High | High revenue growth certainty (policy-driven), strong financing accessibility |
| **Energy efficiency upgrade completed with verifiable results** | Major energy efficiency upgrade completed, per-unit energy consumption significantly reduced (>20% reduction) | Medium | Operating cost reduction + carbon allowance surplus may generate additional revenue |
| **Included in green finance support catalog** | Included in central bank "green loan" support catalog or relevant industry list | Low-Medium | Access to green loan facilities, financing cost reduction |
| **Carbon credit revenue realized** | Successfully registered carbon credit project and generating revenue | Low | Additional revenue source, but typically limited in scale |

---

## 3. S (Social) Risk Assessment

### 3.1 Social Risk Classification System

| Category | Sub-Category | Credit Impact Intensity | Applicable Industries | Data Observability |
|---|---|---|---|---|
| **Workplace Safety Risk** | Major safety accidents / mine disasters / fires / explosions | High (suspension + compensation + management accountability) | Mining/Chemicals/Construction/Manufacturing/Transportation | **Observable** (emergency management authority notification + media reports) |
| **Labor Dispute Risk** | Large-scale strikes / wage arrears / social insurance violations | Medium-High | Manufacturing/Construction/Logistics/F&B | **Partially observable** (only large-scale events reported) |
| **Product Quality Safety** | Product recalls / food safety / drug safety | High | Consumer/Pharma/Food/Automotive | **Observable** (market regulator announcements) |
| **Supply Chain Social Responsibility** | Supplier environmental/labor violations | Medium (indirect) | Brand owners/Retailers/Electronics manufacturing | **Low observability** (typically not publicly available) |
| **Data Privacy / Customer Protection** | Data breaches / infringement of user rights | Medium (tech/financial enterprises) | Internet/Finance/Big Data | **Partially observable** (only after regulatory intervention) |
| **Regional/Community Relations** | Project land acquisition conflicts / forced eviction / community conflicts | Medium (indirect impact of project delays) | Real Estate/Infrastructure/Mining | **Partially observable** (media reports) |

### 3.2 Workplace Safety Risk (S1)

#### 3.2.1 Safety Accident -> Credit Transmission Path

```
Major safety accident
  │
  ├── Immediate consequences
  │     ├── Ordered production suspension (no timeline, depends on remediation inspection)
  │     ├── Casualty compensation (fatality compensation standard: ~100K-150K/person)
  │     ├── Equipment repair / safety upgrade investment
  │     └── Remediation costs
  │
  ├── Regulatory level
  │     ├── Listed as key supervision target by emergency management authority
  │     ├── Safety production license may be suspended/revoked
  │     └── Senior management summoned for questioning / held accountable / dismissed
  │
  ├── Financing channels
  │     ├── Bank credit to the enterprise/group may tighten
  │     ├── Bond issuance plans may be delayed or cancelled
  │     └── Insurance companies may raise premiums / refuse coverage
  │
  └── Long-term impact
        ├── Requires large-scale safety investment -> Capital expenditure increase -> FCF reduction
        ├── Enterprise reputation damaged -> Recruitment difficulty / customer loss / suppliers demand prepayment
        └── If criminal negligence established -> May face criminal prosecution
```

#### 3.2.2 Workplace Safety Red Flag Signal List

| Red Flag Signal | Detection Condition | Signal Strength | Data Source |
|---|---|---|---|
| **Major / extremely major safety accident** | Single accident causing >= 10 deaths (major) or >= 30 deaths (extremely major) | **Strong** | Emergency management authority notification + state council accident investigation report |
| **Severe safety accident** | Single accident causing 3-9 deaths | Medium-Strong | National/provincial emergency management authority notification |
| **General safety accident** | Single accident causing 1-2 deaths | Medium | Provincial/municipal emergency management authority notification |
| **Same enterprise with 2+ safety accidents in 3 years** | Cumulative safety accident count >= 2 (even if individual scale is small) | Medium | Emergency management authority historical accident records |
| **Listed on safety production "blacklist"** | Listed on safety production dishonesty joint punishment list | **Strong** | Emergency management authority website "Safety Production Bad Records" section |
| **Safety production license suspended/revoked** | Confirmed suspension or revocation of license | **Strong** | National/provincial emergency management authority announcement |
| **Summoned for questioning by state council safety committee** | State Council Safety Committee Office summons senior management | Medium | Emergency management authority website + media reports |

**Data Limitation Note**:
- Official notification data for safety production accidents is relatively complete (regulations require hierarchical reporting)
- However, the following situations may be unobservable:
  1. General accidents without fatalities (injury or property damage only) -- may not be publicly reported
  2. Actual duration of production suspension and restart progress -- typically not disclosed
  3. Actual impact of accidents on insurance/credit -- only reflected internally within enterprises

### 3.3 Labor Dispute Risk (S2)

| Red Flag Signal | Detection Condition | Signal Strength | Data Source |
|---|---|---|---|
| **Large-scale strike / collective action** | Media-confirmed strike or collective action involving 100+ people | Medium-Strong | Media reports + local labor inspection notifications |
| **Wage arrears incident** | Confirmed wage arrears by labor inspection authorities, amount > monthly total payroll | Medium | Labor inspection disclosure + media reports (wage arrears more common in construction industry) |
| **Social insurance violations** | Penalized for failing to pay social insurance in full (especially manufacturing with intensive labor use) | Medium | Social insurance authority disclosure (some jurisdictions) |
| **Batch increase in labor arbitration/lawsuits** | Labor dispute cases YoY surge > 100% in one year (signal: deteriorating labor relations) | Low-Medium | Court judgment database (labor arbitration rulings are public) |
| **Involvement in forced labor / child labor** | Exposed by media/NGO for using child labor or forced labor (greater impact with international attention) | **Strong** | Media reports + NGO investigation reports (e.g., HRW/ILO) |
| **Layoff compensation dispute** | Disputes over compensation scheme during mass layoffs (e.g., production disruption due to layoffs) | Medium | Media reports + company announcements |

**Data Limitation Note**: Labor disputes are one of the weakest areas of ESG information disclosure. Media reports are limited by reporting space, labor inspection disclosure coverage is limited, and court judgment database search efficiency is low. For non-listed enterprises, labor dispute signals are almost unobservable -- unless the event escalates to socially concerning levels.

### 3.4 Product Quality Safety Risk (S3)

#### 3.4.1 Credit Impact of Product Quality Events

```
Product quality scandal
  │
  ├── Short-term impact
  │     ├── Product recall cost (recall quantity x unit recall cost)
  │     ├── Regulatory fines (food safety law: maximum fine up to 30x product value)
  │     ├── Inventory write-off (produced but unsalable products)
  │     └── Returns / refund expenses
  │
  ├── Medium-term impact
  │     ├── Sales decline (consumer trust loss, typically lasting 3-12 months)
  │     ├── Channel de-stocking (distributors return goods / stop ordering)
  │     ├── Brand value damage (requires long-term restoration)
  │     └── Regulatory tightening (listed as key inspection target, compliance costs rise)
  │
  └── Credit transmission
        ├── Short-term: One-time cash flow expenditure (recall + fine + returns) -> Liquidity pressure
        ├── Medium-term: Revenue decline -> Working capital self-generation capacity declines -> FCF reduction
        └── Long-term: If core product brand damage is irreversible -> Permanent profitability decline
```

#### 3.4.2 Product Quality Red Flag Signal List

| Red Flag Signal | Detection Condition | Signal Strength | Data Source |
|---|---|---|---|
| **Food/drug safety incident** | Identified as having safety risks by market regulator / drug administration (e.g., melamine contamination-type events) | **Strong** | Market regulator / drug administration announcements |
| **Automotive product recall** | Large-scale product recall due to safety defects (involving core revenue-generating models) | Medium-Strong | National product defect management center |
| **Consumer goods batch recall** | Voluntary/passive recall report submitted to regulator due to quality issues (appliances/children's products/electronics etc.) | Medium | Product defect management center announcements |
| **Public interest lawsuit by consumer association** | Consumer association files consumer civil public interest lawsuit over product quality | Medium-Strong | Consumer association website + court announcements |
| **Media exposure of quality malpractice** | Quality issues exposed by authoritative media (major news outlets / investigative journalism) | Medium | Media reports (requires assessment of channel authority and diffusion extent) |
| **Market share decline due to quality issues** | Industry data shows company market share declining > 2pp for 2 consecutive quarters while industry overall stable | Medium | Industry data (market data platforms or listed company annual report segment revenue disclosure) |
| **Low product quality lawsuit win rate** | Enterprise losing > 60% of product quality dispute cases in court judgment database | Medium | Court judgment database + business information platforms litigation records |

**Data Limitation Note**:
- Product recall data is relatively complete (recall regulations require mandatory reporting and announcement)
- But the early warning window for food/drug safety incidents is extremely short -- typically only known on the same day as regulatory announcement or media exposure, while problems may have been concealed for months before exposure

### 3.5 Social Risk Composite Assessment

| Assessment | Condition |
|---|---|
| **No signal** | No safety accidents, no product quality scandals, no labor dispute reports in 3 years |
| **Weak signal** | Single general safety accident (1-2 deaths) or single minor product quality complaint (no recall) |
| **Medium signal** | Severe safety accident (3-9 deaths) or product batch recall or batch labor disputes |
| **Strong signal** | Major safety accident (10+ deaths) or product quality scandal (food safety/drug safety) or listed on safety production blacklist |
| **Extreme signal** | Extremely major safety accident (30+ deaths) or product quality event leading to core product suspension or enterprise license revocation |

---

## 4. G (Governance) Risk Assessment

### 4.1 Relationship Between This Framework and governance-fraud-risk.md

governance-fraud-risk.md already covers the following governance dimensions:
- Financial fraud red flag signals (revenue quality / profit quality / asset-liability quality / audit opinion)
- Management governance red flags (controlling person risk, management stability, board independence)
- Related party transaction anomaly detection
- Debt evasion risk signals

The governance section of this framework **does not duplicate the above**, but adds the following dimensions not fully covered by governance-fraud-risk.md:

| Governance Dimension | Coverage in governance-fraud-risk.md | New Additions in This Framework |
|---|---|---|
| Equity structure stability | Only covers controlling person change (Section 2.1) | **Expanded**: Control contest, concerted action dissolution, foreign investor exit |
| Board independence | Basic coverage (independent director ratio / non-independence signals, Section 2.3) | **Expanded**: Independent director performance quality, committee effectiveness |
| Information disclosure quality | Only covers violation records (Section 2.4) | **Deep expansion**: Disclosure completeness / comparability / timeliness evaluation |
| Minority shareholder protection | **Not covered** | **New**: Dividend policy, classified voting, minority shareholder voting on related party transactions |

### 4.2 Equity Structure Stability (G1 New)

| Red Flag Signal | Detection Condition | Signal Strength | Data Source |
|---|---|---|---|
| **Control contest / control dispute** | Based on announcements / media reports, company has open control contest (e.g., two or more shareholders simultaneously claiming control, board composition dispute) | **Strong** | Company announcements + media reports + exchange inquiry letters |
| **Concerted action agreement expires without renewal** | Concerted action agreement expires without renewal, leading to controlling person's shareholding falling to < 30% or no controlling person | Medium-Strong | Company announcements (equity change report) |
| **Major shareholders simultaneously reducing holdings** | Multiple major shareholders (non-related parties) concentrated reduction in same quarter (possible signal: insiders collectively bearish) | Medium | Company announcements (shareholder reduction plan disclosure) |
| **Strategic investor exit** | Well-known strategic investor (e.g., sovereign investment fund / industrial capital) rapidly exits in full after lock-up period expires | Medium | Company announcements + quarterly report shareholder changes |
| **Systematic foreign investor exit** | Cross-border stock connect program holdings continuously declining > 50% for 3 months (only applicable to connect-eligible stocks) | Medium | Cross-border stock connect daily data |
| **Equity pledge margin call risk** | Market price of pledged equity falls below forced liquidation line (governance-fraud-risk.md already has pledge ratio detection; this adds "already breached margin call line" red alert) | **Strong** | Company announcements (supplementary pledge / pledge extension) + stock price data |
| **Listed company subject to hostile takeover bid** | External investor increases holdings via secondary market to > 5% (not necessarily hostile -- depends on bidder intent and company countermeasures) | Medium | Company announcements (simplified/detailed equity change report) |

**Data Limitation Note**: Equity structure data accessibility is relatively high -- listed companies must disclose shareholders with >= 5% shareholding and changes. However, the following situations may be unobservable:
- Arrangements behind concerted action agreements (side letters, nominee holdings) -- only exposed when challenged by regulators or in litigation
- Specific investors' willingness to transfer shares -- only announced when reaching disclosure threshold (changes > 5%)
- Non-listed enterprises (LGFVs / private enterprises) -- equity structure almost no public data

### 4.3 Board Independence and Committee Effectiveness (G2 Expanded)

| Red Flag Signal | Detection Condition | Signal Strength | Data Source |
|---|---|---|---|
| **Independent director repeated absence from meetings** | Independent director absent from board meetings 3+ consecutive times (indicating non-diligence) | Medium | Annual report "Board Meeting Convening" section |
| **Independent director votes against / abstains on proposals** | Independent director votes against or abstains on important proposals (e.g., related transactions, external guarantees, profit distribution) in annual/semi-annual report | **Strong** | Company announcements (independent director opinions on relevant matters) |
| **Audit committee meeting frequency abnormally low** | Annual audit committee meetings < 2 times (annual audit should have at least 2: pre-audit + post-audit) | Medium | Annual report "Corporate Governance" section |
| **Remuneration and appraisal committee ineffective** | Executive compensation scheme clearly unreasonable (e.g., total compensation still growing in loss-making years) with no committee objection | Medium | Annual report + Remuneration committee report |
| **Nomination committee role weakened** | All director candidates nominated by major shareholder rather than nomination committee selection (weak governance independence) | Medium | Annual report + shareholder meeting announcements |
| **Internal audit reports directly to management** | Internal audit head reports to CFO or CEO rather than audit committee (already mentioned in governance-fraud-risk.md, confirmed here) | Medium | Annual report "Corporate Governance" section internal audit system description |

### 4.4 Information Disclosure Quality Assessment (G3 New)

| Assessment Dimension | Detection Indicator | Signal Strength | Data Source |
|---|---|---|---|
| **Completeness** | Annual report has "significant missing items" (e.g., failure to disclose top 5 customer names / related transaction details / R&D investment) | Medium-Strong | Annual report chapter-by-chapter review |
| **Completeness** | Whether ESG/sustainability report is disclosed as required by exchange (major exchanges now require certain index constituents to disclose) | Medium | Exchange announcements + company announcements |
| **Timeliness** | Record of delayed annual/quarterly report disclosure (covered in governance-fraud-risk.md, supplemented here) | **Strong** | Exchange regulatory records + company announcements |
| **Timeliness** | Major matters (major litigation / guarantees / related transactions / asset restructuring) announced within 2 trading days | Medium | Company announcement time vs event time comparison (requires cross-verification) |
| **Accuracy** | "Correction announcements" in past 3 years (material data corrections to published annual/quarterly reports) | Medium-Strong | Company announcement "Correction Announcements" |
| **Accuracy** | Whether exchange inquiry letters received (annual report inquiry / restructuring inquiry / attention letters) and response quality | Medium-Strong | Exchange website "Inquiry Letter Response" section |
| **Consistency** | Whether same indicator data is consistent across different sections (e.g., segment revenue to total revenue reconciliation, notes to main statements consistency) | Medium | Annual report cross-checking |

**Data Limitation Note**:
- Information disclosure quality assessment is highly dependent on the completeness of the annual report itself -- if the enterprise "does not disclose as per regulations" (e.g., non-listed enterprises), or "discloses as per regulations but with minimal information content" (template-based "management analysis"), this framework cannot make effective assessment
- For LGFVs -- information disclosure quality is typically low (simple financial data, non-detailed notes, no ESG report disclosure), but this is industry practice rather than a signal of individual governance issues

### 4.5 Minority Shareholder Protection (G4 New)

| Red Flag Signal | Detection Condition | Signal Strength | Data Source |
|---|---|---|---|
| **Abnormal dividend policy** | ① Profitable for 3 consecutive years but no dividends (exchanges encourage cash dividends but no mandatory requirement) ② Suddenly significantly reducing dividend ratio without reasonable explanation | Medium | Annual report profit distribution plan + shareholder meeting resolution |
| **Defeated in classified voting** | Related transactions / external guarantees / major asset restructuring rejected by minority shareholders in classified voting | Medium | Shareholder meeting resolution announcements |
| **Severe dilution from rights issue/placement** | Rights issue/placement dilutes EPS > 20% and issue price significantly below net asset value (harming minority shareholder interests) | Medium | Rights issue/placement announcements + financial data |
| **Takeover offer pricing questioned as unfair** | Takeover offer price below net asset value per share or significantly below market price, with independent financial advisor issuing "unfair" opinion | Medium-Strong | Company announcements (independent financial advisor report) + exchange inquiry letters |
| **Unequal asset transaction between listed company and related party** | Listed company acquires assets from related party at high price / sells assets at low price (suspicion of benefit transfer) -- linked with governance-fraud-risk.md related transaction detection | **Strong** | Annual report related transaction notes + asset appraisal report |
| **Articles of association clauses harming minority shareholder rights** | Such as restricting shareholder proposal rights, supermajority voting requirements, etc. | Medium | Company articles of association |

### 4.6 Governance Risk Composite Assessment

| Assessment | Condition |
|---|---|
| **No signal** | Stable equity structure + independent directors properly performing duties + timely and accurate information disclosure + no minority shareholder rights disputes |
| **Weak signal** | Single dimension weak signal (e.g., one-time independent director absence / dividend ratio decline / exchange inquiry letter received but response adequate) |
| **Medium signal** | Significant equity change (concerted action not renewed / strategic investor exit) + or information disclosure accuracy concerns + or minority shareholder voting divergence |
| **Strong signal** | Control contest + or independent directors collectively resign / vote against + or related transaction unfairness challenged + or regulatory determination of information disclosure violation |
| **Extreme signal** | Linked with governance-fraud-risk.md veto conditions (confirmed financial fraud / controlling person under investigation / core asset stripping) |

---

## 5. ESG-to-Credit Mapping

### 5.1 Core Mapping Relationships

| ESG Event Type | Credit Transmission Path | Transmission Speed | Impact Dimension | Adjustment Magnitude |
|---|---|---|---|---|
| **Major environmental penalty (production suspension ordered)** | Suspension -> Cash flow interruption -> Interest coverage collapse -> Financing channels closed | **Fast (1-3 months)** | Short-term cash flow + financing accessibility | **-0.5 to -1 notch** |
| **Environmental fine (large amount but no suspension)** | Fine -> Profit reduction -> FCF reduction (limited impact on large enterprises) | **Medium (6-12 months)** | Income statement | **0 to -0.5 notch** (typically no adjustment) |
| **High-carbon industry transition risk exposure** | Carbon cost increase -> Profit margin compression -> Competitiveness decline -> Credit quality deterioration | **Slow (2-5 years)** | Long-term profitability + financing cost | **-0.5 notch** (only triggered by landmark events) |
| **New green bond issuance / green finance support** | Financing channels broadened -> Financing cost slightly reduced -> Liquidity improvement | **Medium (6-12 months)** | Financing structure | **0 to +0.5 notch** (upward trigger rare) |
| **Major safety accident (suspension)** | Suspension -> Revenue interruption -> Compensation expenditure -> Regulatory penalties -> Financing tightening | **Fast (1-3 months)** | Short-term cash flow + financing accessibility | **-0.5 to -1 notch** |
| **Product quality scandal (food/drug)** | Recall + fine + returns -> Cash flow expenditure -> Customer loss -> Revenue decline | **Medium-Fast (3-6 months)** | Short-term cash flow + medium-term revenue | **-0.5 to -1 notch** |
| **Product recall (non-food/drug)** | Recall cost -> Brand damage -> Future revenue may decline | **Medium (6-12 months)** | Medium-term revenue + brand value | **-0.5 notch** |
| **Labor dispute (strike / wage dispute)** | Work stoppage -> Production disruption -> Compensation -> Reputation damage | **Medium (3-6 months)** | Short-term production + medium-term reputation | **0 to -0.5 notch** (depending on scale) |
| **Control contest / control instability** | Management instability -> Strategic vacillation -> Investment decision stagnation -> Credit quality uncertainty increases | **Slow (12-24 months)** | Strategic execution + financing accessibility | **0 to -0.5 notch** |
| **Information disclosure violation penalized** | Data credibility damaged -> Capital market trust declines -> Financing cost increases | **Medium (6-12 months)** | Financing accessibility + investor relations | **-0.5 notch** |
| **Independent directors collectively resign / vote against** | Governance signal deterioration -> Investor questioning -> Stock/bond price decline | **Fast (1-3 months)** | Market confidence + financing flexibility | **-0.5 notch** |
| **Related transaction unfairness challenged** | Suspicion of benefit transfer -> Minority shareholder / creditor trust declines -> Financing tightens | **Medium (6-12 months)** | Financing accessibility + legal risk | **-0.5 notch** |

### 5.2 Adjustment Magnitude Determination Rules

```
Adjustment magnitude = f(Event severity, Financial flexibility, Industry characteristics, External environment)

Event severity:
  ├── Level I (Fatal): Core business suspended / core product banned / license revoked -> -1 notch
  ├── Level II (Major): Major safety accident / food/drug safety scandal / suspension -> -0.5 to -1 notch
  ├── Level III (Medium): Batch recall / heavy penalty / equity dispute -> -0.5 notch
  ├── Level IV (Minor): Small fine / minor notification -> 0 (annotate but no adjustment)
  └── Positive (Green): Green bonds / carbon reduction revenue -> +0 to +0.5 notch (rare)

Financial flexibility weight:
  ├── Interest coverage > 5x + cash runway > 12 months -> Strong event impact buffer -> Adjustment magnitude halved
  └── Interest coverage < 2x + cash runway < 6 months -> Weak buffer -> Adjustment magnitude at upper limit

Industry characteristic weight:
  ├── High-carbon industries (environmental event weight x 1.5)
  ├── Consumer brands (product quality event weight x 1.5)
  └── Financial enterprises (governance/compliance event weight x 1.5)
```

### 5.3 Adjustment Rules Quick Reference

| Signal Strength | ESG Adjustment Magnitude | Trigger Condition |
|---|---|---|
| No signal | 0 | No anomalies across dimensions |
| Weak signal | 0 (annotate risk, no rating adjustment) | Single minor event (e.g., small fine, one-time independent director absence) |
| Medium signal (single event triggered) | -0.5 notch | Level II event or 2+ Level III events occurring simultaneously |
| Strong signal (event stacking or fatal level) | -0.5 to -1 notch | Level I event, or Level II event + weak financial flexibility + high industry sensitivity |
| Extreme signal | Triggers non-credit risk veto | ESG event leads to irreversible loss of core business (e.g., license revoked) |

### 5.4 Adjustment Annotation Template

```yaml
# ESG overlay adjustment description
esg_adjustment: -0.5                       # ESG overlay adjustment magnitude
trigger_event: "Major safety accident (3 fatalities)"       # Triggering event
credit_transmission: "Production suspension -> Cash flow interruption -> Interest coverage deterioration -> Financing tightening"
financial_elasticity: "Medium (interest coverage 3.2x, cash runway 9 months)"
industry_sensitivity: "High (chemicals industry, environmental/safety historical penalty record)"
data_availability:
  environment: "Observable (emergency management authority notification)"
  social: "Observable (accident publicly reported)"
  governance: "Partially observable (business registration changes completed but equity details unavailable)"
adjustment_rationale: "Major safety accident triggers production suspension + compensation expenditure; enterprise financial flexibility is medium; chemicals industry is sensitive to safety events; composite judgment: -0.5 notch adjustment"
```

---

## 6. Overlay Adjustment Rules

### 6.1 ESG Overlay Subordination to non-credit-risk-overlay

This ESG framework operates as a sub-module of the non-credit-risk-overlay.md:

```
Non-Credit Risk Overlay (non-credit-risk-overlay.md)
  ├── Market Risk (20%)
  ├── Operational Risk (30%)  <- Includes governance-fraud-risk.md fraud signals + ESG governance signals
  ├── Reputational Risk (15%)  <- Includes ESG environmental + social event signals
  ├── Strategic Risk (25%)
  ├── Liquidity Risk (10%)
  └── * ESG Specialized Assessment (this framework) <- Integrates E/S/G full-dimension assessment, provided as independent input to the overlay
                                       Adjustment magnitude already within +/-1 notch limit of non-credit-risk-overlay
```

### 6.2 Division Between ESG and Existing Governance Modules

| Assessment Content | Assigned Module | Description |
|---|---|---|
| Financial fraud detection | governance-fraud-risk.md -> Operational Risk | Not duplicated |
| Related transaction anomaly detection | governance-fraud-risk.md -> Operational Risk | Not duplicated |
| Debt evasion risk detection | governance-fraud-risk.md -> Operational Risk | Not duplicated |
| Management governance (pledge/change/resignation) | governance-fraud-risk.md -> Operational Risk | Not duplicated |
| Equity structure stability (Section 4.2 new) | governance-fraud-risk.md (expanded) + this framework G1 | This framework adds control contest, concerted action, foreign investor exit not covered by g-f-r.md |
| Information disclosure quality (Section 4.4 new) | **This framework G3** | New dimension |
| Minority shareholder protection (Section 4.5 new) | **This framework G4** | New dimension |
| Environmental assessment (E) | **This framework** | New dimension |
| Social assessment (S) | **This framework** | New dimension |

### 6.3 Interactive Effects of Overlay Adjustments

When ESG signals appear simultaneously with other risk signals in non-credit-risk-overlay.md, the overlay rules (Section 9.3) of non-credit-risk-overlay.md apply:

| Scenario | Handling Rule |
|---|---|
| **ESG event simultaneously triggers reputation + operational risk** | Counted as 1 event, but select the most severe dimension direction for scoring (no double deduction) |
| **ESG signals stacking with other non-credit risk signals** | Composite signal strength calculation, does not exceed +/-1 notch cumulative cap |
| **ESG signal overlapping with governance-fraud-risk.md signal** | No double deduction -- same event only triggers one adjustment, select the transmission path with greatest impact |

---

## 7. Data Availability Honest Labeling

### 7.1 Data Coverage Assessment by ESG Dimension

| Dimension | Observable Ratio (est.) | Main Data Sources | Key Gaps | Impact of Gaps |
|---|---|---|---|---|
| **E (Environment - penalties/accidents)** | 60-70% | Environmental protection authority announcements, emergency management authority notifications, media reports | Small fines (< 5K) not published online; actual suspension duration not disclosed; non-listed enterprise environmental data missing | **Acceptable** -- major environmental events essentially detectable, omissions mainly minor events |
| **E (Environment - carbon emissions)** | 20-30% | National carbon market disclosures, ESG reports, CDP | Enterprise-level carbon emission data coverage extremely low; non-listed enterprises / non-carbon-market-covered industries have no data | **Severe** -- data foundation for high-carbon industry transition risk assessment is weak |
| **E (Environment - green opportunities)** | 70-80% | Green bond announcements, green loan statistics, carbon trading data | Credit impact of green finance support difficult to quantify (does it materially reduce financing cost?) | **Medium** -- positive signals have high data accessibility but credit impact uncertain |
| **S (Safety - major accidents)** | 70-80% | Emergency management authority notifications, accident investigation reports, media reports | General accidents without fatalities not disclosed; suspension/restart timeline not disclosed; compensation amounts not disclosed | **Acceptable** -- major safety accidents essentially detectable |
| **S (Labor disputes)** | 20-30% | Media reports, labor inspection disclosures, court judgment database | Most labor disputes invisible (not escalated to media attention level); non-listed enterprises have no channels | **Severe** -- labor dispute detection capability is seriously insufficient |
| **S (Product quality)** | 50-60% | Product defect management centers, drug administration, media reports | Pre-recall quality risk period unobservable; non-mandatory-recall product quality issues unobservable | **Medium** -- public recalls/penalties detectable, but hidden quality risks unobservable |
| **G (Equity structure)** | 60-70% | Equity change reports, quarterly shareholder information, business information platforms | Non-listed enterprise equity structure not transparent; concerted action side letters invisible | **Medium** -- strong detection for listed enterprises, weak for non-listed |
| **G (Information disclosure quality)** | 50-60% | Annual/quarterly reports, exchange inquiry letters, correction announcements | Non-listed enterprises have no mandatory disclosure obligation; deep issues in disclosure quality (template-style disclosure, selective disclosure) difficult to quantify | **Medium** -- listed enterprises can be indirectly assessed through inquiry letters / correction announcements |
| **G (Minority shareholder protection)** | 40-50% | Shareholder meeting resolutions, classified voting announcements, dividend plans | Behind-the-scenes arrangements between major and minority shareholders (side letters) unobservable; "voting with feet" (shareholder reduction) is a lagging signal | **Medium** -- classified voting and dividend data accessible, but benefit transfer not directly observable |

### 7.2 ESG Detection Capability by Entity Type

| Entity Type | E Environment (penalties/accidents) | S Social (safety/quality) | G Governance (structure/disclosure) | Comprehensive ESG Detection Capability |
|---|---|---|---|---|
| **Listed + bond-issuing enterprises** | Relatively high | Relatively high | Relatively high | **Best** (multi-dimensional ESG information accessible) |
| **Listed non-bond-issuing enterprises** | Relatively high | Relatively high | Relatively high | **Good** (no bond market ESG pricing signal) |
| **Non-listed bond-issuing enterprises (SOEs/LGFVs)** | Relatively high | Medium | Medium | **Medium** (annual reports accessible, but ESG-specific disclosures limited, governance transparency low) |
| **Non-listed bond-issuing enterprises (private)** | Medium | Low-Medium | Low-Medium | **Weak** (ESG data severely insufficient, relies on business registration and penalty records) |
| **Non-listed non-bond-issuing enterprises** | Low | Low | Low | **Extremely low** (almost no public ESG data -- this framework not applicable to such entities) |

### 7.3 Honest Statement

> **ESG Assessment Statement**: This framework has the following inherent limitations for ESG risk assessment of bond market issuers:
>
> 1. **Event-driven rather than forward-looking**: Limited by ESG data disclosure coverage (only approximately 30-40% of bond issuers disclose sufficient information), this framework currently centers on "negative event detection" rather than "forward-looking ESG scoring." This means: ① An enterprise without public ESG events does not imply low ESG risk -- it may simply mean its ESG data is not disclosed or events not exposed; ② ESG forward-looking assessment (e.g., carbon transition pressure) is only applicable to specific industries (high-carbon industries + enterprises with carbon emission disclosures), with limited coverage.
>
> 2. **Extremely weak ESG detection capability for non-listed entities**: For sub-national LGFVs and non-listed SMEs, this framework's ESG signal density is extremely low. Investor risk judgment should primarily rely on industry characteristics and financial analysis, rather than missing ESG data.
>
> 3. **ESG event signals have lag**: There is a time gap between ESG event occurrence and public observability -- environmental penalties typically lag 1-3 months (from inspection to case filing to penalty decision to online publication), safety accidents lag several days (from occurrence to notification), and the early warning window for product quality scandals may be zero (exposure equals outbreak).
>
> 4. **Does not substitute professional ESG ratings**: This framework does not provide independent ESG rating scores or ESG investment advice. Its sole objective is to assess the impact of ESG events on credit quality -- it is an overlay layer within the credit analysis framework, not an independent ESG assessment tool.
>
> 5. **Adjustment magnitude limit**: ESG overlay adjustments do not exceed +/-1 notch (consistent with non-credit-risk-overlay.md) and do not alter the governance/fraud risk veto conditions in governance-fraud-risk.md.

---

## 8. Integration with Existing Frameworks

### 8.1 Integration in non-credit-risk-overlay.md

After this framework is published, ESG-related signals in the Operational Risk (Section 4) and Reputational Risk (Section 5) chapters of non-credit-risk-overlay.md can directly reference this framework:

| Signal in non-credit-risk-overlay.md | Reference to This Framework |
|---|---|
| 4.3.2 Regulatory penalties -- "environmental administrative penalties" | This framework E2 (Environmental Penalties and Production Suspension) provides detailed transmission path |
| 5.3.1 ESG controversial events (major environmental accidents, labor disputes, product quality scandals, supply chain ESG violations) | This framework E2/E3/S1/S2/S3/S4 provides categorical detection and transmission analysis |
| 4.3.3 Key personnel risk -- "sudden departure of CEO/CFO" | This framework 4.2 (Equity Structure Stability) and 4.6 (Governance Risk Composite Assessment) provide governance perspective |
| 5.3.3 Customer/supplier relationships | This framework S3 (Product Quality Safety Risk) customer loss transmission path |

### 8.2 Integration in industry-framework.md

In the industry pyramid, L1 policy layer environmental/social policy content should include ESG sensitivity annotation:

```
At the end of each industry pyramid L1 layer, add:
  WARNING: ESG Risk Sensitivity Annotation:
  This industry belongs to [High/Medium/Low] ESG sensitivity industry.
  Environmental sensitivity: [High/Medium/Low] -- Rationale: [e.g., high-carbon industry, significant carbon cost impact]
  Social sensitivity: [High/Medium/Low] -- Rationale: [e.g., labor-intensive, frequent safety accidents]
  Governance sensitivity: [High/Medium/Low] -- Rationale: [e.g., private enterprise, prominent controlling person risk]
  See esg-framework.md (Appendix A: Industry ESG Sensitivity Cross-Reference).
```

### 8.3 Signal Integration in mosaic-engine.md

ESG signals generated by this framework should be included in the mosaic engine's signal inventory, tagged as "ESG" type:

```
Signal type: ESG (Environmental, Social, Governance)
Signal sub-type: E (Environmental), S (Social), G (Governance)
Signal density: Based on ESG data availability (listed enterprises + high-carbon industries have higher density; non-listed/non-sensitive industries have lower density)
Confidence:
  High: Official penalty / regulatory announcement / company-confirmed ESG events
  Medium: ESG events with media coverage but no official confirmation
  Low: Indirect inference (e.g., industry analysis indicates ESG risk exposure but no specific events)
```

---

## Appendix A: Industry ESG Sensitivity Cross-Reference

| Industry | E Environmental Sensitivity | S Social Sensitivity | G Governance Sensitivity | Most Sensitive ESG Dimension | Notes |
|---|---|---|---|---|---|
| **Coal** | **High** (emissions + safety + environment) | **High** (mine disaster risk) | Medium | E+S | Transition risk + safety accidents are core ESG credit factors for this industry |
| **Steel** | **High** (emissions + environment) | **High** (safety + occupational disease) | Medium | E | Carbon cost increase is a structural risk for this industry |
| **Chemicals** | **High** (environment + emissions + accidents) | **High** (safety + environmental accidents) | Medium | E+S | Safety and environmental penalties are the most frequent ESG events in this industry |
| **Cement** | **High** (emissions + environment) | Medium (safety) | Medium | E | Carbon cost + environmental production curtailment are core industry risks |
| **Power** | **High** (thermal power emissions) | Low | Medium | E | Transition risk varies by sub-type (high for thermal power, low for renewables) |
| **Solar/Wind** | Medium (manufacturing environment) | Low-Medium | Medium | E (positive) | Green premium + carbon reduction revenue are positive credit factors |
| **Semiconductor** | Medium (manufacturing environment + water usage) | Low-Medium | **High** | G | Governance (equity/information/technology security) most important |
| **Biopharma** | Low-Medium (wastewater/emissions) | **High** (drug safety) | Medium | S | Drug safety is the most fatal ESG event |
| **Medical Devices** | Low | **High** (product quality) | Medium | S | Product quality events directly lead to recall + brand damage |
| **Food & Beverage** | Low | **High** (food safety) | Medium | S | Food safety events directly threaten enterprise survival |
| **Automotive** | Medium (emissions + production environment) | **High** (product safety + recall) | Medium | S | Cost and reputational impact of automotive recalls is enormous |
| **New Energy Vehicles** | Medium (positive: carbon reduction) | Medium (product safety) | Medium | E+S | Battery safety + carbon reduction benefits, bidirectional |
| **Data Centers** | **High** (energy consumption + carbon neutrality) | Low | Medium | E | Energy consumption metrics are core operational constraints |
| **Banks/Brokerages** | Low | Low-Medium (data/customer protection) | **High** | G | Governance (compliance + capital) is the most sensitive ESG dimension |
| **Real Estate** | Medium (green building) | Medium (community/labor) | **High** | G | Governance (related transactions + fund occupation + information disclosure) is key |
| **LGFV** | Low-Medium | Low | Medium | G (disclosure quality) | LGFV ESG risk mainly from non-transparent information disclosure |
| **Logistics/Transportation** | Medium (emissions) | Medium (safety + labor) | Medium | E+S | Carbon emission cost + driver safety are main risks |
| **Textile/Apparel** | Medium (environment + supply chain ESG) | **High** (labor + supply chain) | Medium | S | Labor rights and supply chain ESG compliance are key |
| **Pulp & Paper** | **High** (environment + water resources) | Medium | Medium | E | Environmental penalties are main ESG risk |

---

## Appendix B: Public Data Source List

### Environmental (E) Data Sources

| Data Item | Specific Data Source | Free/Paid | Update Frequency | Coverage |
|---|---|---|---|---|
| Environmental administrative penalties | Environmental protection authority websites "Administrative Penalties" section | Free | Real-time | Above provincial level relatively high coverage; municipal/county level varies |
| Environmental protection authority supervised rectification | Environmental protection authority website "Supervised Rectification" section | Free | Real-time | National coverage |
| Central environmental inspection reports | Environmental protection authority "Central Environmental Protection Inspection" section | Free | Batch (published after each inspection round) | National coverage |
| National carbon market data | Carbon emissions exchange websites | Free (basic data) | Daily | National carbon market covered industries (thermal power covered, expanding to steel/cement/aluminum from 2025) |
| Enterprise carbon emission reports (key emitters) | Carbon emissions trading registration system (requires enterprise authorization) | Restricted | Annual | Only key emission entities |
| Enterprise environmental credit rating | Provincial environmental credit evaluation systems | Free | Annual | Some jurisdictions established |
| Soil pollution remediation registry | Environmental protection authority "Soil Pollution Prevention" section | Free | Irregular | Covers sites listed in remediation registry |
| Listed company ESG reports | Financial information portals, stock exchange "Sustainability Report" sections | Free | Annual | Only ~30% of listed companies publish |
| Carbon credit project registration | Voluntary emissions trading information platforms | Free | Irregular | Covers registered carbon credit projects |

### Social (S) Data Sources

| Data Item | Specific Data Source | Free/Paid | Update Frequency | Coverage |
|---|---|---|---|---|
| Safety accident notifications | Emergency management authority website "Accident Investigation" / "Early Warning" sections | Free | Real-time | Full coverage of major+ accidents, partial coverage of severe accidents |
| Safety production blacklist | Emergency management authority "Safety Production Severely Dishonest Entity List" | Free | Real-time | National coverage |
| Product recall information | Product defect management center | Free | Real-time | Full coverage of mandatory recalls |
| Food safety notifications | Market regulator "Food Safety" section | Free | Real-time | National food safety inspection coverage |
| Drug safety notifications | Drug administration "Drug Inspection" / "Drug Recall" sections | Free | Real-time | Coverage of drug safety events |
| Consumer complaint information | Consumer association website | Free | Quarterly | Summary data only, no enterprise-level detail |
| Court judgments (labor disputes) | Court judgment database | Free | Real-time | Coverage 50-70% |
| Media reports | WebSearch / News databases | Free (basic) | Real-time | Only major events |

### Governance (G) Data Sources

| Data Item | Specific Data Source | Free/Paid | Update Frequency | Coverage |
|---|---|---|---|---|
| Company announcements (equity changes / reductions / pledges) | Financial information portals, stock exchange websites | Free | Real-time | Full coverage of listed enterprises |
| Annual / semi-annual / quarterly reports | Financial information portals, exchange disclosure systems | Free | Annual/semi-annual/quarterly | Full coverage of listed enterprises |
| Exchange inquiry letters / regulatory letters | Stock exchange "Regulatory Information Disclosure" sections | Free | Real-time | Full coverage of listed enterprises |
| Independent director opinions | Company announcements "Independent Director Opinions on Relevant Matters" | Free | Real-time | Full coverage of listed enterprises |
| Shareholder meeting resolutions (including classified voting results) | Company announcements "Shareholder Meeting Resolution Announcements" | Free | Real-time | Full coverage of listed enterprises |
| Business registration changes | National enterprise credit information disclosure system | Free (basic) | Real-time | Full enterprise coverage |
| Related party information | Annual report "Related Party Relationships" section + business information platforms | Free (basic) | Annual | Full coverage of listed enterprises |
| Enterprise credit report (including penalties/litigation) | National enterprise credit information disclosure system "Administrative Penalties / Operating Anomalies / Serious Law-Breaking Dishonesty" | Free | Real-time | Full enterprise coverage |

---

## Related Content

- [Non-Credit Risk Overlay](non-credit-risk-overlay.md) -- Entry point for ESG signals and overlay adjustment framework
- [Governance and Financial Fraud Risk Analysis Module](governance-fraud-risk.md) -- Financial fraud / related transactions / debt evasion detection in governance dimension (this framework's governance section interacts with it)
- [Engine Architecture Overview](engine-overview.md) -- Core concepts, overall architecture, design principles
- [Industry Classification and Analysis Framework](industry-framework.md) -- Industry ESG sensitivity cross-reference (Appendix A)
- [Mosaic Engine](mosaic-engine.md) -- Inclusion and completeness assessment of ESG-type signals
- [Dual-Track Analysis Methodology](dual-track-methodology.md) -- ESG signal processing in the cross-validation matrix
- [Rating Outlook and Continuous Monitoring Framework](outlook-monitoring-framework.md) -- ESG event monitoring trigger conditions
