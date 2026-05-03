---
title: data-analysis-standard
url: https://skills.sh/mohitagw15856/pm-claude-skills/data-analysis-standard
---

# data-analysis-standard

skills/mohitagw15856/pm-claude-skills/data-analysis-standard
data-analysis-standard
Installation
$ npx skills add https://github.com/mohitagw15856/pm-claude-skills --skill data-analysis-standard
SKILL.md
Data Analysis Standard Skill

Turn raw numbers into product decisions. Structure every analysis with a clear question, methodology, finding, and recommended action.

Analysis Framework: The 4-Question Method

Every analysis starts here:

What changed? (describe the metric and its movement)
Why did it change? (root cause — segment, funnel step, cohort, channel)
So what? (business or product impact)
Now what? (recommended action with confidence level)

Never deliver data without answering all four. A chart with no narrative is not an analysis.

Metric Triage Template

Use when a metric has moved unexpectedly:

METRIC: [Name]
MOVEMENT: [X% change over Y period]
BASELINE: [What was normal]

SEGMENTATION CHECK:
- By platform (iOS / Android / Web)?
- By user cohort (new / returning / power users)?
- By acquisition channel?
- By geography?
- By plan/tier?

ROOT CAUSE HYPOTHESIS:
1. [Most likely explanation] — Evidence: [data point]
2. [Alternative explanation] — Evidence: [data point]
3. [Ruling out] — Eliminated because: [reason]

CONCLUSION: [Single sentence answer to "why did this change?"]
CONFIDENCE: [High / Medium / Low] — based on [data available]

Funnel Analysis Structure
Stage	Metric	Current	Benchmark/Target	Drop-off %	Notes
[Top of funnel]	[Users]	[N]	[N]	—	
[Step 2]	[Users]	[N]	[N]	[X%]	
[Step 3]	[Users]	[N]	[N]	[X%]	
[Conversion]	[Users]	[N]	[N]	[X%]	

Biggest drop-off: [Step X → Step Y] — Hypothesis: [reason] Recommended investigation: [specific query or test]

Cohort Analysis Guidelines

Always define:

Cohort definition: [What groups users — signup week, first action, plan type]
Retention metric: [What counts as retained — login, core action, revenue]
Retention window: [D1, D7, D30, W4, M3, etc.]

Output a cohort retention table and annotate:

Baseline retention for each cohort
Cohorts that over/underperform and why (feature launch? campaign? seasonal?)
Trend direction across cohorts (improving / declining / stable)
Stakeholder Analysis Output Format
[Analysis Title] — [Date]

Question being answered: [Specific question in plain English] Time period: [Date range] Data source: [Where data comes from]

Finding:

[1–2 sentence plain-English summary of what the data shows]

Key chart / table: [Include or describe]

Root cause: [Best explanation with evidence]

Confidence level: [High / Medium / Low] — [reason]

Recommended action:

[Immediate action — owner, timeline]
[Investigation needed — what to check next]
[Monitoring — what metric to watch and at what cadence]

What this analysis does NOT tell us: [Important caveat — what data is missing or what can't be concluded]

Required Inputs

Ask the user for these if not provided:

Metric or question being investigated
Time period (what changed, from when to when)
Data available (which segments, sources, or queries you have access to)
Business context (what decision this analysis informs)
Audience (who will read this — exec / team / data team)
Quality Checks
 Analysis answers all 4 questions: what changed, why, so what, now what
 Root cause has evidence (not just hypothesis)
 Confidence level is stated and justified
 What the data cannot tell us is explicitly named
 Recommended action includes an owner and timeline
Guidelines
Always state what the data cannot tell you — never oversell confidence
Correlations are not causation — flag this every time
If the user has no baseline, recommend establishing one before drawing conclusions
Recommend the simplest chart for each finding: bar for comparison, line for trends, scatter for correlation, table for detailed breakdowns
Always specify the time window — "conversion dropped" is meaningless without "from X to Y over Z period"
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