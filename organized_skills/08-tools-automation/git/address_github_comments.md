---
rating: ⭐⭐
title: address-github-comments
url: https://skills.sh/sickn33/antigravity-awesome-skills/address-github-comments
---

# address-github-comments

skills/sickn33/antigravity-awesome-skills/address-github-comments
address-github-comments
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill address-github-comments
Summary

Systematically address GitHub PR review comments and issue feedback using the gh CLI.

Fetches and inspects PR comments and review threads to understand feedback before applying fixes
Guides categorization and planning of comments, with user confirmation checkpoints for prioritization
Applies code changes and responds to comment threads as resolved using gh CLI commands
Requires gh authentication; includes auth status verification as a prerequisite step
SKILL.md
Address GitHub Comments
Overview

Efficiently address PR review comments or issue feedback using the GitHub CLI (gh). This skill ensures all feedback is addressed systematically.

Prerequisites

Ensure gh is authenticated.

gh auth status


If not logged in, run gh auth login.

Workflow
1. Inspect Comments

Fetch the comments for the current branch's PR.

gh pr view --comments


Or use a custom script if available to list threads.

2. Categorize and Plan
List the comments and review threads.
Propose a fix for each.
Wait for user confirmation on which comments to address first if there are many.
3. Apply Fixes

Apply the code changes for the selected comments.

4. Respond to Comments

Once fixed, respond to the threads as resolved.

gh pr comment <PR_NUMBER> --body "Addressed in latest commit."

Common Mistakes
Applying fixes without understanding context: Always read the surrounding code of a comment.
Not verifying auth: Check gh auth status before starting.
When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
490
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn