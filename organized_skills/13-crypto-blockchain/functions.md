---
rating: ⭐⭐⭐
title: functions
url: https://skills.sh/browserbase/skills/functions
---

# functions

skills/browserbase/skills/functions
functions
Installation
$ npx skills add https://github.com/browserbase/skills --skill functions
SKILL.md
Browserbase Functions

Deploy serverless browser automation using the official bb CLI.

Prerequisites

Get API key and Project ID from: https://browserbase.com/settings

export BROWSERBASE_API_KEY="your_api_key"
export BROWSERBASE_PROJECT_ID="your_project_id"

Creating a Function Project
1. Initialize
pnpm dlx @browserbasehq/sdk-functions init my-function
cd my-function


This creates:

my-function/
├── package.json
├── index.ts        # Your function code
└── .env            # Add credentials here

2. Add Credentials to .env
echo "BROWSERBASE_API_KEY=$BROWSERBASE_API_KEY" >> .env
echo "BROWSERBASE_PROJECT_ID=$BROWSERBASE_PROJECT_ID" >> .env

3. Install Dependencies
pnpm install

Function Structure
import { defineFn } from "@browserbasehq/sdk-functions";
import { chromium } from "playwright-core";

defineFn("my-function", async (context) => {
  const { session, params } = context;

  // Connect to browser
  const browser = await chromium.connectOverCDP(session.connectUrl);
  const page = browser.contexts()[0]!.pages()[0]!;

  // Your automation
  await page.goto(params.url || "https://example.com");
  const title = await page.title();

  // Return JSON-serializable result
  return { success: true, title };
});


Key objects:

context.session.connectUrl - CDP endpoint to connect Playwright
context.params - Input parameters from invocation
Development Workflow
1. Start Dev Server
pnpm bb dev index.ts


Server runs at http://127.0.0.1:14113

2. Test Locally
curl -X POST http://127.0.0.1:14113/v1/functions/my-function/invoke \
  -H "Content-Type: application/json" \
  -d '{"params": {"url": "https://news.ycombinator.com"}}'

3. Iterate

The dev server auto-reloads on file changes. Use console.log() for debugging - output appears in the terminal.

Deploying
pnpm bb publish index.ts


Output:

Function published successfully
Build ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Function ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx


Save the Function ID - you need it to invoke.

Quick Reference
Command	Description
pnpm dlx @browserbasehq/sdk-functions init <name>	Create new project
pnpm bb dev <file>	Start local dev server
pnpm bb publish <file>	Deploy to Browserbase

For invocation examples, common patterns, and troubleshooting, see REFERENCE.md.

Weekly Installs
803
Repository
browserbase/skills
GitHub Stars
1.5K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn