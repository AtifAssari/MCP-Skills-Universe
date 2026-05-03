---
title: nginx
url: https://skills.sh/nejclovrencic/nginx-agent-skills/nginx
---

# nginx

skills/nejclovrencic/nginx-agent-skills/nginx
nginx
Installation
$ npx skills add https://github.com/nejclovrencic/nginx-agent-skills --skill nginx
SKILL.md
Nginx & OpenResty Development
Core Guidance

When writing or reviewing Nginx configuration:

Always consider the directive inheritance model. Child blocks inherit from parent unless they redefine the directive. For example, adding one proxy_set_header in a location block wipes all inherited proxy_set_header directives from the server block.
Prefer map over if for conditional logic. if in location context is dangerous and only reliably supports return and rewrite. See references/nginx-gotchas.md for the full list.
Always clarify proxy_pass trailing-slash behavior — it is the single most common source of subtle bugs.
When writing upstream blocks, always include keepalive configuration and explain connection pooling implications.
When writing Nginx directives, always check docs, specifically module references, to verify that a directive actually exists, and what values it accepts (on/off, variable, fixed values, etc).

When writing OpenResty/Lua code:

Always check phase restrictions before using cosocket or subrequest APIs. See references/openresty-api.md.
Prefer ngx.ctx over ngx.var for passing data between phases because it's more performant.
Avoid using ngx.var multiple times for the same variable, as it's less performant than accessing Lua variable.
Use ngx.timer.at for background/async work, never block the event loop.

When advising on performance:

Consult references/testing-patterns.md for benchmarking methodology.
Always consider the full request path: client → Nginx → upstream, and tune each segment.
Buffer sizing has cascading effects — refer to the buffer tuning section in references/nginx-gotchas.md.
Reference Files

Load these as needed based on the task:

references/nginx-gotchas.md — Directive behavior gotchas, inheritance rules, location matching, common misconfigurations. Read when writing or debugging any Nginx config.
references/openresty-api.md — Phase handler reference, shared dict operations. Read when writing Lua/OpenResty code.
references/testing-patterns.md — Config validation. Read when testing or benchmarking.
Weekly Installs
10
Repository
nejclovrencic/n…t-skills
GitHub Stars
10
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass