---
title: dyad:e2e-rebase
url: https://skills.sh/dyad-sh/dyad/dyad:e2e-rebase
---

# dyad:e2e-rebase

skills/dyad-sh/dyad/dyad:e2e-rebase
dyad:e2e-rebase
Installation
$ npx skills add https://github.com/dyad-sh/dyad --skill dyad:e2e-rebase
SKILL.md
E2E Snapshot Rebase

Rebase E2E test snapshots based on failed tests from the PR comments.

Instructions

Get the current PR number using gh pr view --json number --jq '.number'

Fetch PR comments and look for the Playwright test results comment. Parse out the failed test filenames from either:

The "Failed Tests" section (lines starting with - \filename.spec.ts`)
The "Update Snapshot Commands" section (contains npm run e2e e2e-tests/filename.spec.ts)

If no failed tests are found in the PR comments, inform the user and stop.

Build the application binary:

npm run build


IMPORTANT: E2E tests run against the built binary. If any application code (anything outside of e2e-tests/) has changed, you MUST run this build step before running E2E tests, otherwise you'll be testing the old version.

For each failed test file, run the e2e test with snapshot update:

PLAYWRIGHT_HTML_OPEN=never npm run e2e e2e-tests/<testFilename>.spec.ts -- --update-snapshots


After updating snapshots, re-run the same tests WITHOUT --update-snapshots to verify they pass consistently:

PLAYWRIGHT_HTML_OPEN=never npm run e2e e2e-tests/<testFilename>.spec.ts


If any test fails on this verification run, inform the user that the snapshots may be flaky and stop.

Show the user which snapshots were updated using git diff on the snapshot files.

Review the snapshot changes to ensure they look reasonable and are consistent with the PR's purpose. Consider:

Do the changes align with what the PR is trying to accomplish?
Are there any unexpected or suspicious changes?

If the snapshots look reasonable, commit and push the changes:

git add e2e-tests/snapshots/
git commit -m "Update E2E snapshots"
git push


Inform the user that the snapshots have been updated and pushed to the PR.

Weekly Installs
24
Repository
dyad-sh/dyad
GitHub Stars
20.2K
First Seen
Feb 27, 2026