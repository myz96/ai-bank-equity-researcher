"""Unit tests for deterministic reference-following (ticket 22).

Every test runs on a synthetic document, so nothing here opens a PDF, calls a
model or touches the network.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher import refs

FOOTER = "  {printed}                    Example Bank - Profit Announcement"

CONTENTS = "\n".join(
    [
        "Contents",
        "Example Bank - Profit Announcement",
        "1. Our Performance",
        "1.1 ",
        "Net Interest Income",
        "5",
        "2. Our Lending Activities",
        "2.1 ",
        "Loans and Other Receivables",
        "6",
        "2.2 ",
        "Provisions for Impairment and Asset Quality",
        "7",
        "6. Other Information",
        "6.2 ",
        "ASX Appendix 4E",
        "9",
    ]
)

IMPAIRMENT_TERMS = {"loan", "impairment", "provisions", "collective", "individual", "credit"}
MARGIN_TERMS = {"interest", "margin", "average", "earning", "assets", "income"}


class _Doc:
    """The three members refs.py uses from a corpus Document."""

    def __init__(self, name: str, pages: list[str], doc_type: str = "profit_announcement") -> None:
        self.doc_id = f"XYZ/FY26/{name}"
        self.doc_type = doc_type
        self.path = f"/nowhere/{name}.pdf"
        self._pages = pages

    def page_texts(self) -> list[str]:
        return list(self._pages)


@pytest.fixture(autouse=True)
def _clear_caches():
    refs._notes_cache.clear()
    refs._printed_cache.clear()
    yield
    refs._notes_cache.clear()
    refs._printed_cache.clear()


def _book() -> _Doc:
    """A ten-page results book: cover, contents, then eight numbered pages.

    Printed page N sits on PDF page N + 2.
    """
    pages = [
        "Example Bank\nFull Year Results",
        CONTENTS,
        "\n".join(["Highlights", FOOTER.format(printed=1), "Cash net profit after tax 10,866"]),
        "\n".join(
            [
                "Financial Statements",
                FOOTER.format(printed=2),
                "Consolidated Income Statement",
                " ",
                "Note ",
                "$M ",
                "Net interest income ",
                "1.1 ",
                "25,586 ",
                "Loan impairment expense ",
                "2.2 ",
                "(788) ",
                "For further details on the balance sheet refer to page 4.",
            ]
        ),
        "\n".join(
            [
                "Group Performance Analysis",
                FOOTER.format(printed=3),
                "Loan Impairment Expense",
                "Refer to Note 2.2 for the provision movements.",
                "Total assets grew and the balance sheet expanded through the year in "
                "every division and every product. page 4",
            ]
        ),
        "\n".join(
            [
                "Group Performance Analysis (continued)",
                FOOTER.format(printed=4),
                "Group Assets and Liabilities",
                "Average interest earning assets grew 4%",
            ]
        ),
        "\n".join(
            [
                "Appendices",
                FOOTER.format(printed=5),
                "2.2 ",
                "Provisions for Impairment and Asset Quality",
                " ",
                "Collective provisions 5,685 5,561",
            ]
        ),
        "\n".join(
            [
                "Appendices (continued)",
                FOOTER.format(printed=6),
                "2.2 ",
                "Provisions for Impairment and Asset Quality (continued)",
                " ",
                "Net collective provision funding 606 456",
            ]
        ),
        "\n".join(
            [
                "  1                    Segment note",
                FOOTER.format(printed=7),
                "A description of the methodology is in Note 2.1 of the 2026 Annual Report.",
            ]
            + [f"Filler row {i}" for i in range(30)]
            + ["2.2 ", "Peer Comparison Table"]
        ),
        "\n".join(
            [
                "Divisional Performance",
                FOOTER.format(printed=8),
                "Loan impairment expense 146",
                "1 See Provisions for Impairment and Asset Quality for the reconciliation.",
            ]
        ),
    ]
    return _Doc("book", pages)


# --- the notes index ---------------------------------------------------------


def test_notes_index_groups_a_note_with_its_continuation_page():
    index = refs.notes_index(_book())
    assert index["2.2"].pages == (7, 8)
    assert index["2.2"].title == "Provisions for Impairment and Asset Quality"


def test_notes_index_never_points_a_note_at_the_contents_page():
    index = refs.notes_index(_book())
    assert all(2 not in note.pages for note in index.values())


def test_notes_index_ignores_a_number_printed_deep_in_a_page():
    # PDF page 9 prints "2.2" below thirty filler rows: a table value, not a
    # heading.
    assert 9 not in refs.notes_index(_book())["2.2"].pages


def test_notes_index_ignores_a_note_the_contents_page_never_declares():
    doc = _Doc(
        "undeclared",
        [
            CONTENTS,
            "\n".join(["9.9 ", "Segment Reporting Detail", "Rows follow"]),
        ],
    )
    assert "9.9" not in refs.notes_index(doc)


def test_notes_index_is_empty_without_a_contents_page():
    # Slides print "1.9" above a two-word caption. Without a contents page
    # declaring the notes, none of that becomes an index.
    doc = _Doc(
        "deck",
        ["\n".join(["1.9 ", "Variable rate", "12.5 ", "Equity investments"])],
        doc_type="results_presentation",
    )
    assert refs.notes_index(doc) == {}


# --- the printed-page map ----------------------------------------------------


def test_printed_page_map_resolves_the_offset():
    mapping = refs.printed_page_map(_book())
    assert mapping[1] == 3
    assert mapping[4] == 6
    assert mapping[8] == 10


def test_printed_page_map_ignores_a_lone_number_without_neighbours():
    # PDF page 9 opens with "1  Segment note"; printed page 1 is page 3.
    assert refs.printed_page_map(_book())[1] == 3


# --- the marker scanner ------------------------------------------------------


def _targets(references):
    return {(r.tier, r.target, r.pages) for r in references}


def test_scan_follows_an_explicit_note_reference():
    found = refs.scan_page(_book(), 5, IMPAIRMENT_TERMS)
    assert (0, "Note 2.2 Provisions for Impairment and Asset Quality", (7, 8)) in _targets(found)


def test_scan_follows_a_bare_note_number_in_a_reference_column():
    # PDF page 4 is the income statement: a column headed "Note" and the bare
    # number 2.2 beside the loan impairment row.
    found = refs.scan_page(_book(), 4, IMPAIRMENT_TERMS)
    assert (0, "Note 2.2 Provisions for Impairment and Asset Quality", (7, 8)) in _targets(found)


def test_scan_follows_the_note_heading_on_the_page_itself():
    # The second page of a note points at the first: the table broke over the
    # page end.
    found = refs.scan_page(_book(), 8, IMPAIRMENT_TERMS)
    assert (0, "Note 2.2 Provisions for Impairment and Asset Quality", (7, 8)) in _targets(found)


def test_scan_refuses_a_reference_into_another_document():
    found = refs.scan_page(_book(), 9, IMPAIRMENT_TERMS)
    assert all("2.1" not in reference.target for reference in found)


def test_scan_follows_a_page_reference():
    found = refs.scan_page(_book(), 4, MARGIN_TERMS)
    assert (1, "page 4", (6,)) in _targets(found)


def test_scan_ignores_a_page_number_no_word_refers_to():
    # Page 5 ends "The balance sheet expanded again. page 4" — a number in a
    # sentence, not a pointer.
    found = refs.scan_page(_book(), 5, MARGIN_TERMS)
    assert all(reference.tier != 1 for reference in found)


def test_scan_follows_a_footnote_that_names_a_note_by_title():
    found = refs.scan_page(_book(), 10, IMPAIRMENT_TERMS)
    assert (2, "Note 2.2 Provisions for Impairment and Asset Quality", (7, 8)) in _targets(found)


def test_scan_scores_a_target_by_the_words_it_shares_with_the_case():
    note = next(r for r in refs.scan_page(_book(), 5, IMPAIRMENT_TERMS) if r.tier == 0)
    assert note.relevance == 2  # "provisions" and "impairment"
