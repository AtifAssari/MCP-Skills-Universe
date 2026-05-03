---
title: skill-reviewer
url: https://skills.sh/microsoft/github-copilot-for-azure/skill-reviewer
---

# skill-reviewer

skills/microsoft/github-copilot-for-azure/skill-reviewer
skill-reviewer
Installation
$ npx skills add https://github.com/microsoft/github-copilot-for-azure --skill skill-reviewer
SKILL.md
Skill PR Reviewer

Performs thorough, structured code reviews of skill PRs — severity-classified findings with actionable fixes, positive acknowledgment, and a summary table.

When to Use
Reviewing a PR that adds or modifies a skill under plugin/skills/ or .github/skills/
Checking skill compliance before submitting a PR
Auditing an existing skill for quality issues

💡 Note: .github/skills/ meta-skills have different conventions — checklist sections 8-9 apply only to plugin/skills/ service skills.

Review Workflow
Collect — Identify all changed skill files (SKILL.md, references, tests, scripts)
Check — Run each category from the review checklist
Classify — Assign severity per the severity guide
Analyze Routing — Check triggers for conflicts per routing analysis
Draft — Write the review per the output format
Validate — Verify suggested fixes are actionable with accurate file/line references
Error Handling
Error	Remediation
Cannot determine changed files	Ask user for the file list or PR number
Token counting unavailable	Estimate at ~4 chars per token
References
Review Checklist
Severity Classification
Routing Analysis
Output Format
Weekly Installs
89
Repository
microsoft/githu…or-azure
GitHub Stars
202
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass