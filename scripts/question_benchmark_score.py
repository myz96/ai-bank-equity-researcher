"""Score the subscription-tier question benchmarks (Fable/Opus/Sonnet
subagents) with the same protocol as every product arm: location coverage
plus two-judge stated-AND-entailed fact accuracy, 48-quote window.

The benchmark agents emit {answer, key_facts:[{fact, citations:[{document,
pdf_page, quote}]}], confidence, limitations}. This adapter mints evidence
records from those citations (ids per citation, quote carried verbatim) so
`evals.score_crossref` consumes them unchanged. Coverage still measures the
same thing: did the answer cite the pages the gold requires.

Usage: uv run python scripts/question_benchmark_score.py [--tiers fable opus sonnet]
Writes evals/results/<stamp>-question-benchmarks.{json,md}.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from bank_equity_researcher.config import COMBOS  # noqa: E402
from bank_equity_researcher.corpus import doc_alias_index  # noqa: E402
from bank_equity_researcher.evals import load_question_gold, score_crossref  # noqa: E402
from bank_equity_researcher.llm import LLM  # noqa: E402

JUDGES = COMBOS["cheap"].judges


def adapt(answer_json: dict) -> dict:
    """Benchmark shape -> the ask_output shape score_crossref reads."""
    records, facts = [], []
    counter = 0
    for fact in answer_json.get("key_facts", []):
        ids = []
        for cite in fact.get("citations", []):
            counter += 1
            rid = f"bm-{counter}"
            records.append({
                "id": rid,
                "doc_id": str(cite.get("document", "")),
                "pdf_page": cite.get("pdf_page"),
                "quote": str(cite.get("quote", "")),
            })
            ids.append(rid)
        facts.append({"fact": fact.get("fact", ""), "evidence": ids})
    return {
        "answer": answer_json.get("answer", ""),
        "key_facts": facts,
        "evidence_records": records,
        "confidence": answer_json.get("confidence"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tiers", nargs="+", default=["fable", "opus", "sonnet"])
    args = parser.parse_args()

    gold = {c["id"]: c for c in load_question_gold("dev")}
    llm = LLM()
    index = doc_alias_index()
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    results: dict = {"stamp": stamp, "judges": list(JUDGES), "tiers": {}}

    for tier in args.tiers:
        rows = {}
        for slug, case in gold.items():
            path = ROOT / "out" / f"baseline-{tier}-questions" / slug / "answer.json"
            if not path.exists():
                rows[slug] = {"status": "missing"}
                print(f"[{tier}] {slug}: MISSING", flush=True)
                continue
            output = adapt(json.loads(path.read_text()))
            row = score_crossref(case, output, llm, JUDGES, index, max_quotes=48)
            row["confidence"] = output.get("confidence")
            rows[slug] = row
            fc = row.get("fact_check", {})
            print(f"[{tier}] {slug}: coverage {row.get('location_coverage')} "
                  f"facts {fc.get('fact_accuracy')} flagged {fc.get('flagged')}", flush=True)
        results["tiers"][tier] = rows

    results["judge_cost_usd"] = round(llm.usage.cost_usd, 4)
    out = ROOT / "evals" / "results" / f"{stamp}-question-benchmarks.json"
    out.write_text(json.dumps(results, indent=1))
    print(f"\nwrote {out} (judge cost ${llm.usage.cost_usd:.4f})")

    print("\n| tier | " + " | ".join(gold) + " |")
    print("|---|" + "---|" * len(gold))
    for tier, rows in results["tiers"].items():
        cells = []
        for slug in gold:
            r = rows.get(slug, {})
            if r.get("status") == "missing":
                cells.append("—")
            else:
                fc = r.get("fact_check", {})
                cells.append(f"{r.get('location_coverage')} / {fc.get('fact_accuracy')}")
        print(f"| {tier} | " + " | ".join(cells) + " |")


if __name__ == "__main__":
    main()
