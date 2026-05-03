---
rating: ⭐⭐
title: obsidian
url: https://skills.sh/steipete/clawdis/obsidian
---

# obsidian

skills/steipete/clawdis/obsidian
obsidian
Installation
$ npx skills add https://github.com/steipete/clawdis --skill obsidian
Summary

Automate Obsidian vault operations and search plain Markdown notes via obsidian-cli.

Requires obsidian-cli binary; install via Homebrew or manually
Core commands: search note names or content with snippets, create notes with optional auto-open, move/rename notes with automatic wikilink and Markdown link updates across the vault, and delete notes
Vaults are standard folders on disk containing .md files, .canvas JSON files, and a .obsidian/ config directory; read the active vault from ~/Library/Application Support/obsidian/obsidian.json rather than hardcoding paths
Set a default vault once with set-default, then use print-default to retrieve it; supports multiple vaults (iCloud, local, work/personal)
SKILL.md
Obsidian

Obsidian vault = a normal folder on disk.

Vault structure (typical)

Notes: *.md (plain text Markdown; edit with any editor)
Config: .obsidian/ (workspace + plugin settings; usually don’t touch from scripts)
Canvases: *.canvas (JSON)
Attachments: whatever folder you chose in Obsidian settings (images/PDFs/etc.)
Find the active vault(s)

Obsidian desktop tracks vaults here (source of truth):

~/Library/Application Support/obsidian/obsidian.json

obsidian-cli resolves vaults from that file; vault name is typically the folder name (path suffix).

Fast “what vault is active / where are the notes?”

If you’ve already set a default: obsidian-cli print-default --path-only
Otherwise, read ~/Library/Application Support/obsidian/obsidian.json and use the vault entry with "open": true.

Notes

Multiple vaults common (iCloud vs ~/Documents, work/personal, etc.). Don’t guess; read config.
Avoid writing hardcoded vault paths into scripts; prefer reading the config or using print-default.
obsidian-cli quick start

Pick a default vault (once):

obsidian-cli set-default "<vault-folder-name>"
obsidian-cli print-default / obsidian-cli print-default --path-only

Search

obsidian-cli search "query" (note names)
obsidian-cli search-content "query" (inside notes; shows snippets + lines)

Create

obsidian-cli create "Folder/New note" --content "..." --open
Requires Obsidian URI handler (obsidian://…) working (Obsidian installed).
Avoid creating notes under “hidden” dot-folders (e.g. .something/...) via URI; Obsidian may refuse.

Move/rename (safe refactor)

obsidian-cli move "old/path/note" "new/path/note"
Updates [[wikilinks]] and common Markdown links across the vault (this is the main win vs mv).

Delete

obsidian-cli delete "path/note"

Prefer direct edits when appropriate: open the .md file and change it; Obsidian will pick it up.

Weekly Installs
1.5K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass