---
title: webapp-testing
url: https://skills.sh/github/awesome-copilot/webapp-testing
---

# webapp-testing

skills/github/awesome-copilot/webapp-testing
webapp-testing
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill webapp-testing
Summary

Browser automation and testing toolkit for local web applications using Playwright.

Supports core browser interactions including navigation, form filling, clicking, dropdown selection, and dialog handling
Includes verification capabilities for element presence, text content, visibility, URLs, and responsive design across viewports
Provides debugging tools: screenshot capture, console log inspection, network request monitoring, and error handling patterns
Works with Node.js environments and the Playwright MCP Server, with automatic Playwright installation if needed
Offers helper functions for common testing patterns like element waiting, error capture, and assertion validation
SKILL.md
Web Application Testing

This skill enables comprehensive testing and debugging of local web applications using Playwright automation.

You should use the Playwright MCP Server to undertake the work if possible. If the MCP Server is unavailable, you can run the code in a local Node.js environment with Playwright installed.

When to Use This Skill

Use this skill when you need to:

Test frontend functionality in a real browser
Verify UI behavior and interactions
Debug web application issues
Capture screenshots for documentation or debugging
Inspect browser console logs
Validate form submissions and user flows
Check responsive design across viewports
Prerequisites
Node.js installed on the system
A locally running web application (or accessible URL)
Playwright will be installed automatically if not present
Core Capabilities
1. Browser Automation
Navigate to URLs
Click buttons and links
Fill form fields
Select dropdowns
Handle dialogs and alerts
2. Verification
Assert element presence
Verify text content
Check element visibility
Validate URLs
Test responsive behavior
3. Debugging
Capture screenshots
View console logs
Inspect network requests
Debug failed tests
Usage Examples
Example 1: Basic Navigation Test
// Navigate to a page and verify title
await page.goto("http://localhost:3000");
const title = await page.title();
console.log("Page title:", title);

Example 2: Form Interaction
// Fill out and submit a form
await page.fill("#username", "testuser");
await page.fill("#password", "password123");
await page.click('button[type="submit"]');
await page.waitForURL("**/dashboard");

Example 3: Screenshot Capture
// Capture a screenshot for debugging
await page.screenshot({ path: "debug.png", fullPage: true });

Guidelines
Always verify the app is running - Check that the local server is accessible before running tests
Use explicit waits - Wait for elements or navigation to complete before interacting
Capture screenshots on failure - Take screenshots to help debug issues
Clean up resources - Always close the browser when done
Handle timeouts gracefully - Set reasonable timeouts for slow operations
Test incrementally - Start with simple interactions before complex flows
Use selectors wisely - Prefer data-testid or role-based selectors over CSS classes
Common Patterns
Pattern: Wait for Element
await page.waitForSelector("#element-id", { state: "visible" });

Pattern: Check if Element Exists
const exists = (await page.locator("#element-id").count()) > 0;

Pattern: Get Console Logs
page.on("console", (msg) => console.log("Browser log:", msg.text()));

Pattern: Handle Errors
try {
  await page.click("#button");
} catch (error) {
  await page.screenshot({ path: "error.png" });
  throw error;
}

Limitations
Requires Node.js environment
Cannot test native mobile apps (use React Native Testing Library instead)
May have issues with complex authentication flows
Some modern frameworks may require specific configuration
Helper Functions

Some helper functions are available in test-helper.js to simplify common tasks like waiting for elements, capturing screenshots, and handling errors. You can import and use these functions in your tests to improve readability and maintainability.

Weekly Installs
9.9K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn