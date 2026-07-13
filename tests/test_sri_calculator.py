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
    # Distribute the residual weight across the other nine industries so the
    # full vector sums to 1.0.  The other industries have zero risk score, so
    # the residual does not change the SRI value.
    residual = 1.0 - sum(weights[:4])
    valid_weights = weights[:4] + [residual / 9] * 9
    result = sri(industries, valid_weights)
    assert 0.35 <= result <= 0.40


def test_thermometer():
    assert thermometer_level(0.2) == "normal"
    assert thermometer_level(0.6) == "watch"
    assert thermometer_level(1.2) == "alert"
    assert thermometer_level(2.0) == "danger"
