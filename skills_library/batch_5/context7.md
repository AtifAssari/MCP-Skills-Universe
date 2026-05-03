---
title: context7
url: https://skills.sh/netresearch/context7-skill/context7
---

# context7

skills/netresearch/context7-skill/context7
context7
Installation
$ npx skills add https://github.com/netresearch/context7-skill --skill context7
SKILL.md
Context7 Documentation Lookup Skill

Fetch current library documentation, API references, and code examples via the Context7 REST API.

When to Use

Use this skill when the user asks about library APIs, framework patterns, or version-specific behavior. Trigger on:

Library questions: "How do I use [library]?", "[library] API docs", "[library] patterns"
Import statements: import, require, from followed by a library name
Framework-specific topics: hooks, routing, middleware, ORM queries, schema definitions
When NOT to Use

Do NOT use this skill for:

General programming concepts (closures, recursion, design patterns)
Code review or refactoring tasks
Debugging business logic
Writing scripts from scratch without library-specific questions
Core Workflow

Search for the library ID:

scripts/context7.sh search "library-name"


Pick the best result: Choose the ID with the highest score and most relevant description. Prefer official sources (e.g., /vercel/next.js over community forks).

Fetch documentation with a focused topic:

scripts/context7.sh docs "<library-id>" "<topic>" "<mode>"


Always extract a specific topic from the user's question. For "How does React Suspense work with server components?", use topic suspense server components.

Parameters
Parameter	Required	Description
library-id	Yes	From search results, format /vendor/library
topic	No	Focus area extracted from user query (e.g., hooks, routing, validation)
mode	No	code (default) for API references; info for conceptual guides
Mode Selection

Use code mode (default) when the user asks for API references, code examples, or implementation patterns.

Use info mode when the user asks for conceptual explanations, architecture guides, or migration tutorials.

Examples
# React hooks API
scripts/context7.sh search "react"
scripts/context7.sh docs "/facebook/react" "hooks" "code"

# Next.js App Router conceptual guide
scripts/context7.sh search "nextjs"
scripts/context7.sh docs "/vercel/next.js" "app router" "info"

# Django ORM queries
scripts/context7.sh search "django"
scripts/context7.sh docs "/django/django" "queryset filter" "code"

# Laravel Eloquent relationships
scripts/context7.sh search "laravel"
scripts/context7.sh docs "/laravel/framework" "eloquent relationships" "code"

Environment Configuration

Set CONTEXT7_API_KEY for higher rate limits (optional):

export CONTEXT7_API_KEY="your-api-key"


Contributing: https://github.com/netresearch/context7-skill

Weekly Installs
298
Repository
netresearch/con…t7-skill
GitHub Stars
15
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn