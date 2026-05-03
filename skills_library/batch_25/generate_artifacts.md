---
title: generate-artifacts
url: https://skills.sh/haibaraaiaptx/frontend-openapi-skills/generate-artifacts
---

# generate-artifacts

skills/haibaraaiaptx/frontend-openapi-skills/generate-artifacts
generate-artifacts
Installation
$ npx skills add https://github.com/haibaraaiaptx/frontend-openapi-skills --skill generate-artifacts
SKILL.md
OpenAPI Artifact Generation

Generate models and request layer code from OpenAPI via aptx-ft CLI.

Contents
Prerequisites
Command Overview
Parameter Reference
Discovery Phase
Workflow
Preserve Parameter Logic for Models
Manifest Tracking
Automatic Barrel Updates
Output Structure
Framework-Specific Guides
Boundaries
Prerequisites
pnpm add -D @aptx/frontend-tk-cli

Command Overview
Command	Purpose
model gen	Generate TypeScript models
aptx functions	Generate endpoint specs + function wrappers
aptx react-query	Generate React Query hooks
aptx vue-query	Generate Vue Query composables

⚠️ Dependency: react-query and vue-query require spec/ from aptx functions. Run functions first.

Parameter Reference

All paths are relative to working directory (project root).

Parameter	Required	Description
-i	✅	OpenAPI file path (e.g., ./openapi.json)
-o	✅	Output directory (e.g., ./src/api)
--model-mode	✅	relative (same project) or package (monorepo)
--model-path	✅	Path or package name for model imports
--client-mode	❌	global (default) / local / package
--client-package	❌	Custom client package name
--no-manifest	❌	Disable manifest tracking (default: false)
--manifest-dir	❌	Custom manifest directory (default: .generated)
--dry-run	❌	Preview mode without updating manifest (default: false)
Model Source Decision
Is models directory inside the same package where API code is generated?
├── YES → --model-mode relative --model-path ./src/models
└── NO  → --model-mode package --model-path @org/models (from package.json "name")

Client Mode Decision
Which HTTP client will the generated code use?
├── Default @aptx/api-client → omit or --client-mode global
├── Custom client in this project → --client-mode local
└── Custom client from npm package → --client-mode package --client-package @org/api-client


⚠️ All aptx commands require --model-mode and --model-path. Without these, generated code will have broken imports.

Discovery Phase - MANDATORY FIRST STEP

Before executing any generation command, discover the actual project configuration.

For Monorepo Projects
# 1. Find packages
ls -d packages/*/

# 2. Get model package name (use THIS for --model-path)
cat packages/domains/package.json  # Extract "name" field

# 3. Verify API package dependencies
cat packages/api/package.json

Critical Rules
❌ NEVER	✅ ALWAYS
Guess package name from directory	Read package.json "name" field
Assume @project-name/models	Use exact value from "name"
Infer from packages/domains/ path	Package name ≠ directory name
Discovery Checklist
 Model package directory (e.g., packages/domains/)
 Model package name from package.json (e.g., @repo/domains)
 API package directory (e.g., packages/api/)
 API output path (e.g., packages/api/src)
Workflow
Discovery → Read package.json files
Check output directory → determine if --preserve is needed for models
Confirm → Output dir, model/client settings with user
Execute → Show command, get approval, run
Preserve Parameter Logic for Models

ALWAYS check if target model directory contains existing files before generating:

# Check if model output directory has existing files
ls ./src/models/*.ts 2>/dev/null || echo "empty"

Directory State	Action
Empty or not exists	Generate models WITHOUT --preserve
Has existing .ts files	Generate models WITH --preserve to keep enum translations

Why: When regenerating models in a non-empty directory, --preserve keeps manually translated enum names while adding new values.

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
└── api files...

When to Use Manifest Options
Scenario	Command
Normal generation	Omit manifest options (default)
CI/CD without tracking	Add --no-manifest
Preview changes before applying	Add --dry-run
Custom manifest location	Add --manifest-dir ./meta
Automatic Barrel Updates

The CLI automatically updates barrel files (index.ts) after generation.

You no longer need to manually run barrel gen after generating artifacts - the generation commands handle this automatically.

What Gets Updated
<output>/index.ts - Barrel file for the output directory
Subdirectory barrel files as needed
When Manual Barrel Update is Needed

The automatic update handles most cases. Use manual barrel gen only when:

Fixing corrupted barrel files
Processing non-standard directory structures
One-time batch updates across multiple directories
Single Project
# 0. Check if models directory has existing files
ls ./src/models/*.ts 2>/dev/null

# 1. Models (add --preserve if directory is NOT empty)
pnpm exec aptx-ft -i ./openapi.json model gen --output ./src/models --style module --preserve

# 2. Functions
pnpm exec aptx-ft aptx functions -i ./openapi.json -o ./src/api \
  --model-mode relative --model-path ./src/models

# 3. Query layer (choose one)
pnpm exec aptx-ft aptx react-query -i ./openapi.json -o ./src/api \
  --model-mode relative --model-path ./src/models

# Preview changes without updating manifest
pnpm exec aptx-ft aptx functions -i ./openapi.json -o ./src/api \
  --model-mode relative --model-path ./src/models --dry-run

Monorepo
# 0. Check if models directory has existing files
ls ./packages/models/src/*.ts 2>/dev/null

# 1. Models (add --preserve if directory is NOT empty)
pnpm exec aptx-ft -i ./openapi.json model gen --output ./packages/models/src --style module --preserve

# 2. Functions
pnpm exec aptx-ft aptx functions -i ./openapi.json -o ./apps/web/src/api \
  --model-mode package --model-path @org/models

# 3. Query layer (choose one)
pnpm exec aptx-ft aptx react-query -i ./openapi.json -o ./apps/web/src/api \
  --client-mode package --client-package @org/api-client \
  --model-mode package --model-path @org/models

# Custom manifest directory
pnpm exec aptx-ft aptx functions -i ./openapi.json -o ./apps/web/src/api \
  --model-mode package --model-path @org/models --manifest-dir ./meta

Output Structure
src/api/
├── .generated/                     # Manifest tracking files
│   ├── manifest.json               # Tracks all generated files
│   ├── deletion-report.json        # Machine-readable change report
│   └── deletion-report.md          # Human-readable change report
├── index.ts                        # Barrel file (auto-updated)
├── spec/namespace/xxx.ts           # Endpoint definitions (from functions)
├── functions/namespace/xxx.ts      # Function wrappers (from functions)
├── react-query/namespace/          # React Query hooks
│   ├── xxx.query.ts
│   └── xxx.mutation.ts
└── vue-query/namespace/            # Vue Query composables
    ├── xxx.query.ts
    └── xxx.mutation.ts

Framework-Specific Guides
React Query: See references/react-query.md
Vue Query: See references/vue-query.md
Boundaries

This skill handles generic OpenAPI → TypeScript generation:

Does NOT process Materal-specific enum semantics → use adapt-materal-enums
Does NOT validate OpenAPI specification correctness
Does NOT handle authenticated URL downloads → use download-openapi first
Related Skills
download-openapi: Fetch OpenAPI spec from URL
generate-models: Model-only generation
adapt-materal-enums: Materal framework enum adaptation
Weekly Installs
24
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