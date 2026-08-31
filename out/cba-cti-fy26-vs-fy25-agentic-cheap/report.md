# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income (%)', column Full Year Ended 30 Jun 25 -> column Full Year Ended 30 Jun 26*

CBA's cash-basis cost-to-income ratio (operating expenses to total operating income) improved by 20 basis points (−0.2 ppt) to 45.5% in FY26 from 45.7% in FY25. The improvement was driven by operating income growing 6.2% ($28,465m to $30,224m), outpacing total operating expense growth of 5.8% ($12,996m to $13,755m). Underlying cost-to-income improved 30 bpts (45.2% to 44.9%), but higher restructuring and notable items ($130m to $170m) offset 10 bpts of that gain.

> [ev-10] CBA/FY26/profit_announcement, printed p3: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts"
> [ev-15] CBA/FY26/results_presentation, printed p54: "Cost to income 45.5% (20bpts)"
> [ev-16] CBA/FY26/results_presentation, printed p54: "Operating income ($m) 30,224 +6.2%"
> [ev-17] CBA/FY26/results_presentation, printed p54: "Operating expenses ($m) 13,755 +5.8%"
> [ev-22] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts"

### income_growth — "Operating income"
*unquantified | confidence 85/100*

Operating income grew 6.2% ($28,465m to $30,224m), pulling the ratio down. Net interest income contributed +$1,563m, driven by average lending volume growth (home loans +5%, business loans +10%, institutional loans +11%) and deposit volume growth (+8%), with broadly stable margin excluding liquids and repos. Other operating income contributed +$196m, supported by higher insurance income, higher CommSec equities income from growth in trading volumes, and benefit of one-off gains including a milestone payment from the sale of CommInsure General Insurance and a fair value gain on Gemini IPO, partly offset by lower retail foreign exchange income.
> [ev-20] CBA/FY26/results_presentation, printed p25: "28,465 30,224 1,563 196 FY25 Net interest income Other operating income FY26"
> [ev-11] CBA/FY26/profit_announcement, printed p2: "Total operating income 30,224 28,465 6"

### expense_growth — "Underlying operating expenses"
*unquantified | confidence 85/100*

Underlying operating expenses grew 5.6% ($12,866m to $13,585m), pushing the ratio up. The walk breaks this into: inflation +$455m (wage inflation including higher super guarantee, vendor IT inflation +5%, higher cloud consumption and software licensing); investment in technology +$444m (cloud consumption, software licensing, infrastructure, resilience and AI capabilities); investment in frontline and operations +$128m; other +$96m; partially offset by productivity −$404m (cumulative cost savings realised over last 8 years: $2,472m in FY26 vs $2,068m in FY25). Staff expenses rose 4% to $8,258m, IT services expenses rose 16% to $2,782m, occupancy decreased 2% to $938m, and other expenses rose 4% to $1,607m.
> [ev-18] CBA/FY26/results_presentation, printed p27: "455 444 128 96 (404) 12,866 13,585 FY25 Inflation Investment in technology Investment in frontline and operations Other Productivity FY26"
> [ev-12] CBA/FY26/profit_announcement, printed p2: "Underlying operating expenses (13,585) (12,866) 6"

### notable_items — "Restructuring and notable items"
*unquantified | confidence 85/100*

Restructuring and notable items increased $40m (31%) from $130m in FY25 to $170m in FY26, adding to the expense base and raising the headline ratio. FY26 items relate to provisions for the settlement of legal proceedings in New Zealand, an additional goodwill payment made to certain customers as a result of ASIC's Better Banking review, and domestic customer remediation. FY25 items included domestic and NZ customer remediation as well as a Bankwest restructuring provision.
> [ev-13] CBA/FY26/profit_announcement, printed p2: "Restructuring and notable items (170) (130) 31"
> [ev-14] CBA/FY26/profit_announcement, printed p2: "Total operating expenses (13,755) (12,996) 6"

## Limitations
- The bank does not publish a formal waterfall or bridge chart decomposing the cost-to-income ratio movement into ppt contributions. Driver contributions are therefore unquantified in ppt terms; the narrative reports the growth rates and dollar movements the bank discloses.
- The results presentation provides primary-year walk charts for operating income (NII +$1,563m, OOI +$196m) and underlying operating expenses (inflation +$455m, tech +$444m, frontline +$128m, other +$96m, productivity −$404m), but no corresponding CTI-specific walk.
- A divisional cost-to-income ratio exists (RBS 39.3%, BB 32.2%, IB&M 40.6%, NZ 46.4%) but is not used for the Group-level movement.
- Confidence capped at 85 per source hierarchy rule since corroborating evidence comes from two documents (profit announcement and results presentation) but neither provides a formal CTI ppt decomposition.
- Failed check: no_quantified_drivers

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-31T01:08:53+00:00
- seconds: 321.5
- cost_usd: 0.0554
- tokens: 1721257 in / 10364 out
- orchestration: agent
- tool_calls: 60
- pages_read: 25
- charts_read: 2
- budget_exhausted: no
