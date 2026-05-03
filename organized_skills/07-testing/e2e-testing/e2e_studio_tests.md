---
rating: ⭐⭐
title: e2e-studio-tests
url: https://skills.sh/supabase/supabase/e2e-studio-tests
---

# e2e-studio-tests

skills/supabase/supabase/e2e-studio-tests
e2e-studio-tests
Installation
$ npx skills add https://github.com/supabase/supabase --skill e2e-studio-tests
SKILL.md
E2E Studio Tests

Run Playwright end-to-end tests for the Studio application.

Running Tests

Tests must be run from the e2e/studio directory:

cd e2e/studio && pnpm run e2e

Run specific file
cd e2e/studio && pnpm run e2e -- features/cron-jobs.spec.ts

Run with grep filter
cd e2e/studio && pnpm run e2e -- --grep "test name pattern"

UI mode for debugging
cd e2e/studio && pnpm run e2e -- --ui

Environment Setup
Tests auto-start Supabase local containers via web server config
Self-hosted mode (IS_PLATFORM=false) runs tests in parallel (3 workers)
No manual setup needed for self-hosted tests
Test File Structure
Tests are in e2e/studio/features/*.spec.ts
Use custom test utility: import { test } from '../utils/test.js'
Test fixtures provide page, ref, and other helpers
Common Patterns

Wait for elements with generous timeouts:

await expect(locator).toBeVisible({ timeout: 30000 })


Add messages to expects for debugging:

await expect(locator).toBeVisible({ timeout: 30000 }, 'Element should be visible after page load')


Use serial mode for tests sharing database state:

test.describe.configure({ mode: 'serial' })

Writing Robust Selectors
Selector priority (best to worst)

getByRole with accessible name - Most robust, tests accessibility

page.getByRole('button', { name: 'Save' })
page.getByRole('button', { name: 'Configure API privileges' })


getByTestId - Stable, explicit test hooks

page.getByTestId('table-editor-side-panel')


getByText with exact match - Good for unique text

page.getByText('Data API Access', { exact: true })


locator with CSS - Use sparingly, more fragile

page.locator('[data-state="open"]')

Patterns to avoid

XPath selectors - Fragile to DOM changes

// BAD
locator('xpath=ancestor::div[contains(@class, "space-y")]')


Parent traversal with locator('..') - Breaks when structure changes

// BAD
element.locator('..').getByRole('button')


Broad filter({ hasText }) on generic elements - May match multiple elements

// BAD - popover may have more than one combobox
// Could consider scoping down the container or filtering the combobox more specifically
popover.getByRole('combobox')

Add accessible labels to components

When a component lacks a good accessible name, add one in the source code:

// In the React component
<Button aria-label="Configure API privileges">
  <Settings />
</Button>


Then use it in tests:

page.getByRole('button', { name: 'Configure API privileges' })

Narrowing search scope

Scope selectors to specific containers to avoid matching wrong elements:

// Good - scoped to side panel
const sidePanel = page.getByTestId('table-editor-side-panel')
const toggle = sidePanel.getByRole('switch')

// Good - find unique element, then scope from there
const popover = page.locator('[data-radix-popper-content-wrapper]')
const roleSection = popover.getByText('Anonymous (anon)', { exact: true })

Avoiding waitForTimeout

Never use waitForTimeout - always wait for something specific:

// BAD
await page.waitForTimeout(1000)

// GOOD - wait for UI element
await expect(page.getByText('Success')).toBeVisible()

// GOOD - wait for API response
const apiPromise = waitForApiResponse(page, 'pg-meta', ref, 'query?key=table-create')
await saveButton.click()
await apiPromise

// GOOD - wait for toast indicating operation complete
await expect(page.getByText('Table created successfully')).toBeVisible({ timeout: 15000 })

Avoiding force: true on clicks

Instead of forcing clicks on hidden elements, make them visible first:

// BAD
await menuButton.click({ force: true })

// GOOD - hover to reveal, then click
await tableRow.hover()
await expect(menuButton).toBeVisible()
await menuButton.click()

Debugging
View trace
cd e2e/studio && pnpm exec playwright show-trace <path-to-trace.zip>

View HTML report
cd e2e/studio && pnpm exec playwright show-report

Error context

Error context files are saved in the test-results/ directory.

Playwright MCP tools

Use Playwright MCP tools to inspect UI when debugging locally.

CI vs Local Development

The key difference is cold start vs warm state:

CI (cold start)

Tests run from a blank database slate. Each test run resets the database and starts fresh containers. Extensions like pg_cron are NOT enabled by default.

Local dev with pnpm dev:studio-local

When debugging with a running dev server, the database may already have state from previous runs (extensions enabled, test data present).

Handling Cold Start Bugs

Tests that work locally but fail in CI often have assumptions about existing state.

Common issues
Extension not enabled (must enable in test setup)
Race conditions when parallel tests try to modify shared state (use test.describe.configure({ mode: 'serial' }))
Locators matching wrong elements because the page structure differs when state isn't set up
Reproducing CI behavior locally

The test framework automatically resets the database when running pnpm run e2e. This matches CI behavior.

If using pnpm dev:studio-local for Playwright MCP debugging, remember the state differs from CI.

Debugging Workflow for CI Failures
First, run the test locally with pnpm run e2e -- features/<file>.spec.ts (cold start)
Check error context in test-results/ directory
If you need to inspect UI state, start pnpm dev:studio-local and use Playwright MCP tools
Remember: what you see in the dev server may have state that doesn't exist in CI
Weekly Installs
211
Repository
supabase/supabase
GitHub Stars
101.8K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass