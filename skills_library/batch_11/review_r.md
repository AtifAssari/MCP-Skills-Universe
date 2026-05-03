---
title: review-r
url: https://skills.sh/pedrohcgs/claude-code-my-workflow/review-r
---

# review-r

skills/pedrohcgs/claude-code-my-workflow/review-r
review-r
Installation
$ npx skills add https://github.com/pedrohcgs/claude-code-my-workflow --skill review-r
SKILL.md
Review R Scripts

Run the comprehensive R code review protocol.

Steps

Identify scripts to review:

If $ARGUMENTS is a specific .R filename: review that file only
If $ARGUMENTS is LectureN: review all R scripts matching that lecture
If $ARGUMENTS is all: review all R scripts in scripts/R/ and Figures/*/

For each script, launch the r-reviewer agent with instructions to:

Follow the full protocol in the agent instructions
Read .claude/rules/r-code-conventions.md for current standards
Save report to quality_reports/[script_name]_r_review.md

After all reviews complete, present a summary:

Total issues found per script
Breakdown by severity (Critical / High / Medium / Low)
Top 3 most critical issues

IMPORTANT: Do NOT edit any R source files. Only produce reports. Fixes are applied after user review.

Weekly Installs
16
Repository
pedrohcgs/claud…workflow
GitHub Stars
1.0K
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass