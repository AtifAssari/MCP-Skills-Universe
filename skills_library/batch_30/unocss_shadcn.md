---
title: unocss-shadcn
url: https://skills.sh/jsonlee12138/prompts/unocss-shadcn
---

# unocss-shadcn

skills/jsonlee12138/prompts/unocss-shadcn
unocss-shadcn
Installation
$ npx skills add https://github.com/jsonlee12138/prompts --skill unocss-shadcn
SKILL.md
unocss-shadcn
Overview

Apply a deterministic setup flow for UnoCSS and unocss-preset-shadcn without running automatic installers. Detect monorepo strictly, route component targets by project shape, and enforce shadcn MCP plus manual-mode component creation.

Core Rules
Run in semi-automatic mode only: propose commands and file edits, but do not auto-install dependencies.
Detect monorepo only when one of these is true:
pnpm-workspace.yaml exists at repo root.
Root package.json contains workspaces.
Use destination policy:
Monorepo: packages/shadcn-ui
Single project: src/components
UnoCSS config location policy:
Monorepo: configure in each apps/<app>/uno.config.* (NOT at repo root or in packages).
Single project: configure at project root uno.config.*.
Default to presetWind4 unless the user explicitly requests a different version (e.g. presetWind3).
For monorepo component package dependencies, write shadcn-related runtime items to peerDependencies.
Use shadcn MCP before any component usage or creation.
Create shadcn components in manual mode only (do not use Tailwind-oriented auto init flow).
If shadcn MCP is unavailable, block the component step and return an explicit error.
Workflow
Inspect project files:
package.json
pnpm-workspace.yaml
uno.config.* or unocss.config.*
components.json if present
Decide branch using strict monorepo detection.
Update UnoCSS config to include unocss-preset-shadcn in presets.
Generate destination-specific instructions from references:
Monorepo path: references/monorepo.md
Single-project path: references/single-project.md
Enforce shadcn MCP chain and manual creation mode.
Verify with references/checklist.md before claiming completion.
Required MCP Chain (shadcn)

Run these in order before component operations:

get_project_registries
search_items_in_registries or list_items_in_registries
get_item_examples_from_registries
Optional reference only: get_add_command_for_items

Use MCP outputs as the source of truth for component API, file content, and dependency hints.

References
references/monorepo.md: monorepo branch instructions and templates
references/single-project.md: single-project branch instructions and templates
references/checklist.md: validation checklist and remediation matrix
Weekly Installs
9
Repository
jsonlee12138/prompts
GitHub Stars
1
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn