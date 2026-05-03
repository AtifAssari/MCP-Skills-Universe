---
title: getting-started
url: https://skills.sh/acquia/acquia-skills/getting-started
---

# getting-started

skills/acquia/acquia-skills/getting-started
getting-started
Installation
$ npx skills add https://github.com/acquia/acquia-skills --skill getting-started
SKILL.md
Getting Started with Acquia CLI

This guide covers installation, authentication, and your first commands.

Use when:

Installing acli for the first time
Authenticating with Acquia Cloud
Learning your first acli commands
Tool Overview

Two separate CLIs exist for Acquia Cloud operations:

Tool	Purpose
acli	General Cloud management: applications, environments, IDEs, SSH keys, code/DB sync
pipelines-cli	CI/CD pipeline operations: trigger builds, check job status, stream logs

Use pipelines-cli for anything related to pipeline jobs. Use acli for everything else.

Installation
macOS & Linux
Option 1: Native Binary (Recommended)

The native binary requires no PHP installation and works on any modern macOS or Linux system.

# Download the latest release
curl -fsSL https://github.com/acquia/cli/releases/latest/download/acli \
  -o /usr/local/bin/acli

# Make it executable
chmod +x /usr/local/bin/acli

# Verify it works
acli --version

Option 2: PHP Archive (PHAR)

If you prefer or already have PHP 8.2 installed:

curl -fsSL https://github.com/acquia/cli/releases/latest/download/acli.phar \
  -o /usr/local/bin/acli.phar
chmod +x /usr/local/bin/acli.phar

# Use as:
acli.phar --version
# Or create an alias
alias acli='acli.phar'

Using Homebrew (macOS)
brew tap acquia/cli
brew install acli
acli --version

Your First Command: Authentication

Acquia CLI uses OAuth to authenticate with your Acquia account. You'll only need to do this once.

acli auth:login


This will:

Open your browser
Prompt you to authorize Acquia CLI
Generate an access token
Store it locally in ~/.acquia/cloud_api/credentials.json (encrypted)

Tokens are valid for 30 days. If your token expires, run acli auth:login again.

Verify Authentication
acli auth:me


Shows your name, email, and account information.

Your First Command: List Applications

See which applications you have access to:

acli api:applications:list


Output:

Select a Cloud Platform application:
  [0] My First App (prod, staging, dev)
  [1] Client Project (prod, staging)
  [2] Development App (dev)

Shell Completion

Enable tab completion for faster command entry.

Bash
eval "$(acli shell:complete bash)"


Add to ~/.bashrc for permanent setup:

echo 'eval "$(acli shell:complete bash)"' >> ~/.bashrc
source ~/.bashrc

Zsh
eval "$(acli shell:complete zsh)"


Add to ~/.zshrc:

echo 'eval "$(acli shell:complete zsh)"' >> ~/.zshrc
source ~/.zshrc

Fish
acli shell:complete fish | source


Add to ~/.config/fish/config.fish:

acli shell:complete fish | source

Getting Help
Command Help

Every command has a built-in help page:

# General help
acli --help
acli -h

# Help for a specific command
acli ide:create --help
acli ide:create -h

# List all available commands by category
acli list

Verbose Output

For debugging, show detailed output:

# -v (normal), -vv (detailed), -vvv (very detailed)
acli ide:list -vvv
acli ide:create -v

Debug Mode

Run any command in debug mode to see behind-the-scenes details:

acli ide:create --debug

Configuration
Config File Location

Configuration is stored at: ~/.acquia/

~/.acquia/
├── cloud_api/
│   └── credentials.json       # Your API token (encrypted)
├── config.yaml                # Settings
└── cache/                      # Cached data

Linking a Local Project

Run acli app:link in your project directory to associate it with a Cloud application. See Application Management for details.

Common First Steps
Step 1: Authenticate
acli auth:login
acli auth:me

Step 2: Set Up a Project
cd /path/to/project
acli app:link

Step 3: Create an IDE (or connect to existing)
acli ide:create    # Create a new one
# OR
acli ide:list      # Connect to existing

Step 4: Set Up SSH
acli ssh-key:list   # See your SSH keys
# If no keys, create one
acli ssh-key:create

Step 5: Try a Drush Command
acli remote:drush status
acli remote:drush cr   # Clear caches

Troubleshooting
"Command not found: acli"

Make sure the binary is in your PATH. Try:

which acli
# If nothing, add to PATH
export PATH="/usr/local/bin:$PATH"
acli --version

"Error: Failed to authenticate"

Your token has expired or isn't valid. Try:

acli auth:login

"Error: Access denied"

You don't have permission to access that application or resource. Check:

Are you logged in with the right Acquia account?
Do you have permissions in Acquia Cloud UI?

Run acli auth:me to verify you're using the right account.

Need more help?

See Troubleshooting Guide for more issues.

Acquia Site Factory (ACSF) Authentication

If your organization uses Acquia Site Factory, register separate credentials:

acli auth:acsf-login


Options:

acli auth:acsf-login \
  --username=myuser \
  --key=MY_API_KEY \
  --factory-url=https://www.myfactory.com


To log out:

acli auth:acsf-logout

Cache Management

Clear local acli caches (useful when commands behave unexpectedly):

acli self:clear-caches


Aliases: acli cc, acli cr

Telemetry

acli collects anonymous usage data by default to help improve the tool. To opt out:

acli self:telemetry:disable


To re-enable:

acli self:telemetry:enable


Toggle interactively:

acli self:telemetry:toggle


Alias: acli telemetry

Open Product Documentation

Open Acquia product docs in your browser:

acli docs


For a specific product:

acli docs acli
acli docs cloud-ide

Best Practices
Authenticate first — Run acli auth:login before anything else; most commands require it.
Discover commands — Use acli list to see all available commands grouped by topic.
Enable shell completion — Run acli shell:complete once to get tab-completion for commands and flags.
Verify your setup — Run acli self:info to confirm your authenticated identity and acli version.
Stay updated — Run acli self:update regularly to get bug fixes and new features.
Clear caches on odd behavior — Run acli self:clear-caches if commands return unexpected results.
Next Steps

Now that you're set up, try:

Create your first IDE — Set up a development environment
Explore applications — Learn about your apps
Set up SSH keys — Secure authentication
Weekly Installs
29
Repository
acquia/acquia-skills
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn