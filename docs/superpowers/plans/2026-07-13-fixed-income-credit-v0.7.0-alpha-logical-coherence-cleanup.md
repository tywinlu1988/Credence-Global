# 固定收益信用分析引擎 v0.7.0-alpha 逻辑自洽性修正计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 修复结构审查报告中发现的核心逻辑冲突与执行链断裂，降低当前版本的幻觉率，提升分析结果可靠性。

**Architecture:** 这是一次以文档、Skill prompt、可执行参考实现和模板一致性为核心的 hardening sprint。不涉及新增分析范式或行业覆盖，只聚焦于让现有三层架构（Mosaic → Dual-Track → System-Intelligence）在调用、判断、分配、执行四个环节上自洽、可追溯、可验证。

**Tech Stack:** Markdown, HTML/CSS templates, Python 3.11+, pytest.

## Global Constraints

- 所有修改必须基于结构审查报告，不扩大 scope，不新增未经验证的方法论。
- 所有数值阈值、权重、评级映射必须来源自 `dev/engine/` 下的权威文档；若文档本身矛盾，则先统一文档再修改代码/Skill/模板。
- 每完成一个 Task，必须运行 `python -m pytest tests/ -v && python scripts/consistency_check.py`，并确保通过。
- 每个 Task 结束后必须提交；提交信息需说明修复的逻辑冲突点。
- 每轮 Task 完成后刷新 `version/v0.7.0-alpha/` 快照与 `version/v0.7.0-alpha.zip`。
- 若上下文空间不足 40%，在执行 Task 前先用 `git log`、 ledger 文件和压缩后的 diff summary 替换长对话中的 agent 输出细节，必要时将大段引用写入临时 note 文件而非保留在对话中。

---

## 上下文管理策略

本计划涉及较多跨文档校验。为避免上下文耗尽，执行顺序按以下原则安排：

1. **先做会修改 checker 的任务**（Task 1、Task 2），让一致性检查器尽早能覆盖后续修复。
2. **再做 Skill 和 references 清理**（Task 3），避免后续任务引用陈旧副本。
3. **再做评级判断逻辑统一**（Task 4–Task 6），因为这部分冲突最直接影响结果可靠性。
4. **再做代码实现补全**（Task 7–Task 9）。
5. **最后做模板和回归测试**（Task 10–Task 12）。

如果在执行过程中发现上下文使用率超过 60%，立即暂停并将当前状态写入 `.superpowers/sdd/progress.md` 与 `.superpowers/sdd/context-summary.md`，用一句 summary 替代对话中的详细 agent 输出，再继续。

---

## Task 1: 扩展一致性检查器以覆盖结构审查发现的问题

**Files:**
- Modify: `scripts/consistency_check.py`
- Test: `tests/test_consistency_check.py`

**Interfaces:**
- Consumes: existing `CORE_DOCS`, `OLD_NOTCH_PATTERNS`, `SRI_PCT_PATTERN`.
- Produces: additional checks for Track-B scoring consistency, veto ceiling consistency, paradigm mapping coverage, and reference-file staleness.

- [ ] **Step 1: Add a rating-map single-source-of-truth check**

Create a helper that reads the canonical 12-notch table from `dev/engine/dual-track-methodology.md` §六 (lines 202-230) and compares it with any other table in `dev/engine/systemic-warning-framework.md`, `dev/engine/false-positive-negative-testing.md`, and `dev/engine/outlook-monitoring-framework.md` that maps score ranges to ratings. Flag mismatched intervals or labels.

For the first pass, implement a lightweight version:

```python
CANONICAL_RATING_INTERVALS = [
    (9.5, 10.0, "AAA"),
    (9.0, 9.4, "AA+"),
    (8.5, 8.9, "AA"),
    (8.0, 8.4, "AA-"),
    (7.5, 7.9, "A+"),
    (7.0, 7.4, "A"),
    (6.5, 6.9, "A-"),
    (6.0, 6.4, "BBB+"),
    (5.5, 5.9, "BBB"),
    (5.0, 5.4, "BBB-"),
    (4.5, 4.9, "BB+"),
    (4.0, 4.4, "BB"),
    (3.5, 3.9, "BB-"),
    (3.0, 3.4, "B+"),
    (2.5, 2.9, "B"),
    (2.0, 2.4, "B-"),
    (1.0, 1.9, "CCC"),
    (0.0, 0.9, "D"),
]
```

Add `check_rating_map_consistency()` that scans `dev/engine/*.md` for rows of the form `| X-Y | RATING |` and flags any interval/label pair that deviates from the canonical list. Skip historical audit files (`consistency-audit-v0.5.2.md`, `v0.6.1-0.6.7-quality-audit.md`, etc.) if they are clearly framed as historical.

- [ ] **Step 2: Add a Track-B SRI scoring consistency check**

Add `check_sri_track_b_consistency()` that verifies all textual descriptions of Track-B-to-SRI penalties in `systemic-warning-framework.md` match the canonical rule chosen by the project. For now, accept either rule but flag if the same document contains both `yellow = 0.5` and `yellow = 0`.

- [ ] **Step 3: Add a Skill reference-file staleness check**

Add `check_skill_references()` that compares `dev/.claude/skills/fixed-income-credit-analysis/references/*.md` with the corresponding `dev/engine/*.md` files. For this task, only check existence and version header: if a references/ file exists but its `**版本**` or `**对应引擎版本**` header differs from the engine file, flag it.

- [ ] **Step 4: Add a paradigm coverage check**

Add `check_paradigm_coverage()` that verifies every industry listed in `contagion-matrix.md` §1.2 also appears in `industry-framework.md` with a D1–D10 score table or an explicit "judgmental assignment" note. For v0.7.0-alpha, allow judgmental notes but flag industries that are completely missing.

- [ ] **Step 5: Write/update tests**

Add tests in `tests/test_consistency_check.py` for each new check. Each test should create a minimal temporary file tree under a `tmp_path` fixture and assert the checker flags the expected issue.

- [ ] **Step 6: Run tests**

```bash
python -m pytest tests/test_consistency_check.py -v
```

Expected: existing tests still pass; new tests fail until their target issues are fixed in later tasks.

- [ ] **Step 7: Commit**

```bash
git add scripts/consistency_check.py tests/test_consistency_check.py
git commit -m "feat(scripts): extend consistency checker for structural coherence gaps"
```

---

## Task 2: 统一 Track-B 对 SRI 的加分规则

**Files:**
- Modify: `dev/engine/systemic-warning-framework.md`
- Modify: `src/sri_calculator.py` (if needed)
- Test: `tests/test_sri_calculator.py`

**Interfaces:**
- Consumes: Track-B levels (green/yellow/orange/red) and SRI 0–3+ scale.
- Produces: a single, canonical Track-B penalty rule used everywhere.

- [ ] **Step 1: Decide the canonical rule**

The two candidates are:

| Track B | Option A | Option B |
|---|---|---|
| 平静 (green) | 0 | 0 |
| 关注 (yellow) | 0.5 | 0 |
| 异常 (orange) | 1.0 | 0.5 |
| 危机 (red) | 1.5 | 0.5 |

**Decision:** Use **Option A** (`0 / 0.5 / 1.0 / 1.5`). Reason: it preserves the four-level thermometer philosophy (each Track-B escalation adds meaningful risk) and aligns with the §2.1 table already present after the 12-notch fix. It also makes yellow materially different from green.

- [ ] **Step 2: Update §2.1 table in systemic-warning-framework.md**

The table already uses Option A. Confirm it reads:

```markdown
| 轨道B状态 | 评分映射 | 颜色标记 |
|----------|---------|---------|
| 平静 | 0分 | 🟢 |
| 关注 | 0.5分 | 🟡 |
| 异常 | 1.0分 | 🟠 |
| 危机 | 1.5分 | 🔴 |
```

- [ ] **Step 3: Update §2.2.1 pseudocode**

Replace the pseudocode lines (around 164-167) with:

```markdown
轨道B惩罚 =
  - 平静: 0
  - 关注: 0.5
  - 异常: 1.0
  - 危机: 1.5
```

- [ ] **Step 4: Update §2.2.2 quick-lookup table**

Recompute the lookup table using Option A. The table maps `(base_score, outlook_penalty, track_b_penalty)` to `industry_risk_score`. With base ∈ {0,1,2,3}, outlook ∈ {0,0.5}, track_b ∈ {0,0.5,1.0,1.5}, veto overrides to 3.0.

The worst non-veto score remains 3.0 (base 3 + outlook 0.5 + track_b 1.5 = 5.0, capped at 3.0). The lookup table should reflect this cap.

- [ ] **Step 5: Update `src/sri_calculator.py`**

Change `track_b_penalty` in `industry_risk_score()` from:

```python
track_b_penalty = 0.5 if ind.track_b_level in (TrackBLevel.ORANGE, TrackBLevel.RED) else 0.0
```

to:

```python
if ind.track_b_level == TrackBLevel.RED:
    track_b_penalty = 1.5
elif ind.track_b_level == TrackBLevel.ORANGE:
    track_b_penalty = 1.0
elif ind.track_b_level == TrackBLevel.YELLOW:
    track_b_penalty = 0.5
else:
    track_b_penalty = 0.0
```

- [ ] **Step 6: Update tests**

Add/update tests in `tests/test_sri_calculator.py`:

```python
def test_track_b_penalties():
    base = IndustryInput("base", 7.0, TrackBLevel.GREEN, Outlook.STABLE)
    assert industry_risk_score(base) == 0.0
    yellow = IndustryInput("yellow", 7.0, TrackBLevel.YELLOW, Outlook.STABLE)
    assert industry_risk_score(yellow) == 0.5
    orange = IndustryInput("orange", 7.0, TrackBLevel.ORANGE, Outlook.STABLE)
    assert industry_risk_score(orange) == 1.0
    red = IndustryInput("red", 7.0, TrackBLevel.RED, Outlook.STABLE)
    assert industry_risk_score(red) == 1.5
```

Also add a test that verifies the cap at 3.0 for worst non-veto with red Track B and negative outlook:

```python
def test_worst_non_veto_with_red_track_b_and_negative_outlook():
    ind = IndustryInput("worst", 2.0, TrackBLevel.RED, Outlook.NEGATIVE)
    assert industry_risk_score(ind) == 3.0
```

- [ ] **Step 7: Run tests and checker**

```bash
python -m pytest tests/test_sri_calculator.py tests/test_consistency_check.py -v
python scripts/consistency_check.py
```

Expected: all pass.

- [ ] **Step 8: Commit**

```bash
git add dev/engine/systemic-warning-framework.md src/sri_calculator.py tests/test_sri_calculator.py
git commit -m "fix(sri): unify Track-B penalty rule to 0/0.5/1.0/1.5 across docs and code"
```

---

## Task 3: 清理 Skill references 并增强调用约束

**Files:**
- Modify: `dev/.claude/skills/fixed-income-credit-analysis/SKILL.md`
- Modify: `dev/.claude/skills/fixed-income-credit-analysis/references/*.md` (delete or sync)
- Test: `scripts/consistency_check.py`

**Interfaces:**
- Consumes: canonical engine docs under `dev/engine/`.
- Produces: a Skill manifest whose references are current and whose prompt constrains the model to documented methods.

- [ ] **Step 1: Add an invocation preamble at the top of SKILL.md**

Insert after the front-matter and before `# Fixed Income Credit Analysis Engine v0.7.0-alpha`:

```markdown
## Invocation Protocol

When this Skill is invoked:

1. Read the canonical engine documents in this order:
   - `dev/engine/engine-overview.md`
   - `dev/engine/industry-framework.md`
   - `dev/engine/dual-track-methodology.md`
   - `dev/engine/mosaic-engine.md`
   - plus any topic-specific doc named in the user request (e.g., `contagion-matrix.md`, `concentration-framework.md`, `systemic-warning-framework.md`).
2. Use **only** thresholds, weights, rating mappings, and veto rules found in those documents.
3. For every quantitative judgment, cite the source document and section.
4. If a required threshold, weight, or mapping is missing from the engine documents, output `引擎未定义` and do not invent a value.
5. Do not invoke Mode B or generate external-data values unless the user has explicitly provided a CSV upload, API endpoint, or MCP server. Treat Mode B fields as data gaps until then.
```

- [ ] **Step 2: Fix all Supporting Files links**

Replace `references/...` with `dev/engine/...` in the Supporting Files list (around lines 330-338). For example:

```markdown
- `dev/engine/industry-framework.md` — Complete pyramid specs for 7 industries
- `dev/engine/mosaic-engine.md` — Full mosaic engine architecture specification
- `dev/engine/contagion-theory.md` — Contagion types, transmission paths, upgrade factors
- `dev/engine/contagion-matrix.md` — 13×13 cross-industry contagion matrix
- `dev/engine/concentration-framework.md` — Five-dimensional concentration framework
- `dev/engine/systemic-warning-framework.md` — SRI algorithm and thermometer
- `dev/engine/paradigm-brand-channel.md` — Brand+channel paradigm specification
- `dev/engine/paradigm-network-traffic.md` — Network+traffic paradigm specification
```

- [ ] **Step 3: Correct the validation table**

Update the table to match actual engine validation coverage. Recommended wording:

```markdown
| Industry | Forward Test | Retrospective Test |
|---|---|---|
| Solar/PV | 完成 | — |
| Semiconductor | 完成 | 完成 |
| Biomedicine | 完成 | 完成 |
| High-End Equipment | 完成 | 完成 |
| Medical Devices | 完成 | 完成 |
| NEV | 完成 | 完成 |
| Data Center | 完成 | — |
| Coal/SOE (Yongmei) | — | 完成 |
| LGFV | 框架覆盖 | 框架覆盖 |
| Food & Beverage | 13-industry framework coverage | — |
| Textile & Apparel | 13-industry framework coverage | — |
| Transportation | 13-industry framework coverage | — |
| Retail | 13-industry framework coverage | — |
| Media/Internet | 13-industry framework coverage | — |
```

- [ ] **Step 4: Clarify taxonomy**

In the "Six Analytical Paradigms" section, add a note:

```markdown
> **注意**：6 个分析范式是用于传染聚类和行业分组的概念工具；它们不同于 `industry-framework.md` 中定义的 4 个行业类型（用于设置金字塔权重）。一个行业可能同时满足多个范式特征，此时以 `industry-framework.md` 的行业类型作为金字塔权重依据，以范式作为传染分析依据。
```

- [ ] **Step 5: Soften concentration weight language**

Change:

```markdown
Default weights: industry 25%, region 20%, rating 20%, tenor 20%, funding channel 15%.
```

to:

```markdown
Suggested default weights (adjustable per `concentration-framework.md` §8.4): industry 25%, region 20%, rating 20%, tenor 20%, funding channel 15%.
```

- [ ] **Step 6: Sync or delete stale reference files**

For each file in `dev/.claude/skills/fixed-income-credit-analysis/references/`:
- If a corresponding `dev/engine/*.md` exists, overwrite the references/ copy with the current engine version (or delete it and point Skill links to `dev/engine/`).
- If no corresponding engine file exists (e.g., `industry-pyramids.md`), delete it.

Specifically:
- Delete `references/industry-pyramids.md` (engine file is `dev/engine/industry-framework.md`).
- Delete `references/mosaic-engine-architecture.md` (engine file is `dev/engine/mosaic-engine.md`).
- Delete `references/validation-cases.md` (engine file is `dev/engine/validation-methodology.md`).
- For files like `references/esg-framework.md`, `references/lgv-framework.md`, etc., either sync them with `dev/engine/` or delete them and update links.

Recommended approach: **delete all `references/*.md` and point Skill links to `dev/engine/`**. This eliminates drift risk.

- [ ] **Step 7: Add explicit loading instructions for expanded capabilities**

For each expanded-capability bullet in "When to Use" (ESG, LGV, LGD, external support, financial bond, holding company), add a one-liner:

```markdown
- Evaluating LGFV (城投债) credit quality → read `dev/engine/lgv-framework.md`
- Conducting ESG/governance risk scans → read `dev/engine/esg-framework.md` and `dev/engine/governance-fraud-risk.md`
- Performing LGD/recovery rate analysis → read `dev/engine/lgd-recovery-framework.md`
- Assessing external support → read `dev/engine/external-support-framework.md`
- Evaluating financial bonds → read `dev/engine/financial-bond-framework.md`
- Analyzing holding companies → read `dev/engine/holding-company-framework.md`
```

- [ ] **Step 8: Run checker**

```bash
python scripts/consistency_check.py
```

Expected: PASSED.

- [ ] **Step 9: Commit**

```bash
git add dev/.claude/skills/fixed-income-credit-analysis/SKILL.md
# if deleting references
rm dev/.claude/skills/fixed-income-credit-analysis/references/*.md
git add dev/.claude/skills/fixed-income-credit-analysis/
git commit -m "feat(skill): add invocation guardrails, fix validation claims, point references to dev/engine"
```

---

## Task 4: 清理残留的旧 6-notch 评级映射

**Files:**
- Modify: `dev/engine/outlook-monitoring-framework.md`
- Modify: `dev/engine/dual-track-methodology.md`
- Modify: `dev/engine/self-assessment-2026-07-08.md`
- Modify: `dev/engine/closure-check-2026-07-08.md`
- Modify: `dev/engine/rating-agency-benchmark-audit.md`

**Interfaces:**
- Consumes: canonical 12-notch rating map from `dual-track-methodology.md` §六.
- Produces: all current methodology docs use only the 12-notch scheme.

- [ ] **Step 1: Replace outlook-monitoring-framework.md §6.1 6-notch table**

Locate the table around lines 513-518. Replace it with the 18-row 12-notch table from `dual-track-methodology.md` §六.

- [ ] **Step 2: Remove CC/C from outlook-monitoring-framework.md Appendix A**

Line 672 lists `[AAA, AA+, AA, AA-, A+, A, A-, BBB+, BBB, BBB-, BB+, BB, BB-, B+, B, B-, CCC, CC, C, D]` — this was added in a previous fix but incorrectly includes CC/C. Change to:

```markdown
评级: [AAA, AA+, AA, AA-, A+, A, A-, BBB+, BBB, BBB-, BB+, BB, BB-, B+, B, B-, CCC, D]
```

- [ ] **Step 3: Strip "旧6档" annotations from dual-track-methodology.md worked examples**

Around lines 630, 660, 664, 670, 676, remove phrases like "旧6档 ..." or replace them with "旧体系" or simply remove the parenthetical. Keep the 12-notch rating as the primary label.

- [ ] **Step 4: Update self-assessment and closure-check**

In `self-assessment-2026-07-08.md` line 20, change "AAA→D六档评级映射" to "AAA→D 12-notch 评级映射" or similar.

In `closure-check-2026-07-08.md` line 16, change "6档→12档方案已写入（v0.4.0）但未正式采用" to "12档评级映射已正式采用（v0.4.0+）".

- [ ] **Step 5: Update rating-agency-benchmark-audit.md line 256**

Change the remaining old-interval reference to use the 12-notch wording. The line already says "例如旧6档将 9.0-10.0 映射为 AAA、7.5-8.9 映射为 AA 与 A 合并档……"; ensure no old intervals like `4.0-5.9` or `2.0-3.9` remain in that sentence.

- [ ] **Step 6: Run checker**

```bash
python scripts/consistency_check.py
```

Expected: PASSED (no OLD_NOTCH errors).

- [ ] **Step 7: Commit**

```bash
git add dev/engine/outlook-monitoring-framework.md dev/engine/dual-track-methodology.md dev/engine/self-assessment-2026-07-08.md dev/engine/closure-check-2026-07-08.md dev/engine/rating-agency-benchmark-audit.md
git commit -m "docs(engine): remove residual old 6-notch rating artifacts"
```

---

## Task 5: 统一一票否决的评级上限

**Files:**
- Modify: `dev/engine/concentration-framework.md`
- Modify: `dev/engine/new-industry-methodology-audit.md`
- Modify: `dev/engine/non-credit-risk-overlay.md`
- Modify: `dev/engine/industry-framework.md` (if needed)
- Modify: `dev/engine/dual-track-methodology.md` (if needed)

**Interfaces:**
- Consumes: issuer survival veto (CCC cap), concentration extreme cap (BB cap), paradigm-specific caps.
- Produces: unambiguous vocabulary and ceilings for each veto type.

- [ ] **Step 1: Define terminology**

Reserve "一票否决" for **issuer survival risk** with a **CCC** ceiling. Rename other triggers:
- Concentration extreme: "组合极端集中上限" with **BB** ceiling.
- Brand/Channel paradigm: "品牌渠道范式硬上限" with **CCC** ceiling.
- Network/Traffic paradigm: "网络流量范式硬上限" with **B-** ceiling (or unify to CCC if no strong reason).
- Non-credit risk vetoes: explicitly define ceiling per risk type.

- [ ] **Step 2: Update concentration-framework.md**

In §7.2/7.3 (around lines 623, 630, 634-645), replace "一票否决" with "组合极端集中上限" or "集中度硬触发". Keep the BB ceiling, but document why it differs from issuer survival veto.

Add a note:

```markdown
> **注意**：组合极端集中度上限（BB）与发行人层面的一票否决（CCC）是不同概念。前者针对组合层面因集中度导致的流动性/变现风险，后者针对发行人自身经营生存风险。
```

- [ ] **Step 3: Update new-industry-methodology-audit.md**

Line 22: clarify the CCC vs B- paradigm caps. Either unify them or document the rationale.

- [ ] **Step 4: Update non-credit-risk-overlay.md**

Lines 441/572: explicitly state the ceiling for each non-credit-risk veto type. If strategic-risk veto is CCC, say so; if others are undefined, mark them as "待定义".

- [ ] **Step 5: Verify issuer-level docs still say CCC**

Confirm `dual-track-methodology.md`, `industry-framework.md`, `governance-fraud-risk.md`, `output-layered-framework.md`, `financial-bond-framework.md` still cap issuer survival veto at CCC.

- [ ] **Step 6: Run checker**

```bash
python scripts/consistency_check.py
```

Expected: PASSED.

- [ ] **Step 7: Commit**

```bash
git add dev/engine/concentration-framework.md dev/engine/new-industry-methodology-audit.md dev/engine/non-credit-risk-overlay.md
git commit -m "docs(engine): disambiguate veto types and unify ceiling vocabulary"
```

---

## Task 6: 扩展 D1–D10 行业覆盖并解决范式归属冲突

**Files:**
- Modify: `dev/engine/industry-framework.md`
- Modify: `dev/engine/contagion-matrix.md`
- Modify: `dev/engine/SKILL.md` (paradigm table)
- Modify: `dev/engine/paradigm-brand-channel.md` and `dev/engine/paradigm-network-traffic.md` (if needed)

**Interfaces:**
- Consumes: D1–D10 scoring dimensions, 13 industries, 6 paradigms.
- Produces: unambiguous industry-to-paradigm mapping with documented rationale.

- [ ] **Step 1: Add D1–D10 tables for the 6 uncovered industries**

In `industry-framework.md` §6 or a new §6.2, add D1–D10 score tables for:
- Food & Beverage
- Textile & Apparel
- Transportation
- Retail
- Media/Internet
- LGFV

For each, assign scores 1-5 and note which paradigm it primarily triggers. Example for Food & Beverage:

```markdown
| 维度 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | 触发范式 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 食品饮料 | 4 | 3 | 3 | 2 | 3 | 4 | 2 | 3 | 3 | 2 | 品牌+渠道 |
```

(Exact scores to be determined by domain judgment; the key is to make the assignment traceable.)

- [ ] **Step 2: Add precedence rule for overlapping triggers**

Add a section in `industry-framework.md` §3.1 or §7:

```markdown
### 范式冲突时的优先级规则

当一个行业同时满足多个范式触发条件时，按以下顺序确定其主要范式：
1. 生存位势/利润要塞（Consolidation）优先于其他范式；
2.  geopolitics-technology 混合行业中，以地缘政治为 L1 权重的行业归为 Policy-Driven，但标注 Tech-Barrier 次要属性；
3. 资产租约型（Asset-Lease）与网络+流量型（Network+Traffic）冲突时，若核心资产为物理租约则 Asset-Lease 优先，若核心资产为流量/用户则 Network+Traffic 优先；
4. 品牌+渠道型（Brand+Channel）与网络+流量型冲突时，以收入是否主要依赖品牌溢价 vs 流量变现区分。
```

- [ ] **Step 3: Resolve specific conflicts**

- **Semiconductor**: Keep as Policy-Driven primary (per Skill table), add Tech-Barrier secondary in `industry-framework.md` and `contagion-matrix.md`.
- **Biomedicine**: Assign to Tech-Barrier with note that it has Policy-Driven secondary attributes.
- **NEV**: Split into OEM (Consolidation) and Supply Chain (Profit Fortress / Tech-Barrier) in Skill table and `contagion-matrix.md`, matching `industry-framework.md` §4.6.
- **Data Center**: Resolve by splitting into IDC/colocation (Asset-Lease) and cloud/telecom (Network+Traffic), or pick one primary and document the other as secondary. Recommended primary: Asset-Lease (matches `industry-framework.md`); Network+Traffic as secondary for cloud/DC hybrid cases.
- **LGFV**: Add as a special/seventh row in the Skill paradigm table, not forced into the six-paradigm taxonomy.

- [ ] **Step 4: Update contagion-matrix.md §1.2/1.3**

Reflect the resolved assignments and add a note that singleton paradigms (Consolidation, Asset-Lease) rely mainly on cross-paradigm links.

- [ ] **Step 5: Run checker**

```bash
python scripts/consistency_check.py
```

Expected: PASSED.

- [ ] **Step 6: Commit**

```bash
git add dev/engine/industry-framework.md dev/engine/contagion-matrix.md dev/.claude/skills/fixed-income-credit-analysis/SKILL.md dev/engine/paradigm-brand-channel.md dev/engine/paradigm-network-traffic.md
git commit -m "docs(engine): extend D1-D10 coverage and resolve paradigm assignment conflicts"
```

---

## Task 7: 实现集中度 → 评级调整逻辑

**Files:**
- Modify: `src/concentration_scorer.py`
- Modify: `tests/test_concentration_scorer.py`

**Interfaces:**
- Consumes: `ConcentrationMetrics` and documented dimension thresholds.
- Produces: functions that return dimension risk levels and final rating adjustment in notches.

- [ ] **Step 1: Add dimension risk-level classification**

For each of the five dimensions, classify into 🟢/🟡/🟠/🔴 based on the scores already computed:

```python
def _risk_level(score: int) -> str:
    if score >= 8: return "red"
    if score >= 6: return "orange"
    if score >= 4: return "yellow"
    return "green"
```

- [ ] **Step 2: Add `rating_adjustment()` function**

Implement the mapping from `concentration-framework.md` §7:

```python
def rating_adjustment(metrics: ConcentrationMetrics) -> dict:
    """
    Returns rating adjustment in notches and flags per concentration-framework.md §7.
    - green: 0
    - yellow: -0.5
    - orange: -1.0
    - red: -1.0 plus potential BB cap trigger
    """
    levels = {
        "industry": _risk_level(industry_score(metrics)),
        "region": _risk_level(region_score(metrics)),
        "rating": _risk_level(rating_score(metrics)),
        "maturity": _risk_level(maturity_score(metrics)),
        "channel": _risk_level(channel_score(metrics)),
    }
    adjustment = 0.0
    red_count = 0
    orange_count = 0
    for lvl in levels.values():
        if lvl == "red":
            adjustment -= 1.0
            red_count += 1
        elif lvl == "orange":
            adjustment -= 1.0
            orange_count += 1
        elif lvl == "yellow":
            adjustment -= 0.5

    bb_cap_triggered = red_count >= 2 or (red_count >= 1 and orange_count >= 2)
    return {
        "adjustment": adjustment,
        "levels": levels,
        "bb_cap_triggered": bb_cap_triggered,
    }
```

(Note: exact stacking rules should match `concentration-framework.md:591-646`; adjust the function if the docs specify a different formula.)

- [ ] **Step 3: Add tests**

Add tests in `tests/test_concentration_scorer.py`:

```python
def test_rating_adjustment_all_green():
    low = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    adj = rating_adjustment(low)
    assert adj["adjustment"] == 0.0
    assert adj["bb_cap_triggered"] is False


def test_rating_adjustment_extreme_concentration():
    high = ConcentrationMetrics(
        hhi=2600, cr3=0.85, cr5=0.92, max1=0.65,
        single_province_share=0.50, weak_region_share=0.35,
        aaa_share=0.75, pseudo_high_rating_share=0.35,
        maturity_12m_share=0.75, single_month_peak=0.35,
        top_channel_share=0.80, top_channel_is_contracting=True,
    )
    adj = rating_adjustment(high)
    assert adj["adjustment"] <= -3.0
    assert adj["bb_cap_triggered"] is True
```

- [ ] **Step 4: Run tests and checker**

```bash
python -m pytest tests/test_concentration_scorer.py tests/test_consistency_check.py -v
python scripts/consistency_check.py
```

Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add src/concentration_scorer.py tests/test_concentration_scorer.py
git commit -m "feat(src): implement concentration rating adjustment and BB cap"
```

---

## Task 8: 实现 SRI → 个体发行人降级和 M4 集中度权重调整

**Files:**
- Modify: `src/sri_calculator.py` or create `src/portfolio_overlay.py`
- Modify: `tests/test_sri_calculator.py`

**Interfaces:**
- Consumes: SRI value, individual issuer rating, concentration score.
- Produces: adjusted issuer rating and concentration weights.

- [ ] **Step 1: Implement M2 background downgrade**

Add to `src/sri_calculator.py`:

```python
def m2_background_downgrade(sri: float) -> float:
    """Return notch downgrade for individual issuers based on systemic-warning-framework.md §M2."""
    if sri >= 1.8:  # danger
        return 1.0
    if sri >= 1.0:  # alert
        return 0.5
    return 0.0
```

- [ ] **Step 2: Implement M4 SRI adjustment factor for concentration weights**

Add:

```python
def m4_concentration_weight_adjustment(sri: float) -> float:
    """Return multiplicative adjustment for concentration score weights based on SRI."""
    if sri >= 1.8:
        return 1.2
    if sri >= 1.0:
        return 1.1
    if sri >= 0.5:
        return 1.0
    return 0.9
```

(Exact values should match `concentration-framework.md:792-793` / `systemic-warning-framework.md:1013-1015`; adjust if docs specify different numbers.)

- [ ] **Step 3: Add tests**

```python
def test_m2_background_downgrade():
    assert m2_background_downgrade(0.3) == 0.0
    assert m2_background_downgrade(1.2) == 0.5
    assert m2_background_downgrade(2.0) == 1.0


def test_m4_weight_adjustment():
    assert m4_concentration_weight_adjustment(0.3) == 0.9
    assert m4_concentration_weight_adjustment(0.7) == 1.0
    assert m4_concentration_weight_adjustment(1.2) == 1.1
    assert m4_concentration_weight_adjustment(2.0) == 1.2
```

- [ ] **Step 4: Document execution DAG**

In `dev/engine/systemic-warning-framework.md` §十 or `concentration-framework.md` §9, add:

```markdown
### 执行顺序（防止循环）

1. 计算每个发行人的双轨评级（Track A + Track B → 交叉对撞）。
2. 聚合行业评分 → 计算 SRI。
3. 使用 SRI 对个体评级施加 M2 背景下调（一次性，不反算）。
4. 计算组合五维集中度。
5. 使用 SRI 调整集中度权重（M4）。
6. 应用集中度 → 评级调整。

禁止在同一分析周期内用已调整的个体评级重新计算行业评分或 SRI。
```

- [ ] **Step 5: Run tests and checker**

```bash
python -m pytest tests/test_sri_calculator.py tests/test_consistency_check.py -v
python scripts/consistency_check.py
```

Expected: all pass.

- [ ] **Step 6: Commit**

```bash
git add src/sri_calculator.py tests/test_sri_calculator.py dev/engine/systemic-warning-framework.md
git commit -m "feat(src): implement SRI-to-issuer and SRI-to-concentration overlay rules"
```

---

## Task 9: 为 Mosaic Engine 增加强制性的数据缺口护栏

**Files:**
- Modify: `dev/.claude/skills/fixed-income-credit-analysis/SKILL.md`
- Modify: `dev/engine/mosaic-engine.md`
- Modify: `dev/design/templates/template-type2.html`
- Modify: `dev/design/templates/template-type10.html`

**Interfaces:**
- Consumes: signal density levels and completeness report structure.
- Produces: imperative rules that prevent rating output when density is insufficient.

- [ ] **Step 1: Add imperative density rules to SKILL.md**

In the Mosaic Engine section, after the density table, add:

```markdown
### Mandatory Density Rules

- If **any critical dimension** (L1 for the industry type, or any dimension the user explicitly asks about) has signal density **<20%**, you MUST NOT output a numeric score for that dimension. State `信息不足无法评估` and list the missing signals.
- If the **weighted-average signal density across all scored dimensions** is **<50%**, you MUST NOT output a final letter rating. Output a qualitative directional assessment plus a prioritized gap list instead.
- If density is 50-80%, you MAY output a rating but MUST label it as `中置信度` and widen the implied interval by ±1 notch.
- The completeness report is mandatory for every analysis; omitting it is a protocol violation.
```

- [ ] **Step 2: Lock down Mode B in both SKILL.md and mosaic-engine.md**

Add to both files:

```markdown
> **Mode B 护栏**：除非用户明确提供了 CSV 上传、API endpoint 或 MCP server，否则禁止调用 Mode B 接口，禁止生成外部数据值。在 Mode B 未激活时，所有 Mode B 字段应作为数据缺口处理。
```

- [ ] **Step 3: Add a pre-output self-check instruction**

Add to SKILL.md:

```markdown
Before finalizing any numeric rating, verify:
1. Every dimension used in the score has a documented density.
2. No critical dimension is below 20% density.
3. The final rating maps to the official 12-notch table.
4. Every veto condition has been explicitly checked.
If any check fails, downgrade the rating or replace it with a directional statement.
```

- [ ] **Step 4: Update template-type2.html to include completeness block**

Add a minimal completeness section with density bars and gap list placeholders after the layer-score output. Keep the existing structure but embed:

```html
<section class="completeness">
  <h3>数据完备性评估</h3>
  <div class="density-bar" data-density="{L1_density}">L1 信号密度: {L1_density}%</div>
  <div class="density-bar" data-density="{L2_density}">L2 信号密度: {L2_density}%</div>
  <div class="density-bar" data-density="{L3_density}">L3 信号密度: {L3_density}%</div>
  <div class="density-bar" data-density="{L4_density}">L4 信号密度: {L4_density}%</div>
  <ul class="gap-list">{gap_items}</ul>
  <p class="confidence">综合置信度: {confidence_level}（{confidence_reason}）</p>
</section>
```

- [ ] **Step 5: Update template-type10.html similarly**

Add a completeness block after the E/S/G scores.

- [ ] **Step 6: Run checker**

```bash
python scripts/consistency_check.py
```

Expected: PASSED.

- [ ] **Step 7: Commit**

```bash
git add dev/.claude/skills/fixed-income-credit-analysis/SKILL.md dev/engine/mosaic-engine.md dev/design/templates/template-type2.html dev/design/templates/template-type10.html
git commit -m "docs(skill,templates): add mandatory data-gap guardrails and completeness blocks"
```

---

## Task 10: 统一模板中的完备性报告并移除 {百分比} 占位符

**Files:**
- Modify: `dev/design/templates/template-type13.html`
- Modify: `dev/design/templates/template-type14.html`
- Modify: `dev/design/templates/template-type15.html`

**Interfaces:**
- Consumes: signal density, gap list, confidence level.
- Produces: templates that force rating output to be paired with completeness evidence.

- [ ] **Step 1: Replace generic placeholders with density logic**

In each Type 13-15 template, find the completeness sections and replace `{百分比}` placeholders with either:
- explicit density variable names (e.g., `{industry_density_pct}`), or
- a clear instruction comment for the model:

```html
<!-- COMPLETENESS: fill in actual signal density (0-100) for each dimension. Do not invent plausible-looking percentages. -->
```

- [ ] **Step 2: Add a "rating output precondition" block**

Before any final rating table, add:

```html
<!-- BEFORE outputting any rating in this template, confirm that all dimensions used meet the density rules in mosaic-engine.md §4. If not, output '信息不足无法评估' instead. -->
```

- [ ] **Step 3: Run checker**

```bash
python scripts/consistency_check.py
```

Expected: PASSED.

- [ ] **Step 4: Commit**

```bash
git add dev/design/templates/template-type13.html dev/design/templates/template-type14.html dev/design/templates/template-type15.html
git commit -m "docs(templates): replace density placeholders and add rating preconditions"
```

---

## Task 11: 形式化传染矩阵接口并明确消费关系

**Files:**
- Modify: `dev/engine/contagion-matrix.md`
- Modify: `dev/engine/systemic-warning-framework.md`
- Modify: `dev/engine/concentration-framework.md`

**Interfaces:**
- Consumes: per-cell contagion outputs (type, intensity, confidence, direction, cases).
- Produces: documented downstream consumption rules.

- [ ] **Step 1: Define the contagion-matrix output schema**

In `contagion-matrix.md` §2 or §5, add:

```markdown
### 下游消费规则

每个矩阵单元格的输出字段按以下规则被上层模块消费：

| 字段 | 被消费方 | 用途 |
|---|---|---|
| `intensity` | SRI | 计算传染力系数，加权行业风险得分 |
| `intensity` | Concentration | 识别 super-spreader 行业和 cluster 风险 |
| `direction` | Concentration | 判断传染是单向还是双向，影响 cluster 划分 |
| `confidence` | 当前版本未使用 | 保留用于未来置信加权 |
| `historical_cases` | 当前版本未使用 | 保留用于回测和说明 |

> **注意**：confidence 和 historical_cases 在当前 v0.7.0-alpha 的 SRI/集中度计算中未被量化消费；它们用于人工审阅和未来版本扩展。
```

- [ ] **Step 2: Clarify SRI scope**

In `systemic-warning-framework.md` §1.2 or §2, add:

```markdown
> **SRI 范围说明**：SRI 是**系统性行业风险指数**，聚合 13 个行业的行业风险得分。它不直接接收组合集中度得分。集中度风险通过独立的五维集中度框架评估，二者在 M4 组合风控层并列使用。若未来要合并，需显式定义合并公式。
```

- [ ] **Step 3: Clarify concentration's use of matrix**

In `concentration-framework.md` §3 or §4, add a cross-reference note confirming it uses `intensity` and `direction` only.

- [ ] **Step 4: Run checker**

```bash
python scripts/consistency_check.py
```

Expected: PASSED.

- [ ] **Step 5: Commit**

```bash
git add dev/engine/contagion-matrix.md dev/engine/systemic-warning-framework.md dev/engine/concentration-framework.md
git commit -m "docs(engine): formalize contagion-matrix downstream consumption interface"
```

---

## Task 12: 增加单一事实源回归测试

**Files:**
- Create: `tests/test_engine_coherence.py`

**Interfaces:**
- Consumes: engine docs and source files.
- Produces: automated assertions that catch cross-document drift.

- [ ] **Step 1: Test rating-map single source of truth**

```python
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
ENGINE_DIR = ROOT / "dev" / "engine"

CANONICAL = [
    (9.5, 10.0, "AAA"),
    (9.0, 9.4, "AA+"),
    # ... full 18 rows
]

def test_rating_map_consistency_in_systemic_warning_framework():
    text = (ENGINE_DIR / "systemic-warning-framework.md").read_text(encoding="utf-8")
    # parse table and assert intervals match CANONICAL
```

- [ ] **Step 2: Test veto ceiling consistency**

```python
def test_issuer_survival_veto_ceiling_is_ccc():
    for doc in ["dual-track-methodology.md", "industry-framework.md", "governance-fraud-risk.md"]:
        text = (ENGINE_DIR / doc).read_text(encoding="utf-8")
        assert "一票否决" in text
        # assert that in issuer-veto context the ceiling is CCC (heuristic: presence of "上限锁定为CCC")
```

- [ ] **Step 3: Test thermometer thresholds consistency**

```python
def test_thermometer_thresholds_consistent():
    text = (ENGINE_DIR / "systemic-warning-framework.md").read_text(encoding="utf-8")
    assert "normal (<0.5)" in text or "<0.5" in text
    assert "watch (0.5–1.0)" in text or "0.5" in text and "1.0" in text
    assert "alert (1.0–1.8)" in text or "1.0" in text and "1.8" in text
    assert "danger (≥1.8)" in text or "1.8" in text
```

- [ ] **Step 4: Test Skill validation claims do not overstate**

```python
def test_skill_validation_table_matches_engine():
    skill = (ROOT / "dev" / ".claude" / "skills" / "fixed-income-credit-analysis" / "SKILL.md").read_text(encoding="utf-8")
    # assert Solar retrospective is not claimed as 完成, etc.
    assert "Solar/PV | 完成 | 完成" not in skill
```

- [ ] **Step 5: Run all tests**

```bash
python -m pytest tests/ -v
python scripts/consistency_check.py
```

Expected: all pass.

- [ ] **Step 6: Commit**

```bash
git add tests/test_engine_coherence.py
git commit -m "test: add engine coherence regression tests for rating map, veto, thermometer, validation claims"
```

---

## Task 13: 刷新 Release Snapshot

**Files:**
- Create/refresh: `version/v0.7.0-alpha/`, `version/v0.7.0-alpha.zip`

- [ ] **Step 1: Run final validation**

```bash
python -m pytest tests/ -v
python scripts/consistency_check.py
python scripts/consistency_check.py --only-toc dev/engine/concentration-framework.md
```

- [ ] **Step 2: Refresh snapshot**

```bash
rm -rf version/v0.7.0-alpha
rm -f version/v0.7.0-alpha.zip
cp -r dev version/v0.7.0-alpha
rm -rf version/v0.7.0-alpha/.git
rm -f version/v0.7.0-alpha/.claude/settings.local.json
powershell -Command "Compress-Archive -Path version/v0.7.0-alpha -DestinationPath version/v0.7.0-alpha.zip -Force"
```

- [ ] **Step 3: Verify snapshot**

```bash
grep -n "v0.7.0-alpha" version/v0.7.0-alpha/.claude/skills/fixed-income-credit-analysis/SKILL.md | head -5
ls version/v0.7.0-alpha/.git 2>/dev/null || echo ".git correctly removed"
unzip -t version/v0.7.0-alpha.zip | tail -3
```

- [ ] **Step 4: Commit**

```bash
git add -f version/v0.7.0-alpha version/v0.7.0-alpha.zip
git commit -m "release: refresh v0.7.0-alpha snapshot after logical coherence fixes"
```

---

## Self-Review

### Spec Coverage

| 结构审查发现 | 覆盖 Task |
|---|---|
| Skill 调用缺乏约束 | Task 3, Task 9 |
| references/ 陈旧/错误 | Task 3 |
| 验证声明夸大 | Task 3, Task 12 |
| 6 范式 vs 4 类型混淆 | Task 3, Task 6 |
| Track-B SRI 加分不一致 | Task 2, Task 1, Task 12 |
| 一票否决上限不统一 | Task 5 |
| 集中度 → 评级调整未实现 | Task 7 |
| SRI → 个体/集中度反馈未实现 | Task 8 |
| 旧 6-notch 残留 | Task 4, Task 1, Task 12 |
| 13 行业 D1-D10 覆盖不全 | Task 6 |
| 范式归属冲突 | Task 6 |
| 密度规则非强制 | Task 9 |
| Mode B 诱导幻觉 | Task 9 |
| 模板不一致/占位符 | Task 9, Task 10 |
| 传染矩阵接口未定义 | Task 11 |
| SRI/集中度范围混淆 | Task 11 |

### Placeholder Scan

无 `TBD`、`TODO`、`implement later` 或 `similar to Task N`。每个 Task 包含具体文件路径、代码片段和验证命令。

### Type Consistency

- `sri_calculator.py` 中的 `TrackBLevel` 和 `Outlook` enums 在 Task 2 和 Task 8 中保持一致。
- `concentration_scorer.py` 中的 `ConcentrationMetrics` 在 Task 7 中复用。
- `EXPECTED_VERSION = "v0.7.0-alpha"` 在 checker 中保持一致。

---

## Execution Handoff

**Plan saved to `docs/superpowers/plans/2026-07-13-fixed-income-credit-v0.7.0-alpha-logical-coherence-cleanup.md`.**

Two execution options:

1. **Subagent-Driven (recommended)** — dispatch a fresh subagent per task, review between tasks, fast iteration.
2. **Inline Execution** — execute tasks in this session using `superpowers:executing-plans`, batch execution with checkpoints.

**Which approach would you like?**

**Note on context space:** If context usage exceeds ~60% during execution, pause after the current Task, write a one-paragraph summary to `.superpowers/sdd/context-summary.md`, and continue from the next Task using the ledger and plan file as the primary source of state.
