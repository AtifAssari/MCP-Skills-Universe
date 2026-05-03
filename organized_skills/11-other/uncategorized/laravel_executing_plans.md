---
rating: ⭐⭐
title: laravel:executing-plans
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:executing-plans
---

# laravel:executing-plans

skills/jpcaparas/superpowers-laravel/laravel:executing-plans
laravel:executing-plans
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:executing-plans
SKILL.md
Executing Plans (Laravel)

Work in small batches. After each batch: tests green, quality clean, checkpoints recorded.

Loop
Pick next small task
Write failing test (feature or unit)
Minimal implementation; commit
Verify queues/events/IO if applicable
Run Pint, static analysis, tests (parallel)
Update docs/notes; checkpoint
Checkpoints
Tests pass locally; no errors/warnings
Pint clean; static analysis passes
Migrations safe and idempotent; no breaking edits to merged migrations
Queues healthy; Horizon metrics reasonable if used
Feature branch notes updated (what changed, why)

Repeat until plan complete, then run laravel:quality-checks and request review.

Weekly Installs
55
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026