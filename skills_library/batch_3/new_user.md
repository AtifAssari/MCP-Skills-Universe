---
title: new-user
url: https://skills.sh/medusajs/medusa-agent-skills/new-user
---

# new-user

skills/medusajs/medusa-agent-skills/new-user
new-user
Installation
$ npx skills add https://github.com/medusajs/medusa-agent-skills --skill new-user
Summary

Create a new admin user in Medusa with email and password.

Accepts email and password as command arguments to set up admin credentials
Executes npx medusa user command via Bash with -e and -p flags
Reports creation success, user email, errors, and next steps for admin dashboard login
SKILL.md
Create Admin User

Create a new admin user in Medusa with the specified email and password.

The user will provide two arguments:

First argument: email address
Second argument: password

For example: /medusa-dev:user admin@test.com supersecret

Use the Bash tool to execute the command npx medusa user -e <email> -p <password>, replacing <email> with the first argument and <password> with the second argument.

Report the results to the user, including:

Confirmation that the admin user was created successfully
The email address of the created user
Any errors that occurred
Next steps (e.g., logging in to the admin dashboard)
Weekly Installs
816
Repository
medusajs/medusa…t-skills
GitHub Stars
157
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail