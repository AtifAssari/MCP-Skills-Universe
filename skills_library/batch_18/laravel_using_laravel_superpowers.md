---
title: laravel:using-laravel-superpowers
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:using-laravel-superpowers
---

# laravel:using-laravel-superpowers

skills/jpcaparas/superpowers-laravel/laravel:using-laravel-superpowers
laravel:using-laravel-superpowers
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:using-laravel-superpowers
SKILL.md
Using Superpowers in Laravel Projects

This plugin adds Laravel-aware guidance while staying platform-agnostic. It works in any Laravel app with or without Sail.

Runner Selection (Sail or non-Sail)

Use the minimal wrapper below when running commands:

# Prefer Sail if available, else fall back to host
alias sail='sh $([ -f sail ] && echo sail || echo vendor/bin/sail)'

# Example (both work depending on environment)
sail artisan test           # with Sail
php artisan test            # without Sail
sail composer require x/y   # with Sail
composer require x/y        # without Sail


See the laravel:runner-selection skill for detection tips, command pairs, and safety notes.

Core Workflows
Test-Driven Development first: use laravel:tdd-with-pest
Database changes: use laravel:migrations-and-factories
Quality gates: use laravel:quality-checks (Pint, Insights/PHPStan)
Queues and Horizon: use laravel:queues-and-horizon
Architecture patterns: laravel:ports-and-adapters, laravel:template-method-and-plugins
Keep complexity low: laravel:complexity-guardrails
Philosophy
Favor small, testable services; avoid fat controllers/commands/jobs
DTOs, typed Collections, and Enums when they clarify intent
Prefer model factories in tests and model scopes for complex queries
Verify before completion—run tests and linters clean

Use slash commands as needed:

/superpowers-laravel:brainstorm
/superpowers-laravel:write-plan
/superpowers-laravel:execute-plan


When a Laravel skill exists for your task, use it exactly as written.

Weekly Installs
59
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026