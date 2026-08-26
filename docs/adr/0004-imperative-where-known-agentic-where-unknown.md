# Imperative where the path is known; agentic where it is unknown

Orchestration follows one heuristic: a step whose route is known and deterministically checkable is written as imperative code (retrieval, walk location, extraction, validation, rendering); a step that is genuine discovery — search, follow, reformulate, judge — runs as an agent (document discovery for an unseen bank; the research that built the disclosure inventories; the author's bounded evidence-request loop as a small declarative pocket). This is the declarative-vs-imperative split applied per stage, not per system.

The evidence behind it: the retrieval bake-off (ticket 13) showed an LLM navigator losing to local code 4–8/10 vs 10/10 on the known path, while the corpus and research subagents (tickets 08–11, 18) handled drifting landing pages and unknown document names faultlessly — the unknown path.

## Consequences

- The pipeline spine stays deterministic and cheap to rerun; agents appear only at the cold-start boundary (unseen bank → discovery agent builds the manifest, then hands off).
- We take the DSPy philosophy — iterate prompts against a measured metric — via our own eval harness, without adopting the framework.
- Revisit a stage's classification only when measurement says the current side is failing, as the bake-off did for navigation.

## The capability trade-off (2026-08-26)

The Fable frontier benchmark made the underlying trade-off concrete: a very smart model with thin tools reconciled conflicting walk framings and surfaced the earnings-neutral insight unaided; our cheap models need thick structure (pipelines, checks, canonical taxonomies) to reach the same accuracy — and still trail on judgment. Policy: the frontier benchmark output (out/baseline-fable/) is the standing quality target; rerun it when the pipeline is complete and optimise toward beating it. The tier above it — a human sector expert scoring both — is the aspirational benchmark, noted on the map as fog.
