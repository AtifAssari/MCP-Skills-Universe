---
rating: ⭐⭐
title: git-pushing
url: https://skills.sh/davila7/claude-code-templates/git-pushing
---

# git-pushing

skills/davila7/claude-code-templates/git-pushing
git-pushing
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill git-pushing
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

Weekly Installs
289
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass