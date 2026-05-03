---
title: swift-testing
url: https://skills.sh/dpearson2699/swift-ios-skills/swift-testing
---

# swift-testing

skills/dpearson2699/swift-ios-skills/swift-testing
swift-testing
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill swift-testing
Summary

Modern Swift testing framework with @Test macros, parameterized tests, traits, and async support.

Write unit tests using @Test macros with #expect and #require assertions; prefer Swift Testing over XCTest for all new tests (Xcode 16+, Swift 6+)
Organize tests with @Suite for grouping, custom tags for filtering, and traits for conditional execution, time limits, and known issues
Support parameterized tests via arguments: with enum cases, ranges, or cartesian products; use confirmation() to verify async callbacks without sleep
Handle async/await patterns natively, test error paths with throws: expectations, and manage actor-isolated state with await
SKILL.md
Swift Testing

Swift Testing is the modern testing framework for Swift (Xcode 16+, Swift 6+). Prefer it over XCTest for all new unit tests. Use XCTest only for UI tests, performance benchmarks, and snapshot tests.

Contents
Basic Tests
@Test Traits
#expect and #require
@Suite and Test Organization
Execution Model
Known Issues
Additional Patterns
Common Mistakes
Test Attachments
Exit Testing
Review Checklist
References
Basic Tests
import Testing

@Test("User can update their display name")
func updateDisplayName() {
    var user = User(name: "Alice")
    user.name = "Bob"
    #expect(user.name == "Bob")
}

@Test Traits
@Test("Validates email format")                                    // display name
@Test(.tags(.validation, .email))                                  // tags
@Test(.disabled("Server migration in progress"))                   // disabled
@Test(.enabled(if: ProcessInfo.processInfo.environment["CI"] != nil)) // conditional
@Test(.bug("https://github.com/org/repo/issues/42"))               // bug reference
@Test(.timeLimit(.minutes(1)))                                     // time limit
@Test("Timeout handling", .tags(.networking), .timeLimit(.seconds(30))) // combined

#expect and #require
// #expect records failure but continues execution
#expect(result == 42)
#expect(name.isEmpty == false)
#expect(items.count > 0, "Items should not be empty")

// #expect with error type checking
#expect(throws: ValidationError.self) {
    try validate(email: "not-an-email")
}

// #expect with specific error value
#expect {
    try validate(email: "")
} throws: { error in
    guard let err = error as? ValidationError else { return false }
    return err == .empty
}

// #require records failure AND stops test (like XCTUnwrap)
let user = try #require(await fetchUser(id: 1))
#expect(user.name == "Alice")

// #require for optionals -- unwraps or fails
let first = try #require(items.first)
#expect(first.isValid)


Rule: Use #require when subsequent assertions depend on the value. Use #expect for independent checks.

@Suite and Test Organization

See references/testing-patterns.md for suite organization, confirmation patterns, known-issue handling, and execution-model details.

Execution Model

Swift Testing runs tests in parallel by default. Do not assume test order, shared suite instances, or exclusive access to mutable state unless you explicitly design for it.

@Suite(.serialized)
struct KeychainTests {
    @Test func storesToken() throws { /* ... */ }
    @Test func deletesToken() throws { /* ... */ }
}


Use .serialized when a test or suite must run one-at-a-time because it touches shared external state. It does not make unrelated tests outside that scope run serially.

Rules:

Each test must set up its own state.
Shared mutable globals are a bug unless protected or intentionally serialized.
@Suite(.serialized) is for exclusive execution, not for expressing logical ordering between tests.
If tests depend on sequence, combine them into one test or move the sequence into shared helper code.
Known Issues

Mark expected failures so they do not cause test failure:

withKnownIssue("Propane tank is empty") {
    #expect(truck.grill.isHeating)
}

// Intermittent / flaky failures
withKnownIssue(isIntermittent: true) {
    #expect(service.isReachable)
}

// Conditional known issue
withKnownIssue {
    #expect(foodTruck.grill.isHeating)
} when: {
    !hasPropane
}


If no known issues are recorded, Swift Testing records a distinct issue notifying you the problem may be resolved.

Additional Patterns

See references/testing-patterns.md for parameterized tests, tags and suites, async testing, traits, and execution-model details.

Test Attachments

Attach diagnostic data to test results for debugging failures. See references/testing-patterns.md for full examples.

@Test func generateReport() async throws {
    let report = try generateReport()
    Attachment.record(report.data, named: "report.json")
    #expect(report.isValid)
}


Image attachments are available via cross-import overlays — import both Testing and a UI framework:

import Testing
import UIKit

@Test func renderedChart() async throws {
    let image = renderer.image { ctx in chartView.drawHierarchy(in: bounds, afterScreenUpdates: true) }
    Attachment.record(image, named: "chart.png")
}

Exit Testing

Test code that calls exit(), fatalError(), or preconditionFailure(). See references/testing-patterns.md for details.

@Test func invalidInputCausesExit() async {
    await #expect(processExitsWith: .failure) {
        processInvalidInput()  // calls fatalError()
    }
}

Common Mistakes
Testing implementation, not behavior. Test what the code does, not how.
No error path tests. If a function can throw, test the throw path.
Flaky async tests. Use confirmation with expected counts, not sleep calls.
Shared mutable state between tests. Each test sets up its own state via init() in @Suite.
Missing accessibility identifiers in UI tests. XCUITest queries rely on them.
Using sleep in tests. Use confirmation, clock injection, or withKnownIssue.
Not testing cancellation. If code supports Task cancellation, verify it cancels cleanly.
Mixing XCTest and Swift Testing in one file. Keep them in separate files.
Non-Sendable test helpers shared across tests. Ensure test helper types are Sendable when shared across concurrent test cases. Annotate MainActor-dependent test code with @MainActor.
Assuming tests run in declaration order. Swift Testing runs in parallel by default; use .serialized only when exclusive execution is required.
Using .serialized to express workflow steps. Serialized execution does not make one test feed another; keep dependent steps in one test.
Review Checklist
 All new tests use Swift Testing (@Test, #expect), not XCTest assertions
 Test names describe behavior (fetchUserReturnsNilOnNetworkError not testFetchUser)
 Error paths have dedicated tests
 Async tests use confirmation(), not Task.sleep
 Parameterized tests used for repetitive variations
 Tags applied for filtering (.critical, .slow)
 Mocks conform to protocols, not subclass concrete types
 No shared mutable state between tests
 Tests do not rely on declaration order or shared suite instances
 .serialized used only for truly exclusive state, not to model workflow sequencing
 Cancellation tested for cancellable async operations
References
Testing patterns: references/testing-patterns.md
Advanced testing (warnings, cancellation, image attachments): references/testing-advanced.md
Weekly Installs
1.2K
Repository
dpearson2699/sw…s-skills
GitHub Stars
512
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass