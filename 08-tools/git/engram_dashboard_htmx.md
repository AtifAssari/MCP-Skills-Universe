---
title: engram-dashboard-htmx
url: https://skills.sh/gentleman-programming/engram/engram-dashboard-htmx
---

# engram-dashboard-htmx

skills/gentleman-programming/engram/engram-dashboard-htmx
engram-dashboard-htmx
Installation
$ npx skills add https://github.com/gentleman-programming/engram --skill engram-dashboard-htmx
SKILL.md
When to Use

Use this skill when:

Adding htmx partial loading or filter controls
Wiring forms or toggles in the dashboard
Changing browser/search interactions
HTMX Rules
Server-rendered HTML is the product; htmx enhances it, it does not replace it.
Prefer simple hx-get and hx-include over custom client-side state.
Filters must preserve the active state users would expect across interactions.
Forms that mutate system state must still work as normal HTTP posts.
Partial endpoints return meaningful HTML on their own, not fragments that depend on hidden JS assumptions.
Interaction Rules
Search and filter controls must compose cleanly.
Toggle actions must visibly reflect the resulting server state.
Connected navigation should keep URLs meaningful and shareable.
Use htmx for speed, not to hide business logic in the browser.
Weekly Installs
32
Repository
gentleman-progr…g/engram
GitHub Stars
3.1K
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass