---
title: e2e-frontend-validation
url: https://skills.sh/mastra-ai/mastra/e2e-frontend-validation
---

# e2e-frontend-validation

skills/mastra-ai/mastra/e2e-frontend-validation
e2e-frontend-validation
Installation
$ npx skills add https://github.com/mastra-ai/mastra --skill e2e-frontend-validation
SKILL.md
E2E Validation for Frontend Modifications
Prerequisites

Requires Playwright MCP server. If the browser_navigate tool is unavailable, instruct the user to add it:

claude mcp add playwright -- npx @playwright/mcp@latest

Validation Steps

After completing frontend changes:

Build the CLI
pnpm build:cli

Start the dev server
cd packages/playground/e2e/kitchen-sink && pnpm dev


Verify server is running

URL: http://localhost:4111
Wait for the server to be ready before proceeding

Identify impacted routes

Routes are defined in packages/playground/src/App.tsx
Browse them ALL to verify behavior

Test with Playwright MCP

Use browser_navigate to visit each impacted route
Visually verify the changes render correctly
Test any interactive elements modified
Use browser_screenshot to capture results for the user

Write E2E Tests

Write Playwright tests covering the validated behavior. Follow the conventions below.

File Placement

Map validated routes to test file paths under packages/playground/e2e/tests/:

Route pattern	Test file
/agents	agents/page.spec.ts
/agents/:id/...	agents/$agentId/page.spec.ts
/agents/:id/chat/:chatId	agents/$agentId/stream.spec.ts (if streaming)
/tools	tools/page.spec.ts
/tools/:id	tools/$toolId/page.spec.ts
/workflows	workflows/page.spec.ts
/workflows/:id	workflows/$workflowId/page.spec.ts
/mcps	mcps/page.spec.ts
/mcps/:id/tools/:toolId	mcps/$serverId/tools/$toolId/page.spec.ts
Layout/navigation tests → page.spec.ts
Streaming/chat tests → stream.spec.ts
New File vs Extend Existing
If the spec file already exists, add new test() blocks to it.
If it doesn't exist, create a new file with the full boilerplate (imports, afterEach hook, etc.).
Fixture Decision Tree
AI streaming responses (text-delta, tool calls, workflow execution) → use selectFixture() + nanoid() for deterministic, isolated tests
Static UI, navigation, forms, deterministic tool execution → no fixture needed
Test Conventions
// Imports
import { test, expect } from '@playwright/test';
import { resetStorage } from '../__utils__/reset-storage';
// Only for streaming tests:
import { selectFixture } from '../__utils__/select-fixture';
import { nanoid } from 'nanoid';

Always call resetStorage() in test.afterEach
For streaming tests, create a fresh browser context in test.beforeEach:
let page: Page;
test.beforeEach(async ({ browser }) => {
  const context = await browser.newContext();
  page = await context.newPage();
});

Locator priority: getByTestId > getByRole > getByLabel > locator('text=...')
Use { timeout: 20000 } for async/streaming content assertions
Use nanoid() for unique chat session IDs in URLs
Verify memory persistence with page.reload() where applicable
Use toMatchAriaSnapshot() for stable layout assertions
Kitchen-Sink Extension

When the feature under test requires new fixtures or entities:

New fixtures: Add to e2e/kitchen-sink/fixtures/, create a <name>.fixture.ts file, and register it in fixtures/index.ts
Update types: Add the fixture name to the Fixtures union in e2e/kitchen-sink/types.ts and e2e/tests/__utils__/select-fixture.ts
New tools/agents/workflows: Add to the corresponding files in e2e/kitchen-sink/src/mastra/

Verify Tests Pass

cd packages/playground && pnpm test:e2e


If tests fail, fix them and re-run until green.

Quick Reference
Step	Command/Action
Build	pnpm build:cli
Start	cd packages/playground/e2e/kitchen-sink && pnpm dev
App URL	http://localhost:4111
Routes	@packages/playground/src/App.tsx
Run tests	cd packages/playground && pnpm test:e2e
Test dir	packages/playground/e2e/tests/
Fixtures	packages/playground/e2e/kitchen-sink/fixtures/
Kitchen-sink	packages/playground/e2e/kitchen-sink/src/mastra/
Weekly Installs
21
Repository
mastra-ai/mastra
GitHub Stars
23.5K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass