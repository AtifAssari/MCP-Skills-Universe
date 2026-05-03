---
title: test-cases
url: https://skills.sh/cexll/myclaude/test-cases
---

# test-cases

skills/cexll/myclaude/test-cases
test-cases
Installation
$ npx skills add https://github.com/cexll/myclaude --skill test-cases
Summary

Comprehensive test case generation from PRD documents and user requirements with full coverage mapping.

Transforms product requirements into structured, executable test cases organized by category: functional, edge case, error handling, and state transition scenarios
Generates requirement-driven test cases with unique IDs, priority levels, preconditions, step-by-step actions, and measurable expected results
Includes traceability matrix linking each requirement to corresponding test cases and coverage status
Follows pragmatic testing philosophy: test what matters, ensure complete coverage, and maintain quality over quantity
SKILL.md
Test Cases Generator

This skill generates comprehensive, requirement-driven test cases from PRD documents or user requirements.

Purpose

Transform product requirements into structured test cases that ensure complete coverage of functionality, edge cases, error scenarios, and state transitions. The skill follows a pragmatic testing philosophy: test what matters, ensure every requirement has corresponding test coverage, and maintain test quality over quantity.

When to Use

Trigger this skill when:

User provides a PRD or requirements document and requests test cases
User asks to "generate test cases", "create test scenarios", or "plan QA"
User mentions testing coverage for a feature or requirement
User needs structured test documentation in markdown format
Core Testing Principles

Follow these principles when generating test cases:

Requirement-driven, not implementation-driven - Test cases must map directly to requirements, not implementation details
Complete coverage - Every requirement must have at least one test case covering:
Happy path (normal use cases)
Edge cases (boundary values, empty inputs, max limits)
Error handling (invalid inputs, failure scenarios, permission errors)
State transitions (if stateful, cover all valid state changes)
Clear and actionable - Each test case must be executable by a QA engineer without ambiguity
Traceable - Maintain clear mapping between requirements and test cases
Workflow
Step 1: Gather Requirements

First, identify the source of requirements:

If user provides a file path to a PRD, read it using the Read tool
If user describes requirements verbally, capture them
If requirements are unclear or incomplete, use AskUserQuestion to clarify:
What are the core user flows?
What are the acceptance criteria?
What are the edge cases or error scenarios to consider?
Are there any state transitions or workflows?
What platforms or environments need testing?
Step 2: Extract Test Scenarios

Analyze requirements and extract test scenarios:

Functional scenarios - Normal use cases from requirements
Edge case scenarios - Boundary conditions, empty states, maximum limits
Error scenarios - Invalid inputs, permission failures, network errors
State transition scenarios - If the feature involves state, map all transitions

For each requirement, identify:

Preconditions (what must be true before testing)
Test steps (actions to perform)
Expected results (what should happen)
Postconditions (state after test completes)
Step 3: Structure Test Cases

Organize test cases using this structure:

# Test Cases: [Feature Name]

## Overview
- **Feature**: [Feature name]
- **Requirements Source**: [PRD file path or description]
- **Test Coverage**: [Summary of what's covered]
- **Last Updated**: [Date]

## Test Case Categories

### 1. Functional Tests
Test cases covering normal user flows and core functionality.

#### TC-F-001: [Test Case Title]
- **Requirement**: [Link to specific requirement]
- **Priority**: [High/Medium/Low]
- **Preconditions**:
  - [Condition 1]
  - [Condition 2]
- **Test Steps**:
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]
- **Expected Results**:
  - [Expected result 1]
  - [Expected result 2]
- **Postconditions**: [State after test]

### 2. Edge Case Tests
Test cases covering boundary conditions and unusual inputs.

#### TC-E-001: [Test Case Title]
[Same structure as above]

### 3. Error Handling Tests
Test cases covering error scenarios and failure modes.

#### TC-ERR-001: [Test Case Title]
[Same structure as above]

### 4. State Transition Tests
Test cases covering state changes and workflows (if applicable).

#### TC-ST-001: [Test Case Title]
[Same structure as above]

## Test Coverage Matrix

| Requirement ID | Test Cases | Coverage Status |
|---------------|------------|-----------------|
| REQ-001 | TC-F-001, TC-E-001 | ✓ Complete |
| REQ-002 | TC-F-002 | ⚠ Partial |

## Notes
- [Any additional testing considerations]
- [Known limitations or assumptions]

Step 4: Generate Test Cases

For each identified scenario, create a detailed test case following the structure above. Ensure:

Unique IDs - Use prefixes: TC-F (functional), TC-E (edge), TC-ERR (error), TC-ST (state)
Clear titles - Descriptive titles that explain what's being tested
Requirement traceability - Link each test case to specific requirements
Priority assignment - Mark critical paths as High priority
Executable steps - Steps must be clear enough for any QA engineer to execute
Measurable results - Expected results must be verifiable
Step 5: Validate Coverage

Before finalizing, verify:

Every requirement has at least one test case
Happy path is covered for all user flows
Edge cases are identified for boundary conditions
Error scenarios are covered for failure modes
State transitions are tested if feature is stateful

If coverage gaps exist, generate additional test cases.

Step 6: Output Test Cases

Write the test cases to tests/<name>-test-cases.md where <name> is derived from:

The feature name from the PRD
The user's specified name
A sanitized version of the requirement title

Use the Write tool to create the file with the structured test cases.

Step 7: Summary

After generating test cases, provide a brief summary in Chinese:

Total number of test cases generated
Coverage breakdown (functional, edge, error, state)
Any assumptions made or areas needing clarification
File path where test cases were saved
Quality Checklist

Before finalizing test cases, verify:

 Every requirement has corresponding test cases
 Happy path scenarios are covered
 Edge cases include boundary values, empty inputs, max limits
 Error handling covers invalid inputs and failure scenarios
 State transitions are tested if applicable
 Test case IDs are unique and follow naming convention
 Test steps are clear and executable
 Expected results are measurable and verifiable
 Coverage matrix shows complete coverage
 File is written to tests/-test-cases.md
Example Usage

User: "Generate test cases for the user authentication feature in docs/auth-prd.md"

Process:

Read docs/auth-prd.md
Extract requirements: login, logout, password reset, session management
Identify scenarios: successful login, invalid credentials, expired session, etc.
Generate test cases covering all scenarios
Write to tests/auth-test-cases.md
Summarize coverage in Chinese
References

For detailed testing methodologies and best practices, see:

references/testing-principles.md - Core testing principles and patterns
Weekly Installs
744
Repository
cexll/myclaude
GitHub Stars
2.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass