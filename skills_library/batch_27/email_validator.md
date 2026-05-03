---
title: email-validator
url: https://skills.sh/guia-matthieu/clawfu-skills/email-validator
---

# email-validator

skills/guia-matthieu/clawfu-skills/email-validator
email-validator
Installation
$ npx skills add https://github.com/guia-matthieu/clawfu-skills --skill email-validator
SKILL.md
Email Validator

Validate email addresses and clean lists to improve deliverability and reduce bounces.

What Claude Does vs What You Decide
Claude Does	You Decide
Structures analysis frameworks	Metric definitions
Identifies patterns in data	Business interpretation
Creates visualization templates	Dashboard design
Suggests optimization areas	Action priorities
Calculates statistical measures	Decision thresholds
Dependencies
pip install email-validator dnspython click

Commands
python scripts/main.py validate email@example.com
python scripts/main.py batch emails.csv --column email --output clean.csv
python scripts/main.py clean emails.txt --remove-disposable

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
category: email-tools
dependencies: [email-validator, dnspython]
difficulty: beginner

Weekly Installs
97
Repository
guia-matthieu/c…u-skills
GitHub Stars
85
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass