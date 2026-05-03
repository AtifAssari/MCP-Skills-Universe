---
rating: ⭐⭐
title: playwriter
url: https://skills.sh/remorses/playwriter/playwriter
---

# playwriter

skills/remorses/playwriter/playwriter
playwriter
Installation
$ npx skills add https://github.com/remorses/playwriter --skill playwriter
Summary

Control your existing Chrome browser via Playwright code snippets in a stateful local sandbox.

Connects to your running Chrome instance instead of launching a new one, ideal for JavaScript-heavy sites like Instagram, Twitter, and pages with login walls or lazy-loaded content
Executes Playwright code in a stateful sandbox with session management, context variables, and utility functions
Requires reading full documentation via playwriter skill command before use to understand timeout configuration, selector strategies, and common pitfalls
Use single quotes for -e argument to prevent bash interpretation of special characters in JavaScript code
SKILL.md
REQUIRED: Read Full Documentation First

Before using playwriter, you MUST run this command:

playwriter skill # IMPORTANT! do not use | head here. read in full!


This outputs the complete documentation including:

Session management and timeout configuration
Selector strategies (and which ones to AVOID)
Rules to prevent timeouts and failures
Best practices for slow pages and SPAs
Context variables, utility functions, and more

Do NOT skip this step. The quick examples below will fail without understanding timeouts, selector rules, and common pitfalls from the full docs.

Read the ENTIRE output. Do NOT pipe through head, tail, or any truncation command. The skill output must be read in its entirety — critical rules about timeouts, selectors, and common pitfalls are spread throughout the document, not just at the top.

Minimal Example (after reading full docs)
playwriter session new
playwriter -s 1 -e 'await page.goto("https://example.com")'


Always use single quotes for the -e argument. Single quotes prevent bash from interpreting $, backticks, and backslashes inside your JS code. Use double quotes or backtick template literals for strings inside the JS.

If playwriter is not found, use npx playwriter@latest or bunx playwriter@latest.

Weekly Installs
3.2K
Repository
remorses/playwriter
GitHub Stars
3.5K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn