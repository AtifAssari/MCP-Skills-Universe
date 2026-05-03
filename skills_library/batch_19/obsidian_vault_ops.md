---
title: obsidian-vault-ops
url: https://skills.sh/ballred/obsidian-claude-pkm/obsidian-vault-ops
---

# obsidian-vault-ops

skills/ballred/obsidian-claude-pkm/obsidian-vault-ops
obsidian-vault-ops
Installation
$ npx skills add https://github.com/ballred/obsidian-claude-pkm --skill obsidian-vault-ops
SKILL.md
Obsidian Vault Operations Skill

Core operations for reading, writing, and managing files in an Obsidian vault.

Vault Structure
vault-root/
├── CLAUDE.md           # Main context (always read first)
├── Daily Notes/        # YYYY-MM-DD.md format
├── Goals/              # Goal cascade files
├── Projects/           # Project folders with CLAUDE.md
├── Templates/          # Reusable note structures
└── Archives/           # Completed/inactive content

File Operations
Reading Notes
Use Glob to find files: *.md, Daily Notes/*.md
Read CLAUDE.md first for vault context
Check for wiki-links to related notes
Creating Notes
Check if note already exists
Use appropriate template if available
Add YAML frontmatter with date and tags
Insert wiki-links to related notes
Editing Notes
Preserve YAML frontmatter structure
Maintain existing wiki-links
Use consistent heading hierarchy
Apply standard tag format
Wiki-Link Format
[[Note Name]]                    # Simple link
[[Note Name|Display Text]]       # Link with alias
[[Note Name#Section]]            # Link to section

YAML Frontmatter

Standard frontmatter structure:

---
date: 2024-01-15
tags: [tag1, tag2]
status: active
---

Template Variables

When processing templates, replace:

{{date}} - Today's date (YYYY-MM-DD)
{{date:format}} - Formatted date
{{date-1}} - Yesterday
{{date+1}} - Tomorrow
{{time}} - Current time
Common Patterns
Daily Note Creation
Calculate today's date in YYYY-MM-DD format
Check if Daily Notes/{date}.md exists
If not, read Templates/Daily Template.md
Replace template variables
Write to Daily Notes/{date}.md
Finding Related Notes
Extract key terms from current note
Search vault for matching content
Suggest wiki-links to related notes
Tag Operations
Priority: #priority/high, #priority/medium, #priority/low
Status: #active, #waiting, #completed, #archived
Context: #work, #personal, #health, #learning
Best Practices
Always check CLAUDE.md for vault-specific conventions
Preserve existing structure when editing
Use relative paths for internal links
Add frontmatter to new notes
Link to relevant goals when creating tasks
Weekly Installs
48
Repository
ballred/obsidia…aude-pkm
GitHub Stars
1.4K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass