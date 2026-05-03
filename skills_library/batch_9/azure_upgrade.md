---
title: azure-upgrade
url: https://skills.sh/microsoft/azure-skills/azure-upgrade
---

# azure-upgrade

skills/microsoft/azure-skills/azure-upgrade
azure-upgrade
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-upgrade
Summary

Assess and automate upgrades of Azure workloads across plans, tiers, and SKUs.

Handles plan migrations (Consumption to Flex Consumption), tier upgrades, and cross-service moves (App Service to Container Apps) with sequential assessment before any changes
Generates pre-upgrade readiness reports, collects existing app settings and configurations, then executes automated upgrade steps with idempotent scripts
Requires explicit user confirmation for destructive actions and target plan/SKU selection before proceeding
Validates upgrades by testing app reachability and monitoring, then hands off to azure-validate or azure-deploy for deeper validation or CI/CD setup
SKILL.md
Azure Upgrade

This skill handles assessment and automated upgrades of existing Azure workloads from one Azure service, hosting plan, or SKU to another — all within Azure. This includes plan/tier upgrades (e.g. Consumption → Flex Consumption), cross-service migrations (e.g. App Service → Container Apps), and SKU changes. It also covers Azure SDK for Java source-code modernization (e.g. legacy Java com.microsoft.azure.* → modern com.azure.*). This is NOT for cross-cloud migration — use azure-cloud-migrate for that.

Triggers
User Intent	Example Prompts
Upgrade Azure Functions plan	"Upgrade my function app from Consumption to Flex Consumption"
Change hosting tier	"Move my function app to a better plan"
Assess upgrade readiness	"Is my function app ready for Flex Consumption?"
Automate plan migration	"Automate the steps to upgrade my Functions plan"
Modernize legacy Azure Java SDK	"Migrate legacy Azure SDKs for Java", "Upgrade legacy Azure Java SDK", "Migrate my Java project from com.microsoft.azure to com.azure"
Rules
Follow phases sequentially — do not skip
Generate an assessment before any upgrade operations
Load the scenario reference and follow its rules
Use mcp_azure_mcp_get_azure_bestpractices and mcp_azure_mcp_documentation MCP tools
Destructive actions require ask_user — global-rules
Always confirm the target plan/SKU with the user before proceeding
Never delete or stop the original app without explicit user confirmation
All automation scripts must be idempotent and resumable
Upgrade Scenarios
Source	Target	Reference
Azure Functions Consumption Plan	Azure Functions Flex Consumption Plan	consumption-to-flex.md
Legacy Azure Java SDK (com.microsoft.azure.*)	Modern Azure Java SDK (com.azure.*)	languages/java/README.md

SDK upgrade scenarios (e.g. Java legacy → modern) run a source-code modernization flow that is distinct from Azure service/plan/SKU upgrades: follow the scenario reference, not the Steps below.

No matching scenario? Use mcp_azure_mcp_documentation and mcp_azure_mcp_get_azure_bestpractices tools to research the upgrade path.

MCP Tools
Tool	Purpose
mcp_azure_mcp_get_azure_bestpractices	Get Azure best practices for the target service
mcp_azure_mcp_documentation	Look up Azure documentation for upgrade scenarios
mcp_azure_mcp_appservice	Query App Service and Functions plan details
mcp_azure_mcp_applicationinsights	Verify monitoring configuration
Steps
Identify — Determine the source and target Azure plans/SKUs. Ask user to confirm.
Assess — Analyze existing app for upgrade readiness → load scenario reference (e.g., consumption-to-flex.md)
Pre-migrate — Collect settings, identities, configs from the existing app
Upgrade — Execute the automated upgrade steps (create new resources, migrate settings, deploy code)
Validate — Hit the function app default URL to confirm the app is reachable, then verify endpoints and monitoring
Ask User — "Upgrade complete. Would you like to verify performance, clean up the old app, or update your IaC?"
Hand off to azure-validate for deep validation or azure-deploy for CI/CD setup

Track progress in upgrade-status.md inside the workspace root.

References
Global Rules
Workflow Details
Functions
Consumption to Flex Consumption
Assessment
Automation Scripts
Java SDK Migration Templates
Plan Template
Progress Template
Summary Template
Next

After upgrade is validated, hand off to:

azure-validate — for thorough post-upgrade validation
azure-deploy — if the user wants to set up CI/CD for the new app
Weekly Installs
238.7K
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