---
rating: ⭐⭐
title: prompt-design
url: https://skills.sh/xmcp-dev/skills/prompt-design
---

# prompt-design

skills/xmcp-dev/skills/prompt-design
prompt-design
Installation
$ npx skills add https://github.com/xmcp-dev/skills --skill prompt-design
SKILL.md
Create xmcp Prompt

You are helping the user create a new xmcp prompt. Follow this interactive workflow.

Step 1: Gather Information

Before generating any code, ask the user these questions using AskUserQuestion:

Prompt name (if not provided): What should the prompt be named? (Use kebab-case)

Prompt type: Ask which type of prompt they need:

Simple - Static prompt text without parameters
Parameterized - Prompt with user-provided parameters (most common)
Multi-content - Returns multiple content blocks (text, images, etc.)

Parameters (if parameterized): What inputs should the prompt accept?

Parameter name
Type (string, number, enum)
Description
Whether it's optional
Any validation or default values

Role: What role should the prompt assume?

user - Prompt from user perspective (most common)
assistant - Prompt as assistant response template

Use case: What is the prompt designed for?

Code review
Documentation generation
Data analysis
Content creation
Other specific task
Step 2: Generate the Prompt

Create the prompt file in src/prompts/:

File Location
src/prompts/{prompt-name}.ts

Prompt Structure Reference

Every xmcp prompt has three main exports:

// 1. Schema (optional) - Define parameters with Zod
export const schema = { /* ... */ };

// 2. Metadata (optional) - Prompt configuration
export const metadata: PromptMetadata = { /* ... */ };

// 3. Handler (required) - Default export function
export default function handler(params?) { /* ... */ }

Quick Reference
Essential Imports
import { type PromptMetadata } from "xmcp";

// For parameterized prompts
import { z } from "zod";
import { type InferSchema, type PromptMetadata } from "xmcp";

Metadata Fields
Field	Type	Required	Description
name	string	No*	Unique prompt identifier
title	string	No	Human-readable title
description	string	No	What this prompt does
role	string	No	"user" or "assistant" (default: user)

*When metadata is omitted, xmcp uses the filename as the prompt name.

Handler Return Types
Return Type	Use Case
string	Simple text prompt
{ type: "text", text: string }	Explicit text content
{ type: "image", data: base64, mimeType: string }	Image content
Array<Content>	Multiple content blocks
Use Cases for Server-Exposed Prompts

MCP prompts are useful for:

Standardized workflows - Consistent code review, documentation patterns
Complex templates - Multi-step analysis prompts with structure
Domain expertise - Specialized prompts for specific domains
Reusable patterns - Common tasks that benefit from parameterization
Client integration - Prompts that MCP clients can discover and use
Detailed Templates

For complete code templates including:

Simple prompt patterns
Parameterized prompts with Zod schemas
Multi-role conversation prompts
Autocompletion support
Code review and documentation examples

Read: references/patterns.md

Checklist After Generation
File created in src/prompts/{prompt-name}.ts
If using metadata, ensure it has name, title, and description
Schema uses .describe() for all parameters (if parameterized)
Handler returns appropriate content format
Role is set appropriately for the use case

Suggest running pnpm build to verify the prompt compiles correctly.

Weekly Installs
28
Repository
xmcp-dev/skills
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass