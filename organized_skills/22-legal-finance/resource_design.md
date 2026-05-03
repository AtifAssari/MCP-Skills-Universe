---
rating: ⭐⭐⭐
title: resource-design
url: https://skills.sh/xmcp-dev/skills/resource-design
---

# resource-design

skills/xmcp-dev/skills/resource-design
resource-design
Installation
$ npx skills add https://github.com/xmcp-dev/skills --skill resource-design
SKILL.md
Create xmcp Resource

You are helping the user create a new xmcp resource. Follow this interactive workflow.

Step 1: Gather Information

Before generating any code, ask the user these questions using AskUserQuestion:

Resource name (if not provided): What should the resource be named? (Use kebab-case)

Resource type: Ask which type of resource they need:

Static - Fixed content that doesn't change (configuration, documentation)
Dynamic - Content that depends on parameters (user profiles, reports)
File-based - Content read from files (logs, data files)

URI pattern: How should the resource be accessed?

Simple: config://app or docs://readme
With parameters: users://[userId]/profile
Nested: reports://[year]/[month]/summary

Content details:

What is the content about?

Widget support (optional): Ask if they need OpenAI widget rendering.

Step 2: Generate the Resource

Create the resource file in src/resources/ following the routing conventions:

File Location & Routing

Resources use file-based routing similar to Next.js:

src/resources/
├── (config)/              # Route group (not in URI)
│   └── app.ts            # → config://app
├── (users)/
│   └── [userId]/         # Dynamic segment
│       └── profile.ts    # → users://[userId]/profile
└── docs/
    └── readme.ts         # → docs://readme


Routing conventions:

(folder) - Route group, excluded from URI path
[param] - Dynamic parameter segment
Filename becomes the final URI segment
Resource Structure Reference

Every xmcp resource has two main exports:

// 1. Metadata (optional) - Resource configuration
export const metadata: ResourceMetadata = { /* ... */ };

// 2. Handler (required) - Default export function
export default function handler(params?) { /* ... */ }

// 3. Schema (optional) - For dynamic resources with parameters
export const schema = { /* ... */ };

Quick Reference
Essential Imports
import { type ResourceMetadata } from "xmcp";

// For dynamic resources
import { z } from "zod";
import { type InferSchema, type ResourceMetadata } from "xmcp";

Metadata Fields
Field	Type	Required	Description
name	string	No*	Unique resource identifier
title	string	No	Human-readable title
description	string	No	What this resource provides
mimeType	string	No	Content type (default: text/plain)
size	number	No	Content size in bytes
_meta	object	No	Vendor extensions (OpenAI, etc.)

*When metadata is omitted, xmcp uses the filename as the resource name.

Handler Return Types
Return Type	Use Case
string	Simple text content
{ text: string }	Explicit text content
{ blob: Uint8Array, mimeType: string }	Binary content
JSON.stringify(data)	JSON content
Detailed Templates

For complete code templates including:

Static resource patterns
Dynamic resource with parameters
File-based resources
Nested routing examples
OpenAI metadata examples

Read: references/patterns.md

Checklist After Generation
File created in correct src/resources/ location
If using metadata, ensure it has descriptive name and description
Schema uses .describe() for all parameters (if dynamic)
Handler returns appropriate content type
File path matches intended URI pattern

Suggest running pnpm build to verify the resource compiles correctly.

Weekly Installs
27
Repository
xmcp-dev/skills
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass