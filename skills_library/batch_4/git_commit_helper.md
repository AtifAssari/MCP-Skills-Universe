---
title: git commit helper
url: https://skills.sh/davila7/claude-code-templates/git-commit-helper
---

# git commit helper

skills/davila7/claude-code-templates/Git Commit Helper
Git Commit Helper
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill 'Git Commit Helper'
SKILL.md
Contains Hooks

This skill uses Claude hooks which can execute code automatically in response to events. Review carefully before installing.

Git Commit Helper
Quick start

Analyze staged changes and generate commit message:

# View staged changes
git diff --staged

# Generate commit message based on changes
# (Claude will analyze the diff and suggest a message)

Commit message format

Follow conventional commits format:

<type>(<scope>): <description>

[optional body]

[optional footer]

Types
feat: New feature
fix: Bug fix
docs: Documentation changes
style: Code style changes (formatting, missing semicolons)
refactor: Code refactoring
test: Adding or updating tests
chore: Maintenance tasks
Examples

Feature commit:

feat(auth): add JWT authentication

Implement JWT-based authentication system with:
- Login endpoint with token generation
- Token validation middleware
- Refresh token support


Bug fix:

fix(api): handle null values in user profile

Prevent crashes when user profile fields are null.
Add null checks before accessing nested properties.


Refactor:

refactor(database): simplify query builder

Extract common query patterns into reusable functions.
Reduce code duplication in database layer.

Analyzing changes

Review what's being committed:

# Show files changed
git status

# Show detailed changes
git diff --staged

# Show statistics
git diff --staged --stat

# Show changes for specific file
git diff --staged path/to/file

Commit message guidelines

DO:

Use imperative mood ("add feature" not "added feature")
Keep first line under 50 characters
Capitalize first letter
No period at end of summary
Explain WHY not just WHAT in body

DON'T:

Use vague messages like "update" or "fix stuff"
Include technical implementation details in summary
Write paragraphs in summary line
Use past tense
Multi-file commits

When committing multiple related changes:

refactor(core): restructure authentication module

- Move auth logic from controllers to service layer
- Extract validation into separate validators
- Update tests to use new structure
- Add integration tests for auth flow

Breaking change: Auth service now requires config object

Scope examples

Frontend:

feat(ui): add loading spinner to dashboard
fix(form): validate email format

Backend:

feat(api): add user profile endpoint
fix(db): resolve connection pool leak

Infrastructure:

chore(ci): update Node version to 20
feat(docker): add multi-stage build
Breaking changes

Indicate breaking changes clearly:

feat(api)!: restructure API response format

BREAKING CHANGE: All API responses now follow JSON:API spec

Previous format:
{ "data": {...}, "status": "ok" }

New format:
{ "data": {...}, "meta": {...} }

Migration guide: Update client code to handle new response structure

Template workflow
Review changes: git diff --staged
Identify type: Is it feat, fix, refactor, etc.?
Determine scope: What part of the codebase?
Write summary: Brief, imperative description
Add body: Explain why and what impact
Note breaking changes: If applicable
Interactive commit helper

Use git add -p for selective staging:

# Stage changes interactively
git add -p

# Review what's staged
git diff --staged

# Commit with message
git commit -m "type(scope): description"

Amending commits

Fix the last commit message:

# Amend commit message only
git commit --amend

# Amend and add more changes
git add forgotten-file.js
git commit --amend --no-edit

Best practices
Atomic commits - One logical change per commit
Test before commit - Ensure code works
Reference issues - Include issue numbers if applicable
Keep it focused - Don't mix unrelated changes
Write for humans - Future you will read this
Commit message checklist
 Type is appropriate (feat/fix/docs/etc.)
 Scope is specific and clear
 Summary is under 50 characters
 Summary uses imperative mood
 Body explains WHY not just WHAT
 Breaking changes are clearly marked
 Related issue numbers are included
Weekly Installs
–
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass