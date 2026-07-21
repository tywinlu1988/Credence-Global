"""Drift guard for the machine-generated derived blocks in contagion-matrix.md.

scripts/build_contagion_derived.py regenerates every `<!-- GENERATED:* -->` block in
dev/engine/contagion-matrix.md from the §2.1 heatmap + §2.4 annotations (via
src.contagion_engine.load_matrix). These tests assert the doc is in sync and pin the
hand-verified values that previously drifted (row sums, distribution, cluster tiers).
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "build_contagion_derived.py"
DOC = ROOT / "dev" / "engine" / "contagion-matrix.md"


def test_derived_blocks_in_sync():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--check"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, (
        f"derived blocks drifted; run `python {SCRIPT} --write`\n{result.stdout}{result.stderr}"
    )


def test_derived_values_match_engine_computation():
    sys.path.insert(0, str(ROOT / "scripts"))
    import importlib.util

    spec = importlib.util.spec_from_file_location("bcd", SCRIPT)
    bcd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bcd)
    from src.contagion_engine import load_matrix, row_sums

    m = load_matrix(DOC)
    sums = row_sums(m)
    # hand-verified against the §2.1 heatmap
    assert sums["Financials (Banks/Insurance)"] == 47
    assert sums["Capital Goods"] == 43
    assert sums["Chemicals"] == sums["Technology Hardware (Semiconductors)"] == 42
    assert sum(sums.values()) == 662

    spreaders = bcd.gen_super_spreaders(m)
    assert "| 1 | **Financials (Banks/Insurance)** | **47** |" in spreaders

    dist = bcd.gen_intensity_distribution(m)
    assert "| 5 | 4 | 2 |" in dist and "| 1 | 150 | 75 |" in dist
    assert "**342**" in dist and "**171**" in dist

    clusters = bcd.gen_clusters(m, DOC.read_text(encoding="utf-8"))
    # F/G/H were mis-tiered as moderate in the hand-maintained era; all 7 sit in high
    assert clusters.count("| **A:") == 1 and "| **E:" in clusters.split("Moderate-Contagion")[1]
    high = clusters.split("#### Moderate-Contagion")[0]
    for label in ("A", "B", "C", "D", "F", "G", "H"):
        assert f"| **{label}:" in high


def test_base_matrix_fully_symmetric():
    from src.contagion_engine import load_matrix

    m = load_matrix(DOC)
    asymmetric = [
        (c.source, c.target)
        for c in m.itercells()
        if c.intensity != m.intensity(c.target, c.source)
    ]
    assert asymmetric == [], f"base matrix no longer symmetric: {asymmetric[:5]}"
