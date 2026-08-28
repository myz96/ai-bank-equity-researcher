# Gold set

Ground truth for the eval harness (ticket 05/17). Every value carries provenance
(document, PDF page, and how it was verified). Gold walks must pass the same
sum checks the agent's extractions face — gold that does not reconcile is a
defect in the gold, never a tolerance to widen.

Tiers per metric. The tier names WHERE the truth comes from, which decides how
strictly a claim can be scored:

- `walk` — **the bank itself published the decomposition**, as one chart or
  one bulleted list on one page (a NIM walk, a CET1 waterfall). Gold is a
  transcription of that artifact. Strictest scoring: every bar has an exact
  published value, and a walk is exhaustive — the bars ARE the whole movement.
  Example: CBA FY26 NIM, PA p28.
- `components` — **the bank published the pieces, but never assembled them**.
  The NII movement sits on one page, expenses on a slide, tax in a note; gold
  records each piece with its own provenance. Scoring is per component, and
  the set is NOT exhaustive — a claim outside the recorded components is
  unscored, not wrong, and reconciliation is never force-fitted.
  Example: CBA FY26 cash earnings.
- `arithmetic` (read: **derived**) — **the bank never decomposes this metric
  at all**. ROE and CTI are ratios; the only decomposition possible is derived
  from the identity (ROE = profit / average equity; CTI = expenses / income).
  Gold fixes the movement exactly and the level-1 split by that identity;
  everything deeper is checklist material. Example: CBA FY26 ROE.

`narrative_checklist` is the "why" layer, on every tier: the reasons a good
first-pass note should MENTION — "funding costs fell because the TFF matured",
"the liquids drag is broadly revenue-neutral". Checklist items are never
value-scored; they are graded by citation-grounding (does the note say it, and
does the cited page support it). Numbers live in the tiers; reasons live in
the checklist.

`split` is `dev` or `holdout`. The holdout assignment (~8 cases) happens once
the full matrix exists, spread across banks, metrics, and period types; until
then everything is dev.

UNVERIFIED markers mean the value was not sighted in a primary source by the
gold author; such values are excluded from scoring until verified.
