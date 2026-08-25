# 14 — Prototype: chart-reading reliability

Type: prototype
Status: claimed
Blocked by: 15, 16

## Gold (hand-verified from rendered pages, 2026-08-25)

- FY26 PA p28 (printed 12) "NIM Movement since June 2025": 208 → Liquids (3), Asset pricing (5), Funding costs 0, Portfolio mix +2, Basis risk 0, Capital/Replicating/Other +5, Treasury & Markets (2) → 205. Note: research 08's record of this walk was incomplete — corrected here from the page image.
- FY26 Presentation slide 60 "Group margin – 12 months": 208 → Liquids & repos (4), Asset pricing (5), Funding costs 0, Portfolio mix +2, Interest rate risk hedging +5, Treasury & Markets (1) → 205. Same movement, different bar framing than the PA — a live example of the two-framings mapping problem.
- FY26 Presentation slide 32 CET1: Dec 25 12.3% → 1H26 dividend (76), Cash NPAT +106, RWA (46) [Credit (38), IRRBB (16), Market +8, Op 0], Other (8) → Jun 26 12.0%. Bars sum to −24 vs headline −30: the slide footnotes that numbers "may not sum precisely" (rounding) — validation checks need a tolerance rule for presentation walks.
- FY25 PA p28 "NIM Movement since June 2024": 199 → Liquids & Pooled +7, Asset pricing 0, Funding (7), Mix 0, Basis risk (1), Capital/Replicating/Other +9, Treasury & Markets +1 → 208. Matches research 11.

## Question

How reliably can each approach read a walk chart? Test on walks whose values are already hand-recorded (gold): the CBA FY26 NIM walk (PA printed p12: FY25 2.08% + liquids −0.02% + asset pricing −0.05% → FY26 2.05%, per ticket 08), the presentation 12-month walk (slide 60: Liquids & repos −4, Asset pricing −5, Funding costs 0, Portfolio mix +2, Interest rate risk hedging +5, Treasury & Markets −1), and the CET1 waterfall (slide 32). Gold values for the CBA FY25 NIM walk also exist in research file 11. Note the two FY26 walks decompose differently (PA p12 vs slide 60) — the prototype must handle both framings.

Arms:
- **(a)** pymupdf text-layer extraction of the chart page (bank charts usually carry text labels; narration repeats values).
- **(b)** Render the page to an image and pass it to a vision model via OpenRouter — test one cheap and one normal vision model.
- **(c)** A hosted PDF-parsing service — only if (a) and (b) both prove unreliable.

Score: bar-level value match rate against gold, deterministic sum-check pass rate, cost per page. Output: a reliability table the user reacts to before ticket 03 closes.

## Results (2026-08-25, prototypes/chart_reading.py)

Four hand-verified gold walks, 24 gold bars total. Score = bars matched within ±0.5bp, in chart order.

| Arm | Bars matched | Cost | Note |
|---|---|---|---|
| **vision: `qwen3.7-flash`** | **24/24** | $0.0006 (8 calls incl. text arm) | Perfect, cheapest |
| vision: `ox-alpha` | 24/24 | $0 | Perfect but rate-limited; 3 of its text-arm calls died on 429 |
| vision: `kimi-k3` | 22/24 | $0.0432 | Missed two PA-chart bars |
| vision: `deepseek-v4-flash-vision-exp` | 14/24 | $0.0016 | Unreliable on the dense PA chart |
| text: `qwen3.7-flash` | 5/24 | — | Text layer scatters chart values; pairing fails |
| text: `ox-alpha` | 3/24 | — | Rate-limited + weak |
| text: `glm-5.3` | 0/24 | $0.1609 | Ignored the reasoning-off flag, burned 32k reasoning tokens, returned empty content every call |

Findings:
1. **Vision reading of rendered chart pages is essentially solved at trivial cost** — the cheapest vision model scored perfectly. Route chart pages to vision `qwen3.7-flash`; the deterministic sum check guards the rare failure.
2. **Text-layer chart extraction is not viable** (values present but bar-label pairing fails).
3. **CET1 slide:** every vision arm got 4/4 bars and the self-sum check *correctly* failed — the slide's own bars do not sum to its headline (rounding footnote). Presentation walks need a documented sum tolerance.
4. **`glm-5.3` operational caveat:** it ignores `reasoning: {enabled: false}` and needs a reasoning-aware client (large max_tokens, read content after reasoning) — matters for its author role in ticket 07.
5. `ox-alpha` confirmed as experiment-only: nothing on the critical path should wait on its rate limiter.

Pending user reaction.
