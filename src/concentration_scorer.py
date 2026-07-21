"""Five-dimensional concentration scoring engine (executable implementation of
dev/engine/concentration-framework.md).

Disambiguation and trimming notes (coding decisions where the document overlaps,
is not explicit, or exceeds what is implemented):

- **Linear interpolation (§1.3)**: bounded bands interpolate linearly and round to the
  nearest integer (`round()`), per §1.3 ("determine the specific score through linear
  interpolation within threshold intervals", HHI 1800 -> 6) and §8.5's D5 note (bond
  channel 75% -> 6). Rounding keeps each band's upper value reachable (5/7/9-class);
  Python's round-half-to-even affects only exact .5 boundaries, all of which land on
  even band starts (4/6). The §8.5 main table's 7s for the same raw metrics predate
  this rule and were corrected in v0.0.3. The top (danger) band floors at 8:
  the doc gives no within-band rule for 8-10.
- **Adjustment steps trimmed**: the per-dimension adjustment steps in §2.3 Step 4-5,
  §3.3.3, §4.4 Step 4-5, §5.4 Step 3-4 and the 24m/36m maturity metrics are NOT
  implemented (single-metric bands only). This is a declared trimming, not silent.
- **§7.2 stacking**: 5 x 🟠 triggers a systemic risk alert with individual
  adjustment "not applicable" (we return adjustment=None + systemic_risk_alert=True;
  it is NOT a §7.3 BB cap). For 1🔴+n🟠 (n>=2) the linear extension from the
  documented 1🔴+1🟠 level is kept (documented ambiguity: the usage note says
  "use the 1🔴+1🟠 level when 🔴 and 🟠 coexist").
- **§7.3 condition #5 ("channel freezing")** is signalled by the legacy
  `top_channel_is_contracting` flag; §6.3 synergy bonuses require the typed
  channel indicators (type + metric), not the bare flag.
"""

from dataclasses import dataclass


@dataclass
class ConcentrationMetrics:
    """Five-dimensional concentration metrics.

    BB-cap §7.3 inputs: condition #1 needs `track_a_score` (industry down-cycle,
    Track A < 5.0) and `industry_is_super_spreader` (contagion-matrix.md §5.1);
    condition #2 needs `region_had_soe_default` (SOE default in the region within
    the past 12 months). Without them, those conditions evaluate to False.
    §6.3 channel synergy needs `top_channel_type` plus the typed indicator
    (cancellation rate / credit growth / non-standard YoY change).
    """

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
    # §7.3 BB-cap conjunct inputs
    track_a_score: float | None = None
    industry_is_super_spreader: bool = False
    region_had_soe_default: bool = False
    # §6.3 channel synergy inputs
    top_channel_type: str = "other"  # bond / non-standard / bank / other
    channel_cancellation_rate: float | None = None
    credit_growth_yoy: float | None = None
    nonstd_balance_yoy_change: float | None = None
    all_channels_available: bool = False


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _interpolate(value: float, bands: tuple) -> int:
    """Linear interpolation within documented threshold bands (§1.3), rounded.

    bands: tuple of (lo, hi, s_lo, s_hi); hi=None marks the top (danger) band,
    which floors at s_lo (the doc defines no within-band rule for 8-10).
    """
    for lo, hi, s_lo, s_hi in bands:
        if hi is None:
            if value >= lo:
                return s_lo
            break
        if lo <= value < hi:
            frac = (value - lo) / (hi - lo)
            return round(s_lo + frac * (s_hi - s_lo))
    return bands[0][2]


# Threshold bands per concentration-framework.md §2.2-§6.2 (1-3 normal / 4-5 watch / 6-7 alert / 8-10 danger).
_HHI_BANDS = ((0.0, 1000.0, 1, 3), (1000.0, 1500.0, 4, 5), (1500.0, 2500.0, 6, 7), (2500.0, None, 8, 10))
_CR3_BANDS = ((0.0, 0.50, 1, 3), (0.50, 0.65, 4, 5), (0.65, 0.80, 6, 7), (0.80, None, 8, 10))
_CR5_BANDS = ((0.0, 0.70, 1, 3), (0.70, 0.80, 4, 5), (0.80, 0.90, 6, 7), (0.90, None, 8, 10))
_MAX1_BANDS = ((0.0, 0.25, 1, 3), (0.25, 0.40, 4, 5), (0.40, 0.60, 6, 7), (0.60, None, 8, 10))
_PROVINCE_BANDS = ((0.0, 0.20, 1, 3), (0.20, 0.35, 4, 5), (0.35, 0.50, 6, 7), (0.50, None, 8, 10))
_WEAK_REGION_BANDS = ((0.0, 0.10, 1, 3), (0.10, 0.20, 4, 5), (0.20, 0.35, 6, 7), (0.35, None, 8, 10))
_AAA_BANDS = ((0.0, 0.30, 1, 3), (0.30, 0.50, 4, 5), (0.50, 0.70, 6, 7), (0.70, None, 8, 10))
_PSEUDO_BANDS = ((0.0, 0.05, 1, 3), (0.05, 0.15, 4, 5), (0.15, 0.30, 6, 7), (0.30, None, 8, 10))
_M12_BANDS = ((0.0, 0.30, 1, 3), (0.30, 0.50, 4, 5), (0.50, 0.70, 6, 7), (0.70, None, 8, 10))
_PEAK_BANDS = ((0.0, 0.10, 1, 3), (0.10, 0.20, 4, 5), (0.20, 0.30, 6, 7), (0.30, None, 8, 10))
_CHANNEL_BANDS = ((0.0, 0.50, 1, 3), (0.50, 0.70, 4, 5), (0.70, 0.90, 6, 7), (0.90, None, 8, 10))


def industry_score(metrics: ConcentrationMetrics) -> int:
    """D1: Industry concentration (HHI/CR3/CR5/MAX1; worst metric governs per §1.3)."""
    return max(
        _interpolate(metrics.hhi, _HHI_BANDS),
        _interpolate(metrics.cr3, _CR3_BANDS),
        _interpolate(metrics.cr5, _CR5_BANDS),
        _interpolate(metrics.max1, _MAX1_BANDS),
    )


def region_score(metrics: ConcentrationMetrics) -> int:
    """D2: Regional concentration (single country/region + weak region share)."""
    return max(
        _interpolate(metrics.single_province_share, _PROVINCE_BANDS),
        _interpolate(metrics.weak_region_share, _WEAK_REGION_BANDS),
    )


def rating_score(metrics: ConcentrationMetrics) -> int:
    """D3: Rating concentration (external AAA + pseudo-high-rating share)."""
    return max(
        _interpolate(metrics.aaa_share, _AAA_BANDS),
        _interpolate(metrics.pseudo_high_rating_share, _PSEUDO_BANDS),
    )


def maturity_score(metrics: ConcentrationMetrics) -> int:
    """D4: Maturity concentration (12-month share + single-month peak)."""
    return max(
        _interpolate(metrics.maturity_12m_share, _M12_BANDS),
        _interpolate(metrics.single_month_peak, _PEAK_BANDS),
    )


def channel_score(metrics: ConcentrationMetrics) -> int:
    """D5: Funding-channel concentration (top channel share + §6.3 synergy)."""
    base = _interpolate(metrics.top_channel_share, _CHANNEL_BANDS)
    bonus = 0
    if (
        metrics.top_channel_type == "bond"
        and metrics.top_channel_share > 0.70
        and metrics.channel_cancellation_rate is not None
        and metrics.channel_cancellation_rate > 15.0
    ):
        bonus = 2  # §6.3: bond channel > 70% + cancellation rate > 15%
    elif (
        metrics.top_channel_type == "non-standard"
        and metrics.top_channel_share > 0.50
        and metrics.nonstd_balance_yoy_change is not None
        and metrics.nonstd_balance_yoy_change < -20.0
    ):
        bonus = 3  # §6.3: non-standard channel > 50% + balance YoY decline > 20%
    elif (
        metrics.top_channel_type == "bank"
        and metrics.top_channel_share > 0.70
        and metrics.credit_growth_yoy is not None
        and metrics.credit_growth_yoy < 8.0
    ):
        bonus = 1  # §6.3: bank channel > 70% + credit growth < 8%
    elif metrics.all_channels_available and metrics.top_channel_share < 0.50:
        bonus = -1  # §6.3: highly diversified funding channels
    return int(_clamp(base + bonus, 1, 10))


def _risk_level(score: int) -> str:
    """Map a 1-10 risk score to a four-level traffic-light classification."""
    if score >= 8:
        return "red"
    if score >= 6:
        return "orange"
    if score >= 4:
        return "yellow"
    return "green"


def rating_adjustment(metrics: ConcentrationMetrics) -> dict:
    """Return rating adjustment in notches and flags per concentration-framework.md §7.

    Implements the non-linear multi-dimensional stacking table in §7.2 and the
    threshold-based BB-cap trigger conditions in §7.3. Returns
    ``{"adjustment", "levels", "bb_cap_triggered", "systemic_risk_alert"}``;
    ``adjustment`` is None when §7.2 declares it not applicable (5 x 🟠).
    """
    levels = {
        "industry": _risk_level(industry_score(metrics)),
        "region": _risk_level(region_score(metrics)),
        "rating": _risk_level(rating_score(metrics)),
        "maturity": _risk_level(maturity_score(metrics)),
        "channel": _risk_level(channel_score(metrics)),
    }

    red_count = sum(1 for lvl in levels.values() if lvl == "red")
    orange_count = sum(1 for lvl in levels.values() if lvl == "orange")

    # §7.2: all 5 dimensions 🟠 -> systemic risk alert; individual issuer
    # adjustment rules NOT applicable (distinct from the §7.3 BB cap).
    systemic_risk_alert = red_count == 0 and orange_count == 5

    # Non-linear stacking lookup per §7.2.
    if systemic_risk_alert:
        adjustment = None
    elif red_count == 0:
        adjustment = {0: 0.0, 1: -0.5, 2: -1.0, 3: -1.5, 4: -2.0}[orange_count]
    elif red_count == 1:
        if orange_count == 0:
            adjustment = -1.0
        elif orange_count == 1:
            adjustment = -1.5
        else:
            # Extend linearly beyond the documented 1-red+1-orange case:
            # -0.5 per additional orange, capped at the 2-red value.
            adjustment = max(-2.5, -1.5 - 0.5 * (orange_count - 1))
    else:  # red_count >= 2
        adjustment = -2.5

    # Threshold-based BB-cap triggers per §7.3 (any single condition).
    bb_cap_triggered = (
        red_count >= 3
        # #1: single industry > 50% AND down-cycle (Track A < 5.0) AND super-spreader
        or (
            metrics.max1 > 0.50
            and metrics.track_a_score is not None
            and metrics.track_a_score < 5.0
            and metrics.industry_is_super_spreader
        )
        # #2: weak region > 35% AND SOE default in region within past 12 months
        or (metrics.weak_region_share > 0.35 and metrics.region_had_soe_default)
        # #3: pseudo-high-rating share > 40%
        or metrics.pseudo_high_rating_share > 0.40
        # #4: next-12-months maturity > 70% AND funding channel dependency > 70%
        or (metrics.maturity_12m_share > 0.70 and metrics.top_channel_share > 0.70)
        # #5: single funding channel > 90% AND that channel is freezing
        or (metrics.top_channel_share > 0.90 and metrics.top_channel_is_contracting)
    )

    return {
        "adjustment": adjustment,
        "levels": levels,
        "bb_cap_triggered": bb_cap_triggered,
        "systemic_risk_alert": systemic_risk_alert,
    }


def concentration_risk_score(
    metrics: ConcentrationMetrics,
    weights: tuple[float, float, float, float, float] = (0.25, 0.20, 0.20, 0.20, 0.15),
) -> float:
    """Five-dimensional weighted concentration risk score (1-10 scale).

    Default weights follow dev/engine/concentration-framework.md §8.2:
    industry 25%, region 20%, rating 20%, maturity 20%, channel 15%.
    """
    if len(weights) != 5:
        raise ValueError("weights must contain exactly 5 values")
    if abs(sum(weights) - 1.0) > 1e-6:
        raise ValueError("weights must sum to 1.0")

    scores = (
        industry_score(metrics),
        region_score(metrics),
        rating_score(metrics),
        maturity_score(metrics),
        channel_score(metrics),
    )
    return sum(s * w for s, w in zip(scores, weights))
