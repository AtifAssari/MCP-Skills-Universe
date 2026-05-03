---
rating: ⭐⭐
title: code-quality-workflow
url: https://skills.sh/nickcrew/claude-ctx-plugin/code-quality-workflow
---

# code-quality-workflow

skills/nickcrew/claude-ctx-plugin/code-quality-workflow
code-quality-workflow
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill code-quality-workflow
SKILL.md
Code Quality Workflow
Overview

Standardize how to analyze, review, and improve code quality. This skill centralizes quality assessment, code review practices, and systematic improvements with validation gates.

When to Use
Quality assessment or code analysis requests
Code review (PRs, refactors, pre-merge checks)
Maintainability or performance improvements
Security hygiene improvements (non-audit level)

Avoid when:

A full security audit is required (use security-specific skills)
The task is purely dependency or artifact cleanup (use repo-cleanup)
Quick Reference
Task	Load reference
Code analysis	skills/code-quality-workflow/references/analyze-code.md
Code review	skills/code-quality-workflow/references/code-review.md
Systematic improvements	skills/code-quality-workflow/references/quality-improve.md
Workflow
Select the mode: analyze, review, or improve.
Load the matching reference file for the expected structure.
Inspect code and identify findings or opportunities.
Apply changes (if improving) with safety validation.
Verify with tests or lint as appropriate.
Report findings, fixes, and follow-ups.
Output
Findings or improvements summary
Validation evidence or recommended checks
Follow-up backlog items if needed
Common Mistakes
Skipping severity prioritization
Mixing review and improvement without sign-off
Applying fixes without baseline tests
Overlapping with full security audit scopes
Weekly Installs
48
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass