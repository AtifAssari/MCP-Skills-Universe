---
rating: ⭐⭐⭐
title: eve-troubleshooting
url: https://skills.sh/incept5/eve-skillpacks/eve-troubleshooting
---

# eve-troubleshooting

skills/incept5/eve-skillpacks/eve-troubleshooting
eve-troubleshooting
Installation
$ npx skills add https://github.com/incept5/eve-skillpacks --skill eve-troubleshooting
SKILL.md
Eve Troubleshooting

Use CLI-first diagnostics. Do not assume cluster access.

Quick Triage Checklist
eve system health
eve auth status
eve job list --phase active

Common Issues and Fixes
Auth Fails or "Not authenticated"
eve auth logout
eve auth login
eve auth status


If SSH key is missing, register it with the admin or follow the CLI prompt to fetch from GitHub.

Secret Missing / Interpolation Error
eve secrets list --project proj_xxx
eve secrets set MISSING_KEY "value" --project proj_xxx


Verify .eve/dev-secrets.yaml exists for local interpolation.

Deploy Job Failed
eve job follow <job-id>
eve job diagnose <job-id>
eve job result <job-id>


Check for registry auth errors, missing secrets, or healthcheck failures.

Registry Push Fails with UNAUTHORIZED

If build jobs fail with UNAUTHORIZED: authentication required when pushing:

Verify secrets are set: eve secrets list --project proj_xxx
If using a custom BYO registry, verify credentials map to registry.host
Confirm the imagePull metadata in your manifest is correct
Add OCI source label to Dockerfile: LABEL org.opencontainers.image.source="https://github.com/ORG/REPO"

Some registries require repository-linked package metadata or workspace-level auth alignment.

Build Failures
Symptoms
Pipeline fails at build step
eve build diagnose shows run status = failed
Triage
eve build list --project <id>          # Find recent builds
eve build diagnose <build_id>          # Full state dump
eve build logs <build_id>              # Raw build output

Common Causes

Registry authentication:

If using custom registry mode, verify REGISTRY_USERNAME and REGISTRY_PASSWORD secrets are set (or provider-equivalent registry credentials). With managed registry (registry: "eve"), this step is usually not required.
Ensure credentials can access the configured registry account and namespace
Check: eve secrets list --project <id>

Dockerfile issues:

Service must have build.context in manifest pointing to directory with Dockerfile
Dockerfile path defaults to <context>/Dockerfile
Multi-stage builds work with BuildKit; may fail with Kaniko

Workspace/clone errors:

Build requires workspace at the correct git SHA
Check eve build diagnose for workspace preparation errors

Image push failures:

OCI labels help link packages to repos: add LABEL org.opencontainers.image.source="https://github.com/OWNER/REPO" to Dockerfile
Ensure registry host and auth match manifest registry.host when using BYO/custom registry
Job Stuck or Blocked
eve job show <job-id>
eve job dep list <job-id>


Resolve dependencies or update phase with eve job update if appropriate.

App Not Reachable After Deploy
Confirm deploy job succeeded (eve job result).
Validate ingress host pattern: {service}.{orgSlug}-{projectSlug}-{env}.{domain}.
Ensure service port matches x-eve.ingress.port.
Escalation

If CLI output is insufficient, collect:

eve system health
eve job diagnose <job-id>
manifest diff (recent changes)

Then hand off to the platform operator.

Weekly Installs
238
Repository
incept5/eve-skillpacks
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass