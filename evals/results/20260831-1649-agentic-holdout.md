# Scorecard — suite holdout, combo agentic, 20260831-1649

| Case | Movement | Driver recall | Precision | Extraction | Scored claims | Unscored | Failed checks | Conf | Cost |
|---|---|---|---|---|---|---|---|---|---|
| CBA cash_earnings FY21 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| CBA-roe-FY21 | OK | n/a (no verified numeric gold) | n/a (no verified numeric gold) | — | 0/3 | 3 | 0 | 90 | $0.0236 |
| CBA impairment FY21 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| CBA cti FY21 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| NAB nim 1H26 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| NAB nim FY25 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| WBC nim 1H26 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |
| WBC nim FY25 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | | | |

## Calibration (scored quantified driver claims only)

Disclosure: confidently_wrong counts wrong claims at confidence 85+. The validation caps write 80 — one notch below that line — so a claim a cap touches is excluded from the metric by construction. The caps-off ablation (evals/results/audits/capsoff-*) measured the raw self-report rates; read this number alongside it, never alone.

- scored_claims: 0
- unscored_claims: 3
- cases_scored: 0
- cases: 8
- brier: None
- confidently_wrong_rate: None
