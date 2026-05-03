---
rating: ⭐⭐⭐
title: laravel:quality-checks
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:quality-checks
---

# laravel:quality-checks

skills/jpcaparas/superpowers-laravel/laravel:quality-checks
laravel:quality-checks
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:quality-checks
SKILL.md
Quality Checks (Laravel)

Run automated checks before handoff or completion. Keep output clean.

PHP Style & Lint
# Check
sail pint --test    # or: vendor/bin/pint --test

# Fix
sail pint           # or: vendor/bin/pint

Static Analysis (choose your tool)
# PHPStan example
sail vendor/bin/phpstan analyse --memory-limit=1G   # or: vendor/bin/phpstan analyse --memory-limit=1G

# Psalm example
sail vendor/bin/psalm                               # or: vendor/bin/psalm

Insights (optional, if installed)
sail artisan insights --no-interaction --format=json --flush-cache   # or: php artisan insights --no-interaction --format=json --flush-cache

Tests
sail artisan test --parallel   # or: php artisan test --parallel

Frontend (if applicable)
sail pnpm run lint    # or: pnpm run lint
sail pnpm run types   # or: pnpm run types

Checklist
 Pint clean (no errors)
 Static analysis passes
 Tests pass locally (parallel where possible)
 Frontend lint/types clean (if present)
 No noisy logs/errors during runs
Weekly Installs
79
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026