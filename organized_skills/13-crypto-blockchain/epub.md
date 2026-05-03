---
rating: ⭐⭐⭐
title: epub
url: https://skills.sh/aliceisjustplaying/claude-resources-monorepo/epub
---

# epub

skills/aliceisjustplaying/claude-resources-monorepo/epub
epub
Installation
$ npx skills add https://github.com/aliceisjustplaying/claude-resources-monorepo --skill epub
SKILL.md
EPUB Reader Skill

Read EPUB ebook files and extract content as clean Markdown.

Instructions

Use the epub-reader CLI tool to interact with EPUB files. The tool is located at: ~/.claude/skills/epub/scripts/epub-reader/dist/index.js

Available Commands
1. View Metadata

Get book information (title, author, publisher, date, description).

node ~/.claude/skills/epub/scripts/epub-reader/dist/index.js metadata "<path-to-epub>"

2. List Table of Contents

View all chapters and their structure. Each entry shows [ch: N] indicating the chapter number to use with the chapter command.

node ~/.claude/skills/epub/scripts/epub-reader/dist/index.js toc "<path-to-epub>"

3. Read Specific Chapter

Read a single chapter by number (1-indexed).

node ~/.claude/skills/epub/scripts/epub-reader/dist/index.js chapter "<path-to-epub>" <chapter-number>

4. Read Entire Book

Extract the complete book as Markdown.

node ~/.claude/skills/epub/scripts/epub-reader/dist/index.js full "<path-to-epub>"

5. Search Text

Find text occurrences with surrounding context.

node ~/.claude/skills/epub/scripts/epub-reader/dist/index.js search "<path-to-epub>" "<search-query>"

Recommended Workflow
Start with metadata to understand what book you're working with
View the TOC to see available chapters and structure
Read specific chapters for targeted analysis, or use full for complete extraction
Use search to find specific topics, quotes, or references
Open-Ended Search

For broad or conceptual queries like "what are the main themes in this book?" or "find all references to the protagonist's childhood", use query expansion:

Expand the query into multiple specific search terms using domain knowledge
Example: "protagonist's childhood" → search for character name, "young", "childhood", "memory", "father", "mother", "grew up", etc.
Run searches in parallel for each expanded term
Synthesize results by deduplicating and consolidating findings across searches

This approach leverages Claude's domain knowledge to catch synonyms, related concepts, and terminology variations that a simple keyword search would miss.

Example

User asks: "What does the book say about the author's research methodology?"

Expand to searches:

"methodology"
"research"
"study"
"analysis"
"data"
"findings"
"evidence"

Then consolidate the results into a comprehensive answer.

Output Format

All output is clean Markdown:

Headings preserved as #, ##, etc.
Lists, links, and emphasis converted properly
Excessive whitespace cleaned up
Chapter separators included for full extraction
Examples
# What book is this?
node ~/.claude/skills/epub/scripts/epub-reader/dist/index.js metadata "/path/to/book.epub"

# Show me the chapters
node ~/.claude/skills/epub/scripts/epub-reader/dist/index.js toc "/path/to/book.epub"

# Read chapter 3
node ~/.claude/skills/epub/scripts/epub-reader/dist/index.js chapter "/path/to/book.epub" 3

# Find all mentions of "democracy"
node ~/.claude/skills/epub/scripts/epub-reader/dist/index.js search "/path/to/book.epub" "democracy"

Notes
Chapter numbers are 1-indexed (first chapter is 1, not 0)
Use the [ch: N] reference from the TOC output to find the correct chapter number
Paths with spaces must be quoted
Large books may produce substantial output with the full command
Search results show up to 5 matches per chapter with context
Weekly Installs
89
Repository
aliceisjustplay…monorepo
GitHub Stars
4
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass