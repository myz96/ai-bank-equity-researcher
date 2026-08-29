"""Bake-off judge sweep (ticket 32): the stated-AND-entailed checklist rate per arm.

Runs the SAME two-judge protocol (judge.py) over every arm's artifacts for the
four anchor cases, so the discriminator column of the decision table is measured
identically for the pipeline arms and the agentic arms.

Arm artifact formats:
- cheap / glm: pipeline format (out/<slug>-cheap|-normal). answer_prose and
  cited_quotes come from the pipeline's own adapters in judge.py.
- sonnet / fable / codex: benchmark format (out/baseline-<arm>/<slug>). The
  answer is report.md minus its citation/source sections and block quotes; the
  quotes are every citations[].quote in attribution.json, in driver order.

Protocol note: MAX_ANSWER_CHARS is raised to 20000 FOR EVERY ARM. The agentic
reports run past the pipeline default of 6000 and their checklist facts sit in
late sections; one shared window keeps the comparison fair.

Usage:
    uv run python scripts/bakeoff_judge.py --arms sonnet fable codex
    uv run python scripts/bakeoff_judge.py            # all five arms
Requires OPENROUTER_API_KEY in the environment (source .env first).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from bank_equity_researcher import judge as J  # noqa: E402
from bank_equity_researcher.llm import LLM  # noqa: E402

J.MAX_ANSWER_CHARS = 20000

JUDGES = ("deepseek/deepseek-v4-pro-0813", "qwen/qwen3.7-flash")

# (bench slug, pipeline slug stem, gold file, metric)
ANCHORS = [
    ("cba-nim-fy26", "cba-nim-fy26-vs-fy25", "cba-fy26.json", "nim"),
    ("cba-cash-earnings-fy26", "cba-cash_earnings-fy26-vs-fy25", "cba-fy26.json", "cash_earnings"),
    ("cba-impairment-fy26", "cba-impairment-fy26-vs-fy25", "cba-fy26.json", "impairment"),
    ("cba-nim-fy21", "cba-nim-fy21-vs-fy20", "cba-fy21.json", "nim"),
]

PIPELINE_ARMS = {"cheap": "cheap", "glm": "normal"}  # arm name -> out/ suffix
BENCH_ARMS = ("sonnet", "fable", "codex")
ALL_ARMS = list(PIPELINE_ARMS) + list(BENCH_ARMS)


def bench_prose(report_md: str) -> str:
    """The benchmark report's own words: drop citation/source sections and
    block quotes, mirroring what answer_prose does for pipeline reports."""
    keep, out = True, []
    for line in report_md.splitlines():
        if line.lstrip().startswith("#"):
            head = line.lower()
            keep = "citation" not in head and "source" not in head
        if keep and not line.lstrip().startswith(">"):
            out.append(line)
    return "\n".join(out).strip()


def bench_quotes(attribution: dict) -> list[str]:
    """Every cited verbatim quote in the attribution JSON, deduplicated, in order.

    Two citation shapes exist in the wild: dicts with a "quote" key (Sonnet,
    Fable) and strings like '(doc.pdf, PDF p. 60, "the quote")' (Codex). For
    the string form the quote is the text between the first and last double
    quote marks.
    """
    found: list[str] = []

    def string_quote(citation: str) -> str | None:
        for mark in ('"', "'"):
            first, last = citation.find(mark), citation.rfind(mark)
            if 0 <= first < last:
                return citation[first + 1 : last].strip() or None
        return None

    def walk(node) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "quote" and isinstance(value, str) and value.strip():
                    found.append(value)
                elif key == "citations" and isinstance(value, list):
                    for item in value:
                        if isinstance(item, str):
                            quote = string_quote(item)
                            if quote:
                                found.append(quote)
                        else:
                            walk(item)
                else:
                    walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(attribution)
    seen: set[str] = set()
    deduped = []
    for quote in found:
        if quote not in seen:
            seen.add(quote)
            deduped.append(quote)
    return deduped


def load_arm_case(arm: str, bench_slug: str, pipe_slug: str):
    """Returns (answer, quotes, movement, path) or None when artifacts are missing."""
    if arm in PIPELINE_ARMS:
        case_dir = ROOT / "out" / f"{pipe_slug}-{PIPELINE_ARMS[arm]}"
    else:
        case_dir = ROOT / "out" / f"baseline-{arm}" / bench_slug
    report_path = case_dir / "report.md"
    attr_path = case_dir / "attribution.json"
    if not report_path.exists() or not attr_path.exists():
        return None
    report = report_path.read_text()
    attribution = json.loads(attr_path.read_text())
    if arm in PIPELINE_ARMS:
        return J.answer_prose(report), J.cited_quotes(attribution), attribution.get("movement"), case_dir
    return bench_prose(report), bench_quotes(attribution), attribution.get("movement"), case_dir


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arms", nargs="+", default=ALL_ARMS, choices=ALL_ARMS)
    parser.add_argument("--cases", nargs="+", default=None, help="bench slugs to judge (default: all four)")
    parser.add_argument("--stamp", default=None, help="timestamp for the output filename")
    args = parser.parse_args()
    anchors = [a for a in ANCHORS if args.cases is None or a[0] in args.cases]

    llm = LLM()
    stamp = args.stamp or dt.datetime.now().strftime("%Y%m%d-%H%M")
    results: dict = {"stamp": stamp, "judges": list(JUDGES), "max_answer_chars": J.MAX_ANSWER_CHARS, "arms": {}}

    for arm in args.arms:
        arm_out: dict = {}
        for bench_slug, pipe_slug, gold_file, metric in anchors:
            gold = json.loads((ROOT / "evals" / "gold" / gold_file).read_text())
            case = next(c for c in gold["cases"] if c["metric"] == metric)
            facts = case.get("narrative_checklist", [])
            loaded = load_arm_case(arm, bench_slug, pipe_slug)
            if loaded is None:
                arm_out[bench_slug] = {"status": "missing_artifacts"}
                print(f"[{arm}] {bench_slug}: MISSING", flush=True)
                continue
            answer, quotes, movement, case_dir = loaded
            verdict = J.judge_facts(llm, facts, answer, quotes, JUDGES)
            verdict["movement_reported"] = movement
            verdict["movement_gold"] = case.get("movement")
            verdict["artifact_dir"] = str(case_dir.relative_to(ROOT))
            arm_out[bench_slug] = verdict
            print(
                f"[{arm}] {bench_slug}: {verdict['fact_accuracy']} "
                f"(flagged {verdict['flagged']}, quotes {verdict['quotes_used']})",
                flush=True,
            )
        results["arms"][arm] = arm_out

    results["judge_cost_usd"] = round(llm.usage.cost_usd, 4)
    out_path = ROOT / "evals" / "results" / f"{stamp}-bakeoff-judge.json"
    out_path.write_text(json.dumps(results, indent=1))
    print(f"\nwrote {out_path}  (judge cost ${llm.usage.cost_usd:.4f})")

    print("\n| arm | " + " | ".join(slug for slug, *_ in anchors) + " | total |")
    print("|---|" + "---|" * (len(anchors) + 1))
    for arm, arm_out in results["arms"].items():
        cells, passed_sum, total_sum = [], 0, 0
        for bench_slug, *_ in anchors:
            v = arm_out.get(bench_slug, {})
            if v.get("status") == "missing_artifacts" or "passed" not in v:
                cells.append("—")
                continue
            cells.append(f"{v['passed']}/{v['total']}" + (f" ⚑{v['flagged']}" if v["flagged"] else ""))
            passed_sum += v["passed"]
            total_sum += v["total"]
        cells.append(f"{passed_sum}/{total_sum}" if total_sum else "—")
        print(f"| {arm} | " + " | ".join(cells) + " |")


if __name__ == "__main__":
    main()
