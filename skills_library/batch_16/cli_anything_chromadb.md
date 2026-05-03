---
title: cli-anything-chromadb
url: https://skills.sh/hkuds/cli-anything/cli-anything-chromadb
---

# cli-anything-chromadb

skills/hkuds/cli-anything/cli-anything-chromadb
cli-anything-chromadb
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-chromadb
SKILL.md
cli-anything-chromadb

A stateless command-line interface for ChromaDB vector database, built on the HTTP API v2. Designed for AI agents and power users who need to manage collections, documents, and run semantic queries without a browser UI.

Installation

This CLI is installed as part of the cli-anything-chromadb package:

pip install cli-anything-chromadb


Prerequisites:

Python 3.10+
ChromaDB server running at localhost:8000 (or specify via --host)
Usage
Basic Commands
# Show help
cli-anything-chromadb --help

# Start interactive REPL mode
cli-anything-chromadb

# Check server health
cli-anything-chromadb --json server heartbeat

# List all collections
cli-anything-chromadb --json collection list

# Semantic search
cli-anything-chromadb --json query search --collection hub_knowledge --text "How to deploy"

REPL Mode

When invoked without a subcommand, the CLI enters an interactive REPL session:

cli-anything-chromadb
# Enter commands interactively with tab-completion and history

Command Groups
server

Server health and version commands.

Command	Description
heartbeat	Check ChromaDB server health
version	Get ChromaDB server version
collection

Manage ChromaDB collections.

Command	Description
list	List all collections
create --name NAME	Create a new collection
delete --name NAME	Delete a collection
info NAME	Get collection info
document

Manage documents in collections.

Command	Description
add --collection C --id ID --document TEXT	Add document(s)
get --collection C	Get documents
delete --collection C --id ID	Delete document(s)
count --collection C	Count documents
query

Semantic search against collections.

Command	Description
search --collection C --text T	Semantic search
Output Formats

All commands support dual output modes:

Human-readable (default): Tables, colors, formatted text
Machine-readable (--json flag): Structured JSON for agent consumption
# Human output
cli-anything-chromadb server heartbeat

# JSON output for agents
cli-anything-chromadb --json server heartbeat

For AI Agents

When using this CLI programmatically:

Always use --json flag for parseable output
Check return codes - 0 for success, non-zero for errors
Parse stderr for error messages on failure
Use --host to connect to non-default ChromaDB instances
Version

1.0.0

Weekly Installs
94
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass