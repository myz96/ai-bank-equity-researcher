"""The attribution author: assembles the case context, calls the author model,
enforces the schema and the evidence gate, and runs the bounded
evidence-request loop (ticket 07)."""

from __future__ import annotations

import json

from .llm import LLM
from .schema import Attribution, EvidenceRecord, enforce_evidence_gate
from .validate import (
    _percent_evidenced,
    movement_arithmetic_tolerance,
    normalize_unit,
)

AUTHOR_PROMPT = """You are a first-pass banking-sector equity research analyst.

TASK: explain how {bank}'s {metric_name} moved in {period} against {comparator},
attribute the movement to drivers, and rate your confidence.

PERIOD DEFINITIONS (computed from the bank's calendar in the registry):
{period_note}

THE CANONICAL DRIVER TAXONOMY for {metric_name} (use these canonical ids):
{taxonomy}

METHOD FOR THIS METRIC: {method_hint}

BANK VOCABULARY AND LABEL MAP (from the bank registry):
{registry}

HEADLINE ROW for {metric_name} at this bank (from the registry): {headline_row}

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
2. BASIS. "basis" names the basis of the numbers inside "movement" — nothing
   else. Use the bank's own primary reporting basis (the one BANK VOCABULARY
   calls its core measure, normally cash) unless the row you actually read is
   labelled statutory or ex-notable. A row that carries NO basis label takes
   the primary basis: never write "statutory" for an unlabelled row, and never
   write it because the figure comes from audited accounts. Naming a basis you
   did not read from is an error even when the numbers are right. Discuss the
   other basis in the headline; do not relabel your own movement.
   This rule tells you how to LABEL the row you read; it never licenses reading
   a non-primary row. A KPI page often prints the SAME row twice, once under a
   "statutory basis" block header and once under the primary-basis block a few
   lines away: take the PRIMARY-basis block, and quote the other as context.
3. If cash and statutory movements differ materially, show both in the headline
   and record a disagreement with reason "definitional".
4. Confidence is 0-100: the probability the claim would be judged correct
   against the bank's own disclosure. 100 means certain. Rate every driver on
   the evidence ladder, because how a number reached you bounds how sure you
   may be:
   - a bar you read from a walk of THIS comparison whose sum check passed: 90-95;
   - a movement the bank STATES in words or in a change column ("increased
     $62 million or 9%", "(3)bpts"): up to 90;
   - a delta YOU computed by subtracting two period levels: cap at 80. The
     arithmetic is yours, the framing is not the bank's, and a level pair can
     be on a different basis from the one the bank bridges;
   - an unquantified narrative driver: cap at 60.
5. Report a residual if quantified drivers do not sum to the movement. Never
   force numbers to fit.
6. PERIOD MATCH. Every walk below carries a code-computed "comparison" field.
   "primary" means its endpoints are exactly {comparator} -> {period}.
   "context" means it describes a DIFFERENT comparison, printed in
   "comparison_span" — most often the half-on-half movement. Build the driver
   table from the PRIMARY walks only. A "contribution" is a statement about
   {period} vs {comparator}, so a context walk's bar may NEVER become one: not
   as a value, not rounded, not re-signed. If no walk is primary, say so in
   limitations, quantify only what period-matching evidence (text, tables,
   footnotes) supports, and give the remaining drivers "contribution": null
   with the context walk's numbers INSIDE the narrative, naming the span they
   belong to (e.g. "the Jun 2025 -> Dec 2025 walk shows this at +106bpts").
   An unquantified but honest driver beats a borrowed number.
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
   NEVER MIX FRAMINGS. Every bar in your driver table comes from the ONE walk
   you adopt, at that walk's own value. A bar only the other document publishes
   is a disagreement or a limitation, never an extra driver; a value only the
   other document prints never replaces the adopted walk's value. A table that
   takes some bars from the book and some from a slide describes no published
   walk at all.
9. CLAIM THE WHOLE WALK. Claim every bar of the PRIMARY walk you adopt —
   including bars whose value is 0 and small +-1 bars. A published zero bar is
   the bank's explicit statement that the driver contributed nothing this
   period; leaving it unclaimed is a recall failure, not caution.
10. MOVEMENT COLUMN — mechanical, do this before anything else. A results
   table prints two or THREE period columns (see PERIOD DEFINITIONS above) and
   one or two comparison columns. Take to_value from the {period} column and
   from_value from the {comparator} column of the SAME row. Never take
   from_value from the prior-half column, and never read a movement out of a
   comparison column. Then record WHERE you read them in three SHORT fields:
   movement_row (the table row label), movement_from_column and
   movement_to_column (the two column headers as printed, e.g. 31 Dec 24 and
   31 Dec 25). Each is at most 12 words, a citation and nothing else: never
   put reasoning, arithmetic or alternatives in them. If a column header you
   name does not match the balance date in PERIOD DEFINITIONS, the movement is
   wrong — correct from_value and to_value, not the note. If a row shows only
   two period columns, check its header names the comparator before you use it.
   THE SAME DISCIPLINE BINDS EVERY COMPONENT of a bridge. A component's
   contribution is its {period} column minus its {comparator} column (or the
   movement the bank states against {comparator}) — never a difference
   involving the prior-half column, and never a single column's level. For
   every quantified driver, fill "columns" with the two column headers you
   subtracted (e.g. "31 Dec 24 -> 31 Dec 25"), or "stated vs {comparator}"
   when the bank prints the movement itself. At most 12 words, a citation
   only. If a component's columns do not match {comparator} -> {period},
   the contribution is a different comparison's number: recompute it from
   the right columns instead of relabelling it.
11. RATIO VARIANT. Use the bank's headline reported measure — the row named in
   HEADLINE ROW above — read from the results book's KPI or summary table.
   HEADLINE ROW names the measure this bank itself headlines, which is not
   always the one the task's metric name suggests: read that row even when a
   neighbouring row carries a plainer name. A row whose label merely resembles
   it is a DIFFERENT measure, and so is any named variant: Level 1 vs Level 2,
   internationally comparable, pro-forma, underlying, ex-notable, tangible
   versus ordinary equity, or a single division's ratio. Report a variant as
   context or as a disagreement; never let one supply the movement. When two
   candidate rows disagree, the source hierarchy decides: the results book's
   KPI table wins over a slide.
12. EXPLAIN, DO NOT RESTATE. A narrative that repeats its own number back
   ("a 5 bps negative contribution from asset pricing") tells a reader nothing
   the driver table already shows. Every driver needs a narrative, and each one
   must carry, from the evidence and no further:
   - the bank's stated reason, in the bank's own words;
   - every SUB-PART the bank names inside that driver, each WITH ITS OWN
     PRINTED NUMBER (a driver the bank splits into two named halves is reported
     as those two halves, not as the total alone);
   - the division, product or portfolio the bank points at.
   A sub-part must describe the SAME comparison as the driver it sits under.
   Rule 6 binds here too: never borrow a sub-split the bank published for a
   different span. Where the only sub-split covers another comparison, name
   that span beside the numbers.
   Carry the printed figures with every fact you mention — the movement, the
   growth rate and the level the bank prints, never the direction alone. The
   explanation belongs INSIDE the driver narratives, not only in the headline,
   and each figure is cited from that driver's own evidence list: that list is
   where a reader checks the claim. Some evidence records carry a "provenance"
   field starting "reference_follow": another page pointed at that page, so it
   holds the bank's own account of a line in the main tables — read those
   records for the explanation and cite them. A record whose "kind" is
   "walk_annotation" was read off the CALLOUT layer of a movement chart: it
   carries one named part of one bar with that part's own printed number, so
   report those parts inside that bar's driver narrative and cite them. One
   page can print two charts of the same metric, so rule 6 binds here as well:
   report each sub-part at the value printed on the chart you adopted, and name
   the span beside any sub-split that describes a different comparison.
   Where no record states a reason,
   write that the bank does not disclose one. Never supply a reason of your own.
13. CITE THE HEADLINE TOO. The headline states facts that belong to no single
   driver: the levels and growth rates the bank leads with, the movement on the
   other basis or framing printed beside it, a second document's figure for the
   same movement. List in "headline_evidence" the id of EVERY record those
   statements come from, and only records you read them from. Rule 1 binds
   here: a headline number with no record behind it is a guess, and a driver's
   own evidence list stays with that driver. Cite the record that PRINTS the
   figure you state. A record carrying only a table title or a bare row label
   says where the figure lives; it does not hold it, so it supports nothing.
14. SAY WHAT THE WALK HIDES. A bar is a net number and the bank often qualifies
   it: it calls a movement broadly revenue neutral or largely offset, points at
   another line that absorbs it, or reports a gross increase beside the
   decrease that funds it. When a record carries such a qualification, repeat
   the bank's OWN qualifying words inside that driver's narrative — not only
   the bar's size — and add the qualification to limitations when it changes
   what the movement means. A bar reported as a number alone, when the bank
   qualified it in words, overstates what the bar means.

UNITS: express from_value, to_value, delta, and every contribution ALL in
"{unit}". Convert percentages when the unit is bps (2.08% = 208; 12.3% = 1230;
a -3 bps move is from 208 to 205, delta -3) and quote ratio metrics in points
when the unit is ppt (45.7% -> 45.7, a 20 bpts improvement is delta -0.2).
When the unit is bps, a ratio printed as "12.2" in a percent column is 1220:
never leave an endpoint in percent while the delta is in bps. Never mix units
inside the movement object.

Reply with JSON only, in this exact shape. Inside a JSON string never type a
double-quote character: write a label plainly, or wrap it in single quotes.
{{"movement": {{"from_value": float, "to_value": float, "delta": float, "unit": "{unit}"}},
  "movement_row": "<table row label, <=12 words>",
  "movement_from_column": "<column header of {comparator}, <=12 words>",
  "movement_to_column": "<column header of {period}, <=12 words>",
  "basis": "cash|statutory|ex_notables",
  "headline": "<=180 words",
  "headline_evidence": ["ev-1", ...],
  "drivers": [{{"canonical": "<taxonomy id>", "bank_label": "<verbatim label or null>",
               "contribution": {{"value": float, "unit": "{unit}"}} | null,
               "columns": "<the two column headers subtracted, or stated vs {comparator}, or null>",
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


def _movement_source(reply: dict) -> str | None:
    """Compose the citation from three short fields.

    A single free-text field became a scratchpad: on the CBA 1H26 impairment
    case the model wrote 120 words of reasoning into it, concluded the right
    delta, and left the wrong numbers in "movement". Three capped fields leave
    no room to think, and their long labels no longer carry the nested
    double quotes that broke the JSON parse on both CTI cases.
    """
    parts = [str(reply.get(key) or "").strip()[:120] for key in
             ("movement_row", "movement_from_column", "movement_to_column")]
    row, from_column, to_column = parts
    if not any(parts):
        return None
    return f"row '{row or '?'}', column {from_column or '?'} -> column {to_column or '?'}"


_BASIS_WORDS = {
    "statutory": ("statutory",),
    "ex_notables": ("ex-notable", "ex notable", "excluding notable", "underlying"),
    "cash": ("cash",),
}


def primary_basis(registry: dict) -> str:
    """The bank's own headline basis, read from the registry vocabulary."""
    core = str(registry.get("measures", {}).get("core_profit", "")).lower()
    for basis, words in _BASIS_WORDS.items():
        if any(word in core for word in words):
            return basis
    return "cash"


def _basis_printed(basis: str, records: list[EvidenceRecord]) -> bool:
    """True when a page we read prints the basis word itself."""
    words = _BASIS_WORDS.get(basis, ())
    return any(word in record.quote.lower() for record in records for word in words)


def drop_off_unit_contributions(drivers: list[dict], unit: str) -> list[str]:
    """A contribution stated in another unit stops being a contribution.

    A contribution is a share of THIS movement, so it is stated in the
    movement's own unit. A value in another unit is a fact about something
    else: the CBA FY26 cash-earnings run claimed a -3 bps margin move as a
    component of a $m bridge, where the reconciliation summed it as -3 dollars.
    The number is not deleted — it stays in the narrative, where it belongs —
    but it stops being a quantified contribution, and the driver falls to the
    narrative cap.

    The closed-loop shell has guarded this since it was written and the
    open-loop author never did, so the same submission was corrected in one
    shell and shipped in the other. Both call this. Mutates; returns the notes.
    """
    dropped: list[str] = []
    for driver in drivers:
        if not isinstance(driver, dict):
            continue
        contribution = driver.get("contribution")
        if not isinstance(contribution, dict) or contribution.get("value") is None:
            continue
        given = str(contribution.get("unit") or unit).strip()
        if normalize_unit(given) == normalize_unit(unit):
            continue
        driver["contribution"] = None
        driver["confidence"] = min(int(driver.get("confidence") or 0), 60)
        dropped.append(
            f"{driver.get('canonical', '?')} was claimed as "
            f"{contribution.get('value')} {given}, which is not the movement's unit "
            f"({unit}); it is reported in the narrative and not as a contribution"
        )
    return dropped


def settle_charge_sign(movement: dict, taxonomy: dict, reply: dict) -> dict:
    """A charge metric states both endpoints as positive charge magnitudes.

    Banks print the impairment line inside the P&L, where an expense carries
    brackets. Westpac's FY25 row reads "Impairment (charges)/benefits (424) |
    (537)" and CBA's FY21 group summary reads "(554) | (2,518)"; both periods
    are charges, and the prose beside each table calls them "$424 million" and
    "$554 million". An author that carries the bracket through re-signs the
    whole movement, so a FALLING charge reports as a rise: Westpac FY25 came
    back as -537 -> -424, delta +113, where the charge fell by $113m.

    Only a pair of NEGATIVE endpoints is re-signed. Under the bracketed
    presentation a benefit prints positive, so a negative pair can only be two
    charges. A mixed pair is a charge in one period and a benefit in the other,
    and it keeps the signs the author read.
    """
    if taxonomy.get("sign_convention") != "positive_charge" or not isinstance(movement, dict):
        return movement
    frm, to = movement.get("from_value"), movement.get("to_value")
    if not (isinstance(frm, (int, float)) and isinstance(to, (int, float))):
        return movement
    if frm >= 0 or to >= 0:
        return movement
    movement["from_value"], movement["to_value"] = -frm, -to
    movement["delta"] = round(-to + frm, 2)
    reply.setdefault("limitations", []).append(
        f"Movement re-signed from ({frm:g}, {to:g}) to charge magnitudes: the row prints the "
        "charge inside the P&L, where an expense is bracketed. A charge is stated as a "
        "positive number, so a falling charge gives a negative delta."
    )
    return movement


def _settle_basis(basis: str, registry: dict, records: list[EvidenceRecord], reply: dict) -> str:
    """A declared basis must be a word the bank printed on a page we read.

    The extractor used to invent one: it tagged CBA's unlabelled Group NIM row
    "statutory", and the author faithfully repeated it, so a correct movement
    was scored wrong on its basis alone. When the claimed basis appears nowhere
    in the cited quotes, fall back to the bank's headline basis from the
    registry and record the substitution.
    """
    basis = str(basis or "").strip().lower() or "cash"
    primary = primary_basis(registry)
    if basis == primary or _basis_printed(basis, records):
        return basis
    reply.setdefault("limitations", []).append(
        f"Basis normalised from '{basis}' to '{primary}': no page in evidence prints "
        f"'{basis}' beside the movement, and the registry names {primary} as the bank's "
        "headline basis."
    )
    return primary


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
    period_note: str = "",
    headline_row: str | None = None,
    max_rounds: int = 2,
) -> Attribution:
    records = list(evidence_records)
    for round_no in range(max_rounds + 1):
        prompt = AUTHOR_PROMPT.format(
            bank=case["bank"],
            metric_name=taxonomy["name"],
            period=case["period"],
            comparator=case["comparator"],
            period_note=period_note,
            unit=taxonomy["unit"],
            taxonomy=json.dumps(taxonomy["drivers"], indent=1),
            method_hint=taxonomy.get("method_hint", "Follow the walk-first layered method."),
            registry=json.dumps(registry.get("measures", {}), indent=1)
            + "\n"
            + json.dumps(registry.get(f"{case['metric']}_walk_labels", registry.get("nim_walk_labels", {})), indent=1),
            headline_row=headline_row
            or (
                "the registry records no row for this metric — take the bank's own headline "
                "measure from the results book's KPI or performance-summary table"
            ),
            # "provenance" is dropped when it is empty, so an ordinary record
            # reads exactly as it did before reference-following existed.
            evidence=json.dumps(
                [
                    {
                        key: value
                        for key, value in record.model_dump().items()
                        if not (key == "provenance" and value is None)
                    }
                    for record in records
                ],
                indent=1,
            ),
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
        if isinstance(movement, dict) and taxonomy["unit"] == "bps":
            # Percent-endpoint lift: the model reads a ratio row printed in
            # percent ("12.3 | 12.3 | 12.2") and reports the endpoints as
            # printed while the delta follows the table's own "10 bpts"
            # column. Both endpoints must be evidenced as percentages before
            # the lift, so a bank whose margin really is under 100bps is not
            # multiplied by mistake.
            frm, to = movement.get("from_value"), movement.get("to_value")
            if (
                isinstance(frm, (int, float))
                and isinstance(to, (int, float))
                and max(abs(frm), abs(to)) < 100
                and _percent_evidenced(frm, records)
                and _percent_evidenced(to, records)
            ):
                movement["from_value"], movement["to_value"] = frm * 100, to * 100
                if abs(movement.get("delta", 0) - round((to - frm) * 100, 1)) > (
                    movement_arithmetic_tolerance(movement.get("unit"))
                ):
                    movement["delta"] = round((to - frm) * 100, 1)
                reply.setdefault("limitations", []).append(
                    f"Movement endpoints converted from percent ({frm}, {to}) to bps: the unit "
                    "for this metric is bps."
                )
        if isinstance(movement, dict):
            # Charge-sign normaliser: run before the delta harmoniser, so the
            # re-signed endpoints and their delta reach it already agreeing.
            movement = settle_charge_sign(movement, taxonomy, reply)
        if isinstance(movement, dict):
            # Delta harmoniser: endpoints are the primary facts; a delta that
            # contradicts them is a unit slip (e.g. "50 bpts" against ppt
            # endpoints). Recompute and record. The threshold is the one
            # check_movement uses, indexed by the movement's own unit: a flat
            # 0.51 is a basis-point quantity, so for a ppt movement the repair
            # stayed silent exactly where the check then failed at 0.1.
            implied = round(movement["to_value"] - movement["from_value"], 2)
            if (
                abs(movement["delta"] - implied)
                > movement_arithmetic_tolerance(movement.get("unit"))
                and implied != 0
            ):
                reply.setdefault("limitations", []).append(
                    f"Movement delta normalised from {movement['delta']} to {implied} "
                    "(unit slip against the endpoints)."
                )
                movement["delta"] = implied
        reply["movement"] = movement
        for driver in reply.get("drivers", []):
            contribution = driver.get("contribution")
            if isinstance(contribution, dict) and contribution.get("value") is None:
                driver["contribution"] = None
            # "columns" is a citation with a 12-word budget, like the three
            # movement fields: the cap leaves no room for it to become a
            # scratchpad.
            if driver.get("columns") is not None:
                driver["columns"] = str(driver["columns"]).strip()[:120] or None
        reply.setdefault("limitations", []).extend(
            drop_off_unit_contributions(reply.get("drivers", []), taxonomy["unit"])
        )
        attribution = Attribution(
            bank=case["bank"],
            metric=case["metric"],
            period=case["period"],
            comparator=case["comparator"],
            basis=_settle_basis(reply.get("basis", "cash"), registry, records, reply),
            movement=reply.get("movement"),
            movement_source=_movement_source(reply),
            headline=reply.get("headline", ""),
            headline_evidence=[
                str(e) for e in (reply.get("headline_evidence") or []) if isinstance(e, (str, int))
            ],
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
