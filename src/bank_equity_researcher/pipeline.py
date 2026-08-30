"""Orchestration shell A: the Python pipeline with one bounded
evidence-request loop (ticket 07)."""

from __future__ import annotations

import json
import re
import time
from datetime import datetime, timezone

from .author import author_attribution, primary_basis
from .config import COMBOS, OUT_DIR, REGISTRY_DIR
from .corpus import Document, documents_for_period
from .extract import (
    WALK_PAGE_HINT,
    extract_text_evidence,
    extract_walk,
    extract_walk_annotations,
)
from .llm import LLM
from .refs import extraction_hint, follow_references
from .render import render_report
from .retrieve import retrieve
from .schema import Attribution
from .taxonomy import METRIC_ALIASES, TAXONOMY
from .validate import (
    MONTH_NUMBERS,
    annotate_walks,
    cap_weakly_cited_claims,
    check_comparison_leak,
    check_component_columns,
    check_drivers_reconcile,
    check_movement,
    check_movement_basis,
    check_movement_columns,
    check_movement_variant,
    check_walk,
    corroborate,
    cross_source_view,
    half_label,
    implied_residual,
    period_end_date,
    settle_identity_scale,
    unclaimed_components,
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
    # The tag a table prints for the prior-half column when it uses tags
    # instead of dates ("2H25" beside "1H26" on a slide).
    prior_half_tag = half_label(prior_half_date, calendar)
    # The text extractor gets the balance dates so it labels each period column
    # by its own date; the WALK reader deliberately does not, because it must
    # copy the endpoint labels off the chart rather than echo the task's
    # periods — code classifies the walk from those labels (defect 24).
    text_case_desc = f"{case_desc}\n{period_note}"
    # The bank's own name for this metric's headline row, when the registry
    # records one. It is used twice: the author prompt NAMES it, so the model
    # does not have to guess which of several adjacent rows the bank headlines
    # (Westpac headlines ROTE ex Notable Items, and the author read the plainer
    # "Return on average ordinary equity" one line above it); and
    # check_movement_variant reads it to tell the headline measure from a
    # named variant.
    # cash_earnings maps to core_profit: Westpac dropped cash earnings at 1H23
    # and headlines "net profit excluding Notable Items", so an author told only
    # the metric's generic name reads the statutory row four lines above it.
    headline_label = registry.get("measures", {}).get(
        {
            "cash_earnings": "core_profit",
            "cti": "cti_label",
            "roe": "roe_label",
            "impairment": "impairment_line",
        }.get(metric_key, "")
    )
    # The basis the bank itself reports on, from the same registry vocabulary.
    # check_movement_basis uses it to catch a movement read from the statutory
    # block of a KPI page that prints the same row under both bases.
    bank_basis = primary_basis(registry) if registry.get("measures") else None

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

    # 2b. Reference following (ticket 22). Retrieval ranks a page by how much
    # it looks like the question, and the why-layer does not: the bank puts it
    # in an appendix note, on a footnote target, or on the next page of a table
    # that broke over the page end. A deterministic scan of the pages already
    # chosen finds the markers that point at those pages and turns to them.
    followed = follow_references(
        doc_by_id,
        [*text_pages, *walk_pages],
        metric_cfg["retrieval_queries"] + [metric_cfg["name"]],
    )
    follow_by_page = {(f.doc_id, f.page): f for f in followed}
    chosen = set(text_pages) | set(walk_pages)
    followed_pages = [(f.doc_id, f.page) for f in followed if (f.doc_id, f.page) not in chosen]

    # 3. Extract evidence.
    counter = iter(range(1, 1000))
    next_id = lambda: f"ev-{next(counter)}"  # noqa: E731
    records, walks, validation = [], [], {"passed": [], "failed": []}
    for doc_id, page in walk_pages:
        bar_labels: tuple[str, ...] = ()
        try:
            walk, record = extract_walk(
                llm, combo.vision, doc_by_id[doc_id], page, case_desc, next_id,
                unit=metric_cfg["unit"],
            )
        except Exception as exc:  # noqa: BLE001
            validation["failed"].append(f"walk_extraction_error p{page}: {exc}")
        else:
            passed, failed = check_walk(
                walk, doc_by_id[doc_id].doc_type, metric_cfg["unit"]
            )
            walk["source"] = f"{doc_id} PDF p{page} ({record.id})"
            walk["record_id"] = record.id
            walk["checks_passed"] = passed
            walk["checks_failed"] = [f"{f} [{walk['source']}]" for f in failed]
            validation["passed"] += passed
            validation["failed"] += walk["checks_failed"]
            walks.append(walk)
            records.append(record)
            bar_labels = tuple(str(bar.get("label", "")) for bar in walk.get("bars", []))
        # The chart's ANNOTATION layer, one extra vision call per walk page
        # (ticket 27, iteration 3). The callouts beside a walk hold the bank's
        # own sub-split of its bars, and the text layer prints their numbers
        # and their labels as two separate blocks, so nothing but a look at the
        # page can pair them. The read degrades to nothing on any failure, so a
        # page whose annotations are unreadable costs the case nothing.
        records.extend(
            extract_walk_annotations(
                llm, combo.vision, doc_by_id[doc_id], page, case_desc, next_id,
                unit=metric_cfg["unit"], bar_labels=bar_labels,
            )
        )
    # Classify each walk against the case comparison before the author sees it,
    # then put the task-comparison walks first: the author reads in order, and
    # the source hierarchy only decides between walks of the SAME comparison.
    annotate_walks(walks, calendar, period, comparator)
    # Deliberately NOT stamped: the comparison of the chart an annotation sits
    # on. A slide prints more than one chart of the same metric — the FY21
    # presentation puts the half-on-half margin chart and the full-year one on
    # one page, with the same bar labels — so a page-level comparison stamp
    # would assert a span the code cannot know. The record names its document,
    # its page and its kind, and rule 6 governs the rest.
    walks.sort(key=lambda w: 0 if w.get("comparison") == "primary" else 1)
    # Walk pages also get text extraction: the narrative beside a walk carries
    # the explanations and caveats (defect 22), and some banks (ANZ) publish
    # the driver decomposition as bulleted text rather than a chart.
    # One unreadable page must not crash the case: the answer then rests on the
    # pages that did read, and the lost page is declared as a limitation so the
    # gap is visible instead of silent (ticket 27).
    unread_pages = []
    walk_page_set = set(walk_pages)
    for doc_id, page in text_pages + walk_pages + followed_pages:
        # A followed page is read with the reference that reached it named in
        # the task, and its records carry that reference as provenance. A walk
        # page is read for the commentary beside the chart (defect 22).
        follow = follow_by_page.get((doc_id, page))
        hints = [WALK_PAGE_HINT] if (doc_id, page) in walk_page_set else []
        if follow is not None:
            hints.append(extraction_hint(follow))
        page_case = "\n".join([text_case_desc, *hints])
        try:
            records.extend(
                extract_text_evidence(
                    llm, combo.extract, doc_by_id[doc_id], page, page_case, next_id,
                    provenance=None if follow is None else follow.provenance,
                )
            )
        except Exception as exc:  # noqa: BLE001 - a lost page is a gap, not a crash
            unread_pages.append(f"{doc_id} p{page} ({type(exc).__name__})")

    # 4. The bounded evidence-request hook.
    def fetch_more(query: str):
        extra = []
        for doc in docs:
            for page, score in retrieve(doc, query, top_k=2):
                if (doc.doc_id, page) not in candidates:
                    candidates[(doc.doc_id, page)] = score
                    extra.extend(extract_text_evidence(llm, combo.extract, doc, page, text_case_desc, next_id))
        # The fetched records join the SHARED pool, not just this attempt's
        # copy of it. `candidates` is never reset, so the page can never be
        # fetched a second time; without this line attempt 2 lost every record
        # attempt 1 had asked for, and asked again to be told nothing. It also
        # made the citation cap misjudge a driver that cited a fetched record,
        # because the record was not in the pool the cap resolves against.
        records.extend(extra)
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
    # The component-column check mirrors the movement-column check one level
    # down, for bridge metrics only: a NIM walk's bars are read off a chart,
    # never subtracted from table columns, so the check has nothing to say
    # there (and replayed over saved NIM artifacts it false-fired).
    is_bridge = metric_cfg["method"] == "bridge_extraction"

    def component_checks(attribution) -> tuple[list[str], list[str]]:
        if not is_bridge:
            return [], []
        return check_component_columns(
            attribution, period_date, comparator_date, prior_half_date, prior_half_tag
        )

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
            headline_row=headline_label,
        )
        # Ratio-identity scale (ticket 27, iteration 3). ROE and CTI derive
        # their level-1 split from an identity, and an author that feeds a
        # growth rate printed in per cent into it — or a dollar movement that
        # never met its denominator — states the split 100x too large. The
        # numbers are corrected before any check reads them, and the retry
        # below asks for the headline to be rewritten on the same scale.
        scale_note = settle_identity_scale(attribution, metric_cfg["method"])
        output_failures = (
            check_movement(attribution.movement)[1]
            + check_drivers_reconcile(attribution)[1]
            + check_comparison_leak(attribution, primary_view, context_view)[1]
            + check_movement_columns(
                attribution, period_date, comparator_date, prior_half_date
            )[1]
            + check_movement_variant(attribution, headline_label)[1]
            + check_movement_basis(attribution, bank_basis, headline_label)[1]
            + component_checks(attribution)[1]
        )
        # Completeness nudge (ticket 27): a disclosed bridge component the
        # author left unclaimed is a recall gap, not a validation failure — it
        # drives one retry, never a confidence cap, and the nudge names the
        # component and its evidence ids only, never a value.
        missing_components = (
            unclaimed_components(attribution, metric_cfg.get("component_labels", {}))
            if is_bridge
            else []
        )
        if not (output_failures or missing_components or scale_note) or attempt == 1:
            break
        author_validation = {
            **validation,
            "your_previous_answer_failed": output_failures,
            "instruction": "Fix these failures: use the walk matching the task periods, "
            "or declare a residual and lower confidence. Do not force numbers.",
        }
        if scale_note:
            # The numbers are already corrected; this asks for one answer whose
            # PROSE agrees with them. Generic wording: it names the arithmetic,
            # never a value to reach.
            author_validation["identity_scale"] = (
                "Your quantified contributions did not sum to the movement at the scale you "
                "wrote them, and they do one factor of 100 down. A ratio identity is stated "
                "in the ratio's own unit: a growth rate enters it as a FRACTION (a fall of 2 "
                "per cent is -0.02, never -2), and a movement in dollars enters it divided by "
                "the identity's denominator. Rewrite every contribution AND the headline on "
                "the ratio's own scale. A contribution larger than the ratio itself is a "
                "scale error, not a driver."
            )
        if missing_components:
            author_validation["components_unclaimed"] = (
                "The evidence quantifies these bridge components and your answer leaves "
                "them unclaimed: " + "; ".join(missing_components) + ". Claim each one as "
                "a quantified contribution from its cited records (delta = the "
                f"{period} column minus the {comparator} column of that component's own "
                "row, or the movement the bank states against the comparator)."
            )
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
    # Evidence-ladder cap, made mechanical (ticket 27, widened in review round
    # 1). Prompt rule 4 caps a delta the model computed itself at 80; the model
    # does not always obey it. This ran for bridge metrics only, so impairment
    # (note_decomposition) and ROE/CTI (two_level_arithmetic) never faced it,
    # and the CBA FY26 impairment run shipped +150 / -17 / -71 at 85 citing
    # records that state none of those numbers.
    cap_weakly_cited_claims(attribution)
    if is_bridge:
        # Framing-uncertainty cap. A bank that prints BOTH an underlying and a
        # headline expense row publishes two valid framings of one component.
        # An author that claims the split (underlying expenses plus a separate
        # notable-items component) has made a framing choice the disclosure
        # itself does not settle, so neither claim may reach near-certainty.
        split = {
            d.canonical: d
            for d in attribution.drivers
            if d.contribution is not None
            and d.canonical in ("operating_expenses", "notable_items")
        }
        if len(split) == 2:
            for driver in split.values():
                driver.confidence = min(driver.confidence, 80)
            attribution.limitations.append(
                "Expenses are claimed on the underlying/notable split; the bank equally "
                "publishes the combined headline framing, so both claims are capped at 80."
            )
    output_failed: list[str] = []
    drivers_passed, drivers_failed = check_drivers_reconcile(attribution)
    for check in (
        check_movement(attribution.movement),
        (drivers_passed, drivers_failed),
        check_comparison_leak(attribution, primary_view, context_view),
        check_movement_columns(attribution, period_date, comparator_date, prior_half_date),
        check_movement_variant(attribution, headline_label),
        check_movement_basis(attribution, bank_basis, headline_label),
        component_checks(attribution),
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
    if unread_pages:
        attribution.limitations.append(
            "These pages could not be read and are missing from the evidence: "
            + "; ".join(unread_pages)
        )
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
    # Per-driver evidence-ladder cap, independent of the fatal branch above
    # (ticket 27, goal 3). When a walk metric has NO successfully extracted
    # primary walk, no driver claim is walk-verified for this comparison, so no
    # driver may exceed 85 — whatever the model said. The elif above already
    # caps the context-walk state, but it is skipped when the fatal cap fires
    # first: the outage run shipped derived drivers at 90 under an attribution
    # capped at 40. Walks that exist but are unclassified are exempt on
    # purpose — the cold path for an unseen bank whose calendar is absent is
    # not evidence the walk covers another comparison.
    if metric_cfg["method"] == "walk_extraction" and not primary_walks and (
        classified or not walks
    ):
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
        "pages_extracted": len(text_pages) + len(walk_pages) + len(followed_pages),
        "reference_follow": [
            f"{f.doc_id} p{f.page} <- p{f.source_page} {f.target}"
            + ("" if (f.doc_id, f.page) in chosen else " [added]")
            for f in followed
        ],
    }

    # 7. Save.
    slug = f"{bank}-{metric_key}-{period}-vs-{comparator}-{combo.name}".lower()
    out = OUT_DIR / slug
    out.mkdir(parents=True, exist_ok=True)
    (out / "attribution.json").write_text(attribution.model_dump_json(indent=2))
    (out / "report.md").write_text(render_report(attribution))
    return attribution, out


__all__ = ["run_case", "default_comparator", "Attribution"]
