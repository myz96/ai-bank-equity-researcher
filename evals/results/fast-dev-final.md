# Rescore — suite dev, combo fast, saved artifacts, 20260901-0848

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | ERROR: no artifact at out/cba-nim-1h26-vs-1h25-fast | | | | | | | | |
| CBA-cash_earnings-1H26 | OK | 2/3 | 2/3 | — | 3/6 | 3 | 1 | 40 | $0.009 |
| CBA-roe-1H26 | WRONG (numbers, unit) | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 0 | $0.016 |
| CBA-cet1-1H26 | ERROR: no artifact at out/cba-cet1-1h26-vs-1h25-fast | | | | | | | | |
| CBA-impairment-1H26 | ERROR: no artifact at out/cba-impairment-1h26-vs-1h25-fast | | | | | | | | |
| CBA-cti-1H26 | ERROR: no artifact at out/cba-cti-1h26-vs-1h25-fast | | | | | | | | |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 92 | $0.0087 |
| CBA-cet1-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/10 | 10 | 0 | 92 | $0.0091 |
| CBA-nim-FY25 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 92 | $0.0054 |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 90 | $0.012 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — | 4/6 | 2 | 1 | 40 | $0.0238 |
| CBA-roe-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 85 | $0.0109 |
| CBA-cet1-FY26 | WRONG (numbers, unit) | n/a (gold decomposes a different comparison) | n/a (gold decomposes a different comparison) | n/a (gold walk is not the case comparison) | 0/0 | 0 | 2 | 0 | $0.0149 |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 90 | $0.0045 |
| CBA-cti-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 88 | $0.0142 |
| NAB-cash_earnings-FY25 | OK | 2/3 | 2/3 | — | 3/6 | 3 | 0 | 92 | $0.0141 |
| NAB-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0099 |
| NAB-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 1 | 40 | $0.0338 |
| NAB-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/1 | 1 | 0 | 70 | $0.0073 |
| NAB-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 4 | 40 | $0.0176 |
| WBC-cash_earnings-FY25 | OK | 3/5 | 3/5 | — | 5/6 | 1 | 0 | 90 | $0.0153 |
| WBC-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.0084 |
| WBC-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 85 | $0.0065 |
| WBC-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/0 | 0 | 1 | 40 | $0.0199 |
| WBC-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/4 | 4 | 1 | 90 | $0.0143 |

## Calibration (scored quantified driver claims only)

Disclosure: confidently_wrong counts wrong claims at confidence 85+. The validation caps write 80 — one notch below that line — so a claim a cap touches is excluded from the metric by construction. The caps-off ablation (evals/results/audits/capsoff-*) measured the raw self-report rates; read this number alongside it, never alone.

- scored_claims: 36
- unscored_claims: 42
- cases_scored: 7
- cases: 25
- brier: 0.088
- confidently_wrong_rate: 0.036
- 70-84: 8 claims, 62% correct
- 85-94: 28 claims, 96% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
