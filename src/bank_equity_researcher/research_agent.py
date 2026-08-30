"""Orchestration shell B: the closed-loop research agent (ADR-0005).

The pipeline assembles a fixed context and asks one author to explain it. This
shell inverts that: the model reads, reasons, and chooses what to read next,
through tools that wrap the SAME deterministic estate the pipeline uses —
retrieval, page text, the vision walk reader, reference following, the bank
registry. Nothing here is a new capability; the loop is the new thing.

The artifact contract does not change. A submission becomes the same
Attribution the pipeline emits, and the same validators and the same
confidence caps then run over it, so the eval harness scores the agent exactly
as it scores the pipeline.

Two gates keep the loop honest and bounded:

- CITATION. Every evidence record the agent submits must quote its page
  verbatim. Code checks each quote against the page's own text and rejects one
  that is not there, so a paraphrase can never reach the artifact wearing a
  citation. Rejection is fed back, so the agent can re-read and correct.
- BUDGET. Tool calls, cost and wall-clock are runaway protection, set
  generously (ADR-0005 point 5). On exhaustion the agent is asked for the
  answer it has, with the shortfall declared as a limitation. It never crashes.
"""

from __future__ import annotations

import json
import re
import time
from datetime import datetime, timezone

from .ask import render_answer, slugify
from .author import (
    _percent_evidenced,
    _settle_basis,
    primary_basis,
    settle_charge_sign,
)
from .config import COMBOS, OUT_DIR, REGISTRY_DIR
from .corpus import Document, documents_for_period, documents_for_question
from .extract import extract_walk, printed_page_of
from .llm import LLM
from .refs import scan_page
from .render import render_report
from .retrieve import retrieve
from .schema import (
    Attribution,
    Disagreement,
    DriverClaim,
    EvidenceRecord,
    NumberFact,
    enforce_answer_gate,
    enforce_evidence_gate,
)
from .taxonomy import METRIC_ALIASES, TAXONOMY
from .validate import (
    annotate_walks,
    check_comparison_leak,
    check_component_columns,
    check_drivers_reconcile,
    check_movement,
    check_movement_basis,
    check_movement_columns,
    check_movement_variant,
    check_walk,
    corroborate,
    cross_source_view,
    half_label,
    period_end_date,
    settle_identity_scale,
    walks_for_view,
)

# How much of one page the read_page tool returns. A results-book page runs to
# about 3000 characters, so this covers the densest of them whole; beyond it a
# page is a chapter and the agent should search inside it instead.
MAX_PAGE_CHARS = 7000
# Search results per call, and how much of each page the snippet shows.
MAX_SEARCH_HITS = 8
SNIPPET_CHARS = 240
# A rejected submission is returned to the agent to correct. After this many
# attempts the answer ships with the unverifiable records dropped, because an
# honest partial answer beats no answer at all.
MAX_SUBMIT_ATTEMPTS = 3
# A model that answers in prose instead of calling a tool is nudged back to the
# tools. A loop of nudges is a stuck model, not a research strategy.
MAX_PROSE_TURNS = 3
# The hard stop, counted in TURNS rather than tool calls. Once a budget runs
# out the loop asks for a submission and offers only the submit tool; a model
# that keeps asking for other tools would never meet another budget, because
# the first one to run out latches. These two bounds end the loop regardless.
MAX_TURNS_AFTER_BUDGET = 10
HARD_STOP_FACTOR = 1.5


# The tool surface, described once. Both research tasks — a metric movement and
# a free-form question — drive the SAME loop over the SAME tools, so a change to
# a tool changes one paragraph, not two.
HOW_TO_RESEARCH = """HOW TO RESEARCH
- search_pages finds candidate pages by keyword and by meaning. Search with
  the words the BANK would print, not the words of the question.
- read_page returns one page's text. Read before you cite.
- read_chart reads a waterfall or bridge chart off the page IMAGE. The text
  layer of a chart page prints the numbers and the labels as separate blocks,
  so only this tool can pair a bar with its label.
- cite turns quotes from a page you just read into evidence records with ids.
  Cite a page's facts WHILE you have the page in front of you, all of them in
  one call. Each quote is checked against the page at once, so you find out
  immediately whether it holds.
- follow_references lists what a page points at: notes, appendices, "refer to
  page 21". A summary line gives you the size of a movement; the note behind it
  gives you the reason, the component rows and the split. Follow those pointers
  - the explanation almost never sits on the page that states the total.
- bank_language returns this bank's own vocabulary for its measures.
- submit ends the research and delivers the answer, citing records by id."""

# The two rules no research task may break, in the words both prompts use.
NEVER_GUESS_RULES = """1. NEVER GUESS. Every number you state must come from an evidence record you
   submit and cite. A quantified claim with no evidence id is deleted before
   the answer ships. If you do not know, say so in limitations.
2. CITATION CONTRACT. An evidence record is a VERBATIM quote from ONE page you
   read, with the document and the PDF page it came from. Copy the words off
   the page exactly - character for character, as the page text shows them.
   Code checks every quote against that page's own text and REJECTS any quote
   it cannot find there, so a paraphrase, a tidied number or a sentence merged
   out of two lines loses you the record and every claim resting on it. Quote a
   table row as the page prints it: the row label followed by its printed
   values, in the order the page prints them. Never quote a page you did not
   read, and never cite a record id no tool gave you."""

BUDGET_NOTE = """You have a bounded budget of tool calls. Spend it on reading, not on
re-checking what you already read. If the budget runs out you will be told to
submit what you have: an honest partial answer with its gaps in limitations is
the correct outcome, never a guess that fills them."""

SYSTEM_PROMPT = f"""You are a first-pass banking-sector equity research analyst.

You research ONE question against a bank's own published documents, then you
submit a structured attribution. Nothing is handed to you: you decide what to
read, in what order, and when you have enough.

{HOW_TO_RESEARCH}

A good order of work: find the headline row and read the movement off the two
period columns; find the bank's own decomposition of that movement (a walk
chart, a bridge table, a note); follow the references behind it for the reason;
then check a second document for the same movement before you submit. Cite as
you go - a page you leave uncited is a page you cannot use.

ABSOLUTE RULES - never break these:
{NEVER_GUESS_RULES}
3. BASIS. "basis" names the basis of the numbers inside "movement" - nothing
   else. Use the bank's own primary reporting basis (the one bank_language
   calls its core measure, normally cash) unless the row you actually read is
   labelled statutory or ex-notable. A row that carries NO basis label takes
   the primary basis: never write "statutory" for an unlabelled row, and never
   write it because the figure comes from audited accounts. A KPI page often
   prints the SAME row twice, once under a "statutory basis" block header and
   once under the primary-basis block a few lines away: take the PRIMARY-basis
   block, and quote the other as context.
4. If cash and statutory movements differ materially, show both in the headline
   and record a disagreement with reason "definitional".
5. CONFIDENCE is 0-100: the probability the claim would be judged correct
   against the bank's own disclosure. Rate every driver on the evidence ladder,
   because how a number reached you bounds how sure you may be:
   - a bar you read from a walk of THIS comparison whose sum check passed: 90-95;
   - a movement the bank STATES in words or in a change column ("increased
     $62 million or 9%", "(3)bpts"): up to 90;
   - a delta YOU computed by subtracting two period levels: cap at 80. The
     arithmetic is yours and the framing is not the bank's;
   - an unquantified narrative driver: cap at 60.
6. Report a residual if quantified drivers do not sum to the movement. Never
   force numbers to fit.
7. PERIOD MATCH. read_chart stamps every chart with a code-computed
   "comparison" field. "primary" means its endpoints are exactly the task's two
   balance dates. "context" means it describes a DIFFERENT comparison, printed
   in "comparison_span" - most often the half-on-half movement. Build the
   driver table from PRIMARY charts only. A "contribution" is a statement about
   the task comparison, so a context chart's bar may NEVER become one: not as a
   value, not rounded, not re-signed. If no chart is primary, say so in
   limitations, quantify only what period-matching evidence supports, and give
   the remaining drivers "contribution": null with the context numbers INSIDE
   the narrative, naming the span they belong to. An unquantified but honest
   driver beats a borrowed number.
8. SOURCE HIERARCHY when sources disagree: audited statements and results-book
   tables > results-book narrative > presentation slides > transcripts > else.
   Restated comparatives from the newer document win. Every disagreement you
   notice must be reported with a reason: definitional | rounding |
   restatement | timing | error.
9. CORROBORATE. Read the same movement in a second document before you submit,
   and cite evidence from every document that supports a claim. A claim seen in
   only one document must not exceed confidence 85.
10. WALK PREFERENCE. When more than one chart describes the SAME comparison,
   the results book's chart is the primary framing for your driver table.
   Slide charts corroborate and annotate. NEVER MIX FRAMINGS: every bar in your
   driver table comes from the ONE chart you adopt, at that chart's own value.
   A bar only the other document publishes is a disagreement or a limitation,
   never an extra driver. CLAIM THE WHOLE WALK - every bar of the chart you
   adopt, including bars whose value is 0 and small +-1 bars. A published zero
   bar is the bank's explicit statement that the driver contributed nothing.
11. MOVEMENT COLUMN - mechanical, do this before anything else. A results table
   prints two or THREE period columns and one or two comparison columns. Take
   to_value from the task period's column and from_value from the comparator's
   column of the SAME row. Never take from_value from the prior-half column,
   and never read a movement out of a comparison column. Record where you read
   them in three SHORT fields: movement_row, movement_from_column and
   movement_to_column, each at most 12 words, a citation and nothing else.
   THE SAME DISCIPLINE BINDS EVERY COMPONENT of a bridge: a component's
   contribution is its period column minus its comparator column, or the
   movement the bank states against the comparator - never a difference
   involving the prior-half column, and never a single column's level. Fill
   "columns" on every quantified driver with the two column headers you
   subtracted, at most 12 words.
12. RATIO VARIANT. Use the bank's headline reported measure, read from the
   results book's KPI or summary table. A row whose label merely resembles it
   is a DIFFERENT measure, and so is any named variant: Level 1 against Level
   2, internationally comparable, pro-forma, underlying, ex-notable, tangible
   against ordinary equity, or a single division's ratio. Report a variant as
   context or as a disagreement; never let one supply the movement.
13. EXPLAIN, DO NOT RESTATE. A narrative that repeats its own number back
   tells a reader nothing the driver table already shows. Every driver needs a
   narrative, and each one must carry, from the evidence and no further:
   - the bank's stated reason, in the bank's own words;
   - every SUB-PART the bank names inside that driver, each WITH ITS OWN
     PRINTED NUMBER;
   - the division, product or portfolio the bank points at.
   Carry the printed figures with every fact you mention - the movement, the
   growth rate and the level the bank prints, never the direction alone. The
   explanation belongs INSIDE the driver narratives, not only in the headline,
   and each figure is cited from that driver's own evidence list. Where no
   record states a reason, write that the bank does not disclose one. Never
   supply a reason of your own.
14. CITE THE HEADLINE TOO. The headline states facts that belong to no single
   driver: the levels and growth rates the bank leads with, the movement on the
   other basis or framing printed beside it, a second document's figure for the
   same movement. List in "headline_evidence" the id of EVERY record those
   statements come from. Cite the record that PRINTS the figure you state.
15. SAY WHAT THE WALK HIDES. A bar is a net number and the bank often qualifies
   it: it calls a movement broadly revenue neutral or largely offset, points at
   another line that absorbs it, or reports a gross increase beside the
   decrease that funds it. Repeat the bank's OWN qualifying words inside that
   driver's narrative, and add the qualification to limitations when it changes
   what the movement means.

{BUDGET_NOTE}"""


CASE_PROMPT = """TASK: explain how {bank}'s {metric_name} moved in {period} against
{comparator}, attribute the movement to drivers, and rate your confidence.

PERIOD DEFINITIONS (computed from the bank's calendar):
{period_note}

METHOD FOR THIS METRIC: {method_hint}

THE CANONICAL DRIVER TAXONOMY for {metric_name} (use these canonical ids):
{taxonomy}

HEADLINE ROW for {metric_name} at this bank: {headline_row}

UNITS: express from_value, to_value, delta, and every contribution ALL in
"{unit}". Convert percentages when the unit is bps (2.08% = 208; 12.3% = 1230;
a -3 bps move is from 208 to 205, delta -3) and quote ratio metrics in points
when the unit is ppt (45.7% -> 45.7, a 20 bpts improvement is delta -0.2).
Never mix units inside the movement object.

DOCUMENTS IN THE CORPUS for this case (doc_id, period, pages):
{documents}

Begin by searching. Submit only when you have the movement, the bank's own
decomposition of it, and the reason behind each driver."""


# --------------------------------------------------------------------------
# The second task the same loop serves: a free-form research question.
#
# A question has no movement, no taxonomy and no single comparison, so its
# submission is smaller: the note, the facts it rests on, a confidence and the
# gaps. Everything else is shared - the tools, the loop, the budgets, and the
# citation gate that checks every quote against its page.
# --------------------------------------------------------------------------


QUESTION_SYSTEM_PROMPT = f"""You are a first-pass banking-sector equity research analyst.

You answer ONE question against the banks' own published documents, then you
submit a short note with the evidence under it. Nothing is handed to you: you
decide what to read, in what order, and when you have enough.

{HOW_TO_RESEARCH}

A good order of work: take the question apart into the things it asks, and
find the page that carries each one. A question with three clauses is answered
on three pages far more often than on one. Cite a page's facts while you have
it in front of you, follow what it points at, and read a second document for
the same fact before you submit.

ABSOLUTE RULES - never break these:
{NEVER_GUESS_RULES}
3. ANSWER THE WHOLE QUESTION. Every clause is a part you must answer or
   declare unanswerable. A question that asks you to reconcile two things is
   not answered by describing one of them.
4. CARRY THE PRINTED FIGURES. Give the bank's own numbers with the period and
   the units the page prints, and the direction of every movement. A judgement
   with no number under it is an opinion.
5. SAY WHAT A FIGURE IS AND WHAT IT IS NOT. A bank qualifies its own numbers: a
   measure that excludes named items, a target rather than an outcome, a
   period flow rather than a closing stock, one large exposure inside a
   portfolio total, a growth rate on a base that was restated. Repeat the
   bank's OWN qualifying words beside the figure, and never let a qualified
   figure answer as though it were unqualified.
6. BASIS AND PERIOD. Name the basis (cash, statutory, ex-notable, underlying)
   and the period of every figure, in the bank's own words. Never set two
   figures against each other on different bases without saying so.
7. SOURCE HIERARCHY when sources disagree: audited statements and results-book
   tables > results-book narrative > presentation slides > transcripts > else.
   Restated comparatives from the newer document win. Report a disagreement you
   find rather than choosing one figure silently.
8. COMPARING BANKS. Two banks' headline measures are not one measure. Compare
   each bank on the measure it prefers, name that measure, and state the limits
   of the comparison instead of blending the definitions.
9. CONFIDENCE is 0-100: the probability the answer would be judged correct
   against the banks' own disclosure. A claim seen in only one document must
   not exceed 85. An answer that leaves part of the question unread must not
   exceed 60.
10. LIMITATIONS. Name everything the question asks for that the documents do
   not establish, and every caveat that changes how the answer reads.

{BUDGET_NOTE}"""


QUESTION_PROMPT = """TASK: answer this question from the banks' own published
documents, then submit the note.

QUESTION: {question}

DOCUMENTS IN SCOPE (doc_id, period, pages):
{documents}

THE NOTE ("answer", markdown, at most 400 words): lead with the direct answer
to the question that was asked, in one or two sentences. Then give the
reasoning that supports it, carrying the printed figures, and close with what
the evidence does not settle. Write for a reader who will check every number
against the pages you cite.

KEY FACTS: one entry for each load-bearing fact the note states, with the ids
of the records that print it. A fact carrying a number and no id is deleted
before the note ships.

Begin by searching. Submit when every clause of the question is answered or
declared unanswerable."""


# --------------------------------------------------------------------------
# The tool surface. Each tool is a thin adapter over a function the pipeline
# already calls; none of them adds a capability the estate did not have.
# --------------------------------------------------------------------------

_NUMBER_SCHEMA = {
    "type": "object",
    "properties": {
        "label": {"type": "string", "description": "what the number is, with its period"},
        "value": {"type": "number"},
        "unit": {"type": "string", "description": "bps | $m | % | ppt | ratio"},
        "basis": {
            "type": "string",
            "description": "cash | statutory | ex_notables, only when the page prints the word",
        },
    },
    "required": ["label", "value", "unit"],
}

TOOL_SPECS: list[dict] = [
    {
        "type": "function",
        "function": {
            "name": "search_pages",
            "description": (
                "Search the case's documents for pages matching a query, by keyword and "
                "by meaning. Returns ranked (doc_id, pdf_page, snippet). Search with the "
                "words the bank prints on the page."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "the search query"},
                    "doc_id": {
                        "type": "string",
                        "description": "optional: restrict the search to one document",
                    },
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_page",
            "description": (
                "Return the text of one page. Quotes you submit are checked against this "
                "text, so read a page before you cite it."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "doc_id": {"type": "string"},
                    "pdf_page": {"type": "integer", "description": "1-based PDF page number"},
                },
                "required": ["doc_id", "pdf_page"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_chart",
            "description": (
                "Read a waterfall or bridge chart off the page image: start, every bar "
                "with its label, and end. Also returns a code-computed check of whether "
                "the bars sum, and whether the chart covers the task comparison. Use it "
                "on any page whose text mentions a movement chart."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "doc_id": {"type": "string"},
                    "pdf_page": {"type": "integer", "description": "1-based PDF page number"},
                    "unit": {
                        "type": "string",
                        "description": "bps | $m | % | ppt; defaults to the metric's unit",
                    },
                },
                "required": ["doc_id", "pdf_page"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "cite",
            "description": (
                "Turn verbatim quotes from ONE page into evidence records you can cite by "
                "id. Each quote is checked against that page immediately, so you learn at "
                "once whether it holds. Cite a page's facts as you read it, in one call."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "doc_id": {"type": "string"},
                    "pdf_page": {"type": "integer", "description": "1-based PDF page number"},
                    "quotes": {
                        "type": "array",
                        "description": "every fact you want to cite from this page",
                        "items": {
                            "type": "object",
                            "properties": {
                                "quote": {
                                    "type": "string",
                                    "description": (
                                        "VERBATIM from the page, 50 words maximum. A table "
                                        "row is quoted as the row label with its printed "
                                        "values."
                                    ),
                                },
                                "kind": {"type": "string", "description": "text | table"},
                                "numbers": {"type": "array", "items": _NUMBER_SCHEMA},
                            },
                            "required": ["quote"],
                        },
                    },
                },
                "required": ["doc_id", "pdf_page", "quotes"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "follow_references",
            "description": (
                "List the pages one page points at: numbered notes and appendices, "
                "'refer to page 21', footnote targets. Use it on a summary page to reach "
                "the note that holds the detail."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "doc_id": {"type": "string"},
                    "pdf_page": {"type": "integer", "description": "1-based PDF page number"},
                },
                "required": ["doc_id", "pdf_page"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "bank_language",
            "description": (
                "The bank's own vocabulary: what it calls its core profit measure, its "
                "headline ratio rows, its reporting calendar, and its labels for the "
                "bars of this metric's movement chart. Labels only, never figures."
            ),
            "parameters": {
                "type": "object",
                "properties": {"bank": {"type": "string", "description": "e.g. CBA"}},
                "required": ["bank"],
            },
        },
    },
]

# The evidence list is the same contract whatever is being submitted: the
# citation gate reads it the same way for a movement and for a question.
_EVIDENCE_SCHEMA: dict = {
    "type": "array",
    "description": (
        "Every record your answer cites. For anything you already cited "
        "or read as a chart, pass {\"id\": \"ev-N\"} and nothing else. A "
        "record you did not cite earlier must carry its doc_id, pdf_page "
        "and a VERBATIM quote, and is checked the same way."
    ),
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "e.g. ev-1"},
            "doc_id": {"type": "string"},
            "pdf_page": {"type": "integer"},
            "quote": {
                "type": "string",
                "description": "VERBATIM from that page, 50 words maximum",
            },
            "kind": {"type": "string", "description": "text | table"},
            "numbers": {"type": "array", "items": _NUMBER_SCHEMA},
        },
        "required": ["id"],
    },
}

SUBMIT_SPEC: dict = {
    "type": "function",
    "function": {
        "name": "submit",
        "description": (
            "Deliver the finished attribution and end the research. Every quoted "
            "evidence record is checked against its page before the answer is accepted."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "evidence": _EVIDENCE_SCHEMA,
                "movement": {
                    "type": "object",
                    "properties": {
                        "from_value": {"type": "number"},
                        "to_value": {"type": "number"},
                        "delta": {"type": "number"},
                        "unit": {"type": "string"},
                    },
                },
                "movement_row": {"type": "string", "description": "table row label, <=12 words"},
                "movement_from_column": {"type": "string", "description": "<=12 words"},
                "movement_to_column": {"type": "string", "description": "<=12 words"},
                "basis": {"type": "string", "description": "cash | statutory | ex_notables"},
                "headline": {"type": "string", "description": "<=180 words"},
                "headline_evidence": {"type": "array", "items": {"type": "string"}},
                "drivers": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "canonical": {"type": "string", "description": "a taxonomy id"},
                            "bank_label": {"type": "string"},
                            "contribution": {
                                "type": "object",
                                "properties": {
                                    "value": {"type": "number"},
                                    "unit": {"type": "string"},
                                },
                            },
                            "columns": {"type": "string", "description": "<=12 words"},
                            "narrative": {"type": "string", "description": "<=60 words"},
                            "confidence": {"type": "integer"},
                            "evidence": {"type": "array", "items": {"type": "string"}},
                        },
                        "required": ["canonical", "narrative", "confidence", "evidence"],
                    },
                },
                "residual": {
                    "type": "object",
                    "properties": {"value": {"type": "number"}, "unit": {"type": "string"}},
                },
                "notable_items": {"type": "array", "items": {"type": "string"}},
                "disagreements": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "topic": {"type": "string"},
                            "values": {"type": "array", "items": {"type": "string"}},
                            "preferred": {"type": "string"},
                            "reason": {
                                "type": "string",
                                "description": (
                                    "definitional | rounding | restatement | timing | error"
                                ),
                            },
                            "explanation": {"type": "string"},
                        },
                        "required": ["topic", "values", "preferred", "reason", "explanation"],
                    },
                },
                "attribution_confidence": {"type": "integer"},
                "limitations": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["evidence", "headline", "drivers", "attribution_confidence"],
        },
    },
}

QUESTION_SUBMIT_SPEC: dict = {
    "type": "function",
    "function": {
        "name": "submit",
        "description": (
            "Deliver the finished note and end the research. Every quoted evidence "
            "record is checked against its page before the answer is accepted."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "evidence": _EVIDENCE_SCHEMA,
                "answer": {
                    "type": "string",
                    "description": (
                        "the note itself, markdown, at most 400 words: the direct "
                        "answer first, then the reasoning with its printed figures"
                    ),
                },
                "key_facts": {
                    "type": "array",
                    "description": "one entry per load-bearing fact the note states",
                    "items": {
                        "type": "object",
                        "properties": {
                            "fact": {"type": "string", "description": "<=40 words"},
                            "citations": {
                                "type": "array",
                                "description": "ids of the records that print this fact",
                                "items": {"type": "string"},
                            },
                        },
                        "required": ["fact", "citations"],
                    },
                },
                "confidence": {"type": "integer", "description": "0-100"},
                "limitations": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["evidence", "answer", "key_facts", "confidence"],
        },
    },
}


# --------------------------------------------------------------------------
# Verbatim quoting
# --------------------------------------------------------------------------

_PUNCTUATION = str.maketrans(
    {
        "‘": "'", "’": "'", "‚": "'", "“": '"', "”": '"',
        "–": "-", "—": "-", "−": "-", " ": " ", " ": " ",
    }
)


def quote_key(text: str) -> str:
    """The comparable form of a quote: no whitespace, one spelling per mark.

    Whitespace is dropped rather than collapsed because a PDF text layer breaks
    a table row wherever the column gaps fall, and era pages split a number
    across a space ("47. 0"). Dropping it compares the characters themselves,
    in order, which is what "verbatim" means on a page whose layout the reader
    cannot see. Case is ignored: a text layer re-cases small-caps headings.
    """
    return "".join(
        ch for ch in str(text or "").translate(_PUNCTUATION).lower() if not ch.isspace()
    )


# --------------------------------------------------------------------------
# The toolbox
# --------------------------------------------------------------------------


class Research:
    """The tools, and the evidence they mint.

    Provenance is stamped by code here exactly as it is in the pipeline: the
    agent names a document and a page, and the record's ids, page numbers and
    kinds are filled in from the corpus, never from the model's reply.
    """

    def __init__(self, llm: LLM, combo, docs: list[Document], case: dict, metric_cfg: dict,
                 registry: dict, registries: dict[str, dict] | None = None) -> None:
        self.llm = llm
        self.combo = combo
        self.docs = docs
        self.doc_by_id: dict[str, Document] = {d.doc_id: d for d in docs}
        self.case = case
        self.metric_cfg = metric_cfg
        self.registry = registry
        # A question may span banks, so bank_language answers for the bank it
        # is asked about. A metric case has one bank and leaves this empty.
        self.registries = registries or {}
        self.calendar = registry.get("calendar", {})
        self.records: list[EvidenceRecord] = []
        self.walks: list[dict] = []
        self.validation: dict = {"passed": [], "failed": []}
        self.pages_read: set[tuple[str, int]] = set()
        self.tool_calls = 0
        self._counter = 0

    # -- helpers ----------------------------------------------------------

    def next_id(self) -> str:
        self._counter += 1
        return f"ev-{self._counter}"

    def _doc(self, doc_id: str) -> Document:
        doc = self.doc_by_id.get(str(doc_id))
        if doc is not None:
            return doc
        # A near-miss on a doc_id is common and cheap to fix: match on the
        # unique suffix so the agent does not spend a call on a typo.
        matches = [d for key, d in self.doc_by_id.items() if str(doc_id).lower() in key.lower()]
        if len(matches) == 1:
            return matches[0]
        raise KeyError(
            f"unknown doc_id {doc_id!r}; the corpus holds: {', '.join(sorted(self.doc_by_id))}"
        )

    def _page_text(self, doc: Document, pdf_page: int) -> str:
        texts = doc.page_texts()
        if not 1 <= int(pdf_page) <= len(texts):
            raise IndexError(
                f"{doc.doc_id} has {len(texts)} pages; page {pdf_page} does not exist"
            )
        return texts[int(pdf_page) - 1]

    # -- tools ------------------------------------------------------------

    def search_pages(self, query: str, doc_id: str | None = None) -> dict:
        docs = [self._doc(doc_id)] if doc_id else self.docs
        hits: list[tuple[float, str, int]] = []
        for doc in docs:
            for page, score in retrieve(doc, str(query), top_k=6):
                hits.append((score, doc.doc_id, page))
        hits.sort(key=lambda h: (-h[0], h[1], h[2]))
        results = []
        for score, did, page in hits[:MAX_SEARCH_HITS]:
            text = self._page_text(self.doc_by_id[did], page)
            results.append(
                {
                    "doc_id": did,
                    "pdf_page": page,
                    "score": round(score, 3),
                    "snippet": _snippet(text, str(query)),
                }
            )
        return {"query": query, "results": results}

    def read_page(self, doc_id: str, pdf_page: int) -> dict:
        doc = self._doc(doc_id)
        page = int(pdf_page)
        text = self._page_text(doc, page)
        self.pages_read.add((doc.doc_id, page))
        body = text[:MAX_PAGE_CHARS]
        return {
            "doc_id": doc.doc_id,
            "pdf_page": page,
            "printed_page": printed_page_of(text, page, doc.doc_type),
            "doc_type": doc.doc_type,
            "period": doc.period,
            "truncated": len(text) > MAX_PAGE_CHARS,
            "text": body,
        }

    def read_chart(self, doc_id: str, pdf_page: int, unit: str | None = None) -> dict:
        doc = self._doc(doc_id)
        page = int(pdf_page)
        unit = str(unit or self.metric_cfg["unit"])
        case_desc = self.case["description"]
        try:
            walk, record = extract_walk(
                self.llm, self.combo.vision, doc, page, case_desc, self.next_id, unit=unit
            )
        except Exception as exc:  # noqa: BLE001 - an unreadable chart is a gap, not a crash
            self.validation["failed"].append(f"walk_extraction_error p{page}: {exc}")
            return {"error": f"the chart on {doc.doc_id} p{page} could not be read: {exc}"}
        passed, failed = check_walk(walk, doc.doc_type)
        walk["source"] = f"{doc.doc_id} PDF p{page} ({record.id})"
        walk["record_id"] = record.id
        walk["checks_passed"] = passed
        walk["checks_failed"] = [f"{f} [{walk['source']}]" for f in failed]
        self.validation["passed"] += passed
        self.validation["failed"] += walk["checks_failed"]
        # Classify the chart against the task comparison before the agent reads
        # it, with the same code the pipeline uses on the author's behalf. A
        # free-form question fixes no single comparison, so there is nothing to
        # classify against: the agent reads the span off the chart's own labels.
        if self.case.get("period") and self.case.get("comparator"):
            annotate_walks([walk], self.calendar, self.case["period"], self.case["comparator"])
        else:
            walk["comparison"] = "unclassified"
            walk["comparison_note"] = (
                "This question fixes no single comparison, so this chart was not matched "
                "against one. Read its endpoint labels before you use a bar, and name the "
                "span the bar belongs to."
            )
        self.walks.append(walk)
        self.records.append(record)
        self.pages_read.add((doc.doc_id, page))
        return {
            "doc_id": doc.doc_id,
            "pdf_page": page,
            "evidence_id": record.id,
            "unit": unit,
            "walk": {k: v for k, v in walk.items() if k != "record_id"},
        }

    def follow_references(self, doc_id: str, pdf_page: int) -> dict:
        doc = self._doc(doc_id)
        page = int(pdf_page)
        terms = _relevance_terms(self.metric_cfg)
        try:
            references = scan_page(doc, page, terms)
        except Exception as exc:  # noqa: BLE001 - an unreadable page points nowhere
            return {"error": f"references on {doc.doc_id} p{page} could not be read: {exc}"}
        return {
            "doc_id": doc.doc_id,
            "pdf_page": page,
            "references": [
                {
                    "target": r.target,
                    "kind": ("note", "page", "footnote")[r.tier],
                    "pdf_pages": list(r.pages),
                    "shared_terms_with_task": r.relevance,
                }
                for r in references
            ],
        }

    def cite(self, doc_id: str, pdf_page: int, quotes: list) -> dict:
        """Mint evidence records from verbatim quotes on ONE page.

        Verification belongs where the reading happens, not at the end. The
        agent learns immediately whether a quote is really on the page, and it
        pays one call for as many quotes as the page supports. A record minted
        here is cited later by its id alone.
        """
        doc = self._doc(doc_id)
        page = int(pdf_page)
        text = self._page_text(doc, page)
        self.pages_read.add((doc.doc_id, page))
        cited, rejected = [], []
        for item in quotes if isinstance(quotes, list) else []:
            entry = item if isinstance(item, dict) else {"quote": item}
            record, reason = self._mint_record(doc, page, text, entry)
            if record is None:
                rejected.append({"quote": str(entry.get("quote"))[:120], "reason": reason})
                continue
            self.records.append(record)
            cited.append({"id": record.id, "quote": record.quote})
        result = {"doc_id": doc.doc_id, "pdf_page": page, "cited": cited}
        if rejected:
            result["rejected"] = rejected
            result["instruction"] = (
                "A rejected quote is not on this page as written. Copy the words from the "
                "page text exactly, or cite the page that really prints them."
            )
        return result

    def _mint_record(self, doc: Document, page: int, text: str,
                     item: dict) -> tuple[EvidenceRecord | None, str]:
        """One evidence record, or the reason the quote does not support one."""
        quote = str(item.get("quote") or "").strip()
        if not quote:
            return None, "no quote was given"
        if quote_key(quote) not in quote_key(text):
            return None, f"the quote is not on {doc.doc_id} p{page}"
        numbers = []
        for number in item.get("numbers") or []:
            try:
                numbers.append(
                    NumberFact(
                        **{k: v for k, v in number.items()
                           if k in ("label", "value", "unit", "basis")}
                    )
                )
            except Exception:  # noqa: BLE001 - a malformed number is dropped, not fatal
                continue
        return (
            EvidenceRecord(
                id=self.next_id(),
                doc_id=doc.doc_id,
                pdf_page=page,
                printed_page=printed_page_of(text, page, doc.doc_type),
                kind=str(item.get("kind") or "text"),
                # One line, always. The words are the page's own; the line
                # breaks are the PDF's column layout, and a record keeps only
                # the words. A stored newline would also break the report's
                # block quote, whose ">" prefix marks the first line alone —
                # and every reader that separates an answer's prose from its
                # quotes reads that prefix.
                quote=" ".join(quote.split())[:600],
                numbers=numbers,
            ),
            "",
        )

    def bank_language(self, bank: str | None = None) -> dict:
        """The registry entry, labels only. The registry holds no figures."""
        wanted = str(bank or self.case.get("bank") or "").upper()
        registry = self.registries.get(wanted, self.registry)
        language = {
            "bank": wanted or self.case.get("bank"),
            "measures": registry.get("measures", {}),
            "calendar": registry.get("calendar", {}),
        }
        metric = self.case.get("metric")
        if metric:
            language[f"{metric}_walk_labels"] = registry.get(f"{metric}_walk_labels", {})
        return language

    def dispatch(self, name: str, arguments: dict) -> dict:
        handlers = {
            "search_pages": self.search_pages,
            "read_page": self.read_page,
            "read_chart": self.read_chart,
            "cite": self.cite,
            "follow_references": self.follow_references,
            "bank_language": self.bank_language,
        }
        handler = handlers.get(name)
        if handler is None:
            return {"error": f"no tool named {name!r}; available: {', '.join(handlers)}"}
        try:
            return handler(**arguments)
        except TypeError as exc:
            return {"error": f"{name} rejected those arguments: {exc}"}
        except Exception as exc:  # noqa: BLE001 - a failed tool is a message, not a crash
            return {"error": f"{name} failed: {type(exc).__name__}: {exc}"}

    # -- the citation gate -------------------------------------------------

    def check_citations(self, submitted: list) -> list[str]:
        """Why a submission's evidence entries would not hold, if any.

        The loop asks this BEFORE it accepts a submission, so a rejection can
        be handed back for correction. It mints nothing: a dry run that spent
        record ids would leave gaps in the artifact for every attempt.
        """
        return self._resolve_evidence(submitted)[1]

    def build_records(self, submitted: list) -> tuple[list[EvidenceRecord], list[str], dict]:
        """Turn a submission's evidence list into records, checking every quote.

        Returns (records, rejections, id_map). A record the agent identified by
        the id a tool already minted is taken from the tool, so a chart read
        keeps the numbers the vision pass extracted. Anything else must quote
        its page verbatim, and a quote that is not on that page is rejected.
        """
        resolved, rejections = self._resolve_evidence(submitted)
        records: list[EvidenceRecord] = []
        id_map: dict[str, str] = {}
        used: set[str] = set()
        for claimed, minted, page_source in resolved:
            if minted is not None:
                if claimed not in used:
                    records.append(minted)
                    used.add(claimed)
                id_map[claimed] = claimed
                continue
            doc, page, text, item = page_source
            record, _reason = self._mint_record(doc, page, text, item)
            if record is None:  # pragma: no cover - _resolve_evidence checked it
                continue
            if claimed and claimed not in used:
                record = record.model_copy(update={"id": claimed})
            used.add(record.id)
            id_map[claimed or record.id] = record.id
            records.append(record)
        return records, rejections, id_map

    def _resolve_evidence(self, submitted: list) -> tuple[list[tuple], list[str]]:
        """Sort a submission's evidence into what holds and what does not."""
        by_id = {record.id: record for record in self.records}
        resolved: list[tuple] = []
        rejections: list[str] = []
        for item in submitted if isinstance(submitted, list) else []:
            if not isinstance(item, dict):
                continue
            claimed = str(item.get("id") or "").strip()
            minted = by_id.get(claimed)
            if minted is not None:
                resolved.append((claimed, minted, None))
                continue
            if not str(item.get("quote") or "").strip():
                rejections.append(
                    f"{claimed or '(no id)'}: no quote, and no tool minted that id"
                )
                continue
            try:
                doc = self._doc(item.get("doc_id"))
                page = int(item.get("pdf_page"))
                text = self._page_text(doc, page)
            except Exception as exc:  # noqa: BLE001
                rejections.append(f"{claimed or '(no id)'}: {exc}")
                continue
            if quote_key(str(item.get("quote"))) not in quote_key(text):
                rejections.append(
                    f"{claimed or '(no id)'}: the quote is not on {doc.doc_id} p{page}. "
                    "Re-read that page and copy the words exactly, or cite the page that "
                    "really prints them."
                )
                continue
            resolved.append((claimed, None, (doc, page, text, item)))
        return resolved, rejections


def _keep_valid(items, model, dropped: list[str], what: str) -> list:
    """Every item the schema accepts, with each rejection recorded.

    One malformed sub-object must not cost a whole research run its answer. A
    driver rated 105, or a disagreement whose reason is not one of the five,
    is dropped and named in limitations — the artifact then says what it lost,
    which is the honest outcome and the one a reader can check.
    """
    kept = []
    for item in items or []:
        try:
            kept.append(model.model_validate(item))
        except Exception as exc:  # noqa: BLE001
            dropped.append(f"{what} dropped as malformed ({str(exc).splitlines()[0][:120]})")
    return kept


def _snippet(text: str, query: str) -> str:
    """A window of the page around the first query word that appears on it."""
    words = [w for w in re.findall(r"[A-Za-z]{4,}", query.lower())]
    lowered = text.lower()
    at = next((lowered.find(w) for w in words if lowered.find(w) >= 0), -1)
    start = max(0, at - SNIPPET_CHARS // 3) if at >= 0 else 0
    return re.sub(r"\s+", " ", text[start:start + SNIPPET_CHARS]).strip()


def _relevance_terms(metric_cfg: dict) -> set[str]:
    from .refs import _words

    return _words(" ".join([*metric_cfg["retrieval_queries"], metric_cfg["name"]]))


# --------------------------------------------------------------------------
# From a submission to the artifact
# --------------------------------------------------------------------------


def build_attribution(payload: dict, research: Research, case: dict, metric_cfg: dict,
                      registry: dict) -> tuple[Attribution, list[str]]:
    """Assemble the Attribution a submission describes.

    The reply-level normalisers are the author's own (unit slips, the charge
    sign convention, the basis word, the delta against its endpoints): the
    agent writes the same reply shape, so it inherits the same corrections and
    the artifact stays one contract rather than two.
    """
    from .author import _movement_source

    records, rejections, id_map = research.build_records(payload.get("evidence"))
    reply = dict(payload)
    movement = reply.get("movement")
    if isinstance(movement, dict) and any(
        movement.get(k) is None for k in ("from_value", "to_value", "delta")
    ):
        movement = None
        reply.setdefault("limitations", []).append(
            "The movement could not be established from the evidence."
        )
    if isinstance(movement, dict) and metric_cfg["unit"] == "bps":
        frm, to = movement.get("from_value"), movement.get("to_value")
        if (
            isinstance(frm, (int, float))
            and isinstance(to, (int, float))
            and max(abs(frm), abs(to)) < 100
            and _percent_evidenced(frm, records)
            and _percent_evidenced(to, records)
        ):
            movement["from_value"], movement["to_value"] = frm * 100, to * 100
            if abs(movement.get("delta", 0) - round((to - frm) * 100, 1)) > 0.51:
                movement["delta"] = round((to - frm) * 100, 1)
            reply.setdefault("limitations", []).append(
                f"Movement endpoints converted from percent ({frm}, {to}) to bps: the unit "
                "for this metric is bps."
            )
    if isinstance(movement, dict):
        movement = settle_charge_sign(movement, metric_cfg, reply)
    if isinstance(movement, dict):
        implied = round(movement["to_value"] - movement["from_value"], 2)
        if abs(movement["delta"] - implied) > 0.51 and implied != 0:
            reply.setdefault("limitations", []).append(
                f"Movement delta normalised from {movement['delta']} to {implied} "
                "(unit slip against the endpoints)."
            )
            movement["delta"] = implied

    def remap(ids) -> list[str]:
        return [id_map.get(str(e), str(e)) for e in ids or [] if isinstance(e, (str, int))]

    # A citation to a record a tool already verified is a citation, whether or
    # not the submission repeated it in the evidence list. The record is
    # carried in rather than stripped: it was minted from the page's own words,
    # so dropping the claim that rests on it would punish bookkeeping, not a
    # guess. An id no tool minted still resolves to nothing and still falls to
    # the evidence gate.
    minted_by_id = {record.id: record for record in research.records}
    present = {record.id for record in records}
    for cited in [
        *(reply.get("headline_evidence") or []),
        *(e for driver in reply.get("drivers") or []
          if isinstance(driver, dict) for e in driver.get("evidence") or []),
    ]:
        key = str(cited)
        if key in minted_by_id and key not in present and key not in id_map:
            records.append(minted_by_id[key])
            present.add(key)

    prepared = []
    for driver in reply.get("drivers") or []:
        if not isinstance(driver, dict):
            continue
        driver = dict(driver)
        contribution = driver.get("contribution")
        if isinstance(contribution, dict) and contribution.get("value") is None:
            driver["contribution"] = None
        if driver.get("columns") is not None:
            driver["columns"] = str(driver["columns"]).strip()[:120] or None
        driver["evidence"] = remap(driver.get("evidence"))
        driver["narrative"] = str(driver.get("narrative") or "")
        prepared.append(driver)
    dropped: list[str] = []
    # A contribution is a share of THIS movement, so it is stated in the
    # movement's own unit. A value in another unit is a fact about something
    # else: the CBA FY26 cash-earnings run claimed the -3 bps margin move as a
    # component of a $m bridge, where the reconciliation summed it as -3
    # dollars. The number is not deleted - it stays in the narrative, where it
    # belongs - but it stops being a quantified contribution.
    unit = metric_cfg["unit"]
    for driver in prepared:
        contribution = driver.get("contribution")
        if not isinstance(contribution, dict):
            continue
        given = str(contribution.get("unit") or unit).strip()
        if given.lower() == unit.lower():
            continue
        driver["contribution"] = None
        driver["confidence"] = min(int(driver.get("confidence") or 0), 60)
        dropped.append(
            f"{driver.get('canonical', '?')} was claimed as "
            f"{contribution.get('value')} {given}, which is not the movement's unit "
            f"({unit}); it is reported in the narrative and not as a contribution"
        )
    drivers = _keep_valid(prepared, DriverClaim, dropped, "driver")
    disagreements = _keep_valid(
        reply.get("disagreements"), Disagreement, dropped, "disagreement"
    )

    # _settle_basis records its own substitution in reply["limitations"], so it
    # runs before the limitations list is read out of the reply.
    basis = _settle_basis(reply.get("basis", "cash"), registry, records, reply)
    limitations = [str(item) for item in reply.get("limitations") or []] + dropped
    if rejections:
        limitations.append(
            "These citations were dropped because the quote was not found on the page "
            "given: " + "; ".join(rejections)
        )
    attribution = Attribution(
        bank=case["bank"],
        metric=case["metric"],
        period=case["period"],
        comparator=case["comparator"],
        basis=basis,
        movement=movement,
        movement_source=_movement_source(reply),
        headline=str(reply.get("headline") or ""),
        headline_evidence=remap(reply.get("headline_evidence")),
        drivers=drivers,
        residual=reply.get("residual") if isinstance(reply.get("residual"), dict) else None,
        notable_items=[str(i) for i in reply.get("notable_items") or []],
        disagreements=disagreements,
        attribution_confidence=int(reply.get("attribution_confidence") or 0),
        limitations=limitations,
        evidence_records=records,
    )
    return enforce_evidence_gate(attribution), rejections


def finalise(attribution: Attribution, research: Research, case: dict, metric_cfg: dict,
             registry: dict, headline_label: str | None) -> Attribution:
    """Run the estate's validators and confidence caps over a submission.

    These are the pipeline's own output-level checks and caps, applied to the
    agent's answer unchanged: the same functions, the same thresholds, the same
    grading of which failure is fatal. An answer is scored by what it can
    prove, whoever assembled it.
    """
    calendar = research.calendar
    period, comparator = case["period"], case["comparator"]
    period_date = period_end_date(period, calendar)
    comparator_date = period_end_date(comparator, calendar)
    prior_half_date = None
    if period_date:
        prior_half_date = (
            (period_date[0] - 6, period_date[1]) if period_date[0] > 6
            else (period_date[0] + 6, period_date[1] - 1)
        )
        if prior_half_date == comparator_date:
            prior_half_date = None
    prior_half_tag = half_label(prior_half_date, calendar)
    bank_basis = primary_basis(registry) if registry.get("measures") else None
    is_bridge = metric_cfg["method"] == "bridge_extraction"

    walks = research.walks
    walks.sort(key=lambda w: 0 if w.get("comparison") == "primary" else 1)
    primary_walks = [w for w in walks if w.get("comparison") == "primary"]
    context_walks = [w for w in walks if w.get("comparison") == "context"]
    classified = primary_walks + context_walks
    label_map = registry.get(f"{case['metric']}_walk_labels", {})
    view_walks, _view_note = walks_for_view(walks)
    cross_source = cross_source_view(view_walks, label_map)
    primary_view = cross_source_view(primary_walks, label_map)
    context_view = cross_source_view(context_walks, label_map)

    settle_identity_scale(attribution, metric_cfg["method"])
    corroborate(attribution, cross_source)
    if is_bridge:
        for driver in attribution.drivers:
            if driver.contribution is None or driver.confidence <= 80:
                continue
            cited = [r for r in attribution.evidence_records if r.id in driver.evidence]
            stated = any(
                abs(abs(number.value) - abs(driver.contribution.value)) <= 0.5
                for record in cited
                for number in record.numbers
            )
            if not stated:
                driver.confidence = 80
                driver.checks_passed.append("computed_delta_cap_80")
        split = {
            d.canonical: d
            for d in attribution.drivers
            if d.contribution is not None
            and d.canonical in ("operating_expenses", "notable_items")
        }
        if len(split) == 2:
            for driver in split.values():
                driver.confidence = min(driver.confidence, 80)
            attribution.limitations.append(
                "Expenses are claimed on the underlying/notable split; the bank equally "
                "publishes the combined headline framing, so both claims are capped at 80."
            )

    validation = research.validation
    output_failed: list[str] = []
    drivers_passed, drivers_failed = check_drivers_reconcile(attribution)
    component = (
        check_component_columns(
            attribution, period_date, comparator_date, prior_half_date, prior_half_tag
        )
        if is_bridge
        else ([], [])
    )
    for check in (
        check_movement(attribution.movement),
        (drivers_passed, drivers_failed),
        check_comparison_leak(attribution, primary_view, context_view),
        check_movement_columns(attribution, period_date, comparator_date, prior_half_date),
        check_movement_variant(attribution, headline_label),
        check_movement_basis(attribution, bank_basis, headline_label),
        component,
    ):
        validation["passed"] += check[0]
        output_failed += check[1]

    peripheral = [f for f in validation["failed"] if f.startswith("walk_extraction_error")]
    primary_sum_ok = any("walk_sum" in walk.get("checks_passed", []) for walk in primary_walks)
    for walk in walks:
        if not walk.get("checks_failed"):
            continue
        load_bearing = walk.get("comparison") == "primary" and not (
            primary_sum_ok and "drivers_reconcile" in drivers_passed
        )
        if not load_bearing:
            peripheral += walk["checks_failed"]
    fatal = output_failed + [f for f in validation["failed"] if f not in peripheral]
    honest_partial: list[str] = []
    if metric_cfg["method"] == "two_level_arithmetic" or (
        metric_cfg["method"] == "walk_extraction" and classified and not primary_walks
    ):
        fatal = [f for f in fatal if f != "no_quantified_drivers"]
        honest_partial += [f for f in output_failed if f == "no_quantified_drivers"]
    if peripheral and "walk_sum" not in validation["passed"]:
        fatal += peripheral
        peripheral = []
    peripheral += honest_partial
    validation["failed"] += output_failed
    if fatal or peripheral:
        attribution.limitations.extend(f"Failed check: {f}" for f in fatal + peripheral)
    if fatal:
        attribution.attribution_confidence = min(attribution.attribution_confidence, 40)
    elif metric_cfg["method"] == "walk_extraction" and classified and not primary_walks:
        attribution.limitations.append(
            f"No published walk covers {period} vs {comparator}: the bank's walk for this "
            "metric describes another comparison, so the driver split is not walk-verified "
            "for this comparison. Confidence is capped at 85."
        )
        attribution.attribution_confidence = min(attribution.attribution_confidence, 85)
        for driver in attribution.drivers:
            driver.confidence = min(driver.confidence, 85)
    if metric_cfg["method"] == "walk_extraction" and not primary_walks and (
        classified or not walks
    ):
        for driver in attribution.drivers:
            driver.confidence = min(driver.confidence, 85)
    return attribution


# --------------------------------------------------------------------------
# The loop
# --------------------------------------------------------------------------


def _arguments(call: dict) -> dict:
    """The arguments of one tool call, whichever way the provider encoded them."""
    raw = (call.get("function") or {}).get("arguments")
    if isinstance(raw, dict):
        return raw
    try:
        parsed = json.loads(raw or "{}")
    except (TypeError, ValueError):
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _assistant_turn(message: dict) -> dict:
    """The assistant message as it must be echoed back into the transcript."""
    turn = {"role": "assistant", "content": message.get("content") or ""}
    if message.get("tool_calls"):
        turn["tool_calls"] = message["tool_calls"]
    return turn


def _tool_result(call_id: str, payload: dict) -> dict:
    return {"role": "tool", "tool_call_id": call_id, "content": json.dumps(payload)[:60000]}


def research_loop(llm: LLM, combo, research: Research, messages: list[dict],
                  submit_spec: dict, started: float) -> tuple[dict | None, str | None]:
    """Drive the closed loop until it submits, or until a budget ends it.

    Returns (the submitted payload or None, the budget that ran out or None).
    The loop knows nothing about what is being submitted: it moves tool calls
    to the toolbox and results back, and it runs the citation gate over any
    submission before it accepts one. That is why a movement and a free-form
    question share it - only the submit schema and the prompts differ.
    """
    tools = [*TOOL_SPECS, submit_spec]
    payload: dict | None = None
    submit_attempts = 0
    prose_turns = 0
    turns = 0
    exhausted: str | None = None
    while payload is None:
        spent = time.time() - started
        # The hard stop. Asking for a submission is a REQUEST, and a model that
        # ignores it — by calling a tool it was no longer offered, turn after
        # turn — would otherwise loop for ever, because the first budget to run
        # out latches and stops being re-read. These two bounds cannot be
        # talked past: they end the loop whatever the reply says.
        turns += 1
        if turns > combo.max_tool_calls + MAX_TURNS_AFTER_BUDGET or (
            spent >= HARD_STOP_FACTOR * combo.wall_clock_s
        ):
            exhausted = exhausted or f"the wall-clock budget ({combo.wall_clock_s:.0f}s)"
            break
        if exhausted is None:
            if research.tool_calls >= combo.max_tool_calls:
                exhausted = f"the tool-call budget ({combo.max_tool_calls} calls)"
            elif llm.usage.cost_usd >= combo.cost_ceiling_usd:
                exhausted = f"the cost ceiling (${combo.cost_ceiling_usd:.2f})"
            elif spent >= combo.wall_clock_s:
                exhausted = f"the wall-clock budget ({combo.wall_clock_s:.0f}s)"
            if exhausted:
                messages.append(
                    {
                        "role": "user",
                        "content": (
                            f"The research budget is spent: you reached {exhausted}. Call "
                            "submit now with the answer your evidence already supports. "
                            "Leave unproved claims unquantified, name every gap in "
                            "limitations, and lower your confidence to match. Do not "
                            "state a number you did not read."
                        ),
                    }
                )
        turn_tools = [submit_spec] if exhausted else tools
        message = llm.chat_tools(
            combo.agent, messages, turn_tools, max_tokens=combo.agent_max_tokens
        )
        messages.append(_assistant_turn(message))
        calls = message.get("tool_calls") or []
        if not calls:
            prose_turns += 1
            if prose_turns > MAX_PROSE_TURNS:
                break
            messages.append(
                {
                    "role": "user",
                    "content": (
                        "Answer only by calling a tool. Keep researching, or call submit "
                        "with the answer."
                    ),
                }
            )
            continue
        # Every call in a turn is answered, whatever happens to the others: a
        # provider that asked for two tools and got one result back rejects the
        # next request outright.
        for call in calls:
            name = (call.get("function") or {}).get("name") or ""
            call_id = call.get("id") or name
            arguments = _arguments(call)
            if name != "submit":
                research.tool_calls += 1
                messages.append(_tool_result(call_id, research.dispatch(name, arguments)))
                continue
            if payload is not None:
                messages.append(
                    _tool_result(call_id, {"accepted": False,
                                           "reason": "the answer was already submitted"})
                )
                continue
            submit_attempts += 1
            rejections = research.check_citations(arguments.get("evidence"))
            if rejections and submit_attempts < MAX_SUBMIT_ATTEMPTS:
                research.tool_calls += 1
                messages.append(
                    _tool_result(
                        call_id,
                        {
                            "accepted": False,
                            "rejected_citations": rejections,
                            "instruction": (
                                "Each rejected quote is not on the page you named. Re-read "
                                "that page with read_page, copy the words exactly as printed, "
                                "and submit again. Drop any claim you cannot quote."
                            ),
                        },
                    )
                )
                continue
            payload = arguments
            messages.append(_tool_result(call_id, {"accepted": True}))
    return payload, exhausted


def run_agent_case(bank: str, metric: str, period: str, comparator: str | None,
                   combo_name: str = "agentic"):
    """Research one case in a closed loop, then write the pipeline's artifacts."""
    from .pipeline import build_period_note, default_comparator

    started = time.time()
    combo = COMBOS[combo_name]
    if not combo.agent:
        raise ValueError(f"combo {combo_name} declares no agent model")
    llm = LLM()
    metric_key = METRIC_ALIASES[metric.lower()]
    metric_cfg = TAXONOMY[metric_key]
    comparator = comparator or default_comparator(period)
    case = {"bank": bank, "metric": metric_key, "period": period, "comparator": comparator}
    case["description"] = f"{bank} {metric_cfg['name']} in {period} vs {comparator}"

    registry_path = REGISTRY_DIR / f"{bank.lower()}.json"
    registry = json.loads(registry_path.read_text()) if registry_path.exists() else {}
    period_note = build_period_note(period, comparator, registry.get("calendar", {}))
    headline_label = registry.get("measures", {}).get(
        {
            "cash_earnings": "core_profit",
            "cti": "cti_label",
            "roe": "roe_label",
            "impairment": "impairment_line",
        }.get(metric_key, "")
    )

    docs = documents_for_period(bank, period, comparator)
    if not docs:
        raise RuntimeError(f"no documents in corpus for {bank} {period}/{comparator}")
    research = Research(llm, combo, docs, case, metric_cfg, registry)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": CASE_PROMPT.format(
                bank=bank,
                metric_name=metric_cfg["name"],
                period=period,
                comparator=comparator,
                period_note=period_note,
                method_hint=metric_cfg.get("method_hint", ""),
                taxonomy=json.dumps(metric_cfg["drivers"], indent=1),
                headline_row=headline_label
                or (
                    "the registry records no row for this metric - take the bank's own "
                    "headline measure from the results book's KPI table"
                ),
                unit=metric_cfg["unit"],
                documents="\n".join(
                    f"- {d.doc_id} ({d.period}, {len(d.page_texts())} pages)" for d in docs
                ),
            ),
        },
    ]

    payload, exhausted = research_loop(llm, combo, research, messages, SUBMIT_SPEC, started)

    if payload is None:
        # The loop ended without a submission. An artifact still ships: it
        # carries what was read and says plainly that nothing was concluded.
        payload = {
            "evidence": [{"id": record.id} for record in research.records],
            "headline": "",
            "drivers": [],
            "attribution_confidence": 0,
            "limitations": [
                "The research loop ended without a submitted attribution "
                f"({exhausted or 'the model stopped calling tools'})."
            ],
        }
    attribution, _rejections = build_attribution(payload, research, case, metric_cfg, registry)
    if exhausted:
        attribution.limitations.append(
            f"Research stopped early: {exhausted} was reached, so the evidence behind this "
            "answer is less complete than a full run's."
        )
    attribution = finalise(attribution, research, case, metric_cfg, registry, headline_label)

    attribution.provenance = {
        "combo": combo.name,
        "models": f"agent={combo.agent}, vision={combo.vision}",
        "documents": ", ".join(f"{d.doc_id} ({(d.sha256 or '')[:12]})" for d in docs),
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "seconds": round(time.time() - started, 1),
        "cost_usd": round(llm.usage.cost_usd, 4),
        "tokens": f"{llm.usage.prompt_tokens} in / {llm.usage.completion_tokens} out",
        "orchestration": "agent",
        "tool_calls": research.tool_calls,
        "pages_read": len(research.pages_read),
        "charts_read": len(research.walks),
        "budget_exhausted": exhausted or "no",
    }

    slug = f"{bank}-{metric_key}-{period}-vs-{comparator}-{combo.name}".lower()
    out = OUT_DIR / slug
    out.mkdir(parents=True, exist_ok=True)
    (out / "attribution.json").write_text(attribution.model_dump_json(indent=2))
    (out / "report.md").write_text(render_report(attribution))
    return attribution, out


# --------------------------------------------------------------------------
# The question shell: the same loop, a smaller submission.
# --------------------------------------------------------------------------


def question_scope(question: str, docs: list[Document]) -> tuple[dict, dict, dict]:
    """The case, the metric config and the registries a question researches with.

    A question has no metric, so the fields the toolbox reads off a metric are
    filled from the question itself: its own words are the relevance terms
    reference-following ranks by, and there is no period pair to classify a
    chart against.
    """
    banks = list(dict.fromkeys(doc.bank for doc in docs))
    registries: dict[str, dict] = {}
    for bank in banks:
        path = REGISTRY_DIR / f"{bank.lower()}.json"
        registries[bank] = json.loads(path.read_text()) if path.exists() else {}
    case = {
        "bank": ", ".join(banks),
        "metric": None,
        "period": None,
        "comparator": None,
        "description": str(question)[:300],
    }
    metric_cfg = {
        "name": "the question",
        "unit": "$m",
        "method": "free_form",
        "retrieval_queries": [str(question)],
        "drivers": {},
    }
    return case, metric_cfg, registries


def build_answer(payload: dict, research: Research, question: str, docs: list[Document]) -> dict:
    """Assemble the answer artifact one submission describes.

    Every record is re-checked against its page here, exactly as a movement's
    records are: the loop's own check is a dry run that mints nothing. The
    output is the shape ask.py emits, so the renderer, the scorers and the
    judge read one artifact whichever shell produced it.
    """
    records, rejections, id_map = research.build_records(payload.get("evidence"))
    # A record a tool minted and the note cites, but the evidence list forgot,
    # is carried in rather than stripped: it was verified against the page's
    # own words when the tool minted it (the same rule the movement path uses).
    minted_by_id = {record.id: record for record in research.records}
    present = {record.id for record in records}
    for fact in payload.get("key_facts") or []:
        if not isinstance(fact, dict):
            continue
        for cited in fact.get("citations", fact.get("evidence")) or []:
            key = str(cited)
            if key in minted_by_id and key not in present and key not in id_map:
                records.append(minted_by_id[key])
                present.add(key)

    def remap(fact: dict) -> dict:
        cited = fact.get("citations", fact.get("evidence")) or []
        cited = [cited] if isinstance(cited, str) else list(cited)
        return {
            "fact": str(fact.get("fact", "")),
            "citations": [id_map.get(str(e), str(e)) for e in cited],
        }

    raw_limitations = payload.get("limitations") or []
    if isinstance(raw_limitations, str):
        raw_limitations = [raw_limitations]
    limitations = [str(item) for item in raw_limitations]
    if rejections:
        limitations.append(
            "These citations were dropped because the quote was not found on the page "
            "given: " + "; ".join(rejections)
        )
    key_facts, limitations, confidence = enforce_answer_gate(
        [remap(f) for f in payload.get("key_facts") or [] if isinstance(f, dict)],
        limitations,
        int(payload.get("confidence") or 0),
        {record.id for record in records},
    )
    return {
        "question": question,
        "bank": ", ".join(dict.fromkeys(doc.bank for doc in docs)),
        "periods": list(dict.fromkeys(doc.period for doc in docs)),
        "answer": str(payload.get("answer") or ""),
        "key_facts": key_facts,
        "confidence": confidence,
        "limitations": limitations,
        "evidence_records": [record.model_dump() for record in records],
    }


def run_agent_question(bank: str | None, question: str, combo_name: str = "agentic",
                       periods: list[str] | None = None):
    """Answer one free-form question in the closed loop. Returns (output, out_dir).

    The signature matches ask.run_ask, so config.question_runner_for hands a
    caller either shell without an adapter. `bank` and `periods` are hints from
    a caller that already knows them; a question that names its own banks and
    periods needs neither.
    """
    started = time.time()
    combo = COMBOS[combo_name]
    if not combo.agent:
        raise ValueError(f"combo {combo_name} declares no agent model")
    llm = LLM()

    docs = documents_for_question(question, bank, periods)
    if not docs:
        raise RuntimeError(
            f"no documents in corpus for {bank or 'the banks named'} "
            f"{'/'.join(periods or []) or 'in the question'}"
        )
    case, metric_cfg, registries = question_scope(question, docs)
    research = Research(
        llm, combo, docs, case, metric_cfg,
        next(iter(registries.values()), {}), registries,
    )

    messages = [
        {"role": "system", "content": QUESTION_SYSTEM_PROMPT},
        {
            "role": "user",
            "content": QUESTION_PROMPT.format(
                question=question,
                documents="\n".join(
                    f"- {d.doc_id} ({d.period}, {len(d.page_texts())} pages)" for d in docs
                ),
            ),
        },
    ]
    payload, exhausted = research_loop(
        llm, combo, research, messages, QUESTION_SUBMIT_SPEC, started
    )
    if payload is None:
        # The loop ended without a submission. An artifact still ships: it
        # carries what was read and says plainly that nothing was concluded.
        payload = {
            "evidence": [{"id": record.id} for record in research.records],
            "answer": "",
            "key_facts": [],
            "confidence": 0,
            "limitations": [
                "The research loop ended without a submitted answer "
                f"({exhausted or 'the model stopped calling tools'})."
            ],
        }
    output = build_answer(payload, research, question, docs)
    if exhausted:
        output["limitations"].append(
            f"Research stopped early: {exhausted} was reached, so the evidence behind this "
            "answer is less complete than a full run's."
        )
    output["provenance"] = {
        "combo": combo.name,
        "models": f"agent={combo.agent}, vision={combo.vision}",
        "documents": ", ".join(f"{d.doc_id} ({(d.sha256 or '')[:12]})" for d in docs),
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "seconds": round(time.time() - started, 1),
        "cost_usd": round(llm.usage.cost_usd, 4),
        "tokens": f"{llm.usage.prompt_tokens} in / {llm.usage.completion_tokens} out",
        "orchestration": "agent",
        "tool_calls": research.tool_calls,
        "pages_read": len(research.pages_read),
        "charts_read": len(research.walks),
        "budget_exhausted": exhausted or "no",
    }

    out = OUT_DIR / f"ask-{slugify(question)}-{combo.name}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "answer.json").write_text(json.dumps(output, indent=2))
    (out / "answer.md").write_text(render_answer(output))
    return output, out


__all__ = [
    "QUESTION_SUBMIT_SPEC",
    "SUBMIT_SPEC",
    "TOOL_SPECS",
    "Research",
    "build_answer",
    "build_attribution",
    "finalise",
    "question_scope",
    "quote_key",
    "research_loop",
    "run_agent_case",
    "run_agent_question",
]
