# 04 — Memory design

Type: grilling
Status: open
Blocked by: 03

## Question

What does the agent carry between banks and periods, and what must it not carry? Candidates to carry: per-bank metric definitions, document layout maps, driver vocabulary. Must-not-carry candidates: figures from one bank applied to another, stale period data, and eval-answer leakage. Decide the storage form, the read/write policy, and whether memory is frozen during eval runs.
