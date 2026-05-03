---
rating: ⭐⭐⭐
title: systematic-testing
url: https://skills.sh/xbklairith/kisune/systematic-testing
---

# systematic-testing

skills/xbklairith/kisune/systematic-testing
systematic-testing
Installation
$ npx skills add https://github.com/xbklairith/kisune --skill systematic-testing
SKILL.md
Systematic Testing Skill
Purpose

Guide test-driven development (TDD), generate comprehensive test suites, and provide systematic debugging frameworks. Ensures code is well-tested and bugs are resolved methodically rather than through trial-and-error.

Activation Triggers

Activate this skill when:

User implements new functionality (auto-suggest tests)
Tests fail (activate debugging framework)
User says "write tests for this"
User mentions "TDD" or "test-driven"
User asks about debugging or troubleshooting
User says "this bug..." or "error..."
Before marking feature complete (verify test coverage)
Core Capabilities
1. Test-Driven Development (TDD)

For complete TDD workflow, use Skill tool to invoke: dev-workflow:test-driven-development

Use Skill tool: Skill(skill: "dev-workflow:test-driven-development")


The test-driven-development skill provides full RED-GREEN-REFACTOR cycle, strict enforcement, anti-patterns, and verification checklists.

Quick TDD Summary:

RED: Write failing test first
GREEN: Write minimal code to pass
REFACTOR: Clean up while tests stay green

This skill focuses on test generation strategies and systematic debugging. For TDD methodology details, use the dedicated skill.

2. Test Generation

Goal: Generate comprehensive test suites covering all scenarios

Test Categories
Normal Cases (Happy Path)

Test expected, typical usage with valid inputs and standard flows.

Edge Cases (Boundary Conditions)

Test limits and boundaries:

Very small/large values
Equal values where difference is expected
Fractional results requiring rounding
Empty collections, zero-length strings
Error Cases (Invalid Inputs)

Test error handling:

Negative values, zero values
Out-of-range parameters
Null/nil/None inputs
Invalid types
Integration Cases

Test component interactions: full request-response flows, token validation chains, cross-component data passing.

Test Generation Template
suite "[Component/Function Name]":

    setup:    # Reset state, create test data
    teardown: # Clean up, reset mocks

    group "normal operation":
        test "should [expected behavior for typical input]"

    group "edge cases":
        test "should handle [boundary condition]"

    group "error handling":
        test "should reject [invalid input]":
            assert_raises(ExpectedError, invalid_call())

    group "integration":
        test "should work with [other component]"

3. Systematic Debugging Framework

Goal: Resolve bugs methodically, not through random trial-and-error

Phase 1: Root Cause Investigation
Reproduce Bug Consistently - Document exact steps and reproducibility rate
Identify Symptoms - Visible errors, expected vs actual behavior
Gather Evidence - Error messages, stack traces, log entries, network requests, triggering inputs
Form Initial Hypothesis - State hypothesis, supporting evidence, and next step
Phase 2: Pattern Analysis

Answer these questions:

When does it fail? - Specific inputs, users, timing, action sequences?
When does it work? - Any succeeding inputs, unaffected users, regression timing?
What changed recently?
git log --since="2 days ago" --oneline
git log -p path/to/file
git bisect  # Find exact commit that introduced bug

Environmental factors? - Local vs production, platform-specific, load-related?

Document the pattern: list conditions under FAILS and WORKS to identify the discriminator.

Phase 3: Hypothesis Testing
Create minimal test case isolating the bug
Add instrumentation (logging) to trace execution
Test hypothesis - Confirm or reject with evidence
Iterate until root cause is found
Phase 4: Fix and Protect
Write test reproducing the bug - Verify it fails before fix
Fix the root cause - Not just symptoms
Verify test passes after fix
Add regression tests for similar edge cases
Document root cause - What, why, and how it was fixed
Commit with context - Reference issue numbers, explain the why
Test Coverage Analysis

Check Coverage: Run your project's test coverage command (e.g., --coverage flag, coverage plugin, or dedicated tool).

Prioritize coverage gaps by:

Critical business logic (highest priority)
Security-sensitive code
Complex algorithms
Error handling paths
Edge cases
Best Practices
TDD
Always write test first - no exceptions
One test at a time - don't batch before implementing
Smallest possible step - each cycle should be 5-10 minutes
Test behavior, not implementation - don't test private methods
Keep tests simple - tests should be easier to understand than code
Test Quality
Clear test names that read like documentation
Arrange-Act-Assert structure consistently
One assertion per test for clear failures
No logic in tests - simple data only
Independent tests - no test depends on another
Debugging
Reproduce first - can't fix what you can't reproduce
Understand before fixing - don't guess and check
Fix root cause - don't just treat symptoms
Add regression test - prevent bug from returning
Document why - help future debuggers
Integration with Dev-Workflow
dev-workflow:test-driven-development - Guided TDD workflow, enhanced RED-GREEN-REFACTOR
dev-workflow:systematic-testing - Complex debugging, root cause tracing, advanced instrumentation
Common Anti-Patterns to Avoid
Writing tests after implementation
Changing tests to match implementation
Testing implementation details instead of behavior
Skipping refactor phase
Making multiple changes before testing
Debugging by randomly changing code
Committing debug logging code
Notes
TDD is slower initially but faster overall (fewer bugs, less debugging)
Good tests are documentation that never gets outdated
Debugging is detective work, not guessing
Always add regression tests after fixing bugs
Test coverage is a minimum bar, not a goal
Weekly Installs
17
Repository
xbklairith/kisune
GitHub Stars
2
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass