---
rating: ⭐⭐
title: code-review-checklist
url: https://skills.sh/mohitagw15856/pm-claude-skills/code-review-checklist
---

# code-review-checklist

skills/mohitagw15856/pm-claude-skills/code-review-checklist
code-review-checklist
Installation
$ npx skills add https://github.com/mohitagw15856/pm-claude-skills --skill code-review-checklist
SKILL.md
Code Review Checklist Skill

Produces a tailored code review checklist for a specific pull request — scaled to the language, type of change, and risk level. Not a generic template.

Required Inputs

Ask the user for these if not provided:

Language and framework (e.g. TypeScript + React / Python + FastAPI / Go)
Type of change (feature / bug fix / refactor / dependency upgrade / security patch / performance)
Risk level (low / medium / high / critical)
PR description (paste the description or link to the PR)
Author context (new starter / experienced / external contributor)
Output Structure
1. Review Summary

PR: [Title or reference] Scope assessment: [Small / Medium / Large / Too large — should be split] Recommended review depth: [Skim / Standard / Deep dive] Estimated review time: [Minutes]

2. Correctness Checks

Language-specific correctness checks — choose based on the language stated:

For TypeScript/JavaScript:

Type definitions match actual usage
No implicit any in non-test code
Async/await used consistently; no unhandled promises
Null/undefined handling is explicit

For Python:

Type hints present on public functions
Exception handling is specific (no bare except)
Resources are closed (context managers, with blocks)

For Go:

Errors are handled or explicitly ignored with a comment
Context propagation is correct
Goroutine lifetimes are bounded

[Include only the section matching the stated language]

3. Change-Type-Specific Checks

For bug fixes:

A test exists that would have caught this bug
The fix addresses root cause, not symptom
Related code paths checked for the same issue

For features:

Acceptance criteria met
Edge cases handled (empty, large, concurrent)
Error paths tested, not just happy path
Telemetry/logging added for debugging

For refactors:

Behaviour unchanged (tests still pass)
No scope creep — refactor only
Complexity reduced, not just moved

For dependency upgrades:

Breaking changes reviewed
Security advisories checked
License compatibility verified

[Include only the section matching the stated change type]

4. Risk-Appropriate Checks

Low risk: basic correctness, style conventions, test coverage Medium risk: above + rollback plan, monitoring updates, performance considerations High risk: above + security implications, data migration safety, feature flag/gradual rollout Critical risk: above + staging validation plan, incident response plan, post-deploy verification checklist

5. Testing Adequacy
Unit tests cover new logic
Integration tests cover the contract changes
Edge cases tested
Failure modes tested
Performance tests if performance-sensitive
6. Review Decision Framework

Approve if: [2-3 specific conditions based on this PR] Request changes if: [Specific blockers] Comment (non-blocking) if: [Items worth discussing but not blocking merge]

7. Common Pitfalls for This Change Type

Based on the change type and language, flag 2-3 things reviewers typically miss for this combination.

Quality Checks
 Checklist is tailored to the stated language (not generic)
 Change-type-specific section is included
 Risk-appropriate depth matches stated risk level
 Decision framework is explicit
Example Trigger Phrases
"Generate a code review checklist for [PR description]"
"What should I check in this pull request?"
"Give me a code review checklist for a [language] [change type]"
"Review checklist for a high-risk PR in [language]"
Weekly Installs
10
Repository
mohitagw15856/p…e-skills
GitHub Stars
293
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass