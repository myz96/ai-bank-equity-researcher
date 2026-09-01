# Rescore — suite holdout, combo fast, saved artifacts, 20260901-0848

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-cash_earnings-FY21 | OK | 2/2 | 2/2 | — | 2/6 | 4 | 1 | 90 | $0.0369 |
| CBA-roe-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 1 | 40 | $0.0402 |
| CBA-impairment-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 90 | $0.0362 |
| CBA-cti-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 78 | $0.0169 |
| NAB-nim-1H26 | OK | 6/6 | 6/6 | 0/6 | 6/6 | 0 | 1 | 40 | $0.0054 |
| NAB-nim-FY25 | WRONG (numbers, unit) | 0/6 | 0/0 | 0/6 | 0/0 | 0 | 2 | 0 | $0.0187 |
| WBC-nim-1H26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 1 | 40 | $0.0088 |
| WBC-nim-FY25 | OK | 6/6 | 6/6 | 6/6 | 6/6 | 0 | 1 | 40 | $0.0078 |

## Calibration (scored quantified driver claims only)

Disclosure: confidently_wrong counts wrong claims at confidence 85+. The validation caps write 80 — one notch below that line — so a claim a cap touches is excluded from the metric by construction. The caps-off ablation (evals/results/audits/capsoff-*) measured the raw self-report rates; read this number alongside it, never alone.

- scored_claims: 21
- unscored_claims: 11
- cases_scored: 4
- cases: 8
- brier: 0.017
- confidently_wrong_rate: 0.0
- 70-84: 3 claims, 100% correct
- 85-94: 18 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
