---
title: test-driven-development
url: https://skills.sh/nguyenhuuca/assessment/test-driven-development
---

# test-driven-development

skills/nguyenhuuca/assessment/test-driven-development
test-driven-development
Installation
$ npx skills add https://github.com/nguyenhuuca/assessment --skill test-driven-development
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
TDD Example (Java + JUnit 5)
Step 1: Red - Write Failing Test
class CalculatorTest {
    @Test
    void add_TwoNumbers_ReturnsSum() {
        // Arrange
        Calculator calc = new Calculator();

        // Act
        int result = calc.add(2, 3);

        // Assert
        assertThat(result).isEqualTo(5);
    }
}

// Run: mvn test
// FAIL - Cannot resolve symbol 'Calculator'

Step 2: Green - Minimal Implementation
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}

// Run: mvn test
// PASS ✓

Step 3: Refactor (if needed)

Code is already clean, move to next test.

Step 4: Next Test
@Test
void subtract_TwoNumbers_ReturnsDifference() {
    // Arrange
    Calculator calc = new Calculator();

    // Act
    int result = calc.subtract(5, 3);

    // Assert
    assertThat(result).isEqualTo(2);
}

// Run: mvn test
// FAIL - Cannot resolve method 'subtract' in 'Calculator'

Step 5: Implement Subtract
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }
}

// Run: mvn test
// PASS ✓ (2 tests passing)

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
10
Repository
nguyenhuuca/assessment
GitHub Stars
24
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass