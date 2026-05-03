---
title: git-commit
url: https://skills.sh/dhruvanbhalara/skills/git-commit
---

# git-commit

skills/dhruvanbhalara/skills/git-commit
git-commit
Installation
$ npx skills add https://github.com/dhruvanbhalara/skills --skill git-commit
SKILL.md
Automated Git Commits

This skill provides instructions for performing atomic, well-structured Git commits following the Conventional Commits specification.

1. Analyze Changes
Identify Modified Files: Run git status --short to see all staged and unstaged changes.
Respect Ignore Rules: Do NOT include files that the user has explicitly requested to ignore or that match .gitignore patterns.
Group by Scope: Group modified files by their logical "scope" (e.g., a specific module, feature, or layer like data, domain, ui).
2. Branching
Feature Branches: ALWAYS create descriptive feature branches from main (e.g., feat/login-logic).
Merge Flow: Merge back into main only after passing all quality checks and PR approval.
3. Generate Commit Message
Conventional Commits: Each commit MUST follow the pattern: <type>(<scope>): <message>.
Types: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert.
Scope: The module or area being changed (e.g., auth, api).
Message: A concise description in imperative mood.
Sub-messages (Commit Body):
ALWAYS include a detailed body if the change involves logic, breaking changes, or multiple steps.
Explain the "What", "Why", and "How" of the change.
Use blank lines to separate the subject from the body.
3. Atomic Commits
One Scope per Commit: Perform separate commits for different scopes.
Stage Selectively: Stage only the files belonging to the current scope.
4. Execution Flow
Step 1: Group files by scope.
Step 2: For each group:
Stage the files.
Generate the conventional commit message (subject + body).
Execute:
git commit -m "<subject>" -m "<body>"

Step 3: Verify history (git log -n 5).
Weekly Installs
65
Repository
dhruvanbhalara/skills
GitHub Stars
17
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass