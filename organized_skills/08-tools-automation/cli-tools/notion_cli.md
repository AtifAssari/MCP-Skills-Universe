---
rating: ⭐⭐⭐
title: notion-cli
url: https://skills.sh/makenotion/skills/notion-cli
---

# notion-cli

skills/makenotion/skills/notion-cli
notion-cli
Installation
$ npx skills add https://github.com/makenotion/skills --skill notion-cli
SKILL.md
Notion CLI
Look things up before answering

The CLI is self-documenting. Always prefer running these commands over guessing syntax or relying on memorized knowledge:

ntn api ls — list every public API endpoint.
ntn api <path> --help — show methods, doc links, and usage for an endpoint.
ntn api <path> --docs — print the full official docs for an endpoint.
ntn api <path> --spec — print a reduced OpenAPI fragment (useful for understanding request/response schemas).
ntn <command> --help — help for any command or subcommand.
Install
curl -fsSL https://ntn.dev | bash

Authentication
The CLI automatically uses NOTION_API_TOKEN when it is set.
Check NOTION_API_TOKEN first. If it is already set, prefer using it instead of telling the user to run ntn login.
ntn login / ntn logout — log the CLI in or out (only use if not using NOTION_API_TOKEN). ntn login requires the user to visit a URL in a web browser.
ntn api

Run ntn api --help for full syntax. Quick summary:

# GET with query param
ntn api v1/users page_size==100

# POST with inline body fields
ntn api v1/pages parent[page_id]=abc123

# POST with JSON body
ntn api v1/pages -d '{"parent":{"page_id":"abc123"}}'


The method is inferred (GET by default, POST when a body is present). Override with -X METHOD.

Markdown for pages and comments

Prefer the markdown field when creating or updating pages and comments.

# Comment with markdown
ntn api v1/comments -d '{"parent":{"page_id":"abc123"},"markdown":"Here is a [link](https://example.com) and **bold text**."}'

# Page with markdown body
ntn api v1/pages -d '{"parent":{"page_id":"abc123"},"properties":{"title":[{"text":{"content":"My Page"}}]},"markdown":"## Heading\nSome *formatted* content."}'


The markdown field supports inline formatting (bold, italic, code, links, etc.). Only fall back to rich_text if you need features that Markdown cannot express (e.g. mentions, custom emoji, or colors).

ntn files

Convenience wrapper around the File Uploads API.

ntn files create < image.png
ntn files create --external-url https://example.com/photo.png
ntn files list
ntn files get <upload-id>

ntn workers

Manage Notion workers (deploy, list, execute, etc.). Run ntn workers --help for subcommands.

ntn workers new my-worker        # scaffold a new project
ntn workers deploy               # deploy from current directory
ntn workers ls                   # list workers
ntn workers exec <capability>    # execute a capability

Weekly Installs
935
Repository
makenotion/skills
GitHub Stars
84
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn