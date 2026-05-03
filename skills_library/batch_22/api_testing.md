---
title: api-testing
url: https://skills.sh/serkan-ozal/browser-devtools-skills/api-testing
---

# api-testing

skills/serkan-ozal/browser-devtools-skills/api-testing
api-testing
Installation
$ npx skills add https://github.com/serkan-ozal/browser-devtools-skills --skill api-testing
SKILL.md
API Testing Skill

Test API integrations by mocking responses, intercepting requests, and monitoring network traffic.

When to Use

This skill activates when:

User wants to test API integrations
User needs to mock backend responses
User wants to simulate error scenarios
User asks about request interception
User needs to test offline behavior
Capabilities
Response Mocking
browser-devtools-cli stub mock-http-response \
  --pattern "**/api/users" \
  --response '{"action":"fulfill","status":200,"body":[{"id":1,"name":"Test"}]}'

Request Interception
browser-devtools-cli stub intercept-http-request \
  --pattern "**/api/**" \
  --modifications '{"headers":{"Authorization":"Bearer token"}}'

Network Monitoring
browser-devtools-cli --json o11y get-http-requests
browser-devtools-cli --json o11y get-http-requests --resource-type fetch
browser-devtools-cli --json o11y get-http-requests --status '{"min":400}'

Stub Management
browser-devtools-cli stub list
browser-devtools-cli stub clear --stub-id <id>
browser-devtools-cli stub clear

Common Scenarios
Mock Successful Response
browser-devtools-cli stub mock-http-response \
  --pattern "**/api/users" \
  --response '{"action":"fulfill","status":200,"body":[{"id":1,"name":"Test"}]}'

Simulate Server Error
browser-devtools-cli stub mock-http-response \
  --pattern "**/api/checkout" \
  --response '{"action":"fulfill","status":500,"body":{"error":"Internal Server Error"}}'

Simulate 404 Not Found
browser-devtools-cli stub mock-http-response \
  --pattern "**/api/missing" \
  --response '{"action":"fulfill","status":404,"body":{"error":"Not Found"}}'

Simulate Network Timeout
browser-devtools-cli stub mock-http-response \
  --pattern "**/api/slow-endpoint" \
  --response '{"action":"abort","abortErrorCode":"timedout"}'

Simulate Connection Failed
browser-devtools-cli stub mock-http-response \
  --pattern "**/api/offline" \
  --response '{"action":"abort","abortErrorCode":"connectionfailed"}'

Add Auth Header
browser-devtools-cli stub intercept-http-request \
  --pattern "**/api/**" \
  --modifications '{"headers":{"Authorization":"Bearer test-token"}}'

Modify Request Body
browser-devtools-cli stub intercept-http-request \
  --pattern "**/api/submit" \
  --modifications '{"body":{"injected":"value"}}'

Add Delay
browser-devtools-cli stub mock-http-response \
  --pattern "**/api/slow" \
  --response '{"action":"fulfill","status":200,"body":{}}' \
  --delay-ms 3000

Simulate Flaky API
browser-devtools-cli stub mock-http-response \
  --pattern "**/api/unreliable" \
  --response '{"action":"fulfill","status":503}' \
  --chance 0.3

One-Shot Mock
browser-devtools-cli stub mock-http-response \
  --pattern "**/api/once" \
  --response '{"action":"fulfill","status":200,"body":{"first":true}}' \
  --times 1

Testing Workflow
SESSION="--session-id api-test"

# 1. Setup mocks before navigation
browser-devtools-cli $SESSION stub mock-http-response \
  --pattern "**/api/users" \
  --response '{"action":"fulfill","status":200,"body":[{"id":1,"name":"Mock User"}]}'

# 2. Navigate to application
browser-devtools-cli $SESSION navigation go-to --url "https://app.example.com"
browser-devtools-cli $SESSION sync wait-for-network-idle

# 3. Interact with the app
browser-devtools-cli $SESSION interaction click --selector "#load-users"
browser-devtools-cli $SESSION sync wait-for-network-idle

# 4. Check network requests
browser-devtools-cli $SESSION --json o11y get-http-requests

# 5. Verify UI shows mocked data
browser-devtools-cli $SESSION content get-as-text --selector ".user-list"

# 6. List active stubs
browser-devtools-cli $SESSION stub list

# 7. Clear all stubs
browser-devtools-cli $SESSION stub clear

# 8. Cleanup
browser-devtools-cli session delete api-test

Error Testing Workflow
SESSION="--session-id error-test"

# Mock error response
browser-devtools-cli $SESSION stub mock-http-response \
  --pattern "**/api/checkout" \
  --response '{"action":"fulfill","status":500,"body":{"error":"Payment failed"}}'

# Navigate and trigger error
browser-devtools-cli $SESSION navigation go-to --url "https://app.example.com/checkout"
browser-devtools-cli $SESSION interaction click --selector "#pay-button"
browser-devtools-cli $SESSION sync wait-for-network-idle

# Check error handling in UI
browser-devtools-cli $SESSION content take-screenshot --name "error-state"
browser-devtools-cli $SESSION content get-as-text --selector ".error-message"

# Cleanup
browser-devtools-cli $SESSION stub clear
browser-devtools-cli session delete error-test

Debugging Backend During API Tests

When testing against a real backend and need to debug why an endpoint fails or returns unexpected data, use node-devtools-cli:

# Connect to API server process
node-devtools-cli --session-id api-debug debug connect --process-name "api"

# Set tracepoint on the handler
node-devtools-cli --session-id api-debug debug put-tracepoint \
  --url-pattern "routes/users.ts" \
  --line-number 42

# Trigger the API from browser (or curl), then get snapshots
node-devtools-cli --session-id api-debug --json debug get-probe-snapshots

# Or inspect backend console logs
node-devtools-cli --session-id api-debug --json debug get-logs --search "error"

Best Practices
Use specific patterns to avoid mocking unintended requests
Clear stubs after tests to prevent interference
List stubs to debug unexpected behavior
Use times limit for one-shot mocks
Add delays to test loading states
Test error scenarios not just happy paths
Set up mocks before navigation for first-load testing
Monitor actual requests to verify mocks are working
Weekly Installs
28
Repository
serkan-ozal/bro…s-skills
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass