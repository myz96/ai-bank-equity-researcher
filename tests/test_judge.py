"""Citation-grounding judge tests (tickets 02, 05; ticket 29 finding 7).

The verdict table is the specification. Every row names the mistake it stops:

- AGREEMENT PASS: both judges say the note states the fact and the quotes
  entail it, so the fact counts.
- AGREEMENT FAIL: the judges agree the grounding is missing. A cited page is
  not a supported claim (finding 7: coverage is not correctness).
- DISAGREEMENT: two judges from different model families split ON THE VERDICT,
  so no verdict is recorded. A tie-break would invent agreement that does not
  exist.
- WORDING SPLIT: the judges name different degrees of the same failure. The
  item fails under either reading, so a human is not called for wording. A
  human is flagged for a decision the judges could not make.
- MALFORMED: a judge that cannot answer inside the vocabulary is not evidence
  that the answer is right, so the fact is flagged, never passed.
- NO CITATION: nothing cannot entail anything.

The judge models are mocked. These tests never touch the network.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher import judge as judge_module
from bank_equity_researcher.evals import crossref_passes, score_crossref
from bank_equity_researcher.judge import (
    ABSENT,
    ENTAILED,
    FAIL,
    FLAGGED,
    NOT_ENTAILED,
    PARTIAL,
    PASS,
    STATED,
    answer_prose,
    cited_quotes,
    judge_fact,
    judge_facts,
)

JUDGES = ("deepseek/deepseek-v4-pro-0813", "qwen/qwen3.7-flash")
FACT = "home lending pricing competition (-4 bps within asset pricing; PA p28 text)"
ANSWER = "Asset pricing cost 5 bps, of which home lending competition was 4 bps."
QUOTES = ['Asset pricing: Decreased margin by 5 basis points driven by home lending pricing (down 4 basis points).']


class FakeLLM:
    """A judge stand-in keyed by model, then by which question it was asked.

    A reply may be a dict (returned as parsed JSON), an Exception (raised, as
    llm.chat_json raises on an unparseable body), or any other object (returned
    as-is, so a non-object reply is exercised too).
    """

    def __init__(self, replies: dict[str, dict[str, object]]) -> None:
        self.replies = replies
        self.prompts: list[tuple[str, str]] = []

    def chat_json(self, model: str, prompt: str, **_kwargs):
        question = ENTAILED if prompt.startswith("You check whether verbatim") else STATED
        self.prompts.append((model, question))
        reply = self.replies[model][question]
        if isinstance(reply, Exception):
            raise reply
        return reply


def both(stated: str, entailed: str) -> dict:
    return {model: {STATED: {"stated": stated}, ENTAILED: {"entailed": entailed}} for model in JUDGES}


# ---------------------------------------------------------------------------
# The verdict table
# ---------------------------------------------------------------------------

VERDICT_TABLE = [
    # name, per-model replies, expected verdict, expected (stated, entailed)
    ("AGREEMENT PASS", both(STATED, ENTAILED), PASS, (STATED, ENTAILED)),
    ("AGREEMENT FAIL: stated but ungrounded", both(STATED, NOT_ENTAILED), FAIL, (STATED, NOT_ENTAILED)),
    ("AGREEMENT FAIL: absent from the note", both(ABSENT, ENTAILED), FAIL, (ABSENT, ENTAILED)),
    ("AGREEMENT FAIL: partial is not a soft pass", both(PARTIAL, ENTAILED), FAIL, (PARTIAL, ENTAILED)),
    (
        "DISAGREEMENT on stated",
        {
            JUDGES[0]: {STATED: {"stated": STATED}, ENTAILED: {"entailed": ENTAILED}},
            JUDGES[1]: {STATED: {"stated": ABSENT}, ENTAILED: {"entailed": ENTAILED}},
        },
        FLAGGED,
        (None, ENTAILED),
    ),
    (
        "DISAGREEMENT: stated against partial changes the verdict",
        {
            JUDGES[0]: {STATED: {"stated": STATED}, ENTAILED: {"entailed": ENTAILED}},
            JUDGES[1]: {STATED: {"stated": PARTIAL}, ENTAILED: {"entailed": ENTAILED}},
        },
        FLAGGED,
        (None, ENTAILED),
    ),
    (
        "DISAGREEMENT on entailment",
        {
            JUDGES[0]: {STATED: {"stated": STATED}, ENTAILED: {"entailed": ENTAILED}},
            JUDGES[1]: {STATED: {"stated": STATED}, ENTAILED: {"entailed": NOT_ENTAILED}},
        },
        FLAGGED,
        (STATED, None),
    ),
    (
        "WORDING SPLIT: partial against absent keeps the same verdict",
        {
            JUDGES[0]: {STATED: {"stated": PARTIAL}, ENTAILED: {"entailed": ENTAILED}},
            JUDGES[1]: {STATED: {"stated": ABSENT}, ENTAILED: {"entailed": ENTAILED}},
        },
        FAIL,
        (PARTIAL, ENTAILED),
    ),
    (
        "MALFORMED: the reply does not parse",
        {
            JUDGES[0]: {STATED: ValueError("no JSON in reply"), ENTAILED: {"entailed": ENTAILED}},
            JUDGES[1]: {STATED: {"stated": STATED}, ENTAILED: {"entailed": ENTAILED}},
        },
        FLAGGED,
        (None, None),
    ),
    (
        "MALFORMED: an answer outside the vocabulary",
        {
            JUDGES[0]: {STATED: {"stated": "yes"}, ENTAILED: {"entailed": ENTAILED}},
            JUDGES[1]: {STATED: {"stated": STATED}, ENTAILED: {"entailed": ENTAILED}},
        },
        FLAGGED,
        (None, None),
    ),
    (
        "MALFORMED: a list where an object belongs",
        {
            JUDGES[0]: {STATED: [STATED], ENTAILED: {"entailed": ENTAILED}},
            JUDGES[1]: {STATED: {"stated": STATED}, ENTAILED: {"entailed": ENTAILED}},
        },
        FLAGGED,
        (None, None),
    ),
    (
        "MALFORMED: the key is missing",
        {
            JUDGES[0]: {STATED: {"why": "it says so"}, ENTAILED: {"entailed": ENTAILED}},
            JUDGES[1]: {STATED: {"stated": STATED}, ENTAILED: {"entailed": ENTAILED}},
        },
        FLAGGED,
        (None, None),
    ),
]


@pytest.mark.parametrize(
    "name,replies,expected,answers", VERDICT_TABLE, ids=[row[0] for row in VERDICT_TABLE]
)
def test_verdict_table(name, replies, expected, answers):
    verdict = judge_fact(FakeLLM(replies), FACT, ANSWER, QUOTES, JUDGES)
    assert verdict.verdict == expected, f"{name}: {verdict.reason}"
    assert (verdict.stated, verdict.entailed) == answers


def test_empty_citations_are_not_entailed_without_asking():
    """NO CITATION: an uncited claim fails even when the note states it well.

    No entailment call is made, so a judge cannot be talked into entailing
    nothing, and the run does not pay for the question.
    """
    llm = FakeLLM(both(STATED, ENTAILED))
    verdict = judge_fact(llm, FACT, ANSWER, [], JUDGES)
    assert verdict.verdict == FAIL
    assert verdict.entailed == NOT_ENTAILED
    assert [q for _, q in llm.prompts] == [STATED, STATED]
    assert verdict.quotes_used == 0


def test_blank_quotes_count_as_no_citation():
    verdict = judge_fact(FakeLLM(both(STATED, ENTAILED)), FACT, ANSWER, ["", "   "], JUDGES)
    assert verdict.entailed == NOT_ENTAILED


def test_each_judge_answers_two_separate_questions():
    """The two questions are two calls, so the entailment ruling is not
    anchored by the judge's own 'the note states it' answer."""
    llm = FakeLLM(both(STATED, ENTAILED))
    judge_fact(llm, FACT, ANSWER, QUOTES, JUDGES)
    assert llm.prompts == [
        (JUDGES[0], STATED),
        (JUDGES[0], ENTAILED),
        (JUDGES[1], STATED),
        (JUDGES[1], ENTAILED),
    ]


@pytest.mark.parametrize(
    "written,expected",
    [("Stated", STATED), ("NOT ENTAILED", NOT_ENTAILED), ("not_entailed", NOT_ENTAILED),
     (" entailed ", ENTAILED)],
)
def test_answer_normalisation(written, expected):
    """Case, spaces and underscores are the same answer; anything else is not."""
    key = STATED if expected in (STATED,) else ENTAILED
    replies = both(STATED, ENTAILED)
    for model in JUDGES:
        replies[model][key] = {key: written}
    verdict = judge_fact(FakeLLM(replies), FACT, ANSWER, QUOTES, JUDGES)
    assert getattr(verdict, key) == expected


def test_a_long_answer_is_truncated_and_says_so(monkeypatch):
    monkeypatch.setattr(judge_module, "MAX_ANSWER_CHARS", 50)
    verdict = judge_fact(FakeLLM(both(STATED, ENTAILED)), FACT, "x" * 500, QUOTES, JUDGES)
    assert verdict.answer_truncated is True


# ---------------------------------------------------------------------------
# Aggregation: a flagged item is never a pass
# ---------------------------------------------------------------------------


def test_judge_facts_counts_flags_apart_from_failures():
    replies = {
        JUDGES[0]: {STATED: {"stated": STATED}, ENTAILED: {"entailed": ENTAILED}},
        JUDGES[1]: {STATED: {"stated": ABSENT}, ENTAILED: {"entailed": ENTAILED}},
    }
    result = judge_facts(FakeLLM(replies), ["fact a", "fact b"], ANSWER, QUOTES, JUDGES)
    assert result["total"] == 2
    assert result["passed"] == 0
    assert result["flagged"] == 2
    assert (result["flagged_split"], result["flagged_unreadable"]) == (2, 0)
    assert result["failed"] == 0
    assert result["fact_accuracy"] == "0/2"
    assert result["accuracy_fraction"] == 0.0


def test_an_unreachable_judge_is_counted_apart_from_a_split():
    """A split needs a human; an unreachable judge needs the run repeating.
    One count for both hides which, and a network fault reads as a finding."""
    replies = {
        JUDGES[0]: {STATED: RuntimeError("chat() failed"), ENTAILED: {"entailed": ENTAILED}},
        JUDGES[1]: {STATED: {"stated": STATED}, ENTAILED: {"entailed": ENTAILED}},
    }
    result = judge_facts(FakeLLM(replies), ["fact a"], ANSWER, QUOTES, JUDGES)
    assert (result["flagged_split"], result["flagged_unreadable"]) == (0, 1)


def test_a_wording_split_records_the_split_it_did_not_flag():
    replies = {
        JUDGES[0]: {STATED: {"stated": PARTIAL}, ENTAILED: {"entailed": ENTAILED}},
        JUDGES[1]: {STATED: {"stated": ABSENT}, ENTAILED: {"entailed": ENTAILED}},
    }
    verdict = judge_fact(FakeLLM(replies), FACT, ANSWER, QUOTES, JUDGES)
    assert "judges split" in verdict.reason
    assert ABSENT in verdict.reason


def test_judge_facts_splits_ungrounded_from_unstated():
    llm = FakeLLM(both(STATED, NOT_ENTAILED))
    result = judge_facts(llm, ["fact a"], ANSWER, QUOTES, JUDGES)
    assert (result["stated_not_entailed"], result["not_stated"]) == (1, 0)
    result = judge_facts(FakeLLM(both(ABSENT, ENTAILED)), ["fact a"], ANSWER, QUOTES, JUDGES)
    assert (result["stated_not_entailed"], result["not_stated"]) == (0, 1)


def test_judge_facts_with_no_facts_is_not_a_perfect_score():
    result = judge_facts(FakeLLM(both(STATED, ENTAILED)), [], ANSWER, QUOTES, JUDGES)
    assert result["accuracy_fraction"] is None
    assert result["fact_accuracy"] == "n/a (no facts)"


# ---------------------------------------------------------------------------
# Artifact adapters
# ---------------------------------------------------------------------------


REPORT_MD = """# CBA — nim — FY26 vs FY25

Asset pricing cost 5 bps.

### asset_pricing
> [ev-18] CBA/FY26/profit_announcement, PDF p29: "Asset pricing: down 5 basis points."

## Provenance
- combo: cheap
"""


def test_answer_prose_drops_quotes_and_provenance():
    """A note that pastes a supporting quote has not itself stated the fact."""
    prose = answer_prose(REPORT_MD)
    assert "Asset pricing cost 5 bps." in prose
    assert "ev-18" not in prose
    assert "combo: cheap" not in prose


def test_cited_quotes_ignores_uncited_records():
    attribution = {
        "drivers": [{"canonical": "asset_pricing", "evidence": ["ev-1"]}],
        "evidence_records": [
            {"id": "ev-1", "quote": "cited quote"},
            {"id": "ev-2", "quote": "never cited"},
        ],
    }
    assert cited_quotes(attribution) == ["cited quote"]


# ---------------------------------------------------------------------------
# Crossref: coverage is not correctness (finding 7)
# ---------------------------------------------------------------------------


CROSSREF_GOLD = {
    "id": "mortgage-offset-footnote",
    "gold_answer_facts": ["Offset balances were $X at Jun 26"],
    "required_locations": [{"doc": "CBA/FY26/profit_announcement", "pdf_page": 29, "holds": "the footnote"}],
}
ASK_OUTPUT = {
    "answer": "Offset balances rose.",
    "key_facts": [{"fact": "Offset balances rose", "evidence": ["ev-1"]}],
    "evidence_records": [
        {"id": "ev-1", "doc_id": "CBA/FY26/profit_announcement", "pdf_page": 29, "quote": "Offset balances."}
    ],
    "confidence": 90,
    "limitations": [],
    "provenance": {},
}


def test_full_coverage_does_not_pass_a_case_the_judges_fail():
    """WRONG-SCORES-RIGHT: the old scorer called this 1/1 and moved on."""
    row = score_crossref(CROSSREF_GOLD, ASK_OUTPUT, FakeLLM(both(ABSENT, NOT_ENTAILED)), JUDGES)
    assert row["location_coverage"] == "1/1"
    assert row["fact_accuracy"] == "0/1"
    assert row["passes"] is False


def test_full_coverage_and_judged_facts_pass_together():
    row = score_crossref(CROSSREF_GOLD, ASK_OUTPUT, FakeLLM(both(STATED, ENTAILED)), JUDGES)
    assert row["passes"] is True


def test_an_unjudged_case_is_not_a_pass():
    row = score_crossref(CROSSREF_GOLD, ASK_OUTPUT)
    assert row["fact_check"]["status"].startswith("not_run")
    assert row["passes"] is None


@pytest.mark.parametrize(
    "coverage,accuracy,expected",
    [(1.0, 1.0, True), (1.0, 0.75, True), (1.0, 0.5, False), (0.5, 1.0, False),
     (None, 1.0, None), (1.0, None, None)],
)
def test_crossref_pass_needs_both(coverage, accuracy, expected):
    assert crossref_passes(coverage, accuracy) is expected
