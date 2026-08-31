# Scorecard — suite dev, combo agentic-glm, 20260831-0246

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 93 | $0.0167 |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 93 | $0.0341 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — | 4/6 | 2 | 0 | 90 | $0.0447 |

## Calibration (scored quantified driver claims only)

- scored_claims: 18
- unscored_claims: 2
- cases_scored: 3
- cases: 3
- brier: 0.011
- confidently_wrong_rate: 0.0
- 70-84: 1 claims, 100% correct
- 85-94: 17 claims, 100% correct
