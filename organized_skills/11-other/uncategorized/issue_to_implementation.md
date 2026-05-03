---
rating: ⭐⭐⭐
title: issue-to-implementation
url: https://skills.sh/illusion47586/isol8/issue-to-implementation
---

# issue-to-implementation

skills/illusion47586/isol8/issue-to-implementation
issue-to-implementation
Installation
$ npx skills add https://github.com/illusion47586/isol8 --skill issue-to-implementation
SKILL.md
Issue to Implementation Skill

Transform GitHub issues into implemented code changes with comprehensive planning, validation, and PR creation.

Overview

This skill provides a complete workflow to go from a GitHub issue URL to a merged-ready pull request:

Fetch and analyze issue details and comments
Create or validate implementation plans
Validate bugs if applicable
Implement the solution with proper commits
Create a well-labeled PR following project templates
Prerequisites
gh CLI installed and authenticated (gh auth status)
Git repository with remote configured
Write access to the repository
Workflow
Phase 0: Repository Setup

Before starting any work:

Checkout to main branch and pull latest changes:

git checkout main
git pull origin main


Check for unstaged changes:

git status


If there are unstaged changes, ask the user what to do with them before proceeding.

Phase 1: Fetch and Analyze

Fetch the issue details and all comments:

# Extract owner/repo from URL
# URL format: https://github.com/owner/repo/issues/NUMBER
OWNER_REPO=$(echo "$ISSUE_URL" | sed -E 's|https://github.com/([^/]+/[^/]+)/issues/.*|\1|')
ISSUE_NUMBER=$(echo "$ISSUE_URL" | sed -E 's|.*/issues/([0-9]+).*|\1|')

# Fetch issue details
gh issue view "$ISSUE_NUMBER" --repo "$OWNER_REPO" --json number,title,body,state,labels,author,createdAt,updatedAt,closed

# Fetch all comments
gh issue view "$ISSUE_NUMBER" --repo "$OWNER_REPO" --comments


Analyze the issue:

Type: Bug fix, feature request, enhancement, documentation
Priority: Based on labels (critical, high, medium, low)
Status: Open/closed, stale comments (check dates)
Scope: Which components are affected
Phase 2: Create Implementation Plan

Create a comprehensive plan document:

# Implementation Plan: [Issue Title]

## Issue Summary
- **Issue**: #NUMBER
- **Type**: Bug/Feature/Enhancement
- **Priority**: [Priority level]

## Problem/Requirements
[Clear description of what needs to be done]

## Analysis
[Findings from code analysis, validation steps if bug]

## Proposed Solution
[Detailed description of the fix/feature]

## File Changes
| File | Change Type | Description |
|------|-------------|-------------|
| path/to/file.ts | Modify | [What changes] |
| path/to/new.ts | Create | [Purpose] |

## Architecture Changes
[Any structural changes, new patterns, interfaces, etc.]

## Testing Plan
- [ ] Unit tests: [what to test]
- [ ] Integration tests: [if needed]
- [ ] Manual testing: [steps]

## Documentation Updates
- [ ] README.md: [what to update]
- [ ] docs/[relevant-file].mdx: [what to update]
- [ ] skill/isol8/SKILL.md: [if applicable]
- [ ] CHANGELOG.md: DO NOT UPDATE - managed via CI only

**Note**: If a testing plan does not exist, it MUST be created for changes related to code. Documentation updates are also required for code changes.

## Dependencies
[Any new packages or external dependencies]

## Risks & Considerations
[Any breaking changes, migration notes, edge cases]

Phase 3: Validate (for Bugs)

If the issue is a bug:

Reproduce the bug first before implementing the fix
Document reproduction steps
Verify the bug exists in the current codebase
After implementing fix, verify the bug is resolved
# Check if bug reproduction exists in tests or issues
gh issue view "$ISSUE_NUMBER" --repo "$OWNER_REPO" --comments | grep -i "repro\|steps\|example"

Phase 4: Check for Stale Plans

If existing comments mention implementation plans:

Compare the plan date with the latest code changes
Check if the codebase structure has changed
Validate that the proposed approach is still valid
If stale, prepare an updated plan comment
Phase 5: Implement

Create a feature branch:

git checkout -b fix/issue-NUMBER-short-description
# or
git checkout -b feat/issue-NUMBER-short-description


Make changes incrementally with clear commits:

git add <files>
git commit -m "type(scope): description

Fixes #NUMBER"


Follow conventional commits:

fix(component): Bug fixes
feat(component): New features
docs(component): Documentation
refactor(component): Code restructuring
test(component): Test additions/changes
chore(component): Maintenance tasks
Phase 6: Testing

Before finalizing:

# Run tests
bun test

# Run linting
bun run lint

# Type checking
bunx tsc --noEmit


Ensure all tests pass and code quality checks succeed.

Phase 7: Create Pull Request

Fetch available labels:

gh label list --repo "$OWNER_REPO" --limit 50


Push branch:

git push -u origin HEAD


Create PR using template:

# Read the PR template
cat .github/pull_request_template.md

# Create PR with proper description
gh pr create \
  --repo "$OWNER_REPO" \
  --title "type(scope): Description" \
  --body-file pr_description.md \
  --label "label1,label2"


PR Description structure (following .github/pull_request_template.md):

## Description

[Summary of changes and motivation]

Fixes #[issue_number]

## Type of Change

- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📝 Documentation update
- [ ] ♻️ Refactor (code improvement without functional change)

## Scope

- [ ] CLI
- [ ] Server
- [ ] Docker Engine
- [ ] Library (SDK)
- [ ] Documentation

## Human Verification Checklist

- [ ] I have **manually reviewed** every line of code in this PR.
- [ ] I have **tested** these changes locally and confirmed they work as expected.
- [ ] This code is NOT entirely generated by AI; I understand and vouch for its correctness.

## Quality Checklist

- [ ] My code follows the style guidelines of this project (run `bun run lint`).
- [ ] I have performed a self-review of my own code.
- [ ] I have commented my code, particularly in hard-to-understand areas.
- [ ] I have made corresponding changes to the documentation.
- [ ] My changes generate no new warnings.
- [ ] I have added tests that prove my fix is effective or that my feature works.
- [ ] New and existing unit tests pass locally with my changes.

## Implementation Notes

[Any additional context, technical details, or migration notes]

Reference Files
.github/pull_request_template.md: PR template to follow
README.md: High-level project documentation
docs/: Detailed documentation directory
skill/isol8/SKILL.md: Agent skill documentation
Helper Scripts

This skill includes helper scripts in scripts/:

fetch_issue.sh <issue_url>: Fetches issue details and comments, saves to .issue-data/
validate_bug.sh <issue_number>: Helps validate bugs before fixing
list_labels.sh [filter]: Lists available PR labels
create_pr.sh <issue_number> <type> [labels]: Creates PR from current branch
Quick Commands
# Fetch issue
gh issue view 123 --repo owner/repo --json number,title,body,labels,state

# Fetch comments
gh issue view 123 --repo owner/repo --comments

# List labels
gh label list --repo owner/repo

# Create PR
gh pr create --repo owner/repo --title "..." --body "..." --label "bug,cli"

Important Notes
CHANGELOG.md

DO NOT UPDATE - The CHANGELOG.md file is managed automatically via CI/CD pipeline. Never manually add entries to it.

Required for Code Changes

When making changes to code:

Testing Plan - If no testing plan exists, you MUST create one
Documentation Updates - Documentation must be updated to reflect the changes
Production Tests - Add production tests wherever required (especially for CLI, Docker engine, and integration scenarios)

These are not optional - they are required parts of the implementation.

Success Criteria

Before marking complete:

 Checked out to main and pulled latest changes
 No unstaged changes (or user has been consulted)
 Issue fully understood and analyzed
 Implementation plan documented (including testing plan if it didn't exist)
 Bug validated (if applicable)
 Code changes implemented
 Tests added/updated and passing
 Documentation updated (README.md, docs/, etc.)
 CHANGELOG.md NOT modified (CI-managed)
 PR created with proper labels and description
 Lint and type checks passing
Weekly Installs
12
Repository
illusion47586/isol8
GitHub Stars
4
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn