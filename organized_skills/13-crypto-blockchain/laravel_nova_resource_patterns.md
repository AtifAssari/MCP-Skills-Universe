---
rating: ⭐⭐
title: laravel:nova:resource-patterns
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:nova:resource-patterns
---

# laravel:nova:resource-patterns

skills/jpcaparas/superpowers-laravel/laravel:nova:resource-patterns
laravel:nova:resource-patterns
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:nova:resource-patterns
SKILL.md
Nova Resource Patterns

Build consistent Nova resources that mirror domain models and evolve safely.

Fields
Keep fields ordered: identifiers → primary attributes → relations → meta
Use ->sortable()/->filterable() where it delivers value
Hide sensitive fields (e.g., tokens) from index/detail unless necessary
Prefer BelongsTo/HasMany/Morph* relations with searchable constraints
Authorization
Use Nova policies mirroring model policies for viewAny, view, create, update, delete
Avoid leaking existence via unauthorized search; scope queries
Actions
Keep actions idempotent or provide safeguards
Provide confirmation messages and clear result feedback
Filters & Lenses
Filters: simple, commonly used constraints (status, owner, date range)
Lenses: opinionated, task‑centric views (e.g., stale items)
Metrics
Value/Trend/Partition metrics for essentials; cache appropriately
Use explicit time ranges; label units clearly
Resource Organization
Group resources by domain (navigation grouping)
Keep display titles meaningful; use title() consistently
Testing
Prefer feature tests that exercise policy + query scope + resource logic
For actions, test success and failure states with realistic seed data
Weekly Installs
47
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026