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

## Progress (2026-08-30): built, verified, ready to gate

Built: `src/bank_equity_researcher/refs.py` (330 lines, new) plus
`tests/test_refs.py` (22 tests, no network). Wired into `pipeline.py` between
page selection and extraction; `extract.py`, `schema.py`, `author.py` and
`taxonomy.py` carry the supporting changes.

Design in two sentences. A notes index is built once per document in two regex
passes: the first reads the contents pages (a page listing three or more
numbered notes) and keeps the note ids the document DECLARES, the second locates
each declared note by its heading in the top 20 lines of a page, grouping
continuation pages under the same note — a document with no contents page yields
an empty index, which is what keeps slide labels like "1.9 Variable rate" out of
it. The scanner then reads the pages the budget already chose for three marker
kinds — (a) a note reference ("Note 2.2", "refer to Appendix 6.2", the bare
number under a "Note"/"Appendix" column header, or the note heading printed on
the page itself), (b) a page reference ("refer to page 21", "Refer to slide 64")
resolved through a printed-to-PDF page map built from footer numbers that
neighbouring pages confirm, and (c) a footnote line naming another note by title
— drops references into other documents ("of the 2026 Annual Report") and
targets that share fewer than two content words with the case, then ranks by
(a) > (b) > (c) and by shared words, and adds at most 4 NEW pages per case.
Pages already in the budget are tagged without spending the cap.

Also done, from the original defect at the top of this ticket:

- walk pages now carry a WALK_PAGE_HINT into text extraction, so the driver
  commentary beside the chart becomes records instead of losing its record
  budget to the balance table on the same page;
- followed pages carry an extraction hint naming the reference that reached
  them, and every record from them carries `provenance: reference_follow:...`;
- author rules 12 (EXPLAIN, DO NOT RESTATE) and 13 (SAY WHAT THE WALK HIDES),
  plus a NEVER MIX FRAMINGS clause on rule 8. No prompt mentions the judge
  checklist or any gold content.

Acceptance check 1 — PASS. `out/cba-impairment-fy26-vs-fy25-cheap`: records
ev-3 to ev-9 sit on PDF p118 with provenance
`reference_follow:CBA/FY26/profit_announcement p118 -> Note 2.2 Provisions for
Impairment and Asset Quality`; pages 116 and 117 were added. The attribution
now runs the Note 2.2 provision-type bridge: collective +150, individual -17,
write-backs -71, residual none. Before this change p118 was already in the
budget but yielded 2 records (the two total rows); the extraction hint on the
followed page is what surfaced the component rows.

Page counts and cost, four anchors (cap is +4 new pages, ~$0.010):
impairment FY26 +2 pages $0.0029 | nim FY26 +1 $0.0025 |
cash_earnings FY26 +3 $0.0048 | nim FY21 +1 $0.0023.

Judge sweep, four anchors (pre-change row was 0/4, 0/3, 0/3, 0/5 = 0/15):

| arm | cba-nim-fy26 | cba-cash-earnings-fy26 | cba-impairment-fy26 | cba-nim-fy21 | total |
|---|---|---|---|---|---|
| cheap | 3/4 ⚑1 | 0/3 ⚑1 | 0/3 | 0/5 | 3/15 |

(`evals/results/20260829-1817-t22-bakeoff-judge.json`, scored on the artifacts
now in `out/`. An earlier sample of the same code scored 4/4 on nim FY26 for
4/15: `evals/results/20260829-1653-t22-bakeoff-judge.json`. The
follower-only build, before the walk hint and rules 12-13, still scored 0/15:
`evals/results/20260829-1550-t22-bakeoff-judge.json` — the pages alone bought
nothing; the extraction hint and the author rules are what moved it.)

Full dev suite, cheap (`evals/results/20260829-1815-cheap-dev.md`):

- movements: all 15 CBA cases OK; the three known misses (NAB cti, WBC roe,
  WBC impairment) unchanged, nothing else went red;
- brier 0.032 (bar 0.058, previous best 0.035);
- confidently_wrong_rate 0.0;
- 85-94: 22 claims 100% correct, 95-100: 12 claims 100% correct = 34/34 at 85+
  (previous best 36/36 — same accuracy, two fewer scored claims, because nim
  FY26 adopted the 6-bar slide framing rather than the 7-bar book framing).

One regression found and fixed inside this round. The first full suite
(`20260829-1737`) came back with confidently_wrong_rate 0.028: CBA nim FY26
took its liquids and markets bars from the presentation slide and then added
the basis-risk bar that only the Profit Announcement publishes — a mixed
framing that describes no published walk. Rule 8 gained a NEVER MIX FRAMINGS
clause and the suite was rerun clean.

Known limits, for the next round:

1. The judge entails a fact only from quotes that a DRIVER cites, so a fact
   that belongs in the headline (the cash-earnings operating-performance and
   statutory-versus-cash frames) is judged "stated" and "not entailed" however
   well it is sourced. Both judges now answer "stated" on the operating
   performance item; the entailment path does not exist in the pipeline's
   report shape.
2. nim FY21's five checklist items live in slide-63 chart annotations whose
   text layer separates every number from its label ("(1) (1) +9 (5) (4)" above
   "Bus. Lending / Consumer Fin. / Home loans"). Text extraction cannot pair
   them; a vision read of the annotation layer would be the fix.
3. Two of the three impairment checklist items are half-year facts that a
   FY-vs-FY report legitimately skips (ticket 32 caveat 1).
