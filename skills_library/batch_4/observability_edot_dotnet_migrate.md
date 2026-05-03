---
title: observability-edot-dotnet-migrate
url: https://skills.sh/elastic/agent-skills/observability-edot-dotnet-migrate
---

# observability-edot-dotnet-migrate

skills/elastic/agent-skills/observability-edot-dotnet-migrate
observability-edot-dotnet-migrate
Installation
$ npx skills add https://github.com/elastic/agent-skills --skill observability-edot-dotnet-migrate
SKILL.md
EDOT .NET Migration

Read the migration guide before making changes:

Migration guide
EDOT .NET setup
EDOT .NET configuration
Guidelines
Remove ALL classic APM references: Elastic.Apm.* NuGet packages (including Elastic.Apm.NetCoreAll), UseAllElasticApm() / AddAllElasticApm() calls, the ElasticApm section from appsettings.json, and all ELASTIC_APM_* env vars
Add NuGet packages: Elastic.OpenTelemetry and OpenTelemetry.Instrumentation.AspNetCore (for ASP.NET Core apps)
Register EDOT in startup: call builder.AddElasticOpenTelemetry() on the IHostApplicationBuilder (in Program.cs or equivalent). Without this, no telemetry is collected
Set exactly three required environment variables:
OTEL_SERVICE_NAME (replaces ELASTIC_APM_SERVICE_NAME / ElasticApm:ServiceName)
OTEL_EXPORTER_OTLP_ENDPOINT — must be the managed OTLP endpoint or EDOT Collector URL. Do NOT reuse the old ELASTIC_APM_SERVER_URLS value. Never use an APM Server URL (no apm-server, no :8200, no /intake/v2/events)
OTEL_EXPORTER_OTLP_HEADERS — "Authorization=ApiKey <key>" or "Authorization=Bearer <token>" (replaces ELASTIC_APM_SECRET_TOKEN)
Do NOT set OTEL_TRACES_EXPORTER, OTEL_METRICS_EXPORTER, or OTEL_LOGS_EXPORTER — the defaults are already correct
Never run both classic Elastic APM agent (Elastic.Apm.*) and EDOT on the same application
Examples

See the EDOT .NET migration guide for complete examples.

Weekly Installs
344
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