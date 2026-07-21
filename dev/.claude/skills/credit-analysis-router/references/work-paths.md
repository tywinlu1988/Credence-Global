# Work Path Routing View

**Version**: v0.0.2

> This table is a condensed routing view of `dev/engine/work-path-registry.md`, for `credit-analysis-router` matching. It only lists path ID / name / role / status / one-liner trigger pattern. It contains no engine thresholds, weights, or rating mappings — the canonical rules are defined by the engine documents referenced via the registry's `engine_sequence`.

| Path ID | Name | Role | Status | Trigger Pattern (One-Liner) |
|---|---|---|---|---|
| WP-CS-01 | Single-Issuer Rating | Credit Selector | ✅ active | Single issuer credit rating |
| WP-CS-02 | LGD + External Support Add-On | Credit Selector | 🟡 partial | LGD/recovery rate/external support on top of issuer rating |
| WP-PM-01 | Investment Dashboard | Portfolio Manager | ✅ active | Single-bond relative value / sector fit / curve / event four-dimension assessment |
| WP-PM-02 | Comparative Analysis | Portfolio Manager | 🟡 partial | Forward comparison of two issuers, pick one |
| WP-AD-01 | Origination Assessment | Advisor | 🔴 planned | Underwriting feasibility / pricing range (under development) |
| WP-TR-01 | Market Watch Signal Card | Trader | 🟡 partial | Single-bond L0 quick-scan signal linked to systemic thermometer |
| WP-RO-01 | Concentration Assessment | Risk Officer | ✅ active | Portfolio five-dimensional concentration (industry/region/rating/tenor/channel) |
| WP-RO-02 | Cross-Industry Contagion | Risk Officer | ✅ active | Cross-industry transmission within portfolio and high-contagion chains |
| WP-RO-03 | Systemic Risk Reading | Risk Officer | ✅ active | Market-wide systemic risk index and thermometer level |
| WP-RO-04 | Portfolio Stress Test | Risk Officer | 🟡 partial | Portfolio loss assessment under extreme scenarios |
| WP-II-01 | Decision Support | Individual Investor | 🔴 planned | Financing channel comparison and timing (under development) |
| WP-X-01 | Black Swan Backtest Validation | Meta | ✅ active | Historical default dual-timepoint backtest to validate framework effectiveness |
| WP-X-02 | Multi-Role Parallel Assessment | Meta | ✅ active | Single-subject multi-role parallel assessment with consensus/divergence matrix |
| WP-X-03 | Industry Framework Builder | Meta | ✅ active | New industry pyramid and ten-dimension scoring framework building |
| WP-X-04 | ESG/Governance Risk Scan | Meta | 🟡 partial | ESG overlay and governance/fraud red-flag scanning |
| WP-X-05 | Outlook & Continuous Monitoring | Meta | ✅ active | Rating outlook / watchlist / continuous monitoring |

> Status distribution: **9 active, 5 partial, 2 planned**. When recommending planned paths (WP-AD-01, WP-II-01), honestly state "this path is under development" and provide alternative active paths. Do not fabricate capabilities.
