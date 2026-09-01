"""The output contract with the never-guess gate: a quantified claim without
evidence references does not survive validation.
"""

from __future__ import annotations

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


import re
from enum import Enum

from pydantic import BaseModel, Field, field_validator


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

    @field_validator("confidence", mode="before")
    @classmethod
    def _null_confidence_is_low(cls, value):
        return 40 if value is None else value
    evidence: list[str] = []
    checks_passed: list[str] = []
    checks_failed: list[str] = []


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


def enforce_evidence_gate(attribution: Attribution) -> Attribution:
    """Structural never-guess rule: strip any quantified contribution that has
    no resolvable evidence reference. The strip is logged, never silent.

    The strip is a structural rule, not a confidence judgment. A companion
    confidence-20 override was deleted because a replay measured it firing on 0
    of the 90 saved attributions.
    """
    known_ids = {record.id for record in attribution.evidence_records}
    # The headline's citation list obeys the same structural rule: an id that
    # resolves to no record cites nothing, so it is dropped before a reader or
    # a judge can read it as grounding.
    attribution.headline_evidence = [
        e for e in dict.fromkeys(attribution.headline_evidence) if e in known_ids
    ]
    for driver in attribution.drivers:
        driver.evidence = [e for e in driver.evidence if e in known_ids]
        if driver.contribution is not None and not driver.evidence:
            attribution.limitations.append(
                f"Stripped unsupported quantified claim: {driver.canonical} "
                f"{driver.contribution.value}{driver.contribution.unit} had no evidence reference."
            )
            driver.contribution = None
    # A movement asserted with ZERO evidence records is a guess wearing a
    # number. The driver gate above cannot reach it (there is no contribution
    # to strip), so without this cap it shipped at 95 with only a peripheral
    # failed check (reproduced: a CTI submission, empty
    # evidence, confidence 95). The cap matches the question shell's
    # nothing-survived cap.
    if (attribution.movement is not None and not attribution.evidence_records
            and attribution.attribution_confidence > ANSWER_GATE_CONFIDENCE_CAP):
        attribution.attribution_confidence = ANSWER_GATE_CONFIDENCE_CAP
        # The drivers rest on the same absent evidence, so a narrative driver
        # must not keep rendering "confidence 95/100" under a capped answer.
        for driver in attribution.drivers:
            driver.confidence = min(driver.confidence, ANSWER_GATE_CONFIDENCE_CAP)
        attribution.limitations.append(
            "The movement cites no evidence records at all, so confidence is "
            f"capped at {ANSWER_GATE_CONFIDENCE_CAP}."
        )
    return attribution


# A free-form answer carries key facts instead of driver claims, so the same
# structural rule needs a second shape to act on. Every shell that answers a
# question calls this one function, so a question is gated exactly once.
ANSWER_GATE_CONFIDENCE_CAP = 20


# A quantity spelt in words is a quantity: "NIM fell three basis points"
# carries the same never-guess duty as "3 bps", and classifying on digits
# alone let it ship uncited at full confidence. A number word counts only beside a quantity noun, so a period
# name ("the first half") never trips it.
_NUMBER_WORDS = (
    "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    "thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|"
    "thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred"
)
_QUANTITY_RE = re.compile(
    rf"\d|\b(?:{_NUMBER_WORDS})\s+(?:basis[-\s]+points?|bps|per\s?cent|percent(?:age)?\s+points?|"
    rf"percent|ppt|points?|million|billion|dollars?)\b",
    re.IGNORECASE,
)


def enforce_answer_gate(
    key_facts: list, limitations: list[str], confidence: int, known_ids: set[str]
) -> tuple[list[dict], list[str], int]:
    """Strip every quantified key fact that cites no resolvable evidence.

    Returns the surviving facts, the limitations with each strip recorded, and
    the confidence, capped when nothing survived: an answer with no supported
    fact left is not an answer anyone should act on.
    """
    kept: list[dict] = []
    limitations = list(limitations)
    stripped: list[str] = []
    for item in key_facts or []:
        if not isinstance(item, dict):
            continue
        # "citations" is the tool-calling spelling and "evidence" the JSON
        # author's; the artifact stores one of them, so every reader (the
        # renderer, the scorer, the judge) sees one shape.
        cited = item.get("citations", item.get("evidence")) or []
        cited = [cited] if isinstance(cited, str) else list(cited)
        resolved = [str(e) for e in cited if str(e) in known_ids]
        fact = str(item.get("fact", ""))
        if _QUANTITY_RE.search(fact) and not resolved:
            stripped.append(fact[:80])
            limitations.append(f'Stripped unsupported quantified fact: "{fact[:80]}"')
            continue
        kept.append({"fact": fact, "evidence": resolved})
    # The gate strips the FACT LIST only. Rewriting the prose to remove a
    # number is a second authoring pass, and this gate is deterministic by
    # design. So the prose can still state a number whose fact was deleted, and
    # a reader who reads only the answer would never know.
    if stripped:
        limitations.append(
            f"{len(stripped)} unsupported quantified claim(s) were removed from the key "
            "facts, but the answer's prose was NOT rewritten and may still state those "
            "numbers: " + "; ".join(f'"{s}"' for s in stripped)
            + ". Treat any number above that carries no citation as unsupported."
        )
    if not kept:
        confidence = min(int(confidence or 0), ANSWER_GATE_CONFIDENCE_CAP)
    return kept, limitations, int(confidence or 0)
