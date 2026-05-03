---
title: documentation-lookup
url: https://skills.sh/upstash/context7/documentation-lookup
---

# documentation-lookup

skills/upstash/context7/documentation-lookup
documentation-lookup
Installation
$ npx skills add https://github.com/upstash/context7 --skill documentation-lookup
Summary

Fetch current library documentation and code examples instead of relying on training data.

Resolves library names to Context7 documentation IDs, then queries for setup, configuration, and API reference information
Supports major frameworks and libraries: React, Vue, Svelte, Next.js, Express, Prisma, Supabase, Tailwind, and others
Activates automatically for setup questions, code generation requests, and framework-specific inquiries
Returns version-aware documentation and official code examples to ensure accuracy and currency
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
1.4K
Repository
upstash/context7
GitHub Stars
54.3K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn