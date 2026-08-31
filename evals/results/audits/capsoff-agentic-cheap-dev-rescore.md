# Rescore — suite dev, combo agentic-cheap, saved artifacts, 20260831-0638

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | OK | 6/6 | 6/6 | 6/6 | 6/6 | 0 | 0 | 88 | $0.0234 |
| CBA-cash_earnings-1H26 | OK | 2/3 | 2/3 | — | 3/6 | 3 | 0 | 90 | $0.0579 |
| CBA-roe-1H26 | WRONG (numbers) | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.044 |
| CBA-cet1-1H26 | OK | 0/1 | 0/0 | — | 0/2 | 2 | 2 | 70 | $0.06 |
| CBA-impairment-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 1 | 85 | $0.0095 |
| CBA-cti-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 75 | $0.0525 |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 0/7 | 7/7 | 0 | 0 | 92 | $0.0104 |
| CBA-cet1-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/4 | 4 | 4 | 65 | $0.0866 |
| CBA-nim-FY25 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 90 | $0.0248 |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 90 | $0.0224 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — | 4/6 | 2 | 0 | 90 | $0.0726 |
| CBA-roe-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 1 | 75 | $0.0341 |
| CBA-cet1-FY26 | OK | n/a (gold decomposes a different comparison) | n/a (gold decomposes a different comparison) | n/a (gold walk is not the case comparison) | 0/0 | 0 | 1 | 75 | $0.0754 |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 85 | $0.0819 |
| CBA-cti-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 75 | $0.0972 |
| NAB-cash_earnings-FY25 | OK | 3/3 | 3/3 | — | 3/6 | 3 | 0 | 90 | $0.1551 |
| NAB-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 75 | $0.0704 |
| NAB-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 75 | $0.0886 |
| NAB-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/1 | 1 | 0 | 65 | $0.0344 |
| NAB-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 85 | $0.1158 |
| WBC-cash_earnings-FY25 | OK | 4/5 | 4/5 | — | 5/5 | 0 | 0 | 90 | $0.0602 |
| WBC-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 75 | $0.1403 |
| WBC-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 75 | $0.0726 |
| WBC-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 65 | $0.1278 |
| WBC-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/4 | 4 | 2 | 88 | $0.0562 |

## Calibration (scored quantified driver claims only)

- scored_claims: 42
- unscored_claims: 41
- cases_scored: 8
- cases: 25
- brier: 0.042
- confidently_wrong_rate: 0.026
- 70-84: 3 claims, 67% correct
- 85-94: 26 claims, 96% correct
- 95-100: 13 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
