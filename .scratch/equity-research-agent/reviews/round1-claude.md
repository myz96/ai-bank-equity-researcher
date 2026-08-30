# Round 1 — reviewer A (Claude, executed repros) @ 4440927

1. HIGH validate.py:754 — reconcile_tolerance unit-blind (1.0/10.0 for every
   metric). Shipped proof: cba-cti-fy26 drivers sum 0.0 ppt vs delta -0.2 ppt
   and PASS drivers_reconcile. Also gates settle_identity_scale; a +50 ppt
   driver set vs +0.1 delta can trigger the /100 "correction" and pass.
2. HIGH research_agent quote_key — verbatim gate rejects faithful table-row
   quotes when the text layer interleaves footnote markers (repro CBA FY26 PA
   p2 "Revenue from ordinary activities 2 3 30,153"); also permissive across
   row boundaries (adjacency, not row membership).
3. MED-HIGH extract.py:359 — walk-record NumberFacts always unit="bps"
   (shipped: $455m bridge bar labelled bps); silently empties
   check_component_columns' pool on $m cases.
4. MED research_agent question_scope — "$m" hardcoded as every chart's unit
   in question mode.
5. MED shell drift — agent read_chart never calls extract_walk_annotations;
   arms not evidence-comparable on sub-split-bearing cases.
6. MED corpus documents_for_question — silently substitutes latest period
   when the named one is absent; no limitation recorded (repro: WBC FY26
   question scoped to 1H26 docs).
7. MED judge.py — quote CHARACTER budget truncates silently; quotes_used
   reports pre-truncation count; 48x600 chars can exceed the 8000 budget.
8. MED validate.py:203 — walk_sum_tolerance bps-calibrated for every unit; a
   ppt walk can never fail its sum check.
9. LOW research_agent:1392 — turn-cap stop misreported as wall-clock stop.
10. LOW corpus banks_named — "National Australia Bank" unrecognisable (all
    words generic) → RuntimeError on a valid question.
11. LOW corpus resolve_doc_name — bank-less fuzzy match accepted (latent
    false coverage hit).

Checked and found clean: all pdf_page/array crossings; enforce_answer_gate
citations→evidence normalisation; settle_charge_sign arithmetic;
period_end_date rollovers; module caches keyed per document (refutes the
cross-bank cache-leak claim in general form); max_quotes=48 plumbing.
