---
rating: ⭐⭐⭐
title: positron-e2e-tests
url: https://skills.sh/posit-dev/positron/positron-e2e-tests
---

# positron-e2e-tests

skills/posit-dev/positron/positron-e2e-tests
positron-e2e-tests
Installation
$ npx skills add https://github.com/posit-dev/positron --skill positron-e2e-tests
SKILL.md
Positron Playwright E2E Testing
Purpose

Provides specialized knowledge and patterns for writing correct, reliable Playwright e2e tests that follow Positron's established conventions and avoid common mistakes.

When to Use This Skill

Load this skill when:

Creating new e2e test files
Adding test cases to existing test files
Debugging flaky or failing tests
Understanding the test fixture system
Working with page objects
Choosing correct selectors and assertions
Critical: Test File Structure

Every test file MUST follow this structure:

import { test, expect, tags } from '../_test.setup';

// REQUIRED: Each test file needs a unique suiteId
test.use({
	suiteId: __filename
});

test.describe('Feature Name', {
	tag: [tags.WEB, tags.WIN, tags.CRITICAL, tags.FEATURE_TAG]
}, () => {

	test.beforeEach(async function ({ app }) {
		// Optional setup for each test
	});

	test.afterEach(async function ({ app, hotKeys }) {
		// Cleanup after each test
		await hotKeys.closeAllEditors();
	});

	test('Test description', async function ({ app, python }) {
		// Test implementation
	});
});


MANDATORY REQUIREMENTS:

Import from ../_test.setup - NOT from @playwright/test
Set suiteId: __filename - Required for app isolation
Use function syntax for tests (not arrow functions) - Required for fixtures
Add appropriate tags for platform filtering
Quick Reference: Available Fixtures
Fixture	Use Case
app	Access workbench page objects: app.workbench.console, etc.
page	Direct Playwright page access: page.getByLabel(...)
python	Auto-start Python interpreter before test
r	Auto-start R interpreter before test
sessions	Manual session management: await sessions.start('python')
executeCode	Execute code: await executeCode('Python', 'print("hi")');
openFile	Open file: await openFile('workspaces/test/file.py');
hotKeys	Keyboard shortcuts: await hotKeys.closeAllEditors();
settings	Change settings: await settings.set({ 'key': value });

See references/fixtures.md for complete fixture documentation.

Quick Reference: Page Objects

Access via app.workbench.*:

const { console, variables, dataExplorer, plots, notebooks, sessions } = app.workbench;

// Execute code
await console.executeCode('Python', 'x = 1');

// Wait for content
await console.waitForConsoleContents('expected text');

// Variable interaction
await variables.doubleClickVariableRow('df');

// Data explorer
await dataExplorer.grid.verifyTableData([{ col: 'value' }]);


See references/page-objects.md for complete page object documentation.

Quick Reference: Assertions
// Visibility with timeout
await expect(locator).toBeVisible({ timeout: 30000 });

// Text content
await expect(locator).toHaveText('expected');
await expect(locator).toContainText('partial');

// Count
await expect(locator).toHaveCount(3, { timeout: 15000 });

// Retry pattern for flaky operations
await expect(async () => {
	await someAction();
	await expect(resultLocator).toBeVisible();
}).toPass({ timeout: 15000 });


See references/assertions.md for complete assertion patterns.

Quick Reference: Test Tags

Feature tags (what the test covers):

tags.CONSOLE, tags.DATA_EXPLORER, tags.NOTEBOOKS, tags.PLOTS, tags.VARIABLES
tags.CRITICAL - High priority tests

Platform tags (where the test runs):

tags.WEB - Enable web browser testing
tags.WIN - Enable Windows testing
Default: Linux/Electron only
test.describe('Console Tests', {
	tag: [tags.WEB, tags.WIN, tags.CRITICAL, tags.CONSOLE]
}, () => { ... });

Common Mistakes to Avoid

Critical (will break tests):

Wrong imports - use ../_test.setup, not @playwright/test
Missing suiteId - must have test.use({ suiteId: __filename })
Arrow functions - use function syntax, not async ({ app }) =>
Missing platform tags - add tags.WEB, tags.WIN for cross-platform

Quality issues: 5. No timeout on assertions - use { timeout: 30000 } for async operations 6. No test.step() - wrap complex multi-action sequences for better reports

See references/common-mistakes.md for 26 detailed gotchas with code examples.

Running Tests
# Run specific test file
npx playwright test <test-name>.test.ts --project e2e-electron

# Run all tests in a category
npx playwright test test/e2e/tests/<category>/

# Run with specific tags
npx playwright test --grep @:critical

# Run in headed mode (see browser)
npx playwright test --headed

# Run with debug mode
npx playwright test --debug

# Show test report
npx playwright show-report

Progressive Documentation

For detailed information, read the bundled reference docs:

references/test-structure.md - Complete test file structure and organization
references/fixtures.md - All available fixtures and their usage
references/page-objects.md - Page object patterns and available POMs
references/assertions.md - Assertion patterns and waiting strategies
references/common-mistakes.md - Comprehensive list of gotchas to avoid
Key Architecture Principles
Worker-scoped app - One app instance per test file (suite)
Test-scoped fixtures - page, sessions, etc. fresh per test
Page Object Model - UI interactions wrapped in POMs via app.workbench.*
Tag-based filtering - Tests tagged for platform and feature filtering
Automatic cleanup - Tracing, screenshots attached on failure
Getting Help
Look at existing tests in test/e2e/tests/<feature>/ for patterns
Check page object source in test/e2e/pages/ for available methods
Read test/e2e/tests/_test.setup.ts for fixture definitions
Use --debug flag to step through tests interactively
Weekly Installs
20
Repository
posit-dev/positron
GitHub Stars
4.0K
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass