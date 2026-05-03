---
title: observability-edot-python-instrument
url: https://skills.sh/elastic/agent-skills/observability-edot-python-instrument
---

# observability-edot-python-instrument

skills/elastic/agent-skills/observability-edot-python-instrument
observability-edot-python-instrument
Installation
$ npx skills add https://github.com/elastic/agent-skills --skill observability-edot-python-instrument
SKILL.md
EDOT Python Instrumentation

Read the setup guide before making changes:

EDOT Python setup
EDOT Python configuration
OpenTelemetry Python auto-instrumentation
Guidelines
Install elastic-opentelemetry via pip (add to requirements.txt or equivalent)
Run edot-bootstrap --action=install during image build to install auto-instrumentation packages for detected libraries
Wrap the application entrypoint with opentelemetry-instrument — e.g. opentelemetry-instrument gunicorn app:app or opentelemetry-instrument python app.py. Without this, no telemetry is collected
Set exactly three required environment variables:
OTEL_SERVICE_NAME
OTEL_EXPORTER_OTLP_ENDPOINT — must be the managed OTLP endpoint or EDOT Collector URL. Never use an APM Server URL (no apm-server, no :8200, no /intake/v2/events)
OTEL_EXPORTER_OTLP_HEADERS — "Authorization=ApiKey <key>" or "Authorization=Bearer <token>"
Do NOT set OTEL_TRACES_EXPORTER, OTEL_METRICS_EXPORTER, or OTEL_LOGS_EXPORTER — the defaults are already correct
Do NOT add code-level SDK setup (no TracerProvider, no configure_azure_monitor, etc.) — opentelemetry-instrument handles everything
Never run both classic elastic-apm and EDOT on the same application
Examples

See the EDOT Python setup guide for complete examples.

Weekly Installs
357
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