## Method

I read `src/` (16.8k LOC repo, 9.1k in src+tests), `README.md`, `docs/design.md`, `evals/gold`, a sample of `evals/results`, and replayed the deterministic layer over the **90 saved `out/*/attribution.json` artifacts** (plus 22 `answer.json`) with read-only `uv run python`. No files written, no API calls. `uv run pytest -q` = 430 passed, 0.53s. Coverage via `uv run --with pytest-cov`.

The strongest evidence available here is that every check writes its own name into the artifact when it fires. So "does this machinery do anything?" is answerable by counting.

---

## Findings, ranked by lines-saved x confidence

### 1. The two shells hold a byte-level clone of the post-answer validation block — ~139 lines, high confidence
`pipeline.py:495-633` and `research_agent.py:1392-1522` (`finalise`). Of the 79 non-comment lines in the pipeline block, **70 match `finalise` exactly** (difflib ratio 0.814; the only real differences are the walk-view setup the agent inlines and a never-firing `unread_pages` branch). Same caps, same fatal grading, same load-bearing walk rule, same 40/85 ceilings, in two places.

It has already drifted: `author.py:281` documents the drift — *"The closed-loop shell has guarded this since it was written and the open-loop author never did, so the same submission was corrected in one shell and shipped in the other."*

Fix: one `finalise(attribution, walks, validation, case, metric_cfg, registry, headline_label)` in `validate.py`, called by both. Nothing in the artifact contract changes.

### 2. The same 11-rule specification is written twice, in two prompts — ~380 lines of prompt, high confidence
`author.py:17-226` (AUTHOR_PROMPT, 2097 words) and `research_agent.py:107-282` (SYSTEM_PROMPT + CASE_PROMPT, 1752 words) carry the **identical named rule set**: NEVER GUESS, BASIS, PERIOD MATCH, CORROBORATE, WALK PREFERENCE, MOVEMENT COLUMN, RATIO VARIANT, EXPLAIN DO NOT RESTATE, CITE THE HEADLINE TOO, SAY WHAT THE WALK HIDES. Reworded, so line-similarity is only 0.156 — which is worse, not better: a rule change must be made twice and the two wordings cannot be diffed. They have already diverged (the agent has CITATION CONTRACT, the author does not). `ask.py:50-86` and `research_agent.py:294-339` are the same story for the question task.

### 3. The unit-declaration subsystem changes **0 of 340** real cap decisions — ~150 lines, high confidence
`validate.py:1109-1258`: `_DECLARED_UNIT_PATTERNS`, `_declarations`, `_declared_grounds`, `_declaration_refuses`, `_same_family`, `MONEY_SCALE_UNSTATED` — the machinery that reads a unit off a table header so a bare cell can ground a claim.

Ablation I ran: replace `quote_states` with a version that keeps glued-suffix conversion and falls back to bare-magnitude match, then re-derive `cap_weakly_cited_claims`'s verdict for every quantified driver in the estate. Result: **340/340 identical (100%)**. On 40,000 randomly paired (real quote, real fact) combinations it changes the answer **40 times (0.10%)** — genuine catches ("Net interest margin (%) 1.99 2.07 (8)bpts" refusing a `2.0 bps` claim), but 1 in 1000.

Wider ablation: the whole 275-line unit-aware citation parser vs a 6-line unit-blind magnitude match agrees on **332/340 (97.6%)**; the 8 disagreements are all bps↔ppt and $m scale cases that `convert_unit` alone (25 lines) already handles.

### 4. Five deterministic checks have never failed on 90 artifacts — ~370 lines + 2 test files, high confidence on the counts
Replayed over every saved artifact:

| check | file:line | pass | fail |
|---|---|---|---|
| `check_movement_variant` | validate.py:824 | 86 | **0** |
| `check_movement_basis` | validate.py:858 | 71 | **0** |
| `check_ratio_level` | validate.py:1532 | 25 | **0** |
| `check_movement_columns` | validate.py:558 | 33 | **0** |
| `check_component_columns` | validate.py:705 | 15 | **0** |

`check_component_columns` is the sharpest case: its gates opened on all 15 bridge artifacts and it built a non-empty "wrong-column delta" pool in 5 of them, and still named zero offenders. It carries ~130 lines of supporting machinery (`_stems_by_period`, `_component_delta_pools`, `_period_tokens`, `half_label`) plus a dedicated 128-line test file.

Each cites a real defect in its comment, so this is (a) evidence-backed. But the defect was fixed twice — once in the prompt, once in code — and the code half has not caught anything since. **Needs ablation**: delete the five checks, re-run `evals run --suite dev` for `cheap` and `agentic`, and compare movement-correct, precision and Brier. If nothing moves, the prompt rule is carrying it.

### 5. Guard normalisers that have fired zero times across 112 artifacts — ~120 lines, high confidence
- `schema.enforce_evidence_gate` driver strip (`schema.py:132-140`) — the flagship "structural never-guess rule": **0** strips in 90 attributions (1 in the question path).
- `author.drop_off_unit_contributions` (`author.py:268-300`) — **0**.
- `author.settle_charge_sign` (`author.py:303-333`) — **0** ("Movement re-signed" never appears).
- percent→bps endpoint lift, written twice (`author.py:425-448` and `research_agent.py:1285-1302`) — **0**.
- `research_agent._keep_valid` malformed-item drop — **0**.
- `pipeline.py:592` `unread_pages` — **0**.
- The agent's final citation gate rejecting a quote — **0** in 54 runs.
- `validate.corroborate`'s cross-source divergence branch (`validate.py:468-486`) — **0 auto-disagreements**; all 89 disagreements in the estate were written by the model. Only the two-line `single_source` cap and the `corroborated_N` marker do work.

### 6. Seven runaway rails on one loop; four have never bound — ~60 lines, high confidence
`config.py:54-63` + `research_agent.py:92-101, 1570-1710`: `max_tool_calls`, `cost_ceiling_usd`, `wall_clock_s`, `HARD_STOP_FACTOR x wall_clock`, `turn_cap = max_tool_calls + 10`, `MAX_PROSE_TURNS`, `MAX_SUBMIT_ATTEMPTS` — each with its own message, its own latch, and a per-call re-check inside the turn loop.

Measured over 54 agent artifacts: **53 recorded `budget_exhausted=no`**. The tool-call budget bound once. Max cost observed $1.62 against a $5.00 ceiling; median $0.108. Wall-clock, hard-stop, and turn-cap never bound. One rail (tool calls) plus the per-call cost check would cover the observed estate.

### 7. `discover.py` — 152 lines, 0% coverage, one manifest, ever
`src/bank_equity_researcher/discover.py` + `cli.py:30-33, 99-106`. Its only product, `manifest/anz.json`, is committed. Nothing imports it, no test touches it, no scorecard reads it. It is the ADR-0004 "agentic pocket" demo. Deleting it changes no test and no scorecard.

### 8. `prototypes/` — 504 lines including a second OpenRouter client
`prototypes/bakeoff.py` (230), `chart_reading.py` (148), `openrouter_client.py` (126, "Throwaway by design"). Referenced only by two `.scratch` tickets. Not imported by `src/`, `tests/`, or `scripts/`. This is ticket 13/14 evidence, and the tickets already record the results.

### 9. `DOC_TYPE_RANK` is copied with **different values** — real drift, small but live
`pipeline.py:210` has `asx_announcement: 2`, default 3. `ask.py:34` has `pre_results_note: 2, asx_announcement: 3`, default 4. The `ask.py` comment says the copy exists because *"pipeline.py is not importable state"* — that is a symptom of the rank living inside `run_case` rather than beside the taxonomy. Same source hierarchy, two answers.

### 10. The "confidently-wrong = 0.0" headline is partly a threshold construction
`CLAIM_CITATION_CAP = 80` (`validate.py:1037`) sits exactly one notch under `CONFIDENT_THRESHOLD = 85` (`evals.py:46`). Every cap in the ladder writes 80, so **any claim a cap touches is by construction excluded from the metric the README leads with**.

Counterfactual ablation (assume an uncapped claim would have self-reported 90):

| arm | Brier as shipped | Brier uncapped | conf-wrong as shipped | conf-wrong uncapped |
|---|---|---|---|---|
| cheap | 0.073 | 0.081 | 0.0 | 0.073 |
| agentic | 0.082 | 0.086 | 0.0 | 0.050 |

So the caps buy the headline number and almost no Brier. The reliability tables confirm the shape: every 85-94 bucket is 100% correct and all the wrongness sits in 70-84 — where the caps put it. Two of the caps (`comparison_leak_cap_80`, `component_column_cap_80`) never fire at all; three do the work (`computed_delta_cap_80` 64x, `unreconciled_bridge_cap_80` 17x, `failed_walk_cap_80` 8x) plus `single_source`→85 (190x, the most-used override in the system, and the only one whose ceiling sits *on* the threshold rather than below it).

**Named ablation**: run the dev suite with `cap_weakly_cited_claims`, `cap_unreconciled_drivers` and `cap_drivers_on_failed_walks` disabled, and report Brier + confidently-wrong from the real self-reports. That is the only way to know whether the model's own confidence is already calibrated, or whether code is doing the calibrating.

### 11. Reference-following costs 461 lines and yields 7 cited facts
`refs.py` (461 lines) + `pipeline.py:236-247, 306-323` + the agent's `follow_references` tool. Across 36 pipeline artifacts it produced **108 evidence records in 8 artifacts, of which answers cited 7**. Compare the annotation layer (`extract.py:314-349`, ~90 lines, one extra vision call per walk page): **235 records, 145 cited** — that one earns its place decisively.

The design doc credits reference-following with the 0/15 → 3/15 checklist lift. That is the ablation to re-run, because a 6.5% citation rate on the records it mints is thin. It also carries **seven hand-tuned constants** (`refs.py:39-60`: `MAX_FOLLOWED_PAGES 4`, `MAX_PAGES_PER_NOTE 4`, `_HEADING_MAX_LINE 20`, `_INDEX_PAGE_HEADINGS 3`, `_MAX_PRINTED_OFFSET 40`, `_TARGET_PROBE_LINES 20`, `_MIN_RELEVANCE 2`), none of which cites a measured run.

### 12. The eval decides only 44% of the claims it grades
`evals/results/cheap-dev-final.md`: `scored_claims: 42, unscored_claims: 54, cases_scored: 9, cases: 25`. Precision, recall, Brier and the confidently-wrong rate all rest on 42 claims from **9 of 25 cases**. The three-state scorer is right to refuse an unverified gold value, but the headline "25 cases" oversells what is measured. Also: README says Brier 0.035 and 36/36 at 85+; the current final scorecards say 0.073 with 32 claims at 85+ (cheap) and 0.082 with 33 (agentic). Documentation drift.

### 13. Four near-parallel scorecard writers in `evals.py` — ~350 lines
`run_suite` (929), `run_answer_suite` (266), `run_judge_suite` (1053), `rescore` (1222), each with its own run loop, `.jsonl` writer and markdown table assembly (`scorecard_lines`, `judge_scorecard_lines`, `delta_table_lines`, plus 55 lines of inline table building inside `run_answer_suite`). The `--since/--until/--baseline/--label` rescore flags (`cli.py:44-52`) produced exactly one `rescore-*-newscorer` pair in the whole results history.

### 14. Dead scaffolding — ~25 lines, certain
- `render.py:73` computes `narrative` and `render.py:106` does `del narrative` — the local is never read.
- `config.py:19` (`deepseek-v4-flash-0731`), `:22` (`stealth/ox-alpha`), `:32` (`claude-sonnet-5`) — price entries for models no combo names and no artifact records.
- `config.py:123-134` `agentic-luna` — combo added 2026-08-31, zero artifacts.
- `__init__.py:1` `hello()` — uv template scaffolding.
- `validate.py:480` `reason=DisagreementReason.rounding if gap <= 3 else ...` — a bare magic 3 with no comment, in the branch that has never fired (finding 5).

### 15. What I would not build fresh
Two orchestration shells, two 2000-word rule specifications, two validation blocks, and a 1800-line deterministic checker — to run **one closed-loop agent** whose measured advantage over the cheap arm is zero on movements (25/25 both) and slightly *worse* on Brier (0.082 vs 0.073). The design doc's own thesis is that the "why" layer is loop-dependent and the numbers are not. If that thesis holds, the pipeline arm (`pipeline.py` 661 + `author.py` 505 + `ask.py` 289 ≈ 1455 lines) is a **control**, and a control should be frozen at a git tag, not maintained line-for-line alongside the product. Every finding above except 7, 8 and 14 exists because it is maintained live in two places.

---

## Hardcoded-override register, classified

The `validate.py:6-13` policy says each override must cite the run that justifies it. Audited against that rule:

**(a) evidence-backed and still firing — keep:** `CLAIM_CITATION_CAP 80` (validate.py:1037, 64x), `computed_delta_cap_80` (1460), `unreconciled_bridge_cap_80` (1676, 17x), `failed_walk_cap_80` (1722, 8x), fatal→40 (pipeline.py:600 / research_agent.py:1503), no-primary-walk→85 (pipeline.py:617-633), `DriverClaim.confidence` default 40 (schema.py:56), the printed-precision tolerances (validate.py:22-43), `IDENTITY_SCALE` (959), `_YEAR_RANGE` (1076), `_LABEL_INDEX_CEILING` (1265), page budgets (pipeline.py:53-64), the llm deadline constants (llm.py:34-40).

**(a) evidence-backed but never fires — deletion candidates under the policy's own last sentence:** `comparison_leak` cap 80 (validate.py:537), `component_column` cap 80 (770), `RATIO_LEVEL_CEILING 200.0` (1529), off-unit→60 (author.py:294), stripped-claim→20 (schema.py:140).

**(b) plausible but unevidenced — no run, defect number or artifact cited:**
- `single_source → 85` (validate.py:491) — cites "user, 2026-08-26", a directive not a measurement. 190 firings, the system's most consequential override.
- underlying/notable split → 80 (pipeline.py:518, research_agent.py:1446) — 12 firings, and the comment gives a *rationale* ("a framing choice the disclosure does not settle") with no run behind it.
- `ANSWER_GATE_CONFIDENCE_CAP = 20` (schema.py:149).
- `CONFIDENT_THRESHOLD = 85` (evals.py:46) — definitional, and it interacts with every 80-cap (finding 10).
- `CROSSREF_COVERAGE_PASS 1.0` / `CROSSREF_FACT_PASS 0.75` (evals.py:230, 235) — "one flagged fact in a four-fact case" is a hand-set bar.
- `MAX_QUOTES 24` / `MAX_ANSWER_CHARS 6000` / `MAX_QUOTE_CHARS 4000` (judge.py:69-71) — and this one is not inert: **the 24-quote window binds in 25 of 90 artifacts**, so a quarter of the estate is judged on truncated grounding. The questions suite already had to widen it to 48 (evals.py:302); the metric suite never did.
- `cited_quotes` driver/headline room split (judge.py:452) — intricate, unmeasured.
- `CORROBORATION_TOL 1.5` (validate.py:40), `COMPONENT_TOL 2.0` (48).
- `refs.py:39-60`, seven constants.
- `research_agent.py:85-101`, seven loop constants (four never bind).
- `ask.py:26-29` `MAX_ASK_PAGES 12` / `MAX_PAGES_PER_DOC 6`.
- The `taxonomy.py` `method_hint` blocks — the impairment hint alone is ~30 lines of prescribed analyst method. These are the largest unevidenced overrides of agent judgment in the repo, and they are the ones a stronger model is most likely to make obsolete.

**(c) unnecessary on its face:** `validate.py:480` `gap <= 3` (bare magic number choosing a disagreement reason, in a never-firing branch); `render.py:73/106` dead local; the three unused `PRICES` entries and `agentic-luna`.

---

## What I could not prove — the exact experiments

1. **The five never-firing checks (finding 4).** Delete them, re-run `evals run --suite dev` for `cheap` and `agentic`, diff movement-correct / precision / Brier against `evals/results/*-dev-final.md`. Zero delta = the prompt rules carry it.
2. **The confidence caps (finding 10).** Disable `cap_weakly_cited_claims` / `cap_unreconciled_drivers` / `cap_drivers_on_failed_walks`, re-run, read Brier and confidently-wrong off the scorecard. This is the one experiment that says whether the model is calibrated or whether code is calibrating it.
3. **Reference-following (finding 11).** Re-run the four bake-off anchors with `follow_references` returning `[]`, and re-run `bakeoff_judge.py`. The design doc claims 0/15 → 3/15; that claim is now three iterations old.
4. **The citation parser (finding 3).** Already run: 340/340 unchanged. What I could not test is whether the declaration machinery prevents *bad extractions from ever being minted* upstream in `extract._numbers_the_quote_prints` — the dropped facts are not persisted. Instrument that path for one dev-suite run and count.
5. **The pipeline arm as a live product (finding 15).** Freeze `pipeline.py` + `author.py` + `ask.py` at a tag, delete from `main`, re-run the agentic suite. If nothing changes, the control was never a product and the duplication was never necessary.