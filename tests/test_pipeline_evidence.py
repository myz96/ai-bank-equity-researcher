"""The open-loop pipeline's evidence pool across its retry (review round 1).

The author may ask for evidence the first pass did not retrieve, once per
round. Those records went into the author's own copy of the pool and nowhere
else, while the page went into `candidates` — the set that decides whether a
page may be fetched at all, and which the retry never resets.

So the second attempt was strictly worse informed than the first: it could not
see what attempt 1 had fetched, and it could not fetch it again either. It
asked, and the fetch returned nothing, in silence.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher import pipeline as P
from bank_equity_researcher.schema import EvidenceRecord


class _Doc:
    def __init__(self, doc_id, pages):
        self.doc_id = doc_id
        self.doc_type = "profit_announcement"
        self.period = "FY26"
        self.bank = "CBA"
        self.sha256 = "0" * 64
        self.path = "/nowhere.pdf"
        self._pages = pages

    def page_texts(self):
        return list(self._pages)

    def render_page(self, page_no, zoom=2.0):  # pragma: no cover - no walk page here
        return b"png"


class _Usage:
    cost_usd = 0.0
    prompt_tokens = 0
    completion_tokens = 0


ANSWER_OK = {
    "movement": {"from_value": 208.0, "to_value": 205.0, "delta": -3.0, "unit": "bps"},
    "basis": "cash",
    "headline": "NIM fell 3bps.",
    "drivers": [
        {
            "canonical": "asset_pricing",
            "contribution": {"value": -3.0, "unit": "bps"},
            "narrative": "Lending competition.",
            "confidence": 70,
            "evidence": ["ev-1"],
        }
    ],
    "attribution_confidence": 50,
    "limitations": [],
}
# A movement the checks reject, so attempt 1 is not accepted and the retry runs.
ANSWER_FAILS = {**ANSWER_OK, "movement": None}


class _LLM:
    """A scripted author that records every prompt it is shown."""

    def __init__(self, script):
        self.script = list(script)
        self.prompts = []
        self.usage = _Usage()

    def chat_json(self, model, prompt, max_tokens=None, image_png=None):
        self.prompts.append(prompt)
        return self.script.pop(0)


@pytest.fixture
def harness(monkeypatch, tmp_path):
    """Every collaborator stubbed: no PDF is opened and no model is called."""
    doc = _Doc("CBA/FY26/profit_announcement", ["p1 summary", "p2 note", "p3 appendix"])
    extracted: list[tuple[int, str]] = []

    def install(llm):
        monkeypatch.setattr(P, "LLM", lambda: llm)
        monkeypatch.setattr(P, "documents_for_period", lambda bank, *periods: [doc])
        monkeypatch.setattr(P, "follow_references", lambda doc_by_id, pages, queries: [])
        monkeypatch.setattr(P, "REGISTRY_DIR", tmp_path / "no-registry")
        monkeypatch.setattr(P, "OUT_DIR", tmp_path / "out")

        def fake_retrieve(document, query, top_k=4):
            # The taxonomy's own queries all land on page 1. The author's
            # request lands on page 2, which the first pass never read.
            return [(2, 9.0)] if query.startswith("EXTRA:") else [(1, 1.0)]

        monkeypatch.setattr(P, "retrieve", fake_retrieve)

        def fake_extract(llm_, model, document, page, case_desc, next_id, provenance=None):
            record_id = next_id()
            extracted.append((page, record_id))
            return [
                EvidenceRecord(
                    id=record_id,
                    doc_id=document.doc_id,
                    pdf_page=page,
                    quote=f"quote from page {page}",
                    numbers=[],
                )
            ]

        monkeypatch.setattr(P, "extract_text_evidence", fake_extract)

    return install, extracted


def test_evidence_fetched_in_attempt_one_survives_the_retry(harness):
    install, extracted = harness
    llm = _LLM(
        [
            {"request_evidence": "EXTRA: impairment note"},  # attempt 1, round 0
            ANSWER_FAILS,                                     # attempt 1, round 1
            {"request_evidence": "EXTRA: impairment note"},  # attempt 2, round 0
            ANSWER_OK,                                        # attempt 2, round 1
        ]
    )
    install(llm)
    attribution, _ = P.run_case("CBA", "nim", "FY26", "FY25", "cheap")

    fetched = [record_id for page, record_id in extracted if page == 2]
    assert len(fetched) == 1, "the page is fetched once; candidates blocks a second fetch"
    fetched_id = fetched[0]

    # The retry must SEE what attempt 1 paid to fetch. Prompt 3 is attempt 2's
    # first round, before it asks for anything of its own.
    assert f'"{fetched_id}"' in llm.prompts[2]
    assert f'"{fetched_id}"' in llm.prompts[3]
    # ...and the shipped artifact keeps it, so a driver may cite it and the
    # citation cap can resolve it.
    assert fetched_id in {r.id for r in attribution.evidence_records}


def test_fetched_evidence_reaches_the_artifact_without_a_retry(harness):
    """The single-attempt path keeps the record too, and keeps it once."""
    install, extracted = harness
    llm = _LLM([{"request_evidence": "EXTRA: impairment note"}, ANSWER_OK])
    install(llm)
    attribution, _ = P.run_case("CBA", "nim", "FY26", "FY25", "cheap")

    ids = [r.id for r in attribution.evidence_records]
    assert len(ids) == len(set(ids)), "a fetched record must not be added twice"
    assert len(ids) == len(extracted)


# ---------------------------------------------------------------------------
# Review round 2: the retry carries the sign hint and the ratio-scale note
# ---------------------------------------------------------------------------


BRIDGE_WITH_A_SIGN_ERROR = {
    "movement": {"from_value": 5132.0, "to_value": 5445.0, "delta": 313.0, "unit": "$m"},
    "basis": "cash",
    "headline": "Cash earnings rose $313m.",
    "drivers": [
        # 312 - 1 = 311 against a delta of 313. The gap is +2.00, which is
        # exactly -2 x the impairment contribution and nothing else.
        {"canonical": "nii", "contribution": {"value": 312.0, "unit": "$m"},
         "narrative": "Volume growth.", "confidence": 85, "evidence": ["ev-1"]},
        {"canonical": "credit_impairment_charge", "contribution": {"value": -1.0, "unit": "$m"},
         "narrative": "The charge fell.", "confidence": 85, "evidence": ["ev-1"]},
    ],
    "attribution_confidence": 60,
    "limitations": [],
}


def test_the_retry_asks_about_a_contribution_whose_sign_fits_the_gap(harness):
    """CBA 1H26: the impairment charge FELL $1m, which ADDS $1m to earnings.

    The author copied the change in the charge (-1) into the contribution
    field, and the bridge then missed by exactly -2 x that contribution.
    Nothing converts a cost line's own movement into its effect on earnings, so
    the retry is handed the question — never the answer.
    """
    install, _extracted = harness
    llm = _LLM([BRIDGE_WITH_A_SIGN_ERROR, BRIDGE_WITH_A_SIGN_ERROR])
    install(llm)
    P.run_case("CBA", "cash_earnings", "1H26", "1H25", "cheap")

    retry_prompt = llm.prompts[1]
    assert "check_this_contribution_sign" in retry_prompt
    assert "credit_impairment_charge" in retry_prompt
    # A hint names no value to reach.
    assert "signature of a sign error" in retry_prompt


def test_the_driver_cap_reaches_a_bridge_that_never_closes(harness):
    """The answer declared 60 and its drivers 85; the calibration metrics read
    the DRIVERS, so a failed check used to be invisible to them."""
    install, _extracted = harness
    llm = _LLM([BRIDGE_WITH_A_SIGN_ERROR, BRIDGE_WITH_A_SIGN_ERROR])
    install(llm)
    attribution, _ = P.run_case("CBA", "cash_earnings", "1H26", "1H25", "cheap")

    assert attribution.attribution_confidence <= 40
    assert all(d.confidence <= 80 for d in attribution.drivers if d.contribution)
