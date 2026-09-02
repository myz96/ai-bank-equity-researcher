# Narrative checklist scorecard — suite holdout, combo agentic

## Run metadata

- run: 20260902-0132 (UTC)
- commit: c2b0dcf (working tree dirty)
- gold sha256 (evals/gold/*.json, first 16): acfb8172d297fa3b
- judges: deepseek/deepseek-v4-pro-0813, qwen/qwen3.7-flash
- input: saved out/*/report.md + attribution.json (no pipeline calls)

## Coverage

- cases in the holdout suite: 8
- cases judged: 8
- cases not judged: 0
- checklist items judged: 27
- items flagged: 6 — 6 judge split (a human must read the fact), 0 unreadable or unreachable judge (repeat the run)

## What a column means

A checklist item PASSES only when both judges rule it STATED by the report's own prose AND ENTAILED by the quotes the report cites. `stated, not entailed` is the ungrounded-narrative failure: the note asserts the reason but the cited source does not carry it. `not stated` means the note left the reason out. Flagged items count as neither a pass nor a fail.

| Case | Checklist pass | Rate | Stated, not entailed | Not stated | Flagged |
|---|---|---|---|---|---|
| CBA-cash_earnings-FY21 | 0/2 | 0% | 0 | 1 | 1 |
| CBA-roe-FY21 | 1/1 | 100% | 0 | 0 | 0 |
| CBA-impairment-FY21 | 0/2 | 0% | 0 | 1 | 1 |
| CBA-cti-FY21 | 0/1 | 0% | 0 | 1 | 0 |
| NAB-nim-1H26 | 1/5 | 20% | 0 | 2 | 2 |
| NAB-nim-FY25 | 1/5 | 20% | 1 | 2 | 1 |
| WBC-nim-1H26 | 3/5 | 60% | 0 | 1 | 1 |
| WBC-nim-FY25 | 4/6 | 67% | 1 | 1 | 0 |
| **TOTAL** | **10/27** | **37%** | **2** | **9** | **6** |

Descriptive for this run only: one run, one combo, no repeat sampling and no case-cluster bootstrap (finding 9). Do not quote the rate as a calibration claim.

## Judged items

### CBA-cash_earnings-FY21 (0/2)
- **fail** — the earnings recovery is dominated by the impairment unwind, not income growth (GPS p31)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)
- **flagged_for_human** — statutory NPAT 8,843 vs 7,388 (+20%) beside cash (KPI p22)
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']

### CBA-roe-FY21 (1/1)
- **pass** — statutory ROE 11.8 vs 10.4, +140bpts (KPI p23)
  - the answer states the fact and the cited quotes entail it

### CBA-impairment-FY21 (0/2)
- **flagged_for_human** — the loss-rate fall from 33bps to 7bps is the era's defining credit story
  - judges disagree — stated: judges answered ['partial', 'stated']
- **fail** — FY20 comparator included the COVID central overlay build
  - stated=partial; entailed=not-entailed

### CBA-cti-FY21 (0/1)
- **fail** — the FY21 text layer prints decimals with an internal space ('47. 0') — an era-specific parsing trap recorded for extraction robustness
  - stated=absent; entailed=not-entailed (no quote was cited to entail it)

### NAB-nim-1H26 (1/5)
- **pass** — excluding M&T +4 and HQLA mix +3, underlying margin up 4bps (book p26)
  - the answer states the fact and the cited quotes entail it
- **flagged_for_human** — deposit and capital replicating portfolios +6bps (book p26)
  - judges disagree — stated: judges answered ['partial', 'stated']; entailed: judges answered ['entailed', 'not-entailed']
- **flagged_for_human** — lending margin -4bps: competition in business and housing lending plus rate-timing differences in Australian home lending (book p26)
  - judges disagree — stated: judges answered ['partial', 'stated']
- **fail** — NII $9,163m, +8.5% PCP; +7.2% underlying excluding economic hedges and NZ FX translation (book p26)
  - stated=partial; entailed=not-entailed
- **fail** — HoH walk (Sep 25 1.78 -> Mar 26 1.81): lending -4, funding 0, deposits +1, replicating +3, liquids +1, M&T +2 (book p26 chart)
  - stated=partial; entailed=not-entailed

### NAB-nim-FY25 (1/5)
- **pass** — deposit costs include competitive pressures and deposit mix impacts (book p17)
  - the answer states the fact and the cited quotes entail it
- **fail** — liquids benefit is a lower mix of lower-yielding HQLA (book p17)
  - stated=stated; entailed=not-entailed
- **flagged_for_human** — lending margin: competitive pressures in housing and business lending, partly offset by NZ housing margin and favourable business-lending mix (book p17)
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **fail** — NII $17,398m vs $16,754m, +3.8%; underlying +$718m or +4.3% excluding a $74m economic-hedge movement (book p17)
  - stated=partial; entailed=not-entailed
- **fail** — HoH walk (Mar 25 1.70 -> Sep 25 1.78): lending 0, funding +1, deposits -1, replicating+other +4, liquids +2, M&T +2 (book p17 chart)
  - stated=partial; entailed=not-entailed

### WBC-nim-1H26 (3/5)
- **flagged_for_human** — the walk is on the excluding-Notable-Items basis
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **pass** — Core NIM 1.78%, down 2bps; Treasury & Markets contribution 11bps, down 1bp on lower Treasury income (RA p13)
  - the answer states the fact and the cited quotes entail it
- **pass** — capital & other -3bps: a remediation provision in the current period and non-repeat of prior-period items (RA p13)
  - the answer states the fact and the cited quotes entail it
- **pass** — liquids +5bps: trading assets reduced, liquid assets grew slower than lending, spreads narrowed (RA p13)
  - the answer states the fact and the cited quotes entail it
- **fail** — HoH walk (2H25 1.95% -> 1H26 1.89%, -6bps): loans -3, deposits 0, timing -2, liquids +2, WSF 0, capital -1, T&M -2 (RA p13)
  - stated=partial; entailed=not-entailed

### WBC-nim-FY25 (4/6)
- **fail** — the walk is on the excluding-Notable-Items basis; Westpac has no cash earnings measure (retired at 1H23)
  - stated=stated; entailed=not-entailed
- **pass** — Core NIM 1.81%, contracted 1bp; Treasury & Markets contribution 13bps, stable (RA p12)
  - the answer states the fact and the cited quotes entail it
- **pass** — loan spread: NZ mortgage repricing benefit more than offset by Australian competition and the auto finance portfolio sale (RA p12)
  - the answer states the fact and the cited quotes entail it
- **pass** — deposit spread -2bps: mix shift to lower-spread savings, term deposit compression, lower rates; hedged deposit earnings higher (RA p12)
  - the answer states the fact and the cited quotes entail it
- **pass** — wholesale funding -1bp: final TFF drawdowns matured in the prior year (RA p12)
  - the answer states the fact and the cited quotes entail it
- **fail** — HoH walk (1H25 1.92% -> 2H25 1.95%): loans 0, deposits 0, liquids +3, WSF 0, capital & other -1, T&M +1 (RA p12)
  - stated=partial; entailed=not-entailed (judges split ['absent', 'partial'], both short of stated)

Judge spend: $0.0869 over 106 calls.
