# 29 — Calibration and reporting honesty (Codex findings 2, 9, 10, 11, 12)

Type: task
Status: open

## Question

Make the reports claim only what the data supports (docs/reviews/codex-eval-review-2026-08-27.md):

1. **Coverage first (finding 2)**: every scorecard leads with the evaluable populations — cases run/crashed, claims scored/unscored/abstained — then reports movement, driver, and whole-attribution calibration as SEPARATE populations. High-confidence movement failures must enter a calibration population (currently invisible to Brier).
2. **Uncertainty (finding 9)**: report raw numerators, Wilson intervals, and case-cluster structure with every rate; label single-run numbers "descriptive for this run only". No externally-quoted calibration claim without repeated runs and case-cluster bootstrap.
3. **Scorecard metadata (finding 10)**: record commit hash, model IDs, case manifest, gold-file hash, and retry policy in every scorecard header so runs are comparable experiments.
4. **Threshold boundary (finding 11)**: decide whether the single-source cap value (85) belongs inside the confidently-wrong population; align the cap and the threshold so a capped claim is not automatically "confident" (e.g. cap to 84 or threshold to >85), and document the choice.
5. **Per-check reporting (finding 12)**: report each deterministic check's outcome by name and stage (pass/fail/not-applicable), not a lossy count of "Failed check:" strings.
