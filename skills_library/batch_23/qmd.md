---
title: qmd
url: https://skills.sh/changeflowhq/skills/qmd
---

# qmd

skills/changeflowhq/skills/qmd
qmd
Installation
$ npx skills add https://github.com/changeflowhq/skills --skill qmd
SKILL.md
qmd - Local Search for Knowledge Bases

Search indexed markdown collections using keyword, semantic, or hybrid search.

When to Use
Searching project documentation or knowledge bases
Finding related files before making changes
Discovering context across many markdown files
Answering questions that span multiple documents
Quick Start
# Keyword search (fast, BM25)
qmd search "your query" --json -n 10

# Find related files
qmd search "topic" --files -n 20

# Semantic search (requires embeddings)
qmd vsearch "conceptual question" -n 10

# Hybrid search with reranking (best quality, slower)
qmd query "natural language question" --json -n 10

# Get full document content
qmd get "path/to/file.md" --full

Search Modes
Mode	Command	Speed	Best For
Keyword (BM25)	qmd search	Fast	Exact terms, known keywords
Semantic	qmd vsearch	Medium	Conceptual queries, synonyms
Hybrid	qmd query	Slow	Complex questions needing both
File list	qmd search --files	Fast	Finding all related files
Workflows
Before answering a question
qmd search "relevant keywords" --json -n 10


Review results, then read specific files for full context.

After making changes (update cascade)
qmd search "topic you changed" --files -n 20


Review all related files and update any that reference the changed topic.

Writing content that needs project context
qmd search "positioning voice tone" --json -n 10
qmd search "topic for content" --json -n 10

Index Management
# Update text index (fast, ~1 sec)
qmd update

# Update embeddings (slow, ~3-4 min)
qmd embed

# Check index health
qmd status

# List collections
qmd collection list

Setup & Troubleshooting

If qmd is not installed or broken, run the doctor script:

bash ~/.claude/skills/qmd/scripts/doctor.sh


For full installation and automation setup, see setup/README.md.

For the complete command reference, see references/commands.md.

Tips
Results below score 0.3 are noise - ignore them
qmd search (BM25) is good enough for day-to-day use
Only use vsearch when keywords don't match concepts
After changes, always run --files query to catch ripple effects
Combine with Read tool: qmd finds files, Read gets full content
Self-Learning

Read LEARNED.md before using this skill. It contains hard-won lessons about what works and what doesn't.

Update LEARNED.md when you discover:

A query that returned bad results and what worked instead
Search mode choice that was wrong (e.g. search missed something vsearch found)
Index issues (stale embeddings, missing files, broken binary)
Installation or automation gotchas
CLAUDE.md patterns that worked or failed for enforcing context-first behavior

Consolidation (keep LEARNED.md under 50 lines): Before adding a new entry, check the file length. If it's over 50 lines:

Merge duplicate/overlapping entries into single proven patterns
Remove entries older than 3 months that haven't been reinforced
Drop one-off observations that never recurred
Move detailed historical context to LEARNED-archive.md if worth preserving
Keep only entries that would change behavior - if it's obvious, cut it
Weekly Installs
16
Repository
changeflowhq/skills
GitHub Stars
9
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass