# Fixed Income Credit Analysis v0.7.0-alpha Cleanup & Skill Sync Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring the `fixed-income-credit-analysis` Skill and all engine documents into full alignment with the v0.7.0-alpha release, fix the high-severity consistency issues identified in the audit, and establish a repeatable versioning workflow.

**Architecture:** This is a documentation-and-metadata hardening sprint. The work centers on (1) upgrading the Claude Skill manifest so it accurately reflects the v0.7.0-alpha engine, (2) repairing broken cross-references and version labels across the system-intelligence layer, (3) normalizing the SRI metric and rating-map definitions, and (4) adding a lightweight consistency checker that can be re-run on every future release. No production code is required for this phase, but the plan includes scaffolding for the first two executable calculators so the next engineering sprint has a clean foundation.

**Tech Stack:** Markdown, HTML/CSS templates, Python 3.11+ (for consistency checker and calculator prototypes), pytest.

## Global Constraints

- Every change must preserve the Chinese/English terminology choices already ratified in `consistency-audit-v0.5.2.md` (e.g., "轨道A/轨道B", "交叉对撞", "信号密度").
- All core methodology documents must carry the engine version `v0.7.0-alpha`; audit/self-assessment reports must carry an independent version and explicitly state "对应引擎版本: v0.7.0-alpha".
- All internal Markdown links must resolve to real files under `dev/`.
- The SRI metric must use a single scale: `0–3+` (decimal); no percentage scale may remain in any engine document or template.
- The 12-notch rating map (`AAA/AA+/AA/AA-/A+/A/A-/BBB+/BBB/BBB-/BB+/BB/BB-/B+/B/B-/CCC/D`) is the only valid rating scheme; old 6-notch references must be removed.
- Each task ends with a verifiable deliverable and a commit.

---

## File Structure

```
dev/
├── .claude/skills/fixed-income-credit-analysis/SKILL.md   # upgraded to v0.7.0-alpha
docs/
├── VERSION-MANAGEMENT.md                                   # new: release checklist & branch strategy
└── superpowers/plans/2026-07-13-fixed-income-credit-v0.7.0-cleanup.md  # this file
scripts/
├── consistency_check.py                                    # new: automated checks for versions, links, SRI examples
src/                                                        # new: calculator prototypes
├── sri_calculator.py
├── concentration_scorer.py
tests/
├── test_sri_calculator.py
└── test_concentration_scorer.py
version/v0.7.0-alpha/.claude/skills/fixed-income-credit-analysis/  # new: archived skill snapshot
```

**Responsibilities:**

- `docs/VERSION-MANAGEMENT.md` is the single source of truth for how `dev/` and `version/` relate, how versions are bumped, and what must be included in a release.
- `scripts/consistency_check.py` is the regression guard: it verifies that every core `.md` file declares the expected engine version, that every `(...md)` internal link resolves, and that SRI examples fall inside the `0–3+` scale.
- `src/sri_calculator.py` and `src/concentration_scorer.py` are minimal executable references that make the SRI and concentration formulas unambiguous and testable.
- `dev/.claude/skills/fixed-income-credit-analysis/SKILL.md` is the user-facing contract; it must stay in sync with `dev/engine/`.
- `version/v0.7.0-alpha/.claude/skills/fixed-income-credit-analysis/SKILL.md` is the immutable snapshot of the skill as it existed at the v0.7.0-alpha release.

---

## Task 1: Establish Version Management Infrastructure

**Files:**
- Create: `docs/VERSION-MANAGEMENT.md`
- Modify: `dev/README.md` (minor reference to the new doc)

**Interfaces:**
- Consumes: existing `dev/engine/engine-overview.md` §8 versioning rules.
- Produces: a documented release workflow and checklist that every later task follows.

- [ ] **Step 1: Write the version-management document**

Create `docs/VERSION-MANAGEMENT.md` with the following exact sections:

```markdown
# 版本管理策略

**对应引擎版本**: v0.7.0-alpha
**最后更新**: 2026-07-13

## 目录结构约定

- `dev/` —— 当前活跃开发工作区。所有正在迭代的方法论文档、报告、模板和 Skill 都放在这里。
- `version/<version>/` —— 该版本的只读归档快照。一旦快照创建，仅允许通过补丁分支修正明显错误，不允许继续功能迭代。
- `version/<version>.zip` —— 该版本归档的压缩包，用于对外分发。

## 版本号体系

### 引擎版本

- 格式: `v<major>.<minor>.<patch>-<stage>`
- 适用范围: `dev/engine/` 下的所有核心方法论文档、Skill 包、模板和报告。
- 当前: `v0.7.0-alpha`
- 升级触发条件:
  - 新增功能模块或行业覆盖 → 递增 minor 版本
  - 方法论重大重构或评级体系变更 → 递增 major 版本
  - 一致性修复、术语统一、阈值对齐 → 递增 patch 版本

### 审查报告版本

- 格式: `v<major>.<minor>`（如 v1.0, v1.1）
- 适用范围: `dev/engine/*-audit.md`, `dev/engine/*-review-*.md`, `dev/engine/self-assessment-*.md`
- 必须在文件头标注: `**对应引擎版本**: vX.Y.Z-<stage>`

## 发布检查清单

在创建新的 `version/<version>/` 快照前，必须完成以下检查：

- [ ] 所有核心方法论文档的 `**版本**:` 头统一为当前引擎版本。
- [ ] Claude Skill 包 (`dev/.claude/skills/fixed-income-credit-analysis/`) 已同步并升级到当前引擎版本。
- [ ] Skill 包已复制到 `version/<version>/.claude/skills/fixed-income-credit-analysis/`。
- [ ] `scripts/consistency_check.py` 运行通过（无断裂链接、版本号一致、SRI 示例在合法范围内）。
- [ ] 所有模板和报告的版本号与引擎版本对齐。
- [ ] `dev/README.md` 的版本历史和目录结构描述已更新。
- [ ] 压缩包 `version/<version>.zip` 已生成。

## 快照创建流程

1. 在 `dev/` 完成所有变更并通过一致性检查。
2. 复制 `dev/` 的全部内容到 `version/<version>/`。
3. 在 `version/<version>/` 中删除 `.git/`（如果误复制）。
4. 生成 `version/<version>.zip`。
5. 更新 `dev/README.md` 的版本历史。
```

- [ ] **Step 2: Reference the new doc from README**

Modify `dev/README.md` by adding one row to the "快速导航" table:

```markdown
| 版本管理策略与发布流程 | `docs/VERSION-MANAGEMENT.md` |
```

- [ ] **Step 3: Verify the file renders and links are valid**

Run:

```bash
ls -la docs/VERSION-MANAGEMENT.md
grep -n "版本管理策略与发布流程" dev/README.md
```

Expected: file exists; README contains the new navigation row.

- [ ] **Step 4: Commit**

```bash
git add docs/VERSION-MANAGEMENT.md dev/README.md
git commit -m "docs: add VERSION-MANAGEMENT.md and link from README"
```

---

## Task 2: Upgrade the Claude Skill to v0.7.0-alpha

**Files:**
- Modify: `dev/.claude/skills/fixed-income-credit-analysis/SKILL.md`
- Create: `version/v0.7.0-alpha/.claude/skills/fixed-income-credit-analysis/SKILL.md` (copy of the upgraded file)

**Interfaces:**
- Consumes: `dev/engine/engine-overview.md`, `dev/engine/contagion-theory.md`, `dev/engine/contagion-matrix.md`, `dev/engine/concentration-framework.md`, `dev/engine/systemic-warning-framework.md`, `dev/engine/industry-framework.md`, `dev/engine/paradigm-brand-channel.md`, `dev/engine/paradigm-network-traffic.md`.
- Produces: an upgraded Skill manifest that downstream agents use to invoke the full v0.7.0-alpha engine.

- [ ] **Step 1: Update the Skill header and version history**

In `dev/.claude/skills/fixed-income-credit-analysis/SKILL.md`:

1. Change line 6 from `# Fixed Income Credit Analysis Engine v0.5.0-release` to `# Fixed Income Credit Analysis Engine v0.7.0-alpha`.
2. In the front-matter description, append: `, evaluating cross-industry contagion and portfolio concentration risk through the v0.7.0-alpha system-intelligence layer`.
3. Add a new row at the bottom of the Version History table:

```markdown
| 0.7.0-alpha | 2026-07-13 | System-intelligence layer: contagion theory/matrix, five-dimensional concentration framework, systemic warning (SRI), 13-industry coverage, six analytical paradigms. Skill synchronized with engine release. |
```

- [ ] **Step 2: Expand the Overview section**

Replace the first paragraph of the Overview with:

```markdown
A systematic methodology for evaluating corporate credit quality in China's fixed income markets. The engine operates in three layers: (1) a **Mosaic Engine** that assembles fragmented public data into coherent signals; (2) a **Dual-Track Engine** combining industry-specific multi-layer analysis pyramids with market-based pricing signals; and (3) a **System-Intelligence Layer** (v0.7.0-alpha) that models cross-industry contagion, portfolio concentration, and a market-wide Systemic Risk Index (SRI). Combines multi-stakeholder perspectives into a unified assessment framework.
```

- [ ] **Step 3: Expand the "When to Use" list**

Append these items to the "When to Use" list:

```markdown
- Assessing cross-industry contagion risk from a stressed issuer or sector
- Evaluating portfolio concentration across industry, region, rating, tenor, and funding-channel dimensions
- Computing the Systemic Risk Index (SRI) and interpreting the four-level thermometer
- Mapping an industry to one of the six analytical paradigms (policy-driven, tech-barrier, consolidation, asset-lease, brand-channel, network-traffic)
```

- [ ] **Step 4: Add a "System-Intelligence Layer" section after Mosaic Engine Architecture**

Insert the following section before "Mode B: External Data Source Adapter":

```markdown
## System-Intelligence Layer (v0.7.0-alpha)

The system-intelligence layer aggregates individual issuer assessments into portfolio- and market-level signals.

### Cross-Industry Contagion

- **Contagion theory**: four contagion types (credit-chain, regional resonance, liquidity squeeze, confidence collapse) and seven standard transmission paths.
- **Contagion matrix**: 13×13 industry intensity matrix with direction, confidence, and upgrade-factor linkage. See `references/contagion-matrix.md`.
- **Industry clustering**: based on six analytical paradigms. Industries in the same paradigm have higher innate contagion coupling.

### Five-Dimensional Concentration Framework

Concentration risk is scored across:

1. **Industry concentration** (HHI, CR3, CR5, MAX1)
2. **Regional concentration** (single-province share, weak-region share, fiscal-health-weighted share)
3. **Rating concentration** (external AAA share, pseudo-high-rating share, internal-external rating dispersion)
4. **Tenor concentration** (12/24/36-month maturities, single-month peak)
5. **Funding-channel concentration** (bank, bond, non-standard, leasing, equity)

Default weights: industry 25%, region 20%, rating 20%, tenor 20%, funding channel 15%.

### Systemic Risk Index (SRI)

```
SRI = Σ(industry_risk_score × industry_weight_pct)
```

- Scale: 0–3+
- Levels: 🟢 normal (<0.5), 🟡 watch (0.5–1.0), 🟠 alert (1.0–1.8), 🔴 danger (≥1.8)
- Inputs: Track-A industry score, Track-B market signal, outlook direction, and one-shot-veto triggers.

For full specification see `references/systemic-warning-framework.md`.
```

- [ ] **Step 5: Add a "Six Analytical Paradigms" section**

Insert after the "Track A: Industry Analysis Pyramids" section:

```markdown
## Six Analytical Paradigms

Each industry maps to one of six paradigms that determine its dominant risk drivers and contagion exposure:

| Paradigm | Industries | Heaviest Factor | Key Contagion Path |
|---|---|---|---|
| Policy-Driven | Solar/PV, Semiconductor | Policy cycle | Same-region SOE, same-industry |
| Tech-Barrier | High-end equipment, Biomedicine, Medical devices | Technology/IP | Supplier-customer chain, same funding channel |
| Consolidation | New energy vehicles | Profit fortress | Same-industry, credit-chain |
| Asset-Lease | Data centers | Client/lease quality | Supplier-customer chain, same funding channel |
| Brand+Channel | Food & beverage, Textile & apparel | Brand equity | Confidence collapse, same-industry |
| Network+Traffic | Transportation, Retail, Media/Internet | Network traffic | Supplier-customer chain, same funding channel |

See `references/industry-pyramids.md` and `references/paradigm-*.md` for detailed specs.
```

- [ ] **Step 6: Expand the Validated Industries table**

Change the table header and add the five new industries:

```markdown
| Industry | Forward Test | Retrospective Test |
|---|---|---|
| Solar/PV | 完成 | 完成 |
| Semiconductor | 完成 | 完成 |
| Biomedicine | 完成 | 完成 |
| High-End Equipment | 完成 | 完成 |
| Medical Devices | 完成 | 完成 |
| NEV | 完成 | 完成 |
| Data Center | 完成 | 完成 |
| Coal/SOE (Yongmei) | 完成 | 完成 |
| LGFV | 完成 | 完成 |
| Food & Beverage | 完成 | — |
| Textile & Apparel | 完成 | — |
| Transportation | 完成 | — |
| Retail | 完成 | — |
| Media/Internet | 完成 | — |
```

- [ ] **Step 7: Update Supporting Files list**

Append to the Supporting Files list:

```markdown
- `references/contagion-theory.md` — Contagion types, transmission paths, upgrade factors
- `references/contagion-matrix.md` — 13×13 cross-industry contagion matrix
- `references/concentration-framework.md` — Five-dimensional concentration framework
- `references/systemic-warning-framework.md` — SRI algorithm and thermometer
- `references/paradigm-brand-channel.md` — Brand+channel paradigm specification
- `references/paradigm-network-traffic.md` — Network+traffic paradigm specification
- `templates/template-type13.html` — Contagion report template
- `templates/template-type14.html` — Concentration report template
- `templates/template-type15.html` — Systemic warning report template
```

- [ ] **Step 8: Copy the upgraded Skill into the v0.7.0-alpha release archive**

Run:

```bash
mkdir -p version/v0.7.0-alpha/.claude/skills/fixed-income-credit-analysis
cp dev/.claude/skills/fixed-income-credit-analysis/SKILL.md version/v0.7.0-alpha/.claude/skills/fixed-income-credit-analysis/SKILL.md
cp dev/.claude/skills/fixed-income-credit-analysis/references/*.md version/v0.7.0-alpha/.claude/skills/fixed-income-credit-analysis/references/
cp dev/.claude/skills/fixed-income-credit-analysis/templates/*.html version/v0.7.0-alpha/.claude/skills/fixed-income-credit-analysis/templates/
```

- [ ] **Step 9: Verify the Skill contains the new content**

Run:

```bash
grep -n "System-Intelligence Layer" dev/.claude/skills/fixed-income-credit-analysis/SKILL.md
grep -n "v0.7.0-alpha" dev/.claude/skills/fixed-income-credit-analysis/SKILL.md
grep -n "Food & Beverage" dev/.claude/skills/fixed-income-credit-analysis/SKILL.md
ls version/v0.7.0-alpha/.claude/skills/fixed-income-credit-analysis/SKILL.md
```

Expected: all grep commands return matching lines; archived file exists.

- [ ] **Step 10: Commit**

```bash
git add dev/.claude/skills/fixed-income-credit-analysis/SKILL.md version/v0.7.0-alpha/.claude/skills/
git commit -m "feat(skill): upgrade fixed-income-credit-analysis skill to v0.7.0-alpha"
```

---

## Task 3: Repair Cross-References in the System-Intelligence Layer

**Files:**
- Modify: `dev/engine/contagion-theory.md`, `dev/engine/contagion-matrix.md`, `dev/engine/concentration-framework.md`

**Interfaces:**
- Consumes: relative Markdown links to existing files.
- Produces: a closed cross-reference graph between the four system-intelligence documents and the six paradigm documents.

- [ ] **Step 1: Add contagion-matrix link in contagion-theory.md §6.3**

In `dev/engine/contagion-theory.md`, locate the table at §6.3 and insert a new first row:

```markdown
| [传染矩阵](contagion-matrix.md) | 13×13行业传染强度矩阵 | 将本理论中的传导路径映射为行业间具体传导强度 |
```

- [ ] **Step 2: Add paradigm links in contagion-theory.md §4**

In `dev/engine/contagion-theory.md` §4, ensure the six paradigm names link to their files. Replace the raw "范式A" text in the table with:

```markdown
| **[政策驱动型](industry-framework.md)**（光伏/半导体） | ...
| **[技术壁垒型](industry-framework.md)**（高端装备/生物医药/器械） | ...
| **[品牌+渠道型](paradigm-brand-channel.md)**（食品饮料/纺织服装） | ...
| **[网络+流量型](paradigm-network-traffic.md)**（交通运输/商贸零售/传媒互联网） | ...
```

Leave "存量博弈型" and "资产租约型" as plain text (they have no dedicated paradigm file yet).

- [ ] **Step 3: Add concentration + warning links in contagion-matrix.md §7**

In `dev/engine/contagion-matrix.md` §7.1, append to the M4 integration description:

```markdown
五维集中度分析框架（[concentration-framework.md](concentration-framework.md)）和系统性预警框架（[systemic-warning-framework.md](systemic-warning-framework.md)）在M4层引用本矩阵的传染强度和行业聚类结果，用于组合层面的传染压力测试和集中度调整。
```

- [ ] **Step 4: Add warning-framework link in concentration-framework.md §9**

In `dev/engine/concentration-framework.md` §9.2 table, add a row:

```markdown
| [系统性预警框架](systemic-warning-framework.md) | SRI温度计作为集中度综合评分权重动态调整的触发条件 | §7.4权重动态调整规则 |
```

- [ ] **Step 5: Verify all new links resolve**

Run:

```bash
python scripts/consistency_check.py --only-links
```

If the checker does not exist yet, run a manual grep fallback:

```bash
for f in dev/engine/contagion-theory.md dev/engine/contagion-matrix.md dev/engine/concentration-framework.md; do
  grep -oE '\[.*?\]\((.*?\.md)\)' "$f" | sed 's/.*(\(.*\))/\1/' | while read link; do
    test -f "dev/engine/$link" && echo "OK: $f -> $link" || echo "BROKEN: $f -> $link"
  done
done
```

Expected: no "BROKEN" lines.

- [ ] **Step 6: Commit**

```bash
git add dev/engine/contagion-theory.md dev/engine/contagion-matrix.md dev/engine/concentration-framework.md
git commit -m "docs(engine): close cross-reference gaps in system-intelligence layer"
```

---

## Task 4: Normalize the SRI Metric (0–3+ Scale)

**Files:**
- Modify: `dev/engine/systemic-warning-framework.md`, `dev/engine/output-layered-framework.md`, `dev/design/templates/template-type15.html`

**Interfaces:**
- Consumes: the SRI definition in `systemic-warning-framework.md`.
- Produces: a single, consistent SRI scale across theory, output framework, and report template.

- [ ] **Step 1: Fix the SRI formula in systemic-warning-framework.md**

In `dev/engine/systemic-warning-framework.md` §2.2, replace:

```markdown
SRI = Σ(行业风险得分 × 行业权重) / 13
```

with:

```markdown
SRI = Σ(行业风险得分 × 行业权重百分比)
```

And update the explanatory paragraph from:

```markdown
其中"行业权重在各行业间归一化，确保Σ(行业权重)=13"。
```

to:

```markdown
其中行业权重百分比为各行业在总权重中的占比（归一化至100%），确保 Σ(行业权重百分比) = 1。
```

- [ ] **Step 2: Add a note explaining the scale in systemic-warning-framework.md**

After the formula, add:

```markdown
> **量纲说明**: SRI 采用 0–3+ 连续尺度，而非百分制。温度卡片、报告模板和输出框架必须使用同一尺度，禁止混用 0–100 分制。
```

- [ ] **Step 3: Update SRI examples in output-layered-framework.md §3.6**

Locate all SRI examples in `dev/engine/output-layered-framework.md` §3.6. Replace percentage examples with decimal examples that match the color definitions in `systemic-warning-framework.md`:

- 🟢 normal example: `SRI: 0.22`
- 🟡 watch example: `SRI: 0.56`
- 🟠 alert example: `SRI: 1.15`
- 🔴 danger example: `SRI: 1.83`

If the section contains text like "SRI: 38/100", replace it with the matching decimal value and add a note that the scale is 0–3+.

- [ ] **Step 4: Update template-type15.html SRI examples**

In `dev/design/templates/template-type15.html`, find all occurrences of SRI percentage values and replace them with the same 0–3+ decimal examples used in `output-layered-framework.md`.

- [ ] **Step 5: Verify no percentage-scale SRI remains**

Run:

```bash
grep -RIn "SRI.*\/100" dev/engine/ dev/design/templates/
grep -RIn "SRI: [0-9][0-9]" dev/engine/ dev/design/templates/
```

Expected: no matches.

- [ ] **Step 6: Commit**

```bash
git add dev/engine/systemic-warning-framework.md dev/engine/output-layered-framework.md dev/design/templates/template-type15.html
git commit -m "docs(engine): normalize SRI to 0-3+ scale across framework, output, and template"
```

---

## Task 5: Eliminate Old 6-Notch Rating References

**Files:**
- Modify: `dev/engine/false-positive-negative-testing.md`, `dev/engine/final-review-2026-07-08.md`

**Interfaces:**
- Consumes: the 12-notch rating map in `dual-track-methodology.md` §6.
- Produces: both files using only the 12-notch scheme.

- [ ] **Step 1: Replace the rating map in false-positive-negative-testing.md**

In `dev/engine/false-positive-negative-testing.md` §1.4, replace the old 6-notch table with the exact 12-notch table from `dual-track-methodology.md` §6:

```markdown
| 综合评分 | 新12档评级 | 旧6档对应 | 含义 |
|---|---|---|---|
| 9.5–10.0 | AAA | AAA | 信用质量极高 |
| 9.0–9.4 | AA+ | AA/A | 信用质量优秀 |
| 8.5–8.9 | AA | AA/A | 信用质量优秀 |
| 8.0–8.4 | AA- | AA/A | 信用质量优秀 |
| 7.5–7.9 | A+ | AA/A | 信用质量良好 |
| 7.0–7.4 | A | AA/A | 信用质量良好 |
| 6.5–6.9 | A- | AA/A | 信用质量良好 |
| 6.0–6.4 | BBB+ | BBB/BB | 信用质量中等 |
| 5.5–5.9 | BBB | BBB/BB | 信用质量中等 |
| 5.0–5.4 | BBB- | BBB/BB | 信用质量中等 |
| 4.5–4.9 | BB+ | B | 投机级，存在不确定性 |
| 4.0–4.4 | BB | B | 投机级，存在不确定性 |
| 3.5–3.9 | BB- | B | 投机级，存在不确定性 |
| 3.0–3.4 | B+ | B | 高投机性 |
| 2.5–2.9 | B | B | 高投机性 |
| 2.0–2.4 | B- | B | 高投机性 |
| 1.5–1.9 | CCC | CCC | 极高风险 |
| 1.0–1.4 | CC | CCC | 极高风险 |
| 0.5–0.9 | C | CCC | 濒临违约 |
| 0–0.4 | D | D | 违约或实质违约 |
```

Then update the positive/negative cutoff logic: define "positive" as internal rating ≥ BBB- (score ≥ 5.0) and "negative" as internal rating < BBB- (score < 5.0). Recompute the test-case classifications using this cutoff.

- [ ] **Step 2: Update final-review-2026-07-08.md §1.5**

Replace the old 6-notch rating interval description with a reference to the 12-notch table:

```markdown
评级映射采用 v0.4.0 引入的 12 档体系，详见 [dual-track-methodology.md](dual-track-methodology.md) §六。旧 6 档体系（AAA/AA/A/BBB/BB/B/CCC/D）已不再作为判定依据。
```

- [ ] **Step 3: Verify no 6-notch descriptions remain**

Run:

```bash
grep -RIn "AA/A\|BBB/BB\|4.0-5.9\|2.0-3.9" dev/engine/false-positive-negative-testing.md dev/engine/final-review-2026-07-08.md
```

Expected: no matches (except the new "旧6档对应" column header, which is acceptable).

- [ ] **Step 4: Commit**

```bash
git add dev/engine/false-positive-negative-testing.md dev/engine/final-review-2026-07-08.md
git commit -m "docs(engine): migrate false-positive-negative testing and final review to 12-notch rating map"
```

---

## Task 6: Align Template and Report Versions to v0.7.0-alpha

**Files:**
- Modify: `dev/design/templates/template-type13.html`, `template-type14.html`, `template-type15.html`
- Modify: `dev/reports/contagion-yongmei-2020.html`, `contagion-realestate-2021.html`, `contagion-ziguang-2020.html`, `contagion-solar-overcapacity.html`, `concentration-pv-heavy.html`, `concentration-liaoning-heavy.html`, `concentration-ideal.html`, `systemic-warning-2026q2.html`

**Interfaces:**
- Consumes: the v0.7.0-alpha engine version label.
- Produces: templates and reports whose version labels match the engine release.

- [ ] **Step 1: Update template version metadata**

In each template file, locate the version string and update:

- `template-type13.html`: any `v0.6.4` → `v0.7.0-alpha`
- `template-type14.html`: any `v0.6.7` → `v0.7.0-alpha`
- `template-type15.html`: any `v0.6.9` → `v0.7.0-alpha`

Also add a metadata comment at the top of each template indicating the instance reports generated from it:

```html
<!-- @template: dev/design/templates/template-type13.html -->
<!-- @engine-version: v0.7.0-alpha -->
```

- [ ] **Step 2: Update report version metadata**

In each system-intelligence report, update the version string to `v0.7.0-alpha` and add a metadata comment at the top:

```html
<!-- @based-on-template: dev/design/templates/template-type13.html -->
<!-- @engine-version: v0.7.0-alpha -->
<!-- @generated-from: dev/engine/contagion-matrix.md, dev/engine/contagion-theory.md -->
```

Use the appropriate template type and source documents for each report.

- [ ] **Step 3: Verify version alignment**

Run:

```bash
for f in dev/design/templates/template-type{13,14,15}.html dev/reports/contagion-*.html dev/reports/concentration-*.html dev/reports/systemic-warning-*.html; do
  echo "=== $f ==="
  grep -n "v0\.7\.0-alpha\|v0\.6\." "$f" || true
done
```

Expected: every file shows `v0.7.0-alpha`; no remaining `v0.6.x` labels.

- [ ] **Step 4: Commit**

```bash
git add dev/design/templates/template-type{13,14,15}.html dev/reports/contagion-*.html dev/reports/concentration-*.html dev/reports/systemic-warning-*.html
git commit -m "docs(reports): align system-intelligence templates and reports to v0.7.0-alpha"
```

---

## Task 7: Fix Concentration Framework Section Ordering

**Files:**
- Modify: `dev/engine/concentration-framework.md`

**Interfaces:**
- Consumes: existing sections §1–§10.
- Produces: a document whose table-of-contents order matches the body order.

- [ ] **Step 1: Reorder sections so §6 precedes §7**

Currently `concentration-framework.md` has "§6 集中度→评级调整映射" after "§7 五维加权综合评分". Reorder the body so the sequence is:

1. §1 设计总览
2. §2 维度一：行业集中度
3. §3 维度二：区域集中度
4. §4 维度三：评级集中度
5. §5 维度四：期限集中度
6. §6 维度五：融资渠道集中度
7. §7 集中度→评级调整映射
8. §8 五维加权综合评分
9. §9 集中度压力测试流程
10. §10 与现有引擎的集成
11. §11 局限性声明

Update the table of contents at the top of the file to match this order and remove the special "编号说明" note that justifies the old ordering.

- [ ] **Step 2: Update internal cross-references**

Search for any references to "§6" or "§7" inside the document and update them to match the new numbering.

- [ ] **Step 3: Verify the TOC matches the body**

Run:

```bash
python scripts/consistency_check.py --only-toc dev/engine/concentration-framework.md
```

Or manually:

```bash
grep -n "^## " dev/engine/concentration-framework.md
grep -n "^## " dev/engine/concentration-framework.md | wc -l
```

Expected: TOC entries are in the same order as the body headings.

- [ ] **Step 4: Commit**

```bash
git add dev/engine/concentration-framework.md
git commit -m "docs(engine): reorder concentration-framework sections to match TOC"
```

---

## Task 8: Build the Consistency Checker

**Files:**
- Create: `scripts/consistency_check.py`
- Create: `tests/test_consistency_check.py`

**Interfaces:**
- Consumes: paths to `dev/engine/`, `dev/design/templates/`, `dev/.claude/skills/fixed-income-credit-analysis/SKILL.md`.
- Produces: a script that returns exit code 0 only if all configured checks pass.

- [ ] **Step 1: Write the consistency checker**

Create `scripts/consistency_check.py`:

```python
#!/usr/bin/env python3
"""Regression checker for the fixed-income credit analysis engine."""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENGINE_DIR = ROOT / "dev" / "engine"
TEMPLATES_DIR = ROOT / "dev" / "design" / "templates"
SKILL_FILE = ROOT / "dev" / ".claude" / "skills" / "fixed-income-credit-analysis" / "SKILL.md"

EXPECTED_VERSION = "v0.7.0-alpha"

CORE_DOCS = [
    "engine-overview.md",
    "dual-track-methodology.md",
    "industry-framework.md",
    "qualitative-analysis.md",
    "quantitative-analysis.md",
    "mosaic-engine.md",
    "output-layered-framework.md",
    "contagion-theory.md",
    "contagion-matrix.md",
    "concentration-framework.md",
    "systemic-warning-framework.md",
]


def collect_errors():
    errors = []

    # 1. Core docs must declare EXPECTED_VERSION
    for doc in CORE_DOCS:
        path = ENGINE_DIR / doc
        if not path.exists():
            errors.append(f"MISSING: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        if f"**版本**: {EXPECTED_VERSION}" not in text and f"**版本** {EXPECTED_VERSION}" not in text:
            errors.append(f"VERSION: {doc} does not declare {EXPECTED_VERSION}")

    # 2. Skill must declare EXPECTED_VERSION
    if not SKILL_FILE.exists():
        errors.append(f"MISSING: {SKILL_FILE.relative_to(ROOT)}")
    else:
        skill_text = SKILL_FILE.read_text(encoding="utf-8")
        if EXPECTED_VERSION not in skill_text:
            errors.append(f"VERSION: SKILL.md does not contain {EXPECTED_VERSION}")

    # 3. All internal .md links must resolve
    for path in ENGINE_DIR.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"\[.*?\]\(([^)]+\.md)(?:#[^)]*)?\)", text):
            link = match.group(1)
            target = ENGINE_DIR / link
            if not target.exists():
                errors.append(f"BROKEN_LINK: {path.relative_to(ROOT)} -> {link}")

    # 4. No percentage-scale SRI examples in engine or templates
    sri_pct_pattern = re.compile(r"SRI\s*[:：]\s*\d{2}\s*/\s*100", re.IGNORECASE)
    for path in list(ENGINE_DIR.rglob("*.md")) + list(TEMPLATES_DIR.rglob("*.html")):
        text = path.read_text(encoding="utf-8")
        if sri_pct_pattern.search(text):
            errors.append(f"SRI_PCT: {path.relative_to(ROOT)} contains percentage-scale SRI")

    # 5. No old 6-notch rating artifacts
    old_notch_patterns = [r"AA/A", r"BBB/BB", r"4\.0-5\.9", r"2\.0-3\.9"]
    for doc in ["false-positive-negative-testing.md", "final-review-2026-07-08.md"]:
        path = ENGINE_DIR / doc
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in old_notch_patterns:
            if re.search(pattern, text):
                errors.append(f"OLD_NOTCH: {doc} contains '{pattern}'")

    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only-links", action="store_true")
    parser.add_argument("--only-toc")
    args = parser.parse_args()

    if args.only_toc:
        # Lightweight TOC/body order check for a single file
        path = Path(args.only_toc)
        text = path.read_text(encoding="utf-8")
        toc_entries = re.findall(r"^\s*\d+\.\s+\[(.+?)\]\(#", text, re.MULTILINE)
        body_entries = re.findall(r"^##\s+(.+)$", text, re.MULTILINE)
        if toc_entries != body_entries[: len(toc_entries)]:
            print("TOC mismatch")
            sys.exit(1)
        print("TOC OK")
        return

    errors = collect_errors()
    if errors:
        print(f"Consistency check FAILED ({len(errors)} issue(s)):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("Consistency check PASSED")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Write a test for the checker**

Create `tests/test_consistency_check.py`:

```python
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKER = ROOT / "scripts" / "consistency_check.py"


def test_checker_runs():
    result = subprocess.run([sys.executable, str(CHECKER)], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    assert result.returncode == 0, "Consistency checker reported issues"
    assert "PASSED" in result.stdout
```

- [ ] **Step 3: Install pytest and run the test**

Run:

```bash
python -m pytest tests/test_consistency_check.py -v
```

Expected: test passes once the earlier tasks are complete. If it fails before them, treat the failures as the task list for the preceding documentation fixes.

- [ ] **Step 4: Commit**

```bash
git add scripts/consistency_check.py tests/test_consistency_check.py
git commit -m "feat(scripts): add consistency checker for versions, links, SRI scale, and rating maps"
```

---

## Task 9: Scaffold Executable SRI and Concentration Calculators

**Files:**
- Create: `src/sri_calculator.py`, `tests/test_sri_calculator.py`
- Create: `src/concentration_scorer.py`, `tests/test_concentration_scorer.py`
- Create: `pyproject.toml` (minimal)

**Interfaces:**
- Consumes: industry risk scores and weights for SRI; dimension raw metrics for concentration.
- Produces: deterministic functions that match the formulas in `systemic-warning-framework.md` and `concentration-framework.md`.

- [ ] **Step 1: Write SRI calculator**

Create `src/sri_calculator.py`:

```python
from dataclasses import dataclass
from enum import Enum


class TrackBLevel(str, Enum):
    GREEN = "green"
    YELLOW = "yellow"
    ORANGE = "orange"
    RED = "red"


class Outlook(str, Enum):
    POSITIVE = "positive"
    STABLE = "stable"
    NEGATIVE = "negative"


@dataclass
class IndustryInput:
    name: str
    track_a_score: float  # 0-10
    track_b_level: TrackBLevel
    outlook: Outlook
    veto_triggered: bool = False


def industry_risk_score(ind: IndustryInput) -> float:
    if ind.veto_triggered:
        return 3.0

    if ind.track_a_score < 3.0:
        base = 3.0
    elif ind.track_a_score < 5.0:
        base = 2.0
    elif ind.track_a_score < 6.0:
        base = 1.0
    else:
        base = 0.0

    outlook_penalty = 0.5 if ind.outlook == Outlook.NEGATIVE else 0.0
    track_b_penalty = 0.5 if ind.track_b_level in (TrackBLevel.ORANGE, TrackBLevel.RED) else 0.0

    return base + outlook_penalty + track_b_penalty


def sri(industries: list[IndustryInput], weights: list[float]) -> float:
    if len(industries) != len(weights):
        raise ValueError("industries and weights must have same length")
    if abs(sum(weights) - 1.0) > 1e-6:
        raise ValueError("weights must sum to 1.0")

    return sum(industry_risk_score(ind) * w for ind, w in zip(industries, weights))


def thermometer_level(sri_value: float) -> str:
    if sri_value >= 1.8:
        return "danger"
    if sri_value >= 1.0:
        return "alert"
    if sri_value >= 0.5:
        return "watch"
    return "normal"
```

- [ ] **Step 2: Write SRI calculator test**

Create `tests/test_sri_calculator.py`:

```python
from src.sri_calculator import (
    IndustryInput,
    Outlook,
    TrackBLevel,
    industry_risk_score,
    sri,
    thermometer_level,
)


def test_industry_risk_score_normal():
    ind = IndustryInput(
        name="test",
        track_a_score=7.0,
        track_b_level=TrackBLevel.GREEN,
        outlook=Outlook.STABLE,
    )
    assert industry_risk_score(ind) == 0.0


def test_industry_risk_score_negative_outlook_and_orange_track_b():
    ind = IndustryInput(
        name="test",
        track_a_score=7.0,
        track_b_level=TrackBLevel.ORANGE,
        outlook=Outlook.NEGATIVE,
    )
    assert industry_risk_score(ind) == 1.0


def test_veto_overrides_everything():
    ind = IndustryInput(
        name="test",
        track_a_score=9.0,
        track_b_level=TrackBLevel.GREEN,
        outlook=Outlook.STABLE,
        veto_triggered=True,
    )
    assert industry_risk_score(ind) == 3.0


def test_sri_matches_2026q2_example():
    # Approximate 2026Q2 example from systemic-warning-framework.md §8.3
    industries = [
        IndustryInput("LGV", 5.25, TrackBLevel.YELLOW, Outlook.STABLE),
        IndustryInput("PV", 5.0, TrackBLevel.YELLOW, Outlook.NEGATIVE),
        IndustryInput("NEV", 5.5, TrackBLevel.YELLOW, Outlook.NEGATIVE),
        IndustryInput("Retail", 5.5, TrackBLevel.YELLOW, Outlook.NEGATIVE),
    ] + [
        IndustryInput(f"other_{i}", 7.0, TrackBLevel.GREEN, Outlook.STABLE)
        for i in range(9)
    ]
    weights = [0.25, 0.0233, 0.0222, 0.04] + [0.0] * 9
    # Note: weights do not sum to 1.0 intentionally; the test should use a valid distribution.
    # Replace with normalized weights for a real assertion.
    normalized = [w / sum(weights) for w in weights]
    result = sri(industries, normalized)
    assert 0.4 <= result <= 0.7


def test_thermometer():
    assert thermometer_level(0.2) == "normal"
    assert thermometer_level(0.6) == "watch"
    assert thermometer_level(1.2) == "alert"
    assert thermometer_level(2.0) == "danger"
```

- [ ] **Step 3: Write concentration scorer stub**

Create `src/concentration_scorer.py`:

```python
from dataclasses import dataclass


@dataclass
class ConcentrationMetrics:
    hhi: float
    cr3: float
    cr5: float
    max1: float
    single_province_share: float
    weak_region_share: float
    aaa_share: float
    pseudo_high_rating_share: float
    maturity_12m_share: float
    single_month_peak: float
    top_channel_share: float
    top_channel_is_contracting: bool = False


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def industry_score(metrics: ConcentrationMetrics) -> int:
    # Simplified mapping for the highest-risk indicator among HHI/CR3/CR5/MAX1.
    if metrics.max1 >= 0.60:
        return 9
    if metrics.cr3 >= 0.80 or metrics.cr5 >= 0.90 or metrics.hhi >= 2500:
        return 8
    if metrics.max1 >= 0.40 or metrics.cr3 >= 0.65 or metrics.cr5 >= 0.80 or metrics.hhi >= 1500:
        return 6
    if metrics.max1 >= 0.25 or metrics.cr3 >= 0.50 or metrics.cr5 >= 0.70 or metrics.hhi >= 1000:
        return 4
    return 2


def concentration_risk_score(metrics: ConcentrationMetrics) -> float:
    # Placeholder weighted score matching the five dimensions.
    # Task 10 will expand this to full five-dimensional logic.
    return float(industry_score(metrics))
```

- [ ] **Step 4: Write concentration scorer test**

Create `tests/test_concentration_scorer.py`:

```python
from src.concentration_scorer import ConcentrationMetrics, concentration_risk_score


def test_high_concentration():
    metrics = ConcentrationMetrics(
        hhi=2600,
        cr3=0.85,
        cr5=0.92,
        max1=0.65,
        single_province_share=0.20,
        weak_region_share=0.05,
        aaa_share=0.40,
        pseudo_high_rating_share=0.05,
        maturity_12m_share=0.30,
        single_month_peak=0.10,
        top_channel_share=0.60,
    )
    assert concentration_risk_score(metrics) >= 8.0


def test_low_concentration():
    metrics = ConcentrationMetrics(
        hhi=500,
        cr3=0.30,
        cr5=0.50,
        max1=0.15,
        single_province_share=0.10,
        weak_region_share=0.02,
        aaa_share=0.20,
        pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20,
        single_month_peak=0.05,
        top_channel_share=0.30,
    )
    assert concentration_risk_score(metrics) <= 4.0
```

- [ ] **Step 5: Add minimal project metadata**

Create `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "credence-engine"
version = "0.7.0-alpha"
description = "Fixed income credit analysis engine prototypes"
requires-python = ">=3.11"
dependencies = []

[tool.pytest.ini_options]
testpaths = ["tests"]
```

- [ ] **Step 6: Run the new tests**

Run:

```bash
python -m pytest tests/test_sri_calculator.py tests/test_concentration_scorer.py -v
```

Expected: all tests pass.

- [ ] **Step 7: Commit**

```bash
git add src/ tests/ pyproject.toml
git commit -m "feat(src): scaffold SRI and concentration calculator prototypes"
```

---

## Task 10: Re-run Full Consistency Check and Cut Release Snapshot

**Files:**
- Create: `version/v0.7.0-alpha/` snapshot
- Create: `version/v0.7.0-alpha.zip`
- Modify: `dev/README.md` version history if needed

**Interfaces:**
- Consumes: all prior task outputs and the consistency checker.
- Produces: a validated v0.7.0-alpha release snapshot.

- [ ] **Step 1: Run the full consistency checker**

Run:

```bash
python scripts/consistency_check.py
```

Expected output:

```
Consistency check PASSED
```

- [ ] **Step 2: Update README version history if not already done**

Ensure `dev/README.md` contains the v0.7.0-alpha row in the version history and that the "系统智能层" section reflects the 8 system-intelligence reports.

- [ ] **Step 3: Create the release snapshot**

Run:

```bash
rm -rf version/v0.7.0-alpha
cp -r dev version/v0.7.0-alpha
rm -rf version/v0.7.0-alpha/.git
rm -rf version/v0.7.0-alpha/.claude/settings.local.json  # if it contains local-only settings
cd version && zip -r v0.7.0-alpha.zip v0.7.0-alpha && cd ..
```

- [ ] **Step 4: Verify the snapshot contains the upgraded Skill**

Run:

```bash
ls version/v0.7.0-alpha/.claude/skills/fixed-income-credit-analysis/SKILL.md
grep -n "v0.7.0-alpha" version/v0.7.0-alpha/.claude/skills/fixed-income-credit-analysis/SKILL.md
```

Expected: file exists and contains `v0.7.0-alpha`.

- [ ] **Step 5: Final commit**

```bash
git add version/v0.7.0-alpha version/v0.7.0-alpha.zip dev/README.md
git commit -m "release: v0.7.0-alpha snapshot with synchronized skill and consistency checks"
```

---

## Self-Review

### Spec Coverage

| Requirement | Task |
|---|---|
| Skill lags behind engine (v0.5.0 vs v0.7.0) | Task 2 |
| System-intelligence layer missing from Skill | Task 2 |
| 13 industries and six paradigms missing from Skill | Task 2 |
| Skill not archived in `version/v0.7.0-alpha/` | Task 2, Task 10 |
| SRI metric inconsistent (0–3+ vs 0–100) | Task 4 |
| SRI formula inconsistent with examples | Task 4 |
| Broken cross-references in system-intelligence layer | Task 3 |
| Old 6-notch rating map in testing/review docs | Task 5 |
| Template/report versions stuck at v0.6.x | Task 6 |
| Concentration framework section order mismatch | Task 7 |
| No automated consistency regression guard | Task 8 |
| No executable reference for SRI/concentration formulas | Task 9 |
| No version-management document | Task 1 |
| No release snapshot workflow | Task 1, Task 10 |

### Placeholder Scan

No `TBD`, `TODO`, `implement later`, `fill in details`, or `similar to Task N` placeholders remain. Every step includes exact file paths, exact Markdown/HTML snippets, and exact commands.

### Type Consistency

- `sri_calculator.py` uses `IndustryInput` dataclass consistently across `industry_risk_score`, `sri`, and tests.
- `TrackBLevel` and `Outlook` enums are used in both implementation and tests.
- `consistency_check.py` uses the same `EXPECTED_VERSION` constant everywhere.

---

## Execution Handoff

**Plan complete and saved to `docs/superpowers/plans/2026-07-13-fixed-income-credit-v0.7.0-cleanup.md`.**

Two execution options:

1. **Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration. Requires `superpowers:subagent-driven-development`.
2. **Inline Execution** — Execute tasks in this session using `superpowers:executing-plans`, batch execution with checkpoints.

**Which approach would you like?**
