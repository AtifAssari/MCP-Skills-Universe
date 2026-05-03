---
rating: ⭐⭐
title: grafana-platform-dashboard
url: https://skills.sh/boshu2/agentops/grafana-platform-dashboard
---

# grafana-platform-dashboard

skills/boshu2/agentops/grafana-platform-dashboard
grafana-platform-dashboard
Installation
$ npx skills add https://github.com/boshu2/agentops --skill grafana-platform-dashboard
SKILL.md
Grafana Platform Dashboard

Design platform operations dashboards so operators see tenant-impacting risk first, then drill into service-specific health without overload.

Quick Start

Use this skill when the user asks for platform dashboard updates and reliability checks.

Confirm dashboard target:
oc --context <ctx> get grafanadashboard -A | rg -i '<dashboard-name-or-theme>'

Export dashboard and JSON:
skills/grafana-platform-dashboard/scripts/grafanadashboard_roundtrip.sh export \
  --context <ctx> \
  --namespace <ns> \
  --name <grafanadashboard-name> \
  --out-dir /tmp/<workspace>

Edit the JSON and validate all PromQL:
skills/grafana-platform-dashboard/scripts/promql_scan_thanos.sh \
  --context <ctx> \
  --dashboard-json /tmp/<workspace>/<name>.json

Apply live safely:
skills/grafana-platform-dashboard/scripts/grafanadashboard_roundtrip.sh apply \
  --context <ctx> \
  --namespace <ns> \
  --name <grafanadashboard-name> \
  --json /tmp/<workspace>/<name>.json

Workflow
1) Lock Scope From Platform Contracts

Use the platform contract in platform-contract.md before editing panels.

Keep L1 command view constrained to critical pre-tenant-impact signals.
Use gate-aligned components first (critical CO gate, nodes, MCP, core API/etcd/ingress).
Keep service-specific sections (Crossplane, Keycloak) below L1.
2) Enforce Information Architecture

Use layout-guidelines.md:

L1: critical-only, immediate action, minimal panel budget.
L2: platform services by dependency domain.
L3: deep dives (for example future GPU dashboard), not in L1.
3) Build Queries From Known Library

Use promql-library.md:

Start from known-good queries and adapt labels minimally.
Prefer counts and action tables over decorative charts.
Filter alert noise explicitly (for example ArgoCD/GitOps) when requested.
4) Validate Before Apply

Always run the scan script after edits:

skills/grafana-platform-dashboard/scripts/promql_scan_thanos.sh \
  --context <ctx> \
  --dashboard-json <file.json> \
  --output <scan.tsv>


Pass criteria: all queries report success, zero bad/parse errors.

5) Apply and Verify Sync

Apply only after validation succeeds:

skills/grafana-platform-dashboard/scripts/grafanadashboard_roundtrip.sh apply ...
oc --context <ctx> -n <ns> get grafanadashboard <name> \
  -o jsonpath='{.status.conditions[?(@.type=="DashboardSynchronized")].status}{"|"}{.status.conditions[?(@.type=="DashboardSynchronized")].reason}{"\n"}'

6) Close With Operator-Focused Summary

Report:

What changed (panel names and intent).
Validation result (query count and failures).
Sync status and any residual risk.
Next step: promote live changes into GitOps-managed source.
Design Rules
Put critical tenant-impact predictors first.
Every red panel must imply an action path.
Avoid ambiguous panel names (for example replace “platform pods” with concrete namespace scope).
Keep L1 low-noise; move detail below or to dedicated dashboards.
Keep GPU deep diagnostics in a dedicated GPU dashboard, not mixed into L1.
References
Platform Contract
PromQL Panel Library
Layout Guidelines
Weekly Installs
129
Repository
boshu2/agentops
GitHub Stars
323
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass