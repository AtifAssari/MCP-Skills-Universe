---
title: azure-diagnostics
url: https://skills.sh/microsoft/azure-skills/azure-diagnostics
---

# azure-diagnostics

skills/microsoft/azure-skills/azure-diagnostics
azure-diagnostics
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-diagnostics
Summary

Systematic diagnosis and remediation for Azure production issues using AppLens, Monitor, and resource health.

Covers Container Apps, Function Apps, and AKS troubleshooting with service-specific guides for image pulls, cold starts, health probes, invocation failures, and node/pod issues
Integrates AppLens (MCP) for AI-powered root cause analysis and Azure Monitor (MCP) for KQL-based log and metric queries
Provides a five-step diagnostic flow: identify symptoms, check resource health, review logs, analyze metrics, and investigate recent changes
Includes quick reference commands for activity logs, container logs, and App Insights queries, plus routing guidance for AKS-specific incidents
SKILL.md
Azure Diagnostics

AUTHORITATIVE GUIDANCE — MANDATORY COMPLIANCE

This document is the official source for debugging and troubleshooting Azure production issues. Follow these instructions to diagnose and resolve common Azure service problems systematically.

Triggers

Activate this skill when user wants to:

Debug or troubleshoot production issues
Diagnose errors in Azure services
Analyze application logs or metrics
Fix image pull, cold start, or health probe issues
Investigate why Azure resources are failing
Find root cause of application errors
Troubleshoot App Service issues (high CPU, deployment failures, crashes, slow responses, TLS/custom domains)
Respond to prompts like "troubleshoot app service", "app service high CPU", or "app service deployment failure"
Troubleshoot Azure Function Apps (invocation failures, timeouts, binding errors)
Find the App Insights or Log Analytics workspace linked to a Function App
Troubleshoot AKS clusters, nodes, pods, ingress, or Kubernetes networking issues
Troubleshoot Azure Messaging SDK issues (Event Hubs, Service Bus connection failures, AMQP errors, message lock issues)
Rules
Start with systematic diagnosis flow
Use AppLens (MCP) for AI-powered diagnostics when available
Check resource health before deep-diving into logs
Select appropriate troubleshooting guide based on service type
Document findings and attempted remediation steps
Route AKS incidents to the dedicated AKS troubleshooting document
Quick Diagnosis Flow
Identify symptoms - What's failing?
Check resource health - Is Azure healthy?
Review logs - What do logs show?
Analyze metrics - Performance patterns?
Investigate recent changes - What changed?
Troubleshooting Guides by Service
Service	Common Issues	Reference
Container Apps	Image pull failures, cold starts, health probes, port mismatches	container-apps/
App Service	High CPU, deployment failures, crashes, slow responses, TLS/custom domains	app-service/
Function Apps	App details, invocation failures, timeouts, binding errors, cold starts, missing app settings	functions/
AKS	Cluster access, nodes, kube-system, scheduling, crash loops, ingress, DNS, upgrades	AKS Troubleshooting
Messaging	Event Hubs & Service Bus SDK errors, AMQP failures, message lock, connectivity	Messaging Troubleshooting
Routing
Keep Container Apps and Function Apps diagnostics in this parent skill.
Route active AKS incidents, AKS-specific intake, evidence gathering, and remediation guidance to AKS Troubleshooting.
Route Azure Messaging SDK troubleshooting (Event Hubs, Service Bus) to Messaging Troubleshooting.
Quick Reference
Common Diagnostic Commands
# Check resource health
az resource show --ids RESOURCE_ID
# View activity log
az monitor activity-log list -g RG --max-events 20
# Container Apps logs
az containerapp logs show --name APP -g RG --follow
# Function App logs (query App Insights traces)
az monitor app-insights query --apps APP-INSIGHTS -g RG \
  --analytics-query "traces | where timestamp > ago(1h) | order by timestamp desc | take 50"

AppLens (MCP Tools)

For AI-powered diagnostics, use:

mcp_azure_mcp_applens
  intent: "diagnose issues with <resource-name>"
  command: "diagnose"
  parameters:
    resourceId: "<resource-id>"

Provides:
- Automated issue detection
- Root cause analysis
- Remediation recommendations

Azure Monitor (MCP Tools)

For querying logs and metrics:

mcp_azure_mcp_monitor
  intent: "query logs for <resource-name>"
  command: "logs_query"
  parameters:
    workspaceId: "<workspace-id>"
    query: "<KQL-query>"


See kql-queries.md for common diagnostic queries.

Check Azure Resource Health
Using MCP
mcp_azure_mcp_resourcehealth
  intent: "check health status of <resource-name>"
  command: "get"
  parameters:
    resourceId: "<resource-id>"

Using CLI
# Check specific resource health
az resource show --ids RESOURCE_ID

# Check recent activity
az monitor activity-log list -g RG --max-events 20

References
KQL Query Library
Azure Resource Graph Queries
App Service Troubleshooting
Function Apps Troubleshooting
Messaging Troubleshooting
Weekly Installs
276.1K
Repository
microsoft/azure-skills
GitHub Stars
796
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass