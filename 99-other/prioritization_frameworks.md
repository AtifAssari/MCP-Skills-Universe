---
rating: ⭐⭐
title: prioritization-frameworks
url: https://skills.sh/phuryn/pm-skills/prioritization-frameworks
---

# prioritization-frameworks

skills/phuryn/pm-skills/prioritization-frameworks
prioritization-frameworks
Installation
$ npx skills add https://github.com/phuryn/pm-skills --skill prioritization-frameworks
SKILL.md
Prioritization Frameworks Reference

A reference guide to help you select and apply the right prioritization framework for your context.

Core Principle

Never allow customers to design solutions. Prioritize problems (opportunities), not features.

Opportunity Score (Dan Olsen, The Lean Product Playbook)

The recommended framework for prioritizing customer problems.

Survey customers on Importance and Satisfaction for each need (normalize to 0–1 scale).

Three related formulas:

Current value = Importance × Satisfaction
Opportunity Score = Importance × (1 − Satisfaction)
Customer value created = Importance × (S2 − S1), where S1 = satisfaction before, S2 = satisfaction after

High Importance + low Satisfaction = highest Opportunity Score = best opportunities. Plot on an Importance vs Satisfaction chart — upper-left quadrant is the sweet spot. Prioritizes customer problems, not solutions.

ICE Framework

Useful for prioritizing initiatives and ideas. Considers not only value but also risk and economic factors.

I (Impact) = Opportunity Score × Number of Customers affected
C (Confidence) = How confident are we? (1-10). Accounts for risk.
E (Ease) = How easy is it to implement? (1-10). Accounts for economic factors.

Score = I × C × E. Higher = prioritize first.

RICE Framework

Splits ICE's Impact into two separate factors. Useful for larger teams that need more granularity.

R (Reach) = Number of customers affected
I (Impact) = Opportunity Score (value per customer)
C (Confidence) = How confident are we? (0-100%)
E (Effort) = How much effort to implement? (person-months)

Score = (R × I × C) / E

9 Frameworks Overview
Framework	Best For	Key Insight
Eisenhower Matrix	Personal tasks	Urgent vs Important — for individual PM task management
Impact vs Effort	Tasks/initiatives	Simple 2×2 — quick triage, not rigorous for strategic decisions
Risk vs Reward	Initiatives	Like Impact vs Effort but accounts for uncertainty
Opportunity Score	Customer problems	Recommended. Importance × (1 − Satisfaction). Normalize to 0–1.
Kano Model	Understanding expectations	Must-be, Performance, Attractive, Indifferent, Reverse. For understanding, not prioritizing.
Weighted Decision Matrix	Multi-factor decisions	Assign weights to criteria, score each option. Useful for stakeholder buy-in.
ICE	Ideas/initiatives	Impact × Confidence × Ease. Recommended for quick prioritization.
RICE	Ideas at scale	(Reach × Impact × Confidence) / Effort. Adds Reach to ICE.
MoSCoW	Requirements	Must/Should/Could/Won't. Caution: project management origin.
Templates
Opportunity Score intro (PDF)
Importance vs Satisfaction Template — Dan Olsen (Google Slides)
ICE Template (Google Sheets)
RICE Template (Google Sheets)
Further Reading
The Product Management Frameworks Compendium + Templates
Kano Model: How to Delight Your Customers Without Becoming a Feature Factory
Continuous Product Discovery Masterclass (CPDM) (video course)
Weekly Installs
571
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