# 22 — Defect: narratives echo the walk instead of explaining it

Type: task
Status: open

## Question

Driver narratives restate the bar ("a 5 bps negative contribution from asset pricing") instead of citing the bank's own explanation (home lending pricing down 4bps, business/institutional down 1bp, competition) that sits in the PA text on the same page — and the ADR-0001 requirement to flag what a walk hides (CBA calls the liquids drag "broadly revenue neutral") is not yet surfaced. Fix: ensure the walk page's text evidence is extracted alongside the vision read (currently walk pages skip text extraction), and prompt the author to ground each narrative in quoted explanation and to note walk caveats like revenue-neutral bars.
