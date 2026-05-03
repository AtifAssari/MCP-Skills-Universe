---
rating: ⭐⭐⭐
title: test-quality-analysis
url: https://skills.sh/secondsky/claude-skills/test-quality-analysis
---

# test-quality-analysis

skills/secondsky/claude-skills/test-quality-analysis
test-quality-analysis
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill test-quality-analysis
SKILL.md
Test Quality Analysis

Expert knowledge for analyzing and improving test quality - detecting test smells, overmocking, insufficient coverage, and testing anti-patterns.

Core Dimensions
Correctness: Tests verify the right behavior
Reliability: Tests are deterministic, not flaky
Maintainability: Tests are easy to understand
Performance: Tests run quickly
Coverage: Tests cover critical code paths
Isolation: Tests don't depend on external state
Test Smells
Overmocking

Problem: Mocking too many dependencies makes tests fragile.

// ❌ BAD: Overmocked
test('calculate total', () => {
  const mockAdd = vi.fn(() => 10)
  const mockMultiply = vi.fn(() => 20)
  // Testing implementation, not behavior
})

// ✅ GOOD: Mock only external dependencies
test('calculate order total', () => {
  const mockPricingAPI = vi.fn(() => ({ tax: 0.1 }))
  const total = calculateTotal(order, mockPricingAPI)
  expect(total).toBe(38)
})


Detection: More than 3-4 mocks, mocking pure functions, complex mock setup.

Fix: Mock only I/O boundaries (APIs, databases, filesystem).

Fragile Tests

Problem: Tests break with unrelated code changes.

// ❌ BAD: Tests implementation details
await page.locator('.form-container > div:nth-child(2) > button').click()

// ✅ GOOD: Semantic selector
await page.getByRole('button', { name: 'Submit' }).click()

Flaky Tests

Problem: Tests pass or fail non-deterministically.

// ❌ BAD: Race condition
test('loads data', async () => {
  fetchData()
  await new Promise(resolve => setTimeout(resolve, 1000))
  expect(data).toBeDefined()
})

// ✅ GOOD: Proper async handling
test('loads data', async () => {
  const data = await fetchData()
  expect(data).toBeDefined()
})

Poor Assertions
// ❌ BAD: Weak assertion
test('returns users', async () => {
  const users = await getUsers()
  expect(users).toBeDefined() // Too vague!
})

// ✅ GOOD: Strong, specific assertions
test('creates user with correct attributes', async () => {
  const user = await createUser({ name: 'John' })
  expect(user).toMatchObject({
    id: expect.any(Number),
    name: 'John',
  })
})

Analysis Tools
# Vitest coverage (prefer bun)
bun test --coverage
open coverage/index.html

# Check thresholds
bun test --coverage --coverage.thresholds.lines=80

# pytest-cov (Python)
uv run pytest --cov --cov-report=html
open htmlcov/index.html

Best Practices Checklist
Unit Test Quality (FIRST)
 Fast: Tests run in milliseconds
 Isolated: No dependencies between tests
 Repeatable: Same results every time
 Self-validating: Clear pass/fail
 Timely: Written alongside code
Mock Guidelines
 Mock only external dependencies
 Don't mock business logic or pure functions
 Use real implementations when possible
 Limit to 3-4 mocks per test maximum
Coverage Goals
 80%+ line coverage for business logic
 100% for critical paths (auth, payment)
 All error paths tested
 Boundary conditions tested
Test Structure (AAA Pattern)
test('user registration', async () => {
  // Arrange
  const userData = { email: 'user@example.com' }

  // Act
  const user = await registerUser(userData)

  // Assert
  expect(user.email).toBe('user@example.com')
})

Code Review Checklist
 Tests verify behavior, not implementation
 Assertions are specific and meaningful
 No flaky tests (timing, ordering issues)
 Proper async/await usage
 Test names clearly describe behavior
 Minimal code duplication
 Critical paths have tests
 Both happy path and error cases covered
Common Anti-Patterns
Testing Implementation Details
// ❌ BAD
const spy = vi.spyOn(Math, 'sqrt')
calculateDistance()
expect(spy).toHaveBeenCalled() // Testing how, not what

// ✅ GOOD
const distance = calculateDistance({ x: 0, y: 0 }, { x: 3, y: 4 })
expect(distance).toBe(5) // Testing output

Mocking Too Much
// ❌ BAD
const mockAdd = vi.fn((a, b) => a + b)

// ✅ GOOD: Use real implementations
import { add } from './utils'
// Only mock external services
const mockPaymentGateway = vi.fn()

See Also
vitest-testing - TypeScript/JavaScript testing
playwright-testing - E2E testing
mutation-testing - Validate test effectiveness
Weekly Installs
177
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass