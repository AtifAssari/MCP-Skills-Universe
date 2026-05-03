---
title: openrouter
url: https://skills.sh/aibtcdev/skills/openrouter
---

# openrouter

skills/aibtcdev/skills/openrouter
openrouter
Installation
$ npx skills add https://github.com/aibtcdev/skills --skill openrouter
SKILL.md
OpenRouter Skill

Provides AI integration capabilities via OpenRouter — a unified API for 100+ LLMs.

Model Discovery — List available OpenRouter models with capabilities, context windows, and pricing.
Integration Guide — Get code examples and patterns for integrating OpenRouter in different environments (Node.js, Cloudflare Workers, browser).
Chat — Send a prompt to any OpenRouter model and return the response. Requires OPENROUTER_API_KEY env var.
Usage
bun run openrouter/openrouter.ts <subcommand> [options]

Subcommands
models

List available OpenRouter models with capabilities and pricing.

bun run openrouter/openrouter.ts models [--filter <term>]


Options:

--filter (optional) — Filter models by name (case-insensitive substring match)
guide

Print integration code examples for a target environment.

bun run openrouter/openrouter.ts guide [--env <environment>] [--feature <feature>]


Options:

--env — Target environment: nodejs | cloudflare-worker | browser | all (default: all)
--feature — Feature to show: chat | completion | streaming | function-calling | all (default: all)
chat

Send a prompt to an OpenRouter model. Requires OPENROUTER_API_KEY environment variable.

bun run openrouter/openrouter.ts chat --prompt "Hello" [--model <model-id>] [--max-tokens <n>]


Options:

--prompt (required) — The prompt to send
--model (optional) — Model ID (default: openai/gpt-4o-mini)
--max-tokens (optional) — Max tokens in response (default: 1024)
Notes
models and guide work without an API key.
chat requires OPENROUTER_API_KEY environment variable (get from https://openrouter.ai/keys).
OpenRouter API base: https://openrouter.ai/api/v1
Weekly Installs
103
Repository
aibtcdev/skills
GitHub Stars
5
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn