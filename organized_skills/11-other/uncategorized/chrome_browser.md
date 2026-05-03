---
rating: ⭐⭐⭐
title: chrome-browser
url: https://skills.sh/oimiragieo/agent-studio/chrome-browser
---

# chrome-browser

skills/oimiragieo/agent-studio/chrome-browser
chrome-browser
Installation
$ npx skills add https://github.com/oimiragieo/agent-studio --skill chrome-browser
SKILL.md
Chrome Browser Automation
Installation

Standalone script: No download; the skill invokes .claude/tools/chrome-browser/chrome-browser.cjs (Node.js v18+ required).

MCP integrations (for full automation):

Chrome DevTools MCP: Usually bundled with the environment; ensure Chrome/Chromium is installed (google.com/chrome).
Claude-in-Chrome: Install the Claude-in-Chrome extension and run with --chrome when needed.
Cheat Sheet & Best Practices

Testing: Test user-visible behavior, not implementation. Isolate tests (own storage/cookies); use before/after hooks for login or setup. Mock third-party networks instead of depending on live services.

DevTools Recorder: Record flows in Recorder panel; export as JSON or test scripts (Puppeteer, Nightwatch). Replay with Puppeteer Replay in CI. Use for performance measurement of user flows.

Hacks: Prefer Chrome DevTools MCP for testing/debugging (always on); use Claude-in-Chrome for authenticated sessions (GIF, forms). Limit GIF frames (e.g. 100) to avoid memory issues. Use take_snapshot for structure; evaluate_script for custom checks.

Certifications & Training

No official cert. Chrome for Developers – DevTools. Frontend Masters / Udemy “Mastering Chrome DevTools.” Skill data: Test user-visible behavior; isolate tests; Recorder + Puppeteer Replay; performance tracing.

Hooks & Workflows

Suggested hooks: Optional: post-test hook to capture screenshots on failure. Use when qa or frontend-pro is routed for browser testing (add chrome-browser to contextual: browser_testing or similar).

Workflows: Use with qa (add to contextual) or frontend-pro for E2E/browser flows. Flow: open URL → interact (click/fill) → snapshot or assert. See .claude/workflows/chrome-browser-skill-workflow.md.

Two Integrations - When to Use Each
Feature	Chrome DevTools MCP	Claude-in-Chrome
Status	✅ Always available	⚠️ Requires --chrome flag
Activation	Automatic (built-in)	claude --chrome + extension
Auth sessions	❌ Fresh browser	✅ Uses your logins
Performance tracing	✅ Full Core Web Vitals	❌ Not available
Network inspection	✅ Detailed with body access	✅ Basic
Device emulation	✅ Mobile, geolocation, CPU	❌ Limited
GIF recording	❌ No	✅ Yes (100 frame limit)
Page text extraction	Via snapshot	✅ Dedicated tool
Best for	Testing, debugging, performance	Authenticated workflows, demos
Performance Limits (Memory Safeguard)

Chrome browser automation can record GIF videos. To prevent memory exhaustion:

GIF frame limit: 100 frames (HARD LIMIT)
Each frame: 5-20 KB (depends on complexity)
100 frames × 10 KB avg = ~1 MB per recording
Keeps browser session memory-efficient

Frame tracking:

Typical actions per frame: 1-2 (click, scroll, type)
50 frames = 25-50 actions
100 frames = 50-100 actions
For longer workflows, use multiple recordings
Decision Guide
Need to test/debug a public site?     → Chrome DevTools MCP
Need performance analysis?            → Chrome DevTools MCP
Need to access authenticated apps?    → Claude-in-Chrome (--chrome)
Need to record a demo GIF?            → Claude-in-Chrome (--chrome)
Need to interact with Google Docs?    → Claude-in-Chrome (--chrome)
Need device/network emulation?        → Chrome DevTools MCP


Claude-in-Chrome:

Authenticated web app interaction (Google Docs, Gmail, Notion)
Session recording as GIF
Natural language element finding
Form automation with your saved data
Page text extraction
Shortcut/workflow execution
Chrome DevTools MCP (Always Available)

No setup required - these tools work immediately.

Step 1: List and Select Pages
// List all open pages
mcp__chrome - devtools__list_pages();

// Select a page to work with
mcp__chrome - devtools__select_page({ pageId: 1 });

// Create a new page
mcp__chrome - devtools__new_page({ url: 'https://example.com' });

Step 2: Navigate and Interact
// Navigate to URL
mcp__chrome - devtools__navigate_page({ url: 'https://example.com' });

// Take accessibility snapshot (get element UIDs)
mcp__chrome - devtools__take_snapshot();

// Click element by UID from snapshot
mcp__chrome - devtools__click({ uid: 'ref_123' });

// Fill form field
mcp__chrome - devtools__fill({ uid: 'ref_456', value: 'test@example.com' });

// Fill entire form
mcp__chrome -
  devtools__fill_form({
    elements: [
      { uid: 'ref_456', value: 'test@example.com' },
      { uid: 'ref_789', value: 'password123' },
    ],
  });

Step 3: Debug and Inspect
// Read console messages
mcp__chrome - devtools__list_console_messages({ types: ['error', 'warn'] });

// Get specific console message details
mcp__chrome - devtools__get_console_message({ msgid: 1 });

// List network requests
mcp__chrome - devtools__list_network_requests({ resourceTypes: ['xhr', 'fetch'] });

// Get request/response details
mcp__chrome - devtools__get_network_request({ reqid: 1 });

// Execute JavaScript
mcp__chrome -
  devtools__evaluate_script({
    function: '() => document.title',
  });

Step 4: Performance Analysis
// Start performance trace (with page reload)
mcp__chrome - devtools__performance_start_trace({ reload: true, autoStop: true });

// Or manual stop
mcp__chrome - devtools__performance_start_trace({ reload: true, autoStop: false });
// ... interact with page ...
mcp__chrome - devtools__performance_stop_trace();

// Analyze specific insight
mcp__chrome -
  devtools__performance_analyze_insight({
    insightSetId: 'navigation-1',
    insightName: 'LCPBreakdown',
  });

Step 5: Device Emulation
// Emulate mobile device
mcp__chrome -
  devtools__emulate({
    viewport: {
      width: 375,
      height: 667,
      deviceScaleFactor: 2,
      isMobile: true,
      hasTouch: true,
    },
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)...',
  });

// Emulate slow network
mcp__chrome - devtools__emulate({ networkConditions: 'Slow 3G' });

// Emulate geolocation
mcp__chrome -
  devtools__emulate({
    geolocation: { latitude: 37.7749, longitude: -122.4194 },
  });

Claude-in-Chrome (Requires Setup)
Prerequisites
Install Claude-in-Chrome extension (v1.0.36+) from Chrome Web Store
Start Claude with flag: claude --chrome
Chrome must be visible (no headless mode)
Paid Claude plan required (Pro, Team, or Enterprise)
Step 1: Get Tab Context
// ALWAYS call first to get available tabs
mcp__claude-in-chrome__tabs_context_mcp({ createIfEmpty: true })

// Create a new tab for this conversation
mcp__claude-in-chrome__tabs_create_mcp()

Step 2: Navigate and Read
// Navigate to URL
mcp__claude-in-chrome__navigate({ url: "https://docs.google.com", tabId: 123 })

// Read page structure (accessibility tree)
mcp__claude-in-chrome__read_page({ tabId: 123 })

// Find elements by natural language
mcp__claude-in-chrome__find({ query: "login button", tabId: 123 })

// Extract page text
mcp__claude-in-chrome__get_page_text({ tabId: 123 })

Step 3: Interact
// Click, type, screenshot via computer tool
mcp__claude-in-chrome__computer({
  action: "left_click",
  coordinate: [100, 200],
  tabId: 123
})

mcp__claude-in-chrome__computer({
  action: "type",
  text: "Hello world",
  tabId: 123
})

mcp__claude-in-chrome__computer({
  action: "screenshot",
  tabId: 123
})

// Fill form by element reference
mcp__claude-in-chrome__form_input({
  ref: "ref_1",
  value: "test@example.com",
  tabId: 123
})

Step 4: Record GIF Demo
// Start recording
mcp__claude-in-chrome__gif_creator({ action: "start_recording", tabId: 123 })

// Take screenshot to capture initial state
mcp__claude-in-chrome__computer({ action: "screenshot", tabId: 123 })

// ... perform actions ...

// Take final screenshot
mcp__claude-in-chrome__computer({ action: "screenshot", tabId: 123 })

// Stop and export
mcp__claude-in-chrome__gif_creator({ action: "stop_recording", tabId: 123 })
mcp__claude-in-chrome__gif_creator({
  action: "export",
  download: true,
  filename: "demo.gif",
  tabId: 123
})

Recording Best Practices

✓ GOOD patterns:

Login flow: 15-20 frames (5-10 actions)
Form filling: 10-15 frames (5-8 actions)
Navigation demo: 20-30 frames (10-15 actions)
Full workflow: 2-3 recordings of 30-50 frames each

✗ BAD patterns:

Single recording with 200+ frames
Waiting for loading (adds 10+ empty frames per second)
Continuous scrolling (can reach 100+ frames quickly)
Multiple simultaneous recordings

If you hit 100 frames:

Stop recording
Export current GIF
Start new recording for next part
Link recordings together in documentation
Timeout Management
Default timeout: 30 seconds per recording
If recording >100 frames: Use multiple 30-second recordings
Don't wait for slow loading (screenshot instead)
Keep actions fast (minimize waits)

</execution_process>

<best_practices>

Chrome DevTools MCP
Always take snapshot first to get element UIDs before clicking/filling
Use includeSnapshot: true on actions to get updated state
Filter network requests by resourceTypes to avoid noise
Save traces to file with filePath parameter for later analysis
Claude-in-Chrome
Call tabs_context_mcp first to get valid tab IDs
Create new tabs rather than reusing existing ones
Use read_page before find to understand page structure
Filter console with patterns to avoid verbosity
Dismiss modal dialogs manually - they block all events
General
Prefer Chrome DevTools MCP for public sites (always available)
Use Claude-in-Chrome only when authentication is required
Don't trigger alert/confirm/prompt - they block browser events

</best_practices>

// Create page and navigate
mcp__chrome - devtools__new_page({ url: 'https://example.com/login' });

// Take snapshot to get element UIDs
mcp__chrome - devtools__take_snapshot();

// Fill login form
mcp__chrome -
  devtools__fill_form({
    elements: [
      { uid: 'email_field', value: 'test@example.com' },
      { uid: 'password_field', value: 'testpass123' },
    ],
  });

// Click submit
mcp__chrome - devtools__click({ uid: 'submit_button' });

// Check for errors
mcp__chrome - devtools__list_console_messages({ types: ['error'] });


</usage_example>

<usage_example> Performance Audit (Chrome DevTools MCP):

// Navigate to page
mcp__chrome - devtools__navigate_page({ url: 'https://example.com' });

// Run performance trace with reload
mcp__chrome -
  devtools__performance_start_trace({
    reload: true,
    autoStop: true,
    filePath: 'trace.json.gz',
  });

// Analyze LCP breakdown
mcp__chrome -
  devtools__performance_analyze_insight({
    insightSetId: 'navigation-1',
    insightName: 'LCPBreakdown',
  });


</usage_example>

<usage_example> Google Docs Editing (Claude-in-Chrome):

// Get tab context
mcp__claude-in-chrome__tabs_context_mcp({ createIfEmpty: true })

// Navigate to Google Docs (uses your login)
mcp__claude-in-chrome__navigate({
  url: "https://docs.google.com/document/d/YOUR_DOC_ID",
  tabId: 123
})

// Read page to find elements
mcp__claude-in-chrome__read_page({ tabId: 123 })

// Click in document and type
mcp__claude-in-chrome__computer({
  action: "left_click",
  ref: "document_body",
  tabId: 123
})

mcp__claude-in-chrome__computer({
  action: "type",
  text: "Meeting notes for today...",
  tabId: 123
})


</usage_example>

<usage_example> Record Demo GIF (Claude-in-Chrome):

// Start recording
mcp__claude-in-chrome__gif_creator({ action: "start_recording", tabId: 123 })

// Initial screenshot
mcp__claude-in-chrome__computer({ action: "screenshot", tabId: 123 })

// Navigate
mcp__claude-in-chrome__navigate({ url: "https://example.com/product", tabId: 123 })
mcp__claude-in-chrome__computer({ action: "screenshot", tabId: 123 })

// Click add to cart
mcp__claude-in-chrome__computer({ action: "left_click", ref: "add_to_cart", tabId: 123 })
mcp__claude-in-chrome__computer({ action: "screenshot", tabId: 123 })

// Stop and export
mcp__claude-in-chrome__gif_creator({ action: "stop_recording", tabId: 123 })
mcp__claude-in-chrome__gif_creator({
  action: "export",
  download: true,
  filename: "add-to-cart-flow.gif",
  options: { showClickIndicators: true, showProgressBar: true },
  tabId: 123
})


</usage_example>

Available Tools
Chrome DevTools MCP (Always Available)
Tool	Description
mcp__chrome-devtools__list_pages	List all browser pages
mcp__chrome-devtools__select_page	Select page for operations
mcp__chrome-devtools__new_page	Create new page with URL
mcp__chrome-devtools__close_page	Close a page
mcp__chrome-devtools__navigate_page	Navigate, reload, back/forward
mcp__chrome-devtools__take_snapshot	Get accessibility tree with UIDs
mcp__chrome-devtools__take_screenshot	Capture page/element screenshot
mcp__chrome-devtools__click	Click element by UID
mcp__chrome-devtools__fill	Fill input/select by UID
mcp__chrome-devtools__fill_form	Fill multiple form elements
mcp__chrome-devtools__hover	Hover over element
mcp__chrome-devtools__drag	Drag element to another
mcp__chrome-devtools__press_key	Press key or combination
mcp__chrome-devtools__evaluate_script	Execute JavaScript
mcp__chrome-devtools__handle_dialog	Accept/dismiss dialogs
mcp__chrome-devtools__upload_file	Upload file via input
mcp__chrome-devtools__wait_for	Wait for text to appear
mcp__chrome-devtools__resize_page	Resize browser window
mcp__chrome-devtools__emulate	Device/network/geo emulation
mcp__chrome-devtools__list_console_messages	List console output
mcp__chrome-devtools__get_console_message	Get message details
mcp__chrome-devtools__list_network_requests	List network requests
mcp__chrome-devtools__get_network_request	Get request/response details
mcp__chrome-devtools__performance_start_trace	Start performance recording
mcp__chrome-devtools__performance_stop_trace	Stop performance recording
mcp__chrome-devtools__performance_analyze_insight	Analyze performance insight
Claude-in-Chrome (Requires --chrome flag)
Tool	Description
mcp__claude-in-chrome__tabs_context_mcp	Get tab context (call first!)
mcp__claude-in-chrome__tabs_create_mcp	Create new tab
mcp__claude-in-chrome__navigate	Navigate to URL
mcp__claude-in-chrome__read_page	Get accessibility tree
mcp__claude-in-chrome__find	Find elements by description
mcp__claude-in-chrome__get_page_text	Extract page text
mcp__claude-in-chrome__computer	Click, type, screenshot, scroll
mcp__claude-in-chrome__form_input	Fill form field
mcp__claude-in-chrome__fill_form	Fill multiple fields
mcp__claude-in-chrome__javascript_tool	Execute JavaScript
mcp__claude-in-chrome__read_console_messages	Read console logs
mcp__claude-in-chrome__read_network_requests	Read network requests
mcp__claude-in-chrome__resize_window	Resize browser window
mcp__claude-in-chrome__upload_image	Upload image to element
mcp__claude-in-chrome__gif_creator	Record/export GIF
mcp__claude-in-chrome__shortcuts_list	List available shortcuts
mcp__claude-in-chrome__shortcuts_execute	Execute shortcut
mcp__claude-in-chrome__update_plan	Present plan for approval
Agent Integration

This skill is automatically assigned to:

developer - Testing, debugging, data extraction
qa - Automated testing, form validation, user flow verification
security-architect - Security testing, authentication flows
devops-troubleshooter - Production debugging, monitoring
researcher - Web scraping, data extraction
Related Workflow

For guidance on using this skill effectively, see the corresponding workflow:

Workflow File: .claude/workflows/chrome-browser-skill-workflow.md
When to Use: When you need browser automation for testing, debugging, authenticated workflows, or demo recording
Integration Methods:
Slash command invocation (/chrome-browser)
Agent skill assignment (via frontmatter)
Direct script execution

Two Integration Options:

Chrome DevTools MCP (always available) - For public site testing, performance analysis, debugging
Claude-in-Chrome (requires --chrome flag) - For authenticated app workflows, GIF recording

The workflow provides examples for invocation methods, agent assignment, and memory integration patterns.

Troubleshooting
Claude-in-Chrome "Browser extension is not connected"

Symptom: When using --chrome flag, tools return "Browser extension is not connected" error despite extension being installed.

Root Cause: Claude.app (desktop) and Claude Code register competing native messaging hosts. When both are installed, the Chrome extension connects to whichever registered last, causing connection failures.

Diagnosis:

Check if both Claude.app and Claude Code are installed
On Windows: Check %APPDATA%\Claude\ChromeNativeHost\com.anthropic.claude_browser_extension.json
On macOS: Check ~/Library/Application Support/Claude/ChromeNativeHost/

Known Bug: This is documented in GitHub issues:

#15336 - Windows Native Messaging Host not installing
#14894 - Reconnect extension fails on macOS
#20790 - Extension connects to Claude.app instead of Claude Code

Workaround (macOS):

# Disable Claude.app's native host (keep file for restoration)
cd ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/
mv com.anthropic.claude_browser_extension.json com.anthropic.claude_browser_extension.json.disabled

# Restart Chrome completely (quit and reopen)
# Then start Claude Code with --chrome flag


Workaround (Windows): Not fully documented. Potential approach:

# Rename the config to disable Claude.app's registration
cd $env:APPDATA\Claude\ChromeNativeHost
ren com.anthropic.claude_browser_extension.json com.anthropic.claude_browser_extension.json.disabled

# Restart Chrome and try again


Alternative: Use Chrome DevTools MCP instead - it works without the extension and provides similar functionality for most use cases.

Modal Dialogs Blocking Events

Symptom: After triggering alert/confirm/prompt, all browser tools stop responding.

Cause: JavaScript modal dialogs block all browser events including extension communication.

Fix: User must manually dismiss the dialog in the browser. Avoid triggering dialogs in automation scripts.

Memory Protocol (MANDATORY)

Before starting:

cat .claude/context/memory/learnings.md


After completing:

New pattern -> .claude/context/memory/learnings.md
Issue found -> .claude/context/memory/issues.md
Decision made -> .claude/context/memory/decisions.md

ASSUME INTERRUPTION: Your context may reset. If it's not in memory, it didn't happen.

Weekly Installs
298
Repository
oimiragieo/agent-studio
GitHub Stars
25
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn