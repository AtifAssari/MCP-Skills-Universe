---
title: mastra
url: https://skills.sh/mastra-ai/skills/mastra
---

# mastra

skills/mastra-ai/skills/mastra
mastra
Installation
$ npx skills add https://github.com/mastra-ai/skills --skill mastra
Summary

Reference guide for building agents and workflows with current Mastra APIs.

Always verify against embedded docs in node_modules/@mastra/*/dist/docs/ (installed version) or remote docs at https://mastra.ai/llms.txt before writing code; training data is outdated
Core building blocks: Agents (autonomous, decision-making), Workflows (structured sequences), Tools (extend capabilities), Memory (maintain context), and RAG (external knowledge)
Requires ES2022 modules in TypeScript config and model format of "provider/model-name" (e.g., "openai/gpt-5.4")
Includes embedded references for setup, common errors, migrations, and API lookup strategies to match your exact installed version
SKILL.md
Mastra Framework Guide

Build AI applications with Mastra. This skill teaches you how to find current documentation and build agents and workflows.

⚠️ Critical: Do not trust internal knowledge

Everything you know about Mastra is likely outdated or wrong. Never rely on memory. Always verify against current documentation.

Your training data contains obsolete APIs, deprecated patterns, and incorrect usage. Mastra evolves rapidly - APIs change between versions, constructor signatures shift, and patterns get refactored.

Prerequisites

Before writing any Mastra code, check if packages are installed:

ls node_modules/@mastra/

If packages exist: Use embedded docs first (most reliable)
If no packages: Install first or use remote docs
Available files
References
User Question	First Check	How To
"Create/install Mastra project"	references/create-mastra.md	Setup guide with CLI and manual steps
"How do I use Agent/Workflow/Tool?"	references/embedded-docs.md	Look up in node_modules/@mastra/*/dist/docs/
"How do I use X?" (no packages)	references/remote-docs.md	Fetch from https://mastra.ai/llms.txt
"I'm getting an error..."	references/common-errors.md	Common errors and solutions
"Upgrade from v0.x to v1.x"	references/migration-guide.md	Version upgrade workflows
Scripts
scripts/provider-registry.mjs: Look up current providers and models available in the model router. Always run this before using a model to verify provider keys and model names.
Priority order for writing code

⚠️ Never write code without checking current docs first.

Embedded docs first (if packages installed)

Look up current docs in node_modules for a package. Example of looking up "Agent" docs in @mastra/core:

grep -r "Agent" node_modules/@mastra/core/dist/docs/references

Why: Matches your EXACT installed version
Most reliable source of truth
More information: references/embedded-docs.md

Source code second (if packages installed)

If you can't find what you need in the embedded docs, look directly at the source code. This is more time consuming but can provide insights into implementation details.

# Check what's available
cat node_modules/@mastra/core/dist/docs/assets/SOURCE_MAP.json | grep '"Agent"'

# Read the actual type definition
cat node_modules/@mastra/core/dist/[path-from-source-map]

Why: Ultimate source of truth if docs are missing or unclear
Use when: Embedded docs don't cover your question
More information: references/embedded-docs.md

Remote docs third (if packages not installed)

You can fetch the latest docs from the Mastra website:

https://mastra.ai/llms.txt

Why: Latest published docs (may be ahead of installed version)
Use when: Packages not installed or exploring new features
More information: references/remote-docs.md
Core concepts
Agents vs workflows

Agent: Autonomous, makes decisions, uses tools Use for: Open-ended tasks (support, research, analysis)

Workflow: Structured sequence of steps Use for: Defined processes (pipelines, approvals, ETL)

Key components
Tools: Extend agent capabilities (APIs, databases, external services)
Memory: Maintain context (message history, working memory, semantic recall, observational memory)
RAG: Query external knowledge (vector stores, graph relationships)
Storage: Persist data (Postgres, LibSQL, MongoDB)
Mastra Studio

Studio provides an interactive UI for building, testing, and managing agents, workflows, and tools. It helps with debugging and improving your applications iteratively.

Inside a Mastra project, run:

npm run dev


Then open http://localhost:4111 in your browser to access Mastra Studio.

Critical requirements
TypeScript config

Mastra requires ES2022 modules. CommonJS will fail.

{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ES2022",
    "moduleResolution": "bundler"
  }
}

Model format

Always use "provider/model-name" when defining models using Mastra's model router.

Use the provider registry script to look up available providers and models:

# List all available providers
node scripts/provider-registry.mjs --list

# List all models for a specific provider (sorted newest first)
node scripts/provider-registry.mjs --provider openai
node scripts/provider-registry.mjs --provider anthropic


When the user asks to use a model or provider, always run the script first to verify the provider key and model name are valid. Do not guess model names from memory as they change frequently.

Example model strings:

"openai/gpt-5.4"
"anthropic/claude-sonnet-4-5"
"google/gemini-2.5-pro"
When you see errors

Type errors often mean your knowledge is outdated.

Common signs of outdated knowledge:

Property X does not exist on type Y
Cannot find module
Type mismatch errors
Constructor parameter errors

What to do:

Check references/common-errors.md
Verify current API in embedded docs
Don't assume the error is a user mistake - it might be your outdated knowledge
Development workflow

Always verify before writing code:

Check packages installed

ls node_modules/@mastra/


Look up current API

If installed → Use embedded docs references/embedded-docs.md
If not → Use remote docs references/remote-docs.md

Write code based on current docs

Test in Studio

npm run dev  # http://localhost:4111

Resources
Setup: references/create-mastra.md
Embedded docs lookup: references/embedded-docs.md - Start here if packages are installed
Remote docs lookup: references/remote-docs.md
Common errors: references/common-errors.md
Migrations: references/migration-guide.md
Weekly Installs
14.3K
Repository
mastra-ai/skills
GitHub Stars
51
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn