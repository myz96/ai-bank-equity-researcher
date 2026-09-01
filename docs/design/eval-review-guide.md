# Eval structure — formal review guide (for Michael)

The eval design claims the system is measured and calibrated. This guide is
the shortest path to auditing that claim yourself. Order matters; ~60–90
minutes total. Write findings as new tickets in `.scratch/equity-research-agent/issues/`
or as comments appended to ticket 26.

## 1. The rules of the game (15 min)

- `evals/gold/README.md` — the tier system and the not-force-fitted policy.
- `.scratch/equity-research-agent/issues/02-confidence-and-calibration.md` and
  `05-eval-design.md` — what we agreed calibration and scoring mean.
- Challenge: does the scorecard actually measure what ticket 05 promised?

## 2. The gold itself (30 min — the highest-value review)

- `evals/gold/cba-fy26.json` — the richest file. Spot-check 3 values against
  the PDFs in `data/raw/CBA/FY26/` (every value carries its page).
- `evals/gold/cba-fy21.json` — the era case; check the walk against
  `data/raw/CBA/FY21/` presentation slide 63.
- `evals/gold/cba-fy26-crossref.json` — the four holdout consolidation cases.
  Case 4 (restatement-web) has NOT had your pass yet. Ideal: author a fifth
  case yourself that I have never seen.
- Challenge: is any gold value wrong, ambiguous, or force-fitted? Gold errors
  silently corrupt every score downstream.

## 3. The scoring code (20 min)

- `src/bank_equity_researcher/evals/harness.py` — `score_case` (P/R semantics,
  alt_framings, `_match` tolerances), `calibration` (Brier, confidently-wrong,
  bucket edges), `score_crossref` (location coverage).
- `src/bank_equity_researcher/validation/validate.py` — every tolerance constant and its
  justifying comment.
- Challenge: find a way a wrong answer scores right (tolerance too loose,
  alt_framings too generous, parent/child id matching) or a right answer
  scores wrong.

## 4. Judgment calls that are yours, not mine

1. **Tolerances**: PA walks ±0.5bp, presentation sum slack = endpoint rounding,
   money ±max(1%, $10m), ratios ±0.1ppt. Too generous? Too strict?
2. **Confidently-wrong threshold at 85** and the 0–100 self-report semantics.
3. **The dev/holdout split** is still pending (~8 cases): which cases do you
   want held out? Current candidates are flagged `holdout_candidate` in gold.
4. **Single-author risk**: the same agent wrote the pipeline AND verified the
   gold (from rendered pages). Mitigations so far: provenance on every value,
   gold sum checks, your spot-check, the Codex review. Is that enough, or do
   you want to independently re-derive one full case?
5. **Calibration sample size**: headline stats currently rest on ~36 claims.
   Decide the minimum n before we quote a confidently-wrong rate externally.

## Known open items (do not re-find these)

- Defect 24 (comparison awareness) + ticket 27 robustness items: in progress.
- Judge-based fact checking for crossref cases: stub.
- NAB/WBC iteration deferred by the depth-first decision.
- An external senior review by Codex runs alongside yours; its findings will
  be triaged into tickets like everything else.

## Vision-read quote strings in the entailment judge (2026-09-01)

A walk-bar or chart-annotation record carries a quote string BUILT BY CODE
from the extracted values ("[walk chart] ... -3", "[chart annotation] ..."),
not page text; the verbatim gate (validation/quotes.py) never sees it, and
its fidelity discipline is the walk sum checks instead. `cited_quotes` hands
these strings to the entailment judge alongside true page quotes, under a
prompt that calls them verbatim source quotes. Judgment call, kept: the
strings state code-verified numbers, so entailment against them tests the
right thing; relabelling them in the judge prompt would change eval
semantics and belongs to a measured change, not a cleanup.

## NAB 1H26 NIM: no YoY walk exists (2026-09-01)

The bank's 1H26 walk charts both describe Sep 25 -> Mar 26 (half on half);
no published walk covers 1H26 vs 1H25. Two consequences, both judgment
calls, kept:
- The gold labels the case tier "walk" while its own provenance cites the
  results book TABLE. The extraction column therefore prints 0/6 where
  "n/a (bank publishes no walk for this comparison)" is the truer reading;
  the driver columns carry the real result (6/6 recall and precision).
- Two correct YoY values coincide numerically with half-on-half bars, so
  comparison_leak fired and the whole-table cap took confidence to 40 — the
  designed conservative direction (a right answer under-claimed, never a
  wrong one certified). Exempting claims whose citations never touch the
  offending chart would be a measured gate change, deliberately not made
  during cleanup.
Also noted: the presentation-chart record for this case carries a
percent-to-bps slip (1.78% read as 1780 bps) in a context-only record the
agent itself excluded.
