---
rating: ⭐⭐⭐
title: ruler-rules-init
url: https://skills.sh/adonis0123/adonis-skills/ruler-rules-init
---

# ruler-rules-init

skills/adonis0123/adonis-skills/ruler-rules-init
ruler-rules-init
Installation
$ npx skills add https://github.com/adonis0123/adonis-skills --skill ruler-rules-init
SKILL.md
Ruler Rules Migration
Overview

Migrate a repository to a reusable Ruler rules structure with a safe audit/apply workflow. Keep default templates in English and avoid overwriting existing repository-specific content unless explicitly forced. Support different project types through preset-based template selection.

Inputs

Collect these inputs before applying changes:

Target repository root path.
Whether to run in audit or apply mode.
Template preset: auto, base, nextjs, monorepo, or node-lib (default: auto).
Whether to include optional skills:sync:claude integration.
Whether overwrite is allowed for differing files (--force).
Presets

Presets control the content of project-specific template files (10-project-context.md, 20-dev-commands.md, 30-coding-conventions.md). Universal files (ruler.toml, AGENTS.md, 00-core-principles.md) are always sourced from the base directory.

Preset	Auto-detect Signal	Use Case
base	Fallback	Any project, minimal with placeholders
nextjs	next.config.* exists	Next.js App Router projects
monorepo	turbo.json or pnpm-workspace.yaml exists	Turborepo / pnpm workspace
node-lib	package.json has main or exports, no next.config.*	Node.js libraries
Preset Selection Priority
Explicit --preset <name> flag (highest priority).
Auto-detection from target repo files (when --preset auto or omitted).
Falls back to base if no signals match.
Workflow
Run the bootstrap script in audit mode.
Review missing files, differences, and manual actions.
Run in apply mode to create missing files and safe defaults.
Re-run apply to confirm idempotency.
Run ruler:apply in the target repo to generate root rule outputs.
Decision Tree

Need only Ruler integration: Use default behavior (do not pass --with-optional-sync).

Need optional Claude skills sync as well: Pass --with-optional-sync to include skills:sync:claude suggestions.

Targeting a specific project type: Pass --preset nextjs, --preset monorepo, or --preset node-lib. Or let auto-detection choose the right preset.

Existing files differ from templates:

Keep defaults safe: do not override without --force.
Use --force only when intentional template replacement is required.
Commands

Use these commands from this skill directory:

# Audit (default preset auto-detection)
node ./scripts/bootstrap-ruler.mjs --target /path/to/repo --mode audit

# Apply with auto-detected preset
node ./scripts/bootstrap-ruler.mjs --target /path/to/repo --mode apply

# Apply with explicit preset
node ./scripts/bootstrap-ruler.mjs --target /path/to/repo --mode apply --preset nextjs
node ./scripts/bootstrap-ruler.mjs --target /path/to/repo --mode apply --preset monorepo
node ./scripts/bootstrap-ruler.mjs --target /path/to/repo --mode apply --preset node-lib
node ./scripts/bootstrap-ruler.mjs --target /path/to/repo --mode apply --preset base

# With optional sync and force
node ./scripts/bootstrap-ruler.mjs --target /path/to/repo --mode apply --preset nextjs --with-optional-sync
node ./scripts/bootstrap-ruler.mjs --target /path/to/repo --mode apply --force

Validation Checklist

After applying, verify:

.ruler/ruler.toml exists and defines codex + claude outputs.
Required .ruler/*.md templates exist.
.gitignore contains the Ruler generated-files block.
package.json contains ruler:apply.
If is-ci style guard is used, is-ci is installed (pnpm add -D is-ci).
postinstall follows the CI-skip recommendation or an explicit local alternative (preserve existing setup commands by chaining with && (...)).
Running ruler:apply succeeds in the target repository.
Resources

Script: scripts/bootstrap-ruler.mjs

References: references/migration-playbook.md references/applyto-patterns.md

Templates: assets/templates/base/.ruler/ (universal + fallback) assets/templates/presets/nextjs/.ruler/ (Next.js overlay) assets/templates/presets/monorepo/.ruler/ (monorepo overlay) assets/templates/presets/node-lib/.ruler/ (Node.js library overlay)

Weekly Installs
18
Repository
adonis0123/adonis-skills
GitHub Stars
1
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass