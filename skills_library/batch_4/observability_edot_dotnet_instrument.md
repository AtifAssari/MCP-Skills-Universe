---
title: observability-edot-dotnet-instrument
url: https://skills.sh/elastic/agent-skills/observability-edot-dotnet-instrument
---

# observability-edot-dotnet-instrument

skills/elastic/agent-skills/observability-edot-dotnet-instrument
observability-edot-dotnet-instrument
Installation
$ npx skills add https://github.com/elastic/agent-skills --skill observability-edot-dotnet-instrument
SKILL.md
EDOT .NET Instrumentation

Read the setup guide before making changes:

EDOT .NET setup
EDOT .NET configuration
OpenTelemetry .NET instrumentation
Guidelines
Add NuGet packages: Elastic.OpenTelemetry and OpenTelemetry.Instrumentation.AspNetCore (for ASP.NET Core apps)
Register EDOT in startup: call builder.AddElasticOpenTelemetry() on the IHostApplicationBuilder (in Program.cs or equivalent). Without this, no telemetry is collected
Set exactly three required environment variables:
OTEL_SERVICE_NAME
OTEL_EXPORTER_OTLP_ENDPOINT — must be the managed OTLP endpoint or EDOT Collector URL. Never use an APM Server URL (no apm-server, no :8200, no /intake/v2/events)
OTEL_EXPORTER_OTLP_HEADERS — "Authorization=ApiKey <key>" or "Authorization=Bearer <token>"
Do NOT set OTEL_TRACES_EXPORTER, OTEL_METRICS_EXPORTER, or OTEL_LOGS_EXPORTER — the defaults are already correct
Do NOT manually configure TracerProvider or MeterProvider — AddElasticOpenTelemetry() handles everything
Never run both classic Elastic APM agent (Elastic.Apm.*) and EDOT on the same application
Examples

See the EDOT .NET setup guide for complete examples.

Weekly Installs
350
Repository
elastic/agent-skills
GitHub Stars
451
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass