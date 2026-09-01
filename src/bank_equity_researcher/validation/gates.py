"""The never-guess gates: the deterministic strips that hold an answer to its
evidence, and the confidence ceiling they apply when nothing survives.
"""

from __future__ import annotations

import re

from .schema import Attribution

# The nothing-supported confidence ceiling, shared by BOTH gates: the answer
# gate applies it when no kept fact is grounded, and the evidence gate when no
# resolved citation grounds a movement.
ANSWER_GATE_CONFIDENCE_CAP = 20


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
    return attribution



# A quantity spelt in words is a quantity: "NIM fell three basis points"
# carries the same never-guess duty as "3 bps", and classifying on digits
# alone let it ship uncited at full confidence. A number word counts only beside a quantity noun, so a period
# name ("the first half") never trips it.
_NUMBER_WORDS = (
    "zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    "thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|"
    "thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred"
)
_QUANTITY_RE = re.compile(
    # A digit is a quantity when it looks like one: a decimal or thousands
    # separator, three or more digits, or a unit/currency beside it. A bare
    # one- or two-digit token can be a LABEL INDEX ("Tier 1 capital", "Stage
    # 3"), and stripping the qualitative sentence it sits in punishes prose
    # that claims no number. The trade accepted: "rose by 5" alone escapes.
    rf"\d+[.,]\d|\d{{3,}}|\$\s*\d|\d+\s*(?:%|bps|bp\b|ppt|per\s?cent|percent|basis|million|billion|bn\b|m\b)|"
    rf"\b(?:{_NUMBER_WORDS})\s+(?:basis[-\s]+points?|bps|per\s?cent|percent(?:age)?\s+points?|"
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
    if not any(fact["evidence"] for fact in kept):
        # Kept facts with no resolved citation are prose the gate cannot call
        # quantified; an answer whose every fact is ungrounded is still an
        # answer with nothing supported ("Outlook remained resilient" at 95).
        confidence = min(int(confidence or 0), ANSWER_GATE_CONFIDENCE_CAP)
    return kept, limitations, int(confidence or 0)
