---
title: tdd
url: https://skills.sh/jellydn/my-ai-tools/tdd
---

# tdd

skills/jellydn/my-ai-tools/tdd
tdd
Installation
$ npx skills add https://github.com/jellydn/my-ai-tools --skill tdd
SKILL.md
Test-Driven Development (TDD)

Guides you through the complete TDD workflow with Red-Green-Refactor cycle.

Usage

/tdd <ACTION> [ARGUMENTS]

Actions
start - Initialize TDD session for a feature
red <TEST_NAME> - Create failing test (Red phase)
green - Run tests and implement code (Green phase)
refactor - Guide refactoring process (Refactor phase)
cycle - Run complete Red-Green-Refactor cycle
watch - Start test watcher for continuous feedback
status - Show current test status and next steps
help - Show this help
TDD Principles
The Red-Green-Refactor Cycle
Red: Write a failing test that defines desired behavior
Green: Write minimal code to make the test pass
Refactor: Improve code quality while keeping tests green
Best Practices
Write tests first - Tests define the interface and behavior
Small steps - Make tiny, incremental changes
Fast feedback - Run tests frequently for immediate validation
Clean code - Refactor regularly to maintain quality
One concept per test - Keep tests focused and atomic
AAA Pattern - Structure tests as Arrange, Act, Assert
Black-box testing - Test only public methods and behavior, not implementation details
Process
For "start ":
Initialize TDD session for the feature
Create or identify target source file
Create corresponding test file if it doesn't exist
Explain the feature requirements and acceptance criteria
For "red <TEST_NAME>":
Create a failing test that describes the desired behavior
Ensure test fails for the right reason (not syntax errors)
Run tests to confirm red state
Explain what the test is validating
For "green":
Implement minimal code to make failing tests pass
Focus on making tests pass, not perfect code
Run tests to confirm green state
Avoid over-engineering at this stage
For "refactor":
Improve code quality while maintaining green tests
Remove duplication and improve design
Run tests continuously during refactoring
Make one refactoring change at a time
Test Template

A test template is available at $SKILL_PATH/templates/test-template.md:

import { describe, it, expect } from 'vitest'
import { functionName } from './module'

describe('functionName', () => {
  it('should return formatted output when given valid input', () => {
    // Arrange - Setup test scenario
    const input = 'test input'
    const expectedOutput = 'expected output'

    // Act - Execute the unit under test
    const result = functionName(input)

    // Assert - Verify expected outcome
    expect(result).toBe(expectedOutput)
  })
})

Common Commands
Run tests: npm test or pnpm test
Watch mode: npm test --watch
With coverage: npm test --coverage
Weekly Installs
27
Repository
jellydn/my-ai-tools
GitHub Stars
71
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass