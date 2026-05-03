---
rating: ⭐⭐
title: context7-mcp
url: https://skills.sh/darraghh1/my-claude-setup/context7-mcp
---

# context7-mcp

skills/darraghh1/my-claude-setup/context7-mcp
context7-mcp
Installation
$ npx skills add https://github.com/darraghh1/my-claude-setup --skill context7-mcp
SKILL.md
Context7 Library Documentation

You are an expert at using the Context7 MCP server to retrieve current, accurate library documentation. Context7 provides up-to-date docs for thousands of libraries and frameworks, eliminating outdated training data issues.

Critical: These Are Direct Tool Calls

MCP tools are direct tool calls — exactly like Read, Grep, or Bash. They are NOT CLI commands.

CORRECT — call the tool directly:

Tool: mcp__context7__resolve-library-id
Parameters: { "libraryName": "next.js" }


WRONG — do NOT shell out:

Bash: claude mcp call context7 resolve-library-id ...  # This does not work


All Context7 MCP tools use the mcp__context7__ prefix.

Critical: Always Resolve Library ID First

You must call resolve-library-id before query-docs unless you already have a confirmed /org/project ID from a previous call in this session.

Critical: Output Size Awareness
Tool	Output Size	Notes
resolve-library-id	Small	Returns list of matching library IDs
query-docs	Medium-Large	Documentation content — scales with topic breadth. Use specific queries to limit size.
Workflow: Find & Query Documentation

Trigger: User asks about library APIs, framework patterns, configuration options, or "how to do X with Y library"

Steps

Resolve the library ID:

resolve-library-id({ libraryName: "next.js" })
→ returns matching libraries with /org/project IDs


Query documentation with a specific question:

query-docs({ libraryId: "/vercel/next.js", query: "how to use middleware for authentication" })
→ returns relevant documentation sections


Refine if needed (max 3 calls per tool per question):

query-docs({ libraryId: "/vercel/next.js", query: "middleware matcher config" })
→ more specific follow-up

Key Patterns
Be specific in queries: "How to set up authentication with JWT in Express.js" beats "auth"
Max 3 calls per tool per question — if 3 queries don't answer it, use a different approach
One library per query — don't try to query multiple libraries in a single query-docs call
Use the full /org/project format for libraryId (e.g., /vercel/next.js, /supabase/supabase)
Decision Tree
User Needs	Action
Docs for a known library	resolve-library-id → query-docs
Not sure which library to use	resolve-library-id with general term, review matches
Already have library ID from this session	Skip resolve, go straight to query-docs
Library not found in Context7	Fall back to tavily-mcp search or WebFetch for official docs site
Common Library IDs

These are frequently used in this project — skip resolve-library-id for these:

Library	ID
Next.js	/vercel/next.js
React	/facebook/react
Supabase JS	/supabase/supabase-js
TanStack Query	/tanstack/query
Zod	/colinhacks/zod
React Hook Form	/react-hook-form/react-hook-form
Tailwind CSS	/tailwindlabs/tailwindcss
date-fns	/date-fns/date-fns
Radix UI	/radix-ui/primitives
Playwright	/microsoft/playwright
Vitest	/vitest-dev/vitest

Note: If a common ID stops working, re-resolve it — library IDs can change when repos are reorganized.

Troubleshooting
"Library not found"
Try alternate names: "react-query" vs "tanstack query" vs "@tanstack/react-query"
Try the npm package name: "next" vs "next.js"
Try the GitHub org/repo format directly: "vercel/next.js"
Fall back to tavily-mcp search for the official docs URL, then use WebFetch
Query Returns Irrelevant Results
Make your query more specific — include the exact API name or concept
Try rephrasing: "server actions" vs "use server directive" vs "form actions"
Add version context: "Next.js 15 app router middleware" vs just "middleware"
Query Returns Too Much Content
Narrow the query to a specific function or concept
Ask about one feature at a time rather than broad overviews
If output is still large, extract the relevant section and summarize for the user
Weekly Installs
24
Repository
darraghh1/my-cl…de-setup
GitHub Stars
44
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn