---
rating: ⭐⭐⭐
title: search-memory
url: https://skills.sh/nowledge-co/community/search-memory
---

# search-memory

skills/nowledge-co/community/search-memory
search-memory
Installation
$ npx skills add https://github.com/nowledge-co/community --skill search-memory
Summary

Search your personal knowledge base to surface relevant past insights, decisions, and solutions.

Proactively searches durable knowledge and conversation history when context suggests prior work would improve the response
Distinguishes between memory searches (nmem m search) for stored breakthroughs and thread searches (nmem t search) for exact session history
Recognizes trigger patterns: user references to prior fixes, resumed features, debugging similarities, requests for rationale, and ambiguous results needing historical context
Supports progressive inspection of threaded results with configurable limits and content boundaries to retrieve only what's needed
SKILL.md
Search Memory
When to Search (Autonomous Recognition)

Strong signals:

Continuity: Current topic connects to prior work
Pattern match: Problem resembles past solved issue
Decision context: "Why/how we chose X" implies documented rationale
Recurring theme: Topic discussed in past sessions
Implicit recall: "that approach", "like before"

Contextual signals:

Complex debugging (may match past root causes)
Architecture discussion (choices may be documented)
Domain-specific question (conventions likely stored)

Skip when:

Fundamentally new topic
Generic syntax questions
Fresh perspective explicitly requested
Tool Usage

Use nmem CLI with --json flag for programmatic search:

# Basic search
nmem --json m search "3-7 core concepts"

# With filters
nmem --json m search "API design" --importance 0.8

# With labels (multiple labels use AND logic)
nmem --json m search "authentication" -l backend -l security

# With time filter
nmem --json m search "meeting notes" -t week


If the runtime already knows the active project or agent lane, add --space "<space name>".

Query: Extract semantic core, preserve terminology, multi-language aware

Filters:

--importance MIN: Minimum importance score (0.0-1.0)
-l, --label LABEL: Filter by label (can specify multiple)
-t, --time RANGE: Time filter (today, week, month, year)
-n NUM: Limit number of results (default: 10)

JSON Response: Parse memories array, check score field for relevance

Use thread search when the user is really asking about a prior conversation, previous session, or exact discussion:

nmem --json t search "query" --limit 5


If a memory result includes source_thread or thread search finds the likely conversation, inspect it progressively instead of loading the whole thread at once:

nmem --json t show <thread_id> --limit 8 --offset 0 --content-limit 1200


Increase --offset only when more messages are actually needed.

Scores: 0.6-1.0 direct | 0.3-0.6 related | <0.3 skip

Examples:

# Search with importance filter
nmem --json m search "database optimization" --importance 0.7

# Search with multiple labels
nmem --json m search "React patterns" -l frontend -l react

# Search recent memories
nmem --json m search "bug fix" -t week -n 5

Response

Found: Synthesize, cite when helpful None: State clearly, suggest distilling if current discussion valuable

Troubleshooting

If nmem is not in PATH: pip install nmem-cli

For remote servers: run nmem config client set url https://... and nmem config client set api-key ... once on this machine.

Run /status to check server connection.

Weekly Installs
525
Repository
nowledge-co/community
GitHub Stars
73
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass