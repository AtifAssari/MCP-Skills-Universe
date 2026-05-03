---
rating: ⭐⭐⭐
title: swift-testing-pro
url: https://skills.sh/twostraws/swift-testing-agent-skill/swift-testing-pro
---

# swift-testing-pro

skills/twostraws/swift-testing-agent-skill/swift-testing-pro
swift-testing-pro
Installation
$ npx skills add https://github.com/twostraws/swift-testing-agent-skill --skill swift-testing-pro
Summary

Write, review, and improve Swift Testing code with modern APIs and best practices.

Validates test structure, assertions, dependency injection, async patterns, and actor isolation against Swift Testing conventions
Guides migration from XCTest to Swift Testing, including assertion mappings and modern concurrency patterns
Covers new features like raw identifiers, test scopes, exit tests, attachments, and range-based confirmations
Targets Swift 6.2+ with emphasis on modern Swift concurrency; does not support UI testing (XCTest required there)
Reports only genuine issues without nitpicking; organizes findings by file with before/after code fixes
SKILL.md

Write and review Swift Testing code for correctness, modern API usage, and adherence to project conventions. Report only genuine problems - do not nitpick or invent issues.

Review process:

Ensure tests follow core Swift Testing conventions using references/core-rules.md.
Validate test structure, assertions, dependency injection, and other best practices using references/writing-better-tests.md.
Check async tests, confirmations, time limits, actor isolation, and networking mocks using references/async-tests.md.
Ensure new features like raw identifiers, test scopes, exit tests, and attachments are used correctly using references/new-features.md.
If migrating from XCTest, follow the conversion guidance in references/migrating-from-xctest.md.

If doing partial work, load only the relevant reference files.

Core Instructions
Target Swift 6.2 or later, using modern Swift concurrency.
As a Swift Testing developer, the user wants all new unit and integration tests to be written using Swift Testing, and they may ask for help migrating existing XCTest code to Swift Testing.
Swift Testing does not support UI tests – XCTest must be used there.
Use a consistent project structure, with folder layout determined by app features.

Swift Testing evolves with each Swift release, so expect three to four releases each year, each introducing new features. This means existing training data you have will naturally be outdated or missing key features.

This skill specifically draws upon the very latest Swift and Swift Testing code, which means it will suggest things you are not aware of. Treat the user’s installed toolchain as authoritative, but there's a fairly high chance Apple's documentation about the APIs will be stale, so treat them carefully.

Output Format

If the user asks for a review, organize findings by file. For each issue:

State the file and relevant line(s).
Name the rule being violated.
Show a brief before/after code fix.

Skip files with no issues. End with a prioritized summary of the most impactful changes to make first.

If the user asks you to write or improve tests, follow the same rules above but make the changes directly instead of returning a findings report.

Example output:

UserTests.swift

Line 5: Use struct, not class, for test suites.

// Before
class UserTests: XCTestCase {

// After
struct UserTests {


Line 12: Use #expect instead of XCTAssertEqual.

// Before
XCTAssertEqual(user.name, "Taylor")

// After
#expect(user.name == "Taylor")


Line 30: Use #require for preconditions, not #expect.

// Before
#expect(users.isEmpty == false)
let first = users.first!

// After
let first = try #require(users.first)

Summary
Fundamentals (high): Test suite on line 5 should be a struct, not a class inheriting from XCTestCase.
Migration (medium): XCTAssertEqual on line 12 should be migrated to #expect.
Assertions (medium): Force-unwrap on line 30 should use #require to unwrap safely and stop the test early on failure.

End of example.

References
references/core-rules.md - core Swift Testing rules: structs over classes, init/deinit over setUp/tearDown, parallel execution, parameterized tests, withKnownIssue, and tags.
references/writing-better-tests.md - test hygiene, structuring tests, hidden dependencies, #expect vs #require, Issue.record(), #expect(throws:), and verification methods.
references/async-tests.md - serialized tests, confirmation(), time limits, actor isolation, testing pre-concurrency code, and mocking networking.
references/new-features.md - raw identifiers, range-based confirmations, test scoping traits, exit tests, attachments, ConditionTrait.evaluate(), and the updated #expect(throws:) return value.
references/migrating-from-xctest.md - XCTest-to-Swift Testing conversion steps, assertion mappings, and floating-point tolerance via Swift Numerics.
Weekly Installs
3.5K
Repository
twostraws/swift…nt-skill
GitHub Stars
298
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass