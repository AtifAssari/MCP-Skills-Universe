---
title: prioritize-assumptions
url: https://skills.sh/phuryn/pm-skills/prioritize-assumptions
---

# prioritize-assumptions

skills/phuryn/pm-skills/prioritize-assumptions
prioritize-assumptions
Installation
$ npx skills add https://github.com/phuryn/pm-skills --skill prioritize-assumptions
SKILL.md
Prioritize Assumptions

Triage assumptions using an Impact × Risk matrix and suggest targeted experiments.

Context

You are helping prioritize assumptions for $ARGUMENTS.

If the user provides files with assumptions or research data, read them first.

Domain Context

ICE works well for assumption prioritization: Impact (Opportunity Score × # Customers) × Confidence (1–10) × Ease (1–10). Opportunity Score = Importance × (1 − Satisfaction), normalized to 0–1 (Dan Olsen). RICE splits Impact into Reach × Impact separately: (R × I × C) / E. See the prioritization-frameworks skill for full formulas and templates.

Instructions

The user will provide a list of assumptions to prioritize. Apply the following framework:

For each assumption, evaluate two dimensions:

Impact: The value created by validating this assumption AND the number of customers affected (in ICE: Impact = Opportunity Score × # Customers)
Risk: Defined as (1 - Confidence) × Effort

Categorize each assumption using the Impact × Risk matrix:

Low Impact, Low Risk → Defer testing until higher-priority assumptions are addressed
High Impact, Low Risk → Proceed to implementation (low risk, high reward)
Low Impact, High Risk → Reject the idea (not worth the investment)
High Impact, High Risk → Design an experiment to test it

For each assumption requiring testing, suggest an experiment that:

Maximizes validated learning with minimal effort
Measures actual behavior, not opinions
Has a clear success metric and threshold

Present results as a prioritized matrix or table.

Think step by step. Save as markdown if the output is substantial.

Further Reading
Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions
Continuous Product Discovery Masterclass (CPDM) (video course)
Weekly Installs
548
Repository
phuryn/pm-skills
GitHub Stars
10.8K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass