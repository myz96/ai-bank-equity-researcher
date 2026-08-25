# 14 — Prototype: chart-reading reliability

Type: prototype
Status: open
Blocked by: 15, 16

## Question

How reliably can each approach read a walk chart? Test on walks whose values are already hand-recorded (gold): the CBA FY26 NIM walk (PA printed p12: FY25 2.08% + liquids −0.02% + asset pricing −0.05% → FY26 2.05%, per ticket 08), the presentation 12-month walk (slide 60: Liquids & repos −4, Asset pricing −5, Funding costs 0, Portfolio mix +2, Interest rate risk hedging +5, Treasury & Markets −1), and the CET1 waterfall (slide 32). Gold values for the CBA FY25 NIM walk also exist in research file 11. Note the two FY26 walks decompose differently (PA p12 vs slide 60) — the prototype must handle both framings.

Arms:
- **(a)** pymupdf text-layer extraction of the chart page (bank charts usually carry text labels; narration repeats values).
- **(b)** Render the page to an image and pass it to a vision model via OpenRouter — test one cheap and one normal vision model.
- **(c)** A hosted PDF-parsing service — only if (a) and (b) both prove unreliable.

Score: bar-level value match rate against gold, deterministic sum-check pass rate, cost per page. Output: a reliability table the user reacts to before ticket 03 closes.
