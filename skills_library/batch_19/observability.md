---
title: observability
url: https://skills.sh/dralgorhythm/claude-agentic-framework/observability
---

# observability

skills/dralgorhythm/claude-agentic-framework/observability
observability
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill observability
SKILL.md
Observability
Three Pillars
1. Logs

Discrete events with context.

{
  "timestamp": "2024-01-01T12:00:00Z",
  "level": "error",
  "message": "Failed to process order",
  "orderId": "123",
  "error": "Payment declined",
  "traceId": "abc123"
}

2. Metrics

Numeric measurements over time.

http_requests_total{method="GET", status="200"} 1234
http_request_duration_seconds{quantile="0.95"} 0.23

3. Traces

Request flow through services.

Trace: abc123
├── API Gateway (50ms)
│   ├── Auth Service (10ms)
│   └── Order Service (35ms)
│       └── Database (20ms)

OpenTelemetry Setup
import { NodeSDK } from '@opentelemetry/sdk-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';

const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter({
    url: 'http://collector:4318/v1/traces',
  }),
  serviceName: 'my-service',
});

sdk.start();

Key Metrics
RED Method (Request-focused)
Rate: Requests per second
Errors: Failed requests per second
Duration: Request latency
USE Method (Resource-focused)
Utilization: % time busy
Saturation: Queue depth
Errors: Error count
Alerting
Good Alerts
Actionable: Something can be done
Urgent: Needs immediate attention
Specific: Clear what's wrong
Alert Template
alert: HighErrorRate
expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.01
for: 5m
labels:
  severity: critical
annotations:
  summary: "High error rate on {{ $labels.service }}"
  description: "Error rate is {{ $value | humanizePercentage }}"

Dashboards

Essential panels:

Request rate
Error rate
Latency (P50, P95, P99)
Saturation (CPU, memory)
Active alerts
Weekly Installs
35
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass