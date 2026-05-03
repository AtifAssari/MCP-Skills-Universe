---
rating: ⭐⭐⭐
title: generating-apex-test
url: https://skills.sh/forcedotcom/afv-library/generating-apex-test
---

# generating-apex-test

skills/forcedotcom/afv-library/generating-apex-test
generating-apex-test
Installation
$ npx skills add https://github.com/forcedotcom/afv-library --skill generating-apex-test
SKILL.md
Generating Apex Tests

Generate production-ready Apex test classes and run disciplined test-fix loops with coverage analysis.

Core Principles
One behavior per method — each test method validates a single scenario. Separate positive, negative, and bulk tests. NEVER combine related-but-distinct inputs (e.g., null and empty) in one method — create _NullInput_ and _EmptyInput_ as separate test methods
Bulkify tests — test with 251+ records to cross the 200-record trigger batch boundary. Batch Apex exception: in test context only one execute() invocation runs, so set batchSize >= testRecordCount. See references/async-testing.md
Isolate test data — every @TestSetup must delegate record creation to a TestDataFactory class. If none exists, create one first. Never build record lists inline in @TestSetup. Never rely on org data (SeeAllData=false) or hardcoded IDs. For duplicate rule handling, see references/test-data-factory.md
Assert meaningfully — use exact expected values computed from test data setup. NEVER use range assertions or approximate counts when the value is deterministic. Always include failure messages. See references/assertion-patterns.md
Use Assert class only — Assert.areEqual, Assert.isTrue, Assert.fail, etc. Never use legacy System.assert, System.assertEquals, or System.assertNotEquals
Mock external boundaries — use HttpCalloutMock for callouts, Test.setFixedSearchResults for SOSL, DML mock classes for database isolation. Design for testability via constructor injection. See references/mocking-patterns.md
Test negative paths — validate error handling and exception scenarios, not just happy paths
Wrap with start/stop — pair Test.startTest() with Test.stopTest() to reset governor limits and force async execution
Test.startTest() / Test.stopTest()

Always wrap the code under test in Test.startTest() / Test.stopTest():

Resets governor limits so the test measures only the code under test
Executes async operations synchronously (queueables, batch, future methods)
Fires scheduled jobs immediately
Test Code Anti-Patterns
Anti-Pattern	Fix
SOQL/DML inside loops	Query once before the loop; use Map<Id, SObject> for lookups
Magic numbers in assertions	Derive expected values from setup constants
God test class (>500 lines)	Split into multiple test classes by behavior area
Long test methods (>30 lines)	Extract Given/When/Then into helper methods
Generic Exception catch	Catch the specific expected type (e.g., DmlException)
Workflow
Step 1 — Gather Context

Before generating or fixing tests, identify:

the target production class(es) under test
existing test classes, test data factories, and setup helpers
desired test scope (single class, specific methods, suite, or local tests)
coverage threshold (75% minimum for deploy, 90%+ recommended)
org alias when running tests against an org
Step 2 — Generate the Test Class

Apply the structure, naming conventions, and patterns from the asset templates and reference docs.

MANDATORY — File Deliverables: For every test class, create BOTH files:

{ClassName}Test.cls — the test class (use assets/test-class-template.cls as starting point)
{ClassName}Test.cls-meta.xml — the metadata file:
<?xml version="1.0" encoding="UTF-8"?>
<ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">
    <apiVersion>66.0</apiVersion>
    <status>Active</status>
</ApexClass>


If no TestDataFactory exists in the project, create TestDataFactory.cls + TestDataFactory.cls-meta.xml using assets/test-data-factory-template.cls.

@TestSetup Example
@TestSetup
static void setupTestData() {
    List<Account> accounts = TestDataFactory.createAccounts(251, true);
}

Test Method Structure

Use Given/When/Then:

@isTest
static void shouldUpdateStatus_WhenValidInput() {
    // Given
    List<Account> accounts = [SELECT Id FROM Account];

    // When
    Test.startTest();
    MyService.processAccounts(accounts);
    Test.stopTest();

    // Then
    List<Account> updated = [SELECT Id, Status__c FROM Account];
    Assert.areEqual(251, updated.size(), 'All accounts should be processed');
}

Negative Test — Exception Pattern

Use try/catch with Assert.fail to verify expected exceptions:

@isTest
static void shouldThrowException_WhenInvalidInput() {
    // Given
    List<Account> emptyList = new List<Account>();

    // When/Then
    Test.startTest();
    try {
        MyService.processAccounts(emptyList);
        Assert.fail('Expected MyCustomException to be thrown');
    } catch (MyCustomException e) {
        Assert.isTrue(e.getMessage().contains('cannot be empty'),
            'Exception message should indicate empty input');
    }
    Test.stopTest();
}

Naming Convention
should[ExpectedResult]_When[Scenario]: shouldSendNotification_WhenOpportunityClosedWon
[SubjectOrAction]_[Scenario]_[ExpectedResult]: AccountUpdate_ChangeName_Success
Step 3 — Run Tests

Start narrow when debugging; widen after the fix is stable.

# Single test class
sf apex run test --class-names MyServiceTest --result-format human --code-coverage --target-org <alias>

# Specific test methods
sf apex run test --tests MyServiceTest.shouldUpdateStatus_WhenValidInput --result-format human --target-org <alias>

# All local tests
sf apex run test --test-level RunLocalTests --result-format human --code-coverage --target-org <alias>

Step 4 — Analyze Results

Focus on:

failing methods — exception types and stack traces
uncovered lines and weak coverage areas
whether failures indicate bad test data, brittle assertions, or broken production logic
Step 5 — Fix Loop

When tests fail, run a disciplined fix loop (max 3 iterations — stop and surface root cause if still failing):

Read the failing test class and the class under test
Identify root cause from error messages and stack traces
Apply fix — adjust test data or assertions for test-side issues; delegate production code issues to the generating-apex skill
Rerun the focused test before broader regression
Repeat until all tests pass, iteration limit reached, or root cause requires design change
Step 6 — Validate Coverage
Level	Coverage	Purpose
Production deploy	75% minimum	Required by Salesforce
Recommended	90%+	Best practice target
Critical paths	100%	Business-critical code

Cover all paths: positive, negative/exception, bulk (251+ records), callout/async.

What to Test by Component
Component	Key Test Scenarios
Trigger	Bulk insert/update/delete, recursion guard, field change detection
Service	Valid/invalid inputs, bulk operations, exception handling
Controller	Page load, action methods, view state
Batch	start/execute/finish, scope matching (batch size >= record count), Database.Stateful tracking, error handling, chaining (separate methods — finish() calling Database.executeBatch() throws UnexpectedException)
Queueable	Chaining (only first job runs in tests), bulkification, error handling, callout mocks before Test.startTest()
Callout	Success response, error response, timeout
Selector	Valid/null/empty inputs, bulk (251+), field population, sort order, WITH USER_MODE via System.runAs
Scheduled	Direct execution via execute(null), CRON registration via CronTrigger query
Platform Event	Test.enableChangeDataCapture(), Test.getEventBus().deliver(), verify subscriber side effects
Output Expectations

Deliverables per test class:

{ClassName}Test.cls + {ClassName}Test.cls-meta.xml (match API version of class under test; default 66.0)
TestDataFactory.cls + TestDataFactory.cls-meta.xml (if not already present)
Reference Files

Load on demand for detailed patterns:

Reference	When to use
references/test-data-factory.md	TestDataFactory patterns, field overrides, duplicate rule handling
references/assertion-patterns.md	Assertion best practices, anti-patterns, common pitfalls
references/mocking-patterns.md	HttpCalloutMock, DML mocking, StubProvider, SOSL, Email, Platform Events
references/async-testing.md	Batch, Queueable, Future, Scheduled job testing
Weekly Installs
468
Repository
forcedotcom/afv-library
GitHub Stars
242
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass