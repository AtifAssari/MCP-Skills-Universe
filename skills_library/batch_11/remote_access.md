---
title: remote-access
url: https://skills.sh/acquia/acquia-skills/remote-access
---

# remote-access

skills/acquia/acquia-skills/remote-access
remote-access
Installation
$ npx skills add https://github.com/acquia/acquia-skills --skill remote-access
SKILL.md
Remote Access with Acquia CLI

Use when:

Opening an SSH shell on a Cloud environment
Running a Drush command on a remote environment
Downloading or listing Drush aliases
Tailing live logs from an environment
SSH into a Cloud Environment

Open an interactive shell in a Cloud Platform environment:

acli remote:ssh <alias>


Alias: acli ssh

The alias format is app-name.env (e.g. myapp.prod, myapp.dev).

# Open interactive shell
acli remote:ssh myapp.prod

# Run a single command without opening a shell
acli remote:ssh myapp.prod -- ls -la /var/www/html

# Run multiple commands
acli remote:ssh myapp.prod -- "cd /var/www/html && git log --oneline -5"

Run Drush Remotely

Run any Drush command on a Cloud environment without SSHing in manually:

acli remote:drush <drush_command>


Aliases: acli drush, acli dr

# Check Drupal status
acli remote:drush status

# Clear caches
acli remote:drush cr

# Run database updates
acli remote:drush updatedb

# Export configuration
acli remote:drush cex

Tail Logs Live

Stream live logs from an environment:

acli app:log:tail


Aliases: acli tail, acli log:tail

Prompts you to select the application, environment, and log type.

List Drush Aliases

List all Drush site aliases for your Cloud environments:

acli remote:aliases:list


Aliases: acli aliases, acli sa

Download Drush Aliases

Download Drush aliases for use with local Drush:

acli remote:aliases:download


Options:

acli remote:aliases:download \
  --destination-dir=/path/to/aliases \
  --all                               # download aliases for all applications

Best Practices
Use remote:drush over SSH for Drush commands — It handles authentication and environment selection automatically.
Use aliases — Download aliases with remote:aliases:download so local Drush can target Cloud environments directly.
Tail logs during deploys — Run acli app:log:tail while deploying to catch errors in real time.
Related Topics
Pull & Push — Sync code, files, and databases
SSH Key Management — Secure access setup
Environment Management — Manage environments
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