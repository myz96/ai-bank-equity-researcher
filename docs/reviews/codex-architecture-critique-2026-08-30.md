## Ranked findings

### 1. The eval command can silently evaluate the baseline when asked to evaluate the product

- **Claim:** `evals run --combo agentic` still calls the open-loop pipeline, so the primary harness does not reliably measure the product selected by the combo.
- **Evidence:** `Combo.orchestration` distinguishes the shells in [config.py:42](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/config.py:42), and `analyse` respects it in [cli.py:93](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/cli.py:93), but `run_suite` imports `pipeline.run_case` unconditionally in [evals.py:802](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/evals.py:802). The routing test covers only `analyse`, not evals, in [test_research_agent.py:883](/Users/michaelzhao/swe/ai-bank-equity-researcher/tests/test_research_agent.py:883).
- **Action:** **merge** routing into one `runner_for(combo)` function used by CLI and evals.
- **Estimated savings:** 0–10 lines, but removes a high-impact measurement ambiguity.
- **Risk/test:** Low. Add a test asserting `run_suite(..., combo="agentic")` invokes `run_agent_case`, while `cheap` invokes the pipeline.

### 2. Submission normalisation and final validation policy are duplicated between the two shells

- **Claim:** The same answer-contract policy exists in two implementations and is already at risk of drifting.
- **Evidence:** Pipeline post-processing, confidence caps, fatal/peripheral classification and limitations occupy [pipeline.py:450](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/pipeline.py:450) through line 590; almost the same policy is repeated in [research_agent.py:1054](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1054) through line 1181. Likewise, movement/basis/unit normalisation in [author.py:383](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/author.py:383) is reimplemented in [research_agent.py:915](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:915).
- **Action:** **merge** into answerer-agnostic `build_attribution()` and `finalise_attribution()` functions. Both shells should supply records, walks, case context and raw submission, then stop owning policy.
- **Estimated savings:** 180–260 lines.
- **Risk/test:** Medium because the policy is load-bearing. Create table-driven tests that pass one raw submission through both adapters and assert identical `Attribution` JSON, failures, limitations and confidence caps. Existing tests have only two direct finaliser cases at [test_research_agent.py:629](/Users/michaelzhao/swe/ai-bank-equity-researcher/tests/test_research_agent.py:629).

### 3. The submit path supports two citation protocols when one is sufficient

- **Claim:** Allowing new inline quotations during `submit` duplicates the already-verified `cite` tool and creates an unnecessary resolve–dry-run–mint–ID-remap subsystem.
- **Evidence:** The prompt explicitly tells the model to cite facts while reading in [research_agent.py:107](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:107), and `cite` verifies and mints records in [research_agent.py:703](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:703). Nevertheless, `submit` accepts fresh `doc_id`, page and quote fields at [research_agent.py:433](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:433), which requires a second resolver in [research_agent.py:803](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:803) and submission retry machinery at [research_agent.py:1347](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1347).
- **Action:** **simplify** `submit.evidence` to verified IDs only. Reject unknown IDs with a short tool result; do not permit late inline evidence.
- **Estimated savings:** 100–140 lines.
- **Risk/test:** Medium: a model that skips `cite` will need another turn. Retain one unknown-ID retry and test: cite→submit succeeds; unknown ID is rejected; unverifiable IDs can never reach the artifact. The existing happy path is [test_research_agent.py:859](/Users/michaelzhao/swe/ai-bank-equity-researcher/tests/test_research_agent.py:859).

### 4. Hand-written tool JSON schemas duplicate the Pydantic contract

- **Claim:** `research_agent.py` manually maintains hundreds of lines of JSON Schema beside Pydantic models describing substantially the same structures.
- **Evidence:** The contract models live in [schema.py:12](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/schema.py:12), while `_NUMBER_SCHEMA`, six tool schemas and the submit schema occupy [research_agent.py:267](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:267) through line 524. `_keep_valid` then invokes Pydantic again at [research_agent.py:878](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:878).
- **Action:** **replace with Pydantic**—already a dependency. Define small `SearchArgs`, `CiteArgs`, `SubmitPayload` models and use `model_json_schema()` for tool parameters and `model_validate()` on arguments.
- **Estimated savings:** 80–130 net lines.
- **Risk/test:** Low-to-medium because provider JSON-Schema support should be checked for `$defs`. Snapshot every emitted tool schema and retain the tool-call integration tests around [test_research_agent.py:915](/Users/michaelzhao/swe/ai-bank-equity-researcher/tests/test_research_agent.py:915).
- **Library judgment:** This is the only clear library replacement. BeautifulSoup, LangChain, an agent SDK, `dateparser`, or fuzzy-matching libraries would mostly relocate domain logic or add dependencies for very little deletion.

### 5. Several output-contract fields are write-only ceremony

- **Claim:** `DriverClaim.columns`, `DriverClaim.checks_failed`, and `Attribution.suggested_registry_patches` do not participate in validation, scoring or useful rendering.
- **Evidence:** They are defined at [schema.py:47](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/schema.py:47), [schema.py:52](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/schema.py:52), and [schema.py:106](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/schema.py:106). Component-column validation infers columns from evidence labels rather than `driver.columns` in [validate.py:536](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:536). `checks_failed` is rendered at [render.py:80](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/render.py:80) but is never populated on a `DriverClaim`; `suggested_registry_patches` has no consumer.
- **Action:** **delete** these fields and their prompt/schema/parsing boilerplate. Preserve movement column provenance, which is rendered and useful.
- **Estimated savings:** 20–35 lines.
- **Risk/test:** Low. Parse a representative historical artifact with ignored extra fields, render it, and rerun the wrong-component-column tests in [test_component_columns.py:82](/Users/michaelzhao/swe/ai-bank-equity-researcher/tests/test_component_columns.py:82).

### 6. Corroboration should cap confidence, not manufacture disagreements

- **Claim:** The corroboration machinery overreaches when it converts a numeric spread into a semantic disagreement reason and explanation.
- **Evidence:** Canonical cross-source views are useful and compact at [validate.py:276](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:276), but [validate.py:310](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:310) automatically labels gaps as rounding or definitional and appends prose such as “framing/rounding, not a data conflict.” The agent is already responsible for source interpretation and reporting disagreements in [research_agent.py:170](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:170). No direct corroboration/disagreement unit test exists.
- **Action:** **simplify** to source counts, `corroborated_N_sources`, and the single-source 85 cap. Delete automatic `Disagreement` creation and `CORROBORATION_TOL`; let the agent describe why sources differ.
- **Estimated savings:** 25–40 lines.
- **Risk/test:** Low-to-medium. Add fixtures with equal walks, rounded walks and materially different framings; verify confidence/status while the two-judge narrative suite catches an omitted material disagreement.

### 7. `ask.py` is a second, untyped open-loop product rather than a thin use of the product agent

- **Claim:** Free-form Q&A duplicates retrieval, page budgeting, evidence extraction, author retries, evidence gating, rendering and artifact persistence outside the closed-loop product.
- **Evidence:** The parallel pipeline occupies [ask.py:128](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/ask.py:128) through line 263. It reimplements the evidence gate at [ask.py:211](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/ask.py:211), including only key facts—not numbers in the main answer prose. Its supporting cross-reference program occupies [evals.py:83](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/evals.py:83) through line 268. Tests cover crossref scoring, but no test invokes `run_ask`.
- **Action:** **merge** `ask` into the `Research` tool loop with a smaller alternate `SubmitPayload`, or delete it if free-form questions are outside the stated product. Do not maintain a second open-loop author.
- **Estimated savings:** 180–320 lines, depending on whether the crossref CLI/reporting arm remains.
- **Risk/test:** Medium. Preserve the four crossref cases: location coverage and two-judge fact accuracy must not fall. Add an end-to-end offline `run_ask` test; currently it is under-covered.

### 8. `evals.py` contains four harnesses; the scoring kernel is much smaller and should remain explicit

- **Claim:** Numeric scoring is not duplicated with validation, but it is buried among crossref execution, artifact discovery, Markdown generation, judge orchestration and rescore comparison code.
- **Evidence:** The core typed scoring spans roughly [evals.py:285](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/evals.py:285) to [evals.py:799](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/evals.py:799). Execution/reporting resumes at [evals.py:802](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/evals.py:802), narrative-judge reporting at [evals.py:894](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/evals.py:894), and offline delta/report machinery at [evals.py:1029](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/evals.py:1029). By contrast, `judge.py` cleanly owns the two-question/two-judge verdict protocol at [judge.py:196](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/judge.py:196).
- **Action:** **merge/simplify** the three run/write loops behind common case-runner and JSONL/metadata helpers. If `ask` is retired, delete its crossref runner. Keep driver scoring, calibration, extraction diagnostics and `judge.py` separate.
- **Estimated savings:** 100–220 lines without changing precision, recall, calibration or judge rules.
- **Risk/test:** Low if scorer output dictionaries remain stable. Snapshot JSONL rows and scorecard totals for a fixed saved-artifact fixture.

### 9. Discovery and unused registry metadata are speculative onboarding machinery

- **Claim:** Autonomous web discovery is not integrated with analysis and emits a model-authored manifest without a typed validation or test boundary.
- **Evidence:** `discover()` fetches arbitrary model-selected URLs and writes the reply at [discover.py:100](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/discover.py:100); its only consumer is the CLI branch at [cli.py:84](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/cli.py:84). The actual product starts from committed manifests in [corpus.py:43](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/corpus.py:43). There are no discovery tests. Registry keys such as `documents`, `results_events`, `source_notes` and `cet1_label_notes` are never read by runtime code; compare [registry/cba.json:7](/Users/michaelzhao/swe/ai-bank-equity-researcher/registry/cba.json:7) with runtime lookups at [research_agent.py:771](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:771).
- **Action:** **delete or demote** discovery to a maintainer script whose output must pass manifest schema/checksum review; **delete** unused registry metadata while retaining calendar, measures and walk-label maps.
- **Estimated savings:** 140–170 Python lines plus roughly 40 registry-data lines.
- **Risk/test:** Medium for onboarding, low for analysis. Rebuild the ANZ corpus from its committed manifest and run the ANZ cold-path suite. A manifest-schema test should replace the untested discovery loop.

### 10. `refs.py` is disproportionate for one optional agent tool, but should be ablated rather than deleted blindly

- **Claim:** A 461-line, bank-format-sensitive parser plus 361 lines of tests is excessive for an agent capability that overlaps `search_pages`.
- **Evidence:** The product exposes only `Research.follow_references`, which calls `scan_page`, at [research_agent.py:681](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:681). That pulls in note-index discovery [refs.py:190](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/refs.py:190), inferred printed-page maps [refs.py:236](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/refs.py:236), three marker tiers [refs.py:294](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/refs.py:294), relevance ranking and batch expansion [refs.py:376](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/refs.py:376). The baseline additionally uses the batch follower at [pipeline.py:229](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/pipeline.py:229).
- **Action:** **simplify after an ablation**: have the closed-loop agent search the exact note identifier/title it just read using existing `search_pages`; keep `refs.py` frozen inside the baseline arm. If explicit-note search preserves the narrative checklist, remove `follow_references` from the product tool surface and eventually delete the parser when baseline reproducibility is handled by a frozen release.
- **Estimated savings:** 180–300 lines eventually; essentially zero while the current baseline implementation remains live.
- **Risk/test:** Medium-high. The must-pass regression is the Note 2.2 impairment case plus the four narrative bake-off anchors. This is not in the “delete today” bucket.

### 11. `taxonomy.py` has the right scope but mixes ontology with a growing prompt patch diary

- **Claim:** Six metrics and their canonical drivers are current requirements, but long method hints repeat global rules and embed case-specific defect history.
- **Evidence:** Stable structure—name, unit, method, queries and drivers—starts at [taxonomy.py:8](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/taxonomy.py:8). The hints include repeated source, comparison, column and confidence instructions plus bank-specific examples, for example [taxonomy.py:92](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/taxonomy.py:92), [taxonomy.py:190](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/taxonomy.py:190), and [taxonomy.py:299](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/taxonomy.py:299). The same universal rules already occupy [research_agent.py:124](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:124).
- **Action:** **simplify** to one shared instruction block per method (`walk`, `bridge`, `identity`, `note`) plus short metric-specific additions. Keep the canonical hierarchy and aliases.
- **Estimated savings:** 60–110 lines.
- **Risk/test:** Medium because prompts affect quality. Gate each deletion on the full numeric dev suite and narrative anchors; do not tune against sealed cases.

## `validate.py` verdict

Most of its checks earn their keep:

- Keep walk-sum validation and the two document-type tolerances. There are only two policies—exact book walks and coarsely rounded presentations—at [validate.py:11](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:11) and [validate.py:203](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:203). That is proportionate.
- Keep comparison classification/leak detection, movement and component column checks, headline-variant/basis checks, identity scaling and driver reconciliation. Each guards a distinct confidently-wrong failure.
- Schema validation does **not** already reject these. [schema.py:78](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/schema.py:78) mostly enforces shape and confidence ranges. The evidence gate at [schema.py:110](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/schema.py:110) is a separate semantic mutation, not ordinary schema validation.
- `check_movement` is the main overlap: both author paths already recompute a contradictory delta at [author.py:421](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/author.py:421) and [research_agent.py:952](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:952). Fold missing/invalid movement handling into the shared normaliser and remove the second check.
- `unclaimed_components` and `implied_residual` are retry aids used only by the baseline, not general validators. Move them beside the baseline author if the baseline remains.

Several important validator paths are under-tested: there are no direct unit tests for `annotate_walks`, `walks_for_view`, `canonical_for`, `corroborate`, `check_comparison_leak`, `check_movement_columns`, or `unclaimed_components`. By contrast, component columns, basis/variant and identity scaling have focused tests. Cleanup should add small table-driven tests around the under-covered comparison classifier before moving it.

## What I would delete or merge today

Low risk, in order:

1. Fix eval runner routing.
2. Merge the two finalisation implementations.
3. Delete dead contract fields.
4. Restrict submit citations to IDs minted by `cite`.
5. Generate tool schemas with Pydantic.
6. Delete automatic corroboration disagreement synthesis.
7. Prune unused registry metadata.
8. Move baseline-only retry helpers out of shared `validate.py`.

I would not yet delete `refs.py`, shorten metric prompts aggressively, or remove extraction scoring without an ablation.

## Load-bearing: do not cut

- The closed-loop search/read/chart/cite/submit research shape.
- Verbatim quote verification and `enforce_evidence_gate`.
- Bank-calendar period resolution and comparison classification.
- Wrong-column detection at movement and component level.
- Walk arithmetic, driver reconciliation, unit/sign/basis/variant handling and the factor-100 identity correction.
- Confidence caps tied to failed checks, single-source evidence and missing primary walks.
- Registry calendars, primary-measure vocabulary and walk-label mappings; especially the rule that registries contain no financial values.
- Three-state driver scoring, coherent alternate framings, parent/child scoring, calibration coverage reporting and the confidently-wrong rate.
- The two-judge, two-question citation-grounding protocol in `judge.py`.

I inspected the tests and existing scorecards, but could not execute pytest: the read-only environment exposes no writable temporary directory. No files were modified.