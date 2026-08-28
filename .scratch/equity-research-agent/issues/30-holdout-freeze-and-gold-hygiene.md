# 30 — Holdout freeze and gold hygiene (Codex findings 3, 7, 8)

Type: task
Status: open

## Question

1. **Freeze the metric holdout NOW (finding 3)**: the planned dev/holdout split never happened and iteration has optimised against every scored case. Freeze a balanced holdout (~8 metric cases across banks/metrics/period-types, including the flagged holdout_candidate cases), mark them split "holdout", and stop running them until milestones. HITL: the user picks or ratifies the split (eval-review-guide judgment call 3) and ideally owns the execution of holdout runs.
2. **Crossref honesty (finding 7)**: stop describing location coverage as "passing" a case; a case passes only when coverage AND judged fact accuracy pass. Implement the fact-check judge (claim-level: does the answer state each gold fact, and does the cited quote entail it), or human adjudication, before any crossref pass is claimed.
3. **Gold hygiene (finding 8)**: (a) the crossref notables case cites a $130m FY25 comparator inferred from the Fable benchmark, not sighted in primary disclosure — fixed 2026-08-27 by quarantining the value (see cba-fy26-crossref.json); (b) sweep all gold for direction-only / value_pct / checklist material the harness silently ignores and mark each entry's evaluation status explicitly (scored | checklist | unscored); (c) the user independently re-derives at least one full case (single-author risk, eval-review-guide judgment call 4).
