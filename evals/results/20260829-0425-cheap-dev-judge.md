# Narrative checklist scorecard — suite dev, combo cheap

## Run metadata

- run: 20260829-0425 (UTC)
- commit: a89086c (working tree dirty)
- gold sha256 (evals/gold/*.json, first 16): b3ff01de30da5ee4
- judges: deepseek/deepseek-v4-pro-0813, qwen/qwen3.7-flash
- input: saved out/*/report.md + attribution.json (no pipeline calls)

## Coverage

- cases in the dev suite: 25
- cases judged: 15
- cases not judged: 10 (no saved artifact at out/nab-cash_earnings-fy25-vs-fy24-cheap; no saved artifact at out/nab-cet1-fy25-vs-fy24-cheap; no saved artifact at out/nab-cti-fy25-vs-fy24-cheap; no saved artifact at out/nab-impairment-fy25-vs-fy24-cheap; no saved artifact at out/nab-roe-fy25-vs-fy24-cheap; no saved artifact at out/wbc-cash_earnings-fy25-vs-fy24-cheap; no saved artifact at out/wbc-cet1-fy25-vs-fy24-cheap; no saved artifact at out/wbc-cti-fy25-vs-fy24-cheap; no saved artifact at out/wbc-impairment-fy25-vs-fy24-cheap; no saved artifact at out/wbc-roe-fy25-vs-fy24-cheap)
- checklist items judged: 43
- items flagged for a human (judge split or unreadable reply): 9

## What a column means

A checklist item PASSES only when both judges rule it STATED by the report's own prose AND ENTAILED by the quotes the report cites. `stated, not entailed` is the ungrounded-narrative failure: the note asserts the reason but the cited source does not carry it. `not stated` means the note left the reason out. Flagged items count as neither a pass nor a fail.

| Case | Checklist pass | Rate | Stated, not entailed | Not stated | Flagged |
|---|---|---|---|---|---|
| CBA-nim-1H26 | 0/6 | 0% | 1 | 4 | 1 |
| CBA-cash_earnings-1H26 | 0/2 | 0% | 0 | 1 | 1 |
| CBA-roe-1H26 | 0/2 | 0% | 0 | 2 | 0 |
| CBA-cet1-1H26 | 0/2 | 0% | 0 | 2 | 0 |
| CBA-impairment-1H26 | 0/2 | 0% | 0 | 1 | 1 |
| CBA-cti-1H26 | 0/1 | 0% | 0 | 0 | 1 |
| CBA-nim-FY21 | 0/5 | 0% | 0 | 5 | 0 |
| CBA-cet1-FY21 | 0/2 | 0% | 0 | 2 | 0 |
| CBA-nim-FY25 | 0/3 | 0% | 1 | 1 | 1 |
| CBA-nim-FY26 | 0/4 | 0% | 0 | 3 | 1 |
| CBA-cash_earnings-FY26 | 0/3 | 0% | 0 | 3 | 0 |
| CBA-roe-FY26 | 0/2 | 0% | 0 | 1 | 1 |
| CBA-cet1-FY26 | 0/3 | 0% | 0 | 1 | 2 |
| CBA-impairment-FY26 | 0/3 | 0% | 0 | 3 | 0 |
| CBA-cti-FY26 | 0/3 | 0% | 1 | 2 | 0 |
| NAB-cash_earnings-FY25 | not judged: no saved artifact at out/nab-cash_earnings-fy25-vs-fy24-cheap | — | — | — | — |
| NAB-roe-FY25 | not judged: no saved artifact at out/nab-roe-fy25-vs-fy24-cheap | — | — | — | — |
| NAB-cti-FY25 | not judged: no saved artifact at out/nab-cti-fy25-vs-fy24-cheap | — | — | — | — |
| NAB-cet1-FY25 | not judged: no saved artifact at out/nab-cet1-fy25-vs-fy24-cheap | — | — | — | — |
| NAB-impairment-FY25 | not judged: no saved artifact at out/nab-impairment-fy25-vs-fy24-cheap | — | — | — | — |
| WBC-cash_earnings-FY25 | not judged: no saved artifact at out/wbc-cash_earnings-fy25-vs-fy24-cheap | — | — | — | — |
| WBC-roe-FY25 | not judged: no saved artifact at out/wbc-roe-fy25-vs-fy24-cheap | — | — | — | — |
| WBC-cti-FY25 | not judged: no saved artifact at out/wbc-cti-fy25-vs-fy24-cheap | — | — | — | — |
| WBC-cet1-FY25 | not judged: no saved artifact at out/wbc-cet1-fy25-vs-fy24-cheap | — | — | — | — |
| WBC-impairment-FY25 | not judged: no saved artifact at out/wbc-impairment-fy25-vs-fy24-cheap | — | — | — | — |
| **TOTAL** | **0/43** | **0%** | **3** | **31** | **9** |

Descriptive for this run only: one run, one combo, no repeat sampling and no case-cluster bootstrap (finding 9). Do not quote the rate as a calibration claim.

## Judged items

### CBA-nim-1H26 (0/6)
- **fail** — asset pricing: home lending -2, business lending -1, consumer finance +1 (PA p28 text)
  - stated=partial; entailed=not-entailed
- **flagged_for_human** — funding costs -3: declining interest rates, unfavourable deposit mix, deposit price competition (PA p28 text)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **fail** — portfolio mix +1 from at-call deposit growth (PA p28 text)
  - stated=stated; entailed=not-entailed
- **fail** — capital/replicating +6: replicating portfolio +5, capital hedges +1 (PA p28 text)
  - stated=partial; entailed=not-entailed
- **fail** — excluding liquid asset growth (broadly revenue neutral), NIM decreased 1 basis point (PA p28 text)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)
- **fail** — NII cash basis $12,695m, +$761m or +6% on PCP (PA p28 table/text)
  - stated=absent; entailed=not-entailed

### CBA-cash_earnings-1H26 (0/2)
- **flagged_for_human** — total operating income 15,021 vs 14,097, +6.6% PCP (GPS p16)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **fail** — statutory NPAT 5,367 vs statutory basis columns shown beside cash (GPS p16)
  - stated=absent; entailed=not-entailed

### CBA-roe-1H26 (0/2)
- **fail** — statutory ROE 13.8 vs 13.8 flat / continuing statutory 13.8 vs 13.7 per table layout (PA p19)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)
- **fail** — 2025 final DRP satisfied by $643m on-market purchase (PA p48)
  - stated=absent; entailed=not-entailed

### CBA-cet1-1H26 (0/2)
- **fail** — HoH: capital generated from earnings and other regulatory adjustments, partly offset by the 2025 final dividend (PA p48)
  - stated=partial; entailed=not-entailed
- **fail** — the capital section footnotes that numbers may not sum precisely due to rounding (PA p48)
  - stated=absent; entailed=not-entailed

### CBA-impairment-1H26 (0/2)
- **flagged_for_human** — divisional deltas PCP: BB -129 to 91; IB&M -17 to an 8 benefit; NZ -12 to 4; RBS +153 to 232 (PA p34)
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **fail** — HoH: down $87m on the prior half, IB&M -$48m on lower individually assessed provisions (PA p34)
  - stated=absent; entailed=not-entailed

### CBA-cti-1H26 (0/1)
- **flagged_for_human** — negative jaws PCP (expenses grew faster than income); HoH CTI improved 20bpts (KPI p18)
  - judges disagree — stated: judges answered ['partial', 'stated']

### CBA-nim-FY21 (0/5)
- **fail** — liquids bar has minimal impact on NII (slide 63 annotation)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)
- **fail** — deposit pricing & funding -3: cash rate cut -8, investment +1, replicating portfolio +2, wholesale +2 (slide 63 annotations)
  - stated=partial; entailed=not-entailed
- **fail** — asset pricing -2: home loans net flat (pricing +9, switching -5, discounting -4), business lending -1, consumer finance -1 (slide 63)
  - stated=partial; entailed=not-entailed
- **fail** — low-rate environment and TFF cited as the FY22 considerations (slide 63)
  - stated=partial; entailed=not-entailed
- **fail** — the Profit Announcement of this era carries the drivers as prose, not a chart (printed pp12-13)
  - stated=absent; entailed=not-entailed

### CBA-cet1-FY21 (0/2)
- **fail** — internationally comparable CET1 19.4% vs 17.4% (KPI p23)
  - stated=absent; entailed=not-entailed
- **fail** — FY21 announced a $6bn off-market buy-back after year end — context for the capital surplus (presentation)
  - stated=partial; entailed=not-entailed

### CBA-nim-FY25 (0/3)
- **fail** — excluding the 7bps from lower liquids/pooled facilities, underlying NIM up 2bps (PA p28 text)
  - stated=partial; entailed=entailed
- **flagged_for_human** — funding costs -7bps driven by deposit price competition (PA p28 text)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **fail** — replicating portfolio and capital hedge earnings within +9bps (PA p12-13 text; research 11)
  - stated=stated; entailed=not-entailed

### CBA-nim-FY26 (0/4)
- **fail** — home lending pricing competition (-4 bps within asset pricing; PA p28 text)
  - stated=partial; entailed=entailed
- **fail** — business and institutional lending pricing (-1 bp within asset pricing; PA p28 text)
  - stated=partial; entailed=entailed
- **fail** — liquids growth has broadly neutral impact on net interest income (PA p28 text)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)
- **flagged_for_human** — portfolio mix from business lending growth and favourable deposit mix (PA p28 text)
  - judges disagree — stated: judges answered ['partial', 'stated']

### CBA-cash_earnings-FY26 (0/3)
- **fail** — operating income growth +6.2% (slide 24)
  - stated=absent; entailed=entailed
- **fail** — operating performance $16,469m, +6.5% (slide 24)
  - stated=absent; entailed=not-entailed
- **fail** — statutory NPAT 10,866 vs cash 10,982; non-cash items are hedging/IFRS volatility and disposals (PA p16/p17)
  - stated=absent; entailed=not-entailed

### CBA-roe-FY26 (0/2)
- **fail** — statutory ROE 13.9 vs 13.4, +50bpts (PA p19)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)
- **flagged_for_human** — DRP satisfied by on-market purchase, no new shares (PA p48)
  - unreadable judge reply — deepseek/deepseek-v4-pro-0813 (stated): call failed: chat() failed for deepseek/deepseek-v4-pro-0813 after 5 attempts: [Errno 8] nodename nor servname provided, or not known; deepseek/deepseek-v4-pro-0813 (entailed): call failed: chat() failed for deepseek/deepseek-v4-pro-0813 after 5 attempts: [Errno 8] nodename nor servname provided, or not known; qwen/qwen3.7-flash (stated): call failed: chat() failed for qwen/qwen3.7-flash after 5 attempts: [Errno 8] nodename nor servname provided, or not known; qwen/qwen3.7-flash (entailed): call failed: chat() failed for qwen/qwen3.7-flash after 5 attempts: [Errno 8] nodename nor servname provided, or not known

### CBA-cet1-FY26 (0/3)
- **flagged_for_human** — FY drivers: capital generated from earnings; 1H26 dividend; higher Credit Risk and IRRBB RWA, partly offset by lower Traded Market Risk RWA (PA p48)
  - unreadable judge reply — deepseek/deepseek-v4-pro-0813 (stated): call failed: chat() failed for deepseek/deepseek-v4-pro-0813 after 5 attempts: [Errno 8] nodename nor servname provided, or not known; deepseek/deepseek-v4-pro-0813 (entailed): call failed: chat() failed for deepseek/deepseek-v4-pro-0813 after 5 attempts: [Errno 8] nodename nor servname provided, or not known; qwen/qwen3.7-flash (stated): call failed: chat() failed for qwen/qwen3.7-flash after 5 attempts: [Errno 8] nodename nor servname provided, or not known; qwen/qwen3.7-flash (entailed): call failed: chat() failed for qwen/qwen3.7-flash after 5 attempts: [Errno 8] nodename nor servname provided, or not known
- **flagged_for_human** — 2026 interim dividend included $530m on-market purchase, CET1 impact -10bpts (PA p48 footnote)
  - unreadable judge reply — deepseek/deepseek-v4-pro-0813 (stated): call failed: chat() failed for deepseek/deepseek-v4-pro-0813 after 5 attempts: [Errno 8] nodename nor servname provided, or not known; deepseek/deepseek-v4-pro-0813 (entailed): call failed: chat() failed for deepseek/deepseek-v4-pro-0813 after 5 attempts: [Errno 8] nodename nor servname provided, or not known
- **fail** — Level 1 ratio 12.1% (slide 32)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)

### CBA-impairment-FY26 (0/3)
- **fail** — divisional deltas vs FY25: RBS +106 to 378; NZ +11 to 66; BB -45 to 310; IB&M -16 to 33 (PA p34)
  - stated=absent; entailed=not-entailed
- **fail** — half-year: 2H26 $469m, +$150m or +47% on prior half, Business Banking +$128m on collective provision charges (PA p34)
  - stated=partial; entailed=not-entailed
- **fail** — half-year loss rate annualised 9bps (PA p34)
  - stated=partial; entailed=not-entailed

### CBA-cti-FY26 (0/3)
- **fail** — positive underlying jaws (income growth above expense growth)
  - stated=stated; entailed=not-entailed
- **fail** — wage inflation and vendor IT inflation cited (slide 27)
  - stated=absent; entailed=not-entailed
- **fail** — investment spend: FY26 $2,472m vs FY25 $2,068m (slide 27)
  - stated=absent; entailed=not-entailed

Judge spend: $0.077 over 163 calls.
