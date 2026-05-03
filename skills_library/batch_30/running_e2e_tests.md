---
title: running-e2e-tests
url: https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/running-e2e-tests
---

# running-e2e-tests

skills/jeremylongshore/claude-code-plugins-plus-skills/running-e2e-tests
running-e2e-tests
Installation
$ npx skills add https://github.com/jeremylongshore/claude-code-plugins-plus-skills --skill running-e2e-tests
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

E2E Test Framework
Current State

!cat package.json 2>/dev/null | grep -oE 'playwright|cypress|selenium' || echo 'No E2E framework detected'

Overview

Execute end-to-end tests that simulate real user workflows across the full application stack -- browser interactions, API calls, database operations, and third-party integrations. Supports Playwright (recommended), Cypress, Selenium, and Puppeteer.

Prerequisites
E2E testing framework installed (Playwright, Cypress, or Selenium WebDriver)
Application running in a test environment with seeded test data
Browser binaries installed (npx playwright install or Cypress binary)
Test user accounts created with known credentials
Environment variables configured for base URL, API keys, and test credentials
Instructions
Identify critical user journeys to cover:
User registration and login flow.
Primary feature workflow (e.g., create item, edit, delete).
Search and filtering functionality.
Checkout or payment flow (if applicable).
Error handling (404 pages, form validation, session expiry).
Create page object models (POM) for reusable page interactions:
One class per page or major component.
Encapsulate locators, actions (click, fill, select), and assertions.
Use data-testid attributes as primary selectors for stability.
Write E2E test files organized by user journey:
Each test file covers one complete workflow.
Use beforeEach to navigate to the starting page and reset state.
Use afterEach to capture screenshots on failure.
Keep tests independent -- no test should depend on another test's output.
Handle authentication efficiently:
Store authenticated session state to a file (storageState in Playwright).
Reuse session across tests that require login.
Create a separate auth setup fixture that runs once per worker.
Configure multi-browser and responsive testing:
Run tests on Chromium, Firefox, and WebKit.
Test at mobile (375px), tablet (768px), and desktop (1280px) viewports.
Use Playwright projects to define browser/viewport combinations.
Add retry and stability mechanisms:
Use expect with auto-waiting locators (Playwright) instead of explicit waits.
Configure test retries (max 2) for CI environments.
Add networkidle or domcontentloaded wait conditions for page transitions.
Generate test reports with screenshots, traces, and video on failure.
Output
E2E test files organized by user journey in tests/e2e/ or e2e/
Page object model classes in tests/e2e/pages/
Playwright/Cypress configuration file with browser and viewport matrix
Authentication state file for session reuse
HTML test report with screenshots, traces, and failure details
Error Handling
Error	Cause	Solution
Element not found / timeout	Selector changed or element lazy-loaded after timeout	Use data-testid attributes; increase timeout; use waitFor with proper state checks
Test passes locally but fails in CI	Headless browser behavior differs or CI is slower	Run CI in headless mode locally to reproduce; increase timeouts; check viewport size
Authentication state expired	Stored session tokens have short TTL	Regenerate auth state before each test run; use long-lived test account tokens
Flaky test due to animation	Click registered before animation completes	Disable CSS animations in test config; use force: true on click; add waitForLoadState
Database state pollution	Previous test left data that affects current test	Seed database in beforeEach; use transactional rollback; reset via API endpoint
Examples

Playwright test for user registration flow:

import { test, expect } from '@playwright/test';

test('new user can register and see dashboard', async ({ page }) => {
  await page.goto('/register');
  await page.getByTestId('name-input').fill('Test User');
  await page.getByTestId('email-input').fill('test@example.com');
  await page.getByTestId('password-input').fill('SecurePass123!');
  await page.getByTestId('register-button').click();

  await expect(page).toHaveURL(/\/dashboard/);
  await expect(page.getByTestId('welcome-message')).toContainText('Test User');
});


Page object model:

export class LoginPage {
  constructor(private page: Page) {}
  async login(email: string, password: string) {
    await this.page.goto('/login');
    await this.page.getByTestId('email').fill(email);
    await this.page.getByTestId('password').fill(password);
    await this.page.getByTestId('submit').click();
    await this.page.waitForURL(/\/dashboard/);
  }
}


Playwright config with multi-browser projects:

export default defineConfig({
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'mobile', use: { ...devices['iPhone 14'] } },
  ],
  use: { screenshot: 'only-on-failure', trace: 'on-first-retry' },
});

Resources
Playwright documentation: https://playwright.dev/docs/intro
Cypress documentation: https://docs.cypress.io/
Page Object Model pattern: https://playwright.dev/docs/pom
Playwright best practices: https://playwright.dev/docs/best-practices
E2E testing strategies: https://martinfowler.com/bliki/TestPyramid.html
Weekly Installs
28
Repository
jeremylongshore…s-skills
GitHub Stars
2.1K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass