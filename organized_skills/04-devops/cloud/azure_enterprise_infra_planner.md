---
rating: ⭐⭐
title: azure-enterprise-infra-planner
url: https://skills.sh/microsoft/azure-skills/azure-enterprise-infra-planner
---

# azure-enterprise-infra-planner

skills/microsoft/azure-skills/azure-enterprise-infra-planner
azure-enterprise-infra-planner
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-enterprise-infra-planner
SKILL.md
Azure Enterprise Infra Planner
When to Use This Skill

Activate this skill when user wants to:

Plan enterprise Azure infrastructure from a workload or architecture description
Architect a landing zone, hub-spoke network, or multi-region topology
Design networking infrastructure: VNets, subnets, firewalls, private endpoints, VPN gateways
Plan identity, RBAC, and compliance-driven infrastructure
Generate Bicep or Terraform for subscription-scope or multi-resource-group deployments
Plan disaster recovery, failover, or cross-region high-availability topologies
Quick Reference
Property	Details
MCP tools	get_azure_bestpractices_get, wellarchitectedframework_serviceguide_get, microsoft_docs_fetch, microsoft_docs_search, bicepschema_get
CLI commands	az deployment group create, az bicep build, az resource list, terraform init, terraform plan, terraform validate, terraform apply
Output schema	plan-schema.md
Key references	research.md, resources/, waf-checklist.md, constraints/
Workflow

Read workflow.md for detailed step-by-step instructions, including MCP tool usage, CLI commands, and decision points. Follow the phases in order, ensuring all key gates are passed before proceeding to the next phase.

Phase	Action	Key Gate
1	Research — WAF Tools	All MCP tool calls complete
2	Research — Refine & Lookup	Resource list approved by user
3	Plan Generation	Plan JSON written to disk
4	Verification	All checks pass, user approves
5	IaC Generation	meta.status = approved
6	Deployment	User confirms destructive actions
MCP Tools
Tool	Purpose
get_azure_bestpractices_get	Azure best practices for code generation, operations, and deployment
wellarchitectedframework_serviceguide_get	WAF service guide for a specific Azure service
microsoft_docs_search	Search Microsoft Learn for relevant documentation chunks
microsoft_docs_fetch	Fetch full content of a Microsoft Learn page by URL
bicepschema_get	Bicep schema definition for any Azure resource type (latest API version)
Error Handling
Error	Cause	Fix
MCP tool error or not available	Tool call timeout, connection error, or tool doesn't exist	Retry once; fall back to reference files and notify user if unresolved
Plan approval missing	meta.status is not approved	Stop and prompt user for approval before IaC generation or deployment
IaC validation failure	az bicep build or terraform validate returns errors	Fix the generated code and re-validate; notify user if unresolved
Pairing constraint violation	Incompatible SKU or resource combination	Fix in plan before proceeding to IaC generation
Infra plan or IaC files not found	Files written to wrong location or not created	Verify files exist at <project-root>/.azure/ and <project-root>/infra/; if missing, re-create the files by following workflow.md exactly
Weekly Installs
196.0K
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