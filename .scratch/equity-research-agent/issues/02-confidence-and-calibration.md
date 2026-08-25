# 02 — Confidence semantics and calibration measurement

Type: grilling
Status: resolved
Blocked by: 01

## Question

What does a confidence rating mean in this system? Decide: the scale (numeric vs bands), what it attaches to (each driver, the whole attribution, or both), what evidence raises or lowers it, and how calibration is measured against gold labels (for example bucketed accuracy or a Brier-style score), so the agent is measurably calibrated rather than confidently wrong.

## Answer

Resolved with the user (grilling, 2026-08-25). The user rejected rubric machinery as one-step-more-obfuscated; the design is deliberately simple:

- **One self-reported confidence, 0–100, per driver and one for the whole attribution.** Sources and deterministic validation-check results attach to the rating in the output. No rubric, no base-plus-adjustment bookkeeping: the model sees the evidence and the check results, then states one number.
- **The number has one fixed meaning** (used by evals, costless at runtime): the probability that the claim would be judged correct.
- **Correctness is checked without circularity**: (1) gold labels hand-recorded from the banks' own published walks during eval construction — deterministic match on direction and magnitude tolerance; (2) deterministic identity checks; (3) narrative-only claims get a citation-grounding judge ("does the cited page say this?") and are reported separately, never mixed into headline calibration.
- **Calibration reporting**: reliability table, Brier score, and the headline **confidently-wrong rate** (share of claims at ≥85 confidence that were wrong), computed only on the objective-truth slice, per metric and per evidence layer.
- **Iteration loop**: if self-reports are miscalibrated, feed the measured accuracy rates back into the prompt; consider post-hoc remapping only if eval volume justifies it.
- Consequence for ticket 05: eval-case construction includes hand-recording gold walks.
