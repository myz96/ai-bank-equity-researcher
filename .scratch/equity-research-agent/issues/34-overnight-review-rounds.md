# 34 — Overnight src/ review rounds (Sun night → Mon morning)

Type: task
Status: claimed (user-directed 2026-08-30 ~23:30)

## Directive

Run as many iteration cycles through the night as possible; a fully working
closed-loop agent by Monday morning. After the question-mode build lands:
code-review subagents over src/ ONLY — Claude reviewer subagents AND Codex
reviewers, alternating rounds. Keep going until the reviews STABILISE: no new
confirmed findings, or proposed fixes start being regressions. If Codex fails
(quota), report it in the morning — the user will upgrade the plan.

## Protocol per round

1. Two independent reviewers over src/bank_equity_researcher/ at the current
   commit: one fresh Claude subagent, one Codex session (pty launcher —
   background codex hangs without one; see the 2026-08-30 diagnosis).
2. Findings verified before fixing (a plausible finding is not a real one);
   confirmed fixes applied in a gated round (tests green, no tolerance
   loosening, leakage scan); suite spot-check on 3 cases.
3. Stop condition: a round with zero new confirmed findings, or fixes that
   regress the suite. Log each round's findings/outcomes below.

## Round log

(appended as rounds complete)

## Round 1 (2026-08-30, Claude reviewer A + Codex reviewer)

Reviewers: one fresh Claude subagent, one Codex session, both over `src/` at
commit 4440927. 18 merged findings. Every finding was verified before any fix;
the four Codex items that arrived without a repro got one each, from
independent read-only agents.

Result: 17 fixed, 1 part-deferred. No finding was refuted. No tolerance or cap
was loosened; the round tightened 4 checks and widened 1.

### Per item

| # | Finding | Verdict | Evidence |
|---|---|---|---|
| 0 | Weak citation: the evidence gate asks whether a citation RESOLVES, never whether it SUPPORTS | fixed | Root cause found: the `computed_delta_cap_80` existed but sat behind `if is_bridge:`. Impairment is `note_decomposition`, so it never ran — which is exactly how `cba-impairment-fy26-vs-fy25-agentic-cheap` shipped +150/-17/-71 $m at confidence 85 citing two chart reads whose only numbers were 6.2, -5.6, 0.0, -8.5, -1.4. Now `validate.cap_weakly_cited_claims`, called by BOTH shells, all methods. |
| 1 | `reconcile_tolerance` unit-blind | fixed | Shipped proof replayed: `cba-cti-fy26-vs-fy25-cheap` drivers sum 0.0 ppt vs delta -0.2 ppt, passed at the flat 1.0. Now `RECONCILE_TOL` per unit; presentation lift restricted to bps. |
| 2 | `walk_sum_tolerance` bps-calibrated for every unit | fixed | A ppt walk could not fail its own sum check. `check_walk` now takes the metric unit; both shells pass it. |
| 3 | `values_match` sign rule is dead code | confirmed, fixed | The rule was gated on `abs(target) > tol`, which only opens where the distance check already fails. 500k random pairs: removing the whole guard changed 0 answers. Two LIVE dev gold targets sit in the hole (`cba-1h26.json` lines 55 and 107): CBA 1H26 impairment moved -1 $m and an answer of +9 $m scored correct. |
| 4 | `crossref_passes` lets a unanimous FAIL use the flagged allowance | confirmed, fixed | Documented intent (`evals.py:230`, `judge.py:60`, ticket 29) is that the allowance covers a fact the judges could not SETTLE. Repro: 3 passes + 1 unanimous fail scored 0.75 and passed. Now `failed == 0` AND flags inside the allowance. Thresholds themselves remain pending user ratification — only the fail-vs-flag distinction changed. |
| 5 | `extract_walk` stamps `unit="bps"` on every walk NumberFact | fixed | `unit=unit`. Replayed: 4 saved artifacts carry mislabelled walk numbers; `check_component_columns` verdicts are unchanged on all of them (the bar labels carry no period token, so they never entered the stem pool either way). The fix corrects the stored unit and the artifact a reader sees; it un-skipped no check on the saved set. |
| 6 | Judge drops quotes past the character budget silently | fixed | `_fit_quotes` keeps whole quotes only, and `quotes_used` now counts what the judge read. New `quotes_truncated` flag on the Verdict and in the summary. |
| 7 | `quote_key` rejects a faithful row quote when footnote markers interleave | fixed | Repro on the real page: CBA FY26 PA p2 "Revenue from ordinary activities 2 3 30,153" — strict False, relaxed True. Markers come off the PAGE only, never the quote, so a quote may OMIT a marker but never STATE a number the page lacks. Recorded on the record's provenance. The gate was duplicated in `_mint_record` and `_resolve_evidence`; both now call one `match_quote`. |
| 8 | Agent's `read_chart` never reads the annotation layer the pipeline reads | fixed | The two shells were not evidence-comparable. `read_chart` now calls `extract_walk_annotations` and returns the callouts. |
| 9 | Question mode hardcodes `$m` for every chart | fixed | `question_scope` declared `"unit": "$m"`, so a margin walk read during a question came back stamped as dollars. Now the unit is empty, and `read_chart` asks the agent to name it rather than assuming one. |
| 10 | Tool calls after an accepted submit still execute | confirmed, fixed | Demonstrated both directions offline: `[submit, cite]` turned a dangling citation the gate had stripped into a quantified 85-confidence claim backed by a quote about another topic; `[submit, read_chart]` dropped a good answer from 85 to 40. `[cite, submit]` behaved correctly, so the artifact depended on call ORDER. Every call is still answered; none after acceptance runs. |
| 11 | Budgets checked between turns only; turn cap misreported as wall clock | confirmed, fixed | Measured overshoot: 25 tool calls against a budget of 2. Budget now binds before each dispatched call. The turn cap reports itself, and names the budget that latched first. (The misreport was real in source but unreachable in practice — no saved artifact shows it.) |
| 12 | `fetch_more` evidence lost on the author retry | confirmed, fixed | Offline repro: attempt 2 saw none of attempt 1's fetched records AND could not refetch, because `candidates` is never reset. One line — `records.extend(extra)` — which also fixes the citation cap misjudging a driver that cites a fetched record. |
| 13 | `banks_named` cannot recognise "National Australia Bank" | fixed | Every word of NAB's full name is generic, so the distinctive-word index held nothing and a valid question raised RuntimeError. Full names are now matched as PHRASES, read from the registry — no bank named in code. |
| 14 | `documents_for_question` substitutes a period silently | fixed | The function now records "the corpus holds no X document for FY26; researched in FY25 instead", and both shells put it in limitations. |
| 15 | `resolve_doc_name` accepts a bank-less fuzzy match | fixed | "results-book" resolved to whichever bank filed one. The containment pass now needs the written name to agree on bank AND period. |
| 16 | Question gate strips facts but leaves the numbers in the prose | fixed | The per-fact strip note already existed; what was missing was that the PROSE is not rewritten. One added limitation names the stripped claims and says the prose may still state them. |
| 17 | Cache keyed by filename stem | part-deferred | Collision REFUTED in practice: all 32 manifest stems are distinct. Staleness CONFIRMED: both caches test only `exists()`, so a PDF replaced in place serves old text for ever. Done now: the invariant is documented in `corpus.py`, and `all_documents()` raises on a duplicate stem instead of serving one bank's pages for another's. DEFERRED: the content-hash key. It is a two-line change, but any key change forces a full re-embed of 2476 pages, and the agentic-cheap dev suite was running in another process. Round 2. |

### New findings, not in this round's brief

- `cba-roe-fy26-vs-fy25-agentic-cheap` reports ROE moving 1350.0 -> 1400.0 "ppt".
  Those are basis points wearing a ppt label; an ROE level of 1350 ppt is not a
  ratio. It reconciles and passes movement arithmetic, so no check sees it. A
  unit-typed tolerance is only as good as the unit LABEL, and nothing validates
  that a ratio's level is ratio-sized. Candidate for round 2.
- `fetch_more` cannot reach any page retrieval already ranked but the page
  budget dropped (`candidates` holds it, so the guard skips it). Probably bites
  more often than the retry loss. Left alone: it has a cost implication and
  belongs in its own decision.
- The weak-citation cap matches on MAGNITUDE only, not unit, and one live case
  shows that is too weak. In the round-1 rerun of `cba-cti-1h26-vs-1h25-cheap`,
  the driver `notable_items +0.0 ppt` keeps confidence 90 because a cited
  record carries a NumberFact of `0.0 $m`. A zero in another unit grounds
  nothing, and a zero-valued claim is the easiest of all to ground by accident.
  The fix is to disqualify a cited number whose unit CONFLICTS with the claim's
  (treating "%" and "ppt" as one family, and an absent unit as no evidence
  either way). It was deliberately NOT applied in this round: the dev suite was
  already running against the round-1 code, and changing a cap mid-run would
  have made the scorecard describe code that no longer existed. Round 2, first
  item — item 5 has by then given the walk records their true units.
- Reviewer A's row-splice permissiveness in `quote_key` is acknowledged and NOT
  fixed blind, per the brief.
- `README.md:44` documents `uv run python scripts/fetch_corpus.py`, but
  `--manifest` is required, so the documented command fails.

### Verification

`uv run python -m pytest tests/ -q` — **308 passed** (246 before; +62). Every
fix carries a test. Red-then-green was confirmed by reverting the fix for items
3, 6, 7, 10, 11 and 12. `ruff check src/ tests/` holds at its pre-existing
29-finding baseline: the round adds none. The prompt-leakage scan over every
`*PROMPT*` string in `src/` finds no mention of gold, checklists, judges or the
scorecard (the one hit is the judge's own prompt describing its own job).

#### Replay over saved artifacts

11 artifacts change verdict. **Every change is a tightening; nothing loosened.**

- `drivers_reconcile` PASS -> FAIL on `cba-cti-fy26-vs-fy25-cheap` and
  `cba-cti-fy26-vs-fy25-agentic-cheap`. Both are ppt cases whose drivers sum to
  ~0.0 against a real movement of -0.2 ppt. They passed only because the slack
  was five times the movement.
- 20 claims across 9 artifacts newly capped to 80 by the weak-citation gate.
- 0 claims lost a cap. 0 `movement_arithmetic` verdicts changed.
- Item 5 (walk unit) changes no saved verdict: 4 artifacts carry mislabelled
  walk numbers, and `check_component_columns` is identical before and after on
  all of them, because those bar labels carry no period token and never entered
  the stem pool. The fix corrects the stored unit, and un-skipped no check.
- Item 4 changes no recorded answer-suite verdict. The hole was open but unused.

#### Cheap dev suite — `evals/results/20260830-1507-cheap-dev.md`, verbatim

- scored_claims: 42
- unscored_claims: 48
- cases_scored: 8
- cases: 25
- brier: 0.067
- confidently_wrong_rate: 0.03
- 70-84: 9 claims, 78% correct
- 85-94: 27 claims, 96% correct
- 95-100: 6 claims, 100% correct

Movements: 24 OK, 1 WRONG (WBC-roe-FY25).
Prior baseline `20260830-1247-cheap-dev.md`: brier 0.051, confidently_wrong 0.0,
24 OK / 1 WRONG (CBA-cet1-1H26).

**Both red numbers were investigated. Neither is a regression.**

1. `confidently_wrong 0.0 -> 0.03` is ONE claim:
   `CBA-cash_earnings-1H26 credit_impairment_charge`, claimed **-1.0 $m**
   against gold **+1 $m**, at confidence 85. The model shipped the sign the
   wrong way round this run. The OLD harness scored that CORRECT — proven
   directly: `old_values_match(-1.0, 1.0, "$m")` returns True, because the sign
   rule was gated behind `abs(target) > tol` and 1 is inside the $10m money
   floor. So the rate did not get worse; the MEASUREMENT got honest, and it
   caught a real sign error on its first live outing. This is item 3 working.
   The brier move is the same one claim: excluding it, brier is 0.021.
2. `WBC-roe-FY25` movement red is model nondeterminism, not a code change. The
   run read `10.97 -> 10.89`, splicing the ex-Notables FY25 ROTE to the
   statutory FY25 ROTE as two endpoints. Its drivers reconcile to that movement
   with gap 0.0, so the tightened ppt tolerance never fired, and both drivers
   sit at confidence 75, below the cap. Re-run three times on the fixed code:
   **3/3 produce the correct gold movement 11.21 -> 10.97, delta -0.24.** The
   two other label flips between runs (`WBC other_operating_income` 144 -> 157,
   `WBC operating_expenses` -699 -> -972, one each way) are the same
   run-to-run variance.

So on this evidence the movements hold and the calibration is unchanged in
substance; one previously invisible sign error is now visible.

#### Anchor probe

`analyse --bank CBA --metric impairment --period FY26 --combo agentic-cheap`,
run after both dev suites finished. The agent path runs end to end with the
gate live: 30 tool calls, 14 pages, 112s, $0.0115, `budget_exhausted: no`. The
brief's own shipped defect is now caught:

```
collective.volume       +150 $m  conf=80  ['single_source', 'computed_delta_cap_80']
individual_provisions    -17 $m  conf=80  ['single_source', 'computed_delta_cap_80']
write_backs_recoveries   -71 $m  conf=80  ['single_source', 'computed_delta_cap_80']
```

with the limitation "Capped at 80: ... The records these claims cite do not
state those numbers, so each one is arithmetic over the evidence rather than a
figure read from it." Those three shipped at confidence 85 before.

#### Pre-fix agentic-cheap baseline

`evals/results/20260830-1456-agentic-cheap-dev.md` was produced by the
concurrent run, which imported its code before this round's first edit, so it
is a clean PRE-fix agentic baseline: brier 0.052, confidently_wrong 0.03,
85-94 band 32 claims at 97%, and `CBA-impairment-FY26` shipping at confidence
85. It was not re-run; the anchor probe above is the post-fix spot check.

### Left undone

- Item 17's content-hash cache key (reason recorded above).
- The unit-blind weak-citation match (see new findings).
- The round-2 candidates listed under "New findings".
- Nothing was committed, per the brief.
