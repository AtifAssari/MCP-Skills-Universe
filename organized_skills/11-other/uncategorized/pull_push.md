---
rating: ⭐⭐⭐
title: pull-push
url: https://skills.sh/acquia/acquia-skills/pull-push
---

# pull-push

skills/acquia/acquia-skills/pull-push
pull-push
Installation
$ npx skills add https://github.com/acquia/acquia-skills --skill pull-push
SKILL.md
Pull & Push with Acquia CLI

Use when:

Syncing your local environment with a Cloud Platform environment
Pulling code, database, or files from Cloud to local
Pushing code, database, files, or build artifacts to Cloud
Pull: Copy from Cloud to Local
Pull everything (code + database + files)
acli pull:all


Aliases: acli refresh, acli pull

Prompts you to select an environment, then copies code, database, and files to your local environment.

Options:

acli pull:all \
  --dir=/path/to/project \
  --no-code \        # skip code
  --no-databases \   # skip database
  --no-files \       # skip files
  --no-scripts       # skip post-pull scripts

Pull code only
acli pull:code


Pulls the latest code from the selected Cloud environment into your local directory.

acli pull:code --dir=/path/to/project

Pull database only
acli pull:database


Alias: acli pull:db

Imports a database backup from a Cloud environment into your local database.

Options:

acli pull:database \
  --on-demand \      # force a fresh on-demand backup (not cached)
  --no-import \      # download the backup file but don't import it
  --multiple-dbs     # download multiple databases (multisite)

Pull files only
acli pull:files


Copies Drupal public files (sites/default/files) from the Cloud environment to your local.

Run post-pull scripts manually

If you skipped scripts during a pull, run them separately:

acli pull:run-scripts
acli pull:run-scripts --dir=/path/to/project

Push: Copy from Local to Cloud
Push database
acli push:database


Alias: acli push:db

Uploads your local database to a Cloud Platform environment. Requires both a local and remote database to be configured.

Push files
acli push:files


Copies your local Drupal public files to the selected Cloud environment.

Push code (IDE only)
acli push:code


Push code from your Cloud IDE to a Cloud Platform environment. This command is only available inside a Cloud IDE or Lando environment.

Build and push a code artifact

Build your project and push the compiled artifact to a Cloud environment or custom git remote:

acli push:artifact


Common options:

# Push to a specific branch on Cloud
acli push:artifact --destination-git-branch=deploy/main

# Push to a specific tag
acli push:artifact --destination-git-tag=release-1.2.3

# Push to an external git URL (e.g. GitHub)
acli push:artifact --destination-git-urls=git@github.com:myorg/myrepo.git

# Dry run — build but don't push
acli push:artifact --no-push

# Build in a specific directory
acli push:artifact --dir=/path/to/project

# Skip sanitization step
acli push:artifact --no-sanitize

Typical Workflows
Refresh local dev environment
acli pull:all

Pull only the database (fastest for testing)
acli pull:database --on-demand

Deploy a build artifact to Cloud
acli push:artifact --destination-git-branch=tags/deploy-branch

Sync files to production (use with care)
acli push:files

Best Practices
Always pull before you push — Avoid overwriting recent Cloud changes.
Use --on-demand for fresh data — The default pull uses a cached backup; --on-demand forces a new one.
Test artifact builds with --no-push — Verify the artifact is correct before pushing.
Use --no-scripts in CI — Post-pull scripts are designed for local dev, not CI pipelines.
Backup before pushing a database — A push:database overwrites the remote database.
Troubleshooting
"Local database not found"

pull:all and pull:database require a running local database. Make sure your local Drupal stack (Lando, DDEV, etc.) is running.

"Access denied" on push

Verify your SSH key is set up and your account has write access to the environment:

acli ssh-key:list
acli auth:me

Artifact push fails

Check that composer install and any build steps complete without errors before pushing:

acli push:artifact --no-push  # dry run to inspect

Related Topics
Application Management — Find environment IDs
SSH Key Management — Authentication
Remote Access — SSH and Drush on Cloud environments
Weekly Installs
25
Repository
acquia/acquia-skills
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass