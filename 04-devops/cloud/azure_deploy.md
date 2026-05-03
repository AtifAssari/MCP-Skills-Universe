---
rating: ⭐⭐
title: azure-deploy
url: https://skills.sh/microsoft/azure-skills/azure-deploy
---

# azure-deploy

skills/microsoft/azure-skills/azure-deploy
azure-deploy
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-deploy
Summary

Execute Azure deployments for prepared applications with built-in error recovery and validation.

Requires .azure/plan.md with Validated status from azure-validate and azure-prepare skills; will not proceed without both prerequisites
Executes azd up, azd deploy, terraform apply, and az deployment commands with error handling and post-deployment verification
Includes pre-deploy checklist, recipe-based deployment workflows, and post-deploy configuration for SQL managed identity and Entity Framework migrations
Supports applications with API Management gateway infrastructure created during preparation phase
SKILL.md
Azure Deploy

AUTHORITATIVE GUIDANCE — MANDATORY COMPLIANCE

PREREQUISITE: The azure-validate skill MUST be invoked and completed with status Validated BEFORE executing this skill.

⛔ STOP — PREREQUISITE CHECK REQUIRED Before proceeding, verify BOTH prerequisites are met:

azure-prepare was invoked and completed → .azure/deployment-plan.md exists
azure-validate was invoked and passed → plan status = Validated

If EITHER is missing, STOP IMMEDIATELY:

No plan? → Invoke azure-prepare skill first
Status not Validated? → Invoke azure-validate skill first

⛔ DO NOT MANUALLY UPDATE THE PLAN STATUS

You are FORBIDDEN from changing the plan status to Validated yourself. Only the azure-validate skill is authorized to set this status after running actual validation checks. If you update the status without running validation, deployments will fail.

DO NOT ASSUME the app is ready. DO NOT SKIP validation to save time. Skipping steps causes deployment failures. The complete workflow ensures success:

azure-prepare → azure-validate → azure-deploy

Triggers

Activate this skill when user wants to:

Execute deployment of an already-prepared application (azure.yaml and infra/ exist)
Push updates to an existing Azure deployment
Run azd up, azd deploy, or az deployment on a prepared project
Ship already-built code to production
Deploy an application that already includes API Management (APIM) gateway infrastructure

Scope: This skill executes deployments. It does not create applications, generate infrastructure code, or scaffold projects. For those tasks, use azure-prepare.

APIM / AI Gateway: Use this skill to deploy applications whose APIM/AI gateway infrastructure was already created during azure-prepare. For creating or changing APIM resources, see APIM deployment guide. For AI governance policies, invoke azure-aigateway skill.

Rules
Run after azure-prepare and azure-validate
.azure/deployment-plan.md must exist with status Validated
Pre-deploy checklist required — Pre-Deploy Checklist
⛔ Destructive actions require ask_user — global-rules
Scope: deployment execution only — This skill owns execution of azd up, azd deploy, terraform apply, and az deployment commands. These commands are run through this skill's error recovery and verification pipeline.
Steps
#	Action	Reference
1	Check Plan — Read .azure/deployment-plan.md, verify status = Validated AND Validation Proof section is populated	.azure/deployment-plan.md
2	Pre-Deploy Checklist — MUST complete ALL steps	Pre-Deploy Checklist
3	Load Recipe — Based on recipe.type in .azure/deployment-plan.md	recipes/README.md
4	RBAC Health Check — For Container Apps + ACR with managed identity: run azd provision --no-prompt, then verify AcrPull role has propagated before proceeding (see checklist)	Pre-Deploy Checklist — Container Apps RBAC
5	Execute Deploy — Follow recipe steps	Recipe README
6	Post-Deploy — Configure SQL managed identity and apply EF migrations if applicable	Post-Deployment
7	Handle Errors — See recipe's errors.md	—
8	Verify Success — Confirm deployment completed and endpoints are accessible	Verification
9	Live Role Verification — Query Azure to confirm provisioned RBAC roles are correct and sufficient	live-role-verification.md
10	Report Results — Present deployed endpoint URLs to the user as fully-qualified https:// links	Verification

⛔ URL FORMAT RULE

When presenting endpoint URLs to the user, you MUST always use fully-qualified URLs with the https:// scheme (e.g. https://myapp.azurewebsites.net, not myapp.azurewebsites.net). Many Azure CLI commands return bare hostnames without a scheme — always prepend https:// before presenting them.

⛔ VALIDATION PROOF CHECK

When checking the plan, verify the Validation Proof section (Section 7) contains actual validation results with commands run and timestamps. If this section is empty, validation was bypassed — invoke azure-validate skill first.

SDK Quick References
Azure Developer CLI: azd
Azure Identity: Python | .NET | TypeScript | Java
MCP Tools
Tool	Purpose
mcp_azure_mcp_subscription_list	List available subscriptions
mcp_azure_mcp_group_list	List resource groups in subscription
mcp_azure_mcp_azd	Execute AZD commands
azure__role	List role assignments for live RBAC verification (step 9)
References
Troubleshooting - Common issues and solutions
Post-Deployment Steps - SQL + EF Core setup
Weekly Installs
276.2K
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