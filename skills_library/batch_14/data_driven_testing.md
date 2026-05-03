---
title: data-driven-testing
url: https://skills.sh/0xbigboss/claude-code/data-driven-testing
---

# data-driven-testing

skills/0xbigboss/claude-code/data-driven-testing
data-driven-testing
Installation
$ npx skills add https://github.com/0xbigboss/claude-code --skill data-driven-testing
SKILL.md
Deprecated

This skill has been replaced by testing-best-practices.

Use testing-best-practices for all test design, test case generation, and test strategy work.

What changed
Test layering policy (unit / integration / e2e) replaces the unit-only DDT focus.
Markdown tables replace the rigid canonical JSON test-case schema.
Output is strategy + matrix + implementation plan, not JSON blocks.
Added: hard rules against fabricated fixtures and invented source locations.
Added: e2e execution guidance (preflight, async polling, flake handling).
Added: CI lane guidance (PR smoke vs nightly full).
Auth-state reuse and idempotent/state-tolerant e2e are first-class concerns.
Weekly Installs
59
Repository
0xbigboss/claude-code
GitHub Stars
43
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass