"""Question scoping: which bank, which period, which document (review round 1).

Three ways a free-form question reached the wrong corpus, or none at all:

- a bank whose full name is built only from generic words could not be named;
- a period the corpus does not hold was swapped for another one in silence;
- a document name that identified no bank still resolved to a document.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher.tools import corpus as C
from bank_equity_researcher.validation import schema as S
from bank_equity_researcher.validation.schema import enforce_answer_gate

# ---------------------------------------------------------------------------
# Item 13: a full name made only of generic words
# ---------------------------------------------------------------------------


def test_a_bank_named_in_full_is_recognised():
    """"National Australia Bank" is national + australia + bank.

    Every one of those words names some Australian bank, so each is generic
    and the distinctive-word index held nothing for NAB. A question that
    spelled the name out raised "the question names no bank in the corpus" —
    a RuntimeError on a valid question.
    """
    assert C.banks_named("What drove National Australia Bank's FY25 margin?") == ["NAB"]


def test_a_full_name_does_not_swallow_its_neighbours():
    named = C.banks_named(
        "Compare National Australia Bank with Westpac and Commonwealth Bank of Australia."
    )
    assert named == ["NAB", "WBC", "CBA"]


def test_a_question_names_its_own_periods():
    assert C.periods_named("Across CBA, NAB and Westpac in FY25, who converted best?") == ["FY25"]
    assert C.periods_named("from FY25 to FY26, and the 1H26 half") == ["FY25", "FY26", "1H26"]


def test_the_newest_period_sorts_last():
    assert sorted(["1H26", "FY25", "FY26", "2H25"], key=C.period_sort_key) == [
        "FY25", "2H25", "1H26", "FY26"
    ]


def test_generic_words_alone_still_name_no_bank():
    """The phrase must be the WHOLE name, not any bank-ish word in a sentence."""
    assert C.banks_named("the Australian banking group reported a national result") == []


# ---------------------------------------------------------------------------
# Item 14: a substituted period is declared
# ---------------------------------------------------------------------------


class _Doc:
    def __init__(self, period: str) -> None:
        self.period = period
        self.bank = "CBA"
        self.doc_id = f"CBA/{period}/profit_announcement"


@pytest.fixture
def only_fy25(monkeypatch):
    monkeypatch.setattr(C, "load_documents", lambda bank: [_Doc("FY25")])
    monkeypatch.setattr(C, "latest_period", lambda bank: "FY25")


def test_a_period_the_corpus_lacks_is_declared(only_fy25):
    """The answer must say which period it was actually researched in.

    A question about FY26 fell back to the newest documents held, and nothing
    recorded the swap, so the answer read as though it came from FY26.
    """
    notes: list[str] = []
    docs = C.documents_for_question("CBA FY26 margin", "CBA", ["FY26"], notes=notes)
    assert [d.period for d in docs] == ["FY25"]
    assert len(notes) == 1
    assert "FY26" in notes[0] and "FY25" in notes[0]


def test_a_period_the_corpus_holds_is_not_declared(only_fy25):
    notes: list[str] = []
    C.documents_for_question("CBA FY25 margin", "CBA", ["FY25"], notes=notes)
    assert notes == []


# ---------------------------------------------------------------------------
# Item 15: a document name must identify its bank
# ---------------------------------------------------------------------------


INDEX = {
    "cba-fy26-profit-announcement": "CBA/FY26/profit_announcement",
    "nab-fy25-results-book": "NAB/FY25/results_book",
    "wbc-fy25-presentation-and-idp": "WBC/FY25/investor_discussion_pack",
}


def test_an_exact_alias_resolves():
    assert C.resolve_doc_name("CBA/FY26/profit-announcement", INDEX) == (
        "CBA/FY26/profit_announcement"
    )


def test_a_partial_name_that_agrees_on_bank_and_period_resolves():
    assert C.resolve_doc_name("WBC/FY25/presentation", INDEX) == (
        "WBC/FY25/investor_discussion_pack"
    )


def test_a_bank_less_name_does_not_resolve():
    """"results-book" sits inside exactly one alias, so it used to resolve.

    It names no bank and no period. One bank filing its book under that word
    is not a reason to hand the reader that bank's document.
    """
    assert C.resolve_doc_name("results-book", INDEX) is None


def test_a_name_with_the_wrong_bank_does_not_resolve():
    assert C.resolve_doc_name("CBA/FY25/results-book", INDEX) is None


def test_a_name_with_the_wrong_period_does_not_resolve():
    """The containment pass agrees on BANK and PERIOD, and the period half of
    that rule needs its own row: the bank above is right here and only the year
    is wrong, so a name naming a book no bank filed that year resolves to
    nothing."""
    assert C.resolve_doc_name("NAB/FY26/results-book", INDEX) is None


def test_an_empty_name_does_not_resolve():
    """The guard before the index lookup. An empty key is inside every alias,
    so without it the containment pass reads a blank name as every document."""
    assert C.resolve_doc_name("", INDEX) is None


# ---------------------------------------------------------------------------
# Item 16: the gate strips facts, not prose
# ---------------------------------------------------------------------------


def test_stripping_a_fact_warns_that_the_prose_still_states_it():
    """The gate deletes the fact and leaves the sentence that made the claim.

    Rewriting the prose would be a second authoring pass, so the gate does not
    try. It must say so instead: a reader of the answer alone would otherwise
    see an unsupported number with nothing marking it.
    """
    facts = [
        {"fact": "CET1 was 12.3%.", "citations": ["ev-1"]},
        {"fact": "Impairments rose $150m.", "citations": ["ev-9"]},
    ]
    kept, limitations, confidence = enforce_answer_gate(facts, [], 85, {"ev-1"})
    assert [f["fact"] for f in kept] == ["CET1 was 12.3%."]
    assert any("Stripped unsupported quantified fact" in x for x in limitations)
    warning = [x for x in limitations if "prose was NOT rewritten" in x]
    assert len(warning) == 1
    assert "Impairments rose $150m." in warning[0]
    # One surviving fact means the answer is still an answer, so the
    # nothing-survived cap does not fire.
    assert confidence == 85


def test_no_warning_when_nothing_is_stripped():
    """The warning is the record of a strip, so an answer that lost nothing
    must not carry it: a limitation telling every reader the prose may state
    unsupported numbers is a false alarm on a clean answer."""
    facts = [{"fact": "CET1 was 12.3%.", "citations": ["ev-1"]}]
    _kept, limitations, _confidence = enforce_answer_gate(facts, [], 85, {"ev-1"})
    assert not any("prose was NOT rewritten" in x for x in limitations)


# ---------------------------------------------------------------------------
# Item 17: the cache-key invariant is enforced, not assumed
# ---------------------------------------------------------------------------


def test_two_documents_sharing_a_filename_stem_are_refused(monkeypatch):
    """The page-text and embedding caches are keyed by the filename stem.

    Two documents with one stem would share both caches, so one bank's pages
    would be served for another's. The manifests hold the convention today;
    discover.py copies a filename out of a model reply, where a generic
    basename is exactly what a bank's IR page offers.
    """

    class _Stemmed:
        def __init__(self, bank, filename):
            self.bank = bank
            self.filename = filename
            self.period = "FY25"
            self.doc_id = f"{bank}/FY25/results_announcement"

    monkeypatch.setattr(C, "manifest_banks", lambda: ["CBA", "NAB"])
    monkeypatch.setattr(
        C, "load_documents",
        lambda bank: [_Stemmed(bank, "results-announcement.pdf")],
    )
    with pytest.raises(RuntimeError, match="share the filename stem"):
        C.all_documents()


def test_the_real_corpus_holds_the_invariant():
    """The committed manifests must keep their stems distinct."""
    C.all_documents()


# ---------------------------------------------------------------------------
# Review round 7: every manifest doc_type is in the shared vocabulary
# ---------------------------------------------------------------------------


def test_every_manifest_doc_type_is_in_the_vocabulary():
    """A doc_type outside schema.DOC_TYPES degrades handling in silence.

    printed_page_of and walk_sum_tolerance both dispatch on the doc_type
    string. The hand-built MQG manifest shipped "mda"/"presentation", so its
    slides lost slide-page numbering and its walks were held to the 1.0 text
    tolerance instead of the presentation lift (review round 7, 2026-09-01).
    discover.py's prompt names the vocabulary, but a hand-built manifest
    bypasses the prompt; this test does not.
    """
    for doc in C.all_documents():
        assert doc.doc_type in S.DOC_TYPES, (
            f"{doc.doc_id}: doc_type {doc.doc_type!r} is not in schema.DOC_TYPES; "
            "either use an existing term or add it there WITH its consumers checked"
        )


def test_presentation_doc_types_are_vocabulary_terms():
    assert set(S.PRESENTATION_DOC_TYPES) <= S.DOC_TYPES


def test_every_manifest_bank_has_a_registry_file():
    """A manifest without a registry file loads a silent empty map.

    Both registry load paths fall back to {}, so the bank loses its calendar,
    its language map, and full-name resolution (banks_named) with no error.
    That happened: manifest/mqg.json landed without registry/mqg.json, and
    "Macquarie" named no bank (review round 9, 2026-09-01). A bank that truly
    needs no registry should record that decision here, not by omission.
    """
    from bank_equity_researcher.config import MANIFEST_DIR, REGISTRY_DIR

    for manifest in MANIFEST_DIR.glob("*.json"):
        assert (REGISTRY_DIR / manifest.name).exists(), (
            f"{manifest.name}: manifest exists but registry/{manifest.name} does not"
        )
