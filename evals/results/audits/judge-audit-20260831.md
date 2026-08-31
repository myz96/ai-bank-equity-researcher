# Judge reliability audit — 2026-08-31

Protocol: 20 verdicts sampled stratified (7 pass, 7 fail, 6 flagged) from
the question-benchmark judging (deepseek-v4-pro + qwen3.7-flash, unanimity
protocol), shuffled, verdicts withheld. A blind frontier adjudicator ruled
stated/entailed per item independently (judge-audit-blind.json is exactly
what it saw; judge-audit-key.json holds the withheld verdicts).

Results:
- Pass agreement 7/7 — no false passes; the headline metric is not inflated.
- Fail agreement 5/7 — both mismatches are judge fails the adjudicator
  passes: the cheap judges err STRICT, never lenient. Scores are a floor.
- 4/6 flagged items independently ruled "hard calls" — flags mark real
  ambiguity.
- Overall definitive-verdict agreement 12/14 (86%), all errors conservative.

Reading: the two-judge unanimity protocol on cheap/mid models is reliable
for this narrow task (string-level stated/entailed checks). Its known bias
is conservatism, which compounds with the conjunctive gold facts to produce
low absolute "fully-grounded facts" scores across all tiers.
