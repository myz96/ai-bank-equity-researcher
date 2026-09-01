# Rescore — suite dev, combo agentic, saved artifacts, 20260901-0342

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-cash_earnings-1H26 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-roe-1H26 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-cet1-1H26 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-impairment-1H26 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-cti-1H26 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-nim-FY21 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-cet1-FY21 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-nim-FY25 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 93 | $0.0148 |
| CBA-cash_earnings-FY26 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-roe-FY26 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-cet1-FY26 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T19: | | | | | | | | |
| CBA-impairment-FY26 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T20: | | | | | | | | |
| CBA-cti-FY26 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T20: | | | | | | | | |
| NAB-cash_earnings-FY25 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T20: | | | | | | | | |
| NAB-roe-FY25 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T20: | | | | | | | | |
| NAB-cti-FY25 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-30T20: | | | | | | | | |
| NAB-cet1-FY25 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-31T01: | | | | | | | | |
| NAB-impairment-FY25 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-31T01: | | | | | | | | |
| WBC-cash_earnings-FY25 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-31T01: | | | | | | | | |
| WBC-roe-FY25 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-31T01: | | | | | | | | |
| WBC-cti-FY25 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-31T01: | | | | | | | | |
| WBC-cet1-FY25 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-31T01: | | | | | | | | |
| WBC-impairment-FY25 | ERROR: artifact predates 2026-09-01T03:00 (generated 2026-08-31T01: | | | | | | | | |

## Calibration (scored quantified driver claims only)

Disclosure: confidently_wrong counts wrong claims at confidence 85+. The validation caps write 80 — one notch below that line — so a claim a cap touches is excluded from the metric by construction. The caps-off ablation (evals/results/audits/capsoff-*) measured the raw self-report rates; read this number alongside it, never alone.

- scored_claims: 7
- unscored_claims: 0
- cases_scored: 1
- cases: 25
- brier: 0.007
- confidently_wrong_rate: 0.0
- 85-94: 7 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
