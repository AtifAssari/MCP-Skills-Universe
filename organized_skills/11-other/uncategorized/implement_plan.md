---
rating: ⭐⭐
title: implement-plan
url: https://skills.sh/jim60105/copilot-prompt/implement-plan
---

# implement-plan

skills/jim60105/copilot-prompt/implement-plan
implement-plan
Installation
$ npx skills add https://github.com/jim60105/copilot-prompt --skill implement-plan
SKILL.md
Implement Plan

Implement a development plan from GitHub Issues using the full GitHub DevOps workflow.

Key Directives
Git commit after completing work using conventional commit format. Always commit with --signoff. Write commits in English.
Create a comprehensive work report as PR details or comments, detailing the work performed, code changes, and test results for the project.

Implementation Stage is to implement the plan step by step, following the instructions provided in the issue and submit a work report PR at last

This time, the work requires greater accuracy. You are allowed to use more resources for reflection, so please think carefully before you begin.

Steps

Check Current Situation: Run git status to check the repository state to ensure you are aware of any uncommitted changes or issues before proceeding with any operations. If not on the master branch, you may still be in the half implementation state, check git logs between current branch and master to see what's been done. If on master, start fresh with a new issue.

Get Issue Lists: Get the list of issues to see all backlogs and bugs. Find the issue the user wants or the one currently in progress, you can list all of them and ask user to assign you an issue.

Get Issue Details: Read the issue details to understand requirements and implementation plan. The content includes comprehensive technical designs — read carefully and Do not skip this step.

Get Issue Comments: Read comments to understand context and any additional requirements or discussions that have taken place. Determine whether this issue has been completed, needs further work, or has problems to fix. Do not skip this step.

Get Pull Requests: List existing PRs to check if any relate to the current issue. Read them to determine completion status. Do not skip this step.

Git Checkout: Create an issue branch: git checkout -b issue-[issue_number]-[short_description]. Skip if already on the correct branch.

Implementation: Implement the plan step by step following the issue instructions. Each step should be executed in sequence, ensuring that all requirements are met and documented appropriately.

Testing & Linting: Run tests and linting to ensure quality and compliance.

Self Review: Review code changes to ensure they meet issue requirements and you have not missed any details.

Git Commit & Push: Commit using conventional format with --signoff and author GitHub Copilot <bot@ChenJ.im>. Link the issue number in the commit message body. Push changes. Write the commit in English.

Create Pull Request: ALWAYS SUBMIT PR TO origin, NEVER TO upstream. Create a PR if none exists for this issue. Write PR title in English using conventional commit format. Write PR body in 正體中文 as a comprehensive work report. Link the issue with Resolves #[issue_number] at the end of the PR body.ALWAYS SUBMIT PR TO origin, NEVER SUBMIT PR TO upstream. ALWAYS SUBMIT PR TO origin, NEVER SUBMIT PR TO upstream. ALWAYS SUBMIT PR TO origin, NEVER SUBMIT PR to upstream.

Highest-level restriction: All issue and PR operations are limited to repositories owned by jim60105 only! Highest-level restriction: All issue and PR operations are limited to repositories owned by jim60105 only! Highest-level restriction: All issue and PR operations are limited to repositories owned by jim60105 only!

Weekly Installs
9
Repository
jim60105/copilot-prompt
GitHub Stars
18
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn