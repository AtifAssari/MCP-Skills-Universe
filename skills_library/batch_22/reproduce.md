---
title: reproduce
url: https://skills.sh/tharsanan1/wso2-se-agent-skills/reproduce
---

# reproduce

skills/tharsanan1/wso2-se-agent-skills/reproduce
reproduce
Installation
$ npx skills add https://github.com/tharsanan1/wso2-se-agent-skills --skill reproduce
SKILL.md
/reproduce — Issue Analysis & Bug Reproduction

You are a Software Engineer determining if a GitHub issue is a valid, reproducible bug. Follow the procedure below precisely.

Step 1: Classify the Issue

Determine whether this is a Bug, Feature Request, Question, or Enhancement.

If it is not a bug, report the classification and stop. Do not proceed further.
If the issue bundles multiple bugs, ask the developer to split it before proceeding.
Step 2: Environment Setup
If a product zip is available use it, else build the product from the relevant branch.
Verify: Ports available, product starts and passes health check.

If setup fails, report the failure and stop

Step 3: Reproduce the Bug

THIS STEP IS MANDATORY. YOU MUST ACTUALLY TRIGGER THE BUG IN A RUNNING PRODUCT.

"Reproduction" means observing the bug happen at runtime — NOT reading source code, NOT analyzing logic, NOT grepping compiled output. If you have not seen the actual incorrect behavior with your own eyes (via Playwright screenshots, curl responses, or log output from a running server), you have NOT reproduced the bug. Do not mark it as reproduced.

Code inspection is useful for root cause analysis (Step 5), but it is NOT reproduction. You must complete this step before writing any root cause analysis.

How to reproduce
Start the product server and wait for it to be ready.
Follow the reproduction steps from the issue (or infer reasonable steps if not provided).
Determine whether this is a frontend or backend issue:
Frontend issue (involves UI behavior — clicking, forms, navigation): Use Playwright to drive a real browser. Save the script as .ai/reproduce-<issue_number>.mjs so verify-fix can reuse it. Refer CLAUDE.md for Playwright guides.
Backend issue (involves REST API responses, server errors): Use curl to make real HTTP requests to the running server.
Capture concrete evidence:
Frontend: Screenshots at each key step showing the actual buggy behavior.
Backend: Full HTTP responses (status code, headers, body), error logs from the server.
Record expected vs. actual behavior based on what you observed, not what you read in code.
What counts as reproduction evidence
Playwright screenshot showing a UI element is hidden when it should be visible
curl response showing HTTP 500 when it should be 200
Server log showing an exception during an API call you made
What does NOT count as reproduction evidence
"Code analysis confirms the bug" — this is NOT reproduction
"The logic shows enableDirectToken is never restored" — this is analysis, NOT reproduction
curl -sk -o /dev/null -w "%{http_code}" <url> returning 200 — this only proves the page loads, NOT that the bug exists REST API reference: See the REST API Reference section in CLAUDE.md
Step 4: Locate Related Tests

Analyze only the unit test coverage related to the issue.

Step 5: Write the Output Artifact

Create the directory .ai/ at the repo root if it doesn't exist. Write the analysis to .ai/ia-<issue_number>.md using this exact format:

# Issue Analysis — [Issue #ID]: [Issue Title]

## Classification
- **Type:** Bug / Not a Bug (with explanation)
- **Severity Assessment:** Critical / High / Medium / Low
- **Affected Component(s):** [component names]
- **Affected Feature(s):** [feature names]

## Reproducibility
- **Reproducible:** Yes / No (ONLY "Yes" if you triggered the bug at runtime and observed it. Code analysis alone = "No")
- **Reproduction method:** Playwright / curl / server logs (specify which)
- **Environment:** [branch, language/runtime version, OS, relevant config]
- **Steps Executed:**
  1. [step]
  2. [step]
- **Expected Behavior:** [what should happen]
- **Actual Behavior:** [what actually happened — describe what you OBSERVED, not what you read in code]
- **Evidence:** [screenshots in .ai/screenshots-<issue_number>/, curl output, or server log excerpts — MUST be from runtime, not code]

## Root Cause Analysis
Brief analysis of what is likely causing the bug based on reproduction results.

## Test Coverage Assessment
- **Existing tests covering this path:** [list test files/functions]
- **Coverage gaps identified:** [paths with no tests]
- **Proposed test plan:**
  - Unit test: [description]
  - Negative/edge cases: [description]

Step 6: Cleanup
Revert any temporary config or data changes.
Ensure the working tree is clean.
Important Rules
Never guess. If you encounter ambiguity you cannot resolve from available documents, stop and ask the developer.
Artifacts over memory. The output artifact must be complete enough for a different agent to pick up where you left off.
Server startup: The start command and the log polling loop MUST be in the same Bash tool call with timeout: 200000. Do not split them into separate calls.
Playwright best practices: Wait for elements rather than using fixed sleeps (page.waitForSelector(), page.locator().waitFor()). Log assertions clearly — print expected vs actual so the output is useful in artifacts.
Weekly Installs
42
Repository
tharsanan1/wso2…t-skills
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn