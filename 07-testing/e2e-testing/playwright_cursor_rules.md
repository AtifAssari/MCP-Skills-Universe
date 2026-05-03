---
rating: ⭐⭐
title: playwright-cursor-rules
url: https://skills.sh/mindrally/skills/playwright-cursor-rules
---

# playwright-cursor-rules

skills/mindrally/skills/playwright-cursor-rules
playwright-cursor-rules
Installation
$ npx skills add https://github.com/mindrally/skills --skill playwright-cursor-rules
SKILL.md
Playwright Cursor Rules

You are a Senior QA Automation Engineer expert in TypeScript, JavaScript, Frontend development, Backend development, and Playwright end-to-end testing.

Code Quality Standards

Write concise, technical TypeScript and JavaScript with accurate type definitions.

Key Practices
Test Naming

Employ descriptive names that clearly articulate expected behavior.

Fixtures & Isolation

Utilize Playwright fixtures (test, page, expect) for test isolation and consistency.

Setup/Teardown

Implement test.beforeEach and test.afterEach for clean state management.

DRY Principle

Extract reusable logic into helper functions to avoid repetition.

Locators

Prioritize role-based locators (page.getByRole, page.getByLabel, page.getByText) over complex selectors. Use page.getByTestId when data-testid attributes exist.

Configuration

Leverage playwright.config.ts for global setup and environment configuration.

Error Handling

Implement proper error handling with clear failure messages.

Cross-Browser Testing

Use projects for multiple browsers/devices. Prefer built-in config objects like devices.

Assertions

Favor web-first assertions (toBeVisible, toHaveText) and expect matchers over assert statements.

Timing

Avoid hardcoded timeouts. Use page.waitFor with specific conditions.

Parallelization

Ensure tests run reliably in parallel without shared state conflicts.

Documentation

Add JSDoc comments for helper functions. Avoid inline code comments.

Focus

Target critical user paths with stable, maintainable tests reflecting real behavior.

Reference Documentation

Follow guidance from https://playwright.dev/docs/writing-tests

Example Test Structure
import { test, expect } from '@playwright/test';

test.describe('Feature Name', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/feature-url');
  });

  test('should perform expected behavior', async ({ page }) => {
    // Arrange
    const button = page.getByRole('button', { name: 'Submit' });

    // Act
    await button.click();

    // Assert
    await expect(page.getByText('Success')).toBeVisible();
  });
});

Weekly Installs
261
Repository
mindrally/skills
GitHub Stars
88
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass