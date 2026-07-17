# Fixed Income Credit Intelligent Analysis Engine

**Project Codename**: Credence
**Version**: v0.0.1
**Status**: Methodology documentation phase · Product design complete · International industry coverage · System intelligence layer online · Documentation structure reorganized

---

## Project Overview

International fixed-income credit analysis engine. Through industry-customized multi-layer analysis pyramid, dual-track cross-validation framework, mosaic public data engine, multi-stakeholder perspective, non-credit risk overlay, and system intelligence layer, it provides credit insight beyond traditional financial analysis for credit approval, bond investment, market trading, and risk management. Coverage includes international industry sectors with cross-industry contagion mapping, five-dimensional concentration dashboard, and systemic risk thermometer.

**Core Principle**: Traditional financial analysis systematically fails in policy-driven, technology-moat, and asset-lease industries. The heaviest credit factors rarely appear on the balance sheet. External credit ratings lag true credit deterioration by an average of 17+ months.

---

## Directory Structure

```
../AGENTS.md                                       ← 跨 CLI 通用入口（仓库根级 · 任何 agent CLI 从这里开始）
dev/
├── README.md                                        ← 你在这里
├── engine/                                          → 算法与方法论（28份现行文档）
│   ├── engine-overview.md                          架构总览 · 文档导航
│   ├── industry-framework.md                       行业分类（十维评分·13行业金字塔）
│   ├── qualitative-analysis.md                     定性分析（信源·政策·马赛克·叙事）
│   ├── quantitative-analysis.md                    定量分析（利差·波动率·因子·压力·市场信号）
│   ├── dual-track-methodology.md                   双轨+交叉对撞·12档评级·EL整合·缓释建议
│   ├── mosaic-engine.md                            马赛克引擎（信号·拼图·完备性·Mode B）
│   ├── multi-stakeholder.md                        多利益相关者（M0-M6·集中度风险·系统智能层集成）
│   ├── validation-methodology.md                   验证方法论（黑天鹅回溯·双时点·前瞻对比）
│   ├── financial-deep-dive.md                      财务深度（三表联动·营运资金·FCF·压力测试）
│   ├── lgd-recovery-framework.md                   LGD回收率（五级·抵押物·回收路径）
│   ├── external-support-framework.md               外部支持（政府/集团/战投·能力vs意愿）
│   ├── outlook-monitoring-framework.md             展望+监控（展望·观察名单·持续监控·迁移矩阵）
│   ├── lgfv-framework.md                           城投债（政府+平台双轨·四级分类）
│   ├── governance-fraud-risk.md                    治理/欺诈风险（20+信号·逃废债检测）
│   ├── esg-framework.md                            ESG + 治理/欺诈检测框架
│   ├── financial-bond-framework.md                 金融债分析框架
│   ├── holding-company-framework.md                控股公司信用分析框架
│   ├── non-credit-risk-overlay.md                  非信用风险叠加层（市场/操作/声誉/战略/流动性）
│   ├── output-layered-framework.md                 分层输出（L0信号卡+L1快照+L2深度+温度计卡片）
│   ├── contagion-theory.md                         传染理论（四类型·七传导路径·升级因子）
│   ├── contagion-matrix.md                         ⭐13×13行业传染矩阵（传导强度·行业聚类）
│   ├── concentration-framework.md                  ⭐五维集中度分析框架（阈值·评级调整·压力测试）
│   ├── systemic-warning-framework.md               ⭐系统性预警框架（SRI信号聚合·温度计·历史回测）
│   ├── paradigm-brand-channel.md                   品牌+渠道范式（食品饮料·纺织服装）
│   ├── paradigm-network-traffic.md                 网络+流量范式（交运·零售·传媒互联网）
│   ├── dimension-registry.md                       维度注册表（6范式+LGFV·M0-M5角色·可寻址索引）
│   └── audits/                                     15份历史审查/审计归档
│
├── templates/                                       → 报告模板单一事实源（16文件）
│   ├── template-base.css                           共享样式基底
│   └── template-type1..15.html                     Type 1 - Type 15 报告模板
│
├── design/                                          → 报告设计体系
│   ├── report-style-system.md                      报告样式系统
│   └── archive/                                    4份历史规划/审计（v0.6/v0.7路线图·phase2/报告审计）
│
├── data/                                            → 数据架构
│   ├── data-architecture.md                        数据源分层·可达性验证·缺口映射
│   └── data-pipeline-spec.md                       数据管道规格
│
├── product/                                         → 产品设计
│   ├── product-overview.md                         产品愿景 · 魔法体验 · 用户画像
│   └── commercial-model.md                         商业化模型 · 买方模拟 · GTM策略
│
└── .claude/skills/                                → AI技能包（四段链；模板统一引用 dev/templates/）
    ├── credit-analysis-router/                    ① intake：四问路由，产出《工作路径单》
    ├── fixed-income-credit-analysis/              ② analysis：按路径单执行分析，产出《分析产物》
    ├── credit-report-builder/                     ③ report：装配交付报告，产出《交付单》
    └── credit-qa-verifier/                        ④ qa：交付前终态质检，产出《质检裁决》
```

> 能力验证证据（72 份测试报告等）存档于仓库根级 `../validation/`，为测试输出而非项目组成部分，永不进入版本快照。（GitHub 主仓库仅公开 2 份行业方法论参照，其余实测报告保留在维护者本地。）

---

## Current Progress

### System Intelligence Layer

| 模块 | 状态 | 核心文档 |
|---|---|---|
| 传染图谱 | ✅ 完成 | contagion-theory.md · contagion-matrix.md |
| 集中度仪表盘 | ✅ 完成 | concentration-framework.md |
| 系统性预警 | ✅ 完成 | systemic-warning-framework.md |
| 温度计L0卡片 | ✅ 完成 | 集成至output-layered-framework.md §3.6 |

### Report Templates

| 类型 | 数量 | 说明 |
|---|---|---|
| 报告模板 | 15种（Type 1-Type 15） | `templates/` 单一事实源（template-base.css + type1-15.html） |

### Product Design (Complete)

产品愿景·Magic Experience·三层输出体系·商业化模型·定价·GTM

### Technical Implementation (Not Started)

方法和产品设计全部固化后启动。

---

## Quick Navigation

| 想了解... | 去看... |
|---|---|
| 报告模板（Type 1-15 + 共享样式） | `templates/` |
| 系统智能层总览 | `engine/systemic-warning-framework.md` + `engine/contagion-matrix.md` + `engine/concentration-framework.md` |
| 产品愿景和魔法体验 | `product/product-overview.md` |
| 怎么卖、卖给谁 | `product/commercial-model.md` |
| 分析引擎架构总览 | `engine/engine-overview.md` |
| 某个行业的分析框架 | `engine/industry-framework.md` |
| 定性分析方法论 | `engine/qualitative-analysis.md` |
| 定量分析方法论 | `engine/quantitative-analysis.md` |
| 双轨框架+交叉对撞 | `engine/dual-track-methodology.md` |
| 马赛克引擎+完备性评估 | `engine/mosaic-engine.md` |
| 多利益相关者视角 | `engine/multi-stakeholder.md` |
| 城投债分析框架 | `engine/lgfv-framework.md` |
| LGD/回收率评估 | `engine/lgd-recovery-framework.md` |
| 外部支持评估 | `engine/external-support-framework.md` |
| 传染矩阵与跨行业分析 | `engine/contagion-matrix.md` |
| 组合集中度评估 | `engine/concentration-framework.md` |
| 系统性风险指数 | `engine/systemic-warning-framework.md` |
| 报告设计样式体系 | `design/report-style-system.md` |
| 任意 agent CLI 的通用入口（Claude Code/Codex/Cursor/Gemini/OpenCode） | `../AGENTS.md` |
| 四段链产物契约（工作路径单/分析产物/交付单/质检裁决） | `engine/pipeline-contract.md` |
| 维度注册表（6范式+LGFV 与 M0-M5 角色的可寻址索引，单源指针层） | `engine/dimension-registry.md` |
| 可执行编排器（v0.7.8：以代码驱动四段链，接 WP-M4-01/-02/-03 三个编码引擎） | `../src/pipeline.py` |
| AI Agent使用这套方法论（四段链：路由/分析/报告/质检） | `.claude/skills/` |
| 版本管理策略与发布流程 | `../docs/VERSION-MANAGEMENT.md` |

---

## Version History

| Version | Date | Milestone |
|---|---|---|
| v0.0.1 | 2026-07-17 | Initial release: international fixed-income credit analysis engine |

---

*Last updated: 2026-07-17*
