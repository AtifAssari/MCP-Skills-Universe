---
title: wbfy
url: https://skills.sh/willbooster/agent-skills/wbfy
---

# wbfy

skills/willbooster/agent-skills/wbfy
wbfy
Installation
$ npx skills add https://github.com/willbooster/agent-skills --skill wbfy
SKILL.md
wbfy application workflow
If the current branch is main, create and switch to a new branch based on the latest remote main branch.
Ensure the new branch is derived from the latest remote main branch to prevent merge conflicts when opening a pull request (PR).
Run yarn start <root_path_of_target_repo> inside ~/ghq/github.com/WillBooster/shared/packages/wbfy.
Run either yarn check-for-ai or bun check-for-ai in the target repository (do not run this within the wbfy directory).
If any checks fail, resolve them using one of the following methods:
If the failure originates in the target repository (e.g., existing code violates new linter rules), fix the issue there, commit and push the changes, then return to step 3.
If the failure is caused by configuration files modified by wbfy (e.g., a wbfy-edited tsconfig.json does not match the target repository), fix the issue in the wbfy directory, commit and push the changes, open a PR in the wbfy repository, then return to step 2.
Ensure wbfy generates the correct configuration files without manual adjustments, as all projects rely on its automation.
Avoid ad-hoc hotfixes; prefer general and versatile solutions applicable to all projects.
Add comments to the wbfy codebase to clarify the reasoning behind your fixes.
Commit and push the applied changes to the target repository, then run either the open-pr or update-pr skill.
Since wbfy creates, modifies, and deletes multiple files in the target repository, verify that all changes are included in your commit.
Weekly Installs
20
Repository
willbooster/agent-skills
GitHub Stars
1
First Seen
10 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass