---
rating: ⭐⭐
title: e2e testing (frontend)
url: https://skills.sh/exceptionless/exceptionless/e2e-testing-(frontend)
---

# e2e testing (frontend)

skills/exceptionless/exceptionless/E2E Testing (Frontend)
E2E Testing (Frontend)
Installation
$ npx skills add https://github.com/exceptionless/exceptionless --skill 'E2E Testing (Frontend)'
SKILL.md
E2E Testing (Frontend)

Note: E2E test coverage is currently limited. This is an area for improvement.

Running Tests
npx playwright install  # First time only
npm run test:e2e

Page Object Model

Create page objects for reusable page interactions:

// e2e/pages/login-page.ts
import { type Page, type Locator, expect } from '@playwright/test';

export class LoginPage {
    readonly page: Page;
    readonly emailInput: Locator;
    readonly passwordInput: Locator;
    readonly submitButton: Locator;
    readonly errorMessage: Locator;

    constructor(page: Page) {
        this.page = page;
        this.emailInput = page.getByLabel('Email');
        this.passwordInput = page.getByLabel('Password');
        this.submitButton = page.getByRole('button', { name: /log in/i });
        this.errorMessage = page.getByRole('alert');
    }

    async goto() {
        await this.page.goto('/login');
    }

    async login(email: string, password: string) {
        await this.emailInput.fill(email);
        await this.passwordInput.fill(password);
        await this.submitButton.click();
    }

    async expectError(message: string) {
        await expect(this.errorMessage).toContainText(message);
    }
}

Using Page Objects in Tests
// e2e/auth/login.spec.ts
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/login-page';

test.describe('Login', () => {
    test('successful login redirects to dashboard', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.goto();
        await loginPage.login('user@example.com', 'password123');

        await expect(page).toHaveURL('/');
    });

    test('invalid credentials shows error', async ({ page }) => {
        const loginPage = new LoginPage(page);

        await loginPage.goto();
        await loginPage.login('wrong@example.com', 'wrongpassword');

        await loginPage.expectError('Invalid email or password');
    });
});

Selector Priority

Semantic selectors first:

page.getByRole('button', { name: /submit/i });
page.getByLabel('Email address');
page.getByText('Welcome back');


Fallback to test IDs:

page.getByTestId('stack-trace');


Avoid implementation details:

// ❌ Avoid CSS classes and IDs
page.locator('.btn-primary');

Backend Data Setup

E2E tests run against the full Aspire stack. The backend uses the same AppWebHostFactory infrastructure from backend-testing.

For tests requiring specific data, consider:

API calls in beforeEach — Use Playwright's request context to set up data
Test-specific endpoints — Create /api/test/* endpoints for test data management
Database seeding — Seed required data before test runs
Aspire orchestration — Tests start with Elasticsearch and Redis pre-configured
test.beforeEach(async ({ request }) => {
    // Set up test data via API
    await request.post('/api/test/seed', {
        data: { scenario: 'events-with-errors' }
    });
});

test.afterEach(async ({ request }) => {
    await request.delete('/api/test/cleanup');
});


Note: Backend services use in-memory implementations during tests. See AppWebHostFactory for how test infrastructure is configured.

Accessibility Audits
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('login page has no accessibility violations', async ({ page }) => {
    await page.goto('/login');

    const results = await new AxeBuilder({ page }).analyze();
    expect(results.violations).toEqual([]);
});


See accessibility for WCAG guidelines.

Weekly Installs
–
Repository
exceptionless/e…tionless
GitHub Stars
2.5K
First Seen
–