---
rating: ⭐⭐
title: code-review-playbook
url: https://skills.sh/yonatangross/orchestkit/code-review-playbook
---

# code-review-playbook

skills/yonatangross/orchestkit/code-review-playbook
code-review-playbook
Installation
$ npx skills add https://github.com/yonatangross/orchestkit --skill code-review-playbook
SKILL.md
Contains Hooks

This skill uses Claude hooks which can execute code automatically in response to events. Review carefully before installing.

Code Review Playbook

This skill provides a comprehensive framework for effective code reviews that improve code quality, share knowledge, and foster collaboration. Whether you're a reviewer giving feedback or an author preparing code for review, this playbook ensures reviews are thorough, consistent, and constructive.

Overview
Reviewing pull requests or merge requests
Preparing code for review (self-review)
Establishing code review standards for teams
Training new developers on review best practices
Resolving disagreements about code quality
Improving review processes and efficiency
Code Review Philosophy
Purpose of Code Reviews

Code reviews serve multiple purposes:

Quality Assurance: Catch bugs, logic errors, and edge cases
Knowledge Sharing: Spread domain knowledge across the team
Consistency: Ensure codebase follows conventions and patterns
Mentorship: Help developers improve their skills
Collective Ownership: Build shared responsibility for code
Documentation: Create discussion history for future reference
Principles

Be Kind and Respectful:

Review the code, not the person
Assume positive intent
Praise good solutions
Frame feedback constructively

Be Specific and Actionable:

Point to specific lines of code
Explain why something should change
Suggest concrete improvements
Provide examples when helpful

Balance Speed with Thoroughness:

Aim for timely feedback (< 24 hours)
Don't rush critical reviews
Use automation for routine checks
Focus human review on logic and design

Distinguish Must-Fix from Nice-to-Have:

Use conventional comments to indicate severity
Block merges only for critical issues
Allow authors to defer minor improvements
Capture deferred work in follow-up tickets
Conventional Comments
issue [blocking]: Missing error handling for API call
If the API returns a 500 error, this will crash. Add try/catch.

security [blocking]: API endpoint is not authenticated
The /api/admin/users endpoint is missing auth middleware.


Load Read("${CLAUDE_SKILL_DIR}/references/conventional-comments.md") for the full format, labels (praise, nitpick, suggestion, issue, question, security, bug, breaking), decorations ([blocking], [non-blocking], [if-minor]), and examples.

Review Process
1. Before Reviewing

Check Context:

Read the PR/MR description
Understand the purpose and scope
Review linked tickets or issues
Check CI/CD pipeline status

Verify Automated Checks:

 Tests are passing
 Linting has no errors
 Type checking passes
 Code coverage meets targets
 No merge conflicts

Set Aside Time:

Small PR (< 200 lines): 15-30 minutes
Medium PR (200-500 lines): 30-60 minutes
Large PR (> 500 lines): 1-2 hours (or ask to split)
2. During Review

Follow a Pattern:

High-Level Review (5-10 minutes)

Read PR description and understand intent
Skim all changed files to get overview
Verify approach makes sense architecturally
Check that changes align with stated purpose

Detailed Review (20-45 minutes)

Line-by-line code review
Check logic, edge cases, error handling
Verify tests cover new code
Look for security vulnerabilities
Ensure code follows team conventions

Testing Considerations (5-10 minutes)

Are tests comprehensive?
Do tests test the right things?
Are edge cases covered?
Is test data realistic?

Documentation Check (5 minutes)

Are complex sections commented?
Is public API documented?
Are breaking changes noted?
Is README updated if needed?
3. After Reviewing

Provide Clear Decision:

✅ Approve: Code is ready to merge
💬 Comment: Feedback provided, no action required
🔄 Request Changes: Issues must be addressed before merge

Respond to Author:

Answer questions promptly
Re-review after changes made
Approve when issues resolved
Thank author for addressing feedback
Review Checklists
General Code Quality
 Readability: Code is easy to understand
 Naming: Variables and functions have clear, descriptive names
 Comments: Complex logic is explained
 Formatting: Code follows team style guide
 DRY: No unnecessary duplication
 SOLID Principles: Code follows SOLID where applicable
 Function Size: Functions are focused and < 50 lines
 Cyclomatic Complexity: Functions have complexity < 10
Security
 Authentication: Protected endpoints require auth
 Authorization: Users can only access their own data
 Input Sanitization: SQL injection, XSS prevented
 Secrets Management: No hardcoded credentials or API keys
 Encryption: Sensitive data encrypted at rest and in transit
 Rate Limiting: Endpoints protected from abuse
Quick Start Guide

For Reviewers:

Read PR description and understand intent
Check that automated checks pass
Do high-level review (architecture, approach)
Do detailed review (logic, edge cases, tests)
Use conventional comments for clear communication
Provide decision: Approve, Comment, or Request Changes

For Authors:

Write clear PR description
Perform self-review before requesting review
Ensure all automated checks pass
Keep PR focused and reasonably sized (< 400 lines)
Respond to feedback promptly and respectfully
Make requested changes or explain reasoning

Skill Version: 2.0.0 Last Updated: 2026-01-08 Maintained by: AI Agent Hub Team

Related Skills
ork:architecture-patterns - Enforce testing and architectural best practices during code review
security-scanning - Automated security checks to complement manual review
ork:testing-unit - Unit testing patterns to verify during review
Rules

Each category has individual rule files in rules/ loaded on-demand:

Category	Rule	Impact	Key Pattern
TypeScript Quality	rules/typescript-quality.md	HIGH	No any, Zod validation, exhaustive switches, React 19
Python Quality	rules/python-quality.md	HIGH	Pydantic v2, ruff, mypy strict, async timeouts
Security Baseline	rules/security-baseline.md	CRITICAL	No secrets, auth on endpoints, input validation
Linting	rules/linting-biome-setup.md	HIGH	Biome setup, ESLint migration, gradual adoption
Linting	rules/linting-biome-rules.md	HIGH	Biome config, type-aware rules, CI integration

Total: 5 rules across 4 categories

Available Scripts

scripts/review-pr.md - Dynamic PR review with auto-fetched GitHub data

Auto-fetches: PR title, author, state, changed files, diff stats, comments count
Usage: /ork:review-pr [PR-number]
Requires: GitHub CLI (gh)
Uses $ARGUMENTS and !command for live PR data

assets/review-feedback-template.md - Static review feedback template

assets/pr-template.md - PR description template

Weekly Installs
159
Repository
yonatangross/orchestkit
GitHub Stars
163
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn