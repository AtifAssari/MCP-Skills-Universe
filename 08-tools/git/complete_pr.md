---
title: complete-pr
url: https://skills.sh/willbooster/agent-skills/complete-pr
---

# complete-pr

skills/willbooster/agent-skills/complete-pr
complete-pr
Installation
$ npx skills add https://github.com/willbooster/agent-skills --skill complete-pr
SKILL.md

Use the fetch-pr skill to read the PR body and its messages. Fetch the latest changes from the remote. If the remote default branch has new commits, merge it into the current branch, resolve any conflicts, and push the changes. Next, fetch the current repository owner using the command gh repo view --json owner --jq '.owner.login'. If the owner is WillBooster or WillBoosterLab, follow the first workflow below; otherwise, follow the second workflow.

Workflow for WillBooster or WillBoosterLab repositories
Check the CI (GitHub Actions) results using the check-pr-ci skill.
If any workflow fails, pull the latest remote changes, resolve the issues, commit, push, and return to step 1. Otherwise, proceed to the next step.
Fetch unresolved review threads using the manage-pr-review-threads skill.
Review each unresolved thread to determine if it requires code or documentation changes. Validate each claim against the current codebase first, and reproduce issues or consult official documentation when necessary instead of relying on memory.
Address valid review comments by updating the code. For invalid comments, add explanatory comments to the code detailing why the existing implementation is necessary.
If there are valid review comments that are out of scope for the current PR, create new issues for them.
Reply to all review threads using the manage-pr-review-threads skill.
If you made changes in step 5, commit and push them, post /gemini review on the PR, wait for 5 minutes (sleep 5m), and return to step 1.
Update the PR title and body using the update-pr skill to reflect all changes.
Workflow for the other repositories
Check the CI (GitHub Actions) results using the check-pr-ci skill.
If any workflow fails, pull the latest remote changes, resolve the issues, commit, push, and return to step 1. Otherwise, proceed to the next step.
Fetch unresolved review threads using the manage-pr-review-threads skill.
Review each unresolved thread and decide whether it requires a code or documentation change. Validate each claim against the current codebase first, and reproduce it or check official documentation when needed instead of relying on memory. Ignore only comments that are clearly outdated, incorrect, or intentionally declined with solid reasoning.
If there are valid review comments to address, make only the changes supported by the validation from step 4, commit, push, and then return to step 1.
Do not post any message like review replies on non-WillBooster repositories.
Update the PR title and body using the update-pr skill to reflect all changes.
Weekly Installs
54
Repository
willbooster/agent-skills
GitHub Stars
1
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn