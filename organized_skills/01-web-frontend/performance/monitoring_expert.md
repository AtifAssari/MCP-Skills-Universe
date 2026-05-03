---
rating: ⭐⭐
title: monitoring-expert
url: https://skills.sh/jeffallan/claude-skills/monitoring-expert
---

# monitoring-expert

skills/jeffallan/claude-skills/monitoring-expert
monitoring-expert
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill monitoring-expert
Summary

Comprehensive monitoring, logging, metrics, tracing, and performance testing implementation for production systems.

Covers structured logging (Pino/JSON), Prometheus metrics (counters, histograms, gauges), and OpenTelemetry distributed tracing with span instrumentation
Includes Prometheus alerting rule configuration, RED/USE dashboard design patterns, and health check endpoint setup
Provides load testing with k6 and Artillery, application profiling for CPU/memory bottlenecks, and capacity planning guidance
Enforces best practices: correlation IDs for request tracking, no sensitive data in logs, alert thresholds on critical paths to prevent alert fatigue
SKILL.md
Monitoring Expert

Observability and performance specialist implementing comprehensive monitoring, alerting, tracing, and performance testing systems.

Core Workflow
Assess — Identify what needs monitoring (SLIs, critical paths, business metrics)
Instrument — Add logging, metrics, and traces to the application (see examples below)
Collect — Configure aggregation and storage (Prometheus scrape, log shipper, OTLP endpoint); verify data arrives before proceeding
Visualize — Build dashboards using RED (Rate/Errors/Duration) or USE (Utilization/Saturation/Errors) methods
Alert — Define threshold and anomaly alerts on critical paths; validate no false-positive flood before shipping
Quick-Start Examples
Structured Logging (Node.js / Pino)
import pino from 'pino';

const logger = pino({ level: 'info' });

// Good — structured fields, includes correlation ID
logger.info({ requestId: req.id, userId: req.user.id, durationMs: elapsed }, 'order.created');

// Bad — string interpolation, no correlation
console.log(`Order created for user ${userId}`);

Prometheus Metrics (Node.js)
import { Counter, Histogram, register } from 'prom-client';

const httpRequests = new Counter({
  name: 'http_requests_total',
  help: 'Total HTTP requests',
  labelNames: ['method', 'route', 'status'],
});

const httpDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request latency',
  labelNames: ['method', 'route'],
  buckets: [0.05, 0.1, 0.3, 0.5, 1, 2, 5],
});

// Instrument a route
app.use((req, res, next) => {
  const end = httpDuration.startTimer({ method: req.method, route: req.path });
  res.on('finish', () => {
    httpRequests.inc({ method: req.method, route: req.path, status: res.statusCode });
    end();
  });
  next();
});

// Expose scrape endpoint
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});

OpenTelemetry Tracing (Node.js)
import { NodeSDK } from '@opentelemetry/sdk-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { trace } from '@opentelemetry/api';

const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter({ url: 'http://jaeger:4318/v1/traces' }),
});
sdk.start();

// Manual span around a critical operation
const tracer = trace.getTracer('order-service');
async function processOrder(orderId) {
  const span = tracer.startSpan('order.process');
  span.setAttribute('order.id', orderId);
  try {
    const result = await db.saveOrder(orderId);
    span.setStatus({ code: SpanStatusCode.OK });
    return result;
  } catch (err) {
    span.recordException(err);
    span.setStatus({ code: SpanStatusCode.ERROR });
    throw err;
  } finally {
    span.end();
  }
}

Prometheus Alerting Rule
groups:
  - name: api.rules
    rules:
      - alert: HighErrorRate
        expr: |
          rate(http_requests_total{status=~"5.."}[5m])
          / rate(http_requests_total[5m]) > 0.05
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Error rate above 5% on {{ $labels.route }}"

k6 Load Test
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '1m', target: 50 },   // ramp up
    { duration: '5m', target: 50 },   // sustained load
    { duration: '1m', target: 0 },    // ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95th percentile < 500 ms
    http_req_failed:   ['rate<0.01'],  // error rate < 1%
  },
};

export default function () {
  const res = http.get('https://api.example.com/orders');
  check(res, { 'status is 200': (r) => r.status === 200 });
  sleep(1);
}

Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Logging	references/structured-logging.md	Pino, JSON logging
Metrics	references/prometheus-metrics.md	Counter, Histogram, Gauge
Tracing	references/opentelemetry.md	OpenTelemetry, spans
Alerting	references/alerting-rules.md	Prometheus alerts
Dashboards	references/dashboards.md	RED/USE method, Grafana
Performance Testing	references/performance-testing.md	Load testing, k6, Artillery, benchmarks
Profiling	references/application-profiling.md	CPU/memory profiling, bottlenecks
Capacity Planning	references/capacity-planning.md	Scaling, forecasting, budgets
Constraints
MUST DO
Use structured logging (JSON)
Include request IDs for correlation
Set up alerts for critical paths
Monitor business metrics, not just technical
Use appropriate metric types (counter/gauge/histogram)
Implement health check endpoints
MUST NOT DO
Log sensitive data (passwords, tokens, PII)
Alert on every error (alert fatigue)
Use string interpolation in logs (use structured fields)
Skip correlation IDs in distributed systems

Documentation

Weekly Installs
2.1K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass