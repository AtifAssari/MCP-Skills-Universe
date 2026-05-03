---
title: git-pushing
url: https://skills.sh/sickn33/antigravity-awesome-skills/git-pushing
---

# git-pushing

skills/sickn33/antigravity-awesome-skills/git-pushing
git-pushing
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill git-pushing
Summary

Stage, commit, and push git changes with conventional commit messages.

Automatically stages all changes, generates conventional commits, and pushes to the remote branch using a provided bash script
Supports custom commit messages or auto-generates them based on changes
Includes Claude footer in commits and uses the -u flag to set upstream tracking on first push
Activates when users request commits, mention pushing to remote, or ask to save work
SKILL.md
Git Push Workflow

Stage all changes, create a conventional commit, and push to the remote branch.

When to Use

Automatically activate when the user:

Explicitly asks to push changes ("push this", "commit and push")
Mentions saving work to remote ("save to github", "push to remote")
Completes a feature and wants to share it
Says phrases like "let's push this up" or "commit these changes"
Workflow

ALWAYS use the script - do NOT use manual git commands:

bash skills/git-pushing/scripts/smart_commit.sh


With custom message:

bash skills/git-pushing/scripts/smart_commit.sh "feat: add feature"


Script handles: staging, conventional commit message, Claude footer, push with -u flag.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
574
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykPass