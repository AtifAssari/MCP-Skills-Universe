---
title: e2e-playwright
url: https://skills.sh/7spade/black-tortoise/e2e-playwright
---

# e2e-playwright

skills/7spade/black-tortoise/e2e-playwright
e2e-playwright
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill e2e-playwright
SKILL.md
Playwright E2E Testing Skill
🎯 Purpose

Provide patterns for robust end-to-end testing in the Black-Tortoise ecosystem, ensuring that user journeys and architectural boundaries are verified.

🛠️ Core Patterns
1. Test Organization
Base URL: Defined in playwright.config.ts.
Naming: .spec.ts files under e2e/.
Parallelism: Tests should be independent to allow parallel execution.
2. Firebase Emulator Integration

Tests should run against local emulators to ensure speed and isolation.

// e2e/auth.spec.ts
import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  // Reset emulator state or seed data via GQL mutations
  await page.goto('/');
});

test('should login successfully', async ({ page }) => {
  await page.getByLabel('Email').fill('test@example.com');
  await page.getByLabel('Password').fill('password123');
  await page.getByRole('button', { name: 'Login' }).click();
  
  await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
});

3. Architecture Guard Verification

Verification of the architecture:gate can be automated as part of the test suite or CI.

// Example of checking for console errors or network violations
test('should not have console errors', async ({ page }) => {
  const logs: string[] = [];
  page.on('console', msg => {
    if (msg.type() === 'error') logs.push(msg.text());
  });
  
  await page.goto('/workspace');
  expect(logs.length).toBe(0);
});

4. Custom Selectors (MANDATORY)
REQUIRED: Use data-testid for stable selection of components.
REQUIRED: Prefer ARIA roles (getByRole, getByLabel) to ensure a11y.
FORBIDDEN: Selecting by brittle CSS classes or deep DOM structures.
🚀 Execution Commands
Run all: pnpm e2e
UI Mode: pnpm exec playwright test --ui
Debug: pnpm exec playwright test --debug
🔐 Architecture Gate (dependency-cruiser)

Black-Tortoise uses dependency-cruiser to enforce DDD boundaries.

Rule: Presentation cannot import Domain directly.
Rule: Application cannot import Infrastructure.
Check: pnpm run architecture:gate should be part of the pre-commit hook (Husky).
Weekly Installs
9
Repository
7spade/black-tortoise
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass