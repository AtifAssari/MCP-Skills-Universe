---
title: review-fix-all
url: https://skills.sh/willbooster/agent-skills/review-fix-all
---

# review-fix-all

skills/willbooster/agent-skills/review-fix-all
review-fix-all
Installation
$ npx skills add https://github.com/willbooster/agent-skills --skill review-fix-all
SKILL.md
Review workflow
Run the following command with a 1-hour timeout (RUN IT AS A BLOCKING, FOREGROUND TASK TO PREVENT PREMATURE TERMINATION): bunx @willbooster/agent-skills@latest review --agent all
Treat the combined output as candidate review comments generated concurrently by multiple agents.
Merge the review results into a single set of candidate comments, deduplicating those that address the same underlying issue.
If there are no candidate comments, quit the workflow without modifying the code.
Determine whether each candidate comment is still valid for the current codebase.
Address valid review comments by updating the code. For invalid comments, add explanatory comments to the code detailing why the existing implementation is necessary.
If there are valid review comments that are out of scope for the current PR, create new issues for them.
If you made any code changes, commit and push them to the current branch.
If you fixed any valid comments, return to step 1. Otherwise, quit the workflow.
Weekly Installs
50
Repository
willbooster/agent-skills
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn