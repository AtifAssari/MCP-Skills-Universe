---
rating: ⭐⭐
title: report-generator
url: https://skills.sh/guia-matthieu/clawfu-skills/report-generator
---

# report-generator

skills/guia-matthieu/clawfu-skills/report-generator
report-generator
Installation
$ npx skills add https://github.com/guia-matthieu/clawfu-skills --skill report-generator
SKILL.md
Report Generator

Automate marketing report generation from templates and data sources.

What Claude Does vs What You Decide
Claude Does	You Decide
Structures analysis frameworks	Metric definitions
Identifies patterns in data	Business interpretation
Creates visualization templates	Dashboard design
Suggests optimization areas	Action priorities
Calculates statistical measures	Decision thresholds
Dependencies
pip install jinja2 pandas click
# For PDF output:
pip install weasyprint

Commands
python scripts/main.py generate template.html --data data.json --output report.html
python scripts/main.py weekly metrics.csv --output weekly-report.html
python scripts/main.py client data/ --template agency --output client-report.pdf

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
dependencies: [jinja2, pandas]
difficulty: intermediate

Weekly Installs
92
Repository
guia-matthieu/c…u-skills
GitHub Stars
85
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass