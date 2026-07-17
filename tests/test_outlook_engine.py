"""WP-X-05 outlook_engine 测试。

单一事实源纪律：漂移门期望值从文档运行时解析（§2.2 行数、§3.1 行数、§5.1 评级行、
§5.3 行业行），计算层测试用 fixture 信号/触发表。
"""

import re

import pytest

from src.outlook_engine import (
    LAYER_WEIGHTS,
    load_factor_matrix,
    load_migration_table,
    migration_range,
    outlook_assessment,
    watchlist_check,
)
from src.path_sheet import engine_dir

DOC = engine_dir() / "outlook-monitoring-framework.md"


def _text():
    return DOC.read_text(encoding="utf-8")


# ---------------- 解析层（真实文档） ----------------

def test_factor_matrix_counts():
    fm = load_factor_matrix(DOC)
    pos = [k for k, v in fm.items() if v[1] == "positive"]
    neg = [k for k, v in fm.items() if v[1] == "negative"]
    text = _text()
    pos_sec = re.search(r"#### 正面展望触发信号\n(.*?)(?=\n#### |\Z)", text, re.DOTALL).group(1)
    neg_sec = re.search(r"#### 负面展望触发信号\n(.*?)(?=\n### |\Z)", text, re.DOTALL).group(1)
    assert len(pos) == len(re.findall(r"^\|\s*\*\*(?:L[1-4]|外部支持)", pos_sec, re.MULTILINE))
    assert len(neg) == len(re.findall(r"^\|\s*\*\*(?:L[1-4]|外部支持)", neg_sec, re.MULTILINE))
    assert len(pos) > 0 and len(neg) > 0
    assert all(v[0] in LAYER_WEIGHTS for v in fm.values())


def test_watchlist_trigger_counts_in_doc():
    """§3.1 触发表行数漂移门（负 21 / 正 6，以文档行为为准）。"""
    text = _text()
    neg = re.search(r"#### 负面观察触发条件\n(.*?)(?=\n#### |\Z)", text, re.DOTALL).group(1)
    pos = re.search(r"#### 正面观察触发条件\n(.*?)(?=\n### |\Z)", text, re.DOTALL).group(1)
    assert len(re.findall(r"^\|\s*\*\*(事件驱动|财务突变|政策冲击|市场信号)\*\*", neg, re.MULTILINE)) == 21
    assert len(re.findall(r"^\|\s*\*\*(事件驱动|财务突变|政策冲击|市场信号)\*\*", pos, re.MULTILINE)) == 6


def test_migration_table_structure():
    table, adj = load_migration_table(DOC)
    assert len(table) == 12
    for rating in ("AAA", "AA+", "D"):
        assert rating in table
    assert "A / A-" in table and "BBB / BBB-" in table
    for cells in table.values():
        assert all(cells[k] for k in ("上调", "维持", "下调", "违约"))
    text = _text()
    assert len(adj) == len(re.findall(r"^\|\s*\*\*.+?\*\*\s*\|\s*(?:上调|下调)概率\+", text, re.MULTILINE))


# ---------------- 展望计分（§2.3） ----------------

def test_outlook_positive():
    r = outlook_assessment([
        {"layer": "L1", "direction": "positive"},
        {"layer": "L2", "direction": "positive"},
        {"layer": "L3", "direction": "negative"},
    ])
    # +1.5 +1.2 -1.0 = +1.7 < 2.0 → 稳定（单方向不足阈）
    assert r["outlook"] == "稳定"
    assert abs(r["net_score"] - 1.7) < 1e-9


def test_outlook_negative_and_counts():
    r = outlook_assessment([
        {"layer": "L1", "direction": "negative"},
        {"layer": "L4", "direction": "negative"},
        {"layer": "L4", "direction": "positive"},
    ])
    # -1.5 -0.8 +0.8 = -1.5 未达 -2.0 → 稳定
    assert r["outlook"] == "稳定"
    assert r["counts"] == {"positive": 1, "negative": 2}
    r2 = outlook_assessment([
        {"layer": "L1", "direction": "negative"},
        {"layer": "外部支持", "direction": "negative"},
    ])
    # -1.5 -1.2 = -2.7 ≤ -2.0 且负≥2 → 负面
    assert r2["outlook"] == "负面"


def test_outlook_developing_precedence():
    sigs = [{"layer": "L1", "direction": "positive"}] * 3 + [
        {"layer": "L1", "direction": "negative"}] * 3
    r = outlook_assessment(sigs)
    assert r["outlook"] == "发展中"  # 正≥3 且负≥3 且 |net|=0 < 2.0


def test_outlook_confidence_tiers():
    high = outlook_assessment(
        [{"layer": "L1", "direction": "positive"},
         {"layer": "L2", "direction": "positive"},
         {"layer": "L3", "direction": "positive"},
         {"layer": "L4", "direction": "positive"}])
    assert high["confidence"] == "高"
    low = outlook_assessment([{"layer": "L1", "direction": "positive"}])
    assert low["confidence"] == "低"
    none = outlook_assessment([])
    assert none["confidence"] == "极低" and none["outlook"] == "稳定"


def test_outlook_layer_weights_values():
    assert LAYER_WEIGHTS["L1"] > LAYER_WEIGHTS["L2"] > LAYER_WEIGHTS["L3"] > LAYER_WEIGHTS["L4"]
    # 与文档 §2.3 文本互证（权重已写回文档）
    for layer, w in LAYER_WEIGHTS.items():
        assert f"{layer}={w}" in _text()


# ---------------- 观察名单（§3.1/§3.2） ----------------

def test_watchlist_negative_priority_and_windows():
    r = watchlist_check([
        {"side": "positive", "event": "集团注资"},
        {"side": "negative", "event": "被监管立案调查"},
    ])
    assert r["entered"] and r["side"] == "负面观察"  # 双方同触发→负面优先
    assert r["review"]["initial_review_days"] == 30 and r["review"]["full_review_days"] == 60
    assert r["window_days"] == 90 and r["extension_max_days"] == 60


def test_watchlist_positive_and_empty():
    r = watchlist_check([{"side": "positive", "event": "政府纾困"}])
    assert r["side"] == "正面观察" and r["review"]["full_review_days"] == 60
    assert watchlist_check([])["entered"] is False


# ---------------- 迁移矩阵（§5.1/§5.3） ----------------

def test_migration_range_base_and_merged():
    r = migration_range("AA+")
    assert set(("上调", "维持", "下调", "违约", "paradigm_note")) <= set(r)
    a = migration_range("A")
    am = migration_range("A-")
    assert a["上调"] == am["上调"]  # 合并行 "A / A-" 接受任一子级
    with pytest.raises(ValueError, match="未知评级"):
        migration_range("CC")


def test_migration_range_paradigm_shift():
    base = migration_range("AA")
    shifted = migration_range("AA", paradigm="政策驱动型")
    assert shifted["paradigm_note"]
    # 基础下调 "10%" → 政策驱动型 +5-10% → 15-20%
    assert base["下调"] == "10%" and shifted["下调"] == "15-20%"
    with pytest.raises(ValueError, match="未知行业类型"):
        migration_range("AA", paradigm="不存在型")
