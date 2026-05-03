---
title: obsidian-skills
url: https://skills.sh/founderjourney/claude-skills/obsidian-skills
---

# obsidian-skills

skills/founderjourney/claude-skills/obsidian-skills
obsidian-skills
Installation
$ npx skills add https://github.com/founderjourney/claude-skills --skill obsidian-skills
SKILL.md
Obsidian Skills

Agent skills for creating and editing Obsidian-compatible plain text files, following the Agent Skills specification.

When to Use This Skill
Creating Obsidian notes with proper formatting
Building knowledge bases with wikilinks
Creating canvas files for visual organization
Working with Obsidian Bases (databases)
Managing PKM (Personal Knowledge Management) systems
Zettelkasten-style note-taking
Supported File Types
1. Obsidian Flavored Markdown (.md)

Standard markdown with Obsidian extensions:

# Note Title

Regular markdown content with [[wikilinks]] to other notes.

## Features

- [[Internal Links]]
- [[Links with Alias|Custom Text]]
- ![[Embedded Notes]]
- ![[image.png]]
- #tags and #nested/tags
- ^block-references
- %%comments%%

## Frontmatter

---
title: Note Title
date: 2025-01-12
tags: [tag1, tag2]
aliases: [alias1, alias2]
---

2. Obsidian Bases (.base)

Database-like views for notes:

{
  "type": "base",
  "version": 1,
  "name": "Projects Database",
  "source": "folder:Projects",
  "columns": [
    {"name": "Name", "type": "text", "property": "file.name"},
    {"name": "Status", "type": "select", "property": "status"},
    {"name": "Due Date", "type": "date", "property": "due"},
    {"name": "Priority", "type": "number", "property": "priority"}
  ],
  "filters": [
    {"property": "status", "operator": "!=", "value": "done"}
  ],
  "sorts": [
    {"property": "due", "direction": "asc"}
  ]
}

3. JSON Canvas (.canvas)

Visual canvas for spatial organization:

{
  "nodes": [
    {
      "id": "1",
      "type": "text",
      "text": "Main Idea",
      "x": 0,
      "y": 0,
      "width": 200,
      "height": 100
    },
    {
      "id": "2",
      "type": "file",
      "file": "Notes/Related Note.md",
      "x": 300,
      "y": 0,
      "width": 200,
      "height": 100
    }
  ],
  "edges": [
    {
      "id": "e1",
      "fromNode": "1",
      "toNode": "2",
      "label": "relates to"
    }
  ]
}

Common Tasks
Create a New Note
Create an Obsidian note about [topic]
Include: frontmatter, sections, relevant links

Build a MOC (Map of Content)
Create a Map of Content for [topic]
Link to: existing notes in vault
Structure: hierarchical with categories

Create a Daily Note
Create daily note for today
Include: tasks, meetings, notes sections
Template: my-daily-template

Design a Canvas
Create a canvas for [project/concept]
Nodes: key ideas, files, images
Connections: relationships between nodes

Create a Database View
Create a Base for tracking [items]
Columns: [properties to track]
Filters: [criteria]
Sort: [ordering]

Obsidian Syntax Reference
Links
Syntax	Description
[[Note]]	Internal link
[[Note|Alias]]	Link with alias
[[Note#Heading]]	Link to heading
[[Note#^block]]	Link to block
![[Note]]	Embed note
![[image.png]]	Embed image
Tags
Syntax	Description
#tag	Simple tag
#parent/child	Nested tag
tags: [a, b]	Frontmatter tags
Callouts
> [!note] Title
> Content

> [!warning] Important
> Warning content

> [!tip] Pro tip
> Helpful information

Tasks
- [ ] Incomplete task
- [x] Completed task
- [ ] Task with [[link]]
- [ ] Task #tag
- [ ] Task 📅 2025-01-12

Dataview Queries
```dataview
TABLE status, due
FROM "Projects"
WHERE status != "done"
SORT due ASC


## Templates

### Note Template

```markdown
---
created: {{date}}
tags: []
---

# {{title}}

## Overview


## Details


## Related
-

Meeting Note
---
date: {{date}}
attendees: []
type: meeting
---

# Meeting: {{title}}

## Attendees
-

## Agenda
1.

## Notes


## Action Items
- [ ]

Integration with PKM Systems
Zettelkasten
# 202501121030 Atomic Note Title

Brief atomic concept.

## Links
- [[202501121025 Related Concept]]
- [[202501121035 Another Idea]]

## References
- Source material

PARA Method
/vault
├── 1 Projects/
├── 2 Areas/
├── 3 Resources/
└── 4 Archive/

Best Practices
Atomic Notes: One idea per note
Descriptive Titles: Clear, searchable names
Liberal Linking: Connect related concepts
Consistent Frontmatter: Use templates
Regular Review: Maintain connections
Credits

Created by kepano (Steph Ango, CEO of Obsidian). Licensed under MIT.

Weekly Installs
86
Repository
founderjourney/…e-skills
GitHub Stars
10
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass