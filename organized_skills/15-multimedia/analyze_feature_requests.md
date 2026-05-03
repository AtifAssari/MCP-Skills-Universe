---
rating: ⭐⭐
title: analyze-feature-requests
url: https://skills.sh/phuryn/pm-skills/analyze-feature-requests
---

# analyze-feature-requests

skills/phuryn/pm-skills/analyze-feature-requests
analyze-feature-requests
Installation
$ npx skills add https://github.com/phuryn/pm-skills --skill analyze-feature-requests
SKILL.md
Analyze Feature Requests

Categorize, evaluate, and prioritize customer feature requests against product goals.

Context

You are analyzing feature requests for $ARGUMENTS.

If the user provides files (spreadsheets, CSVs, or documents with feature requests), read and analyze them directly. If data is in a structured format, consider creating a summary table.

Domain Context

Never allow customers to design solutions. Prioritize opportunities (problems), not features. Use Opportunity Score (Dan Olsen) to evaluate customer-reported problems: Opportunity Score = Importance × (1 − Satisfaction), normalized to 0–1. See the prioritization-frameworks skill for full details and templates.

Instructions

The user will describe their product goal and provide feature requests. Work through these steps:

Understand the goal: Confirm the product objective and desired outcomes that will guide prioritization.

Categorize requests into themes: Group related requests together and name each theme.

Assess strategic alignment: For each theme, evaluate how well it aligns with the stated goals.

Prioritize the top 3 features based on:

Impact: Customer value and number of users affected
Effort: Development and design resources required
Risk: Technical and market uncertainty
Strategic alignment: Fit with product vision and goals

For each top feature, provide:

Rationale (customer needs, strategic alignment)
Alternative solutions worth considering
High-risk assumptions
How to test those assumptions with minimal effort

Think step by step. Save as markdown or create a structured output document.

Further Reading
Kano Model: How to Delight Your Customers Without Becoming a Feature Factory
Continuous Product Discovery Masterclass (CPDM) (video course)
Weekly Installs
555
Repository
phuryn/pm-skills
GitHub Stars
10.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass