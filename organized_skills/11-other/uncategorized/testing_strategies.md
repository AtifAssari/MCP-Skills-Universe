---
rating: ⭐⭐⭐
title: testing-strategies
url: https://skills.sh/1mangesh1/dev-skills-collection/testing-strategies
---

# testing-strategies

skills/1mangesh1/dev-skills-collection/testing-strategies
testing-strategies
Installation
$ npx skills add https://github.com/1mangesh1/dev-skills-collection --skill testing-strategies
SKILL.md
Testing Strategies and Methodologies
Testing Pyramid
         /  E2E   \          ~5-10% of tests
        / --------- \
       / Integration  \      ~15-25% of tests
      / --------------- \
     /    Unit Tests      \   ~65-80% of tests
    /______________________\


Unit tests form the base. Fast (milliseconds), test a single function or class in isolation. When one fails, it should point to exactly what broke.

Integration tests verify components work together: a service calling a database, two modules interacting, an HTTP handler processing a request through the application. Slower, more setup, but catch issues unit tests cannot.

End-to-end tests simulate real user behavior through the full stack. Slow, expensive to maintain, prone to flakiness. Use sparingly for critical user journeys only.

Inverting the pyramid (many E2E, few unit) leads to slow feedback, flaky CI, and difficult debugging.

Unit Testing Patterns
Arrange-Act-Assert (AAA)
def test_apply_discount_reduces_price_by_percentage():
    # Arrange
    product = Product(name="Widget", price=100.00)
    discount = Discount(percentage=15)
    # Act
    final_price = discount.apply(product)
    # Assert
    assert final_price == 85.00

Given-When-Then

Equivalent to AAA with BDD terminology. Useful when tests map to user stories.

test('registered user with valid credentials receives auth token', () => {
  // Given
  const user = createUser({ email: 'test@example.com', password: 'secure123' });
  // When
  const result = authService.login(user.email, 'secure123');
  // Then
  expect(result.token).toBeDefined();
});


If the test name contains "and", it is likely testing too much.

Mocking Strategies
Types of Test Doubles

Stub: Returns predetermined data. Does not verify how it was called.

Spy: Records calls for later verification. jest.spyOn(logger, 'warn') then assert it was called with expected arguments.

Mock: Pre-programmed with expectations. Fails the test if not called correctly. Created via frameworks like Mockito, unittest.mock, or Jest.

Fake: A working but simplified implementation, such as an in-memory database replacing PostgreSQL.

When to Mock

Mock when the dependency is slow (network, disk I/O), nondeterministic (time, randomness), has side effects (emails, payments), or you need to simulate errors (timeouts, 500s).

Do not mock when the collaborator is a value object, you are testing the integration itself, the mock replicates the dependency's logic, or you are mocking three layers deep.

Over-mocking makes tests pass while the real system is broken. If refactoring breaks twenty mocks, those tests are testing the wrong thing.

Integration Testing
Database Tests

Use a real database, not mocks, for repository and query tests. Roll back transactions after each test or use a fresh schema for isolation.

def test_find_active_users_excludes_deactivated(db_session):
    db_session.add(User(name="Alice", active=True))
    db_session.add(User(name="Bob", active=False))
    db_session.commit()
    result = user_repo.find_active(db_session)
    assert len(result) == 1
    assert result[0].name == "Alice"

Container-Based Testing with Testcontainers

Testcontainers spins up real services (PostgreSQL, Redis, Kafka) in Docker for tests. Available for Java, Python, Node.js, Go, .NET. Eliminates "works on my machine" discrepancies.

API Integration Tests

Test HTTP endpoints with a running server and real or containerized dependencies. Verify both the response and the persisted state.

End-to-End Testing

Test critical user journeys: signup, checkout, payment, core workflows. Do not use E2E for edge cases coverable at lower levels.

Playwright: Multi-browser (Chromium, Firefox, WebKit), multi-language, supports multiple tabs and iframes. Better for cross-browser and complex scenarios.

Cypress: JavaScript only, primarily Chromium-based. Strong DX with time-travel debugging. Better for JS-only teams with simpler needs.

test('user completes purchase', async ({ page }) => {
  await page.goto('/products');
  await page.click('[data-testid="product-add-to-cart"]');
  await page.click('[data-testid="cart-checkout"]');
  await page.fill('[data-testid="card-number"]', '4242424242424242');
  await page.click('[data-testid="place-order"]');
  await expect(page.locator('[data-testid="order-confirmation"]')).toBeVisible();
});


Use data-testid attributes for selectors. Never select by CSS classes or DOM structure.

Test-Driven Development
Red-Green-Refactor
Red: Write a failing test for the next small piece of behavior.
Green: Write the minimum code to pass. No more.
Refactor: Clean up while keeping tests green.
Practical Workflow

Pick the simplest behavior first. Write one test. Run it, confirm it fails for the right reason. Write just enough code. Confirm it passes. Refactor if needed. Repeat.

TDD works best when you resist writing more production code than the current test demands. The discipline is in the small steps.

Property-Based Testing

Generates hundreds of random inputs and checks that invariants hold for all of them.

What it catches that examples miss: off-by-one errors at unexpected boundaries, Unicode handling failures, integer overflow, rare input combinations humans would not think to test.

from hypothesis import given
from hypothesis.strategies import lists, integers

@given(lists(integers()))
def test_sort_preserves_length(xs):
    assert len(sorted(xs)) == len(xs)

@given(lists(integers()))
def test_sort_output_is_ordered(xs):
    result = sorted(xs)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]


In JavaScript, use fast-check for the same approach. Property-based tests complement example-based tests. Use them for pure functions, serialization roundtrips, data transformations, and functions with well-defined invariants.

Snapshot Testing

When useful: Catching unintended changes to serialized output (HTML, JSON, CLI output), guarding generated code against accidental changes.

When harmful: Large snapshots no one reviews, tests that break on every intentional change leading to blind --update usage, snapshots of volatile data (timestamps, random IDs).

Keep snapshots small. If longer than 30-40 lines, assert on specific fields instead.

Test Coverage
Meaningful Coverage vs Vanity Metrics

Line coverage measures execution, not verification. 100% coverage with no assertions proves nothing.

Focus on branch coverage (both sides of conditionals), behavior coverage (every documented behavior verified), and critical path coverage (error handling tested). 80% line coverage is a reasonable floor. Chasing 100% creates low-value tests for trivial code.

Mutation Testing

Modifies production code (changes > to >=, removes lines, swaps booleans) and checks whether tests fail. Surviving mutants indicate undertested code.

Tools: Stryker (JS/TS), PIT (Java), mutmut (Python), cargo-mutants (Rust).

A high mutation score is a stronger quality signal than high line coverage.

API Testing
Contract Testing with Pact

Verifies consumer and provider agree on an API's shape without both services running simultaneously. The consumer generates a contract file; the provider verifies it independently. This decouples service testing in microservice architectures.

Schema Validation

Validate responses against OpenAPI/JSON Schema definitions in tests. This catches drift between documentation and actual behavior.

from jsonschema import validate

def test_users_endpoint_matches_schema(client, user_schema):
    response = client.get('/api/users')
    for user in response.json():
        validate(instance=user, schema=user_schema)

Performance Testing
Load Testing with k6
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 100 },  // ramp up
    { duration: '5m', target: 100 },  // hold
    { duration: '2m', target: 0 },    // ramp down
  ],
};

export default function () {
  const res = http.get('https://api.example.com/products');
  check(res, { 'status is 200': (r) => r.status === 200 });
  sleep(1);
}


Measure response time percentiles (p50, p95, p99) -- not averages. Track throughput, error rate under load, and resource consumption. k6 is scriptable and CI-friendly. Artillery is YAML-configured for quick HTTP/WebSocket load tests.

Testing in CI/CD
Parallel Execution

Split tests across runners using jest --shard, pytest-split, or CI-native parallelism (GitHub Actions matrix, CircleCI). Distribute by timing data to prevent one slow shard from bottlenecking.

Flaky Test Management

Flaky tests erode trust. Quarantine them into non-blocking jobs. Track flake rates (BuildPulse, Datadog Test Visibility). Fix or delete within a defined SLA. Never use retry-and-ignore as a permanent solution.

Test Naming Conventions

Test names should read as behavior specifications.

# [unit]_[scenario]_[expected result]
test_parse_date_with_invalid_format_raises_value_error
test_calculate_shipping_for_oversized_item_applies_surcharge

# should [behavior] when [condition]
should return empty list when no results match
should throw AuthError when token is expired

# given [context] when [action] then [outcome]
given_premium_user_when_applying_coupon_then_discount_is_doubled


The name should tell you what failed without reading the test body.

Test Data Management

Factories generate objects with sensible defaults, allowing override of specific fields. Use factory_boy (Python), FactoryBot (Ruby), or Fishery (TypeScript).

Builders give fine-grained control for complex objects via chained method calls (new OrderBuilder().withCustomer("Alice").withItem("Widget", 2).build()).

Fixtures provide shared setup data. Keep them minimal -- large shared fixtures create hidden coupling. Prefer factories over fixtures; they make each test self-describing and independent.

Anti-Patterns

Testing implementation details: Asserting on internal state, private methods, or exact SQL. Breaks on refactoring without behavior changes.

Brittle selectors: .btn-primary or div > span:nth-child(3) in E2E tests. Use data-testid.

Slow suites: A 30-minute suite will not be run before pushing. Keep unit tests under 5 minutes. Parallelize the rest.

Mocking everything: Tests only verify mock wiring, not real behavior.

Shared mutable state: Tests pass alone but fail together. Each test must set up and tear down its own state.

Ignoring maintenance: Dead tests, commented-out tests, misleading names. Treat test code with production rigor.

What NOT to Test

Trivial code: Getters, setters, constructors with no logic.

Framework internals: ORM SQL generation, router dispatch, React rendering. Framework maintainers test these.

Third-party libraries: Do not verify that JSON.parse or lodash.groupBy works. Test your code that uses them.

Constants: Testing MAX_RETRIES = 3 equals 3 adds nothing. Test the behavior that uses it.

Every test should justify its existence by catching a real class of bugs. Tests that cannot fail, or fail only on harmless refactoring, are noise.

Weekly Installs
10
Repository
1mangesh1/dev-s…llection
GitHub Stars
3
First Seen
Feb 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass