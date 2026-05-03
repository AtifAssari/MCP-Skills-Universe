---
rating: ⭐⭐
title: data-storyteller
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/data-storyteller
---

# data-storyteller

skills/dkyazzentwatwa/chatgpt-skills/data-storyteller
data-storyteller
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill data-storyteller
SKILL.md
Data Storyteller

Use this as the primary analytics skill for structured data. It now absorbs the repo's audit, comparison, statistics, pivot, experiment, and time-series helpers.

Use This For
Executive summaries and narrative reports from CSV or spreadsheet data
Data quality audits, comparisons, and anomaly reviews
Statistical analysis, pivots, experiment reads, ROI and budget analysis
Survey summaries and time-series decomposition
Workflow
Profile the dataset shape, column types, and missing-value risk.
Pick the smallest useful analysis path instead of running every script by default.
Start with scripts/data_storyteller.py when the user wants a cohesive report.
Reach for focused helpers when the task is narrow:
data_quality_auditor.py
dataset_comparer.py
correlation_explorer.py
outlier_detective.py
statistical_analyzer.py
survey_analyzer.py
ts_decomposer.py
pivot_table_generator.py
ab_test_calc.py
roi_calculator.py
budget_analyzer.py
Translate outputs into plain-English findings, risks, and next actions.
Guardrails
Do not overstate causal claims from correlations.
Call out data quality problems before presenting strong conclusions.
Keep executive summaries short and move method detail behind them.
Weekly Installs
102
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass