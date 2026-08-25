"""Ticket 14 prototype: how reliably can each arm read a walk chart?

Arms:
  text:<model>   — the page's PDF text layer, structured by a text model
  vision:<model> — the page rendered to PNG at 2x, read by a vision model

Gold was hand-verified from the rendered pages on 2026-08-25 (see ticket 14).
Scoring: ordered signed bar values in bps; a bar matches within +-0.5bp.

Usage: uv run python prototypes/chart_reading.py
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import pymupdf

from openrouter_client import USAGE, chat, parse_json_block

REPO_ROOT = Path(__file__).resolve().parent.parent

TEXT_MODELS = ["qwen/qwen3.7-flash", "z-ai/glm-5.3", "stealth/ox-alpha"]
VISION_MODELS = ["qwen/qwen3.7-flash", "deepseek/deepseek-v4-flash-vision-exp", "stealth/ox-alpha", "moonshotai/kimi-k3"]

WALKS = [
    {
        "id": "fy26_pa_nim",
        "pdf": "data/raw/CBA/FY26/CBA-FY26-profit-announcement.pdf",
        "page": 28,
        "hint": "the chart titled 'NIM Movement since June 2025' (full-year NIM walk)",
        "gold": {"start": 208.0, "bars": [-3.0, -5.0, 0.0, 2.0, 0.0, 5.0, -2.0], "end": 205.0,
                 "labels": ["Liquids", "Asset pricing", "Funding costs", "Portfolio mix", "Basis risk",
                            "Capital, Replicating and Other", "Treasury & Markets"]},
    },
    {
        "id": "fy26_slide60_nim",
        "pdf": "data/raw/CBA/FY26/CBA-FY26-results-presentation.pdf",
        "page": 60,
        "hint": "the waterfall on the slide 'Group margin - 12 months'",
        "gold": {"start": 208.0, "bars": [-4.0, -5.0, 0.0, 2.0, 5.0, -1.0], "end": 205.0,
                 "labels": ["Liquids & repos", "Asset pricing", "Funding costs", "Portfolio mix",
                            "Interest rate risk hedging", "Treasury & Markets"]},
    },
    {
        "id": "fy26_slide32_cet1",
        "pdf": "data/raw/CBA/FY26/CBA-FY26-results-presentation.pdf",
        "page": 32,
        "hint": "the CET1 capital ratio waterfall on the 'Capital' slide (movements in bpts)",
        "gold": {"start": 1230.0, "bars": [-76.0, 106.0, -46.0, -8.0], "end": 1200.0,
                 "labels": ["1H26 dividend (DRP neutralised)", "Cash NPAT", "RWA", "Other"]},
    },
    {
        "id": "fy25_pa_nim",
        "pdf": "data/raw/CBA/FY25/CBA-FY25-profit-announcement.pdf",
        "page": 28,
        "hint": "the chart titled 'NIM Movement since June 2024' (full-year NIM walk)",
        "gold": {"start": 199.0, "bars": [7.0, 0.0, -7.0, 0.0, -1.0, 9.0, 1.0], "end": 208.0,
                 "labels": ["Liquids & Pooled Facilities", "Asset pricing", "Funding costs", "Portfolio mix",
                            "Basis risk", "Capital, Replicating and Other", "Treasury and Markets"]},
    },
]

PROMPT = (
    "This bank results page contains a waterfall (walk) chart: {hint}. Extract it as JSON only:\n"
    '{{"start_label": str, "start_bps": float, "bars": [{{"label": str, "bps": float}}], '
    '"end_label": str, "end_bps": float}}\n'
    "Rules: values in basis points (a percentage like 2.08% is 208 bps; a ratio movement chart "
    "labelled 'bpts' is already in bps). Bars in parentheses are negative. A dash bar is 0. "
    "Keep the chart's bar order. Use only what is on this page."
)


def score(gold: dict, extraction: dict) -> dict:
    bars = [float(b.get("bps", 0)) for b in extraction.get("bars", [])]
    matched = sum(
        1 for i, g in enumerate(gold["bars"]) if i < len(bars) and abs(bars[i] - g) <= 0.5
    )
    start_ok = abs(float(extraction.get("start_bps", 0)) - gold["start"]) <= 0.5
    end_ok = abs(float(extraction.get("end_bps", 0)) - gold["end"]) <= 0.5
    total = float(extraction.get("start_bps", 0)) + sum(bars)
    sum_ok = abs(total - float(extraction.get("end_bps", 0))) <= 1.0
    return {
        "bars": f"{matched}/{len(gold['bars'])}",
        "bars_matched": matched,
        "bar_count": len(gold["bars"]),
        "endpoints": start_ok and end_ok,
        "self_sum_ok": sum_ok,
    }


def main() -> None:
    pages: dict[str, str] = {}
    images: dict[str, bytes] = {}
    for walk in WALKS:
        doc = pymupdf.open(REPO_ROOT / walk["pdf"])
        page = doc[walk["page"] - 1]
        pages[walk["id"]] = page.get_text()
        images[walk["id"]] = page.get_pixmap(matrix=pymupdf.Matrix(2, 2)).tobytes("png")

    rows = []
    for kind, models in (("text", TEXT_MODELS), ("vision", VISION_MODELS)):
        for model in models:
            for walk in WALKS:
                arm = f"{kind}:{model.split('/')[-1]}"
                prompt = PROMPT.format(hint=walk["hint"])
                started = time.time()
                try:
                    if kind == "text":
                        reply = chat(model, prompt + "\n\nPAGE TEXT:\n" + pages[walk["id"]], max_tokens=2000)
                    else:
                        reply = chat(model, prompt, image_png=images[walk["id"]], max_tokens=2000)
                    extraction = parse_json_block(reply)
                    result = score(walk["gold"], extraction)
                except Exception as exc:  # noqa: BLE001
                    result = {"bars": "FAIL", "bars_matched": 0, "bar_count": len(walk["gold"]["bars"]),
                              "endpoints": False, "self_sum_ok": False}
                    print(f"  {arm} {walk['id']} failed: {exc}")
                result.update({"arm": arm, "walk": walk["id"], "seconds": time.time() - started})
                rows.append(result)

    print("\n=== Chart-reading results (bars matched / gold bars; EP = endpoints ok; SUM = self-consistent) ===")
    arms = sorted({r["arm"] for r in rows})
    header = f"{'arm':38s}" + "".join(f"{w['id']:>20s}" for w in WALKS) + f"{'total':>10s}"
    print(header)
    for arm in arms:
        cells, matched_total, bar_total = "", 0, 0
        for walk in WALKS:
            r = next(r for r in rows if r["arm"] == arm and r["walk"] == walk["id"])
            flags = ("E" if r["endpoints"] else "-") + ("S" if r["self_sum_ok"] else "-")
            cells += f"{r['bars'] + ' ' + flags:>20s}"
            matched_total += r["bars_matched"]
            bar_total += r["bar_count"]
        print(f"{arm:38s}{cells}{f'{matched_total}/{bar_total}':>10s}")

    print(f"\nModel usage: {USAGE.calls} calls, ${USAGE.cost_usd:.4f}")
    for model, m in USAGE.by_model.items():
        print(f"  {model}: {m['calls']} calls, {m['prompt']} in / {m['completion']} out, ${m['cost']:.4f}")

    out = REPO_ROOT / "data/cache/chart_reading_results.json"
    out.write_text(json.dumps(rows, indent=2))
    print(f"\nRaw rows saved to {out.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
