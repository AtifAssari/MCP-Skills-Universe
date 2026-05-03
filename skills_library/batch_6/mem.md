---
title: mem
url: https://skills.sh/runablehq/memory/mem
---

# mem

skills/runablehq/memory/mem
mem
Installation
$ npx skills add https://github.com/runablehq/memory --skill mem
SKILL.md
mem — Agent Memory Store

A CLI tool for storing and retrieving memories with full-text search. Data is stored locally in ~/.mem/mem.db.

When to Use
Remember user preferences, project decisions, important facts
Store code snippets, commands, configurations for later recall
Search your knowledge base before asking the user for information you may have stored
Attach images (screenshots, diagrams) to memories
Commands

Three operators: (none) = recall, + = remember, - = forget.

Recall (search, list, get)
mem                             # list recent memories
mem "deploy"                    # full-text search
mem "database" --tag db         # search filtered by tag
mem 7sjtNVyZrNIa                # get full content by ID
mem --tag prefs                 # list filtered by tag
mem "api" --limit 5 --json     # limit results, JSON output
mem --full                      # show full content for all

Remember
mem + "user prefers dark mode" --tag prefs
mem + "deploy: bun build --compile" --tag deploy
mem + "chose SQLite for simplicity" --tag architecture
mem + --image ./screenshot.png --title "Current UI" --tag ui
echo "long content" | mem + --tag notes

Forget
mem - <id>                      # delete one memory
mem - id1 id2 id3               # delete multiple

Piping
mem "old" --json | jq -r '.[].id' | xargs -I{} mem - {}
echo "long content" | mem + --tag notes

Best Practices
Tag consistently — Use lowercase, descriptive tags like prefs, api, deploy, db
Search before asking — Check if you've stored relevant information before asking the user
Store decisions — When making architectural or design decisions, store the reasoning
Keep memories atomic — One concept per memory for better searchability
Output Formats
Default: One-line summary per result
--full: Complete content inline
--json: Structured JSON for parsing
Weekly Installs
2.3K
Repository
runablehq/memory
GitHub Stars
5
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass