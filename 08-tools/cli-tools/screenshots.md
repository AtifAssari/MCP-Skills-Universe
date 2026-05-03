---
title: screenshots
url: https://skills.sh/morphet81/cheat-sheets/screenshots
---

# screenshots

skills/morphet81/cheat-sheets/screenshots
screenshots
Installation
$ npx skills add https://github.com/morphet81/cheat-sheets --skill screenshots
SKILL.md

Take screenshots of components affected by recent changes, either from the running application (with e2e authentication) or from Storybook.

Usage:

/screenshots - Detect changed components and take screenshots automatically
/screenshots navigate to /settings, open the "Profile" tab, screenshot the form - Follow custom instructions to take screenshots

Instructions:

Check for custom instructions:

If $ARGUMENTS is provided and non-empty, run step 2 (prerequisites), then jump to step 6 (Custom instructions mode)
If $ARGUMENTS is empty, continue with the automatic detection flow below (steps 2–5, then 7–10)

Check prerequisites:

Run playwright-cli --help to verify the Playwright CLI is available
If the command fails (not found or errors), display the following message and STOP:
## Missing Prerequisite: Playwright CLI

Playwright CLI is not installed. This skill requires the Playwright CLI for taking screenshots.

Install it with: npm install -g @playwright/cli@latest


Determine the base branch:

Check if a .agent file exists in the current directory. If it contains a baseBranch=<value> line, use that value as the base branch
If no .agent file or no baseBranch key, default to main

Identify changed components:

Run git diff --name-only $(git merge-base HEAD <base-branch>)..HEAD to find recently changed files compared to the base branch
Filter for component files: .tsx, .jsx, .vue, .svelte extensions
Exclude test files (*.test.*, *.spec.*), story files (*.stories.*), and type definition files (*.d.ts)
If no component files are found in the changes, inform the developer and STOP
Present the list of changed components to the developer

Ask the developer: App or Storybook?

Use AskUserQuestion to ask for each component (or batch if many):
Storybook — component has stories, screenshot from Storybook
App — component is visible in the running application
Skip — don't screenshot this component

Custom instructions mode (when $ARGUMENTS is provided):

This mode gives the developer full control over what to screenshot. The developer's instructions in $ARGUMENTS describe which pages to visit, which actions to perform (click buttons, fill forms, open menus, etc.), and when to take screenshots. Screenshots are captured by writing a temporary e2e test, running it, then reverting the test file.

a. Explore the e2e test setup:

Search the codebase for existing e2e/Playwright test files (e.g., *.e2e.ts, *.e2e-spec.ts, files under e2e/, tests/, or a Playwright test directory)
Identify the test runner config (e.g., playwright.config.ts) to understand the base URL, test directory, and any global setup (authentication, storage state, etc.)
Note how existing tests handle authentication — reuse the same approach (e.g., storageState, global setup, beforeEach login)

b. Write a temporary e2e test file:

Create a new test file in the project's e2e test directory following existing conventions (e.g., e2e/tmp-screenshots.e2e.ts)
The test should:
Handle authentication using the project's existing auth pattern
Navigate to the specified pages/routes from $ARGUMENTS
Perform any requested actions (click elements, fill inputs, select options, hover, scroll, etc.)
Wait for animations/transitions to complete before taking each screenshot — use page.waitForTimeout() or wait for specific CSS states (e.g., wait for an element to have opacity: 1, or for a transition class to be removed, or for the element to be stable). For modals and overlays, ensure the opening animation has fully finished before capturing.
Take screenshots using page.screenshot({ path: '.tmp/<descriptive-name>.png' }) or element.screenshot() for targeted captures
Use descriptive filenames based on the page/action context (e.g., .tmp/settings-profile-tab.png, .tmp/modal-confirm-delete.png)
Create the .tmp/ directory if it doesn't exist: mkdir -p .tmp

c. Run the temporary test:

Run only the temporary test file using the project's Playwright test command (e.g., playwright-cli test e2e/tmp-screenshots.e2e.ts)
If the test fails, show the error, attempt to fix the test, and re-run. If it still fails after a reasonable attempt, show the error and continue to cleanup.

d. View results:

Use the Read tool to view each generated screenshot and present them to the developer

e. Cleanup — revert the temporary test file:

Run git restore <test-file-path> to revert the temporary test file if it was an existing file that was modified
If the test file was newly created, run rm <test-file-path> to delete it
Verify with git status that no temporary test changes remain

f. Summary:

After all screenshots are taken and cleanup is done, present a summary listing saved files and what each one shows
Then STOP (do not continue to the automatic detection steps)

For components using the Storybook path:

a. Find the corresponding story file:

Look for a .stories.tsx, .stories.jsx, .stories.ts, or .stories.js file next to the component or in the same directory
If no story file is found, inform the developer and skip this component

b. Extract story metadata:

Read the story file
Extract the meta.title (or default.title) from the default export
Extract all named exports (these are the story names), excluding the default export and any non-story exports (like args, argTypes, etc.)

c. Construct story URLs:

Convert the title to kebab-case: replace spaces, /, and special characters with -, lowercase everything
Convert each story name to kebab-case
Build the story ID: <title-kebab-case>--<story-name-kebab-case>
Build the iframe URL: http://localhost:6006/iframe.html?id=<story-id>&viewMode=story

d. Verify Storybook is running:

Try to reach http://localhost:6006 (e.g., curl -s -o /dev/null -w "%{http_code}" http://localhost:6006)
If Storybook is not running (connection refused or non-200 response), ask the developer to start it and wait for confirmation

e. Take screenshots:

Create the .tmp/ directory if it doesn't exist: mkdir -p .tmp
For each story, run:
playwright-cli screenshot --browser chromium --wait-for-timeout 2000 "<iframe-URL>" .tmp/<component-name>-<story-name>.png

Run screenshots in parallel when there are multiple stories (use & and wait in Bash)
Inform the developer that --wait-for-timeout 2000 is the default; they can ask to increase it for heavier components

f. View results:

Use the Read tool to view each generated screenshot and present them to the developer

For components using the App path:

Screenshots from the running app are captured by writing a temporary e2e test, running it, then reverting the changes.

a. Ask the developer which URL/route to navigate to:

Use AskUserQuestion to get the URL or route where the component is visible in the running app
Also ask if any actions are needed to reach the desired state (e.g., "click the Edit button", "open the dropdown")

b. Explore the e2e test setup:

Search for existing e2e/Playwright test files and config (same as step 6a)
Note how existing tests handle authentication — reuse the same approach

c. Write a temporary e2e test file:

Create a new test file in the project's e2e test directory (e.g., e2e/tmp-screenshots.e2e.ts)
The test should:
Handle authentication using the project's existing auth pattern
Navigate to the specified URL/route
Perform any actions needed to reach the desired component state
Wait for animations/transitions to complete before capturing — use page.waitForTimeout() or wait for specific CSS states (e.g., opacity: 1, transition classes removed, element stable). For modals, dropdowns, and overlays, ensure the opening animation has fully finished.
Take a screenshot using page.screenshot({ path: '.tmp/<component-name>-app.png' }) or element.screenshot() for targeted captures
Create the .tmp/ directory if it doesn't exist: mkdir -p .tmp

d. Run the temporary test:

Run only the temporary test file (e.g., playwright-cli test e2e/tmp-screenshots.e2e.ts)
If the test fails, show the error, attempt to fix, and re-run

e. View results:

Use the Read tool to view each generated screenshot and present them to the developer

f. Cleanup — revert the temporary test file:

If the file was newly created, run rm <test-file-path>
Verify with git status that no temporary test changes remain

Summary:

After all screenshots are taken, present a summary:
## Screenshots Complete

Saved to `.tmp/`:
- .tmp/ComponentA-Default.png (Storybook)
- .tmp/ComponentA-WithProps.png (Storybook)
- .tmp/ComponentB-app.png (App - /dashboard)

Screenshots are stored in the .tmp/ directory of your project.


Handle edge cases:

If a screenshot command fails, show the error and continue with the remaining screenshots
If the .tmp/ directory cannot be created, show the error and STOP
If a story file has no named exports (no stories), skip it and inform the developer
If the developer skips all components, inform them and STOP
Weekly Installs
64
Repository
morphet81/cheat-sheets
First Seen
3 days ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass