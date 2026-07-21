import pytest

from src.concentration_scorer import (
    ConcentrationMetrics,
    channel_score,
    concentration_risk_score,
    industry_score,
    maturity_score,
    rating_adjustment,
    rating_score,
    region_score,
)


def test_high_concentration():
    metrics = ConcentrationMetrics(
        hhi=2600,
        cr3=0.85,
        cr5=0.92,
        max1=0.65,
        single_province_share=0.40,
        weak_region_share=0.25,
        aaa_share=0.75,
        pseudo_high_rating_share=0.35,
        maturity_12m_share=0.75,
        single_month_peak=0.35,
        top_channel_share=0.80,
        top_channel_is_contracting=True,
    )
    assert concentration_risk_score(metrics) >= 6.0


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


def test_all_five_dimensions_contribute():
    high = ConcentrationMetrics(
        hhi=2600,
        cr3=0.85,
        cr5=0.92,
        max1=0.65,
        single_province_share=0.50,
        weak_region_share=0.35,
        aaa_share=0.75,
        pseudo_high_rating_share=0.35,
        maturity_12m_share=0.75,
        single_month_peak=0.35,
        top_channel_share=0.80,
        top_channel_type="bond",
        channel_cancellation_rate=18.0,
    )
    assert industry_score(high) >= 8
    assert region_score(high) >= 8
    assert rating_score(high) >= 8
    assert maturity_score(high) >= 8
    assert channel_score(high) >= 8
    assert concentration_risk_score(high) >= 8.0


def test_channel_contraction_bonus():
    # §6.3 synergy: bond channel > 70% + cancellation rate > 15% -> base + 2.
    # 75% share lands in the alert band -> floor-interp 6 (§8.5) + 2 = 8.
    contracting = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.75,
        top_channel_type="bond", channel_cancellation_rate=18.0,
    )
    assert channel_score(contracting) == 8

    # Share below the >70% synergy gate -> no bonus even with high cancellation.
    below_gate = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.60,
        top_channel_type="bond", channel_cancellation_rate=18.0,
    )
    relaxed = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.60,
    )
    assert channel_score(below_gate) == channel_score(relaxed)


def test_channel_synergy_nonstandard_and_bank():
    base = dict(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
    )
    # §6.3: non-standard channel > 50% + balance YoY decline > 20% -> +3.
    nonstd = ConcentrationMetrics(
        **base, top_channel_share=0.55,
        top_channel_type="non-standard", nonstd_balance_yoy_change=-25.0,
    )
    # 55% in [50,70) watch band -> 4 + 3 = 7
    assert channel_score(nonstd) == 7

    # §6.3: bank channel > 70% + credit growth < 8% -> +1.
    bank = ConcentrationMetrics(
        **base, top_channel_share=0.75,
        top_channel_type="bank", credit_growth_yoy=6.0,
    )
    # 75% in [70,90) alert band -> 6 + 1 = 7
    assert channel_score(bank) == 7


def test_channel_diversification_bonus():
    # §6.3: all channels available with single < 50% -> -1.
    diversified = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.45, all_channels_available=True,
    )
    # 45% in normal band [0,50) -> round-interp 3 - 1 = 2
    assert channel_score(diversified) == 2


def test_rating_orange_and_danger_bands():
    # 20% pseudo-high-rating is in the alert band [15%, 30%) -> floor-interp 6.
    orange = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.20,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    assert rating_score(orange) == 6

    # 75% AAA share reaches the top (danger) band -> floor at 8.
    danger = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.75, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    assert rating_score(danger) == 8


def test_maturity_orange_band():
    # 60% 12-month maturity is in the alert band [50%, 70%) -> floor-interp 6.
    metrics = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.60, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    assert maturity_score(metrics) == 6


def test_region_danger_band():
    # 50% single-province share reaches the top (danger) band -> floor at 8.
    metrics = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.50, weak_region_share=0.35,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    assert region_score(metrics) == 8


def test_interpolation_matches_doc_examples():
    # §1.3: HHI = 1800 (warning band 1500-2500) -> linear interpolation -> 6.
    # §8.5: MAX1 = 42% (alert band 40-60%) -> 6.
    metrics = ConcentrationMetrics(
        hhi=1800, cr3=0.30, cr5=0.50, max1=0.42,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    assert industry_score(metrics) == 6


def test_interpolation_rounds_to_nearest_band_value():
    # Interpolation rounds (not floors): the upper half of a band reaches the
    # band's upper score, keeping 5/7/9-class values reachable.
    # HHI 2200 in [1500, 2500) -> 6 + 0.7 -> 7.
    assert industry_score(_base_metrics(hhi=2200)) == 7
    # MAX1 55% in [40%, 60%) -> 6 + 0.75 -> 7.
    assert industry_score(_base_metrics(max1=0.55)) == 7
    # HHI 1800 in [1500, 2500) -> 6 + 0.3 -> 6 (doc §1.3 anchor).
    assert industry_score(_base_metrics(hhi=1800)) == 6


def test_concentration_weights_must_sum_to_one():
    metrics = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    with pytest.raises(ValueError):
        concentration_risk_score(metrics, weights=(0.25, 0.25, 0.25, 0.25, 0.10))


def test_concentration_weights_must_have_length_five():
    metrics = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    with pytest.raises(ValueError):
        concentration_risk_score(metrics, weights=(0.25, 0.25, 0.25, 0.25))


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


def test_rating_adjustment_two_oranges():
    metrics = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.25,
        aaa_share=0.20, pseudo_high_rating_share=0.20,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    adj = rating_adjustment(metrics)
    assert adj["levels"]["region"] == "orange"
    assert adj["levels"]["rating"] == "orange"
    assert adj["adjustment"] == -1.0
    assert adj["bb_cap_triggered"] is False


def test_rating_adjustment_one_red_one_orange():
    # Industry red driven by HHI only, avoiding the single-industry proxy.
    metrics = ConcentrationMetrics(
        hhi=2600, cr3=0.55, cr5=0.65, max1=0.30,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.20,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    adj = rating_adjustment(metrics)
    assert adj["levels"]["industry"] == "red"
    assert adj["levels"]["rating"] == "orange"
    assert adj["adjustment"] == -1.5
    assert adj["bb_cap_triggered"] is False


def test_rating_adjustment_two_reds():
    # Industry red via HHI; region red via single province (not weak region).
    metrics = ConcentrationMetrics(
        hhi=2600, cr3=0.55, cr5=0.65, max1=0.30,
        single_province_share=0.50, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    adj = rating_adjustment(metrics)
    assert adj["levels"]["industry"] == "red"
    assert adj["levels"]["region"] == "red"
    assert adj["adjustment"] == -2.5
    assert adj["bb_cap_triggered"] is False


def test_rating_adjustment_three_reds():
    metrics = ConcentrationMetrics(
        hhi=2600, cr3=0.55, cr5=0.65, max1=0.30,
        single_province_share=0.50, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.35,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    adj = rating_adjustment(metrics)
    assert sum(1 for lvl in adj["levels"].values() if lvl == "red") == 3
    assert adj["bb_cap_triggered"] is True


def test_bb_cap_weak_region_threshold():
    # §7.3 #2: weak region > 35% AND SOE defaults in region within past 12 months.
    with_default = _base_metrics(weak_region_share=0.40, region_had_soe_default=True)
    assert rating_adjustment(with_default)["bb_cap_triggered"] is True
    # Share alone is not sufficient without the SOE-default condition.
    without_default = _base_metrics(weak_region_share=0.40, region_had_soe_default=False)
    assert rating_adjustment(without_default)["bb_cap_triggered"] is False


def test_bb_cap_pseudo_high_rating_threshold():
    metrics = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.45,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    adj = rating_adjustment(metrics)
    assert adj["bb_cap_triggered"] is True


def test_bb_cap_maturity_channel_overlap():
    metrics = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.75, single_month_peak=0.05,
        top_channel_share=0.75,
    )
    adj = rating_adjustment(metrics)
    assert adj["bb_cap_triggered"] is True


def test_bb_cap_channel_freeze_threshold():
    metrics = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.95, top_channel_is_contracting=True,
    )
    adj = rating_adjustment(metrics)
    assert adj["bb_cap_triggered"] is True


def _base_metrics(**overrides) -> ConcentrationMetrics:
    values = dict(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    values.update(overrides)
    return ConcentrationMetrics(**values)


def test_region_watch_band_scores_four():
    # 25% single-province share is in the documented watch band (20-35%) -> 4-5 score.
    assert region_score(_base_metrics(single_province_share=0.25)) == 4


def test_rating_watch_band_scores_four():
    # 40% AAA share is in the documented watch band (30-50%) -> 4-5 score.
    assert rating_score(_base_metrics(aaa_share=0.40)) == 4


def test_maturity_watch_band_scores_four():
    # 40% 12-month maturity share is in the documented watch band (30-50%) -> 4-5 score.
    assert maturity_score(_base_metrics(maturity_12m_share=0.40)) == 4


def test_channel_watch_band_scores_four():
    # 60% top-channel share is in the documented watch band (50-70%) -> 4-5 score.
    assert channel_score(_base_metrics(top_channel_share=0.60)) == 4


def test_watch_band_dimension_maps_to_yellow_level():
    # A watch-band dimension must surface as yellow, not green (concentration-framework.md §1.3).
    adj = rating_adjustment(_base_metrics(single_province_share=0.25))
    assert adj["levels"]["region"] == "yellow"


def test_risk_level_boundaries():
    from src.concentration_scorer import _risk_level
    assert _risk_level(2) == "green"
    assert _risk_level(3) == "green"
    assert _risk_level(4) == "yellow"
    assert _risk_level(5) == "yellow"
    assert _risk_level(6) == "orange"
    assert _risk_level(7) == "orange"
    assert _risk_level(8) == "red"
    assert _risk_level(9) == "red"
    assert _risk_level(10) == "red"


def test_rating_adjustment_four_oranges():
    metrics = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.25,
        aaa_share=0.20, pseudo_high_rating_share=0.20,
        maturity_12m_share=0.60, single_month_peak=0.05,
        top_channel_share=0.80,
    )
    adj = rating_adjustment(metrics)
    assert sum(1 for lvl in adj["levels"].values() if lvl == "orange") == 4
    assert adj["adjustment"] == -2.0
    assert adj["bb_cap_triggered"] is False


def test_rating_adjustment_one_red_zero_orange():
    metrics = ConcentrationMetrics(
        hhi=2600, cr3=0.55, cr5=0.65, max1=0.30,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.01,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    adj = rating_adjustment(metrics)
    assert sum(1 for lvl in adj["levels"].values() if lvl == "red") == 1
    assert sum(1 for lvl in adj["levels"].values() if lvl == "orange") == 0
    assert adj["adjustment"] == -1.0
    assert adj["bb_cap_triggered"] is False


def test_bb_cap_single_industry_boundary():
    # §7.3 #1 is a triple conjunct: single industry > 50% AND down-cycle
    # (Track A < 5.0) AND super-spreader. Share alone never triggers.
    assert rating_adjustment(_base_metrics(max1=0.50))["bb_cap_triggered"] is False
    assert rating_adjustment(_base_metrics(max1=0.51))["bb_cap_triggered"] is False
    # Full conjunct triggers.
    full = _base_metrics(max1=0.51, track_a_score=4.5, industry_is_super_spreader=True)
    assert rating_adjustment(full)["bb_cap_triggered"] is True
    # Missing super-spreader attribute -> no trigger.
    no_spreader = _base_metrics(max1=0.51, track_a_score=4.5, industry_is_super_spreader=False)
    assert rating_adjustment(no_spreader)["bb_cap_triggered"] is False
    # Not in down-cycle -> no trigger.
    up_cycle = _base_metrics(max1=0.51, track_a_score=5.5, industry_is_super_spreader=True)
    assert rating_adjustment(up_cycle)["bb_cap_triggered"] is False


def test_bb_cap_weak_region_boundary():
    # §7.3 #2 boundary: > 35% (strict) with the SOE-default condition met.
    at_cap = _base_metrics(weak_region_share=0.36, region_had_soe_default=True)
    below_cap = _base_metrics(weak_region_share=0.34, region_had_soe_default=True)
    assert rating_adjustment(at_cap)["bb_cap_triggered"] is True
    assert rating_adjustment(below_cap)["bb_cap_triggered"] is False


def test_five_oranges_systemic_alert_not_bb_cap():
    # §7.2: all 5 dimensions 🟠 triggers a systemic risk alert — the individual
    # issuer adjustment rules are NOT applicable. It is not a §7.3 BB cap.
    metrics = ConcentrationMetrics(
        hhi=1800, cr3=0.70, cr5=0.85, max1=0.45,
        single_province_share=0.40, weak_region_share=0.25,
        aaa_share=0.55, pseudo_high_rating_share=0.20,
        maturity_12m_share=0.60, single_month_peak=0.25,
        top_channel_share=0.80,
    )
    adj = rating_adjustment(metrics)
    assert set(adj["levels"].values()) == {"orange"}
    assert adj["adjustment"] is None
    assert adj["systemic_risk_alert"] is True
    assert adj["bb_cap_triggered"] is False


def test_bb_cap_pseudo_high_rating_boundary():
    at_cap = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.41,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    below_cap = ConcentrationMetrics(
        hhi=500, cr3=0.30, cr5=0.50, max1=0.15,
        single_province_share=0.10, weak_region_share=0.02,
        aaa_share=0.20, pseudo_high_rating_share=0.39,
        maturity_12m_share=0.20, single_month_peak=0.05,
        top_channel_share=0.30,
    )
    assert rating_adjustment(at_cap)["bb_cap_triggered"] is True
    assert rating_adjustment(below_cap)["bb_cap_triggered"] is False


def test_metrics_share_range_checked():
    with pytest.raises(ValueError, match="range"):
        rating_adjustment(_base_metrics(aaa_share=-0.1))
    with pytest.raises(ValueError, match="range"):
        rating_adjustment(_base_metrics(top_channel_share=1.2))
    with pytest.raises(ValueError, match="range"):
        concentration_risk_score(_base_metrics(weak_region_share=1.5))
    with pytest.raises(ValueError, match="range"):
        concentration_risk_score(_base_metrics(hhi=-100))
