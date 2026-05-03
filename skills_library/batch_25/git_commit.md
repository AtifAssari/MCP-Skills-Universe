---
title: git-commit
url: https://skills.sh/dauquangthanh/hanoi-rainbow/git-commit
---

# git-commit

skills/dauquangthanh/hanoi-rainbow/git-commit
git-commit
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill git-commit
SKILL.md
Git Commit

Generates well-structured git commit messages following conventional commit standards and best practices.

Key Principles
Be specific: Describe exactly what changed
Be consistent: Follow conventional commit format
Be atomic: One logical change per commit
Be clear: Write for others (including future you)
Be complete: Include why and context when needed
Be conventional: Follow standard format for automation
Standard Format
<type>(<scope>): <subject>

<body>

<footer>


Components:

type: Category of change (required) - feat, fix, docs, refactor, perf, test, build, ci, chore, style, revert
scope: Area affected (optional) - auth, api, ui, db, etc.
subject: Brief description (required, ≤50 chars)
body: Detailed explanation (optional, wrap at 72 chars)
footer: Breaking changes, issue refs (optional)
Basic Workflow

Choose the commit type:

feat: New user-facing functionality
fix: Bug fix for users
docs: Documentation only
refactor: Code restructuring without behavior change
perf: Performance improvement
test: Adding/updating tests
build: Dependency/build system changes
ci: CI/CD configuration changes
chore: Maintenance tasks
style: Code formatting
revert: Reverting previous commit

Write subject line (imperative mood, ≤50 chars):

✅ feat(auth): add OAuth2 authentication
✅ fix(api): resolve race condition in user updates
❌ feat: added some stuff
❌ fix: bug fix


Add body if needed (explain why, not just what):

Required for breaking changes
Recommended for complex changes
Wrap lines at 72 characters

Include footer:

Breaking changes: BREAKING CHANGE: description
Issue references: Closes #123, Fixes #456
Quick Examples

Simple feature:

feat(auth): add password reset endpoint


Bug fix with context:

fix(api): prevent null pointer in user preferences

User preferences API crashed when optional fields were null.
Added null checks and default values.

Closes #456


Breaking change:

feat(api)!: change response format to JSON:API spec

BREAKING CHANGE: API responses now follow JSON:API format.
Update client code to parse data from `data` key instead
of root level.

Closes #789

Reference Documentation

For detailed guidance, load these reference files as needed:

commit-types.md: Complete list of commit types with examples
quick-reference.md: Decision trees and checklists
best-practices.md: Atomic commits, meaningful messages, issue references
writing-guidelines.md: Subject line rules, scope selection, body formatting
common-scenarios.md: Examples for typical development situations
common-mistakes-to-avoid.md: Anti-patterns and how to fix them
team-conventions.md: Customizing conventions for teams
commit-message-structure.md: Detailed format specifications
commit-message-templates.md: Ready-to-use templates
commit-workflow.md: Integration with git workflows
examples-by-project-type.md: Examples for web apps, libraries, mobile, microservices
advanced-patterns.md: Complex scenarios and edge cases
commit-message-convention.md: Enforcement tools and configurations
Weekly Installs
15
Repository
dauquangthanh/h…-rainbow
GitHub Stars
10
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass