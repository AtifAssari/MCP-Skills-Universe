---
rating: ⭐⭐
title: tdd-workflows-tdd-red
url: https://skills.sh/sickn33/antigravity-awesome-skills/tdd-workflows-tdd-red
---

# tdd-workflows-tdd-red

skills/sickn33/antigravity-awesome-skills/tdd-workflows-tdd-red
tdd-workflows-tdd-red
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill tdd-workflows-tdd-red
SKILL.md

Write comprehensive failing tests following TDD red phase principles.

[Extended thinking: Generates failing tests that properly define expected behavior using test-automator agent.]

Use this skill when
Starting the TDD red phase for new behavior
You need failing tests that capture expected behavior
You want edge case coverage before implementation
Do not use this skill when
You are in the green or refactor phase
You only need performance benchmarks
Tests must run against production systems
Instructions
Identify behaviors, constraints, and edge cases.
Generate failing tests that define expected outcomes.
Ensure failures are due to missing behavior, not setup errors.
Document how to run tests and verify failures.
Safety
Keep test data isolated and avoid production environments.
Avoid flaky external dependencies in the red phase.
Role

Generate failing tests using Task tool with subagent_type="unit-testing::test-automator".

Prompt Template

"Generate comprehensive FAILING tests for: $ARGUMENTS

Core Requirements

Test Structure

Framework-appropriate setup (Jest/pytest/JUnit/Go/RSpec)
Arrange-Act-Assert pattern
should_X_when_Y naming convention
Isolated fixtures with no interdependencies

Behavior Coverage

Happy path scenarios
Edge cases (empty, null, boundary values)
Error handling and exceptions
Concurrent access (if applicable)

Failure Verification

Tests MUST fail when run
Failures for RIGHT reasons (not syntax/import errors)
Meaningful diagnostic error messages
No cascading failures

Test Categories

Unit: Isolated component behavior
Integration: Component interaction
Contract: API/interface contracts
Property: Mathematical invariants
Framework Patterns

JavaScript/TypeScript (Jest/Vitest)

Mock dependencies with vi.fn() or jest.fn()
Use @testing-library for React components
Property tests with fast-check

Python (pytest)

Fixtures with appropriate scopes
Parametrize for multiple test cases
Hypothesis for property-based tests

Go

Table-driven tests with subtests
t.Parallel() for parallel execution
Use testify/assert for cleaner assertions

Ruby (RSpec)

let for lazy loading, let! for eager
Contexts for different scenarios
Shared examples for common behavior
Quality Checklist
Readable test names documenting intent
One behavior per test
No implementation leakage
Meaningful test data (not 'foo'/'bar')
Tests serve as living documentation
Anti-Patterns to Avoid
Tests passing immediately
Testing implementation vs behavior
Complex setup code
Multiple responsibilities per test
Brittle tests tied to specifics
Edge Case Categories
Null/Empty: undefined, null, empty string/array/object
Boundaries: min/max values, single element, capacity limits
Special Cases: Unicode, whitespace, special characters
State: Invalid transitions, concurrent modifications
Errors: Network failures, timeouts, permissions
Output Requirements
Complete test files with imports
Documentation of test purpose
Commands to run and verify failures
Metrics: test count, coverage areas
Next steps for green phase"
Validation

After generation:

Run tests - confirm they fail
Verify helpful failure messages
Check test independence
Ensure comprehensive coverage
Example (Minimal)
// auth.service.test.ts
describe('AuthService', () => {
  let authService: AuthService;
  let mockUserRepo: jest.Mocked<UserRepository>;

  beforeEach(() => {
    mockUserRepo = { findByEmail: jest.fn() } as any;
    authService = new AuthService(mockUserRepo);
  });

  it('should_return_token_when_valid_credentials', async () => {
    const user = { id: '1', email: 'test@example.com', passwordHash: 'hashed' };
    mockUserRepo.findByEmail.mockResolvedValue(user);

    const result = await authService.authenticate('test@example.com', 'pass');

    expect(result.success).toBe(true);
    expect(result.token).toBeDefined();
  });

  it('should_fail_when_user_not_found', async () => {
    mockUserRepo.findByEmail.mockResolvedValue(null);

    const result = await authService.authenticate('none@example.com', 'pass');

    expect(result.success).toBe(false);
    expect(result.error).toBe('INVALID_CREDENTIALS');
  });
});


Test requirements: $ARGUMENTS

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
223
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass