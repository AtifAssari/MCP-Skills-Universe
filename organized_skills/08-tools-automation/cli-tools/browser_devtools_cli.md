---
rating: ⭐⭐⭐
title: browser-devtools-cli
url: https://skills.sh/serkan-ozal/browser-devtools-skills/browser-devtools-cli
---

# browser-devtools-cli

skills/serkan-ozal/browser-devtools-skills/browser-devtools-cli
browser-devtools-cli
Installation
$ npx skills add https://github.com/serkan-ozal/browser-devtools-skills --skill browser-devtools-cli
SKILL.md
Browser DevTools CLI

Command-line interface for browser automation, debugging, and testing using Playwright. This CLI is for the browser platform; for Node.js backend debugging, use node-devtools-cli (see node-devtools-cli skill).

Installation
npm install -g browser-devtools-mcp

Quick Start
# Navigate to a URL
browser-devtools-cli navigation go-to --url "https://example.com"

# Take a screenshot
browser-devtools-cli content take-screenshot --name "homepage"

# Get page content as text
browser-devtools-cli content get-as-text


Ref-based workflow (recommended for AI agents): Call a11y take-aria-snapshot first to get refs (e1, e2, ...), then use refs in interaction click --selector "e1" or content take-screenshot --annotate for numbered element labels.

Global Options
Option	Description	Default
--port <number>	Daemon server port	2020
--session-id <string>	Session ID for browser state persistence	auto
--json	Output results as JSON (recommended for AI)	false
--quiet	Suppress log messages	false
--verbose	Enable debug output	false
--timeout <ms>	Operation timeout	30000
--headless	Run browser in headless mode	true
--no-headless	Run browser with visible window	-
--persistent	Preserve cookies/localStorage	false
--no-persistent	Clear state on session end	-
--user-data-dir <path>	Browser user data directory	OS temp
--use-system-browser	Use system Chrome	false
--browser-path <path>	Custom browser path	auto

AI Agent Recommended Options:

# JSON output for parsing, quiet mode for clean output, session for state persistence
browser-devtools-cli --json --quiet --session-id "my-session" <command>

Tool Domains

The CLI provides tools organized by domain:

Domain	Description	Reference
navigation	Page navigation (go-to, back, forward, reload)	
content	Content extraction (screenshot, PDF, HTML, text)	
interaction	User interactions (click, fill, hover, scroll)	
a11y	Accessibility snapshots (ARIA, AX tree)	
o11y	Observability (Web Vitals, console, HTTP, traces)	
debug	Non-blocking debugging (tracepoints, logpoints, exceptions)	
stub	HTTP mocking (intercept, mock, clear)	
sync	Synchronization (wait for network idle)	
react	React DevTools integration	
figma	Figma design comparison	
execute	Batch JavaScript execution (run execute; VM has page, callTool)	

Execute is available in both CLI and MCP. Use it to run JavaScript and batch tool calls: CLI run execute --code "<js>" (optionally --timeout-ms); MCP tool execute with the same params. Inside the VM: page (browser only) — Playwright Page; use await page.title(), await page.evaluate(...), etc. callTool(name, input, returnOutput?) — invoke any tool; always await; name is underscore form (e.g. 'navigation_go-to'); input is an object (camelCase keys); returnOutput: true adds the result to the response toolOutputs. See execute reference for full bindings and args.

CLI Management Commands
Daemon Management
browser-devtools-cli daemon status      # Check daemon status
browser-devtools-cli daemon info        # Show daemon info (version, uptime, sessions)
browser-devtools-cli daemon start       # Start daemon
browser-devtools-cli daemon stop        # Stop daemon
browser-devtools-cli daemon restart     # Restart daemon

Session Management
browser-devtools-cli session list                  # List active sessions
browser-devtools-cli session info <session-id>     # Show session details
browser-devtools-cli session delete <session-id>   # Delete a session

Tool Discovery
browser-devtools-cli tools list              # List all available tools
browser-devtools-cli tools search <query>    # Search tools by name or description
browser-devtools-cli tools info <tool-name>  # Show tool details and parameters

Configuration
browser-devtools-cli config    # Show current configuration

Updates
browser-devtools-cli update --check   # Check for updates
browser-devtools-cli update           # Check and install updates

Examples
Basic Navigation and Screenshot
# Navigate to URL
browser-devtools-cli navigation go-to --url "https://example.com"

# Take screenshot
browser-devtools-cli content take-screenshot --name "homepage"

# Get page text
browser-devtools-cli content get-as-text

Form Automation
# Use same session for state persistence
SESSION="--session-id login-test"

# Navigate to login page
browser-devtools-cli $SESSION navigation go-to --url "https://app.example.com/login"

# Fill form fields
browser-devtools-cli $SESSION interaction fill --selector "#email" --value "user@example.com"
browser-devtools-cli $SESSION interaction fill --selector "#password" --value "password123"

# Submit form
browser-devtools-cli $SESSION interaction click --selector "button[type=submit]"

# Wait for navigation
browser-devtools-cli $SESSION sync wait-for-network-idle

# Capture result
browser-devtools-cli $SESSION content take-screenshot --name "dashboard"

Performance Analysis
# Navigate
browser-devtools-cli navigation go-to --url "https://example.com"

# Get Web Vitals metrics
browser-devtools-cli --json o11y get-web-vitals

# Check console for errors
browser-devtools-cli --json o11y get-console-messages --type warning

# Analyze HTTP requests
browser-devtools-cli --json o11y get-http-requests

Accessibility Audit
# Navigate
browser-devtools-cli navigation go-to --url "https://example.com"

# Get ARIA snapshot
browser-devtools-cli a11y take-aria-snapshot

# Get detailed AX tree
browser-devtools-cli --json a11y take-ax-tree-snapshot --roles button,link,textbox

Batch Execution (execute)
# Run JavaScript in session VM (page + callTool available)
browser-devtools-cli run execute --code "return await page.title();"

# Batch multiple tools in one call (fewer round-trips)
browser-devtools-cli run execute --code "await callTool('a11y_take-aria-snapshot', {}, true); await callTool('content_take-screenshot', {}, true);"

API Mocking
# Mock API response
browser-devtools-cli stub mock-http-response \
  --pattern "**/api/users" \
  --body '[{"id": 1, "name": "Test User"}]'

# Navigate and test
browser-devtools-cli navigation go-to --url "https://app.example.com"

# Clear mocks
browser-devtools-cli stub clear

Non-Blocking Debugging
SESSION="--session-id debug-session"

# Navigate to app
browser-devtools-cli $SESSION navigation go-to --url "http://localhost:3000"

# Set tracepoint on a function
browser-devtools-cli $SESSION debug put-tracepoint \
  --url-pattern "app.js" \
  --line-number 42

# Add watch expression
browser-devtools-cli $SESSION debug add-watch --expression "this"

# Enable exception catching
browser-devtools-cli $SESSION debug put-exceptionpoint --state uncaught

# Interact with app (triggers probes)
browser-devtools-cli $SESSION interaction click --selector "#submit-btn"

# Get captured snapshots
browser-devtools-cli $SESSION --json debug get-probe-snapshots
browser-devtools-cli $SESSION --json debug get-probe-snapshots --types tracepoint,exceptionpoint

Shell Script for CI/CD
#!/bin/bash
set -e

CLI="browser-devtools-cli --json --quiet --session-id ci-test-$$"

# Navigate
$CLI navigation go-to --url "https://example.com"

# Wait for load
$CLI sync wait-for-network-idle

# Take screenshot
$CLI content take-screenshot --name "ci-test"

# Get Web Vitals
VITALS=$($CLI o11y get-web-vitals)
echo "Web Vitals: $VITALS"

# Check for console errors
ERRORS=$($CLI o11y get-console-messages --type error)
if [ "$ERRORS" != "[]" ]; then
  echo "Console errors found: $ERRORS"
  exit 1
fi

# Cleanup
$CLI session delete "ci-test-$$"

Interactive Mode (Human Users)

For manual exploration, an interactive REPL mode is available:

browser-devtools-cli interactive
browser-devtools-cli --no-headless interactive   # With visible browser

Command	Description
help	Show available commands
exit, quit	Exit interactive mode
<domain> <tool>	Execute a tool
Shell Completions
# Bash
browser-devtools-cli completion bash
echo 'eval "$(browser-devtools-cli completion bash)"' >> ~/.bashrc

# Zsh
browser-devtools-cli completion zsh
echo 'eval "$(browser-devtools-cli completion zsh)"' >> ~/.zshrc

Weekly Installs
36
Repository
serkan-ozal/bro…s-skills
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail