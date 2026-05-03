---
rating: ⭐⭐
title: product-health-analysis
url: https://skills.sh/mohitagw15856/pm-claude-skills/product-health-analysis
---

# product-health-analysis

skills/mohitagw15856/pm-claude-skills/product-health-analysis
product-health-analysis
Installation
$ npx skills add https://github.com/mohitagw15856/pm-claude-skills --skill product-health-analysis
SKILL.md
Product Health Analysis Skill

Transform raw metrics data into a clear health narrative — what's working, what's not, and what needs immediate attention.

Required Inputs

Ask the user for these if not provided:

Metrics data (current values for key metrics — even rough numbers work)
Targets or benchmarks (OKR targets, historical baselines, or industry benchmarks)
Period (week / month / quarter being analysed)
Product area or segment (are we looking at the whole product or a specific feature?)
Metrics Framework

Analyse across four layers:

Acquisition — new users, source quality, CAC trends
Activation — time to first value, onboarding completion rates
Engagement — DAU/MAU, feature adoption, session depth
Retention — D1/D7/D30 retention, churn rate, resurrection rate
Process
For each metric, compare: current period vs. previous period, current vs. target
Flag anything more than 10% off target as requiring investigation
Look for correlations — does a drop in activation explain a retention dip 2 weeks later?
Write a plain-English health summary (no jargon) suitable for sharing with non-data stakeholders
Recommend top 3 areas for immediate investigation with suggested diagnostic steps
Validate — Confirm every flagged metric has a plausible root cause hypothesis, not just a raw number, and every recommended action has a specific owner or team
Output Structure
Product Health Report — [Period]

Overall Health: 🟢 On Track / 🟡 Watch / 🔴 Action Required

Metric	Current	Target	vs. Last Period	Status
[metric]	[value]	[target]	[+/-%]	[🟢/🟡/🔴]

Key Observations: [3-5 bullet observations written in plain English]

Areas Requiring Investigation:

[Metric + hypothesis + suggested diagnostic]
[Metric + hypothesis + suggested diagnostic]
[Metric + hypothesis + suggested diagnostic]

Recommended Actions: [Specific next steps with owners and timelines]

Quality Checks
 Every metric includes both a target and a trend (not just a snapshot)
 At least one correlation is drawn between metrics (e.g., activation → retention)
 Every flagged metric has a root cause hypothesis, not just "it dropped"
 Observations are written for a non-technical stakeholder (no raw query language or data jargon)
 Overall health rating is justified with specific evidence
Weekly Installs
12
Repository
mohitagw15856/p…e-skills
GitHub Stars
293
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass