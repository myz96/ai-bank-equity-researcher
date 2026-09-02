# Rescore — suite dev, combo agentic, saved artifacts, 20260902-0219

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA-nim-1H26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 93 | $0.4828 |
| CBA-cash_earnings-1H26 | OK | 2/3 | 2/3 | — | 3/6 | 3 | 0 | 93 | $1.1509 |
| CBA-roe-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 80 | $0.53 |
| CBA-cet1-1H26 | OK | 1/1 | 1/1 | — | 1/3 | 2 | 1 | 40 | $0.8227 |
| CBA-impairment-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 88 | $0.9319 |
| CBA-cti-1H26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 80 | $0.7395 |
| CBA-nim-FY21 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 93 | $0.6091 |
| CBA-cet1-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/7 | 7 | 1 | 88 | $1.3967 |
| CBA-nim-FY25 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 93 | $0.5184 |
| CBA-nim-FY26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 0 | 93 | $0.0148 |
| CBA-cash_earnings-FY26 | OK | 4/4 | 4/4 | — | 4/6 | 2 | 0 | 93 | $1.3339 |
| CBA-roe-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 76 | $0.8596 |
| CBA-cet1-FY26 | OK | n/a (gold decomposes a different comparison) | n/a (gold decomposes a different comparison) | n/a (gold walk is not the case comparison) | 0/3 | 3 | 2 | 40 | $1.2791 |
| CBA-impairment-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 88 | $0.6485 |
| CBA-cti-FY26 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 83 | $1.1235 |
| NAB-cash_earnings-FY25 | OK | 2/3 | 2/5 | — | 5/8 | 3 | 1 | 40 | $1.6171 |
| NAB-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 76 | $0.5763 |
| NAB-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 1 | 40 | $0.88 |
| NAB-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/1 | 1 | 0 | 60 | $0.0413 |
| NAB-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 1 | 40 | $0.0461 |
| WBC-cash_earnings-FY25 | OK | 0/5 | 0/0 | — | 0/0 | 0 | 2 | 40 | $0.0291 |
| WBC-roe-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 85 | $0.0202 |
| WBC-cti-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/2 | 2 | 0 | 88 | $0.8532 |
| WBC-cet1-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/1 | 1 | 0 | 58 | $1.0484 |
| WBC-impairment-FY25 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/5 | 5 | 0 | 91 | $0.9744 |

## Calibration (scored quantified driver claims only)

Disclosure: confidently_wrong counts wrong claims at confidence 85+. The validation caps write 80 — one notch below that line — so a claim a cap touches is excluded from the metric by construction. The caps-off ablation (evals/results/audits/capsoff-*) measured the raw self-report rates; read this number alongside it, never alone.

- scored_claims: 41
- unscored_claims: 55
- cases_scored: 8
- cases: 25
- brier: 0.072
- confidently_wrong_rate: 0.0
- 70-84: 8 claims, 50% correct
- 85-94: 33 claims, 100% correct

Scored offline from saved out/*/attribution.json artifacts. No model calls.
