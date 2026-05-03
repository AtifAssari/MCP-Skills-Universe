---
rating: ⭐⭐⭐
title: vault-management
url: https://skills.sh/mwguerra/claude-code-plugins/vault-management
---

# vault-management

skills/mwguerra/claude-code-plugins/vault-management
vault-management
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill vault-management
SKILL.md
Obsidian Vault Management

Manage the Obsidian vault as a developer knowledge base and automatic work journal.

When to Use

Activate this skill when:

User requests note operations (add, search, update, import, link, archive)
Working with project documentation that should be stored in the vault
Auto-capturing commits, tasks, or Claude Code components
User asks about their notes, documentation, or knowledge base
Organizing or finding information in the vault
Vault Structure
~/guerra_vault/
├── projects/              # Project-specific documentation
├── technologies/          # Technology knowledge (Laravel, React, etc.)
├── claude-code/           # Claude Code components
│   ├── agents/
│   ├── hooks/
│   ├── skills/
│   └── tools/
├── ideas/                 # Feature ideas and experiments
├── personal/              # Career and learning goals
├── todo/                  # Tasks and checklists
├── references/            # Bookmarks, snippets, cheatsheets
├── journal/               # Auto-captured events
│   ├── commits/           # Git commit documentation
│   ├── tasks/             # Completed task summaries
│   └── creations/         # Component creation logs
└── _archive/              # Archived notes

Frontmatter Standard

All notes MUST include this YAML frontmatter:

---
title: "Note Title"
description: "Brief description of the content"
tags: [tag1, tag2, category]
related: [[path/to/related-note]]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---


Rules:

title: Descriptive, matches the main heading
description: One sentence explaining the content
tags: Always include the category as a tag
related: Wiki-link format, add related notes when relevant
created: Set once when created
updated: Update whenever the note changes
Available Commands
Command	Purpose
/obsidian-vault:init	Set up vault configuration and structure
/obsidian-vault:add <category> <title>	Create a new note
/obsidian-vault:search <query>	Find notes by title, content, or tags
/obsidian-vault:update <note>	Edit note frontmatter or append content
/obsidian-vault:import <file>	Import external files with frontmatter
/obsidian-vault:list [category]	List notes, optionally by category
/obsidian-vault:tags [--stats]	View tags and usage statistics
/obsidian-vault:link <note1> <note2>	Create bidirectional related links
/obsidian-vault:archive <note>	Move note to archive
Auto-Capture Behavior

The plugin automatically captures:

Git Commits
Creates journal/commits/YYYY-MM-DD-<slug>.md
Includes: commit message, date, project, branch, files changed
Placeholder sections for "What" and "Why" (fill in with context)
Task Completions
Creates journal/tasks/YYYY-MM-DD-<slug>.md
Captures subagent summaries
Includes: summary, what was done, decisions made
Claude Code Components
Creates claude-code/<type>s/<name>.md
Tracks: agents, hooks, skills, tools
Also logs to journal/creations/
Best Practices
Creating Notes
Choose the appropriate category
Use descriptive titles
Add relevant tags immediately
Link to related notes when obvious
Updating Notes
Update the updated date (done automatically by scripts)
Add new related links as connections emerge
Keep descriptions current
Searching
Start broad, narrow with --title, --content, or --tag
Use --category to focus on specific areas
Check related notes for additional context
Organization
Use consistent naming within categories
Archive rather than delete
Maintain bidirectional links
Integration with Workflows
After Completing Features

When finishing a feature or fix:

Ensure commit is captured
Add/update project documentation
Link new notes to project README
When Learning Technologies
Create note in technologies/
Link to projects that use it
Add code snippets as needed
For Ideas and Experiments
Start in ideas/
Move to projects/ when starting implementation
Archive if abandoned
Additional Resources
Reference Files
references/frontmatter-spec.md - Detailed frontmatter specification
Configuration
Config: ~/.claude/obsidian-vault.json
Vault path: ~/guerra_vault
Weekly Installs
21
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