"""The output contract (ticket 06) with the never-guess gate (ticket 07):
a quantified claim without evidence references does not survive validation.
"""

from __future__ import annotations

import re
from enum import Enum

from pydantic import BaseModel, Field


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
    # How the page reached the evidence pool when retrieval did not rank it
    # there on its own: "reference_follow:<doc> p<source> -> <target>" for a
    # page the deterministic follower turned to (ticket 22). None means the
    # page came from the ordinary page budget.
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
    # An author reply that omits the field crashed a whole case mid-suite
    # (WBC impairment FY25, round-3 log). An unstated self-report is LOW
    # confidence, not a crash: 40 is the fatal-cap floor, so the claim can
    # never read as confident and the calibration table shows it honestly.
    confidence: int = Field(default=40, ge=0, le=100)
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
    # half-on-half one (defect 24).
    movement_source: str | None = None
    headline: str = ""
    # Evidence ids the HEADLINE's own statements rest on. A headline carries
    # facts that belong to no single driver — the movement as another document
    # states it, the statutory-versus-cash framing, the summary measures the
    # bank leads with — and until this list existed those facts had no citation
    # list at all. A reader checks a claim against the records the answer cites,
    # and so does the grounding judge, so a headline fact with no citation could
    # never be graded however well the pipeline had sourced it.
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
    no resolvable evidence reference. The strip is logged, never silent."""
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
            driver.confidence = min(driver.confidence, 20)
    return attribution


# A free-form answer carries key facts instead of driver claims, so the same
# structural rule needs a second shape to act on. Both shells that answer a
# question — the open-loop author and the closed-loop research agent — call
# this one function, so a question is gated exactly once however it was
# answered.
ANSWER_GATE_CONFIDENCE_CAP = 20


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
        if re.search(r"\d", fact) and not resolved:
            stripped.append(fact[:80])
            limitations.append(f'Stripped unsupported quantified fact: "{fact[:80]}"')
            continue
        kept.append({"fact": fact, "evidence": resolved})
    # The gate strips the FACT LIST. It does not touch the answer's prose,
    # because rewriting an answer to remove a number is a second authoring
    # pass, and this gate is deterministic by design. So the prose can still
    # state a number whose fact was just deleted, and a reader who reads only
    # the answer would never know. Say so, once, naming the claims.
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
