---
title: playwright-mcp-dev
url: https://skills.sh/microsoft/playwright/playwright-mcp-dev
---

# playwright-mcp-dev

skills/microsoft/playwright/playwright-mcp-dev
playwright-mcp-dev
Installation
$ npx skills add https://github.com/microsoft/playwright --skill playwright-mcp-dev
Summary

Developer guide for extending Playwright MCP tools and CLI commands.

Add new MCP tools in packages/playwright/src/mcp/browser/tools/, register in tools.ts, and define capabilities in config.d.ts
CLI commands map to MCP tools; register new commands in packages/playwright/src/mcp/terminal/commands.ts and update help generator if adding a category
Config options require updates across program.ts (CLI option), config.d.ts (definition), and config.ts (implementation and environment mapping)
Run npm run ctest-mcp <category> for testing and npm run flint before commit; always keep watch mode running and use lint to catch type errors
SKILL.md
MCP
Adding MCP Tools
Create a new tool in packages/playwright/src/mcp/browser/tools/your-tool.ts
Register the tool in packages/playwright/src/mcp/browser/tools.ts
Add ToolCapability in packages/playwright/src/mcp/config.d.ts
Place new tests in tests/mcp/mcp-<category>.spec.ts
Building
Assume watch is running at all times, run lint to see type errors
Testing
Run tests as npm run ctest-mcp <category>
Do not run test --debug
CLI
Adding commands
CLI commands are based on MCP tools. Implement the corresponding MCP tool as per Adding MCP Tools section above, if needed.
Add new CLI category for tool if needed:
Add Category in packages/playwright/src/mcp/terminal/command.ts
Update doc generator packages/playwright/src/mcp/terminal/helpGenerator.ts
Register command in packages/playwright/src/mcp/terminal/commands.ts
Update skill file at packages/playwright/src/skill/SKILL.md and references if necessary in packages/playwright/src/skill/references/
Place new tests in tests/mcp/cli-<category>.spec.ts
Adding CLI options or Config options

When you need to add something to config.

packages/playwright/src/mcp/program.ts
add CLI option and doc
packages/playwright/src/mcp/config.d.ts
add and document the option
packages/playwright/src/mcp/config.ts
modify FullConfig if needed
and CLIOptions if needed
add it to configFromEnv
Building
Assume watch is running at all times, run lint to see type errors
Testing
Run tests as npm run ctest-mcp cli-<category>
Do not run test --debug
Lint
run npm run flint to lint everything before commit
SKILL File

The skill file is located at packages/playwright/src/skill/SKILL.md. It contains documentation for all available CLI commands and MCP tools. Update it whenever you add new commands or tools. At any point in time you can run "npm run playwright-cli -- --help" to see the latest available commands and use them to update the skill file.

Weekly Installs
319
Repository
microsoft/playwright
GitHub Stars
87.8K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass