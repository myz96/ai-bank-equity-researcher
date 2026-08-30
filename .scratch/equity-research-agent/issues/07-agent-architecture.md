# 07 — Agent architecture

Type: grilling
Status: resolved
Blocked by: 03, 06

## Question

What is the orchestration shape? Decide: a single agent with tools vs a staged pipeline, the tool surface the model can call, where document acquisition sits, how the source hierarchy resolves disagreement between documents, which pipeline stages run on the cheap model vs the normal model, and the CLI/library entry points the evaluators will call.

## Answer

Resolved with the user (grilling, 2026-08-25):

1. **Orchestration is decided empirically, not by instinct.** All candidate shapes share one deterministic tool layer (corpus, retrieval, extraction, vision, validation, rendering). The POC (ticket 19) runs two thin shells over identical tools — (a) a Python pipeline with one bounded evidence-request loop, (b) a single tool-calling agent where the author model drives — and compares correctness vs gold, tokens, context size, latency. A parent-with-subagents shape is deferred: evidence records already compress context hard, so subagent isolation only earns its complexity if measured context pressure appears. User instinct: single agent with tools; the measurement settles it.
2. **Source hierarchy**: audited/reviewed statements and PA tables > PA narrative > presentation/IDP > transcripts > else; restated comparatives from the newer document win. **User amendment**: every disagreement record must classify *why* the sources differ — `definitional | rounding | restatement | timing | error` — because a definitional gap (cash vs statutory) is analysis, not noise.
3. **Model roles in combo configs**, no names hardcoded: extract/vision `qwen3.7-flash`; author `glm-5.3` behind a reasoning-aware client; author fallback `deepseek-v4-pro-0813`; judges `deepseek-v4-pro` + `qwen3.7-flash`. **`ox-alpha` is out of the combos for now** (rate-limited despite strong quality); revisit if its limits ease.
4. **CLI**: `analyse --bank --metric --period [--comparator] [--combo]` writing `out/<case>/attribution.json` + `report.md`; same call as a library; `evals run` for the harness.
5. **Never-guess is enforced in code, not prompt** (user: guessing is extremely bad): schema validation rejects any quantified claim without evidence-record references; an unsupported number is stripped, moved to the limitations section, and the strip is logged in the output. Prompt reinforces; evals punish; but the structural gate is what guarantees it. Insufficient evidence ships as a partial attribution with low confidence and explicit limitations.

### Closed-loop research agent (2026-08-30)

ADR-0005 is built. `src/bank_equity_researcher/research_agent.py` (1421 lines,
about half of it the system prompt and the tool schemas) is orchestration
shell B: the model reads, reasons and chooses what to read next. The artifact
contract, the validators and the confidence caps are unchanged, so the eval
harness scores the agent exactly as it scores the pipeline.

**What was built**

- `research_agent.py` (new): the tool loop, the citation gate, the submit
  path, and `finalise()` — the pipeline's own output-level checks and caps,
  applied to the agent's answer with the same functions and thresholds.
- `llm.py` (+103): `chat_tools()` under `chat()`'s deadline/retry discipline;
  `with_cache_breakpoint()`; `Usage.add(cost_usd=...)` prefers the price the
  provider reports.
- `config.py` (+54): `Combo` gains `orchestration`, `agent`,
  `agent_max_tokens`, `max_tool_calls`, `cost_ceiling_usd`, `wall_clock_s`,
  all defaulted; combos `agentic` and `agentic-cheap`.
- `cli.py` (+11): `--combo` routes on `orchestration`; `analyse` now defaults
  to `agentic`.
- `tests/test_research_agent.py` (48 tests), `tests/test_llm_tools.py` (6).
  Suite: 226 pass, no network, the model faked throughout.

**Tools** (each a thin adapter over a function the pipeline already calls):
`search_pages`, `read_page`, `read_chart` (`extract_walk`, then
`annotate_walks` so the agent sees the comparison classification),
`cite`, `follow_references` (`refs.scan_page`), `bank_language`, `submit`.

`cite` was added after the first live probe. The agent had reached PDF p118 and
computed the right bridge, but its quotes failed the verbatim check at submit
time and the budget ran out before it could correct them, so the citation gate
stripped the whole bridge. Verification belongs where the reading happens:
`cite` checks a page's quotes at once, mints records with ids, and `submit`
then cites by id.

**Model choice.** The OpenRouter catalogue was read live.
`anthropic/claude-opus-5` is the newest Anthropic model (2026-07-24) and the
top of the Opus line, above `claude-sonnet-5` (2026-06-30) and
`claude-fable-5` (2026-06-09). A live tool-call probe passed for opus-5,
sonnet-5, qwen3.7-flash and glm-5.3: each emitted a well-formed call, read the
result and called the next tool. `agentic` therefore runs opus-5;
`agentic-cheap` runs qwen3.7-flash (glm-5.3 stays the documented fallback).

**Anchor results** (CBA; movements compared against the pipeline's committed
`out/*-cheap` artifacts at git HEAD; every movement MATCHES):

| combo | case | movement | pipeline | conf | cost | secs | calls | p118 |
|---|---|---|---|---|---|---|---|---|
| agentic | nim FY26 | 208->205 (-3bps) | same | 93 | $0.48 | 139 | 18 | - |
| agentic | cash_earnings FY26 | +730$m | same | 91 | $1.57 | 273 | 40 | - |
| agentic | impairment FY26 | +62$m | same | 86 | $0.58 | 129 | 22 | YES |
| agentic | nim FY21 | 207->203 (-4bps) | same | 93 | $0.49 | 111 | 16 | - |
| agentic-cheap | nim FY26 | 208->205 (-3bps) | same | 90 | $0.011 | 123 | 26 | - |
| agentic-cheap | cash_earnings FY26 | +730$m | same | 85 | $0.043 | 160 | 45 | - |
| agentic-cheap | impairment FY26 | +62$m | same | 75 | $0.032 | 142 | 40 | - |
| agentic-cheap | nim FY21 | 207->203 (-4bps) | same | 88 | $0.035 | 167 | 34 | - |

Both arms reproduce every driver table the pipeline publishes, including the
impairment bridge (+150 / -17 / -71, zero residual). `evals rescore` over the
saved artifacts, harness unmodified: agentic 4/4 movements, 7/7 recall and 7/7
precision on both NIM cases, 4/4 on cash earnings, brier 0.010,
confidently-wrong 0.0, 17/17 at 85-94. agentic-cheap: 4/4 movements, same
recall, brier 0.016, confidently-wrong 0.0.

**p118.** Only `agentic` reaches Note 2.2 on PDF p118 by itself and cites it:
it read the income statement, called `follow_references`, turned to the note,
and quoted four provision-type rows. `agentic-cheap` produced the same three
numbers without ever citing p118 (see the defect below).

**Prompt caching.** A tool loop re-sends its transcript every turn, so an
uncached opus-5 run priced out at about $3 a case. One `cache_control`
breakpoint on the last message cut the CBA impairment case from an estimated
$3.1 to $0.53 (measured on a probe: 6232 prompt tokens, $0.039 written,
$0.0038 read back). Providers outside `CACHE_BREAKPOINT_PREFIXES` get the
transcript unchanged.

**Pipeline untouched.** `evals run --suite dev --combo cheap` ran to completion
with these changes in the tree (`evals/results/20260830-1247-cheap-dev.md`):
24/25 movements OK, brier 0.051, confidently-wrong 0.0, 34/34 correct at 85-94.
The one miss, CBA-cet1-1H26, is NOT from this work: it is already WRONG in
`evals/results/20260830-0341-cheap-dev.md`, written before this session opened
a file, and its cause is visible in the artifact (the movement is read from the
"CET1 Level 2" row, 1260 -> 1230, instead of the headline row 1220 -> 1230).
It belongs to the concurrent iteration-3 work. Nothing here can reach the
pipeline: `Usage.add` gained a defaulted keyword, `chat()` is unchanged,
`with_cache_breakpoint` is called only from `chat_tools`, the `cheap` and
`normal` combos are unchanged, and `research_agent` is imported by nothing the
pipeline runs.

**Failures found and fixed during the round**

1. Submit-time-only verification starved the impairment case (above) -> `cite`.
2. Quotes were stored with the PDF's own line breaks, so a multi-line quote
   escaped the report's `>` prefix and would have reached the judge as the
   note's own prose -> a record stores one line.
3. A rejected submission returned early and left its neighbours in the same
   turn unanswered, which a provider rejects outright -> every call in a turn
   is answered.
4. The first budget to run out LATCHED, so a model that kept calling tools it
   was no longer offered never met another budget. The agentic-cheap
   impairment case hung on exactly this -> a turn bound and a hard wall-clock
   stop that no reply can talk past.
5. A `bps` contribution entered a `$m` bridge (agentic cash_earnings, first
   run: `nii.margin` -3, summed as -3 dollars) -> a contribution not in the
   movement's unit is reported in the narrative, not as a contribution.
6. One malformed sub-object used to raise and discard a whole research run ->
   it is dropped and named in limitations.

**Left undone / findings for the next round**

- WEAK CITATION, both shells. `enforce_evidence_gate` requires a driver to cite
  a RESOLVABLE record, not one whose numbers support the claim. The
  agentic-cheap impairment run shipped +150 / -17 / -71 at confidence 85 citing
  two `walk_vision` records that read "FY25 72.6 -> FY26 78.8" and "FY25 0.0 ->
  FY26 0.071" off pages 24 and 29. The values are right and the run is honest
  about its pages, but nothing grounds them. `computed_delta_cap_80` does this
  for `bridge_extraction` only; impairment is `note_decomposition`. Deliberately
  NOT fixed here: it lives in the shared validators, and changing one shell's
  semantics mid-round would break the comparison.
- The 40-call rail BINDS on the two densest cases (cash earnings on both arms,
  impairment on agentic-cheap), so it is shaping runs, which ADR-0005 point 5
  says a rail must not do. A turn can also overshoot it, because the check runs
  once per turn and a turn may carry several calls (45 and 54 observed).
- `read_chart` will read a chart off any page it is pointed at, including pages
  with no chart, and returns a walk that is then classified and pooled. The
  cheap arm did this three times on the impairment case.
- Not measured: the narrative checklist (`scripts/bakeoff_judge.py`), the full
  25-case dev suite on either agentic combo, and any bank other than CBA.

### Question mode (2026-08-30)

Codex critique finding 7 said: do not maintain a second open-loop author; merge
`ask` into the research loop with a smaller submit payload. That is built. One
loop, one tool surface, one citation gate and one artifact now serve both
tasks - a metric movement and a free-form research question.

**What was built**

- `research_agent.research_loop(llm, combo, research, messages, submit_spec,
  started)` - the loop, lifted out of `run_agent_case` and given the submit
  schema as a parameter. Both tasks drive the same copy, so the budgets, the
  latch, the turn bound, the prose nudge and the submit-rejection retry are one
  piece of code and a fix to any of them reaches both.
- `research_agent.run_agent_question(bank, question, combo, periods)` - the
  question shell. It resolves the scope, runs the loop with
  `QUESTION_SUBMIT_SPEC`, and writes `out/ask-<slug>-<combo>/answer.md` and
  `answer.json` with the provenance the movement artifact carries (models,
  cost, seconds, tool calls, pages read, charts read, orchestration "agent",
  budget_exhausted).
- The submit payload is `{answer, key_facts:[{fact, citations}], confidence,
  limitations}` over the SAME `evidence` schema object the movement submit uses
  (`_EVIDENCE_SCHEMA`, shared by identity and pinned by a test). The citation
  gate is unchanged: `build_records` re-checks every quote against its page.
- `schema.enforce_answer_gate` - the never-guess gate for an answer, moved out
  of `ask.py` and shared by both shells. A key fact with a number and no
  resolvable citation is deleted, the deletion is named in limitations, and an
  answer with nothing left is capped at confidence 20.
- `corpus.documents_for_question` - the scope of a question, read from the
  question's own words (`banks_named`, `periods_named`), with the bank and the
  periods as optional hints. The bank vocabulary comes from the registry's
  `full_name`, never from a hand-written table.
- `corpus.doc_alias_index` / `resolve_doc_name` - a document named as a person
  writes it ("WBC/FY25/presentation-and-IDP") resolves onto its doc_id
  ("WBC/FY25/investor_discussion_pack") through the manifest's own file names.
  All 4 crossref and all 12 researcher-question gold names resolve.
- `config.question_runner_for(combo)` - the second routing point, the twin of
  `runner_for`. Both runners take `(bank, question, combo, periods)` and return
  `(output, out_dir)`, so no caller needs an adapter or a branch of its own.
- `evals.run_answer_suite(kind, gold_cases, combo)` - ONE runner and one
  scorecard writer for both answer suites (finding 8). `run_crossref_suite` and
  `run_question_suite` are wrappers that differ only in the gold they load, and
  both route through `question_runner_for`, so a crossref run can no longer
  measure the baseline while wearing the agent's label (finding 1).
- `evals.load_question_gold(split, bank)` and the `evals run --suite questions`
  route. Scoring is `score_crossref` unchanged apart from one new argument, the
  doc-name index.

**Reused, not rewritten**

- `ask.py` keeps its retrieval, page budgeting, extraction and author rounds:
  it is still the measured open-loop control, reachable at `--combo cheap`. It
  lost its private evidence gate to the shared one, `_slugify` became public
  `slugify`, and `render_answer` now renders both shells' artifacts.
- `evals.py`: the scorer, the pass rule, the two-judge protocol and the
  scorecard layout are untouched; only the run loop was generalised.
- The metric `SYSTEM_PROMPT` is byte-identical apart from ONE word: rule 1 now
  reads "a quantified claim" where it read "a quantified driver", because the
  rule is now shared (`NEVER_GUESS_RULES`). `HOW_TO_RESEARCH` (the tool
  descriptions) and the budget note are shared too.

**The two probes** (`evals run --suite questions --only
nab-business-growth-quality`)

| Arm | Coverage | Fact accuracy | Flagged | Conf | Tool calls | Pages | Cost | Seconds |
|---|---|---|---|---|---|---|---|---|
| agentic-cheap (qwen3.7-flash) | 1/3 | 0/4 | 1 | 78 | 31 | 10 | $0.0117 | 114 |
| agentic (opus-5) | 3/3 | 0/4 | 2 | 83 | 31 | 14 | $0.7431 | 209 |

Scorecards: `evals/results/20260830-1345-agentic-cheap-questions.md` and
`evals/results/20260830-1347-agentic-questions.md`. Artifacts:
`out/ask-assess-whether-nab-s-fy25-business-private-banking-{agentic,agentic-cheap}/`.
The opus arm cited all three required pages, minted 50 records over 14 pages,
and wrote 19 key facts; the cheap arm answered mostly out of the results book
and reached one required page. Both artifacts validate and every citation is a
verbatim quote from a real page.

**Findings from the probes**

1. FACT ACCURACY IS NOT COVERAGE, AND THE JUDGE WINDOW BINDS. The opus answer
   scored 0/4 with full coverage. Two facts are judge splits, not failures.
   The other two fail on entailment: the researcher-question gold facts are
   long conjunctions of printed values ("the chart shows X and Y and the page
   also states Z"), and `judge.py` requires EVERY load-bearing number to appear
   in the cited quotes. The answer cited 39 records; `MAX_QUOTES = 24` means 15
   of them never reached the entailment judge. A more thorough answer therefore
   loses grounding it actually has. NOT changed here - the caps are part of the
   frozen protocol and moving them mid-round would break comparability with the
   crossref set - but the head-to-head must read fact accuracy with this in
   mind, or measure it after raising the window for BOTH arms.
2. The cheap arm reads the results book and the opus arm reads both documents.
   The gold locates this question's answer in the investor presentation, so the
   coverage gap (1/3 against 3/3) is a real difference in reading strategy, not
   a harness artifact.
3. `read_chart` was never called by either arm on this question. The chart
   pages the gold points at (p49, p50, p27) were read as text, and the text
   layer carried enough. In question mode a chart is stamped "unclassified"
   because a question fixes no comparison to classify against.

**Left undone**

- The other four dev questions are unrun on purpose (Monday's head-to-head).
- `ask` on `--combo cheap` was not re-run against the live corpus. It is now
  covered offline end to end (finding 7 asked for that test), which pins the
  signature, the shared gate and the artifact shape, but the baseline arm's
  answer quality on these questions is still unmeasured.
- The answer note ran to 460 words against a 400-word instruction. The cap is
  not enforced in code, unlike the movement headline's.
