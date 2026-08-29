# 22 — Defect: narratives echo the walk instead of explaining it

Type: task
Status: open

## Question

Driver narratives restate the bar ("a 5 bps negative contribution from asset pricing") instead of citing the bank's own explanation (home lending pricing down 4bps, business/institutional down 1bp, competition) that sits in the PA text on the same page — and the ADR-0001 requirement to flag what a walk hides (CBA calls the liquids drag "broadly revenue neutral") is not yet surfaced. Fix: ensure the walk page's text evidence is extracted alongside the vision read (currently walk pages skip text extraction), and prompt the author to ground each narrative in quoted explanation and to note walk caveats like revenue-neutral bars.

## Design: deterministic reference-following (added 2026-08-29, from the bake-off diagnosis)

The judge sweep scored the cheap pipeline 1/43 on narrative checklist items. The root cause
is page starvation: the why-layer lives on pages the retrieval budget never ranks — appendix
notes, footnote targets, divisional sub-splits. The closed-loop agents (Sonnet, Fable) find
these pages because they FOLLOW REFERENCES: the impairment case's decisive evidence (Note 2.2,
PDF p118) is reachable only by reading "refer Note 2.2" on the income statement and turning to
it. Retrieval scores that appendix page near zero for every query.

Mechanism — a deterministic expansion pass between retrieval and extraction:

1. After the initial page budget is chosen, scan the SELECTED pages' text for reference
   markers, in priority order:
   a. "Note X.Y" / "refer to Note X.Y" — resolve against a notes index built once per
      document (regex over the text layer for note headings, e.g. "^2.2 Loan impairment").
   b. "page NN" / "refer to page NN" / "(page NN)" — resolve the printed page number via the
      existing printed_page_of offset for that document.
   c. Footnote superscripts on extracted table rows whose footnote text names another
      section or note.
2. Add each resolved target page to the extraction set, tagged provenance
   "reference_follow:<source page>" — capped at +N pages per case (start N=4) so the budget
   stays bounded; ranked by (a) > (b) > (c) when the cap binds.
3. The author prompt already grounds narratives in quoted explanation; the new pages simply
   enter the same evidence pool. No model choice is involved — the expansion is pure code.

Why deterministic first: the bake-off shows insight is loop-dependent, not tier-dependent.
If reference-following recovers the checklist items at cheap-tier cost, the research loop
stays cheap; if it half-works, the fallback is a closed-loop research pass at Sonnet tier
(bake-off arm 3's result prices that option). Ticket 32 round 2 scores this engineered arm
on the same four anchor cases with the same judge checklist.

Acceptance: (1) the impairment case's evidence pool contains PDF p118 with a
reference_follow tag; (2) the judge checklist rate on the four anchor cases moves
materially off 1/43 with no movement/scoring regression on the 15 frozen baseline cases;
(3) added cost per case stays within the cheap-combo budget envelope (~2x worst case).
