---
title: groq-local-dev-loop
url: https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/groq-local-dev-loop
---

# groq-local-dev-loop

skills/jeremylongshore/claude-code-plugins-plus-skills/groq-local-dev-loop
groq-local-dev-loop
Installation
$ npx skills add https://github.com/jeremylongshore/claude-code-plugins-plus-skills --skill groq-local-dev-loop
SKILL.md
Groq Local Dev Loop
Overview

Set up a fast, reproducible local development workflow for Groq.

Prerequisites
Completed groq-install-auth setup
Node.js 18+ with npm/pnpm
Code editor with TypeScript support
Git for version control
Instructions
Step 1: Create Project Structure
my-groq-project/
├── src/
│   ├── groq/
│   │   ├── client.ts       # Groq client wrapper
│   │   ├── config.ts       # Configuration management
│   │   └── utils.ts        # Helper functions
│   └── index.ts
├── tests/
│   └── groq.test.ts
├── .env.local              # Local secrets (git-ignored)
├── .env.example            # Template for team
└── package.json

Step 2: Configure Environment
set -euo pipefail
# Copy environment template
cp .env.example .env.local

# Install dependencies
npm install

# Start development server
npm run dev

Step 3: Setup Hot Reload
{
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "test": "vitest",
    "test:watch": "vitest --watch"
  }
}

Step 4: Configure Testing
import { describe, it, expect, vi } from 'vitest';
import { GroqClient } from '../src/groq/client';

describe('Groq Client', () => {
  it('should initialize with API key', () => {
    const client = new GroqClient({ apiKey: 'test-key' });
    expect(client).toBeDefined();
  });
});

Output
Working development environment with hot reload
Configured test suite with mocking
Environment variable management
Fast iteration cycle for Groq development
Error Handling
Error	Cause	Solution
Module not found	Missing dependency	Run npm install
Port in use	Another process	Kill process or change port
Env not loaded	Missing .env.local	Copy from .env.example
Test timeout	Slow network	Increase test timeout
Examples
Mock Groq Responses
vi.mock('@groq/sdk', () => ({
  GroqClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));

Debug Mode
set -euo pipefail
# Enable verbose logging
DEBUG=GROQ=* npm run dev

Resources
Groq SDK Reference
Vitest Documentation
tsx Documentation
Next Steps

See groq-sdk-patterns for production-ready code patterns.

Weekly Installs
26
Repository
jeremylongshore…s-skills
GitHub Stars
2.1K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass