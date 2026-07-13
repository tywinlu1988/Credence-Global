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
