# Rescore — suite dev, combo fast, saved artifacts, 20260901-0400

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | ERROR: no artifact at out/cba-nim-1h26-vs-1h25-fast | | | | | | | | |
| CBA-cash_earnings-1H26 | ERROR: no artifact at out/cba-cash_earnings-1h26-vs-1h25-fast | | | | | | | | |
| CBA-roe-1H26 | ERROR: no artifact at out/cba-roe-1h26-vs-1h25-fast | | | | | | | | |
| CBA-cet1-1H26 | ERROR: no artifact at out/cba-cet1-1h26-vs-1h25-fast | | | | | | | | |
| CBA-impairment-1H26 | ERROR: no artifact at out/cba-impairment-1h26-vs-1h25-fast | | | | | | | | |
| CBA-cti-1H26 | ERROR: no artifact at out/cba-cti-1h26-vs-1h25-fast | | | | | | | | |
| CBA-nim-FY21 | ERROR: no artifact at out/cba-nim-fy21-vs-fy20-fast | | | | | | | | |
| CBA-cet1-FY21 | ERROR: no artifact at out/cba-cet1-fy21-vs-fy20-fast | | | | | | | | |
| CBA-nim-FY25 | ERROR: no artifact at out/cba-nim-fy25-vs-fy24-fast | | | | | | | | |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 92 | $0.0082 |
| CBA-cash_earnings-FY26 | ERROR: no artifact at out/cba-cash_earnings-fy26-vs-fy25-fast | | | | | | | | |
| CBA-roe-FY26 | ERROR: no artifact at out/cba-roe-fy26-vs-fy25-fast | | | | | | | | |
| CBA-cet1-FY26 | ERROR: no artifact at out/cba-cet1-fy26-vs-fy25-fast | | | | | | | | |
| CBA-impairment-FY26 | ERROR: no artifact at out/cba-impairment-fy26-vs-fy25-fast | | | | | | | | |
| CBA-cti-FY26 | ERROR: no artifact at out/cba-cti-fy26-vs-fy25-fast | | | | | | | | |
| NAB-cash_earnings-FY25 | ERROR: no artifact at out/nab-cash_earnings-fy25-vs-fy24-fast | | | | | | | | |
| NAB-roe-FY25 | ERROR: no artifact at out/nab-roe-fy25-vs-fy24-fast | | | | | | | | |
| NAB-cti-FY25 | ERROR: no artifact at out/nab-cti-fy25-vs-fy24-fast | | | | | | | | |
| NAB-cet1-FY25 | ERROR: no artifact at out/nab-cet1-fy25-vs-fy24-fast | | | | | | | | |
| NAB-impairment-FY25 | ERROR: no artifact at out/nab-impairment-fy25-vs-fy24-fast | | | | | | | | |
| WBC-cash_earnings-FY25 | ERROR: no artifact at out/wbc-cash_earnings-fy25-vs-fy24-fast | | | | | | | | |
| WBC-roe-FY25 | ERROR: no artifact at out/wbc-roe-fy25-vs-fy24-fast | | | | | | | | |
| WBC-cti-FY25 | ERROR: no artifact at out/wbc-cti-fy25-vs-fy24-fast | | | | | | | | |
| WBC-cet1-FY25 | ERROR: no artifact at out/wbc-cet1-fy25-vs-fy24-fast | | | | | | | | |
| WBC-impairment-FY25 | ERROR: no artifact at out/wbc-impairment-fy25-vs-fy24-fast | | | | | | | | |

## Calibration (scored quantified driver claims only)

Disclosure: confidently_wrong counts wrong claims at confidence 85+. The validation caps write 80 — one notch below that line — so a claim a cap touches is excluded from the metric by construction. The caps-off ablation (evals/results/audits/capsoff-*) measured the raw self-report rates; read this number alongside it, never alone.

- scored_claims: 7
- unscored_claims: 0
- cases_scored: 1
- cases: 25
- brier: 0.01
- confidently_wrong_rate: 0.0
- 85-94: 7 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
