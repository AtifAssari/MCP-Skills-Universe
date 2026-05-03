---
title: chrome-devtools
url: https://skills.sh/chromedevtools/chrome-devtools-mcp/chrome-devtools
---

# chrome-devtools

skills/chromedevtools/chrome-devtools-mcp/chrome-devtools
chrome-devtools
Installation
$ npx skills add https://github.com/chromedevtools/chrome-devtools-mcp --skill chrome-devtools
Summary

Chrome DevTools integration for debugging, performance analysis, and browser automation via MCP.

Provides tools for page navigation, element inspection via snapshots, clicking, form filling, screenshot capture, and JavaScript evaluation
Operates on a persistent Chrome profile with automatic browser startup; switch between multiple pages using list_pages and select_page
Supports efficient workflows: navigate, wait for content, take snapshots to identify elements by uid, then interact with those elements
Handles large outputs via file paths and offers pagination/filtering to minimize data transfer; use take_snapshot for automation and take_screenshot for visual inspection
SKILL.md
Core Concepts

Browser lifecycle: Browser starts automatically on first tool call using a persistent Chrome profile. Configure via CLI args in the MCP server configuration: npx chrome-devtools-mcp@latest --help. To enable extensions, use --categoryExtensions. Page selection: Tools operate on the currently selected page. Use list_pages to see available pages, then select_page to switch context.

Element interaction: Use take_snapshot to get page structure with element uids. Each element has a unique uid for interaction. If an element isn't found, take a fresh snapshot - the element may have been removed or the page changed.

Workflow Patterns
Before interacting with a page
Navigate: navigate_page or new_page
Wait: wait_for to ensure content is loaded if you know what you look for.
Snapshot: take_snapshot to understand page structure
Interact: Use element uids from snapshot for click, fill, etc.
Efficient data retrieval
Use filePath parameter for large outputs (screenshots, snapshots, traces)
Use pagination (pageIdx, pageSize) and filtering (types) to minimize data
Set includeSnapshot: false on input actions unless you need updated page state
Tool selection
Automation/interaction: take_snapshot (text-based, faster, better for automation)
Visual inspection: take_screenshot (when user needs to see visual state)
Additional details: evaluate_script for data not in accessibility tree
Parallel execution

You can send multiple tool calls in parallel, but maintain correct order: navigate → wait → snapshot → interact.

Testing an extension
Install: Use install_extension with the path to the unpacked extension.
Identify: Get the extension ID from the response or by calling list_extensions.
Trigger Action: Use trigger_extension_action to open the popup or side panel if applicable.
Verify Service Worker: Use evaluate_script with serviceWorkerId to check extension state or trigger background actions.
Verify Page Behavior: Navigate to a page where the extension operates and use take_snapshot to check if content scripts injected elements or modified the page correctly.
Troubleshooting

If chrome-devtools-mcp is insufficient, guide users to use Chrome DevTools UI:

https://developer.chrome.com/docs/devtools
https://developer.chrome.com/docs/devtools/ai-assistance

If there are errors launching chrome-devtools-mcp or Chrome, refer to https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/troubleshooting.md.

Weekly Installs
2.8K
Repository
chromedevtools/…ools-mcp
GitHub Stars
37.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn