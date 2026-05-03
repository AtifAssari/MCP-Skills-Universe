---
rating: ⭐⭐⭐
title: memos
url: https://skills.sh/akhy/agent-skills/memos
---

# memos

skills/akhy/agent-skills/memos
memos
Installation
$ npx skills add https://github.com/akhy/agent-skills --skill memos
SKILL.md
Memos Skill

Interact with a Memos instance via its REST API (/api/v1/memos).

Prerequisites

Set these env vars before using this skill:

export MEMOS_URL="https://memos.example.com"
export MEMOS_ACCESS_TOKEN="your_access_token"  # from Memos account settings


All requests use Authorization: Bearer $MEMOS_ACCESS_TOKEN.

Script

All operations go through scripts/memos.sh. Run it with bash memos/scripts/memos.sh <command> [options].

Run without arguments to see full usage:

bash memos/scripts/memos.sh --help

Operations
List memos
# All memos
bash memos/scripts/memos.sh list

# With filter (AIP-160 syntax)
bash memos/scripts/memos.sh list --filter 'state == "NORMAL"' --page-size 20

# Include deleted
bash memos/scripts/memos.sh list --show-deleted

Create a memo
bash memos/scripts/memos.sh create --content "Hello, world!" --visibility PUBLIC

# Pinned private memo
bash memos/scripts/memos.sh create --content "Important note" --pinned


--visibility: PUBLIC | PROTECTED | PRIVATE (default: PRIVATE)

Get a memo
bash memos/scripts/memos.sh get memos/123


Memo resource names follow the format memos/{id}.

Update a memo
bash memos/scripts/memos.sh update memos/123 --content "Updated content"
bash memos/scripts/memos.sh update memos/123 --visibility PUBLIC --pinned true
bash memos/scripts/memos.sh update memos/123 --state ARCHIVED


Only specified fields are sent in updateMask.

Delete a memo
# Soft delete
bash memos/scripts/memos.sh delete memos/123

# Hard delete
bash memos/scripts/memos.sh delete memos/123 --force

Comments
# List comments
bash memos/scripts/memos.sh comments memos/123

# Post a comment
bash memos/scripts/memos.sh comment memos/123 --content "Great memo!"

Reactions
# List reactions
bash memos/scripts/memos.sh reactions memos/123

# Add a reaction
bash memos/scripts/memos.sh react memos/123 --reaction "👍"

# Remove a reaction (reaction ID from list response)
bash memos/scripts/memos.sh delete-reaction memos/123 reactions/456

Attachments
# List attachments
bash memos/scripts/memos.sh attachments memos/123

# Set attachments (replaces existing)
bash memos/scripts/memos.sh set-attachments memos/123 --names "attachments/1,attachments/2"

Relations
# List relations
bash memos/scripts/memos.sh relations memos/123

# Set relations (replaces existing)
bash memos/scripts/memos.sh set-relations memos/123 --relations '[{"memo":"memos/123","relatedMemo":"memos/456","type":"REFERENCE"}]'

Pagination

List commands support --page-size N and --page-token TOKEN. The response includes nextPageToken when more results are available:

result=$(bash memos/scripts/memos.sh list --page-size 10)
next=$(echo "$result" | jq -r '.nextPageToken // empty')

# Fetch next page
bash memos/scripts/memos.sh list --page-size 10 --page-token "$next"

Filtering

Use AIP-160 filter expressions with --filter:

bash memos/scripts/memos.sh list --filter 'state == "NORMAL"'
bash memos/scripts/memos.sh list --filter 'visibility == "PUBLIC"'

Response Format

All responses are JSON. Pipe through jq to extract fields:

# Get all memo names and snippets
bash memos/scripts/memos.sh list | jq '.memos[] | {name, snippet}'

# Get a single field
bash memos/scripts/memos.sh get memos/123 | jq '.content'

Weekly Installs
28
Repository
akhy/agent-skills
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn