# Path → Template → Tier Mapping View

**Version**: v0.0.1

> This table is an assembly mapping view for `credit-report-builder`: given a `path_id`, it lists the templates and primary tier to use. The single source of truth for the template list is `dev/engine/work-path-registry.md` (the `templates` field of each path); the single source of truth for tier semantics is `dev/engine/output-layered-framework.md` §§2/3/5. This table contains no thresholds, tier time budgets, or rating values — all numeric judgments are subject to the referenced engine documents. In case of any inconsistency between this table and those two documents, the latter take precedence.

## Assembly Mapping

| Path ID | Name | Depth | Primary Tier | Templates |
|---|---|---|---|---|
| WP-CS-01 | Credit Selector Single-Issuer Rating | L2 | L2 Deep Report | template-type1 + template-type6 |
| WP-CS-02 | Credit Selector Add-On (LGD+External Support) | Special | Special (template-defined) | template-type8 + template-type9 |
| WP-PM-01 | Portfolio Manager Investment Dashboard | L2 | L2 Deep Report | template-type5 |
| WP-PM-02 | PM Comparative Analysis | L2 | L2 Deep Report | template-type2 |
| WP-AD-01 | Advisor Origination Assessment | Special | Special (template-defined) | planned |
| WP-TR-01 | Trader Market Watch Signal Card | L0 | L0 Signal Card | L0-spec |
| WP-RO-01 | Risk Officer Concentration Assessment | Special | Special (template-defined) | template-type14 |
| WP-RO-02 | Risk Officer Cross-Industry Contagion | Special | Special (template-defined) | template-type13 |
| WP-RO-03 | Risk Officer Systemic Risk Reading | Special | Special (template-defined) | template-type15 |
| WP-RO-04 | Risk Officer Portfolio Stress Test | Special | Special (template-defined) | template-type11 |
| WP-II-01 | Individual Investor Decision Support | Special | Special (template-defined) | planned |
| WP-X-01 | Black Swan Backtest Validation | Special | Special (template-defined) | template-type3 |
| WP-X-02 | Multi-Role Parallel Assessment | L2 | L2 Deep Report | template-type4 |
| WP-X-03 | Industry Framework Builder | Special | Special (template-defined) | template-type7 |
| WP-X-04 | ESG/Governance Risk Scan | Special | Special (template-defined) | template-type10 |
| WP-X-05 | Outlook & Continuous Monitoring | Special | Special (template-defined) | template-type18 |

## Tier Pointers (Single Source of Truth)

- Three-layer output overview and navigation relationship: `dev/engine/output-layered-framework.md` §2
- L0 Signal Card (layout/elements/thermometer card): `dev/engine/output-layered-framework.md` §3
- L1 Snapshot (four-dimensional radar/key anomalies/rating comparison/ranking): `dev/engine/output-layered-framework.md` §4
- L2 Deep Report (four-panel structure/navigation rules): `dev/engine/output-layered-framework.md` §5
- Completeness indicator presentation: `dev/engine/output-layered-framework.md` §8.4

## Template Marker Values (Consistent with Registry §schema)

- `planned`: Template pending development (no file exists); honestly state "pending development," do not fabricate rendered output.
- `L0-spec`: No standalone template file; specification is defined in the referenced engine document (L0 signal card specification see `dev/engine/output-layered-framework.md` §3).

> Depth tier `L0/L1/L2` determines the primary tier; deliverables for `Special` paths are defined by the selected template, with tier semantics still governed by the aforementioned engine documents.
