# 28 — Harness correctness round (Codex findings 1, 4, 5, 6, 13)

Type: task
Status: open

## Question

Fix the scorer so a wrong answer cannot score right and a right answer cannot score wrong (docs/reviews/codex-eval-review-2026-08-27.md):

1. **Three-state labels (finding 1)**: claims match against gold slots that are correct/incorrect/UNSCORED. A claim whose canonical has no verified gold value (e.g. FY21 `nii` "not probed") is unscored — excluded from precision AND calibration, counted in a coverage stat instead.
2. **Coherent-framing scoring (finding 4)**: score the answer one-to-one against ONE eligible framing (primary first; an alt framing only as a whole), no hybrids; enforce unique canonical claims; define parent/child aggregation (children may sum to a parent slot; a parent claim satisfies a parent slot only). Fix the CET1 gold's `rwa` parent id missing from the taxonomy (add the parent id to the taxonomy — do not edit gold).
3. **Extraction metric one-to-one (finding 5)**: match bars by normalized label AND value AND comparison (only walks classified as the case's comparison count); each extracted bar satisfies at most one gold bar.
4. **Movement scoring completeness (finding 6)**: verify unit and basis against gold basis; one shared typed tolerance implementation used by both evals.py and validate.py ($m tolerance = max(1%, $10m) as documented).
5. **Scorer regression tests (finding 13)**: table-driven pytest cases covering duplicate claims, hybrid framings, parent/child, wrong unit/basis, unscored gold, duplicate extraction values — each demonstrating the wrong-scores-right or right-scores-wrong counterexample it prevents.

Verification: rerun scoring OFFLINE against the existing out/*/attribution.json artifacts (no model calls needed — add a rescore mode if simplest); expect scores to move DOWN where the old scorer was generous; document every delta in the ticket.
