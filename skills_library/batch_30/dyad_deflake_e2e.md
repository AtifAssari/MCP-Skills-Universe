---
title: dyad:deflake-e2e
url: https://skills.sh/dyad-sh/dyad/dyad:deflake-e2e
---

# dyad:deflake-e2e

skills/dyad-sh/dyad/dyad:deflake-e2e
dyad:deflake-e2e
Installation
$ npx skills add https://github.com/dyad-sh/dyad --skill dyad:deflake-e2e
SKILL.md
Deflake E2E Tests

Identify and fix flaky E2E tests by running them repeatedly and investigating failures.

Arguments
$ARGUMENTS: (Optional) Specific E2E test file(s) to deflake (e.g., main.spec.ts or e2e-tests/main.spec.ts). If not provided, will prompt to deflake the entire test suite.
Instructions

Check if specific tests are provided:

If $ARGUMENTS is empty or not provided, ask the user:

"No specific tests provided. Do you want to deflake the entire E2E test suite? This can take a very long time as each test will be run 10 times."

Wait for user confirmation before proceeding. If they decline, ask them to provide specific test files.

Install dependencies:

npm install


Build the app binary:

npm run build


IMPORTANT: This step is required before running E2E tests. E2E tests run against the built binary. If you make any changes to application code (anything outside of e2e-tests/), you MUST re-run npm run build before running E2E tests again, otherwise you'll be testing the old version.

Run tests repeatedly to detect flakiness:

For each test file, run it 10 times:

PLAYWRIGHT_RETRIES=0 PLAYWRIGHT_HTML_OPEN=never npm run e2e -- e2e-tests/<testfile>.spec.ts --repeat-each=10


IMPORTANT: PLAYWRIGHT_RETRIES=0 is required to disable automatic retries. Without it, CI environments (where CI=true) default to 2 retries, causing flaky tests to pass on retry and be incorrectly skipped as "not flaky."

Notes:

If $ARGUMENTS is provided without the e2e-tests/ prefix, add it
If $ARGUMENTS is provided without the .spec.ts suffix, add it
A test is considered flaky if it fails at least once out of 10 runs

For each flaky test, investigate with debug logs:

Run the failing test with Playwright browser debugging enabled:

DEBUG=pw:browser PLAYWRIGHT_RETRIES=0 PLAYWRIGHT_HTML_OPEN=never npm run e2e -- e2e-tests/<testfile>.spec.ts


Analyze the debug output to understand:

Timing issues (race conditions, elements not ready)
Animation/transition interference
Network timing variability
State leaking between tests
Snapshot comparison differences

Fix the flaky test:

Common fixes following Playwright best practices:

Use await expect(locator).toBeVisible() before interacting with elements
Use await page.waitForLoadState('networkidle') for network-dependent tests
Use stable selectors (data-testid, role, text) instead of fragile CSS selectors
Add explicit waits for animations: await page.waitForTimeout(300) (use sparingly)
Use await expect(locator).toHaveScreenshot() options like maxDiffPixelRatio for visual tests
Ensure proper test isolation (clean state before/after tests)

IMPORTANT: Do NOT change any application code. Assume the application code is correct. Only modify test files and snapshot baselines.

Update snapshot baselines if needed:

If the flakiness is due to legitimate visual differences:

PLAYWRIGHT_RETRIES=0 PLAYWRIGHT_HTML_OPEN=never npm run e2e -- e2e-tests/<testfile>.spec.ts --update-snapshots


Verify the fix:

Re-run the test 10 times to confirm it's no longer flaky:

PLAYWRIGHT_RETRIES=0 PLAYWRIGHT_HTML_OPEN=never npm run e2e -- e2e-tests/<testfile>.spec.ts --repeat-each=10


The test should pass all 10 runs consistently.

Summarize results:

Report to the user:

Which tests were identified as flaky
What was causing the flakiness
What fixes were applied
Verification results (all 10 runs passing)
Any tests that could not be fixed and need further investigation
Weekly Installs
23
Repository
dyad-sh/dyad
GitHub Stars
20.2K
First Seen
Feb 27, 2026