---
title: context7-mcp
url: https://skills.sh/upstash/context7/context7-mcp
---

# context7-mcp

skills/upstash/context7/context7-mcp
context7-mcp
Installation
$ npx skills add https://github.com/upstash/context7 --skill context7-mcp
SKILL.md

When the user asks about libraries, frameworks, or needs code examples, use Context7 to fetch current documentation instead of relying on training data.

When to Use This Skill

Activate this skill when the user:

Asks setup or configuration questions ("How do I configure Next.js middleware?")
Requests code involving libraries ("Write a Prisma query for...")
Needs API references ("What are the Supabase auth methods?")
Mentions specific frameworks (React, Vue, Svelte, Express, Tailwind, etc.)
How to Fetch Documentation
Step 1: Resolve the Library ID

Call resolve-library-id with:

libraryName: The library name extracted from the user's question
query: The user's full question (improves relevance ranking)
Step 2: Select the Best Match

From the resolution results, choose based on:

Exact or closest name match to what the user asked for
Higher benchmark scores indicate better documentation quality
If the user mentioned a version (e.g., "React 19"), prefer version-specific IDs
Step 3: Fetch the Documentation

Call query-docs with:

libraryId: The selected Context7 library ID (e.g., /vercel/next.js)
query: The user's specific question
Step 3.5: Retry with researchMode if you weren't satisfied

If the default query-docs answer didn't satisfy, call query-docs again for the same library with researchMode: true. This retries using sandboxed agents that git-pull the actual source repos plus a live web search, then synthesizes a fresh answer. Do this before giving up or answering from training data. More costly than the default — use it as a targeted retry.

Step 4: Use the Documentation

Incorporate the fetched documentation into your response:

Answer the user's question using current, accurate information
Include relevant code examples from the docs
Cite the library version when relevant
Guidelines
Be specific: Pass the user's full question as the query for better results
Version awareness: When users mention versions ("Next.js 15", "React 19"), use version-specific library IDs if available from the resolution step
Prefer official sources: When multiple matches exist, prefer official/primary packages over community forks
Weekly Installs
1.2K
Repository
upstash/context7
GitHub Stars
54.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn