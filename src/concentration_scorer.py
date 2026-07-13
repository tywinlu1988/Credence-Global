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
