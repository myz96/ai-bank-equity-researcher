# 06 — Output contract

Type: grilling
Status: resolved
Blocked by: 01, 02

## Question

What exactly does the agent emit? Decide: the JSON schema for an attribution (movement, comparator, drivers, contributions, confidence, citations), citation granularity (document + page + verbatim quote), how source disagreement appears in the output, and the human-readable report rendered from the same data.

## Answer

Resolved with the user (grilling, 2026-08-25):

1. **One JSON document is the entire output**; everything else derives from it. Top level: bank, metric, period, comparator, basis, movement {from, to, delta, unit}, headline, drivers[], residual, notable_items[], disagreements[], attribution_confidence, evidence_records[], suggested_registry_patches[], provenance {document checksums, models, run}. Each driver: canonical id + verbatim bank_label, contribution (nullable for unquantified), narrative, confidence 0–100, evidence refs, per-driver check results.
2. **Citations**: document id, printed page AND PDF page, verbatim quote ≤50 words (or table fragment), parsed numbers. Verbatim quotes are what the citation-grounding judge verifies.
3. **The report is rendered, not written**: deterministic markdown template over the JSON; no second model pass around the numbers. Model-written prose exists only in the headline and narrative fields inside the JSON, where checks and judges see it.
4. **Disagreements are first-class**: both values, both citations, which was preferred and why. The preference logic (source hierarchy) belongs to ticket 07; the output slot is fixed here.
