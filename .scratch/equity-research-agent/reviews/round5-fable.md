All verification is done. Here is the round-5 report.

---

# Round 5 — Fable reviewer, read-only @ 4e21e27

I read all six archived reports and the full round log first. I skip all 47 fixed items and every known-open item. The test suite passes at this commit (420 passed). Every finding below carries an executed repro or an executed reference census.

**Verdict up front:** the scoring and validation core has NORMALISED — I found no new correctness defect in `validate.py`, `evals.py` scoring, `judge.py`, or the submission path of `research_agent.py`. The four real new issues below all sit at the edges: the grace ladder's classifier, CLI text, one harness entry point, and dead code from the collapse. None changes a shipped verdict.

## 1. MEDIUM — the grace ladder does not recognise the timeout shape of a network gap

**File:** `src/bank_equity_researcher/llm.py:120-129` (`_NETWORK_ERROR_MARKS`, `_network_error`), used at `llm.py:221` and `llm.py:291`.

**Claim.** The classifier matches error message substrings. It covers DNS failure, connection refused, connection reset, no route, and network unreachable. It does not cover the timeout shape. Executed repro:

```
ConnectError '[Errno 8] nodename nor servname ...'  grace=True
ConnectError '[Errno 61] Connection refused'        grace=True
ConnectTimeout 'timed out'                          grace=False
ConnectTimeout ''                                   grace=False
ConnectError '[Errno 60] Operation timed out'       grace=False
ReadTimeout 'timed out'                             grace=False
```

**Failure scenario.** The ladder's own comment names mobile-hotspot gaps as its reason to exist. In a hotspot gap the router often stays up and DROPS packets silently. Then `CHUNK_TIMEOUT` (connect=20.0, `llm.py:40`) raises `httpx.ConnectTimeout`, or the OS raises ETIMEDOUT ("[Errno 60] Operation timed out"). Neither string matches a mark. The call then burns the five normal attempts in about three minutes and the 20-minute case dies inside the gap — the exact failure the commit c2b0dcf exists to prevent. Only the gap modes where the router answers (DNS failure, refusal, reset) get grace.

**Severity:** MEDIUM. Infra only; no scoring effect. It matters most for the sealed-exam runs on hotspots.

**Suggested fix.** Classify connect-phase failures by TYPE, not by message: `isinstance(exc, (httpx.ConnectError, httpx.ConnectTimeout))` grants grace, plus the existing marks for anything else. Keep read-phase timeouts fail-fast: a mid-body stall can be one stuck provider route, and the retry-on-another-route design handles that better.

**Verification.** Executed classifier repro above; re-run it after the fix and add the six shapes as unit cases.

## 2. MEDIUM-LOW — the CLI help documents combos that no longer exist

**File:** `src/bank_equity_researcher/cli.py:18-19, 27-28, 39-40`.

**Claim.** Three `--combo` help strings read "agentic | agentic-glm | agentic-cheap". `COMBOS` holds only `agentic` since the collapse (config.py:65-87). Executed repro: `runner_for("agentic-cheap")` raises `KeyError: "unknown combo: agentic-cheap (known: agentic). The open-loop combos 'cheap' and 'normal' were frozen ..."`.

**Failure scenario.** A user follows the help text and the command fails. The error message compounds the confusion: it explains the open-loop freeze, but `agentic-cheap` was a closed-loop combo retired separately.

**Severity:** MEDIUM-LOW. User-facing text; deterministic failure; trivial fix.

**Suggested fix.** The three help strings say `agentic`. The `evals --combo` help keeps its correct rescore note. Optionally `_require_agent`'s message says "retired combos are frozen in git history" instead of naming only 'cheap' and 'normal'.

**Verification.** Repro above; read of config.py COMBOS.

## 3. MEDIUM-LOW — `evals judge` cannot grade the frozen-baseline artifacts, and its own default crashes

**File:** `src/bank_equity_researcher/evals.py:1054-1058` (`run_judge_suite`).

**Claim.** The judge action reads SAVED `out/*/` artifacts and runs no shell — the same class as `rescore`. `rescore` deliberately accepts retired combo names (it uses the combo only for the slug; the CLI help and config._require_agent's docstring both promise this). `run_judge_suite` instead reads `COMBOS[combo].judges` on its first line, so any retired name raises a raw `KeyError`. Its own default is `combo="cheap"` — a retired name — so `run_judge_suite()` with defaults crashes. Executed: `COMBOS['cheap']` → `KeyError: 'cheap'`. The frozen-baseline artifacts are still present (`out/anz-nim-1h26-vs-1h25-cheap`, …) and now have no judge path.

**Failure scenario.** A comparison of the frozen baseline against the product combo needs the checklist judge over the `-cheap` slugs. The command dies before any work.

**Severity:** MEDIUM-LOW. Blocks one documented workflow; no silent wrong number.

**Suggested fix.** Take the judge models from the one live combo (`COMBOS["agentic"].judges`) and keep the `combo` argument as the slug selector, exactly as `rescore` treats it. Change both stale defaults (`run_judge_suite` and `rescore` carry `combo="cheap"`) to `"agentic"`.

**Verification.** Repro above; read of `rescore` (evals.py:1233-1272) confirming it never touches COMBOS.

## 4. LOW — the collapse left an orphaned author-retry and extractor estate, kept green by its own tests

**Files and executed reference census (zero callers in src/):**

- `extract.py:159` `extract_text_evidence` and `extract.py:202` `_numbers_the_quote_prints` — zero references anywhere, tests included. `TEXT_PROMPT` (extract.py:13) and `WALK_PAGE_HINT` (extract.py:126) likewise.
- `validate.py:1917` `sign_flip_hint`, `validate.py:956` `implied_residual`, `validate.py:816` `unclaimed_components` — referenced only by `tests/test_review_round2.py` and `tests/test_review_round3.py`.
- `refs.py:434` `extraction_hint` — referenced only by `tests/test_refs.py`.
- `taxonomy.py`: three config keys nothing reads any more — `walk_markers`, `extract_focus`, `component_labels` (the last fed only `unclaimed_components`). The comment at taxonomy.py:233 says "author.py reads this flag"; `validate.settle_charge_sign` reads it now.
- Stale comments that cite the deleted module as live code: `research_agent.py:1305` and `:1353` ("author.py carries the same repair").

**The functional wrinkle, stated plainly.** `sign_flip_hint` and `unclaimed_components` were retry-feedback mitigations. Only the deleted open-loop author retry consumed them. The surviving closed loop has no validation retry, so these two mitigations are unreachable by construction — they are not "temporarily unwired", they have no consumer. Their companion caps survive and run (`cap_unreconciled_drivers`, both shells' `if fatal:` path), so no calibration protection was lost. A future decision is either to delete the helpers with their tests, or to feed the hints back into the loop as a post-`finalise` turn.

**Severity:** LOW. Dead code plus tests asserting retired behaviour; no live effect.

**Suggested fix.** Delete the five functions, the two prompts, the three taxonomy keys, and their review-round tests, or file the retry-feedback decision as its own ticket first. Fix the two comments.

**Verification.** AST-based caller census over src/, confirmed by grep over src/ and tests/.

## Grace-ladder audit (priority 2) — the loop itself is sound

I audited the while-loop restructure in both `chat` and `chat_tools` adversarially. No starvation and no infinite loop exists: every path increments `attempt`, increments the bounded `grace` (max 12), or removes `"reasoning"` exactly once. The 400-reasoning `continue` is single-shot because the pop is unconditional; a second 400 raises and consumes an attempt. The 429 path accounts correctly and exits with the 429 as `last_error`. Grace is a local counter per call, so one call can never inherit another's spent grace. Two notes, not findings:

- The final 429 sleep is wasted: on the fifth 429 the code sleeps 75s and then exits the loop (llm.py:204-206). One line reorders it.
- The known-open "LLM-side retry deadline" item (round-2 not-re-reported list) is now larger: one `chat_tools` call can legally hold ~9-10 minutes of grace sleeps, and each of up to 17 posts carries its own 320s streaming deadline at 16k tokens. The research loop reads its wall clock only between calls, so one stuck call can exceed the 45-minute hard stop. Same item, new magnitude; it deserves its own decision, not a blind fix.

Also noted: the round-4 "left undone" item about the percent-to-bps lift keeping the model's unit label named `author.py:425`. That file is gone; the live copy of the same code is `research_agent.py:1283-1300`. The item stays open at the new address.

## Checked and found clean

- `research_loop`: post-submit atomicity, per-call budget ladder, exhaustion latching, the turn cap, and the mid-turn latch path (the tool-result text carries the submit instruction where the user message does not).
- `build_records` / `_resolve_evidence` id remapping, and the carried-in cited-record rule in both `build_attribution` and `build_answer`.
- `finalise` cap order matches the round-3 cap-stack trace; `check_ratio_level` and `settle_ratio_scale` both key on the metric's unit.
- The ticket-33 cap deletions (`single_source` override, `comparison_leak_cap_80`, `component_column_cap_80`, the off-unit-60 and strip-20 overrides) each carry their replayed evidence in comments and match the caps-off ablation the brief describes; the fatal-path caps that guard the confidently-wrong metric all survive.
- I suspected `score_crossref` reads `fact.get("evidence")` while the agent emits `citations`; refuted — `enforce_answer_gate` normalises to `evidence` (schema.py:183).
- I suspected `walk_endpoints` breaks on comma-formatted endpoints; refuted — `extract_walk` stamps bare floats into the quote.
- `DriverClaim.confidence` now defaults to 40 with a null validator, closing the round-3 crash item.
- corpus/retrieve hold the documented stem-cache invariant with the `all_documents()` guard; the content-hash key stays known-deferred.
- `judge.py` verdict combination, quote budgeting, and the flag split; `calibration` and `crossref_passes`; `discover.py`; `render.py`.

**Stop-signal assessment:** four real new issues, so the formal threshold for "normalised" is not met — but none is a correctness defect in the measurement core, and none changes any shipped verdict. The defect classes the first four rounds hunted are, on this evidence, exhausted; what remains is collapse hygiene and one infra classifier.