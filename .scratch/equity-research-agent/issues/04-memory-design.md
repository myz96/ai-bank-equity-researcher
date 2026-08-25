# 04 — Memory design

Type: grilling
Status: resolved
Blocked by: 03

## Question

What does the agent carry between banks and periods, and what must it not carry? Candidates to carry: per-bank metric definitions, document layout maps, driver vocabulary. Must-not-carry candidates: figures from one bank applied to another, stale period data, and eval-answer leakage. Decide the storage form, the read/write policy, and whether memory is frozen during eval runs.

## Answer

Resolved with the user (grilling, 2026-08-25). Note: the retrieval bake-off removed the need for page-location memory — local retrieval finds pages cold — so memory is purely semantic.

1. **Memory is versioned files in the repo**: one registry file per bank (financial calendar, IR landing pages, document-suite names, per-bank driver label mappings, measure vocabulary). Git history is the audit trail. No runtime database.
2. **Read-only at runtime.** Discoveries become **suggested registry patches** in the run output; a human applies them deliberately. No silent self-modification.
3. **No financial numbers in memory — structural ban.** Numbers exist only in evidence records derived from the run's own corpus, so cross-bank and cross-period contamination has no path. The derived-data cache is keyed by document checksum: cache, not memory.
4. **Eval hygiene**: eval runs pin the registry at a commit, read-only; the unseen-bank case runs with that bank's registry entry deleted, so generalisation is a measured number.

Recorded as [ADR-0003](../../../docs/adr/0003-memory-as-versioned-registry.md).
