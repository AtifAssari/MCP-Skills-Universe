---
title: unit-testing-framework
url: https://skills.sh/aj-geddes/useful-ai-prompts/unit-testing-framework
---

# unit-testing-framework

skills/aj-geddes/useful-ai-prompts/unit-testing-framework
unit-testing-framework
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill unit-testing-framework
SKILL.md
Unit Testing Framework
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Write effective unit tests that are fast, isolated, readable, and maintainable following industry best practices and AAA (Arrange-Act-Assert) pattern.

When to Use
Writing tests for new code
Improving test coverage
Establishing testing standards
Refactoring with test safety
Implementing TDD (Test-Driven Development)
Creating test utilities and mocks
Quick Start

Minimal working example:

// Jest/JavaScript example
describe("UserService", () => {
  describe("createUser", () => {
    it("should create user with valid data", async () => {
      // Arrange - Set up test data and dependencies
      const userData = {
        email: "john@example.com",
        firstName: "John",
        lastName: "Doe",
      };
      const mockDatabase = createMockDatabase();
      const service = new UserService(mockDatabase);

      // Act - Execute the function being tested
      const result = await service.createUser(userData);

      // Assert - Verify the outcome
      expect(result.id).toBeDefined();
      expect(result.email).toBe("john@example.com");
      expect(mockDatabase.save).toHaveBeenCalledWith(
        expect.objectContaining(userData),
      );
    });
  });
});

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Test Structure (AAA Pattern)	Test Structure (AAA Pattern)
Test Cases by Language	Test Cases by Language
Mocking & Test Doubles	Mocking & Test Doubles
Testing Async Code	Testing Async Code, Test Coverage
Testing Edge Cases	Testing Edge Cases
Example: Complete Test Suite	import { UserService } from "./user-service";
Best Practices
✅ DO
Write tests before or alongside code (TDD)
Test one thing per test
Use descriptive test names
Follow AAA pattern
Test edge cases and error conditions
Keep tests isolated and independent
Use setup/teardown appropriately
Mock external dependencies
Aim for high coverage on critical paths
Make tests fast (< 10ms each)
Use parameterized tests for similar cases
Test public interfaces, not implementation
❌ DON'T
Test implementation details
Write tests that depend on each other
Ignore failing tests
Test third-party library code
Use real databases/APIs in unit tests
Make tests too complex
Skip edge cases
Forget to clean up resources
Test everything (focus on business logic)
Write flaky tests
Weekly Installs
289
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass