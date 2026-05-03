---
rating: ⭐⭐
title: nestjs-testing-expert
url: https://skills.sh/shipshitdev/library/nestjs-testing-expert
---

# nestjs-testing-expert

skills/shipshitdev/library/nestjs-testing-expert
nestjs-testing-expert
Installation
$ npx skills add https://github.com/shipshitdev/library --skill nestjs-testing-expert
Summary

Jest test patterns and best practices for NestJS unit, integration, and e2e testing.

Covers the testing pyramid: unit tests for pure logic, integration tests with real providers using Test.createTestingModule, and e2e tests with supertest for HTTP APIs
Provides patterns for mocking external services with jest.fn and test doubles, plus in-memory database adapters and test containers for data layer testing
Emphasizes deterministic tests with proper mock reset between runs, avoiding shared mutable state, and following arrange/act/assert structure
Includes a practical checklist covering error path coverage, minimal mocking, and test execution speed
SKILL.md
NestJS Testing Expert

You build reliable Jest test suites for NestJS modules, services, and controllers.

When to Use
Writing unit or integration tests for NestJS
Setting up TestModule, mocking providers, or database fakes
Debugging flaky tests
Testing Pyramid
Unit tests for pure logic and services
Integration tests for modules with real providers
E2E tests for HTTP APIs
Common Patterns
Use Test.createTestingModule with explicit providers.
Mock external services with jest.fn or test doubles.
For DB: use in-memory adapters or test containers when needed.
Prefer supertest for HTTP-level e2e.
Tips
Keep tests deterministic.
Reset mocks between tests.
Avoid shared mutable state.
Checklist
Clear arrange/act/assert structure
Minimal mocking
Covers error paths
Fast to run
Weekly Installs
521
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass