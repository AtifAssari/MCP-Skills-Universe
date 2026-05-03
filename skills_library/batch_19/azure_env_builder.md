---
title: azure-env-builder
url: https://skills.sh/aktsmm/agent-skills/azure-env-builder
---

# azure-env-builder

skills/aktsmm/agent-skills/azure-env-builder
azure-env-builder
Installation
$ npx skills add https://github.com/aktsmm/agent-skills --skill azure-env-builder
SKILL.md
Azure Environment Builder

Enterprise Azure environment builder skill.

When to Use
Azure, Bicep, infrastructure, deploy app
Building enterprise Azure environments
Deploying apps to App Service, AKS, or Container Apps
Designing Hub-Spoke, AKS, or AI Foundry architectures
Features
Category	Capabilities
Architecture	Hub-Spoke, Web+DB, AKS, AI Foundry
AVM Modules	200+ Azure Verified Modules
VM Init	Squid, Nginx, Docker, IIS setup
Config Linking	SQL/Storage/Redis, Managed ID RBAC
CI/CD	GitHub Actions / Azure Pipelines
Workflow
Interview - Gather requirements + select architecture pattern
MCP Tools - Fetch latest AVM/schema info
Scaffold - Generate environment folder via scripts/scaffold_environment.ps1
Implement - Write Bicep with AVM modules + VM init
CI/CD - Generate pipeline templates
Deploy - what-if → execute
Required: MCP Tools

Run before generating Bicep code:

mcp_bicep_experim_get_bicep_best_practices
mcp_bicep_experim_list_avm_metadata
mcp_bicep_experim_get_az_resource_type_schema(azResourceType, apiVersion)
microsoft_docs_search(query: "Private Endpoint Bicep")

Interview Checklist

→ references/hearing-checklist.md

Item	Details
Subscription	ID or az account show
Environment	dev / staging / prod
Region	japaneast / japanwest
Deploy Type	Azure CLI / Bicep
Architecture Patterns

→ references/architecture-patterns.md

Pattern	Use Case
Hub-Spoke	Large enterprise
Web + DB	Standard web applications
AKS	Container microservices
AI Foundry	AI/ML workloads
Proxy VM	Private network egress control
Commands
# Scaffold environment folder
pwsh scripts/scaffold_environment.ps1 -Environment <env> -Location <region>

# Validate
az deployment group what-if --resource-group <rg> --template-file main.bicep

# Deploy
az deployment group create --resource-group <rg> --template-file main.bicep

Key References
File	Purpose
architecture-patterns.md	Architecture patterns
avm-modules.md	AVM module catalog
vm-app-scripts.md	VM init scripts
app-deploy-patterns.md	App deploy patterns
service-config-templates.md	Service config linking
cicd-templates/	CI/CD templates
Done Criteria
 Interview checklist completed
 MCP tools fetched latest info
 Bicep files generated
 az deployment group what-if succeeded
Weekly Installs
49
Repository
aktsmm/agent-skills
GitHub Stars
11
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn