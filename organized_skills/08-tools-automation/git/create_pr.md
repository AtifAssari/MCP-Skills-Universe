---
rating: ⭐⭐⭐
title: create-pr
url: https://skills.sh/n8n-io/n8n/create-pr
---

# create-pr

skills/n8n-io/n8n/create-pr
create-pr
Installation
$ npx skills add https://github.com/n8n-io/n8n --skill create-pr
Summary

GitHub pull requests with titles validated against n8n's commit convention standards.

Enforces conventional commit format with type, optional scope, and summary; supports nine commit types (feat, fix, perf, test, docs, refactor, build, ci, chore) with configurable changelog inclusion
Provides predefined scopes for common areas (API, core, editor, benchmark, specific nodes) and validates title format including breaking change indicators and capitalization rules
Includes PR body template with sections for summary, related tickets, and pre-merge checklist; automatically links Linear tickets and GitHub issues with close keywords
Analyzes local git state and pushes branches before creating draft PRs via gh CLI
SKILL.md
Create Pull Request

Creates GitHub PRs with titles that pass n8n's check-pr-title CI validation.

PR Title Format
<type>(<scope>): <summary>

Types (required)
Type	Description	Changelog
feat	New feature	Yes
fix	Bug fix	Yes
perf	Performance improvement	Yes
test	Adding/correcting tests	No
docs	Documentation only	No
refactor	Code change (no bug fix or feature)	No
build	Build system or dependencies	No
ci	CI configuration	No
chore	Routine tasks, maintenance	No
Scopes (optional but recommended)
API - Public API changes
benchmark - Benchmark CLI changes
core - Core/backend/private API
editor - Editor UI changes
* Node - Specific node (e.g., Slack Node, GitHub Node)
Summary Rules
Use imperative present tense: "Add" not "Added"
Capitalize first letter
No period at the end
No ticket IDs (e.g., N8N-1234)
Add (no-changelog) suffix to exclude from changelog
Steps

Check current state:

git status
git diff --stat
git log origin/master..HEAD --oneline


Check for implementation plan: Look for a plan file in .claude/plans/ that matches the current branch's ticket ID (e.g. if branch is scdekov/PAY-1234-some-feature, check for .claude/plans/PAY-1234.md). If a plan file exists, ask the user whether they want to include it in the PR description as a collapsible <details> section (see Plan Section below). Only include the plan if the user explicitly approves.

If this is a security fix, audit every public-facing artifact before proceeding (see Security Fixes below).

Analyze changes to determine:

Type: What kind of change is this?
Scope: Which package/area is affected?
Summary: What does the change do?

Push branch if needed:

git push -u origin HEAD


Create PR using gh CLI with the template from .github/pull_request_template.md:

gh pr create --draft --title "<type>(<scope>): <summary>" --body "$(cat <<'EOF'
## Summary

<Describe what the PR does and how to test. Photos and videos are recommended.>

## Related Linear tickets, Github issues, and Community forum posts

<!-- Link to Linear ticket: https://linear.app/n8n/issue/[TICKET-ID] -->
<!-- Use "closes #<issue-number>", "fixes #<issue-number>", or "resolves #<issue-number>" to automatically close issues -->

## Review / Merge checklist

- [ ] PR title and summary are descriptive. ([conventions](../blob/master/.github/pull_request_title_conventions.md))
- [ ] [Docs updated](https://github.com/n8n-io/n8n-docs) or follow-up ticket created.
- [ ] Tests included.
- [ ] PR Labeled with `release/backport` (if the PR is an urgent fix that needs to be backported)
EOF
)"

PR Body Guidelines

Based on .github/pull_request_template.md:

Summary Section
Describe what the PR does
Explain how to test the changes
Include screenshots/videos for UI changes
Related Links Section
Link to Linear ticket: https://linear.app/n8n/issue/[TICKET-ID]
Link to GitHub issues using keywords to auto-close:
closes #123 / fixes #123 / resolves #123
Link to Community forum posts if applicable
Checklist

All items should be addressed before merging:

PR title follows conventions
Docs updated or follow-up ticket created
Tests included (bugs need regression tests, features need coverage)
release/backport label added if urgent fix needs backporting
Examples
Feature in editor
feat(editor): Add workflow performance metrics display

Bug fix in core
fix(core): Resolve memory leak in execution engine

Node-specific change
fix(Slack Node): Handle rate limiting in message send

Breaking change (add exclamation mark before colon)
feat(API)!: Remove deprecated v1 endpoints

No changelog entry
refactor(core): Simplify error handling (no-changelog)

No scope (affects multiple areas)
chore: Update dependencies to latest versions

Validation

The PR title must match this pattern:

^(feat|fix|perf|test|docs|refactor|build|ci|chore|revert)(\([a-zA-Z0-9 ]+( Node)?\))?!?: [A-Z].+[^.]$


Key validation rules:

Type must be one of the allowed types
Scope is optional but must be in parentheses if present
Exclamation mark for breaking changes goes before the colon
Summary must start with capital letter
Summary must not end with a period
Plan Section

If a matching plan file was found in .claude/plans/ and the user has approved including it, add a collapsible section at the end of the PR body (after the checklist, before EOF):

<details>
<summary>Implementation plan</summary>

<!-- paste plan file contents here -->

</details>

Security Fixes

This repo is public. Never expose the attack vector in any public artifact. Describe what the code does, not what threat it prevents.

Artifact	BAD	GOOD
Branch	fix-sql-injection-in-webhook	fix-webhook-input-validation
PR title	fix(core): Prevent SSRF	fix(core): Validate outgoing URLs
Commit msg	fix: prevent denial of service	fix: add payload size validation
PR body	"attacker could trigger SSRF…"	"validates URL protocol and host"
Linear ref	URL with slug (leaks title)	URL without slug or ticket ID only
Test name	'should prevent SQL injection'	'should sanitize query parameters'

Before pushing a security fix, verify: no branch name, commit, PR title, PR body, Linear URL, test name, or code comment hints at the vulnerability.

Weekly Installs
850
Repository
n8n-io/n8n
GitHub Stars
186.4K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass