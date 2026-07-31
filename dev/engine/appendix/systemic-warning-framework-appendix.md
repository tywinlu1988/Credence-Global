# Systemic Warning Framework — Signal Aggregation Algorithm + Thermometer + Historical Backtests — Appendix

> Appendix to `systemic-warning-framework.md` — version tracks the parent document; reference
> material (worked examples, derivations, historical validation) moved here in
> the 2026-07 restructure. Read on demand.

---

## 5. Historical Backtest 1: GFC 2008 (Pre-Lehman)

### 5.1 Scenario Background

**Time Window:** Q3 2008 (approximately 1 month before Lehman Brothers bankruptcy)
**Actual Event Date:** September 15, 2008 (Lehman Brothers filed for Chapter 11 bankruptcy protection)
**Market Environment at the Time:** After the subprime mortgage crisis emerged in 2007, the market experienced a period of relative calm in early-to-mid 2008. Bear Stearns had been rescued by JPMorgan in March 2008. The AAA-rated MBS/CDO ratings bubble was still largely intact. The market broadly believed that systemically important institutions would be bailed out.

### 5.2 Industry Signal State at the Time (19-Industry GICS Composition)

Estimated signal states for the 19 industries in Q3 2008 (pre-Lehman), reconstructed from public historical data:

| Industry | Track A Score (Est.) | Base | Outlook | Track B | Risk Score | Basis |
|----------|---------------------|------|---------|---------|------------|-------|
| **Financials (Banks/Insurance)** | 3.0-4.0 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | Bear Stearns rescued in March; Lehman/AIG/Merrill under severe stress; bank CDS spreads already blown out |
| Sovereigns & GSEs | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | US Treasuries as safe haven; no sovereign stress pre-crisis |
| Energy (Oil & Gas) | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | Oil peaked at $147 in July 2008, then collapsed; demand destruction beginning |
| Metals & Mining | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | Copper/iron ore peaked in 2008 H1 and rolled over |
| Construction Materials | 4.0-5.0 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | US housing collapse already underway |
| Automobiles | 3.0-4.0 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | Detroit 3 in crisis (pre-bailout); sales collapsing |
| Transportation | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | Baltic Dry Index crashed mid-2008 |
| Chemicals | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Demand weakening but feedstock costs falling in parallel |
| Capital Goods | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Order books still at cycle top |
| Commercial Services | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Staffing/services beginning to soften |
| Technology Hardware (Semis) | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Cycle turn starting; balance sheets still solid |
| Consumer Durables | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Housing-linked durables weakening |
| Retail | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Discretionary spending weakening |
| Consumer Staples | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Software & Services | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Resilient |
| Biotech & Pharma | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Healthcare Equipment | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Stable |
| Utilities (Regulated) | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Telecommunications | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Stable |

### 5.3 SRI Calculation

Weights use the §4.1 illustrative outstanding shares with the **25% single-industry cap** applied (Financials' normalized 33.9% is capped at 25%; the excess is redistributed pro-rata, factor ≈ 1.135):

```
Weighted contributions (risk score × capped weight):
  Financials            3.0 × 25.00% = 0.750
  Energy                2.0 ×  8.40% = 0.168
  Transportation        2.0 ×  4.56% = 0.091
  Automobiles           3.0 ×  2.89% = 0.087
  Capital Goods         1.0 ×  5.04% = 0.050
  Technology Hardware   1.0 ×  4.91% = 0.049
  Metals & Mining       2.0 ×  2.05% = 0.041
  Chemicals             1.0 ×  3.68% = 0.037
  Construction Materials 3.0 ×  0.94% = 0.028
  Consumer Durables     1.5 ×  0.91% = 0.014
  Retail                1.5 ×  0.91% = 0.014
  Commercial Services   1.0 ×  0.91% = 0.009
  (Sovereigns, Utilities, Telecom, Staples, Software, Biotech, HealthEquip: 0)

SRI ≈ 1.29  →  🟠 Alert (1.0 - 1.8)
```

### 5.4 Could It Provide Early Warning?

| Assessment Dimension | Conclusion |
|---------------------|-----------|
| **Did SRI enter 🟠?** | **Yes.** SRI ≈ 1.29, crossing the 1.0 alert threshold about one month before Lehman |
| **Main risk contribution** | Financials alone contributes 0.75 (58% of SRI) — consistent with the crisis's actual epicenter. Commodity-cyclical industries (Energy, Metals, Transportation) and housing-linked industries (Construction Materials, Automobiles) form the secondary belt |
| **Contrast with the legacy 13-industry composition** | Under the retired composition, financial risk entered only through an indirect LGFV/sub-sovereign mapping (1 point × 25%), yielding SRI ≈ 0.70 (🟡). The 19-industry GICS composition makes Financials a first-class 25%-weighted risk source at risk score 3, and the framework would have been at **🟠 Alert** — a materially stronger and historically more accurate signal |
| **Framework Limitations** | Even at 🟠, the SRI cannot predict confidence-collapse events themselves; it identifies that risk has accumulated to alert level. The thermometer downgrade condition (§4.3) would also be checked here: SRI is elevated with a single dominant contributor, but Energy/Metals/Automobiles/Construction are simultaneously stressed, so the downgrade does not apply |

### 5.5 Backtest Conclusion

| Backtest Conclusion | Specific Description |
|--------------------|---------------------|
| **Warning Effective** | SRI entered 🟠 Alert range about one month before Lehman, with the risk contribution concentrated in the sector that actually failed |
| **Actionable Level** | At 🟠, the framework prescribes portfolio-wide stress testing and exposure-reduction review — an appropriate response to what became the GFC |
| **Escalation Cross-Check** | By September 2008, Market Panic + High Leverage + Information Asymmetry were all triggering (3+ factors → 3.0x synergy per contagion-matrix §6.3), which would escalate the contagion matrix to systemic tipping-point — corroborating the 🟠 reading |
| **Overall Assessment** | Under the 19-industry GICS composition, the framework's GFC backtest is strong: alert-level warning with the correct epicenter identified, without relying on hindsight-only China-market mappings |

---


---

## 6. Historical Backtest 2: Eurozone Sovereign Debt Crisis 2011-12

### 6.1 Scenario Background

**Time Window:** Q3 2011 (peak of the Eurozone sovereign debt crisis — Greek escalation)
**Actual Event Time:** Summer/Fall 2011 — Greek bond yields exceeded 50%, CDS spreads peaked, contagion spread to Italy, Spain, Portugal, and Ireland (PIIGS); ECB launched SMP interventions in August; Dexia required rescue in October; Greek PSI agreed in October.
**Market Environment at the Time:** The aftermath of the 2008 GFC was still unfolding. Greece had revealed a much larger deficit than previously reported in late 2009. By 2011 the crisis had evolved into a full sovereign debt crisis threatening eurozone integrity. The bank-sovereign "doom loop" was in full effect — banks held large amounts of sovereign debt, while struggling sovereigns needed healthy banks.

### 6.2 Industry Signal State at the Time (19-Industry GICS Composition)

Estimated signal states for the 19 industries in Q3 2011, reconstructed from public historical data:

| Industry | Track A Score (Est.) | Base | Outlook | Track B | Risk Score | Basis |
|----------|---------------------|------|---------|---------|------------|-------|
| **Sovereigns & GSEs** | 3.0-4.0 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | The epicenter: Greek yields >50%, PIIGS contagion, CDS at peaks |
| **Financials (Banks/Insurance)** | 3.5-4.5 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | The other end of the doom loop: European banks holding peripheral sovereign debt (Dexia failed in October) |
| Utilities (Regulated) | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | State-owned utilities repriced with sovereigns |
| Energy (Oil & Gas) | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Resource-fiscal risk, demand slowdown |
| Construction Materials | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | Periphery infrastructure freeze (Spain/Ireland bust aftermath) |
| Transportation | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Trade/freight slowing |
| Metals & Mining | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Global slowdown |
| Capital Goods | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Capex freeze |
| Automobiles | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Weak European sales |
| Consumer Durables | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Austerity-hit consumer |
| Retail | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Austerity |
| Telecommunications | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Some sovereign-linked operators |
| Chemicals | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Export-linked softness |
| Commercial Services | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | — |
| Technology Hardware (Semis) | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | US/global tech unaffected |
| Software & Services | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | — |
| Consumer Staples | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Biotech & Pharma | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Healthcare Equipment | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | — |

### 6.3 SRI Calculation

Weights as in §5.3 (§4.1 illustrative shares, 25% single-industry cap applied):

```
Weighted contributions (risk score × capped weight):
  Sovereigns & GSEs     3.0 × 19.49% = 0.585
  Financials            3.0 × 25.00% = 0.750
  Utilities             2.0 ×  7.48% = 0.150
  Energy                1.5 ×  8.40% = 0.126
  Capital Goods         1.5 ×  5.04% = 0.076
  Transportation        1.5 ×  4.56% = 0.068
  Telecommunications    1.0 ×  4.24% = 0.042
  Automobiles           1.5 ×  2.89% = 0.043
  Chemicals             1.0 ×  3.68% = 0.037
  Metals & Mining       1.5 ×  2.05% = 0.031
  Construction Materials 2.0 ×  0.94% = 0.019
  Consumer Durables     1.5 ×  0.91% = 0.014
  Retail                1.5 ×  0.91% = 0.014
  Commercial Services   1.0 ×  0.91% = 0.009

SRI ≈ 1.96  →  🔴 Danger (>= 1.8)
```

### 6.4 Could It Provide Early Warning?

| Assessment Dimension | Conclusion |
|---------------------|-----------|
| **Did SRI enter 🔴?** | **Yes.** SRI ≈ 1.96 crosses the 1.8 danger threshold in Q3 2011 — the window of ECB SMP interventions (August), Dexia's failure (October), and the Greek PSI (October) |
| **Doom-loop capture** | Sovereigns & GSEs (0.585) and Financials (0.750) are both first-class inputs at risk score 3 — the framework captures the bank-sovereign doom loop **directly**, rather than through an indirect proxy mapping. The two largest contributions sit exactly at the two ends of the loop |
| **Contrast with the legacy composition** | The retired 13-industry composition had no sovereign/banking industry at all and yielded SRI ≈ 1.23 (🟠) via indirect sub-sovereign mapping. The 19-industry composition reads the same event at 🔴 — consistent with how close the eurozone came to breakup |
| **§4.3 downgrade check** | The thermometer downgrade condition (single dominant contributor, all else 🟢) does not apply: Utilities, Construction, Capital Goods, Automobiles, and the consumer belt are simultaneously stressed |
| **Framework Limitations** | 🔴 marks systemic severity, not timing. The framework cannot forecast the political decisions (SMP, EFSF/ESM, OMT in 2012) that ultimately contained the crisis |

### 6.5 Backtest Conclusion

| Backtest Conclusion | Specific Description |
|--------------------|---------------------|
| **Danger-level warning effective** | SRI entered 🔴 Danger during the crisis peak, identifying systemic severity in real time |
| **First-class sovereign channel validated** | The sovereign-bank nexus — the matrix's strongest link (Financials ↔ Sovereigns, intensity 5) — is exercised end-to-end: both ends appear as top-weighted risk sources |
| **Escalation cross-check** | Regulatory Vacuum (ambiguous rescue stance through summer 2011) + Market Panic were simultaneously active; per contagion-matrix §6.3, the 1.5x synergy multiplies affected link intensities — corroborating the 🔴 reading |
| **Overall Assessment** | The framework reads the Eurozone crisis at the correct severity tier with the correct mechanism. It would have prescribed emergency position review and hedge activation (🔴 actions) during the window when those actions were most valuable |

---


---

## 7. Historical Backtest 3: Exogenous Synchronous Shock (Case: COVID-19, Q1 2020)

> **Purpose of this case:** This backtest is NOT about pandemic prediction. It calibrates
> the **boundary of the SRI framework**: what kind of systemic event the framework can be
> forward-looking about (endogenous credit accumulation — §5, §6) versus what it can only
> be reactive about (exogenous synchronous non-credit shocks — this case). It also validates
> the thermometer's real-time accuracy once such a shock has occurred.

### 7.1 Scenario Background

**Time Window:** February-March 2020 (global COVID-19 pandemic outbreak)
**Actual Impact Time:** January 30, 2020 WHO declared a Public Health Emergency of International Concern; March 11, 2020 declared a global pandemic
**Market Environment at the Time:** An unprecedented public health crisis caused simultaneous shocks to all industries. Unlike the GFC or Eurozone crisis, COVID-19 was an **exogenous, synchronous, non-credit** shock — no industry balance sheet showed it coming.

### 7.2 Industry Signal State at the Time (19-Industry GICS Composition)

Estimated signal states for the 19 industries in Q1 2020, reconstructed from public historical data:

| Industry | Track A Score (Est.) | Base | Outlook | Track B | Risk Score | Basis |
|----------|---------------------|------|---------|---------|------------|-------|
| Transportation | 2.0-3.0 (B/B+) | 3 | Negative | 🔴 (Crisis) | **3.0** | Passenger traffic collapsed; airlines burning cash daily |
| Automobiles | 3.0-4.0 (B+/BB) | 2 | Negative | 🔴 (Crisis) | **3.0** | Factories shut; sales down 80%+ |
| Retail | 2.5-3.5 (B/B+) | 2 | Negative | 🔴 (Crisis) | **3.0** | Zero foot traffic at physical stores |
| Consumer Durables | 3.0-4.0 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **3.0** | Stores closed; big-ticket purchases deferred |
| Energy (Oil & Gas) | 3.0-4.0 (B+/BB) | 2 | Negative | 🔴 (Crisis) | **3.0** | Demand collapse; WTI briefly negative in April |
| Capital Goods | 3.5-4.5 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **2.5** | Production paused, deliveries delayed |
| Metals & Mining | 3.5-4.5 (B+/BB) | 2 | Negative | 🟠 (Abnormal) | **2.5** | Demand cliff |
| Construction Materials | 4.0-5.0 (B+/BB+) | 2 | Negative | 🟡 (Watch) | **2.5** | Sites paused |
| Commercial Services | 4.0-5.0 (B+/BB+) | 2 | Negative | 🟡 (Watch) | 2.0 | Offices closed |
| **Financials (Banks/Insurance)** | 4.0-5.0 (B+/BB) | 2 | Stable | 🟡 (Watch) | **2.5** | Spreads blew out, but central banks backstopped forcefully by end-March |
| Chemicals | 4.5-5.5 (BB+/BBB-) | 2 | Negative | 🟢 (Calm) | 1.5 | Demand weakening; feedstock costs falling |
| Technology Hardware (Semis) | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | 1.5 | Supply-chain disruption; WFH partly offsets |
| Sovereigns & GSEs | 5.5-6.0 (BBB+) | 1 | Stable | 🟢 (Calm) | 1.0 | Fiscal response expanding; safe-haven demand |
| Software & Services | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | WFH beneficiary |
| Biotech & Pharma | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Vaccine race |
| Healthcare Equipment | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Surge demand for medical supplies |
| Consumer Staples | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Pantry stocking |
| Utilities (Regulated) | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Telecommunications | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Traffic surge |

### 7.3 SRI Calculation

Weights as in §5.3 (§4.1 illustrative shares, 25% single-industry cap applied):

```
Weighted contributions (risk score × capped weight):
  Financials            2.5 × 25.00% = 0.625
  Energy                3.0 ×  8.40% = 0.252
  Sovereigns & GSEs     1.0 × 19.49% = 0.195
  Transportation        3.0 ×  4.56% = 0.137
  Capital Goods         2.5 ×  5.04% = 0.126
  Automobiles           3.0 ×  2.89% = 0.087
  Technology Hardware   1.5 ×  4.91% = 0.074
  Chemicals             1.5 ×  3.68% = 0.055
  Metals & Mining       2.5 ×  2.05% = 0.051
  Construction Materials 2.5 ×  0.94% = 0.024
  Consumer Durables     3.0 ×  0.91% = 0.027
  Retail                3.0 ×  0.91% = 0.027
  Commercial Services   2.0 ×  0.91% = 0.018

SRI ≈ 1.70  →  🟠 Alert (1.0 - 1.8)
```

### 7.4 Known Unknown vs Unknown Unknown: What This Case Calibrates

| Assessment Dimension | Analysis |
|---------------------|---------|
| **Nature of the shock** | A "known unknown" in taxonomy but an un-forecastable event in practice — public health experts had long warned about pandemic risk, yet no Track A/B signal in January 2020 showed it |
| **Could the SRI provide pre-event warning?** | **No — and it must not claim to.** The framework reads credit-state signals; an exogenous synchronous non-credit shock has no accumulation phase in those signals. Any framework claiming to predict such events is overfitting hindsight |
| **Could the SRI reflect the impact?** | **Yes, in real time.** Once the shock landed, SRI rose to ≈ 1.70 (🟠) — high but below 🔴, correctly reflecting that unprecedented central-bank and fiscal response prevented the credit spiral from reaching GFC depth |
| **Where does black-swan response live instead?** | Not in the SRI. Exogenous-shock response belongs to (a) the contagion escalation-factor layer (event-driven triggers, contagion-matrix §6), and (b) the portfolio stress test path (WP-RO-04) — the engine's "response protocol" — while the SRI's job is to report severity honestly after impact |
| **Reactive vs forward-looking** | GFC (§5) and Eurozone (§6) are endogenous transmission shocks — the SRI is forward-looking there. COVID is the boundary case proving the framework knows when it is only a seismograph, not a crystal ball |

### 7.5 Backtest Conclusion

| Backtest Conclusion | Specific Description |
|--------------------|---------------------|
| **Boundary calibrated** | The framework correctly does NOT claim pre-event prediction for exogenous synchronous shocks — this case exists to document that limit, not to showcase accuracy |
| **Reactive accuracy validated** | Post-impact, the thermometer reached 🟠 1.70 with contributions spanning the actually-hit sectors (transport, autos, retail, energy) and zero contribution from genuinely resilient sectors — a correct real-time map of the shock |
| **Complementarity documented** | Black-swan response is assigned to the escalation-factor layer and WP-RO-04 stress testing; the SRI stays an honest seismograph |
| **Overall Assessment** | Three backtests now cover the full taxonomy: endogenous credit accumulation (GFC, 🟠 forward) → sovereign-bank nexus (Eurozone, 🔴 forward) → exogenous synchronous shock (COVID, 🟠 reactive). The framework's claims match its demonstrated capabilities |

---


---

## 8. Current Period Calculation: Scenario-Based SRI Example

### 8.1 Scenario: Hypothetical 2026 Market State (Illustrative)

This section shows how the SRI is calculated under a **hypothetical** 2026 market state: higher-for-longer rates pressuring commercial real estate and rate-sensitive consumption, elevated sovereign deficits, and a two-speed technology sector (AI capex boom vs everything else). **The signal states below are illustrative, not a real-time reading.**

| Industry | Track A Score (Est.) | Base | Outlook | Track B | Risk Score | Rationale |
|----------|---------------------|------|---------|---------|------------|-----------|
| **Financials (Banks/Insurance)** | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | Regional-bank CRE exposure stress; NIM normalization |
| **Sovereigns & GSEs** | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Elevated deficits; term premium rising |
| Energy (Oil & Gas) | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Mid-cycle |
| Construction Materials | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | CRE/housing slowdown |
| Capital Goods | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Reshoring capex supportive |
| Transportation | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Freight stable |
| Chemicals | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | — |
| Metals & Mining | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | Energy-transition metals firm |
| Automobiles | 5.0-6.0 (BBB) | 1 | Negative | 🟡 (Watch) | **2.0** | EV price war + rate-sensitive demand |
| Consumer Durables | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | Rate-sensitive big-ticket |
| Retail | 5.0-6.0 (BBB) | 1 | Negative | 🟢 (Calm) | 1.5 | K-shaped consumer |
| Commercial Services | 5.0-6.0 (BBB) | 1 | Stable | 🟢 (Calm) | 1.0 | — |
| Technology Hardware (Semis) | 7.0+ (A) | 0 | Positive | 🟢 (Calm) | 0 | AI capex boom |
| Software & Services | 7.0+ (A) | 0 | Positive | 🟢 (Calm) | 0 | AI tailwind |
| Utilities (Regulated) | 7.0+ (A) | 0 | Positive | 🟢 (Calm) | 0 | Datacenter demand boom |
| Telecommunications | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | — |
| Consumer Staples | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | Defensive |
| Biotech & Pharma | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | — |
| Healthcare Equipment | 7.0+ (A) | 0 | Stable | 🟢 (Calm) | 0 | — |

### 8.2 SRI Calculation

```
Weighted contributions (risk score × capped weight, §4.1 illustrative):
  Financials            2.0 × 25.00% = 0.500
  Sovereigns & GSEs     1.5 × 19.49% = 0.292
  Energy                1.0 ×  8.40% = 0.084
  Capital Goods         1.0 ×  5.04% = 0.050
  Transportation        1.0 ×  4.56% = 0.046
  Chemicals             1.0 ×  3.68% = 0.037
  Automobiles           2.0 ×  2.89% = 0.058
  Metals & Mining       1.0 ×  2.05% = 0.021
  Construction Materials 2.0 ×  0.94% = 0.019
  Consumer Durables     1.5 ×  0.91% = 0.014
  Retail                1.5 ×  0.91% = 0.014
  Commercial Services   1.0 ×  0.91% = 0.009

SRI ≈ 1.14  →  🟠 Alert (1.0 - 1.8)
```

### 8.3 SRI Interpretation

| Dimension | Analysis |
|-----------|---------|
| **Reading** | SRI ≈ 1.14 (🟠 Alert): elevated but far from crisis. The two dominant contributors are Financials (0.500) and Sovereigns (0.292) — a rates/fiscal-driven stress pattern, not a broad credit event |
| **Two-speed structure** | Technology, software, and utilities carry zero risk contribution (AI capex boom), while the rate-sensitive belt (construction, autos, durables, retail) forms the secondary layer. The thermometer sees the divergence, not just the average |
| **§4.3 downgrade check** | Would the thermometer downgrade to 🟡? No: the stress is shared by 8+ industries, not a single dominant contributor |
| **Prescribed actions (🟠)** | Re-run concentration (WP-RO-01) and contagion (WP-RO-02) for the Financials/Sovereigns-linked exposures; portfolio-wide stress test (WP-RO-04); review rate-sensitive belt sizing |

### 8.4 How to Use This Example

This scenario is a **template for computing the SRI on live inputs**: replace the illustrative Track A / outlook / Track B values with current assessments (Track A from the industry pyramid, outlook from `outlook-monitoring-framework.md`, Track B from market pricing signals), replace the §4.1 illustrative weights with live benchmark sector weights, and the same arithmetic yields the current SRI. The coded engine (`src/sri_calculator.py` via WP-RO-03) executes exactly this calculation; the orchestrator (`src/pipeline.py`) accepts the inputs as plain dicts/YAML.

---


---

## 9. Threshold Sensitivity Analysis

### 9.1 Impact of Thresholds on SRI Results

The core parameters of the SRI (threshold settings) have a decisive impact on the final temperature and action recommendations. The following sensitivity analysis shows how parameter changes alter SRI readings:

**Scenario A: Baseline Thresholds (Current Version)**

| Track A Range | Base Score | Negative Outlook | Track B 🟡 | Track B 🟠 | Track B 🔴 |
|--------------|-----------|-----------------|-----------|-----------|-----------|
| > 6.0 | 0 | +0.5 | +0.5 | +1.0 | +1.5 |
| 5.0-6.0 | 1 | +0.5 | +0.5 | +1.0 | +1.5 |
| 3.0-5.0 | 2 | +0.5 | +0.5 | +1.0 | +1.5 |
| < 3.0 | 3 | +0.5 | +0.5 | +1.0 | +1.5 |

**Scenario B: Pessimistic Thresholds (More Sensitive)**

| Track A Range | Base Score | Negative Outlook | Track B 🟡 | Track B 🟠 | Track B 🔴 |
|--------------|-----------|-----------------|-----------|-----------|-----------|
| > 6.0 | 0 | +1.0 | +1.0 | +1.5 | +2.0 |
| 5.0-6.0 | 1 | +1.0 | +1.0 | +1.5 | +2.0 |
| 3.0-5.0 | 3 | +1.0 | +1.0 | +1.5 | +2.0 |
| < 3.0 | 4 | Not stacked | Not stacked | Not stacked | Not stacked |

Under pessimistic thresholds, SRI calculations are more aggressive — the negative outlook penalty is doubled, Track B penalties are raised one level each (Watch +1.0, Abnormal +1.5, Crisis +2.0), and the speculative-grade base score is raised from 2 to 3. This version is suitable for conservative investors or periods of high systemic risk.

**Scenario C: Optimistic Thresholds (Less Sensitive)**

| Track A Range | Base Score | Negative Outlook | Track B 🟡 | Track B 🟠 | Track B 🔴 |
|--------------|-----------|-----------------|-----------|-----------|-----------|
| > 6.0 | 0 | No penalty | No penalty | No penalty | No penalty |
| 5.0-6.0 | 1 | +0.5 | +0.5 | +0.5 | +0.5 |
| 3.0-5.0 | 2 | +0.5 | +0.5 | +0.5 | +0.5 |
| < 3.0 | 3 | +0.5 | +0.5 | +0.5 | +0.5 |

Under optimistic thresholds, negative outlook and Track B signals have no penalty when Track A > 6.0 (assuming negative signals for high-grade industries are noise), and Track B penalties in other ranges are unified to half a notch. This version is suitable for high-risk-appetite investors.

### 9.2 SRI Comparison Across Three Scenarios (Scenario Example)

| Parameter Version | Calculation Process | SRI | Thermometer |
|-----------------|-------------------|-----|-------------|
| **A. Baseline (Current)** | As calculated in §8.3 | 0.57 | 🟡 Watch |
| **B. Pessimistic** | Solar: 3+1+1=5→3; NEV: 1+1+1=3; Sub-sovereign: 1+0+1=2; Retail: 1+1+1=3 | 0.76 | 🟡 Watch (upper bound) |
| **C. Optimistic** | Solar: 2+0.5+0=2.5; NEV: 1+0.5+0=1.5; Sub-sovereign: 1+0+0=1; Retail: 1+0.5+0=1.5 | 0.40 | 🟢 Normal |

**Analysis:**
- Under the optimistic version, SRI falls to 0.40, landing in 🟢 range
- Under the pessimistic version, SRI rises to 0.76, still in 🟡 range but near the upper bound
- None of the three versions reach 🟠 Alert (1.0) — indicating that parameter variation does not cause over- or under-warning given the current signal distribution

### 9.3 Threshold Applicability Recommendations

| Market Environment | Recommended Threshold | Rationale |
|-------------------|---------------------|-----------|
| Normal market (credit spreads stable, no systemic shock) | Baseline (A) | Balanced sensitivity and specificity |
| Credit tightening cycle (credit spreads widening, high cancellation rates) | Pessimistic (B) | Increase warning sensitivity, prepare early |
| Rating bubble burst period (mass AAA downgrades) | Pessimistic (B) | Increase vigilance during concentrated rating adjustment window |
| Loose monetary + asset shortage (credit spreads compressing) | Optimistic (C) | Avoid over-warning in high-liquidity environments |
| Contagion matrix escalation factor triggered (panic/high leverage) | Pessimistic (B) | Escalation factors already triggered, raise warning level |

---


---

## 11. Limitations Statement

### 11.1 Framework Inherent Limitations

| Limitation | Specific Description | Mitigation |
|-----------|---------------------|------------|
| **1. Lags behind exogenous shocks** | The SRI framework is based on industry fundamental signals and cannot pre-warn exogenous, non-credit shocks (e.g., pandemics, natural disasters, geopolitical conflicts) | For known external risks (e.g., trade frictions, regulatory policy changes), advance reflection in outlook assessment can partially mitigate the lag |
| **2. Industry granularity** | The framework aggregates at the level of 19 GICS-based industries; intra-industry divergence (e.g., IG vs HY issuers within one sector) is averaged out | Pair SRI with single-issuer Track A analysis for issuer-level differentiation |
| **3. Static weight risk** | Industry weights based on credit bond outstanding share and contagion coefficients are fixed parameters that cannot reflect short-term market structural changes | Establish quarterly weight update mechanism; update immediately when an industry's credit bond outstanding changes > 20% |
| **4. Parameter subjectivity** | Industry risk score thresholds (3.0/5.0/6.0), penalty factors (0.5), and thermometer thresholds (0.5/1.0/1.8) are based on subjective judgment and historical calibration, not statistical optimization | Provide pessimistic/baseline/optimistic parameter versions for user selection based on risk preference; conduct annual backtest calibration |
| **5. Linear weighting limitation** | SRI uses linear weighted aggregation and cannot capture non-linear interaction effects between industries (e.g., industry A in trouble → contagion to B → feedback loop strengthening A) | Partially compensated through thermometer and contagion matrix escalation factor linkage (§3.4) — automatically activate escalation factor synergy when SRI ≥ 1.0 |
| **6. Signal quality dependency** | The calculation quality of SRI depends on the accuracy of input Track A scores and Track B signals. If these foundational signals are biased (e.g., inflated ratings), SRI will also be distorted | Reference the engine's "pseudo-high rating" identification mechanism as auxiliary validation of SRI quality |

### 11.2 Usage Restrictions

| Restriction | Description |
|-------------|-------------|
| **Not Investment Advice** | The SRI provides systemic risk level assessment and does not constitute specific buy/sell/hold investment advice |
| **Not a Regulatory Metric** | This framework has not been reviewed or certified by any regulatory authority and cannot be used for regulatory capital calculation or compliance reporting |
| **Limited Historical Samples** | The framework has only been validated through 3 historical events (2020 COVID-19, 2008 GFC, 2011-12 Eurozone crisis) for backtesting, with limited statistical significance. As more credit events accumulate, the framework requires continuous recalibration |
| **Market-Specific Parameters** | The framework's thresholds, weights, and contagion coefficients are based on specific market data and characteristics. Direct application to other markets requires comprehensive parameter reset |

### 11.3 Version Evolution Roadmap

| Version | Planned Content |
|---------|----------------|
| v0.0.1 | Initial version: Basic aggregation algorithm + thermometer + 3 historical backtests + current calculation |
| v0.0.1 | System intelligence layer integration: complete M4 portfolio risk control system with contagion matrix/concentration framework, unified engine version |
| v0.0.1 | Engine-level integration release: cross-CLI entry (AGENTS.md) · four-segment chain product contract · executable orchestrator · dimension registry |
| v0.0.1 | Gate reinforcement and promotion mechanism (no change to framework/thresholds): .gitattributes mandatory LF · CI launch · promote.py promotion script |
| v0.0.1 | Contagion matrix connected to encoding engine; §2.3.1 Contagion Coefficient Table and §4 weight example aligned with matrix truth values (ranking unchanged) |
| v0.0.1 | Reliability iteration: consistency audit and gate expansion (framework includes §2.3.2/§4.1 data center consolidation note) |
| v0.0.1 (Current) | Outlook monitoring activation wiring (no change to framework/thresholds) |
| v0.0.1 | Add SRI time series tracking (plot SRI historical curves, identify trends and turning points) |
| v0.0.1 | Introduce real-time SRI and contagion matrix escalation factor linkage (automatically adjust SRI reading when escalation factors trigger) |
| v0.0.1 | Add portfolio-level SRI calculation (based on actual portfolio holding weights replacing industry weights), achieving true portfolio systemic risk assessment |
| v0.0.1 | Introduce SRI stress testing (input hypothetical shock → output post-stress SRI thermometer), deeply integrated with M4 portfolio risk control |
| v1.0.0 | Stable release: all backtest validations passed + at least 6 months of real-time operational data validation |

---

---

### Appendix B: SRI Comparison Summary Across Three Backtests

| Backtest Scenario | Time Window | SRI Estimate | Thermometer | Framework Performance |
|------------------|------------|-------------|-------------|----------------------|
| Pre-Lehman (GFC 2008) | Q3 2008 | 0.70 | 🟡 Watch | Identified risk accumulation 1 month ahead — reasonable |
| Eurozone Sovereign Crisis | Q3 2011 | 1.23 | 🟠 Alert | Crossed alert threshold, identified systemic risk — good |
| COVID-19 Shock | Q1 2020 | 1.15 | 🟠 Alert | Real-time crisis severity reflection — effective but could not pre-warn |
| Scenario Example | Current | 0.57 | 🟡 Watch | Sub-sovereign weight-driven moderate risk — reasonable |

### Appendix C: Quick Calculation Table

Use the following table to quickly estimate SRI for any combination of 19 industry signals:

```
SRI Estimate = (A×3 + B×2 + C×1 + D×0) / 13 × Weight Adjustment Factor

Where:
  A = Number of high-risk industries (risk score ≥ 3, including veto-forced 3)
  B = Number of medium-high risk industries (risk score 2.0-2.9)
  C = Number of medium risk industries (risk score 1.0-1.9)
  D = Number of low-risk industries (risk score < 1.0)
  
  Weight Adjustment Factor ≈ 1.3 (considering the dominance effect of heavy-weight 
  industries like sub-sovereign/LGFV, default weighted factor is 1.3)
```

**Quick Reference:**

| A (High Risk) | B (Med-High) | C (Medium) | D (Low Risk) | Weighted SRI (Est.) | Thermometer |
|--------------|-------------|-----------|-------------|--------------------|-------------|
| 0 | 0 | 1 | 12 | 0.10 | 🟢 Normal |
| 0 | 1 | 2 | 10 | 0.31 | 🟢 Normal |
| 0 | 2 | 2 | 9 | 0.51 | 🟡 Watch |
| 1 | 0 | 3 | 9 | 0.58 | 🟡 Watch |
| 1 | 2 | 2 | 8 | 0.95 | 🟡 Watch (near Alert) |
| 1 | 3 | 3 | 6 | 1.38 | 🟠 Alert |
| 2 | 2 | 3 | 6 | 1.55 | 🟠 Alert |
| 3 | 3 | 2 | 5 | 2.15 | 🔴 Danger |
| 4 | 4 | 3 | 2 | 3.02 | 🔴 Danger |
| 7 | 3 | 2 | 1 | 4.10 | 🔴 Danger (Extreme) |
