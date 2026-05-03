---
rating: ⭐⭐⭐
title: behavior-driven-testing
url: https://skills.sh/robotlearning123/behavior-driven-testing/behavior-driven-testing
---

# behavior-driven-testing

skills/robotlearning123/behavior-driven-testing/behavior-driven-testing
behavior-driven-testing
Installation
$ npx skills add https://github.com/robotlearning123/behavior-driven-testing --skill behavior-driven-testing
SKILL.md
Behavior-Driven Testing

Start from user behavior, not code structure. Every user-reachable path must be tested—no branch left uncovered, no edge case assumed.

Core Principles
Behavior over Implementation - Test what users see, not how code works
Exhaustive Coverage - Every branch, every condition, every edge case
Context Awareness - Every test must define its preconditions explicitly
Real Environment Validation - Mocks are tools, not destinations
Workflow Overview

Testing follows three phases. Follow them in order:

Analysis → Design → Execution → Verify Coverage → Ship (or loop back)


Analysis Phase:

Requirements Definition - Define "correct" behavior with Gherkin specs
Code Change Tracking - Know exactly what changed
State Machine Analysis - Map all UI states and transitions
Branch Mapping - Create the branch matrix (core artifact)

Design Phase: 5. Test Case Design - Apply equivalence partitioning, boundary analysis 6. Impact Analysis - Ensure new code doesn't break existing behavior 7. Test Prioritization - P0 (every commit) → P3 (periodic)

Execution Phase: 8. Test Data Preparation - Create fixtures, mocks, factories 9. Test Implementation - Write unit, integration, E2E tests 10. Test Execution - Run tests in phases (local → CI → staging) 11. Coverage Verification - Verify branch matrix completion

Quick Reference: Must-Test Branches
Category	Test Cases	Priority
Empty values	null, undefined, "", " " (whitespace), [], {}	P0
Boundaries	min-1, min, min+1, max-1, max, max+1	P1
Auth states	logged in, logged out, loading, session expired	P0
API responses	200+data, 200+empty, 400, 401, 403, 404, 500, timeout, offline	P0
User chaos	double-click, rapid navigation, refresh mid-action, back button	P1
The Whitespace Trap (Most Common Bug)
// ❌ WRONG - whitespace "   " is truthy!
if (!text) throw new Error('Required');

// ✅ CORRECT
if (!text?.trim()) throw new Error('Required');

Common Mistakes
Mistake	Why It's Bad	Fix
Only happy path	Error paths are 50% of code	Test ALL branches
Skip empty value tests	Most common production bugs	Test null, undefined, "", whitespace separately
Mock everything	Mocks hide real problems	Add integration + E2E tests
"Tested manually"	Not repeatable, not reliable	Automate it
Ignore loading states	Users interact during load	Test loading behavior
Skip double-click test	Users double-click everything	Test rapid interactions
Branch Matrix Template

For each code change, create a branch matrix:

| ID | Condition | True Behavior | False Behavior | Priority | Status |
|----|-----------|---------------|----------------|:--------:|:------:|
| B01 | user.isPremium | Skip credit check | Check credits | P0 | ⬜ |
| B02 | credits >= required | Proceed | Show error | P0 | ⬜ |
| B03 | credits == required | Boundary: Proceed | - | P1 | ⬜ |

Status: ⬜ Pending | ✅ Passed | ❌ Failed

Detailed References

Load these files only when you need detailed guidance:

Analysis details: See references/analysis-phase.md

Gherkin specification format
State machine diagrams
Complete branch mapping methodology

Test templates: See references/test-templates.md

Unit test structure (Vitest/Jest)
Integration test patterns
E2E test examples (Playwright)

Branch matrices: See references/branch-matrices.md

Entry point branches
Authentication branches
API response branches
Input validation branches

Testing principles: See references/testing-principles.md

Mock vs Real testing
Creating test conditions you don't have
Progressive testing strategy (Day 1-4)
Pre-Release Checklist

Before shipping, verify:

## Mock Tests (CI)
- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] Coverage thresholds met

## Real Tests (Before release)
- [ ] E2E tests pass on staging
- [ ] Manual smoke test on staging
- [ ] Core paths verified in real environment

## Branch Matrix
- [ ] All P0 branches tested
- [ ] All P1 branches tested
- [ ] No untested edge cases

## Production (After deploy)
- [ ] Smoke test passes
- [ ] Error rate monitoring normal

Related Skills
test-driven-development - Write tests first, then implementation
systematic-debugging - Debug issues methodically
Weekly Installs
46
Repository
robotlearning12…-testing
GitHub Stars
12
First Seen
Feb 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass