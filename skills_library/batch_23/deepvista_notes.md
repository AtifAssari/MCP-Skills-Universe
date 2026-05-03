---
title: deepvista-notes
url: https://skills.sh/deepvista-ai/deepvista-cli/deepvista-notes
---

# deepvista-notes

skills/deepvista-ai/deepvista-cli/deepvista-notes
deepvista-notes
Installation
$ npx skills add https://github.com/deepvista-ai/deepvista-cli --skill deepvista-notes
SKILL.md
Notes

PREREQUISITE: Read deepvista-shared for auth, profiles, and global flags.

Notes are context cards with type=note. They support rich markdown content and are the primary way to explicitly capture knowledge — meeting notes, summaries, research, decisions.

deepvista notes is a convenience shorthand. Every notes command has an exact equivalent using deepvista card:

Notes command	Equivalent card command
deepvista notes list	deepvista card list --type note
deepvista notes get <id>	deepvista card get <id>
deepvista notes create ...	deepvista card create --type note ...
deepvista notes +quick "..."	(shorthand only, no direct card equivalent)
App URLs

After any write operation (create, update, +quick), always show the note URL to the user:

https://app.deepvista.ai/notes/<id>


Extract the id from the JSON response (card.id) and present it as a clickable link.

Commands
list
deepvista notes list [--limit N] [--page N]


Read-only — lists all notes, newest first.

get
deepvista notes get <note_id>


Read-only — returns full note content including markdown body.

create
deepvista notes create --title "Title" [--content "Markdown content"] [--tags '["t1","t2"]']


[!CAUTION] Write command — confirm with user before executing.

update
deepvista notes update <note_id> [--title "..."] [--content "..."] [--tags '["t1"]']


[!CAUTION] Write command — confirm with user before executing.

delete
deepvista notes delete <note_id>


[!CAUTION] Destructive command — confirm with user before executing.

+quick
deepvista notes +quick "your text here"


Quick-create a note from a single line of text. The first ~50 characters become the title; the full text becomes the content. Entity enrichment runs automatically.

[!CAUTION] Write command — creates a new note. Confirm with the user before executing.

Ideal for capturing quick observations mid-workflow.
For notes with custom titles or structured content, use notes create instead.
Created notes are searchable with deepvista card +search.
Examples
# List recent notes
deepvista notes list --limit 5

# Create a meeting note
deepvista notes create --title "Standup 2026-03-26" --content "## Discussed\n- Roadmap priorities\n- CLI release"

# Quick capture from a single line
deepvista notes +quick "Alice mentioned the API migration deadline is April 15"

# Update a note
deepvista notes update note_abc --content "Updated content with new findings..."

# Search notes (uses card search)
deepvista card +search "API migration" --type note

See Also
deepvista-shared — Auth and global flags
deepvista-memory — Full knowledge base API (all card types)
deepvista-recipe-analyze-notes — Analyze patterns across notes
Weekly Installs
27
Repository
deepvista-ai/de…ista-cli
GitHub Stars
5
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass