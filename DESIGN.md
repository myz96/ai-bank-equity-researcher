# Design doc: the four owned decisions

Status: FINAL 2026-09-02. All suites run and committed; scorecards under
`evals/results/`.

This document records the four design decisions the project owns end-to-end:
tools, context management, memory, and evals. Each section states the
decision, the evidence behind it, and the alternatives that lost.

## The task

Given a bank, a period, and a headline metric, explain the movement against
the prior comparable period, attribute it to drivers, and produce a
confidence-rated attribution that cites the evidence behind every claim.
Banks: CBA, NAB, Westpac (ANZ unseen; Macquarie sealed). Metrics: NIM,
cash earnings, ROE, CET1, credit impairment charge, cost-to-income.

The one-sentence finding that shaped everything: **getting the movement
numbers right is easy even for cheap models; explaining WHY is a context
problem, not a model-size problem.** The four decisions below all serve
that split.

## Decision 1 — Tools: a closed loop over a deterministic estate

The product is one tool-calling model researching in a loop
(`agent/research_agent.py` + `agent/toolbox.py`). The tool set is small,
and each tool wraps machinery that code fully controls:

- `plan_research` — the model's first call lists where the answer's pieces
  should live; the loop reads the plan back once at submit time.
- `search_pages` — keyword plus meaning-based search over all the case's
  documents at once, run with 1-3 phrasings of the query per call.
- `read_page` / `read_chart` — page text, and vision reads of walk charts
  (endpoints and bars validated by arithmetic; a misread chart must fail a
  sum check, not become a citation).
- `cite` — turns quotes into evidence records; every quote is checked
  verbatim against the page at mint time, and a paraphrase is rejected back
  to the model.
- `follow_references` / `bank_language` — deterministic note-pointer
  scanning and the registry's label vocabulary.
- `submit` — the answer, which code then validates: units and signs, the
  right comparison period, walk arithmetic, tolerances, and the confidence
  caps.

Model roles: glm-5.3-flash drives the loop (the most accurate option for
the cost); qwen3.7-flash reads charts; deepseek-v4-pro and qwen3.7-flash
judge (two different model families, so they cannot share blind spots; if
they disagree, a human is flagged). A `fast` combo swaps deepseek-v4-flash
into the same loop for evaluators in a hurry — its movement numbers hold,
but on the dev suite it let a wrong claim ship at high confidence, which
the default never does. The scorecards document that trade.

Why this shape: the failure that matters most in equity research is a
confident wrong number. Every code check exists because a model once
produced a plausible-looking mistake that arithmetic caught — a chart's
endpoint read as a movement, a table column read as the wrong period, a
movement "supported" by a note number that wasn't a value at all. The
checks turn those from silent errors into visible failures that push
confidence down.

Rejected: the fixed pipeline this project built first (retired; the
bake-off below is why); a frontier model per query (the quality ceiling,
at ~100x the price, with nothing to catch it when it slips); agent
frameworks (the system is plain Python in five small packages; a framework
would hide exactly the layer we need to control).

## Decision 2 — Context management: let the model choose pages, hold it to evidence

Documents are 100-200 page PDFs, and six can be in scope for one case.
Nothing fits in one context window, and most pages are irrelevant. Version
one picked pages up front: search nominated candidates, a fixed budget
chose among them, and the model never got a say. That was good enough for
the numbers — and it exposed the project's central finding, **page
starvation**: on the "does the note explain the bank's own why" test, the
fixed pipeline scored roughly zero, because the explanations live on pages
search never ranks highly (notes in appendices, footnote targets,
divisional detail).

The five-arm bake-off isolated the cause. Four anchor cases, one judge
protocol, identical for every arm:

| arm | loop | checklist | movement | cost/case |
|---|---|---|---|---|
| cheap pipeline | open | 0/15 | 4/4 | $0.002-0.005 |
| glm-5.3 author, same context | open | 1/15 | 4/4 | $0.22-0.86 |
| Sonnet agentic | closed | 6/15 | 4/4 | ~40k tokens |
| Fable agentic | closed | 3/15 | 4/4 | ~25k tokens |
| Codex agentic | closed | 1/15* | 4/4 | quota |

*Codex's row carries 5 judge flags and a citation-style interaction; its
numbers match gold with zero residual.

The glm control row settles it: a reasoning model ~100x the price, given
the same starved pages, gained one checklist item. The gap is the loop, not
the model size — agents in a loop follow references while they reason. The
clearest example is CBA's Note 2.2 on PDF page 118: it breaks the
impairment movement down exactly, and the only way to find it is to read
"refer Note 2.2" on the income statement and go there. Search ranks that
page near zero for every query we tried.

So the decision: the model assembles its own context, inside the loop,
under never-guess rules — and code holds it to evidence at every step.
Budgets (80 tool calls, $1, 30 minutes) exist only to stop a runaway run;
they are set far above what a normal run needs, because a budget that
shapes the research would defeat the design. Two depth mechanisms were
added after the sealed exam showed the remaining gap was search depth: the
research plan the loop reads back at submit time, and the multi-phrasing
search. Both are general — the model steers itself, and code holds it to
its own commitments. On the sealed exam they lifted page coverage from 73%
to 82%, most on the two weakest answers.

The cost of this trade is speed. A timing measurement during development
showed ~97% of a case's wall time is the model thinking — glm-flash takes
20-300 seconds per reply across 25-80 calls. That is the price of the most
accurate option; the `fast` combo answers in ~4 minutes when you need the
machine to move.

## Decision 3 — Memory: a versioned registry, not a vector store

The system remembers between runs exactly what a sector analyst carries
between reporting seasons: how each bank talks. The registry
(`registry/*.json`) maps each bank's own labels to one shared driver
vocabulary — chart bar names, basis words (cash vs statutory), calendar
dates. Two rules carry the design:

1. **No financial numbers.** The registry stores language, never values.
   A remembered number could leak into a fresh case and fake a result; a
   remembered label is just vocabulary. This rule is what makes the holdout
   results trustworthy. It shaped the sealed bank too: Macquarie's registry
   is a deliberate skeleton (names and calendar only), because writing its
   language map after the exam questions existed could have steered the
   agent toward the answers.
2. **Versioned and reviewable.** The registry is JSON in git. Every
   addition is a diff a reviewer can read.

Session memory lives in the artifacts: every answer carries provenance
(models, document hashes, cost, seconds) and its full
evidence records, so any claim is auditable months later without rerunning
anything. Process memory is the wayfinder map plus tickets.

Rejected: a database of "learned facts" (impossible to audit, easy to
contaminate); fine-tuning (nothing here needs new model weights; everything
needs a paper trail).

## Ruling — the two answer shapes hold evidence to different standards (user, 2026-09-01)

A metric case and a free question run the same research loop but face
different code checks, on purpose.

- A metric case asks for a known shape: one movement and drivers that each
  carry one number. Because we know the shape, the code checks it hard: a
  claimed number must appear in the quotes it cites, or its confidence
  drops to 80; a movement no cited record states caps at 20.
- A free question has no fixed shape. A fact is a full sentence; it can
  hold several numbers or a phrase like "roughly doubled". A hard number
  check here would be fragile and would punish good answers. So the code
  checks only that every citation points at a real, word-for-word quote,
  and the judges check every fact against its quotes during evals.

In short: where we know what the answer must contain, code enforces it.
Where we do not, we keep the checks loose rather than over-engineer ones
that break on honest prose.

## Decision 4 — Evals: calibration first, judges second, holdouts sealed

The eval harness answers three questions in order of importance:

1. **Is a stated number right?** Every gold value was sighted on a printed
   page of the bank's own documents, and the page is recorded next to the
   value. Scoring has three states — correct, incorrect, or unscored (a
   claim the gold cannot verify is left out, never guessed at). The grader
   keeps its OWN tolerance numbers, deliberately separate from the
   product's checks, so if a product check is ever loosened the evals catch
   it. If a bank publishes two valid ways to split a movement, both count.
   A made-up sub-driver cannot claim credit for a real one.
2. **Is confidence honest?** Confidence is a 0-100 score the model gives
   itself, and code can only push it down: a failed arithmetic check caps
   it at 40; a claim whose quotes do not print its number caps at 80; a
   movement no cited quote states caps at 20. These caps are few on
   purpose, and each one carries the experiment that justified it in a
   comment — one cap was deleted when a replay showed it never actually
   fired on anything real. Final numbers: dev Brier 0.039, holdout 0.015,
   and zero wrong claims at high confidence anywhere — across 33 graded
   cases, the two wrong movements both gave themselves confidence 0.
3. **Does the narrative say true things?** Two judge models from
   different companies each answer two narrow questions per fact: does the
   note state it, and do the cited quotes back it up? A fact passes only on
   yes-and-yes. If the judges disagree, a human is flagged. If the judging
   window cut off part of the answer or its quotes, the fact is flagged for
   a human too, instead of being counted as wrong — a shortfall in the
   grader's budget is not the answer's error.

The test sets are layered, because iterating on a test slowly bakes its
answers into the system: 25 dev cases (iterated on freely), 8 frozen
holdout cases (run once at a code freeze: 7/8 movements, Brier 0.015, the
one miss at confidence 0), and a sealed 10-question Macquarie exam —
written by an independent model from the documents alone, kept outside the
repository, and sat twice: once by the frozen agent (73% of required pages
found) and once by the final agent (82%). One disclosure: the coordinator
accidentally saw the gold answer for one question; the agent never did,
and that question's marks carry the caveat in both scorecards.

Rejected: judging by model only, with no gold numbers (citing the right
page proves you found it, not that the claim is true); one blended quality
score (it hides exactly the wrong-but-confident tail we care about);
calling any in-repo case "pristine" (every case in the repo existed while
we iterated, so none can honestly claim to be untouched).

## Costs

Whole project: about USD 230 of model spend, most of it on the frontier
bake-off arms and judge runs. The product itself answers a case for
$0.01-0.13 in 6-30 minutes (default) or ~$0.01 in ~4 minutes (fast). A
frontier model per case would cost ~100x more; the system's job was to
close the insight gap without paying that gap in price, and the sealed
exam measures how much of it closed.


## Appendix — judgment calls and probes worth knowing

- **NAB 1H26 NIM**: the bank publishes no year-on-year walk (both charts are
  half-on-half). The agent read them, refused their bars for the wrong
  comparison, built the split from the driver table, and got all six drivers
  right — then capped itself to 40 because two correct values coincide with
  the wrong chart's bars and the leak check cannot prove innocence. The
  designed direction: under-claim a right answer, never certify a wrong one.
- **Vision quote strings**: walk-bar records carry code-built quote strings,
  not page text; their fidelity discipline is the walk sum checks, and the
  entailment judge receives them as quotes. Kept deliberately: the strings
  state code-verified numbers.
- **Frontier probes on the hardest misses**: three frontier-model subagents
  answered the worst-missed questions under the benchmark protocol. They
  found most of the pages the loop missed — the residual gap is retrieval
  depth, priced at roughly 100x per case. The README's next-steps section
  holds the designed (unbuilt) responses.
