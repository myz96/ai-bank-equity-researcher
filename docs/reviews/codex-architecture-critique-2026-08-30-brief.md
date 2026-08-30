# Architecture critique brief: simplicity and over-engineering

You are an external architecture reviewer. Your job is to find over-engineering in this
repo and to say what to cut, merge, or simplify. Read the code, not just the docs.

## What the repo is

A bank equity-research agent for Australian banks. It explains why a headline metric
moved between reporting periods, with cited evidence. The stated objective (ADR-0005,
docs/adr/0005-*.md) is: most accurate and most generalisable agent; calibration is
measured (the headline stat is the confidently-wrong rate); cost is a guard rail, not
the target. The closed-loop agent (src/bank_equity_researcher/research_agent.py) is the
product; the open-loop pipeline (pipeline.py + author.py) survives only as the baseline
comparison arm.

Calibrate your critique to that objective. A check that guards measured accuracy is not
over-engineering just because it is code. But redundant checks, speculative generality,
and hand-rolled machinery that a simpler mechanism could replace ARE over-engineering.

## Questions to answer

1. validate.py (853 lines): which checks earn their keep? Which overlap each other or
   duplicate what schema validation already rejects? Are the per-document-type
   tolerances and the corroboration/disagreement machinery proportionate?
2. Is there duplication or blurred responsibility across validate.py, evals.py
   (1,147 lines), and judge.py (425 lines)? Could the eval harness be materially
   smaller without losing driver precision/recall, calibration, or the two-judge
   citation-grounding protocol?
3. Where is the code general beyond current need (speculative generality)? Look hard at
   refs.py (461 lines, demoted from primary path to one agent tool), taxonomy.py,
   discover.py, the registry machinery, and ask.py.
4. research_agent.py is 1,382 lines. What inside it is loop/harness ceremony that could
   shrink, versus load-bearing tool logic?
5. Are there places where an off-the-shelf library would genuinely replace hand-rolled
   code line-for-line, without losing the domain semantics? Name the library and the
   exact code it replaces. Do not propose framework migrations that merely relocate the
   same logic behind a dependency.
6. What would you delete or merge today at low risk?

## Output format

Ranked findings, highest value-per-effort first. For each finding give:
- claim (one sentence)
- evidence (file:line references you actually read)
- action (delete / merge / simplify / replace-with-X)
- estimated line savings
- risk, and what test or eval case would catch a regression

Then a short section: what is load-bearing and must NOT be cut, so later cleanup does
not hit it.

## Constraints

- Read-only. Do not modify files. Do not use the network.
- Ignore data/ (PDF cache) and out/ (generated run outputs) except as evidence of the
  output contract.
- tests/ counts as part of the architecture; note if tests over- or under-cover a
  component you flag.
