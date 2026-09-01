# Rescore — suite holdout, combo fast, saved artifacts, 20260901-1814

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-cash_earnings-FY21 | WRONG (numbers, unit) | 2/2 | 2/2 | — | 2/6 | 4 | 2 | 40 | $0.0111 |
| CBA-roe-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 90 | $0.0053 |
| CBA-impairment-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 92 | $0.0035 |
| CBA-cti-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 82 | $0.0104 |
| NAB-nim-1H26 | OK | 6/6 | 6/6 | 0/6 | 6/6 | 0 | 1 | 40 | $0.0038 |
| NAB-nim-FY25 | OK | 6/6 | 6/6 | 0/6 | 6/6 | 0 | 3 | 40 | $0.0037 |
| WBC-nim-1H26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 1 | 40 | $0.004 |
| WBC-nim-FY25 | OK | 6/6 | 6/6 | 6/6 | 6/6 | 0 | 0 | 90 | $0.0032 |

## Calibration (scored quantified driver claims only)

Disclosure: confidently_wrong counts wrong claims at confidence 85+. The validation caps write 80 — one notch below that line — so a claim a cap touches is excluded from the metric by construction. The caps-off ablation (evals/results/audits/capsoff-*) measured the raw self-report rates; read this number alongside it, never alone.

- scored_claims: 27
- unscored_claims: 12
- cases_scored: 5
- cases: 8
- brier: 0.021
- confidently_wrong_rate: 0.0
- 70-84: 7 claims, 100% correct
- 85-94: 20 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
