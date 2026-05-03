---
title: deepvista-vistabase
url: https://skills.sh/deepvista-ai/deepvista-cli/deepvista-vistabase
---

# deepvista-vistabase

skills/deepvista-ai/deepvista-cli/deepvista-vistabase
deepvista-vistabase
Installation
$ npx skills add https://github.com/deepvista-ai/deepvista-cli --skill deepvista-vistabase
SKILL.md
VistaBase

PREREQUISITE: Read deepvista-shared for auth, profiles, and global flags.

VistaBase is DeepVista's knowledge base — a collection of context cards that represent people, organizations, topics, notes, files, and more. Cards have vector embeddings for semantic search and keyword indexing for precise lookups.

CRUD Commands
list
deepvista --profile local vistabase list [--type TYPE] [--status STATUS] [--limit N] [--page N] [--order-by FIELD] [--order DIR]

Flag	Required	Default	Description
--type	No	all	Card type filter
--status	No	all	pinned, archived, or normal
--limit	No	20	Max results
--page	No	1	Page number
--order-by	No	—	created_at or updated_at
--order	No	—	asc or desc
get
deepvista --profile local vistabase get <card_id>

create
deepvista --profile local vistabase create --type TYPE --title "Title" [--content "Description"] [--tags '["t1","t2"]'] [--no-enrich]


[!CAUTION] Write command — confirm with user before executing.

update
deepvista --profile local vistabase update <card_id> [--title "..."] [--content "..."] [--type TYPE] [--tags '["t1"]'] [--status pinned|archived]


[!CAUTION] Write command — confirm with user before executing.

delete
deepvista --profile local vistabase delete <card_id> [--type TYPE]


[!CAUTION] Destructive command — confirm with user before executing.

Helper Commands
+search
deepvista --profile local vistabase +search "query text" [--type TYPE] [--limit N]


Search across all context cards using hybrid vector + keyword search.

Flag	Required	Default	Description
<query>	Yes	—	Search query (natural language)
--type	No	all	Filter by card type
--limit	No	10	Max results

Read-only. Results include relevance scores from hybrid search (vector similarity + keyword matching). Use vistabase get <id> to read the full content of a result.

+similar
deepvista --profile local vistabase +similar <card_id> [--limit N]


Find context cards semantically similar to a given card. Uses the source card's content as a search query.

Flag	Required	Default	Description
<card_id>	Yes	—	Source card to find similar cards for
--limit	No	5	Max results

Read-only. The source card is excluded from results. Useful for discovering related knowledge you may not have thought to search for.

+pin
deepvista --profile local vistabase +pin <card_id>


[!CAUTION] Write command.

+archive
deepvista --profile local vistabase +archive <card_id>


[!CAUTION] Write command.

Card Types

person, organization, message, todo, topic, keypoint, file, note, vistabook, vistabook_run

Examples
# Search for anything about quarterly metrics
deepvista --profile local vistabase +search "quarterly metrics"

# Find people related to a topic
deepvista --profile local vistabase +search "machine learning team" --type person

# Find cards similar to a specific card
deepvista --profile local vistabase +similar card_abc123 --limit 10

# List all people cards
deepvista --profile local vistabase list --type person

# Create a topic card
deepvista --profile local vistabase create --type topic --title "Machine Learning Strategy" --content "Our approach to ML..."

# Pin an important card
deepvista --profile local vistabase +pin abc123

# Get full details of a card
deepvista --profile local vistabase get abc123

See Also
deepvista-shared — Auth and global flags
deepvista-notes — Notes (subset of vistabase)
Weekly Installs
22
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