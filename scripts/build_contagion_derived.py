#!/usr/bin/env python3
"""Regenerate the derived (computed) tables in dev/engine/contagion-matrix.md from the
§2.1 heatmap + §2.4 annotations -- the doc's derived sections were historically
hand-maintained and drifted from the heatmap (wrong row sums, impossible odd link
counts for a symmetric matrix, mis-tiered clusters).

Single source of truth chain: §2.1/§2.4 (parsed by src.contagion_engine.load_matrix)
-> this generator -> GENERATED blocks in the doc. Narrative text outside the markers
is hand-maintained; everything between `<!-- GENERATED:<key> -->` and
`<!-- /GENERATED -->` is machine-owned.

Usage:
  python scripts/build_contagion_derived.py --write   # regenerate blocks in place
  python scripts/build_contagion_derived.py --check   # exit 1 if any block drifts
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "dev" / "engine" / "contagion-matrix.md"

sys.path.insert(0, str(ROOT))
from src.contagion_engine import load_matrix, row_sums  # noqa: E402

BEGIN_RE = re.compile(r"<!-- GENERATED:([a-z-]+) -->")
END = "<!-- /GENERATED -->"


# ---------------------------------------------------------------------------
# Derived data
# ---------------------------------------------------------------------------

def _unique_pairs(m):
    """Unordered unique pairs from directed cells, with the source->target cell."""
    pairs = {}
    for c in m.itercells():
        key = tuple(sorted((c.source, c.target)))
        pairs.setdefault(key, c)
    return pairs


def _fmt_annotation(c) -> str:
    types = "+".join(c.types) if c.types else "-"
    return f"({types}, {c.confidence})"


def gen_high_intensity_links(m) -> str:
    pairs = [c for c in _unique_pairs(m).values() if c.intensity >= 4]
    fives = sorted((c for c in pairs if c.intensity == 5), key=lambda c: (c.source, c.target))
    fours = sorted((c for c in pairs if c.intensity == 4), key=lambda c: (c.source, c.target))
    lines = ["```", "Score 5 (Very Strong):"]
    for c in fives:
        arrow = "↔" if c.bidirectional else "→"
        lines.append(f"  {c.source} {arrow} {c.target}  {_fmt_annotation(c)}")
    lines.append("")
    lines.append("Score 4 (Strong):")
    for c in fours:
        arrow = "↔" if c.bidirectional else "→"
        lines.append(f"  {c.source} {arrow} {c.target}  {_fmt_annotation(c)}")
    lines.append("")
    lines.append(
        f"Total: {len(pairs)} unique high-intensity pairs "
        f"({len(pairs) * 2} directed links, score >= 4), including {len(fives)} pairs at score 5"
    )
    lines.append("```")
    return "\n".join(lines)


def _key_targets(m, industry, n_min=3) -> str:
    hits = []
    for c in m.itercells():
        if c.source == industry and c.intensity >= n_min:
            hits.append((c.target, c.intensity))
    hits.sort(key=lambda x: (-x[1], x[0]))
    return ", ".join(f"{t}({s})" for t, s in hits)


def gen_super_spreaders(m) -> str:
    sums = row_sums(m)
    ranked = sorted(sums.items(), key=lambda kv: (-kv[1], kv[0]))
    lines = [
        "| Rank | Industry | Row Sum | Key Targets (Score >= 3) |",
        "|---|---|---|---|",
    ]
    prev_sum, rank = None, 0
    for i, (name, s) in enumerate(ranked[:5]):
        rank = i + 1 if s != prev_sum else rank
        prev_sum = s
        lines.append(f"| {rank} | **{name}** | **{s}** | {_key_targets(m, name)} |")
    return "\n".join(lines)


def gen_vulnerable(m) -> str:
    # Base matrix is symmetric: column sums == row sums (see §4.2).
    sums = row_sums(m)
    ranked = sorted(sums.items(), key=lambda kv: (-kv[1], kv[0]))
    lines = [
        "| Rank | Industry | Column Sum | Key Sources (Score >= 3) |",
        "|---|---|---|---|",
    ]
    prev_sum, rank = None, 0
    for i, (name, s) in enumerate(ranked[:5]):
        rank = i + 1 if s != prev_sum else rank
        prev_sum = s
        lines.append(f"| {rank} | **{name}** | **{s}** | {_key_targets(m, name)} |")
    return "\n".join(lines)


def _coeff_table(m, col_header: str) -> str:
    sums = row_sums(m)
    top = max(sums.values())
    ranked = sorted(sums.items(), key=lambda kv: (-kv[1], kv[0]))
    lines = [
        f"| Rank | Industry | {col_header} | Coefficient |",
        "|---|---|---|---|",
    ]
    prev_sum, rank = None, 0
    for i, (name, s) in enumerate(ranked):
        rank = i + 1 if s != prev_sum else rank
        prev_sum = s
        lines.append(f"| {rank} | {name} | {s} | {s / top:.2f} |")
    return "\n".join(lines)


def gen_cfc(m) -> str:
    return _coeff_table(m, "Row Sum")


def gen_cvc(m) -> str:
    return _coeff_table(m, "Col Sum")


def gen_cner(m) -> str:
    sums = row_sums(m)
    ranked = sorted(sums.items(), key=lambda kv: (-kv[1], kv[0]))
    lines = [
        "| Industry | Row Sum | Col Sum | CNER | Interpretation |",
        "|---|---|---|---|---|",
    ]
    for name, s in ranked:
        lines.append(f"| {name} | {s} | {s} | 1.00 | Balanced |")
    return "\n".join(lines)


def gen_intensity_distribution(m) -> str:
    directed = Counter(c.intensity for c in m.itercells())
    pairs = Counter(c.intensity for c in _unique_pairs(m).values())
    total_d = sum(directed.values())
    lines = [
        "| Intensity | Directed Links | Unique Pairs | Share of Directed |",
        "|---|---|---|---|",
    ]
    for score in sorted(directed):
        d, u = directed[score], pairs[score]
        lines.append(f"| {score} | {d} | {u} | {d / total_d * 100:.1f}% |")
    lines.append(f"| **Total** | **{total_d}** | **{sum(pairs.values())}** | 100.0% |")
    return "\n".join(lines)


def gen_row_col_sums(m) -> str:
    sums = row_sums(m)
    top = max(sums.values())
    ranked = sorted(sums.items(), key=lambda kv: (-kv[1], kv[0]))
    lines = [
        "| Rank | Industry | Row Sum | Col Sum | CFC (Row/Max) |",
        "|---|---|---|---|---|",
    ]
    prev_sum, rank = None, 0
    for i, (name, s) in enumerate(ranked):
        rank = i + 1 if s != prev_sum else rank
        prev_sum = s
        lines.append(f"| {rank} | {name} | {s} | {s} | {s / top:.2f} |")
    total = sum(sums.values())
    mean = total / len(sums)
    lines.append(f"| | **Total / Mean** | **{total}** | **{total}** | mean {mean:.2f} |")
    return "\n".join(lines)


def gen_clusters(m, text: str) -> str:
    """Parse the §5.4 cluster tables (composition is methodology, hand-maintained),
    compute each cluster's intra-cluster average intensity from the heatmap, and
    re-emit the two tier tables with computed averages. Tier rule (§5.4): high >= 3.0."""
    cluster_re = re.compile(
        r"^\|[ \t]*\*\*([A-H]):[ \t]*([^*]+)\*\*[ \t]*\|([^|]+)\|([^|]+)\|",
        re.MULTILINE,
    )
    sec = re.search(r"### 5\.4 .*?(?=\n## |\Z)", text, re.DOTALL)
    clusters = []
    for mm in cluster_re.finditer(sec.group(0) if sec else ""):
        label = mm.group(1).strip()
        title = mm.group(2).strip()
        industries = [i.strip() for i in mm.group(3).split(",")]
        core_links = mm.group(4).strip()
        clusters.append((label, title, industries, core_links))

    def avg_intensity(industries):
        vals = []
        for i, a in enumerate(industries):
            for b in industries[i + 1:]:
                try:
                    vals.append(m.intensity(a, b))
                except ValueError:
                    return None
        return sum(vals) / len(vals) if vals else None

    computed = []
    for label, title, industries, core_links in clusters:
        avg = avg_intensity(industries)
        computed.append((label, title, industries, core_links, avg))

    high = [c for c in computed if c[4] is not None and c[4] >= 3.0]
    moderate = [c for c in computed if c[4] is not None and c[4] < 3.0]
    unknown = [c for c in computed if c[4] is None]

    def table(rows):
        lines = [
            "| Cluster | Industries | Core Links | Intra Avg |",
            "|---|---|---|---|",
        ]
        for label, title, industries, core_links, avg in rows:
            lines.append(f"| **{label}: {title}** | {', '.join(industries)} | {core_links} | {avg:.1f} |")
        return lines

    out = ["#### High-Contagion Cluster (Intra-cluster average intensity >= 3.0)", ""]
    out.extend(table(high))
    out.append("")
    out.append("#### Moderate-Contagion Cluster (Intra-cluster average intensity 2.0-2.9)")
    out.append("")
    out.extend(table(moderate))
    if unknown:
        out.append("")
        out.append("> Warning: cluster(s) with unresolvable industries: " + ", ".join(c[0] for c in unknown))
    return "\n".join(out)


GENERATORS = {
    "high-intensity-links": gen_high_intensity_links,
    "super-spreaders": gen_super_spreaders,
    "vulnerable-industries": gen_vulnerable,
    "cfc-table": gen_cfc,
    "cvc-table": gen_cvc,
    "cner-table": gen_cner,
    "intensity-distribution": gen_intensity_distribution,
    "row-col-sums": gen_row_col_sums,
    "clusters": gen_clusters,
}


def regenerate(text: str, m) -> tuple[str, list[str]]:
    """Replace every GENERATED block's content. Returns (new_text, keys_not_generated)."""
    lines = text.split("\n")
    out = []
    i = 0
    skipped = []
    while i < len(lines):
        line = lines[i]
        match = BEGIN_RE.search(line)
        if not match:
            out.append(line)
            i += 1
            continue
        key = match.group(1)
        # find the END marker
        j = i + 1
        while j < len(lines) and lines[j].strip() != END:
            j += 1
        if j >= len(lines):
            raise ValueError(f"unterminated GENERATED block: {key}")
        gen = GENERATORS.get(key)
        if gen is None:
            skipped.append(key)
            out.extend(lines[i:j + 1])
        else:
            out.append(line)
            if key == "clusters":
                out.append(gen(m, text))
            else:
                out.append(gen(m))
            out.append(END)
        i = j + 1
    return "\n".join(out), skipped


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true", help="regenerate blocks in place")
    ap.add_argument("--check", action="store_true", help="exit 1 if any GENERATED block drifts")
    args = ap.parse_args()
    if not (args.write or args.check):
        ap.error("pass --write or --check")

    m = load_matrix(DOC)
    text = DOC.read_text(encoding="utf-8")
    new_text, skipped = regenerate(text, m)
    if skipped:
        print(f"warning: no generator for block keys: {skipped}", file=sys.stderr)

    if args.write:
        if new_text != text:
            DOC.write_text(new_text, encoding="utf-8", newline="\n")
            print(f"regenerated derived blocks in {DOC}")
        else:
            print("all derived blocks already up to date")
        return 0

    if new_text != text:
        print("DRIFT: contagion-matrix.md GENERATED blocks are stale; run --write")
        return 1
    print("derived blocks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
