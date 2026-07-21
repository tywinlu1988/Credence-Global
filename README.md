# Credence · Fixed-Income Credit Analysis Engine

> **A methodology-first credit analysis engine for global fixed-income markets** — delivered as **Agent Skills** (`SKILL.md`), installable into Claude Code, Codex, Cursor, Gemini, and OpenCode. Built for credit professionals who need rigorous, reproducible, and transparent credit analysis that goes beyond traditional financial metrics.

<p align="center">
  <strong>Version <code>v0.0.2</code></strong> ·
  <strong>License</strong> Source-Available · Non-Commercial ·
  <strong>Tests</strong> pytest regression suite + consistency gates · CI on Python 3.11 &amp; 3.12 ·
  <strong>27 methodology documents</strong>
</p>

<p align="center">
  🌐 <a href="#"><strong>English</strong></a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="README.fr.md">Français</a>
</p>

---

## Table of Contents

- [What Is Credence](#what-is-credence)
- [Engine Architecture](#engine-architecture)
  - [Layer 1: Mosaic Engine](#layer-1-mosaic-engine)
  - [Layer 2: Dual-Track Engine](#layer-2-dual-track-engine)
  - [Layer 3: Multi-Stakeholder Engine](#layer-3-multi-stakeholder-engine)
  - [Layer 4: System-Intelligence Layer](#layer-4-system-intelligence-layer)
- [The Four-Stage Pipeline](#the-four-stage-pipeline)
- [International Paradigms & Work Paths](#international-paradigms--work-paths)
- [Quick Start](#quick-start)
- [Agent CLI Compatibility](#agent-cli-compatibility)
- [Repository Map](#repository-map)
- [FAQ](#faq)
- [License &amp; Disclaimer](#license--disclaimer)

---

## What Is Credence

Credence packages the methodology of a seasoned fixed-income credit analyst into a form an AI agent can load and execute directly. It is **not an agent framework and not a standalone app** — it is a **domain-methodology skill pack** designed for institutional-grade credit analysis across international bond markets.

### Core Principle

Traditional financial analysis rests on an implicit assumption — that a firm's credit risk can be read from its financial statements. This assumption systematically fails in three industry archetypes:

| Industry Type | Why Financial Analysis Fails | Heaviest Factor Location |
|---|---|---|
| **Policy-Driven** (Solar, Semiconductors) | Policy cycles determine industry demand ceilings; sudden shifts can devastate an industry within weeks | Industrial policy / Geopolitics (not on balance sheet) |
| **Technology-Moat** (Advanced Equipment, Biopharma) | Core assets (IP, pipeline, certifications) are not on balance sheet; many pre-revenue firms cannot be valued by PE/PB | Technology roadmap / Core IP (not on balance sheet) |
| **Asset-Lease** (Data Centers, Infrastructure REITs) | REIT-like profile; core metrics are NOI/DSCR rather than traditional indicators | Customer lease quality (not on balance sheet) |

**The heaviest credit factors are never on the balance sheet.** External credit ratings lag real credit deterioration by an average of 17+ months (Enron, Lehman Brothers, Wirecard, Greece sovereign — all rated investment grade within months of default).

### Two Theoretical Foundations

| Theory | Implication | Engine Implementation |
|---|---|---|
| **Mosaic Theory** | Individual public data fragments are meaningless in isolation; assembled together they form a complete picture | Multi-source data aggregation, signal stacking, confidence weighting |
| **Information Completeness Theory** | Data gaps are not defects — they are risk signals. "We do not have this data" itself tells the user that a dimension carries uncertainty | Every analysis conclusion includes a data completeness score and a gap list |

### Architecture at a Glance

```
System-Intelligence Layer (Layer 4)
  Contagion Map x Concentration Dashboard x Systemic Risk Index (SRI)
                        |
                  Single-Issuer Results
                        |
              ┌─────────┴─────────┐
              │   Mosaic Engine   │   Signal extraction + assembly + completeness
              │    (Layer 1)      │
              └─────────┬─────────┘
                        |
           ┌────────────┼────────────┐
           │            │            │
      Track A       Track B      Track C+: Multi-Stakeholder
    Fundamental    Market         6 Buy-Side Roles
     Analysis      Pricing
           │            │
           └──────┬─────┘
                  ▼
       Cross-Validation Matrix
    Consensus -> Mutual reinforcement
    Divergence -> Most valuable insight
                  │
                  ▼
          Integrated Output
    Rating + Signals + Completeness Report
```

---

## Engine Architecture

### Layer 1: Mosaic Engine

**Extracting signals from fragmented public data.**

The Mosaic Engine operates as the data-inception layer of the entire analysis pipeline. It ingests unstructured, multi-source public data and transforms it into structured, confidence-weighted signals ready for downstream dual-track analysis.

#### Signal Extraction

The engine collects data from seven public-source categories — macro policy, industry data, supply chain pricing, corporate filings, litigation/regulatory records, bond market data, and macroeconomic indicators — all through free, publicly available channels (WebSearch, SEC EDGAR, central bank portals, FRED, TRACE, etc.).

#### Mosaic Assembly

Individual data points are assembled into an industry-pyramid-aligned mosaic using a rules engine. The assembly process stacks signals by source reliability, temporal recency, and cross-source corroboration, producing a structured signal map for each issuer.

#### Completeness Assessment

Every analysis conclusion includes a quantitative **completeness score** (0-100) and an explicit gap list. The engine distinguishes between:

- **Known knowns** — data points confirmed from multiple sources
- **Known unknowns** — data gaps identified and flagged as risk signals
- **Unknown unknowns** — structural blind spots documented as methodological limitations

#### Key Metrics

| Metric | Description |
|---|---|
| Completeness Score | 0-100 score per analysis dimension |
| Signal Confidence | Source-weighted confidence for each extracted signal |
| Gap Impact | Qualitative assessment of how each data gap affects rating reliability |

---

### Layer 2: Dual-Track Engine

**Fundamental analysis (Track A) vs. market pricing (Track B) cross-validation.**

The Dual-Track engine runs two independent analysis tracks in parallel, then cross-validates their outputs. Divergence between tracks generates the engine's most valuable insights.

#### Track A: Fundamental Analysis

Applies the industry-pyramid framework — a ten-dimension scoring system (D1-D10) that evaluates:

| Dimension | Focus |
|---|---|
| D1-D3 | Structural industry position, policy environment, competitive moat |
| D4-D6 | Business model resilience, revenue stability, cost structure |
| D7-D8 | Financial policy, capital structure, liquidity |
| D9-D10 | Governance, management track record, external support |

Scoring follows a strict layer-by-layer progression: Layer 1 (heaviest structural factors) must pass before Layer 2 analysis is meaningful; layers cannot be skipped. The financial layer (L4) serves as a validation layer for upper-layer judgments.

#### Track B: Market Pricing Signals

Analyzes four tiers of market-implied signals:

| Signal Tier | Indicators |
|---|---|
| Credit Spreads | Z-spread, asset swap spread, CDS premium |
| Volatility | Price volatility, implied volatility skew |
| Fund Flows | Primary market demand, secondary turnover, investor composition |
| Rating Migration | External rating trends, outlook changes, watch list entries |

#### Cross-Validation Matrix

| Track A / Track B | Positive Signals | Negative Signals |
|---|---|---|
| **Positive** | **Mutual Reinforcement** — high confidence | **Track B Leading** — market pricing ahead of fundamentals |
| **Negative** | **Track A Leading** — fundamentals deteriorate before market prices in | **Mutual Confirmation** — high certainty of distress |

On conflict, **Track A (auditable public financial facts) takes priority** over external ratings.

#### Rating Mapping

The engine's internal 0-10 composite score maps to the three major international rating agencies on an 18-notch scale — **higher score means higher rating** (9.5-10.0 = AAA at the top, 0-0.9 = D at the bottom), with a one-vote veto locking the composite ceiling at CCC. The full tier-by-tier alignment with S&P / Moody's / Fitch is single-sourced in `dev/engine/dual-track-methodology.md` §6 and is not duplicated here.

**Financial framework**: IFRS (International Financial Reporting Standards) and US GAAP (Generally Accepted Accounting Principles) are both supported, with automatic detection of reporting standards from issuer filings and adjustments for key differences (operating lease capitalization, R&D capitalization, deferred tax recognition).

---

### Layer 3: Multi-Stakeholder Engine

**Six buy-side roles with cross-role analysis matrix.**

Different market participants look at the same credit through different lenses. The Multi-Stakeholder engine runs parallel assessments across six buy-side roles, then constructs a cross-comparison matrix that highlights consensus and divergence.

#### The Six Roles

| # | Role | Core Decision | Horizon | Key Data Needs |
|---|---|---|---|---|
| 1 | **Credit Selector** | "Does this credit belong in the book?" — single-issuer rating, default probability | 12-36 months | Industry pyramid, financial deep-dive, LGD/recovery, external support |
| 2 | **Portfolio Manager** | "Is this the best risk/reward?" — relative value, sector allocation | 6-24 months | Relative value metrics, comparative analysis, curve positioning |
| 3 | **Risk Officer** | "Where are concentration/contagion hotspots?" — portfolio risk monitoring | Continuous (monthly SRI + event-driven) | Concentration dashboard, contagion matrix, SRI, stress tests |
| 4 | **Trader** | "Is today the day to act?" — execution, market timing | Intraday to 2 weeks | L0 signal card, real-time spreads, liquidity conditions |
| 5 | **Advisor** | "What should my client do?" — allocation advice, suitability | 3-12 months | Client risk profile overlay, L1 snapshot, thematic views |
| 6 | **Individual Investor** | "Should I own this bond?" — personal investment decision | 6-36 months | Simplified L0/L1, buy/hold/sell signal, plain-language risk summary |

#### Cross-Role Matrix

When multiple stakeholders analyze the same issuer, the engine constructs a consensus/divergence matrix:

| Aspect | Consensus Scenario | Divergence Scenario |
|---|---|---|
| Credit Quality | All roles agree on rating direction | Credit Selector bullish, Risk Officer bearish -> deeper investigation |
| Risk Appetite | Portfolio Manager and Risk Officer align on concentration | Trader sees short-term opportunity, Risk Officer warns of tail risk |
| Time Horizon | All roles' signals point to the same trigger window | Diverging time horizons expose maturity-mismatch risk |

The cross-role matrix is proven in the Brilliance Auto case study, where differing role perspectives revealed structural weaknesses that single-role analysis missed.

---

### Layer 4: System-Intelligence Layer

**Cross-issuer systemic risk perception — contagion, concentration, and early warning.**

The System-Intelligence Layer (SIL) is the topmost aggregation layer, responsible for detecting systemic risk patterns that no single-issuer analysis can reveal. It comprises three integrated modules and a fourth coded monitoring engine.

#### Contagion Matrix (19 International Industries)

A full 19x19 inter-industry contagion intensity matrix based on the Global Industry Classification Standard (GICS), covering all major international economic sectors:

| # | Industry | Primary Paradigm | Contagion Role |
|---|---|---|---|
| 1 | Energy (Oil & Gas) | P1: Cyclical | Super-spreader (high outbound contagion) |
| 2 | Chemicals | P1: Cyclical | Moderate transmitter |
| 3 | Metals & Mining | P1: Cyclical | Cyclical amplifier |
| 4 | Construction Materials | P1: Cyclical | Infrastructure-linked transmitter |
| 5 | Capital Goods | P1: Cyclical | Manufacturing contagion hub |
| 6 | Commercial Services | P1: Cyclical | Low systemic linkage |
| 7 | Transportation | P4: Regulated Utility | Logistics transmission vector |
| 8 | Automobiles | P1: Cyclical | Consumer-industrial bridge |
| 9 | Consumer Durables | P1: Cyclical | Demand-cyclical receiver |
| 10 | Consumer Staples | P2: Defensive | Defensive, low contagion |
| 11 | Retail | P1: Cyclical | End-demand transmission receiver |
| 12 | Technology Hardware (Semis) | P3: Growth | Geopolitical contagion super-spreader |
| 13 | Software & Services | P3: Growth | Low direct contagion, high narrative spillover |
| 14 | Biotech & Pharma | P3: Growth | Regulatory shock receiver |
| 15 | Healthcare Equipment | P2: Defensive | Low cyclical contagion |
| 16 | Utilities (Regulated) | P4: Regulated Utility | Defensive, low contagion |
| 17 | Telecommunications | P4: Regulated Utility | Infrastructure contagion receiver |
| 18 | Financials (Banks/Insurance) | P5: Financial | **Systemic super-spreader** (highest outbound contagion) |
| 19 | Sovereigns & GSEs | P6: Sovereign-Linked | Foundational risk factor |

Key derived metrics include the Contagion Forward Coefficient (CFC), Contagion Vulnerability Coefficient (CVC), and Contagion Net Exposure Ratio (CNER), plus stress-escalation jump tables for factor-specific intensity increases.

#### Five-Dimension Concentration Dashboard

Evaluates portfolio concentration risk across five independent dimensions:

| Dimension | Assessment |
|---|---|
| Industry Concentration | CR3 / CR5 / HHI / MAX1 by GICS industry |
| Regional Concentration | Single country/region share + weak-region share |
| Rating Concentration | External AAA share + pseudo-high-rating share |
| Tenor Concentration | 12-month maturity share + single-month peak |
| Funding Channel Concentration | Top funding-channel share + contraction status |

Thresholds, traffic-light bands, and the notch-impact mapping for each dimension are single-sourced in `dev/engine/concentration-framework.md` and are not duplicated here.

#### Systemic Risk Index (SRI) with Four-Tier Thermometer

The SRI aggregates multi-source signals into a single systemic risk reading, visualized as a four-tier thermometer:

| Thermometer Tier | SRI Range (0-3+ scale) | Meaning |
|---|---|---|
| 🟢 Normal | below 0.5 | Systemic risk within normal bounds |
| 🟡 Watch | 0.5 - 1.0 | Elevated risk in specific sectors |
| 🟠 Alert | 1.0 - 1.8 | Broad-based risk accumulation |
| 🔴 Danger | 1.8 and above | Systemic stress imminent |

The SRI uses a continuous 0-3+ scale — never a percentage system. Tier definitions and mandated actions are single-sourced in `dev/engine/systemic-warning-framework.md` §3. The SRI calculation engine (`src/sri_calculator.py`) implements the aggregation algorithm, and the thermometer level feeds into the L0 signal card and triggers escalation across the four-stage pipeline.

#### Outlook Monitoring Engine

The fourth coded engine (`src/outlook_engine.py`) provides:

- **12-24 month rating outlook** assessment with directional probability
- **90-day watchlist** with automated trigger conditions
- **Rating migration matrix** with historical transition probabilities
- **Continuous monitoring triggers** that propagate through the work-path registry

---

## The Four-Stage Pipeline

Every credit analysis flows through a four-stage chained pipeline, with `path_id` as the join key across stages:

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ ① Intake │ -> │ ② Analysis│ -> │ ③ Report │ -> │ ④ QA     │
│ (Router) │    │ (Engine)  │    │ (Builder)│    │ (Verifier)│
└──────────┘    └──────────┘    └──────────┘    └──────────┘
```

| Stage | Name | Artifact | Hosting Skill | Status |
|---|---|---|---|---|
| S1 | **Intake** | Path Sheet | `credit-analysis-router` | ✅ Delivered |
| S2 | **Analysis** | Analysis Artifact | `fixed-income-credit-analysis` | ✅ Delivered |
| S3 | **Report** | Delivery Note | `credit-report-builder` | ✅ Delivered |
| S4 | **QA** | QA Verdict | `credit-qa-verifier` | ✅ Delivered |

**S1 — Intake (Router)** : The `credit-analysis-router` skill uses a four-question routing mechanism to classify vague user requests ("analyze this company", "what analysis should I run") into a concrete **Path Sheet**. The sheet carries a `path_id`, engine reading order, template selection, and quality gate specifications — all derived from the single source of truth in `dev/engine/work-path-registry.md`.

**S2 — Analysis** : The `fixed-income-credit-analysis` skill executes the analysis per the path sheet's engine reading order. For four wired paths, the orchestrator (`src/pipeline.py`) invokes the corresponding coded engine directly:
- **WP-RO-01** -> `src/concentration_scorer.py` (five-dimension concentration)
- **WP-RO-02** -> `src/contagion_engine.py` (contagion matrix)
- **WP-RO-03** -> `src/sri_calculator.py` (systemic risk index)
- **WP-X-05** -> `src/outlook_engine.py` (outlook monitoring)

All non-wired paths are LLM-orchestrated per engine documentation.

**S3 — Report** : The `credit-report-builder` skill assembles the completed analysis into a deliverable HTML report. Template selection (Type 1-18) follows the path sheet specification and maps to the L0/L1/L2 three-tier output system:
- **L0** (Signal Card) — 5-second summary: rating, outlook, key signals of the day
- **L1** (Snapshot) — One-page dashboard with radar charts and key anomaly list
- **L2** (Deep Dive) — Full analytical report with pyramid layering and cross-validation

**S4 — QA** : The `credit-qa-verifier` skill performs a pre-delivery quality gate review, enforcing signal-density rules, one-shot-veto ceiling compliance, Mode B guardrails, and single-source-of-truth integrity. This is the terminal stage in the four-stage chain — no report is delivered without passing QA.

**Executable Orchestrator**: `src/pipeline.py` drives the entire four-stage chain in code. It reads stage definitions from `dev/engine/pipeline-contract.md` (never hardcodes stage names), validates path sheets using `src/path_sheet.py`, and invokes coded engines only for explicitly wired paths. The single source of truth for all four artifacts (path sheet, analysis artifact, delivery note, QA verdict) and their chaining edges is `dev/engine/pipeline-contract.md`.

---

## International Paradigms & Work Paths

### Six International Paradigms (P1-P6)

The engine classifies all industries into six analytical paradigms, each with distinct weight templates, scoring priorities, and factor emphasis:

| Paradigm | Code | Core Industries | Key Differentiator |
|---|---|---|---|
| **Cyclical** | P1 | Energy, Chemicals, Metals & Mining, Construction Materials, Capital Goods, Commercial Services, Automobiles, Consumer Durables, Retail | Commodity/freight/spending cycles determine demand and margins |
| **Defensive** | P2 | Consumer Staples, Healthcare Equipment | Inelastic demand; brand moats and pricing power stabilize margins |
| **Growth** | P3 | Technology Hardware (Semis), Software & Services, Biotech & Pharma | R&D intensity and IP drive revenue growth; pre-revenue valuation is standard |
| **Regulated Utility** | P4 | Transportation, Utilities, Telecommunications | License/concession revenue; NOI/DSCR are the core metrics; infrastructure financing |
| **Financial** | P5 | Financials (Banks/Insurance) | Capital adequacy, asset quality, and funding structure are the core risk drivers |
| **Sovereign-Linked** | P6 | Sovereigns & GSEs | Fiscal capacity and institutional strength determine credit |

### 16 Work Paths

The engine defines **16 work paths** mapped to international buy-side roles, each specifying an engine sequence, report template, and quality gate requirements.

#### By Role

**Credit Selector (2 paths)**
| ID | Path | Status | Output |
|---|---|---|---|
| WP-CS-01 | Single-Issuer Rating | ✅ Active | Rating + Signals + Completeness Report |
| WP-CS-02 | LGD + External Support Add-On | 🟡 Partial | LGD Tier + Recovery Rate + Support Adjustment |

**Portfolio Manager (2 paths)**
| ID | Path | Status | Output |
|---|---|---|---|
| WP-PM-01 | Investment Dashboard | ✅ Active | Four-Dimension Score + Investment Recommendation |
| WP-PM-02 | Comparative Analysis | 🟡 Partial | Comparison Score + Differentiation Conclusion |

**Risk Officer (4 paths)**
| ID | Path | Status | Output |
|---|---|---|---|
| WP-RO-01 | Concentration Assessment | ✅ Active | Five-Dimension Concentration Score + Adjustment Recommendations |
| WP-RO-02 | Cross-Industry Contagion | ✅ Active | Contagion Path Map + Adjustment Recommendations |
| WP-RO-03 | Systemic Risk Reading | ✅ Active | SRI Reading + Thermometer Tier |
| WP-RO-04 | Portfolio Stress Test | 🟡 Partial | Stress Scenario Loss + Threshold Jump Results |

**Trader (1 path)**
| ID | Path | Status | Output |
|---|---|---|---|
| WP-TR-01 | Market Watch Signal Card | 🟡 Partial | L0 Signal Card + Thermometer Reading |

**Advisor (1 path)**
| ID | Path | Status | Output |
|---|---|---|---|
| WP-AD-01 | Origination Assessment | 🔴 Planned | Underwriting Feasibility + Pricing Range |

**Individual Investor (1 path)**
| ID | Path | Status | Output |
|---|---|---|---|
| WP-II-01 | Decision Support | 🔴 Planned | Financing Channel Comparison + Timing Recommendation |

**Meta / Special-Purpose (5 paths)**
| ID | Path | Status | Output |
|---|---|---|---|
| WP-X-01 | Black Swan Backtest Validation | ✅ Active | Validation Conclusion + Framework Improvements |
| WP-X-02 | Multi-Role Parallel Assessment | ✅ Active | Multi-Role Score Matrix + Consensus/Divergence Report |
| WP-X-03 | Industry Framework Builder | ✅ Active | Industry Pyramid + D1-D10 Scores |
| WP-X-04 | ESG/Governance Risk Scan | 🟡 Partial | ESG Risk Scan + Governance Red-Flag List |
| WP-X-05 | Outlook & Continuous Monitoring | ✅ Active | Rating Outlook + Watchlist |

**Status summary**: 9 active, 5 partial, 2 planned.

### Report Templates (Type 1-18)

Each work path maps to one or more HTML report templates:

| Template | Type | Used By |
|---|---|---|
| Type 1 | Single-Issuer Deep Dive | WP-CS-01 |
| Type 2 | Comparative Analysis | WP-PM-02 |
| Type 3 | Backtest Validation | WP-X-01 |
| Type 4 | Multi-Role Matrix | WP-X-02 |
| Type 5 | PM Dashboard | WP-PM-01 |
| Type 6 | Rating Summary Card | WP-CS-01 |
| Type 7 | Industry Framework | WP-X-03 |
| Type 8 | LGD Assessment | WP-CS-02 |
| Type 9 | External Support | WP-CS-02 |
| Type 10 | ESG/Governance Scan | WP-X-04 |
| Type 11 | Stress Test | WP-RO-04 |
| Type 12 | *Reserved* | — |
| Type 13 | Contagion Map | WP-RO-02 |
| Type 14 | Concentration Dashboard | WP-RO-01 |
| Type 15 | SRI Thermometer | WP-RO-03 |
| Type 16 | *Planned (Origination)* | WP-AD-01 |
| Type 17 | *Planned (Advisory)* | WP-II-01 |
| Type 18 | Outlook Monitoring | WP-X-05 |

---

## Quick Start

**Key premise**: the skills are NOT self-contained — at runtime they read `engine/` and `templates/` from the **package root** (single source of truth, never copied). The install unit is the whole package root; **open the package root as your project** and everything resolves with zero copying.

### A. npx (Recommended)

```bash
npx github:tywinlu1988/credence-global
```

Downloads the latest release zip from GitHub Releases, verifies its SHA-256 checksum, and unpacks it into `./credence/`; open that folder with your agent CLI. Pin a specific version with `--tag vX.Y.Z`.

### B. GitHub Release

Download the latest `vX.Y.Z-release.zip` from the [Releases page](https://github.com/tywinlu1988/Credence-Global/releases), verify it against the attached `vX.Y.Z-release.zip.sha256`, unzip, and open the package root as a project.

### C. Clone the Source

```bash
git clone git@github.com:tywinlu1988/Credence-Global.git
cd credence-global
pip install -e .
```

### D. Running Tests

```bash
python -m pytest tests/ -q          # full regression suite
python scripts/consistency_check.py  # Cross-document consistency validation
```

### First Steps

1. Open the package root in your agent CLI
2. Start a conversation: *"Analyze company XYZ in the semiconductor industry"*
3. The `credit-analysis-router` skill will route your request to a work path
4. Execution follows the four-stage pipeline: intake -> analysis -> report -> QA
5. A Type-1 deep-dive HTML report or Type-6 rating summary is produced

For detailed engine documentation, see `dev/engine/engine-overview.md`.

---

## Agent CLI Compatibility

Credence delivers its methodology as Agent Skills (`SKILL.md`) that any AI coding agent can load. Compatibility varies by client:

| Agent CLI | Discovery Mechanism | Setup Complexity | Notes |
|---|---|---|---|
| **Claude Code** | Auto-discovers `dev/.claude/skills/` | None | Full support; automatic skill loading |
| **Codex** | Reads `AGENTS.md` + manual `SKILL.md` load | Low | See `docs/adapters/codex.md` for deep-dive setup |
| **Cursor** | Reads `AGENTS.md` + manual `SKILL.md` load | Low | Manual skill invocation |
| **Gemini** | Reads `AGENTS.md` + manual `SKILL.md` load | Medium | May require prompt engineering for skill context |
| **OpenCode** | Reads `AGENTS.md` + manual `SKILL.md` load | Low | Compatible with standard agent workflows |

**Universal posture**: read `AGENTS.md` first, then load the relevant `SKILL.md` for the task at hand. The `AGENTS.md` file at the repository root serves as the cross-CLI entry point.

---

## Repository Map

```
credence-global/
|
|-- dev/                                # Methodology & skill source
|   |-- engine/                         # 27 core methodology documents
|   |   |-- engine-overview.md          # Architecture overview & document navigation
|   |   |-- industry-framework.md       # Industry classification, 10-dimension scoring, 6 paradigms
|   |   |-- mosaic-engine.md            # Signal extraction, puzzle assembly, completeness
|   |   |-- dual-track-methodology.md   # Track A+B cross-validation, rating mapping, worked examples
|   |   |-- multi-stakeholder.md         # 6 buy-side roles, cross-role matrix
|   |   |-- quantitative-analysis.md    # Spread, volatility, multi-factor models, stress testing
|   |   |-- qualitative-analysis.md     # Information source grading, policy, mosaic assembly
|   |   |-- financial-deep-dive.md      # 3-statement linkage, working capital, FCF
|   |   |-- lgd-recovery-framework.md   # LGD 5-tier, collateral valuation, recovery path
|   |   |-- external-support-framework.md    # Government/group/strategic support
|   |   |-- outlook-monitoring-framework.md # 12-24m outlook, watchlist, migration matrix
|   |   |-- governance-fraud-risk.md    # 20+ fraud signals, default evasion detection
|   |   |-- esg-framework.md            # ESG + governance/fraud detection
|   |   |-- financial-bond-framework.md # FI bond analysis framework
|   |   |-- holding-company-framework.md
|   |   |-- non-credit-risk-overlay.md  # Market/operational/reputational/strategic/liquidity
|   |   |-- output-layered-framework.md # L0 signal card, L1 snapshot, L2 deep dive
|   |   |-- contagion-theory.md         # 4 contagion types, 7 transmission paths
|   |   |-- contagion-matrix.md         # 19x19 industry contagion matrix
|   |   |-- concentration-framework.md  # 5-dimension concentration analysis
|   |   |-- systemic-warning-framework.md    # SRI signal aggregation, 4-tier thermometer
|   |   |-- validation-methodology.md   # Black swan backtesting, dual-point validation
|   |   |-- paradigm-brand-channel.md   # Brand/channel application note (P2 Defensive)
|   |   |-- paradigm-network-traffic.md # Network/throughput secondary-attribute application note
|   |   |-- dimension-registry.md       # Addressable index of 6 paradigms + M0-M5 roles
|   |   |-- work-path-registry.md       # 16 work paths, routing, pipeline integration
|   |   |-- pipeline-contract.md        # 4-stage pipeline I/O contracts, chain edges
|   |
|   |-- templates/                      # Report template source of truth (16 HTML files)
|   |   |-- template-base.css           # Shared style base
|   |   |-- template-type{1..15}.html   # Type 1-15 report templates
|   |   |-- template-type18.html        # Type 18 outlook monitoring template
|   |
|   |-- design/                         # Report design system
|   |-- data/                           # Data architecture & pipeline specs
|   |-- product/                        # Product vision, commercial model, GTM strategy
|   |-- .claude/skills/                 # 4-stage skill chain
|       |-- credit-analysis-router/     # Intake: 4-question routing -> Work Path Sheet
|       |-- fixed-income-credit-analysis/ # Analysis: per-path execution
|       |-- credit-report-builder/      # Report: HTML assembly from templates
|       |-- credit-qa-verifier/         # QA: pre-delivery quality gate
|
|-- src/                                # Executable orchestrator & coded engines
|   |-- pipeline.py                     # 4-stage chain orchestrator
|   |-- path_sheet.py                   # Path sheet validation & registry parsing
|   |-- sri_calculator.py               # Systemic Risk Index calculation engine
|   |-- concentration_scorer.py         # 5-dimension concentration scoring engine
|   |-- contagion_engine.py             # Contagion matrix & escalation engine
|   |-- outlook_engine.py              # Outlook & monitoring assessment engine
|
|-- tests/                              # Regression test suite (pytest)
|-- scripts/                            # Build & validation tools
|   |-- build_dist.py                   # dev/ -> release-package assembler
|   |-- consistency_check.py            # Cross-document consistency validation
|   |-- promote.py                      # Version promotion utility
|
|-- docs/                               # Cross-CLI adapters & version management
|-- validation/                         # Capability evidence (2 public methodology reference reports)
|-- version/                            # Locally built release zips (gitignored; shipped via GitHub Releases)
|-- AGENTS.md                           # Cross-CLI universal entry point
|-- DEVELOPMENT.md                      # Development guide
|-- LICENSE                             # Source-available, non-commercial license
|-- pyproject.toml                      # Python project configuration
|-- package.json                        # npm registry metadata
```

---

## FAQ

### Q1: What makes Credence different from traditional credit analysis?

Credence addresses three systematic failures in traditional financial analysis: (1) the heaviest credit factors (policy, IP, lease quality) are never on the balance sheet, (2) external ratings lag real deterioration by 17+ months on average, and (3) single-perspective analysis misses structural weaknesses. Credence uses a layered pyramid framework, dual-track cross-validation, mosaic data assembly, and multi-stakeholder perspective to surface what traditional analysis misses.

### Q2: Do I need a paid subscription or API key?

No. Credence operates on zero-cost public data sources — SEC EDGAR, FRED, central bank portals, TRACE, industry association reports, and web search. The POC phase is intentionally data-source constrained to prove that effective credit analysis is possible with public data alone.

### Q3: Which credit rating agencies does the engine align with?

The engine's internal rating scale maps to S&P (AAA through D), Moody's (Aaa through C), and Fitch (AAA through D). See the rating mapping table in `dev/engine/dual-track-methodology.md` for the full alignment.

### Q4: Can Credence be used with any AI agent CLI?

Yes. Credence is CLI-agnostic. It works with Claude Code (full auto-discovery), Codex, Cursor, Gemini, and OpenCode. The `AGENTS.md` file at the repository root serves as the universal entry point.

### Q5: How are the 16 work paths organized?

Paths are organized by buy-side role: Credit Selector (2 paths), Portfolio Manager (2), Risk Officer (4), Trader (1), Advisor (1), Individual Investor (1), and Meta/Special-Purpose (5). Each path specifies an engine sequence, report template, and quality gates. 9 paths are fully active, 5 are partially implemented, and 2 are planned.

### Q6: What are the 6 international paradigms?

Cyclical (P1), Defensive (P2), Growth (P3), Regulated Utility (P4), Financial (P5), and Sovereign-Linked (P6). Each paradigm determines the weight template and scoring priorities for industry analysis.

### Q7: What does "System-Intelligence Layer" mean?

It is the topmost aggregation layer that goes beyond single-issuer analysis to detect systemic patterns: cross-industry contagion (19x19 matrix), portfolio concentration (5 dimensions), and the Systemic Risk Index (SRI) with a four-tier thermometer. Together, these modules answer "what is happening across the entire portfolio/market" rather than "is this single issuer risky."

### Q8: What is the test and CI setup?

The pytest regression suite covers the coded engines, the pipeline orchestrator, the document registries, the consistency checker, and the release-package builder. CI runs it on Python 3.11 and 3.12 via GitHub Actions. Run locally with `python -m pytest tests/ -q`. Cross-document consistency is validated separately with `python scripts/consistency_check.py`.

### Q9: What financial reporting standards are supported?

IFRS (International Financial Reporting Standards) and US GAAP (Generally Accepted Accounting Principles). The engine auto-detects the reporting standard from issuer filings and adjusts for key differences.

### Q10: How do I get started with the four skill chain?

Open the package root in your CLI, then say "analyze company [X] in the [Y] industry." The `credit-analysis-router` skill handles the routing. For direct skill usage, load the relevant `SKILL.md` per the `AGENTS.md` instructions.

### Q11: What is the difference between the coded engines and the LLM-orchestrated paths?

Four work paths have dedicated Python implementations (coded engines): concentration scoring, contagion matrix, SRI calculation, and outlook monitoring. These are invoked directly by the orchestrator (`src/pipeline.py`) when the path ID matches. All other paths are orchestrated by the LLM using the engine documentation as reference — no Python code duplicates the methodology.

### Q12: Can I use Credence for commercial purposes?

Commercial use requires prior written permission from the copyright holder. See the [LICENSE](LICENSE) file for full terms. The engine is source-available for non-commercial evaluation, research, and internal assessment.

---

## License & Disclaimer

This repository is **source-available** under the Credence Source-Available Non-Commercial License. You may view, learn from, and use the work for non-commercial / internal evaluation purposes. **Any commercial use requires prior written permission** from the copyright holder.

**Key terms**:
- Non-commercial use (research, teaching, internal evaluation) is free and permitted
- Commercial use (SaaS, paid consulting, production systems, redistribution) requires a separate commercial license
- The engine's output is a methodology demonstration and research artifact — **it is not investment advice**
- No warranty is provided; the software is offered "as is"

See the full [LICENSE](LICENSE) file for complete terms.

**Methodology validation**: The engine's methodology has been exercised against five documented historical default/distress cases — Lehman Brothers, Wirecard, Valeant, Credit Suisse, and the Greece sovereign restructuring (see `dev/engine/validation-methodology.md` §6). Two public methodology reference reports ship in the `validation/` directory; the full test archive is maintained privately and available on request.

---

<p align="center">
  <strong>Credence</strong> · Fixed-Income Credit Analysis Engine · v0.0.2<br>
  Built for rigorous, transparent, and reproducible credit analysis.
</p>
