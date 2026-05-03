---
rating: ⭐⭐
title: prioritize-features
url: https://skills.sh/phuryn/pm-skills/prioritize-features
---

# prioritize-features

skills/phuryn/pm-skills/prioritize-features
prioritize-features
Installation
$ npx skills add https://github.com/phuryn/pm-skills --skill prioritize-features
SKILL.md
Prioritize Feature Backlog

Evaluate and rank a backlog of feature ideas to identify the top 5 to pursue.

Context

You are helping prioritize features for $ARGUMENTS.

If the user provides files (spreadsheets, backlogs, opportunity assessments), read and analyze them directly.

Domain Context

For framework selection guidance, see the prioritization-frameworks skill. Key recommendations:

Opportunity Score (Dan Olsen, The Lean Product Playbook) is recommended for evaluating customer problems: Opportunity Score = Importance × (1 − Satisfaction), normalized to 0–1. High Importance + low Satisfaction = best opportunities. Prioritize problems (opportunities), not solutions.

ICE is recommended for quick scoring of initiatives: Impact (Opportunity Score × # Customers) × Confidence × Ease. RICE adds Reach as a separate factor for larger teams.

Instructions

The user will describe their product objective, desired outcomes, and provide feature ideas. Work through these steps:

Understand priorities: Confirm the product objective and success metrics.

Evaluate each feature against:

Impact: How much does it move the needle on desired outcomes? Consider Opportunity Score if customer data is available.
Effort: How much development, design, and coordination is required?
Risk: How much uncertainty exists? What assumptions need testing?
Strategic alignment: How well does it fit the product vision and current goals?

Recommend the top 5 features with:

Clear ranking (1-5)
Brief rationale for each selection
Key trade-offs considered
What was deprioritized and why

Present as a prioritization table if helpful.

Think step by step. Save as markdown if the output is substantial.

Further Reading
Kano Model: How to Delight Your Customers Without Becoming a Feature Factory
The Product Management Frameworks Compendium + Templates
Continuous Product Discovery Masterclass (CPDM) (video course)
Weekly Installs
564
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