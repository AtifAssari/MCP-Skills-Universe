---
rating: ⭐⭐
title: playwright-generate-test
url: https://skills.sh/github/awesome-copilot/playwright-generate-test
---

# playwright-generate-test

skills/github/awesome-copilot/playwright-generate-test
playwright-generate-test
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill playwright-generate-test
Summary

Generate Playwright tests from scenarios using interactive browser exploration and validation.

Guides you through step-by-step test creation: scenario review, browser exploration, element inspection, interaction validation, and final test generation
Integrates with Playwright MCP tools to inspect page elements, capture selectors, and validate interactions before writing test code
Generates TypeScript tests using @playwright/test framework and automatically saves them to the tests directory
Executes generated tests and iterates until they pass, ensuring reliability before completion
SKILL.md
Test Generation with Playwright MCP

Your goal is to generate a Playwright test based on the provided scenario after completing all prescribed steps.

Specific Instructions
You are given a scenario, and you need to generate a playwright test for it. If the user does not provide a scenario, you will ask them to provide one.
DO NOT generate test code prematurely or based solely on the scenario without completing all prescribed steps.
DO run steps one by one using the tools provided by the Playwright MCP.
Only after all steps are completed, emit a Playwright TypeScript test that uses @playwright/test based on message history
Save generated test file in the tests directory
Execute the test file and iterate until the test passes
Weekly Installs
11.3K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass