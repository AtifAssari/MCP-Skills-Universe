---
rating: ⭐⭐
title: litestar-metrics
url: https://skills.sh/alti3/litestar-skills/litestar-metrics
---

# litestar-metrics

skills/alti3/litestar-skills/litestar-metrics
litestar-metrics
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill litestar-metrics
SKILL.md
Metrics
Execution Workflow
Choose the metrics backend first: OpenTelemetry for OTel ecosystem integration or Prometheus for scrape-based metrics exposure.
Register instrumentation at app scope with the appropriate plugin or middleware.
Decide which routes, methods, and paths should be excluded from metrics.
Keep labels low-cardinality and group dynamic paths when needed.
Add custom dimensions or exemplars only when they materially improve observability.
Validate exporter or scrape behavior before depending on dashboards and alerts.
Core Rules
Keep instrumentation centralized at app construction.
Prefer backend defaults until concrete monitoring needs justify customization.
Avoid high-cardinality labels such as user IDs, request IDs, or raw path values.
Exclude noisy or irrelevant paths and methods intentionally.
Group dynamic paths to avoid cardinality explosion.
Treat metrics naming, units, and label sets as stable contracts.
Keep metrics concerns separate from logs, traces, and exception-response formatting.
Decision Guide
Use OpenTelemetry when the service already participates in an OTel pipeline or shared collector/exporter setup.
Use Prometheus when the service should expose a scrape endpoint directly.
Use Prometheus group_path=True when route path cardinality could explode.
Use Prometheus labels or OTel resource dimensions only when the values are stable and bounded.
Use exemplars only when the exposition format and monitoring stack actually support them.
Use litestar-logging and tracing separately when the task is not primarily metrics.
Reference Files

Read only the sections you need:

For OpenTelemetry plugin setup, provider/exporter expectations, and OTel-focused decisions, read references/open-telemetry-patterns.md.
For Prometheus middleware, controller wiring, labels, buckets, exemplars, exclusions, and path grouping, read references/prometheus-patterns.md.
Recommended Defaults
Start with built-in request instrumentation before adding domain-specific metrics.
Keep labels bounded and documented.
Exclude metrics endpoints from self-observation only when it helps reduce noise.
Group dynamic paths when cardinality would otherwise grow with route parameters.
Keep dashboard and alert assumptions close to the metric definitions they depend on.
Anti-Patterns
Emitting labels with unbounded values.
Building dashboards around unstable metric names or label keys.
Adding metrics middleware or plugins at multiple layers without intent.
Treating Prometheus and OpenTelemetry as interchangeable without considering the downstream stack.
Enabling exemplars without openmetrics support.
Measuring everything before deciding what operators actually need.
Validation Checklist
Confirm instrumentation is registered exactly once.
Confirm exporter or scrape endpoint emits baseline request metrics.
Confirm excluded paths and methods behave as intended.
Confirm path grouping and label choices keep cardinality under control.
Confirm custom labels and exemplars are bounded and supported by the stack.
Confirm dashboards and alerts map to real operational questions.
Confirm instrumentation overhead is acceptable.
Cross-Skill Handoffs
Use litestar-logging for event-level diagnostics and structured logs.
Use litestar-debugging and litestar-testing to validate instrumentation assumptions.
Use litestar-exception-handling when error-contract decisions interact with what metrics should count as failures.
Litestar References
https://docs.litestar.dev/latest/usage/metrics/index.html
https://docs.litestar.dev/latest/usage/metrics/open-telemetry.html
https://docs.litestar.dev/latest/usage/metrics/prometheus.html
Weekly Installs
13
Repository
alti3/litestar-skills
GitHub Stars
5
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass