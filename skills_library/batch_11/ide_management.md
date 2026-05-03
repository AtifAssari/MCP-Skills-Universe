---
title: ide-management
url: https://skills.sh/acquia/acquia-skills/ide-management
---

# ide-management

skills/acquia/acquia-skills/ide-management
ide-management
Installation
$ npx skills add https://github.com/acquia/acquia-skills --skill ide-management
SKILL.md
Managing Cloud IDEs

Use when:

Creating, opening, or sharing a Cloud IDE
Deleting or listing Cloud IDEs
Configuring IDE services or checking hibernation status
What is a Cloud IDE?

A Cloud IDE is a complete Drupal development environment that includes:

Theia IDE — Web-based code editor (VS Code-like interface)
Apache & PHP — Full Drupal web server
MySQL Database — Development database
Drush — Drupal command-line tool
Composer — PHP dependency manager
Git — Version control

Hibernation: IDEs automatically enter hibernation after 2 hours of inactivity, consuming minimal resources. They wake automatically when you access them.

List Your IDEs
See all IDEs for a given application
acli ide:list 2>/dev/null | grep -v "is available\|self-update"
acli ide:list:app <applicationUuid> 2>/dev/null | grep -v "is available\|self-update"
acli ide:list:app myapp 2>/dev/null | grep -v "is available\|self-update"


Output:

Select a Cloud Platform application:
  [0] My App (prod, staging, dev)
  [1] Other App (prod, staging)

IDEs for My App:
  My IDE (another.user@example.com)
    Web URL: https://ide-12345.ides.acquia.com
    IDE URL: https://ide-12345.web.ahdev.cloud
    Created: 2024-01-15

Other IDE (another.user@example.com)
    Web URL: https://ide-67890.ides.acquia.com
    IDE URL: https://ide-67890.web.ahdev.cloud
    Created: 2024-02-20

List IDEs belonging to you (across all applications)
acli ide:list:mine 2>/dev/null | grep -v "is available\|self-update"


Shows only IDEs you personally own across all applications.

Create a New IDE
Interactive Wizard
acli ide:create 2>/dev/null


Prompts you step-by-step:

? Do you want to link a local project? (Yes/No)
? Select a Cloud Platform application: [0] My App
? Enter a label for your IDE: (optional, default shows your name)
? Creating your Cloud IDE...
✓ IDE created successfully!

Your IDE is ready at: https://ide-12345.ides.acquia.com

Scripted (non-interactive)
# Create IDE for specific application
acli ide:create --application=abc123-def456 --label="My IDE" 2>/dev/null

# Fastest option - uses defaults if possible
acli ide:create --application=abc123-def456 2>/dev/null

What happens after creation?
IDE provisioning (~2-3 minutes)
Theia loads with your codebase
Databases are cloned from your application
Development environment is ready
Open an IDE in Your Browser
Open directly
acli ide:open 2>/dev/null


Prompts which IDE if you have multiple.

With application context
acli ide:open --application=abc123 2>/dev/null

Get just the URL
acli ide:info 2>/dev/null


Shows the IDE URL and details.

Get IDE Information
acli ide:info 2>/dev/null


Output:

IDE: My IDE
  Application: My App (abc123-def456)
  Owner: another.user@example.com
  Label: My IDE
  Created: 2024-01-15
  Last Activity: 2024-02-20 14:23:00
  Status: Running
  Web URL: https://ide-12345.web.ahdev.cloud
  IDE URL: https://ide-12345.ides.acquia.com

Delete an IDE
Delete with confirmation
acli ide:delete 2>/dev/null


Prompts for confirmation:

? Select the IDE you want to delete: [0] My IDE
? Delete "My IDE"? This cannot be undone. (yes/no)
Deleting IDE...
✓ IDE deleted successfully.

Delete non-interactively
acli ide:delete --ide=12345 2>/dev/null


Note: This is permanent and cannot be undone. Make sure to push any uncommitted code to Git!

Share an IDE with Teammates
Get the share URL
acli ide:share


Prints the share URL for your IDE:

Share URL: https://ide-12345.ides.acquia.com?share_token=abc123xyz

Regenerate the share token
acli ide:share --regenerate


Invalidates the old token and prints a new share URL.

Access shared IDE

Your teammate clicks the share URL and gets temporary read access. They don't need their own IDE or application access.

Configure & Manage IDE Services
Change PHP version
acli ide:php-version <version>


Example:

acli ide:php-version 8.2
acli ide:php-version 8.1


Validates the version exists on the system, updates the config, and restarts php-fpm automatically.

Manage IDE Services

Valid service names: php, php-fpm, apache, apache2, mysql, mysqld

# Start a service
acli ide:service-start apache
acli ide:service-start mysql

# Stop a service
acli ide:service-stop apache

# Restart a service
acli ide:service-restart php
acli ide:service-restart apache
acli ide:service-restart mysql

Toggle Xdebug
acli ide:xdebug-toggle


Checks the current state and switches it — enables if disabled, disables if enabled. Alias: xdebug.

Hibernation

IDEs automatically hibernate after 2 hours of inactivity and wake automatically when accessed (1–2 minute startup). Hibernated IDEs consume minimal resources.

To check status or get URLs:

acli ide:info 2>/dev/null


To wake a hibernated IDE, simply open it:

acli ide:open


The IDE will wake automatically. If stuck, try restarting services:

acli ide:service-restart apache
acli ide:service-restart php

Best Practices
1. One IDE per Feature Branch

Create a new IDE for each feature you're working on:

acli ide:create --label="Feature: New Homepage" 2>/dev/null


This keeps work isolated and makes it easy to switch between tasks.

2. Delete Idle IDEs

Remove IDEs you're no longer using to keep your account clean:

acli ide:delete 2>/dev/null

3. Use IDE Labels Wisely

Choose descriptive labels:

# ✓ Good
acli ide:create --label="Feature: ACN Migration" 2>/dev/null
acli ide:create --label="Bug Fix: Login Form Issue" 2>/dev/null
acli ide:create --label="Client: Acme Corp Review" 2>/dev/null

# ✗ Bad
acli ide:create --label="IDE 1" 2>/dev/null
acli ide:create --label="Test" 2>/dev/null

4. Push Code Regularly

Your IDE has Git access. Push to your repository frequently.

5. Monitor Resources

Large IDEs use more resources. Check your Acquia Cloud dashboard if you hit limits.

Troubleshooting
IDE won't start / stuck loading

Delete and recreate the IDE:

acli ide:delete 2>/dev/null
acli ide:create 2>/dev/null

"Access Denied" error

You might not have permission to the application. Verify:

acli api:applications:list 2>/dev/null

IDE is very slow

This is often due to hibernation waking (wait 30–60 seconds) or a large codebase. If it persists, recreate the IDE:

acli ide:create 2>/dev/null

Can't SSH into IDE

Set up SSH keys first:

acli ssh-key:list 2>/dev/null

# If no keys, create one
acli ssh-key:create 2>/dev/null

Related Topics
SSH Key Management — Set up secure SSH access
Troubleshooting
Weekly Installs
23
Repository
acquia/acquia-skills
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass