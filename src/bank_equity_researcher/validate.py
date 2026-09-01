"""Deterministic validation checks and their tolerances (tickets 01, 05),
plus the deterministic comparison classifier (defect 24).

Every constant carries the reason it has that value.

HARDCODED-OVERRIDE POLICY (user directive, 2026-08-31): any line in this
module that overrides an agent's own stated judgment - a cap, a threshold,
a forced rule - stays SPARSE and must EARN its place. Each one's comment
cites the experiment or run showing the failure it prevents - a defect
number, an artifact, a scorecard - never a hunch. The default lean is to
trust the self-report and let the evals catch failures; an override without
traceable evidence is a cleanup-round deletion candidate (ticket 33 audits
every one against this rule).

STANDING EVIDENCE for the confidence-cap ladder: the caps-off ablation
(2026-08-31, evals/results/audits/capsoff-*-dev-rescore.md). Raw
self-reports rank claims WELL (uncapped Brier beats capped on a fixed claim
set) but put a few genuinely wrong claims at 90; the kept caps exist for
that tail alone, at a measured Brier cost of ~0.003-0.007, and they write
80 - one notch below the 85 confident threshold, which any reader of the
confidently-wrong rate must know. The single_source override was deleted by
the same run.
"""

from __future__ import annotations

import re

from .corpus import PRESENTATION_DOC_TYPES

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
# A tolerance means nothing without the unit it is stated in. The constants
# above are calibrated in BASIS POINTS: 1.0 is a rounding step in bps and five
# times the whole movement in percentage points. The shipped CBA FY26
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
# A tolerance table is a dict keyed by a unit STRING, so "PPT", "bpts" and
# "$ m" miss every entry and take the default: a ppt movement measured with the
# 1.0 reconciliation slack is measured with five times its own size. One
# canonical spelling keeps the scorer and the checks reading the same answer the
# same way. The vocabulary lives here, beside the tolerances it keys, and evals
# imports it (the reverse import is a cycle).
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


def default_comparator(period: str) -> str:
    """FY input -> prior FY; half input -> PCP (same half, prior year)."""
    match = re.fullmatch(r"(FY|1H|2H)(\d{2})", period)
    if not match:
        raise ValueError(f"unrecognised period: {period} (expected FY26, 1H26, 2H25 ...)")
    return f"{match.group(1)}{int(match.group(2)) - 1}"


def _month_name(month: int) -> str:
    return next(k for k, v in MONTH_NUMBERS.items() if v == month).capitalize()


def build_period_note(period: str, comparator: str, calendar: dict) -> str:
    """Spell out both balance dates, and the prior-half column that sits
    between them (defect 24).

    Half-year results tables print THREE period columns — the current period,
    the prior half, and the same half one year earlier — with two comparison
    columns beside them. The middle column is the trap: it is the prior half,
    never the comparator. Full-year books print the same three columns.
    """
    end, start = period_end_date(period, calendar), period_end_date(comparator, calendar)
    if end is None or start is None:
        return f"- The task compares {period} against {comparator}."
    span = "12 months" if period.upper().startswith("FY") else "half"
    lines = [
        f"- {period} = the {span} ended {_month_name(end[0])} {end[1]}. Its column gives to_value.",
        (
            f"- {comparator} = the {span} ended {_month_name(start[0])} {start[1]}. "
            "Its column gives from_value."
        ),
    ]
    middle = (end[0] - 6, end[1]) if end[0] > 6 else (end[0] + 6, end[1] - 1)
    if middle != start:
        lines.append(
            f"- Results tables also print a column for the half ended {_month_name(middle[0])} "
            f"{middle[1]} (the PRIOR HALF). That column is neither endpoint. A comparison "
            "against it is half-on-half, which is a different question from this task."
        )
    return "\n".join(lines)


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
    if normalize_unit(unit) in PRESENTATION_LIFT_UNITS and doc_type in PRESENTATION_DOC_TYPES:
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
    delta before any check sees it. A hard-coded 0.51 is a basis-point
    quantity: a ppt movement whose delta was out by 0.5 escaped the repair,
    then failed the 0.1 ppt check, and the answer shipped at confidence 40.
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
    """Annotate each quantified driver with its corroboration status.

    Mutates the attribution in place. No Disagreement is synthesised here: an
    auto-disagreement branch over CORROBORATION_TOL fired on 0 of the 90 saved
    artifacts, where the model itself wrote all 89 disagreements the estate
    holds.
    """
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
        elif n_sources <= 1:
            # The single-source TAG stays: a reader deserves to know a number
            # was seen in one document. No confidence override sits here. The
            # caps-off ablation (2026-08-31, evals/results/audits/capsoff-*)
            # deleted the min-85 cap: it fired 70x on a 25-case suite, demoted
            # overwhelmingly-correct claims, capped exactly ON the 85 confident
            # threshold rather than below it, and still left a wrong claim
            # inside the confident band.
            driver.checks_passed.append("single_source")


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

    The check does not cap the offender BY NAME: the `comparison_leak_cap_80`
    override fired on 0 of the 90 saved artifacts, so it carried no evidence
    under the hardcoded-override policy above. `comparison_leak` is a
    `WHOLE_TABLE_FAILURE` instead, so a leak takes every quantified claim to
    `CLAIM_CITATION_CAP`, and the named failure still reaches the fatal grading
    the shell applies to a failed check.
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

    The check does not cap the offender BY NAME, on the same ground as
    `check_comparison_leak`: the `component_column_cap_80` override fired on 0
    of the 90 saved artifacts, so it carried no evidence under the
    hardcoded-override policy. `component_from_prior_half` is a
    `WHOLE_TABLE_FAILURE` instead, so a component read from the prior half's
    column takes every quantified claim to `CLAIM_CITATION_CAP`.
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
# vocabulary as _BASIS_WORDS below, kept separate because this check reads the
# citation text, not the declared basis field.
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
    apart, so check_movement_variant sees nothing wrong. _settle_basis then
    masks the slip: it substitutes the registry's primary basis for a
    declaration no cited quote prints, so statutory numbers reach the scorer
    wearing the cash label.

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


# --------------------------------------------------------------------------
# Movement, basis and sign normalisers
#
# These read a model's own submission and restate it before any check runs,
# so a check downstream of one of them is asserting that the restatement
# worked. They sit here beside the checks that read their output.
# --------------------------------------------------------------------------


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


def primary_basis(registry: dict) -> str | None:
    """The bank's own headline basis, read from the registry vocabulary.

    None when the registry carries no measures block: a skeleton registry
    (MQG) or a missing one knows no basis, and a "cash" default there let
    _settle_basis rewrite a declared "statutory" to "cash" and claim the
    registry named it (review round 10). The default survives only under a
    measures block whose core_profit names no basis word, where every committed
    registry is an Australian major reporting cash earnings.
    """
    measures = registry.get("measures")
    if not measures:
        return None
    core = str(measures.get("core_profit", "")).lower()
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
    but it stops being a quantified contribution.

    No confidence override sits here: the drop fired on 0 of the 90 saved
    artifacts, so a hardcoded 60 carried no evidence. The drop itself stays,
    because it is a shape rule and not a confidence judgment.

    Mutates; returns the notes.
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

    An extractor invents one: it tagged CBA's unlabelled Group NIM row
    "statutory", and the author repeated it, so a correct movement was scored
    wrong on its basis alone. When the claimed basis appears nowhere in the
    cited quotes, fall back to the bank's headline basis from the registry and
    record the substitution.

    This function owns the no-declaration default too. The registry's headline
    basis stands in when it knows one, and "as reported" says plainly that
    nothing was declared or known. Never "cash" without a registry behind it: a
    hardcoded "cash" shipped an invented basis for MQG, which reports statutory
    NPAT under a skeleton registry that knows no basis (review round 11).
    """
    declared = str(basis or "").strip().lower()
    primary = primary_basis(registry)
    if not declared:
        return primary or "as reported"
    if primary is None or declared == primary or _basis_printed(declared, records):
        return declared
    reply.setdefault("limitations", []).append(
        f"Basis normalised from '{declared}' to '{primary}': no page in evidence prints "
        f"'{declared}' beside the movement, and the registry names {primary} as the bank's "
        "headline basis."
    )
    return primary


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
# it the trailing (?![\w]) fails on every glued unit, the engine backtracks,
# and the pool takes a PREFIX of the number: "$10,982m" reads as 10, "$2.5bn"
# as 2, and "5bps" vanishes. 8% of the shipped quotes carry a digit glued to a
# letter.
#
# The unit a bank SPELLS OUT counts as a glued unit too. "decreased 5 basis
# points" reached the pool as a bare 5, so the number carried no unit into the
# conversion table and any unit the model named was accepted for it. A
# multi-word alternative must precede every alternative that is a prefix of it,
# because the engine takes the first that matches: "percentage points" before
# "per cent", "basis point" before "b".
#
# A bank writes a negative change in brackets and glues the unit OUTSIDE them:
# "Net interest margin (%) 2.05 2.08 (3)bpts". The closing bracket stood
# between the number and its unit, so 73 of the 2,034 shipped quotes put a
# UNITLESS number in the pool where the page had named its unit — and a
# unitless number is read in whatever family the rest of the quote mentions.
_QUOTE_NUMBER_RE = re.compile(
    r"(?<![\w.])(-?\d[\d,]*(?:\.\d+)?)\)?"
    r"\s*(basis\s+points?|percentage\s+points?|per\s?cents?"
    r"|bpts|bpt|bps|bp|ppts|ppt|pp|billion|bn|million|m|b|%|c)?(?![\w])",
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
    "bps": "bps", "bpts": "bps", "bpt": "bps", "bp": "bps",
    "basis point": "bps", "basis points": "bps",
    "ppt": "ppt", "ppts": "ppt", "pp": "ppt", "%": "%",
    "percentage point": "ppt", "percentage points": "ppt",
    "per cent": "%", "per cents": "%", "percent": "%", "percents": "%",
    "m": "$m", "million": "$m",
    "bn": "$bn", "b": "$bn", "billion": "$bn",
    "c": "cents",
}
# The unit a quote DECLARES for the bare numbers in it — the header of a table
# row ("Net interest margin (%) 2.05 2.08", "Assets ($bn) 2.5", "Movement in
# CET1 (bps) 12 34") or a unit word standing in the sentence ("Cost to income
# ratio, per cent 45.0 46.2"). A table prints its unit once, above the column
# or beside the row, and the cells bare; the declaration is how a bare cell is
# read at all.
#
# The key is the unit's canonical spelling, so a declaration reaches a claim
# through UNIT_CONVERSIONS and through nothing else. The generic "$" is not a
# key here: it names the money family and no scale inside it, and holding it
# for both "$m" and "$bn" is what let "Assets ($bn) 2.5" state 2.5 $m without
# the 1000x conversion.
#
# The test is on a WORD, not on a substring. "pt" is inside "bpts", so a table
# headed "Movements in bpts" named the POINTS family and a bare 34 grounded a
# claim of 34 ppt — the basis-point reading is 0.34, so the citation cap was
# inverted by a factor of 100. "pt" is also inside "September", "accepted",
# "adopted" and "except", and "cent" is inside "recent" and inside "per cent"
# itself. "$" and "%" are not word characters, so they stay plain substrings.
_DECLARED_UNIT_PATTERNS = {
    "$m": re.compile(r"\$\s?m\b|\bmillions?\b", re.IGNORECASE),
    "$bn": re.compile(r"\$\s?bn?\b|\bbillions?\b", re.IGNORECASE),
    "bps": re.compile(r"\bbp(?:s|t|ts)?\b|\bbasis point", re.IGNORECASE),
    "%": re.compile(r"%|\bper\s?cent|\bpercent|\bpercentage point|\bppts?\b", re.IGNORECASE),
    "cents": re.compile(r"\bcents\b|\bcps\b", re.IGNORECASE),
}
# A quote that writes "$" and never says which scale. It names the money family
# and leaves the scale to the row, so a bare number under it reads 1:1 in
# whichever money unit the claim is stated in — the reading a plain "$" column
# has always had.
MONEY_SCALE_UNSTATED = "$"
_MONEY_MARK = re.compile(r"\$")


def _scan_numbers(quote: str | None) -> list[tuple[float, str, re.Match[str]]]:
    """(magnitude, unit, match) for every number a verbatim quote states.

    The unit is the one glued to the number, or "" when the quote prints the
    number bare. The caller decides what a bare number may ground. The match is
    kept so a caller can read the words around the number.
    """
    values: list[tuple[float, str, re.Match[str]]] = []
    for match in _QUOTE_NUMBER_RE.finditer(quote or ""):
        token, suffix = match.group(1), match.group(2)
        try:
            value = abs(float(token.replace(",", "")))
        except ValueError:  # pragma: no cover - the pattern admits only numbers
            continue
        # A spelled-out unit reaches here with the page's own spacing, and a
        # PDF text layer breaks a line wherever it likes.
        unit = _SUFFIX_UNITS.get(" ".join(suffix.lower().split()), "") if suffix else ""
        if (
            not unit
            and "," not in token
            and "." not in token
            and _YEAR_RANGE[0] <= value <= _YEAR_RANGE[1]
            and len(token.lstrip("-")) == 4
        ):
            continue
        values.append((value, unit, match))
    return values


def _quote_numbers(quote: str | None) -> list[tuple[float, str]]:
    """(magnitude, unit) for every number a verbatim quote states."""
    return [(value, unit) for value, unit, _ in _scan_numbers(quote)]


def _declarations(quote: str | None) -> tuple[tuple[int, str], ...]:
    """(position, unit) for every unit the quote's own WORDS declare.

    A unit token that a number has already taken as its glued suffix declares
    nothing: it belongs to that one figure. "Operating expenses 6,000 5,800
    3.4%" prints a percentage CHANGE beside two dollar cells, and reading its
    "%" as the row's unit would refuse the cells their own. So a token inside
    the span of a number is skipped, and what remains is the row label and the
    column headers.
    """
    text = quote or ""
    spans = [match.span() for match in _QUOTE_NUMBER_RE.finditer(text)]

    def taken(start: int, end: int) -> bool:
        return any(start < span_end and end > span_start for span_start, span_end in spans)

    found: list[tuple[int, str]] = []
    money = False
    for unit, pattern in _DECLARED_UNIT_PATTERNS.items():
        for match in pattern.finditer(text):
            if taken(*match.span()):
                continue
            found.append((match.start(), unit))
            money = money or unit in ("$m", "$bn")
    if not money:
        # A "$" that a number has taken as its own currency mark ("$554m") is
        # that figure's, not the row's.
        found += [
            (match.start(), MONEY_SCALE_UNSTATED)
            for match in _MONEY_MARK.finditer(text)
            if not taken(match.start(), match.end() + 1)
        ]
    return tuple(sorted(found))


def _declared_grounds(
    declared: tuple[tuple[int, str], ...], quoted: float, value: float, unit: str | None
) -> bool:
    """Does a BARE number, read in a unit the quote declares, state this claim?

    Every declared unit is tried, wherever it stands, because one quote can
    carry several ("Net interest margin (%) 2.05 2.08 (3)bpts", and a quote
    that spans four rows of a table carries one per row). A reading through
    UNIT_CONVERSIONS is the only reading there is: a cell under a "($bn)"
    header states 2500 $m and never 2.5 $m.
    """
    for _position, family in declared:
        if family == MONEY_SCALE_UNSTATED:
            if normalize_unit(unit) in ("$m", "$bn") and abs(quoted - abs(value)) <= _tolerance_for(
                CITATION_TOL, unit, CITATION_TOL_DEFAULT
            ):
                return True
            continue
        if _converted_prints(quoted, family, value, unit):
            return True
    return False


def _same_family(declared_unit: str, claim_unit: str | None) -> bool:
    """Do a declared unit and a claimed unit restate each other?"""
    claim = normalize_unit(claim_unit)
    if declared_unit == MONEY_SCALE_UNSTATED:
        return claim in ("$m", "$bn")
    return convert_unit(1.0, declared_unit, claim) is not None


def _declaration_refuses(
    declared: tuple[tuple[int, str], ...], start: int, unit: str | None
) -> bool:
    """Does the row this bare number sits in deny it to this claim?

    Asked only after `_declared_grounds` has failed, and measured over the 79
    saved artifacts, because both halves of it are a fact about how banks print
    a table.

    Only a declaration STANDING BEFORE the number binds it. A quote often spans
    four rows of one table — "Average net assets 78,004 ... ROE - cash basis
    (%) 13.8" — and the header of the last row says nothing about the cells of
    the first. Reading the "(%)" backwards over the whole quote dropped 54 real
    dollar facts in the saved set.

    The denial is one-directional, and that too is how the pages read:

    - A row that declares the claim's own FAMILY has already had its say
      through the conversion. "Assets ($bn) 2.5" prints 2500 $m, so it denies a
      claim of 2.5 $m; "Movement in CET1 (bps) 12 34" denies 34 ppt.
    - A row that declares a RATIO or a rate denies a MONEY claim outright.
      "Net interest margin (%) 2.05 2.08" carries no dollar column, and reading
      its cells as dollars is what minted an invented 2.05 $m fact and left a
      driver at 95.
    - A row that declares MONEY does NOT deny a ratio claim: a bank prints the
      percentage change beside the dollar columns of the same row, under the
      one "($M)" header ("Corporate tax expense ($M) 4,699 4,491 5"). Denying
      it dropped 10 real change-column facts.
    """
    before = [family for position, family in declared if position < start]
    if not before:
        return False
    if any(_same_family(family, unit) for family in before):
        return True
    return normalize_unit(unit) in ("$m", "$bn")


def _converted_prints(quoted: float, quoted_unit: str, value: float, unit: str | None) -> bool:
    """Does a number the quote printed in ONE unit state this claim in another?

    The slack is the TIGHTER of the two units' own slack, both read in the
    claim's unit. A single tolerance taken from the claim's unit is wrong in
    both directions once a conversion sits between the two numbers: the
    citation slack for ppt is 0.1, which is TEN BASIS POINTS, so the sentence
    "Return on equity increased 10 basis points" grounded a component claim of
    +0.08 ppt and of +0.02 ppt at once — the whole movement was inside the
    slack. Read the other way, a "$2.5bn" quote carries 0.5 $bn of slack, which
    is $500m against a $m claim.

    A page prints a number to its own unit's precision, and a claim is stated
    to its own. Neither may be relaxed by the conversion between them.
    """
    converted = convert_unit(quoted, quoted_unit, unit)
    if converted is None:
        return False
    claim_tol = _tolerance_for(CITATION_TOL, unit, CITATION_TOL_DEFAULT)
    quoted_tol = convert_unit(
        _tolerance_for(CITATION_TOL, quoted_unit, CITATION_TOL_DEFAULT), quoted_unit, unit
    )
    tolerance = claim_tol if quoted_tol is None else min(claim_tol, quoted_tol)
    return abs(converted - abs(value)) <= tolerance


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
    declared = _declarations(quote)
    for quoted, quoted_unit in _quote_numbers(quote):
        if quoted_unit:
            if _converted_prints(quoted, quoted_unit, value, unit):
                return True
            continue
        if _declared_grounds(declared, quoted, value, unit):
            return True
    return False


def quote_prints(quote: str | None, value: float, unit: str | None = None) -> bool:
    """Does this quote print this magnitude at all?

    The value question, with the unit question asked only where the QUOTE
    answers it. `quote_states` asks whether a record GROUNDS a claim, and needs
    the quote to name the unit before any number in it counts. This asks the
    weaker question a model-supplied NumberFact has to pass before anything may
    rest on it: the agent's `cite` tool took those facts on trust, so an
    unrelated verbatim sentence could carry an invented {"value": 150,
    "unit": "$m"} and every check that reads record.numbers would then read a
    number no page prints.

    A number the quote prints BARE grounds the fact whatever unit the fact
    names, because a table cell prints no unit and the row is what says which
    unit it is in. A number the quote prints WITH a unit must convert into the
    fact's unit: the value check alone let "decreased 5 basis points" mint
    {"value": 5, "unit": "$m"}, and B3's conversion table then bound a unit the
    page never printed.

    A row does say which unit it is in, whenever it prints a header.
    "Net interest margin (%) 2.05 2.08" minted an invented {"value": 2.05,
    "unit": "$m"} off a percent cell, and the weak-citation cap then left a
    +2.05 $m driver at 95. So a bare number is read first in the units the
    quote declares, through UNIT_CONVERSIONS and through nothing else, and the
    row that denies the claim (`_declaration_refuses`) ends it there. A bare
    number under no unit signal at all is untouched: a plain table cell still
    grounds a claim of an unstated unit.
    """
    tolerance = _tolerance_for(CITATION_TOL, unit, CITATION_TOL_DEFAULT)
    declared = _declarations(quote)
    for quoted, quoted_unit, match in _scan_numbers(quote):
        if quoted_unit:
            if _converted_prints(quoted, quoted_unit, value, unit):
                return True
            continue
        if _declared_grounds(declared, quoted, value, unit):
            return True
        if _declaration_refuses(declared, match.start(1), unit):
            continue
        if abs(quoted - abs(value)) <= tolerance:
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


def _cap_drivers(attribution, tag: str, reason: str, applies=None) -> list[str]:
    """Cap every quantified driver above CLAIM_CITATION_CAP that `applies`
    selects (all of them when None), stamp `tag`, and record one limitation
    with `reason`. Mutates; returns what it capped. The cap never raises a
    confidence and never strips a claim. All three cap rules share this body,
    so a capped claim always reads the same in the artifact."""
    capped: list[str] = []
    for driver in attribution.drivers:
        if driver.contribution is None or driver.confidence <= CLAIM_CITATION_CAP:
            continue
        if applies is not None and not applies(driver):
            continue
        driver.confidence = CLAIM_CITATION_CAP
        driver.checks_passed.append(tag)
        capped.append(
            f"{driver.canonical} {driver.contribution.value:+g} {driver.contribution.unit}"
        )
    if capped:
        attribution.limitations.append(
            f"Capped at {CLAIM_CITATION_CAP}: " + ", ".join(capped) + ". " + reason
        )
    return capped


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
    by_id = {record.id: record for record in attribution.evidence_records}

    def unread(driver) -> bool:
        value = abs(driver.contribution.value)
        unit = driver.contribution.unit
        tolerance = _tolerance_for(CITATION_TOL, unit, CITATION_TOL_DEFAULT)
        cited = [by_id[e] for e in driver.evidence if e in by_id]
        return not (
            any(
                _states(number.value, number.unit, value, unit, tolerance)
                for record in cited
                for number in record.numbers
            )
            or any(quote_states(record.quote, value, unit) for record in cited)
        )

    return _cap_drivers(
        attribution, "computed_delta_cap_80",
        "The records these claims cite do not state those numbers, so each one is "
        "arithmetic over the evidence rather than a figure read from it.",
        applies=unread,
    )


def check_drivers_reconcile(attribution) -> tuple[list[str], list[str]]:
    """Quantified drivers + residual should sum to the movement delta.

    The SUM is unit-typed as well as the tolerance. A unit-blind addition let a
    `+3 bps` bar reconcile a `$m` bridge: three basis points were added as
    three dollars-million. A contribution stated in another unit is a fact
    about something else, so it is named and it never enters the total.

    The RESIDUAL follows the same rule. An untyped residual was named in
    `drivers_unit_mismatch` and then added to the total anyway, so three basis
    points closed a dollar bridge and `drivers_reconcile` PASSED beside its own
    mismatch failure. A residual with NO unit makes no competing claim, so it
    is read in the movement's unit.
    """
    passed, failed = [], []
    if attribution.movement is None:
        return passed, failed
    unit = normalize_unit(attribution.movement.unit)
    contributions = [d.contribution for d in attribution.drivers if d.contribution]
    off_unit = [c for c in contributions if normalize_unit(c.unit) != unit]
    residual_fact = attribution.residual
    residual_in_unit = residual_fact is not None and normalize_unit(residual_fact.unit) in ("", unit)
    if residual_fact is not None and not residual_in_unit:
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
    residual = residual_fact.value if residual_in_unit else 0.0
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


def check_ratio_level(movement, metric_unit: str | None = None) -> tuple[list[str], list[str]]:
    """A ratio movement's endpoints must be ratio-sized.

    Every other check is self-consistent at the wrong scale, so a ppt metric
    whose endpoints arrive in BASIS POINTS passes them all: the arithmetic
    holds (1160 - 20 = 1140), the drivers reconcile at that same scale, and
    settle_identity_scale's guard needs a contribution larger than the level,
    which 1160 never is. A unit-typed tolerance is only as good as the unit
    LABEL, so this check asks whether the label fits the number.

    The gate is the METRIC's unit, which the taxonomy fixes, exactly as it is
    in settle_ratio_scale. Keyed on the movement's unit, which the model
    writes, the check went silent on the very submission it exists for: an ROE
    of "1160 -> 1140" labelled "bps" is not a ratio unit, so nothing asked
    whether 1160 is the level of a ratio. `metric_unit` defaults to the
    movement's own unit for a caller that has no taxonomy to hand.
    """
    passed, failed = [], []
    if movement is None:
        return passed, failed
    gate = normalize_unit(metric_unit) if metric_unit else normalize_unit(movement.unit)
    if gate not in RATIO_UNITS:
        return passed, failed
    level = max(abs(movement.from_value), abs(movement.to_value))
    if level > RATIO_LEVEL_CEILING:
        failed.append(
            f"movement_level_not_ratio_sized ({level:g} is not the level of a ratio stated in "
            f"{gate}; the ceiling is {RATIO_LEVEL_CEILING:g}. A ratio of 11.6 per cent is 11.6 "
            "in points and 1160 in basis points: read the endpoints in the metric's own unit, "
            "and convert a change column printed in basis points by dividing it by 100)"
        )
    else:
        passed.append("movement_level_is_ratio_sized")
    return passed, failed


def settle_ratio_scale(attribution, metric_unit: str | None, records=None) -> str | None:
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

    The gate is the METRIC's unit, which the taxonomy fixes, and never the
    movement's unit, which the model writes. Keyed on the model's label this
    corrector REVERSED the percent-to-bps lift: a CET1 movement the model had
    labelled "%" was lifted 12.20 -> 1220 by the lift, seen as a ratio unit
    here, and divided straight back. Every check then passed, because the
    endpoints, the delta and the level are all self-consistent at either scale,
    and the artifact shipped +0.1 % against a gold of +10 bps under two
    limitations that contradicted each other.
    """
    movement = attribution.movement
    if movement is None or normalize_unit(metric_unit) not in RATIO_UNITS:
        return None
    records = attribution.evidence_records if records is None else records
    frm, to = movement.from_value / IDENTITY_SCALE, movement.to_value / IDENTITY_SCALE
    if not (_percent_evidenced(frm, records) and _percent_evidenced(to, records)):
        return None
    # The UNIT is settled with the numbers, because the two travel together and
    # this corrector is the one thing that knows both. An ROE submitted as
    # "1160 -> 1140, -20, bps" against a ppt metric came out of here as
    # "11.6 -> 11.4, -0.2, bps" — the gold movement, written in a unit 100x out
    # — and every downstream check then keyed off the retained label:
    # check_ratio_level saw a non-ratio unit and stayed silent, and the scorer
    # read the answer in basis points. A movement restated on the metric's own
    # scale is stated in the metric's own unit.
    was = movement.unit
    settled = normalize_unit(metric_unit)
    note = (
        f"Movement endpoints converted from basis points ({movement.from_value:g}, "
        f"{movement.to_value:g}) to {settled}: the evidence prints this ratio as "
        f"{frm:g}% and {to:g}%, and the unit for this metric is {settled}. "
        "A change column printed in basis points is divided by 100 to enter a movement "
        "stated in points."
    )
    if normalize_unit(was) != settled:
        note += f" The movement's unit is restated with its numbers ({was} -> {settled})."
    movement.from_value, movement.to_value = round(frm, 4), round(to, 4)
    movement.delta = round(movement.delta / IDENTITY_SCALE, 4)
    movement.unit = settled
    attribution.limitations.append(note)
    return note


# The failures that condemn the WHOLE quantified driver table rather than one
# claim. A bridge that does not close proves that one contribution is wrong and
# not which one; a movement read at the wrong scale, or one whose own three
# numbers disagree, is a movement the whole table was written against. Either
# way code cannot name the offender, so every quantified claim loses its right
# to near-certainty.
#
# `drivers_unit_mismatch` is here for the same reason as `drivers_reconcile`:
# a contribution in a foreign unit is dropped from the sum, so the bridge that
# "closed" was never closed, and code cannot say which of the remaining shares
# is carrying the gap.
#
# `comparison_leak` and `component_from_prior_half` are here because no named
# cap survives: `comparison_leak_cap_80` and `component_column_cap_80` fired on
# 0 of the 90 saved artifacts, so neither carried evidence under the
# hardcoded-override policy. Without these two names nothing caps the offender
# at all — a driver the check proves wrong shipped at 95 and entered the
# confidently-wrong population. EVIDENCE: the repro is synthetic —
# tests/test_review_round5.py (Codex round-5 finding 2) builds the failing
# driver and asserts the cap; no saved artifact fires either check, and with
# both names present evals/results/round6-check.jsonl is byte-identical to
# evals/results/pre-cleanup-baseline.jsonl (the .md pair differs only in the
# run-timestamp title). The whole table pays because the failure indicts the
# COLUMN the table was read from — a walk for another comparison, or the prior
# half's column — and one driver reading the wrong column is evidence its
# neighbours were read the same way.
#
# `walk_sum` and `walk_extraction_error` are absent for a different reason.
# They indict the CHART READ, not the driver table: the bars extracted off a
# slide do not sum to that slide's own endpoints, which says the vision read
# is unsafe and says nothing about a driver grounded in a table or in prose.
# The load-bearing rule in each shell already decides when a failed walk is
# fatal at all, and the no-primary-walk rule already caps every driver at 85
# when no usable walk covers the comparison. A blanket cap here would lower a
# driver whose evidence never touched the chart.
WHOLE_TABLE_FAILURES = (
    "drivers_reconcile",
    "drivers_unit_mismatch",
    "movement_arithmetic",
    "movement_level_not_ratio_sized",
    "comparison_leak",
    "component_from_prior_half",
)


def cap_unreconciled_drivers(attribution, failures: list[str]) -> list[str]:
    """Carry a fatal check down to the DRIVERS. Mutates; returns what it capped.

    The calibration metrics read the DRIVER's confidence, so a failed check
    that lowers `attribution_confidence` alone is invisible to the Brier score
    and the confidently-wrong rate: 22 saved artifacts carry a "Failed check"
    limitation and ship drivers at 80-90, and the suite's one confidently-wrong
    claim is exactly this — a bridge that failed drivers_reconcile, an answer
    that declared 40, and the offending driver still at 85.
    """
    hits = [f for f in failures if any(f.startswith(name) for name in WHOLE_TABLE_FAILURES)]
    if not hits:
        return []
    return _cap_drivers(
        attribution, "unreconciled_bridge_cap_80",
        hits[0].split(" (")[0]
        + " failed. That check condemns the whole quantified table: it proves one of "
        "these claims is wrong, or that the table was read from the wrong column, "
        "without saying which claim carries the fault. None of them may claim "
        "near-certainty.",
    )


def cap_drivers_on_failed_walks(attribution, walks) -> list[str]:
    """Cap a driver whose cited walk did not sum. Mutates; returns what it capped.

    A failed `walk_sum` indicts the CHART READ, not the driver table, so it is
    not a whole-table failure: the saved set holds a NIM run where one driver
    of seven cites the broken walk and the other six cite prose, and a blanket
    cap would lower all seven. It is not nothing either: the same set holds a
    CET1 run whose five drivers ALL cite one walk record whose bars miss that
    chart's own endpoints by 28 bps, and every one of them shipped at 85.

    So the rule is the same one `check_comparison_leak` follows — a check that
    can NAME its offender caps the offender. A walk carries the id of the
    record it minted, and a driver names the records it cites, so the drivers
    resting on a self-contradicting chart read are exactly nameable.

    This runs whether or not the failure was graded load-bearing for the
    ANSWER. That grading asks whether the walk carries the whole attribution;
    this asks whether the walk carries THIS claim, and a claim read off a chart
    that disagrees with itself is not a reading anybody may certify at 85.
    """
    broken = {
        walk.get("record_id")
        for walk in walks or []
        if walk.get("checks_failed") and walk.get("record_id")
    }
    if not broken:
        return []
    return _cap_drivers(
        attribution, "failed_walk_cap_80",
        "Each of these claims cites a walk whose own bars do not sum to that chart's "
        "endpoints, so the read it rests on disagrees with itself.",
        applies=lambda driver: bool(broken.intersection(driver.evidence or [])),
    )
