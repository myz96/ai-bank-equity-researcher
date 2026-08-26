# 21 — Defect: presentation citations show "printed p1"

Type: task
Status: open

## Question

`printed_page_of()` misreads presentation slides (footer parse returned 1 for slide 60). Slides carry a slide number, not a printed page. Fix: for presentation doc_types, take the slide number (usually the bare integer in a corner line equal to the PDF page or nearby); validate printed_page against pdf_page plausibility (|printed − pdf| bounded); drop the field when implausible rather than citing a wrong page.
