# Rescore — suite dev, combo cheap, saved artifacts, 20260831-0056

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | OK | 6/6 | 6/6 | 6/6 | 6/6 | 0 | 1 | 90 | $0.0032 |
| CBA-cash_earnings-1H26 | OK | 2/3 | 2/3 | — | 3/6 | 3 | 0 | 95 | $0.005 |
| CBA-roe-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0021 |
| CBA-cet1-1H26 | OK | 1/1 | 1/1 | — | 1/2 | 1 | 0 | 75 | $0.0021 |
| CBA-impairment-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/4 | 4 | 1 | 40 | $0.0024 |
| CBA-cti-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 90 | $0.0018 |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 95 | $0.0027 |
| CBA-cet1-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/4 | 4 | 5 | 40 | $0.0028 |
| CBA-nim-FY25 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 95 | $0.0037 |
| CBA-nim-FY26 | OK | 6/6 | 6/6 | 7/7 | 6/6 | 0 | 0 | 90 | $0.0031 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — | 4/6 | 2 | 0 | 95 | $0.005 |
| CBA-roe-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0015 |
| CBA-cet1-FY26 | OK | n/a (gold decomposes a different comparison) | n/a (gold decomposes a different comparison) | n/a (gold walk is not the case comparison) | 0/0 | 0 | 1 | 40 | $0.0022 |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/5 | 5 | 0 | 80 | $0.0024 |
| CBA-cti-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 90 | $0.0023 |
| NAB-cash_earnings-FY25 | OK | 2/3 | 2/3 | — | 3/6 | 3 | 1 | 40 | $0.0051 |
| NAB-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0016 |
| NAB-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 80 | $0.0014 |
| NAB-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/5 | 5 | 1 | 40 | $0.002 |
| NAB-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 85 | $0.0021 |
| WBC-cash_earnings-FY25 | OK | 3/5 | 3/5 | — | 5/6 | 1 | 1 | 40 | $0.0049 |
| WBC-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 75 | $0.0014 |
| WBC-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0012 |
| WBC-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/7 | 7 | 1 | 40 | $0.0031 |
| WBC-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 1 | 40 | $0.002 |

## Calibration (scored quantified driver claims only)

- scored_claims: 42
- unscored_claims: 54
- cases_scored: 9
- cases: 25
- brier: 0.073
- confidently_wrong_rate: 0.0
- 50-69: 1 claims, 0% correct
- 70-84: 9 claims, 67% correct
- 85-94: 29 claims, 100% correct
- 95-100: 3 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
