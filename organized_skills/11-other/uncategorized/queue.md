---
rating: ⭐⭐⭐
title: queue
url: https://skills.sh/mwguerra/claude-code-plugins/queue
---

# queue

skills/mwguerra/claude-code-plugins/queue
queue
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill queue
SKILL.md
Article Queue

Manage the article queue stored in the SQLite database (.article_writer/article_writer.db).

Data Access

All data is stored in the articles table of the SQLite database. Use the provided scripts for all operations:

# Queue summary
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/queue.ts status

# List articles (with filters)
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/queue.ts list [filter]

# Show article details
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/queue.ts show <id>

# Stats and operations
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/article-stats.ts --summary
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/article-stats.ts --get <id>
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/article-stats.ts --set-status <status> <id>

Schema Reference

See references/schema-reference.md for fields.

Key Fields
Author Reference

Articles reference authors via author_id, author_name, and author_languages columns:

{
  "author_id": "mwguerra",
  "author_name": "MW Guerra",
  "author_languages": ["pt_BR", "en_US"]
}


If author not specified, the default author (lowest sort_order) is used.

Output Files (per language)
{
  "output_folder": "content/articles/2025_01_15_rate-limiting/",
  "output_files": [
    {
      "language": "pt_BR",
      "path": "content/articles/2025_01_15_rate-limiting/rate-limiting.pt_BR.md",
      "translated_at": "2025-01-15T14:00:00Z"
    },
    {
      "language": "en_US",
      "path": "content/articles/2025_01_15_rate-limiting/rate-limiting.en_US.md",
      "translated_at": "2025-01-15T16:00:00Z"
    }
  ]
}

Timestamps
created_at: When task was added to queue
written_at: When primary article was completed
published_at: When article went live
updated_at: Last modification
Operations
Status Summary
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/queue.ts status

Filter by Author
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/queue.ts list author:mwguerra

Filter by Language
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/queue.ts list lang:en_US

Update After Writing
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/queue.ts update <id> status:draft

Add Translation

Update the output_files JSON column with additional language entries.

Status Flow
pending -> in_progress -> draft -> review -> published
               |
           archived

Default Author

When adding tasks without author:

Query default author: SELECT * FROM authors ORDER BY sort_order ASC LIMIT 1
Store author_id, author_name, author_languages in article record
Validation

Before processing:

Verify author_id exists in authors table
Validate languages are subset of author's languages
Check all required fields present
Weekly Installs
19
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass