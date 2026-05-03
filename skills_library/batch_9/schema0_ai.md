---
title: schema0-ai
url: https://skills.sh/schema0/skills/schema0-ai
---

# schema0-ai

skills/schema0/skills/schema0-ai
schema0-ai
Installation
$ npx skills add https://github.com/schema0/skills --skill schema0-ai
SKILL.md
AI Integration

AI SDK integration with ORPC for chat, prompt-response, and tool-calling features.

Generator Commands
# Full-stack chat with streaming
schema0 sandbox exec "bun run .claude/skills/ai-integration/scripts/generate.ts chat <name>"

# Simple prompt-response (no streaming)
schema0 sandbox exec "bun run .claude/skills/ai-integration/scripts/generate.ts simple <name>"

# Backend router only
schema0 sandbox exec "bun run .claude/skills/ai-integration/scripts/generate.ts router <name>"

# Tool definition for function calling
schema0 sandbox exec "bun run .claude/skills/ai-integration/scripts/generate.ts tool <name>"

Prerequisites
Add API key using manage-secrets skill to securely add it and update packages/auth/env.ts
Install dependencies:
schema0 sandbox exec "bun add ai @ai-sdk/openai @ai-sdk/anthropic @ai-sdk/google @orpc/ai-sdk @orpc/client"

Add key to env schema in packages/auth/env.ts (e.g., OPENAI_API_KEY: z.string().optional())
Generated Files
Template	Output Location	Purpose
ai-router.hbs	packages/api/src/routers/[name].ts	ORPC router with AI SDK streaming
ai-chat-route.hbs	apps/web/src/routes/_auth.[name].tsx	Full chat UI with streaming
ai-simple.hbs	apps/web/src/routes/_auth.[name].tsx	Simple prompt-response UI
ai-tool.hbs	packages/api/src/tools/[name].ts	Tool definitions for function calling
Post-Generation Steps
Register router in packages/api/src/routers/index.ts
Add route to sidebar in apps/web/src/components/app-sidebar.tsx
Set the API key environment variable during build/deploy
References
references/patterns.md -- Chat mode, simple mode, tool calling, provider examples (OpenAI, Anthropic, Google), streaming, naming conventions
Weekly Installs
17
Repository
schema0/skills
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass