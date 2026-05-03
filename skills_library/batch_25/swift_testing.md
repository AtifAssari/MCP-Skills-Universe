---
title: swift_testing
url: https://skills.sh/swiftzilla/skills/swift_testing
---

# swift_testing

skills/swiftzilla/skills/swift_testing
swift_testing
Installation
$ npx skills add https://github.com/swiftzilla/skills --skill swift_testing
SKILL.md
Swift Testing

This skill covers the modern Swift Testing framework introduced in Swift 5.9 for writing clean, expressive tests.

Overview

Swift Testing is Apple's modern testing framework that provides a more expressive and flexible way to write tests compared to XCTest. It features Swift-native syntax, parameterized tests, and better async support.

Available References
Test Basics - Test declarations, assertions, and lifecycle
Async Testing - Testing async/await code
Parameterized Tests - Running tests with multiple inputs
Test Organization - Suites, tags, and test structure
Quick Reference
Basic Test
import Testing

@Test
func addition() {
    let result = 1 + 1
    #expect(result == 2)
}

@Test
func throwsError() throws {
    #expect(throws: MyError.invalid) {
        try riskyOperation()
    }
}

Async Test
@Test
func fetchData() async throws {
    let data = try await fetchUser()
    #expect(data.name == "Ada")
}

Parameterized Test
@Test(arguments: ["hello", "world", "swift"])
func stringLength(string: String) {
    #expect(string.count > 0)
}

@Test(arguments: zip([1, 2, 3], [1, 4, 9]))
func squared(input: Int, expected: Int) {
    #expect(input * input == expected)
}

Test Suite
@Suite
struct CalculatorTests {
    let calculator = Calculator()
    
    @Test
    func add() {
        #expect(calculator.add(2, 3) == 5)
    }
    
    @Test
    func subtract() {
        #expect(calculator.subtract(5, 3) == 2)
    }
}

Swift Testing vs XCTest
Feature	Swift Testing	XCTest
Syntax	Native Swift	Objective-C heritage
Async	First-class	Added later
Parameters	Built-in	Manual loops
Assertions	#expect, #require	XCTAssert
Suite	@Suite	Class-based
Best Practices
Use descriptive names - Test names should explain behavior
Test one thing - Each test should verify one concept
Use #require for preconditions - Fail fast if setup fails
Leverage parameterized tests - Test multiple inputs efficiently
Organize with suites - Group related tests
Use tags - Categorize tests for selective running
Test async code - Use async test functions
Keep tests independent - No shared state between tests
Running Tests
# Run all tests
swift test

# Run specific test
swift test --filter addition

# Run tests by tag
swift test --tag unit

# Run with verbose output
swift test --verbose

For More Information

Visit https://swiftzilla.dev for comprehensive Swift Testing documentation.

Weekly Installs
26
Repository
swiftzilla/skills
GitHub Stars
6
First Seen
Jan 28, 2026