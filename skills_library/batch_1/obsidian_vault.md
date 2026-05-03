---
title: obsidian-vault
url: https://skills.sh/mattpocock/skills/obsidian-vault
---

# obsidian-vault

skills/mattpocock/skills/obsidian-vault
obsidian-vault
Installation
$ npx skills add https://github.com/mattpocock/skills --skill obsidian-vault
SKILL.md
Obsidian Vault
Vault location

/mnt/d/Obsidian Vault/AI Research/

Mostly flat at root level.

Naming conventions
Index notes: aggregate related topics (e.g., Ralph Wiggum Index.md, Skills Index.md, RAG Index.md)
Title case for all note names
No folders for organization - use links and index notes instead
Linking
Use Obsidian [[wikilinks]] syntax: [[Note Title]]
Notes link to dependencies/related notes at the bottom
Index notes are just lists of [[wikilinks]]
Workflows
Search for notes
# Search by filename
find "/mnt/d/Obsidian Vault/AI Research/" -name "*.md" | grep -i "keyword"

# Search by content
grep -rl "keyword" "/mnt/d/Obsidian Vault/AI Research/" --include="*.md"


Or use Grep/Glob tools directly on the vault path.

Create a new note
Use Title Case for filename
Write content as a unit of learning (per vault rules)
Add [[wikilinks]] to related notes at the bottom
If part of a numbered sequence, use the hierarchical numbering scheme
Find related notes

Search for [[Note Title]] across the vault to find backlinks:

grep -rl "\\[\\[Note Title\\]\\]" "/mnt/d/Obsidian Vault/AI Research/"

Find index notes
find "/mnt/d/Obsidian Vault/AI Research/" -name "*Index*"

Weekly Installs
4.5K
Repository
mattpocock/skills
GitHub Stars
53.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass