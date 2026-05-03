---
title: verify-fix
url: https://skills.sh/tharsanan1/wso2-se-agent-skills/verify-fix
---

# verify-fix

skills/tharsanan1/wso2-se-agent-skills/verify-fix
verify-fix
Installation
$ npx skills add https://github.com/tharsanan1/wso2-se-agent-skills --skill verify-fix
SKILL.md
/verify-fix — Bug Fix Verification through Reproduction
Steps

Fetch the issue — get the issue details and understand the expected behavior.

Check the fix plan — Read .ai/fix-<issue_number>.md if it exists. This tells you:

Whether the dev test passed or failed during plan-fix
What changes were made and in which files
Any known issues or limitations If the dev test status is FAILED, pay special attention to the "Known Issues" section — the fix may be incomplete.

Build and patch the product — Follow the patching instructions in CLAUDE.md:

Build the changed module(s): mvn clean install -Dmaven.test.skip=true
Extract a fresh product pack from the zip
Apply JAR patches to repository/components/patches/patch9999/
Apply any template or WAR patches
Start the server

Verify at runtime — You MUST actually test the fix against a running product. Checking code diffs, grepping compiled bundles, or confirming "the build succeeded" is NOT verification. You must observe the correct behavior at runtime.

For frontend bugs: Use Playwright — follow the "Interacting with the Frontend (Playwright)" section in CLAUDE.md.

If a reproduction script exists from the reproduce step (.ai/reproduce-<issue_number>.mjs), run it — the bug behavior should no longer occur.
If no script exists, write one following the Playwright guidelines in CLAUDE.md.
Save verification screenshots to .ai/screenshots-<issue_number>/verify/.
The screenshots must show the correct behavior (e.g., an element that was hidden is now visible).

For backend bugs: Use curl or REST API calls against the running server.

After deploying APIs/products, immediately check the server log for errors before attempting invocation — follow the "Troubleshooting / Log Analysis" section in CLAUDE.md for the exact command and filtering rules.
If deployment errors are found, report them immediately — do not proceed to invocation.
If deployment is clean, proceed with invocation and compare results.

What does NOT count as verification:

❌ "The compiled bundle contains the fix logic" — grepping minified JS is not verification
❌ "The build succeeded" — a successful build only means the code compiles
❌ "The admin portal loads (HTTP 200)" — this only means the server is running
✅ Playwright screenshots showing the correct UI behavior after the fix
✅ curl response showing the correct HTTP status/body after the fix
✅ Server logs showing no errors where there were errors before

Report — Create .ai/verify-<issue_number>.md:

# Fix Verification Report

**Issue**: <url>
**Verdict**: FIXED | NOT FIXED
**Verification method**: Playwright / curl / server logs

## Reproduction Steps Executed
<what you did — must be runtime steps, not code analysis>

## Result
<what happened — describe observed runtime behavior>

## Evidence
<screenshots in .ai/screenshots-<issue_number>/verify/, curl output, or server log excerpts — MUST be from runtime>

Important Rules
Server startup: The start command and the log polling loop MUST be in the same Bash tool call with timeout: 200000. Do not split them into separate calls.
Playwright best practices: Wait for elements rather than using fixed sleeps (page.waitForSelector(), page.locator().waitFor()). Log assertions clearly — print expected vs actual so the output is useful in artifacts.
Weekly Installs
43
Repository
tharsanan1/wso2…t-skills
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn