"""Ticket 13 prototype: retrieval bake-off on the CBA corpus.

Arms:
  A. Section-map navigation (doc map built once by a cheap model; a navigator
     model picks pages from the map) — run per model.
  B. BM25 over pages (lexical baseline, no model calls).
  C. Dense embeddings over pages (local bge-small model).

Gold pages are located by distinctive marker strings, not hardcoded page
numbers, so drifted assumptions fail loudly.

Usage: uv run python prototypes/bakeoff.py
"""

from __future__ import annotations

import json
import re
import time
from pathlib import Path

import pymupdf

from openrouter_client import USAGE, chat, parse_json_block

REPO_ROOT = Path(__file__).resolve().parent.parent
PA = REPO_ROOT / "data/raw/CBA/FY26/CBA-FY26-profit-announcement.pdf"
PRES = REPO_ROOT / "data/raw/CBA/FY26/CBA-FY26-results-presentation.pdf"

NAV_MODELS = ["qwen/qwen3.7-flash", "stealth/ox-alpha"]
TOP_K = 8

# (target id, document, marker strings that identify the gold page(s), query)
TARGETS = [
    ("nim_walk_fy", "pa", ["NIM Movement since June 2025"],
     "The FY26 full-year net interest margin movement walk with driver contributions in basis points"),
    ("nim_walk_hoh", "pa", ["NIM Movement since December 2025"],
     "The half-on-half NIM movement from the December 2025 half to the June 2026 half"),
    ("profit_reconciliation", "pa", ["Profit Reconciliation"],
     "The line-by-line profit reconciliation between statutory and cash basis"),
    ("group_performance_summary", "pa", ["Group Performance Summary"],
     "The group performance summary table showing statutory and cash net profit side by side"),
    ("loan_impairment", "pa", ["Loan Impairment Expense"],
     "Loan impairment expense analysis by division and its drivers"),
    ("capital", "pa", ["Summary Group Capital Adequacy Ratios"],
     "Group capital adequacy ratios and the CET1 movement analysis"),
    ("expenses", "pa", ["Staff expenses"],
     "Operating expenses breakdown including staff, occupancy and technology expenses"),
    ("kpis", "pa", ["Key Performance Indicators"],
     "The key performance indicators table with cash and statutory ratios"),
    ("stat_vs_cash_slide", "pres", ["Statutory vs cash NPAT", "Statutory vs Cash NPAT"],
     "The slide reconciling statutory and cash NPAT"),
    ("margin_walk_slide", "pres", ["Group margin – 12 months"],
     "The twelve month group margin walk with driver bars in basis points"),
]


def page_texts(pdf_path: Path) -> list[str]:
    cache = REPO_ROOT / "data/cache/pages" / (pdf_path.stem + ".json")
    if cache.exists():
        return json.loads(cache.read_text())
    doc = pymupdf.open(pdf_path)
    texts = [page.get_text() for page in doc]
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(texts))
    return texts


def marker_hit(text: str, marker: str) -> bool:
    """Long markers match as substrings; short generic ones must be a whole line
    (a heading or a table label), which keeps gold sets tight."""
    if len(marker) >= 25:
        return marker.lower() in text.lower()
    return any(line.strip().lower() == marker.lower() for line in text.splitlines())


def locate_gold(texts: list[str], markers: list[str]) -> tuple[set[int], set[int]]:
    """Return (gold pages, contents pages excluded). 1-based page numbers."""
    per_target_hits = []
    for _, _, target_markers, _ in TARGETS:
        per_target_hits.append({
            i + 1 for i, text in enumerate(texts) if any(marker_hit(text, m) for m in target_markers)
        })
    contents = {
        page
        for page in set().union(*per_target_hits)
        if sum(page in hits for hits in per_target_hits) >= 4
    }
    gold = {
        i + 1
        for i, text in enumerate(texts)
        if any(marker_hit(text, m) for m in markers) and (i + 1) not in contents
    }
    return gold, contents


def page_digest(texts: list[str]) -> str:
    lines = []
    for i, text in enumerate(texts):
        head = " | ".join([ln.strip() for ln in text.splitlines() if ln.strip()][:4])[:160]
        lines.append(f"p{i + 1}: {head}")
    return "\n".join(lines)


def build_map(model: str, doc_name: str, texts: list[str]) -> str:
    cache = REPO_ROOT / "data/cache/maps" / f"{doc_name}.{model.replace('/', '_')}.json"
    if cache.exists():
        return cache.read_text()
    prompt = (
        "Below are one-line digests of every page of an Australian bank results document. "
        "Produce a section map as JSON: a list of objects {\"title\": str, \"start_page\": int, "
        '"end_page": int, "gist": str} covering the whole document in reading order, at most 45 sections. '
        "The gist is one sentence on what evidence the section holds. Reply with JSON only.\n\n"
        + page_digest(texts)
    )
    reply = chat(model, prompt, max_tokens=6000)
    section_map = json.dumps(parse_json_block(reply))
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(section_map)
    return section_map


def navigate(model: str, section_map: str, query: str) -> list[int]:
    prompt = (
        "You are locating evidence in a bank results document. Here is its section map (JSON):\n"
        f"{section_map}\n\n"
        f"Analyst query: {query}\n\n"
        f"Reply with JSON only: {{\"pages\": [...]}} — up to {TOP_K} page numbers most likely to "
        "contain that evidence, best first."
    )
    reply = chat(model, prompt, max_tokens=2000)
    pages = parse_json_block(reply).get("pages", [])
    return [int(p) for p in pages][:TOP_K]


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def main() -> None:
    docs = {"pa": page_texts(PA), "pres": page_texts(PRES)}

    print("=== Gold locations (marker search) ===")
    gold: dict[str, set[int]] = {}
    for tid, doc, markers, _ in TARGETS:
        pages, contents = locate_gold(docs[doc], markers)
        gold[tid] = pages
        print(f"{tid:26s} {doc:4s} gold={sorted(pages)} (contents pages excluded: {sorted(contents)})")
        if not pages:
            print(f"  WARNING: no gold for {tid}; target dropped")
    targets = [t for t in TARGETS if gold[t[0]]]

    results: dict[str, dict[str, bool]] = {}
    timings: dict[str, float] = {}

    # Arm A: section maps
    for model in NAV_MODELS:
        arm = f"map:{model.split('/')[-1]}"
        started = time.time()
        try:
            maps = {doc: build_map(model, {"pa": PA, "pres": PRES}[doc].stem, docs[doc]) for doc in ("pa", "pres")}
        except Exception as exc:  # noqa: BLE001
            print(f"  arm {arm} failed to build maps: {exc}")
            results[arm] = {tid: False for tid, _, _, _ in targets}
            timings[arm] = time.time() - started
            continue
        hits = {}
        for tid, doc, _, query in targets:
            try:
                pages = navigate(model, maps[doc], query)
            except Exception as exc:  # noqa: BLE001
                print(f"  navigate failed ({arm}, {tid}): {exc}")
                pages = []
            hits[tid] = bool(gold[tid] & set(pages))
        results[arm] = hits
        timings[arm] = time.time() - started

    # Arm B: BM25
    from rank_bm25 import BM25Okapi

    started = time.time()
    hits = {}
    for doc_key in ("pa", "pres"):
        corpus = [tokenize(t) for t in docs[doc_key]]
        bm25 = BM25Okapi(corpus)
        for tid, doc, _, query in targets:
            if doc != doc_key:
                continue
            scores = bm25.get_scores(tokenize(query))
            top = sorted(range(len(scores)), key=lambda i: -scores[i])[:TOP_K]
            hits[tid] = bool(gold[tid] & {i + 1 for i in top})
    results["bm25"] = hits
    timings["bm25"] = time.time() - started

    # Arm C: dense embeddings
    from sentence_transformers import SentenceTransformer, util

    started = time.time()
    encoder = SentenceTransformer("BAAI/bge-small-en-v1.5")
    hits = {}
    for doc_key in ("pa", "pres"):
        embeddings = encoder.encode([t[:2000] for t in docs[doc_key]], normalize_embeddings=True, show_progress_bar=False)
        for tid, doc, _, query in targets:
            if doc != doc_key:
                continue
            q = encoder.encode([query], normalize_embeddings=True)
            scores = util.cos_sim(q, embeddings)[0]
            top = scores.argsort(descending=True)[:TOP_K].tolist()
            hits[tid] = bool(gold[tid] & {i + 1 for i in top})
    results["dense:bge-small"] = hits
    timings["dense:bge-small"] = time.time() - started

    print("\n=== Results (hit = a gold page inside the arm's selection) ===")
    header = f"{'target':26s}" + "".join(f"{arm:>22s}" for arm in results)
    print(header)
    for tid, _, _, _ in targets:
        row = f"{tid:26s}" + "".join(f"{'HIT' if results[arm].get(tid) else 'miss':>22s}" for arm in results)
        print(row)
    print("-" * len(header))
    summary = {arm: sum(v.values()) for arm, v in results.items()}
    print(f"{'TOTAL':26s}" + "".join(f"{summary[arm]}/{len(targets)}".rjust(22) for arm in results))
    print(f"\nTimings (s): " + ", ".join(f"{arm}={t:.1f}" for arm, t in timings.items()))
    print(f"Model usage: {USAGE.calls} calls, {USAGE.prompt_tokens} in / {USAGE.completion_tokens} out, "
          f"${USAGE.cost_usd:.4f}")
    for model, m in USAGE.by_model.items():
        print(f"  {model}: {m['calls']} calls, {m['prompt']} in / {m['completion']} out, ${m['cost']:.4f}")


if __name__ == "__main__":
    main()
