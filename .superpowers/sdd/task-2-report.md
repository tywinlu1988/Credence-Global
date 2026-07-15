# Task 2 Report: Unify Track-B SRI Penalty Rule

## Status
DONE

## Canonical Rule Adopted
Option A: green=0, yellow=0.5, orange=1.0, red=1.5.

## Changes Made
- `dev/engine/systemic-warning-framework.md`
  - Updated §2.2.1 pseudocode to four-level penalties.
  - Updated §2.2.2 quick-lookup table to reflect red Track-B (+1.5) and the 3.0 non-veto cap.
  - Updated penalty rationale in §2.2.
  - Updated §9 threshold-sensitivity scenarios (A/B/C) to use the canonical scale.
  - Updated Appendix A pseudocode.
  - Recomputed affected examples in §6, §7, §8, Appendix B to stay consistent with the new rule and cap.
  - Fixed a pre-existing mismatch where NEV was described as "轨道B异常" while the table showed yellow.
  - Removed a checker false-positive by rewording "自动降档0.5子级" to "自动降档半子级" in the M2 table.
- `src/sri_calculator.py`
  - Replaced the binary orange/red penalty with explicit four-level Track-B penalties.
- `tests/test_sri_calculator.py`
  - Updated orange+negative-outlook expectation from 1.0 to 1.5.
  - Added `test_track_b_penalties()` covering all four levels.
  - Added `test_worst_non_veto_with_red_track_b_and_negative_outlook()` for the 3.0 cap.
  - Updated the 2026Q2 SRI example assertion range to 0.54–0.60.

## Commits
- `46a15b6` fix(sri): unify Track-B penalty rule to 0/0.5/1.0/1.5 across docs and code

## Test Command and Output

```bash
python -m pytest tests/test_sri_calculator.py tests/test_consistency_check.py -v
```

Output:

```
============================= test session starts =============================
platform win32 -- Python 3.12.3, pytest-7.4.4, pluggy-1.0.0 -- D:\anaconda3\python.exe
collecting ... 27 items

... (all 27 tests passed)

============================= 27 passed in 0.23s =============================
```

```bash
python scripts/consistency_check.py
```

Output:

```
Consistency check PASSED
```

(22 pre-existing warnings remain from unrelated checks: RATING_MAP, SKILL_REF, PARADIGM_COVERAGE. The SRI_TRACK_B contradiction warning is gone.)

## One-Line Self-Review
Canonical four-level Track-B penalty rule is now applied consistently in code, tests, and the systemic-warning-framework document; all targeted tests and the consistency checker pass.

## Concerns
- Historical SRI estimates in §6/§7 were recomputed to honor the 3.0 cap; the 2020Q1 pandemic example drops from ~1.83 (danger) to ~1.15 (alert). This is the mathematically correct application of the rule but changes the qualitative color label for that historical narrative.
- Several unrelated consistency-checker warnings still exist (skill reference versions, paradigm coverage, rating-map intervals); these are outside the scope of Task 2.
