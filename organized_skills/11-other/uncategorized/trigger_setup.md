---
rating: ⭐⭐⭐
title: trigger-setup
url: https://skills.sh/triggerdotdev/skills/trigger-setup
---

# trigger-setup

skills/triggerdotdev/skills/trigger-setup
trigger-setup
Installation
$ npx skills add https://github.com/triggerdotdev/skills --skill trigger-setup
Summary

Initialize Trigger.dev in your project with configuration and first task setup.

Scaffolds trigger.config.ts, trigger/ directory, and example task via npx trigger init
Requires Node.js 18+, Bun, and a Trigger.dev account with project credentials from the dashboard
Development server runs locally with npx trigger dev; tasks are triggered from app code or the dashboard test interface
Common setup issues covered: task export requirements, project ID verification, and secret key configuration
SKILL.md
Trigger.dev Setup

Get Trigger.dev running in your project in minutes.

When to Use
Adding Trigger.dev to an existing project
Creating your first task
Setting up trigger.config.ts
Connecting to Trigger.dev cloud
Prerequisites
Node.js 18+ or Bun
A Trigger.dev account (https://cloud.trigger.dev)
Quick Start
1. Install the SDK
npm install @trigger.dev/sdk

2. Initialize Your Project
npx trigger init


This creates:

trigger.config.ts - project configuration
trigger/ directory - where your tasks live
trigger/example.ts - a sample task
3. Configure trigger.config.ts
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "proj_xxxxx", // From dashboard
  dirs: ["./trigger"],
});

4. Create Your First Task
// trigger/my-task.ts
import { task } from "@trigger.dev/sdk";

export const myFirstTask = task({
  id: "my-first-task",
  run: async (payload: { name: string }) => {
    console.log(`Hello, ${payload.name}!`);
    return { message: `Processed ${payload.name}` };
  },
});

5. Start Development Server
npx trigger dev

6. Trigger Your Task

From your app code:

import { tasks } from "@trigger.dev/sdk";
import type { myFirstTask } from "./trigger/my-task";

await tasks.trigger<typeof myFirstTask>("my-first-task", {
  name: "World",
});


Or from the Trigger.dev dashboard "Test" tab.

Project Structure
your-project/
├── trigger.config.ts    # Required - project config
├── trigger/             # Required - task files
│   ├── my-task.ts
│   └── another-task.ts
├── package.json
└── ...

Environment Variables

Create .env or set in your environment:

TRIGGER_SECRET_KEY=tr_dev_xxxxx  # From dashboard > API Keys

Common Issues
"No tasks found"
Ensure tasks are exported from files in dirs folders
Check trigger.config.ts points to correct directories
"Project not found"
Verify project in config matches dashboard
Check TRIGGER_SECRET_KEY is set
"Task not registered"
Restart npx trigger dev after adding new tasks
Tasks must use task() or schemaTask() from @trigger.dev/sdk
Next Steps
Add retry logic → see trigger-tasks skill
Configure build extensions → see trigger-config skill
Build AI workflows → see trigger-agents skill
Add real-time UI → see trigger-realtime skill
Weekly Installs
1.2K
Repository
triggerdotdev/skills
GitHub Stars
25
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass