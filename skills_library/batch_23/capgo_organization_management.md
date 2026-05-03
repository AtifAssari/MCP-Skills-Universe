---
title: capgo-organization-management
url: https://skills.sh/cap-go/capgo-skills/capgo-organization-management
---

# capgo-organization-management

skills/cap-go/capgo-skills/capgo-organization-management
capgo-organization-management
Installation
$ npx skills add https://github.com/cap-go/capgo-skills --skill capgo-organization-management
SKILL.md
Capgo Organization Management

Use this skill for Capgo account and organization administration commands.

When to Use This Skill
User wants the current account ID
User wants to list or create organizations
User wants to inspect members or enforce organization security settings
Procedures
Step 1: Identify the Scope

Decide whether the request is:

account lookup
organization listing or creation
member inspection
organization security configuration
Step 2: Use the Matching CLI Command

Prefer the Capgo CLI:

npx @capgo/cli@latest organization list


Use account id for safe account sharing and support workflows.

Step 3: Apply Security Changes Carefully

For security settings such as 2FA enforcement, password policy, or API key expiration:

inspect current member status first
verify the acting user has the required admin role
change one policy area at a time
Error Handling
For permission failures, verify the current user role before retrying administrative changes.
For organization security changes, inspect member readiness first so enforcement does not lock users out unexpectedly.
Use organization, not the deprecated organisation, in all new guidance.
Weekly Installs
83
Repository
cap-go/capgo-skills
GitHub Stars
32
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass