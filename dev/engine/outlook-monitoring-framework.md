# Rating Outlook and Continuous Monitoring Framework

**Version**: v0.0.2 | **Date**: 2026-07-10 | **Positioning**: On top of dual-track static ratings, add forward-looking direction and continuous monitoring mechanisms

---

## 1. Why Outlook and Monitoring Are Needed

### 1.1 The Current Engine Gap

The current engine (v0.0.2) outputs a **static snapshot rating** (AAA through D) that only reflects the credit quality assessment at the time of analysis. Beyond static ratings, professional rating agencies consistently maintain **three time dimensions**:

| Time Dimension | Traditional Rating Output | Engine Current State | Gap |
|---|---|---|---|
| **Current moment** | Rating (AAA-D) | Implemented | -- |
| **12-24 months** | Outlook (Positive/Stable/Negative) | **Missing** | Cannot convey directional trends in credit quality |
| **Within 90 days** | Watchlist (Positive Watch/Negative Watch) | **Missing** | Cannot respond quickly to near-term credit events |

### 1.2 Practical Problems from Both Missing Components

| Scenario | Without Outlook | Without Watchlist |
|---|---|---|
| **Rating maintained at BB+ but trend deteriorating** | User assumes "risk is controllable" | -- |
| **Sudden asset transfer announcement** | -- | User cannot assess whether action is needed within 90 days |
| **Abrupt industry policy shift** | Rating unchanged but risk has risen significantly | Lack of warning time window |
| **Multiple signals pointing in different directions** | Cannot express uncertainty of "inconsistent directional assessment" | -- |

### 1.3 Position of Outlook and Watchlist in the Overall Architecture

```
Engine Output (before v0.0.1)
  ├── Rating (AAA ~ D)                         ← Static Snapshot
  └── Signal Completeness Report

Engine Output (v0.0.1 + this module)
  ├── Rating (AAA ~ D)                         ← Current credit quality assessment
  ├── Outlook: Positive / Stable / Negative               ← 12-24 month directional assessment  ★New
  ├── Watchlist: Positive Watch / Negative Watch / None    ← Potential rating action within 90 days  ★New
  ├── Continuous Monitoring Checklist                      ← Items requiring active monitoring  ★New
  └── Signal Completeness Report
```

---

## 2. Rating Outlook Mechanism (12-24 Month Directional Assessment)

### 2.1 Definition of Outlook and Probability Criteria

The outlook is a **probabilistic assessment** of the direction of rating changes over the next 12-24 months, not a precise prediction.

| Outlook | Definition | Probability Threshold | Time Window |
|---|---|---|---|
| **Positive** | Probability of a 1-2 notch rating upgrade within the next 12-24 months >= 50% | >= 50% | 12-24 months |
| **Stable** | Probability of rating remaining unchanged within the next 12-24 months >= 70% | >= 70% | 12-24 months |
| **Negative** | Probability of a 1-2 notch rating downgrade within the next 12-24 months >= 50% | >= 50% | 12-24 months |
| **Developing** | Rating may be upgraded or downgraded within the next 12-24 months, direction unclear | -- | 12-24 months |

**Additional Definitions**:

| Concept | Explanation |
|---|---|
| **Outlook Adjustment Window** | The outlook rating is valid for 12-24 months from the date of issuance; reassessment is required upon expiry |
| **Notch Change** | 1 notch = one rating step (e.g., BBB+ to BBB-), 2 notches = two steps (e.g., A- to BBB+) |
| **Handling Directional Uncertainty** | When positive and negative signals exist simultaneously with comparable weight, use "Developing" outlook and annotate bidirectional trigger conditions |

### 2.2 Outlook Trigger Factor Matrix

Outlook signals are extracted from the engine's existing pyramid layers (L1-L4) and the external support layer. Each trigger factor includes a **data source** and **signal direction**.

#### Positive Outlook Trigger Signals

| Pyramid Layer | Positive Outlook Trigger Signal | Data Source | Verification Method |
|---|---|---|---|
| **L1 Policy/Macro** | Industry policy explicitly increases support (subsidy extension/tax incentive expansion/capacity quota relaxation) | MIIT/NDRC/MOF official announcements | Cross-verification of policy document text + industry association interpretation |
| **L1 Policy/Macro** | Industry added to national strategic support list (e.g., IC Grand Fund/New Energy Special Program) | State Council/NDRC industry planning documents | WebSearch policy text analysis |
| **L1 Policy/Macro** | Financial regulatory orientation trends looser (increased credit quotas/faster bond issuance approval) | PBOC/CBIRC policy documents | Open market operation announcements + interbank market data |
| **L2 Technology/Competition** | Technology roadmap confirmed as industry mainstream (e.g., BC tech receives >50% share in central enterprise centralized procurement) | Central enterprise procurement results announcements, industry association white papers | WebSearch bidding data cross-verification |
| **L2 Technology/Competition** | Key market access qualification obtained (e.g., innovative drug NDA approval/medical device registration certificate) | NMPA/CDE announcements | Government affairs open platform announcement confirmation |
| **L2 Technology/Competition** | Market share continues to expand (market share increase for 2+ consecutive quarters) | Industry association data, brokerage research reports | WebSearch industry data aggregation |
| **L3 Supply Chain/Operations** | Vertical integration completed and operational (raw material self-sufficiency rate rises to >50%) | Company announcements/EIA disclosure/completion announcements | Provincial NDRC project filing queries |
| **L3 Supply Chain/Operations** | Overseas production capacity operational (circumventing trade barriers/currency risk) | Company announcements, host country government disclosures | Cross-border project filing + overseas commerce office announcements |
| **L3 Supply Chain/Operations** | Core customer signs long-term supply agreement (>3 year lock-in) | Major contract announcements (SSE/SZSE announcement platforms) | Exchange announcement original text |
| **L4 Financial** | Operating cash flow positive for 2+ consecutive quarters | Quarterly/annual report cash flow statements | Structured financial data extraction |
| **L4 Financial** | FCF/Revenue continuously improving (rising >2% for 2+ consecutive quarters) | Quarterly/annual reports | Cross-period FCF trend calculation |
| **L4 Financial** | Interest coverage ratio recovering for 2+ consecutive quarters (EBITDA/Interest >3x) | Quarterly/annual reports | Financial ratio calculation verification |
| **L4 Financial** | Short-term debt/total liabilities ratio continuously declining (declining >5%/quarter) | Quarterly/annual report balance sheets | Liability structure trend analysis |
| **External Support** | Provincial government/SASAC explicitly states intent to provide funding or resource support | Local government announcements, SASAC meeting minutes | WebSearch official information sources |
| **External Support** | Group/parent company plans capital injection or asset injection | Company announcements, major asset restructuring plans | Exchange announcements |

#### Negative Outlook Trigger Signals

| Pyramid Layer | Negative Outlook Trigger Signal | Data Source | Verification Method |
|---|---|---|---|
| **L1 Policy/Macro** | Accelerated subsidy phase-out (phase-out schedule published and faster than market expectations) | MOF/NDRC subsidy policy documents | Comparison of policy document versions before and after |
| **L1 Policy/Macro** | Industry access tightened/capacity restriction policy introduced | MIIT industry policy announcements | Policy original text + industry association interpretation |
| **L1 Policy/Macro** | Financial regulation tightened (credit concentration control/bond issuance conditions tightened) | CBIRC/PBOC window guidance documents | Open market analysis report cross-verification |
| **L1 Policy/Macro** | Increased macroeconomic downturn pressure leading to industry demand contraction | NBS PMI/industrial value-added data | Macro data confirmed over 2+ consecutive quarters of trend |
| **L2 Technology/Competition** | Core product technology roadmap confirmed obsolete (e.g., PERC replaced by TOPCon) | Industry efficiency data, bidding technical specification changes | PVInfoLink/TrendForce price + efficiency data |
| **L2 Technology/Competition** | Core product added to restricted/prohibited list (e.g., export control entity list) | MOFCOM announcements, BIS Entity List (US) | Official announcements + industry impact assessment |
| **L2 Technology/Competition** | Key technical talent loss (CSO/CTO departure) | Company announcements, Qichacha/Tianyancha business registration changes | Qichacha executive change records + company announcements |
| **L2 Technology/Competition** | Major competitor achieves significant technological breakthrough posing substitution threat | Industry conference papers, patent publications | WebSearch industry technology intelligence |
| **L2 Technology/Competition** | Core license/qualification suspended or revoked (e.g., drug GMP/GSP certificate revocation) | NMPA flight inspection announcements | Government affairs open platform inspection records query |
| **L3 Supply Chain/Operations** | Core supplier halts supply or significantly raises prices (cost increase >15%) | Company announcements, industry price data | SMM/LME/Mysteel commodity price tracking |
| **L3 Supply Chain/Operations** | Major customer loss (top 5 customer list changes or concentration >50%) | Annual report customer information disclosure, exchange inquiry letters | Prospectus/annual report customer concentration data comparison |
| **L3 Supply Chain/Operations** | Key production facility shutdown/safety accident/environmental penalty | MEM announcements, MEE penalty disclosure | Government affairs open administrative penalty queries |
| **L3 Supply Chain/Operations** | Core subsidiary equity frozen/enforcement | Qichacha/Tianyancha judicial freezing data | Qichacha + China Judgments Online cross-verification |
| **L4 Financial** | Operating cash flow persistently negative for 4 consecutive quarters | Quarterly/annual report cash flow statements | Cash flow trend analysis (rolling 12 months) |
| **L4 Financial** | Interest coverage ratio persistently deteriorating (EBITDA/Interest <1.5x for >2 quarters) | Quarterly/annual reports | Financial ratio deterioration trend confirmation |
| **L4 Financial** | Short-term debt ratio accelerating upward (short-term debt/total liabilities >60% and still rising) | Quarterly/annual reports | Liability maturity structure trend analysis |
| **L4 Financial** | Cash and cash equivalents significantly reduced (QoQ decline >30% without reasonable explanation) | Quarterly/annual reports | Cross-period cash changes analysis + audit opinion verification |
| **L4 Financial** | Asset-liability ratio exceeds industry threshold (policy-driven >80%/tech-moat >70%) | Quarterly/annual reports | Industry benchmarking + leverage trend |
| **L4 Financial** | Modified audit opinion issued (emphasis of matter/qualified opinion/disclaimer of opinion) | Audit report | Audit opinion type + emphasis of matter specifics |
| **External Support** | Core assets transferred without compensation (e.g., Huachen Group model) | Company announcements, SASAC state asset transfer disclosures | Exchange announcements |
| **External Support** | Supporting entity (provincial government/group) itself experiencing financial deterioration | Government fiscal reports, group financial statements | Local fiscal data + group statements cross-verification |
| **External Support** | Supporting entity credit rating downgraded | Rating agency announcements | WebSearch rating action announcements |

### 2.3 Outlook Assessment Scoring Logic

It is not possible to precisely calculate "outlook probability" -- but the consistency strength of signal direction can be used to assess outlook confidence.

**Signal Counting Rules**:

```
Positive Signal Count   = +1 for each positive trigger signal detected
Negative Signal Count   = +1 for each negative trigger signal detected
Signal Direction Weight = Pyramid layer weight of the factor (L1 > L2 > L3 > L4): L1=1.5, L2=1.2, L3=1.0, L4=0.8, External Support=1.2 (values defined at v0.0.1, satisfying L1>L2>L3>L4 order)

Net Direction Signal = Σ(Positive Signals × Layer Weight) - Σ(Negative Signals × Layer Weight)

If Net Direction Signal >= +2.0 and Positive Signal Count >= 2 → Positive Outlook
If Net Direction Signal <= -2.0 and Negative Signal Count >= 2 → Negative Outlook
If -1.9 < Net Direction Signal < +1.9 → Stable Outlook
If both Positive and Negative Signal Counts >= 3 and directional signal strength is close → Developing Outlook
```

**Confidence Levels**:

| Confidence | Condition | Meaning |
|---|---|---|
| **High** | 4+ signals in same direction, covering >=3 pyramid layers | Directional assessment is very reliable |
| **Medium-High** | 3 signals in same direction, covering >=2 pyramid layers | Directional assessment is fairly reliable |
| **Medium** | 2 signals in same direction, covering >=1 pyramid layer | Directional assessment has reference value |
| **Low** | Only 1 signal or all signals from the same layer | Directional assessment is only indicative |
| **Very Low** | Only 0-1 identifiable signals | Insufficient data to form directional assessment |

### 2.4 Outlook Output Specification

```yaml
Rating: BB+
Outlook: Negative
Outlook Validity: 2026-07-08 to 2028-07-07
Outlook Trigger Factors:
  - L2 Technology: TOPCon capacity >90%, with BC route posing structural substitution threat (Source: 2026Q2 central enterprise procurement results announcement)
  - L4 Financial: Operating cash flow negative for 4 consecutive quarters, deterioration trend not reversed (Source: 2026Q1 quarterly report cash flow statement)
  - External Support: Local government debt ratio >150%, support capacity marginally weakening (Source: 2025 local government fiscal final accounts report)
Positive Factors (if any):
  - L3 Supply Chain: Overseas capacity already operational, expected to contribute revenue in 2026H2 (Source: Company April 2026 capacity announcement)
Outlook Confidence: Medium-High (3/4 signals in same direction, covering 3 layers)
Negative Scenario: If operating cash flow still not positive in 2026H2 and local support not implemented, probability of 1-2 notch downgrade >60%
Positive Scenario: If overseas capacity contribution exceeds expectations and government introduces industry rescue policies, outlook could be adjusted to Stable (probability <20%)
```

```yaml
Rating: A-
Outlook: Positive
Outlook Validity: 2026-07-08 to 2028-07-07
Outlook Trigger Factors:
  - L1 Policy: Industry added to national strategic emerging industry catalog, special support fund expected in 2026Q4 (Source: State Council industry planning document)
  - L2 Technology: Core product won provincial centralized procurement bid, expected market share to increase from 8% to 15% (Source: Provincial procurement platform winning bid announcement)
  - L4 Financial: FCF/Revenue improved from -2% to +3%, positive for 2 consecutive quarters (Source: 2026Q1 quarterly report)
Outlook Confidence: Medium (3 signals but mainly from L1 and L4, L2 signal pending confirmation)
Negative Scenario: No significant negative factors
Positive Scenario: If L2 market share increase confirmed in 2026Q3, probability of 1 notch upgrade >50%
```

```yaml
Rating: CCC
Outlook: Developing
Outlook Validity: 2026-07-08 to 2028-07-07
Outlook Trigger Factors:
  Negative Direction:
    - L4 Financial: Interest coverage ratio 0.8x, short-term debt ratio 72%, default risk imminent (Source: 2026Q1 quarterly report)
    - L3 Supply Chain: Core supplier has suspended shipments (Source: Supplier announcement/industry reports)
  Positive Direction:
    - External Support: Provincial government has stated it will coordinate bailout funds (Source: Provincial government special meeting minutes, WebSearch confirmed)
    - L2 Technology: Core patent pledged to bank as condition for new loan (Source: CNIPA pledge registration announcement)
Outlook Confidence: Medium (positive and negative signals comparable in strength, outcome depends on whether government bailout materializes)
Bidirectional Trigger Conditions:
  - If provincial bailout funds are in place by 2026Q3 → Outlook could be adjusted to Stable, rating maintained at CCC or upgraded to B-
  - If bailout funds do not materialize → Outlook adjusted to Negative, rating downgraded to D
```

### 2.5 Connection Logic Between Outlook and Existing Rating Mapping

The outlook is not an independent judgment -- it is a **directional extension** based on the existing rating mapping results.

```
        Track A Score + Track B Score → Cross-Collision → Composite Rating → Outlook  ← Based on signal direction assessment
                                                                      ↓
                                                                Watchlist ← Based on event assessment
```

**Connection Rules**:

| Current Rating | Negative Outlook | Stable Outlook | Positive Outlook |
|---|---|---|---|
| AAA | Extremely rare (maintenance rate >95%) | Default state | Does not exist (AAA is the highest) |
| AA / A | Technically feasible | Most common | Less common |
| BBB / BB | Most common | Most common | Less common |
| B | Common | Most common | Less common |
| CCC | Common (usually accompanied by Negative Watch) | Rare | Extremely rare (only when clear support signals exist) |
| D | Does not exist | Does not exist | Does not exist (D is the terminal state) |

**Key Constraints**:
- **AAA rating cannot have a Positive outlook** (already at the highest level)
- **D rating is not assigned an outlook** (terminal state does not need directional assessment)
- **CCC rating paired with Negative Outlook or Negative Watch should be the default**
- **When outlook direction deviates from the current rating, special explanation is required** (e.g., "B+/Positive Outlook" implies potential upgrade in the longer term, but the current rating is constrained by short-term risk factors)

---

## 3. Watchlist Mechanism (Potential Rating Actions Within 90 Days)

### 3.1 Trigger Conditions for Entering the Watchlist

The watchlist targets **recent event-driven** potential rating changes, divided into "Positive Watch" and "Negative Watch." Unlike the outlook -- the watchlist is based on explicit event signals, not trend assessment.

#### Negative Watch Trigger Conditions

| Trigger Type | Specific Condition | Data Source | Information Lag |
|---|---|---|---|
| **Event-Driven** | Major asset restructuring announcement (sale of core subsidiary/principal operating assets) | Exchange announcements | Real-time (within T+1 day) |
| **Event-Driven** | Core subsidiary equity change/transfer without compensation | SASAC announcements, business registration changes | T+1~3 days |
| **Event-Driven** | Actual controller change/subject to compulsory measures | Company announcements, China Judgments Online, Enforcement Information Publicity Network | Real-time |
| **Event-Driven** | Regulatory investigation initiated (CSRC/Exchange investigation) | Company announcements, CSRC announcements | Real-time |
| **Event-Driven** | Core management unreachable/abnormal departure (CEO/CFO) | Company announcements, media reports | Real-time |
| **Event-Driven** | Bondholders' meeting triggered + material adverse resolution passed | Bond announcements | T+1 day |
| **Financial Mutation** | Sudden large loss (single quarter loss exceeding 50% of sum of net profit of past three years) | Quarterly reports/performance forecasts | T+1 day |
| **Financial Mutation** | Modified audit opinion issued (qualified opinion/disclaimer/going concern material uncertainty) | Audit report | Within 48 hours after annual report disclosure |
| **Financial Mutation** | Debt default or extension (any bond/loan principal or interest not paid when due) | Company announcements, China Money Network | Real-time |
| **Financial Mutation** | Rating downgraded significantly by another agency (downgraded >=3 notches) | Rating agency announcements | Real-time |
| **Financial Mutation** | Cross-default clause triggered | Bond announcements, trustee reports | T+1 day |
| **Financial Mutation** | Large asset impairment (single impairment >20% of net assets) | Quarterly/annual report announcements | T+1 day |
| **Policy Shock** | Abrupt industry policy shift (subsidies/access/environmental standards suddenly change) | NDRC/MIIT/MEE announcements | Real-time |
| **Policy Shock** | Added to entity list/sanctions list/anti-dumping investigation | MOFCOM/BIS announcements | Real-time |
| **Policy Shock** | Core license suspended or revoked (financial/pharmaceutical/production permit) | Regulatory agency announcements | Real-time |
| **Policy Shock** | Major environmental/safety administrative penalty resulting in core production line shutdown | MEM/MEE disclosures | T+1 day |
| **Market Signal** | Bond price plunges >10% in a single day | Exchange bond closing price data | Real-time |
| **Market Signal** | Credit spread widens >100bp in a single week | ChinaBond valuation/SHCH data | Daily |
| **Market Signal** | Financing channel suddenly closed (credit line withdrawn/bond issuance rejected/private placement terminated) | Company announcements | Real-time |
| **Market Signal** | Stock price plunges >20% in a single day without reasonable explanation (listed companies) | Exchange market data | Real-time |
| **Market Signal** | Multiple large equity pledges approaching margin call | CSDC equity pledge announcements | Daily |

#### Positive Watch Trigger Conditions

| Trigger Type | Specific Condition | Data Source | Information Lag |
|---|---|---|---|
| **Event-Driven** | Group/parent company announces capital injection plan with clear source | Company announcements, SASAC meeting minutes | Real-time |
| **Event-Driven** | Major favorable cooperation (e.g., central enterprise long-term order/overseas large contract) | Major contract announcements | Real-time |
| **Event-Driven** | Debt restructuring plan approved, extended debt repaid normally | Company announcements, creditors' meeting announcements | T+1 day |
| **Policy Shock** | Government introduces explicit rescue policy or arranges bailout funds | Local government announcements, financial regulatory bureau announcements | Real-time |
| **Market Signal** | Bond price rebounds >20% for 5 consecutive trading days with increased volume | Exchange bond data | Daily |
| **Financial Mutation** | New investor invests at a premium (PE/strategic investor increases capital at price above net asset value) | Company announcements, business registration changes | T+1 day |

### 3.2 Watchlist Management Rules

| Management Item | Rule |
|---|---|
| **Entry Condition** | Any entry condition triggered → automatically enters the corresponding watchlist; the same entity can enter "Negative Watch" or "Positive Watch" (cannot enter both simultaneously) |
| **Observation Period** | Automatic reassessment completed within 90 days from entry date; can be extended once under special circumstances (max 60 days), reason for extension must be recorded before 60 days of entry |
| **Reassessment Timeline** | Negative Watch: preliminary assessment within 30 days, reassessment within 60 days; Positive Watch: reassessment within 60 days |
| **Exit Conditions** | (1) 90-day period expires and the event has clarified, output formal reassessment; (2) The triggering event is proven to be a misreading or has reversed within the period; (3) Default/rating action has actually occurred -- watchlist mission complete |
| **List Publication** | Watchlist entities should form a regularly updated list, annotated with entry date, triggering event, and current status |

### 3.3 Watchlist Output Specification

```yaml
Watchlist Status: Negative Watch
Entry Date: 2026-07-08
Entry Reason: Event-Driven Trigger - Core subsidiary transferred without compensation
Trigger Event Specific Description: On July 7, announced core subsidiary A was transferred without compensation to the provincial state-owned capital operation platform; this subsidiary contributed 68% of the issuer's 2025 revenue and 75% of net profit
Expected Action: Reassessment within 60 days, expected downgrade of 1-2 notches
Key Monitoring Points During Observation Period:
  - Valuation of transferred assets and consideration payment method (whether the company receives equivalent assets)
  - Profitability and cash flow sustainability of remaining assets
  - Government compensation measures (if any, such as tax incentives/other asset injections)
  - Whether the bondholders' meeting for outstanding bonds triggers cross-default clauses
Data Sources:
  - Company major asset restructuring announcement (Exchange announcement 2026-07-07)
  - Provincial SASAC state asset transfer approval disclosure (Provincial SASAC website 2026-07-06)
  - Business registration change information (Qichacha/Tianyancha, updating)
```

```yaml
Watchlist Status: Positive Watch
Entry Date: 2026-06-25
Entry Reason: Event-Driven Trigger - Provincial government arranges bailout funds
Trigger Event Specific Description: On June 24, the Provincial Financial Regulatory Bureau announced a 5 billion yuan special bailout fund to support the enterprise in resolving liquidity risk, with the first tranche of 2 billion already disbursed
Expected Action: Reassessment within 60 days, tentative rating maintained, long-term downside risk reduced
Key Monitoring Points During Observation Period:
  - Actual use direction and disbursement pace of the bailout funds
  - Whether the enterprise has used the bailout window to improve operating cash flow
  - Whether subsequent financing channels have reopened (e.g., new bond issuance/bank renewal approval)
  - Whether there are other hidden debt risks not yet exposed
Data Sources:
  - Provincial Financial Regulatory Bureau bailout fund announcement (2026-06-24)
  - Company bailout fund usage progress announcement (pending)
  - Secondary market price trend of outstanding bonds
```

### 3.4 Outlook vs Watchlist: Boundaries and Collaboration

The two mechanisms are easily confused; boundaries need to be clarified:

| Dimension | Outlook | Watchlist |
|---|---|---|
| **Time Window** | 12-24 months | 90 days |
| **Driving Factors** | Trend signals (policy direction/technology roadmap/financial trends) | Event triggers (announcements/shocks/sudden policy changes) |
| **Signal Type** | Multi-signal accumulation/directional consistency | Single event trigger |
| **Output Frequency** | With rating cycle (quarterly/annually) | Real-time (assess upon event trigger) |
| **Probability Meaning** | >=50% probability of rating change | High likelihood of near-term rating change |
| **Rating Change Magnitude** | 1-2 notches | Usually >1 notch |

**Collaboration Rules**:

```
The outlook and watchlist for the same entity can exist simultaneously:

Scenario 1: Negative Outlook + Negative Watch
  → Credit quality inherently trending poorly + recent triggering event occurred
  → Default action: Initiate reassessment during observation period, expected downgrade

Scenario 2: Stable Outlook + Negative Watch
  → Normal trend + sudden negative event
  → Default action: Quickly assess event impact; if material negative impact confirmed → adjust outlook to Negative and downgrade rating

Scenario 3: Negative Outlook + No Watchlist
  → Trend deteriorating but no specific event yet triggered
  → Default action: Maintain outlook, review quarterly

Scenario 4: Positive Outlook + Negative Watch (Contradictory Scenario)
  → Long-term trend positive but short-term negative event encountered
  → Default action: Prioritize watchlist (short-term events take precedence); maintain Positive outlook if negative impact is controllable
```

---

## 4. Continuous Monitoring Trigger Mechanism

### 4.1 Design Principles

Monitoring is not about passively waiting for user queries -- it is about the engine actively and continuously scanning the watch list and portfolio. The following framework defines **what** to monitor, **when** to monitor, and under what conditions to **trigger reassessment**.

### 4.2 Monitoring Matrix

| Monitoring Item | Frequency | Data Source | Conditions Triggering Reassessment | Priority |
|---|---|---|---|---|
| **Policy Changes** | Real-time (within 24 hours of new policy release) | State Council/NDRC/MIIT/PBOC official websites | Policy impact scope covers the industry of the monitored entity | P0 |
| **Financial Data** | Within 48 hours of quarterly/annual report release | Exchange announcements, China Money Network | Any L4 indicator deteriorates beyond threshold (short-term debt ratio >60%/interest coverage <1.5x/FCF negative for 2 consecutive quarters) | P0 |
| **Credit Events** | Real-time | China Money Network, exchange announcements, rating agency announcements | Rating adjustment/default/extension/bankruptcy filing/enforcement filing/dishonest person subject to enforcement | P0 |
| **Market Signals** | Daily (trading hours) | Exchange bond data, ChinaBond valuation, SHCH | Spread single-day jump >50bp / bond price single-day fluctuation >10% / northbound funds weekly sharp outflow >20% | P1 |
| **Management Changes** | Real-time | Company announcements, Qichacha/Tianyancha business registration changes | CEO/CFO/actual controller change/subject to compulsory measures/unreachable | P0 |
| **Asset Transactions** | Real-time | Exchange major asset restructuring announcements, SASAC announcements | Major M&A (transaction amount >20% of net assets) / sale of core assets / transfer without compensation | P0 |
| **Judicial Enforcement** | Daily | China Enforcement Information Publicity Network, China Judgments Online, Qichacha judicial data | New enforcement records/equity freeze amount >10% of net assets | P0 |
| **Equity Pledge** | Weekly | CSDC pledge data | Major shareholder pledge ratio >80% / margin call triggered / abnormal supplemental pledge frequency | P1 |
| **Audit Opinion** | Within 30 days after annual report disclosure season | Annual audit report | Audit opinion change (standard→modified/modified→more severe modified) | P0 |
| **Industry Competition** | Monthly | PVInfoLink/TrendForce/industry association data | Core product price falls below industry-wide cost line / industry inventory >3 months | P1 |
| **Capital Flows** | Weekly | Exchange capital flow data, mutual fund quarterly reports | Industry allocation ratio declining for 2 consecutive quarters / number of heavy-position funds significantly reduced | P2 |
| **News Sentiment** | Daily | WebSearch media monitoring | Negative reports involving financial fraud/major litigation/major product quality issues | P1 |

### 4.3 Intelligent Priority Ranking for Push Notifications

Not all monitoring signals are pushed to the user. The following three dimensions determine the **urgency** and **presentation format** of each push.

**Dimension Definitions**:

| Dimension | Level | Score |
|---|---|---|
| **Urgency**: Probability of rating change within 90 days | Urgent (>=60% probability) | 3 points |
|  | Fairly urgent (30-60% probability) | 2 points |
|  | Normal (<30% probability) | 1 point |
| **Importance**: Potential impact magnitude on rating | >3 notches | 3 points |
|  | 1-2 notches | 2 points |
|  | <1 notch | 1 point |
| **Novelty**: Whether the user already knows (repeat signals get reduced weight) | First occurrence signal | 3 points |
|  | Repeat but not yet sufficiently confirmed signal | 2 points |
|  | Already pushed multiple times | 1 point |

**Push Priority Calculation**:

```
Push Priority Score = Urgency x Importance x Novelty

27 points (3x3x3) → Highest Priority: Immediate push notification, red alert
18-24 points       → High Priority: Topplacement in daily report
9-16 points        → Medium Priority: Included in weekly monitoring report
3-8 points         → Low Priority: Included in monthly trend summary
1-2 points         → Archive Level: Store in historical records, no active push needed
```

**Push Channel Recommendations**:

| Priority | Push Method | Frequency |
|---|---|---|
| Highest (27 points) | Real-time push alert + email notification | Immediate |
| High (18-24 points) | Daily briefing topplacement | Each business day |
| Medium (9-16 points) | Weekly monitoring report | Weekly |
| Low (3-8 points) | Monthly trend summary | Monthly |
| Archive (1-2 points) | No active push needed | Queryable |

### 4.4 Monitoring Signal Historical Record Management

Each monitoring signal should have a structured historical record established, used for trend assessment and signal density calculation.

```yaml
Monitoring Record ID: MON-2026-07-08-001
Entity: [Company Name]
Monitoring Item: Credit Event - Rating Adjustment
Signal Summary: China Chengxin International downgraded the entity rating from AA+/Negative to AA-/Negative
Source: China Chengxin International announcement 2026-07-08
Priority Score: 27 (Urgency 3 x Importance 3 x Novelty 3)
Push Status: Pushed (2026-07-08 09:30)
User Response: Pending confirmation
Associated Reassessment: Pending trigger
```

**Signal Density Calculation**: Each monitoring record counts toward the signal density numerator of the corresponding pyramid layer.

```
Signal Density for a Layer = Existing Signal Count for that Layer / Target Signal Count for that Layer (preset by industry type)

When Signal Density > Threshold (policy-driven L1 threshold 70%; tech-moat L2 threshold 70%):
  → Trigger comprehensive reassessment recommendation
```

---

## 5. Rating Migration Matrices

### 5.1 China Credit Bond Market Migration Probability Reference

Based on approximate estimates from historical market data. **Important limitations are stated in the data quality notes**.

#### 1-Year Migration Probability Matrix

| Current Rating | Upgrade Probability | Maintain Probability | Downgrade Probability | Default Probability | Notes |
|---|---|---|---|---|---|
| **AAA** | 0% | 95%+ | <5% | <0.5% | AAA is the highest, upgrade probability is 0; default rate is extremely low but not zero (Peking University Founder, Huachen were both AAA) |
| **AA+** | 3-5% | 88-92% | 5-8% | <1% | High maintenance rate, limited upgrade probability |
| **AA** | 5% | 85% | 10% | 1-2% | Significant downgrade risk begins to appear |
| **AA-** | 5-8% | 80-85% | 10-15% | 2-3% | Upside and downside volatility increases |
| **A+** | 5-8% | 78-82% | 12-18% | 3-5% | Downgrade probability begins to exceed upgrade |
| **A / A-** | 5% | 75% | 15-20% | 5% | Credit quality divergence is significant |
| **BBB+** | 5-8% | 70-75% | 18-25% | 5-8% | Approaching speculative-grade boundary |
| **BBB / BBB-** | 3-5% | 65-70% | 20-30% | 8-10% | Speculative-grade characteristics emerge |
| **BB** | 3-5% | 60% | 25-30% | 10-15% | High-risk zone |
| **B** | <3% | 50-55% | 30-35% | 15-20% | Half of entities downgraded or defaulted within 1 year |
| **CCC** | <2% | 30-40% | 30-40% | 30%+ | Over half default within 3 years |
| **D** | 0% | -- | -- | 100% | Terminal state |

### 5.2 Data Quality and Usage Limitations

| Limitation | Specific Explanation |
|---|---|
| **Limited Sample Size** | China's credit bond market history is only about 20 years (officially launched in 2005); material default cases are concentrated after 2018, sample size is far smaller than the US market (over 100 years of data) |
| **Rating Inflation Issue** | External rating median is severely inflated (AAA and AA grades account for over 80% of outstanding credit bonds); current migration probabilities may underestimate actual default risk |
| **Missing Tail Risk** | Lack of defaults across a complete economic cycle -- the Chinese market has not yet experienced a complete "boom → recession → recovery" credit cycle |
| **Non-Randomness** | China's credit bond defaults have significant industry clustering and "state-owned enterprise faith" distortion effects; migration probabilities cannot be simply extrapolated |
| **Structural Changes** | Default characteristics of LGFV/real estate/corporate bonds each differ; a single migration matrix cannot reflect structural differences |

**Honest Statement**:
> The above migration matrices are **directional references** based on limited historical data, not precise probability predictions. The statistical significance of the matrices is insufficient to support quantitative default probability calculations. In engine output, the migration matrices are only used for: (1) rough calibration reference for outlook judgments; (2) marking general rating change probability ranges in continuous monitoring. It is not recommended to use migration probabilities directly for pricing or risk measurement.

### 5.3 Industry-Differentiated Migration Probability Adjustments

Different industries, due to their structural characteristics, should have industry-specific directional migration biases:

| Industry Type (paradigm codes per industry-framework.md §2-§3) | Migration Deviation Relative to Overall Market | Reason |
|---|---|---|
| **P1 Cyclical** | Downgrade probability +5-10% | Cycle turns (commodity prices, freight rates, capacity utilization, consumer spending) can rapidly impair industry-wide credit quality; overcapacity/price-war phases amplify tail risk |
| **P2 Defensive** | Upgrade probability +2% | Inelastic demand and pricing power; gross-margin stability limits downgrade pressure in normal recessions |
| **P3 Growth** | Upgrade probability +3-5% | Core IP/technology roadmap forms a relatively strong moat; once established, advantages compound rapidly |
| **P4 Regulated Utility** | Upgrade probability +2% | Regulated asset base / concession cash flows; relatively high business-model stability |
| **Semiconductor (Special)** | Downgrade probability +10-15% | Geopolitical/export-control risk is the heaviest factor; adjustment magnitude may be larger |
| **Automobiles (EV transition)** | Downgrade probability +5-10% | Intense competition + fast technology iteration + policy-change risk |

**Delegated paradigms (no generic adjustment):**

| Industry Type | Adjustment |
|---|---|
| **P5 Financial** | No generic adjustment — governed by the dedicated framework in financial-bond-framework.md |
| **P6 Sovereign-Linked** | No generic adjustment — governed by the dedicated framework in external-support-framework.md |

---

## 6. Integration with the Existing Framework

This module is not an independent document -- corresponding modifications need to be made in the following five existing documents.

### 6.1 Integration in engine-overview.md

**Needs modification**: Update "Composite Output" and "Rating Mapping Table" in the "Overall Architecture" section.

**Rating Output Specification Changes**:

```
# Current (v0.0.2)
Composite Output
Rating + Signals + Completeness Report

# Revised (v0.0.2)
Composite Output
Rating + Outlook + Watchlist + Continuous Monitoring Checklist + Signal Completeness Report
```

**Rating Mapping Table Extension**:

| Score Range | Rating | Default Outlook | Meaning |
|---|---|---|---|
| 9.5 - 10.0 | AAA | Stable (Positive outlook does not exist) | Extremely Low Risk |
| 9.0 - 9.4 | AA+ | Stable (default) | |
| 8.5 - 8.9 | AA | Stable (default) | Low Risk |
| 8.0 - 8.4 | AA- | Stable (default) | |
| 7.5 - 7.9 | A+ | Stable (default) | Medium-Low Risk |
| 7.0 - 7.4 | A | Stable (default) | |
| 6.5 - 6.9 | A- | Stable (default) | |
| 6.0 - 6.4 | BBB+ | Stable | Medium Risk |
| 5.5 - 5.9 | BBB | Stable | |
| 5.0 - 5.4 | BBB- | Stable | |
| 4.5 - 4.9 | BB+ | Stable or Negative | Medium-High Risk |
| 4.0 - 4.4 | BB | Stable or Negative | |
| 3.5 - 3.9 | BB- | Stable or Negative | |
| 3.0 - 3.4 | B+ | Stable or Negative | High Risk |
| 2.5 - 2.9 | B | Stable or Negative | |
| 2.0 - 2.4 | B- | Stable or Negative | |
| 1.0 - 1.9 | CCC | Negative | Extremely High Risk (default paired with Negative outlook) |
| 0 - 0.9 | D | N/A | Default/Imminent Default |

### 6.2 Integration in dual-track-methodology.md

**Needs modification**: Add "Outlook + Watchlist" output paragraph after the "Rating Mapping" section.

**New paragraph location**: Between "6. Rating Mapping" and "7. Decision Rules," or add "8. Outlook and Watchlist Output" after "7. Decision Rules."

**Content to add**:

```
## 8. Outlook and Watchlist Output

After rating mapping is completed, output the outlook and watchlist using the following logic:

### 8.1 Outlook Output Logic

1. Extract all identifiable positive and negative signal factors from Track A and Track B
2. Calculate Net Direction Signal per the scoring logic in Section 2.3
3. Map to one of Positive/Stable/Negative/Developing
4. Cross-validate with rating consistency and historical outlook continuity

### 8.2 Watchlist Output Logic

1. Scan all six major trigger types (Event-Driven/Financial Mutation/Policy Shock/Market Signal/Management Changes/Asset Transactions)
2. Any condition triggered → automatically enters the corresponding watchlist
3. If outlook direction signal conditions are also met → combine with outlook to form a dual-track assessment
```

### 6.3 Integration in multi-stakeholder.md

**Needs modification**: Add "Outlook Change Response Strategies" for each implemented identity (M0, M1).

**M0 Credit Approval (Bank) Outlook Response Strategies**:

```
M0 Credit Approval Outlook Response Strategies:
  - Stable Outlook → Maintain existing credit terms (normal renewal/extension)
  - Negative Outlook → Reduce exposure: suspend new credit, reduce renewal amounts for existing maturities, add collateral/guarantors
  - Positive Outlook → Can moderately increase exposure (but core variable is industry policy stability; should not overly rely on outlook upgrades)
  - Negative Watch → Immediately freeze new credit, initiate special post-lending review (complete within 30 days)
  - Positive Watch → Can moderately accelerate approval pace, but continue to review per normal risk control standards
```

**M1 Bond Investment Outlook Response Strategies**:

```
M1 Bond Investment Outlook Response Strategies:
  - Stable Outlook → Can maintain positions, assess buy/sell timing at normal frequency
  - Negative Outlook → Gradually reduce positions (6-12 month window), shorten duration, stop new purchases
  - Positive Outlook → Can add positions appropriately, extend duration (but need to confirm terms and liquidity meet requirements)
  - Negative Watch → Immediately assess exit timeline, recommend deciding to reduce/watch/hold within 30 days
  - Positive Watch → Do not chase if spread already reflects positive expectations; opportunity if market has not yet fully priced in
```

**Other Identity Response Strategies (placeholders)**:

```
M2 Bond Underwriting: Negative outlook/watch industry entity → issuance window closed, recommend issuer wait for policy clarity
M3 Market Trading: Negative Watch → do not make markets, do not bet on directional long/short
M4 Portfolio Risk Control: Negative Outlook → add concentration and spread warning lines for this entity to the portfolio monitoring dashboard
M5 Corporate Financing: Negative Outlook → initiate proactive investor communication, accelerate activation of backup financing channels (e.g., bank credit lines)
```

### 6.4 Integration in validation-methodology.md

**Needs modification**: Add verification of **outlook directional correctness** to the validation process.

**New Validation Dimension**: Add the following dimension to forward-looking comparison validation:

```
### 4.5 Outlook Directional Correctness Validation (New)

In retrospective and forward-looking validation, not only verify "whether ratings can foresee default risk," but also verify "whether the outlook direction is correct."

Validation Criteria:
  - If T0 gives "Negative Outlook," and within T-12 to T-24 the rating is actually downgraded → Outlook direction correct
  - If T0 gives "Positive Outlook," and within T-12 to T-24 the rating is actually upgraded → Outlook direction correct
  - If T0 gives "Stable Outlook," and within T-12 to T-24 the rating change is <=1 notch → Outlook direction correct
  - If the outlook direction is opposite to the actual rating change direction → Outlook direction incorrect (requires attribution analysis)

Outlook Correctness Metrics:
  Outlook Accuracy = Number of directionally correct outlooks / Total number of outlooks
  Outlook Bias Analysis: Attribution of incorrect outlooks (insufficient data? signal misreading? unforeseeable events?)
```

### 6.5 Integration in mosaic-engine.md

**Needs modification**: Add outlook and watchlist output fields in the "Composite Output" section.

```
Composite Output Field Expansion:
  rating: {current rating}
  outlook: {Positive/Stable/Negative/Developing}              # New
  outlook_trigger_factors: [{signal list}]                     # New
  outlook_confidence: {High/Medium-High/Medium/Low/Very Low}   # New
  watchlist: {Positive Watch/Negative Watch/None}              # New
  watchlist_entry_date: {date}                                 # New
  watchlist_trigger_event: {trigger event description}         # New
  watchlist_next_action: {expected subsequent action}          # New
  monitoring_items: [{monitoring item list}]                   # New
  rating: {current rating}
  signals: [{signal list}]
  completeness_report: {completeness report}
```

---

## 7. Outlook Reliability Under Public Data Constraints

### 7.1 Inherent Limitations of This Framework's Outlook

| Limitation | Reason | Constraints on Usage |
|---|---|---|
| **Outlook is a directional assessment, not a precise prediction** | Signal scoring logic is based on the quantity and consistency of available public data, not a quantitative default probability model | The outlook cannot be equated with "probability of rating change"; it can only serve as a directional reference |
| **Limited statistical foundation** | China's credit bond market lacks default samples across a complete cycle (see Section 5.2) | Migration matrices serve only as rough calibrations, not as inputs for VaR/PD |
| **Timeliness depends on data updates** | Policy documents/financial reports/market data inherently have publication lags | Continuous monitoring can at most shorten the information lag window, not eliminate it |
| **Insufficient information content in public data** | Non-listed companies lack market pricing and real-time financial data; non-standard asset penetration data is unavailable | Outlook confidence for non-listed entities is naturally lower than for listed entities |
| **Force majeure is outside the prediction scope** | Sudden policy shifts, financial crises, wars, pandemics, and other systemic external shocks | The outlook does not cover the trigger probability of these events |
| **Group risk penetration is difficult** | Consolidated financial statements obscure the parent company's standalone risk; core assets may reside at the subsidiary level | For group holding entity outlooks, "group penetration level" must be specially noted |

### 7.2 Outlook Confidence Under Different Data Availability

| Entity Type | Data Availability | Outlook Confidence | Remarks |
|---|---|---|---|
| **Listed company (with outstanding bonds)** | High (financial statements + audit + market pricing + rating + announcements) | Medium-High | Optimal conditions |
| **Listed company (no outstanding bonds)** | Medium-High (market pricing available but no bond spreads) | Medium | Missing credit spread signal |
| **Non-listed company (with bond issuance/disclosure requirements)** | Medium (annual reports + bond announcements but no market pricing) | Medium | Lacking market signals, relies on fundamentals |
| **Non-listed company (no bond issuance/disclosure obligations)** | Low (only fragmented information such as judicial/bidding/recruitment) | Low | Outlook only serves as directional indication |
| **Single project entity (SPV)** | Medium (project financial statements + interest payment records but complex structure) | Medium | Asset-side data is better than entity-side data |

### 7.3 Standard Disclaimer for Outlook Statements

All engine outputs containing an outlook must include the following disclaimer (or equivalent phrasing):

> **Outlook Disclaimer**: The outlook (Positive/Stable/Negative/Developing) provided by this framework for [Company Name] is a **directional assessment** based on publicly available data. It does not represent a quantitative probability of rating change and does not constitute a precise prediction of future credit events. The outlook is valid for 12-24 months and should be reassessed upon expiry or upon the occurrence of a material triggering event. Sudden policy shifts, financial crises, force majeure, and other systemic external shocks are outside the prediction scope of this outlook. This framework assumes no liability for any investment decisions or financial losses arising from reliance on this outlook.

---

## 8. Appendices

### Appendix A: Outlook and Watchlist Output Templates (Directly Embeddable in Reports)

#### Full Output Template

```yaml
# ============================================================
# Comprehensive Credit Assessment Output (with Outlook and Monitoring)
# Generation Date: 2026-07-08
# Entity: [Company Name]
# Industry: [Industry Name]
# ============================================================

# --- Part 1: Current Rating ---
Rating: [AAA, AA+, AA, AA-, A+, A, A-, BBB+, BBB, BBB-, BB+, BB, BB-, B+, B, B-, CCC, D]
Rating Confidence: [High/Medium-High/Medium/Low/Very Low]
Rating Data Completeness: [X%]

# --- Part 2: Outlook ---
Outlook: [Positive/Stable/Negative/Developing]
Outlook Validity: [Date] to [Date+24 months]
Outlook Trigger Factors:
  Positive Signals:
    - [Layer]: [Specific signal] (Source: [Data source] [Date])
    - [Layer]: [Specific signal] (Source: [Data source] [Date])
  Negative Signals:
    - [Layer]: [Specific signal] (Source: [Data source] [Date])
    - [Layer]: [Specific signal] (Source: [Data source] [Date])
Outlook Confidence: [High/Medium-High/Medium/Low/Very Low]
  Notes: [X signals in same direction, covering X pyramid layers]
Negative Scenario: [Describe scenario that could lead to downgrade]
Positive Scenario: [Describe scenario that could lead to upgrade]

# --- Part 3: Watchlist ---
Watchlist Status: [Positive Watch/Negative Watch/None]
[If "None," omit the following fields]
Entry Date: [Date]
Entry Reason: [Trigger type]
Trigger Event: [Event specific description]
Expected Action: [Reassessment within X days, expected adjustment of X notches]
Key Monitoring Points During Observation Period:
  - [Key monitoring item 1]
  - [Key monitoring item 2]
  - [Key monitoring item 3]
Data Sources:
  - [Source 1: link/description]
  - [Source 2: link/description]

# --- Part 4: Continuous Monitoring Checklist ---
Monitoring Item List:
  - [Monitoring item]: [Current status] — Last checked: [date]
  - [Monitoring item]: [Current status] — Last checked: [date]
  - [Monitoring item]: [Current status] — Last checked: [date]
Upcoming Events to Watch:
  - [Date]: [Event]
  - [Date]: [Event]

# --- Part 5: Disclaimer ---
Disclaimer: >-
  This outlook is a directional assessment based on publicly available data
  and does not represent a quantitative probability of rating change.
  Valid for 12-24 months; should be reassessed upon expiry.
  Force majeure is outside the prediction scope.
```

#### Concise Output Template (Suitable for Embedding in Report Body)

| Item | Content |
|---|---|
| **Rating** | BB+ |
| **Outlook** | Negative (Confidence: Medium-High) |
| **Trigger Factors** | L2 Technology roadmap obsolescence risk / L4 Cash flow deterioration / External support weakening |
| **Watchlist** | Negative Watch (Entry date: 2026-07-08, expected reassessment within 60 days) |
| **Trigger Event** | Core subsidiary transferred without compensation |
| **Monitoring Focus** | Asset valuation consideration / Remaining profit sustainability / Government compensation measures |

### Appendix B: Outlook and Watchlist Role Responsibility Matrix

| Role | Responsibility |
|---|---|
| **Analyst** | Quarterly assessment and output of outlook; assess watchlist upon event trigger; write outlook adjustment rationale |
| **Engine (Automation)** | Continuously scan signals in the monitoring matrix; push alerts when signals reach threshold; maintain monitoring history records |
| **Risk Control Director** | Review outlook adjustments; approve watchlist entry and exit; give special attention to Negative Outlook + Negative Watch entities |
| **Portfolio Manager** | Adjust positions based on outlook changes; complete reduction/hedging decisions during the Negative Watch period |

### Appendix C: Document List Related to This Module

| Document | Relationship | Action |
|---|---|---|
| engine-overview.md | Architecture overview, needs update to rating output specification | Check modifications in Section 6.1 |
| dual-track-methodology.md | Add outlook output after dual-track rating mapping | Check modifications in Section 6.2 |
| multi-stakeholder.md | Add outlook response strategies to each identity decision matrix | Check modifications in Section 6.3 |
| validation-methodology.md | Add outlook direction validation to validation process | Check modifications in Section 6.4 |
| mosaic-engine.md | Output field expansion | Check modifications in Section 6.5 |
| qualitative-analysis.md | Signal source support in qualitative analysis methodology | Trigger factors in this module reference the information source grading in this document |
| industry-framework.md | Industry pyramid weights determine outlook signal layer weights | Trigger factor matrix weight references |

### Appendix D: Version History and Change Log

| Version | Date | Changes |
|---|---|---|
| 0.1.0 | 2026-07-08 | Initial release: Outlook mechanism + trigger factor matrix + output specification; Watchlist mechanism + trigger conditions + output specification; Continuous monitoring matrix + push ranking; Rating migration matrix + data quality statement; Integration plan with 5 existing documents |
