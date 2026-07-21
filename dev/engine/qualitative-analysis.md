# Qualitative Analysis Methodology — Fixed Income Credit Analysis Engine

**Version**: v0.0.4 | **Date**: 2026-07-10
**Role**: Qualitative judgment methodology for Track A (Fundamental Analysis) · Normative guidance for "direction judgment" in the dual-track framework

---

## 1. Positioning of Qualitative Analysis

### 1.1 Role in the Dual-Track Framework

Core division of the dual-track analysis framework: **Qualitative analysis judges direction, quantitative analysis calibrates precision**. Qualitative analysis answers "is credit quality improving or deteriorating," while quantitative analysis answers "how much has it changed and how is the market pricing it."

```
Role Matrix in the Dual-Track Framework:

                        Qualitative Analysis (This Document)       Quantitative Analysis (quantitative-analysis.md)
                        ────────────────────────────────           ──────────────────────────────────
Track A (Fundamental)  ✅ Core domain                              Auxiliary validation
                        Industry trend judgment                     Financial ratio threshold checks
                        Policy direction interpretation             Historical financial data statistics
                        Competitive position assessment             Industry average benchmarking
                        Governance and strategy assessment

Track B (Market Pricing) Auxiliary validation                       ✅ Core domain
                        Market sentiment qualitative judgment       Spread calculation and anomaly detection
                        Narrative vs. pricing separation            Volatility factor decomposition
                        Event-driven force assessment               Correlation analysis
```

| What It Does | What It Does NOT Do |
|-------------|---------------------|
| Judge industry trend direction (upward/stable/downward) | Replace quantitative financial indicators |
| Identify key variables in policy signals | Replace cash flow modeling |
| Assess management capability and governance quality | Provide precise default probability |
| Identify market narratives and collective blind spots | Replace external ratings (ratings themselves are one input) |
| Evaluate the soundness of corporate strategy | Predict precise default timing |
| Integrate fragmented information into a complete picture | Replace the layered pyramid scoring (scoring is a result of qualitative + quantitative) |

### 1.2 Qualitative vs. Quantitative: Four-Level Division of Responsibilities

| Level | Qualitative Responsibility | Quantitative Responsibility | Who Has Final Say |
|-------|---------------------------|----------------------------|-------------------|
| **Trend Judgment** | Direction (upward/stable/downward) | Magnitude (+x% / -x%) | Qualitative — direction is meaningless without correct orientation |
| **Anomaly Identification** | "Why is it anomalous" | "Is it anomalous" | Quantitative — detect first, then explain |
| **Attribution Analysis** | "Who is driving it" | "How much is each driving" | Collaboration — qualitative identifies factors, quantitative measures contribution |
| **Prediction Judgment** | "What scenarios might occur" | "Probability and loss for each scenario" | Qualitative — scenario construction is a matter of judgment |

**Core Principle: Qualitative analysis defines the boundaries of possibility; quantitative analysis makes precise measurements within those boundaries. When the two conflict, resolve the qualitative issue first — if the direction is wrong, precision is meaningless.**

### 1.3 Differences in Qualitative Analysis Roles Across Six Stakeholder Perspectives

The six stakeholder roles have different weights for qualitative analysis needs. The following shows the weight and focus of qualitative analysis for each perspective (role definitions: multi-stakeholder.md §1):

| Role | Qualitative Analysis Weight | Core Focus of Qualitative Analysis |
|------|---------------------------|------------------------------------|
| **Credit Selector** | **High (60-70%)** | Industry risk, policy stability, management integrity, reliability of secondary repayment source |
| **Portfolio Manager** | **Medium (40-50%)** | Industry trend direction, substance of covenant protection, event-driven judgment |
| **Advisor** | **High (50-60%)** | Qualitative judgment of investor demand, issuance window selection, comparable case studies |
| **Trader** | **Low (20-30%)** | Qualitative assessment of market sentiment, extreme event scenario judgment |
| **Risk Officer** | **Medium (40-50%)** | Tail risk scenario construction, qualitative explanation of correlation mutations |
| **Individual Investor** | **High (60-70%)** | Capital market window judgment, investor preference shifts, rating agency focus areas |

**Credit Selector and Individual Investor have the highest dependence on qualitative analysis — because these two roles face the greatest information asymmetry and long-term uncertainty. Trader has the lowest dependence — quantitative signals dominate in short-term trading.**

### 1.4 Types of Qualitative Analysis Methodologies

This engine uses four types of qualitative analysis methods, listed by frequency of use:

| Method Type | Definition | Applicable Scenarios | Section in This Document |
|------------|-----------|---------------------|-------------------------|
| **Information Classification and Verification** | Assess the reliability of information sources, cross-validate signals | Foundation for all qualitative judgments | Chapter 2 |
| **Policy Text Interpretation** | Structurally parse policy documents, predict industry impact | Policy-driven industries (solar PV, semiconductor) | Chapter 3 |
| **Industry Structured Analysis** | Organize fragmented information within industry cognitive frameworks | Baseline analysis for all industries | Chapter 4 |
| **Mosaic Assembly** | Aggregate multi-source fragments into a complete credit profile | Reasoning when information is insufficient | Chapter 5 |

---

## 2. Information Source Classification and Credibility Assessment

### 2.1 Six-Level Credibility System

All information sources entering the analysis process must be labeled with credibility according to the following six-level system. This is the first step in qualitative analysis — **signals not labeled with credibility level do not enter the mosaic assembly process**.

| Level | Name | Characteristics | Timeliness | Credibility | Applicable Scenarios |
|-------|------|----------------|------------|-------------|---------------------|
| **L6** | Official Government Announcements | Official releases from the State Council, National Development and Reform Commission, Ministry of Industry and Information Technology, Central Bank, Ministry of Finance, etc.; official document format; traceable to original text | Published immediately, but transmission to enterprises takes 1-12 months | ★★★★★ Extremely High | Industry policy direction, regulatory rule changes, industrial support intensity |
| **L5** | Industry Associations / Authoritative Third Parties | CPIA, China Association of Automobile Manufacturers, China Nonferrous Metals Industry Association; PVInfoLink/TrendForce/SMM and other professional institutions; CCDC/Clear registered data | Weekly-Monthly | ★★★★☆ High | Industry statistics, price trends, installed capacity/shipment volumes |
| **L4** | Brokerage/Research Institution Reports | Reports from CITIC Securities, CICC, Huatai and other leading brokerage research institutes; industry deep-dive reports, research visit memos | Monthly-Quarterly | ★★★☆☆ Medium-High | Industry deep analysis, corporate research information, competitive landscape assessment |
| **L3** | Mainstream Media / Financial News | Caixin, Securities Times, 21st Century Business Herald, China Business News, Economic Observer and other licensed financial media; exchange announcement reprints | Instant-Daily | ★★★☆☆ Medium | Corporate activity tracking, industry news, policy interpretation |
| **L2** | Voluntary Corporate Disclosure | Listed company announcements, earnings call transcripts, official corporate website news, roadshow materials, ESG reports | By disclosure rules (quarterly/semi-annual/annual) | ★★☆☆☆ Medium-Low | Corporate strategy, operating data, management judgment |
| **L1** | Anonymous Sources / Rumors / Social Media | Posts on online investment forums, unverified articles from WeChat public accounts, WeChat group screenshots, disclosures from unnamed individuals | Instant (but unverifiable) | ★☆☆☆☆ Low | ⚠️ Leads only, **must not be used as standalone basis for judgment** |

**Processing Rules:**

```
L6-L4 signals → Can directly enter the mosaic assembly layer (after timeliness check)
L3-L2 signals → Must have source level labeled, require ≥2 independent verifications to be upgraded to valid signals
L1 signals   → Used only to generate "areas requiring attention," not as scoring basis
               Labeling format: "Rumor: [content] — Source unverifiable, requires further investigation"
```

### 2.2 Detailed Characteristics and Pitfalls of Each Source Level

| Source Level | Typical Pitfalls | Mitigation Methods |
|-------------|-----------------|-------------------|
| **L6 Government Announcements** | Discrepancy between policy intent and actual effect ("policy temperature gap"); disconnect between ministerial documents and local implementation | Must trace to local implementation level; monitor whether provincial supporting documents follow ministerial documents |
| **L5 Industry Associations / Third Parties** | Sample bias (CPIA only covers major enterprises, SME data missing); statistical methodology changes | Check consistency of statistical methodology; monitor changes in "sample enterprise" scope |
| **L4 Brokerage Research Reports** | Conflicts of interest (investment banking relationships, proprietary holdings); optimism bias; herd consensus | Check research report rating distribution (if a brokerage gives "Buy" to all companies in an industry → be cautious); compare conclusions across multiple brokerages |
| **L3 Mainstream Media** | Information amplification from chasing hot topics; information distortion during reproduction ("telephone game losses") | Trace back to original/source announcement; be wary of phrasing like "according to informed sources" |
| **L2 Voluntary Corporate Disclosure** | Selective disclosure (good news released promptly, bad news delayed); euphemistic language ("industry-wide challenges" = losses) | Compare disclosure wording changes across periods; monitor items "that should have been but were not disclosed" |
| **L1 Anonymous Sources** | Motivation to short or pump; misleading due to incomplete information | Use only for "needs attention" list, not for scoring; can be upgraded only if cross-validated by L4+ sources |

### 2.3 Cross-Validation Rules

A single signal cannot serve as the basis for judgment. All key determinations require cross-validation.

| Validation Type | Rule | Example |
|----------------|------|---------|
| **Same-Level Cross** | 2 independent L4+ sources point to the same fact | Two research reports from CITIC Securities and CICC both mention "Company X's module shipments declined 15% QoQ in Q2" |
| **Cross-Level Cross** | L6+L4 or L5+L3 point in the same direction | NDRC policy document (L6) + brokerage interpretation (L4) = policy direction confirmed |
| **Top-Down Joint** | L6 official announcement + L5 industry data validating impact | Solar PV subsidy phase-down policy announced + CPIA data showing installed capacity growth slowing |
| **Counter-Direction Validation** | Actively search for counter-direction evidence — "under what conditions would this judgment be wrong" | When judging "industry downturn," check for unexpected positive policy signals |

**Cross-Validation Status Labels:**

| Status | Meaning | Representation in Reports |
|--------|---------|--------------------------|
| ✅ Verified | ≥2 independent sources (cross-level allowed) confirm the same fact | Signal confidence upgraded |
| ⏳ Partially Verified | 1 source + 1 directionally consistent weak signal | Label "partially verified" |
| ⚠️ Pending Verification | Only 1 source, no independent cross-validation | Label "pending verification," this signal not included in scoring |
| 🔴 Contradiction | Multiple sources point to different directions | Enter contradictory signal processing workflow |

### 2.4 Contradictory Signal Processing Rules

When signals from different sources point in opposite directions, process according to the following priority:

```
Step 1: Check source level differences
  ├── L6/L5 vs L2 → Favor L6/L5 (unless there is specific reason to doubt official data)
  ├── L4 vs L4   → Check for conflicts of interest; if none, treat as "difference of opinion"
  └── L3 vs L6   → Favor L6, label "media interpretation differs from official document"

Step 2: Check timestamp differences
  ├── Newer signal vs Older signal → Favor newer signal (label timeliness difference)
  └── But: if older signal is official announcement, newer signal is rumor → Favor older signal

Step 3: Escalate verification
  ├── Contradiction unresolvable → Label as "significant divergence exists on this dimension"
  ├── Affecting rating precision → Widen scoring range (±1 → ±2)
  └── If divergence involves a veto condition → Escalate to highest priority

Step 4: Output specification
  Output format:
  [Dimension Name] — Signal Contradiction
  ├── Signal A: [content] — Source: [Level] — Timestamp
  ├── Signal B: [content] — Source: [Level] — Timestamp
  ├── Contradiction Cause Analysis: [analysis]
  ├── Preferred Choice: [selection logic]
  └── Residual Uncertainty: [range]
```

**Contradictory Signal Processing Example: 2026 Solar PV Installation Forecast**

| Signal Source | Level | Forecast Content | Timestamp |
|--------------|-------|-----------------|-----------|
| CPIA | L5 | China's new solar PV installations in 2026: 220-260GW | 2026-03 |
| Leading Brokerage Firm | L4 | 2026 installations estimated at only 180-200GW (due to grid connection bottlenecks) | 2026-05 |

**Processing Procedure:**
1. Source level: L5 vs L4 → L5 has higher priority (association data based on member company statistics)
2. Timestamp: Brokerage report is newer (+2 months), but contains new information (grid connection bottlenecks)
3. Conclusion: Use CPIA data as the baseline range (220-260GW), but note "grid connection bottlenecks mentioned in brokerage report may push actual results to lower end" → Use 220-260GW range with downside risk annotation

### 2.5 Source Credibility Decay Curves

Different levels of sources have different rates of credibility decay over time:

| Source Level | Half-Life (Time for credibility to drop to 50%) | Processing Rules |
|-------------|-------------------------------------------------|-----------------|
| **L6 Government Announcements** | 6-12 months (major policies may last 1-2 years, implementation details need updates) | Valid for 1 year; beyond 1 year, check for updated documents |
| **L5 Industry Association Data** | 3-6 months (industry data valid quarterly) | Quarterly data valid for current quarter; cross-quarter data must be labeled "previous quarter" |
| **L4 Brokerage Research Reports** | 1-3 months (research judgments on markets and policies decay quickly) | Monthly updates; beyond 3 months, no longer valid as effective signal |
| **L3 Mainstream Media** | 2-4 weeks (direct information from news events decays quickly) | Short valid window for news event information, but "factual" parts (e.g., data citations) can be retained |
| **L2 Corporate Disclosure** | By disclosure cycle (quarterly/semi-annual/annual) | Valid until next disclosure; mark as "pending update" beyond disclosure cycle |
| **L1 Anonymous Sources** | Real-time to 1 week | Beyond 1 week, mark as "expired, unverifiable" |

---

## 3. Policy Interpretation Methodology

### 3.1 Structured Policy Text Analysis Framework

Industrial policy is **the most important yet most easily misinterpreted information source** in credit analysis. This engine uses a five-dimensional analysis framework to structurally deconstruct each policy document.

```
Five-Dimensional Policy Document Analysis:
┌──────────────────────────────────────────────────────────┐
│  D1 Issuing Authority — Who issued it?                   │
│    ├── CPC Central Committee / State Council → Highest level, national strategy     │
│    ├── Ministries (NDRC/MIIT/National Energy Administration, etc.) → Departmental regulations  │
│    ├── Provincial governments → Local implementation level                           │
│    └── Industry associations → Self-regulatory norms, no legal force                │
│                                                          │
│  D2 Document Type — What form?                           │
│    ├── Opinion/Notice/Measure/Regulation/Law (binding force ascending)               │
│    └── Draft for Comments/Trial/Formal Implementation (implementation stage)        │
│                                                          │
│  D3 Binding Force Level — Mandatory or voluntary?        │
│    ├── Mandatory ("must," "shall not," "prohibited")                                │
│    ├── Conditional ("those meeting conditions may enjoy," "those meeting standards may apply") │
│    └── Guiding ("encourage," "support," "guide")                                    │
│                                                          │
│  D4 Industry Impact Pathway — Which link does it directly affect?                   │
│    ├── Demand side (subsidies/procurement/access restrictions)                      │
│    ├── Supply side (capacity approval/technical standards/environmental production caps)│
│    └── Cost side (tax/financing/land/energy costs)                                  │
│                                                          │
│  D5 Enforcement Signal — Will it be seriously enforced?  │
│    ├── Strong: Quantified targets set ("achieve XX by 2025")                        │
│    ├── Medium: Supervision mechanisms exist ("regular inspections," "assessment accountability") │
│    └── Weak: No quantified targets, no supervision mechanisms                       │
└──────────────────────────────────────────────────────────┘
```

**AI Agent Analysis Rules:**

```
Input: Policy text URL or text content
Output: Structured policy signal object

Analysis Process:
1. Identify issuing authority → Label administrative level (CPC Central Committee > State Council > Ministries > Provincial > Associations)
2. Identify document type → Label binding force level (Law > Regulation > Measures > Notice > Opinion > Trial)
3. Extract binding force keywords → Count frequency of "must/shall not/prohibited" (mandatory) vs "encourage/support" (guiding)
4. Determine impact pathway → Demand side/Supply side/Cost side (may be multiple pathways)
5. Assess enforcement strength → Presence of quantified targets + presence of supervision mechanism + clarity of timeline
6. Output comprehensive assessment:
   ├── Policy Strength Score (1-5): D1 weight 40% + D3 weight 30% + D5 weight 30%
   ├── Direction: Positive/Negative/Neutral
   └── Impact Time Window: Immediate/Short-term (1-3 months)/Medium-term (3-12 months)/Long-term (12+ months)
```

### 3.2 Policy Transmission Chain: From National Intent to Actual Enterprise Impact

Policy never directly affects enterprises — it operates through a multi-layer transmission chain. Understanding the energy loss at each link (the "policy temperature gap") is central to qualitative analysis.

```
National Level (CPC Central Committee / State Council)
    │
    │   Policy direction established ("vigorously develop XX," "strictly control XX")
    │   Energy loss: Abstract statements, no specific implementation pathway
    ▼
Ministerial Level (NDRC/MIIT/Ministry of Finance/National Energy Administration, etc.)
    │
    │   Implementation details formulated (subsidy amounts/access conditions/technical standards/timelines)
    │   Energy loss: Coordination difficulty among ministries (documents from multiple departments may contradict)
    ▼
Provincial/Local Level (Provincial government/Local NDRC/Park Management Committee)
    │
    │   Local supporting policies (subsidy support/land/tax incentives/environmental impact assessment approval)
    │   Energy loss: Differences in local fiscal capacity + local protectionism
    ▼
Enterprise Level
    │
    │   Actual policy effects (capacity expansion/contraction/technology switching/cost changes)
    │   Energy loss: Enterprise's own execution capability + strategic choices
    ▼
Credit Impact (Profit/Cash Flow/Leverage Ratio/Financing Ability)
```

**Energy Loss Assessment at Each Transmission Chain Link:**

| Transmission Link | Typical Energy Loss | Assessment Points |
|------------------|-------------------|-------------------|
| Central → Ministries | Clear direction but no implementation details | Monitor whether ministries issue supporting implementation rules within 1-3 months; if no rules after 6 months → policy may be shelved |
| Inter-Ministerial Coordination | Conflicting goals across departments (e.g., environmental protection vs. growth) | Check whether the lead ministry has cross-departmental coordination authority; joint issuance has higher enforcement effectiveness than single-department issuance |
| Ministries → Local | Implementation deviation due to differences in local fiscal capacity | Developed provinces have high implementation intensity; less developed provinces may compromise; distinguish "eastern coastal" vs. "central/western" implementation differences |
| Local → Enterprises | Selective enterprise implementation | Leading enterprises actively comply (receive subsidies, obtain resources); SMEs may wait-and-see or fail to meet standards |

### 3.3 "Signal" vs. "Noise" Distinction Criteria

Not all policy documents deserve attention. The following criteria distinguish information requiring in-depth analysis from information that can be ignored:

| Category | Characteristics | Processing Method |
|----------|---------------|------------------|
| **Strong Signal** | Simultaneously satisfies: Issuing authority L6 + Contains quantified targets + Mandatory language + Has supervision mechanism | Immediately incorporate into analysis framework, reassess relevant industries/enterprises |
| **Weak Signal** | Satisfies partial conditions (e.g., L6 issuing authority but no quantified targets, or only guiding language) | Mark as "needs attention," include in routine monitoring, does not trigger immediate reassessment |
| **Noise** | Industry association recommendations, individual expert opinions, media interpretations, draft for comments (not yet formal) | Do not enter analysis framework, label "for reference only" |

**Determination Rules:**

```
Strength Score = D1(Issuing Authority) × 0.3 + D3(Binding Force) × 0.3 + D5(Enforcement) × 0.4

Score > 4.0 → Strong Signal → Triggers reassessment
Score 2.0-4.0 → Weak Signal → Include in observation list
Score < 2.0 → Noise → Do not enter analysis framework

Example:
  State Council issues "Several Opinions on Promoting the Healthy Development of the Solar PV Industry"
  D1=5 (State Council) + D3=4 (contains "must," "shall not") + D5=5 (contains quantified targets + supervision mechanism)
  Score = 5×0.3 + 4×0.3 + 5×0.4 = 1.5 + 1.2 + 2.0 = 4.7 → Strong Signal

Example:
  An industry association expert publishes "Suggestions on Raising Solar PV Power Station Construction Standards"
  D1=2 (Association) + D3=2 (Advisory) + D5=1 (No quantified targets)
  Score = 2×0.3 + 2×0.3 + 1×0.4 = 0.6 + 0.6 + 0.4 = 1.6 → Noise
```

### 3.4 Special Treatment for SOEs/LGFVs: Support Capability vs. Support Willingness Analysis Framework

When the analysis target is a state-owned enterprise (SOE) or local government financing vehicle (LGFV), the standard policy interpretation process requires an additional analysis step — **assessment of the policy's impact on "external support."** This step directly relates to the core credit question of "whether the government will provide rescue."

**Why this step is necessary**: Policies not only affect the issuer's fundamentals (profit/cash flow/leverage ratio) but also directly influence the government's capability and willingness to support the issuer. In some cases, the impact of policy environment changes on "external support" may be greater than the impact on the enterprise's fundamentals.

#### 3.4.1 Dual Pathways of Policy → External Support

```
Policy Changes
    |
    ├── Pathway A: Direct Impact on Support Capability
    |      ├── Fiscal and tax policies (central-local revenue sharing ratios, transfer payment structures)
    |      ├── Debt control (implicit debt resolution requirements, new debt limits)
    |      └── Land policies (changes in land transfer revenue) → Directly affects local fiscal revenue
    |
    └── Pathway B: Indirect Impact on Support Willingness
           ├── SOE reform policies (pace of competitive neutrality advancement)
           ├── Industry reform policies (university-affiliated enterprise reform/healthcare reform — directly changes support logic)
           └── Local government assessment orientation (debt accountability intensity → changes in incentives for rescue vs. non-rescue)
```

**Determination Rules**: For each policy change affecting SOEs/LGFVs, conduct the following two-step independent analysis:

```
Step A: Support Capability Impact Assessment
  → Does the policy affect local government fiscal revenue or expenditure?
  → Do debt control policies limit local government's capacity to increase leverage?
  → Is the change in transfer payment structure favorable/unfavorable to the locality?

  If yes: Adjust support capability score (see external-support-framework.md Chapter 4)

Step B: Support Willingness Impact Assessment
  → Is the policy environment weakening the "SOE faith"? (competitive neutrality/mixed ownership reform)
  → Is industry reform reducing the issuer's strategic importance?
  → Is there a policy direction toward core asset transfer/control delegation?

  If yes: Reduce support willingness score (see external-support-framework.md Chapter 5)
```

#### 3.4.2 Integration into the Policy Transmission Chain

Between links 2-3 of the standard policy transmission chain (Central → Ministries → Local → Enterprises), add a "support capability vs. support willingness" filter layer:

```
National Level (CPC Central Committee / State Council)
    |
    v
Ministerial Level ———→ Does the policy adjust local government fiscal authority/spending authority?
    |                       ↓ Affects support capability
    |
    v
Provincial/Local Level ——→ Does the local government have the fiscal capacity/willingness to implement?
    |                       ↓ Evaluate both capability and willingness
    |
    v
Enterprise Level ———→ The actual impact of external support changes on the enterprise
```

#### 3.4.3 Impact of Typical Policy Signals on "External Support"

| Policy Signal | Impact on Support Capability | Impact on Support Willingness | Overall Impact |
|--------------|-----------------------------|------------------------------|----------------|
| Increase in central transfer payments | Enhances support capability of central/western provinces | Neutral | Positive — somewhat favorable for western LGFVs |
| Implicit debt resolution "clear to zero" requirement | Limits local fiscal flexibility | LGFV rigid repayment may be broken (willingness decreases) | Negative — LGFV faith weakening |
| "Competitive Neutrality" policy advancement | Neutral | Implicit SOE preferential treatment reduced | Negative — external support weakening |
| Enhanced local government debt accountability | Neutral | Local officials' willingness to rescue decreases (accountability costs rise) | Negative — rescue probability decreases |
| Province-managed-county/City-managed-county system reform | May affect county-level government support capability | Neutral | Case-by-case analysis |
| Industry consolidation policy (e.g., coal/steel) | Neutral | Strategic enterprises may see increased support willingness | Positive — leading SOEs benefit |
| SOE mixed ownership reform | Neutral | SOE attributes weakened = support willingness decreases | Negative — for entities post-reform |
| Significant decline in land transfer revenue | Significantly reduces local government support capability | Neutral | Significantly negative — both LGFVs and SOEs affected |
| Other SOE default in same province without rescue | Neutral | Strong negative signal — support willingness has changed | Extremely negative — requires reassessment of entire region's SOEs |

#### 3.4.4 Practical Checklist

When conducting policy analysis for SOEs/LGFVs, after completing the standard policy interpretation (3.1-3.3), answer each item:

```
□ Does the policy affect the supporter's fiscal revenue/debt capacity?
□ Does the policy change the supporter's rescue incentives (accountability/assessment orientation changes)?
□ Does the policy reduce the issuer's strategic importance (industry reform/intensified competition)?
□ Is the policy driving changes in the issuer's control/equity structure?
□ Are there precedents of other SOE defaults in the same region?
□ Are there signals that the issuer's core assets may be transferred?

Conclusion:
- Support Capability Change: Enhanced / Weakened / Unchanged
- Support Willingness Change: Enhanced / Weakened / Unchanged
- Overall Assessment: External support will likely be Maintained/Enhanced/Weakened
```

---

### 3.5 Policy Volatility Assessment Framework

For policy-driven industries (solar PV, semiconductor), policy volatility is a core variable in credit analysis. Qualitative analysis should assess:

| Dimension | Assessment Method | Low Volatility Characteristics | High Volatility Characteristics |
|-----------|-----------------|-------------------------------|-------------------------------|
| **Policy Frequency** | Number of major policies in past 12 months | <3 times/year | >6 times/year |
| **Directional Consistency** | Whether successive policies are directionally consistent | Continuous support or continuous restriction | Repeated reversal (support → restrict → re-support) |
| **Enforcement Predictability** | Whether policies are published for public comment in advance | Public comment → Trial → Formal Implementation (gradual) | Sudden release, no public comment period |
| **International Constraints** | Degree of impact from international dynamics | Does not involve international relations | Highly tied to geopolitics |
| **Administrative Transition Impact** | Correlation with government transition cycles | Stable across cycles | Direction changes with each cycle |

**Policy Volatility Composite Rating:**

| Rating | Industry Example | Impact on Credit Analysis |
|--------|-----------------|--------------------------|
| **High Volatility** | Solar PV (D4=4) | All credit judgments carry a "policy risk premium"; scoring ranges should be widened |
| **Medium Volatility** | Semiconductor (D4=3) | Policy direction stable but implementation details variable; focus on ministerial implementation rules |
| **Low Volatility** | Data Centers (D4=3) | Policy changes predictable (Eastern Data Western Computing 4-year plan); analyze according to planning cadence |

### 3.6 Example: Electricity Tariff Document No. 136 → Solar PV Module Manufacturer Transmission Chain

**Background:** Assume the National Development and Reform Commission issues a "Notice on Further Improving the On-Grid Electricity Pricing Policy for New Energy" (NDRC Price [2026] No. 136), specifying a 5% reduction in on-grid electricity prices for new solar PV projects in 2026.

**Step 1: Policy Text Analysis**

| Dimension | Analysis Result |
|-----------|----------------|
| D1 Issuing Authority | National Development and Reform Commission (Ministerial level, medium weight) |
| D2 Document Type | Notice (medium-high binding force — "notices" have relatively strong binding force in China's administrative system) |
| D3 Binding Force Level | Conditional ("applicable to new 2026 projects," "existing projects not retroactively affected") |
| D4 Industry Impact Pathway | Demand side (power station IRR declines → reduced installation willingness) + Cost side (module manufacturers face price pressure) |
| D5 Enforcement Strength | Strong: quantified magnitude (5%) + clear scope of application (new projects) |

**Step 2: Transmission Chain Analysis**

```
NDRC issues Document No. 136 (electricity price reduction of 5%)
    │
    │   Policy intent: Reduce subsidy pressure, promote industry grid parity
    │  └─ Not a negative signal — this is a sign the "industry has matured," not "suppression"
    ▼
Provincial Implementation Level
    │
    │   Differences in provincial supporting measures:
    │  ├── Eastern provinces (Jiangsu/Guangdong): Likely to implement directly, as solar PV already at grid parity
    │  └── Western provinces (Gansu/Xinjiang): May delay or compromise (high curtailment rates, already low project IRR)
    │
    ▼
Power Station Investors (Major Power Generators/Local Energy Groups)
    │
    │   Investment Decision Impact:
    │  ├── 5% electricity price reduction → New station full-investment IRR drops from 6.5% to 5.8%
    │  ├── IRR below 6% → Some central SOE internal rate of return thresholds breached → project delays
    │  └── But continued decline in module costs may partially offset electricity price reduction
    │
    ▼
Module Manufacturing Enterprises
    │
    │   Competitive Landscape Impact:
    │  ├── Leading enterprises (LONGi Green Energy/JinkoSolar): Cost leadership → Still able to maintain profits
    │  ├── Second-tier enterprises: Further profit compression → May face losses
    │  ├── Module prices: Expected to continue declining 5-10% (pass-through pressure)
    │  └── Capacity rationalization: Accelerates exit of marginal players
    │
    ▼
Credit Impact
    ├── Industry overall: Neutral (electricity price reduction was anticipated, industry has priced it in)
    ├── Leading enterprises: Somewhat positive (accelerates rationalization of weaker competitors)
    ├── Second-tier enterprises: Somewhat negative (margin pressure)
    └── Pure power station operators: Somewhat negative (project IRR declines, expansion slows)
```

**Step 3: Qualitative Conclusion**

```
Document No. 136 Electricity Tariff Comprehensive Assessment:
├── Policy Strength Score: 4.2 (Strong Signal)
├── Direction Judgment: Not "negative" — electricity price reduction is a sign of industry maturity, leading enterprises actually benefit from rationalization effects
├── Time Window: Short-term (1-3 months) investment wait-and-see → Medium-term (3-6 months) price adjustment completion → Long-term rationalization
├── Differential Impact on Enterprises:
│   ├── LONGi Green Energy: Minimal impact (cost leadership + high overseas revenue share + BC technology premium)
│   ├── Yidao New Energy: Greater impact (cost disadvantage + primarily domestic customers + unlisted, limited financing)
│   └── Enterprises with high centralized power station share: Greater impact (distributed generation less affected by electricity price changes)
└── Data Requiring Ongoing Monitoring:
    ├── Module price trends (PVInfoLink weekly data)
    ├── Central SOE centralized procurement tender prices
    └── Provincial supporting implementation documents (whether adjustments are upward or downward)
```

---

## 4. Structured Provision of Industry Knowledge

### 4.1 Industry Cognitive Framework Construction Process

Industry knowledge in qualitative analysis is not aimless "learning about an industry," but structured knowledge collected and organized according to a fixed framework. The cognitive framework for each industry is built in the following six steps:

```
Step 1: Industry Chain → Know where the money is
Step 2: Cost Structure → Know where the money goes
Step 3: Profit Distribution → Know who is making money
Step 4: Competitive Landscape → Know who will survive
Step 5: Technology Evolution → Know who will be disrupted
Step 6: Regulatory Cycle → Know how the rules change
```

**Analysis Template for Each Step:**

| Step | Core Question | Structured Framework | Output Format |
|------|--------------|---------------------|--------------|
| **1. Industry Chain** | How does the value chain flow from raw materials to end users? | Five Forces Model + Value Chain Positioning | Industry chain map (Upstream → Midstream → Downstream → End Users) |
| **2. Cost Structure** | What is the largest cost item per unit of product? | Cost funnel (top = direct materials, bottom = depreciation + expenses) | Cost composition pie chart + volatility assessment for each item |
| **3. Profit Distribution** | Which link in the value chain has the highest margin? | Gross margin/Net margin range for each link | Profit distribution map ("smile curve" or "inverted smile curve" assessment) |
| **4. Competitive Landscape** | What is the CR5? What are the entry barriers? | Concentration (CR5/CR10) + Effective barriers | Competitive quadrant (Leaders/Challengers/Followers/Niche players) |
| **5. Technology Evolution** | How many years of lifecycle does the current technology have? Where is the replacement technology? | Technology S-curve + Substitution threat assessment | Technology maturity + switching cost assessment |
| **6. Regulatory Cycle** | Is the industry in a deregulation or tightening cycle? | Policy volatility (see Section 3.4) | Regulatory cycle position + forward-looking judgment |

**AI Agent Industry Knowledge Initialization Checklist:**

```
Industry: [Industry Name] Initial Cognitive Framework Checklist:

[ ] Is the industry chain map complete? (3-5 upstream links + 2-3 midstream links + 2-3 downstream links)
[ ] Are the core listed companies at each link labeled (each labeled: A-share/H-share/Unlisted)?
[ ] Are the Top 3 cost items in the cost structure identified?
[ ] Profit distribution — which link has the highest gross margin? What is the approximate total gross profit pool?
[ ] Competitive landscape — Has CR5 data been obtained? (Source labeled)
[ ] Technology pathway — Has maturity assessment been completed for current mainstream pathway and alternative pathways?
[ ] Regulatory cycle — Have major regulatory changes in the past 3 years been reviewed?
[ ] Information sources — Is each structured item labeled with its source level?
[ ] Gap list — What key data has not been obtained?

Processing Rules:
  Completed 80%+ → Industry knowledge framework "ready," can support scoring
  Completed 50-80% → Label "framework pending improvement," scoring includes wider range
  Completed <50% → Suspend analysis for this industry, prioritize framework completion
```

### 4.2 Industry Benchmark Data Comparison

The structured provision of industry knowledge ultimately serves as a **benchmarking yardstick** — to judge whether an enterprise is good or bad, one must know what "good" means. This engine uses three types of benchmarking:

| Benchmarking Type | Method | Example | Applicable Scenarios |
|------------------|--------|---------|---------------------|
| **Listed Company Benchmarking** | Identify comparable listed companies in the same industry and compare key indicators one by one | LONGi Green Energy vs. JinkoSolar vs. Trina Solar (module gross margin comparison) | Most precise — but only applicable when comparable listed companies exist |
| **Industry Average Benchmarking** | Use industry associations/L5 data sources to obtain industry averages | CPIA published industry average gross margin / average capacity utilization | Applicable when precise competitive data is unavailable |
| **Historical Self-Benchmarking** | Current level of the same enterprise vs. its own past 3 years | Tongwei Co. 2026 gross margin vs. 2024 gross margin | Applicable for cyclical industries (determine where in the cycle the company currently stands) |

**AI Agent Benchmark Data Comparison Execution Rules:**

```
Benchmarking Process:
1. Determine benchmarking type (priority: Listed Company > Industry Average > Historical Self)
2. Select benchmarking indicators (depends on current analysis dimension)
3. Construct benchmarking table (rows = enterprises/indicators, columns = values/sources/timestamps)
4. Label data quality (each cell labeled with source level)
5. Determine position ("above industry median" / "in bottom 25% of industry")
6. Output deviation analysis and explanation

Example (Solar PV module gross margin benchmarking, FY2025 data):
| Enterprise | Gross Margin | Source | Timestamp | Position in Industry |
|-----------|-------------|--------|-----------|--------------------|
| LONGi Green Energy | 18.5% | Annual Report (L2) | 2025-Q4 | Industry Top 3 |
| JinkoSolar | 16.2% | Annual Report (L2) | 2025-Q4 | Industry Upper-Mid |
| Trina Solar | 15.8% | Annual Report (L2) | 2025-Q4 | Industry Median |
| Industry Average | 14.5% | CPIA (L5) | 2025-Q4 | — |
| Yidao New Energy | ~10-12% | Brokerage Estimate (L4) | 2025-Q4 | Industry Bottom 25% ← Watch |
```

### 4.3 Industry-Specific Red Flags

Each industry has unique red flags — early warning indicators specific to that industry's structural characteristics. The judgment capability of qualitative analysis largely comes from sensitivity to these industry-specific red flags.

| Industry | Red Flag | Source Level | Warning Window | Severity |
|----------|---------|-------------|---------------|----------|
| **Solar PV** | PERC capacity share >70% (signal of technology pathway obsolescence) | Corporate Disclosure (L2) | 12-24 months | 🔴 Veto |
| | Failed to qualify for central SOE centralized procurement or market share continuously declining | Tender Announcements (L6-L5) | 6-12 months | 🟠 Major |
| | Accounts receivable turnover days increasing for 3 consecutive quarters | Quarterly Reports (L2) | 3-6 months | 🟡 Watch |
| **Semiconductor** | Placed on Entity List or SDN List | U.S. Department of Commerce (L6) | 0 (immediate) | 🔴 Veto |
| | Key equipment/EDA supply disruption risk | Corporate Disclosure + News (L2/L3) | 0-6 months | 🔴 Survival |
| | Consecutive departures of core technical personnel | Company Announcements (L2) | 6-12 months | 🟠 Major |
| **NEV-OEM** | Monthly sales <10,000 units and declining for 3 consecutive months | CPCA (L5) | 3-6 months | 🔴 Survival |
| | Cash runway <12 months | Financial Reports (L2) | 6-12 months | 🔴 Survival |
| | Dealer inventory >2 months | Channel Research (L4) | 3-6 months | 🟠 Major |
| **Advanced Manufacturing** | CNC system + spindle + servo all externally sourced without domestic alternative | Technical Teardown + Annual Reports (L4/L2) | 12-24 months | 🔴 Veto |
| | R&D capitalization rate >40% | Annual Reports (L2) | 12-24 months | 🟠 Major |
| | Q4 revenue share >40% for 2 consecutive years | Annual Reports (L2) | 6-12 months | 🟡 Watch |
| **Biopharma** | Core pipeline Phase III clinical trial failure | Company Announcements (L2) | Immediate | 🔴 Veto |
| | Cash runway <6 months and no new BD upfront payments | Financial Reports (L2) | 3-6 months | 🔴 Survival |
| | FDA/NDA approval rejected or delayed | FDA Announcements (L6) | Immediate | 🟠 Major |
| **Data Centers** | Core customer lease expires with confirmed non-renewal | Company Disclosure (L2) | 6-12 months | 🔴 Veto |
| | Utilization rate declining for 2 consecutive quarters | Company Disclosure (L2) | 6-12 months | 🟠 Major |
| | PUE consistently 0.15+ above industry peers | Industry Reports (L4/L5) | 12-24 months | 🟡 Watch |
| **Medical Devices** | Class III registration certificate expired and cannot be renewed | NMPA Official Website (L6) | 0-12 months | 🔴 Veto |
| | Failed volume-based procurement bid or price reduction >80% | Volume-Based Procurement Announcements (L6) | 0-3 months | 🟠 Major |
| | Share of hospital accounts receivable aging >1 year increasing | Annual Reports (L2) | 6-12 months | 🟡 Watch |

**AI Agent Red Flag Processing Rules:**

```
When a red flag signal is detected:
1. Immediately escalate the priority of that signal (upgrade from routine monitoring to focused attention)
2. Check whether the red flag belongs to a veto condition for that industry
3. If a veto condition → Immediately suspend subsequent analysis, output "Veto Triggered"
4. If not a veto condition but classified as Major level (🔴 / 🟠) →
   a. Set the maximum score for that dimension to 4 (out of 10)
   b. Mark that dimension's low confidence in the cross-validation matrix
   c. Require the red flag and its potential impact to be separately listed in the report
5. Continuous monitoring (set to weekly check frequency, not quarterly)
```

### 4.4 Cross-Industry Universal Red Flags

Some red flags apply across all industries. These signals are typically **governance-level** issues, not industry-specific knowledge, but need to be standard check items in qualitative analysis:

| Red Flag | Detection Method | Source Level | Severity |
|----------|-----------------|-------------|----------|
| **Major shareholder high pledge ratio (>70%)** | Company announcements/Quarterly reports | L2 | 🔴 Major — Risk of major shareholder capital chain rupture |
| **Controlling shareholder/actual controller change** | Company announcements | L2 | 🟠 Watch — Control instability |
| **Auditor non-standard opinion/change** | Annual report audit opinion | L2 | 🔴 Major — Possible financial issues |
| **Exchange inquiry letter/regulatory attention** | Exchange announcements | L6 | 🟠 Watch — Regulators have noted anomalies |
| **Asset restructuring/core asset divestiture** | Company announcements | L2 | 🟠 Watch — Possible asset stripping |
| **Related party transaction share jump (>20% of revenue)** | Annual report related party transaction disclosure | L2 | 🟠 Watch — Possible tunneling |
| **Concentrated departures of executives/core technical personnel** | Company announcements | L2 | 🟠 Major — Talent drain signal |
| **Sharp increase in arbitration/litigation filings** | Judgment documents website (L6) | L6 | 🟠 Watch — Reflects increasing business disputes |
| **Equity financing failure/IPO termination** | Exchange announcements | L6 | 🟠 Major — Capital market confidence insufficient |
| **Net assets negative/insolvent** | Annual reports | L2 | 🔴 Veto (de facto D rating) |

**Cumulative Effect of Universal Red Flags:**

```
Two or more universal red flags appearing simultaneously → Severity automatically escalates one level
Three or more universal red flags appearing simultaneously → Regardless of industry score, composite rating cap automatically lowered to B

Example:
  Enterprise A: Major shareholder pledge 75% (🔴) + Auditor change (🔴) + Related party transactions 25% (🟠)
  → 3 universal red flags appearing simultaneously → Severity escalation
  → Even if fundamental scoring appears good (e.g., L1-L4 scores all >6), composite rating cap lowered to B
  → Label: "Multiple governance red flags superimposed, hidden risks not covered by fundamental framework"
```

---

## 5. Practical Methodology of Mosaic Assembly

### 5.1 Fragment → Signal → Picture: Five-Step Process

Mosaic assembly is the core methodology for aggregating multiple pieces of fragmented information into a credit judgment. This process is not linear but iterative — each new fragment may revise previous judgments.

```
Five-Step Process:

Step 1: Fragment Collection
    ├── Source: Multi-dimensional WebSearch (policy/industry/enterprise/market/legal)
    ├── Output: Raw fragment list (each item includes source URL + timestamp + source level)
    └── Key Constraint: No pre-set positions — "collect first, judge later"

Step 2: Signal Extraction
    ├── Operation: Extract structured signals from each fragment
    ├── Output: Signal object (content + dimension + direction + strength + credibility)
    └── Key Constraint: LLM extracts but does not judge — "only structure, no evaluation"

Step 3: Dimension-Based Aggregation
    ├── Operation: Group and aggregate signals by industry pyramid dimensions (L1-L4)
    ├── Same direction accumulation: Same-dimension, same-direction signals reinforce each other (confidence level upgraded one tier)
    ├── Contradictory signal labeling: Same-dimension, opposite-direction signals require explanation of contradiction
    └── Output: Signal package for each dimension (signal count + direction + confidence + strength)

Step 4: Cross-Dimension Cross-Validation
    ├── Operation: Check whether signals from different dimensions support or contradict each other
    ├── Reinforcement mechanism: L1 bullish + L2 bullish = Judgment strengthened (confidence greatly increased)
    ├── Contradiction mechanism: L1 bullish + L4 (financial) bearish = Divergent signal → check for framework omissions
    └── Output: Cross-dimension consistency score (Consistent/Partially Consistent/Significant Divergence)

Step 5: Picture Construction
    ├── Operation: Based on signal packages from each dimension and cross-dimension consistency, write a complete credit profile
    ├── Output: Comprehensive judgment + confidence label + residual uncertainty
    └── Key Constraint: Must label "what is not known" — "what you know must be explained clearly, what you don't know even more so"
```

### 5.2 Signal Accumulation Rules

Signal accumulation qualitative rules are used to determine the combined strength of multiple same-direction signals:

| Accumulation Combination | Accumulation Result | Example |
|----------------|-----------|---------|
| 1 L5 + 1 L4 same direction | Assessed as "L4+ credible" (not upgraded to L5, but confidence greatly increased) | CPIA data (L5) + brokerage research (L4) both indicating overcapacity |
| 2 L4 same direction | Can be upgraded to "L4 cross-validated" (equivalent to L5 confidence) | CITIC Securities + CICC research both predicting losses for a specific enterprise |
| 1 L4 + 1 L3 same direction | Assessed as "partially confirmed" (requires more source support) | Brokerage research (L4) + financial news report (L3) both mentioning capital chain strain at a specific enterprise |
| 3 L3 same direction | Can be upgraded to "multi-source media confirmation" (still below L4) | 3 different media outlets all reporting work stoppage at a specific enterprise |
| 1 L6 + 1 L2 | Favor L6, with L2 as supplement | NDRC document (L6) + company announcement (L2) consistent on subsidy phase-down statements |
| L4 + L4 opposite direction | Label as "significant disagreement on this dimension" | CITIC Securities bullish, CICC bearish on same industry's 2026 installed capacity |

**Strength Upgrade Rules (Auto-Trigger):**

```
Strength Upgrade: Same dimension receives ≥2 independent same-direction signals → Signal strength for that dimension automatically upgraded one level
  L4 (single source) → L4 (cross-validated)
  L3 (single source) → L3 (multi-source confirmed)

Strength Downgrade: Same dimension has contradictory signals → Confidence for that dimension automatically downgraded one level
  All signals labeled with disagreement status
```

### 5.3 Missing Fragment Handling

Incomplete information is the norm, not the exception. The core principle of the mosaic methodology is: **"Not knowing" is itself an important signal.**

| Missing Type | Meaning | Processing Rules |
|-------------|---------|-----------------|
| **Knowable but not obtained** | Data exists in the public domain but was not covered by this search | Label "data obtainable but not covered in this analysis" → Suggest supplementary search |
| **Theoretically exists but not disclosed** | The enterprise holds the data but has not publicly disclosed it | Label "not publicly disclosed by enterprise" → This itself is a risk signal (suspicion of selective disclosure) |
| **Fundamentally unknowable** | The data does not publicly exist (e.g., unaudited operational data) | Label "data unavailable" → Use alternative proxies or accept reduced confidence for this dimension |

**AI Agent Missing Fragment Handling Process:**

```
For each analysis dimension, check signal density (number of signals obtained / number of signals expected):

Signal density > 80% → Directly output judgment for this dimension, confidence "High"
Signal density 50-80% → Output judgment with "partial data missing, confidence Medium"
Signal density 20-50% → Output only "directional judgment," label "insufficient information, pending supplementation"
Signal density < 20% → Do not output judgment for this dimension, label "this dimension cannot be assessed"

Missing Fragment Labeling Format:
  [Dimension Name] Key Missing Signals:
  1. [Specific missing data] — Source: [where it should exist] — Impact: [uncertainty caused by absence]
  2. [Specific missing data] — Source: [where it should exist] — Impact: [uncertainty caused by absence]
  
  Gap Composite Assessment:
  ├── Signal density: [%]
  ├── Impact on final score: [± range]
  └── Recommended supplementation method: [additional searches, paid data source access, etc.]
```

### 5.4 Narrative vs. Fact Separation Technique

China's credit market is awash with "market narratives" — widely circulated but unverified collective beliefs. One of the core capabilities of qualitative analysis is separating facts from narratives.

**Common Market Narrative Inventory:**

| Market Narrative | Corresponding Industry | Narrative Analysis | Source Level Warning |
|-----------------|----------------------|-------------------|---------------------|
| "National Semiconductor Fleet" | Semiconductor | State support does not guarantee individual enterprises won't default — Tsinghua Unigroup has been proven | L4-L2 signals over-interpreted as L6-level certainty |
| "SOE Faith" | All SOEs | SOE status does not guarantee no default — Yongcheng Coal has been proven | L6 (SOE status) incorrectly linked to credit quality |
| "Too Big to Fail" | Leading enterprises across industries | Large scale does not guarantee no risk — Evergrande has been proven | Scale indicators (L2) misinterpreted as safety signals |
| "Good sector means good company" | High-growth industries | Profitable industries still have loss-making enterprises — over half of solar PV industry was loss-making in 2025 | Industry signals (L5) incorrectly mapped to individual enterprises (L2) |
| "IPO approval = credit endorsement" | Pre-IPO companies | IPO approval does not confirm financial statement accuracy | L2 (prospectus) incorrectly valued above its actual credibility |
| "Technology leadership = moat" | Technology companies | Technology leadership can be quickly caught up — patent time windows are limited | L2 technology data overvalued |

**Narrative Checklist (Execute Before Each Judgment Output):**

```
[ ] Is this judgment based on "publicly verifiable facts" or "industry consensus"?
[ ] If all media reports and brokerage research were removed, and only official data and industry data were examined, would the conclusion change?
[ ] How do most people in the current market view this enterprise? Are we consistent with or different from the mainstream view?
[ ] If the conclusion differs from market consensus, what basis do we have to support a contrarian judgment?
[ ] Is there any suspicion of "copying because everyone is saying this"?

Determination Rules:
  If the judgment is primarily based on "industry consensus/market narrative" rather than independently cross-verified facts →
    Label "this judgment is influenced by market narrative, insufficient independent factual support"
    Confidence automatically downgraded one level
    Scoring range widened (±1 → ±2)
```

**Narrative vs. Fact Separation Example: "SOE Faith" in the Yongcheng Coal Case:**

| Narrative Layer (What the market believed) | Fact Layer (What public data revealed) |
|-------------------------------------------|--------------------------------------|
| "Henan SOE, AAA rated, AAA backed by government credit" | Parent company debt ratio 94.87% (annual report data) |
| "Although profitability declining, SOEs can always refinance" | Net profit attributable to parent -11.44 billion (annual report data) |
| "Short-term bond issuance smooth, market accepted" | Short-term debt ratio 59.14%, severe maturity mismatch (annual report data) |
| "Henan provincial government will provide rescue" | Related party receivables 22.5 billion — funds already tied up (annual report data) |

**Separation Technique Operation:** List L2 (enterprise annual report data) and L6+L3 (market narrative) separately, clearly labeling "fundamental conflict between market consensus and public data" → Use L6+L2 as judgment basis, L4+L3 as reference but not dominant.

### 5.5 Complete Example: Five Fragments of Tongwei Co. Piecing Together "Deteriorating Debt Servicing Capacity + Lagging Ratings"

This example already has signal-level analysis in the mosaic engine document. Here it is presented from the perspective of the **qualitative judgment construction process** to demonstrate the methodology.

**Analysis Objective:** Assess Tongwei Co.'s credit trend through fragment assembly without relying on precise financial models.

**Fragment Collection Phase:**

| Fragment ID | Fragment Content | Source | Level | Timestamp |
|------------|-----------------|--------|-------|-----------|
| A | Tongwei short-term bond issuance rate decreased from 2.60% to 2.02% (-58bp) in 2025 | China Money Network | L5 | 2025/Q1-Q3 |
| B | Tongwei short-term bond issuance rate rebounded from 2.02% to 2.15% (+13bp) in January 2026 | China Money Network | L5 | 2026-01 |
| C | Tongwei 2025 performance forecast: loss of 9-10 billion RMB | Company Announcement | L2 | 2026-01 |
| D | Tongwei accounts receivable jumped from Q3 to Q4 (announcement data) | Company Announcement | L2 | 2025-Q4 |
| E | External rating maintained at AAA/Stable | Rating Agency Announcement | L5 | 2026-03 |

**Step 1: Classification and Aggregation (by L4 Financial Dimension)**

| Signal | Direction | Strength | Credibility |
|--------|-----------|----------|-------------|
| A: Issuance rate continuously declining | Positive (cost decreasing) | Weak (broad monetary easing, not the enterprise's own improvement) | L5 |
| B: Issuance rate rebounding 13bp | Negative | Medium (inflection point signal) | L5 |
| C: Loss of 9-10 billion | Negative | Strong (quantified, significant negative signal) | L2 |
| D: Accounts receivable jumping | Negative | Medium (requires comparison with historical data to confirm not seasonal) | L2 |
| E: AAA/Stable maintained | Positive | Weak (known rating lag — this signal's credibility should be downwardly revised) | L5 (but low credibility) |

**Step 2: Signal Accumulation**

```
Fragment A (Positive) + Fragment B (Negative) = Inflection Point Signal
  ├── Fragment A's "positive" is driven by monetary environment (not the enterprise's own improvement)
  ├── Fragment B's "negative" cannot be explained by monetary environment (money market rates were stable)
  └── Accumulation Conclusion: The A→B change is a signal of independently rising credit premium

Fragment C (Loss) + Fragment D (Receivables Jump) = Double Negative Signal Accumulation
  ├── C: Profitability deterioration (losses)
  ├── D: Cash flow deterioration (slower collection)
  └── Accumulation Conclusion: Not just "losing money" — but a double hit of "losing money + not collecting cash"

Fragment E (AAA Maintained) vs. Fragments A-D = Signal Contradiction
  ├── A-D all point to "credit deterioration"
  ├── E points to "everything is normal"
  └── Contradiction handling: Favor A-D (positive + negative cross-validated) → E treated as "lagging signal"
```

**Step 3: Cross-Dimension Cross-Validation**

```
L4 (Financial Layer) Signal Summary:
  ├── 📉 Massive losses (3/5 strength)
  ├── 📉 Receivables jump (3/5 strength)
  ├── 📉 Financing cost inflection point appears (4/5 strength — because this is a market signal, most real-time)
  ├── 📗 External rating maintained (2/5 strength — serious lag issue)
  └── Composite: L4 direction is clearly "negative," confidence medium-high

L1 (Policy Layer) Check: No major solar PV policy changes in 2025-2026 → Industry-level additional pressure on Tongwei is limited
L2 (Technology Layer) Check: Tongwei's TOPCon capacity share is high, technology pathway not obsolete → No technology risk
L3 (Supply Chain Layer) Check: Customer concentration medium-high but controllable → No supply chain crisis

Cross-Dimension Consistency Assessment:
  └── L1/L2/L3: No major negative signals + L4: Strongly negative → Not systemic risk, but individual enterprise financial deterioration
  └── Conclusion: Tongwei's debt servicing capacity deterioration is "enterprise-specific," not "industry-wide"
```

**Step 4: Comprehensive Picture**

```
Tongwei Co. Credit Qualitative Assessment (as of 2026-03):
├── Core Trend: Debt servicing capacity deteriorating (direction clear)
├── Nature of Deterioration: Enterprise-specific rather than systemic (no major negative industry factors)
├── Deterioration Speed: Medium-paced — gradual rather than sudden
├── Signal Structure:
│   ├── ✅ Losses + Receivables + Financing inflection point: three independent sources pointing to the same direction (high confidence)
│   ├── ⚠️ AAA maintained: contradictory to the above three signals — assessed as rating lag (known deficiency of this framework)
│   └── ❌ Parent company individual financial statements unavailable: cannot precisely assess true debt servicing capacity at parent level
├── Residual Uncertainty:
│   ├── Parent company financial data missing → Scoring range ±1.5
│   └── Timing of rating adjustment uncertain → But does not affect direction judgment
└── Qualitative Conclusion: Tongwei's actual credit quality has fallen below AAA, but there is still significant distance to CCC
    → Estimated in BB-B range (ex post: downgraded to AA in May 2026, further downgraded later)
```

---

## 6. Information Timeliness Management

### 6.1 Decay Curves for Different Information Types

Each type of information has a different "useful life" after entering the analysis framework. Qualitative analysis must clearly understand the timeliness window for each type of information and label or replace it after expiration.

| Information Type | Useful Life | Decay Characteristics | Expiration Handling |
|-----------------|------------|----------------------|-------------------|
| **Macro Policy Documents** | 1-2 years (major policies) / 6-12 months (implementation rules) | Slow decay — but when new documents are issued, old documents immediately become invalid | Within 24 hours of new document issuance, old signal downgraded to "expired" |
| **Industry Statistics** | 1 statistical period (quarterly data = 3 months, annual data = 12 months) | Stepped decay — becomes invalid when new period data is released | Immediately replaced when new data is released |
| **Enterprise Financial Data** | Until next financial report release | Stepped decay — semi-annual financial data partially invalidated upon Q3 report release | Updated upon quarterly/semi-annual/annual report release |
| **Market Data (Spreads/Prices)** | Weekly window | Fast continuous decay — spread data from 2 weeks ago has limited value for current judgment | Rolling window — historical data beyond 60 trading days used only for trend analysis |
| **News Events** | 3-7 days (event information) / 1-3 months (structural information) | Fast decay — 1 week after the event, value as "news" essentially disappears | But "factual" parts of events (e.g., announcement content) can be retained, converted to structured signals |
| **Rumors/Social Media** | 1-7 days | Very fast decay — needs tracking of "whether confirmed or disproven" | Rumors unverified beyond 7 days automatically downgraded to "invalid signal" |
| **Brokerage Research Reports** | 1-3 months | Slow decay — industry judgments in reports lose effectiveness monthly | Beyond 3 months, mark as "possibly outdated," check for updated reports |

### 6.2 Event Types Triggering Reassessment

Not all new information warrants triggering a full reassessment. The following event types should trigger different levels of reassessment:

| Event Type | Trigger Level | Action | Timeliness Requirement |
|-----------|--------------|--------|----------------------|
| **Policy Sudden Change** (e.g., subsidy suspension, export ban) | 🔴 Full Reassessment | Re-run complete analysis process (L1-L4 all rescored) | Within 24 hours of receiving information |
| **Veto Condition Triggered** | 🔴 Immediate Suspension | Stop subsequent analysis, output "Veto" | Immediately upon receiving information |
| **Rating Adjustment** (upgrade or downgrade) | 🟠 Partial Reassessment | Update Track B signals, check whether Track A needs revision | Within 1 week of rating announcement |
| **Financial Report Release** | 🟠 Quarterly Reassessment | Update financial layer scores, check whether upper-level judgments need revision | Within 2 weeks of financial report release |
| **Major Operational Event** (production halt/recall/major customer loss) | 🟠 Partial Reassessment | Reassess signals for relevant dimensions | Within 1 week of event confirmation |
| **Major Management/Shareholder Change** | 🟡 Watch Level | Update governance assessment, incorporate into monitoring | Within 2 weeks |
| **Industry Data Update** (CPIA quarterly data, etc.) | 🟡 Monitoring Level | Update industry benchmark data | Within 2 weeks of data release |
| **Market Rumors** (unverified major negative) | 🟢 Alert Level | Label "pending verification," initiate search verification | Determine whether upgrade needed within 1 week |

**AI Agent Trigger Rules:**

```
When a new signal is received:

1. Check if it belongs to a "Full Reassessment" event (policy sudden change/veto)
   ├── Yes → Immediately suspend current analysis, initiate full reassessment process
   └── No → Continue

2. Check if it belongs to a "Partial Reassessment" event (rating adjustment/financial report/major operational event)
   ├── Yes → Update relevant dimensions on basis of current analysis
   └── No → Continue

3. Check if it belongs to a "Watch Level" event (management change/industry data update)
   ├── Yes → Update relevant monitoring list, does not trigger rescoring
   └── No → Continue

4. Default handling: Low-priority signals incorporated into monitoring list, processed at next routine reassessment
```

### 6.3 Expired Information Labeling and Replacement Rules

Once information exceeds its useful life, it must be explicitly labeled rather than silently removed — **expired information still provides historical reference value**.

| Expiration Status | Labeling Method | Usage Restrictions |
|------------------|----------------|-------------------|
| **Updated** | Label "has been updated by [new data source][timestamp]" | Old data retained in historical records, but scoring based on new data |
| **Partially Outdated** | Label "data source from [timestamp], may not fully reflect current situation" | Used only for trend reference, not for precise scoring |
| **Fully Outdated** | Label "information expired — exceeds useful life by [X] times" | Not used for current scoring, only retained in historical records |
| **Disproven** | Label "disproven by [source]" | Removed from valid signal list, retained in "disproven signals" record |

**Routine Reassessment Cycles:**

| Industry Type | Recommended Reassessment Cycle | Explanation |
|--------------|------------------------------|-------------|
| **Policy-Driven** (solar PV/semiconductor) | Monthly | Frequent policy changes require high-frequency tracking |
| **Technology Barrier** (advanced manufacturing/biopharma/medical devices) | Quarterly | Major pipeline/product events trigger reassessment |
| **Volume Competition** (NEV-OEM) | Monthly | Sales/price changes rapidly |
| **Asset Lease** (data centers) | Quarterly | Stable lease structure, slower changes |

**General Rule: When any industry triggers a full reassessment event, immediately execute reassessment regardless of the cycle.**

---

## 7. Qualitative Analysis Output Standards

### 7.1 Output Specification for Each Judgment

The output of qualitative analysis is not "feelings" or "opinions" — but structured conclusions with a complete supporting chain. **Each qualitative judgment must include the following five elements:**

```
[Judgment Content] — Concise conclusive statement

├── 1. Supporting Signal List
│   ├── Signal A: [content] — Source Level: [Lx] — Timestamp
│   ├── Signal B: [content] — Source Level: [Lx] — Timestamp
│   └── Signal C: [content] — Source Level: [Lx] — Timestamp
│
├── 2. Source Credibility Composite Assessment
│   ├── Overall Credibility Level: [High/Medium-High/Medium/Medium-Low/Low]
│   ├── Highest Quality Signal: [which signal, what level]
│   └── Weakest Signal/[Concern]: [which signal may have bias]
│
├── 3. Cross-Validation Status
│   ├── ✅ Verified: [number of independent sources confirming]
│   ├── ⏳ Partially Verified: [which signals have only single source]
│   └── ⚠️ Pending Verification: [which signals require further investigation]
│
├── 4. Uncertainty Labeling
│   ├── Known Sources of Uncertainty: [specifically list]
│   ├── Degree of Impact on Judgment: [Minor Impact/Medium Impact/Could Reverse Judgment]
│   ├── Key Data Gaps: [which data is missing]
│   └── If the judgment is wrong, the most likely reason: [reverse validation consideration]
│
└── 5. Timestamp and Validity Period
    ├── Judgment Formation Time: [date]
    ├── Valid Until: [date] (or "after next financial report release")
    └── Conditions Triggering Update: [what events require this judgment to be updated]
```

**Output Example:**

```
Judgment: Tongwei Co.'s debt servicing capacity is gradually deteriorating, AAA rating has lagging risk

1. Supporting Signal List:
   ├── A: 2025 pre-loss of 9-10 billion RMB — Company Announcement (L2) — 2026-01
   ├── B: Accounts receivable jumped from Q3 to Q4 — Company Announcement (L2) — 2025-Q4
   ├── C: Short-term bond issuance rate showed 13bp inflection point in January 2026 — China Money Network (L5) — 2026-01
   └── D: AAA/Stable rating maintained — Rating Agency (L5) — 2026-03 (but this signal contradicts A-C)

2. Source Credibility Composite Assessment:
   ├── Overall Credibility: Medium-High (L2+L5 multi-source coverage)
   ├── Highest Quality Signal: C (L5-level issuance rate data, objective and real-time)
   └── Weakest Signal: D (AAA rating — known lag issue, use downward-revised assessment)

3. Cross-Validation Status:
   ├── ✅ Verified: Profit deterioration (A+C cross-validated, losses + financing cost increase)
   ├── ⏳ Partially Verified: Accounts receivable jump (D single source, needs confirmation of whether seasonal)
   └── ⚠️ Pending Verification: Parent company debt servicing capacity (no parent company individual financial statement data)

4. Uncertainty Labeling:
   ├── Known Sources of Uncertainty: Parent company financial data unavailable
   ├── Degree of Impact: Medium — consolidated statements already show clear deterioration signals, but parent company precise leverage ratio unknown
   ├── Key Data Gaps: Parent company individual financial statements (debt ratio/cash flow/short-term debt coverage)
   └── If the judgment is wrong, the most likely reason: 2026 solar PV industry recovers beyond expectations, Tongwei's profitability rebounds significantly

5. Timestamp and Validity Period:
   ├── Judgment Formation Time: 2026-03-15
   ├── Valid Until: After Q1 2026 quarterly report release (approximately 2026-04)
   └── Trigger Update Conditions: New quarterly report release, rating adjustment, major industry policy change
```

### 7.2 Prohibited Output List

The following types of output must not appear in qualitative analysis reports under any circumstances:

| Prohibited Type | Example | Why Prohibited | Should Be Replaced With |
|----------------|---------|----------------|------------------------|
| **Unsupported Assertion** | "This company is insolvent" | No specific data and sources attached to support this judgment | "Based on FY2025 annual report data (L2), the company's net assets are -X billion, debt ratio XX%" |
| **Untimestamped Judgment** | "LONGi Green Energy is an industry leader" | No timestamp basis for the judgment (leader status may change over time) | "As of end of 2025, LONGi Green Energy's module shipments rank X globally (PVInfoLink/L5)" |
| **Certainty Conclusion Without Uncertainty Labeling** | "Tongwei will definitely default" | There are no 100% conclusions in credit analysis | "Based on current signals (losses + financing inflection point + receivables rising), Tongwei's credit quality is deteriorating, but default depends on [key variables]" |
| **Subjective Impression** | "Management seems very reliable" | Unverifiable subjective judgment | "Management stated [specific statements] at the 2025 earnings call, and the fulfillment status of [specific past commitments] is [result]" |
| **Projected Financial Data** | "Estimated net profit of 5 billion in 2026" | No projection basis and assumption conditions labeled | "If module prices remain at current levels (0.8 RMB/W), LONGi's 2026 gross margin may be 18-20% (based on [basis])" |
| **Stock Price Advice** | "Recommend buying" | This engine does credit analysis, not equity investment advice | "Based on current spread level (258bp, above industry median), this bond is in the relatively expensive range within the solar PV industry" |
| **Vague Source Citation** | "According to sources" / "According to industry insiders" | Source unverifiable | Label exact source or explicitly label L1 "anonymous source, unverifiable" |
| **Rating Agency Conclusion Replication** | "External rating AAA, good credit quality" | External ratings are input not output, and are known to lag | Independently analyzed judgment; may cite external rating but must label known issues |

### 7.3 Output Quality Checklist

Before each qualitative judgment output, the following checks must be performed:

```
[ ] Is each judgment accompanied by a supporting signal list (≥2 independent sources)?
[ ] Is each signal labeled with its source level (L1-L6)?
[ ] Is each signal labeled with a timestamp?
[ ] Is the cross-validation status labeled (Verified/Partially Verified/Pending Verification/Contradiction)?
[ ] Are sources of uncertainty and degree of impact labeled?
[ ] Are the judgment validity period and trigger update conditions labeled?
[ ] Is there a distinction between "fact" and "interpretation" (what the facts are + what I judged based on the facts)?
[ ] Has the influence of market narrative been excluded? (Execute narrative checklist)
[ ] If contradictory signals exist, is the contradiction cause and handling method explained?
[ ] Are key data gaps labeled?
[ ] Are all prohibited output types avoided?
[ ] If the judgment involves a predictive element, are the underlying assumptions labeled?
```

### 7.4 Position of Qualitative Analysis in Comprehensive Reports

Qualitative analysis is not output independently — it serves as the underlying methodology for Track A (Fundamental Pyramid Scoring), reflected in the following parts of the report:

| Report Position | Specific Qualitative Analysis Content | Format Requirements |
|----------------|--------------------------------------|-------------------|
| **Core Conclusion** | Qualitative judgment on credit trend (deteriorating/stable/improving) | One-sentence summary + confidence label |
| **Each Layer's Scoring Basis** | Qualitative support for each layer's scoring (industry trend, policy impact, competitive position) | Each signal labeled with source and level |
| **Cross-Dimension Cross-Validation** | Consistency/divergence judgment across different levels of signals | Consistency score + divergence reasons |
| **Uncertainty Statement** | Known uncertainties and data gaps | Structured gap list |
| **Mosaic Completeness Report** | Signal density and gaps for each dimension | Signal density bar chart + gap list |

**Standard Format for Qualitative Analysis Sections in Reports:**

```
## [Dimension Name] Qualitative Analysis

### Industry Background Assessment (1-2 paragraphs)
Overview of industry trends based on L6/L5 data, no more than 100 words.

### Enterprise Position in This Dimension
Specific signal support, each signal labeled with source and timestamp.

### Key Uncertainties (if applicable)
Clearly label blind spots and assumptions in the analysis.

### Qualitative Judgment Conclusion
Integrated output of direction + strength + confidence.
```

### 7.5 Confidence Levels for Qualitative Analysis

All qualitative judgments must be labeled with a confidence level. Confidence is not a guarantee of judgment correctness, but an assessment of the **sufficiency of supporting signals**:

| Confidence Level | Meaning | Applicable Conditions | Representation in Reports |
|-----------------|---------|----------------------|--------------------------|
| **High** | Sufficient signals, clear trend, multiple independent sources cross-validated | ≥3 independent L4+ signals pointing to same direction, no unresolved contradictions | Green labeling |
| **Medium-High** | Relatively sufficient signals, trend discernible, main signals already cross-validated | ≥2 L4+ signals + no fatal contradictions, but 1 minor contradictory signal | Blue labeling |
| **Medium** | Signals exist but not sufficient, direction discernible but magnitude uncertain | 1 L4+ signal + 1-2 L3 signals, no serious contradictions | Yellow labeling |
| **Medium-Low** | Sparse signals, direction judgment has significant uncertainty | Only L3 and below signal support, or unresolved contradictory signals exist | Orange labeling |
| **Low** | Severely insufficient signals, only directional speculation | Signal density <30%, or judgment primarily based on L1-L2 signals | Red labeling — consider "not outputting this judgment" |

**Confidence Constraints on Scoring:**

| Confidence Level | Constraint on Scoring |
|-----------------|----------------------|
| High | Precise score can be output (±0.5 range) |
| Medium-High | Scoring range ±1.0 |
| Medium | Scoring range ±1.5 |
| Medium-Low | Only directional score output (e.g., "score ≤4" or "score ≥6") |
| Low | Do not output score for this dimension, label "insufficient information to score" |

---

## Appendix

### A. Full-Process Integration of Qualitative Analysis

Qualitative analysis as part of the engine methodology, its integration with the existing framework:

```
Information Input (Various data and signals)
    │
    ▼
Chapter 2: Information Credibility Assessment
    │  └─ Six-level classification + Cross-validation + Contradiction handling
    ▼
Chapters 3 + 4: Industry Knowledge Framework
    │  └─ Policy interpretation + Industry cognition + Red flag monitoring
    ▼
Chapter 5: Mosaic Assembly
    │  └─ Five-step process + Signal accumulation + Narrative separation
    ▼
Chapter 6: Timeliness Check
    │  └─ Decay curves + Trigger reassessment + Expiration replacement
    ▼
Chapter 7: Output Standards
    │  └─ Five elements + Prohibited list + Checklist
    ▼
Track A (Fundamental Pyramid Scoring)
    │
    └─→ Cross-Validation Matrix → Composite Rating Output
```

### B. Core Principles Summary

| # | Principle | Meaning |
|---|-----------|---------|
| 1 | **Qualitative judges direction, quantitative calibrates precision** | Core division of the dual-track framework, not to be confused |
| 2 | **Source classification is the foundation of everything** | Signals not labeled with source level shall not enter the analysis framework |
| 3 | **A single signal does not constitute a judgment** | All key judgments require ≥2 independent sources for cross-validation |
| 4 | **Policy is the biggest variable but the most easily misinterpreted** | Policy interpretation follows the five-dimensional framework, quantify strength score before incorporation |
| 5 | **Industry knowledge is structured, not felt** | Six-step industry cognitive framework ensures comprehensive coverage |
| 6 | **Mosaic assembly pursues completeness, not precision** | Acknowledge gaps, make "not knowing" part of the output |
| 7 | **Narrative and facts must be separated** | Market consensus is not fact; train to recognize common narrative traps |
| 8 | **Information has timeliness, expiration must be labeled** | Untimestamped judgments are equivalent to invalid judgments |
| 9 | **Every judgment carries an uncertainty imprint** | There is no 100% certain credit judgment |
| 10 | **Qualitative analysis is methodology, not intuition** | Every step has a structured process, traceable, verifiable, improvable |

### C. Cross-References with Existing Documents

| Existing Document | Relationship with This Document | Key Integration Points |
|-----------------|-------------------------------|----------------------|
| [Dual-Track Analysis Methodology](dual-track-methodology.md) | Top-level design of the dual-track framework | Qualitative analysis is the methodological foundation of Track A (Fundamental Scoring) |
| [Mosaic Engine](mosaic-engine.md) | Technical implementation of signal extraction and assembly | Chapter 5 (Mosaic Assembly Practice) is the qualitative supporting methodology for the Mosaic Engine |
| [Quantitative Analysis Methodology](quantitative-analysis.md) | Track B quantitative analysis standards | Qualitative judges direction (this document) → Quantitative calibrates precision (quantitative document) = complete dual-track |
| [Engine Architecture Overview](engine-overview.md) | Engine global architecture | This document is one of the underlying methodologies for Track A |
| [Multi-Stakeholder Perspective Framework](multi-stakeholder.md) | 6 role perspectives | Section 1.3 of this document details the weight differences of qualitative analysis across roles |
| [Industry Classification and Analysis Framework](industry-framework.md) | Industry types and pyramid specifications | Section 4.3 (Industry-Specific Red Flags) directly relates to veto conditions for each industry pyramid |

### D. Document Version History

| Version | Date | Changes |
|---------|------|---------|
| v0.0.1 | 2026-07-08 | Initial release: Seven-chapter qualitative analysis methodology |
| — | — | Coverage: Positioning, source classification, policy interpretation, industry knowledge, mosaic assembly, timeliness, output standards |
| — | — | Examples: Electricity tariff Document No. 136 policy transmission, Tongwei multi-fragment mosaic, policy signal vs. noise differentiation, SOE narrative separation |
