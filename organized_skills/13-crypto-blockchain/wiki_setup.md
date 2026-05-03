---
rating: ⭐⭐⭐
title: wiki-setup
url: https://skills.sh/ar9av/obsidian-wiki/wiki-setup
---

# wiki-setup

skills/ar9av/obsidian-wiki/wiki-setup
wiki-setup
Installation
$ npx skills add https://github.com/ar9av/obsidian-wiki --skill wiki-setup
SKILL.md
Obsidian Setup — Vault Initialization

You are setting up a new Obsidian wiki vault (or repairing an existing one).

Step 1: Create .env

If .env doesn't exist, create it from .env.example. Ask the user for:

Where should the vault live? → OBSIDIAN_VAULT_PATH

Default: ~/Documents/obsidian-wiki-vault
Must be an absolute path (after expansion)

Where are your source documents? → OBSIDIAN_SOURCES_DIR

Can be multiple paths, comma-separated
Default: ~/Documents

Want to import Claude history? → CLAUDE_HISTORY_PATH

Default: auto-discovers from ~/.claude
Set explicitly if Claude data is elsewhere

Have QMD installed? → QMD_WIKI_COLLECTION / QMD_PAPERS_COLLECTION

Optional. Enables semantic search in wiki-query and source discovery in wiki-ingest.
If unsure, skip for now — both skills fall back to Grep automatically.
Install instructions: see .env.example (QMD section).
Step 2: Create Vault Directory Structure
mkdir -p "$OBSIDIAN_VAULT_PATH"/{concepts,entities,skills,references,synthesis,journal,projects,_archives,_raw,.obsidian}

.obsidian/ — Obsidian's own config. Creates vault recognition.
projects/ — Per-project knowledge (populated during ingest).
_archives/ — Stores wiki snapshots for rebuild/restore operations.
_raw/ — Staging area for unprocessed drafts. Drop rough notes here; wiki-ingest will promote them to proper wiki pages and delete the originals.
Step 3: Create Special Files
index.md
---
title: Wiki Index
---

# Wiki Index

*This index is automatically maintained. Last updated: TIMESTAMP*

## Concepts

*No pages yet. Use `wiki-ingest` to add your first source.*

## Entities

## Skills

## References

## Synthesis

## Journal

log.md
---
title: Wiki Log
---

# Wiki Log

- [TIMESTAMP] INIT vault_path="OBSIDIAN_VAULT_PATH" categories=concepts,entities,skills,references,synthesis,journal

hot.md
---
title: Hot Cache
updated: TIMESTAMP
---

# Hot Cache

*A ~500-word semantic snapshot of recent activity. Updated after every major write operation.*

## Recent Activity

- [TIMESTAMP] INIT — vault created at OBSIDIAN_VAULT_PATH

## Active Threads

*None yet — start ingesting sources to populate.*

## Key Takeaways

*None yet.*

## Flagged Contradictions

*None yet.*

Step 4: Create .obsidian Configuration

Create minimal Obsidian config for a good out-of-box experience:

.obsidian/app.json
{
  "strictLineBreaks": false,
  "showFrontmatter": false,
  "defaultViewMode": "preview",
  "livePreview": true
}

.obsidian/appearance.json
{
  "baseFontSize": 16
}

Step 5: Recommend Obsidian Plugins

Tell the user about these recommended community plugins (they install manually):

Dataview — Query page metadata, create dynamic tables. Essential for a wiki.
Graph Analysis — Enhanced graph view for exploring connections.
Templater — If they want to create pages manually using templates.
Obsidian Git — Auto-backup the vault to a git repo.
Step 6: Verify Setup

Run a quick sanity check:

 Vault directory exists with: concepts/, entities/, skills/, references/, synthesis/, journal/, projects/, _archives/, _raw/
 index.md exists at vault root
 log.md exists at vault root
 hot.md exists at vault root
 .env has OBSIDIAN_VAULT_PATH set
 .obsidian/ directory exists
 Source directories (if configured) exist and are readable

Report the results and tell the user they can now:

Open the vault in Obsidian (File → Open Vault → select the directory)
Run wiki-status to see what's available to ingest
Run wiki-ingest to add their first sources
Run claude-history-ingest to mine their Claude conversations
Run codex-history-ingest to mine their Codex sessions (if they use Codex)
Run wiki-status again anytime to check the delta
Weekly Installs
966
Repository
ar9av/obsidian-wiki
GitHub Stars
893
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass