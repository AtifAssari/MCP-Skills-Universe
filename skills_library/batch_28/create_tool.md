---
title: create-tool
url: https://skills.sh/xmcp-dev/skills/create-tool
---

# create-tool

skills/xmcp-dev/skills/create-tool
create-tool
Installation
$ npx skills add https://github.com/xmcp-dev/skills --skill create-tool
SKILL.md
Create xmcp Tool

You are helping the user create a new xmcp tool. Follow this interactive workflow.

Step 1: Gather Information

Before generating any code, ask the user these questions using AskUserQuestion:

Tool name (if not provided as argument): What should the tool be named? (Use kebab-case)

Handler type: Ask which handler type they need:

Standard - For data queries, calculations, API calls (returns string/JSON)
Template Literal (HTML) - For HTML widgets with external scripts
React Component - For interactive stateful widgets (.tsx file)

Schema fields: What parameters should the tool accept? Ask for:

Parameter name
Type (string, number, boolean, enum, array, object)
Description
Whether it's optional
Any validation rules

Annotations: Ask about behavior hints:

Is it read-only? (doesn't modify environment)
Is it destructive? (may delete or modify data)
Is it idempotent? (repeated calls have same effect)
Does it interact with external world? (openWorldHint)

Widget support (if Template Literal or React): Ask if they need:

OpenAI tool invocation messages (invoking/invoked status)
Widget accessibility (widgetAccessible)
Widget-to-tool communication
Step 2: Generate the Tool

Create the tool file in src/tools/ with the appropriate extension:

.ts for Standard and Template Literal handlers
.tsx for React Component handlers
File Location
src/tools/{tool-name}.ts   # or .tsx for React

Tool Structure Reference

Every xmcp tool has three main exports:

// 1. Schema (optional) - Define parameters with Zod
export const schema = { /* ... */ };

// 2. Metadata (optional) - Tool configuration
export const metadata: ToolMetadata = { /* ... */ };

// 3. Handler (required) - Default export function
export default function handler(params) { /* ... */ }

Quick Reference
Essential Imports
import { z } from "zod";
import { type InferSchema, type ToolMetadata } from "xmcp";

Handler Types Summary
Type	Use Case	File Extension
Standard (string)	Simple queries, calculations	.ts
Standard (async)	API calls, database queries	.ts
Template Literal	HTML widgets, iframes, scripts	.ts
React Component	Interactive stateful UIs	.tsx
No Parameters	Tools that don't need input	.ts
With Extra Args	Auth/context-dependent tools	.ts
Annotations Quick Reference
Annotation	Use When
readOnlyHint: true	Tool doesn't modify environment
destructiveHint: true	Tool may delete/modify data
idempotentHint: true	Repeated calls have same effect
openWorldHint: true	Tool interacts with external world
Detailed Templates

For complete code templates including:

Schema patterns (simple, validation, enum, optional, object)
Metadata patterns (basic, annotations, OpenAI widgets, MCP Apps UI)
All handler type templates (A through G)
Return value patterns
Type imports reference

Read: references/templates.md

Checklist After Generation
File created in src/tools/{tool-name}.ts (or .tsx)
Schema uses .describe() for all parameters
If using metadata, ensure it has descriptive name and description
Appropriate annotations set based on tool behavior
Handler matches the chosen type
All imports are correct

Suggest running pnpm build to verify the tool compiles correctly.

Weekly Installs
33
Repository
xmcp-dev/skills
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn