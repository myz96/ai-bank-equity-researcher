"""The output contract: the pydantic models an artifact is made of, and the
manifest doc-type vocabulary. The gates that enforce it live in gates.py.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field, field_validator

# The manifest doc_type vocabulary. Two consumers dispatch on these strings —
# printed-page mapping (extract.printed_page_of) and the walk-sum tolerance
# (validate.walk_sum_tolerance) — so a manifest value outside this set
# silently degrades both. That happened: the hand-built MQG manifest shipped
# "mda"/"presentation" and lost slide-page handling and the presentation walk
# tolerance. tests/test_corpus_scope.py holds every manifest to this set.
DOC_TYPES = frozenset({
    "asx_announcement",
    "investor_discussion_pack",
    "investor_presentation",
    "key_financial_information_xlsx",
    "pre_results_note",
    "profit_announcement",
    "results_announcement",
    "results_book",
    "results_presentation",
})

# The doc types whose pages are numbered by slide, and whose published walks
# earn the endpoint-rounding tolerance lift (WALK_SUM_TOL_PRESENTATION).
PRESENTATION_DOC_TYPES = ("results_presentation", "investor_presentation", "investor_discussion_pack")


class NumberFact(BaseModel):
    label: str
    value: float
    unit: str
    basis: str | None = None  # cash | statutory | ex_notables | n/a


class EvidenceRecord(BaseModel):
    id: str
    doc_id: str
    pdf_page: int
    printed_page: int | None = None
    kind: str = "text"  # text | table | walk_vision
    quote: str = Field(max_length=600)  # verbatim, <=50 words by prompt contract
    numbers: list[NumberFact] = []
    # The weaker test this quote matched its page under, when it did not match
    # the page's characters as printed (validation.quotes.MARKER_RELAXATION). None
    # means the strict test passed.
    provenance: str | None = None


class Contribution(BaseModel):
    value: float
    unit: str


class DriverClaim(BaseModel):
    canonical: str
    bank_label: str | None = None
    contribution: Contribution | None = None  # None = unquantified narrative driver
    # The two period COLUMNS this component delta was subtracted from, as the
    # bank prints them. A bridge component carries the same column trap as the
    # movement: the middle column of a three-column table is the prior half, so
    # subtracting it gives a half-on-half number, not the task's comparison.
    columns: str | None = None
    narrative: str = ""
    # An unstated self-report is LOW confidence, not a crash (an omitted field
    # once failed a whole case: WBC impairment FY25). 40 is the fatal-cap
    # floor, so such a claim can never read as confident. The validator covers
    # the other form of an unstated field, an explicit JSON null.
    confidence: int = Field(default=40, ge=0, le=100)
    evidence: list[str] = []
    checks_passed: list[str] = []
    checks_failed: list[str] = []

    @field_validator("confidence", mode="before")
    @classmethod
    def _null_confidence_is_low(cls, value):
        return 40 if value is None else value


class DisagreementReason(str, Enum):
    definitional = "definitional"
    rounding = "rounding"
    restatement = "restatement"
    timing = "timing"
    error = "error"


class Disagreement(BaseModel):
    topic: str
    values: list[str]  # each: "value — source/citation"
    preferred: str
    reason: DisagreementReason
    explanation: str


class Movement(BaseModel):
    from_value: float
    to_value: float
    delta: float
    unit: str


class Attribution(BaseModel):
    bank: str
    metric: str
    period: str
    comparator: str
    basis: str
    movement: Movement | None = None
    # Which document, row and period COLUMN each endpoint came from. Half-year
    # tables print three period columns, so naming the column is the only way
    # a reader can tell a prior-corresponding-period movement from a
    # half-on-half one.
    movement_source: str | None = None
    headline: str = ""
    # Evidence ids the HEADLINE's own statements rest on. A headline carries
    # facts that belong to no single driver — the movement as another document
    # states it, the statutory-versus-cash framing, the summary measures the
    # bank leads with. A reader checks a claim against the records the answer
    # cites, and so does the grounding judge, so a headline fact with no
    # citation can never be graded however well the answer sourced it.
    headline_evidence: list[str] = []
    drivers: list[DriverClaim] = []
    residual: Contribution | None = None
    notable_items: list[str] = []
    disagreements: list[Disagreement] = []
    attribution_confidence: int = Field(default=0, ge=0, le=100)
    limitations: list[str] = []
    evidence_records: list[EvidenceRecord] = []
    suggested_registry_patches: list[str] = []
    provenance: dict = {}
