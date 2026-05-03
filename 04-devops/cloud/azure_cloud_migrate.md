---
rating: ⭐⭐
title: azure-cloud-migrate
url: https://skills.sh/microsoft/azure-skills/azure-cloud-migrate
---

# azure-cloud-migrate

skills/microsoft/azure-skills/azure-cloud-migrate
azure-cloud-migrate
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-cloud-migrate
Summary

Assess and migrate cloud workloads from AWS, GCP, and other providers to Azure services.

Supports Lambda-to-Azure Functions migration with dedicated scenario reference and best practices
Generates assessment reports mapping source services to Azure equivalents before any code conversion
Converts source code to target Azure runtime models, with output isolated in a separate <source-folder>-azure/ directory
Requires sequential phase execution: assessment first, then migration, with user confirmation before destructive actions
Hands off to azure-prepare skill for infrastructure provisioning, local testing, and deployment workflows
SKILL.md
Azure Cloud Migrate

This skill handles assessment and code migration of existing cloud workloads to Azure.

Rules
Follow phases sequentially — do not skip
Generate assessment before any code migration
Load the scenario reference and follow its rules
Use mcp_azure_mcp_get_azure_bestpractices and mcp_azure_mcp_documentation MCP tools
Use the latest supported runtime for the target service
Destructive actions require ask_user — global-rules
Report progress to user — During long-running operations (deployments, image pushes), provide resource-level status updates so the user is never left waiting without feedback — see workflow-details.md
Audit service discovery in app code — Kubernetes DNS names (e.g., http://order-service:3001) do not resolve in Container Apps. During assessment, scan source code for hardcoded hostnames/ports in HTTP clients and flag them for env-var-driven URL injection
Migration Scenarios
Source	Target	Reference
AWS Lambda	Azure Functions	lambda-to-functions.md (assessment, code-migration)
AWS Fargate (ECS)	Azure Container Apps	fargate-to-container-apps.md (assessment, deployment)
Kubernetes (GKE/EKS/Self-hosted)	Azure Container Apps	k8s-to-container-apps.md
GCP Cloud Run	Azure Container Apps	cloudrun-to-container-apps.md

No matching scenario? Use mcp_azure_mcp_documentation and mcp_azure_mcp_get_azure_bestpractices tools.

Output Directory

All output goes to <workspace-root-basename>-azure/ at workspace root, where <workspace-root-basename> is the name of the top-level workspace directory itself (NOT a subdirectory within it). Never modify the source directory.

Steps
Create <workspace-root-basename>-azure/ at workspace root
Assess — Analyze source, map services, generate report using scenario-specific assessment guide
Migrate — Convert code/config using scenario-specific migration guide
Ask User — "Migration complete. Test locally or deploy to Azure?"
Hand off to azure-prepare for infrastructure, testing, and deployment

Track progress in migration-status.md — see workflow-details.md.

Weekly Installs
275.9K
Repository
microsoft/azure-skills
GitHub Stars
796
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn