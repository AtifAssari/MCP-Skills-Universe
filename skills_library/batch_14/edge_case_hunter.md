---
title: edge-case-hunter
url: https://skills.sh/sungkhum/agent-skills-pack/edge-case-hunter
---

# edge-case-hunter

skills/sungkhum/agent-skills-pack/edge-case-hunter
edge-case-hunter
Installation
$ npx skills add https://github.com/sungkhum/agent-skills-pack --skill edge-case-hunter
SKILL.md
Edge Case Hunter Review
Overview

Perform a strict, method-driven edge-case review. This is not a general code review: report only unhandled paths and boundary conditions.

Inputs
content: Diff, full file, or function to analyze.
also_consider (optional): Areas to keep in mind while tracing paths.
Workflow

Follow references/workflow.md exactly. Do not add commentary or extra sections. Output must be valid JSON only.

Output Rules
Return a JSON array of findings with fields: location, trigger_condition, guard_snippet, potential_consequence.
If none found, return [].
If input is empty or undecodable, return the required single-item array from the workflow.
Reference
references/workflow.md for the canonical step-by-step instructions and output format.
Weekly Installs
11
Repository
sungkhum/agent-…lls-pack
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass