---
rating: ⭐⭐
title: data-visualizer
url: https://skills.sh/guia-matthieu/clawfu-skills/data-visualizer
---

# data-visualizer

skills/guia-matthieu/clawfu-skills/data-visualizer
data-visualizer
Installation
$ npx skills add https://github.com/guia-matthieu/clawfu-skills --skill data-visualizer
SKILL.md
Data Visualizer

Generate professional charts and visualizations from CSV data for marketing reports.

What Claude Does vs What You Decide
Claude Does	You Decide
Structures analysis frameworks	Metric definitions
Identifies patterns in data	Business interpretation
Creates visualization templates	Dashboard design
Suggests optimization areas	Action priorities
Calculates statistical measures	Decision thresholds
Dependencies
pip install plotly pandas click

Commands
python scripts/main.py chart data.csv --type bar --x month --y revenue
python scripts/main.py dashboard data.csv --metrics "revenue,users,churn"
python scripts/main.py export chart.html --format png

Skill Boundaries
What This Skill Does Well
Structuring data analysis
Identifying patterns and trends
Creating visualization frameworks
Calculating statistical measures
What This Skill Cannot Do
Access your actual data
Replace statistical expertise
Make business decisions
Guarantee prediction accuracy
Skill Metadata
Mode: centaur
category: automation
dependencies: [plotly, pandas]
difficulty: beginner

Weekly Installs
92
Repository
guia-matthieu/c…u-skills
GitHub Stars
85
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass