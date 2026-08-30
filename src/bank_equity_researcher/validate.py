"""Deterministic validation checks and their tolerances (tickets 01, 05),
plus the deterministic comparison classifier (defect 24).

Every constant carries the reason it has that value.
"""

from __future__ import annotations

import re

# Profit Announcement walks label bars to two decimals of a percent (0.01% =
# 1bp), so extraction should be exact; +-0.5bp absorbs float noise only.
WALK_BAR_TOL_PA = 0.5
# PA walk bars are exact, so their sum should reconcile within rounding of the
# endpoints (each endpoint rounded to 1bp): 1bp.
WALK_SUM_TOL_PA = 1.0
# Presentation walks round endpoints coarsely (CET1 slides round to 0.1% =
# 10bps; CBA FY26 slide 32 bars sum to -24 vs a -30 headline and the slide
# footnotes the rounding). Tolerance = one endpoint rounding step.
WALK_SUM_TOL_PRESENTATION = 10.0
# Money figures: banks round to $m; 1% or $10m (whichever larger) absorbs
# re-presented comparatives without letting real errors through.
MONEY_REL_TOL = 0.01
MONEY_ABS_TOL_M = 10.0
# Ratio metrics quoted to one decimal of a percent.
RATIO_TOL_PPT = 0.1
# Two documents quoting the same driver agree if within this (covers 1bp
# rounding on each side, e.g. PA "Liquids -3" vs slide "Liquids & repos (4)"
# is a framing gap, not agreement). Beyond it, the gap is surfaced as a
# disagreement, never averaged away.
CORROBORATION_TOL = 1.5
# A claim "matches" a walk bar when it repeats it: bars are printed exactly, so
# the match is tight. Used by the comparison-leak check, never by corroboration.
LEAK_TOL = {"bps": 0.5, "$m": 10.0, "ppt": 0.1}
# Component deltas subtract two integer $m table cells, so a repeat is exact;
# 2.0 absorbs a restated comparative. LEAK_TOL's 10.0 is for movement LEVELS —
# at component scale it let one component's half-on-half delta hide behind a
# neighbouring component's nearby PCP delta.
COMPONENT_TOL = 2.0

# --------------------------------------------------------------------------
# Unit-typed tolerances
#
# A tolerance means nothing without the unit it is stated in. Every constant
# above was calibrated in BASIS POINTS, and the checks below applied them to
# whatever unit the answer happened to use: 1.0 is a rounding step in bps and
# five times the whole movement in percentage points. The shipped CBA FY26
# cost-to-income artifact carried drivers summing to 0.0 ppt against a -0.2 ppt
# movement and passed drivers_reconcile, because the movement it claimed to
# explain was smaller than the slack it was measured with.
#
# One table per QUESTION the checks ask, because the two questions have
# different answers:
#
#   RECONCILE_TOL - do these parts sum to that whole? Endpoint rounding on
#   each side, so one print step of the unit.
#   CITATION_TOL - does this record print that number? A repeat is exact, so
#   this one is always tighter.
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# One spelling per unit
#
# A tolerance table is a dict keyed by a unit STRING, so "PPT" and "bpts" and
# "$ m" missed every entry and took the default: a ppt movement measured with
# the 1.0 reconciliation slack is measured with five times its own size. The
# scorer already canonicalised aliases and the checks did not, so the two
# disagreed about the same answer. The vocabulary lives here, beside the
# tolerances it keys, and evals imports it (the reverse import is a cycle).
# --------------------------------------------------------------------------

UNIT_ALIASES = {
    "bps": "bps", "bp": "bps", "bpt": "bps", "bpts": "bps", "basis": "bps",
    "$m": "$m", "$": "$m", "m": "$m", "$millions": "$m", "$million": "$m",
    "aud$m": "$m", "a$m": "$m",
    "$bn": "$bn", "$b": "$bn", "bn": "$bn", "b": "$bn", "$billion": "$bn",
    "$billions": "$bn",
    "ppt": "ppt", "ppts": "ppt", "pp": "ppt", "pt": "ppt", "pts": "ppt",
    "%": "%", "pct": "%", "percent": "%",
    "ratio": "ratio",
    "cents": "cents", "cent": "cents", "cps": "cents", "c": "cents",
}


# The ratio family: a level or a movement in any of these units is a ratio's.
# This estate stores a ratio as printed, so a CET1 rise of 4bps is 0.04 in all
# three spellings.
RATIO_UNITS = ("ppt", "%", "ratio")


def normalize_unit(unit: str | None) -> str:
    """'bps of average GLAA' -> 'bps'; '$ m' -> '$m'; 'PPT' -> 'ppt'; None -> ''."""
    if not unit:
        return ""
    token = str(unit).strip().lower().split(" ")[0]
    return UNIT_ALIASES.get(token, token)


def _tolerance_for(table: dict[str, float], unit: str | None, default: float) -> float:
    """One tolerance lookup, on the unit's canonical spelling."""
    return table.get(normalize_unit(unit), default)


# How a number printed in one unit restates itself in another. The key is
# (claim unit, grounding unit); a pair the table does not hold cannot ground the
# claim at all. Every factor is stated in the direction "multiply the grounding
# number by this to read it in the claim's unit".
#
#   ppt, % and ratio are one family: this estate stores a ratio movement as
#   printed (a CET1 rise of 4bps is 0.04 ratio, 0.04 ppt or 0.04%).
#   bps is that family divided by 100: a -20 bps fact grounds -0.2 ppt, and
#   never -20 ppt.
#   Money and ratios never ground each other, whatever their magnitudes: the
#   0.0 $m cell of a dollar row grounded a 0.0 ppt claim at confidence 90.
UNIT_CONVERSIONS: dict[tuple[str, str], float] = {}
for _claim in ("ppt", "%", "ratio"):
    for _source in ("ppt", "%", "ratio"):
        UNIT_CONVERSIONS[(_claim, _source)] = 1.0
    UNIT_CONVERSIONS[(_claim, "bps")] = 0.01
    UNIT_CONVERSIONS[("bps", _claim)] = 100.0
UNIT_CONVERSIONS[("bps", "bps")] = 1.0
UNIT_CONVERSIONS[("$m", "$m")] = 1.0
UNIT_CONVERSIONS[("$m", "$bn")] = 1000.0
UNIT_CONVERSIONS[("$bn", "$bn")] = 1.0
UNIT_CONVERSIONS[("$bn", "$m")] = 0.001
UNIT_CONVERSIONS[("cents", "cents")] = 1.0
del _claim, _source


def convert_unit(value: float, source_unit: str | None, claim_unit: str | None) -> float | None:
    """`value`, printed in source_unit, restated in claim_unit.

    None means the two units cannot ground each other — including the case
    where either unit is missing, because a number with no unit is no evidence
    either way.
    """
    source, claim = normalize_unit(source_unit), normalize_unit(claim_unit)
    if not source or not claim:
        return None
    factor = UNIT_CONVERSIONS.get((claim, source))
    return None if factor is None else value * factor


RECONCILE_TOL = {"bps": WALK_SUM_TOL_PA, "ppt": RATIO_TOL_PPT, "%": RATIO_TOL_PPT, "$m": 1.0}
RECONCILE_TOL_DEFAULT = 1.0
# The endpoint-rounding lift a presentation walk earns (WALK_SUM_TOL_PRESENTATION)
# is a quantity in BASIS POINTS: the slide rounds a ratio to 0.1% and the metric
# is stated in bps there. The same slide prints a ppt ratio to 0.1 ppt and a
# dollar figure to the million, so neither unit earns the lift. Granting it to
# them made 10.0 the slack on a movement of 0.2.
PRESENTATION_LIFT_UNITS = ("bps",)
# Self-consistency of the three numbers the author states for one movement
# (from + delta == to). All three are printed at the unit's own precision.
MOVEMENT_ARITHMETIC_TOL = {"bps": 0.51, "ppt": RATIO_TOL_PPT, "%": RATIO_TOL_PPT, "$m": 0.51}
MOVEMENT_ARITHMETIC_TOL_DEFAULT = 0.51
# "This record prints that number." Bars and table cells are printed exactly,
# so the match is tight in every unit; only the ratio units move, and they move
# tighter.
CITATION_TOL = {"bps": 0.5, "ppt": RATIO_TOL_PPT, "%": RATIO_TOL_PPT, "$m": 0.5}
CITATION_TOL_DEFAULT = 0.5


# --------------------------------------------------------------------------
# Comparison classification (defect 24)
#
# One results event publishes several walks: the period-on-period walk, the
# half-on-half walk, and sometimes the prior year's walk. Pooling their bars
# makes different comparisons look like disagreeing sources, and lets the
# half-on-half bars leak into a full-year driver table. Classification is
# deterministic: resolve each walk's printed endpoint LABELS to a balance date
# through the bank's registry calendar, then compare the pair against the
# case's own two balance dates.
#
# Chart TITLES are deliberately ignored. The vision reader is given the case
# description, and it echoes it into the title ("CBA CET1 ratio in FY21 vs
# FY20" sat on a half-on-half chart), so a title is not evidence of the
# comparison. Endpoint labels are read off the chart itself.
# --------------------------------------------------------------------------

MONTH_NUMBERS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}
_MONTH_ALTERNATION = (
    r"jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|"
    r"aug(?:ust)?|sep(?:t|tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?"
)
# "Jun 25 Level 2", "Dec 24 Half", "30 June 2021", "Mar-26". The word boundary
# after the month name stops "margin" matching "mar".
_MONTH_LABEL_RE = re.compile(rf"\b({_MONTH_ALTERNATION})\b\.?[\s\-']*(\d{{4}}|\d{{2}})\b", re.IGNORECASE)
# "FY25", "1H26", "2H25 Cash net interest margin".
_TAG_LABEL_RE = re.compile(r"\b(FY|1H|2H)\s?(\d{4}|\d{2})\b", re.IGNORECASE)
# An endpoint labelled pro-forma is a hypothetical, not the reported value.
_PRO_FORMA_RE = re.compile(r"pro[\s\-]?forma", re.IGNORECASE)


def _calendar_month(text: str) -> int | None:
    """'30 June' or 'ends 31 December' -> the month number."""
    match = re.search(rf"\b({_MONTH_ALTERNATION})\b", text or "", re.IGNORECASE)
    return MONTH_NUMBERS[match.group(1).lower()[:3]] if match else None


def _four_digit(year: int) -> int:
    return year + 2000 if year < 100 else year


def period_end_date(period: str, calendar: dict) -> tuple[int, int] | None:
    """Balance date (month, year) of a period label such as FY26, 1H26, 2H25.

    The bank's own calendar decides it. CBA's financial year ends in June, so
    1H26 is the half ended December 2025; NAB, WBC and ANZ end in September,
    so their 1H26 is the half ended March 2026. A half whose end month falls
    after the financial year end belongs to the previous calendar year.
    """
    match = re.fullmatch(r"\s*(FY|1H|2H)\s?(\d{4}|\d{2})\s*", period or "", re.IGNORECASE)
    fy_month = _calendar_month(calendar.get("fy_end", ""))
    if not match or fy_month is None:
        return None
    tag, year = match.group(1).upper(), _four_digit(int(match.group(2)))
    if tag == "FY":
        return (fy_month, year)
    half_month = _calendar_month(calendar.get("halves", {}).get(tag, ""))
    if half_month is None:
        return None
    return (half_month, year - 1 if half_month > fy_month else year)


def label_end_date(label: str | None, calendar: dict) -> tuple[int, int] | None:
    """Balance date named by a walk endpoint label, or None if it names none."""
    if not label:
        return None
    match = _MONTH_LABEL_RE.search(label)
    if match:
        return (MONTH_NUMBERS[match.group(1).lower()[:3]], _four_digit(int(match.group(2))))
    match = _TAG_LABEL_RE.search(label)
    if match:
        return period_end_date(f"{match.group(1).upper()}{match.group(2)}", calendar)
    return None


def _span_text(start: tuple[int, int] | None, end: tuple[int, int] | None) -> str:
    def one(date):
        if date is None:
            return "?"
        month = next(k for k, v in MONTH_NUMBERS.items() if v == date[0]).capitalize()
        return f"{month} {date[1]}"

    return f"{one(start)} -> {one(end)}"


def annotate_walks(walks: list[dict], calendar: dict, period: str, comparator: str) -> None:
    """Stamp every walk with the comparison it describes (in place).

    walk["comparison"] is "primary" when the walk runs from the comparator's
    balance date to the period's balance date, "context" when it runs between
    any other pair, and "unclassified" when the labels name no period at all.
    """
    want = (period_end_date(comparator, calendar), period_end_date(period, calendar))
    for walk in walks:
        start = label_end_date(walk.get("start_label"), calendar)
        end = label_end_date(walk.get("end_label"), calendar)
        # A pro-forma endpoint is a hypothetical, so the walk's bars add up to
        # a figure the bank never reported: CBA's FY21 slide bridges Jun 20 to
        # a Jun 21 pro-forma that already subtracts a buy-back announced after
        # balance date. The dates match the task, the movement does not, so
        # such a walk is context however its endpoints are labelled.
        pro_forma = [
            key for key in ("start_label", "end_label")
            if _PRO_FORMA_RE.search(str(walk.get(key) or ""))
        ]
        walk["comparison_span"] = _span_text(start, end)
        if start is None or end is None:
            walk["comparison"] = "unclassified"
            walk["comparison_note"] = (
                "The endpoint labels name no period, so this walk's comparison is unknown. "
                "Treat it as context unless its endpoints match the task."
            )
        elif want[0] is not None and (start, end) == want and not pro_forma:
            walk["comparison"] = "primary"
            walk["comparison_note"] = f"This walk IS the task comparison ({comparator} -> {period})."
        elif pro_forma:
            walk["comparison"] = "context"
            walk["comparison_note"] = (
                f"CONTEXT ONLY: the {', '.join(k.split('_')[0] for k in pro_forma)} endpoint of "
                "this walk is PRO-FORMA - a hypothetical adjusted figure, not the reported "
                "ratio. Its bars therefore sum to a figure the bank never reported. Never use "
                "them as contributions and never use its endpoints as the movement."
            )
        else:
            walk["comparison"] = "context"
            walk["comparison_note"] = (
                f"CONTEXT ONLY: this walk runs {walk['comparison_span']}, which is NOT the task "
                f"comparison ({comparator} -> {period}). Never present its bars as this "
                "period's driver contributions."
            )
        if pro_forma:
            walk["endpoints_reported"] = False


def walks_for_view(walks: list[dict]) -> tuple[list[dict], str]:
    """The one comparison group whose bars corroborate each other (defect 24).

    Primary walks when the bank published one for the case comparison. When it
    published none, the largest single other-comparison group: two walks of the
    SAME other comparison still corroborate each other (CBA publishes only a
    half-on-half CET1 walk, whatever the reporting period), and dropping them
    would leave the author with no decomposition at all.
    """
    primary = [w for w in walks if w.get("comparison") == "primary"]
    if primary:
        return primary, f"PRIMARY - the task comparison ({primary[0].get('comparison_span')})"
    groups: dict[str, list[dict]] = {}
    for walk in walks:
        groups.setdefault(walk.get("comparison_span", "?"), []).append(walk)
    if not groups:
        return [], "no walks extracted"
    span, group = max(groups.items(), key=lambda item: len(item[1]))
    return group, (
        f"CONTEXT - the bank published no walk for the task comparison; these walks "
        f"describe {span}"
    )


def walk_sum_tolerance(doc_type: str, unit: str = "bps") -> float:
    """Slack for "these bars sum to that endpoint gap", in the walk's own unit.

    The presentation lift is a bps quantity, so a ppt or $m walk keeps the
    ratio or money tolerance however the walk was published. Before the unit
    entered here a ppt walk was measured against 1.0 or 10.0, and no such walk
    could fail its own sum check.
    """
    if normalize_unit(unit) in PRESENTATION_LIFT_UNITS and doc_type in (
        "results_presentation", "investor_discussion_pack", "investor_presentation"
    ):
        return WALK_SUM_TOL_PRESENTATION
    return _tolerance_for(RECONCILE_TOL, unit, RECONCILE_TOL_DEFAULT)


def check_walk(walk: dict, doc_type: str, unit: str = "bps") -> tuple[list[str], list[str]]:
    """walk: {start_bps, bars: [{label, bps}], end_bps}. Returns (passed, failed).

    The dict keys say bps for history; the values carry the METRIC's unit, so
    the caller passes it in.
    """
    passed, failed = [], []
    tolerance = walk_sum_tolerance(doc_type, unit)
    total = walk["start_bps"] + sum(b["bps"] for b in walk["bars"])
    if abs(total - walk["end_bps"]) <= tolerance:
        passed.append("walk_sum")
    else:
        failed.append(
            f"walk_sum (start {walk['start_bps']} + bars {sum(b['bps'] for b in walk['bars']):+.1f} "
            f"= {total:.1f} != end {walk['end_bps']}, tol {tolerance} {unit})"
        )
    return passed, failed


def movement_arithmetic_tolerance(unit: str | None) -> float:
    """Slack for "from + delta == to", in the movement's own unit.

    check_movement reads it, and so do the two delta harmonisers that REPAIR a
    delta before any check sees it. They used to carry a hard-coded 0.51, which
    is a basis-point quantity: a ppt movement whose delta was out by 0.5 was
    left alone by the repair and then failed the 0.1 ppt check, so a repairable
    one-line slip sank the answer to confidence 40 instead of being corrected.
    """
    return _tolerance_for(MOVEMENT_ARITHMETIC_TOL, unit, MOVEMENT_ARITHMETIC_TOL_DEFAULT)


def check_movement(movement) -> tuple[list[str], list[str]]:
    passed, failed = [], []
    if movement is None:
        return passed, ["movement_missing"]
    tolerance = movement_arithmetic_tolerance(movement.unit)
    if abs(movement.from_value + movement.delta - movement.to_value) <= tolerance:
        passed.append("movement_arithmetic")
    else:
        failed.append(
            f"movement_arithmetic ({movement.from_value} + {movement.delta} != {movement.to_value}, "
            f"tol {tolerance} {movement.unit})"
        )
    return passed, failed


def _normalize_label(label: str) -> str:
    return "".join(ch for ch in label.lower() if ch.isalnum())


# Filler words that a bank drops or adds between documents for the same bar
# ("Capital, Replicating & Other" on one page, "Capital, Replicating and Other"
# on the next). They must not decide a mapping.
_LABEL_FILLERS = {"and", "the", "of", "incl", "including", "other", "cost", "costs"}


def _label_tokens(label: str) -> frozenset[str]:
    words = re.split(r"[^a-z0-9]+", label.lower())
    return frozenset(w for w in words if w and w not in _LABEL_FILLERS)


def canonical_for(label: str, normalized_map: dict[str, str], token_map=None) -> str:
    """Map one verbatim bar label to a canonical driver id.

    Three passes, most exact first: the registry's normalised label, substring
    containment either way, then a token match that ignores filler words. The
    token pass exists because the same bar is printed with small wording
    differences across documents, and a mapping miss silently costs the bar its
    corroboration and its comparison check.
    """
    norm = _normalize_label(label)
    if norm in normalized_map:
        return normalized_map[norm]
    hit = next((c for k, c in normalized_map.items() if k and (k in norm or norm in k)), None)
    if hit:
        return hit
    tokens = _label_tokens(label)
    best, best_size = None, 0
    for key_tokens, canonical in (token_map or {}).items():
        if not key_tokens or not tokens:
            continue
        if (key_tokens <= tokens or tokens <= key_tokens) and len(key_tokens & tokens) > best_size:
            best, best_size = canonical, len(key_tokens & tokens)
    return best or "other_unmapped"


def cross_source_view(walks: list[dict], label_map: dict[str, str]) -> dict[str, list[dict]]:
    """canonical driver -> [{source, label, value}] over the walks given.

    Callers pass walks of ONE comparison (defect 24): corroboration and
    disagreement only mean something between documents describing the same
    movement. Labels map to canonical ids via the registry's label map.
    """
    normalized_map = {_normalize_label(k): v for k, v in label_map.items()}
    token_map = {_label_tokens(k): v for k, v in label_map.items()}
    view: dict[str, list[dict]] = {}
    for walk in walks:
        for bar in walk.get("bars", []):
            canonical = canonical_for(str(bar.get("label", "")), normalized_map, token_map)
            view.setdefault(canonical, []).append(
                {"source": walk.get("source", "?"), "label": bar.get("label"), "value": float(bar.get("bps", 0))}
            )
    return view


def corroborate(attribution, cross_source: dict[str, list[dict]]) -> None:
    """Annotate each quantified driver with its corroboration status; surface
    cross-source divergence as a disagreement; cap single-source confidence.
    Mutates the attribution in place."""
    from .schema import Disagreement, DisagreementReason

    for driver in attribution.drivers:
        if driver.contribution is None:
            continue
        entries = cross_source.get(driver.canonical, [])
        cited_docs = {
            r.doc_id for r in attribution.evidence_records if r.id in driver.evidence
        }
        walk_docs = {e["source"].split(" PDF")[0] for e in entries}
        n_sources = len(cited_docs | walk_docs)
        if len(entries) >= 2 and len(walk_docs) >= 2:
            values = [e["value"] for e in entries]
            if max(values) - min(values) <= CORROBORATION_TOL:
                driver.checks_passed.append(f"corroborated_{len(walk_docs)}_sources")
            else:
                driver.checks_passed.append("cross_source_divergence_surfaced")
                gap = max(values) - min(values)
                attribution.disagreements.append(
                    Disagreement(
                        topic=f"{driver.canonical} contribution",
                        values=[f"{e['value']:+g} — {e['label']} ({e['source']})" for e in entries],
                        preferred=f"{driver.contribution.value:+g} (per the source hierarchy)",
                        reason=DisagreementReason.rounding if gap <= 3 else DisagreementReason.definitional,
                        explanation="The documents decompose the same movement with different bar framings; "
                        "the gap is framing/rounding, not a data conflict."
                        if gap <= 3
                        else "The documents use different decompositions of the same movement.",
                    )
                )
        elif n_sources <= 1:
            # Corroboration dimension (user, 2026-08-26): a quantified claim
            # seen in only one document cannot claim near-certainty.
            driver.checks_passed.append("single_source")
            driver.confidence = min(driver.confidence, 85)


def check_comparison_leak(
    attribution, primary_view: dict[str, list[dict]], context_view: dict[str, list[dict]]
) -> tuple[list[str], list[str]]:
    """Defect 24: a quantified driver must not carry another comparison's bar.

    The check fires on the exact symptom, not on a suspicion: the claimed value
    repeats a bar from a walk of a DIFFERENT comparison, and no bar of the
    task's own walk gives that value for the same canonical driver. A claim
    that agrees with both comparisons is not a leak. A quantified contribution
    is a statement about THIS comparison, so a bar borrowed from another one is
    a leak whether or not the bank published a walk for the task — where it did
    not, the other comparison's numbers belong in the driver narrative.
    """
    passed, failed = [], []
    for driver in attribution.drivers:
        if driver.contribution is None:
            continue
        tol = _tolerance_for(LEAK_TOL, driver.contribution.unit, 0.5)
        value = driver.contribution.value
        primary_bars = [e["value"] for e in primary_view.get(driver.canonical, [])]
        context_bars = [e for e in context_view.get(driver.canonical, []) if abs(e["value"] - value) <= tol]
        if not context_bars:
            continue
        if any(abs(bar - value) <= tol for bar in primary_bars):
            continue
        reference = (
            f"the task-comparison walk shows {', '.join(f'{b:+g}' for b in primary_bars)}"
            if primary_bars
            else "no walk covers the task comparison, so this bar cannot be a contribution for "
            "it — move the number into the driver narrative and name the span it belongs to"
        )
        failed.append(
            f"comparison_leak ({driver.canonical} claims {value:+g}, which is the "
            f"'{context_bars[0]['label']}' bar of {context_bars[0]['source']}, a walk for a "
            f"different comparison; {reference})"
        )
    if not failed:
        passed.append("no_comparison_leak")
    return passed, failed


def _date_tokens(date: tuple[int, int] | None) -> set[str]:
    """Normalised spellings a table column header uses for one balance date:
    'Dec 24', '31 Dec 24', 'December 2024', 'Dec-24'."""
    if date is None:
        return set()
    month = next(k for k, v in MONTH_NUMBERS.items() if v == date[0])
    full = {"jan": "january", "feb": "february", "mar": "march", "apr": "april",
            "may": "may", "jun": "june", "jul": "july", "aug": "august",
            "sep": "september", "oct": "october", "nov": "november", "dec": "december"}[month]
    year2, year4 = str(date[1])[2:], str(date[1])
    return {f"{m}{y}" for m in (month, full) for y in (year2, year4)}


def check_movement_columns(
    attribution, period_date, comparator_date, prior_half_date
) -> tuple[list[str], list[str]]:
    """The movement's from_value must not be the PRIOR HALF's column.

    Half-year and full-year books print three period columns, and the middle
    one is the trap (defect 24). The check reads the extracted evidence, not
    the model's own note: it groups every extracted number by the balance date
    its label names, then fires only when from_value is a prior-half figure and
    is not a comparator figure. It stays silent unless both groups exist, so a
    page whose columns were never labelled cannot trigger it.
    """
    passed, failed = [], []
    movement = attribution.movement
    if movement is None:
        return passed, failed
    wanted, prior = _date_tokens(comparator_date), _date_tokens(prior_half_date)
    current = _date_tokens(period_date)
    if not wanted or not prior or wanted & prior:
        return passed, failed

    def dated(tokens: set[str], others: list[set[str]]) -> list[float]:
        values = []
        for record in attribution.evidence_records:
            for number in record.numbers:
                label = _normalize_label(number.label)
                if any(t in label for t in tokens) and not any(
                    t in label for group in others for t in group
                ):
                    values.append(number.value)
        return values

    comparator_values = dated(wanted, [prior, current])
    prior_values = dated(prior, [wanted, current])
    if not comparator_values or not prior_values:
        return passed, failed
    tolerance = _tolerance_for(LEAK_TOL, movement.unit, 0.5)

    def seen(value: float, pool: list[float]) -> bool:
        # Evidence keeps percentages as printed (2.08) while a bps movement
        # carries 208, so accept either scale.
        return any(abs(v - value) <= tolerance or abs(v * 100 - value) <= tolerance for v in pool)

    if seen(movement.from_value, prior_values) and not seen(movement.from_value, comparator_values):
        failed.append(
            f"movement_from_prior_half (from_value {movement.from_value:g} appears in the "
            "evidence only against the PRIOR HALF's column, never against the comparator's; "
            "this is a half-on-half movement, not the movement the task asks for)"
        )
    else:
        passed.append("movement_from_comparator_column")
    return passed, failed


def _period_tokens(label: str | None, date: tuple[int, int] | None) -> set[str]:
    """Every spelling a column header uses for one task period.

    Two families: the balance date ("31 Dec 24", "December 2024") and the
    period tag a bank prints above a full-year column ("FY25"). A bridge table
    uses either, so both must group to the same period.
    """
    tokens = _date_tokens(date)
    tag = _normalize_label(label or "")
    if tag:
        tokens.add(tag)
    return tokens


def half_label(date: tuple[int, int] | None, calendar: dict) -> str | None:
    """The bank's own tag for a half's balance date: (6, 2025) -> '2H25' at CBA.

    Tables label the prior-half column either by its date ("30 Jun 25") or by
    its tag ("2H25"), and a slide usually prefers the tag.
    """
    if date is None:
        return None
    for tag in ("1H", "2H"):
        for year in (date[1], date[1] + 1):
            if period_end_date(f"{tag}{year}", calendar) == date:
                return f"{tag}{str(year)[2:]}"
    return None


# The day of the month printed in front of a column header ("31 Dec 25",
# "30 Jun 25"). It belongs to the date, not to the row, so it comes off with
# the date: otherwise the same row's December and June columns end as two
# different stems and no delta can be formed between them.
_LEADING_DAY_RE = re.compile(r"\d{1,2}$")


def _stems_by_period(
    records, groups: dict[str, set[str]], unit: str
) -> dict[str, dict[str, set[float]]]:
    """row stem -> period -> the values the evidence prints for that column.

    A number's label names its own period column; the rest of the label is the
    ROW it was read from. Strip the period out and two columns of one row share
    a stem, so their difference is that row's movement. Only numbers in the
    metric's own unit take part: a percentage row of the same table would
    otherwise contribute deltas that mean nothing in dollars.
    """
    stems: dict[str, dict[str, set[float]]] = {}
    wanted = normalize_unit(unit)
    for record in records:
        for number in record.numbers:
            if normalize_unit(number.unit) != wanted:
                continue
            label = _normalize_label(number.label)
            hits = [(key, t) for key, tokens in groups.items() for t in tokens if t in label]
            if len({key for key, _ in hits}) != 1:
                continue
            key, token = max(hits, key=lambda hit: len(hit[1]))
            cut = label.find(token)
            stem = _LEADING_DAY_RE.sub("", label[:cut]) + label[cut + len(token):]
            stems.setdefault(stem, {}).setdefault(key, set()).add(number.value)
    return stems


def _component_delta_pools(
    stems: dict[str, dict[str, set[float]]]
) -> tuple[set[float], set[float]]:
    """(deltas a component MAY claim, deltas it may NOT) as magnitudes.

    A component delta of the task's comparison subtracts the comparator column
    from the period column of ONE row. Every other pairing inside the same row
    describes a different comparison: period minus prior half is the
    half-on-half movement, prior half minus comparator is the half before that.
    Magnitudes, because the author signs a cost component the other way up.
    """
    correct: set[float] = set()
    wrong: set[float] = set()
    for periods in stems.values():
        current = periods.get("period", set())
        comparator = periods.get("comparator", set())
        prior = periods.get("prior_half", set())
        for value in current:
            correct.update(abs(value - other) for other in comparator)
            wrong.update(abs(value - other) for other in prior)
        for value in prior:
            wrong.update(abs(value - other) for other in comparator)
        # A prior-half LEVEL claimed as a contribution is the same trap one
        # step earlier: the 1H26 case claimed impairment -406, which is the
        # 30 Jun 25 column's figure, not any movement at all.
        wrong.update(abs(value) for value in prior)
    return correct, wrong


def check_component_columns(
    attribution, period_date, comparator_date, prior_half_date, prior_half_label=None
) -> tuple[list[str], list[str]]:
    """Rule 10's column discipline, applied to every COMPONENT of a bridge.

    check_movement_columns guards the headline only. A bridge answer can carry
    the right movement and still read its components out of the wrong columns:
    the CBA 1H26 cash-earnings case reported the movement 5,132 -> 5,445
    correctly while taking impairment off the prior half's column. This check
    mirrors it one level down and reads the extracted evidence, not the model's
    note: it groups every extracted number by the period column its label
    names, forms each row's three possible deltas, and fires when a claimed
    contribution matches a delta that spans the PRIOR HALF and matches no
    period-versus-comparator delta anywhere in the evidence.

    The second condition is what keeps the check quiet. A component that
    reconciles with any row's own prior-corresponding-period movement is never
    reported, so a claim that is right for a reason this code cannot see still
    passes.
    """
    passed, failed = [], []
    if attribution.movement is None:
        return passed, failed
    unit = normalize_unit(attribution.movement.unit)
    groups = {
        "period": _period_tokens(attribution.period, period_date),
        "comparator": _period_tokens(attribution.comparator, comparator_date),
        "prior_half": _period_tokens(prior_half_label, prior_half_date),
    }
    if not all(groups.values()):
        return passed, failed
    if any(
        groups[a] & groups[b]
        for a, b in (("period", "comparator"), ("period", "prior_half"), ("comparator", "prior_half"))
    ):
        return passed, failed
    correct, wrong = _component_delta_pools(_stems_by_period(attribution.evidence_records, groups, unit))
    if not wrong:
        return passed, failed
    tolerance = COMPONENT_TOL if unit == "$m" else _tolerance_for(LEAK_TOL, unit, 0.5)
    for driver in attribution.drivers:
        if driver.contribution is None:
            continue
        value = abs(driver.contribution.value)
        # A contribution smaller than the tolerance matches almost any pool, so
        # this check cannot diagnose it either way.
        if value <= tolerance:
            continue
        if not any(abs(value - w) <= tolerance for w in wrong):
            continue
        if any(abs(value - c) <= tolerance for c in correct):
            continue
        failed.append(
            f"component_from_prior_half ({driver.canonical} claims "
            f"{driver.contribution.value:+g} {unit}, which is a delta against the PRIOR HALF's "
            f"column and matches no {attribution.period} versus {attribution.comparator} delta "
            "in the evidence; subtract the comparator column from the period column of that "
            "component's own row)"
        )
    if not failed:
        passed.append("components_from_comparator_column")
    return passed, failed


def unclaimed_components(attribution, component_labels: dict[str, tuple[str, ...]]) -> list[str]:
    """Bridge components the evidence quantifies and the author left unclaimed.

    Feeds the author retry as a completeness nudge (ticket 27). Across three
    runs the CBA FY26 cash-earnings case claimed four, four and then three of
    its disclosed components, so the recall of a disclosed component was a
    matter of luck. The list names the canonical id and one evidence id, never
    a target value.
    """
    quantified = {d.canonical for d in attribution.drivers if d.contribution is not None}
    missing = []
    for canonical, keywords in component_labels.items():
        if canonical in quantified:
            continue
        seen = [
            record.id
            for record in attribution.evidence_records
            for number in record.numbers
            if any(word in _normalize_label(number.label) for word in keywords)
        ]
        if seen:
            missing.append(f"{canonical} (quantified in evidence {', '.join(sorted(set(seen))[:3])})")
    return missing


# A ratio the bank prints under one of these words is a NAMED VARIANT, not the
# headline measure: the same page usually prints both, one line apart. CBA's
# 1H26 CTI case took "Underlying operating expenses to underlying operating
# income" instead of the KPI row, and CET1 FY21 took a pro-forma endpoint.
VARIANT_WORDS = (
    "underlying", "ex notable", "excluding notable",
    "pro forma", "proforma", "internationally comparable", "level 1",
)


def _variant_text(text: str) -> str:
    """One spelling for a hyphenated word, so the label and the citation match.

    "ex-Notables" and "ex Notable Items" are the same word, and the author
    picks either. Westpac's registry label spells it with a space, so a run
    that wrote "row 'ROTE ex-notables'" failed a check that its own headline
    row should have exempted.
    """
    return text.lower().replace("-", " ").replace("_", " ")


def check_movement_variant(attribution, headline_label: str | None) -> tuple[list[str], list[str]]:
    """The movement must come from the headline row, not a named variant.

    Read from the row the author says it used. The check only fires on a word
    the bank's OWN headline label does not contain, so a bank whose headline
    measure is itself an underlying figure is unaffected.
    """
    passed, failed = [], []
    source = _variant_text(attribution.movement_source or "")
    if not source or attribution.movement is None:
        return passed, failed
    label = _variant_text(headline_label or "")
    hits = [word for word in VARIANT_WORDS if word in source and word not in label]
    if hits:
        failed.append(
            f"movement_from_variant (the row you read is a '{hits[0]}' variant: "
            f"{attribution.movement_source}. Read the headline measure instead, and "
            "report the variant as context or as a disagreement)"
        )
    else:
        passed.append("movement_from_headline_row")
    return passed, failed


# The words a movement_source uses to name the basis it was read on. Same
# vocabulary as author._BASIS_WORDS, kept here because the check reads the
# author's citation, not the author's basis field.
BASIS_SOURCE_WORDS = {
    "statutory": ("statutory",),
    "ex_notables": ("ex notable", "excluding notable"),
    "cash": ("cash",),
}


def check_movement_basis(
    attribution, primary_basis: str | None, headline_label: str | None
) -> tuple[list[str], list[str]]:
    """The movement must be read on the bank's own primary basis.

    A KPI page prints the SAME row twice, once under a "statutory basis" block
    header and once under a "cash earnings basis" one, a few lines apart: NAB's
    FY25 book page 15 prints "Cost to income ratio 49.6% | 48.5%" and then
    "Cost to income ratio 47.3% | 46.5%". The row label alone cannot tell them
    apart, so check_movement_variant sees nothing wrong.

    The masking made it worse. The author declared basis "statutory", no cited
    quote printed that word, and _settle_basis substituted the registry's
    primary basis — so the statutory numbers reached the scorer wearing the
    cash label and the basis check passed on a wrong row.

    Two signals, in order. First the basis word inside the author's own
    citation. Then the basis the answer DECLARES, for the case where the
    citation names no basis at all: Westpac's FY25 cash-earnings run cited "row
    'Net profit attributable to owners of WBC'" — no basis word — and declared
    "statutory", where Westpac reports on the excluding-Notable-Items basis and
    prints "Net profit excluding Notable Items" four rows above.

    A word the metric's registry HEADLINE ROW carries is exempt, so a bank whose
    headline row really is on another basis (Westpac's ROTE ex Notable Items) is
    unaffected. CET1 is skipped: a regulatory capital ratio has no basis.
    """
    passed, failed = [], []
    source = _variant_text(attribution.movement_source or "")
    if not source or attribution.movement is None or attribution.metric == "cet1":
        return passed, failed
    if not primary_basis:
        return passed, failed
    label = _variant_text(headline_label or "")
    for basis, words in BASIS_SOURCE_WORDS.items():
        if basis == primary_basis:
            continue
        hits = [word for word in words if word in source and word not in label]
        if hits:
            failed.append(
                f"movement_basis (the row you read is a '{hits[0]}' row: "
                f"{attribution.movement_source}. This bank reports on the {primary_basis} "
                "basis, and the same table prints the same row under that basis a few lines "
                "away. Read the movement there, and quote the other basis as context)"
            )
            return passed, failed
    declared = (attribution.basis or "").strip().lower()
    if declared and declared != primary_basis and not any(
        word in label for word in BASIS_SOURCE_WORDS.get(declared, ())
    ):
        failed.append(
            f"movement_basis (you declared basis '{declared}' where this bank reports on the "
            f"{primary_basis} basis. The {primary_basis} row is printed in the same table: read "
            f"the movement from it, and give the {declared} movement in the headline as context)"
        )
        return passed, failed
    passed.append("movement_on_primary_basis")
    return passed, failed


def implied_residual(attribution) -> float | None:
    """Movement delta minus the quantified contributions the author claimed.

    Fed back into the author retry (ticket 27) so the model corrects its
    arithmetic against a computed number instead of guessing a second time.
    """
    if attribution.movement is None:
        return None
    quantified = [d.contribution.value for d in attribution.drivers if d.contribution]
    if not quantified:
        return None
    return round(attribution.movement.delta - sum(quantified), 2)


def reconcile_tolerance(attribution) -> float:
    """The slack check_drivers_reconcile allows, and the scale normaliser reads.

    Tolerance follows the UNIT first and the evidence second. Drivers sourced
    from a presentation walk inherit its endpoint-rounding slack (the CBA CET1
    slide case), but only where that slack is denominated: it is a quantity in
    basis points, so a ppt or $m answer never earns it.
    """
    unit = normalize_unit(attribution.movement.unit if attribution.movement is not None else None)
    base = _tolerance_for(RECONCILE_TOL, unit, RECONCILE_TOL_DEFAULT)
    if unit not in PRESENTATION_LIFT_UNITS:
        return base
    presentation_walk = any(
        r.kind == "walk_vision" and ("presentation" in r.doc_id or "discussion" in r.doc_id)
        for r in attribution.evidence_records
    )
    return WALK_SUM_TOL_PRESENTATION if presentation_walk else base


# A ratio identity is stated in the RATIO's own unit. ROE is profit divided by
# average equity, so a profit movement enters the identity divided by that
# denominator, and a growth rate enters it as a FRACTION: earnings_effect =
# prior ROE x growth. An author that multiplies the prior ratio by a growth
# rate printed in PER CENT — or that carries a dollar movement straight into a
# ppt field — states the split exactly 100 times too large. The WBC FY25 ROE
# run split a -0.24 ppt movement into -23.76 and +0.56 ppt, so a CORRECT
# movement failed drivers_reconcile and shipped capped at 40.
IDENTITY_SCALE = 100.0


def _percent_evidenced(value: float, records) -> bool:
    """True when the extracted evidence prints this exact value as a percent.

    Both scale correctors are self-evidencing through this one test, so they
    read the pages the same way: the bps lift asks whether the endpoints the
    author wrote are printed as percentages, and settle_ratio_scale asks
    whether the endpoints divided by 100 are.
    """
    return any(
        abs(number.value - value) <= 0.005 and normalize_unit(number.unit) in RATIO_UNITS
        for record in records
        for number in record.numbers
    )


def settle_identity_scale(attribution, method: str) -> str | None:
    """Restate a ratio identity that was written 100x too large. Mutates.

    The correction is arithmetic, never evidence, and it is self-evidencing:
    it fires only when the identity does NOT close at the scale the author
    wrote AND does close one factor of 100 down AND some contribution is
    larger than the ratio's own endpoints. A ppt contribution bigger than the
    ratio itself is not a movement of that ratio; it is a number on another
    scale. A bridge whose components are genuinely wrong still fails the
    reconciliation check, because dividing wrong numbers by 100 does not make
    them sum.

    Returns the note it appended to limitations, or None when nothing changed.
    """
    if method != "two_level_arithmetic" or attribution.movement is None:
        return None
    unit = normalize_unit(attribution.movement.unit)
    quantified = [
        d for d in attribution.drivers
        if d.contribution is not None and normalize_unit(d.contribution.unit) == unit
    ]
    if not quantified or len(quantified) != len([d for d in attribution.drivers if d.contribution]):
        return None
    delta = attribution.movement.delta
    residual = attribution.residual.value if attribution.residual else 0.0
    tolerance = reconcile_tolerance(attribution)
    raw = sum(d.contribution.value for d in quantified)
    if abs(raw + residual - delta) <= tolerance:
        return None
    # A contribution to a ratio movement cannot outrun the ratio's own level.
    level = max(abs(attribution.movement.from_value), abs(attribution.movement.to_value))
    if not any(abs(d.contribution.value) > level for d in quantified):
        return None
    # The author may have written the residual on either scale, so try the two
    # readings in order: the residual as written, then the residual rescaled
    # with the contributions.
    for scaled_residual in (residual, residual / IDENTITY_SCALE):
        if abs(raw / IDENTITY_SCALE + scaled_residual - delta) > tolerance:
            continue
        for driver in quantified:
            driver.contribution.value = round(driver.contribution.value / IDENTITY_SCALE, 4)
            driver.checks_passed.append("identity_scale_normalised")
        if attribution.residual is not None and scaled_residual != residual:
            attribution.residual.value = round(scaled_residual, 4)
        note = (
            f"Identity contributions restated from {raw:+.2f} to {raw / IDENTITY_SCALE:+.4f} "
            f"{unit}: the identity closes on the movement delta at the ratio's own scale and "
            "not at the scale they were written on, and a contribution larger than the ratio "
            "itself cannot be a movement of that ratio. A growth rate enters a ratio identity "
            "as a fraction, and a dollar movement enters it divided by the identity's "
            "denominator."
        )
        attribution.limitations.append(note)
        return note
    return None


# The evidence ladder's ceiling for a number the model worked out rather than
# read. Named for the bridge check it grew out of, and kept as one value so a
# reader of the artifact sees one rule however the claim was assembled.
CLAIM_CITATION_CAP = 80
# A number written inside a quote, as a standalone token, WITH the unit a bank
# glues to it. The lookarounds keep a period tag out of the pool: "FY25" must
# not ground a claim of +25, "1H26" must not ground +26, and "p12" must not
# ground +12.
#
# The suffix group is what makes the rest of the pattern work at all. Without
# it the trailing (?![\w]) failed on every glued unit, the engine backtracked,
# and the pool took a PREFIX of the number: "$10,982m" read as 10, "$2.5bn" as
# 2, and "5bps" vanished. Both directions of the citation cap inverted at once
# — the driver whose number the record printed was capped, and a neighbour with
# a small round value was certified by a digit prefix. 8% of the shipped quotes
# carry a digit glued to a letter.
_QUOTE_NUMBER_RE = re.compile(
    r"(?<![\w.])(-?\d[\d,]*(?:\.\d+)?)"
    r"\s*(bpts|bps|bp|ppts|ppt|pp|billion|bn|million|m|b|%|c)?(?![\w])",
    re.IGNORECASE,
)
# A bare four-digit integer inside this window is a year, not a quantity: the
# saved quotes put "2025" in the pool beside a footnote index. A period TAG
# ("FY25") was already excluded, so this closes the same hole for the spelling
# a sentence uses. A magnitude the quote states with a separator ("2,025") or a
# decimal is unaffected.
_YEAR_RANGE = (1990, 2099)
# The unit a glued suffix names, in the estate's own spelling. "m" and "bn" are
# money because that is what a bank glues to a figure; a ratio is glued "%" or
# "bps".
_SUFFIX_UNITS = {
    "bps": "bps", "bpts": "bps", "bp": "bps",
    "ppt": "ppt", "ppts": "ppt", "pp": "ppt", "%": "%",
    "m": "$m", "million": "$m",
    "bn": "$bn", "b": "$bn", "billion": "$bn",
    "c": "cents",
}
# The words a quote uses to name a unit family, for a number the page prints
# WITHOUT a glued suffix (a table row: "Loan impairment expense 319 406 320").
# A bare number is read in the claim's own unit only when the quote names that
# unit family somewhere, so a dollar row can no longer ground a ratio claim.
_FAMILY_WORDS = {
    "$m": ("$", "million"),
    "$bn": ("$", "billion"),
    "ppt": ("%", "per cent", "percent", "percentage point", "ppt", "pt"),
    "%": ("%", "per cent", "percent", "percentage point", "ppt", "pt"),
    "ratio": ("%", "per cent", "percent", "percentage point", "ppt", "pt"),
    "bps": ("bps", "bpts", "basis point"),
    "cents": ("cent", "cps"),
}


def _quote_numbers(quote: str | None) -> list[tuple[float, str]]:
    """(magnitude, unit) for every number a verbatim quote states.

    The unit is the one glued to the number, or "" when the quote prints the
    number bare. The caller decides what a bare number may ground.
    """
    values: list[tuple[float, str]] = []
    for token, suffix in _QUOTE_NUMBER_RE.findall(quote or ""):
        try:
            value = abs(float(token.replace(",", "")))
        except ValueError:  # pragma: no cover - the pattern admits only numbers
            continue
        unit = _SUFFIX_UNITS.get(suffix.lower(), "") if suffix else ""
        if (
            not unit
            and "," not in token
            and "." not in token
            and _YEAR_RANGE[0] <= value <= _YEAR_RANGE[1]
            and len(token.lstrip("-")) == 4
        ):
            continue
        values.append((value, unit))
    return values


def quote_states(quote: str | None, value: float, unit: str | None) -> bool:
    """Does this quote PRINT this number, read in this unit?

    Three readings, in order of how much the page itself says:
    1. the number carries its own glued unit, which must convert into the
       claim's ("a -20 bps fall" grounds -0.2 ppt, never -20 ppt);
    2. the number is bare and the quote names the claim's unit family
       elsewhere in the sentence or the row;
    3. otherwise the quote says nothing about the claim's unit, so it grounds
       nothing.
    """
    tolerance = _tolerance_for(CITATION_TOL, unit, CITATION_TOL_DEFAULT)
    lowered = (quote or "").lower()
    family = any(word in lowered for word in _FAMILY_WORDS.get(normalize_unit(unit), ()))
    for quoted, quoted_unit in _quote_numbers(quote):
        if quoted_unit:
            converted = convert_unit(quoted, quoted_unit, unit)
            if converted is not None and abs(converted - abs(value)) <= tolerance:
                return True
            continue
        if family and abs(quoted - abs(value)) <= tolerance:
            return True
    return False


def quote_prints(quote: str | None, value: float, unit: str | None = None) -> bool:
    """Does this quote print this magnitude at all?

    The value question, without the unit question. `quote_states` asks whether
    a record GROUNDS a claim, and binds the unit to do it. This asks only
    whether the number is on the page, which is what a model-supplied
    NumberFact has to answer before anything may rest on it: the agent's `cite`
    tool took those facts on trust, so an unrelated verbatim sentence could
    carry an invented {"value": 150, "unit": "$m"} and every check that reads
    record.numbers would then read a number no page prints.
    """
    tolerance = _tolerance_for(CITATION_TOL, unit, CITATION_TOL_DEFAULT)
    for quoted, quoted_unit in _quote_numbers(quote):
        if abs(quoted - abs(value)) <= tolerance:
            return True
        converted = convert_unit(quoted, quoted_unit, unit) if quoted_unit else None
        if converted is not None and abs(converted - abs(value)) <= tolerance:
            return True
    return False


def _states(
    number: float, number_unit: str | None, value: float, unit: str | None, tolerance: float
) -> bool:
    """Does this extracted NumberFact print that claim's number?

    The magnitudes used to be compared with no unit at all, so the `0.0 $m`
    cell of a dollar row grounded a `+0.0 ppt` claim at confidence 90, and a
    `-5.0 bps` fact grounded a `-5.0 $m` claim at 95. A fact whose unit cannot
    be read in the claim's unit is not evidence for the claim, whatever its
    magnitude; a fact carrying NO unit is not evidence either way.
    """
    converted = convert_unit(abs(number), number_unit, unit)
    return converted is not None and abs(converted - abs(value)) <= tolerance


def cap_weakly_cited_claims(attribution) -> list[str]:
    """Cap a quantified claim whose own citations do not state its number.

    The evidence gate (schema.enforce_evidence_gate) asks whether a citation
    RESOLVES. That is a structural question, and a claim passes it while the
    records it points at say nothing like the number claimed: the CBA FY26
    impairment run shipped +150 / -17 / -71 $m at confidence 85 citing two
    chart reads whose only numbers were 6.2, -5.6, 0.0, -8.5 and -1.4. The
    bridge metrics already asked the second question; impairment is a
    note_decomposition and ROE a two_level_arithmetic, so for them nobody did.

    A record supports a quantified claim when it PRINTS that number - as an
    extracted NumberFact, or in the words of the quote itself, because prose
    evidence carries its number in the sentence ("Decreased margin by 5 basis
    points" grounds a -5 bps claim exactly as well as an extracted bar does).
    Anything else is the model's own arithmetic over the evidence, which is
    what the evidence ladder caps at 80.

    The cap never raises a confidence and never strips a claim: a computed
    delta is still an answer, it is just not a reading. Returns the claims it
    capped; mutates the attribution.
    """
    capped: list[str] = []
    by_id = {record.id: record for record in attribution.evidence_records}
    for driver in attribution.drivers:
        if driver.contribution is None or driver.confidence <= CLAIM_CITATION_CAP:
            continue
        value = abs(driver.contribution.value)
        unit = driver.contribution.unit
        tolerance = _tolerance_for(CITATION_TOL, unit, CITATION_TOL_DEFAULT)
        cited = [by_id[e] for e in driver.evidence if e in by_id]
        stated = any(
            _states(number.value, number.unit, value, unit, tolerance)
            for record in cited
            for number in record.numbers
        ) or any(quote_states(record.quote, value, unit) for record in cited)
        if stated:
            continue
        driver.confidence = CLAIM_CITATION_CAP
        driver.checks_passed.append("computed_delta_cap_80")
        capped.append(
            f"{driver.canonical} {driver.contribution.value:+g} {driver.contribution.unit}"
        )
    if capped:
        attribution.limitations.append(
            f"Capped at {CLAIM_CITATION_CAP}: " + ", ".join(capped) + ". The records these "
            "claims cite do not state those numbers, so each one is arithmetic over the "
            "evidence rather than a figure read from it."
        )
    return capped


def check_drivers_reconcile(attribution) -> tuple[list[str], list[str]]:
    """Quantified drivers + residual should sum to the movement delta.

    The SUM is unit-typed as well as the tolerance. Round 1 made the slack
    follow the movement's unit and left the addition unit-blind, so a `+3 bps`
    bar still reconciled a `$m` bridge: three basis points were added as three
    dollars-million. A contribution stated in another unit is a fact about
    something else, so it is named and it never enters the total.
    """
    passed, failed = [], []
    if attribution.movement is None:
        return passed, failed
    unit = normalize_unit(attribution.movement.unit)
    contributions = [d.contribution for d in attribution.drivers if d.contribution]
    off_unit = [c for c in contributions if normalize_unit(c.unit) != unit]
    residual_fact = attribution.residual
    if residual_fact is not None and normalize_unit(residual_fact.unit) not in ("", unit):
        off_unit = [*off_unit, residual_fact]
    quantified = [c.value for c in contributions if normalize_unit(c.unit) == unit]
    if off_unit:
        failed.append(
            "drivers_unit_mismatch ("
            + ", ".join(f"{c.value:+g} {c.unit}" for c in off_unit)
            + f" is not stated in the movement's unit ({attribution.movement.unit}); a "
            "contribution is a share of THIS movement, so it carries the movement's unit)"
        )
    if not quantified:
        return passed, [*failed, "no_quantified_drivers"]
    tolerance = reconcile_tolerance(attribution)
    residual = residual_fact.value if residual_fact else 0.0
    total = sum(quantified) + residual
    if abs(total - attribution.movement.delta) <= tolerance:
        passed.append("drivers_reconcile")
    else:
        failed.append(
            f"drivers_reconcile (drivers {sum(quantified):+.1f} + residual {residual:+.1f} "
            f"!= delta {attribution.movement.delta:+.1f}, tol {tolerance})"
        )
    return passed, failed


# A ratio's LEVEL, above which the number is not a ratio at all. The largest
# ratio these banks print is a liquidity coverage ratio near 130% or an NSFR
# near 115%, and the largest legitimate level in the whole saved set is a
# Westpac cost-to-income ratio of 53.04. 200 leaves 3.8x headroom above real
# data and sits 5.8x below the smallest defect it must catch (an ROE of 1160,
# which is 11.6% written in basis points).
RATIO_LEVEL_CEILING = 200.0


def check_ratio_level(movement) -> tuple[list[str], list[str]]:
    """A ratio movement's endpoints must be ratio-sized.

    A percent-to-bps lift exists for a bps metric; its mirror never did. So a
    ppt metric whose endpoints arrived in BASIS POINTS passed every check:
    movement arithmetic is self-consistent (1160 - 20 = 1140), the drivers
    reconcile at the same wrong scale, and settle_identity_scale's guard needs
    a contribution larger than the level, which 1160 never is. The unit-typed
    tolerances round 1 introduced are only as good as the unit LABEL, and
    nothing asked whether the label fitted the number.
    """
    passed, failed = [], []
    if movement is None or normalize_unit(movement.unit) not in RATIO_UNITS:
        return passed, failed
    level = max(abs(movement.from_value), abs(movement.to_value))
    if level > RATIO_LEVEL_CEILING:
        failed.append(
            f"movement_level_not_ratio_sized ({level:g} {movement.unit} is not the level of a "
            f"ratio; the ceiling is {RATIO_LEVEL_CEILING:g}. A ratio of 11.6 per cent is 11.6 "
            "in points and 1160 in basis points: read the endpoints in the metric's own unit, "
            "and convert a change column printed in basis points by dividing it by 100)"
        )
    else:
        passed.append("movement_level_is_ratio_sized")
    return passed, failed


def settle_ratio_scale(attribution, records=None) -> str | None:
    """Restate a ratio movement written in basis points. Mutates.

    The mirror of the percent-to-bps lift the bps metrics have: there the
    author reads "12.20" off a percent column while the metric is bps, here it
    reads the level to match a change column printed in basis points while the
    metric is points. NAB's FY25 ROE run read the RIGHT row — "Cash return on
    equity 11.4% 11.6% (20 bps)" — and then submitted 1160.0 -> 1140.0 ppt.

    The correction is self-evidencing, exactly as the lift is: it fires only
    when the evidence PRINTS both endpoints, divided by 100, as percentages. A
    movement already written in points cannot pass that test, because no page
    prints an ROE of 0.116 per cent.
    """
    movement = attribution.movement
    if movement is None or normalize_unit(movement.unit) not in RATIO_UNITS:
        return None
    records = attribution.evidence_records if records is None else records
    frm, to = movement.from_value / IDENTITY_SCALE, movement.to_value / IDENTITY_SCALE
    if not (_percent_evidenced(frm, records) and _percent_evidenced(to, records)):
        return None
    note = (
        f"Movement endpoints converted from basis points ({movement.from_value:g}, "
        f"{movement.to_value:g}) to {movement.unit}: the evidence prints this ratio as "
        f"{frm:g}% and {to:g}%, and the unit for this metric is {movement.unit}. A change "
        "column printed in basis points is divided by 100 to enter a movement stated in "
        "points."
    )
    movement.from_value, movement.to_value = round(frm, 4), round(to, 4)
    movement.delta = round(movement.delta / IDENTITY_SCALE, 4)
    attribution.limitations.append(note)
    return note


# The failures that condemn the WHOLE quantified driver table rather than one
# claim. A bridge that does not close proves that one contribution is wrong and
# not which one; a movement read at the wrong scale is a movement the whole
# table was written against. Either way code cannot name the offender, so every
# quantified claim loses its right to near-certainty.
WHOLE_TABLE_FAILURES = ("drivers_reconcile", "movement_level_not_ratio_sized")


def cap_unreconciled_drivers(attribution, failures: list[str]) -> list[str]:
    """Carry a fatal check down to the DRIVERS. Mutates; returns what it capped.

    A failed check used to lower `attribution_confidence` alone, and every
    per-driver `confidence` survived it untouched. The calibration metrics read
    the DRIVER's confidence, so the Brier score and the confidently-wrong rate
    were blind to every failed check: 22 saved artifacts carry a "Failed check"
    limitation and ship drivers at 80-90, and the suite's one confidently-wrong
    claim is exactly this — a bridge that failed drivers_reconcile, an answer
    that declared 40, and the offending driver still at 85.
    """
    hits = [f for f in failures if any(f.startswith(name) for name in WHOLE_TABLE_FAILURES)]
    if not hits:
        return []
    capped = []
    for driver in attribution.drivers:
        if driver.contribution is None or driver.confidence <= CLAIM_CITATION_CAP:
            continue
        driver.confidence = CLAIM_CITATION_CAP
        driver.checks_passed.append("unreconciled_bridge_cap_80")
        capped.append(f"{driver.canonical} {driver.contribution.value:+g} {driver.contribution.unit}")
    if capped:
        attribution.limitations.append(
            f"Capped at {CLAIM_CITATION_CAP}: " + ", ".join(capped) + ". "
            + hits[0].split(" (")[0]
            + " failed, so the parts and the whole disagree. That proves one of these claims "
            "is wrong without saying which, so none of them may claim near-certainty."
        )
    return capped


def sign_flip_hint(attribution) -> str | None:
    """A retry hint when the reconciliation gap is exactly twice one claim.

    Nothing converts a COST component's own movement into its effect on
    earnings. CBA's 1H26 loan impairment expense fell from 320 to 319, which
    ADDS $1m to cash earnings, and the author copied the change in the charge
    (-1) into the contribution field. The bridge then missed by +2, which is
    exactly -2 x the offending contribution.

    This is a HINT and never a correction: it names the driver whose sign to
    re-read, and it never states a value the author should reach. Where two
    contributions fit the gap it says so, so an ambiguous case gets a question
    rather than an answer.
    """
    movement = attribution.movement
    if movement is None:
        return None
    quantified = [
        d for d in attribution.drivers
        if d.contribution is not None
        and normalize_unit(d.contribution.unit) == normalize_unit(movement.unit)
    ]
    if not quantified:
        return None
    residual = attribution.residual.value if attribution.residual else 0.0
    gap = movement.delta - (sum(d.contribution.value for d in quantified) + residual)
    tolerance = reconcile_tolerance(attribution)
    if abs(gap) <= tolerance:
        return None
    candidates = [
        d for d in quantified
        if d.contribution.value != 0 and abs(gap + 2 * d.contribution.value) <= tolerance
    ]
    if not candidates:
        return None
    names = ", ".join(
        f"'{d.canonical}' ({d.contribution.value:+g} {d.contribution.unit})" for d in candidates
    )
    if len(candidates) == 1:
        return (
            f"The gap between your contributions and the movement delta is exactly TWICE your "
            f"{names} contribution, with the opposite sign. That is the signature of a sign "
            "error: check that contribution's direction against the movement's. A line the "
            "bank prints as a cost or a charge moves the total the OTHER way — a charge that "
            "falls adds to earnings — so the contribution is not always the change in the row "
            "as printed. Correct the sign only if the evidence supports it; otherwise declare "
            "the residual."
        )
    return (
        f"The gap between your contributions and the movement delta is exactly TWICE one of "
        f"these contributions, with the opposite sign: {names}. One of them may carry the "
        "wrong direction: a line the bank prints as a cost or a charge moves the total the "
        "OTHER way, so a charge that falls adds to earnings. Check each against the evidence, "
        "and declare the residual if the evidence does not settle it."
    )
