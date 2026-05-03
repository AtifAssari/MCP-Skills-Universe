---
rating: ⭐⭐⭐
title: deepvista-recipe-analyze-notes
url: https://skills.sh/deepvista-ai/deepvista-cli/deepvista-recipe-analyze-notes
---

# deepvista-recipe-analyze-notes

skills/deepvista-ai/deepvista-cli/deepvista-recipe-analyze-notes
deepvista-recipe-analyze-notes
Installation
$ npx skills add https://github.com/deepvista-ai/deepvista-cli --skill deepvista-recipe-analyze-notes
SKILL.md
Analyze Notes

PREREQUISITE: Read deepvista-shared, deepvista-memory, and deepvista-notes.

Search, retrieve, and analyze notes from the knowledge base to surface insights, patterns, and summaries.

Steps

Search for relevant notes using a query derived from the user's request:

deepvista card +search "<topic or keyword>" --type note --limit 20


List recent notes if no specific topic was given, to get a broad view:

deepvista notes list --limit 20


Fetch full content for the most relevant notes (pick IDs from search/list results):

deepvista notes get <note_id>


Repeat for each note you need to read in full.

Analyze and synthesize — read the content and identify:

Recurring themes or topics
Key decisions or action items
Open questions or unresolved threads
Timeline of ideas if dates are present

Present findings to the user as a structured summary.

Optionally save the analysis back as a new note (confirm with user first):

deepvista notes create --title "Analysis: <topic> — <date>" --content "<synthesis>"


[!CAUTION] Write command — confirm with user before saving.

Tips
Use card +search with specific keywords rather than listing everything — it uses hybrid vector+keyword search and returns the most relevant results.
Filter by type to stay focused on notes: deepvista card +search "<query>" --type note.
For time-bounded analysis ("notes from this week"), use notes list and filter by created_at in the JSON output.
Use chat +send to ask the AI agent to synthesize across a large set of notes:
deepvista chat +send "Here are my recent notes: <paste content>. What are the key themes?"

Examples
# Find all notes about a project
deepvista card +search "project alpha" --type note --limit 15

# Get full content of a note
deepvista notes get note_abc123

# Save analysis as a new note
deepvista notes create \
  --title "Weekly Themes — 2026-04-02" \
  --content "## Key Themes\n- Theme 1\n- Theme 2\n\n## Open Questions\n- ..."

See Also
deepvista-notes — CRUD operations on individual notes
deepvista-memory — Full knowledge base search and management
deepvista-recipe-research-to-recipe — Run a Recipe workflow with research findings
Weekly Installs
17
Repository
deepvista-ai/de…ista-cli
GitHub Stars
5
First Seen
Apr 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass