# Narrative checklist scorecard — suite dev, combo agentic-cheap

## Run metadata

- run: 20260902-0137 (UTC)
- commit: 8742618 (working tree dirty)
- gold sha256 (evals/gold/*.json, first 16): acfb8172d297fa3b
- judges: deepseek/deepseek-v4-pro-0813, qwen/qwen3.7-flash
- input: saved out/*/report.md + attribution.json (no pipeline calls)

## Coverage

- cases in the dev suite: 25
- cases judged: 25
- cases not judged: 0
- checklist items judged: 57
- items flagged: 19 — 17 judge split (a human must read the fact), 1 truncated quote window (a human must read the dropped quotes), 1 unreadable or unreachable judge (repeat the run)

## What a column means

A checklist item PASSES only when both judges rule it STATED by the report's own prose AND ENTAILED by the quotes the report cites. `stated, not entailed` is the ungrounded-narrative failure: the note asserts the reason but the cited source does not carry it. `not stated` means the note left the reason out. Flagged items count as neither a pass nor a fail.

| Case | Checklist pass | Rate | Stated, not entailed | Not stated | Flagged |
|---|---|---|---|---|---|
| CBA-nim-1H26 | 0/6 | 0% | 1 | 2 | 3 |
| CBA-cash_earnings-1H26 | 0/2 | 0% | 0 | 1 | 1 |
| CBA-roe-1H26 | 0/2 | 0% | 0 | 1 | 1 |
| CBA-cet1-1H26 | 0/2 | 0% | 0 | 0 | 2 |
| CBA-impairment-1H26 | 0/2 | 0% | 1 | 1 | 0 |
| CBA-cti-1H26 | 0/1 | 0% | 0 | 1 | 0 |
| CBA-nim-FY21 | 1/5 | 20% | 1 | 1 | 2 |
| CBA-cet1-FY21 | 0/2 | 0% | 1 | 0 | 1 |
| CBA-nim-FY25 | 3/3 | 100% | 0 | 0 | 0 |
| CBA-nim-FY26 | 3/4 | 75% | 0 | 0 | 1 |
| CBA-cash_earnings-FY26 | 0/3 | 0% | 0 | 1 | 2 |
| CBA-roe-FY26 | 0/2 | 0% | 1 | 0 | 1 |
| CBA-cet1-FY26 | 0/3 | 0% | 1 | 2 | 0 |
| CBA-impairment-FY26 | 0/3 | 0% | 0 | 2 | 1 |
| CBA-cti-FY26 | 0/3 | 0% | 1 | 0 | 2 |
| NAB-cash_earnings-FY25 | 1/2 | 50% | 0 | 1 | 0 |
| NAB-roe-FY25 | 0/1 | 0% | 0 | 1 | 0 |
| NAB-cti-FY25 | 0/1 | 0% | 1 | 0 | 0 |
| NAB-cet1-FY25 | 0/2 | 0% | 1 | 0 | 1 |
| NAB-impairment-FY25 | 0/1 | 0% | 0 | 1 | 0 |
| WBC-cash_earnings-FY25 | 0/2 | 0% | 2 | 0 | 0 |
| WBC-roe-FY25 | 0/1 | 0% | 0 | 1 | 0 |
| WBC-cti-FY25 | 0/1 | 0% | 0 | 0 | 1 |
| WBC-cet1-FY25 | 0/2 | 0% | 0 | 2 | 0 |
| WBC-impairment-FY25 | 1/1 | 100% | 0 | 0 | 0 |
| **TOTAL** | **9/57** | **16%** | **11** | **18** | **19** |

Descriptive for this run only: one run, one combo, no repeat sampling and no case-cluster bootstrap (finding 9). Do not quote the rate as a calibration claim.

## Judged items

### CBA-nim-1H26 (0/6)
- **flagged_for_human** — asset pricing: home lending -2, business lending -1, consumer finance +1 (PA p28 text)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **flagged_for_human** — funding costs -3: declining interest rates, unfavourable deposit mix, deposit price competition (PA p28 text)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **flagged_for_human** — portfolio mix +1 from at-call deposit growth (PA p28 text)
  - unreadable judge reply — deepseek/deepseek-v4-pro-0813 (stated): call failed: Expecting ':' delimiter at pos 27; near: ...{\n  "stated": "stated", " "stated": "stated|absent"...
- **fail** — capital/replicating +6: replicating portfolio +5, capital hedges +1 (PA p28 text)
  - stated=stated; entailed=not-entailed
- **fail** — excluding liquid asset growth (broadly revenue neutral), NIM decreased 1 basis point (PA p28 text)
  - stated=partial; entailed=not-entailed
- **fail** — NII cash basis $12,695m, +$761m or +6% on PCP (PA p28 table/text)
  - stated=absent; entailed=not-entailed

### CBA-cash_earnings-1H26 (0/2)
- **flagged_for_human** — total operating income 15,021 vs 14,097, +6.6% PCP (GPS p16)
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **fail** — statutory NPAT 5,367 vs statutory basis columns shown beside cash (GPS p16)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)

### CBA-roe-1H26 (0/2)
- **flagged_for_human** — statutory ROE 13.8 vs 13.8 flat / continuing statutory 13.8 vs 13.7 per table layout (PA p19)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **fail** — 2025 final DRP satisfied by $643m on-market purchase (PA p48)
  - stated=absent; entailed=not-entailed

### CBA-cet1-1H26 (0/2)
- **flagged_for_human** — HoH: capital generated from earnings and other regulatory adjustments, partly offset by the 2025 final dividend (PA p48)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **flagged_for_human** — the capital section footnotes that numbers may not sum precisely due to rounding (PA p48)
  - stated-check ran on a truncated answer window

### CBA-impairment-1H26 (0/2)
- **fail** — divisional deltas PCP: BB -129 to 91; IB&M -17 to an 8 benefit; NZ -12 to 4; RBS +153 to 232 (PA p34)
  - stated=stated; entailed=not-entailed
- **fail** — HoH: down $87m on the prior half, IB&M -$48m on lower individually assessed provisions (PA p34)
  - stated=partial; entailed=not-entailed

### CBA-cti-1H26 (0/1)
- **fail** — negative jaws PCP (expenses grew faster than income); HoH CTI improved 20bpts (KPI p18)
  - stated=absent; entailed=not-entailed (no quote was cited to entail it)

### CBA-nim-FY21 (1/5)
- **fail** — liquids bar has minimal impact on NII (slide 63 annotation)
  - stated=stated; entailed=not-entailed
- **pass** — deposit pricing & funding -3: cash rate cut -8, investment +1, replicating portfolio +2, wholesale +2 (slide 63 annotations)
  - the answer states the fact and the cited quotes entail it
- **flagged_for_human** — asset pricing -2: home loans net flat (pricing +9, switching -5, discounting -4), business lending -1, consumer finance -1 (slide 63)
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **flagged_for_human** — low-rate environment and TFF cited as the FY22 considerations (slide 63)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **fail** — the Profit Announcement of this era carries the drivers as prose, not a chart (printed pp12-13)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)

### CBA-cet1-FY21 (0/2)
- **fail** — internationally comparable CET1 19.4% vs 17.4% (KPI p23)
  - stated=stated; entailed=not-entailed
- **flagged_for_human** — FY21 announced a $6bn off-market buy-back after year end — context for the capital surplus (presentation)
  - judges disagree — stated: judges answered ['partial', 'stated']

### CBA-nim-FY25 (3/3)
- **pass** — excluding the 7bps from lower liquids/pooled facilities, underlying NIM up 2bps (PA p28 text)
  - the answer states the fact and the cited quotes entail it
- **pass** — funding costs -7bps driven by deposit price competition (PA p28 text)
  - the answer states the fact and the cited quotes entail it
- **pass** — replicating portfolio and capital hedge earnings within +9bps (PA p12-13 text; research 11)
  - the answer states the fact and the cited quotes entail it

### CBA-nim-FY26 (3/4)
- **pass** — home lending pricing competition (-4 bps within asset pricing; PA p28 text)
  - the answer states the fact and the cited quotes entail it
- **pass** — business and institutional lending pricing (-1 bp within asset pricing; PA p28 text)
  - the answer states the fact and the cited quotes entail it
- **flagged_for_human** — liquids growth has broadly neutral impact on net interest income (PA p28 text)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **pass** — portfolio mix from business lending growth and favourable deposit mix (PA p28 text)
  - the answer states the fact and the cited quotes entail it

### CBA-cash_earnings-FY26 (0/3)
- **flagged_for_human** — operating income growth +6.2% (slide 24)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **flagged_for_human** — operating performance $16,469m, +6.5% (slide 24)
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **fail** — statutory NPAT 10,866 vs cash 10,982; non-cash items are hedging/IFRS volatility and disposals (PA p16/p17)
  - stated=partial; entailed=not-entailed

### CBA-roe-FY26 (0/2)
- **fail** — statutory ROE 13.9 vs 13.4, +50bpts (PA p19)
  - stated=stated; entailed=not-entailed
- **flagged_for_human** — DRP satisfied by on-market purchase, no new shares (PA p48)
  - judges disagree — stated: judges answered ['partial', 'stated']; entailed: judges answered ['entailed', 'not-entailed']

### CBA-cet1-FY26 (0/3)
- **fail** — FY drivers: capital generated from earnings; 1H26 dividend; higher Credit Risk and IRRBB RWA, partly offset by lower Traded Market Risk RWA (PA p48)
  - stated=partial; entailed=not-entailed
- **fail** — 2026 interim dividend included $530m on-market purchase, CET1 impact -10bpts (PA p48 footnote)
  - stated=partial; entailed=not-entailed
- **fail** — Level 1 ratio 12.1% (slide 32)
  - stated=stated; entailed=not-entailed

### CBA-impairment-FY26 (0/3)
- **flagged_for_human** — divisional deltas vs FY25: RBS +106 to 378; NZ +11 to 66; BB -45 to 310; IB&M -16 to 33 (PA p34)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **fail** — half-year: 2H26 $469m, +$150m or +47% on prior half, Business Banking +$128m on collective provision charges (PA p34)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)
- **fail** — half-year loss rate annualised 9bps (PA p34)
  - stated=partial; entailed=not-entailed

### CBA-cti-FY26 (0/3)
- **flagged_for_human** — positive underlying jaws (income growth above expense growth)
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **fail** — wage inflation and vendor IT inflation cited (slide 27)
  - stated=stated; entailed=not-entailed
- **flagged_for_human** — investment spend: FY26 $2,472m vs FY25 $2,068m (slide 27)
  - judges disagree — stated: judges answered ['partial', 'stated']

### NAB-cash_earnings-FY25 (1/2)
- **pass** — statutory net profit decreased $201m or 2.9% while cash earnings fell only 0.2% — the bases diverge (p14)
  - the answer states the fact and the cited quotes entail it
- **fail** — impairment increase driven by individually assessed charges, primarily Corporate and Institutional Banking (p14)
  - stated=absent; entailed=not-entailed

### NAB-roe-FY25 (0/1)
- **fail** — statutory ROE 10.8% vs 11.4%, -60bps (p10)
  - stated=absent; entailed=not-entailed

### NAB-cti-FY25 (0/1)
- **fail** — a statutory-basis CTI row also exists (49.6% vs 48.5%) — basis must be named (p15)
  - stated=stated; entailed=not-entailed

### NAB-cet1-FY25 (0/2)
- **fail** — pro-forma CET1 11.81% reflecting the MLC Life 20% stake sale ($497m, completed 31 Oct 2025) — pro-forma is not the reported ratio (p6)
  - stated=stated; entailed=not-entailed
- **flagged_for_human** — Level 2 basis under APRA's revised framework (p6 footnote)
  - judges disagree — stated: judges answered ['absent', 'stated']

### NAB-impairment-FY25 (0/1)
- **fail** — NAB's label is credit impairment charge (CIC); halves shown 181/171/333 on p5
  - stated=partial; entailed=not-entailed

### WBC-cash_earnings-FY25 (0/2)
- **fail** — statutory net profit 6,916 vs 6,990 (-1%); Notable Items are hedging only: -56 vs -123 post-tax (p9)
  - stated=stated; entailed=not-entailed
- **fail** — the basis divergence must be stated: ex-Notables fell 2% while statutory fell 1%
  - stated=stated; entailed=not-entailed

### WBC-roe-FY25 (0/1)
- **fail** — variants on the same page: statutory ROE 9.66 vs 9.77 (-11bps); statutory ROTE 10.89 vs 11.01 (-12bps); ex-Notables ROE 9.74 vs 9.94 (-20bps) — the variant used must be named (p10)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)

### WBC-cti-FY25 (0/1)
- **flagged_for_human** — the ratio itself is on the ex-Notables basis; restructuring is inside it as an operating cost (p9/p10)
  - judges disagree — stated: judges answered ['partial', 'stated']

### WBC-cet1-FY25 (0/2)
- **fail** — 12.53% is $3.1bn above the 11.25% target (p6)
  - stated=absent; entailed=not-entailed
- **fail** — internationally comparable variant 18.28% on the same page — variant discipline (p10)
  - stated=absent; entailed=not-entailed

### WBC-impairment-FY25 (1/1)
- **pass** — Westpac's label is 'impairment charges'; mortgage 90+ delinquencies improved 1.05% -> 0.70% (p10)
  - the answer states the fact and the cited quotes entail it

Judge spend: $0.156 over 234 calls.
