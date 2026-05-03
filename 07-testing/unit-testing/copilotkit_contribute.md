---
title: copilotkit-contribute
url: https://skills.sh/copilotkit/skills/copilotkit-contribute
---

# copilotkit-contribute

skills/copilotkit/skills/copilotkit-contribute
copilotkit-contribute
Installation
$ npx skills add https://github.com/copilotkit/skills --skill copilotkit-contribute
SKILL.md
Contributing to CopilotKit

Important: CopilotKit's internal v2 packages use the @copilotkit/* namespace. The public API that users install is @copilotkit/*. When contributing, you work with @copilotkit/* source but users never see that namespace.

Live Documentation (MCP)

This plugin includes an MCP server (copilotkit-docs) that provides search-docs and search-code tools for querying live CopilotKit documentation and source code.

Claude Code: Auto-configured by the plugin's .mcp.json -- no setup needed.
Codex: Requires manual configuration. See the copilotkit-debug skill for setup instructions.
Workflow
Fork and clone the CopilotKit/CopilotKit repository.
Install dependencies with pnpm install (requires pnpm v9.x and Node 20+).
Build once with pnpm build to bootstrap all packages.
Create a branch using the naming convention: feat/<ISSUE>-<name>, fix/<ISSUE>-<name>, or docs/<ISSUE>-<name>.
Develop with pnpm dev (watches all packages) or target a specific package with nx run @copilotkit/<pkg>:dev.
Write and run tests with nx run @copilotkit/<pkg>:test. All v2 packages use Vitest.
Lint and format with pnpm run lint --fix && pnpm run format.
Commit using conventional commit format: <type>(<scope>): <subject> (enforced by commitlint).
Push and open a PR against the main branch. CI builds all packages and publishes preview packages via pkg-pr-new.
Before Opening a PR
Reach out to the maintainers first for any significant work (file an issue or ask on Discord).
Run pnpm run test to verify all tests pass.
Run pnpm run build to verify the full build succeeds.
Run pnpm run check-prettier to verify formatting.
Ensure commit messages follow the <type>(<scope>): <subject> format.
Quick Reference
Task	Command
Install dependencies	pnpm install
Build all packages	pnpm build
Dev mode (all)	pnpm dev
Dev mode (v2 only)	pnpm dev:next
Run all tests	pnpm run test
Run v2 tests only	pnpm test:next
Run single package tests	nx run @copilotkit/core:test
Test with coverage	pnpm run test:coverage
Lint	pnpm run lint
Format	pnpm run format
Check formatting	pnpm run check-prettier
Type check	pnpm run check-types
Package quality checks	pnpm run check:packages
Dependency graph	pnpm run graph
Key Architecture Points
V2 (@copilotkit/*) is the real implementation. V1 (@copilotkit/*) wraps V2.
New features always go in V2 packages under packages/v2/.
Communication between frontend and runtime uses the AG-UI protocol (SSE-based events).
The monorepo uses Nx for task orchestration and pnpm workspaces.
Reference Documents
Contribution Guide — full onboarding walkthrough
Repo Structure — package layout and architecture
Testing Guide — Vitest setup, running tests, coverage
PR Guidelines — CI checks, review process, expectations
Weekly Installs
152
Repository
copilotkit/skills
GitHub Stars
22
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass