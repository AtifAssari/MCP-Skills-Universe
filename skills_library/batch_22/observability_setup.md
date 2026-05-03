---
title: observability-setup
url: https://skills.sh/patricio0312rev/skills/observability-setup
---

# observability-setup

skills/patricio0312rev/skills/observability-setup
observability-setup
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill observability-setup
SKILL.md
Observability Setup

Implement the three pillars: Traces, Metrics, and Logs.

OpenTelemetry Tracing
// tracing.ts
import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";
import { Resource } from "@opentelemetry/resources";
import { SemanticResourceAttributes } from "@opentelemetry/semantic-conventions";
import { registerInstrumentations } from "@opentelemetry/instrumentation";
import { HttpInstrumentation } from "@opentelemetry/instrumentation-http";
import { ExpressInstrumentation } from "@opentelemetry/instrumentation-express";
import { PrismaInstrumentation } from "@prisma/instrumentation";

const provider = new NodeTracerProvider({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: "my-api",
    [SemanticResourceAttributes.SERVICE_VERSION]: "1.0.0",
  }),
});

registerInstrumentations({
  instrumentations: [
    new HttpInstrumentation(),
    new ExpressInstrumentation(),
    new PrismaInstrumentation(),
  ],
});

provider.register();

// Custom spans
import { trace } from "@opentelemetry/api";

const tracer = trace.getTracer("my-app");

async function processOrder(orderId: string) {
  const span = tracer.startSpan("processOrder");
  span.setAttribute("order.id", orderId);

  try {
    await validateOrder(orderId);
    await chargePayment(orderId);
    await fulfillOrder(orderId);
    span.setStatus({ code: 0 }); // OK
  } catch (error) {
    span.setStatus({ code: 2, message: error.message }); // ERROR
    throw error;
  } finally {
    span.end();
  }
}

Prometheus Metrics
// metrics.ts
import { Registry, Counter, Histogram, Gauge } from "prom-client";

const register = new Registry();

// HTTP request counter
export const httpRequestCounter = new Counter({
  name: "http_requests_total",
  help: "Total HTTP requests",
  labelNames: ["method", "route", "status_code"],
  registers: [register],
});

// HTTP request duration
export const httpRequestDuration = new Histogram({
  name: "http_request_duration_seconds",
  help: "HTTP request duration in seconds",
  labelNames: ["method", "route", "status_code"],
  buckets: [0.1, 0.5, 1, 2, 5, 10],
  registers: [register],
});

// Active connections
export const activeConnections = new Gauge({
  name: "active_connections",
  help: "Number of active connections",
  registers: [register],
});

// Business metrics
export const ordersProcessed = new Counter({
  name: "orders_processed_total",
  help: "Total orders processed",
  labelNames: ["status"],
  registers: [register],
});

// Middleware
app.use((req, res, next) => {
  const start = Date.now();

  res.on("finish", () => {
    const duration = (Date.now() - start) / 1000;
    const route = req.route?.path || "unknown";

    httpRequestCounter.inc({
      method: req.method,
      route,
      status_code: res.statusCode,
    });

    httpRequestDuration.observe(
      { method: req.method, route, status_code: res.statusCode },
      duration
    );
  });

  next();
});

// Metrics endpoint
app.get("/metrics", async (req, res) => {
  res.set("Content-Type", register.contentType);
  res.end(await register.metrics());
});

Structured Logging
// logger.ts
import pino from "pino";

export const logger = pino({
  level: process.env.LOG_LEVEL || "info",
  formatters: {
    level: (label) => ({ level: label }),
  },
  base: {
    service: "my-api",
    environment: process.env.NODE_ENV,
  },
});

// Usage
logger.info({ userId: "123", action: "login" }, "User logged in");
logger.error({ err: error, orderId: "456" }, "Order processing failed");

Sample Dashboard (Grafana)
{
  "dashboard": {
    "title": "API Overview",
    "panels": [
      {
        "title": "Request Rate",
        "targets": [{
          "expr": "rate(http_requests_total[5m])"
        }]
      },
      {
        "title": "Error Rate",
        "targets": [{
          "expr": "rate(http_requests_total{status_code=~"5.."}[5m])"
        }]
      },
      {
        "title": "p95 Latency",
        "targets": [{
          "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))"
        }]
      },
      {
        "title": "Active Connections",
        "targets": [{
          "expr": "active_connections"
        }]
      }
    ]
  }
}

Alert Candidates
# alerts.yml
groups:
  - name: api_alerts
    interval: 30s
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status_code=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"

      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 2
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "p95 latency above 2s"

      - alert: LowAvailability
        expr: rate(http_requests_total{status_code="200"}[5m]) / rate(http_requests_total[5m]) < 0.95
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Availability below 95%"

Output Checklist
 OpenTelemetry tracing configured
 Prometheus metrics instrumented
 Structured logging implemented
 Sample dashboards created
 Alert rules defined
 Metrics endpoint exposed
 Instrumentation tested ENDFILE
Weekly Installs
100
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass