# Report Style and Layout System · Design Specification

**Version**: v1.0
**Date**: 2026-07-08
**Status**: Design Under Review

---

## 1. Color System

### Base Palette (Common to All Reports)

```css
:root {
  /* Background Layer */
  --bg-primary:    #0f1117;
  --bg-secondary:  #1a1d28;
  --bg-tertiary:   #212433;
  --bg-hover:      #252b38;

  /* Text Layer */
  --text-primary:   #e2e4ea;
  --text-secondary: #9398a9;
  --text-tertiary:  #5d6270;

  /* Border Layer */
  --border-default: #2a2e3c;
  --border-strong:  #3d4250;
}
```

### Semantic Palette (Common to All Reports)

```css
  /* Red: Risk/Warning/Decline/Veto */
  --red:       #ef4444;
  --red-bg:    rgba(239,68,68,0.08);

  /* Amber: Watch/Pending/Volatility/Mitigation */
  --amber:     #f59e0b;
  --amber-bg:  rgba(245,158,11,0.08);

  /* Green: Safe/Passed/Increase/Positive */
  --green:     #22c55e;
  --green-bg:  rgba(34,197,94,0.08);

  /* Blue: Information/Link/Neutral/Data */
  --blue:      #6366f1;
  --blue-bg:   rgba(99,102,241,0.08);

  /* Purple: Methodology/Meta-Analysis/System/Version */
  --purple:    #a855f7;
  --purple-bg: rgba(168,85,247,0.08);
```

### Usage Rules

| Color | Text Color | Background Color | Bar/Border | Prohibited Use |
|---|---|---|---|---|
| Red | `.text-red` | `.bg-red` | `.border-red` | Decorative large area use |
| Amber | `.text-amber` | `.bg-amber` | `.border-amber` | Headings (easily confused with red) |
| Green | `.text-green` | `.bg-green` | `.border-green` | Warning/risk annotations |
| Blue | `.text-blue` | `.bg-blue` | `.border-blue` | Positive/negative signals |
| Purple | `.text-purple` | `.bg-purple` | `.border-purple` | Data display |

---

## 2. Typography and Layout

### Font Stack

```css
--font-body: -apple-system, BlinkMacSystemFont, "Segoe UI",
             "PingFang SC", "Microsoft YaHei", sans-serif;
--font-mono: "SF Mono", "Cascadia Code", "Consolas", monospace;
```

### Font Size Hierarchy (16px Base)

| Level | Selector | Size | Weight | Usage |
|---|---|---|---|---|
| H1 | `.report-title` | 30px | 800 | Page main title |
| H2 | `.section-title` | 19px | 700 | Section title |
| H3 | `.card-title` | 15px | 600 | Card title |
| H4 | `.sub-title` | 14px | 600 | Subtitle |
| Body | `body, p, li` | 14px | 400 | Body text |
| Caption | `.caption` | 12px | 400 | Auxiliary description |
| Micro | `.micro` | 10px | 400 | Footnote/watermark |
| Table Head | `thead th` | 11px | 600 | Table header |
| Table Body | `tbody td` | 13px | 400 | Table body |
| Num Large | `.num-lg` | 26px | 800 | Score/amount |
| Num XLarge | `.num-xl` | 36px | 800 | Core conclusion number |

### Typography Rules

- Line height: body 1.6, long text 1.8, heading 1.3
- Paragraph spacing: 1em
- Container max width: 960px (page level)
- Global padding: 24px (desktop) / 16px (mobile)
- Number columns right-aligned, text columns left-aligned

---

## 3. Layout Skeleton

```
┌──────────────────────────────────────────────┐
│  HERO Area (Full Width, Gradient Background)  │
│  .hero                                          │
│  ├── .hero-chip  Type tag (rounded chip)        │
│  ├── h1          Main title                     │
│  ├── p           Subtitle/description           │
│  └── .hero-meta  Meta information tag row       │
├──────────────────────────────────────────────┤
│  CONTENT Area (Centered max-width: 960px)      │
│  .container                                     │
│  ├── .strip      Top bar number strip (4-6 cols)│
│  ├── .section    Content section                │
│  │   ├── .section-title  Section title          │
│  │   ├── .card    Card component                │
│  │   ├── table    Table component               │
│  │   ├── .metric-grid  Metric grid (2-4 cols)   │
│  │   └── .timeline     Timeline component       │
│  └── ...                                        │
├──────────────────────────────────────────────┤
│  FOOTER (Full Width, Single Line Divider)      │
│  .footer                                        │
└──────────────────────────────────────────────┘
```

### Responsive Breakpoints

| Breakpoint | Adjustment |
|---|---|
| ≤768px | Grid reduces to 1 column · Hero title 24px · strip reduces to 2 columns · Global padding 16px |
| ≤480px | strip reduces to 1 column · Font size proportionally reduced 10% · Table horizontal scroll |

---

## 4. Component Library

### 4.1 Card

```css
.card {
  background: var(--bg-secondary);
  border-radius: 8px;
  padding: 20px 24px;
  border: 1px solid var(--border-default);
}
.card-red   { border-left: 4px solid var(--red); }
.card-amber { border-left: 4px solid var(--amber); }
.card-green { border-left: 4px solid var(--green); }
.card-blue  { border-left: 4px solid var(--blue); }
.card-purple{ border-left: 4px solid var(--purple); }
```

### 4.2 Strip (Top Bar Number Strip)

```css
.strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);  /* or 2/3/5/6 columns */
  gap: 1px;
  background: var(--border-default);
  border-radius: 10px;
  overflow: hidden;
}
.strip-item {
  background: var(--bg-secondary);
  padding: 20px 16px;
  text-align: center;
}
```

### 4.3 Table

```css
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  background: var(--bg-secondary);
  border-radius: 6px;
  overflow: hidden;
}
thead th {
  background: var(--bg-tertiary);
  padding: 9px 13px;
  font-weight: 600;
  font-size: 11px;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.4px;
  border-bottom: 2px solid var(--border-default);
}
tbody td {
  padding: 9px 13px;
  border-bottom: 1px solid var(--border-default);
}
tbody tr:hover { background: var(--bg-hover); }
```

### 4.4 Metric Grid

```css
.metric-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 12px;
}
.metric {
  background: var(--bg-tertiary);
  border-radius: 8px;
  padding: 16px 18px;
  text-align: center;
  border: 1px solid var(--border-default);
}
.metric .m-num  { font-size: 28px; font-weight: 800; }
.metric .m-label{ font-size: 12px; color: var(--text-secondary); }
```

### 4.5 Timeline

```css
.timeline {
  position: relative;
  padding-left: 28px;
}
.timeline::before {
  content: '';
  position: absolute;
  left: 12px;
  top: 4px; bottom: 4px;
  width: 2px;
  background: var(--border-default);
}
.timeline-item {
  position: relative;
  padding: 10px 0 10px 20px;
  font-size: 13px;
}
.timeline-item::before {
  content: '';
  position: absolute;
  left: -20px; top: 14px;
  width: 12px; height: 12px;
  border-radius: 50%;
}
.timeline-item.red::before   { background: var(--red); }
.timeline-item.amber::before { background: var(--amber); }
.timeline-item.green::before { background: var(--green); }
```

### 4.6 Score Colors

| Score Range | Color | Class Name |
|---|---|---|
| ≥7.5 | Green | `.score-good` |
| 5.0-7.4 | Blue | `.score-ok` |
| 3.0-4.9 | Amber | `.score-warn` |
| <3.0 | Red | `.score-bad` |

### 4.7 Signal Indicator Light

```css
.signal { display: inline-block; width: 10px; height: 10px; border-radius: 50%; }
.signal-red   { background: var(--red); }
.signal-amber { background: var(--amber); }
.signal-green { background: var(--green); }
```

### 4.8 Tab Navigation (Multi-Industry Overview Page Only)

```css
.tab-bar {
  display: flex;
  gap: 0;
  overflow-x: auto;
  border-bottom: 1px solid var(--border-default);
}
.tab-label {
  flex-shrink: 0;
  padding: 10px 18px;
  font-size: 13px;
  font-weight: 500;
  color: var(--text-secondary);
  cursor: pointer;
  border-bottom: 2px solid transparent;
  white-space: nowrap;
}
.tab-label.active {
  color: var(--blue);
  border-bottom-color: var(--blue);
}
```

---

## 5. 12 Report Types

| # | Type | Hero Gradient Direction | Typical Strip Columns | Core Components |
|---|---|---|---|---|
| 1 | Single Entity Deep Analysis | 135deg, #0f172a, #1e3a5f | 4 columns | Pyramid + Cross Collision + Risk List + Completeness |
| 2 | Dual Entity Forward-Looking Comparison | 135deg, #0f172a, #1e3a5f, #065f46 | 2x4 columns | Layer-by-layer comparison table + Score gap analysis + Framework improvement |
| 3 | Black Swan Retrospective Verification | 135deg, #0f172a, #4a1a1a, #7c2d12 | 4 columns | Timeline + Dual time points + Narrative decomposition + Rating analysis |
| 4 | Multi-Identity Parallel Assessment | 135deg, #0f172a, #1e3a5f, #4a1a1a | 3 columns | Identity cards + Cross matrix + Consensus/Divergence |
| 5 | Bond Investment Dashboard | 135deg, #0f172a, #1e3a5f, #1a3a2a | 4 columns | Four-dimensional analysis + Ranking table + Event calendar + Gaps |
| 6 | Mosaic Completeness Report | 135deg, #0f172a, #312e81 | 4 columns | Signal density bar + Signal list + Gap mapping |
| 7 | Industry Methodology Page | 135deg, #0f172a, #1e3a5f, #312e81 | 6 columns | Pyramid diagram + Indicator list + Veto + Peer benchmarking |
| 8 | Bond LGD Assessment | 135deg, #0f172a, #5b21b6 | 5 columns | LGD classification + Collateral valuation + Recovery path |
| 9 | External Support Special Assessment | 135deg, #0f172a, #0e7490 | 4 columns | Support capacity vs willingness + Upgrade rules + Trap signals |
| 10 | ESG + Governance Risk Scan | 135deg, #0f172a, #065f46 | 4 columns | E/S/G three dimensions + Fraud signals + Operational risk |
| 11 | Stress Test Report | 135deg, #0f172a, #991b1b | 4 columns | Severe scenario + Critical point + Second-order effects |
| 12 | Engine Validation Statistics | 135deg, #0f172a, #6366f1 | 6 columns | Confusion matrix + FNR/FPR + Migration matrix + Confidence |

---

## 6. Code Organization

> Since v0.0.1, templates are centrally stored as a single source of truth in the top-level `dev/templates/` directory; `design/` only retains this design specification.

```
dev/
├── design/
│   └── report-style-system.md   ← This file (design specification)
└── templates/                   ← Template single source of truth (since v0.0.1)
    ├── template-base.css        Base palette + font + layout (shared by 15 types)
    ├── template-type1.html      Single entity deep analysis
    ├── template-type2.html      Dual entity forward-looking comparison
    ├── template-type3.html      Black swan retrospective verification
    ├── template-type4.html      Multi-identity parallel assessment
    ├── template-type5.html      Bond investment dashboard
    ├── template-type6.html      Mosaic completeness report
    ├── template-type7.html      Industry methodology page
    ├── template-type8.html      Bond LGD assessment
    ├── template-type9.html      External support special assessment
    ├── template-type10.html     ESG + governance risk scan
    ├── template-type11.html     Stress test report
    ├── template-type12.html     Engine validation statistics
    ├── template-type13.html     Contagion analysis report
    ├── template-type14.html     Portfolio concentration report
    └── template-type15.html     Systemic risk alert
```

### File Usage

- `template-base.css` is referenced by each template (`<link rel="stylesheet">`, same directory relative path `template-base.css`)
- Each `.html` template only contains: type-specific Hero gradient + Strip column count adjustment + specific content structure
- Example reports are located in `validation/reports/<subdirectory>/`, referencing styles via `../../../dev/templates/template-base.css`
- Semantic color variables and font variables are inherited from `template-base.css`

---

## 7. Version History

| Version | Date | Changes |
|---|---|---|
| v1.0 | 2026-07-08 | Initial design: Color system, typography, layout skeleton, 6 components, 12 report types |
| v1.1 | 2026-07-15 | Code organization chapter synced with v0.0.1 structure: templates moved to `dev/templates/` (15 types), removed non-existent components/ directory |
