"""The closed-loop research agent (ADR-0005).

Every test here is offline: the documents are synthetic, the model is a
stand-in that replays a scripted transcript, and no PDF is opened. What the
tests pin down is the part that must not drift — the tool adapters, the
verbatim-citation gate, and the submit path that turns one submission into the
same artifact the pipeline emits.
"""

from __future__ import annotations

import json
from dataclasses import dataclass

import pytest

from bank_equity_researcher import research_agent as RA
from bank_equity_researcher.schema import Attribution, EvidenceRecord
from bank_equity_researcher.taxonomy import TAXONOMY

CALENDAR = {"fy_end": "30 June", "halves": {"1H": "ends 31 December", "2H": "ends 30 June"}}
REGISTRY = {
    "calendar": CALENDAR,
    "measures": {"core_profit": "cash NPAT (net profit after tax, cash basis)"},
    "nim_walk_labels": {"Deposits": "funding.deposits"},
}

KPI_PAGE = (
    "Group Performance Summary\n"
    "                       FY26     FY25\n"
    "Net interest margin    2.05%    2.08%\n"
    "Refer to Note 2.2 for further information.\n"
    "                                                       5"
)
NOTE_PAGE = (
    "2.2 Provisions for Impairment and Asset Quality\n"
    "Loan impairment expense    1,050    900\n"
    "The increase reflects higher collective provisioning.\n"
    "                                                       6"
)
CHART_PAGE = "Net interest margin movement\nJun 25 Full Year\nJun 26 Full Year\n7"


class _Doc:
    """The members of a corpus Document the agent's tools use."""

    def __init__(self, doc_id: str, pages: list[str], doc_type: str = "profit_announcement",
                 period: str = "FY26") -> None:
        self.doc_id = doc_id
        self.doc_type = doc_type
        self.period = period
        self.bank = doc_id.split("/")[0]
        self.sha256 = "0" * 64
        self.path = f"/nowhere/{doc_id.replace('/', '-')}.pdf"
        self._pages = pages

    def page_texts(self) -> list[str]:
        return list(self._pages)

    def render_page(self, page_no, zoom=2.0):
        return b"png"


@dataclass
class _Combo:
    name: str = "agentic"
    vision: str = "vision-model"
    agent: str = "agent-model"
    agent_max_tokens: int = 4000
    max_tool_calls: int = 6
    cost_ceiling_usd: float = 1.0
    wall_clock_s: float = 600.0
    orchestration: str = "agent"


class _Usage:
    def __init__(self) -> None:
        self.cost_usd = 0.0
        self.prompt_tokens = 0
        self.completion_tokens = 0


class _LLM:
    """Replays a scripted list of assistant messages."""

    def __init__(self, script: list[dict], walk_reply: dict | None = None) -> None:
        self.script = list(script)
        self.walk_reply = walk_reply
        self.usage = _Usage()
        self.turns: list[list[dict]] = []

    def chat_tools(self, model, messages, tools, max_tokens=None):
        self.turns.append([t["function"]["name"] for t in tools])
        if not self.script:
            return {"role": "assistant", "content": "I have no more moves."}
        return self.script.pop(0)

    def chat_json(self, model, prompt, image_png=None, max_tokens=None):
        if self.walk_reply is None:
            raise RuntimeError("no chart on this page")
        return self.walk_reply


def _tool_call(call_id: str, name: str, arguments: dict) -> dict:
    return {
        "id": call_id,
        "type": "function",
        "function": {"name": name, "arguments": json.dumps(arguments)},
    }


def _assistant(*calls: dict) -> dict:
    return {"role": "assistant", "content": "", "tool_calls": list(calls)}


@pytest.fixture
def docs() -> list[_Doc]:
    return [
        _Doc("CBA/FY26/profit_announcement", ["cover", *([""] * 10), KPI_PAGE, NOTE_PAGE, CHART_PAGE]),
        _Doc("CBA/FY25/results_presentation", ["cover", KPI_PAGE], "results_presentation", "FY25"),
    ]


@pytest.fixture
def case() -> dict:
    return {
        "bank": "CBA",
        "metric": "nim",
        "period": "FY26",
        "comparator": "FY25",
        "description": "CBA net interest margin in FY26 vs FY25",
    }


def _research(llm, docs, case, metric="nim") -> RA.Research:
    return RA.Research(llm, _Combo(), docs, case, TAXONOMY[metric], REGISTRY)


# ---------------------------------------------------------------------------
# The verbatim gate
# ---------------------------------------------------------------------------


def test_quote_key_ignores_layout_but_not_words():
    """A PDF text layer breaks a row wherever the column gaps fall."""
    assert RA.quote_key("Net interest margin  2.05%") == RA.quote_key(
        "Net interest\nmargin\n2.05%"
    )
    # An era page splits a number across a space; dropping whitespace pairs it
    # with the number a reader sees.
    assert RA.quote_key("47.0") == RA.quote_key("47. 0")
    # Different words are still different.
    assert RA.quote_key("margin fell") != RA.quote_key("margin rose")


def test_quote_key_unifies_typographic_marks():
    assert RA.quote_key("the bank’s margin – down") == RA.quote_key("the bank's margin - down")


def test_build_records_accepts_a_verbatim_quote(docs, case):
    research = _research(_LLM([]), docs, case)
    records, rejections, id_map = research.build_records(
        [
            {
                "id": "e1",
                "doc_id": "CBA/FY26/profit_announcement",
                "pdf_page": 12,
                "quote": "Net interest margin    2.05%    2.08%",
                "numbers": [{"label": "NIM FY26", "value": 2.05, "unit": "%"}],
            }
        ]
    )
    assert rejections == []
    assert len(records) == 1
    assert records[0].doc_id == "CBA/FY26/profit_announcement"
    assert records[0].pdf_page == 12
    assert records[0].numbers[0].value == 2.05
    assert id_map["e1"] == records[0].id


def test_build_records_rejects_a_paraphrase(docs, case):
    """A quote that is not on the page it names never reaches the artifact."""
    research = _research(_LLM([]), docs, case)
    records, rejections, _ = research.build_records(
        [
            {
                "id": "e1",
                "doc_id": "CBA/FY26/profit_announcement",
                "pdf_page": 12,
                "quote": "The margin declined by three basis points over the year.",
            }
        ]
    )
    assert records == []
    assert len(rejections) == 1
    assert "not on CBA/FY26/profit_announcement p12" in rejections[0]


def test_build_records_rejects_a_quote_from_another_page(docs, case):
    research = _research(_LLM([]), docs, case)
    records, rejections, _ = research.build_records(
        [
            {
                "id": "e1",
                "doc_id": "CBA/FY26/profit_announcement",
                "pdf_page": 13,
                "quote": "Net interest margin    2.05%    2.08%",
            }
        ]
    )
    assert records == []
    assert rejections and "p13" in rejections[0]


def test_build_records_rejects_an_unknown_page(docs, case):
    research = _research(_LLM([]), docs, case)
    records, rejections, _ = research.build_records(
        [{"id": "e1", "doc_id": "CBA/FY26/profit_announcement", "pdf_page": 99, "quote": "x"}]
    )
    assert records == []
    assert "does not exist" in rejections[0]


def test_build_records_keeps_a_record_a_tool_minted(docs, case):
    """A chart read keeps the numbers the vision pass extracted."""
    research = _research(_LLM([]), docs, case)
    minted = EvidenceRecord(
        id="ev-1", doc_id="CBA/FY26/profit_announcement", pdf_page=14, kind="walk_vision",
        quote="[walk chart] NIM movement",
    )
    research.records.append(minted)
    records, rejections, id_map = research.build_records([{"id": "ev-1"}])
    assert rejections == []
    assert records == [minted]
    assert id_map["ev-1"] == "ev-1"


def test_build_records_rejects_an_id_no_tool_minted(docs, case):
    research = _research(_LLM([]), docs, case)
    _records, rejections, _ = research.build_records([{"id": "ev-9"}])
    assert "no quote" in rejections[0]


# ---------------------------------------------------------------------------
# The tool adapters
# ---------------------------------------------------------------------------


def test_search_pages_ranks_and_snippets(docs, case, monkeypatch):
    monkeypatch.setattr(
        RA, "retrieve",
        lambda doc, query, top_k=6: [(12, 1.5), (13, 0.5)] if len(doc.page_texts()) > 13 else [],
    )
    research = _research(_LLM([]), docs, case)
    out = research.search_pages("net interest margin")
    assert out["results"][0]["doc_id"] in {d.doc_id for d in docs}
    assert out["results"][0]["pdf_page"] == 12
    assert "margin" in out["results"][0]["snippet"].lower()
    assert len(out["results"]) <= RA.MAX_SEARCH_HITS


def test_search_pages_can_restrict_to_one_document(docs, case, monkeypatch):
    monkeypatch.setattr(RA, "retrieve", lambda doc, query, top_k=6: [(2, 1.0)])
    research = _research(_LLM([]), docs, case)
    out = research.search_pages("margin", doc_id="CBA/FY25/results_presentation")
    assert {r["doc_id"] for r in out["results"]} == {"CBA/FY25/results_presentation"}


def test_read_page_returns_the_text_and_the_printed_number(docs, case):
    research = _research(_LLM([]), docs, case)
    out = research.read_page("CBA/FY26/profit_announcement", 12)
    assert "Net interest margin" in out["text"]
    assert out["printed_page"] == 5
    assert out["truncated"] is False
    assert ("CBA/FY26/profit_announcement", 12) in research.pages_read


def test_read_page_caps_a_long_page(docs, case):
    long_doc = _Doc("CBA/FY26/results_book", ["x" * (RA.MAX_PAGE_CHARS + 500)])
    research = _research(_LLM([]), [long_doc], case)
    out = research.read_page("CBA/FY26/results_book", 1)
    assert len(out["text"]) == RA.MAX_PAGE_CHARS
    assert out["truncated"] is True


def test_read_chart_mints_a_record_and_classifies_the_comparison(docs, case):
    llm = _LLM(
        [],
        walk_reply={
            "title": "NIM movement",
            "start_label": "Jun 25 Full Year", "start_bps": 208,
            "bars": [{"label": "Deposits", "bps": -3}],
            "end_label": "Jun 26 Full Year", "end_bps": 205,
        },
    )
    research = _research(llm, docs, case)
    out = research.read_chart("CBA/FY26/profit_announcement", 14)
    assert out["evidence_id"] == "ev-1"
    assert out["walk"]["comparison"] == "primary"
    assert "walk_sum" in out["walk"]["checks_passed"]
    assert research.walks[0]["record_id"] == "ev-1"
    assert research.records[0].kind == "walk_vision"


def test_read_chart_marks_another_comparison_as_context(docs, case):
    llm = _LLM(
        [],
        walk_reply={
            "title": "NIM movement",
            "start_label": "Dec 25 Half", "start_bps": 206,
            "bars": [{"label": "Deposits", "bps": -1}],
            "end_label": "Jun 26 Half", "end_bps": 205,
        },
    )
    research = _research(llm, docs, case)
    out = research.read_chart("CBA/FY26/profit_announcement", 14)
    assert out["walk"]["comparison"] == "context"


def test_read_chart_reports_a_failure_without_crashing(docs, case):
    research = _research(_LLM([]), docs, case)  # walk_reply is None, so the read raises
    out = research.read_chart("CBA/FY26/profit_announcement", 14)
    assert "could not be read" in out["error"]
    assert research.walks == []
    assert any(f.startswith("walk_extraction_error") for f in research.validation["failed"])


def test_cite_mints_records_for_verbatim_quotes(docs, case):
    research = _research(_LLM([]), docs, case)
    out = research.cite(
        "CBA/FY26/profit_announcement",
        12,
        [
            {
                "quote": "Net interest margin    2.05%    2.08%",
                "kind": "table",
                "numbers": [{"label": "NIM FY26", "value": 2.05, "unit": "%"}],
            },
            {"quote": "Group Performance Summary"},
        ],
    )
    assert [c["id"] for c in out["cited"]] == ["ev-1", "ev-2"]
    assert "rejected" not in out
    assert research.records[0].kind == "table"
    assert research.records[0].numbers[0].value == 2.05


def test_a_cited_quote_is_stored_on_one_line(docs, case):
    """The report marks a quote with ">" on its first line only, and every
    reader that separates prose from quotes reads that prefix."""
    table = _Doc("CBA/FY26/results_book", ["Total loan impairment expense \n788 \n726  \n469"])
    research = _research(_LLM([]), [table], case)
    out = research.cite("CBA/FY26/results_book", 1,
                        [{"quote": "Total loan impairment expense \n788 \n726"}])
    assert out["cited"][0]["quote"] == "Total loan impairment expense 788 726"
    assert "\n" not in research.records[0].quote


def test_cite_rejects_what_the_page_does_not_say_and_keeps_the_rest(docs, case):
    research = _research(_LLM([]), docs, case)
    out = research.cite(
        "CBA/FY26/profit_announcement",
        12,
        [
            {"quote": "Net interest margin    2.05%    2.08%"},
            {"quote": "the margin fell three basis points"},
        ],
    )
    assert len(out["cited"]) == 1
    assert len(out["rejected"]) == 1
    assert "not on" in out["rejected"][0]["reason"]
    assert len(research.records) == 1


def test_a_cited_record_is_referenced_by_id_alone_at_submit(docs, case):
    research = _research(_LLM([]), docs, case)
    research.cite("CBA/FY26/profit_announcement", 12,
                  [{"quote": "Net interest margin    2.05%    2.08%"}])
    records, rejections, id_map = research.build_records([{"id": "ev-1"}])
    assert rejections == []
    assert [r.id for r in records] == ["ev-1"]
    assert id_map == {"ev-1": "ev-1"}


def test_follow_references_resolves_a_note_pointer(docs, case, monkeypatch):
    from bank_equity_researcher import refs

    refs._notes_cache.clear()
    refs._printed_cache.clear()
    contents = "\n".join(
        ["Contents", "1.1 ", "Net Interest Income", "5",
         "2.2 ", "Provisions for Impairment and Asset Quality", "7",
         "6.2 ", "ASX Appendix 4E", "9"]
    )
    doc = _Doc("CBA/FY26/profit_announcement", [contents, *([""] * 10), KPI_PAGE, NOTE_PAGE])
    research = _research(_LLM([]), [doc], case, metric="impairment")
    out = research.follow_references("CBA/FY26/profit_announcement", 12)
    targets = [r["target"] for r in out["references"]]
    assert any("2.2" in t for t in targets)
    assert 13 in [p for r in out["references"] for p in r["pdf_pages"]]
    refs._notes_cache.clear()
    refs._printed_cache.clear()


def test_bank_language_returns_labels_and_no_figures(docs, case):
    research = _research(_LLM([]), docs, case)
    out = research.bank_language("CBA")
    assert out["measures"]["core_profit"].startswith("cash NPAT")
    assert out["nim_walk_labels"] == {"Deposits": "funding.deposits"}
    assert "\"value\"" not in json.dumps(out)


def test_dispatch_reports_an_unknown_tool_instead_of_raising(docs, case):
    research = _research(_LLM([]), docs, case)
    assert "no tool named" in research.dispatch("read_the_room", {})["error"]


def test_dispatch_reports_bad_arguments_instead_of_raising(docs, case):
    research = _research(_LLM([]), docs, case)
    assert "error" in research.dispatch("read_page", {"page": 3})


def test_dispatch_names_the_corpus_when_the_doc_id_is_wrong(docs, case):
    research = _research(_LLM([]), docs, case)
    out = research.dispatch("read_page", {"doc_id": "NAB/FY26/whatever", "pdf_page": 1})
    assert "unknown doc_id" in out["error"]


def test_a_unique_doc_id_suffix_still_resolves(docs, case):
    research = _research(_LLM([]), docs, case)
    out = research.read_page("FY25/results_presentation", 2)
    assert out["doc_id"] == "CBA/FY25/results_presentation"


# ---------------------------------------------------------------------------
# The submit path: one submission becomes the pipeline's artifact
# ---------------------------------------------------------------------------


def _submission(**overrides) -> dict:
    payload = {
        "evidence": [
            {
                "id": "e1",
                "doc_id": "CBA/FY26/profit_announcement",
                "pdf_page": 12,
                "quote": "Net interest margin    2.05%    2.08%",
                "numbers": [
                    {"label": "NIM FY26", "value": 2.05, "unit": "%"},
                    {"label": "NIM FY25", "value": 2.08, "unit": "%"},
                ],
            }
        ],
        "movement": {"from_value": 208, "to_value": 205, "delta": -3, "unit": "bps"},
        "movement_row": "Net interest margin",
        "movement_from_column": "FY25",
        "movement_to_column": "FY26",
        "basis": "cash",
        "headline": "The margin fell 3 basis points.",
        "headline_evidence": ["e1"],
        "drivers": [
            {
                "canonical": "funding.deposits",
                "bank_label": "Deposits",
                "contribution": {"value": -3, "unit": "bps"},
                "columns": "FY25 -> FY26",
                "narrative": "Deposit pricing competition.",
                "confidence": 90,
                "evidence": ["e1"],
            }
        ],
        "attribution_confidence": 85,
        "limitations": [],
    }
    payload.update(overrides)
    return payload


def test_submission_becomes_a_valid_attribution(docs, case):
    research = _research(_LLM([]), docs, case)
    attribution, rejections = RA.build_attribution(
        _submission(), research, case, TAXONOMY["nim"], REGISTRY
    )
    assert rejections == []
    assert isinstance(attribution, Attribution)
    assert attribution.movement.delta == -3
    assert attribution.movement_source == "row 'Net interest margin', column FY25 -> column FY26"
    # The agent's own ids are remapped onto the records code minted.
    ids = {record.id for record in attribution.evidence_records}
    assert attribution.drivers[0].evidence[0] in ids
    assert attribution.headline_evidence[0] in ids


def test_an_unquotable_citation_loses_the_claim_that_rests_on_it(docs, case):
    """The never-guess gate, applied to the agent: no quote, no number."""
    research = _research(_LLM([]), docs, case)
    payload = _submission(
        evidence=[
            {
                "id": "e1",
                "doc_id": "CBA/FY26/profit_announcement",
                "pdf_page": 12,
                "quote": "Deposit competition cost the margin three basis points.",
            }
        ]
    )
    attribution, rejections = RA.build_attribution(
        payload, research, case, TAXONOMY["nim"], REGISTRY
    )
    assert rejections
    assert attribution.drivers[0].contribution is None
    assert attribution.drivers[0].confidence <= 20
    assert any("were dropped" in limit for limit in attribution.limitations)


def test_the_charge_sign_convention_reaches_the_agent_too(docs, case):
    """An impairment movement read out of a bracketed P&L is re-signed."""
    research = _research(_LLM([]), docs, case | {"metric": "impairment"}, metric="impairment")
    payload = _submission(
        evidence=[
            {
                "id": "e1",
                "doc_id": "CBA/FY26/profit_announcement",
                "pdf_page": 13,
                "quote": "Loan impairment expense    1,050    900",
            }
        ],
        movement={"from_value": -900, "to_value": -1050, "delta": -150, "unit": "$m"},
        drivers=[],
        headline_evidence=["e1"],
    )
    attribution, _ = RA.build_attribution(
        payload, research, case | {"metric": "impairment"}, TAXONOMY["impairment"], REGISTRY
    )
    assert (attribution.movement.from_value, attribution.movement.to_value) == (900, 1050)
    assert attribution.movement.delta == 150


def test_a_delta_that_contradicts_its_endpoints_is_normalised(docs, case):
    research = _research(_LLM([]), docs, case)
    payload = _submission(
        movement={"from_value": 208, "to_value": 205, "delta": -0.03, "unit": "bps"}
    )
    attribution, _ = RA.build_attribution(payload, research, case, TAXONOMY["nim"], REGISTRY)
    assert attribution.movement.delta == -3
    assert any("normalised" in limit for limit in attribution.limitations)


def test_a_driver_may_cite_a_verified_record_the_evidence_list_forgot(docs, case):
    """The record was minted from the page's own words, so the claim stands."""
    research = _research(_LLM([]), docs, case)
    research.cite("CBA/FY26/profit_announcement", 12,
                  [{"quote": "Net interest margin    2.05%    2.08%"}])
    payload = _submission(
        evidence=[],
        headline_evidence=[],
        drivers=[{
            "canonical": "funding.deposits",
            "contribution": {"value": -3, "unit": "bps"},
            "narrative": "Deposit pricing.", "confidence": 90, "evidence": ["ev-1"],
        }],
    )
    attribution, _ = RA.build_attribution(payload, research, case, TAXONOMY["nim"], REGISTRY)
    assert [r.id for r in attribution.evidence_records] == ["ev-1"]
    assert attribution.drivers[0].contribution.value == -3


def test_an_id_no_tool_minted_still_loses_its_claim(docs, case):
    research = _research(_LLM([]), docs, case)
    payload = _submission(
        evidence=[],
        headline_evidence=[],
        drivers=[{
            "canonical": "funding.deposits",
            "contribution": {"value": -3, "unit": "bps"},
            "narrative": "n", "confidence": 90, "evidence": ["ev-99"],
        }],
    )
    attribution, _ = RA.build_attribution(payload, research, case, TAXONOMY["nim"], REGISTRY)
    assert attribution.evidence_records == []
    assert attribution.drivers[0].contribution is None


def test_a_contribution_in_another_unit_stops_being_a_contribution(docs, case):
    """A bps margin move is not a component of a dollar bridge, and the
    reconciliation would otherwise sum it as three dollars."""
    bridge = case | {"metric": "cash_earnings"}
    research = _research(_LLM([]), docs, bridge, metric="cash_earnings")
    payload = _submission(
        movement={"from_value": 10252, "to_value": 10982, "delta": 730, "unit": "$m"},
        drivers=[
            {"canonical": "nii", "contribution": {"value": 733, "unit": "$m"},
             "narrative": "n", "confidence": 92, "evidence": ["e1"]},
            {"canonical": "nii.margin", "contribution": {"value": -3, "unit": "bps"},
             "narrative": "NIM fell 3bpts.", "confidence": 92, "evidence": ["e1"]},
        ],
    )
    attribution, _ = RA.build_attribution(
        payload, research, bridge, TAXONOMY["cash_earnings"], REGISTRY
    )
    margin = next(d for d in attribution.drivers if d.canonical == "nii.margin")
    assert margin.contribution is None
    assert margin.confidence <= 60
    assert margin.narrative == "NIM fell 3bpts."
    assert any("not the movement's unit" in limit for limit in attribution.limitations)
    # The dollar component is untouched, and the bridge still reconciles.
    assert next(d for d in attribution.drivers if d.canonical == "nii").contribution.value == 733


def test_one_malformed_sub_object_does_not_discard_the_run(docs, case):
    """A driver rated 105 and a disagreement with an invented reason are
    dropped and named, so the rest of the research still ships."""
    research = _research(_LLM([]), docs, case)
    payload = _submission(
        drivers=[
            {"canonical": "funding.deposits", "contribution": {"value": -3, "unit": "bps"},
             "narrative": "ok", "confidence": 90, "evidence": ["e1"]},
            {"canonical": "mix", "narrative": "bad", "confidence": 105, "evidence": ["e1"]},
        ],
        disagreements=[{"topic": "t", "values": ["a"], "preferred": "a",
                        "reason": "presentation", "explanation": "e"}],
    )
    attribution, _ = RA.build_attribution(payload, research, case, TAXONOMY["nim"], REGISTRY)
    assert [d.canonical for d in attribution.drivers] == ["funding.deposits"]
    assert attribution.disagreements == []
    assert sum("dropped as malformed" in limit for limit in attribution.limitations) == 2


def test_finalise_caps_a_failing_answer_at_40(docs, case):
    """The pipeline's fatal cap runs over the agent's answer unchanged."""
    research = _research(_LLM([]), docs, case)
    payload = _submission(
        movement={"from_value": 208, "to_value": 205, "delta": -3, "unit": "bps"},
        drivers=[
            {
                "canonical": "funding.deposits",
                "contribution": {"value": -30, "unit": "bps"},
                "narrative": "n",
                "confidence": 95,
                "evidence": ["e1"],
            }
        ],
    )
    attribution, _ = RA.build_attribution(payload, research, case, TAXONOMY["nim"], REGISTRY)
    attribution = RA.finalise(attribution, research, case, TAXONOMY["nim"], REGISTRY, None)
    assert attribution.attribution_confidence == 40
    assert any("drivers_reconcile" in limit for limit in attribution.limitations)


def test_finalise_caps_drivers_at_85_without_a_primary_walk(docs, case):
    """A walk metric with no walk of this comparison is not walk-verified."""
    llm = _LLM(
        [],
        walk_reply={
            "title": "NIM movement",
            "start_label": "Dec 25 Half", "start_bps": 206,
            "bars": [{"label": "Deposits", "bps": -1}],
            "end_label": "Jun 26 Half", "end_bps": 205,
        },
    )
    research = _research(llm, docs, case)
    research.read_chart("CBA/FY26/profit_announcement", 14)
    attribution, _ = RA.build_attribution(
        _submission(), research, case, TAXONOMY["nim"], REGISTRY
    )
    attribution = RA.finalise(attribution, research, case, TAXONOMY["nim"], REGISTRY, None)
    assert attribution.attribution_confidence <= 85
    assert all(driver.confidence <= 85 for driver in attribution.drivers)


# ---------------------------------------------------------------------------
# The loop
# ---------------------------------------------------------------------------


@pytest.fixture
def wired(monkeypatch, tmp_path, docs):
    """run_agent_case with the corpus, the registry and out/ replaced."""
    registry_dir = tmp_path / "registry"
    registry_dir.mkdir()
    (registry_dir / "cba.json").write_text(json.dumps(REGISTRY))
    monkeypatch.setattr(RA, "REGISTRY_DIR", registry_dir)
    monkeypatch.setattr(RA, "OUT_DIR", tmp_path / "out")
    monkeypatch.setattr(RA, "documents_for_period", lambda bank, *periods: docs)
    monkeypatch.setattr(
        RA, "retrieve",
        lambda doc, query, top_k=6: [(12, 1.0)] if len(doc.page_texts()) > 13 else [],
    )
    return tmp_path


def _run(llm, monkeypatch, combo=None):
    monkeypatch.setattr(RA, "LLM", lambda: llm)
    monkeypatch.setitem(RA.COMBOS, "agentic", combo or _Combo())
    return RA.run_agent_case("CBA", "nim", "FY26", "FY25", "agentic")


def test_the_loop_researches_then_submits(wired, monkeypatch):
    llm = _LLM(
        [
            _assistant(_tool_call("c1", "search_pages", {"query": "net interest margin"})),
            _assistant(_tool_call("c2", "read_page",
                                  {"doc_id": "CBA/FY26/profit_announcement", "pdf_page": 12})),
            _assistant(_tool_call("c3", "submit", _submission())),
        ]
    )
    attribution, out = _run(llm, monkeypatch)
    assert attribution.movement.delta == -3
    assert attribution.provenance["orchestration"] == "agent"
    assert attribution.provenance["tool_calls"] == 2
    assert attribution.provenance["budget_exhausted"] == "no"
    # The artifacts the harness reads are both written, in the pipeline's shape.
    saved = json.loads((out / "attribution.json").read_text())
    assert saved["bank"] == "CBA" and saved["metric"] == "nim"
    assert (out / "report.md").read_text().startswith("# CBA — nim — FY26 vs FY25")
    assert out.name == "cba-nim-fy26-vs-fy25-agentic"


def test_a_rejected_submission_is_returned_for_correction(wired, monkeypatch):
    bad = _submission(
        evidence=[
            {
                "id": "e1",
                "doc_id": "CBA/FY26/profit_announcement",
                "pdf_page": 12,
                "quote": "the margin fell three basis points",
            }
        ]
    )
    llm = _LLM(
        [
            _assistant(_tool_call("c1", "submit", bad)),
            _assistant(_tool_call("c2", "submit", _submission())),
        ]
    )
    attribution, _out = _run(llm, monkeypatch)
    assert attribution.drivers[0].contribution is not None
    assert not any("were dropped" in limit for limit in attribution.limitations)


def test_a_submission_still_ships_when_the_agent_cannot_fix_it(wired, monkeypatch):
    """After the last attempt the answer ships with the bad records dropped."""
    bad = _submission(
        evidence=[
            {
                "id": "e1",
                "doc_id": "CBA/FY26/profit_announcement",
                "pdf_page": 12,
                "quote": "the margin fell three basis points",
            }
        ]
    )
    llm = _LLM([_assistant(_tool_call(f"c{i}", "submit", bad)) for i in range(4)])
    attribution, _out = _run(llm, monkeypatch)
    assert attribution.drivers[0].contribution is None
    assert any("were dropped" in limit for limit in attribution.limitations)


def test_the_tool_call_budget_forces_a_submission(wired, monkeypatch):
    combo = _Combo(max_tool_calls=2)
    search = _assistant(_tool_call("c", "search_pages", {"query": "margin"}))
    llm = _LLM([search, search, _assistant(_tool_call("cs", "submit", _submission()))])
    attribution, _out = _run(llm, monkeypatch, combo)
    assert attribution.provenance["budget_exhausted"].startswith("the tool-call budget")
    assert any("Research stopped early" in limit for limit in attribution.limitations)
    # The last turn offers the submit tool alone, so the loop cannot restart.
    assert llm.turns[-1] == ["submit"]


def test_the_cost_ceiling_forces_a_submission(wired, monkeypatch):
    combo = _Combo(cost_ceiling_usd=0.01)
    llm = _LLM([_assistant(_tool_call("cs", "submit", _submission()))])
    llm.usage.cost_usd = 0.5
    attribution, _out = _run(llm, monkeypatch, combo)
    assert attribution.provenance["budget_exhausted"].startswith("the cost ceiling")


def test_a_model_that_ignores_the_submit_request_is_stopped(wired, monkeypatch):
    """Once a budget runs out it latches, so only a turn bound can end a model
    that keeps asking for tools it was no longer offered."""
    combo = _Combo(max_tool_calls=2)
    ignore = _assistant(_tool_call("c", "search_pages", {"query": "margin"}))
    llm = _LLM([ignore] * 200)
    attribution, out = _run(llm, monkeypatch, combo)
    assert len(llm.turns) <= combo.max_tool_calls + RA.MAX_TURNS_AFTER_BUDGET + 1
    assert attribution.movement is None
    assert any("without a submitted attribution" in limit for limit in attribution.limitations)
    assert (out / "report.md").exists()


def test_an_artifact_still_ships_when_the_agent_never_submits(wired, monkeypatch):
    """A model that will not call submit costs the case its answer, not a crash."""
    llm = _LLM([{"role": "assistant", "content": "Here is my analysis in prose."}] * 6)
    attribution, out = _run(llm, monkeypatch)
    assert attribution.movement is None
    assert attribution.attribution_confidence == 0
    assert any("without a submitted attribution" in limit for limit in attribution.limitations)
    assert (out / "report.md").exists()


def test_a_failing_tool_is_a_message_the_agent_can_answer(wired, monkeypatch):
    llm = _LLM(
        [
            _assistant(_tool_call("c1", "read_page",
                                  {"doc_id": "CBA/FY26/profit_announcement", "pdf_page": 999})),
            _assistant(_tool_call("c2", "submit", _submission())),
        ]
    )
    attribution, _out = _run(llm, monkeypatch)
    assert attribution.movement.delta == -3


def test_a_rejected_submit_still_answers_the_other_calls_in_its_turn(wired, monkeypatch):
    """A provider that asked for two tools and got one result rejects the next
    request, so a rejected submission must not swallow its neighbours."""
    bad = _submission(
        evidence=[{"id": "e1", "doc_id": "CBA/FY26/profit_announcement", "pdf_page": 12,
                   "quote": "the margin fell three basis points"}]
    )
    captured: list[list[dict]] = []

    class _Recording(_LLM):
        def chat_tools(self, model, messages, tools, max_tokens=None):
            captured.append(list(messages))
            return super().chat_tools(model, messages, tools, max_tokens)

    llm = _Recording(
        [
            _assistant(
                _tool_call("c1", "submit", bad),
                _tool_call("c2", "read_page",
                           {"doc_id": "CBA/FY26/profit_announcement", "pdf_page": 12}),
            ),
            _assistant(_tool_call("c3", "submit", _submission())),
        ]
    )
    _run(llm, monkeypatch)
    final = captured[-1]
    asked = {c["id"] for m in final if m.get("tool_calls") for c in m["tool_calls"]}
    answered = {m["tool_call_id"] for m in final if m["role"] == "tool"}
    assert asked <= answered


def test_two_tool_calls_in_one_turn_are_both_answered(wired, monkeypatch):
    llm = _LLM(
        [
            _assistant(
                _tool_call("c1", "bank_language", {"bank": "CBA"}),
                _tool_call("c2", "read_page",
                           {"doc_id": "CBA/FY26/profit_announcement", "pdf_page": 12}),
            ),
            _assistant(_tool_call("c3", "submit", _submission())),
        ]
    )
    attribution, _out = _run(llm, monkeypatch)
    assert attribution.provenance["tool_calls"] == 2


def test_the_loop_can_cite_a_page_then_submit_by_id(wired, monkeypatch):
    llm = _LLM(
        [
            _assistant(_tool_call("c1", "read_page",
                                  {"doc_id": "CBA/FY26/profit_announcement", "pdf_page": 12})),
            _assistant(_tool_call("c2", "cite", {
                "doc_id": "CBA/FY26/profit_announcement", "pdf_page": 12,
                "quotes": [{"quote": "Net interest margin    2.05%    2.08%"}],
            })),
            _assistant(_tool_call("c3", "submit", _submission(
                evidence=[{"id": "ev-1"}], headline_evidence=["ev-1"],
                drivers=[{
                    "canonical": "funding.deposits",
                    "contribution": {"value": -3, "unit": "bps"},
                    "narrative": "Deposit pricing.", "confidence": 90, "evidence": ["ev-1"],
                }],
            ))),
        ]
    )
    attribution, _out = _run(llm, monkeypatch)
    assert [r.id for r in attribution.evidence_records] == ["ev-1"]
    assert attribution.drivers[0].contribution.value == -3


def test_the_combo_chooses_the_orchestration_shell(monkeypatch, tmp_path, capsys):
    """--combo routes to the shell the combo declares, and to nothing else."""
    import sys

    from bank_equity_researcher import cli, pipeline, research_agent

    called: list[str] = []

    def _fake(shell):
        def run(bank, metric, period, comparator, combo):
            called.append(f"{shell}:{combo}")
            out = tmp_path / shell
            out.mkdir(exist_ok=True)
            (out / "report.md").write_text("report")
            return None, out

        return run

    monkeypatch.setattr(pipeline, "run_case", _fake("pipeline"))
    monkeypatch.setattr(research_agent, "run_agent_case", _fake("agent"))
    for combo, shell in (("cheap", "pipeline"), ("normal", "pipeline"),
                         ("agentic", "agent"), ("agentic-cheap", "agent")):
        monkeypatch.setattr(
            sys, "argv",
            ["x", "analyse", "--bank", "CBA", "--metric", "nim", "--period", "FY26",
             "--combo", combo],
        )
        assert cli.main() == 0
        assert called[-1] == f"{shell}:{combo}"
    capsys.readouterr()


def test_the_tool_surface_is_the_documented_one():
    names = [spec["function"]["name"] for spec in RA.TOOL_SPECS]
    assert names == [
        "search_pages", "read_page", "read_chart", "cite", "follow_references",
        "bank_language",
    ]
    assert RA.SUBMIT_SPEC["function"]["name"] == "submit"
    for spec in [*RA.TOOL_SPECS, RA.SUBMIT_SPEC]:
        assert spec["function"]["parameters"]["type"] == "object"
        assert spec["function"]["description"]
