---
rating: ⭐⭐
title: laravel-11-12-app-guidelines
url: https://skills.sh/thienanblog/awesome-ai-agent-skills/laravel-11-12-app-guidelines
---

# laravel-11-12-app-guidelines

skills/thienanblog/awesome-ai-agent-skills/laravel-11-12-app-guidelines
laravel-11-12-app-guidelines
Installation
$ npx skills add https://github.com/thienanblog/awesome-ai-agent-skills --skill laravel-11-12-app-guidelines
Summary

Structured workflow for Laravel 11/12 apps with stack detection, Docker support, and framework-specific conventions.

Detects and adapts to your stack: API-only, Inertia + React, Livewire, Vue, or Blade; Docker Compose/Sail or host commands
Enforces Laravel 11/12 conventions: bootstrap configuration, Eloquent models, Form Requests, named routes, and safe migrations
Integrates Laravel Boost MCP tools for docs search, Artisan commands, routing inspection, and database queries
Prioritizes repository instructions (AGENTS.md, docs/) and existing patterns over generic assumptions
Includes testing and formatting guidance: PHPUnit feature tests, Pint linting, and minimal test runs before full suite execution
SKILL.md
Laravel 11/12 App Guidelines
Overview

Apply a consistent workflow for Laravel 11/12 apps with optional frontend stacks, Dockerized commands, and Laravel Boost tooling.

Quick Start
Read repository instructions first: AGENTS.md. If docs/ exists, read docs/README.md and relevant module docs before decisions.
Detect the stack and command locations; do not guess.
Use Laravel Boost search-docs for Laravel ecosystem guidance; use Context7 only if Boost docs are unavailable.
Follow repo conventions for naming, UI language, docs-first policies, and existing component patterns.
Stack Detection
Check composer.json, package.json, docker-compose.*, and config/* to confirm:
Docker Compose/Sail vs host commands
API-only vs full-stack
Frontend framework (Inertia/React, Livewire, Vue, Blade)
Auth (Fortify, Sanctum, Passport, custom)
Laravel 11/12 Core Conventions
Use the Laravel 11/12 structure: configure middleware, exceptions, and routes in bootstrap/app.php; service providers in bootstrap/providers.php; console configuration in routes/console.php.
Use Eloquent models and relationships first; avoid raw queries and DB:: unless truly necessary.
Create Form Request classes for validation instead of inline validation.
Prefer named routes and route() for URL generation.
When altering columns, include all existing attributes in the migration to avoid dropping them.
Ask before destructive database operations (e.g., reset/rollback/fresh).
API-Only Mode
Use routes/api.php; avoid Inertia and frontend assumptions.
Prefer API Resources and versioning if the repo already uses them.
Follow the repo's auth stack (Sanctum/Passport/custom) and response format conventions.
Do not require Vite/Tailwind/NPM unless the repo already includes them.
Inertia + React + Wayfinder (if present)
Use Inertia::render() for server-side routing; place pages under resources/js/Pages unless the repo says otherwise.
Use <Form> or useForm for Inertia forms; add skeleton/empty states for deferred props.
Use <Link> or router.visit() for navigation.
Use Wayfinder named imports for tree-shaking; avoid default imports; regenerate routes after changes if required.
Livewire / Vue / Blade (if present)
Follow existing component patterns and conventions; do not mix frameworks unless the repo already does.
Keep UI strings in the repo's expected language.
Tailwind CSS v4 (if present)
Use @import "tailwindcss"; and @theme for tokens.
Avoid deprecated utilities; use replacements (e.g., shrink-*, grow-*, text-ellipsis).
Use gap-* for spacing between items; follow existing dark mode conventions if present.
Testing and Formatting
Use PHPUnit; generate tests with php artisan make:test --phpunit and prefer feature tests.
Run the minimal relevant tests (php artisan test <file> or --filter=).
Run vendor/bin/pint --dirty before finalizing code changes.
After minimal tests pass, offer to run the full test suite.
Laravel Boost MCP Tools (when available)
search-docs before changing behavior or using framework features.
list-artisan-commands to confirm Artisan options.
list-routes to inspect routing changes.
tinker for PHP debugging and database-query for read-only DB checks.
browser-logs to inspect frontend errors.
get-absolute-url for sharing project URLs.
See references/boost-tools.md for query patterns and tool usage tips.
Output Expectations
Preserve existing architecture, structure, and dependencies unless the user explicitly requests changes.
Reuse existing components and follow local patterns.
Ask concise clarifying questions when repo guidance is missing or ambiguous.
Weekly Installs
720
Repository
thienanblog/awe…t-skills
GitHub Stars
56
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass