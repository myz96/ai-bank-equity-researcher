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
from .validate import check_drivers_reconcile, check_movement, check_walk, corroborate, cross_source_view

MAX_TEXT_PAGES = 8
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


def run_case(bank: str, metric: str, period: str, comparator: str | None, combo_name: str = "cheap"):
    started = time.time()
    combo = COMBOS[combo_name]
    llm = LLM()
    metric_key = METRIC_ALIASES[metric.lower()]
    metric_cfg = TAXONOMY[metric_key]
    comparator = comparator or default_comparator(period)
    case = {"bank": bank, "metric": metric_key, "period": period, "comparator": comparator}
    case_desc = f"{bank} {metric_cfg['name']} in {period} vs {comparator}"

    registry_path = REGISTRY_DIR / f"{bank.lower()}.json"
    registry = json.loads(registry_path.read_text()) if registry_path.exists() else {}

    docs = documents_for_period(bank, period, comparator)
    if not docs:
        raise RuntimeError(f"no documents in corpus for {bank} {period}/{comparator}")

    # 1. Retrieve candidate pages per query, per document.
    candidates: set[tuple[str, int]] = set()
    doc_by_id: dict[str, Document] = {d.doc_id: d for d in docs}
    for query in metric_cfg["retrieval_queries"]:
        for doc in docs:
            for page in retrieve(doc, query, top_k=4):
                candidates.add((doc.doc_id, page))

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
    text_pages = [
        (doc_id, page) for doc_id, page in sorted(candidates) if (doc_id, page) not in set(walk_pages)
    ][:MAX_TEXT_PAGES]

    # 3. Extract evidence.
    counter = iter(range(1, 1000))
    next_id = lambda: f"ev-{next(counter)}"  # noqa: E731
    records, walks, validation = [], [], {"passed": [], "failed": []}
    for doc_id, page in walk_pages:
        try:
            walk, record = extract_walk(llm, combo.vision, doc_by_id[doc_id], page, case_desc, next_id)
        except Exception as exc:  # noqa: BLE001
            validation["failed"].append(f"walk_extraction_error p{page}: {exc}")
            continue
        passed, failed = check_walk(walk, doc_by_id[doc_id].doc_type)
        walk["source"] = f"{doc_id} PDF p{page} ({record.id})"
        walk["checks_passed"], walk["checks_failed"] = passed, failed
        validation["passed"] += passed
        validation["failed"] += failed
        walks.append(walk)
        records.append(record)
    # Walk pages also get text extraction: the narrative beside a walk carries
    # the explanations and caveats (defect 22), and some banks (ANZ) publish
    # the driver decomposition as bulleted text rather than a chart.
    for doc_id, page in text_pages + walk_pages:
        records.extend(
            extract_text_evidence(llm, combo.extract, doc_by_id[doc_id], page, case_desc, next_id)
        )

    # 4. The bounded evidence-request hook.
    def fetch_more(query: str):
        extra = []
        for doc in docs:
            for page in retrieve(doc, query, top_k=2):
                if (doc.doc_id, page) not in candidates:
                    candidates.add((doc.doc_id, page))
                    extra.extend(extract_text_evidence(llm, combo.extract, doc, page, case_desc, next_id))
        return extra

    # 4b. The cross-source view: every walk bar mapped to canonical drivers,
    # across documents, so the author sees corroboration before writing.
    label_map = registry.get(f"{metric_key}_walk_labels", {})
    cross_source = cross_source_view(walks, label_map)
    validation["cross_source_view"] = cross_source

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
        )
        output_failures = check_movement(attribution.movement)[1] + check_drivers_reconcile(attribution)[1]
        if not output_failures or attempt == 1:
            break
        author_validation = {
            **validation,
            "your_previous_answer_failed": output_failures,
            "instruction": "Fix these failures: use the walk matching the task periods, "
            "or declare a residual and lower confidence. Do not force numbers.",
        }

    # 6. Corroboration annotation, then output-level validation.
    corroborate(attribution, cross_source)
    for check in (check_movement(attribution.movement), check_drivers_reconcile(attribution)):
        validation["passed"] += check[0]
        validation["failed"] += check[1]
    if validation["failed"]:
        attribution.limitations.extend(f"Failed check: {f}" for f in validation["failed"])
        # Overconfidence cap: an attribution whose checks fail cannot claim
        # high confidence, whatever the model said (ticket 02/07).
        attribution.attribution_confidence = min(attribution.attribution_confidence, 40)

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
