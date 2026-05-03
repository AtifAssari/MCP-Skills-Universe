---
title: laravel:daily-workflow
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:daily-workflow
---

# laravel:daily-workflow

skills/jpcaparas/superpowers-laravel/laravel:daily-workflow
laravel:daily-workflow
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:daily-workflow
SKILL.md
Daily Workflow (Laravel)

Run through this checklist at the start of a session or before handoff.

# Start services
sail up -d && sail ps                     # Sail
# or (non‑Sail): ensure PHP/DB are running locally

# Schema as needed
sail artisan migrate                      # or: php artisan migrate

# Queue worker if required
sail artisan queue:work --tries=3         # or: php artisan queue:work --tries=3

# Quality gates
sail pint --test && sail pint             # or: vendor/bin/pint --test && vendor/bin/pint
sail artisan test --parallel              # or: php artisan test --parallel

# Frontend (if present)
sail pnpm run lint && sail pnpm run types # or: pnpm run lint && pnpm run types

Weekly Installs
49
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026