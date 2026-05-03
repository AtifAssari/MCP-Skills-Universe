---
title: collavre
url: https://skills.sh/sh1nj1/plan42/collavre
---

# collavre

skills/sh1nj1/plan42/collavre
collavre
Installation
$ npx skills add https://github.com/sh1nj1/plan42 --skill collavre
SKILL.md
Collavre

CLI for managing Collavre Creatives via MCP protocol.

Setup
# Configure (once)
collavre auth --url https://collavre.example.com --token <oauth_token>

# Verify
collavre list


The collavre script lives in scripts/collavre. Config is stored at ~/.config/collavre/config.json.

Commands
List root creatives
collavre list
collavre list --level 5              # deeper tree
collavre list --format json          # structured output

Get a creative subtree
collavre get 123
collavre get 123 --level 5 --comments

Search
collavre search "project name"
collavre search "urgent" --tags "v2"

Create
collavre create --parent 123 --desc "New task"
collavre create --parent 123 --desc "<h1>Rich content</h1>"

Update
collavre update 456 --desc "Updated title"
collavre update 456 --progress 1.0        # mark complete (leaf only)
collavre update 456 --parent 789           # move

Import markdown
collavre import --parent 123 --file plan.md
collavre import --parent 123 --stdin < plan.md
echo "# Quick\n## Plan" | collavre import --parent 123 --stdin

Batch operations
collavre batch --file ops.json


ops.json format:

[
  { "action": "create", "parent_id": 100, "description": "Task A" },
  { "action": "update", "id": 200, "progress": 1.0 },
  { "action": "delete", "id": 300 }
]

Discover & run tools (meta)
collavre tool list                                # list available tools
collavre tool list --full                         # list with full details
collavre tool search "github"                     # search by name/description
collavre tool info <tool_name>                    # show tool parameters
collavre tool run <tool_name> --json '{"k":"v"}'  # run with JSON args
collavre tool run <tool_name> --key value         # run with flag args

Key Concepts
Tree structure: Creatives nest via parent_id. Use --level to control depth.
Progress: Leaf = manual (0.0 or 1.0). Parent = auto-calculated from children.
Import: Markdown headings/bullets become nested Creatives.
Batch: All-or-nothing transaction. Requires approval.
Description format: Accepts HTML. Plain text auto-wraps in <p> tags.

For detailed MCP tool parameters, see references/tool-reference.md.

Weekly Installs
22
Repository
sh1nj1/plan42
GitHub Stars
9
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail