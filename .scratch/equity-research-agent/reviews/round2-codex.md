Eight verified findings:

1. **High — `research_agent.py:975-985`, `validate.py:943-949`: `cap_weakly_cited_claims` trusts model-supplied `NumberFact`s that were never verified against the quote.**  
   Failure: an agent can cite an unrelated verbatim sentence, attach `{"value": 150, "unit": "$m"}`, and retain a `+150 $m` claim at confidence 95 because the cap treats that invented fact as printed evidence.  
   Fix: derive facts from verified text or trusted extraction tools; never use submission-supplied `NumberFact`s for citation strength without validating value and unit against the page.

2. **High — `author.py:394`, `research_agent.py:1180`, `validate.py:865`: ratio endpoint scale is never validated, and the identity normaliser exits when incorrectly scaled numbers reconcile internally.**  
   Failure: the current CBA FY26 ROE artifact’s `1350 → 1400 ppt`, `delta +50`, and drivers `+96/-46 ppt` all pass because only bps endpoints are normalised and the wrong-scale identity closes exactly.  
   Fix: validate ratio levels against cited percentage facts and normalize or fail 100×-scaled ppt movements before reconciliation.

3. **High — `author.py:272`, `validate.py:561-580`, `validate.py:943-953`: bridge-component sign conversion remains prompt-only while both supporting validators deliberately compare magnitudes.**  
   Failure: CBA loan impairment expense fell from `$320m` to `$319m`; the author copied the disclosed expense delta `-1` instead of converting it to the cash-earnings effect `+1`, while column validation and the citation cap both accept its magnitude, leaving the wrong driver at confidence 85.  
   Fix: deterministically derive expense, impairment, and tax contributions as the negative of their cited line-item delta and reject inconsistent submitted signs.

4. **High — `validate.py:943-953`: the weak-citation cap ignores unit, label, and numeric role, so an unrelated same-magnitude fact certifies a claim.**  
   Failure: the live `notable_items +0.0 ppt` claim stays at confidence 90 because a cited record contains `0.0 $m`; similarly, an endpoint can accidentally ground a same-sized delta.  
   Fix: require normalized unit compatibility and a matching semantic label/role; ambiguous quote numbers and cross-unit zeroes must not count as stated contributions.

5. **Medium — `research_agent.py:1489-1494`, `research_agent.py:1557-1561`: intra-turn budget enforcement still omits the cost ceiling and the normal wall-clock limit.**  
   Failure: a reproduced turn with a `$0.50` ceiling dispatched three calls costing `$1` each before latching exhaustion; calls can likewise continue until `1.5 × wall_clock_s`, and rejected submits can increment the counter beyond its cap at line 1580.  
   Fix: use one budget predicate before every call—including cost and normal elapsed time—and pass the remaining absolute deadline into nested LLM calls.

6. **Medium — `schema.py:72-76`, `validate.py:61-77`, `validate.py:817`: the new tolerance tables use raw, case-sensitive unit strings even though the scorer canonicalizes aliases.**  
   Failure: `unit="PPT"` receives the default reconciliation tolerance `1.0`; drivers totaling `+0.6` therefore pass a `-0.2` movement despite a `0.8 ppt` gap, while `evals.normalize_unit` considers `"PPT"` valid ppt.  
   Fix: canonicalize units once with a shared normalizer and require movement, contribution, residual, and taxonomy units to agree before applying tolerances.

7. **Medium — `research_agent.py:690-722`: marker relaxation removes every standalone one- or two-digit page number, including genuine measurements.**  
   Failure: `match_quote("The margin fell basis points…", "The margin fell 3 basis points…")` returns true because the real `3` is stripped as though it were a footnote marker.  
   Fix: restrict relaxation to tokens positively identified as table-reference markers, and reject matches that omit numeric content from the matched span.

8. **Medium — `pipeline.py:250-280`, `research_agent.py:857-898`: annotation-layer parity disappears when the primary walk extraction fails.**  
   Failure: the pipeline still attempts callout extraction after an unreadable walk, but `Research.read_chart` returns immediately, so the agent loses valid annotation evidence available to the baseline shell.  
   Fix: attempt annotation extraction independently of the walk result, using empty bar labels when the main read fails.
