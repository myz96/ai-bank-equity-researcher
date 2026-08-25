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
