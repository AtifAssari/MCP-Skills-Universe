---
title: frontend-testing-best-practices
url: https://skills.sh/sergiodxa/agent-skills/frontend-testing-best-practices
---

# frontend-testing-best-practices

skills/sergiodxa/agent-skills/frontend-testing-best-practices
frontend-testing-best-practices
Installation
$ npx skills add https://github.com/sergiodxa/agent-skills --skill frontend-testing-best-practices
Summary

End-to-end testing focused on real user behavior, minimal mocking, and avoiding component unit tests.

Prioritizes E2E tests over unit tests; reserves unit tests for pure functions only
Emphasizes accessible selectors (role-based, label-based) over CSS selectors and test IDs in E2E tests
Recommends writing E2E tests instead of heavily mocked unit tests; suggests 3+ mocks as a signal to switch approaches
Includes rules for test structure, selector strategy, and when to apply each testing pattern
SKILL.md
Testing Best Practices

Guidelines for writing effective, maintainable tests that provide real confidence. Contains 6 rules focused on preferring E2E tests, minimizing mocking, and testing behavior over implementation.

Core Philosophy
Prefer E2E tests over unit tests - Test the whole system, not isolated pieces
Minimize mocking - If you need complex mocks, write an E2E test instead
Test behavior, not implementation - Test what users see and do
Avoid testing React components directly - Test them through E2E
When to Apply

Reference these guidelines when:

Deciding what type of test to write
Writing new E2E or unit tests
Reviewing test code
Refactoring tests
Rules Summary
Testing Strategy (CRITICAL)
prefer-e2e-tests - @rules/prefer-e2e-tests.md

Default to E2E tests. Only write unit tests for pure functions.

// E2E test (PREFERRED) - tests real user flow
test("user can place an order", async ({ page }) => {
  await createTestingAccount(page, { account_status: "active" });
  await page.goto("/catalog");
  await page.getByRole("heading", { name: "Example Item" }).click();
  await page.getByRole("link", { name: "Buy" }).click();
  // ... complete flow
  await expect(page.getByAltText("Thank you")).toBeVisible();
});

// Unit test - ONLY for pure functions
test("formatCurrency formats with two decimals", () => {
  expect(formatCurrency(1234.5)).toBe("$1,234.50");
});

avoid-component-tests - @rules/avoid-component-tests.md

Don't unit test React components. Test them through E2E or not at all.

// BAD: Component unit test
describe("OrderCard", () => {
  test("renders amount", () => {
    render(<OrderCard amount={100} />);
    expect(screen.getByText("$100")).toBeInTheDocument();
  });
});

// GOOD: E2E test covers the component naturally
test("order history shows orders", async ({ page }) => {
  await page.goto("/orders");
  await expect(page.getByText("$100")).toBeVisible();
});

minimize-mocking - @rules/minimize-mocking.md

Keep mocks simple. If you need 3+ mocks, write an E2E test instead.

// BAD: Too many mocks = write E2E test
vi.mock("~/lib/auth");
vi.mock("~/lib/transactions");
vi.mock("~/hooks/useAccount");

// GOOD: Simple MSW mock for loader test
mockServer.use(
  http.get("/api/user", () => HttpResponse.json({ name: "John" })),
);

E2E Tests (HIGH)
e2e-test-structure - @rules/e2e-test-structure.md

E2E tests go in e2e/tests/, not frontend/.

// e2e/tests/order.spec.ts
import { test, expect } from "@playwright/test";
import { addAccountBalance, createTestingAccount } from "./utils";

test.describe("Orders", () => {
  test.beforeEach(async ({ page, context }) => {
    await createTestingAccount(page, { account_status: "active" });
    let cookies = await context.cookies();
    let account_id = cookies.find((c) => c.name === "account_id").value;
    await addAccountBalance({ account_id, amount: 10000, replaceBalance: true });
  });

  test("place order with default values", async ({ page }) => {
    await page.goto("/catalog");
    // ... user flow
  });
});

e2e-selectors - @rules/e2e-selectors.md

Use accessible selectors: role > label > text > testid.

// GOOD: Role-based (preferred)
await page.getByRole("button", { name: "Submit" }).click();
await page.getByRole("heading", { name: "Dashboard" });

// GOOD: Label-based
await page.getByLabel("Email").fill("test@example.com");

// OK: Test ID when no accessible selector exists
await expect(page.getByTestId("balance")).toHaveText("$1,234");

// BAD: CSS selectors
await page.locator(".btn-primary").click();

Unit Tests (MEDIUM)
unit-test-structure - @rules/unit-test-structure.md

Unit tests for pure functions only. Co-locate with source files.

// app/utils/format.test.ts
import { describe, test, expect } from "vitest";
import { formatCurrency } from "./format";

describe("formatCurrency", () => {
  test("formats positive amounts", () => {
    expect(formatCurrency(1234.5)).toBe("$1,234.50");
  });

  test("handles zero", () => {
    expect(formatCurrency(0)).toBe("$0.00");
  });
});

Key Files
e2e/tests/ - E2E tests (Playwright)
e2e/tests/utils.ts - E2E test utilities
vitest.config.ts - Unit test configuration
vitest.setup.ts - Global test setup with MSW
app/utils/test-utils.ts - Unit test utilities
Weekly Installs
1.6K
Repository
sergiodxa/agent-skills
GitHub Stars
83
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass