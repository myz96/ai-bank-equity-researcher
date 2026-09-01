"""The walk-page annotation read (ticket 27, iteration 3).

A walk chart carries two layers. extract_walk reads the bars. The annotation
layer — the callouts that split one bar into its named parts, each part with
its own number — defeats text extraction, because the PDF text layer emits the
numbers as one block and the labels as another, so nothing but a look at the
page can pair them.

The layer is a bonus, so the rule that matters most is how it FAILS: a call
that errors, a reply in the wrong shape, or an item missing its label must cost
the case nothing at all. Every test below is offline; the vision model is a
stand-in.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher.tools.extract import (
    ANNOTATION_PROMPT,
    MAX_ANNOTATION_RECORDS,
    annotation_records,
    extract_walk_annotations,
)


class _Doc:
    doc_id = "BANK/FY21/results_presentation"
    doc_type = "results_presentation"

    def page_texts(self):
        # Page 63 holds the chart; the text layer prints the callout NUMBERS in
        # one block and their LABELS in another, which is why the pairing needs
        # a look at the page.
        return [""] * 62 + ["(1) (1) +9 (5) (4)\nBus. Lending\nConsumer Fin.\nHome loans\n63"]

    def render_page(self, page_no, zoom=None):
        return b"png"


class _LLM:
    """Returns a scripted reply, or raises it when it is an exception."""

    def __init__(self, reply):
        self.reply = reply
        self.calls = 0

    def chat_json(self, model, prompt, image_png=None, max_tokens=None, deadline_monotonic=None):
        self.calls += 1
        if isinstance(self.reply, Exception):
            raise self.reply
        return self.reply


def _ids():
    counter = iter(range(1, 99))
    return lambda: f"ev-{next(counter)}"


GOOD = {
    "annotations": [
        {"bar": "Asset Pricing", "label": "Home loans: Pricing", "value": 9},
        {"bar": "Asset Pricing", "label": "Bus. Lending", "value": -1},
        {"bar": "Liquids", "label": "Minimal impact on NII", "value": None},
    ]
}


def test_annotation_records_pair_each_label_with_its_own_value():
    records = annotation_records(GOOD, _Doc(), 63, 61, _ids(), "bps")
    assert [r.kind for r in records] == ["walk_annotation"] * 3
    assert records[0].numbers[0].value == 9.0
    assert records[0].numbers[0].unit == "bps"
    assert records[0].numbers[0].label == "Asset Pricing Home loans: Pricing"
    assert records[1].numbers[0].value == -1.0


def test_annotation_records_keep_a_callout_that_carries_no_number():
    """A qualifying phrase beside a bar is evidence too; it just has no value."""
    records = annotation_records(GOOD, _Doc(), 63, 61, _ids(), "bps")
    assert records[2].numbers == []
    assert "Minimal impact on NII" in records[2].quote


@pytest.mark.parametrize(
    "name,why,raw",
    [
        ("not an object", "a list reply is the wrong shape", [1, 2, 3]),
        ("no annotations key", "the key the prompt asked for is missing", {"bars": []}),
        ("annotations not a list", "a string is not a list of callouts", {"annotations": "none"}),
        ("item not an object", "a bare string cannot carry a label", {"annotations": ["+9"]}),
        ("no label", "a number with no label is the defect, not the fix",
         {"annotations": [{"bar": "Liquids", "value": 9}]}),
        ("blank label", "whitespace is not a label",
         {"annotations": [{"label": "   ", "value": 9}]}),
    ],
)
def test_annotation_records_degrade_to_nothing(name, why, raw):
    assert annotation_records(raw, _Doc(), 63, 61, _ids(), "bps") == [], why


def test_annotation_records_drop_a_value_that_is_not_a_number():
    """The label still stands; only the unreadable number goes."""
    raw = {"annotations": [{"label": "Home loans", "value": "about nine"}]}
    records = annotation_records(raw, _Doc(), 63, 61, _ids(), "bps")
    assert len(records) == 1
    assert records[0].numbers == []


def test_annotation_records_are_capped():
    raw = {"annotations": [{"label": f"part {i}", "value": i} for i in range(40)]}
    records = annotation_records(raw, _Doc(), 63, 61, _ids(), "bps")
    assert len(records) == MAX_ANNOTATION_RECORDS


def test_extract_walk_annotations_returns_records_on_a_good_read():
    llm = _LLM(GOOD)
    records = extract_walk_annotations(llm, "vision", _Doc(), 63, "a case", _ids(), unit="bps")
    assert llm.calls == 1, "at most one extra vision call per walk page"
    assert len(records) == 3


def test_extract_walk_annotations_swallows_a_failed_call():
    """An unreachable or unparseable vision read must never crash the case."""
    llm = _LLM(ValueError("unparseable reply"))
    assert extract_walk_annotations(llm, "vision", _Doc(), 63, "a case", _ids()) == []


def test_annotation_prompt_names_no_bank_chart_or_value():
    """Prompts stay generic: the shape of a callout, never its content."""
    prompt = ANNOTATION_PROMPT.format(case="{case}", unit="bps", max_items=12)
    lowered = prompt.lower()
    for word in ("cba", "commonwealth", "westpac", "wbc", "nab", "anz", "home loan", "liquids"):
        assert word not in lowered, f"the prompt names {word}"


def test_annotation_records_drop_a_repeat_of_a_bar_the_walk_already_read():
    """An "annotation" that only repeats a bar is not a callout, and the same
    bar reaching the author twice invites it to claim the bar twice."""
    raw = {
        "annotations": [
            {"bar": "Asset pricing", "label": "Asset pricing", "value": -5},
            {"bar": "Asset pricing", "label": "Home loans", "value": -4},
        ]
    }
    records = annotation_records(
        raw, _Doc(), 63, 61, _ids(), "bps", bar_labels=("Asset pricing", "Liquids")
    )
    assert [r.numbers[0].value for r in records] == [-4.0]


def test_annotation_records_keep_everything_when_no_bar_was_read():
    """A walk read that failed leaves no bar labels, and the callouts still stand."""
    raw = {"annotations": [{"bar": None, "label": "Asset pricing", "value": -5}]}
    assert len(annotation_records(raw, _Doc(), 63, 61, _ids(), "bps")) == 1


# ---------------------------------------------------------------------------
# Review round 2: the endpoint scale harmoniser is measured in the walk's unit
#
# The harmoniser fires when the bars do not reach the endpoints and one scale
# factor on the endpoints closes the gap. Its trigger was a flat 10, which is a
# quantity in BASIS POINTS: a ppt walk could never reach it, so the harmoniser
# was dead code there, and a $m walk accepted a residual of ten dollars-million
# as "the walk sums" — ten times the money tolerance.
# ---------------------------------------------------------------------------


class _WalkDoc(_Doc):
    doc_id = "CBA/FY26/profit_announcement"
    doc_type = "profit_announcement"

    def page_texts(self):
        return ["Cost to income ratio movement"]


def test_a_ratio_walk_reaches_the_endpoint_harmoniser():
    """The endpoints arrive as a fraction and the bars in points. A factor of
    100 closes the walk exactly; the old trigger never looked."""
    from bank_equity_researcher.tools.extract import extract_walk

    walk, _record = extract_walk(
        _LLM({
            "title": "CTI movement",
            "start_label": "FY25", "start_bps": 0.4570,
            "bars": [{"label": "Expense growth", "bps": -0.2}],
            "end_label": "FY26", "end_bps": 0.4550,
        }),
        "vision-model", _WalkDoc(), 1, "CBA cost to income", _ids(), unit="ppt",
    )
    assert walk.get("scale_adjusted") == "endpoints x100.0"
    assert round(walk["start_bps"], 2) == 45.70
    assert round(walk["end_bps"], 2) == 45.50


def test_a_walk_that_already_sums_is_left_alone():
    from bank_equity_researcher.tools.extract import extract_walk

    walk, _record = extract_walk(
        _LLM({
            "title": "CTI movement",
            "start_label": "FY25", "start_bps": 45.70,
            "bars": [{"label": "Expense growth", "bps": -0.2}],
            "end_label": "FY26", "end_bps": 45.50,
        }),
        "vision-model", _WalkDoc(), 1, "CBA cost to income", _ids(), unit="ppt",
    )
    assert "scale_adjusted" not in walk
