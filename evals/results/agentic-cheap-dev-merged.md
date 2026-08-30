# Rescore — suite dev, combo agentic-cheap, saved artifacts, 20260830-2039

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 92 | $0.0111 |
| CBA-cash_earnings-1H26 | OK | 2/3 | 2/3 | — | 3/6 | 3 | 1 | 90 | $0.1761 |
| CBA-roe-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0362 |
| CBA-cet1-1H26 | OK | 1/1 | 1/1 | — | 1/1 | 0 | 1 | 40 | $0.0706 |
| CBA-impairment-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 88 | $0.0042 |
| CBA-cti-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/1 | 1 | 0 | 80 | $0.036 |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 90 | $0.0062 |
| CBA-cet1-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/6 | 6 | 0 | 90 | $0.038 |
| CBA-nim-FY25 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 90 | $0.0266 |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 6/6 | 7/7 | 0 | 1 | 90 | $0.0083 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — | 4/6 | 2 | 0 | 80 | $0.1681 |
| CBA-roe-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 80 | $0.0497 |
| CBA-cet1-FY26 | OK | n/a (gold decomposes a different comparison) | n/a (gold decomposes a different comparison) | n/a (gold walk is not the case comparison) | 0/1 | 1 | 2 | 40 | $0.1261 |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 85 | $0.0448 |
| CBA-cti-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 75 | $0.0479 |
| NAB-cash_earnings-FY25 | OK | 3/3 | 3/3 | — | 3/7 | 4 | 0 | 85 | $0.0346 |
| NAB-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 75 | $0.0441 |
| NAB-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/1 | 1 | 1 | 40 | $0.1608 |
| NAB-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/1 | 1 | 1 | 40 | $0.098 |
| NAB-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 85 | $0.0779 |
| WBC-cash_earnings-FY25 | OK | 4/5 | 4/5 | — | 5/5 | 0 | 0 | 90 | $0.0444 |
| WBC-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0579 |
| WBC-cti-FY25 | WRONG (numbers, unit) | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 0 | $0.1529 |
| WBC-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 55 | $0.0509 |
| WBC-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 2 | 40 | $0.0416 |

## Calibration (scored quantified driver claims only)

- scored_claims: 44
- unscored_claims: 33
- cases_scored: 9
- cases: 25
- brier: 0.047
- confidently_wrong_rate: 0.0
- 70-84: 11 claims, 82% correct
- 85-94: 29 claims, 100% correct
- 95-100: 4 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
