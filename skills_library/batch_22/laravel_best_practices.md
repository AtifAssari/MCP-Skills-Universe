---
title: laravel-best-practices
url: https://skills.sh/masterfermin02/laravel-agent-skill/laravel-best-practices
---

# laravel-best-practices

skills/masterfermin02/laravel-agent-skill/laravel-best-practices
laravel-best-practices
Installation
$ npx skills add https://github.com/masterfermin02/laravel-agent-skill --skill laravel-best-practices
SKILL.md
Purpose

This skill guides an AI coding agent to:

generate Laravel code aligned with established best practices,
review Laravel code (or diffs) and propose refactors aligned to those practices,
propose and scaffold tests (Pest preferred; PHPUnit supported).
Use when
Implementing or refactoring controllers, FormRequests, service/action classes, jobs, events/listeners, policies, observers
Reviewing PRs, diffs, or entire files in a Laravel application
Designing maintainable application layering and test strategy
Working on Inertia + React or Inertia + Vue frontends within a Laravel project
Rulebook

Use references/rulebook.json as the source of truth for:

rule ids
detection signals
recommended refactor patterns
expected outputs

When you flag an issue, always include:

rule_id
evidence (file + line numbers or excerpt)
minimal refactor steps first
test impact plan
Core principles (high-level)
Single Responsibility: one reason to change per class; one main concern per method.
Thin controllers: controllers orchestrate; business logic lives elsewhere.
Validation in FormRequests: move validation and authorization there.
Business logic in services/actions: extract workflows into testable units.
DRY: centralize repeated logic (Eloquent scopes, value objects/DTOs, helpers).
Prefer Eloquent + Collections: use expressive domain modeling where practical.
No queries in Blade: views must not query the database; eager load to avoid N+1.
Chunk/stream large datasets: avoid loading large tables into memory.
Policies for authorization: use Policy classes per model; keep authorize() calls in the HTTP layer, never inside services.
No env() outside config files: access environment values via config() throughout the app; env() only in config/*.php.
Follow naming conventions: singular PascalCase models and controllers, camelCase methods, snake_case config/migration keys, kebab-case route slugs.
Frontend / Inertia principles
Inertia + React

When reviewing or generating Inertia React code, apply rules INRT-001–INRT-010 from the rulebook. See references/inertia-react-summary.md for a quick-reference cheat sheet, or references/inertia-react.md for the full annotated directory structure and examples.

Directory structure: common (shared primitives), modules (feature code), pages (Inertia-rendered), shadcn (generated components).
Page components: suffix with Page, use a default export (e.g. PostsIndexPage.tsx).
Component files: one component per .tsx file, PascalCase filenames, function declarations.
Type page props: define a TypeScript interface per page; use usePage<SharedProps>() for globally shared data.
Form submissions: use useForm from @inertiajs/react; avoid raw fetch/axios for Inertia-driven forms.
Shared data: access via usePage() rather than prop-drilling auth/flash data through every component layer.
Internal navigation: use <Link> from @inertiajs/react; reserve plain <a> tags for external URLs.
Partial reloads: use router.reload({ only: [...] }) to refresh a subset of props instead of a full page visit.
Inertia + Vue

When reviewing or generating Inertia Vue code, apply rules INRT-VUE-001–INRT-VUE-005 from the rulebook. See references/inertia-vue.md for the annotated directory structure and conventions.

Directory structure: common (shared UI primitives), modules (feature code), pages (Inertia-rendered), lib (third-party/generated).
Page components: suffix with Page, use <script setup> or export default (e.g. PostsIndexPage.vue).
Component files: one component per .vue file, PascalCase filenames, prefer <script setup> + Composition API.
Third-party UI: keep in resources/js/lib; wrap in common for a project-friendly API — don't modify sources directly.
Workflow: Review

When asked to review code:

Identify the layer (Controller, Request, Model, Service/Action, Blade, etc.).
Apply rules from rulebook.json; emit findings with rule ids.
Provide a patch outline (what files to create/change) and a test plan.
Recommended output (JSON)

Return a JSON object:

summary: score, counts
findings[]: rule_id, severity, evidence, rationale, recommendations, patch outline
tests: a short matrix or list of impacted tests
Workflow: Generate code

When asked to implement a feature:

Propose file layout first (Controller + FormRequest + Service/Action + Model scopes, etc.).
Generate code using Laravel idioms: dependency injection, FormRequests, policies, resources.
Include a minimal test plan (Feature + Unit tests).
Workflow: Generate tests

Prefer Pest if repository uses Pest (presence of pestphp/pest in composer.json); otherwise PHPUnit.

FormRequest validation/authorization
Service/action business rules (unit)
Feature tests for endpoints (happy path + validation + authz)
Mock external systems (HTTP, queues, notifications) as needed
Weekly Installs
9
Repository
masterfermin02/…nt-skill
GitHub Stars
1
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass