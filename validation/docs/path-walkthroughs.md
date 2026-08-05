# Path Walkthroughs — 16/16 Active Paths

**Date**: 2026-07-31 · **Engine Version**: v0.3.1
**Nature**: Test execution record (validation evidence archive — not a project deliverable; never enters `version/` snapshots)

---

## What This Is

An end-to-end walkthrough matrix for all **16 active work paths**. Each entry traces one
concrete scenario through the four-stage chain (① intake → ② analysis → ③ report → ④ QA)
exactly as registered in `dev/engine/work-path-registry.md` and contracted in
`dev/engine/pipeline-contract.md`.

**Evidence classes** (honest labeling, per this archive's conventions):

- **Executed** — a real end-to-end run exists as recorded evidence (linked).
- **Coded-engine verified** — the path's analysis stage is executed in code
  (`src/` engines) and covered by the pytest engine suites + the executable-manifest
  integration tests.
- **Structural** — walkthrough derived from the registry entry, path playbook, and
  pipeline contract; the four-stage plan is machine-verified (integration tests assert
  every active path yields a valid S1→S4 plan), but no full human-readable run is archived.

## Coverage Summary

| Path | Role | Depth | Templates | Evidence |
|---|---|---|---|---|
| WP-CS-01 | credit-selector | L2 | Type 1 + Type 6 | ✅ Executed (Siemens) |
| WP-CS-02 | credit-selector | special | Type 8 + Type 9 | Structural |
| WP-PM-01 | portfolio-manager | L2 | Type 5 | Structural |
| WP-PM-02 | portfolio-manager | L2 | Type 2 | Structural |
| WP-AD-01 | advisor | special | Type 16 | ✅ Executed (Schneider) |
| WP-TR-01 | trader | L0 | L0-spec (no HTML) | ✅ Executed (Schneider) |
| WP-RO-01 | risk-officer | special | Type 14 | Coded-engine verified |
| WP-RO-02 | risk-officer | special | Type 13 | Coded-engine verified |
| WP-RO-03 | risk-officer | special | Type 15 | Coded-engine verified |
| WP-RO-04 | risk-officer | special | Type 11 | Structural |
| WP-II-01 | individual-investor | special | Type 17 | Structural |
| WP-X-01 | meta | special | Type 3 | ✅ Executed (Yongmei/Ziguang cases) |
| WP-X-02 | meta | L2 | Type 4 | Structural |
| WP-X-03 | meta | special | Type 7 | Structural |
| WP-X-04 | meta | special | Type 10 | Structural |
| WP-X-05 | meta | special | Type 18 | Coded-engine verified |

---

## 1. WP-CS-01 — Credit Selector Single-Issuer Rating (credit-selector · L2)

**Scenario**: "Rate Siemens AG for a 5-year hold."

- **① Intake** — Router matches single-issuer rating intent → Path Sheet: depth L2,
  templates Type 1 + Type 6, gates Signal Density / Veto / Cross-Validation.
- **② Analysis** — `industry-framework.md`: paradigm determination (§3) → D1-D10 scoring
  (§1) → pyramid layers (§4) → veto check (§5). `mosaic-engine.md`: signal extraction,
  density floors (§4.3), completeness (§5). `dual-track-methodology.md`: Track A/B,
  cross-validation matrix (§4), 18-notch rating mapping (§6).
- **③ Report** — `template-type1.html` + `template-type6.html` at L2 depth; more than 1
  report → `report-index.html` navigation page auto-generated.
- **④ QA** — Gate-by-gate review + four mandatory checks (density rule, veto ceiling,
  Mode B, single source) → QA Verdict.
- **Evidence**: ✅ **Executed** — Siemens AG full walkthrough
  (`validation/reports/industrial/siemens-walkthrough.md` + 3 rendered reports + index).
  Two further executed runs (Andritz AG unrated, 2026-07; Schneider Electric SE rated,
  2026-08 — timed baseline 1,107s) are retained in the maintainer's local
  isolated-sandbox records (not shipped, per this archive's local-evidence convention).

## 2. WP-CS-02 — Credit Selector Add-On: LGD + External Support (credit-selector · special)

**Scenario**: "The Siemens rating is done — what do we recover if it defaults, and does
external support change the picture?"

- **① Intake** — Router matches recovery/support intent (requires a completed WP-CS-01)
  → Path Sheet: templates Type 8 + Type 9, gates Five-Tier LGD Classification / Support Capacity.
- **② Analysis** — `lgd-recovery-framework.md` §§1-3: five-tier LGD classification,
  collateral valuation, recovery path. `external-support-framework.md` §§1-6: support
  capacity vs willingness, uplift rules.
- **③ Report** — `template-type8.html` (LGD) + `template-type9.html` (support) + report index.
- **④ QA** — LGD tier and support adjustment must cite framework sections; uplift may not
  exceed the §6 rules.
- **Evidence**: Structural (four-stage plan machine-verified).

## 3. WP-PM-01 — Portfolio Manager Investment Dashboard (portfolio-manager · L2)

**Scenario**: "Is this Novartis 2030 bond worth buying on its own merits?"

- **① Intake** — Router matches instrument-level investment intent → Path Sheet: Type 5,
  gates Four-Dimension / Relative Value.
- **② Analysis** — `multi-stakeholder.md` §2.2b Single-Instrument Dashboard (Relative Value
  / Covenant Protection / Liquidity / Event Calendar — not to be conflated with §2.2
  Portfolio Construction); dual-track foundations for relative value; mosaic density rules.
- **③ Report** — `template-type5.html` dashboard at L2.
- **④ QA** — Four-dimension weights from §2.2b only; relative-value claims need citations.
- **Evidence**: Structural.

## 4. WP-PM-02 — PM Comparative Analysis (portfolio-manager · L2)

**Scenario**: "Compare Nestlé vs Unilever — which credit is relatively stronger?"

- **① Intake** — Router matches peer-comparison intent → Path Sheet: Type 2, gates
  Forward-Looking Comparison Method / Comparative Assessment Results.
- **② Analysis** — `dual-track-methodology.md`: parallel Track A/B for both issuers,
  cross-validation. `validation-methodology.md` §4/§4.2: forward-looking comparison and
  differentiation analysis.
- **③ Report** — `template-type2.html` comparison report at L2.
- **④ QA** — Differentiation conclusion must precede any default event (forward-looking);
  both issuers' ratings from the §6 mapping.
- **Evidence**: Structural.

## 5. WP-AD-01 — Advisor Origination Assessment (advisor · special)

**Scenario**: "Can BASF issue a 7-year bond now — at what price, to whom?"

- **① Intake** — Router matches underwriting-feasibility intent (layers on a completed
  WP-CS-01 rating) → Path Sheet: Type 16, gates Issuance Window / Investor Matching /
  Comparable Pricing.
- **② Analysis** — `advisor-origination-framework.md`: three-dimension issuance window
  (§2, market 40% / issuer 35% / demand 25% + refinancing-urgency override), five-segment
  investor matching with ESG overlay (§3), comparable pricing with five-factor adjustment
  and asymmetric range (§4).
- **③ Report** — `template-type16.html` origination report; Go / Conditional / No-Go
  conclusion with sensitivity table (§5).
- **④ QA** — Window grade, demand tier, and pricing range must trace to §§2-4 rules.
- **Evidence**: ✅ **Executed** — Schneider Electric SE origination assessment
  (2026-08 sandbox: Conditional call, Type 16 rendered, QA pass-with-findings);
  maintainer-local sandbox record.

## 6. WP-TR-01 — Trader Market Watch Signal Card (trader · L0)

**Scenario**: "Daily signal card for the Siemens bond — is it flashing red today, and
can I act on it?"

- **① Intake** — Router matches market-watch intent → Path Sheet: L0 depth, L0-spec
  template marker, gates L0 Signal Card / Thermometer / Execution Dimensions /
  Execution Decision Matrix.
- **② Analysis** — `trader-framework.md`: four execution dimensions (§2, 35/25/25/15),
  Track B input mapping (§3), Execution Decision Matrix row selection (§5.2), thermometer
  overlay (§4 — Alert/Danger suspends new longs). Inherits rating + outlook from the most
  recent WP-CS-01; never recalculates.
- **③ Report** — L0 signal card as a structured text block per
  `output-layered-framework.md` §3 (max 3 signals, priority > 30) + thermometer reading +
  one-line execution posture. **No HTML template by design.**
- **④ QA** — Card within 5-second scope; SRI reading from the WP-RO-03 coded run, never
  fabricated; posture is one line.
- **Evidence**: ✅ **Executed** — Schneider Electric SE L0 card (2026-08 sandbox:
  coded SRI 0.23 Normal from the plugin package, Hold posture, data-gap rule honored);
  maintainer-local sandbox record.

## 7. WP-RO-01 — Risk Officer Concentration Assessment (risk-officer · special)

**Scenario**: "Our book is 40% European financials — run the concentration check."

- **① Intake** — Router matches portfolio-concentration intent → Path Sheet: Type 14,
  gates Five-Dimensional Concentration / Threshold System.
- **② Analysis** — **coded engine** `src/concentration_scorer.py` executes
  `concentration-framework.md`: five dimensions (§§2-6), rating adjustment mapping (§7),
  weighted composite (§8).
- **③ Report** — `template-type14.html` concentration dashboard + adjustment recommendations.
- **④ QA** — Scores reproduce from the coded run; thresholds cited from the framework doc.
- **Evidence**: Coded-engine verified (engine pytest suite + executable-manifest
  integration test).

## 8. WP-RO-02 — Risk Officer Cross-Industry Contagion (risk-officer · special)

**Scenario**: "If US semiconductors wobble, what happens to our Asian tech credits?"

- **① Intake** — Router matches contagion intent → Path Sheet: Type 13, gates
  Contagion Matrix / Escalation Factor / Transmission Path.
- **② Analysis** — **coded engine** `src/contagion_engine.py` executes
  `contagion-matrix.md`: 19×19 matrix lookup, cluster identification, escalation factors;
  `contagion-theory.md` §§1-2 for transmission typing.
- **③ Report** — `template-type13.html` contagion path map + adjustment recommendations.
- **④ QA** — Matrix values only from contagion-matrix.md (single source); escalation
  factors applied per the derived tables.
- **Evidence**: Coded-engine verified.

## 9. WP-RO-03 — Risk Officer Systemic Risk Reading (risk-officer · special)

**Scenario**: "Where is the systemic thermometer today?"

- **① Intake** — Router matches market-wide systemic intent → Path Sheet: Type 15, gates
  Signal Aggregation / Four-Level Thermometer.
- **② Analysis** — **coded engine** `src/sri_calculator.py` executes
  `systemic-warning-framework.md`: signal aggregation (§2), four-level thermometer (§3),
  industry weights and contagion coefficients (§4).
- **③ Report** — `template-type15.html` SRI reading + thermometer tier + per-tier mandated
  actions (§3).
- **④ QA** — SRI on the 0-3+ scale (never 0-100); tier boundaries 0.5 / 1.0 / 1.8 exact.
- **Evidence**: Coded-engine verified. Monthly WP-RO-03 readings feed WP-TR-01's overlay.

## 10. WP-RO-04 — Risk Officer Portfolio Stress Test (risk-officer · special)

**Scenario**: "Stress the portfolio: spreads +200bp and two sectors in crisis — what breaks?"

- **① Intake** — Router matches stress-test intent → Path Sheet: Type 11, gates
  Stress Test / Scenario Sensitivity.
- **② Analysis** — `concentration-framework.md` §9 stress-test procedure with §§7-8
  thresholds as stress inputs; `financial-deep-dive.md` §E scenario sensitivity matrix
  (stress effects on the three statements).
- **③ Report** — `template-type11.html` stress report: scenario losses, threshold-jump results.
- **④ QA** — Scenario definitions from §9 only; sensitivity from §E; no invented shocks.
- **Evidence**: Structural.

## 11. WP-II-01 — Individual Investor Decision Support (individual-investor · special)

**Scenario**: "Should I own this bond — and is the issuer's bond-vs-loan financing mix
a warning sign for my holding?"

- **① Intake** — Router matches personal-investment / financing-channel intent → Path
  Sheet: Type 17, gates Channel Comparison / Timing Assessment.
- **② Analysis** — `financing-channel-framework.md`: three-channel comparison (§3,
  six factors), timing assessment (§4, five factors), recommendation structure (§§5-6).
- **③ Report** — `template-type17.html` advisory report: channel comparison + timing
  recommendation in plain language.
- **④ QA** — Recommendation must trace to the six-factor/five-factor rules; suitability
  framing, no return promises.
- **Evidence**: Structural.

## 12. WP-X-01 — Black Swan Backtest Validation (meta · special)

**Scenario**: "Would the framework have flagged Wirecard before the default?"

- **① Intake** — Router matches validation/backtest intent → Path Sheet: Type 3, gates
  Black Swan Back-Testing / Dual-Timepoint.
- **② Analysis** — `validation-methodology.md`: 6-step backtest process (§2), dual-timepoint
  protocol T1/T2 (§3), forward-looking comparison (§4), mosaic completeness in validation (§5).
- **③ Report** — `template-type3.html` validation report: framework conclusion vs actual
  outcome, warning-window length, improvement record.
- **④ QA** — Strict time-point limitation (no ex-post information); external-rating lag
  baseline documented.
- **Evidence**: ✅ **Executed** — Yongmei and Ziguang completed cases recorded in
  `validation-methodology.md` §6; further case archives in `validation/reports/validation/`.

## 13. WP-X-02 — Multi-Role Parallel Assessment (meta · L2)

**Scenario**: "Give me all six roles' views on Siemens in parallel — where do they disagree?"

- **① Intake** — Router matches multi-role intent → Path Sheet: Type 4, gates
  Multi-Role Parallel / Cross-Role Comparison.
- **② Analysis** — `multi-stakeholder.md` §§1-4: six role deep-dives (§2), cross-role
  tension matrix (§3), five-step parallel process (§4); per-role analyses inherit the
  underlying single-role methodologies.
- **③ Report** — `template-type4.html` multi-role score matrix + consensus/divergence report.
- **④ QA** — Divergences resolved per §3.2 rules (e.g., Trader negative vs CS/PM positive
  → delay 5 trading days); no role may invent dimensions.
- **Evidence**: Structural.

## 14. WP-X-03 — Industry Framework Builder (meta · special)

**Scenario**: "Build an analysis framework for a new sector — green hydrogen."

- **① Intake** — Router matches new-industry-framework intent → Path Sheet: Type 7, gates
  Ten-Dimension / Pyramid / Veto.
- **② Analysis** — `industry-framework.md` §§1-5: paradigm assignment for the new industry,
  D1-D10 weight template selection, four-layer pyramid construction, veto conditions;
  `mosaic-engine.md` density rules; `dimension-registry.md` as the pointer index.
- **③ Report** — `template-type7.html` industry framework document (pyramid + D1-D10 scores).
- **④ QA** — New framework must reuse P1-P6 paradigms and D1-D10 vocabulary — no invented
  dimensions (Non-Negotiable #5).
- **Evidence**: Structural.

## 15. WP-X-04 — ESG/Governance Risk Scan (meta · special)

**Scenario**: "Run an ESG and governance red-flag scan on this issuer."

- **① Intake** — Router matches ESG/governance intent → Path Sheet: Type 10, gates ESG /
  Financial Fraud Red Flag Checklist / Earnings Management and Manipulation Signals.
- **② Analysis** — `esg-framework.md` §§2-5: ESG scoring dimensions, risk assessment,
  mapping rules; `governance-fraud-risk.md` §§1-2 + §4: fraud red flags, earnings
  management and manipulation signals.
- **③ Report** — `template-type10.html` ESG risk scan + governance red-flag list.
- **④ QA** — Red flags from the checklists only; ESG scores per §2-5 mapping; fraud
  signals feed the veto check where applicable.
- **Evidence**: Structural.

## 16. WP-X-05 — Outlook & Continuous Monitoring (meta · special)

**Scenario**: "Set outlook monitoring on our 20 holdings — who goes on the watchlist?"

- **① Intake** — Router matches monitoring/outlook intent → Path Sheet: Type 18, gates
  Rating Outlook / Watchlist / Rating Migration Matrices.
- **② Analysis** — **coded engine** `src/outlook_engine.py` executes
  `outlook-monitoring-framework.md`: trigger factors, scoring, watchlist construction,
  migration matrix (§§1-3).
- **③ Report** — `template-type18.html` outlook report: rating outlooks + watchlist +
  migration probabilities.
- **④ QA** — Migration matrix values from the framework doc only; outlook horizon and
  confidence disclosed.
- **Evidence**: Coded-engine verified.

---

## Maintenance

- This matrix is regenerated in substance whenever a path's registry entry changes;
  the integration tests (T11.1-T11.3) enforce that every active path is registered,
  yields a valid four-stage plan, and is named in this document.
- Executed-run evidence is linked where it exists; maintainers running new end-to-end
  validations should link them under the corresponding path and upgrade its evidence class.
