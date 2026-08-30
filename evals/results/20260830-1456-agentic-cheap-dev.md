# Scorecard — suite dev, combo agentic-cheap, 20260830-1456

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | OK | 6/6 | 6/6 | 6/6 | 6/6 | 0 | 0 | 90 | $0.0159 |
| CBA-cash_earnings-1H26 | OK | 2/3 | 2/3 | — | 3/5 | 2 | 1 | 40 | $0.1135 |
| CBA-roe-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0128 |
| CBA-cet1-1H26 | OK | 1/1 | 1/1 | — | 1/1 | 0 | 1 | 40 | $0.0496 |
| CBA-impairment-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 85 | $0.0204 |
| CBA-cti-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 1 | 40 | $0.0633 |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 92 | $0.0056 |
| CBA-cet1-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/6 | 6 | 0 | 85 | $0.0665 |
| CBA-nim-FY25 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 90 | $0.0538 |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 6/7 | 7/7 | 0 | 1 | 85 | $0.0315 |
| CBA-cash_earnings-FY26 | OK | 0/4 | 0/0 | — | 0/0 | 0 | 2 | 40 | $0.0397 |
| CBA-roe-FY26 | WRONG (numbers) | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0127 |
| CBA-cet1-FY26 | OK | n/a (gold decomposes a different comparison) | n/a (gold decomposes a different comparison) | n/a (gold walk is not the case comparison) | 0/0 | 0 | 1 | 65 | $0.0685 |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 85 | $0.0269 |
| CBA-cti-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 75 | $0.0658 |
| NAB-cash_earnings-FY25 | OK | 3/3 | 3/3 | — | 3/6 | 3 | 1 | 40 | $0.1029 |
| NAB-roe-FY25 | WRONG (numbers) | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 75 | $0.038 |
| NAB-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/1 | 1 | 0 | 75 | $0.0235 |
| NAB-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/1 | 1 | 0 | 65 | $0.0807 |
| NAB-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 85 | $0.0989 |
| WBC-cash_earnings-FY25 | OK | 4/5 | 4/5 | — | 5/5 | 0 | 0 | 90 | $0.0906 |
| WBC-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 75 | $0.0497 |
| WBC-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 85 | $0.0462 |
| WBC-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 55 | $0.0509 |
| WBC-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 2 | 40 | $0.0416 |

## Calibration (scored quantified driver claims only)

- scored_claims: 39
- unscored_claims: 37
- cases_scored: 8
- cases: 25
- brier: 0.052
- confidently_wrong_rate: 0.03
- 70-84: 6 claims, 83% correct
- 85-94: 32 claims, 97% correct
- 95-100: 1 claims, 100% correct
