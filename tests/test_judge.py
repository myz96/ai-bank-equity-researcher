"""Citation-grounding judge tests (tickets 02, 05, 29).

The verdict table is the specification. Every row names the mistake it stops:

- AGREEMENT PASS: both judges say the note states the fact and the quotes
  entail it, so the fact counts.
- AGREEMENT FAIL: the judges agree the grounding is missing. A cited page is
  not a supported claim: coverage is not correctness.
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

from bank_equity_researcher.evals.harness import crossref_passes, score_crossref
from bank_equity_researcher.judging import judge as judge_module
from bank_equity_researcher.judging.judge import (
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
        # The only NON-OBJECT reply in the table. `_ask` reads the answer out
        # of the reply and reads "why" only when the reply is a dict, so a list
        # is the shape that reaches both guards at once.
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
    """A record whose quote is empty is still a citation in the list.

    The quote block is filtered before the entailment question is asked, so
    blank strings must leave the list empty and take the same path as no
    citation at all — a judge asked to entail whitespace will oblige.
    """
    verdict = judge_fact(FakeLLM(both(STATED, ENTAILED)), FACT, ANSWER, ["", "   "], JUDGES)
    assert verdict.entailed == NOT_ENTAILED
    assert verdict.quotes_used == 0


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
    # Three writings, three of the normaliser's own steps: case, the
    # underscore, and the surrounding space that a model adds to a bare word.
    [("Stated", STATED), ("not_entailed", NOT_ENTAILED), (" NOT ENTAILED ", NOT_ENTAILED)],
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


# ---------------------------------------------------------------------------
# Headline citations (ticket 27)
#
# A headline states facts that belong to no single driver: the movement as a
# second document states it, the statutory-versus-cash framing, the summary
# measures the bank leads with. While only DRIVER evidence lists were read
# here, such a fact was judged "stated" and "not entailed" however well the
# answer had sourced it, because the entailment path did not exist for it. The
# rule that a record the answer never cited is not the answer's grounding is
# unchanged.
# ---------------------------------------------------------------------------


HEADLINE_ATTRIBUTION = {
    "drivers": [{"canonical": "asset_pricing", "evidence": ["ev-1"]}],
    "headline_evidence": ["ev-3"],
    "evidence_records": [
        {"id": "ev-1", "quote": "driver quote"},
        {"id": "ev-2", "quote": "never cited"},
        {"id": "ev-3", "quote": "headline quote"},
    ],
}


def test_cited_quotes_includes_headline_citations():
    assert cited_quotes(HEADLINE_ATTRIBUTION) == ["driver quote", "headline quote"]


def test_cited_quotes_still_excludes_records_neither_list_cites():
    assert "never cited" not in cited_quotes(HEADLINE_ATTRIBUTION)


def _many(driver_count: int, headline_count: int) -> dict:
    records = [{"id": f"d-{i}", "quote": f"driver {i}"} for i in range(driver_count)]
    records += [{"id": f"h-{i}", "quote": f"headline {i}"} for i in range(headline_count)]
    return {
        "drivers": [{"canonical": "x", "evidence": [f"d-{i}" for i in range(driver_count)]}],
        "headline_evidence": [f"h-{i}" for i in range(headline_count)],
        "evidence_records": records,
    }


def test_cited_quotes_never_starves_the_headline_when_the_cap_binds():
    """The cap is unchanged; what changes is which citations it drops.

    The CBA FY26 cash-earnings answer cited 21 records from its drivers and 5
    more from its headline. Under a flat "drivers first, headline after" order
    the two quotes carrying the headline's own figures fell off the end of the
    window — the new citations were the first thing the cap threw away.
    """
    quotes = cited_quotes(_many(21, 5))
    assert len(quotes) == judge_module.MAX_QUOTES
    assert quotes[-5:] == [f"headline {i}" for i in range(5)]


def test_cited_quotes_splits_the_window_when_both_lists_are_long():
    quotes = cited_quotes(_many(30, 30))
    assert len(quotes) == judge_module.MAX_QUOTES
    assert sum(1 for q in quotes if q.startswith("headline")) == judge_module.MAX_QUOTES // 2


def test_cited_quotes_gives_the_drivers_the_whole_window_when_alone():
    """An answer with no headline citations reads exactly as it did before."""
    quotes = cited_quotes(_many(30, 0))
    assert quotes == [f"driver {i}" for i in range(judge_module.MAX_QUOTES)]


def test_cited_quotes_lists_a_shared_record_once():
    attribution = {
        "drivers": [{"canonical": "asset_pricing", "evidence": ["ev-1"]}],
        "headline_evidence": ["ev-1"],
        "evidence_records": [{"id": "ev-1", "quote": "shared quote"}],
    }
    assert cited_quotes(attribution) == ["shared quote"]


def test_cited_quotes_reads_an_attribution_with_no_headline_list():
    """Every artifact saved before the field existed still judges."""
    attribution = {
        "drivers": [{"canonical": "asset_pricing", "evidence": ["ev-1"]}],
        "evidence_records": [{"id": "ev-1", "quote": "driver quote"}],
    }
    assert cited_quotes(attribution) == ["driver quote"]


def test_headline_evidence_survives_the_report_round_trip():
    """The report must print the headline's citations as BLOCK QUOTES: the
    judge's "does the note state it" question reads answer_prose, and a pasted
    quote there would answer its own question."""
    from bank_equity_researcher.render import render_report
    from bank_equity_researcher.validation.schema import Attribution, EvidenceRecord

    attribution = Attribution(
        bank="BANK",
        metric="cash_earnings",
        period="FY26",
        comparator="FY25",
        basis="cash",
        headline="Operating performance rose 6.5 per cent.",
        headline_evidence=["ev-1"],
        evidence_records=[
            EvidenceRecord(
                id="ev-1",
                doc_id="BANK/FY26/results_presentation",
                pdf_page=24,
                quote="Operating performance 16,469 up 6.5%",
            )
        ],
    )
    report = render_report(attribution)
    assert '> [ev-1] BANK/FY26/results_presentation' in report
    prose = answer_prose(report)
    assert "Operating performance rose 6.5 per cent." in prose
    assert "16,469" not in prose


def test_headline_evidence_drops_an_id_that_resolves_to_no_record():
    """The never-guess gate is structural: an id citing nothing cites nothing."""
    from bank_equity_researcher.validation.schema import (
        Attribution,
        EvidenceRecord,
        enforce_evidence_gate,
    )

    attribution = enforce_evidence_gate(
        Attribution(
            bank="BANK",
            metric="roe",
            period="FY26",
            comparator="FY25",
            basis="cash",
            headline_evidence=["ev-1", "ev-404", "ev-1"],
            evidence_records=[
                EvidenceRecord(id="ev-1", doc_id="BANK/FY26/x", pdf_page=1, quote="q")
            ],
        )
    )
    assert attribution.headline_evidence == ["ev-1"]


# ---------------------------------------------------------------------------
# Crossref: coverage is not correctness
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


def _fact_check(total: int, passed: int, flagged: int = 0) -> dict:
    return {
        "total": total,
        "passed": passed,
        "failed": total - passed - flagged,
        "flagged": flagged,
        "accuracy_fraction": round(passed / total, 3) if total else None,
    }


@pytest.mark.parametrize(
    "name,coverage,fact_check,expected",
    [
        # The 0.75 allowance exists for ONE FLAGGED fact in a four-fact case.
        ("one flagged of four", 1.0, _fact_check(4, 3, flagged=1), True),
        ("two flagged of four", 1.0, _fact_check(4, 2, flagged=2), False),
        # ...and never for an outright failure. A judged, unanimous FAIL is the
        # answer getting the fact WRONG, which no allowance covers. The old
        # rule read one blended number, so it could not tell these two apart.
        ("one unanimous fail of four", 1.0, _fact_check(4, 3), False),
        ("coverage short", 0.5, _fact_check(4, 4), False),
        ("no coverage figure", None, _fact_check(4, 4), None),
        ("no facts judged", 1.0, {"total": 0, "accuracy_fraction": None}, None),
    ],
    ids=lambda v: v if isinstance(v, str) else "",
)
def test_crossref_pass_needs_both(name, coverage, fact_check, expected):
    assert crossref_passes(coverage, fact_check) is expected


# ---------------------------------------------------------------------------
# Researcher questions: the same scorer, over documents named as a person
# writes them
# ---------------------------------------------------------------------------

QUESTION_GOLD = {
    "id": "nab-business-growth-quality",
    "gold_answer_facts": ["Business lending grew 6.7%"],
    "required_locations": [
        {"doc": "NAB/FY25/investor-presentation", "pdf_page": 49, "holds": "the growth chart"},
        {"doc": "WBC/FY25/presentation-and-IDP", "pdf_page": 27, "holds": "the expense bridge"},
    ],
}
QUESTION_OUTPUT = {
    "answer": "Business lending grew 6.7%.",
    "key_facts": [{"fact": "Business lending grew 6.7%", "evidence": ["ev-1"]}],
    "evidence_records": [
        {"id": "ev-1", "doc_id": "NAB/FY25/investor_presentation", "pdf_page": 49,
         "quote": "Business lending 155.0 166.3 6.7%"},
        {"id": "ev-2", "doc_id": "WBC/FY25/investor_discussion_pack", "pdf_page": 27,
         "quote": "Staff costs 397"},
    ],
    "confidence": 80,
    "limitations": [],
    "provenance": {"cost_usd": 0.4, "seconds": 60},
}
DOC_INDEX = {
    "nab-fy25-investor-presentation": "NAB/FY25/investor_presentation",
    "nab-fy25-investor_presentation": "NAB/FY25/investor_presentation",
    "wbc-fy25-presentation-and-idp": "WBC/FY25/investor_discussion_pack",
    "wbc-fy25-investor-discussion-pack": "WBC/FY25/investor_discussion_pack",
}


def test_coverage_maps_a_written_document_name_onto_the_corpus():
    """The gold names the file; the corpus names the doc_type. One document."""
    row = score_crossref(QUESTION_GOLD, QUESTION_OUTPUT, doc_index=DOC_INDEX)
    hit = next(loc for loc in row["locations"] if loc["pdf_page"] == 49)
    assert hit["hit"] is True and hit["cited_by"] == ["ev-1"]
    # ev-2 is on a required page but no key fact cites it, so it is not
    # coverage: an uncited record is not part of the answer.
    missed = next(loc for loc in row["locations"] if loc["pdf_page"] == 27)
    assert missed["hit"] is False
    assert row["location_coverage"] == "1/2"
    assert row["coverage_fraction"] == 0.5


def test_coverage_without_the_index_still_matches_on_the_name():
    """The crossref gold writes doc_ids, so the old substring path must hold."""
    gold = {
        "id": "x",
        "gold_answer_facts": [],
        "required_locations": [
            {"doc": "NAB/FY25/investor_presentation", "pdf_page": 49, "holds": ""}
        ],
    }
    assert score_crossref(gold, QUESTION_OUTPUT)["location_coverage"] == "1/1"


def test_the_question_gold_loads_as_its_own_suite():
    from bank_equity_researcher.evals.harness import (
        load_crossref_gold,
        load_question_gold,
    )

    questions = load_question_gold("dev")
    assert questions, "the dev researcher-question set must load"
    ids = {case["id"] for case in questions}
    assert {case["id"] for case in load_crossref_gold()}.isdisjoint(ids)
    for case in questions:
        assert case["question"] and case["required_locations"] and case["gold_answer_facts"]
        assert "movement" not in case
    # The bank filter reads the banks a question names, since a case may span
    # three of them.
    assert {c["id"] for c in load_question_gold("dev", "NAB")} <= ids


def test_judge_fact_max_quotes_widens_the_window():
    """The questions suite widens the evidence window; the default stays
    frozen. A wider window must reach the quotes the default drops."""
    from bank_equity_researcher.judging import judge as J

    class FakeLLM:
        def __init__(self):
            self.prompts = []

        def chat_json(self, model, prompt, max_tokens=None):
            self.prompts.append(prompt)
            if "does the NOTE state" in prompt or '"stated"' in prompt:
                return {"stated": "stated", "why": ""}
            return {"entailed": "entailed", "why": ""}

    quotes = [f"quote number {i}" for i in range(40)]
    default = J.judge_fact(FakeLLM(), "a fact", "the note", quotes, ("j1", "j2"))
    assert default.quotes_used == 24
    widened = J.judge_fact(FakeLLM(), "a fact", "the note", quotes, ("j1", "j2"), max_quotes=48)
    assert widened.quotes_used == 40
    # The window dropped quotes; the CHARACTER budget did not. The two counts
    # are reported side by side on the scorecard, so the flag must stay off
    # when nothing was cut for length.
    assert default.quotes_truncated is False
    assert widened.quotes_truncated is False
    llm = FakeLLM()
    J.judge_fact(llm, "a fact", "the note", quotes, ("j1", "j2"), max_quotes=48)
    assert any("quote number 39" in p for p in llm.prompts)


def test_quotes_dropped_by_the_character_budget_are_reported():
    """quotes_used must count what the judge SAW, not what it was offered.

    The count came from the pre-truncation list while a separate character
    budget silently cut the block, so a scorecard could report 48 quotes
    behind a verdict the judge reached on 12. An entailment ruling made on
    quotes the judge never read is the failure this number exists to expose.
    """
    from bank_equity_researcher.judging import judge as J

    class FakeLLM:
        def __init__(self):
            self.prompts = []

        def chat_json(self, model, prompt, max_tokens=None):
            self.prompts.append(prompt)
            if '"stated"' in prompt or "does the NOTE state" in prompt:
                return {"stated": "stated", "why": ""}
            return {"entailed": "entailed", "why": ""}

    # Twenty quotes of 500 characters overrun the 4000-character budget.
    quotes = [f"q{i} " + "x" * 500 for i in range(20)]
    llm = FakeLLM()
    verdict = J.judge_fact(llm, "a fact", "the note", quotes, ("j1", "j2"))
    assert verdict.quotes_truncated is True
    assert 0 < verdict.quotes_used < 20
    entailment = next(p for p in llm.prompts if "q0" in p)
    # Every quote the count claims is whole and present; none beyond it is.
    for i in range(verdict.quotes_used):
        assert f"q{i} " in entailment
    assert f"q{verdict.quotes_used} " not in entailment


def test_quotes_inside_the_budget_are_not_flagged():
    """The negative control for quote truncation: a small set is never marked
    truncated, and the count is the set's own size."""
    from bank_equity_researcher.judging import judge as J

    class FakeLLM:
        def chat_json(self, model, prompt, max_tokens=None):
            if '"stated"' in prompt or "does the NOTE state" in prompt:
                return {"stated": "stated", "why": ""}
            return {"entailed": "entailed", "why": ""}

    verdict = J.judge_fact(FakeLLM(), "a fact", "the note", ["short one", "short two"], ("j1",))
    assert verdict.quotes_truncated is False
    assert verdict.quotes_used == 2

