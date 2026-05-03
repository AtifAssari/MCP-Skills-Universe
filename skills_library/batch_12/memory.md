---
title: memory
url: https://skills.sh/johnlindquist/claude/memory
---

# memory

skills/johnlindquist/claude/memory
memory
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill memory
SKILL.md
Memory - Persistent Knowledge Storage

Store and retrieve knowledge across sessions using semantic search.

Prerequisites

Install basic-memory:

pip install basic-memory

CLI Reference
Write a Note
# Basic note
basic-memory tool write-note --title "Note Title" --content "Note content in markdown"

# With tags
basic-memory tool write-note --title "React Patterns" --content "# Content here" --tags "react,patterns,frontend"

# To specific folder
basic-memory tool write-note --title "Meeting Notes" --content "# Notes" --folder "meetings"

# With specific project
basic-memory tool write-note --title "Project Notes" --content "# Notes" --project myproject

Read a Note
# By identifier/permalink
basic-memory tool read-note "note-title"

# From specific project
basic-memory tool read-note "note-title" --project myproject

Search Memories
# Semantic search (query is positional)
basic-memory tool search-notes "your search query"

# Limit results
basic-memory tool search-notes "react hooks" --page-size 10

# Search by permalink
basic-memory tool search-notes "pattern" --permalink

# Search by title
basic-memory tool search-notes "meeting" --title

# Filter by date
basic-memory tool search-notes "feature" --after_date "7d"

# With specific project
basic-memory tool search-notes "authentication" --project myproject

Build Context for a Topic
# Get related notes for a URL/topic (URL is positional)
basic-memory tool build-context "memory://topic/authentication"

# With depth and timeframe
basic-memory tool build-context "memory://note/my-note" --depth 2 --timeframe 30d

# With specific project
basic-memory tool build-context "memory://topic/api" --project myproject

List Recent Activity
# Default (depth 1, 7 days)
basic-memory tool recent-activity

# With depth
basic-memory tool recent-activity --depth 3

# With timeframe
basic-memory tool recent-activity --timeframe 30d

# Combined
basic-memory tool recent-activity --depth 3 --timeframe 14d

Continue Conversation
# Get prompt to continue previous work
basic-memory tool continue-conversation "previous topic or context"

Sync Database
basic-memory sync

Check Status
basic-memory status

Note Format

Notes are stored as markdown with YAML frontmatter:

---
title: My Note
tags: [tag1, tag2]
created: 2024-01-15
---

# My Note

Content here in markdown format.

## Sections

More content...

Workflow Patterns
Save Learning

When you discover something useful:

basic-memory tool write-note \
  --title "TypeScript Utility Types" \
  --content "# Utility Types\n\n- Partial<T> - Makes all properties optional\n- Required<T> - Makes all properties required\n- Pick<T, K> - Picks specific properties" \
  --tags "typescript,types,reference"

Save Decision

When making an architectural decision:

basic-memory tool write-note \
  --title "Auth Strategy Decision" \
  --content "# Decision: Use JWT for API auth\n\n## Context\n...\n\n## Decision\n...\n\n## Consequences\n..." \
  --tags "architecture,auth,decision" \
  --folder "decisions"

Retrieve Context

Before starting related work:

# Search for relevant notes
basic-memory tool search-notes "authentication jwt tokens"

# Or build comprehensive context
basic-memory tool build-context "memory://topic/api-authentication"

Review Recent Work
basic-memory tool recent-activity --depth 5 --timeframe 7d

Use Cases
Personal Wiki
Store code snippets and patterns
Document project decisions
Keep reference material
Learning Log
Record things you learn
Tag by topic for later retrieval
Build knowledge over time
Project Context
Save project-specific knowledge
Retrieve relevant context at session start
Share knowledge across sessions
Best Practices
Use meaningful titles - They become permalinks
Add tags - Improves search and organization
Use markdown - Full markdown support in content
Organize with folders - Group related notes
Search before writing - Check if knowledge already exists
Keep notes focused - One topic per note
Update, don't duplicate - Revise existing notes
Integration Pattern
Session Start
# Get context for today's work
basic-memory tool build-context "memory://topic/feature-youre-building"

During Work
# Save discoveries
basic-memory tool write-note --title "Discovery Title" --content "What I learned"

Session End
# Sync to ensure persistence
basic-memory sync

Weekly Installs
248
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass