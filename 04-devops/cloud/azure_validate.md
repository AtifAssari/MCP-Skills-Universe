---
rating: ⭐⭐
title: azure-validate
url: https://skills.sh/microsoft/azure-skills/azure-validate
---

# azure-validate

skills/microsoft/azure-skills/azure-validate
azure-validate
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-validate
Summary

Pre-deployment validation for Azure infrastructure, configuration, and permissions before deployment.

Requires .azure/plan.md from a prior azure-prepare run; stops immediately if the plan is missing
Executes recipe-specific validation commands (azd provision, bicep build, terraform validate) and records proof in the plan document
Performs build verification, configuration checks, and permission validation; blocks deployment if any check fails
Only authorized method to set plan status to Validated; must be followed by azure-deploy skill to execute the actual deployment
SKILL.md
Azure Validate

AUTHORITATIVE GUIDANCE — Follow these instructions exactly unless they contradict security policies given to you.

⛔ STOP — PREREQUISITE CHECK REQUIRED

Before proceeding, verify this prerequisite is met:

azure-prepare was invoked and completed → .azure/deployment-plan.md exists with status Approved or later

If the plan is missing, STOP IMMEDIATELY and invoke azure-prepare first.

The complete workflow ensures success:

azure-prepare → azure-validate → azure-deploy

Triggers
Check if app is ready to deploy
Validate azure.yaml or Bicep
Run preflight checks
Troubleshoot deployment errors
Rules
Run after azure-prepare, before azure-deploy
All checks must pass—do not deploy with failures
⛔ Destructive actions require ask_user — global-rules
Steps
#	Action	Reference
1	Load Plan — Read .azure/deployment-plan.md for recipe and configuration. If missing → run azure-prepare first	.azure/deployment-plan.md
2	Add Validation Steps — Copy recipe "Validation Steps" to .azure/deployment-plan.md as children of "All validation checks pass"	recipes/README.md, .azure/deployment-plan.md
3	Run Validation — Execute recipe-specific validation commands	recipes/README.md
4	Build Verification — Build the project and fix any errors before proceeding	See recipe
5	Static Role Verification — Review Bicep/Terraform for correct RBAC role assignments in code	role-verification.md
6	Record Proof — Populate Section 7: Validation Proof with commands run and results	.azure/deployment-plan.md
7	Resolve Errors — Fix failures before proceeding	See recipe's errors.md
8	Update Status — Only after ALL checks pass, set status to Validated	.azure/deployment-plan.md
9	Deploy — Invoke azure-deploy skill	—

⛔ VALIDATION AUTHORITY

This skill is the officially verified way to set plan status to Validated. You MUST follow these steps to make sure every prerequisite is fulfilled before setting status to Validated:

Run actual validation commands (azd provision --preview, bicep build, terraform validate, etc.)
Populate Section 7: Validation Proof with the commands you ran and their results
Only then set status to Validated

Do NOT set status to Validated without running checks and recording proof.

⚠️ MANDATORY NEXT STEP — DO NOT SKIP

After ALL validations pass, you MUST invoke azure-deploy to execute the deployment. Do NOT attempt to run azd up, azd deploy, or any deployment commands directly. Let azure-deploy handle execution.

If any validation failed, fix the issues and re-run azure-validate before proceeding.

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
SnykFail