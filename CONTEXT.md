# Bank Equity Research

First-pass equity research on Australian banks: explaining how a headline metric moved between reporting periods, and attributing the movement to drivers with cited evidence.

## Language

**Bank**:
An ASX-listed Australian deposit-taking institution under analysis.
_Avoid_: institution, company, ticker

**Headline metric**:
One of six: net interest margin, cash earnings, return on equity, CET1 ratio, credit impairment charge, cost-to-income ratio.
_Avoid_: KPI, measure, figure

**Reporting period**:
A half-year or full-year in the bank's own financial calendar.
_Avoid_: quarter

**Comparator**:
The prior period a movement is measured against. The agent always names its comparator.
_Avoid_: baseline, benchmark

**PCP**:
The prior corresponding period: the same period one year earlier. Default comparator for a half-year input.

**Prior half**:
The immediately preceding half-year. A comparison against it is HoH.

**Period type**:
Whether a case targets a half-year result, a full-year result, or an older period whose disclosure format differs.
_Avoid_: time span

**Movement**:
The change in a headline metric from the comparator to the reporting period.
_Avoid_: delta, variance, change

**Driver**:
A named cause that contributed to a movement, with a direction and, where evidence allows, a magnitude.
_Avoid_: factor, lever, contributor

**Attribution**:
The set of drivers, with contributions and confidence ratings, that explains a movement.
_Avoid_: explanation, breakdown

**Confidence rating**:
The agent's self-stated number from 0 to 100: the probability that the claim would be judged correct against gold evidence. One per driver, one per attribution.
_Avoid_: certainty, score

**Cash earnings**:
The bank-defined profit measure that excludes items the bank treats as non-recurring or non-cash. Defined per bank; not statutory. Westpac dropped this measure at 1H23 and now headlines net profit excluding Notable Items.
_Avoid_: underlying profit, adjusted profit

**Statutory profit**:
Net profit after tax under accounting standards, as reported in the audited financial statements.
_Avoid_: reported profit

**NIM walk**:
A bank-published bridge that attributes the movement in net interest margin to named drivers.

**Earnings bridge**:
A bank-published bridge that attributes the movement in cash earnings to named drivers.

**Canonical driver**:
A bank-agnostic driver concept in the fixed taxonomy. Each bank's verbatim walk label maps to one canonical driver.
_Avoid_: normalised driver, generic driver

**Basis**:
The profit measurement a figure belongs to: cash, statutory, or ex-Notables. Every figure is tagged with its basis.

**Notable items**:
Large separately disclosed items a bank strips from its underlying result. ANZ says "significant items".
_Avoid_: one-offs

**Residual**:
The unexplained remainder after quantified drivers are summed against a movement. Always reported, never force-fitted.
_Avoid_: plug, balancing item

**Loss rate**:
The credit impairment charge as basis points of average gross loans, annualised for half-years. The bank's denominator is always named.

**Jaws**:
Income growth minus expense growth versus the comparator. Positive jaws lowers the cost-to-income ratio.

**Validation check**:
A deterministic test in code that an extracted figure must pass: walk bars sum to the movement, identities hold, documents agree.

**Evidence record**:
A typed extract from a source page: document, printed and PDF page, verbatim quote or table, parsed numbers with units and basis tags. The reasoning model reads only evidence records.
_Avoid_: chunk, snippet

**Registry**:
The per-bank versioned memory file: financial calendar, document names, label mappings, measure vocabulary. It holds no financial numbers.
_Avoid_: knowledge base, profile

**Corroboration**:
Agreement of independent documents on the same claim, within tolerance. A single-source claim caps its confidence; a divergent pair raises a disagreement, never an average.
_Avoid_: cross-check (that word is reserved for validation checks)

**Citation grounding**:
The grade a narrative claim gets instead of a numeric score. Two judge models from different families each answer two questions: does the answer STATE the claim, and do the answer's cited quotes ENTAIL it. The claim passes only on both, and only when the two judges agree.
_Avoid_: fact check, verification

**Narrative checklist**:
The reasons a good first-pass note should mention for one gold case. Checklist items carry no gold value; citation grounding grades them.
_Avoid_: rubric, criteria

**Location coverage**:
The share of a cross-reference case's required pages that the answer cited. It measures retrieval, never correctness: a case passes only when location coverage AND judged fact accuracy pass.
_Avoid_: recall (that word is reserved for driver scoring)
