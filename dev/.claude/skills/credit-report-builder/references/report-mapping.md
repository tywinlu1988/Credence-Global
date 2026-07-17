# 路径 → 模板 → 分层 映射视图

**版本**: v0.0.1

> 本表是 `credit-report-builder` 的装配映射视图：给定 `path_id`，列出应选模板与主分层。模板清单的单一事实源为 `dev/engine/work-path-registry.md`（各路径 `templates` 字段）；分层语义的单一事实源为 `dev/engine/output-layered-framework.md` §二/§三/§五。本表不含任何阈值、分层时间预算或评级值——凡数值判断以所引引擎文档为准。本表如出现与该两份文档不一致之处，以其为准。

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

## 分层指针（单一事实源）

- 三层输出总览与导航关系：`dev/engine/output-layered-framework.md` §二
- L0 信号卡（版面/元素/温度计卡片）：`dev/engine/output-layered-framework.md` §三
- L1 快照（四维雷达/关键异常/评级对比/排名）：`dev/engine/output-layered-framework.md` §四
- L2 深度报告（四屏结构/导航规则）：`dev/engine/output-layered-framework.md` §五
- 完备性灯号呈现：`dev/engine/output-layered-framework.md` §8.4

## 模板标记值（与 registry §schema 一致）

- `planned`：模板待开发（无文件），如实告知"待开发"，不伪造渲染产物。
- `L0-spec`：无独立模板文件，规范定义于所引引擎文档（L0 信号卡规范见 `dev/engine/output-layered-framework.md` §三）。

> 深度档 `L0/L1/L2` 决定主分层；`专项` 路径的交付物由所选模板定义，分层语义仍以上述引擎文档为准。
