---
title: commit-message
url: https://skills.sh/ycs77/skills/commit-message
---

# commit-message

skills/ycs77/skills/commit-message
commit-message
Installation
$ npx skills add https://github.com/ycs77/skills --skill commit-message
SKILL.md
Git Commit Message Generator

Generate concise, descriptive Git commit messages in English.

Process
Run git diff --cached directly (NOT git -C <path> diff --cached, NOT cd <path> && git diff --cached) to check for staged changes
If staged changes exist: generate commit message based on staged changes only
If no staged changes: run git diff directly (NOT git -C <path> diff, NOT cd <path> && git diff) and git status directly (NOT git -C <path> status, NOT cd <path> && git status) to view unstaged and untracked files
For untracked files, intelligently assess which need content review (code/config files) vs which can be inferred from filename (assets, dependencies)
Generate a single-line commit message
Output

Output ONLY the commit message — a single line, no explanation, no follow-up questions, no code block fencing.

Format
Imperative mood, under 72 characters
Focus on the 'what' and 'why' of the change, not the 'how'. Avoid generic messages like 'update code' or 'fix bug'.
No type prefix (e.g., feat:, fix:) unless the user explicitly requests Conventional Commits format
Examples
Add user authentication with JWT tokens
Update navbar to include search functionality
Remove deprecated API endpoints
Rename userService to UserAccountService
Fix null pointer exception in user service
Improve error handling in payment module
Optimize database queries for faster loading
Refactor user service to use repository pattern
Document API endpoints in README
Add edge case tests for payment processing
Bump dependencies
Add login page with validation and error handling
Migrate CI pipeline from Travis to GitHub Actions
Fix authentication bug and update related tests

Weekly Installs
21
Repository
ycs77/skills
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass