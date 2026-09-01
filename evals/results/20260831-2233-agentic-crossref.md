# Crossref scorecard — combo agentic, 20260831-2233

## Run metadata

- run: 20260831-2233 (UTC)
- commit: 63c6208 (working tree dirty)
- gold sha256 (evals/gold/*.json, first 16): acfb8172d297fa3b
- judges: deepseek/deepseek-v4-pro-0813, qwen/qwen3.7-flash

Two populations, reported apart. **Location coverage** measures the retriever: did the answer cite the pages that carry the answer? **Fully-grounded facts** measures citation discipline, not analysis quality: did the judges rule each gold fact both STATED by the answer and ENTAILED by its cited quotes, with EVERY load-bearing number present in those quotes? An answer whose analysis is right but whose quotes omit a number it used scores a fail here by design (measured 2026-08-31: frontier agents state nearly every gold fact and lose this column on quote completeness). A case PASSES only when coverage is 100%, NO fact failed, and the facts the judges could not settle stay inside 25% of the case. A flagged fact is neither a pass nor a fail; a failed fact is the answer getting it wrong, and no allowance covers that. Coverage alone is not correctness (ticket 29, finding 7).

| Case | Pass | Location coverage | Fully-grounded facts | Flagged | Missed locations | Conf | Cost |
|---|---|---|---|---|---|---|---|
| CBA dividend-drp-web | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |
| CBA mortgage-offset-footnote | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |
| CBA notables-cti-web | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |
| CBA restatement-web | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |
| CBA nim-longitudinal-fy21-fy26 | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |

## Judged facts

Judge cost: $0.0 over 0 calls (on top of the per-case answer cost).
