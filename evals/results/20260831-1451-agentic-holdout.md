# Scorecard — suite holdout, combo agentic, 20260831-1451

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA cash_earnings FY21 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| CBA roe FY21 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| CBA impairment FY21 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| CBA cti FY21 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| NAB nim 1H26 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| NAB nim FY25 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| WBC-nim-1H26 | OK | 7/7 | 7/7 | 7/7 | 7/7 | 0 | 1 | 40 | $0.0134 |
| WBC-nim-FY25 | OK | 0/6 | 0/0 | 6/6 | 0/0 | 0 | 2 | 40 | $0.0061 |

## Calibration (scored quantified driver claims only)

Disclosure: confidently_wrong counts wrong claims at confidence 85+. The validation caps write 80 — one notch below that line — so a claim a cap touches is excluded from the metric by construction. The caps-off ablation (evals/results/audits/capsoff-*) measured the raw self-report rates; read this number alongside it, never alone.

- scored_claims: 7
- unscored_claims: 0
- cases_scored: 1
- cases: 8
- brier: 0.006
- confidently_wrong_rate: 0.0
- 85-94: 7 claims, 100% correct
