---
title: debugging
url: https://skills.sh/serkan-ozal/browser-devtools-skills/debugging
---

# debugging

skills/serkan-ozal/browser-devtools-skills/debugging
debugging
Installation
$ npx skills add https://github.com/serkan-ozal/browser-devtools-skills --skill debugging
SKILL.md
Debugging Skill

Debug web applications and Node.js backends using console inspection, network analysis, and non-blocking code debugging with tracepoints, logpoints, and exception monitoring.

When to Use

This skill activates when:

User reports a bug or error on a web page or backend
User asks to debug JavaScript (frontend or Node.js)
User wants to inspect API calls or network requests
User needs to troubleshoot page loading or API handler issues
User mentions console errors or warnings
User wants to debug without breakpoints
User needs to trace function calls or monitor variables
Capabilities
Console Inspection
browser-devtools-cli o11y get-console-messages
browser-devtools-cli o11y get-console-messages --type warning
browser-devtools-cli --json o11y get-console-messages --type error

Network Analysis
browser-devtools-cli o11y get-http-requests
browser-devtools-cli --json o11y get-http-requests --resource-type fetch
browser-devtools-cli --json o11y get-http-requests --status '{"min":400}'

Tracepoints (Non-Blocking)
browser-devtools-cli debug put-tracepoint --url-pattern "app.js" --line-number 42
browser-devtools-cli debug list-probes --types tracepoint
browser-devtools-cli debug remove-probe --type tracepoint --id <probe-id>
browser-devtools-cli debug clear-probes --types tracepoint

Logpoints
browser-devtools-cli debug put-logpoint --url-pattern "app.js" --line-number 50 --log-expression "user.id"
browser-devtools-cli debug list-probes --types logpoint
browser-devtools-cli debug remove-probe --type logpoint --id <probe-id>
browser-devtools-cli debug clear-probes --types logpoint

Exception Monitoring
browser-devtools-cli debug put-exceptionpoint --state uncaught
browser-devtools-cli debug put-exceptionpoint --state all

Watch Expressions
browser-devtools-cli debug add-watch --expression "this"
browser-devtools-cli debug add-watch --expression "user.id"
browser-devtools-cli debug list-probes --types watch
browser-devtools-cli debug remove-probe --type watch --id <probe-id>
browser-devtools-cli debug clear-probes --types watches

Retrieve and Clear Snapshots (Unified)
browser-devtools-cli --json debug get-probe-snapshots
browser-devtools-cli --json debug get-probe-snapshots --types tracepoint,logpoint,exceptionpoint
browser-devtools-cli --json debug get-probe-snapshots --probe-id "tp_abc" --from-sequence 0
browser-devtools-cli debug clear-probe-snapshots
browser-devtools-cli debug clear-probe-snapshots --types tracepoint --probe-id "tp_abc"

Node.js Backend Debugging (node-devtools-cli)

For debugging Node.js API servers, backends, or scripts:

# 1. Connect to process (by PID, name, or Docker)
node-devtools-cli --session-id backend-debug debug connect --pid 12345
node-devtools-cli --session-id backend-debug debug connect --process-name "server.js"

# 2. Tracepoint on route handler or service
node-devtools-cli --session-id backend-debug debug put-tracepoint \
  --url-pattern "routes/api.ts" \
  --line-number 42

# 3. Exception monitoring
node-devtools-cli --session-id backend-debug debug put-exceptionpoint --state uncaught

# 4. Console logs from Node process
node-devtools-cli --session-id backend-debug --json debug get-logs
node-devtools-cli --session-id backend-debug --json debug get-logs --search "error"

# 5. Retrieve snapshots (after triggering the code path)
node-devtools-cli --session-id backend-debug --json debug get-probe-snapshots
node-devtools-cli --session-id backend-debug --json debug get-probe-snapshots --types tracepoint,exceptionpoint

# 6. Status and cleanup
node-devtools-cli --session-id backend-debug debug status
node-devtools-cli debug disconnect


urlPattern in Node context matches script file paths (e.g., server.js, routes/users.ts). See node-devtools-cli skill for full reference.

Error Investigation
browser-devtools-cli content take-screenshot --name "error-state"
browser-devtools-cli content get-as-html --selector ".error-container"

Basic Debugging Workflow
Reproduce: Navigate to the problematic page
Capture: Take screenshot of current state
Inspect Console: Check for JavaScript errors
Analyze Network: Look for failed requests
Investigate: Run diagnostic JavaScript
Document: Summarize findings with evidence
# Quick debug workflow
browser-devtools-cli navigation go-to --url "https://example.com"
browser-devtools-cli content take-screenshot --name "initial"
browser-devtools-cli --json o11y get-console-messages --type warning
browser-devtools-cli --json o11y get-http-requests --status '{"min":400}'

Advanced Debugging Workflow (Non-Blocking)
1. Set Up Probes
SESSION="--session-id debug-session"

# Navigate to app
browser-devtools-cli $SESSION navigation go-to --url "http://localhost:3000"

# Tracepoint on a function
browser-devtools-cli $SESSION debug put-tracepoint \
  --url-pattern "app.js" \
  --line-number 42

# Exception monitoring
browser-devtools-cli $SESSION debug put-exceptionpoint --state uncaught

2. Add Watch Expressions
browser-devtools-cli $SESSION debug add-watch --expression "this"
browser-devtools-cli $SESSION debug add-watch --expression "user.id"

3. Interact with Application
browser-devtools-cli $SESSION interaction click --selector "#submit-btn"
browser-devtools-cli $SESSION sync wait-for-network-idle

4. Retrieve Snapshots
browser-devtools-cli $SESSION --json debug get-probe-snapshots
browser-devtools-cli $SESSION --json debug get-probe-snapshots --types tracepoint,exceptionpoint
browser-devtools-cli $SESSION --json debug get-probe-snapshots --from-sequence 0

5. Clean Up
browser-devtools-cli $SESSION debug clear-probes
browser-devtools-cli $SESSION debug clear-probe-snapshots
browser-devtools-cli session delete debug-session

Probe Types Summary
Probe	Purpose	Output	CLI
Tracepoint	Function calls	Stack, locals, watches	browser-devtools-cli, node-devtools-cli
Logpoint	Expression values	Evaluated result	both
Exceptionpoint	Error catching	Error, stack trace	both
Watch	Per-tracepoint expressions	watchResults in snapshot	list/remove via list-probes, remove-probe, clear-probes
Best Practices
Choose the right CLI: Use browser-devtools-cli for frontend/page debugging; use node-devtools-cli for Node.js backend/API debugging
Always check console for errors first
Filter network requests to relevant endpoints
Take screenshots before and after actions (browser)
Use source maps for minified/bundled code
Start with exceptions to catch errors first
Use logpoints for lightweight monitoring
Poll snapshots with --from-sequence for efficiency
Clear probes when done to avoid overhead
Document reproduction steps clearly
Weekly Installs
30
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