# Rescore — suite dev, combo cheap, saved artifacts, 20260829-0347

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 95 | $0.0023 |
| CBA-cash_earnings-1H26 | OK | 0/3 | 0/3 | — | 3/4 | 1 | 1 | 40 | $0.0023 |
| CBA-roe-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0016 |
| CBA-cet1-1H26 | OK | 1/1 | 1/1 | — | 1/2 | 1 | 1 | 40 | $0.0022 |
| CBA-impairment-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/4 | 4 | 1 | 40 | $0.0021 |
| CBA-cti-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 80 | $0.0022 |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 95 | $0.002 |
| CBA-cet1-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 60 | $0.0022 |
| CBA-nim-FY25 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 95 | $0.0022 |
| CBA-nim-FY26 | OK | 6/6 | 6/6 | 6/7 | 6/6 | 0 | 1 | 95 | $0.0022 |
| CBA-cash_earnings-FY26 | OK | 3/4 | 3/3 | — | 3/3 | 0 | 1 | 40 | $0.0024 |
| CBA-roe-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0013 |
| CBA-cet1-FY26 | OK | n/a (gold decomposes a different comparison) | n/a (gold decomposes a different comparison) | n/a (gold walk is not the case comparison) | 0/0 | 0 | 1 | 60 | $0.0019 |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0017 |
| CBA-cti-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 85 | $0.0023 |

## Calibration (scored quantified driver claims only)

- scored_claims: 34
- unscored_claims: 12
- cases_scored: 7
- cases: 15
- brier: 0.058
- confidently_wrong_rate: 0.0
- 50-69: 1 claims, 0% correct
- 70-84: 2 claims, 0% correct
- 85-94: 13 claims, 100% correct
- 95-100: 18 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
