---
title: conventional-commit
url: https://skills.sh/marcelorodrigo/agent-skills/conventional-commit
---

# conventional-commit

skills/marcelorodrigo/agent-skills/conventional-commit
conventional-commit
Installation
$ npx skills add https://github.com/marcelorodrigo/agent-skills --skill conventional-commit
Summary

Structured commit message format following the Conventional Commits specification.

Defines 12 commit types (feat, fix, refactor, docs, test, chore, ci, build, perf, style, deps, revert) with clear purposes and semantic versioning correlation
Enforces a required header format with optional scope and body, all lines under 100 characters, subject line capped at 70 characters
Includes guidelines for imperative present-tense language, body content explaining what and why, and support for BREAKING CHANGE footers to signal major version bumps
Provides branch naming conventions matching commit types and examples covering simple fixes, features with scope, refactors, breaking changes, and reverts
SKILL.md
Conventional Commit Messages

Follow these conventions when creating commits.

Prerequisites

Before committing, ensure you're working on a feature branch, not the main branch.

# Check current branch
git branch --show-current


If you're on main or master, create a new branch first:

# Create and switch to a new branch
git checkout -b <type>/<short-description>


Branch naming should follow the pattern: <type>/<short-description> where type matches the commit type (e.g., feat/add-user-auth, fix/null-pointer-error, refactor/extract-validation).

Format
<type>(<scope>): <subject>

<body>

<footer>


The header is required. Scope is optional. All lines must stay under 100 characters.

Commit Types
Type	Purpose
build	Build system or CI changes
chore	Routine maintenance tasks
ci	Continuous integration configuration
deps	Dependency updates
docs	Documentation changes
feat	New feature
fix	Bug fix
perf	Performance improvement
refactor	Code refactoring (no behavior change)
revert	Revert a previous commit
style	Code style and formatting
test	Tests added, updated or improved
Subject Line Rules
Use imperative, present tense: "Add feature" not "Added feature"
Capitalize the first letter
No period at the end
Maximum 70 characters
Body Guidelines
Explain what and why, not how
Use imperative mood and present tense
Include motivation for the change
Contrast with previous behavior when relevant
Conventional Commits

The commit contains the following structural elements, to communicate intent to the consumers of your library:

fix: a commit of the type fix patches a bug in your codebase (this correlates with PATCH in Semantic Versioning).
feat: a commit of the type feat introduces a new feature to the codebase (this correlates with MINOR in Semantic Versioning).
BREAKING CHANGE: a commit that has a footer BREAKING CHANGE:, or appends a ! after the type/scope, introduces a breaking API change (correlating with MAJOR in Semantic Versioning). A BREAKING CHANGE can be part of commits of any type.
types other than fix: and feat: are allowed, for example @commitlint/config-conventional (based on the Angular convention) recommends build:, chore:, ci:, docs:, style:, refactor:, perf:, test:, and others.
footers other than BREAKING CHANGE: may be provided and follow a convention similar to git trailer format.
Examples
Simple fix
fix(api): Handle null response in user endpoint

The user API could return null for deleted accounts, causing a crash
in the dashboard. Add null check before accessing user properties.

Feature with scope
feat(alerts): Add Slack thread replies for alert updates

When an alert is updated or resolved, post a reply to the original
Slack thread instead of creating a new message. This keeps related
notifications grouped together.

Refactor
refactor: Extract common validation logic to shared module

Move duplicate validation code from three endpoints into a shared
validator class. No behavior change.

Breaking change
feat(api)!: Remove deprecated v1 endpoints

Remove all v1 API endpoints that were deprecated in version 23.1.
Clients should migrate to v2 endpoints.

BREAKING CHANGE: v1 endpoints no longer available

Revert Format
revert: feat(api): Add new endpoint

This reverts commit abc123def456.

Reason: Caused performance regression in production.

Principles
Each commit should be a single, stable change
Commits should be independently reviewable
The repository should be in a working state after each commit
References
Conventional Commits Specification
Weekly Installs
716
Repository
marcelorodrigo/…t-skills
GitHub Stars
8
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass