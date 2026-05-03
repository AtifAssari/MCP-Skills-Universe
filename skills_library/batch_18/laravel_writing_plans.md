---
title: laravel:writing-plans
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:writing-plans
---

# laravel:writing-plans

skills/jpcaparas/superpowers-laravel/laravel:writing-plans
laravel:writing-plans
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:writing-plans
SKILL.md
Writing Plans (Laravel)

Turn a confirmed design into a sequence of small, testable steps. Include guardrails and validation before handoff.

Structure
Scaffolding
Runner: confirm Sail or host
Branch & workspace prep (worktrees optional)
Data Model
Migrations and factories (one commit per change)
Seeders if needed for demo flows
Services & Interfaces
Controllers/Requests/Resources (or actions)
Ports & adapters for external systems
Jobs/events/listeners as needed
Tests (TDD)
Feature tests for behavior; unit tests for pure logic
Use factories; verify failure first, then pass
Quality Gates
Pint, static analysis, tests clean
Rollout & Observability
Logs/metrics; Horizon queues; toggles/migrations safety
Example Task Format
Add migration + model + factory for X
Write failing feature test for route Y
Implement controller + request + policy for Y
Add service with port+adapter for Z
Dispatch job; add listener + events as needed
Verify queues; add tags and Horizon metrics
Run quality checks; update docs

After writing the plan, use laravel:executing-plans to execute in batches.

Weekly Installs
69
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026