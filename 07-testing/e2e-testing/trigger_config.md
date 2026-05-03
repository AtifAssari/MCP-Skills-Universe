---
rating: ⭐⭐
title: trigger-config
url: https://skills.sh/triggerdotdev/skills/trigger-config
---

# trigger-config

skills/triggerdotdev/skills/trigger-config
trigger-config
Installation
$ npx skills add https://github.com/triggerdotdev/skills --skill trigger-config
Summary

Configure Trigger.dev projects with build extensions for databases, browsers, media processing, and Python.

Supports seven core build extensions: Prisma, Playwright, Puppeteer, FFmpeg, Python, apt-get system packages, and additional files
Includes environment variable syncing, global lifecycle hooks (onStartAttempt, onSuccess, onFailure), and machine configuration for deployment
Extensions apply only to production builds; local development uses your native environment
Common patterns provided for full-stack web apps, AI/ML processing, and web scraping workflows
SKILL.md
Trigger.dev Configuration

Configure your Trigger.dev project with trigger.config.ts and build extensions.

When to Use
Setting up a new Trigger.dev project
Adding database support (Prisma, TypeORM)
Configuring browser automation (Playwright, Puppeteer)
Adding media processing (FFmpeg)
Running Python scripts from tasks
Syncing environment variables
Installing system packages
Basic Configuration
// trigger.config.ts
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "<project-ref>",
  dirs: ["./trigger"],
  runtime: "node", // "node", "node-22", or "bun"
  logLevel: "info",

  retries: {
    enabledInDev: false,
    default: {
      maxAttempts: 3,
      minTimeoutInMs: 1000,
      maxTimeoutInMs: 10000,
      factor: 2,
    },
  },

  build: {
    extensions: [], // Add extensions here
  },
});

Common Build Extensions
Prisma
import { prismaExtension } from "@trigger.dev/build/extensions/prisma";

export default defineConfig({
  // ...
  build: {
    extensions: [
      prismaExtension({
        schema: "prisma/schema.prisma",
        migrate: true,
        directUrlEnvVarName: "DIRECT_DATABASE_URL",
      }),
    ],
  },
});

Playwright (Browser Automation)
import { playwright } from "@trigger.dev/build/extensions/playwright";

extensions: [
  playwright({
    browsers: ["chromium"], // or ["chromium", "firefox", "webkit"]
  }),
]

Puppeteer
import { puppeteer } from "@trigger.dev/build/extensions/puppeteer";

extensions: [puppeteer()]

// Set env var: PUPPETEER_EXECUTABLE_PATH="/usr/bin/google-chrome-stable"

FFmpeg (Media Processing)
import { ffmpeg } from "@trigger.dev/build/extensions/core";

extensions: [
  ffmpeg({ version: "7" }),
]
// Automatically sets FFMPEG_PATH and FFPROBE_PATH

Python
import { pythonExtension } from "@trigger.dev/build/extensions/python";

extensions: [
  pythonExtension({
    scripts: ["./python/**/*.py"],
    requirementsFile: "./requirements.txt",
    devPythonBinaryPath: ".venv/bin/python",
  }),
]

// Usage in tasks:
const result = await python.runScript("./python/process.py", ["arg1"]);

System Packages (apt-get)
import { aptGet } from "@trigger.dev/build/extensions/core";

extensions: [
  aptGet({
    packages: ["imagemagick", "curl"],
  }),
]

Additional Files
import { additionalFiles } from "@trigger.dev/build/extensions/core";

extensions: [
  additionalFiles({
    files: ["./assets/**", "./templates/**"],
  }),
]

Environment Variable Sync
import { syncEnvVars } from "@trigger.dev/build/extensions/core";

extensions: [
  syncEnvVars(async (ctx) => {
    return [
      { name: "API_KEY", value: await getSecret(ctx.environment) },
      { name: "ENV", value: ctx.environment },
    ];
  }),
]

Common Extension Combinations
Full-Stack Web App
extensions: [
  prismaExtension({ schema: "prisma/schema.prisma", migrate: true }),
  additionalFiles({ files: ["./assets/**"] }),
  syncEnvVars(async (ctx) => [...envVars]),
]

AI/ML Processing
extensions: [
  pythonExtension({
    scripts: ["./ai/**/*.py"],
    requirementsFile: "./requirements.txt",
  }),
  ffmpeg({ version: "7" }),
]

Web Scraping
extensions: [
  playwright({ browsers: ["chromium"] }),
  additionalFiles({ files: ["./selectors.json"] }),
]

Global Lifecycle Hooks
export default defineConfig({
  // ...
  onStartAttempt: async ({ payload, ctx }) => {
    console.log("Task starting:", ctx.task.id);
  },
  onSuccess: async ({ payload, output, ctx }) => {
    console.log("Task succeeded");
  },
  onFailure: async ({ payload, error, ctx }) => {
    console.error("Task failed:", error);
  },
});

Machine Defaults
export default defineConfig({
  // ...
  defaultMachine: "medium-1x",
  maxDuration: 300, // seconds
});

Telemetry Integration
import { PrismaInstrumentation } from "@prisma/instrumentation";

export default defineConfig({
  // ...
  telemetry: {
    instrumentations: [new PrismaInstrumentation()],
  },
});

Best Practices
Pin versions for reproducible builds
Use syncEnvVars for dynamic secrets
Add native modules to build.external array
Debug with --log-level debug --dry-run

Extensions only affect deployment, not local development.

See references/config.md for complete documentation.

Weekly Installs
1.3K
Repository
triggerdotdev/skills
GitHub Stars
25
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass