---
title: observability
url: https://skills.sh/serkan-ozal/browser-devtools-skills/observability
---

# observability

skills/serkan-ozal/browser-devtools-skills/observability
observability
Installation
$ npx skills add https://github.com/serkan-ozal/browser-devtools-skills --skill observability
SKILL.md
Observability Skill

Monitor and debug web and Node.js applications using OpenTelemetry, console logs, network requests, and distributed tracing.

When to Use

This skill activates when:

User asks about distributed tracing
User wants to correlate frontend and backend requests
User mentions OpenTelemetry, Jaeger, Zipkin, or tracing
User needs to debug request flow across services
User wants to monitor application behavior
Capabilities
Distributed Tracing
browser-devtools-cli o11y get-trace-id
browser-devtools-cli o11y new-trace-id
browser-devtools-cli o11y set-trace-id --trace-id "abc123def456..."

Console Monitoring
browser-devtools-cli o11y get-console-messages
browser-devtools-cli --json o11y get-console-messages --type warning
browser-devtools-cli --json o11y get-console-messages --search "error"

Network Observability
browser-devtools-cli --json o11y get-http-requests
browser-devtools-cli --json o11y get-http-requests --resource-type fetch
browser-devtools-cli --json o11y get-http-requests --status '{"min":400}'

Performance Metrics
browser-devtools-cli --json o11y get-web-vitals
browser-devtools-cli --json o11y get-web-vitals --wait-ms 3000
browser-devtools-cli --json o11y get-web-vitals --include-debug

OpenTelemetry Integration
Trace Context

Browser DevTools MCP can inject and extract W3C Trace Context headers:

traceparent: Contains trace-id, span-id, and trace flags
tracestate: Vendor-specific trace information
Correlation Flow
Browser Session
    │
    ├─► trace-id: abc123
    │
    ▼
Frontend Request
    │
    ├─► Header: traceparent: 00-abc123-def456-01
    │
    ▼
Backend Service
    │
    ├─► Logs with trace-id: abc123
    │
    ▼
Observability Platform
    │
    └─► Full trace visualization

Backend Observability (node-devtools-cli)

When correlating frontend traces with backend behavior, use node-devtools-cli to inspect Node.js processes:

# Connect to backend
node-devtools-cli --session-id backend debug connect --pid 12345

# Get console logs from Node process (can correlate with trace ID in logs)
node-devtools-cli --session-id backend --json debug get-logs
node-devtools-cli --session-id backend --json debug get-logs --search "trace"

# Optional: set tracepoints on backend handlers to capture call context
node-devtools-cli --session-id backend debug put-tracepoint \
  --url-pattern "routes/api.ts" \
  --line-number 25

Debugging Workflow
SESSION="--session-id trace-session"

# 1. Generate new trace ID
browser-devtools-cli $SESSION o11y new-trace-id

# 2. Navigate (requests will carry trace ID)
browser-devtools-cli $SESSION navigation go-to --url "https://app.example.com"
browser-devtools-cli $SESSION sync wait-for-network-idle

# 3. Perform actions
browser-devtools-cli $SESSION interaction click --selector "#submit"
browser-devtools-cli $SESSION sync wait-for-network-idle

# 4. Get trace ID for backend correlation
browser-devtools-cli $SESSION o11y get-trace-id

# 5. Check console errors
browser-devtools-cli $SESSION --json o11y get-console-messages --type error

# 6. Check network requests
browser-devtools-cli $SESSION --json o11y get-http-requests

# 7. Cleanup
browser-devtools-cli session delete trace-session

Use Existing Trace ID
SESSION="--session-id trace-session"

# Set trace ID from backend
browser-devtools-cli $SESSION o11y set-trace-id --trace-id "abc123def456789..."

# Navigate (requests will use this trace ID)
browser-devtools-cli $SESSION navigation go-to --url "https://app.example.com"

# All subsequent requests carry the trace ID
browser-devtools-cli $SESSION interaction click --selector "#api-call"

Configuration
Environment Variables
Variable	Description	Default
OTEL_ENABLE	Enable OpenTelemetry	false
OTEL_SERVICE_NAME	Service identifier	frontend
OTEL_EXPORTER_TYPE	Export destination	none
OTEL_EXPORTER_HTTP_URL	Collector endpoint	-
OTEL_EXPORTER_HTTP_HEADERS	Auth headers	-
Exporter Types
Type	Description
none	Disabled
console	Log to console
otlp/http	Send to OTLP collector
Common Platforms
Jaeger
OTEL_EXPORTER_HTTP_URL=http://localhost:4318

Grafana Tempo
OTEL_EXPORTER_HTTP_URL=http://tempo:4318

Honeycomb
OTEL_EXPORTER_HTTP_URL=https://api.honeycomb.io
OTEL_EXPORTER_HTTP_HEADERS=x-honeycomb-team=YOUR_API_KEY

Datadog
OTEL_EXPORTER_HTTP_URL=http://localhost:4318

Best Practices
Generate new trace IDs for each test scenario
Document trace IDs in bug reports
Check console first for JavaScript errors
Filter network requests to relevant endpoints
Correlate timestamps between frontend and backend
Use structured logging with trace context
Set up OTEL exporter for full trace visibility
Weekly Installs
26
Repository
serkan-ozal/bro…s-skills
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn