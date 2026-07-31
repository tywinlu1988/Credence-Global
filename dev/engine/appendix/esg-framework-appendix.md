# ESG Risk Assessment Framework (Applicable to Global Fixed Income Markets) — Appendix

> Appendix to `esg-framework.md` — version tracks the parent document; reference
> material (worked examples, derivations, historical validation) moved here in
> the 2026-07 restructure. Read on demand.

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
