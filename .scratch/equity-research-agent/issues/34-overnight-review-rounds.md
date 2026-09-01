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

## Round 2 (2026-08-31, Claude reviewer B + Codex reviewer)

Reviewers: one fresh Claude subagent and one Codex session, both read-only over
`src/` at commit 2177917. Reviewer B filed 12 findings, each with an executed
repro; Codex filed 8. The two lists overlap, and the merged list is 15 items.
Where they disagreed, B's repro'd design won.

Result: 15 fixed, 0 refuted, 0 deferred. No tolerance and no cap was loosened.
The round tightened five checks, added two, and moved three helpers into one
place so both shells share them.

Two items are fixes of ROUND-1 code (B1 and B6). Both got a red test first: the
round-2 assertions were executed against the round-1 implementation, where they
fail.

### Per item

| # | Finding | Verdict | Evidence |
|---|---|---|---|
| B1 | HIGH — `_quote_numbers` reads a PREFIX of any number with a glued unit suffix (round-1 code) | fixed | Pre-fix, B's repro re-executed: `"cash NPAT of $10,982m"` -> `[10.0]`, `"fell 5bps"` -> `[]`, `"$2.5bn buyback"` -> `[2.0]`, `"(-3bps)"` -> `[]`, `"(CET1 impact of -13bpts)"` -> `[]`. Both directions of the citation cap inverted on one record: the driver whose number the quote printed was capped, and a neighbour claiming +10 was certified by the digit prefix. 163 of 2042 shipped quotes (8.0%) glue a digit to a letter. The pattern now consumes the suffix and RETURNS it as the number's unit, which feeds B3, and it drops a bare four-digit year. Spelled-out money units ("$1 million", "$1,002.9 billion") are read the same way. |
| B2 | HIGH — a fatal check caps the attribution and never the drivers | fixed | The calibration metrics read PER-DRIVER confidence, so every failed check was invisible to them. New `validate.cap_unreconciled_drivers`, called by both shells inside `if fatal:`. Replayed over the saved set: 9 quantified drivers across 4 artifacts fall from 85-90 to 80, including `cba-cash_earnings-1h26-vs-1h25-cheap credit_impairment_charge -1.0` at 85 — the suite's only confidently-wrong claim, now below CONFIDENT_THRESHOLD. |
| B3 / Codex 4 | PRE-SEEDED (a) — the citation cap matches magnitude only, never unit | fixed | B's conversion table, applied to the NumberFact branch and, after B1, to the quote branch. Replayed over all 65 artifacts with walk facts carrying the metric unit (as extraction has stamped since round-1 item 5): **exactly one** verdict change — `cba-cti-1h26-vs-1h25-cheap notable_items +0.0 ppt` 90 -> 80, the live case both reviewers named, where a `0.0 $m` cell grounded a percentage-point claim. The strict and lenient readings of the quote branch were measured against each other and cap the same 16 claims, so the strict reading costs nothing. |
| B4 / Codex 2 | PRE-SEEDED (b) + priority 3 — nothing validates that a ratio's LEVEL is ratio-sized | fixed | B's measured design, unchanged: `check_ratio_level` with `RATIO_LEVEL_CEILING = 200.0`, plus `settle_ratio_scale`, the mirror of the percent-to-bps lift. Replayed over all 65 artifacts: the check fires on the two known bps-as-ppt artifacts (`cba-roe-fy26` at 1400 ppt, `nab-roe-fy25` at 1160 ppt) and **on nothing else**; the largest legitimate level in the set is a WBC cost-to-income ratio of 53.04. The corrector fires once and turns `1160 -> 1140` into `11.6 -> 11.4, delta -0.2`, which is the gold movement. Confirmed live (see the probe below). |
| B5 / Codex 3 | PRE-SEEDED (c) — the `credit_impairment_charge -1.0` sign flip | fixed | Diagnosis confirmed: none of the three suspected normalisers touched it. CBA's 1H26 charge FELL $1m, which ADDS $1m to earnings, and nothing converts a cost line's own movement into its effect on the total. Two parts, as B specified: B2's cap removes the confidently-wrong claim, and `sign_flip_hint` gives the retry a QUESTION. Replayed over the non-reconciling artifacts: unique on `cba-cash_earnings-1h26-vs-1h25-cheap`, naming `credit_impairment_charge (-1 $m)`; ambiguous (two candidates) on `cba-cti-fy26-vs-fy25-agentic-cheap`; silent on the other nine. It names no gold value and corrects nothing. |
| B6 / Codex 7 | MED-HIGH — `strip_markers` removes far more than footnote markers (round-1 code) | fixed | Pre-fix measurement reproduced exactly: over the 607 pages of CBA FY26 and 1H26 the pattern removed 10,158 tokens, 16.7 a page, with 324 pages losing ten or more. Three quotes were accepted as verbatim that must not be, including "Additional Tier and Tier Capital" against a page reading "Additional Tier 1 and Tier 2 Capital". The pattern now matches the SHAPE of a marker — a one- or two-digit run between a letter and a value — plus superscripts, which are never data. After: 198 digit tokens, 0.33 a page, 2 pages losing ten or more, and 519 superscript runs. The round-1 repro still passes and the three quotes are now rejected. |
| Codex 1 | HIGH — model-supplied NumberFacts on `cite` records are never verified | fixed | An agent could quote an unrelated verbatim sentence, attach `{"value": 150, "unit": "$m"}`, and every check that reads `record.numbers` would read a number no page prints. `_mint_record` now keeps only facts the verified quote prints, and `cite` reports each drop so the agent can re-cite. |
| B9 | MED — the agent's `cite` makes `numbers` optional, so the column checks go silent | fixed | Census over the saved artifacts: the pipeline carries 2.45 NumberFacts a record, the agent 0.54, and SEVEN agentic artifacts hold zero — `check_component_columns`, `check_movement_columns` and `_percent_evidenced` are all inert there. `numbers` is now required, with one generic line in the shared HOW_TO_RESEARCH block. An empty list stays valid for a prose quote. |
| B7 | MED — the reconciliation SUM is unit-blind, and the scorer uses the gold unit | fixed | Repro: `movement 5132 -> 5445 $m` with `nii +310 $m` and `mix +3 bps` passed. The sum now takes only same-unit contributions and names a `drivers_unit_mismatch`. The off-unit guard the agent shell already had moved into `author.drop_off_unit_contributions`, and both shells call it. `score_drivers` labels a claim in a conflicting unit INCORRECT; a claim with NO unit keeps the old behaviour, because absence of evidence is not a mismatch. Live: 0 off-unit contributions across the saved set, so this is a latent hole, not a shipped defect. |
| B8 | MED — the delta harmonisers keep a flat 0.51 that `check_movement` no longer uses | fixed | Repro: `45.0 -> 46.0 ppt, delta 1.5` — the harmoniser did not fire (gap 0.5 against 0.51) and `check_movement` then failed at 0.1 ppt, so a repairable one-line slip sank the answer to 40. Both harmonisers now read `movement_arithmetic_tolerance(unit)`. |
| Codex 8 | MED — the agent loses annotation evidence when the walk read fails | fixed | The pipeline attempts the callout layer whatever the walk read did; `Research.read_chart` returned early. It now reads the annotations with empty bar labels and returns them beside the error. |
| B10 | MED-LOW — the period-substitution note reaches the reader and never the model | fixed | Both question shells added the note AFTER the answer existed, so the model was asked about FY26, handed FY25 documents, and told nothing. `ANSWER_PROMPT` and `QUESTION_PROMPT` now carry it. |
| B11 | LOW — `extract_walk`'s endpoint harmoniser is bps-calibrated | fixed | The two `10` literals are now `walk_sum_tolerance(doc_type, unit)`. For a ppt walk the old trigger was unreachable, so the harmoniser was dead code there; for a $m walk it accepted a residual of ten dollars-million as "the walk sums". Replayed over all 51 saved walk records: the new trigger opens on 6 of them, and **no scale factor closes any of them**, so the harmoniser's OUTCOME is unchanged everywhere. This closes a latent hole and moves nothing live. |
| B12 / Codex 5 | LOW — the per-call budget binds tool calls and time, but not cost | fixed | One `read_chart` costs TWO vision calls and counts as one tool call, so a turn carrying five chart reads issued ten vision calls with no cost check between them. The cost ceiling joins the per-call stop ladder. |
| Codex 6 | MED — the tolerance tables use raw, case-sensitive unit strings | fixed | `unit="PPT"` took the default reconciliation tolerance 1.0 instead of 0.1. `UNIT_ALIASES` and `normalize_unit` moved from `evals.py` into `validate.py`, beside the tolerances they key, and `evals` imports them (the reverse import is a cycle). Every tolerance lookup in `validate.py` canonicalises first. `bpts`, `$bn`, `$b`, `cents` and `ratio` joined the table — the saved set uses all five. Live: every unit string in the saved set is already canonical, so this too is latent. |

### Verification

`uv run python -m pytest tests/ -q` — **369 passed** (308 before; +61). Every
fix carries a test. The two fix-of-fix items were shown RED first by executing
the round-2 assertions against the round-1 implementation: `_quote_numbers`
returns the prefix on all five repro strings, and `match_quote` accepts all
three quotes that delete real data.

`ruff check src/ tests/` holds at its 29-finding baseline; the round adds none.
The prompt-leakage scan over every `*PROMPT*` string finds no mention of gold,
checklists or the scorecard. The two new retry keys (`ratio_scale` and
`check_this_contribution_sign`) name arithmetic and a driver's own canonical
id, never a value to reach.

#### Replay over saved artifacts

Every tightened check was replayed over all `out/*/attribution.json` before and
after. **Every change is a tightening; nothing loosened.**

- `check_ratio_level` fires on exactly TWO artifacts, both known bps-as-ppt
  reads. The largest legitimate ratio level in the whole set is 53.04, so the
  200.0 ceiling has 3.8x headroom above real data.
- `settle_ratio_scale` fires on exactly ONE artifact and produces the gold
  movement.
- The citation cap changes exactly ONE verdict: `cba-cti-1h26` `notable_items
  +0.0 ppt`, capped at 80. Three older artifacts also change, and all three
  trace to walk NumberFacts stamped `bps` before round-1 item 5 gave walks
  their true unit; with the units corrected, those changes disappear.
- `check_component_columns` and `check_movement_columns` are byte-identical
  over every saved artifact, so the unit canonicalisation silenced nothing.
- `check_movement` and `drivers_reconcile` verdicts are unchanged everywhere.
- The walk endpoint harmoniser's outcome is unchanged on all 51 walk records.

#### Cheap dev suite — `evals/results/20260830-1638-cheap-dev.md`, verbatim

- scored_claims: 42
- unscored_claims: 48
- cases_scored: 8
- cases: 25
- brier: 0.05
- confidently_wrong_rate: 0.0
- 70-84: 10 claims, 80% correct
- 85-94: 29 claims, 100% correct
- 95-100: 3 claims, 100% correct

Movements: 24 OK, 1 WRONG (CBA-cet1-1H26).

Against round 1 (`20260830-1507-cheap-dev.md`): brier 0.067 -> **0.050**,
confidently_wrong 0.03 -> **0.0**, and the 85+ band goes from 33 claims with
one wrong to 32 claims with none. Against the frozen baseline
(`baseline-20260829-devonly.md`, brier 0.058, confidently_wrong 0.0) the round
is better on both. The confidently-wrong claim is gone for two independent
reasons: this run shipped `credit_impairment_charge +1 $m`, which is the gold
value and reconciles the bridge exactly, and B2's cap would have removed it had
it shipped wrong again.

#### The one movement miss, investigated

`CBA-cet1-1H26` read 15.30 -> 15.10 bps from a capital table instead of the
CET1 row's 12.20 -> 12.30. The drivers were left unquantified, so it shipped at
40 with `no_quantified_drivers` — an honest partial, not a confident error.

This case has flipped before: it was WRONG in the pre-round-1 baseline
(`20260830-1247`) and OK in round 1. It was re-run four more times on the round-2
code — **WRONG, OK, OK, OK** — and twice on the round-1 code as a control —
**OK, OK**. So the round-2 arm is 3 of 5 and the round-1 arm 4 of 5, which the
sample cannot separate.

The round cannot reach this case. Every new function is inert for a bps
movement with no quantified drivers: `check_ratio_level` and
`settle_ratio_scale` return nothing for `bps`, `sign_flip_hint` needs a
quantified contribution, and `check_drivers_reconcile` returns the identical
`no_quantified_drivers`. The only change that CAN touch a bps walk is B11, and
its outcome is unchanged on all 51 saved walk records. The author therefore
sees the same prompt it saw in round 1, and the flip is model nondeterminism on
a page that prints several capital ratios one under another.

#### Agentic probe — NAB ROE FY25 vs FY24, `agentic-cheap`

The case reviewer B diagnosed as priority 3. The agent again submitted
`1160.0 -> 1140.0 ppt`; the corrector chain now repairs it end to end:

```
movement: 11.6 -> 11.4 ppt, delta -0.2      (gold: 11.6 -> 11.4, delta -0.2)
movement_source: row 'Cash return on equity', column Year to Sep 24 -> Year to Sep 25
attribution_confidence: 40      drivers: earnings_effect -1.8, equity_effect -0.2, both at 80
limitations: "Movement delta normalised from -2.0 to -20 (unit slip against the endpoints)."
             "Movement endpoints converted from basis points (1160, 1140) to ppt ..."
             "Failed check: drivers_reconcile (drivers -2.0 + residual +0.0 != delta -0.2, tol 0.1)"
42 tool calls, 14 pages, 232s, $0.0298, budget_exhausted: no
```

The movement is now right where it was 100x wrong. The identity split is still
wrong, and the run says so instead of hiding it: the drivers do not reconcile
against the corrected delta, the answer is capped at 40, and the drivers sit at
80. Before this round the same submission reconciled at the wrong scale and
nothing fired.

### Left undone

- Item 17's content-hash cache key, still deferred from round 1.
- `fetch_more` cannot reach a page retrieval ranked but the page budget
  dropped (round-1 note; it has a cost implication and needs its own decision).
- The ROE identity split itself. The scale is now correct and the checks catch
  the residual error, but no code derives the split.
- Nothing was committed, per the brief.

## Round 3 (2026-08-31, Claude reviewer C + Codex reviewer) — the convergence round

Reviewers: one fresh Claude subagent and one Codex session, both read-only over
`src/` at commit d84a2f7. Reviewer C filed 6 findings with executed repros and
a clean cap-stack trace; Codex filed 5. The two lists overlap heavily, and the
merged list is 6 items. Where they disagreed, C's design won.

The finding count converges: 18 -> 15 -> 6. Every round-3 item refines a
round-1 or round-2 fix; none opens new ground.

Result: 6 fixed, 0 refuted, 1 partly deferred (item 3, step 2). No tolerance
and no cap was loosened. Three items got a red test first, using the reviewers'
repros verbatim.

### Per item

| # | Finding | Verdict | Evidence |
|---|---|---|---|
| C1 + C5 / Codex 2 | HIGH — `quote_prints` verifies a NumberFact's VALUE and never its UNIT, and `_FAMILY_WORDS["ppt"]` holds the token `"pt"` | fixed | One change, because C1's repro needs C5's suffix table. Pre-fix, both repros re-executed: `quote_prints("Net interest margin decreased 5 basis points to 2.03 per cent.", 5, "$m")` -> `True`, so `_mint_record` kept `{"value": 5, "unit": "$m"}` and a `+5 $m` driver stayed at 95; `quote_prints("NPAT was $150m", 150, "bps")` -> `True`. `_quote_numbers("Movements in bpts Credit Risk (34)")` -> `[(34.0, "")]` and `quote_states(34.0, "ppt")` -> `True`, which is 100x wrong, while the correct `0.34 ppt` was refused. Three parts: the number pool now reads the SPELLED-OUT ratio units (`basis point(s)`, `bpt(s)`, `percentage point(s)`, `per cent`); `quote_prints` accepts a number carrying a glued unit only through `convert_unit`, and keeps the bare-number branch untouched; `_FAMILY_WORDS` matches on WORD BOUNDARIES with `"pt"` and `"cent"` removed. Family-word census over all 2,034 shipped quotes: ppt/% hits 795 -> 732, bps 415 -> 373, cents 37 -> 9, `$m` unchanged; of the 35 quotes that name `bps` and print no `%`, 35 passed the ppt family test before and 2 do now. |
| C2 | HIGH — `settle_ratio_scale` reverses the percent-to-bps lift | fixed | C's repro re-executed: a CET1 movement the model labelled `"%"` was lifted `12.20 -> 1220` by the bps lift, and the corrector — keyed on the model's own label — divided it straight back to `12.2 -> 12.3, delta 0.1`. `check_movement` and `check_ratio_level` both PASSED, so the artifact shipped `+0.1 %` against a gold of `+10 bps` under two limitations that contradicted each other. The gate is now the METRIC's unit, which the taxonomy fixes; both call sites already held `metric_cfg["unit"]`. After: the corrector stays silent and `check_ratio_level` FIRES `movement_level_not_ratio_sized (1230 %)`, so the answer is capped at 40 with its drivers at 80 instead of shipping a silent 100x error. |
| C6 / Codex 1 | MED — `cap_unreconciled_drivers` covers two fatal names out of eight | fixed | Three parts, on one rule: a check that CAN name its offender caps the offender, and a check that cannot condemns the table. `check_comparison_leak` and `check_component_columns` both print the offending driver, so each now caps that driver at `CLAIM_CITATION_CAP` in place and records `comparison_leak_cap_80` / `component_column_cap_80`. `movement_arithmetic` and `drivers_unit_mismatch` join `WHOLE_TABLE_FAILURES`: a movement whose own three numbers disagree is the movement the whole table was written against, and a contribution dropped from the sum for its unit means the bridge that closed was never closed. `walk_sum` is deliberately NOT in the list — see below. |
| C4 / Codex 5 | MED-HIGH — an off-unit RESIDUAL is named as a mismatch and then added to the sum | fixed | C's repro re-executed: `movement 5132 -> 5445 $m`, `nii +310 $m`, `residual +3 bps` returned `drivers_reconcile` PASS beside its own `drivers_unit_mismatch` FAIL — three basis points closed a dollar bridge. The residual now joins the total only when its unit is empty or equal, which is the rule B7 already set for the contributions. `sign_flip_hint` carried the same unit-blind arithmetic, so an off-unit residual closed the gap it exists to measure; it now applies the same guard. |
| C3 / Codex 3 | MED-HIGH — the narrowed `strip_markers` still deletes real table data | fixed (step 1); step 2 deferred | C's repro re-executed on ANZ 1H26 results announcement p59: `match_quote("Credit and Capital Markets 102 114", page)` -> `(True, markers_stripped)`, dropping the current-period value 80 and presenting 102 as the first column. The run of digits must now sit on the LABEL'S OWN LINE (`[ \t]+` in place of `\s+` inside the run; the lookahead keeps `\s+`, so the value may wrap). Corpus census over all 30 documents and 3,546 pages reproduces C's numbers exactly: **1,670 tokens -> 779**, and the newline-crossing class (891 tokens) goes to zero. The round-1 footnote repro still passes and the ANZ quote is now rejected. Replayed over every shipped quote in `out/`: 0 quotes that matched before fail now, and 0 that failed match now. |
| Codex 4 | MED — the cost ceiling is not enforced between a chart's two vision calls | fixed | Codex's repro re-executed: a $0.50 ceiling admitted two $0.60 vision calls and ended at $1.20, because the loop's per-call check binds the PAIR and neither call inside it. `Research._read_annotations` now re-reads the ceiling and returns no callouts when the run is over it. After: the annotation read is skipped and the run ends at $0.60. The walk read is what the caller asked for, so the callout layer is the half that gives way. |
| Codex 2 (second half) | HIGH — the open-loop extractor accepts NumberFacts without validating them against their quote | fixed | `extract_text_evidence` now keeps only the facts its quote prints, from the same `quote_prints` the agent's `_mint_record` uses, so a fact means the same thing whichever shell assembled it. Measured, not rewritten (see the replay below). |

### The walk_sum decision, and why it is not a whole-table failure

The brief asked for reasoning rather than a blanket rule. A failed `walk_sum`
says the bars a vision call read off a slide do not sum to that slide's own
endpoints. That indicts the CHART READ. It does not say the driver table is
wrong, because a driver may be grounded in a table or in prose the chart never
touched.

The saved set settles it, and it settles it BOTH ways:

- `wbc-cet1-fy25-vs-fy24-cheap` — all five drivers cite `ev-1`, the walk record
  whose bars sum to 1225 against that chart's own end of 1253. Every one of
  them shipped at 85. A whole-table cap would be right here.
- `cba-nim-fy26-vs-fy25-agentic-cheap` — one driver of seven (`liquids -3 bps`)
  cites the broken walk `ev-2`; the other six cite text records. A whole-table
  cap would lower six claims the chart never touched.

So the rule is the one `check_comparison_leak` already follows: a check that
can NAME its offender caps the offender. A walk carries `record_id`, and a
driver names the records it cites, so the drivers resting on a
self-contradicting chart read are exactly nameable. New
`validate.cap_drivers_on_failed_walks`, called by both shells. It runs whether
or not the failure was graded load-bearing for the ANSWER: that grading asks
whether the walk carries the whole attribution, this asks whether it carries
THIS claim.

`walk_extraction_error` stays out of every cap. An unreadable chart is a
coverage gap, not a contradiction; `anz-nim-1h26-vs-1h25-cheap` carries one and
its seven drivers are already at 85 under the no-primary-walk rule, which is
the rule that fits.

### Two changes the round found while verifying its own fixes

1. **The citation tolerance was relaxed by every unit conversion.**
   `CITATION_TOL["ppt"]` is 0.1, which is TEN BASIS POINTS, and the slack was
   taken from the CLAIM's unit alone. Once C1's fix taught the pool to read
   "increased 10 basis points", that sentence grounded a component claim of
   `+0.08 ppt` AND one of `+0.02 ppt` at once — the whole movement fitted
   inside the slack. Read the other way, a `$2.5bn` quote carried $500m of
   slack against a `$m` claim. New `_converted_prints` takes the TIGHTER of the
   two units' own slack, both read in the claim's unit. This was reachable
   before this round through the glued-`bps` path; the round did not create it,
   it made it visible.
2. **A bracketed negative lost its glued unit.** A bank writes
   `Net interest margin (%) 2.05 2.08 (3)bpts`, and the closing bracket stood
   between the number and its unit, so 73 of the 2,034 shipped quotes put a
   UNITLESS number in the pool where the page had named its unit. The pattern
   now steps over the bracket.

### Verification

`uv run python -m pytest tests/ -q` — **402 passed** (369 before; +33). Three
items were shown RED first by executing the reviewers' repros against the
round-2 implementation: `quote_prints` accepts the dollar fact off a
basis-point sentence, `settle_ratio_scale` divides the lift back out, and the
off-unit residual closes the bridge.

`ruff check src/ tests/` is byte-identical to its 29-finding baseline. The
prompt-leakage scan over every `*PROMPT*` string finds no mention of gold,
checklists or the scorecard.

#### Replay over saved artifacts — the deterministic layer

All 65 saved `out/*/attribution.json` were replayed under the round-2 tree (a
worktree at 8d5569d) and the round-3 tree, and the two blobs diffed.

`check_movement`, `check_ratio_level`, `check_drivers_reconcile`,
`sign_flip_hint`, `settle_ratio_scale`, `cap_weakly_cited_claims` and
`cap_unreconciled_drivers` return the IDENTICAL verdict on all 65. The round
changes no shipped verdict. Two things move, and both move one way:

- **Grounding: 2 changes, both tightenings, 0 loosenings.**
  `wbc-roe-fy25-vs-fy24-cheap` and `wbc-roe-fy25-vs-fy24-agentic-cheap` both
  claimed `earnings_effect -0.26 ppt` citing `ROTE 10.97% 11.21% (24 bps)`.
  The old slack read 24 bps as 0.24 ppt against a 0.1 ppt tolerance — TEN basis
  points — so a ROTE change certified an ROE earnings COMPONENT. Both are now
  ungrounded. (Both drivers were already at 80, so no confidence moves.)
- **`cap_drivers_on_failed_walks` fires on exactly the two artifacts the
  reasoning above predicts**: `cba-nim-fy26-vs-fy25-agentic-cheap` caps
  `liquids -3 bps` and leaves the six prose-grounded drivers alone;
  `wbc-cet1-fy25-vs-fy24-cheap` caps all five.

C6's three named artifacts, before -> after:

| artifact | failure | before | after |
|---|---|---|---|
| `anz-nim-1h26-vs-1h25-cheap` | `walk_extraction_error` | attr 40, 7 drivers at 85 | unchanged — an unreadable chart is a coverage gap, and the no-primary-walk rule already put those drivers at 85 |
| `cba-nim-fy26-vs-fy25-agentic-cheap` | `walk_sum` | attr 85, drivers at 85/90 | `liquids -3 bps` 85 -> 80; the six drivers citing text records keep 85-90 |
| `wbc-cet1-fy25-vs-fy24-cheap` | `walk_sum` | attr 40, 5 drivers at 85 | all five -> 80; every one of them cites `ev-1`, the walk that misses its own endpoint by 28 bps |

The `comparison_leak` artifact C named, `cba-cet1-fy21-vs-fy20-cheap`, has its
drivers at 80 already, so the new in-place cap is reachable rather than
shipped there. It DOES fire in the fresh suite run below, beside a new
`component_column_cap_80` on `cba-cash_earnings-1h26-vs-1h25-cheap`.

Marker relaxation, replayed over every shipped quote against its own page: **0
quotes that matched before fail now, and 0 that failed match now.** No saved
record carries the relaxation at all, so the narrowing costs nothing live.

#### The extractor NumberFact gate — measured, then narrowed

`quote_prints` applied at full strength to `extract_text_evidence` fails **660
of 3,552** shipped non-chart facts (18.6%): 411 sit under a quote that prints
NO number, 247 name a magnitude the quote does not print, and 2 conflict on
unit. Every sample inspected is genuinely derived or invented — "Loan
impairment expense was $554 million, a decrease of $1,964 million" carrying a
fact of 2,518; "Staff expenses increased by 3% to $3,211 million" carrying 96.

Applied at full strength it also destroyed a case. The first suite run
(`20260830-1758-cheap-dev.md`) lost WBC-roe-FY25 outright: all six of its
records quoted a row LABEL ("ROTE", "Average ordinary equity ($m)") with the
values in `numbers`, every value was dropped, and the author reported "the
movement could not be established". Brier 0.156.

So the gate is narrowed by one condition, and the condition is principled: a
quote that prints NO number says nothing about the numbers beside it, and
absence of evidence is not a conflict. A quote that DOES print numbers is the
model quoting the row, and a fact that row does not carry is contradicted by
its own evidence. That drops **249 of 3,552 (7.0%)** and keeps every
unit-conflict and every derived figure in the samples above. The agent shell
keeps the strict gate, because there the quote is verified against the page
first and every drop is handed back to the model to re-quote.

#### Cheap dev suite — `evals/results/20260830-1906-cheap-dev.md`, verbatim

- scored_claims: 42
- unscored_claims: 48
- cases_scored: 8
- cases: 25
- brier: 0.066
- confidently_wrong_rate: 0.0
- 70-84: 10 claims, 70% correct
- 85-94: 32 claims, 100% correct

Movements: 23 OK, 2 WRONG (CBA-cet1-1H26, WBC-roe-FY25).

Three runs were needed, and all three are reported:

| run | gate | brier | confidently wrong | movements |
|---|---|---|---|---|
| `20260830-1758` | strict extractor gate | 0.156 | 0.0 | 23 OK, 2 WRONG |
| `20260830-1833` | narrowed gate | 0.077 | 0.0 | 24 OK, 1 WRONG, 1 crash |
| `20260830-1906` | narrowed gate | 0.066 | 0.0 | 23 OK, 2 WRONG |

Against round 2 (`20260830-1638`, brier 0.050) and the frozen baseline
(`baseline-20260829-devonly.md`, brier 0.058) the round is worse on brier and
level on the invariant that matters:

- **`confidently_wrong_rate` is 0.0 in all three runs.**
- **Every incorrect claim in all three runs sits at exactly 80**, the evidence
  ladder's ceiling. The 85-94 band is 100% correct in every run.

The brier moves with the COUNT of wrong claims, and that count is model
variance in the values, not a cap misfiring. The wrong claims are: CBA 1H26
`operating_expenses -348` against a gold of -518 (in every run, including
round 2); WBC FY25 `operating_expenses -672` against -972; NAB FY25
`credit_impairment_charge +0` against -105. All three are the
underlying/notable expense split and the impairment sign — known open items,
not this round's code. Round 2's run held two such claims and this one holds
three.

#### The two movement misses, and one crash

- `CBA-cet1-1H26` — the known flake, now 4 of 8 across the recorded history
  (round-2's log has it at 3 of 5). It was OK in the 1833 run and WRONG in the
  1906 run on identical code. It ships at 40 with `no_quantified_drivers`, so
  it is an honest partial, not a confident error.
- `WBC-roe-FY25` — WRONG in both round-3 runs and OK in round 2. The 1906 run
  read the RIGHT row (`ROTE ex Notable Items`, printed "10.97% 11.21%") and
  took the columns in the printed order, submitting `10.97 -> 10.89` against a
  gold of `11.21 -> 10.97`. `drivers_reconcile` failed and the answer shipped
  at 40. This is a column-order read on a row that prints FY25 first, and the
  checks caught it.
- `WBC-impairment-FY25` crashed in the 1833 run only: the author's reply left
  `confidence` off driver 0, and `DriverClaim.confidence` has no default, so
  `Attribution(**reply)` raised. The suite scores a crashed case as a failure,
  which is honest, but a required int with no default is a brittle contract
  against a model reply. Filed below as a finding for the next round; it did
  not recur in the 1906 run.

### Left undone

- **`strip_markers` step 2**, per C's own bound. The remaining 779 tokens are
  digits inside a LABEL, and the proposed fix is to read the page's own
  numbered footnote block and strip only an index the page defines. Measured
  composition of the 779: **47% are the digits 1-3**, which is exactly the set
  a footnote block defines, so the rule would still delete "stage 2", "Peer 1"
  and "Tier 1" — the risky half. It would protect the year columns ("Mar 26",
  "25", "22", 127 tokens). That is not enough return for a page-shape parser,
  so it stays the documented residual limitation.
- **`DriverClaim.confidence` has no default**, so one missing field in an
  author reply crashes the whole case (seen once in the 1833 run). Either the
  author reply is normalised before construction, or the field takes an
  explicitly-low default. Needs its own decision.
- Item 17's content-hash cache key, still deferred from rounds 1 and 2.
- `fetch_more` cannot reach a page retrieval ranked but the page budget
  dropped.
- The ROE identity split itself, and the underlying/notable expense framing,
  which supplies every wrong claim in every run of this round.
- Nothing was committed, per the brief.

## Round 4 (2026-08-31, Codex reviewer) — the unit-declaration round

Reviewer: one Codex session, read-only over `src/` at commit 5b4e890, with an
executed repro for every item. Four findings, all inside round-2 and round-3
fresh code. Three tighten a unit test; the fourth repairs a round-3
overcorrection and is the only one with a LIVE footprint in the saved set.

The finding count converges: 18 -> 15 -> 6 -> 4.

Result: 4 fixed, 0 refuted. Every item was shown RED first by executing the
reviewer's own repro against the round-3 tree.

**Live suite deferred: credits exhausted.** OpenRouter credits ran out during
the overnight head-to-head (commit 15e52f5), so this round made NO model call
of any kind. Every number below comes from pytest, from an executed repro, or
from a replay over the 79 saved `out/*/attribution.json`. The suite re-run is
owed before this round is called done.

### Per item

| # | Finding | Verdict | Evidence |
|---|---|---|---|
| 1 | HIGH — a row-header unit bypasses NumberFact verification | fixed | Repro re-executed: `quote_prints("Net interest margin (%) 2.05 2.08", 2.05, "$m")` -> `True`, so `_mint_record` kept an invented `{"value": 2.05, "unit": "$m"}` and a `+2.05 $m` driver stayed at 95. Round 3 bound the unit of a number that carries its unit GLUED to it, and a table row does not: it prints the unit once, in the header, and the cells bare. New `_declarations` reads the units the quote's own WORDS declare, and a bare number is read in those units through `UNIT_CONVERSIONS` and nothing else. After: the mint drops the fact, the record ships with no numbers, and `cap_weakly_cited_claims` takes the driver to 80. |
| 2 | HIGH — `settle_ratio_scale` corrects the numbers and keeps a conflicting movement unit | fixed | Repro re-executed: an ROE submitted `1160 -> 1140, -20, unit bps` against a ppt metric came out of the corrector as `11.6 -> 11.4, -0.2, bps` — the gold movement written in a unit 100x out. `check_ratio_level` then keyed off the retained `"bps"`, saw a non-ratio unit, and stayed silent; the `no_quantified_drivers` exemption left confidence 95. Two parts: the corrector settles the UNIT with the numbers and records the change in its note (`bps -> ppt`), and `check_ratio_level` takes the METRIC's unit, exactly as the corrector does. After: `11.6 -> 11.4, -0.2, ppt`; and an UNCORRECTED `1160 bps` against a ppt metric now fires `movement_level_not_ratio_sized`, which is a `WHOLE_TABLE_FAILURE`. Both call sites already held `metric_cfg["unit"]`. |
| 3 | MED-HIGH — the money family test collapses `$m` and `$bn` | fixed | Repro re-executed: `quote_states("Assets ($bn) 2.5", 2.5, "$m")` -> `True`, because `_FAMILY_WORDS` held the generic token `"$"` for both units. The declaration table now keys on the canonical unit — `$m` and `$bn` are separate patterns — and a bare cell reaches the claim only through `convert_unit`. After: `2.5 $m` is refused and `2500 $m` grounds. A quote that writes `"$"` and never names a scale still grounds either money unit 1:1, which is the reading a plain `$` column has always had. |
| 4 | MED-HIGH — the narrowed extractor gate parses label digits as numbers | fixed | Repro re-executed: `_quote_numbers("Level 2 common equity Tier 1 capital ratio")` -> `[(2.0, ""), (1.0, "")]`, so the quote looked like one that prints numbers, the no-number exemption was lost, and the 12.53%/12.49% facts the record was cited for were dropped. Visible in `out/wbc-cet1-fy25-vs-fy24-cheap/attribution.json` as `ev-16` with an empty `numbers` list. New `validate.printed_numbers` states the rule; the gate asks it instead of `_quote_numbers`. |

### The label-index rule, stated exactly

A number in a quote is a LABEL INDEX, and not a quantity the quote prints, when
ALL five hold. The conjunction is what keeps a real figure out.

1. It carries no glued unit. A bank never writes "Level 2bps".
2. It is one or two digits, with no decimal point and no thousands separator.
3. Its magnitude is at most 99.
4. A word ends immediately before it AND a word starts immediately after it, so
   it sits inside the label rather than in the row's run of figures. "Stage 2
   4,504" is a figure with an index in front of it, and the figure keeps the
   gate on.
5. It is unlike the fact being checked — outside that claim's citation
   tolerance. A digit the fact itself claims is not an absence of evidence
   about that fact: the row may yet declare a unit the fact conflicts with, so
   the exemption is not handed out on it. ("Segment 3 income ($bn) by division"
   still refuses a fact of `3.0 $m`.)

Replayed over all 79 artifacts, 2,569 records: the gate turns OFF on **12
records** and on no others. Every one is a label, a date or a footnote index —
"Level 2 common equity Tier 1 capital ratio", "Jun 21 Pro-forma", "for the 6
months ended 30 June 2026", "Net interest margin 4 Total Group", "APRA Common
Equity Tier 1 ratios". None is a measurement.

### Verification

`uv run python -m pytest tests/ -q` — **430 passed** (403 before; +27, all in
the new `tests/test_review_round4.py`). All four items were RED first: 8
failures against the round-3 tree, one or more per finding.

`uv run ruff check src/ tests/` — back to the 29-finding baseline, byte for
byte. No prompt string changed in this round; `author.py` is untouched.

#### Replay over saved artifacts — 79 artifacts, 2,569 records, 5,564 facts

A worktree at 15e52f5 supplies the "before" and the working tree the "after".
The same script runs against both and the two blobs are diffed.

**The extractor gate, per fact: 13 lost, 2 regained.** Both directions were
inspected one by one.

- The 13 losses are one class, and it is finding 3's class exactly: a `($bn)`
  row whose fact claims the same magnitude in `$m`. "Risk weighted assets
  ($bn) 482 496 505" carrying `482 $m`; "Total assets ($bn) 1,409" carrying
  `1409 $m`; "Average interest earning assets ($bn) 1,001.2 978.7" carrying
  `1001.2 $m`. Every one is wrong by a factor of 1000. Each is a test case in
  `test_a_billions_row_does_not_print_the_same_number_in_millions`.
- The 2 regains are `cba-nim-fy26-vs-fy25-normal` `ev-5`: the quote is "Net
  interest margin 4 Total Group" — a row label with footnote index 4 — and the
  facts are the NIM row's own 2.08% and 2.05%.

**`quote_states`: 158 grounding pairs after, 153 before. 0 lost, 5 gained.**
The five are `nab-cet1-fy25-vs-fy24-cheap` `ev-2`, a walk table headed
"Movements in CET1 capital ratio (%)" printing 0.82, (0.61), (0.45), 0.01,
(0.08), whose drivers claim +82, -61, -45, +1, -8 bps. The page prints those
numbers; the old family test could not read a "(%)" header into a bps claim, so
five correct claims were denied their citation. This is a widening of ONE
reading — a declared unit converted through `UNIT_CONVERSIONS` — and it changes
no confidence anywhere in the saved set.

**Every deterministic verdict is unchanged on all 79.** `cap_weakly_cited_claims`
with all driver confidences reset to 95 caps the same 90 claims before and
after. `settle_ratio_scale`, `check_ratio_level` and `check_drivers_reconcile`
return the identical result on all 79.

#### The over-tightening this round found in its own first cut, and how

The first implementation read a declared unit over the WHOLE quote. Replayed,
it dropped **92 facts**, and **75 of them were real**:

- **54** were multi-row quotes. A quote spans four rows of one table — "Average
  net assets 78,004 ... ROE - cash basis (%) 13.8" — and the header of the last
  row was read backwards over the cells of the first.
- **10** were percent-change columns. A bank prints the change beside the dollar
  columns of the same row, under the one "($M)" header: "Corporate tax expense
  ($M) 4,699 4,491 5 2,332 2,367 (1)".
- **11** were a cents row whose fact named "%" or "bps" ("Dividends per share -
  fully franked (cents) 235 260 225" carrying `235 %`). Those facts ARE wrong,
  but the rule that caught them is the rule that caught the 64 above, so it is
  not the rule.
- **17** were the `$bn`/`$m` class finding 3 exists for.

The refined rule loses 13 and restores 79: all 75 real facts, plus 4 of the 17
`$bn` cases it cannot reach — a chart annotation that prints its "($bn)" label
AFTER its bars ("5 40 42 12 (10) Jun 25 ... IRRBB RWA ($bn)"), where no
declaration stands before the number.

So the denial is positional and one-directional, and both halves are measured
facts about how a bank prints a table:

- Only a declaration STANDING BEFORE the number binds it.
- A row that declares the claim's own FAMILY has already had its say through
  the conversion ("Assets ($bn) 2.5" denies 2.5 $m).
- A row that declares a RATIO denies a MONEY claim outright (finding 1).
- A row that declares MONEY does NOT deny a ratio claim (the change column).

`test_a_declaration_binds_only_what_stands_after_it` holds both halves with the
saved quotes verbatim.

#### The three named live cases, before -> after

| case | before | after |
|---|---|---|
| `wbc-cet1-fy25-vs-fy24-cheap` `ev-16` — "Level 2 common equity Tier 1 capital ratio: - APRA" | `_quote_numbers` -> `[2, 1]`, gate ON, both gold facts (12.53%, 12.49%) DROPPED | `printed_numbers` -> `[]`, gate OFF, both facts KEPT. The sibling `wbc-cet1-fy25-vs-fy24-agentic-cheap` `ev-5` quotes the same row WITH its figures, so its gate stays ON and keeps the same two facts by printing them. |
| `nab-roe-fy25` / `cba-roe-fy26` ratio artifacts | the corrector returned `11.6 -> 11.4, -0.2 bps` and `14.0 -> 13.5, 0.5 bps` — right numbers, wrong unit; `check_ratio_level` silent | `-0.2 ppt` and `0.5 ppt`, and the uncorrected `1160 bps` against a ppt metric now fires `movement_level_not_ratio_sized`. The six SAVED roe artifacts already carry `ppt` movements (the model labelled them correctly), so **no saved artifact changes**: this defect is latent in the saved set and proved by the repro. |
| `cba-cti-fy26-vs-fy25-*` (the 0.0 ppt residual) | agentic: `drivers_reconcile` PASS, residual 0.0 ppt, cap-at-95 takes all three drivers; cheap: PASS; agentic-cheap: `no_quantified_drivers` | identical in every field. The round does not touch it. |

### Left undone

- **The live suite re-run.** Owed as soon as OpenRouter credits return: dev and
  questions, both shells, against `agentic-dev-merged` and the frozen baseline.
  Until then the round's claim is "no deterministic verdict moves on 79 saved
  artifacts", which is weaker than "the suite holds".
- **The percent-to-bps lift does not settle the movement's unit either.**
  `author.py:425` multiplies the endpoints by 100 for a bps metric and leaves
  the model's own label in place, which is finding 2's defect in the mirror
  position. It is out of this round's brief and untouched. Note that
  `check_ratio_level` keying on the METRIC's unit already stops the false
  positive it used to cause (a lifted `1220` labelled `"%"` failed the ratio
  ceiling on a metric whose unit is bps).
- A cents row still grounds a "%" fact of the same magnitude ("Dividends per
  share (cents) 235 260 225" carrying `235 %`). The asymmetric rule above lets
  it through deliberately: the same row prints its percentage change column,
  and no shape rule separates the two. It was let through before this round as
  well, so nothing regressed; it is a candidate for a later round.
- Everything left undone by round 3 stands.

## Disposition (2026-08-31 morning)

Four rounds ran overnight; the finding count converged 18 -> 15 -> 7 -> 5 -> 4
with severity narrowing each round (rounds 3-4 were refinements of earlier
fixes, not new defect classes). 47 findings fixed, zero refuted, zero
loosenings, 430 tests. This ticket CLOSES when the round-4 live verification
suite is green (running this morning). Further review passes fold into
Tuesday's six cleanup passes (ticket 33), which review the same code with the
same discipline on the cleaned layout.

## Round 7 — mattpocock code-review skill, cycle 1 (2026-09-01)

Two-axis review of `holdout-freeze-20260831...HEAD` (Standards + Spec
sub-agents in parallel, per the skill).

Fixed this round (gate: 442 tests green, dev rescore byte-identical to
`pre-cleanup-baseline.md`):
- `manifest/mqg.json` doc_types `mda`/`presentation` sat outside the shared
  vocabulary, so `printed_page_of` skipped slide numbers and `walk_sum_tolerance`
  used the 1.0 text tolerance on presentation walks. Renamed to
  `results_announcement`/`results_presentation`; filenames kept (page caches
  key on the filename stem; data/ is shared with the frozen exam checkout).
  The frozen checkout keeps the old values — the exam runs handicapped, never
  flattered; noted for the exam writeup.
- `WHOLE_TABLE_FAILURES` comment now cites its evidence paths (synthetic repro
  in tests/test_review_round5.py; round6-check.md == pre-cleanup-baseline.md)
  per the hardcoded-override policy.
- Stale-doc falsehoods: README results table retitled as the retired open-loop
  baseline's; "How it works" rewritten for the closed loop; ADR-0005 no longer
  claims the pipeline is in the repo; src file count corrected. Full
  README/design.md rewrite stays Wednesday report work.

Queued for the code-simplifier phase (judgement-call smells, both agents):
- llm.py: chat/chat_tools duplicate the 35-line retry ladder; extract one.
- llm.py/research_agent.py: deadline/clock data clump; HARD_STOP_FACTOR
  computed at 4 sites on two clocks.
- cli.py repeats "agentic (the only live combo)" x3; evals.py JUDGE_COMBO
  beside a combo="agentic" default can drift.
- Test files named by review round (shotgun surgery); fold into the test
  pruning pass.

Noted, no action: scope-creep list (out-of-time error taxonomy, committed
overnight scorecards) — all defensible; `validate.py` "lived in author.py"
comment is accurate history.

## Round 8 — code-review skill, cycle 2 (2026-09-01)

Both axes verified every cycle-1 fix. Six new findings, all doc-truth or
drift-prevention, none behavioural; all fixed this cycle (gate: 444 tests,
dev rescore identical to baseline, ruff delta zero):
- corpus.py now owns the manifest doc_type vocabulary: DOC_TYPES + the shared
  PRESENTATION_DOC_TYPES (extract.py and walk_sum_tolerance both import it —
  their two hand-kept copies had already drifted apart in order). New tests
  hold every committed manifest to the vocabulary, so the MQG class of drift
  cannot recur silently.
- validate.py evidence comment now states the match exactly (jsonl pair
  byte-identical; md pair differs in the timestamp title). The stray
  rescore jsonl committed in 94a987a is deleted.
- design.md carries a STALE SECTIONS banner pointing at ADR-0005 until the
  Wednesday rewrite; README's rotting counts ("32 stems", "32 tickets")
  replaced with count-free wording; extract.py docstring now names both of
  the module's jobs (vision walk reads + printed-page mapping).

Convergence: cycle 1 found 2 hard + ~6 judgement; cycle 2 found 0 hard
behavioural, 6 doc/count nits. Cycle 3 is the convergence check.

## Round 9 — code-review skill, cycle 3 (2026-09-01)

Both axes verified every cycle-2 fix. Four new findings, all fixed:
- registry/mqg.json did not exist — both registry load paths fall back to {},
  so MQG ran without its calendar, language map, or full-name resolution
  ("Macquarie" named no bank). Fixed with a deliberate SKELETON only (names,
  31 March calendar, doc naming): measure/walk-label maps stay absent until
  after the sealed exam, because distilling Macquarie's disclosure language
  after the exam questions were authored risks steering the agent toward exam
  topics. A new test requires a registry file for every manifest bank.
  NOTE for the exam writeup: the frozen checkout runs WITHOUT this skeleton
  (and with the old doc_types) — both handicaps are conservative.
- discover.py wrote the model's doc_type into the manifest unchecked (the
  4th hand-kept copy problem); it now fails loudly on any term outside
  corpus.DOC_TYPES before writing.
- discover.py's manifest note claimed "verified by fetch_corpus" at write
  time, before any fetch; reworded to what actually happens.
- 3 ruff hits that entered with f94aa99 (I001, ISC004 x2 in
  test_review_round5.py) fixed; repo lint count 29 -> 26, remainder queued.

Gate: 445 tests, dev rescore identical to baseline, no new ruff.

## Round 10 — code-review skill, cycle 4 (2026-09-01)

Both axes verified every cycle-3 fix. Three new findings, all fixed:
- BEHAVIOURAL (Spec, reproduced live): primary_basis defaulted to "cash" for
  a registry with no measures block, so _settle_basis rewrote a declared
  "statutory" to "cash" and its limitation claimed the registry named it —
  false, and exactly what MQG (statutory NPAT, skeleton registry) would hit.
  primary_basis now returns None without measures; _settle_basis keeps the
  agent's declared basis; research_agent's duplicate inline guard removed
  (one source of truth). Dev banks all carry measures blocks, so the dev
  rescore is untouched — verified identical.
- The round-9 discovery gate shipped unexecuted (no test imported
  discover.py). tests/test_discover.py now drives the gate both ways with a
  scripted LLM and pins the manifest stays unwritten on refusal.
- The discovery PROMPT's own doc_type enumeration is now held to
  corpus.DOC_TYPES by test, so a vocabulary rename cannot strand it.

Gate: 450 tests, dev rescore identical to baseline, ruff steady at 26
(all pre-existing, queued).

## Round 11 — code-review skill, cycle 5 (2026-09-01) — CONVERGED

Both axes verified every cycle-4 fix. Findings this cycle:
- Spec (minor, fixed): the no-declaration path still invented "cash" — at
  research_agent's reply.get("basis", "cash") and _settle_basis's `or "cash"`.
  _settle_basis now owns the whole default: registry headline when known,
  "as reported" when nothing is declared and nothing is known, never "cash"
  without a registry behind it. Three new tests pin the paths; the surviving
  cash default (measures block naming no basis word) is documented and tested.
- Standards (cosmetic, fixed): stale author.py mention in a test docstring;
  in-body imports moved to the top block; try/except-AssertionError converted
  to pytest.raises and the double sleep-skip collapsed to one patch.

Gate: 453 tests, dev rescore identical to baseline, ruff steady at 26.

CONVERGENCE CALL: cycle 1 found 2 hard + judgement backlog; cycle 2 six
doc-truth nits; cycles 3-5 found only consequences of in-review fixes plus
cosmetics, and every verification passed. The code-review skill phase closes
here. The queued judgement-call smells hand over to the code-simplifier phase.

## Simplifier round 1 (2026-09-01) — the queued backlog

The judgement-call smells queued by review rounds 7-11, implemented:
- llm.py: chat() and chat_tools() now climb ONE retry ladder — _completion()
  takes the payload and a success-parse callback; the ~55 duplicated lines
  and their comments live once. A parse that raises still charges an attempt.
- research_agent.py: _hard_stop_s(combo) states the hard stop once for the
  four sites that computed HARD_STOP_FACTOR * wall_clock_s on two clocks.
- config.py: LIVE_COMBO names the live combo once; cli.py (3 defaults + help)
  and evals.py (run_judge_suite, rescore, judges lookup) read it; the
  JUDGE_COMBO constant beside a hand-kept default is gone.
- cli.py: one _COMBO_HELP string instead of three copies.

Gate: 453 tests, dev rescore identical to baseline, ruff steady at 26, CLI
--help runs.

Still queued: review-round test file naming (folds into the test pruning
pass); 26 pre-existing ruff pedantic hits; validate.py's indirect pymupdf
dependency via corpus (accepted shape).

## Simplifier round 2 (2026-09-01) — fresh-eyes pass, verified and applied

Dead code deleted (with the tests that were its only callers):
- refs.follow_references + FollowedPage + MAX_FOLLOWED_PAGES + _MIN_RELEVANCE
  (the open-loop budget expander; the agent's follow_references tool builds on
  scan_page directly). test_refs.py keeps its 15 live-behaviour tests.
- validate.printed_numbers + its two regexes + _LABEL_INDEX_CEILING (fed a
  gate deleted in round 6). test_review_round4 keeps its quote_prints pins.
- judge._format_quotes (zero callers); evals.Tolerance.unit (written, never
  read). Lint fell 26 -> 21, all deletions.

Extractions (drift-prevention and duplication):
- render.case_slug: the artifact writer and the rescore/judge readers build
  the out/<slug>/ name in one place.
- research_agent: _start_run (shared shell head), _provenance (byte-identical
  audit block), _stopped_early_note, _budget_hit (the twice-written budget
  ladder, soft wall clock at turn top / hard stop per call), _recover_minted
  (both shells restore tool-minted citations identically).
- validate._cap_drivers: all three cap rules share one body, so a capped
  claim always reads the same in the artifact.
- llm: the reasoning-off flag moved into _completion; LIVE_COMBO now also
  covers research_agent's two entry-point defaults.

Declined, with reasons: evals' "unreachable" failed-fallback reads persisted
crossref JSON that may predate the key (kept); the twin one-line label
helpers (a cross-module private import is worse); the three RISKY proposals
(confidence-cap subsumption claim needs a replay; quote_states merge touches
the grounding gate; the unreachable combo.agent guard is a rail).

Gate: 443 tests, dev rescore identical to baseline, ruff 21 (down 5).

## Comment sweep wave 1 (2026-09-01) — user directive

Five parallel agents, one per file group, comments/docstrings only (AST
verified identical in both groups that checked). Rule: keep non-obvious
constraints, business logic, and the evidence receipts the override policy
requires; cut narration, ticket/round breadcrumbs, and blow-by-blow defect
stories (each compressed to rule + one receipt). Net -115 lines across 14
files. Kept whole: the validate.py HARDCODED-OVERRIDE POLICY, every artifact
path and measured value, judge prompts and scorecard Disclosure (runtime
text), cache-key invariant, clock semantics. Restored one over-cut: the
NETWORK_GRACE infra-only/disclosure sentence (frozen-baseline comparability).

Gate: 443 tests, dev rescore identical to baseline, ruff steady at 21.

## Restructure (2026-09-01) — src into informative subpackages

Layout (moves only; one rename to avoid a package/module stutter):
- agent/research_agent.py — the product shell.
- tools/{corpus,retrieve,refs,extract,discover}.py — the document layer.
- validation/{validate,schema}.py — the contract and the checks.
- judging/judge.py; evals/harness.py (was evals.py).
- Top level stays cross-cutting: cli, config (REPO_ROOT counts its parents),
  llm, render, taxonomy.
Imports rewritten in src/tests/scripts; ruff --fix sorted the shuffled
blocks and cleared 6 pre-existing I001s (src+tests lint 21 -> 15).

Gate: 443 tests, CLI --help runs, dev rescore identical to baseline.

## Test pruning (2026-09-01) — LAST cleanup phase before final proof

443 tests / 15 files -> 349 tests / 13 files. The four review-round files
are gone; their keepers moved with their docstring receipts into
behaviour-named homes, plus two new files: test_quote_grounding.py (the
quote-numbers/prints/states matrix, rounds 2-4 merged and deduped) and
test_confidence_caps.py (cap_* rules, WHOLE_TABLE_FAILURES, null
confidence). Deletions were near-duplicates, subsumed parametrize rows, and
re-assertions of pins held elsewhere. Three proposal deviations, each a
sole-pin keep (walk_extraction_error surfacing, bank_language label
positive pin, residual/ratio branch pairs). validate.py's evidence citation
now points at test_confidence_caps.py.

Gate: 349 passed, ruff 15 (all pre-existing), dev rescore identical.

## FINAL PROOF (2026-09-01 ~12:00) — cleanup day CLOSED

Live spot-check on the fully cleaned code (post review-convergence,
simplifier, comment sweeps, restructure, test pruning): CBA NIM FY26,
fresh end-to-end run. Result: movement OK (208 -> 205 bps), recall 7/7,
precision 7/7, extraction 7/7, all 7 claims correct at confidence 93,
Brier 0.007, confidently-wrong 0.0, $0.0148, 366s, 19 tool calls, no
budget touched, zero failed checks. Scorecard:
evals/results/spotcheck-postcleanup.md.

Static gates held through every commit: suite green at each step
(443 -> 349 by design), dev rescore byte-identical to
pre-cleanup-baseline at every commit, lint 29 -> 15 with zero new hits.

Open (not cleanup): the user-invoked architecture skill (blocked on
their keystroke); exam + holdout runs; Wednesday report.

## Codex round 1 applied (2026-09-01)

Architecture (2 MUST + 1 TASTE applied, 1 TASTE deferred):
- The doc-type contracts (DOC_TYPES, PRESENTATION_DOC_TYPES) moved from
  tools/corpus.py to validation/schema.py — validation no longer imports the
  pymupdf-backed corpus module; the package graph's only cycle is gone.
- The routing seams (runner_for, question_runner_for, _require_agent) moved
  from config.py to agent/routing.py — config is data only; the config<->agent
  lazy-import cycle is gone. Callers (cli, harness, tests) updated.
- refs.relevance_terms() is the public form of _words; the agent no longer
  imports a private tokenizer to agree with scan_page.
- DEFERRED with reasons: splitting the 2,040-line research_agent.py into
  prompts/toolbox/assembly (Codex itself grades it maintainability, not a
  defect; deadline-week churn risk on the product shell outweighs it).

Cleanup audit round 1: simplifier, comment sweeps, and dead deletions HOLD
under adversarial git-history comparison. Test pruning had overcut: Codex
named 8 lost pins; pruning round 2 independently restored 4 of them plus 8
more of its own; the 5 neither caught alone are restored (commit e0a982b).

Gate: 362 tests, dev rescore identical, ruff 15.

## Fable architecture round 1 applied (2026-09-01)

Findings (import graph verified acyclic by AST walk) and dispositions:
- APPLIED: the grader owns its tolerances — SCORER_* constants in harness.py,
  pinned by literal value in test_scoring; a loosened product tolerance now
  SURFACES as eval failures instead of being inherited by the grader.
- APPLIED: the verbatim-quote gate moved to validation/quotes.py (match_quote,
  quote_key, strip_markers, MARKER_RELAXATION with the full _MARKER_RE
  evidence block) — every EvidenceRecord minter shares one gate; schema's
  docstring no longer points up the layer stack.
- APPLIED: agent/prompts.py — 591 lines of pure prompt/schema data out of
  research_agent.py (2030 -> ~1450 lines); no logic moved. This was the
  SAFE slice of the deferred three-way split.
- APPLIED: harness's seven in-function imports hoisted (no cycle needs them);
  tool-surface drift test added (every TOOL_SPECS name must be a Research
  method).
- ESCALATED to the user, not changed: the two shells run different gate sets
  (cap_weakly_cited_claims runs in the case shell only; the question shell
  has resolvability-stripping but no stated-number cap). Whether question
  facts should get the weak-citation cap is a product decision.
- NOTED: question_scope's synthetic case/metric_cfg shape (product shape).

## Fable simplifier round 3 applied (2026-09-01)

Six proposals applied: Combo.extract/author/author_max_tokens deleted (zero
readers; open-loop residue); render._quote_line builds the citation line once
(indent stays a parameter — judge.answer_prose strips on lstrip); validate
_reconcile_tol shares the sum-check slack body between walk_sum_tolerance and
reconcile_tolerance; crossref_answer_prose moved beside its sibling adapters
in judging/judge.py; llm RETRIES/JSON_RETRIES are module policy, not knobs;
run_question_suite's unvaried split parameter dropped. DECLINED: merging the
three gold loaders (the proposer itself graded it RISKY — the filters and
stitched fields genuinely differ). Retired PRICES entries stay: rescoring
saved artifacts reads them.

Gate: 366 tests, dev rescore identical, ruff 15.

## Fable review cycle 6 applied (2026-09-01)

Five findings; four fixed, one already fixed convergently:
- MUST: build_attribution crashed on submissions its own tool schema permits
  (movement/residual without a unit, string endpoints, confidence 105) — a
  10-30 minute run ended with NO artifact against the documented never-crash
  contract. Now: _numeric() coercion reads numbers-as-strings; a malformed
  movement or residual degrades to None with the reason declared; confidence
  clamps into 0-100 with a limitation. Four regression tests.
- MUST: Research.bank_language returned the case bank's vocabulary stamped
  with another bank's name (registries is {} in a metric case, and the
  fallback always answered). Now refuses with an explicit no-language-map
  note. Test added.
- NOTE: the stem-collision guard only ran on the doc_alias_index path;
  _assert_distinct_stems (manifest-read, cached) now runs on every
  load_documents call, and the stale comment class dies with it.
- NOTE: validate.py's two F821s fixed (EvidenceRecord imported after the
  schema split). Repo lint 15 -> 13.
- Dead Combo fields: already deleted by simplifier round 3 (convergent).

Gate: 371 tests, dev rescore identical to baseline.

## Sol (Codex) round 2 applied (2026-09-01)

- Architecture r2: CONSOLIDATED — full AST scan (function-local imports
  included) confirms zero package cycles; the tokenizer boundary is public.
  TASTE applied: tests/test_architecture.py pins the two broken cycles
  mechanically; routing.py's over-broad docstring corrected.
- Cleanup audit r2: seven of the eight restored pins verified as genuinely
  executing their branches; wave 3 loses no constraint; the moved routing and
  contracts are textually identical. One MUST fixed: the restored
  wrong-period test was mutation-insensitive (containment failed first), so
  the period predicate had no real pin — a bare bank name ("NAB") is the
  sensitive case and now pins it.
- Sol correctness review r1 DIED on the network gap mid-run (websocket DNS
  failures); it does not count and is relaunched.

Gate: 374 tests, dev rescore identical to baseline.

## Fable simplifier round 4 applied (2026-09-01)

Five of six applied: the all_documents stem guard deleted (strictly weaker
than _assert_distinct_stems, which now runs on every load path; the
collision test drives the real guard through tmp manifests with cache
clears); WALK_BAR_TOL_PA / MONEY_REL_TOL / MONEY_ABS_TOL_M deleted (zero
readers after the SCORER_* split); the harness bps branch collapsed; the
relevance_terms import hoisted; _document_lines shares the corpus listing
both prompts print. DECLINED: flattening build_answer's per-fact
_recover_minted loop — touches citation recovery, needs a replay first.

Gate: 374 tests, dev rescore identical, ruff 13.

## Fable architecture round 2 applied (2026-09-01)

Round-1 landings verified (prompts pure data; SCORER split clean). Applied:
- quotes.py docstring narrowed to the truth — the gate covers TEXT quotes;
  vision-read records carry code-built quote strings whose discipline is the
  walk checks. The entailment-judge nuance (those strings enter the judge as
  "verbatim source quotes") is a documented judgment call in
  docs/design/eval-review-guide.md, kept as-is: relabelling changes eval
  semantics and is not cleanup.
- harness's stale "constants live in validate.py" comment now points at the
  SCORER block.
- research_agent's unused quote_key import and re-export deleted (one import
  path to the gate).
DEFERRED with reasons: moving finalise into validation (arguable seam, churn
risk); splitting harness at the scorer boundary (noted as the natural seam);
question_scope's synthetic metric shape (third noting — bundled into the
escalation list for the user).

Gate: 374 tests, dev rescore identical, ruff 13.

## Sol review round 1 + Sol audit round 3 + Fable pruning round 4 (2026-09-01)

Sol review r1 (relaunched after the outage killed the first run): three
MUSTs, all offline-reproduced, all fixed with pins — the zero-evidence
movement cap at 20 (a CTI submission with empty evidence shipped at 95),
spelled-out quantities now face the question gate (number word + quantity
noun; a period name never trips it), question confidence clamps like the
case shell. NOTEs applied: scoped ask slugs (collision on shared first
words), failed-walk pages count as read. Deferred: socket-stall deadline
precision (overshoot <=65s, absorbed by the hard-stop factor).

Sol audit r3: caught my own round-6 fixes being incomplete — _numeric now
rejects nan/inf, the coerced residual is stored, the deliberate empty-unit
residual semantics restored, run_question_suite's split truly removed.

Fable pruning r4: 19 pins incl. the first tests on two hardcoded overrides;
absolute-import forms now caught by the layering walker; suite 399, ruff 0.

## Fable review cycle 7 applied (2026-09-01)

Three executed MUSTs and three NOTEs, all fixed with pins (suite 404):
- A submission whose JSON was cut off by the reply limit was ACCEPTED as an
  empty zero-confidence answer. _arguments now returns None on a parse
  failure, and a None submit is rejected back to the model through the
  existing retry machinery; exhausted retries fall to the declared
  no-submission artifact, never a silent zero.
- A bare-string citation ("ev-1") was iterated into characters at three
  sites (remap, _recover_minted, and the recovery call-site spread); one id
  is now one id everywhere.
- The verbatim gate rejected page-faithful quotes over characters a reader
  cannot see: zero-width spaces and non-breaking hyphens, measured on 15 of
  36 corpus documents. The punctuation table now normalises U+2011 and drops
  U+200B/200C/200D/FEFF on both sides of the comparison.
- The zero-evidence cap now reaches driver confidences (a narrative driver
  rendered 95/100 under a capped answer); "basis  points" with doubled
  whitespace no longer slips the spelt-quantity gate.

Gate: 404 tests, ruff clean, dev rescore identical.

## Sol audit round 4 applied (2026-09-01)

Five MUST-FIXes, all applied with pins (suite 407): the question-confidence
clamp disclosure was read out of the payload BEFORE the clamp wrote it (the
note vanished; ordering fixed); discovery's calendar date reverted from UTC
to the aware LOCAL date (the lint fix moved Hong Kong's midnight boundary);
the layering walker now reads `from bank_equity_researcher import x` and
plain `import` spellings; the split removal and direct float('inf')
rejection are pinned. Residual coercion, empty-unit semantics, the stem
guard mutation test, and every noqa reason verified as holding.

## Sol review round 2 applied (2026-09-01)

Round-1 fixes verified by re-running the probes; four new MUSTs, all fixed
with pins (suite 412):
- The zero-evidence movement cap now keys on RESOLVED CITATIONS (headline +
  drivers), not on the evidence pool being non-empty — an unrelated dividend
  record no longer launders a 95.
- _states adopts the _converted_prints doctrine across unit conversions: the
  TIGHTER of the two units' slack, so a 10 bps fact stops certifying a 0.02
  ppt claim.
- _QUANTITY_RE: "zero" joins the number words; a bare one-or-two-digit token
  is no longer a quantity (label indexes like "Tier 1" stripped qualitative
  prose), digits count with a decimal/thousands mark, three digits, or a
  unit/currency beside them. Trade accepted and documented: bare "rose by 5"
  escapes.
- The answer-confidence cap counts GROUNDED kept facts: an answer of only
  ungrounded prose ("Outlook remained resilient") no longer carries 95.

Gate-change neutrality replay (the rescore gate cannot see cap changes):
all 111 saved out/*/attribution.json artifacts replayed through the new
movement cap and the tightened _states — 0 new firings on either. The
changes bind only in the reproduced defect paths; receipts stamped beside
both overrides.

## Fable simplifier round 5 applied (2026-09-01)

Five proposals, all applied: one clamp (the case shell now calls
_clamped_confidence); _states deleted — cap_weakly_cited_claims calls
_converted_prints directly (the proposer executed a 300,000-triple
equivalence; the artifact replay re-run after the change: 113 artifacts, 0
new firings); the walk-cap elif's subsumed per-driver loop deleted with the
implication named; one _as_ids helper replaces four string-wrapping copies;
schema tidy (vocabulary below imports, the shared cap constant above its
first use with a both-gates comment, DriverClaim fields above the
validator). Declined by the proposer with reasons: moving the gates to
validate.py.

Gate: 412 tests, ruff clean, dev rescore identical.

## Sol review round 3 applied, part 1 (2026-09-01)

Three of four MUSTs fixed with pins (413 tests):
- cap_ungrounded_movement: a movement none of the CITED records states —
  endpoints or delta, via quote_prints (bare table cells and walk endpoints
  count) or converted NumberFacts — caps to 20 with drivers. It replaces the
  weaker any-citation-resolves rule, whose laundering Sol reproduced (an ROE
  movement citing only a dividend fact at 95). Replay: 113 movements, one
  firing, a true-positive retired-arm CTI artifact; zero live-arm impact.
  First draft was falsified by the replay itself (quote_states refused the
  walk chart's bare "171.0 -> 174.0"); quote_prints is the right bar.
- Unclassified walks: each unknown-span walk stands alone in walks_for_view
  (two of them were stamped corroborated_2_sources), and the no-primary-walk
  cap now fires whenever walks exist without a primary — an "Opening ->
  Closing" chart no longer ships at 95 with no limitation.
- The peripheral->fatal escalation is scoped to walk_extraction metrics: one
  unreadable optional chart dropped a reconciled ROE from 95 to 40.
Remaining from round 3: the retrieval fusion comparability MUST (next), and
the arch-round walker bypass.

## Sol review round 3 part 2 + Sol architecture round 4 applied (2026-09-01)

- Retrieval is POOLED: one BM25 index over the task's whole corpus (idf
  computed once, scores comparable across documents) and one pooled dense
  ranking, global reciprocal-rank fusion. The per-document rank reset gave
  every document's own top page 2.0 and lexical tie-breaks dropped the one
  relevant document from the top eight (Sol's executed 13-document repro).
  search_pages rewired; the old per-document retrieve() deleted; a mocked
  comparability pin added.
- The layering walker's two bypasses closed (`from .. import tools` and
  `from bank_equity_researcher import tools`), with a five-spelling pin that
  tests the walker itself.
- Sol arch r4 TASTE items (validation/gates.py split; agent/toolbox.py
  slice) queued for the next architecture application round.

Gate: 415 tests, ruff clean, dev rescore identical.

## Fable architecture round 3 applied (2026-09-01)

The two blessed splits, moves only, bodies verbatim: validation/gates.py
(the two gates, the shared cap, the quantity classifier — 109 lines; schema
keeps models and vocabulary, 136 lines) and agent/toolbox.py (the Research
class with its limits and helpers — 468 lines; research_agent.py is the
orchestration/assembly module at 1,000 lines). Importers updated everywhere;
no re-export shims.

Gate: 415 tests, ruff clean, CLI runs, dev rescore identical.

## Pruning r5 + Sol audit r5 + Sol review r4 applied (2026-09-01, three commits)

- Pruning r5 (1155da7): 13 mutation-verified pins (each applied its mutation,
  failed, reverted); the weak pooled/movement pins rebuilt; two deletions;
  one src proposal (the redundant prior-half guard) applied in the product
  commit. Suite 415 -> 428.
- Product batch (6e8da1c): stale embedding caches rebuild on row mismatch
  (the pooled matrix misattributed B/p1 as A/p3); discover clears corpus
  caches after writing; cap_ungrounded_movement holds the quantity digit
  standard (bare note numbers stripped) and stands down for worded
  movements; the cap moved after the scale normalisers (a repaired percent
  movement stayed wrongly capped); quotes render one-line (source text
  leaked past answer_prose's line filter into judged prose — live repro);
  residuals render outside the table too, and the table row has six cells.
  Grounding replay: 119 movements, two firings, both retired-arm artifacts
  citing divisional pieces but never the group movement — true positives.
- Eval batch (f77c1f5): an entailment fail under a truncated quote window
  FLAGS instead of failing (the count cap now counts as truncation); the
  framing rank orders by recall fraction first; a dotted child outside the
  metric's taxonomy vocabulary is unscored and cannot fill a parent slot.

## Fable arch r4 + simplifier r6 + pruning r6 applied (2026-09-01)

- validation/quantities.py: ONE home for the quantity standard (NUMBER_WORDS,
  UNIT_TOKENS, WORDED_NOUNS, QUANTITY_RE, WORDED_QUANTITY_RE, BARE_INDEX_RE).
  The worded noun list unified with the digit standard's (the undocumented
  million/billion/dollars gap removed) — gated on the 119-movement replay:
  identical two true-positive firings.
- ANSWER_GATE_CONFIDENCE_CAP renamed NOTHING_SUPPORTED_CAP with a truthful
  comment (the second applier is cap_ungrounded_movement, not the evidence
  gate).
- cap_drivers (renamed from _cap_drivers) gains a cap parameter; the bridge
  expense-split cap routes through it (tag expense_split_cap_80, shared
  wording). The walk 85 driver-follow stays a follow-of-answer-cap.
- QUESTION_MAX_QUOTES lives in judge.py with its measured reason; finalise
  states its min-only ordering rule once; corroborate marked tags-only.
- Simplifier r6 micros: toolbox doc lookup, findall, dead defaults deleted,
  the classified alias replaced by context_walks.
- Pruning r6: 7/7 newest pins verified killing their mutations; the 5
  surviving mutations pinned (taxonomy wiring via source inspection, cap
  ordering via source order, both residual render branches, stale embedding
  rebuild, discover cache clears, the already-capped early return).
  Suite 428 -> 435.

## Sol review r5 + audit r6 + arch r5 applied (2026-09-01)

The three rounds convergently dismantled the afternoon grounding/truncation
work; every finding fixed with probes and pins (suite 439):
- The grounding cap is value-aware on all three branches:
  quantities.worded_quantities parses worded statements to (value, unit)
  ("rose ten basis points" no longer grounds a -3 fall; money-worded
  movements ground); BARE_INDEX_RE spares digits with numeric neighbours
  ("(%) 13 14" table rows survive; "See Note 1" still strips); NumberFacts
  are held to the stripped-text standard (the mint-gate blind spot closed).
  All seven Sol repros verified; replay 119 movements -> 5 firings, every
  one a retired-arm artifact with a genuinely uncited movement, zero
  live-arm.
- The truncation flag works in the PRODUCTION path: cited_quotes orders
  (headline share first) and no longer pre-cuts, judge_fact owns the window
  and flags; a fact the note never states FAILS regardless (truncation
  cannot explain absence); flagged_truncated is its own scorecard category
  ("a human must read the dropped quotes", not "repeat the run").
- The multiline-quote leak was NOT fixed by the earlier commit (the edit
  silently failed to match) — Sol caught it live; the one-line collapse now
  lands in _quote_line with a pin against the leaking artifact shape.
- taxonomy: impairment gains the representable `collective` parent (an
  undivided net-collective row is a total, not one causal child).
- refs recognises "Section 1.1" pointers (the MQG MDA's house style); the
  mid-page heading index gap stays noted, not fixed.
- crossref_answer_prose exported properly. Arch r5 TASTE deferred with
  reasons: the harness scorer split and the validate comparison-cluster
  split go to the next architecture application round.

## Fable architecture round 5 applied (2026-09-01)

evals/scoring.py: the pure metric-scoring block out of harness (873 + 448
lines, bodies verbatim by line diff; test_scoring imports each name from its
real home). The validate comparison-cluster split judged NON-trivial (400
lines sharing private date helpers with staying code) and deferred to its
own round with that reason.

## Sol review r6 + Sol arch r6 applied (2026-09-01)

Arch r6: CONSOLIDATED (27 modules, 53 edges, zero cycles; quantities.py a
sound leaf) — the Sol architecture floor closes.
Review r6 verified every round-5 closure and found four last edges, all
fixed with probes and pins (suite 442):
- An absent/partial fact judged against a CUT answer window flags for a
  human (35/150 saved artifacts exceed the window; a fact past character
  6,000 failed as absent — reproduced).
- worded_quantities parses compounds ("twenty five" = 25, never a bare 5)
  and direction verbs; a signed phrase that disagrees with the delta's sign
  does not ground it ("rose three" is not a three-point fall).
- strip_bare_indexes: a bare-digit run is a table row ONLY under a
  unit-declaration header; a numeric neighbour proves nothing ("Stage 2
  4,504" and "See Notes 1 2" no longer launder).
- Bare "dollars" no longer maps to $m.
Replay: 119 movements, 6 firings, zero live-arm (the sixth is another
retired-arm artifact under the stricter run rule).

## Fable architecture round 6 (2026-09-01) — CONSOLIDATED; THE FLOOR CLOSES

The closer verified the scoring split clean, ruled quantities.py one concept
(three surfaces of one question: does text state a number, what number in
words, which digits are not numbers — the strip policy is vocabulary), and
swept 28 nodes / 55 edges / zero cycles, layering strictly downward. Its
MUST is applied: the general acyclicity pin (full-graph DFS with the cycle
path in the failure) so the floor guards itself; its TASTE too
(scoring._gold_number — gold values must BE numbers; the agent-side
_numeric parses strings; opposite contracts, different names).

THE 6+6 MATRIX IS CLOSED: review F7/S6, simplifier F6/S6, sweep F6/S6,
pruning F6/S6, architecture F6/S6 — 63 rounds landed across two model
families, every applied finding pinned, every commit gated (suite green,
dev rescore byte-identical to pre-cleanup-baseline, ruff clean), every
behaviour-bearing gate change replayed over the saved-artifact estate with
receipts.

## User ruling: the two-shells gate question (2026-09-01)

DOCUMENT, not build. Metric cases have a known shape, so code checks the
numbers hard; free questions are loose prose, and a hard printed-number
check would be fragile over-engineering. Written into docs/design.md (the
ruling section before Decision 4) and as the comment above
gates.enforce_answer_gate. The escalation is closed.

## Scoped iteration reopening: depth mechanisms (user, 2026-09-01 evening)

The Fable probes priced the crossref gap as retrieval depth. The user
approved two GENERAL mechanisms and rejected the hardcoded second-source
rule:
- plan_research: the model's first call lists where the answer's pieces
  should live; at the first submit the loop reads the plan back ONCE and
  asks each item be cited, researched, or written off in limitations. A
  rail, not a gate — the second submission is judged on citations alone.
- search_pages variants: 1-3 phrasings per call, pooled and merged by best
  score, prompted as the default ("the bank's printed vocabulary AND your
  own words"). Under-querying becomes over-querying at cent cost.
Both land before the exam re-sit so it runs the best agent.
