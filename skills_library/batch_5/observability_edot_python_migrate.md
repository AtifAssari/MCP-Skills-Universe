---
title: observability-edot-python-migrate
url: https://skills.sh/elastic/agent-skills/observability-edot-python-migrate
---

# observability-edot-python-migrate

skills/elastic/agent-skills/observability-edot-python-migrate
observability-edot-python-migrate
Installation
$ npx skills add https://github.com/elastic/agent-skills --skill observability-edot-python-migrate
SKILL.md
EDOT Python Migration

Read the migration guide before making changes:

Migration guide
EDOT Python setup
EDOT Python configuration
Guidelines
Remove ALL classic APM references: elastic-apm from requirements, ElasticAPM(app) / elasticapm.contrib.* from application code, app.config['ELASTIC_APM'] blocks, and all ELASTIC_APM_* env vars
Install elastic-opentelemetry via pip (add to requirements.txt or equivalent)
Run edot-bootstrap --action=install during image build to install auto-instrumentation packages for detected libraries
Wrap the application entrypoint with opentelemetry-instrument — e.g. opentelemetry-instrument gunicorn app:app. Without this, no telemetry is collected
Set exactly three required environment variables:
OTEL_SERVICE_NAME (replaces ELASTIC_APM_SERVICE_NAME)
OTEL_EXPORTER_OTLP_ENDPOINT — must be the managed OTLP endpoint or EDOT Collector URL. Do NOT reuse the old ELASTIC_APM_SERVER_URL value. Never use an APM Server URL (no apm-server, no :8200, no /intake/v2/events)
OTEL_EXPORTER_OTLP_HEADERS — "Authorization=ApiKey <key>" or "Authorization=Bearer <token>" (replaces ELASTIC_APM_SECRET_TOKEN)
Do NOT set OTEL_TRACES_EXPORTER, OTEL_METRICS_EXPORTER, or OTEL_LOGS_EXPORTER — the defaults are already correct
Never run both classic elastic-apm and EDOT on the same application
Examples

See the EDOT Python migration guide for complete examples.

Weekly Installs
341
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