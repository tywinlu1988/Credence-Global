# Fixed Income Credit Intelligent Analysis Engine

**Project Codename**: Credence
**Version**: v0.0.1
**Status**: Methodology documentation phase -- Product design complete -- International industry coverage -- System intelligence layer online -- Documentation structure reorganized

---

## Project Overview

International fixed-income credit analysis engine. Through industry-customized multi-layer analysis pyramid, dual-track cross-validation framework, mosaic public data engine, multi-stakeholder perspective, non-credit risk overlay, and system intelligence layer, it provides credit insight beyond traditional financial analysis for credit approval, bond investment, market trading, and risk management. Coverage includes international industry sectors with cross-industry contagion mapping, five-dimensional concentration dashboard, and systemic risk thermometer.

**Core Principle**: Traditional financial analysis systematically fails in policy-driven, technology-moat, and asset-lease industries. The heaviest credit factors rarely appear on the balance sheet. External credit ratings lag true credit deterioration by an average of 17+ months.

---

## Directory Structure

```
../AGENTS.md                                       Cross-CLI entry point (repo root -- any agent CLI starts here)
dev/
|-- README.md                                        You are here
|-- engine/                                          Methodology and algorithms (27 current documents)
|   |-- engine-overview.md                          Architecture overview, document navigation
|   |-- industry-framework.md                       Industry classification (10-dimension scoring, 13-industry pyramid)
|   |-- qualitative-analysis.md                     Qualitative analysis (sources, policy, mosaic, narrative)
|   |-- quantitative-analysis.md                    Quantitative analysis (spread, volatility, factors, stress, market signals)
|   |-- dual-track-methodology.md                   Dual-track + cross-validation, 12-notch rating, EL integration, mitigation
|   |-- mosaic-engine.md                            Mosaic engine (signals, puzzle, completeness, Mode B)
|   |-- multi-stakeholder.md                        Multi-stakeholder (M0-M6, concentration risk, system intelligence layer)
|   |-- validation-methodology.md                   Validation methodology (black swan backtesting, dual-point, forward comparison)
|   |-- financial-deep-dive.md                      Financial deep dive (3-statement linkage, working capital, FCF, stress test)
|   |-- lgd-recovery-framework.md                   LGD recovery (5-tier, collateral, recovery path)
|   |-- external-support-framework.md               External support (government/group/strategic, capability vs. willingness)
|   |-- outlook-monitoring-framework.md             Outlook + monitoring (outlook, watch list, ongoing monitoring, transition matrix)
|   |-- governance-fraud-risk.md                    Governance/fraud risk (20+ signals, default evasion detection)
|   |-- esg-framework.md                            ESG + governance/fraud detection framework
|   |-- financial-bond-framework.md                 Financial institution bond analysis framework
|   |-- holding-company-framework.md                Holding company credit analysis framework
|   |-- non-credit-risk-overlay.md                  Non-credit risk overlay (market/operational/reputational/strategic/liquidity)
|   |-- output-layered-framework.md                 Layered output (L0 signal card + L1 snapshot + L2 deep dive + thermometer card)
|   |-- contagion-theory.md                         Contagion theory (4 types, 7 transmission paths, escalation factors)
|   |-- contagion-matrix.md                         Star 13x13 industry contagion matrix (transmission intensity, industry clustering)
|   |-- concentration-framework.md                  Star 5-dimension concentration framework (thresholds, rating adjustments, stress testing)
|   |-- systemic-warning-framework.md               Star systemic warning framework (SRI signal aggregation, thermometer, historical backtest)
|   |-- paradigm-brand-channel.md                   Defensive (P2) paradigm: brand moat and distribution channels (Consumer Staples, Healthcare)
|   |-- paradigm-network-traffic.md                 Network and Throughput (P4) paradigm: network effects and traffic/throughput (Transportation, Telecom, Technology)
|   |-- dimension-registry.md                       Dimension registry (6 paradigms + LGFV, M0-M5 roles, addressable index)
|   |-- work-path-registry.md                       Work path registry (analysis route selection, pipeline routing)
|   |-- pipeline-contract.md                        Pipeline contract (work path order, analysis output, delivery order, QA ruling)
|
|-- templates/                                      Report template single source of truth (17 files)
|   |-- template-base.css                           Shared style base
|   +-- template-type1..15.html + type18.html       Type 1-15 and Type 18 report templates
|
|-- design/                                         Report design system
|   |-- report-style-system.md                      Report style system
|
|-- data/                                           Data architecture
|   |-- data-architecture.md                        Data source stratification, accessibility validation, gap mapping
|   +-- data-pipeline-spec.md                       Data pipeline specification
|
|-- product/                                        Product design
|   |-- product-overview.md                         Product vision, magic experience, user personas
|   +-- commercial-model.md                         Commercial model, buy-side simulation, GTM strategy
|
+-- .claude/skills/                                 AI skill bundles (4-chain; templates reference dev/templates/)
    |-- credit-analysis-router/                     Intake: 4-question routing, produces Work Path Order
    |-- fixed-income-credit-analysis/               Analysis: executes per path order, produces Analysis Output
    |-- credit-report-builder/                      Report: assembles delivery report, produces Delivery Order
    +-- credit-qa-verifier/                         QA: pre-delivery final quality check, produces QA Ruling
```

> Capability validation evidence (72+ test reports) is archived at repo root `../validation/`. These are test outputs, not project components, and are never included in version snapshots. (The GitHub main repository publishes only 2 industry methodology references; all other test reports remain on the maintainer's local machine.)

---

## Current Progress

### System Intelligence Layer

| Module | Status | Core Document |
|---|---|---|
| Contagion Map | Done | contagion-theory.md, contagion-matrix.md |
| Concentration Dashboard | Done | concentration-framework.md |
| Systemic Warning | Done | systemic-warning-framework.md |
| Thermometer L0 Card | Done | Integrated into output-layered-framework.md Sect. 3.6 |

### Report Templates

| Item | Count | Description |
|---|---|---|
| Report templates | 16 types (Type 1-15, Type 18) | Templates/ single source of truth (template-base.css + type1-15.html + type18.html) |

### Product Design (Complete)

Product vision, Magic Experience, 3-layer output system, commercial model, pricing, GTM

### Technical Implementation (Not Started)

To commence after methodology and product design are fully documented.

---

## Quick Navigation

| To learn about... | Go to... |
|---|---|
| Report templates (Type 1-15 + Type 18 + shared CSS) | `templates/` |
| System intelligence layer overview | `engine/systemic-warning-framework.md` + `engine/contagion-matrix.md` + `engine/concentration-framework.md` |
| Product vision and magic experience | `product/product-overview.md` |
| Commercial model and GTM strategy | `product/commercial-model.md` |
| Analysis engine architecture overview | `engine/engine-overview.md` |
| Industry analysis framework | `engine/industry-framework.md` |
| Qualitative analysis methodology | `engine/qualitative-analysis.md` |
| Quantitative analysis methodology | `engine/quantitative-analysis.md` |
| Dual-track framework + cross-validation | `engine/dual-track-methodology.md` |
| Mosaic engine + completeness | `engine/mosaic-engine.md` |
| Multi-stakeholder perspective | `engine/multi-stakeholder.md` |
| LGD / recovery assessment | `engine/lgd-recovery-framework.md` |
| External support assessment | `engine/external-support-framework.md` |
| Contagion matrix and cross-industry analysis | `engine/contagion-matrix.md` |
| Portfolio concentration assessment | `engine/concentration-framework.md` |
| Systemic risk index | `engine/systemic-warning-framework.md` |
| Report design and style system | `design/report-style-system.md` |
| Cross-CLI entry point (Claude Code, Codex, Cursor, Gemini, OpenCode) | `../AGENTS.md` |
| 4-chain pipeline contracts (work path order, analysis output, delivery order, QA ruling) | `engine/pipeline-contract.md` |
| Dimension registry (6 paradigms + LGFV, M0-M5 roles, addressable pointer layer) | `engine/dimension-registry.md` |
| Executable orchestrator (v0.0.1: code-driven 4-chain, WP-M4-01/-02/-03 coding engines) | `../src/pipeline.py` |
| AI Agent methodology (4-chain: routing, analysis, report, QA) | `.claude/skills/` |
| Version management strategy and release process | `../docs/VERSION-MANAGEMENT.md` |

---

## Version History

| Version | Date | Milestone |
|---|---|---|
| v0.0.1 | 2026-07-18 | Initial release: international fixed-income credit analysis engine |

---

*Last updated: 2026-07-18*
