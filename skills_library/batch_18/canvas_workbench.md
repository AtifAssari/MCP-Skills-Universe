---
title: canvas-workbench
url: https://skills.sh/drupal-canvas/skills/canvas-workbench
---

# canvas-workbench

skills/drupal-canvas/skills/canvas-workbench
canvas-workbench
Installation
$ npx skills add https://github.com/drupal-canvas/skills --skill canvas-workbench
SKILL.md
Installation gate

Before trying to use Workbench, detect the project's package manager and use its executable runner for @drupal-canvas/workbench.

Preferred commands:

npm: npx @drupal-canvas/workbench
pnpm: pnpm dlx @drupal-canvas/workbench
bun: bunx @drupal-canvas/workbench
yarn: yarn dlx @drupal-canvas/workbench

Choose the command that matches the repository's package manager. Use lockfiles and existing project conventions to decide.

If the package runner or @drupal-canvas/workbench is not available, stop and tell the user that Canvas Workbench is not available in the current environment. Ask whether they want you to install it. If they say yes, install @drupal-canvas/workbench as a dev dependency with the matching package manager:

npm: npm install --save-dev @drupal-canvas/workbench
pnpm: pnpm add --save-dev @drupal-canvas/workbench
bun: bun add --dev @drupal-canvas/workbench
yarn: yarn add --dev @drupal-canvas/workbench

After installation completes, use the matching runner command and continue with Workbench verification. If the user says no, stop and do not guess alternate startup commands.

Configuration gate

Workbench does not require a canvas.config.json file when the project uses the default Canvas layout.

Before starting Workbench, check whether the project appears to use the default paths:

componentDir: project root
pagesDir: ./pages
aliasBaseDir: src
globalCssPath: ./src/components/global.css

If the project uses those defaults and canvas.config.json is missing, proceed without creating one.

If the project uses different component paths, pages paths, @/ import resolution, or global CSS entrypoints, add or update canvas.config.json in the project root before starting Workbench. Set only the options the project needs.

Example:

{
  "componentDir": "./src/components",
  "pagesDir": "./pages",
  "aliasBaseDir": "src",
  "globalCssPath": "./src/global.css"
}

Start Workbench

When Workbench verification is needed and the package-runner command is available:

Run the matching Workbench command from the project root.
Treat it as a long-running local dev server process.
Read the startup output and use the local URL it prints.
Leave the server running while you verify the result.

If a Workbench server is already running for the current project, reuse it instead of starting a second instance.

Verification workflow

Workbench is the runtime surface for local preview verification. When verification is iterative, reuse the same Workbench server and preview route across fix/review loops.

Use Workbench as part of the normal implementation loop:

Start or reuse Workbench.
Open the relevant component preview state or page preview.
Verify that the requested change renders correctly.
If the result is wrong, update the implementation and verify again.
Finish only after Workbench verification passes, or explain clearly what blocked verification.
Scope

This skill is for starting and using Workbench and for coordinating page/mock authoring. It is not the source of truth for the Canvas component contract.

Use canvas-component-definition when creating or validating the component structure, component.yml, naming, or mock coverage expectations.
Use canvas-page-definition when creating or validating page JSON files, page structure, or page schema requirements.
Use canvas-component-definition/references/component-mocks.md when you need to author or validate mocks.json.
Use references/components.md when you need the Workbench-specific component review flow and where component preview files live.
Use references/pages.md when you need the Workbench-specific page preview flow and configured page location.
Weekly Installs
37
Repository
drupal-canvas/skills
GitHub Stars
1
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn