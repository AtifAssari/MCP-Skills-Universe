---
title: commit-helper
url: https://skills.sh/nodnarbnitram/claude-code-extensions/commit-helper
---

# commit-helper

skills/nodnarbnitram/claude-code-extensions/commit-helper
commit-helper
Installation
$ npx skills add https://github.com/nodnarbnitram/claude-code-extensions --skill commit-helper
SKILL.md
Commit Helper

Generate well-structured commit messages following conventional commit format.

Instructions
Run git diff --staged to see staged changes
Analyze the changes to understand:
What files were modified
What type of change (feat, fix, refactor, docs, etc.)
The scope/component affected
Generate a commit message with:
Summary line under 50 characters
Type prefix (feat, fix, docs, refactor, test, chore)
Optional scope in parentheses
Detailed body explaining what and why
Commit Types
feat: New feature
fix: Bug fix
docs: Documentation changes
refactor: Code restructuring without behavior change
test: Adding or updating tests
chore: Maintenance tasks
Best Practices
Use present tense ("Add feature" not "Added feature")
Explain what and why, not how
Keep summary concise but descriptive
Reference issue numbers when applicable
Example Output
feat(auth): add OAuth2 support for GitHub login

- Implement OAuth2 flow with PKCE
- Add token refresh mechanism
- Store tokens securely in encrypted storage

Closes #123

Weekly Installs
53
Repository
nodnarbnitram/c…tensions
GitHub Stars
8
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass