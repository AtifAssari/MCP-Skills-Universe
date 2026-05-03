---
title: internal-comms
url: https://skills.sh/composiohq/awesome-claude-skills/internal-comms
---

# internal-comms

skills/composiohq/awesome-claude-skills/internal-comms
internal-comms
Originally fromanthropics/skills
Installation
$ npx skills add https://github.com/composiohq/awesome-claude-skills --skill internal-comms
Summary

Templates and guidelines for writing company-standard internal communications across multiple formats.

Covers seven communication types: 3P updates, company newsletters, FAQ responses, status reports, leadership updates, project updates, and incident reports
Provides format-specific guideline files in the examples/ directory to ensure consistency with company conventions
Includes a fallback general communications template for formats not explicitly covered by dedicated guidelines
Designed to be invoked automatically when Claude detects internal communication requests, eliminating manual format lookups
SKILL.md
When to use this skill

To write internal communications, use this skill for:

3P updates (Progress, Plans, Problems)
Company newsletters
FAQ responses
Status reports
Leadership updates
Project updates
Incident reports
How to use this skill

To write any internal communication:

Identify the communication type from the request
Load the appropriate guideline file from the examples/ directory:
examples/3p-updates.md - For Progress/Plans/Problems team updates
examples/company-newsletter.md - For company-wide newsletters
examples/faq-answers.md - For answering frequently asked questions
examples/general-comms.md - For anything else that doesn't explicitly match one of the above
Follow the specific instructions in that file for formatting, tone, and content gathering

If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.

Keywords

3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms

Weekly Installs
1.6K
Repository
composiohq/awes…e-skills
GitHub Stars
57.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass