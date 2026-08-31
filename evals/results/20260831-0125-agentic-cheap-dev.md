# Scorecard — suite dev, combo agentic-cheap, 20260831-0125

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-roe-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 75 | $0.0359 |
| CBA-cet1-FY26 | OK | n/a (gold decomposes a different comparison) | n/a (gold decomposes a different comparison) | n/a (gold walk is not the case comparison) | 0/2 | 2 | 2 | 40 | $0.056 |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 85 | $0.0085 |
| CBA-cti-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 80 | $0.0554 |
| NAB-cash_earnings-FY25 | OK | 0/3 | 0/0 | — | 0/0 | 0 | 1 | 40 | $0.1238 |
| WBC-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 85 | $0.0473 |
| WBC cet1 FY25 | ERROR: 1 validation error for Attribution
residual.value
  Input sh | | | | | | | | |
| WBC-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/6 | 6 | 2 | 40 | $0.0506 |

## Calibration (scored quantified driver claims only)

- scored_claims: 0
- unscored_claims: 15
- cases_scored: 0
- cases: 8
- brier: None
- confidently_wrong_rate: None
