---
rating: ⭐⭐
title: csharp-xunit
url: https://skills.sh/github/awesome-copilot/csharp-xunit
---

# csharp-xunit

skills/github/awesome-copilot/csharp-xunit
csharp-xunit
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill csharp-xunit
Summary

Comprehensive XUnit testing guide covering standard facts, data-driven theories, and best practices.

Covers test structure using Arrange-Act-Assert pattern, naming conventions, and fixture-based setup/teardown with IClassFixture<T> and ICollectionFixture<T>
Explains data-driven testing with [Theory] combined with [InlineData], [MemberData], and [ClassData] attributes, plus custom data attribute creation
Details assertion methods for equality, collections, regex patterns, and exception handling, with optional fluent assertions library integration
Includes mocking strategies using Moq or NSubstitute, test organization with traits and collections, and diagnostic output via ITestOutputHelper
SKILL.md
XUnit Best Practices

Your goal is to help me write effective unit tests with XUnit, covering both standard and data-driven testing approaches.

Project Setup
Use a separate test project with naming convention [ProjectName].Tests
Reference Microsoft.NET.Test.Sdk, xunit, and xunit.runner.visualstudio packages
Create test classes that match the classes being tested (e.g., CalculatorTests for Calculator)
Use .NET SDK test commands: dotnet test for running tests
Test Structure
No test class attributes required (unlike MSTest/NUnit)
Use fact-based tests with [Fact] attribute for simple tests
Follow the Arrange-Act-Assert (AAA) pattern
Name tests using the pattern MethodName_Scenario_ExpectedBehavior
Use constructor for setup and IDisposable.Dispose() for teardown
Use IClassFixture<T> for shared context between tests in a class
Use ICollectionFixture<T> for shared context between multiple test classes
Standard Tests
Keep tests focused on a single behavior
Avoid testing multiple behaviors in one test method
Use clear assertions that express intent
Include only the assertions needed to verify the test case
Make tests independent and idempotent (can run in any order)
Avoid test interdependencies
Data-Driven Tests
Use [Theory] combined with data source attributes
Use [InlineData] for inline test data
Use [MemberData] for method-based test data
Use [ClassData] for class-based test data
Create custom data attributes by implementing DataAttribute
Use meaningful parameter names in data-driven tests
Assertions
Use Assert.Equal for value equality
Use Assert.Same for reference equality
Use Assert.True/Assert.False for boolean conditions
Use Assert.Contains/Assert.DoesNotContain for collections
Use Assert.Matches/Assert.DoesNotMatch for regex pattern matching
Use Assert.Throws<T> or await Assert.ThrowsAsync<T> to test exceptions
Use fluent assertions library for more readable assertions
Mocking and Isolation
Consider using Moq or NSubstitute alongside XUnit
Mock dependencies to isolate units under test
Use interfaces to facilitate mocking
Consider using a DI container for complex test setups
Test Organization
Group tests by feature or component
Use [Trait("Category", "CategoryName")] for categorization
Use collection fixtures to group tests with shared dependencies
Consider output helpers (ITestOutputHelper) for test diagnostics
Skip tests conditionally with Skip = "reason" in fact/theory attributes
Weekly Installs
8.8K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass