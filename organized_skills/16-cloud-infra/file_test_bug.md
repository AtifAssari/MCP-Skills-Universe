---
rating: ⭐⭐⭐⭐⭐
title: file-test-bug
url: https://skills.sh/microsoft/github-copilot-for-azure/file-test-bug
---

# file-test-bug

skills/microsoft/github-copilot-for-azure/file-test-bug
file-test-bug
Installation
$ npx skills add https://github.com/microsoft/github-copilot-for-azure --skill file-test-bug
SKILL.md
File Test Bug

Creates a GitHub issue in microsoft/github-copilot-for-azure for integration test failures.

Input
Skill name (required): e.g., azure-rbac, appinsights-instrumentation
Test run (optional): Timestamp of test run. Defaults to most recent with logs for the skill.
Steps
Ask user for skill name if not provided
Parse tests/reports/junit.xml for failures matching the skill
Find test run directory (specified or most recent with matching logs)
Read agent-metadata.md from tests/reports/test-run-<timestamp>/<skillname>-<testname>/
For each failure, read the actual line of code from the test file using the location (file:line) from junit.xml
REQUIRED - Write diagnosis BEFORE creating issue:
Analyze the agent-metadata.md to understand what the agent did
Compare agent behavior to what the test expected (from the assertion)
Identify the root cause (skill issue, test issue, or model behavior)
Write 2-3 sentences per failed test explaining WHY it failed
Suggest potential fixes (update skill, update test, or update fixtures)
Create issue via github-mcp-server-create_issue:
owner: microsoft
repo: github-copilot-for-azure
title: Integration test failure in <skill-name>
labels: ["bug", "integration-test"]
body: |
  ## Failed Tests
  - <test-name>: <error message>
  
  ## Diagnosis
  
  ### Root Cause
  <1-2 sentences explaining WHY the test failed based on agent-metadata.md analysis>
  
  ### Analysis per Test
  - **<test-name>**: <what agent did vs what test expected>
  
  ### Suggested Fix
  <one of: update skill, update test assertions, provide test fixtures>

  ## Details
  ### <test-name>
  **Error:** <failure from junit.xml>
  **Location:** <file:line>
  ```typescript
  <actual line of code from the test file at the specified line number>


<full contents of agent-metadata.md file, verbatim>

Important

Include the complete, unmodified contents of each agent-metadata.md file in the issue body. Do NOT summarize or truncate the logs. Wrap each log in a <details> block with the test name as the summary.

Weekly Installs
1.1K
Repository
microsoft/githu…or-azure
GitHub Stars
202
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail