"""The attribution author: assembles the case context, calls the author model,
enforces the schema and the evidence gate, and runs the bounded
evidence-request loop (ticket 07)."""

from __future__ import annotations

import json

from .llm import LLM
from .schema import Attribution, EvidenceRecord, enforce_evidence_gate

AUTHOR_PROMPT = """You are a first-pass banking-sector equity research analyst.

TASK: explain how {bank}'s {metric_name} moved in {period} against {comparator},
attribute the movement to drivers, and rate your confidence.

THE CANONICAL DRIVER TAXONOMY for {metric_name} (use these canonical ids):
{taxonomy}

BANK VOCABULARY AND LABEL MAP (from the bank registry):
{registry}

SOURCE HIERARCHY when sources disagree: audited statements and Profit
Announcement tables > Profit Announcement narrative > presentation slides >
transcripts > else. Restated comparatives from the newer document win. Every
disagreement you notice must be reported with a reason:
definitional | rounding | restatement | timing | error.

EVIDENCE RECORDS (the only facts you may use; cite records by id):
{evidence}

WALK CHARTS EXTRACTED (already validated where possible):
{walks}

VALIDATION RESULTS so far: {validation}

ABSOLUTE RULES — never break these:
1. NEVER GUESS. Every number you state must come from an evidence record you
   cite. A quantified driver contribution without evidence ids will be deleted
   by the validator. If you do not know, say so in limitations.
2. State the basis (cash / statutory / ex_notables) and the comparator you use.
3. If cash and statutory movements differ materially, show both in the headline
   and record a disagreement with reason "definitional".
4. Confidence is 0-100: the probability the claim would be judged correct
   against the bank's own disclosure. 100 means certain — reserve >=90 for a
   bar backed by a walk whose sum check passed. Unquantified narrative drivers
   cap at 60.
5. Report a residual if quantified drivers do not sum to the movement. Never
   force numbers to fit.
6. PERIOD MATCH. The task is {period} vs {comparator}. Check every walk's
   endpoint labels: a walk describing a different comparison (e.g. the prior
   year's movement) is background context ONLY — never present its bars as this
   period's attribution. If no walk matches {period} vs {comparator}, say so in
   limitations and attribute only what period-matching evidence supports.
7. CORROBORATE. The validation results include a cross_source_view: the same
   drivers as seen by each document. Cite evidence from every document that
   supports a claim, not just one. When two documents frame the same movement
   differently (e.g. one folds hedging into a capital bar, the other splits
   it), note it in the driver narrative or as a disagreement. A claim seen in
   only one document must not exceed confidence 85.
8. WALK PREFERENCE. When more than one walk describes the SAME comparison,
   the results book's walk (profit announcement / results announcement) is
   the primary framing for your driver table — per the source hierarchy.
   Slide walks corroborate and annotate; where their framing differs, say so
   in a disagreement, but do not adopt the slide framing as primary.

Reply with JSON only, in this exact shape:
{{"movement": {{"from_value": float, "to_value": float, "delta": float, "unit": "{unit}"}},
  "basis": "cash|statutory|ex_notables",
  "headline": "<=120 words",
  "drivers": [{{"canonical": "<taxonomy id>", "bank_label": "<verbatim label or null>",
               "contribution": {{"value": float, "unit": "{unit}"}} | null,
               "narrative": "<=60 words", "confidence": int,
               "evidence": ["ev-1", ...]}}],
  "residual": {{"value": float, "unit": "{unit}"}} | null,
  "notable_items": ["..."],
  "disagreements": [{{"topic": str, "values": ["<value — source>", ...],
                     "preferred": str, "reason": "definitional|rounding|restatement|timing|error",
                     "explanation": str}}],
  "attribution_confidence": int,
  "limitations": ["..."]}}

If — and only if — one specific missing table or section blocks you, reply
instead with: {{"request_evidence": "<one retrieval query>"}} (you may do this
at most {rounds_left} more time(s))."""


def author_attribution(
    llm: LLM,
    model: str,
    *,
    max_tokens: int,
    case: dict,
    taxonomy: dict,
    registry: dict,
    evidence_records: list[EvidenceRecord],
    walks: list[dict],
    validation: dict,
    fetch_more,
    max_rounds: int = 2,
) -> Attribution:
    records = list(evidence_records)
    for round_no in range(max_rounds + 1):
        prompt = AUTHOR_PROMPT.format(
            bank=case["bank"],
            metric_name=taxonomy["name"],
            period=case["period"],
            comparator=case["comparator"],
            unit=taxonomy["unit"],
            taxonomy=json.dumps(taxonomy["drivers"], indent=1),
            registry=json.dumps(registry.get("measures", {}), indent=1)
            + "\n"
            + json.dumps(registry.get(f"{case['metric']}_walk_labels", registry.get("nim_walk_labels", {})), indent=1),
            evidence=json.dumps([r.model_dump() for r in records], indent=1),
            walks=json.dumps(walks, indent=1),
            validation=json.dumps(validation),
            rounds_left=max_rounds - round_no,
        )
        reply = llm.chat_json(model, prompt, max_tokens=max_tokens)
        if isinstance(reply, dict) and "request_evidence" in reply and round_no < max_rounds:
            new_records = fetch_more(reply["request_evidence"])
            records.extend(new_records)
            continue
        # Honest-partial sanitisation: a movement or contribution the model
        # could not establish arrives as nulls; that is a valid partial
        # answer (never-guess), not a schema violation.
        movement = reply.get("movement")
        if isinstance(movement, dict) and any(
            movement.get(k) is None for k in ("from_value", "to_value", "delta")
        ):
            movement = None
            reply.setdefault("limitations", []).append(
                "The movement could not be established from the evidence."
            )
        reply["movement"] = movement
        for driver in reply.get("drivers", []):
            contribution = driver.get("contribution")
            if isinstance(contribution, dict) and contribution.get("value") is None:
                driver["contribution"] = None
        attribution = Attribution(
            bank=case["bank"],
            metric=case["metric"],
            period=case["period"],
            comparator=case["comparator"],
            basis=reply.get("basis", "cash"),
            movement=reply.get("movement"),
            headline=reply.get("headline", ""),
            drivers=reply.get("drivers", []),
            residual=reply.get("residual"),
            notable_items=reply.get("notable_items", []),
            disagreements=reply.get("disagreements", []),
            attribution_confidence=int(reply.get("attribution_confidence", 0)),
            limitations=reply.get("limitations", []),
            evidence_records=records,
        )
        return enforce_evidence_gate(attribution)
    raise RuntimeError("author exceeded evidence-request rounds without answering")
