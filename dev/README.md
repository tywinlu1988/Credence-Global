# Fixed Income Credit Intelligent Analysis Engine

**Project Codename**: Credence
**Version**: v0.0.6
**Status**: Methodology documentation complete — 4 coded engines wired (concentration / contagion / SRI / outlook) — 19-industry GICS coverage — four-stage skill chain delivered

---

## Project Overview

International fixed-income credit analysis engine. Through industry-customized multi-layer analysis pyramids, dual-track cross-validation, the mosaic public-data engine, multi-stakeholder perspectives, the non-credit risk overlay, and the system-intelligence layer, it provides credit insight beyond traditional financial analysis for credit approval, bond investment, market trading, and risk management. Coverage spans 19 GICS-based industries with a 19x19 cross-industry contagion matrix, five-dimensional concentration dashboard, and systemic risk thermometer.

**Core Principle**: Traditional financial analysis systematically fails in policy-driven, technology-moat, and asset-lease industries. The heaviest credit factors rarely appear on the balance sheet. External credit ratings lag true credit deterioration by an average of 17+ months.

---

## Directory Structure

```
../AGENTS.md                                       Cross-CLI entry point (repo root -- any agent CLI starts here)
dev/
|-- README.md                                        You are here
|-- engine/                                          Methodology and algorithms (27 current documents)
|   |-- engine-overview.md                          Architecture overview, document navigation
|   |-- industry-framework.md                       Industry classification (D1-D10 scoring, six paradigms P1-P6, pyramids, veto)
|   |-- qualitative-analysis.md                     Qualitative analysis (sources, policy, mosaic, narrative)
|   |-- quantitative-analysis.md                    Quantitative analysis (spread, volatility, factors, stress, market signals)
|   |-- dual-track-methodology.md                   Dual-track + cross-validation, 18-notch rating mapping, worked examples
|   |-- mosaic-engine.md                            Mosaic engine (signals, puzzle, completeness, Mode B)
|   |-- multi-stakeholder.md                        Multi-stakeholder (6 buy-side roles, cross-role matrix)
|   |-- validation-methodology.md                   Validation methodology (black swan backtesting, dual-point, forward comparison)
|   |-- financial-deep-dive.md                      Financial deep dive (3-statement linkage, working capital, FCF, stress test)
|   |-- lgd-recovery-framework.md                   LGD recovery (5-tier, collateral, recovery path)
|   |-- external-support-framework.md               External support (government/group/strategic, capability vs. willingness)
|   |-- outlook-monitoring-framework.md             Outlook + monitoring (outlook, watch list, ongoing monitoring, transition matrix)
|   |-- governance-fraud-risk.md                    Governance/fraud risk (20+ signals, default evasion detection)
|   |-- esg-framework.md                            ESG + governance/fraud detection framework
|   |-- financial-bond-framework.md                 Financial institution bond analysis framework (P5)
|   |-- holding-company-framework.md                Holding company credit analysis framework
|   |-- non-credit-risk-overlay.md                  Non-credit risk overlay (market/operational/reputational/strategic/liquidity)
|   |-- output-layered-framework.md                 Layered output (L0 signal card + L1 snapshot + L2 deep dive + thermometer card)
|   |-- contagion-theory.md                         Contagion theory (4 types, 7 transmission paths, escalation factors)
|   |-- contagion-matrix.md                         19x19 industry contagion matrix (intensity, clustering, escalation)
|   |-- concentration-framework.md                  5-dimension concentration framework (thresholds, rating adjustments, stress testing)
|   |-- systemic-warning-framework.md               Systemic warning framework (SRI signal aggregation, thermometer, backtests)
|   |-- paradigm-brand-channel.md                   Brand/channel application note (P2 Defensive)
|   |-- paradigm-network-traffic.md                 Network/throughput secondary-attribute application note
|   |-- dimension-registry.md                       Dimension registry (6 paradigms + 6 roles, addressable pointer index)
|   |-- work-path-registry.md                       Work path registry (16 paths: 9 active / 5 partial / 2 planned)
|   |-- pipeline-contract.md                        Pipeline contract (Path Sheet / Analysis Artifact / Delivery Note / QA Verdict)
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
+-- .claude/skills/                                 AI skill bundles (4-stage chain; templates reference dev/templates/)
    |-- credit-analysis-router/                     Intake: 4-question routing, produces Path Sheet
    |-- fixed-income-credit-analysis/               Analysis: executes per path sheet, produces Analysis Artifact
    |-- credit-report-builder/                      Report: assembles delivery report, produces Delivery Note
    +-- credit-qa-verifier/                         QA: pre-delivery final quality check, produces QA Verdict
```

> Capability validation evidence ships as 2 public methodology reference reports at repo root `../validation/` (food-beverage, transportation). The full test archive is maintained privately and available on request. Validation artifacts are test outputs, not project components, and are never included in version snapshots.

---

## Current Progress

### System Intelligence Layer

| Module | Status | Core Document |
|---|---|---|
| Contagion Map (19x19) | Done | contagion-theory.md, contagion-matrix.md |
| Concentration Dashboard | Done | concentration-framework.md |
| Systemic Warning (SRI) | Done | systemic-warning-framework.md |
| Thermometer L0 Card | Done | Integrated into output-layered-framework.md §3.6 |

### Coded Engines (src/)

| Engine | Wired Path | Status |
|---|---|---|
| `concentration_scorer.py` | WP-RO-01 | Wired, tested |
| `contagion_engine.py` | WP-RO-02 | Wired, tested |
| `sri_calculator.py` | WP-RO-03 | Wired, tested |
| `outlook_engine.py` | WP-X-05 | Wired, tested |
| `pipeline.py` + `path_sheet.py` | Orchestrator (all paths) | Wired, tested |

### Report Templates

| Item | Count | Description |
|---|---|---|
| Report templates | 16 types (Type 1-15, Type 18) | templates/ single source of truth (template-base.css + type1-15.html + type18.html) |

### Product Design (Complete)

Product vision, Magic Experience, 3-layer output system, commercial model, pricing, GTM

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
| 4-stage pipeline contracts (Path Sheet / Analysis Artifact / Delivery Note / QA Verdict) | `engine/pipeline-contract.md` |
| Dimension registry (6 paradigms + 6 roles, addressable pointer layer) | `engine/dimension-registry.md` |
| Executable orchestrator (code-driven 4-stage chain; WP-RO-01/02/03 + WP-X-05 coded engines) | `../src/pipeline.py` |
| AI Agent methodology (4-stage chain: routing, analysis, report, QA) | `.claude/skills/` |
| Version management strategy and release process | `../docs/VERSION-MANAGEMENT.md` |

---

## Version History

| Version | Date | Milestone |
|---|---|---|
| v0.0.6 | 2026-07-21 | Hotfix: installer unzip fallback chain — GNU tar (Linux) cannot extract zip; install.js now tries unzip -> tar -> PowerShell (caught by the new CI npm-installer-smoke job on day one) |
| v0.0.5 | 2026-07-21 | Engineering hardening: SRI runtime rule parsing; drift guards; input validation + error isolation; path_sheet semantic validation; checker release/dependency gates; CI windows+npm+pip expansion |
| v0.0.4 | 2026-07-21 | Residual convergence: round interpolation + §8.5 recompute; PM four-dimension by-name split; §6.3 synergy implemented; systemic-warning examples re-derived (GFC/Eurozone/COVID/2026) |
| v0.0.3 | 2026-07-21 | Single-source convergence: paradigm taxonomy adjudication + full propagation; 13→19 GICS migration; machine-generated contagion derived tables; engine correctness rework (concentration/outlook/contagion); skills cleanup; naming convergence |
| v0.0.2 | 2026-07-21 | Consistency convergence: paradigm taxonomy unified on industry-framework P1-P6; 13→19-industry document migration; contagion derived tables machine-generated; concentration/outlook/contagion engine corrections; skills ghost references purged |
| v0.0.1 | 2026-07-18 | Initial release: international fixed-income credit analysis engine |

---

*Last updated: 2026-07-21*
