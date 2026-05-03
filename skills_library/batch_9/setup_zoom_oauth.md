---
title: setup-zoom-oauth
url: https://skills.sh/anthropics/knowledge-work-plugins/setup-zoom-oauth
---

# setup-zoom-oauth

skills/anthropics/knowledge-work-plugins/setup-zoom-oauth
setup-zoom-oauth
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill setup-zoom-oauth
SKILL.md
/setup-zoom-oauth

Use this skill when auth is the blocker or when auth choices will shape the entire integration.

Scope
App type selection
OAuth grant selection
Scope planning
Token exchange and refresh
Auth debugging and environment assumptions
Workflow
Determine the app model and who is authorizing whom.
Choose the correct grant flow.
Identify minimum scopes for the user flow.
Define token storage and refresh behavior.
Route into the deepest relevant reference docs only after the above is clear.
Primary References
oauth
general
rest-api
Common Mistakes
Picking a grant before clarifying the actor and tenant model
Asking for broad scopes before confirming the exact workflow
Forgetting refresh-token behavior and token lifecycle handling
Reusing an old refresh token after a successful refresh instead of storing the newly returned one
Treating auth failures as API failures without checking app configuration first
Weekly Installs
298
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass