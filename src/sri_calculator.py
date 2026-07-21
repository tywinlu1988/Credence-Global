"""Systemic Risk Index calculation engine (executable implementation of
dev/engine/systemic-warning-framework.md).

Single-source discipline: every rule value is parsed from the engine document at load
time via `load_sri_rules` — §2.2.1 base bands / outlook & Track-B penalties / veto,
Appendix A score cap, §3.1 thermometer tiers, and §10.1 M4 adjustment factors.
Nothing in this module may hardcode a threshold; if the document changes, the engine
follows (and `load_sri_rules` raises loudly on structural drift).
"""

import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from src.path_sheet import engine_dir


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


# ---------------------------------------------------------------------------
# Runtime-parsed rules (document = single source of truth)
# ---------------------------------------------------------------------------

_BASE_BAND_RE = re.compile(r"(?:(\d+\.\d+)\s*≤\s*)?Track A\s*<\s*(\d+\.\d+)[^\n]*?→\s*(\d+)\s*points?")
_BASE_TOP_RE = re.compile(r"(\d+\.\d+)\s*≤\s*Track A\s*≤\s*(\d+\.\d+)[^\n]*?→\s*(\d+)\s*points?")
_OUTLOOK_RE = re.compile(r"(Negative|Stable|Positive) outlook\s*→\s*\+?(\d+(?:\.\d+)?)\s*points?")
_TRACKB_RE = re.compile(r"Track B signal (🟢|🟡|🟠|🔴)\s*\((\w+)\)\s*→\s*\+?(\d+(?:\.\d+)?)\s*points?")
_VETO_RE = re.compile(r"Industry Risk Score = (\d+(?:\.\d+)?) points \(forced\)")
_CAP_RE = re.compile(r"min\(base \+ outlook_penalty \+ track_B_penalty, (\d+(?:\.\d+)?)\)")
_THERMO_RE = re.compile(
    r"^\|\s*(Normal|Watch|Alert|Danger)\s*\|\s*(?:(\d+(?:\.\d+)?)\s*≤\s*)?SRI\s*(?:<|≤|≥)\s*(\d+(?:\.\d+)?)",
    re.MULTILINE,
)
_M4_RE = re.compile(r"(🟢|🟡|🟠|🔴)\s*\w+:\s*\+?(\d+)%")

_TRACKB_NAME_TO_LEVEL = {"calm": "green", "watch": "yellow", "abnormal": "orange", "crisis": "red"}
_EMOJI_TO_TIER = {"🟢": "normal", "🟡": "watch", "🟠": "alert", "🔴": "danger"}

_RULES_CACHE: dict = {}


def load_sri_rules(path=None) -> dict:
    """Parse SRI rules from systemic-warning-framework.md (cached per path)."""
    doc = Path(path) if path else engine_dir() / "systemic-warning-framework.md"
    key = str(doc.resolve())
    if key in _RULES_CACHE:
        return _RULES_CACHE[key]
    text = doc.read_text(encoding="utf-8")

    sec = re.search(r"#### 2\.2\.1 .*?(?=\n#### |\n### |\Z)", text, re.DOTALL)
    if not sec:
        raise ValueError("systemic-warning-framework.md §2.2.1 missing")
    body = sec.group(0)

    bands = [(float(m.group(2)), int(m.group(3))) for m in _BASE_BAND_RE.finditer(body)]
    top = _BASE_TOP_RE.search(body)
    if top:
        bands.append((float("inf"), int(top.group(3))))
    bands = sorted(set(bands), key=lambda b: b[0])
    if len(bands) != 4:
        raise ValueError(f"§2.2.1 should define 4 base bands, got {bands}")

    outlook = {m.group(1).lower(): float(m.group(2)) for m in _OUTLOOK_RE.finditer(body)}
    if set(outlook) != {"negative", "stable", "positive"}:
        raise ValueError(f"§2.2.1 outlook penalties incomplete: {outlook}")

    track_b = {}
    for m in _TRACKB_RE.finditer(body):
        level = _TRACKB_NAME_TO_LEVEL.get(m.group(2).lower())
        if level is None:
            raise ValueError(f"unknown Track B level name: {m.group(2)!r}")
        track_b[level] = float(m.group(3))
    if set(track_b) != {"green", "yellow", "orange", "red"}:
        raise ValueError(f"§2.2.1 Track B penalties incomplete: {track_b}")

    veto = _VETO_RE.search(body)
    cap = _CAP_RE.search(text)
    if not veto or not cap:
        raise ValueError("veto score (§2.2.1) or score cap (Appendix A) missing")

    tiers = []
    for m in _THERMO_RE.finditer(text):
        name = m.group(1).lower()
        if name == "normal":
            continue
        # tier lower bound: explicit lower bound when present ("0.5 ≤ SRI < 1.0"),
        # else the single bound ("SRI ≥ 1.8")
        tiers.append((float(m.group(2) or m.group(3)), name))
    tiers.sort()
    if [t[1] for t in tiers] != ["watch", "alert", "danger"]:
        raise ValueError(f"§3.1 thermometer tiers incomplete: {tiers}")

    sec_m4 = re.search(r"#### M4 .*?```(.*?)```", text, re.DOTALL)
    if not sec_m4:
        raise ValueError("§10.1 M4 adjustment block missing")
    m4_factor = {}
    for m in _M4_RE.finditer(sec_m4.group(1)):
        tier = _EMOJI_TO_TIER.get(m.group(1))
        if tier:
            m4_factor[tier] = int(m.group(2)) / 100.0
    if set(m4_factor) != {"normal", "watch", "alert", "danger"}:
        raise ValueError(f"§10.1 M4 factors incomplete: {m4_factor}")

    rules = {
        "base_bands": bands,
        "outlook_penalty": outlook,
        "track_b_penalty": track_b,
        "veto_score": float(veto.group(1)),
        "cap": float(cap.group(1)),
        "thermometer": tiers,
        "m4_factor": m4_factor,
    }
    _RULES_CACHE[key] = rules
    return rules


# ---------------------------------------------------------------------------
# Engine functions (all values from load_sri_rules)
# ---------------------------------------------------------------------------

def _validate_industry(ind: IndustryInput) -> None:
    """Hard-fail on invalid inputs — a silently zero-scored industry is worse than a crash."""
    if not (0.0 <= ind.track_a_score <= 10.0):
        raise ValueError(f"track_a_score out of 0-10 range: {ind.track_a_score!r} (industry {ind.name!r})")
    if not isinstance(ind.track_b_level, TrackBLevel):
        try:
            TrackBLevel(ind.track_b_level)
        except ValueError:
            raise ValueError(
                f"unknown track_b_level: {ind.track_b_level!r} (industry {ind.name!r}, "
                f"available {[e.value for e in TrackBLevel]})"
            ) from None
    if not isinstance(ind.outlook, Outlook):
        try:
            Outlook(ind.outlook)
        except ValueError:
            raise ValueError(
                f"unknown outlook: {ind.outlook!r} (industry {ind.name!r}, "
                f"available {[e.value for e in Outlook]})"
            ) from None


def industry_risk_score(ind: IndustryInput) -> float:
    _validate_industry(ind)
    rules = load_sri_rules()
    if ind.veto_triggered:
        return rules["veto_score"]

    base = 0
    for upper, score in rules["base_bands"]:
        if ind.track_a_score < upper:
            base = score
            break

    outlook_penalty = rules["outlook_penalty"].get(ind.outlook.value, 0.0)
    track_b_penalty = rules["track_b_penalty"].get(ind.track_b_level.value, 0.0)
    return min(base + outlook_penalty + track_b_penalty, rules["cap"])


def sri(industries: list[IndustryInput], weights: list[float]) -> float:
    if len(industries) != len(weights):
        raise ValueError("industries and weights must have same length")
    if any(w < 0 for w in weights):
        raise ValueError(f"weights must not contain negative values: {weights}")
    if abs(sum(weights) - 1.0) > 1e-6:
        raise ValueError("weights must sum to 1.0")

    return sum(industry_risk_score(ind) * w for ind, w in zip(industries, weights))


def thermometer_level(sri_value: float) -> str:
    level = "normal"
    for threshold, name in load_sri_rules()["thermometer"]:
        if sri_value >= threshold:
            level = name
    return level


def m2_background_downgrade(sri: float) -> float:
    """Return notch downgrade for individual issuers based on systemic-warning-framework.md §10.1 M2."""
    tiers = dict((name, t) for t, name in load_sri_rules()["thermometer"])
    if sri >= tiers["danger"]:
        return 1.0
    if sri >= tiers["alert"]:
        return 0.5
    return 0.0


def m4_concentration_weight_adjustment(sri: float) -> float:
    """Return the SRI adjustment multiplier for the concentration composite score.

    Per systemic-warning-framework.md §10.1 M4:
      Composite Score = Original Score × (1 + SRI Adjustment Factor)
      (factor values are parsed from the document's M4 percentage table)
    """
    factors = load_sri_rules()["m4_factor"]
    tier = thermometer_level(sri)
    return 1.0 + factors[tier]
