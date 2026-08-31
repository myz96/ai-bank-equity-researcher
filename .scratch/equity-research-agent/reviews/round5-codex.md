Found 8 new/current issues. The tree has not normalised.

1. **High — late-added evidence misses the percent-to-bps normaliser.** [research_agent.py:1273](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1273), [research_agent.py:1283](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1283), [research_agent.py:1327](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1327)

   The shell deliberately recovers tool-minted records cited by a headline/driver but omitted from the submission’s `evidence` list. However, that recovery happens after `_percent_evidenced` decides whether to scale ratio endpoints. Executed repro: evidence printing `2.08% → 2.05%`, cited through `headline_evidence` but omitted from `evidence`, produced `2.08 → 2.05, -0.03 bps`; the record and citation were then accepted. Move minted-record recovery before all evidence-dependent normalisation.

2. **High — cleanup reintroduced the driver-confidence hole for two named wrong-claim checks.** [validate.py:553](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:553), [validate.py:767](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:767), [validate.py:1818](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:1818)

   `comparison_leak` and `component_from_prior_half` no longer cap the offending driver, while `WHOLE_TABLE_FAILURES` still excludes them on the now-false assertion that they cap in place. Their failures lower only attribution confidence; a demonstrably wrong driver remains at 95 and enters the confidently-wrong population. Executed repro: `comparison_leak` fired on a 95-confidence driver; `cap_unreconciled_drivers` returned `[]` and confidence remained 95. This is a post-round-4 regression caused by commit `2624c14`.

3. **Medium-high — the grace ladder misses normal `httpx` connection failures.** [llm.py:120](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/llm.py:120), [llm.py:127](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/llm.py:127)

   Classification relies on message substrings. Executed repro: `httpx.ConnectTimeout("timed out")` and `httpx.ConnectError("All connection attempts failed")` both returned false, so they consume the five ordinary attempts instead of receiving grace. Classify the `httpx` exception hierarchy and chained causes rather than selected English messages.

4. **Medium-high — grace waits are outside the case’s absolute deadline.** [llm.py:193](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/llm.py:193), [research_agent.py:1568](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1568), [research_agent.py:1612](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1612), [research_agent.py:984](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:984)

   The outer wall clock is checked only between model/tool calls; `chat` and `chat_tools` receive no remaining deadline. One call can therefore add roughly ten minutes after the budget, and `read_chart` can run separate walk and annotation ladders. A submission turn can add another ladder. Pass an absolute monotonic case deadline through every LLM call and cap both requests and sleeps to the remaining time.

5. **Medium — every CLI help surface advertises deleted combos.** [cli.py:18](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/cli.py:18), [cli.py:27](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/cli.py:27), [cli.py:39](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/cli.py:39), [config.py:65](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/config.py:65)

   `analyse`, `ask`, and `evals` advertise `agentic-glm` and `agentic-cheap`, but `COMBOS` contains only `agentic`. Executed calls to `runner_for` show both advertised names raise `KeyError`.

6. **Medium — primary documentation still describes and invokes the deleted product.** [README.md:50](/Users/michaelzhao/swe/ai-bank-equity-researcher/README.md:50), [README.md:53](/Users/michaelzhao/swe/ai-bank-equity-researcher/README.md:53), [README.md:75](/Users/michaelzhao/swe/ai-bank-equity-researcher/README.md:75), [design.md:28](/Users/michaelzhao/swe/ai-bank-equity-researcher/docs/design.md:28), [design.md:68](/Users/michaelzhao/swe/ai-bank-equity-researcher/docs/design.md:68), [0005-quality-first-closed-loop-research-agent.md:53](/Users/michaelzhao/swe/ai-bank-equity-researcher/docs/adr/0005-quality-first-closed-loop-research-agent.md:53)

   The README quickstart runs retired `cheap`, predicts a `-cheap` output, and describes staged cheap extraction/authoring. The design doc presents the open loop as the current architecture and still documents the deleted single-source cap. ADR-0005 says the pipeline remains in the repository. These should distinguish historical measurements from the current closed-loop product.

7. **Low — the while-loop conversion doubled ordinary backoff and sleeps after the terminal failure.** [llm.py:226](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/llm.py:226), [llm.py:296](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/llm.py:296)

   Five immediate 500 responses now sleep `[2, 4, 8, 16, 32]`—62 seconds, including 32 seconds after no retry remains. The former loop slept `[1, 2, 4, 8, 16]`. Sleep only when another attempt is available and retain the original exponent.

8. **Low — deletion left baseline-only mechanisms orphaned but still tested as though live.** [extract.py:159](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/extract.py:159), [validate.py:816](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:816), [validate.py:956](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:956), [validate.py:1917](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:1917)

   `extract_text_evidence`, `unclaimed_components`, `implied_residual`, and `sign_flip_hint` have no live source caller after `pipeline.py` was removed. The latter three were pipeline retry feedback, not validators used by the remaining shell. Either integrate the still-required safeguards into the closed loop or delete the dead code and tests.

The 400-reasoning fallback itself is correct: with `retries=1`, an executed repro made two requests, removed `reasoning` after the first 400, and succeeded on the fallback without looping.

Verification: all 15 package modules import. Of the tests runnable in the read-only environment, 396 passed; 24 `tmp_path` tests could not start because the sandbox exposes no writable temporary directory.
261,919
