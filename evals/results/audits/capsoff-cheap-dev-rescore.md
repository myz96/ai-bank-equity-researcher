# Rescore — suite dev, combo cheap, saved artifacts, 20260831-0554

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 90 | $0.0033 |
| CBA-cash_earnings-1H26 | OK | 2/3 | 2/3 | — | 3/6 | 3 | 0 | 95 | $0.0048 |
| CBA-roe-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0017 |
| CBA-cet1-1H26 | OK | 0/1 | 0/0 | — | 0/3 | 3 | 1 | 60 | $0.0027 |
| CBA-impairment-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/4 | 4 | 1 | 90 | $0.0025 |
| CBA-cti-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0022 |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 95 | $0.0027 |
| CBA-cet1-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/5 | 5 | 4 | 60 | $0.0028 |
| CBA-nim-FY25 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 95 | $0.0035 |
| CBA-nim-FY26 | OK | 6/6 | 6/6 | 7/7 | 6/6 | 0 | 0 | 90 | $0.0031 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — | 4/6 | 2 | 0 | 95 | $0.005 |
| CBA-roe-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0016 |
| CBA-cet1-FY26 | OK | n/a (gold decomposes a different comparison) | n/a (gold decomposes a different comparison) | n/a (gold walk is not the case comparison) | 0/0 | 0 | 1 | 60 | $0.0026 |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 80 | $0.0023 |
| CBA-cti-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 90 | $0.002 |
| NAB-cash_earnings-FY25 | OK | 2/3 | 2/3 | — | 3/5 | 2 | 1 | 85 | $0.0053 |
| NAB-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0017 |
| NAB-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 80 | $0.0014 |
| NAB-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/5 | 5 | 1 | 85 | $0.0021 |
| NAB-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 90 | $0.0021 |
| WBC-cash_earnings-FY25 | OK | 4/5 | 4/5 | — | 5/6 | 1 | 1 | 75 | $0.0046 |
| WBC-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 1 | 75 | $0.0018 |
| WBC-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0014 |
| WBC-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/7 | 7 | 1 | 75 | $0.0025 |
| WBC-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0013 |

## Calibration (scored quantified driver claims only)

- scored_claims: 42
- unscored_claims: 53
- cases_scored: 8
- cases: 25
- brier: 0.061
- confidently_wrong_rate: 0.049
- 70-84: 1 claims, 0% correct
- 85-94: 27 claims, 93% correct
- 95-100: 14 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
