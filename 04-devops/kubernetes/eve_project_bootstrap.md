---
rating: ⭐⭐⭐
title: eve-project-bootstrap
url: https://skills.sh/incept5/eve-skillpacks/eve-project-bootstrap
---

# eve-project-bootstrap

skills/incept5/eve-skillpacks/eve-project-bootstrap
eve-project-bootstrap
Installation
$ npx skills add https://github.com/incept5/eve-skillpacks --skill eve-project-bootstrap
SKILL.md
Eve Project Bootstrap

Use this flow to connect an existing repo to Eve and get the first deploy running.

Set the API Target
Get the staging API URL from your admin.
Create and use a profile:
eve profile create staging --api-url https://api.eh1.incept5.dev
eve profile use staging

Create Org and Project
eve org ensure my-org --slug myorg
eve project ensure --name "My App" --slug my-app --repo-url git@github.com:me/my-app.git --branch main


URL impact: These slugs determine your deployment URLs and K8s namespaces:

URL: {service}.{orgSlug}-{projectSlug}-{env}.{domain} (e.g., api.myorg-my-app-staging.eh1.incept5.dev)
Namespace: eve-{orgSlug}-{projectSlug}-{env} (e.g., eve-myorg-my-app-staging)

Slugs are immutable — choose short, meaningful values.

Set defaults:

eve profile set --org org_xxx --project proj_xxx

Add the Manifest
Ensure .eve/manifest.yaml is present and uses schema: eve/compose/v1.
Use the eve-manifest-authoring skill for structure details.
First Deploy
# Create environment if needed
eve env create staging --project proj_xxx --type persistent

# Deploy (requires --ref with 40-char SHA or a ref resolved against --repo-dir)
eve env deploy staging --ref main --repo-dir .

# If the environment has a pipeline configured, this triggers the pipeline.
# Use --direct to bypass pipeline and deploy directly:
eve env deploy staging --ref main --repo-dir . --direct

Verify
eve system health
eve job list --phase active
eve job follow <job-id>
eve job result <job-id>


Access apps via {service}.{orgSlug}-{projectSlug}-{env}.{domain}.

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