---
rating: ⭐⭐⭐
title: glean-cli-documents
url: https://skills.sh/gleanwork/glean-cli/glean-cli-documents
---

# glean-cli-documents

skills/gleanwork/glean-cli/glean-cli-documents
glean-cli-documents
Installation
$ npx skills add https://github.com/gleanwork/glean-cli --skill glean-cli-documents
SKILL.md
glean documents

PREREQUISITE: Read ../glean-cli/SKILL.md for auth, global flags, and security rules.

Retrieve and summarize Glean documents. Subcommands: get, get-by-facets, get-permissions, summarize.

glean documents <subcommand> [flags]

Subcommands
Subcommand	Description
get	Retrieve document metadata by URL or ID
get-by-facets	Retrieve documents matching facet filters
get-permissions	Inspect who has access to a document
summarize	Generate an AI summary of a document
Flags
Flag	Type	Default	Description
--dry-run	boolean	false	
--json	string		JSON request body
--output	json | ndjson | text	json	
Examples
glean documents summarize --json '{"documentId":"DOC_ID"}' | jq .summary

Discovering Commands
# Show machine-readable schema for this command
glean schema documents

# List all available commands
glean schema | jq '.commands'

Weekly Installs
34
Repository
gleanwork/glean-cli
GitHub Stars
45
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass