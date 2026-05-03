---
title: testing-expert
url: https://skills.sh/shipshitdev/library/testing-expert
---

# testing-expert

skills/shipshitdev/library/testing-expert
testing-expert
Installation
$ npx skills add https://github.com/shipshitdev/library --skill testing-expert
SKILL.md
Testing Expert Skill

Expert in testing strategies for React, Next.js, and NestJS applications.

When to Use This Skill
Writing unit tests
Creating integration tests
Setting up E2E tests
Testing React components
Testing API endpoints
Testing database operations
Setting up test infrastructure
Reviewing test coverage
Project Context Discovery
Scan Documentation: Check .agents/SYSTEM/ARCHITECTURE.md for testing architecture
Identify Tools: Jest/Vitest, React Testing Library, Supertest, Playwright/Cypress
Discover Patterns: Review existing test files, utilities, mocking patterns
Use Project-Specific Skills: Check for [project]-testing-expert skill
Core Testing Principles
Testing Pyramid
Unit Tests (70%): Fast, isolated, test individual functions/components
Integration Tests (20%): Test component interactions
E2E Tests (10%): Test full user flows
Coverage Targets
Line coverage: > 80%
Branch coverage: > 75%
Function coverage: > 85%
Critical paths: 100%
Test Organization
src/
  users/
    users.controller.ts
    users.controller.spec.ts  # Unit tests
    users.service.ts
    users.service.spec.ts
  __tests__/
    integration/
    e2e/

Test Quality (AAA Pattern)
it('should return users filtered by organization', async () => {
  // Arrange: Set up test data
  const organizationId = 'org1';
  const expectedUsers = [{ organization: organizationId }];

  // Act: Execute the code being tested
  const result = await service.findAll(organizationId);

  // Assert: Verify the result
  expect(result).toEqual(expectedUsers);
});

Good Tests Are
Independent (no test dependencies)
Fast (< 100ms each)
Repeatable (same result every time)
Meaningful (test real behavior)
Maintainable (easy to update)
Testing Best Practices Summary
Test Isolation: Each test independent, clean up after
Meaningful Tests: Test behavior, not implementation
Mocking Strategy: Mock external dependencies, not what you're testing
Test Data: Use factories, keep data minimal, clean up
Coverage: High coverage, focus on critical paths
Integration
Test Type	Tools	Use Case
Unit	Jest/Vitest	Functions, components, services
Integration	Supertest + Jest	Controller + Service + DB
E2E	Playwright/Cypress	Full user flows
Component	React Testing Library	React component behavior

For complete React Testing Library examples, hook testing, Next.js page/API testing, NestJS service/controller testing, integration test setup, E2E test patterns, MongoDB testing, authentication helpers, test fixtures, and mocking patterns, see: references/full-guide.md

Weekly Installs
111
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass