---
title: commit
url: https://skills.sh/parcadei/continuous-claude-v3/commit
---

# commit

skills/parcadei/continuous-claude-v3/commit
commit
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill commit
SKILL.md
Commit Changes

You are tasked with creating git commits for the changes made during this session.

Process:

Think about what changed:

Review the conversation history and understand what was accomplished
Run git status to see current changes
Run git diff to understand the modifications
Consider whether changes should be one commit or multiple logical commits

Plan your commit(s):

Identify which files belong together
Draft clear, descriptive commit messages
Use imperative mood in commit messages
Focus on why the changes were made, not just what

Present your plan to the user:

List the files you plan to add for each commit
Show the commit message(s) you'll use
Ask: "I plan to create [N] commit(s) with these changes. Shall I proceed?"

Execute upon confirmation:

Use git add with specific files (never use -A or .)
Create commits with your planned messages
Show the result with git log --oneline -n [number]

Generate reasoning (after each commit):

Run: bash "$CLAUDE_PROJECT_DIR/.claude/scripts/generate-reasoning.sh" <commit-hash> "<commit-message>"
This captures what was tried during development (build failures, fixes)
The reasoning file helps future sessions understand past decisions
Stored in .git/claude/commits/<hash>/reasoning.md
Important:
NEVER add co-author information or Claude attribution
Commits should be authored solely by the user
Do not include any "Generated with Claude" messages
Do not add "Co-Authored-By" lines
Write commit messages as if the user wrote them
Remember:
You have the full context of what was done in this session
Group related changes together
Keep commits focused and atomic when possible
The user trusts your judgment - they asked you to commit
Weekly Installs
305
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass