# Rescore — suite dev, combo agentic-cheap, saved artifacts, 20260831-1441

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | OK | 6/6 | 6/6 | 6/6 | 6/6 | 0 | 0 | 85 | $0.0102 |
| CBA-cash_earnings-1H26 | OK | 2/3 | 2/3 | — | 3/6 | 3 | 0 | 88 | $0.0456 |
| CBA-roe-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 75 | $0.0218 |
| CBA-cet1-1H26 | OK | 0/1 | 0/0 | — | 0/0 | 0 | 3 | 70 | $0.0406 |
| CBA-impairment-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 2 | 40 | $0.0176 |
| CBA-cti-1H26 | WRONG (numbers, unit) | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 0 | $0.0475 |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 88 | $0.0362 |
| CBA-cet1-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/6 | 6 | 0 | 90 | $0.0393 |
| CBA-nim-FY25 | OK | 7/7 | 7/7 | 0/7 | 7/7 | 0 | 0 | 90 | $0.023 |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 92 | $0.0094 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — | 4/6 | 2 | 0 | 88 | $0.0777 |
| CBA-roe-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 75 | $0.0359 |
| CBA-cet1-FY26 | OK | n/a (gold decomposes a different comparison) | n/a (gold decomposes a different comparison) | n/a (gold walk is not the case comparison) | 0/2 | 2 | 2 | 40 | $0.056 |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 85 | $0.0085 |
| CBA-cti-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 80 | $0.0554 |
| NAB-cash_earnings-FY25 | OK | 0/3 | 0/0 | — | 0/0 | 0 | 1 | 40 | $0.1238 |
| NAB-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 1 | 40 | $0.037 |
| NAB-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 75 | $0.0824 |
| NAB-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/1 | 1 | 2 | 40 | $0.0925 |
| NAB-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 85 | $0.1307 |
| WBC-cash_earnings-FY25 | OK | 0/5 | 0/0 | — | 0/0 | 0 | 1 | 40 | $0.0538 |
| WBC-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0502 |
| WBC-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 85 | $0.0473 |
| WBC-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 40 | $0.0592 |
| WBC-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/6 | 6 | 2 | 40 | $0.0506 |

## Calibration (scored quantified driver claims only)

Disclosure: confidently_wrong counts wrong claims at confidence 85+. The validation caps write 80 — one notch below that line — so a claim a cap touches is excluded from the metric by construction. The caps-off ablation (evals/results/audits/capsoff-*) measured the raw self-report rates; read this number alongside it, never alone.

- scored_claims: 34
- unscored_claims: 39
- cases_scored: 6
- cases: 25
- brier: 0.039
- confidently_wrong_rate: 0.0
- 70-84: 7 claims, 86% correct
- 85-94: 27 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
