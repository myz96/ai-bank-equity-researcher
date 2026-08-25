# Walk-first layered attribution with deterministic validation

Attribution numbers come first from the bank's own published walks and bridges, mapped into a fixed canonical driver taxonomy; arithmetic derivation covers metrics without a walk (ROE, CTI); unquantified narrative drivers are included but marked; and every extracted figure passes deterministic Python validation checks (walk sums, accounting identities, cross-document agreement). We chose this over independent recomputation because public disclosure cannot reproduce a NIM walk (repricing detail is not published), and over narrative-only synthesis because it is unverifiable.

## Consequences

- The known risk is parroting management's framing. Mitigations are structural: the agent must flag what a walk hides (e.g. "revenue neutral" liquids bars), report an explicit residual instead of force-fitting, and surface every failed validation check in the output.
- Confidence semantics (ticket 02) inherit a natural evidence ladder: walk-quantified > arithmetic-derived > narrative-only, adjusted by validation results.
- Full taxonomy and method: [docs/design/driver-taxonomy.md](../design/driver-taxonomy.md).
