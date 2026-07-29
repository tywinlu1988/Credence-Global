# WP-CS-02 Execution Contract — LGD + External Support Add-On

**Status**: ✅ active · **Role**: credit-selector · **Object**: single-issuer · **Depth**: special

> This playbook is the execution contract for WP-CS-02. Read it fully before starting.
> AGENTS.md Non-Negotiables apply. This path is an **add-on**: it layers on top of the
> WP-CS-01 main rating result — do not run it standalone without a completed rating.

## 1. Trigger & Scope

Use when: the user needs facility-level LGD assessment ("what's the recovery rate if this defaults", "LGD tier for this bond"), external support uplift ("does government/group support boost the rating"), or credit-enhancement impact on a rated issuer.
Do not use when: main credit rating (→ WP-CS-01 first, then this as add-on), portfolio-level concentration (→ WP-RO-01), systemic/contagion (→ WP-RO-02/03), multi-stakeholder review (→ WP-X-02).

## 2. Required Reading Order

1. `${CLAUDE_PLUGIN_ROOT}/engine/lgd-recovery-framework.md` — LGD five-tier classification, collateral valuation, recovery path
2. `${CLAUDE_PLUGIN_ROOT}/engine/external-support-framework.md` — government/group/strategic support assessment

## 3. Procedure

1. **Verify prerequisite** — WP-CS-01 main rating must be complete before this add-on runs. The add-on refines the rating for a specific facility, not a standalone assessment.
2. **LGD tiering** — Map the facility to one of five LGD tiers (L1-L5) per `lgd-recovery-framework.md` §2: L1 (0-20%, senior secured prime collateral) through L5 (80-100%, deeply subordinated / unsecured distressed). Collateral type, seniority, and jurisdiction determine placement.
3. **Recovery estimate** — Factor in enforcement timeline, jurisdiction efficiency, and collateral liquidation discounts per §3.
4. **External support assessment** — Per `external-support-framework.md` §3, evaluate government support capacity (fiscal capacity, strategic importance, track record) and group/strategic support (ownership, integration, historical support). Grade as: Strong / Moderate / Weak / None.
5. **Support uplift** — Apply support uplift to the base rating per §4. The uplift is capped; government support cannot lift a standalone CCC to investment grade.
6. **Output** — LGD tier, recovery rate estimate, support adjustment recommendation, and the combined facility-level rating.

## 4. Dimension Vocabulary

- LGD tiers: L1-L5 per `lgd-recovery-framework.md` §2 only.
- Collateral types, seniority classes, enforcement timelines: per that document.
- Support capacity dimensions: fiscal capacity, strategic importance, ownership integration, historical precedent per `external-support-framework.md` §3.
- Support grades: Strong / Moderate / Weak / None only — no invented intermediate grades.

## 5. Output Shape

Analysis Artifact per `${CLAUDE_PLUGIN_ROOT}/engine/pipeline-contract.md` §2.2 (add-on refinement, layered on WP-CS-01 base).
Path outputs (registry): LGD tier + recovery rate, external support adjustment recommendation.

## 6. Templates

- `${CLAUDE_PLUGIN_ROOT}/templates/template-type8.html` — LGD Assessment
- `${CLAUDE_PLUGIN_ROOT}/templates/template-type9.html` — External Support

Render via `credit-report-builder` using exactly these files; no ad-hoc layouts.

## 7. Quality Gates (all must pass)

- `Five-Tier LGD Classification (${CLAUDE_PLUGIN_ROOT}/engine/lgd-recovery-framework.md §2)`
- `Support Capacity (${CLAUDE_PLUGIN_ROOT}/engine/external-support-framework.md §3)`

## 8. Drift Blacklist (forbidden)

- Running this add-on before WP-CS-01 main rating (no standalone LGD/support assessment without a base rating).
- Inventing LGD tiers outside L1-L5 or fabricating recovery rates without collateral/seniority basis.
- Inventing support grades outside Strong/Moderate/Weak/None, or assigning support uplift without evaluating capacity.
- Fabricating government fiscal data or group financials (Mode B: treat absent data as data gaps per mosaic-engine §6).
- Numeric claims without a `doc §section` citation.
- Designing ad-hoc HTML/dashboards/templates.
- Delivering before `credit-qa-verifier` issues a passing QA Verdict.
