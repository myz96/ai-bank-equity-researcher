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

## Progress 2026-08-28: the five items are implemented and verified offline

All five items are done in `src/bank_equity_researcher/evals.py`, with 47
pytest cases in `tests/test_scoring.py` and an offline rescore of the 0801
artifacts in `evals/results/rescore-20260827-0801-newscorer.md`. The rescore
made no model calls and spent nothing.

### What the scorer does now

1. **Three-state labels.** Each quantified claim gets `correct`, `incorrect` or
   `unscored`. A claim is unscored when the gold verifies no value for it (FY21
   `nii` is "not probed"), when the canonical is the `other_unmapped` bucket, or
   when the gold framing does not cover the driver AND the framing is not
   exhaustive. A walk framing is exhaustive, because a published walk is the
   whole movement; `components` and `arithmetic` gold is not, because the gold
   README says reconciliation is never force-fitted. Precision and calibration
   use scored claims only. The scorecard reports coverage per case: scored
   claims, unscored claims, and unscored gold slots.
2. **One coherent framing.** `score_drivers` scores the answer against each
   eligible framing separately and reports the best one. Precision and recall
   always come from that one framing, so a mixture of framings cannot collect
   credit. Ties go to the primary framing. Canonical claims must be unique: a
   repeat of a canonical with a verified gold value is incorrect, a repeat
   without one is unscored, and both raise a `duplicate_canonicals` count.
   Parent and child: a dotted id's parent is its prefix before the dot, a set of
   child claims satisfies a parent slot when the children sum to the parent
   value, a parent claim satisfies a parent slot only, and a child with its own
   verified gold value (`rwa_children`) is scored on that value.
3. **Extraction one-to-one.** `score_extraction` matches gold bars against ONE
   walk record, by canonical label AND value, each extracted bar used at most
   once. A walk record is eligible only when its endpoints are the case's
   movement endpoints. When the gold walk declares another comparison, the case
   is unscored, exactly as driver scoring already treated it.
4. **Movement completeness and one typed tolerance.** `score_movement` checks
   numbers, unit, basis and comparator, and reports each check separately.
   `Tolerance` applies validate.py's documented constants: $m = max(1%, $10m),
   bps = 0.5, ppt = 0.1, and a sign flip never matches.
5. **Regression tests.** `tests/test_scoring.py` is table-driven. Each row names
   the counterexample it prevents (WRONG-SCORES-RIGHT or RIGHT-SCORES-WRONG).
   Run `uv run pytest -q`: 47 passed.

### Amendments applied, as instructed

- The `rwa` parent gap is handled in the scorer, generically. taxonomy.py is
  unchanged.
- The typed tolerance lives in evals.py and imports validate.py's constants, so
  there is one set of numbers today. validate.py is unchanged.

### Rescore of the 0801 artifacts (no model calls, no spend)

```
uv run bank-equity-researcher evals rescore --suite dev --combo cheap --bank CBA \
  --since 2026-08-27T07:30 --until 2026-08-27T08:05 \
  --baseline evals/results/20260827-0801-cheap-dev.jsonl \
  --label rescore-20260827-0801-newscorer
```

Five score deltas, each traced to its finding in the rescore document:

- CBA-nim-1H26 recall and precision 4/7 -> 3/7 (finding 4, hybrid framing).
- CBA-nim-FY25 movement OK -> WRONG (finding 6, basis `statutory` against a
  `cash` case).
- CBA-nim-FY25 extraction 4/7 -> 0/7 (finding 5, the only extracted walk is
  half on half, and one extracted 0 used to satisfy two gold zero bars).
- CBA-cet1-FY26 extraction 4/4 -> n/a (finding 5, the gold walk is not the
  case's comparison).
- CBA-cash_earnings-FY21 precision 1/4 -> 1/1 (finding 1, three claims the gold
  cannot decide are unscored, not wrong). This delta goes up on purpose.

Calibration moves from 36 claims / Brier 0.229 / 0.265 confidently wrong to 33
scored claims / Brier 0.211 / 0.226. The 95-100 bucket gets worse, 77% -> 69%,
once the hybrid credit goes away. Coverage is the real news: only 6 of the 16
rescored cases contribute a scored claim, and 30 claims are unscored.

Three baseline rows have no comparable artifact: two cases crashed in the 0801
run, and a concurrent run overwrote the CBA-cet1-1H26 artifact on 2026-08-28.
The rescore therefore takes `--since` and `--until` and scores one run's
artifacts on their own.

### Changes needed in files this ticket could not edit

1. **taxonomy.py — the `rwa` parent id is missing.** `TAXONOMY["cet1"]["drivers"]`
   has `rwa.credit`, `rwa.market`, `rwa.operational` and `rwa.irrbb`, but no
   `rwa`. The FY26 CET1 gold uses `rwa` as a parent slot. Add:
   `"rwa": "Total risk-weighted assets movement (parent of rwa.credit, rwa.market, rwa.operational, rwa.irrbb)"`.
   The scorer no longer needs it, but the author has no legal id for a whole-RWA
   bar and must mislabel it as a child.
2. **registry/cba.json — `cet1_walk_labels` maps "RWA" to `rwa.credit`.** The
   slide-32 bar labelled "RWA" is the TOTAL movement (-46 = credit -38 + IRRBB
   -16 + market +8). It must map to the `rwa` parent once the taxonomy has the
   id. Until then every CET1 answer states total RWA as credit RWA, which the
   new scorer marks incorrect wherever the case is scored. FY26 CET1 escapes
   only because its gold walk is another comparison.
3. **validate.py — one tolerance rule, not two.** `check_movement` uses a flat
   0.51 for every unit; it should call `evals.tolerance_for(movement.unit)`.
   `WALK_SUM_TOL_*` should become `Tolerance` objects too. The constants are
   already shared; the application rules are not.
4. **extract.py — walk endpoints are not structured.** `score_extraction`
   classifies a walk by its endpoints, which it can only read by parsing the
   quote string `extract_walk` stamps. Put the endpoint VALUES and the endpoint
   LABELS on the record (`NumberFact` entries, or fields on `EvidenceRecord`),
   and the classification stops depending on a text format.
   Follow-up for whoever lands defect 24: `validate.annotate_walks` classifies a
   walk by resolving its endpoint labels through the registry calendar, which is
   stronger than the endpoint values `score_extraction` uses today. Values
   cannot separate the two comparisons when they share endpoints — CBA 1H26
   publishes a PCP walk and a half-on-half walk that both run 208 -> 204. Once
   the labels reach the evidence record, `score_extraction` should call
   `label_end_date` and accept only walks classified as the case comparison.
5. **pipeline.py — artifacts are overwritten in place.** `out/<slug>/` holds one
   run only, so a later run destroys the evidence an earlier scorecard was built
   from. This happened during this ticket. Write `out/<slug>/<stamp>/`, or copy
   the artifacts beside the run's .jsonl.

### Gold observations (not edited, per instruction)

- CTI gold gives `value_pct` growth rates, but the agent claims ppt
  contributions to the ratio. The two are different quantities, so CTI driver
  claims can never be value-scored. Either the gold or the taxonomy must state
  the CTI contribution unit.
- ROE, CTI, impairment and FY21 CET1 gold is direction-only. Those cases now
  report "n/a (no verified numeric gold)" honestly, which is why 10 of 16 cases
  contribute nothing to precision. This is a gold-coverage problem (finding 8),
  not a scorer problem.
- Gold carries a file-level `basis` only. The scorer treats `cet1` as
  basis-not-applicable, because a regulatory capital ratio has no cash,
  statutory or ex-notables basis. If the team disagrees, gold needs a per-case
  basis field.
