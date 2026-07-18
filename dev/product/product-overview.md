# Product Vision and Design

**Version**: v0.3.0
**Status**: Design Phase

---

## 1. Product Vision

### In One Sentence

> Enter a company name. The engine unfolds a multi-dimensional cognitive mosaic that no single analyst could manually construct in an hour — not answering your questions, but showing you the questions you didn't know to ask.

### Core Experience: Magic Experience

Users don't need to know what AI can do. They just need to do one minimal thing.

**Four Magic Moments**:

| Moment | What the User Did | What the Engine Returned | User Feeling |
|---|---|---|---|
| **Minimal Input -> Rich Output** | Enter a company name | Not a standard report, but a multi-dimensional mosaic: the rules of the industry game, where the company stands, how the market prices it, what covenant traps bondholders face, what events will impact it in the next three months | "I asked one question, it told me ten I should have asked" |
| **Seeing What You Can't See** | Did nothing — the engine knows their jurisdiction/industry/portfolio | Three solar companies in the jurisdiction. A's gross margin is squeezed by upstream and downstream. B has the thickest inverter margins but has been eliminated from central enterprise procurement. C's actual controller's related company was listed as dishonest person subject to enforcement three months ago | "It knows my jurisdiction. It knows I'm looking for clients. It knows which ones are traps" |
| **Cross-Dimensional Connection** | Query a convertible bond | Conversion premium 74%. Same industry Jingneng only 3.3%. Issuer refused downward revision last time. Meanwhile, the issuer was eliminated from central enterprise procurement three months ago, while a competitor just secured a 10GW order. Plus, this bond has no cross-default clause | "I knew each piece individually, but only together do I see the risk" |
| **Being Reminded of Unknown Unknowns** | Finished reading the report | Data completeness: Medium confidence. The following three key data items are currently not publicly available. If any one can be obtained through internal bank channels, the assessment can be re-evaluated to narrow the range | "When it says it doesn't know, it's more trustworthy than when it says it knows" |

### The Source of Magic is Not Technical Flashiness

It is four cognitive architectures:

| Cognitive Architecture | Meaning |
|---|---|
| **Multi-Dimensional Auto-Expansion** | The engine knows which dimensions to scan for any enterprise, no user specification needed |
| **Spatial Awareness** | The engine knows the user's jurisdiction/industry/portfolio, automatically locating relevant signals |
| **Signal Aggregation (Mosaic)** | Piecing together fragments scattered across different data sources into a complete picture |
| **Completeness Honesty** | Clearly marking "don't know", inversely enhancing the credibility of "know" |

---

## 2. User Personas

### Primary Users

| Persona | Role | Typical Scenario | Core Anxiety |
|---|---|---|---|
| **City Commercial Bank Relationship Manager** | Frontline credit officer | Head office wants to invest in new energy/semiconductor, team has no domain knowledge. Facing clients in unfamiliar industries, doesn't even know what questions to ask | "I dare not touch industries I don't understand" |
| **Small/Medium Broker Credit Analyst** | Credit analysis | Team of 3-5 people covering the entire credit bond market. Every industry is as complex as solar, impossible to keep up | "I can't keep up, but my signature means lifetime accountability" |
| **Fixed Income Fund Manager** | Investment decision-maker | Holding hundreds of bonds, each with industry logic, covenant traps, liquidity risk. No time to deep-dive each one | "I need someone to check the bonds I've default-assumed are 'fine'" |
| **Private Credit Analyst** | Deep research | Needs independent judgment not reliant on ratings. Ratings lagging 17 months is an open secret in the industry | "I can't trust rating reports, but I have no alternative tool" |

### Decision Makers (Payers)

| Persona | Purchase Motivation | Budget Source |
|---|---|---|
| City Commercial Bank HQ Corporate Banking Head | "Empower my team to venture into new industries" | Tech investment/business innovation budget |
| Broker Fixed Income Department Credit Research Head | "Use AI to supplement headcount shortage" | Department annual budget |
| Fund Company Fixed Income Director | "I need an independent referee that doesn't take money from rating agencies" | Investment research tool budget |

---

## 3. Product Form

### Three-Layer Delivery Architecture

```
Layer 1: ChatBot (Entry Layer · Free Customer Acquisition)
  Users: Relationship managers/credit analysts
  Scenario: "Analyze company XX"
  Output: Condensed industry cognition + core risk signals (readable within 2 minutes)
  
Layer 2: Deep Dashboard (Paid Layer · Per-report/Annual Fee)
  Users: Fund managers/risk control directors/deep researchers
  Scenario: Regular portfolio scan + industry deep dive + multi-identity perspective
  Output: Complete multi-dimensional analysis + completeness report + cross-dimensional connection
  
Layer 3: API Embedding (Scale Layer · Annual License)
  Users: Institutions already using Wind/O32 and other terminals
  Scenario: Embed independent credit analysis signals into existing workflows
  Output: Structured signals + scores + gap annotations
```

### Design Principles

1. **Don't ask the user any questions** — the engine judges the industry, loads the pyramid, pulls data in parallel by itself
2. **Don't give the user a "report"** — give them a "discovery"
3. **Don't pretend to be omniscient** — clearly mark data gaps and uncertainty ranges
4. **Don't passively wait for queries** — actively monitor portfolios/watchlists, push on changes
5. **Don't make users learn new tools** — conversational interaction, natural language input and output

---

## 4. Product Development Roadmap

### Alpha: First Impression
**Core Experience**: Enter company name -> Receive multi-dimensional mosaic
**Key Capabilities**: Automatic industry identification + pyramid loading + multi-source parallel data pull + NLP signal extraction + LLM report generation
**Status**: Methodology verified, product form designed

### Beta: Active Monitoring
**Core Experience**: Automatic portfolio/watchlist monitoring -> Active push of signal changes
**Key Capabilities**: Scheduled scanning + signal change detection + event calendar + push engine
**Status**: Not started

### Gamma: Role Switching
**Core Experience**: One-click switch of analysis perspective by identity (credit officer <-> fund manager <-> trader <-> risk control director)
**Key Capabilities**: Multi-identity analysis template + terminology adaptation + focus indicator switching
**Status**: Methodology documents complete, productization not started

### Delta: Memory Growth
**Core Experience**: Remembering user's industry preferences, decision history, focus dimensions
**Key Capabilities**: User profile + preference learning + personalized weights
**Status**: Not started
