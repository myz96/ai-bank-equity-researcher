"""Orchestration shell A: the Python pipeline with one bounded
evidence-request loop (ticket 07)."""

from __future__ import annotations

import json
import re
import time
from datetime import datetime, timezone

from .author import author_attribution
from .config import COMBOS, OUT_DIR, REGISTRY_DIR
from .corpus import Document, documents_for_period
from .extract import extract_text_evidence, extract_walk
from .llm import LLM
from .render import render_report
from .retrieve import retrieve
from .schema import Attribution
from .taxonomy import METRIC_ALIASES, TAXONOMY
from .validate import (
    MONTH_NUMBERS,
    annotate_walks,
    check_comparison_leak,
    check_drivers_reconcile,
    check_movement,
    check_movement_columns,
    check_movement_variant,
    check_walk,
    corroborate,
    cross_source_view,
    implied_residual,
    period_end_date,
    walks_for_view,
)

MAX_TEXT_PAGES = 14
# Text pages are also capped per document (ticket 25): the doc-type-ranked
# ordering let the FY26 Profit Announcement's ~20 candidate pages fill every
# slot, so the presentation's income and expense waterfall slides — the only
# pages carrying the bridge quantification — were never extracted. The cap
# keeps the source hierarchy (books still read first) while guaranteeing the
# lower-ranked documents a share of the budget.
MAX_TEXT_PAGES_PER_DOC = 7
# Per document, so the Profit Announcement cannot crowd out the presentation's
# walk — cross-document corroboration needs both framings extracted.
MAX_WALK_PAGES_PER_DOC = 2
MAX_WALK_PAGES = 4


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


def run_case(bank: str, metric: str, period: str, comparator: str | None, combo_name: str = "cheap"):
    started = time.time()
    combo = COMBOS[combo_name]
    llm = LLM()
    metric_key = METRIC_ALIASES[metric.lower()]
    metric_cfg = TAXONOMY[metric_key]
    comparator = comparator or default_comparator(period)
    case = {"bank": bank, "metric": metric_key, "period": period, "comparator": comparator}
    case_desc = f"{bank} {metric_cfg['name']} in {period} vs {comparator}"
    # Derived metrics (ROE, CTI) need their identity INPUTS extracted too; a
    # literal-minded extractor otherwise drops profit/equity rows as
    # irrelevant to "return on equity" (ticket 25 follow-up).
    if metric_cfg.get("extract_focus"):
        case_desc += f" ({metric_cfg['extract_focus']})"

    registry_path = REGISTRY_DIR / f"{bank.lower()}.json"
    registry = json.loads(registry_path.read_text()) if registry_path.exists() else {}
    calendar = registry.get("calendar", {})
    period_note = build_period_note(period, comparator, calendar)
    period_date = period_end_date(period, calendar)
    comparator_date = period_end_date(comparator, calendar)
    prior_half_date = None
    if period_date:
        prior_half_date = (
            (period_date[0] - 6, period_date[1]) if period_date[0] > 6
            else (period_date[0] + 6, period_date[1] - 1)
        )
        if prior_half_date == comparator_date:
            prior_half_date = None
    # The text extractor gets the balance dates so it labels each period column
    # by its own date; the WALK reader deliberately does not, because it must
    # copy the endpoint labels off the chart rather than echo the task's
    # periods — code classifies the walk from those labels (defect 24).
    text_case_desc = f"{case_desc}\n{period_note}"
    # The bank's own name for this metric's headline row, when the registry
    # records one; used to tell the headline measure from a named variant.
    headline_label = registry.get("measures", {}).get(
        {"cti": "cti_label", "roe": "roe_label", "impairment": "impairment_line"}.get(metric_key, "")
    )

    docs = documents_for_period(bank, period, comparator)
    if not docs:
        raise RuntimeError(f"no documents in corpus for {bank} {period}/{comparator}")

    # 1. Retrieve candidate pages per query, per document, keeping scores.
    candidates: dict[tuple[str, int], float] = {}
    doc_by_id: dict[str, Document] = {d.doc_id: d for d in docs}
    for query in metric_cfg["retrieval_queries"]:
        for doc in docs:
            for page, score in retrieve(doc, query, top_k=4):
                key = (doc.doc_id, page)
                candidates[key] = max(candidates.get(key, 0.0), score)

    # 2. Walk pages come from a deterministic marker scan over the
    # current-period documents (retrieval luck must not decide walk coverage);
    # comparator-period walks join only if capacity remains.
    def scan_walks(period_filter: str) -> list[tuple[str, int]]:
        found = []
        for doc in docs:
            if doc.period != period_filter:
                continue
            per_doc = 0
            for i, text in enumerate(doc.page_texts()):
                if per_doc >= MAX_WALK_PAGES_PER_DOC:
                    break
                if any(marker.lower() in text.lower() for marker in metric_cfg["walk_markers"]):
                    found.append((doc.doc_id, i + 1))
                    per_doc += 1
        return found

    walk_pages = scan_walks(period)[:MAX_WALK_PAGES]
    if len(walk_pages) < MAX_WALK_PAGES:
        walk_pages += scan_walks(comparator)[: MAX_WALK_PAGES - len(walk_pages)]
    # Source hierarchy (defect 20): the results book's walk is primary; slide
    # walks corroborate. Books first, so the author reads them first.
    book_types = ("profit_announcement", "results_announcement", "results_book")
    walk_pages.sort(key=lambda dp: 0 if doc_by_id[dp[0]].doc_type in book_types else 1)
    # Page priority = (current period first, then the source hierarchy).
    # Alphabetical ordering starved authors twice: FY25 < FY26 lexically
    # (scorecard 1), then asx_announcement < profit_announcement put the
    # 4-page media release ahead of the results book (ticket 25).
    DOC_TYPE_RANK = {
        "profit_announcement": 0, "results_announcement": 0, "results_book": 0,
        "results_presentation": 1, "investor_presentation": 1, "investor_discussion_pack": 1,
        "asx_announcement": 2,
    }

    def page_order(dp: tuple[str, int]):
        doc = doc_by_id[dp[0]]
        return (
            0 if doc.period == period else 1,
            DOC_TYPE_RANK.get(doc.doc_type, 3),
            -candidates.get(dp, 0.0),
            dp[1],
        )

    text_pages: list[tuple[str, int]] = []
    pages_per_doc: dict[str, int] = {}
    for dp in sorted(candidates, key=page_order):
        if dp in set(walk_pages) or pages_per_doc.get(dp[0], 0) >= MAX_TEXT_PAGES_PER_DOC:
            continue
        text_pages.append(dp)
        pages_per_doc[dp[0]] = pages_per_doc.get(dp[0], 0) + 1
        if len(text_pages) >= MAX_TEXT_PAGES:
            break

    # 3. Extract evidence.
    counter = iter(range(1, 1000))
    next_id = lambda: f"ev-{next(counter)}"  # noqa: E731
    records, walks, validation = [], [], {"passed": [], "failed": []}
    for doc_id, page in walk_pages:
        try:
            walk, record = extract_walk(
                llm, combo.vision, doc_by_id[doc_id], page, case_desc, next_id,
                unit=metric_cfg["unit"],
            )
        except Exception as exc:  # noqa: BLE001
            validation["failed"].append(f"walk_extraction_error p{page}: {exc}")
            continue
        passed, failed = check_walk(walk, doc_by_id[doc_id].doc_type)
        walk["source"] = f"{doc_id} PDF p{page} ({record.id})"
        walk["record_id"] = record.id
        walk["checks_passed"] = passed
        walk["checks_failed"] = [f"{f} [{walk['source']}]" for f in failed]
        validation["passed"] += passed
        validation["failed"] += walk["checks_failed"]
        walks.append(walk)
        records.append(record)
    # Classify each walk against the case comparison before the author sees it,
    # then put the task-comparison walks first: the author reads in order, and
    # the source hierarchy only decides between walks of the SAME comparison.
    annotate_walks(walks, calendar, period, comparator)
    walks.sort(key=lambda w: 0 if w.get("comparison") == "primary" else 1)
    # Walk pages also get text extraction: the narrative beside a walk carries
    # the explanations and caveats (defect 22), and some banks (ANZ) publish
    # the driver decomposition as bulleted text rather than a chart.
    for doc_id, page in text_pages + walk_pages:
        records.extend(
            extract_text_evidence(llm, combo.extract, doc_by_id[doc_id], page, text_case_desc, next_id)
        )

    # 4. The bounded evidence-request hook.
    def fetch_more(query: str):
        extra = []
        for doc in docs:
            for page, score in retrieve(doc, query, top_k=2):
                if (doc.doc_id, page) not in candidates:
                    candidates[(doc.doc_id, page)] = score
                    extra.extend(extract_text_evidence(llm, combo.extract, doc, page, text_case_desc, next_id))
        return extra

    # 4b. The cross-source view: walk bars mapped to canonical drivers across
    # documents, so the author sees corroboration before writing. Only walks of
    # ONE comparison are pooled (defect 24) — a half-on-half bar beside a
    # full-year bar is a different question, not a disagreeing source.
    label_map = registry.get(f"{metric_key}_walk_labels", {})
    primary_walks = [w for w in walks if w.get("comparison") == "primary"]
    # "unclassified" means the endpoint labels named no period — the cold path
    # for an unseen bank, whose registry (and calendar) is deleted on purpose.
    # It is not evidence of a different comparison, so those walks drive
    # neither the leak check nor the confidence cap below.
    context_walks = [w for w in walks if w.get("comparison") == "context"]
    classified = primary_walks + context_walks
    view_walks, view_note = walks_for_view(walks)
    cross_source = cross_source_view(view_walks, label_map)
    primary_view = cross_source_view(primary_walks, label_map)
    context_view = cross_source_view(context_walks, label_map)
    validation["cross_source_view"] = {"comparison": view_note, "drivers": cross_source}
    if context_view:
        validation["other_comparison_walks"] = {
            "warning": "These bars belong to a DIFFERENT comparison. Context only.",
            "drivers": context_view,
        }

    # 5. Author, with one retry if output-level validation fails: the failure
    # text goes back to the author so it can correct or declare a residual.
    author_validation = dict(validation)
    attribution = None
    for attempt in range(2):
        attribution = author_attribution(
            llm,
            combo.author,
            max_tokens=combo.author_max_tokens,
            case=case,
            taxonomy=metric_cfg,
            registry=registry,
            evidence_records=records,
            walks=walks,
            validation=author_validation,
            fetch_more=fetch_more,
            period_note=period_note,
        )
        output_failures = (
            check_movement(attribution.movement)[1]
            + check_drivers_reconcile(attribution)[1]
            + check_comparison_leak(attribution, primary_view, context_view)[1]
            + check_movement_columns(
                attribution, period_date, comparator_date, prior_half_date
            )[1]
            + check_movement_variant(attribution, headline_label)[1]
        )
        if not output_failures or attempt == 1:
            break
        author_validation = {
            **validation,
            "your_previous_answer_failed": output_failures,
            "instruction": "Fix these failures: use the walk matching the task periods, "
            "or declare a residual and lower confidence. Do not force numbers.",
        }
        # Residual assist (ticket 27): hand back the arithmetic, not just the
        # verdict. The model recomputed the residual wrongly a second time when
        # it only saw "drivers_reconcile failed".
        residual = implied_residual(attribution)
        if residual is not None and any(f.startswith("drivers_reconcile") for f in output_failures):
            author_validation["code_computed_implied_residual"] = (
                f"{residual:+.2f} {metric_cfg['unit']}. This is the movement delta minus the sum "
                "of the contributions you claimed. Either declare exactly this value as the "
                "residual, or correct the contributions so they reconcile. Do not invent a "
                "third number."
            )

    # 6. Corroboration annotation, then output-level validation.
    corroborate(attribution, cross_source)
    output_failed: list[str] = []
    drivers_passed, drivers_failed = check_drivers_reconcile(attribution)
    for check in (
        check_movement(attribution.movement),
        (drivers_passed, drivers_failed),
        check_comparison_leak(attribution, primary_view, context_view),
        check_movement_columns(attribution, period_date, comparator_date, prior_half_date),
        check_movement_variant(attribution, headline_label),
    ):
        validation["passed"] += check[0]
        output_failed += check[1]
    # Graded cap (defect 23): output-level failures are always fatal;
    # extraction/walk failures are fatal only when nothing else validated —
    # a broken read of a peripheral page must not sink a validated answer.
    peripheral = [f for f in validation["failed"] if f.startswith("walk_extraction_error")]
    # Load-bearing grading of walk_sum failures (ticket 27). A walk_sum failure
    # is fatal only when the drivers rest on the walk that failed. The failing
    # walk is load-bearing when BOTH hold:
    #   1. it is classified primary — a walk of a different comparison never
    #      supplies this period's driver table (defect 24), so its misread bars
    #      cannot corrupt the answer; and
    #   2. no sibling primary walk passed its own sum check, or the author's
    #      claims do not reconcile with the movement — either condition means
    #      no validated decomposition of this comparison survives.
    # Otherwise the failure is a peripheral secondary read: it stays visible as
    # a limitation, but it must not cap confidence on an answer that validated
    # by another route (nim FY26 scored 7/7 recall and precision while a
    # secondary misread capped it at 40).
    primary_sum_ok = any(
        "walk_sum" in walk.get("checks_passed", []) for walk in primary_walks
    )
    for walk in walks:
        if not walk.get("checks_failed"):
            continue
        load_bearing = walk.get("comparison") == "primary" and not (
            primary_sum_ok and "drivers_reconcile" in drivers_passed
        )
        if not load_bearing:
            peripheral += walk["checks_failed"]
    fatal = output_failed + [f for f in validation["failed"] if f not in peripheral]
    # For arithmetic-derivation metrics (ROE, CTI) full driver quantification
    # is often genuinely undisclosed; an honest unquantified attribution is
    # not a fatal failure there (it stays visible as a limitation). The same
    # holds for a walk metric whose walk covers another comparison: borrowing
    # that walk's bars would be the defect-24 error, so leaving the drivers
    # unquantified is the correct answer, not a failure to punish.
    honest_partial: list[str] = []
    if metric_cfg["method"] == "two_level_arithmetic" or (
        metric_cfg["method"] == "walk_extraction" and classified and not primary_walks
    ):
        fatal = [f for f in fatal if f != "no_quantified_drivers"]
        honest_partial += [f for f in output_failed if f == "no_quantified_drivers"]
    # The escalation below covers WALK failures only: "a broken read sinks the
    # answer when no other walk validated". It must not reach the honest
    # partial above, because ROE and CTI publish no walk at all — running it
    # over them cancelled the exemption the line before had just granted.
    if peripheral and "walk_sum" not in validation["passed"]:
        fatal += peripheral
        peripheral = []
    peripheral += honest_partial
    validation["failed"] += output_failed
    if fatal or peripheral:
        attribution.limitations.extend(f"Failed check: {f}" for f in fatal + peripheral)
    if fatal:
        # Overconfidence cap: an attribution whose load-bearing checks fail
        # cannot claim high confidence, whatever the model said (ticket 02/07).
        attribution.attribution_confidence = min(attribution.attribution_confidence, 40)
    elif metric_cfg["method"] == "walk_extraction" and classified and not primary_walks:
        # Evidence-ladder cap (defect 24), the CBA CET1 case: the bank
        # publishes only a half-on-half CET1 walk, so a full-year or
        # prior-corresponding-period driver table rests on another
        # comparison's bars or on narrative. Prompt rule 4 reserves >=90 for a
        # bar backed by a walk of THIS comparison; this makes it mechanical, so
        # a mis-sourced claim can no longer certify itself at 100.
        attribution.limitations.append(
            f"No published walk covers {period} vs {comparator}: the bank's walk for this "
            "metric describes another comparison, so the driver split is not walk-verified "
            "for this comparison. Confidence is capped at 85."
        )
        attribution.attribution_confidence = min(attribution.attribution_confidence, 85)
        for driver in attribution.drivers:
            driver.confidence = min(driver.confidence, 85)

    attribution.provenance = {
        "combo": combo.name,
        "models": f"extract={combo.extract}, vision={combo.vision}, author={combo.author}",
        "documents": ", ".join(f"{d.doc_id} ({(d.sha256 or '')[:12]})" for d in docs),
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "seconds": round(time.time() - started, 1),
        "cost_usd": round(llm.usage.cost_usd, 4),
        "tokens": f"{llm.usage.prompt_tokens} in / {llm.usage.completion_tokens} out",
        "orchestration": "pipeline",
    }

    # 7. Save.
    slug = f"{bank}-{metric_key}-{period}-vs-{comparator}-{combo.name}".lower()
    out = OUT_DIR / slug
    out.mkdir(parents=True, exist_ok=True)
    (out / "attribution.json").write_text(attribution.model_dump_json(indent=2))
    (out / "report.md").write_text(render_report(attribution))
    return attribution, out


__all__ = ["run_case", "default_comparator", "Attribution"]
