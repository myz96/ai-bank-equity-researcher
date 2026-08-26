# Gold set

Ground truth for the eval harness (ticket 05/17). Every value carries provenance
(document, PDF page, and how it was verified). Gold walks must pass the same
sum checks the agent's extractions face — gold that does not reconcile is a
defect in the gold, never a tolerance to widen.

Tiers per metric, mirroring the evidence ladder (ticket 01):

- `walk` — bar values hand-recorded from the bank's published walk, read from
  the rendered page image and cross-checked against the page text/narrative.
- `components` — component movements as disclosed in tables/text (bridge
  metrics). Reconciliation to the headline movement is NOT force-fitted;
  agents are scored per component plus honest residual handling.
- `arithmetic` — the movement is exact; level-1 decomposition is checked by
  identity; level-2 is a documented driver checklist (narrative claims are
  citation-graded, not value-graded).

`narrative_checklist` items are things a good first-pass note should mention;
they are scored by citation-grounding, never by exact wording.

`split` is `dev` or `holdout`. The holdout assignment (~8 cases) happens once
the full matrix exists, spread across banks, metrics, and period types; until
then everything is dev.

UNVERIFIED markers mean the value was not sighted in a primary source by the
gold author; such values are excluded from scoring until verified.
