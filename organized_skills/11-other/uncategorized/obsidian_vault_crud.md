---
rating: ⭐⭐
title: obsidian-vault-crud
url: https://skills.sh/richfrem/agent-plugins-skills/obsidian-vault-crud
---

# obsidian-vault-crud

skills/richfrem/agent-plugins-skills/obsidian-vault-crud
obsidian-vault-crud
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill obsidian-vault-crud
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See ./requirements.txt for the dependency lockfile (currently empty — standard library only).

Obsidian Vault CRUD

Status: Active Author: Richard Fremmerlid Domain: Obsidian Integration Depends On: obsidian-markdown-mastery (WP05)

Core Mandate

This skill provides the disk I/O layer for all agent interactions with the Obsidian Vault. It does NOT handle syntax parsing (that belongs to obsidian-markdown-mastery). Instead, it ensures that every file write is:

Atomic — via POSIX os.rename() from a .tmp staging file
Locked — via an advisory .agent-lock file at the vault root
Conflict-aware — via mtime comparison before/after read
Lossless — via ruamel.yaml for frontmatter (never PyYAML)
Available Commands
Read a Note
python ./vault_ops.py read --file <path>

Create a Note
python ./vault_ops.py create --file <path> --content <text> [--frontmatter key=value ...]

Update a Note
python ./vault_ops.py update --file <path> --content <text>

Append to a Note
python ./vault_ops.py append --file <path> --content <text>

Safety Guarantees
Atomic Write Protocol
Write content to <target>.agent-tmp
Verify the .agent-tmp file was written completely
os.rename('<target>.agent-tmp', '<target>') — atomic on POSIX
If any step fails, the .agent-tmp is cleaned up
Advisory Lock Protocol
Before any write batch: create <vault_root>/.agent-lock
After write batch completes: remove .agent-lock
Other agents check for .agent-lock before writing
This is advisory (does not block Obsidian UI)
Concurrent Edit Detection
Capture os.stat(file).st_mtime before reading
Before writing, check st_mtime again
If mtime changed → another process edited the file → ABORT
Frontmatter Handling
Uses ruamel.yaml (NOT PyYAML) to preserve comments, indentation, and array styles
Ensures Dataview and Obsidian Properties remain intact
Weekly Installs
20
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass