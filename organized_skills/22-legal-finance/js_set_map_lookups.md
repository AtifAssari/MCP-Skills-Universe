---
rating: ⭐⭐
title: js-set-map-lookups
url: https://skills.sh/theorcdev/8bitcn-ui/js-set-map-lookups
---

# js-set-map-lookups

skills/theorcdev/8bitcn-ui/js-set-map-lookups
js-set-map-lookups
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill js-set-map-lookups
SKILL.md
Use Set/Map for O(1) Lookups

Convert arrays to Set/Map for repeated membership checks.

Incorrect (O(n) per check):

const allowedIds = ['a', 'b', 'c', ...]
items.filter(item => allowedIds.includes(item.id))


Correct (O(1) per check):

const allowedIds = new Set(['a', 'b', 'c', ...])
items.filter(item => allowedIds.has(item.id))

Weekly Installs
24
Repository
theorcdev/8bitcn-ui
GitHub Stars
1.8K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass