# 05 — Eval design: gold cases, judges, sources of truth

Type: grilling
Status: resolved
Blocked by: 01, 02, 08

## Question

How do we know the agent works, and how do we know it is calibrated? Decide: gold-case construction (bank-published walks and bridges as sources of truth; what to do for metrics without a published walk), judge design (cross-judge attribution validation), the case matrix (banks × metrics × period-types, with at least one older-format period and the named cash-vs-statutory case), the cheap-vs-normal model-combination axis, calibration reporting, and pass thresholds.

## Answer

Resolved with the user (grilling, 2026-08-25):

1. **Case matrix**: ~42 gold cases — 6 metrics × 7 bank-periods (CBA FY26/1H26/FY21-older; NAB FY25/1H26; WBC FY25/1H26). Combos: all-cheap; cheap-extract + normal-author; experimental free `ox-alpha` combo where limits allow. The unseen-bank dry run (registry entry deleted) sits on top. Estimated matrix cost USD 5–10.
2. **Gold, honest about tiers**: walk metrics → hand-recorded published walks; ROE/CTI → deterministic level-1 arithmetic + documented level-2 driver lists; impairment → hand-recorded note splits. Narrative-only drivers never enter numeric gold.
3. **Scorecard, not one number**: movement exact; driver precision/recall (wrong quantified claims punished hardest); calibration (reliability table, Brier, confidently-wrong rate); citation grounding (cross-judge: `deepseek-v4-pro` + `qwen3.7-flash` must agree; disagreement → human flag); validation pass rate. Reported per metric/bank/period-type/combo, **and per pipeline stage** so a weak extractor is visible in isolation.
4. **Tolerances as commented constants**: PA walks ±0.5bp (sum ±1bp); presentation walks ±1bp (sum = endpoint rounding granularity); money ±max(1%, $10m); ratios ±0.1ppt.
5. **Named adversarial cases**: NAB 1H26 cash-vs-statutory ($949m amortisation); the Westpac retired-cash-measure trap; CBA FY26 restated comparatives; CBA FY26 walk-framing conflict (PA vs slide 60).
6. **User amendments**: an extraction micro-eval runs before the matrix to test `qwen3.7-flash` as extractor empirically; the gold set is the backbone — every gold value carries provenance, gold passes its own sum checks, and the set splits ~34 dev / 8 holdout to detect overfitting. Gold construction is ticket 17 with a user spot-check.
