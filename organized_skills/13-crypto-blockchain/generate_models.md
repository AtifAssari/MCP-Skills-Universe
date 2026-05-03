---
title: generate-models
url: https://skills.sh/haibaraaiaptx/frontend-openapi-skills/generate-models
---

# generate-models

skills/haibaraaiaptx/frontend-openapi-skills/generate-models
generate-models
Installation
$ npx skills add https://github.com/haibaraaiaptx/frontend-openapi-skills --skill generate-models
SKILL.md
Generate TypeScript Models

Generate TypeScript interfaces/enums from OpenAPI via aptx-ft.

Prerequisites
pnpm add -D @aptx/frontend-tk-cli

Discovery Phase - MANDATORY FIRST STEP

Before executing any generation command, you MUST discover the actual project configuration.

For Monorepo Projects

Find packages directory:

ls -d packages/*/


Identify model package and get its name:

# Find package that likely contains models (domains, models, types, shared, etc.)
cat packages/domains/package.json 2>/dev/null || cat packages/models/package.json 2>/dev/null


Extract the "name" field - this is your --model-path value.

Critical Rules
❌ NEVER Do This	✅ ALWAYS Do This
Guess package name from project directory	Read package.json to get actual "name"
Assume @project-name/models	Use the exact value from "name" field
Infer from packages/domains/ path	Package name ≠ directory name
Example Discovery
# User says: "generate to packages/domains"

$ cat packages/domains/package.json
{ "name": "@repo/domains", ... }  ← Package name is @repo/domains

Workflow
Discovery → Read package.json files to get actual package names
Identify project type → recommend parameters
Check output directory → determine if --preserve is needed
Confirm with user → output dir, style, filters
Execute → show command, get approval, run
Preserve Parameter Logic

ALWAYS check if target directory contains existing models before generating:

# Check if output directory has existing model files
ls ./src/models/*.ts 2>/dev/null || echo "empty"

Directory State	Action
Empty or not exists	Generate WITHOUT --preserve
Has existing .ts files	Generate WITH --preserve to keep enum translations

Why: When regenerating models in a non-empty directory, --preserve keeps manually translated enum names while adding new values. Only skip --preserve for fresh generation.

Project Types
Type	Output	Command
Single project	./src/models	pnpm exec aptx-ft -i ./openapi.json model gen --output ./src/models --style module
Monorepo	./packages/models/src	pnpm exec aptx-ft -i ./openapi.json model gen --output ./packages/models/src --style module
Key Options
Option	Purpose
--style module	ES modules, individual exports (default, recommended)
--style declaration	Single declaration file (legacy compatibility)
--name <Schema>	Generate only specified models (repeatable)
--preserve	Keep manually translated enum names on regeneration
Manifest Tracking

The CLI automatically tracks generated files and detects changes between generations.

Manifest CLI Options
Option	Default	Purpose
--no-manifest	false	Disable manifest tracking
--manifest-dir <path>	.generated	Custom manifest directory
--dry-run	false	Preview mode: generate report without updating manifest
Generated Manifest Files

When manifest tracking is enabled (default), the following files are generated:

<output>/
├── .generated/
│   ├── manifest.json           # Tracks all generated files
│   ├── deletion-report.json    # Machine-readable change report
│   └── deletion-report.md      # Human-readable change report with LLM suggestions
└── models...

Manifest Report Contents

The deletion-report.md includes:

Summary table: Added/deleted/unchanged file counts
Deleted files: List of files removed since last generation
Added files: List of new files added
LLM suggestions: Follow-up actions for handling deleted files
When to Use Manifest Options
Scenario	Command
Normal generation	Omit manifest options (default)
CI/CD without tracking	Add --no-manifest
Preview changes before applying	Add --dry-run
Custom manifest location	Add --manifest-dir ./meta
Automatic Barrel Updates

The CLI automatically updates barrel files (index.ts) after generation.

You no longer need to manually run barrel gen after generating models - the model gen command handles this automatically.

What Gets Updated
<output>/index.ts - Barrel file for the models directory
When Manual Barrel Update is Needed

The automatic update handles most cases. Use manual barrel gen only when:

Fixing corrupted barrel files
Processing non-standard directory structures
One-time batch updates across multiple directories
Preserve Workflow
Preserve Workflow

Recommended when regenerating models after API updates. Keeps manually translated enum names while adding new values.

Generate models
Manually translate enums (e.g., Value1 → Success)
API updates with new enum values
Regenerate with --preserve → keeps translations, adds new values
# First generation
pnpm exec aptx-ft -i ./openapi.json model gen --output ./src/models

# After translating enums, regenerate with preserve
pnpm exec aptx-ft -i ./openapi.json model gen --output ./src/models --preserve

Quick Reference
# Check if output directory has existing models first
ls ./src/models/*.ts 2>/dev/null

# First generation (empty directory)
pnpm exec aptx-ft -i ./openapi.json model gen --output ./src/models

# Regeneration (non-empty directory) - use --preserve
pnpm exec aptx-ft -i ./openapi.json model gen --output ./src/models --preserve

# Declaration style
pnpm exec aptx-ft -i ./openapi.json model gen --output ./src/models --style declaration

# Selective generation
pnpm exec aptx-ft -i ./openapi.json model gen --output ./src/models --name User --name Role

# Preview changes without updating manifest
pnpm exec aptx-ft -i ./openapi.json model gen --output ./src/models --dry-run

# Disable manifest tracking (CI/CD)
pnpm exec aptx-ft -i ./openapi.json model gen --output ./src/models --no-manifest

# Custom manifest directory
pnpm exec aptx-ft -i ./openapi.json model gen --output ./src/models --manifest-dir ./meta

# Without pnpm
npx aptx-ft -i ./openapi.json model gen --output ./src/models

Output

TypeScript model files (interface/enum). Does not include request layer code.

Boundaries

This skill generates TypeScript models only:

Does NOT generate request layer code (functions, hooks) → use generate-artifacts
Does NOT adapt Materal-specific enum semantics → use adapt-materal-enums
Does NOT validate OpenAPI specification correctness
Only supports JSON format (not YAML)
Related Skills
generate-artifacts: Full generation (models + request layer)
adapt-materal-enums: Materal framework enum adaptation
download-openapi: Fetch OpenAPI spec from URL
Weekly Installs
23
Repository
haibaraaiaptx/f…i-skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass