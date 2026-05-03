---
rating: ⭐⭐
title: review-plan-implementation
url: https://skills.sh/tstelzer/skills/review-plan-implementation
---

# review-plan-implementation

skills/tstelzer/skills/review-plan-implementation
review-plan-implementation
Installation
$ npx skills add https://github.com/tstelzer/skills --skill review-plan-implementation
SKILL.md
Review Implementation
Inputs
Plan location (file path)
Git commit(s) that implemented the plan (hashes or ranges), or assume HEAD~
Workflow
Open and read the plan file; note promised behavior, tasks, files, and verify steps.
Inspect the specified commit(s) and identify the files and changes related to the plan.
Review the implementation against the plan, prioritizing the following list, unless the user says otherwise
performance
security
extensibility
testability
comprehensibility
Call out mismatches between plan and implementation, missing steps, or unverified tasks.
Provide actionable fixes and any tests or checks to run.
Output
Findings ordered by severity with file/line references
Open questions or assumptions
Brief change summary
Examples
"Review the implementation of this plan: plans/2026-02-19-1200_cache.md. Commits: 1a2b3c4, 9d8e7f6."
Weekly Installs
31
Repository
tstelzer/skills
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass