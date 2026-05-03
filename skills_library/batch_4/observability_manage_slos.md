---
title: observability-manage-slos
url: https://skills.sh/elastic/agent-skills/observability-manage-slos
---

# observability-manage-slos

skills/elastic/agent-skills/observability-manage-slos
observability-manage-slos
Installation
$ npx skills add https://github.com/elastic/agent-skills --skill observability-manage-slos
SKILL.md
Service-Level Objectives (SLOs)

Create and manage SLOs in Elastic Observability. SLOs track service performance against measurable targets using service-level indicators (SLIs) computed from Elasticsearch data.

Authentication

SLO operations go through the Kibana API. Authenticate with either an API key or basic auth:

# API key
curl -H "Authorization: ApiKey <base64-encoded-key>" -H "kbn-xsrf: true" <KIBANA_URL>/api/observability/slos

# Basic auth
curl -u "$KIBANA_USER:$KIBANA_PASSWORD" -H "kbn-xsrf: true" <KIBANA_URL>/api/observability/slos


For non-default spaces, prefix the path: /s/<space_id>/api/observability/slos.

Include kbn-xsrf: true on all POST, PUT, and DELETE requests.

SLI Types
Type	API value	Use case
Custom KQL	sli.kql.custom	Raw logs — good/total using KQL queries
Custom metric	sli.metric.custom	Metric fields — equations with aggregations
Timeslice metric	sli.metric.timeslice	Metric fields — per-slice threshold check
Histogram metric	sli.histogram.custom	Histogram fields — range/value_count
APM latency	sli.apm.transactionDuration	APM — latency threshold
APM availability	sli.apm.transactionErrorRate	APM — success rate
Synthetics availability	sli.synthetics.availability	Synthetics monitors — uptime percentage
Guidelines
objective.target is a decimal between 0 and 1 (for example 0.995 for 99.5%).
Timeslice metric indicators require budgetingMethod: "timeslices".
Updating an SLO resets the underlying transform — historical data is recomputed.
The cluster needs nodes with both transform and ingest roles.
Use POST .../slos/{id}/_reset when an SLO is stuck or after index mapping changes.
Group-by SLOs create one instance per unique value — avoid high-cardinality fields.
Synthetics SLOs are auto-grouped by monitor and location; do not set groupBy manually.
Burn rate alert rules are not auto-created using the API — set them up separately.
Additional references

For official documentation, refer to the following resources:

SLO documentation
Service-level objectives (SLOs) — concepts, SLI types, budgeting methods, and dashboard panels.
Create an SLO — step-by-step guide for creating SLOs in the Kibana UI.
View and manage SLOs — searching, filtering, and managing existing SLOs.
Kibana SLO API
Create an SLO — full request body schema with all SLI type payloads.
Get an SLO | Update | Delete | Reset
Enable | Disable | Get definitions
Troubleshooting and access
Troubleshoot SLOs
Configure SLO access
Create an SLO burn rate rule
Weekly Installs
393
Repository
elastic/agent-skills
GitHub Stars
451
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass