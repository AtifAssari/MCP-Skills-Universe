---
title: mfg-supplier-scorecard
url: https://skills.sh/asgard-ai-platform/skills/mfg-supplier-scorecard
---

# mfg-supplier-scorecard

skills/asgard-ai-platform/skills/mfg-supplier-scorecard
mfg-supplier-scorecard
Installation
$ npx skills add https://github.com/asgard-ai-platform/skills --skill mfg-supplier-scorecard
SKILL.md
Supplier Scorecard
Framework
IRON LAW: Evaluate on QCDS (Quality, Cost, Delivery, Service) — Not Just Price

The cheapest supplier who delivers defective parts late with no support
is the most expensive supplier. Total Cost of Ownership (TCO) includes:
purchase price + incoming inspection + rework + downtime from defects +
expediting fees + management overhead.

NEVER select suppliers on price alone.

Four Evaluation Dimensions (QCDS)
Dimension	Weight (typical)	KPIs
Quality	30-40%	Defect rate (PPM), incoming inspection pass rate, certifications (ISO 9001), corrective action responsiveness
Cost	20-30%	Unit price, total cost of ownership, price stability, payment terms
Delivery	20-30%	On-time delivery rate, lead time, lead time variability, flexibility for rush orders
Service	10-20%	Responsiveness, communication quality, technical support, willingness to collaborate on improvements
Scoring Method
Define KPIs per dimension (2-3 per dimension)
Set weights (must sum to 100%)
Score each KPI: 1-5 scale with clear definitions:
5 = Excellent (top 10% of suppliers)
4 = Good (meets all requirements consistently)
3 = Acceptable (meets most requirements)
2 = Below expectations (frequent issues)
1 = Unacceptable (critical problems)
Calculate weighted total
Classify: A (>4.0), B (3.0-4.0), C (2.0-3.0), D (<2.0)
Supplier Classification & Actions
Grade	Score	Strategy
A	>4.0	Preferred supplier, increase business, joint development
B	3.0-4.0	Approved supplier, maintain, targeted improvement
C	2.0-3.0	Conditional, improvement plan required within 90 days
D	<2.0	Phase out, begin alternative sourcing immediately
Risk Assessment
Risk Factor	Question	Mitigation
Single source	Is this supplier the only source for a critical component?	Develop backup supplier
Geographic	Is the supplier in a region prone to disruption?	Dual-source across regions
Financial	Is the supplier financially stable?	Monitor credit, require financial disclosures
Capacity	Can the supplier scale with our growth?	Capacity commitment agreements
IP	Does the supplier have access to our proprietary designs?	NDA + IP clauses in contract
Supplier Development Program (SDP)

For C-grade suppliers worth keeping:

Gap analysis: Where specifically are they falling short?
Improvement plan: Specific, measurable, time-bound targets
Support: Provide training, share best practices, co-invest if needed
Review: Monthly progress checks, 90-day formal reassessment
Decision: Improved to B+ → continue. Still C or worse → phase out.
Output Format
# Supplier Scorecard: {Supplier Name}

## Overall Score: {X.X} / 5.0 — Grade: {A/B/C/D}

## Detailed Scores
| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|---------|
| Quality | {%} | {X.X} | {X.XX} |
| Cost | {%} | {X.X} | {X.XX} |
| Delivery | {%} | {X.X} | {X.XX} |
| Service | {%} | {X.X} | {X.XX} |
| **Total** | **100%** | — | **{X.XX}** |

## KPI Details
| KPI | Target | Actual | Score |
|-----|--------|--------|-------|
| Defect rate | <500 PPM | {X} PPM | {1-5} |
| On-time delivery | >95% | {%} | {1-5} |
| ... | ... | ... | ... |

## Risk Assessment
| Risk | Level | Mitigation |
|------|-------|-----------|
| {risk} | H/M/L | {action} |

## Action Plan
{Based on grade: preferred/maintain/improve/phase out}

Gotchas
Weighting should reflect YOUR priorities: A medical device company should weight Quality at 50%+. A commodity buyer might weight Cost at 40%. Don't use generic weights.
Score inflation: Purchasing teams may inflate scores to avoid difficult conversations with suppliers. Require data-backed evidence for each score.
Review frequency: A-grade quarterly, B/C-grade monthly, D-grade weekly until resolved.
Supplier relationship matters: Scorecards are tools for improvement, not punishment. Share results with suppliers transparently — the best suppliers want feedback.
TCO includes hidden costs: Don't forget: incoming inspection labor, warehouse space for safety stock (to cover unreliable delivery), engineering time for quality issues, customs/logistics for overseas suppliers.
References
For TCO calculation methodology, see references/tco-calculation.md
For supplier audit checklists, see references/supplier-audit.md
Weekly Installs
22
Repository
asgard-ai-platf…m/skills
GitHub Stars
126
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass