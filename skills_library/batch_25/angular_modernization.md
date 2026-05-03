---
title: angular-modernization
url: https://skills.sh/bitwarden/clients/angular-modernization
---

# angular-modernization

skills/bitwarden/clients/angular-modernization
angular-modernization
Installation
$ npx skills add https://github.com/bitwarden/clients --skill angular-modernization
SKILL.md
Angular Modernization

Transforms legacy Angular components to modern architecture using a two-step approach:

Automated migrations - Angular CLI schematics for standalone, control flow, and signals
Bitwarden patterns - ADR compliance, OnPush change detection, proper visibility, thin components
Workflow
Step 1: Run Angular CLI Migrations

⚠️ CRITICAL: ALWAYS use Angular CLI migrations when available. DO NOT manually migrate features that have CLI schematics.

Angular provides automated schematics that handle edge cases, update tests, and ensure correctness. Manual migration should ONLY be used for patterns not covered by CLI tools.

IMPORTANT:

Always run the commands using npx ng.
All the commands must be run on directories and NOT files. Use the --path option to target directories.
Run migrations in order (some depend on others)
1. Standalone Components
npx ng generate @angular/core:standalone --path=<directory> --mode=convert-to-standalone


NgModule-based → standalone architecture

2. Control Flow Syntax
npx ng generate @angular/core:control-flow


*ngIf, *ngFor, *ngSwitch → @if, @for, @switch

3. Signal Inputs
npx ng generate @angular/core:signal-input-migration


@Input() → signal inputs

4. Signal Outputs
npx ng generate @angular/core:output-migration


@Output() → signal outputs

5. Signal Queries
npx ng generate @angular/core:signal-queries-migration


@ViewChild, @ContentChild, etc. → signal queries

6. inject() Function
npx ng generate @angular/core:inject-migration


Constructor injection → inject() function

7. Self-Closing Tag
npx ng generate @angular/core:self-closing-tag


Updates templates to self-closing syntax

8. Unused Imports
npx ng generate @angular/core:unused-imports


Removes unused imports

Step 2: Apply Bitwarden Patterns

See migration-patterns.md for detailed examples.

Add OnPush change detection
Apply visibility modifiers (protected for template access, private for internal)
Convert local component state to signals
Keep service observables (don't convert to signals)
Extract business logic to services
Organize class members correctly
Update tests for standalone
Step 3: Validate
Fix linting and formatting using npm run lint:fix
Run tests using npm run test

If any errors occur, fix them accordingly.

Key Decisions
Signals vs Observables
Signals - Component-local state only (ADR-0027)
Observables - Service state and cross-component communication (ADR-0003)
Use toSignal() to bridge observables into signal-based components
Visibility
protected - Template-accessible members
private - Internal implementation
Other Rules
Always add OnPush change detection
No TypeScript enums (use const objects with type aliases per ADR-0025)
No code regions (refactor instead)
Thin components (business logic in services)
Validation Checklist

Before completing migration:

 OnPush change detection added
 Visibility modifiers applied (protected/private)
 Signals for component state, observables for service state
 Class members organized (see migration-patterns.md)
 Tests updated and passing
 No new TypeScript enums
 No code regions
References
Bitwarden ADRs
ADR-0003: Observable Data Services
ADR-0025: No TypeScript Enums
ADR-0027: Angular Signals
Bitwarden Angular Style Guide
Angular Resources
Angular Style Guide
Angular Migrations
Angular CLI Schematics
Weekly Installs
91
Repository
bitwarden/clients
GitHub Stars
12.7K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass