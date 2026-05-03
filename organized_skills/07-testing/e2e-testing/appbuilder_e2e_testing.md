---
rating: ⭐⭐
title: appbuilder-e2e-testing
url: https://skills.sh/adobe/skills/appbuilder-e2e-testing
---

# appbuilder-e2e-testing

skills/adobe/skills/appbuilder-e2e-testing
appbuilder-e2e-testing
Installation
$ npx skills add https://github.com/adobe/skills --skill appbuilder-e2e-testing
SKILL.md
App Builder E2E Testing

Playwright-based browser E2E testing for Adobe App Builder SPAs and AEM extensions. This skill generates Playwright configs, test files, and CI workflows for browser-level validation.

Pattern Quick-Reference

Identify the user's intent, then read the referenced sections to generate tailored tests.

User wants	Reference	Asset
E2E test for ExC Shell SPA	references/e2e-testing-patterns.md	assets/playwright.config.ts, assets/e2e-test-template.spec.ts
Test AEM extension in browser	references/aem-extension-testing.md	assets/playwright.config.ts
E2E tests in CI pipeline	references/ci-integration.md	assets/e2e-ci-workflow.yml
Fast Path (for clear requests)

When the user says "add E2E tests" or "write Playwright tests" and intent is clear:

Scan project for web-src/ (SPA) or @adobe/uix-guest in dependencies (AEM extension)
Install Playwright if not present: npm install -D @playwright/test && npx playwright install chromium
Generate playwright.config.ts from assets/playwright.config.ts
For ExC Shell SPA: read references/e2e-testing-patterns.md, generate test with iframe navigation, shell wait, Spectrum ARIA selectors
For AEM extension: read references/aem-extension-testing.md, generate test with Extension Tester URL, nested iframe handling, modal flows
Run tests: npx playwright test
If CI requested: generate GitHub Actions workflow from assets/e2e-ci-workflow.yml
Quick Reference
Test directory: e2e/ at project root (separate from Jest test/)
Config file: playwright.config.ts at project root
Install command: npm install -D @playwright/test && npx playwright install chromium (installs Playwright + Chromium browser)
Run command: npx playwright test (headless) or npx playwright test --headed (visible browser)
Debug command: npx playwright test --debug (step-through mode)
Report command: npx playwright show-report (open HTML report)
ExC Shell iframe: Access SPA inside shell via page.frameLocator('iframe') — exact selector varies, see references/e2e-testing-patterns.md
Spectrum selectors: Use ARIA roles, not CSS classes: getByRole('button', { name: 'Save' }), getByRole('grid'), getByRole('textbox')
Auth note: Full ExC Shell auth automation is complex — recommend testing against aio app dev (local) first. See references/e2e-testing-patterns.md § Authentication.
AEM extensions: Use Extension Tester URL with devMode=true. See references/aem-extension-testing.md.
Full Workflow (for ambiguous or complex requests)
Scan project — Check for web-src/ (SPA), @adobe/uix-guest (AEM extension), existing test setup, app.config.yaml extension type
Confirm scope — Which pages/flows to test? Local dev or deployed? CI needed?
Install Playwright — npm install -D @playwright/test && npx playwright install chromium if not already installed
Generate config — Copy and customize assets/playwright.config.ts for the project
Generate test files — Read appropriate reference doc, generate tests matching project structure:
ExC Shell SPA → references/e2e-testing-patterns.md
AEM extension → references/aem-extension-testing.md
Add action stubbing — If tests need deterministic backend responses, add page.route() intercepts
Run and iterate — npx playwright test, fix selectors/timing as needed
Add CI workflow — If requested, read references/ci-integration.md and generate workflow from assets/e2e-ci-workflow.yml
Validate — All tests pass, use ARIA selectors, have assertions, no hardcoded waits
Inputs To Request
Current repository path and project type (SPA vs AEM extension)
Which pages or user flows need E2E coverage
Whether tests should run against local dev or deployed environment
Whether CI integration is needed
Deliverables
playwright.config.ts configured for the project
E2E test files in e2e/ directory
GitHub Actions workflow (if CI requested)
Passing test run output
Quality Bar
All tests use ARIA selectors (getByRole, getByLabel) — no CSS class selectors
Iframe navigation uses frameLocator() — no frame() with index
All tests have await expect() assertions — no assertion-free tests
Action responses are stubbed with page.route() for deterministic results
No hardcoded page.waitForTimeout() — use waitForSelector, waitForResponse, or Playwright auto-waiting
Tests run in < 60s on local machine
References
Use references/e2e-testing-patterns.md for Playwright E2E patterns for ExC Shell SPAs (iframe nav, Spectrum selectors, auth, action stubbing).
Use references/aem-extension-testing.md for AEM extension testing patterns (Extension Tester, nested iframes, modal lifecycle, extension points).
Use references/ci-integration.md for running Playwright in GitHub Actions (browser install, artifact upload, headless config).
Use assets/playwright.config.ts as the base Playwright configuration template.
Use assets/e2e-ci-workflow.yml as the GitHub Actions workflow template for E2E tests.
Common Issues
Iframe not found: The ExC Shell iframe selector varies — use DevTools to inspect. Try page.frameLocator('iframe[src*="your-app"]') or discover with page.frames().
Shell spinner never dismissed: Ensure runtime.done() is called in the SPA. For E2E, wait for content inside the iframe rather than the shell itself.
Spectrum component not clickable: React Spectrum components render ARIA roles — use getByRole() instead of CSS selectors. Check references/e2e-testing-patterns.md § Spectrum Selectors.
Auth popup blocks test: Test against local dev (aio app dev) which skips shell auth. See auth section in references/e2e-testing-patterns.md.
AEM extension not loading: Extension Tester requires IMS login. Use generous timeouts (10s+) for extension load. Check references/aem-extension-testing.md § Common Gotchas.
Tests flaky in CI: Add retries (retries: 1), use waitForResponse() for action calls, and check references/ci-integration.md for headless configuration.
Chaining
Chains FROM appbuilder-ui-scaffolder (after UI components are generated, add E2E tests)
Chains FROM appbuilder-testing (when user wants browser-level validation beyond Jest unit tests)
Chains TO appbuilder-cicd-pipeline (add E2E test job to CI/CD pipeline)
Weekly Installs
57
Repository
adobe/skills
GitHub Stars
62
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn