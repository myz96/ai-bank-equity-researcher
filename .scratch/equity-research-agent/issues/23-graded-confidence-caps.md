# 23 — Defect: peripheral check failures over-cap confidence; null bars crash walk parsing

Type: task
Status: open

## Question

In the ANZ 1H26 cold-start run, a vision read of the secondary HoH walk page returned a bar with a null value, crashed `float()`, and the resulting `walk_extraction_error` capped the whole attribution at 40 — even though the primary PCP walk validated and all seven drivers were exact. Fix: (1) walk parsing skips/flags null bars instead of crashing; (2) the confidence cap grades failures — a failure on evidence the attribution actually rests on caps hard; a failure on peripheral/unused evidence lands in limitations without the hard cap.
