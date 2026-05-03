---
title: playwright-dev
url: https://skills.sh/microsoft/playwright/playwright-dev
---

# playwright-dev

skills/microsoft/playwright/playwright-dev
playwright-dev
Installation
$ npx skills add https://github.com/microsoft/playwright --skill playwright-dev
Summary

Guide for extending Playwright with new APIs, MCP tools, CLI commands, and vendored dependencies.

Covers monorepo structure, build/test/lint workflows, and coding conventions via CLAUDE.md reference
Includes detailed walkthroughs for implementing client/server APIs, writing tests, and modifying protocol layers
Explains how to add MCP tools, CLI commands, and configuration options within the Playwright ecosystem
Documents the vendoring process for bundling third-party npm packages into playwright-core or playwright
SKILL.md
Playwright Development Guide

See CLAUDE.md for monorepo structure, build/test/lint commands, and coding conventions.

Detailed Guides
Library Architecture — client/server/dispatcher structure, protocol layer, DEPS rules
Adding and Modifying APIs — define API docs, implement client/server, add tests
MCP Tools and CLI Commands — add MCP tools, CLI commands, config options
Vendor Dependencies & Bundling — utilsBundle, coreBundle, babelBundle; adding vendored npm packages; DEPS.list; check_deps
Updating WebKit Safari Version — update the Safari version string in the WebKit user-agent
Bisecting Across Published Versions — reproduce regressions side-by-side from npm and diff node_modules/playwright/lib/ between versions
Dashboard - the UI powering the "playwright cli show" command, and how to work on it
Weekly Installs
1.4K
Repository
microsoft/playwright
GitHub Stars
87.8K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn