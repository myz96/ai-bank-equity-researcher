"""The eval harness (ticket 05): runs gold cases through the pipeline and
produces a scorecard — driver precision/recall, calibration, per-stage
extraction accuracy — never one blended number."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .config import OUT_DIR, REPO_ROOT
from .schema import Attribution

GOLD_DIR = REPO_ROOT / "evals" / "gold"
RESULTS_DIR = REPO_ROOT / "evals" / "results"

# Tolerances for matching a claimed contribution against gold (ticket 05).
UNIT_TOL = {"bps": 0.5, "$m": 10.0, "ppt": 0.1}
CONFIDENT_THRESHOLD = 85  # claims at/above this count for the confidently-wrong rate
RELIABILITY_BUCKETS = [(0, 50), (50, 70), (70, 85), (85, 95), (95, 101)]


def load_gold(suite: str, bank: str | None = None) -> list[dict]:
    cases = []
    for path in sorted(GOLD_DIR.glob("*.json")):
        gold_file = json.loads(path.read_text())
        for case in gold_file["cases"]:
            if case.get("split", "dev") != suite:
                continue
            if bank and gold_file["bank"].upper() != bank.upper():
                continue
            if "movement" not in case:
                # Cross-reference consolidation cases (ticket 26) run through
                # the ask entry point, not the metric pipeline; skip here.
                continue
            cases.append({**case, "bank": gold_file["bank"], "period": gold_file["period"],
                          "comparator": gold_file["comparator"], "basis": gold_file["basis"]})
    return cases


def _gold_driver_values(gold_drivers: dict) -> dict[str, float]:
    """Normalise the two gold shapes ({canonical: value} and
    {canonical: {value, provenance}}) into {canonical: float}."""
    values = {}
    for canonical, entry in gold_drivers.get("drivers", {}).items():
        if isinstance(entry, dict):
            if "value" in entry and isinstance(entry["value"], (int, float)):
                values[canonical] = float(entry["value"])
        elif isinstance(entry, (int, float)):
            values[canonical] = float(entry)
    return values


def _match(value: float, target: float, unit: str) -> bool:
    tol = UNIT_TOL.get(unit, 0.5)
    if abs(target) > tol and value * target < 0:
        return False
    return abs(value - target) <= tol


def score_case(gold: dict, attribution: Attribution) -> dict:
    unit = gold["movement"]["unit"].split(" ")[0]
    result: dict = {"case": f"{gold['bank']}-{gold['metric']}-{gold['period']}", "metric": gold["metric"]}

    # 1. Movement.
    m, g = attribution.movement, gold["movement"]
    result["movement_ok"] = bool(
        m and _match(m.from_value, g["from"], unit) and _match(m.to_value, g["to"], unit)
        and _match(m.delta, g["delta"], unit)
    )

    # 2. Driver precision/recall against gold (and accepted alt framings).
    gold_sets = [_gold_driver_values(gold.get("gold_drivers", {}))]
    for framing in gold.get("alt_framings", []):
        gold_sets.append({k: float(v) for k, v in framing.get("drivers", {}).items()})
    comparison_mismatch = (
        "comparison" in gold.get("gold_drivers", {})
        and gold["gold_drivers"]["comparison"].lower().replace(" ", "")
        != f"{gold['period']}vs{gold['comparator']}".lower()
    )
    claims = [(d.canonical, d.contribution.value, d.confidence)
              for d in attribution.drivers if d.contribution is not None]
    per_claim: list[dict] = []
    if gold_sets[0] and not comparison_mismatch:
        matched_gold: set[str] = set()
        for canonical, value, confidence in claims:
            correct = any(
                canonical in gs and _match(value, gs[canonical], unit) for gs in gold_sets
            )
            if correct:
                matched_gold.add(canonical)
            per_claim.append({"canonical": canonical, "value": value,
                              "confidence": confidence, "correct": correct})
        primary = set(gold_sets[0])
        result["driver_recall"] = f"{len(matched_gold & primary)}/{len(primary)}"
        result["driver_precision"] = f"{sum(c['correct'] for c in per_claim)}/{len(per_claim)}" if per_claim else "0/0"
    else:
        result["driver_recall"] = "n/a (checklist or comparison-mismatch gold)"
        result["driver_precision"] = "n/a"
    result["claims"] = per_claim

    # 3. Per-stage extraction score: gold walk bars found in walk_vision records.
    gold_walk = _gold_driver_values(gold.get("gold_drivers", {})) if gold.get("gold_drivers", {}).get("tier") == "walk" else {}
    if gold_walk:
        extracted = [n.value for r in attribution.evidence_records if r.kind == "walk_vision" for n in r.numbers]
        hit = sum(1 for v in gold_walk.values() if any(_match(e, v, "bps") for e in extracted))
        result["extraction"] = f"{hit}/{len(gold_walk)}"

    # 4. Honesty signals.
    result["failed_checks"] = sum(1 for item in attribution.limitations if item.startswith("Failed check:"))
    result["attribution_confidence"] = attribution.attribution_confidence
    result["cost_usd"] = attribution.provenance.get("cost_usd")
    result["seconds"] = attribution.provenance.get("seconds")
    return result


def calibration(rows: list[dict]) -> dict:
    claims = [c for r in rows for c in r.get("claims", [])]
    if not claims:
        return {"claims": 0}
    brier = sum((c["confidence"] / 100 - (1.0 if c["correct"] else 0.0)) ** 2 for c in claims) / len(claims)
    confident = [c for c in claims if c["confidence"] >= CONFIDENT_THRESHOLD]
    table = []
    for lo, hi in RELIABILITY_BUCKETS:
        bucket = [c for c in claims if lo <= c["confidence"] < hi]
        if bucket:
            accuracy = sum(c["correct"] for c in bucket) / len(bucket)
            table.append(f"{lo}-{hi - 1}: {len(bucket)} claims, {accuracy:.0%} correct")
    return {
        "claims": len(claims),
        "brier": round(brier, 3),
        "confidently_wrong_rate": (
            round(sum(1 for c in confident if not c["correct"]) / len(confident), 3) if confident else None
        ),
        "reliability": table,
    }


def run_suite(suite: str, combo: str, bank: str | None = None) -> Path:
    from .pipeline import run_case

    gold_cases = load_gold(suite, bank)
    rows = []
    for gold in gold_cases:
        label = f"{gold['bank']} {gold['metric']} {gold['period']}"
        try:
            attribution, _ = run_case(gold["bank"], gold["metric"], gold["period"], gold["comparator"], combo)
            row = score_case(gold, attribution)
        except Exception as exc:  # noqa: BLE001 - a crashed case is a scored failure
            row = {"case": label, "metric": gold["metric"], "error": str(exc)[:300]}
        print(f"scored {label}: {json.dumps({k: v for k, v in row.items() if k != 'claims'})[:200]}")
        rows.append(row)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = RESULTS_DIR / f"{stamp}-{combo}-{suite}.jsonl"
    raw_path.write_text("\n".join(json.dumps(r) for r in rows))

    cal = calibration(rows)
    lines = [f"# Scorecard — suite {suite}, combo {combo}, {stamp}", ""]
    lines.append("| Case | Movement | Driver recall | Precision | Extraction | Failed checks | Conf | Cost |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in rows:
        if "error" in r:
            lines.append(f"| {r['case']} | ERROR | | | | | | |")
            continue
        lines.append(
            f"| {r['case']} | {'OK' if r['movement_ok'] else 'WRONG'} | {r['driver_recall']} "
            f"| {r['driver_precision']} | {r.get('extraction', '—')} | {r['failed_checks']} "
            f"| {r['attribution_confidence']} | ${r.get('cost_usd', 0)} |"
        )
    lines += ["", "## Calibration (quantified driver claims)", ""]
    for key, value in cal.items():
        if key == "reliability":
            lines += [f"- {row}" for row in value]
        else:
            lines.append(f"- {key}: {value}")
    card_path = RESULTS_DIR / f"{stamp}-{combo}-{suite}.md"
    card_path.write_text("\n".join(lines) + "\n")
    return card_path
