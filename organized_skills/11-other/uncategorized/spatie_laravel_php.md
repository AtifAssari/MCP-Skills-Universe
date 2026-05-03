---
rating: ⭐⭐
title: spatie-laravel-php
url: https://skills.sh/spatie/guidelines-skills/spatie-laravel-php
---

# spatie-laravel-php

skills/spatie/guidelines-skills/spatie-laravel-php
spatie-laravel-php
Installation
$ npx skills add https://github.com/spatie/guidelines-skills --skill spatie-laravel-php
SKILL.md
Spatie Laravel & PHP Guidelines
Overview

Apply Spatie's Laravel and PHP guidelines to keep code style consistent and Laravel-native.

When to Activate
Activate this skill for any Laravel or PHP coding work, even if the user does not explicitly mention Spatie.
Activate this skill when asked to generate, edit, format, refactor, review, or align Laravel/PHP code.
Activate this skill when working on .php or .blade.php files, routes, controllers, models, config, validation, migrations, or tests.
Scope
In scope: .php, .blade.php, Laravel conventions (routes, controllers, config, validation, migrations, tests).
Out of scope: JS/TS, CSS, infrastructure, database schema design, non-Laravel frameworks.
Workflow
Identify the artifact (controller, route, config, model, Blade, test, etc.).
Read references/spatie-laravel-php-guidelines.md and focus on the relevant sections.
Apply the core Laravel principle first, then PHP standards, then section-specific rules.
If a rule conflicts with existing project conventions, follow Laravel conventions and keep changes consistent.
Core Rules (Summary)
Follow Laravel conventions first.
Follow PSR-1, PSR-2, and PSR-12.
Prefer typed properties and explicit return types (including void).
Use short nullable syntax like ?string.
Use constructor property promotion when all properties can be promoted.
One trait per line with separate use statements.
Prefer early returns and avoid else when possible.
Always use curly braces for control structures.
Use string interpolation over concatenation.
Happy path last: handle error conditions first.
Do and Don't

Do:

Use kebab-case URLs, camelCase route names, and camelCase route parameters.
Use tuple notation for routes: [Controller::class, 'method'].
Use plural resource names for controllers (PostsController).
Use array notation for validation rules.
Use config() helper and avoid env() outside config files.
Add service configs to config/services.php, not new files.
Use __() for translations instead of @lang.
Use PascalCase for enum values.

Don't:

Add docblocks when full type hints already exist.
Use fully qualified classnames in docblocks.
Use final or readonly by default.
Use else when early returns work.
Add spaces after Blade control structures.
Write down methods in migrations, only up methods.
Examples
// Happy path last with early returns
if (! $user) {
    return null;
}

if (! $user->isActive()) {
    return null;
}

// Process active user...

// Short ternary
$name = $isFoo ? 'foo' : 'bar';

// Constructor property promotion
class MyClass {
    public function __construct(
        protected string $firstArgument,
        protected string $secondArgument,
    ) {}
}

@if($condition)
    Something
@endif

References
references/spatie-laravel-php-guidelines.md
Weekly Installs
225
Repository
spatie/guidelines-skills
GitHub Stars
77
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass