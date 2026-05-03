---
rating: ⭐⭐
title: rice-prioritisation
url: https://skills.sh/mohitagw15856/pm-claude-skills/rice-prioritisation
---

# rice-prioritisation

skills/mohitagw15856/pm-claude-skills/rice-prioritisation
rice-prioritisation
Installation
$ npx skills add https://github.com/mohitagw15856/pm-claude-skills --skill rice-prioritisation
SKILL.md
RICE Prioritisation Skill

Apply consistent, criteria-based RICE scoring to a list of features or initiatives to produce an objective prioritisation ranking.

Required Inputs

Ask the user for these if not provided:

List of initiatives or features to score (names and brief descriptions)
Reach estimates (users affected per quarter — from analytics if available)
Impact estimates (use the standard scale below)
Effort estimates (person-months — from engineering if available)
Quarter or planning period
RICE Definitions (adapt to your context)
Reach: Number of users affected per quarter (use actual DAU/MAU data where available)
Impact: Effect on your primary metric — use scale: 3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal
Confidence: How certain are we about R and I estimates? 100%=high, 80%=medium, 50%=low
Effort: Person-months required across all functions
RICE Formula

RICE Score = (Reach × Impact × Confidence) / Effort

Process
For each initiative provided, gather or estimate R, I, C, E values
Flag where estimates are weak and note what data would improve them
Calculate RICE score for each
Rank highest to lowest
Flag any "quick wins" (high RICE score, low effort) and "moonshots" (high impact, high effort)
Note dependencies between items that affect sequencing
Validate — Cross-check: if the top-ranked item surprises the team, investigate whether an estimate is inflated. RICE is a tool, not a verdict.
Output Structure
RICE Prioritisation: [Backlog/Quarter]
Initiative	Reach	Impact	Confidence	Effort	RICE Score	Notes
[name]	[n]	[score]	[%]	[months]	[score]	[flags]
Recommended Sequence

[Top 5 initiatives with rationale]

Quick Wins (high score, low effort)

[Items to pick up alongside bigger bets]

Data Gaps to Address

[What information would most improve scoring accuracy]

Quality Checks
 Every initiative has all four RICE components estimated (even roughly)
 Confidence is 50% for anything without data backing (not 100% as a default)
 Quick wins and moonshots are explicitly called out
 Dependencies that affect sequencing are noted
 Any surprising ranking is investigated before accepting it
Weekly Installs
11
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