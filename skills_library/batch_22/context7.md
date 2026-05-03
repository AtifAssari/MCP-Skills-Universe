---
title: context7
url: https://skills.sh/huynguyen03dev/opencode-setup/context7
---

# context7

skills/huynguyen03dev/opencode-setup/context7
context7
Installation
$ npx skills add https://github.com/huynguyen03dev/opencode-setup --skill context7
SKILL.md
Context7

Base directory for this skill: /home/hazeruno/.config/opencode/skills/context7

Retrieve up-to-date documentation and code examples for any library via the Context7 MCP service.

Quick Start

Run the CLI script with bun (use absolute path):

bun /home/hazeruno/.config/opencode/skills/context7/scripts/context7.ts <command> [options]

Available Commands
resolve-library-id

Resolve a package/product name to a Context7-compatible library ID.

bun /home/hazeruno/.config/opencode/skills/context7/scripts/context7.ts resolve-library-id --library-name "react"
bun /home/hazeruno/.config/opencode/skills/context7/scripts/context7.ts resolve-library-id --library-name "next.js"


Required before get-library-docs unless user provides library ID in format /org/project.

get-library-docs

Fetch documentation for a library.

# Basic usage
bun /home/hazeruno/.config/opencode/skills/context7/scripts/context7.ts get-library-docs \
  --context7-compatible-library-i-d "/vercel/next.js"

# With topic focus
bun /home/hazeruno/.config/opencode/skills/context7/scripts/context7.ts get-library-docs \
  --context7-compatible-library-i-d "/vercel/next.js" --topic "routing"

# Different modes: code (API refs) or info (conceptual guides)
bun /home/hazeruno/.config/opencode/skills/context7/scripts/context7.ts get-library-docs \
  --context7-compatible-library-i-d "/mongodb/docs" --mode "info"


Parameters:

--context7-compatible-library-i-d: Library ID (e.g., /mongodb/docs, /vercel/next.js)
--mode: code (default) for API/examples, info for conceptual guides
--topic: Focus on specific topic (e.g., hooks, routing, authentication)
--page: Pagination (1-10), use higher pages if context insufficient
Global Options
-t, --timeout <ms>: Call timeout (default: 30000)
-o, --output <format>: Output format: text | markdown | json | raw
Common Library IDs
Library	ID
React	/facebook/react
Next.js	/vercel/next.js
MongoDB	/mongodb/docs
Supabase	/supabase/supabase
Prisma	/prisma/prisma
Requirements
Bun runtime
mcporter package (embedded in script)
Weekly Installs
15
Repository
huynguyen03dev/…de-setup
GitHub Stars
5
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn