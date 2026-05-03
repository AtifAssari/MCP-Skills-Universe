---
rating: ⭐⭐⭐
title: browsing-with-playwright
url: https://skills.sh/bilalmk/todo_correct/browsing-with-playwright
---

# browsing-with-playwright

skills/bilalmk/todo_correct/browsing-with-playwright
browsing-with-playwright
Installation
$ npx skills add https://github.com/bilalmk/todo_correct --skill browsing-with-playwright
Summary

Browser automation with Playwright MCP for web navigation, form interaction, and data extraction.

Supports navigation, element interaction (click, type, select), screenshots, and accessibility snapshots that return element references for precise targeting
Includes JavaScript execution via browser_evaluate and multi-step atomic operations through browser_run_code for complex workflows
Requires --shared-browser-context flag to maintain browser state across sequential commands; server runs on port 8808
Common workflows covered: form submission, data extraction, waiting for page conditions, and element verification via snapshots
SKILL.md
Browser Automation

Automate browser interactions via Playwright MCP server.

Server Lifecycle
Start Server
# Using helper script (recommended)
bash scripts/start-server.sh

# Or manually
npx @playwright/mcp@latest --port 8808 --shared-browser-context &

Stop Server
# Using helper script (closes browser first)
bash scripts/stop-server.sh

# Or manually
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_close -p '{}'
pkill -f "@playwright/mcp"

When to Stop
End of task: Stop when browser work is complete
Long sessions: Keep running if doing multiple browser tasks
Errors: Stop and restart if browser becomes unresponsive

Important: The --shared-browser-context flag is required to maintain browser state across multiple mcp-client.py calls. Without it, each call gets a fresh browser context.

Quick Reference
Navigation
# Go to URL
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_navigate \
  -p '{"url": "https://example.com"}'

# Go back
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_navigate_back -p '{}'

Get Page State
# Accessibility snapshot (returns element refs for clicking/typing)
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_snapshot -p '{}'

# Screenshot
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_take_screenshot \
  -p '{"type": "png", "fullPage": true}'

Interact with Elements

Use ref from snapshot output to target elements:

# Click element
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_click \
  -p '{"element": "Submit button", "ref": "e42"}'

# Type text
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_type \
  -p '{"element": "Search input", "ref": "e15", "text": "hello world", "submit": true}'

# Fill form (multiple fields)
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_fill_form \
  -p '{"fields": [{"ref": "e10", "value": "john@example.com"}, {"ref": "e12", "value": "password123"}]}'

# Select dropdown
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_select_option \
  -p '{"element": "Country dropdown", "ref": "e20", "values": ["US"]}'

Wait for Conditions
# Wait for text to appear
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_wait_for \
  -p '{"text": "Success"}'

# Wait for time (ms)
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_wait_for \
  -p '{"time": 2000}'

Execute JavaScript
python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_evaluate \
  -p '{"function": "return document.title"}'

Multi-Step Playwright Code

For complex workflows, use browser_run_code to run multiple actions in one call:

python3 scripts/mcp-client.py call -u http://localhost:8808 -t browser_run_code \
  -p '{"code": "async (page) => { await page.goto(\"https://example.com\"); await page.click(\"text=Learn more\"); return await page.title(); }"}'


Tip: Use browser_run_code for complex multi-step operations that should be atomic (all-or-nothing).

Workflow: Form Submission
Navigate to page
Get snapshot to find element refs
Fill form fields using refs
Click submit
Wait for confirmation
Screenshot result
Workflow: Data Extraction
Navigate to page
Get snapshot (contains text content)
Use browser_evaluate for complex extraction
Process results
Verification

Run: python3 scripts/verify.py

Expected: ✓ Playwright MCP server running

If Verification Fails
Run diagnostic: pgrep -f "@playwright/mcp"
Check: Server process running on port 8808
Try: bash scripts/start-server.sh
Stop and report if still failing - do not proceed with downstream steps
Tool Reference

See references/playwright-tools.md for complete tool documentation.

Troubleshooting
Issue	Solution
Element not found	Run browser_snapshot first to get current refs
Click fails	Try browser_hover first, then click
Form not submitting	Use "submit": true with browser_type
Page not loading	Increase wait time or use browser_wait_for
Server not responding	Stop and restart: bash scripts/stop-server.sh && bash scripts/start-server.sh
Weekly Installs
1.6K
Repository
bilalmk/todo_correct
GitHub Stars
1
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail