"""The output contract (ticket 06) with the never-guess gate (ticket 07):
a quantified claim without evidence references does not survive validation.
"""

from __future__ import annotations

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


class Contribution(BaseModel):
    value: float
    unit: str


class DriverClaim(BaseModel):
    canonical: str
    bank_label: str | None = None
    contribution: Contribution | None = None  # None = unquantified narrative driver
    narrative: str = ""
    confidence: int = Field(ge=0, le=100)
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
    headline: str = ""
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
