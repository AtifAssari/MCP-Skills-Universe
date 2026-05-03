---
rating: ⭐⭐⭐
title: application-management
url: https://skills.sh/acquia/acquia-skills/application-management
---

# application-management

skills/acquia/acquia-skills/application-management
application-management
Installation
$ npx skills add https://github.com/acquia/acquia-skills --skill application-management
SKILL.md
Managing Applications

Use when:

Listing applications you have access to
Linking or unlinking a local repo to a Cloud application
Creating a new Drupal or Next.js project
Checking branch/tag deployment status
Waiting for an async task to complete
Exporting a full site archive
List Applications
acli api:applications:list


Returns a JSON array of all applications you have access to. Each entry includes id, uuid, name, type, status, and organization.

To display a readable table:

acli api:applications:list | python3 -c "
import json, sys
apps = json.load(sys.stdin)
for a in apps:
    print(f\"{a['id']:<10} {a['name']:<40} {a.get('type',''):<10} {a.get('status',''):<10}\")
"

Open Application in Browser
acli app:open


Aliases: acli open, acli o

Opens the selected Cloud application in your default browser.

Link and Unlink a Local Repository

Associate your local checkout with a Cloud application so commands like env:deploy can detect the app automatically:

cd /path/to/project
acli app:link


To remove the association:

acli app:unlink

Tail Application Logs

Stream live logs from a Cloud environment:

acli app:log:tail


Prompts for the application and environment, then tails all available log streams in real time. Useful for monitoring deployments or debugging live issues.

Check Branch and Tag Deployment Status
acli app:vcs:info


Lists all branches and tags in the application's git repository along with which environment (if any) each is currently deployed to.

Wait for an Async Task

Some Cloud operations (database copies, environment mirrors) return a notification UUID. Wait for them to complete:

acli app:task-wait <notification-uuid>


Useful in CI/CD pipelines to block until a task finishes before proceeding.

Create a New Local Project

Scaffold a new Drupal or Next.js project from an Acquia-recommended template:

# Interactive — prompts for template and directory
acli app:new:local

# Non-interactive
acli app:new:local my-project --template=acquia_drupal_recommended
acli app:new:local my-project --template=acquia_drupal_cms


Alias: acli new

Available templates:

acquia_drupal_recommended — Standard Acquia Drupal project
acquia_drupal_cms — Acquia Drupal CMS project
Migrate from Drupal 7

Generate a new Drupal 9+ project from an existing Drupal 7 application using Acquia Migrate Accelerate:

acli app:new:from:drupal7


Options: --drupal7-directory, --drupal7-uri, --stored-analysis, --recommendations, --directory

Aliases: acli ama, acli from:d7

Export a Site Archive

Export an application's code, files, and database as a single archive file:

acli archive:export /path/to/destination/


Options:

# Exclude public files
acli archive:export /path/to/destination/ --no-files

# Exclude database
acli archive:export /path/to/destination/ --no-database

# Use a specific source directory
acli archive:export /path/to/destination/ --dir=/path/to/drupal

Best Practices
Link your repo — Run acli app:link in every project checkout so app-aware commands work without extra flags.
Check VCS status before deploying — Use acli app:vcs:info to confirm the right branch is ready.
Use app:task-wait in CI — Ensures async Cloud operations complete before the next pipeline step runs.
Related Topics
Environment Management — List environments, deploy, create CDEs
Pull & Push — Sync code, database, and files
Remote Access — SSH, Drush, and log tailing
SSH Key Management — Secure access setup
Weekly Installs
31
Repository
acquia/acquia-skills
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass