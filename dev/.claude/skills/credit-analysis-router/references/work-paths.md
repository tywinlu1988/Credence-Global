# Work Path Routing View

**Version**: v0.0.2

> This table is a condensed routing view of `dev/engine/work-path-registry.md`, for `credit-analysis-router` matching. It only lists path ID / name / role / status / one-liner trigger pattern. It contains no engine thresholds, weights, or rating mappings — the canonical rules are defined by the engine documents referenced via the registry's `engine_sequence`.

| Path ID | Name | Role | Status | Trigger Pattern (One-Liner) |
|---|---|---|---|---|
| WP-CS-01 | Credit Approval Single-Issuer Rating | M0 Credit Approval | ✅ active | Single issuer credit approval rating |
| WP-CS-02 | Credit Approval Add-On Package (LGD+External Support) | M0 Credit Approval | 🟡 partial | LGD/recovery rate/external support on top of issuer rating |
| WP-PM-01 | Bond Investment Dashboard | M1 Investment | ✅ active | Single-bond relative value / terms / liquidity / event four-dimensional assessment |
| WP-PM-02 | Dual-Issuer Forward Comparison | M1 Investment | 🟡 partial | Forward comparison of two issuers, pick one |
| WP-AD-01 | Underwriting Feasibility Assessment | M2 Underwriting | 🔴 planned | Issuance window / investor matching / comparable pricing (pending) |
| WP-TR-01 | Trading Market-Watch Signal Card | M3 Trading | 🟡 partial | Single-bond L0 quick-scan signal linked to systemic thermometer |
| WP-RO-01 | Portfolio Concentration Assessment | M4 Risk Control | ✅ active | Portfolio five-dimensional concentration (industry/region/rating/tenor/channel) |
| WP-RO-02 | Cross-Industry Contagion Analysis | M4 Risk Control | ✅ active | Cross-industry transmission within portfolio and high-contagion chains |
| WP-RO-03 | Systemic Risk Reading | M4 Risk Control | ✅ active | Market-wide systemic risk index and thermometer level |
| WP-RO-04 | Portfolio Stress Test | M4 Risk Control | 🟡 partial | Portfolio loss assessment under extreme scenarios |
| WP-II-01 | Corporate Financing Advisor | M5 Financing | 🔴 planned | Financing channel comparison and timing (pending) |
| WP-X-01 | Black Swan Backtest Validation | Meta Validation | ✅ active | Historical default dual-timepoint backtest to validate framework effectiveness |
| WP-X-02 | Multi-Role Parallel Assessment | Meta Comparison | ✅ active | Single-subject multi-role parallel assessment with consensus/divergence matrix |
| WP-X-03 | Industry Analysis Framework Builder | Meta Builder | ✅ active | New industry pyramid and ten-dimension scoring framework building |
| WP-X-04 | ESG/Governance Risk Scan | Special | 🟡 partial | ESG overlay and governance/fraud red-flag scanning |
| WP-X-05 | Outlook & Continuous Monitoring | Special | 🟡 partial | Rating outlook/watchlist/continuous monitoring (template pending) |

> Status distribution: 8 active, 6 partial, 2 planned. When recommending planned paths (WP-AD-01, WP-II-01), honestly state "this path is pending development" and provide alternative active paths. Do not fabricate capabilities.
