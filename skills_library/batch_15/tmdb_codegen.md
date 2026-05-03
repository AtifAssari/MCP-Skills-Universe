---
title: tmdb-codegen
url: https://skills.sh/qingqishi/shiqingqi.com/tmdb-codegen
---

# tmdb-codegen

skills/qingqishi/shiqingqi.com/tmdb-codegen
tmdb-codegen
Installation
$ npx skills add https://github.com/qingqishi/shiqingqi.com --skill tmdb-codegen
SKILL.md
TMDB Code Generation
Overview

This project uses automatic code generation for TMDB API integration with selective Zod schema generation for optimal performance.

Critical Rule

NEVER manually edit src/_generated/tmdb-server-functions.ts - it is auto-generated.

Always use pnpm codegen:tmdb to regenerate after making changes to endpoint configurations.

Architecture
Selective Zod Schema Generation

The project uses a selective approach to Zod schema generation:

Performance optimization: 98.7% size reduction (from 16K lines to ~200 lines)
On-demand schemas: Only generates Zod schemas for endpoints that need them
AI tool compatibility: Schemas are generated for endpoints requiring OpenAI Structured Outputs validation
When Zod Schemas Are Generated

Zod schemas are only generated for endpoints marked with needsZodSchema: true in endpoints-config.js.

Why selective?

Most endpoints only need TypeScript types
Zod schemas are only required for AI tools using OpenAI Structured Outputs
Dramatically improves developer experience (faster builds, smaller bundles, better IDE performance)
Configuration
Endpoint Configuration File

Location: tooling/tmdb-codegen/endpoints-config.js

export const endpoints = [
  {
    path: "/3/search/movie",
    functionName: "searchMovies",
    needsZodSchema: true, // ✅ Zod schema generated for AI tools
  },
  {
    path: "/3/movie/{movie_id}",
    functionName: "getMovieDetails",
    // ❌ No needsZodSchema flag = TypeScript types only
  },
];

Adding New Endpoints
Add endpoint configuration to endpoints-config.js
Set needsZodSchema: true only if needed for AI tools
Run pnpm codegen:tmdb to regenerate
{
  path: "/3/discover/tv",
  functionName: "discoverTvShows",
  needsZodSchema: false, // Only TS types needed
}

Code Generation Commands
# Full pipeline (TypeScript types + Zod schemas)
pnpm codegen

# Only regenerate TMDB server functions
pnpm codegen:tmdb

# Only regenerate Zod schemas (fast!)
pnpm codegen:zod

Generated Files
Auto-Generated (DO NOT EDIT)
src/_generated/tmdb-server-functions.ts - Server functions with TypeScript types
src/_generated/tmdb-zod-schemas.ts - Selective Zod schemas (only for endpoints with needsZodSchema: true)

These files are git-ignored and must be regenerated after cloning:

pnpm codegen:tmdb

How It Works
1. Custom Generator

Location: tooling/tmdb-codegen/generate-selective-zod.js

Reads endpoints-config.js to find endpoints needing Zod schemas
Generates hand-crafted Zod schemas (not auto-generated from TypeScript)
Applies OpenAI compatibility fixes (.nullable().optional())
Outputs minimal, optimized schemas
2. OpenAI Compatibility

Automatically applies fixes for OpenAI Structured Outputs:

// Generated schema with OpenAI compatibility
export const movieSchema = z.object({
  id: z.number(),
  title: z.string().nullable().optional(), // OpenAI-compatible
  overview: z.string().nullable().optional(),
});

Usage in Code
Importing Server Functions
import { searchMovies, getMovieDetails } from "@/utils/tmdb-server-functions";

// Use in server components
const movies = await searchMovies({ query: "Inception" });

Importing Zod Schemas (for AI tools)
import { movieSearchSchema } from "@/utils/tmdb-zod-schemas";

// Use with OpenAI Structured Outputs
const completion = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [...],
  response_format: zodResponseFormat(movieSearchSchema, "movies"),
});

When to Regenerate

Regenerate TMDB code when:

Adding new endpoints - Add to endpoints-config.js, then run pnpm codegen:tmdb
Changing endpoint configuration - Modify endpoints-config.js, then regenerate
After cloning repository - Generated files are git-ignored
Updating TMDB API version - Update base URL, then regenerate
Best Practices
Never edit generated files - Always use pnpm codegen:tmdb
Minimal Zod schemas - Only set needsZodSchema: true when needed for AI tools
Check generation - Verify generated files after running codegen
Commit config changes - endpoints-config.js is version-controlled
Don't commit generated files - They're git-ignored for a reason
Performance Impact
Before Selective Generation
16,000+ lines of Zod schemas
Slow builds and IDE performance
Large bundle size
After Selective Generation
~200 lines of Zod schemas (98.7% reduction)
Fast builds and responsive IDE
Minimal bundle impact
Common Workflows
Add New TMDB Endpoint
# 1. Edit configuration
# Add to tooling/tmdb-codegen/endpoints-config.js

# 2. Regenerate
pnpm codegen:tmdb

# 3. Use in code
import { newFunction } from "@/utils/tmdb-server-functions";

Add Zod Schema to Existing Endpoint
# 1. Edit configuration
# Set needsZodSchema: true in endpoints-config.js

# 2. Regenerate Zod schemas only (fast!)
pnpm codegen:zod

# 3. Use schema
import { newSchema } from "@/utils/tmdb-zod-schemas";

Troubleshooting
Generated files missing after clone
pnpm codegen:tmdb

TypeScript errors in generated files
# Regenerate from scratch
rm -rf src/_generated
pnpm codegen:tmdb

Zod schema needed but not generated

Check endpoints-config.js - ensure needsZodSchema: true is set for that endpoint, then regenerate.

Weekly Installs
12
Repository
qingqishi/shiqingqi.com
GitHub Stars
4
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass