---
rating: ⭐⭐⭐
title: drupal-update-deploy
url: https://skills.sh/acquia/acquia-skills/drupal-update-deploy
---

# drupal-update-deploy

skills/acquia/acquia-skills/drupal-update-deploy
drupal-update-deploy
Installation
$ npx skills add https://github.com/acquia/acquia-skills --skill drupal-update-deploy
SKILL.md
Drupal Update and Deploy Workflow

Use when:

Applying Drupal dependency updates and deploying to an Acquia environment
Running the full cycle: update packages → push code → deploy → trigger pipeline

Prerequisites: The following skill sets must be loaded: drupal-maintenance, acli, pipelines-cli.

Workflow
Step 1 — Apply dependency updates

Ask the user: "Do you need to apply dependency updates first, or are updates already done?"

If updates are needed → follow Security Updates or Dependency Updates depending on the use case, then return here.
If updates are already applied → proceed to Step 2.
Step 2 — Fetch application and environments

Always run these before asking the user where to deploy. This ensures the correct application and environment IDs are used.

# List available applications and note the UUID
acli api:applications:list


Output shows application names and UUIDs. Ask the user: "Which application do you want to deploy to?" and confirm the UUID.

# List environments for the selected application
acli api:environments:list <app-uuid>


Output shows environment labels (dev, stage, prod, CDEs), IDs, and the currently deployed branch. Ask the user: "Which environment do you want to deploy to?"

Step 3 — Commit code changes

Before pushing, check for uncommitted changes:

git status


If there are uncommitted changes, ask the user: "Do you want to commit these changes before deploying?"

If yes — ask for a commit message, then commit:
git add -A
git commit -m "<user-provided message>"

If no — warn the user that uncommitted changes will not be included in the deployment and confirm they want to proceed.
Step 4 — Push code to Acquia Cloud

Push the committed code to the selected environment:

acli push:code


Follow Pull & Push for full options (selecting environments, handling conflicts).

Step 5 — Switch code on the environment

After pushing, switch the environment to the updated branch using the environment ID from Step 2:

acli api:environments:switchCode <environment-id> --branch=<branch-name>


Follow Environment Management for deploy options.

Step 6 — Trigger a pipeline build (optional)

Ask the user: "Do you want to trigger a pipeline build for the deployed branch?"

If yes → follow Pipeline Operations to start the build and stream logs:
pipelines start --application-id=<app-id> --vcs-path=<branch> --tail

If no → workflow complete.
Step 7 — Verify deployment

After the pipeline completes (or if skipping pipelines), confirm the environment is running the expected code:

acli api:environments:list <app-uuid>


Check the vcs field of the target environment to confirm the branch matches.

Quick Reference
Step	Tool	Skill
Update packages	composer	drupal-maintenance-security-updates or drupal-maintenance-dependency-updates
Fetch application + environments	acli	acli-application-management, acli-environment-management
Commit code changes	git	—
Push code	acli	acli-pull-push
Deploy to environment	acli	acli-environment-management
Trigger pipeline	pipelines-cli	pipelines-cli-pipeline-operations
Weekly Installs
24
Repository
acquia/acquia-skills
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass