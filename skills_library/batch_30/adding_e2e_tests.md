---
title: adding-e2e-tests
url: https://skills.sh/spencerpauly/awesome-cursor-skills/adding-e2e-tests
---

# adding-e2e-tests

skills/spencerpauly/awesome-cursor-skills/adding-e2e-tests
adding-e2e-tests
Installation
$ npx skills add https://github.com/spencerpauly/awesome-cursor-skills --skill adding-e2e-tests
SKILL.md
Add E2E Tests (Playwright)

Use this skill when the user asks to add end-to-end tests, browser tests, integration tests, or set up Playwright.

Steps

Install Playwright

npm init playwright@latest


This creates playwright.config.ts, a tests/ directory, and installs browsers. If the project already has a test runner, install manually:

npm install -D @playwright/test
npx playwright install


Configure playwright.config.ts

Set baseURL to the local dev server URL (e.g. http://localhost:3000).

Configure webServer to start the dev server automatically:

webServer: {
  command: "npm run dev",
  url: "http://localhost:3000",
  reuseExistingServer: !process.env.CI,
},


Enable only chromium for local dev speed; enable all browsers in CI.

Create a smoke test — write a basic test that verifies the app loads:

import { test, expect } from "@playwright/test";

test("homepage loads", async ({ page }) => {
  await page.goto("/");
  await expect(page).toHaveTitle(/.+/);
});


Add page object pattern (optional) — for larger apps, create a tests/pages/ directory with page objects that encapsulate selectors and actions.

Add npm scripts

{
  "test:e2e": "playwright test",
  "test:e2e:ui": "playwright test --ui"
}


Add to .gitignore

test-results/
playwright-report/
blob-report/


CI integration — add a GitHub Actions step that runs npx playwright install --with-deps then npm run test:e2e. Use the official actions/upload-artifact to save the HTML report on failure.

Notes
Use data-testid attributes for selectors instead of CSS classes.
Use test.describe to group related tests.
Run npx playwright codegen to record tests interactively.
Weekly Installs
18
Repository
spencerpauly/aw…r-skills
GitHub Stars
220
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass