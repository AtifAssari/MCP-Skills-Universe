---
title: laravel:e2e-playwright
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:e2e-playwright
---

# laravel:e2e-playwright

skills/jpcaparas/superpowers-laravel/laravel:e2e-playwright
laravel:e2e-playwright
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:e2e-playwright
SKILL.md
E2E Playwright (Laravel)

Keep E2E tests reliable, fast, and maintainable.

Environment
# Sail
sail pnpm playwright:test

# Non‑Sail
pnpm playwright:test


Use a dedicated .env.playwright and rebuild schema with migrate:fresh --seed before running.

State & Seeds
Provide seeders for common scenarios (users, roles, demo content)
Use factories for per‑test setup; reset state between specs
Test IDs & Selectors
Prefer data-testid attributes over CSS paths
Keep selectors stable through refactors
Auth
Reuse storage state when possible (logged‑in cookies/session)
Otherwise create user via API/setup to avoid UI login flakiness
Patterns
Break large flows into steps; assert key milestones
Record videos/screenshots only on failure to keep suites fast
Weekly Installs
49
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026