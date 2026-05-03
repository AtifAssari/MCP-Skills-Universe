---
title: market-research
url: https://skills.sh/sungkhum/agent-skills-pack/market-research
---

# market-research

skills/sungkhum/agent-skills-pack/market-research
market-research
Installation
$ npx skills add https://github.com/sungkhum/agent-skills-pack --skill market-research
SKILL.md
Market Research
Overview

Conduct comprehensive market research using current web data and verified sources to produce a structured research document with citations.

Prerequisite
Web search is required. If web search is unavailable, stop and tell the user.
Quick Start
Ask for research topic, goals, and scope.
Set research_type = "market", and capture research_topic and research_goals.
Create the output file using the template in references/research.template.md.
Follow the step sequence in references/market-steps/step-01-init.md onward.
Output Expectations
Provide a narrative report with clear sections and citations.
Use the user’s requested language and skill level; if not provided, ask.
References
references/workflow-market-research.md for the canonical workflow.
references/market-steps/ for the step-by-step execution.
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