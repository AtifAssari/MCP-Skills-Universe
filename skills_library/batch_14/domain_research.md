---
title: domain-research
url: https://skills.sh/sungkhum/agent-skills-pack/domain-research
---

# domain-research

skills/sungkhum/agent-skills-pack/domain-research
domain-research
Installation
$ npx skills add https://github.com/sungkhum/agent-skills-pack --skill domain-research
SKILL.md
Domain Research
Overview

Conduct comprehensive domain/industry research using current web data and verified sources to produce a structured research document with citations.

Prerequisite
Web search is required. If web search is unavailable, stop and tell the user.
Quick Start
Ask for research domain, goals, and scope.
Set research_type = "domain", and capture research_topic and research_goals.
Create the output file using the template in references/research.template.md.
Follow the step sequence in references/domain-steps/step-01-init.md onward.
Output Expectations
Provide a narrative report with clear sections and citations.
Use the user’s requested language and skill level; if not provided, ask.
References
references/workflow-domain-research.md for the canonical workflow.
references/domain-steps/ for the step-by-step execution.
references/research.template.md for the report structure.
Weekly Installs
10
Repository
sungkhum/agent-…lls-pack
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn