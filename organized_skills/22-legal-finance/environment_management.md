---
rating: ⭐⭐⭐
title: environment-management
url: https://skills.sh/acquia/acquia-skills/environment-management
---

# environment-management

skills/acquia/acquia-skills/environment-management
environment-management
Installation
$ npx skills add https://github.com/acquia/acquia-skills --skill environment-management
SKILL.md
Environment Management with Acquia CLI

Use when:

Creating or deleting Continuous Delivery Environments (CDEs)
Making one environment identical to another (mirroring)
Copying cron tasks between environments
Installing SSL certificates
Listing or inspecting environments
Deploying code to an environment
List Environments
acli api:applications:environment-list


Shows all environments for an application (prod, staging, dev, and any CDEs).

Get Environment Details
acli env:info


Shows PHP version, database, last deployment, URLs, and status for the selected environment.

Create a Continuous Delivery Environment (CDE)

CDEs are on-demand environments — useful for testing feature branches before merging.

acli env:create "My Feature Branch" feature/my-branch


Arguments:

label (required) — Human-readable name for the new environment
branch (optional) — The git branch to deploy; prompts if omitted
# Interactive (prompts for branch)
acli env:create "QA Review"

# Non-interactive
acli env:create "Sprint 42 Demo" release/sprint-42

Delete a CDE
acli env:delete


Prompts you to select the environment to delete. Only CDEs can be deleted; production and standard environments cannot.

Deploy Code to an Environment
acli api:environments:code-switch <environmentId> <branch>


Example:

acli api:environments:code-switch 112927-9454a2b1-cce0-475e-ae5f-5374dbca9b0a master


Returns a notification UUID you can track with acli app:task-wait <uuid>.

Mirror an Environment

Makes a destination environment identical to a source — copies code, database, files, and config.

acli env:mirror <source-environment> <destination-environment>


Use environment aliases in the format app-name.env:

acli env:mirror myapp.prod myapp.staging


Skip specific components:

acli env:mirror myapp.prod myapp.staging \
  --no-code \      # -c: skip code
  --no-databases \ # -d: skip databases
  --no-files \     # -f: skip files
  --no-config      # -p: skip configuration


Warning: This overwrites the destination. All existing data in the destination environment is replaced.

Copy Cron Tasks Between Environments

Copy all cron tasks from one environment to another:

acli env:cron-copy <source_env> <dest_env>


Example:

acli env:cron-copy myapp.prod myapp.staging


Useful after mirroring an environment to ensure scheduled tasks match.

Install an SSL Certificate
acli env:certificate-create <certificate> <private-key>


Options:

acli env:certificate-create \
  /path/to/cert.pem \
  /path/to/private-key.pem \
  --label="My SSL Cert" \
  --ca-certificates=/path/to/ca-bundle.pem \
  --legacy              # Use legacy SSL (non-SNI)


To install from an existing CSR:

acli env:certificate-create cert.pem key.pem --csr-id=<csr-uuid>

Typical Workflows
Set up a CDE for a feature branch
# Create the environment
acli env:create "Feature: New Checkout" feature/new-checkout

# Mirror prod data to it
acli env:mirror myapp.prod myapp.<new-cde-id>

Refresh staging from production
acli env:mirror myapp.prod myapp.staging

Promote staging to prod
acli api:environments:code-switch <prod-env-id> main

Best Practices
Mirror before testing — Always sync a CDE from prod or staging before QA.
Clean up CDEs — Delete CDEs when done; they consume resources.
Test deploys in staging first — Always deploy to staging before production.
Copy crons after mirror — Run env:cron-copy after mirroring to keep scheduled tasks in sync.
Troubleshooting
"Environment not found"

Check available environments:

acli api:applications:environment-list

Mirror fails midway

Check logs and retry. Use --no-databases or --no-files to skip the component that failed:

acli env:mirror myapp.prod myapp.staging --no-files

Related Topics
Pull & Push — Sync local and Cloud environments
Application Management — Find application UUIDs
Remote Access — SSH and Drush on environments
Weekly Installs
26
Repository
acquia/acquia-skills
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass