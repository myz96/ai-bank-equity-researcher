# Rescore — suite dev, combo cheap, saved artifacts, 20260828-0923

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | OK | 3/7 | 3/7 | 7/7 | 7/7 | 0 | 0 | 95 | $0.0022 |
| CBA-cash_earnings-1H26 | ERROR: no artifact at out/cba-cash_earnings-1h26-vs-1h25-cheap | | | | | | | | |
| CBA-roe-1H26 | WRONG (numbers) | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 95 | $0.0012 |
| CBA-cet1-1H26 | ERROR: artifact postdates 2026-08-27T08:05 (generated 2026-08-28T09 | | | | | | | | |
| CBA-impairment-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/4 | 4 | 1 | 40 | $0.0021 |
| CBA-cti-1H26 | WRONG (numbers) | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 85 | $0.0012 |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 90 | $0.0019 |
| CBA-cash_earnings-FY21 | OK | 1/2 | 1/1 | — | 1/4 | 3 | 1 | 40 | $0.0018 |
| CBA-roe-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 90 | $0.0014 |
| CBA-cet1-FY21 | WRONG (numbers) | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/4 | 4 | 0 | 100 | $0.0016 |
| CBA-impairment-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 40 | $0.0029 |
| CBA-cti-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 90 | $0.0013 |
| CBA-nim-FY25 | WRONG (basis) | 2/7 | 2/7 | 0/7 | 7/7 | 0 | 1 | 75 | $0.0013 |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 1 | 40 | $0.0021 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — | 4/4 | 0 | 1 | 40 | $0.0031 |
| CBA-roe-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 95 | $0.0012 |
| CBA-cet1-FY26 | OK | n/a (gold decomposes a different comparison) | n/a (gold decomposes a different comparison) | n/a (gold walk is not the case comparison) | 0/4 | 4 | 0 | 95 | $0.0015 |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/5 | 5 | 0 | 95 | $0.0016 |
| CBA-cti-FY26 | ERROR: artifact predates 2026-08-27T07:30 (generated 2026-08-26T06: | | | | | | | | |

## Calibration (scored quantified driver claims only)

- scored_claims: 33
- unscored_claims: 30
- cases_scored: 6
- cases: 19
- brier: 0.211
- confidently_wrong_rate: 0.226
- 50-69: 1 claims, 0% correct
- 70-84: 1 claims, 0% correct
- 85-94: 18 claims, 83% correct
- 95-100: 13 claims, 69% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.

## Old vs new scorer (baseline 20260827-0801-cheap-dev.jsonl)

| Case | Movement | Driver recall | Precision | Extraction |
|---|---|---|---|---|
| CBA-nim-1H26 | OK | 4/7 -> **3/7** | 4/7 -> **3/7** | 7/7 |
| CBA-cash_earnings-1H26 | ERROR | ERROR | ERROR | ERROR |
| CBA-roe-1H26 | WRONG -> **WRONG (numbers)** | n/a (checklist or comparison-mismatch gold) -> **n/a (no verified numeric gold)** | n/a -> **n/a (no verified numeric gold)** | — |
| CBA-cet1-1H26 | WRONG -> **ERROR** | 0/1 -> **ERROR** | 0/0 -> **ERROR** | — -> **ERROR** |
| CBA-impairment-1H26 | OK | n/a (checklist or comparison-mismatch gold) -> **n/a (no verified numeric gold)** | n/a -> **n/a (no verified numeric gold)** | — |
| CBA-cti-1H26 | WRONG -> **WRONG (numbers)** | n/a (checklist or comparison-mismatch gold) -> **n/a (no verified numeric gold)** | n/a -> **n/a (no verified numeric gold)** | — |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 |
| CBA-cash_earnings-FY21 | OK | 1/2 | 1/4 -> **1/1** | — |
| CBA-roe-FY21 | OK | n/a (checklist or comparison-mismatch gold) -> **n/a (no verified numeric gold)** | n/a -> **n/a (no verified numeric gold)** | — |
| CBA-cet1-FY21 | WRONG -> **WRONG (numbers)** | n/a (checklist or comparison-mismatch gold) -> **n/a (no verified numeric gold)** | n/a -> **n/a (no verified numeric gold)** | — |
| CBA-impairment-FY21 | OK | n/a (checklist or comparison-mismatch gold) -> **n/a (no verified numeric gold)** | n/a -> **n/a (no verified numeric gold)** | — |
| CBA-cti-FY21 | OK | n/a (checklist or comparison-mismatch gold) -> **n/a (no verified numeric gold)** | n/a -> **n/a (no verified numeric gold)** | — |
| CBA-nim-FY25 | OK -> **WRONG (basis)** | 2/7 | 2/7 | 4/7 -> **0/7** |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 7/7 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — |
| CBA-roe-FY26 | OK | n/a (checklist or comparison-mismatch gold) -> **n/a (no verified numeric gold)** | n/a -> **n/a (no verified numeric gold)** | — |
| CBA-cet1-FY26 | OK | n/a (checklist or comparison-mismatch gold) -> **n/a (gold decomposes a different comparison)** | n/a -> **n/a (gold decomposes a different comparison)** | 4/4 -> **n/a (gold walk is not the case comparison)** |
| CBA-impairment-FY26 | OK | n/a (checklist or comparison-mismatch gold) -> **n/a (no verified numeric gold)** | n/a -> **n/a (no verified numeric gold)** | — |
| CBA-cti-FY26 | ERROR | ERROR | ERROR | ERROR |

<!-- The sections below are written by hand. A new rescore run overwrites this
     file, so copy them forward if you re-run the command. -->

## How this table was made (ticket 28)

Command, no model calls and no OpenRouter spend:

```
uv run bank-equity-researcher evals rescore --suite dev --combo cheap --bank CBA \
  --since 2026-08-27T07:30 --until 2026-08-27T08:05 \
  --baseline evals/results/20260827-0801-cheap-dev.jsonl \
  --label rescore-20260827-0801-newscorer
```

The same saved `out/<slug>/attribution.json` artifacts go through the old and
the new scorer, so every delta is a scorer change and never an agent change.
The `--since` and `--until` window keeps the comparison like for like.

Three of the 19 baseline rows carry no comparable artifact:

- `CBA-cash_earnings-1H26` and `CBA-cti-FY26` crashed in the 0801 run (malformed
  author JSON), so the run wrote no artifact for them.
- `CBA-cet1-1H26` had its artifact overwritten by a later run on 2026-08-28
  (a concurrent ticket). The 0801 artifact is gone, so the row is excluded
  rather than compared against a different answer.

## Why each delta moved

Scores DROP where the old scorer was generous. That is the result the round
wanted, never a regression to tune away.

- **CBA-nim-1H26 recall 4/7 -> 3/7, precision 4/7 -> 3/7 (finding 4).** The old
  scorer let each claim pick its own framing: `markets_treasury -2` matched the
  slide-60 alternate framing while the other six claims were scored against the
  Profit Announcement framing. No document publishes that mixture. The new
  scorer scores one framing as a whole; the primary and the alternate framing
  both match three slots, so the tie goes to the primary. The answer itself is
  the half-on-half walk, not the PCP walk.
- **CBA-nim-FY25 movement OK -> WRONG (basis) (finding 6).** The answer states
  basis `statutory` for a `cash` basis case. The old scorer compared three
  numbers only and never read the unit, the basis or the comparator.
- **CBA-nim-FY25 extraction 4/7 -> 0/7 (finding 5).** The single extracted walk
  runs 208 -> 208 (Dec 24 -> Jun 25, half on half), not the case's 199 -> 208
  full-year walk. The old metric pooled every number from every walk record and
  ignored labels, so one extracted `0` satisfied two gold zero bars and two more
  gold values matched by coincidence.
- **CBA-cet1-FY26 extraction 4/4 -> n/a (finding 5).** The gold walk is the
  Dec 25 -> Jun 26 half-on-half walk, which the gold itself marks as "not
  FY-on-FY". There is no verified FY-on-FY gold walk, so extraction is unscored
  for this case. Driver scoring already said this; the two layers now agree.
- **CBA-cash_earnings-FY21 precision 1/4 -> 1/1 (finding 1).** This delta goes
  UP because the old scorer manufactured false labels. FY21 `nii` is explicitly
  "not probed", and `tax_and_other` and `other_operating_income` sit outside a
  components gold that the gold README says is never force-fitted. Three claims
  the gold cannot decide are now unscored, not wrong. Recall stays 1/2: the
  unverified `nii` slot leaves the recall denominator too.
- **Every "n/a" and "WRONG" label (no score change).** The strings now name the
  reason: "no verified numeric gold" against "gold decomposes a different
  comparison", and `WRONG (numbers)` against `WRONG (basis)`. The 0801 scorecard
  reported one undifferentiated "n/a (checklist or comparison-mismatch gold)".
- **No delta from parent/child aggregation or from duplicate claims.** No 0801
  answer claimed a child against a parent slot, and the only duplicate canonical
  (CBA-impairment-1H26 claims `collective.asset_quality` twice) sits in a case
  with no verified numeric gold, so it is reported as a duplicate and stays
  unscored. Both rules are covered by tests/test_scoring.py.

## Calibration, old against new

| Statistic | 0801 scorer | New scorer |
|---|---|---|
| Claims in the population | 36 | 33 scored (+ 30 unscored, reported as coverage) |
| Cases contributing a scored claim | not reported | 6 of the 16 rescored cases |
| Brier | 0.229 | 0.211 |
| Confidently wrong (>=85) | 0.265 | 0.226 |
| 85-94 bucket | 21 claims, 71% correct | 18 claims, 83% correct |
| 95-100 bucket | 13 claims, 77% correct | 13 claims, 69% correct |

Brier and the confidently-wrong rate improve only because three falsely
labelled claims left the population. The 95-100 bucket gets WORSE (77% -> 69%)
once the hybrid-framing credit goes away, and the top bucket is now less
accurate than the bucket below it. The population is still six CBA cases: these
numbers stay descriptive for this run, never a calibration claim.
