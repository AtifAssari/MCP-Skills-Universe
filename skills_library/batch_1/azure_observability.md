---
title: azure-observability
url: https://skills.sh/microsoft/azure-skills/azure-observability
---

# azure-observability

skills/microsoft/azure-skills/azure-observability
azure-observability
Originally frommicrosoft/github-copilot-for-azure
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-observability
Summary

Query metrics, logs, and traces across Azure Monitor, Application Insights, and Log Analytics.

Access metrics, KQL log queries, and distributed tracing through MCP tools or Azure CLI commands
Supports Application Insights for APM and performance analysis, Log Analytics for custom KQL queries, and Azure Monitor for infrastructure metrics
Includes common KQL query patterns for errors, request performance, and resource usage monitoring
Workbooks integration for building interactive observability dashboards and reports
SKILL.md
Azure Observability Services
Services
Service	Use When	MCP Tools	CLI
Azure Monitor	Metrics, alerts, dashboards	azure__monitor	az monitor
Application Insights	APM, distributed tracing	azure__applicationinsights	az monitor app-insights
Log Analytics	Log queries, KQL	azure__kusto	az monitor log-analytics
Alerts	Notifications, actions	-	az monitor alert
Workbooks	Interactive reports	azure__workbooks	-
MCP Server (Preferred)

When Azure MCP is enabled:

Monitor
azure__monitor with command monitor_metrics_query - Query metrics
azure__monitor with command monitor_logs_query - Query logs with KQL
Application Insights
azure__applicationinsights with command applicationinsights_component_list - List App Insights resources
Log Analytics
azure__kusto with command kusto_cluster_list - List clusters
azure__kusto with command kusto_query - Execute KQL queries

If Azure MCP is not enabled: Run /azure:setup or enable via /mcp.

CLI Reference
# List Log Analytics workspaces
az monitor log-analytics workspace list --output table

# Query logs with KQL
az monitor log-analytics query \
  --workspace WORKSPACE_ID \
  --analytics-query "AzureActivity | take 10"

# List Application Insights
az monitor app-insights component list --output table

# List alerts
az monitor alert list --output table

# Query metrics
az monitor metrics list \
  --resource RESOURCE_ID \
  --metric "Percentage CPU"

Common KQL Queries
// Recent errors
AppExceptions
| where TimeGenerated > ago(1h)
| project TimeGenerated, Message, StackTrace
| order by TimeGenerated desc

// Request performance
AppRequests
| where TimeGenerated > ago(1h)
| summarize avg(DurationMs), count() by Name
| order by avg_DurationMs desc

// Resource usage
AzureMetrics
| where TimeGenerated > ago(1h)
| where MetricName == "Percentage CPU"
| summarize avg(Average) by Resource

Monitoring Strategy
What to Monitor	Service	Metric/Log
Application errors	App Insights	Exceptions, failed requests
Performance	App Insights	Response time, dependencies
Infrastructure	Azure Monitor	CPU, memory, disk
Security	Log Analytics	Sign-ins, audit logs
Costs	Cost Management	Budget alerts
SDK Quick References

For programmatic access to monitoring services, see the condensed SDK guides:

OpenTelemetry: Python | TypeScript | Python Exporter
Monitor Query: Python | Java
Log Ingestion: Python | Java
App Insights Mgmt: .NET
Service Details

For deep documentation on specific services:

Application Insights setup -> appinsights-instrumentation skill
KQL query patterns -> Log Analytics KQL documentation
Alert configuration -> Azure Monitor alerts documentation
Weekly Installs
13.4K
Repository
microsoft/azure-skills
GitHub Stars
796
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass