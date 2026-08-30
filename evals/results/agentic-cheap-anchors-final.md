# Rescore — suite dev, combo agentic-cheap, saved artifacts, 20260830-1303

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | ERROR: no artifact at out/cba-nim-1h26-vs-1h25-agentic-cheap | | | | | | | | |
| CBA-cash_earnings-1H26 | ERROR: no artifact at out/cba-cash_earnings-1h26-vs-1h25-agentic-ch | | | | | | | | |
| CBA-roe-1H26 | ERROR: no artifact at out/cba-roe-1h26-vs-1h25-agentic-cheap | | | | | | | | |
| CBA-cet1-1H26 | ERROR: no artifact at out/cba-cet1-1h26-vs-1h25-agentic-cheap | | | | | | | | |
| CBA-impairment-1H26 | ERROR: no artifact at out/cba-impairment-1h26-vs-1h25-agentic-cheap | | | | | | | | |
| CBA-cti-1H26 | ERROR: no artifact at out/cba-cti-1h26-vs-1h25-agentic-cheap | | | | | | | | |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 88 | $0.0349 |
| CBA-cet1-FY21 | ERROR: no artifact at out/cba-cet1-fy21-vs-fy20-agentic-cheap | | | | | | | | |
| CBA-nim-FY25 | ERROR: no artifact at out/cba-nim-fy25-vs-fy24-agentic-cheap | | | | | | | | |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 0/7 | 7/7 | 0 | 0 | 90 | $0.0112 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — | 4/6 | 2 | 0 | 85 | $0.0427 |
| CBA-roe-FY26 | ERROR: no artifact at out/cba-roe-fy26-vs-fy25-agentic-cheap | | | | | | | | |
| CBA-cet1-FY26 | ERROR: no artifact at out/cba-cet1-fy26-vs-fy25-agentic-cheap | | | | | | | | |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 75 | $0.0318 |
| CBA-cti-FY26 | ERROR: no artifact at out/cba-cti-fy26-vs-fy25-agentic-cheap | | | | | | | | |

## Calibration (scored quantified driver claims only)

- scored_claims: 18
- unscored_claims: 5
- cases_scored: 3
- cases: 15
- brier: 0.016
- confidently_wrong_rate: 0.0
- 70-84: 4 claims, 100% correct
- 85-94: 14 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
