---
title: test-design-istqb
url: https://skills.sh/javalenciacai/qaskills/test-design-istqb
---

# test-design-istqb

skills/javalenciacai/qaskills/test-design-istqb
test-design-istqb
Installation
$ npx skills add https://github.com/javalenciacai/qaskills --skill test-design-istqb
SKILL.md
Test Design - ISTQB Techniques

Expert skill for designing comprehensive test cases using ISTQB Foundation Level test design techniques.

When to Use

Use this skill when you need to:

Design test cases from requirements
Apply black-box testing techniques
Create test data specifications
Ensure comprehensive test coverage
Generate test scenarios for positive, negative, and edge cases
ISTQB Test Design Techniques
1. Equivalence Partitioning

What it is: Divide input domains into classes where all members should be treated the same.

How to apply:

Identify all inputs and outputs
Determine valid and invalid partitions
Create one test case per partition
Cover both valid and invalid classes

Example:

Requirement: Age must be 18-65
Partitions:
- Invalid: < 18 (e.g., 17)
- Valid: 18-65 (e.g., 30)
- Invalid: > 65 (e.g., 66)

2. Boundary Value Analysis

What it is: Test at the edges of equivalence partitions where defects often hide.

How to apply:

Identify boundaries in requirements
Test: min-1, min, min+1, max-1, max, max+1
Focus on limits, ranges, and thresholds

Example:

Requirement: Password 8-20 characters
Test values: 7, 8, 9, 19, 20, 21 characters

3. Decision Tables

What it is: Test combinations of conditions and their resulting actions.

How to apply:

Identify conditions (inputs/states)
List possible actions (outputs/behaviors)
Create table with all meaningful combinations
Generate test cases from each column

Example:

Condition 1: Premium customer? (Y/N)
Condition 2: Order > $100? (Y/N)

| Premium | Order>$100 | Discount |
|---------|-----------|----------|
| Y       | Y         | 20%      |
| Y       | N         | 10%      |
| N       | Y         | 10%      |
| N       | N         | 0%       |

= 4 test cases

4. State Transition Testing

What it is: Test how system behavior changes based on state and events.

How to apply:

Identify all states
Map valid transitions
Identify invalid transitions
Test all valid paths
Test invalid transitions for error handling

Example:

Order States: Draft → Submitted → Approved → Shipped → Delivered

Valid transitions:
- Draft → Submitted
- Submitted → Approved
- Approved → Shipped
- Shipped → Delivered

Invalid transitions to test:
- Draft → Shipped (should reject)
- Delivered → Draft (should reject)

5. Error Guessing

What it is: Use experience to anticipate common defects.

Common areas:

Empty/null values
Special characters
Boundary conditions
Concurrent access
Network failures
Timeout scenarios
Test Case Template
Test Case ID: TC-XXX
Title: [Clear, descriptive title]
Preconditions: [System state before test]
Test Data: [Specific values to use]

Steps:
1. [Action]
2. [Action]
3. [Action]

Expected Results:
1. [Expected outcome]
2. [Expected outcome]
3. [Expected outcome]

Actual Results: [Filled during execution]
Status: [Pass/Fail]
Notes: [Any observations]

Coverage Checklist

Ensure test design includes:

✓ Positive scenarios (happy path)
✓ Negative scenarios (error handling)
✓ Edge cases (boundaries)
✓ Data validation tests
✓ State transitions
✓ Error messages verification
✓ Performance considerations
✓ Security aspects
✓ Usability/UX validation
Test Design Output

Deliverables:

Test cases with clear steps and expected results
Test data specifications with valid/invalid examples
Traceability matrix linking requirements to tests
Coverage analysis showing technique application
Risk assessment highlighting critical test areas
Best Practices
Start with happy path, then add negative cases
Use meaningful test case IDs with prefixes
Keep test cases atomic (one objective per test)
Make steps reproducible by anyone
Include cleanup/teardown procedures
Review test cases with team
Update tests when requirements change
Weekly Installs
10
Repository
javalenciacai/qaskills
GitHub Stars
3
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass