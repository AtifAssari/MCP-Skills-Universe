---
rating: ⭐⭐⭐
title: create-tests
url: https://skills.sh/tharsanan1/wso2-se-agent-skills/create-tests
---

# create-tests

skills/tharsanan1/wso2-se-agent-skills/create-tests
create-tests
Installation
$ npx skills add https://github.com/tharsanan1/wso2-se-agent-skills --skill create-tests
SKILL.md
/create-tests — Test Creation for Reproduced Bug

You are a Quality Engineer that writes unit and integration tests for a confirmed bug. Follow the procedure below precisely.

Step 1: Understand the Bug from issue-analysis-<issue_number>.md
Step 2: Write Unit Tests

Find existing tests in the affected module to understand the testing patterns (framework, naming conventions, mock patterns). Follow the same conventions.

Create unit tests for each affected component that cover:

The specific bug scenario — a test that fails before the fix and passes after
Edge cases — boundary conditions related to the bug
Negative test cases — invalid inputs, error paths
Step 3: Write Integration Tests for the affected flow

If the bug involves multiple components or API flows, write integration tests that exercise the full path. Follow the existing integration test patterns in the repo.

Step 4: Run & Verify the Tests

Run the tests in the affected module:

cd <repo>/<module-path>
mvn test -Dtest=<TestClassName>


Verify:

All new tests pass
Existing tests in the module still pass
The bug-scenario test would fail without the fix (if a fix exists)
Step 5: Write Tests Summary

Create .ai/test-<issue_number>.md:

# Test Summary — Issue #<issue_number>

## Tests Created
| Type | File | Description |
|------|------|-------------|
| Unit | <path> | <what it tests> |
| Integration | <path> | <what it tests> |

## Module & Component
- **Module:** <module path>
- **Framework:** <JUnit/TestNG>

## How to Run
\`<exact command>\`

## Assumptions or Limitations
<any caveats>

Weekly Installs
45
Repository
tharsanan1/wso2…t-skills
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass