---
title: test-driven-development
url: https://skills.sh/dralgorhythm/claude-agentic-framework/test-driven-development
---

# test-driven-development

skills/dralgorhythm/claude-agentic-framework/test-driven-development
test-driven-development
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill test-driven-development
SKILL.md
Test-Driven Development
The TDD Cycle
Red: Write a failing test
Green: Write minimal code to pass
Refactor: Improve code while keeping tests green
Workflows
 Write Test: Write a test that describes desired behavior
 Run Test: Verify it fails (Red)
 Implement: Write minimal code to pass
 Run Test: Verify it passes (Green)
 Refactor: Clean up while tests stay green
 Repeat: Next test case
TDD Example
Step 1: Red - Write Failing Test
describe("Calculator", () => {
  test("adds two numbers", () => {
    const calc = new Calculator();
    expect(calc.add(2, 3)).toBe(5);
  });
});

// Run: FAIL - Calculator is not defined

Step 2: Green - Minimal Implementation
class Calculator {
  add(a: number, b: number): number {
    return a + b;
  }
}

// Run: PASS

Step 3: Refactor (if needed)

Code is already clean, move to next test.

Step 4: Next Test
test("subtracts two numbers", () => {
  const calc = new Calculator();
  expect(calc.subtract(5, 3)).toBe(2);
});

// Run: FAIL - subtract is not defined

TDD Benefits
Design Feedback: Tests reveal design issues early
Documentation: Tests document expected behavior
Confidence: Refactor fearlessly with test safety net
Focus: One behavior at a time
TDD Tips
Start Simple: Begin with the simplest test case
One Assert: Each test should verify one behavior
Descriptive Names: Test names are documentation
No Logic in Tests: Tests should be obvious
Fast Feedback: Tests should run in milliseconds
When to Use TDD
New features with clear requirements
Bug fixes (write failing test first)
Complex business logic
API contract development
When TDD is Less Useful
Exploratory/prototype code
UI layout changes
Simple CRUD operations
Weekly Installs
35
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass