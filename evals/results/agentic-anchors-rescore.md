# Rescore — suite dev, combo agentic, saved artifacts, 20260830-1258

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | ERROR: no artifact at out/cba-nim-1h26-vs-1h25-agentic | | | | | | | | |
| CBA-cash_earnings-1H26 | ERROR: no artifact at out/cba-cash_earnings-1h26-vs-1h25-agentic | | | | | | | | |
| CBA-roe-1H26 | ERROR: no artifact at out/cba-roe-1h26-vs-1h25-agentic | | | | | | | | |
| CBA-cet1-1H26 | ERROR: no artifact at out/cba-cet1-1h26-vs-1h25-agentic | | | | | | | | |
| CBA-impairment-1H26 | ERROR: no artifact at out/cba-impairment-1h26-vs-1h25-agentic | | | | | | | | |
| CBA-cti-1H26 | ERROR: no artifact at out/cba-cti-1h26-vs-1h25-agentic | | | | | | | | |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 93 | $0.4862 |
| CBA-cet1-FY21 | ERROR: no artifact at out/cba-cet1-fy21-vs-fy20-agentic | | | | | | | | |
| CBA-nim-FY25 | ERROR: no artifact at out/cba-nim-fy25-vs-fy24-agentic | | | | | | | | |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 93 | $0.4764 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — | 4/6 | 2 | 0 | 91 | $1.5745 |
| CBA-roe-FY26 | ERROR: no artifact at out/cba-roe-fy26-vs-fy25-agentic | | | | | | | | |
| CBA-cet1-FY26 | ERROR: no artifact at out/cba-cet1-fy26-vs-fy25-agentic | | | | | | | | |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 86 | $0.5786 |
| CBA-cti-FY26 | ERROR: no artifact at out/cba-cti-fy26-vs-fy25-agentic | | | | | | | | |

## Calibration (scored quantified driver claims only)

- scored_claims: 18
- unscored_claims: 5
- cases_scored: 3
- cases: 15
- brier: 0.01
- confidently_wrong_rate: 0.0
- 70-84: 1 claims, 100% correct
- 85-94: 17 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
