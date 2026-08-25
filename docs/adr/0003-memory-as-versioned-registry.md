# Memory is a versioned registry with no numbers in it

Cross-bank, cross-period memory is a set of per-bank registry files in the repo (calendar, document names, label mappings, measure vocabulary), read-only at runtime; runs emit suggested patches instead of writing. Financial numbers are banned from memory entirely — they exist only in evidence records derived from the run's own corpus — so contamination across banks or periods has no code path, rather than being discouraged by prompt. We chose this over a self-updating memory store because stale or wrong learned "knowledge" compounds silently, and over a vector memory because the retrieval bake-off (ticket 13) showed local search needs no learned priors.

## Consequences

- Eval runs pin the registry at a git commit; the unseen-bank case deletes that bank's entry to measure the cold path.
- The registry starts as a distillation of research tickets 08–11, so it is citable.
