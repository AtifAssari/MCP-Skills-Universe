---
rating: ⭐⭐
title: otel-instrumentation
url: https://skills.sh/dash0hq/agent-skills/otel-instrumentation
---

# otel-instrumentation

skills/dash0hq/agent-skills/otel-instrumentation
otel-instrumentation
Installation
$ npx skills add https://github.com/dash0hq/agent-skills --skill otel-instrumentation
SKILL.md
OpenTelemetry Instrumentation Guide

Expert guidance for implementing high-quality, cost-efficient OpenTelemetry telemetry.

Rules & Quick Reference
Use Case / Rule	Description
telemetry	Entrypoint — signal types, correlation, and navigation
resolve-values	Resolving configuration values from the codebase
resources	Resource attributes — service identity and environment
k8s	Kubernetes deployment — downward API, pod spec
spans	Spans — naming, kind, status, and hygiene
logs	Logs — structured logging, severity, trace correlation
metrics	Metrics — instrument types, naming, units, cardinality
sensitive-data	Sensitive data — PII prevention, sanitization, redaction
validation	Telemetry validation — post-deployment verification checklist
nodejs	Node.js instrumentation setup
go	Go instrumentation setup
python	Python instrumentation setup
java	Java instrumentation setup
scala	Scala instrumentation setup
dotnet	.NET instrumentation setup
ruby	Ruby instrumentation setup
php	PHP instrumentation setup
browser	Browser instrumentation setup
nextjs	Next.js full-stack instrumentation (App Router)
Official documentation
OpenTelemetry Documentation
Semantic Conventions
Dash0 Integration Hub
Getting started

Follow these steps when instrumenting an application from scratch:

Pick your SDK rule — choose the language-specific rule from the table above (e.g., nodejs, python).
Set up resource attributes — define service identity and environment per resources.
Add spans, metrics, and logs — instrument your code following spans, metrics, and logs.
Guard sensitive data — scrub PII before export per sensitive-data.
Validate — confirm telemetry reaches the backend using the checklist in validation.

The snippet below shows a complete span with attributes and status for Node.js — see nodejs for full setup including SDK initialisation, exporter configuration, and auto-instrumentation:

const { trace, SpanStatusCode } = require('@opentelemetry/api');
const tracer = trace.getTracer('my-service', '1.0.0');

tracer.startActiveSpan('operation-name', async (span) => {
  try {
    span.setAttribute('user.id', userId);
    span.setAttribute('order.id', orderId);

    const result = await processOrder(orderId);

    span.setAttribute('order.status', result.status);
    span.setStatus({ code: SpanStatusCode.OK });
    return result;
  } catch (err) {
    span.setStatus({ code: SpanStatusCode.ERROR, message: err.message });
    span.recordException(err);
    throw err;
  } finally {
    span.end();
  }
});

Key principles
Signal density over volume

Every telemetry item should serve one of three purposes:

Detect - Help identify that something is wrong
Localize - Help pinpoint where the problem is
Explain - Help understand why it happened

If it doesn't serve one of these purposes, don't emit it.

Sample in the pipeline, not the SDK

Use the AlwaysOn sampler (the default) in every SDK. Do not configure SDK-side samplers — they make irreversible decisions before the outcome of a request is known. Defer all sampling to the Collector, where policies can be changed centrally without redeploying applications.

SDK (AlwaysOn)  →  Collector (sampling)  →  Backend (retention)
     ↓                    ↓                       ↓
  All spans         Head or tail            Storage policies
  exported          sampling applied

Weekly Installs
214
Repository
dash0hq/agent-skills
GitHub Stars
50
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn