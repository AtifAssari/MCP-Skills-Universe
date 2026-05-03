---
title: notebooklm
url: https://skills.sh/sanjay3290/ai-skills/notebooklm
---

# notebooklm

skills/sanjay3290/ai-skills/notebooklm
notebooklm
Installation
$ npx skills add https://github.com/sanjay3290/ai-skills --skill notebooklm
SKILL.md
NotebookLM Skill

Query NotebookLM notebooks and manage notebooks/sources via Playwright browser automation.

All commands run from the skill directory. All scripts output JSON to stdout and exit 1 on error. Use --help on any script for full flag reference.

Workflow
Authenticate: python scripts/auth_manager.py setup --profile <name>
Register notebook: python scripts/notebook_manager.py add --url <url> --name <name> --description <desc> --topics <topics>
Ask questions: python scripts/ask_question.py --question "..." --notebook-id <id>
Manage sources: python scripts/remote_manager.py add-source|sync-sources ...
Key Behaviors
Runs headless by default; use --show-browser for debugging only.
Persistent Chrome profiles stored at ~/.config/claude/notebooklm-skill/ (override with NOTEBOOKLM_DATA_DIR).
Hash-based dedupe: file uploads skip unchanged sources automatically.
--dry-run available on all destructive/bulk operations (create, add-source, delete-source, sync-sources).
--retries N retries transient browser failures with screenshot/HTML artifact capture.
Batch mode (--questions "q1||q2||q3") and multi-notebook comparison (--compare-notebook-ids) supported.
Exports to JSON or Markdown via --export-format markdown --save-notes.
Answers include a follow-up reminder prompting Claude to ask clarifying questions before replying.
Quick Reference
# Auth
python scripts/auth_manager.py setup --profile work
python scripts/auth_manager.py status --profile work

# Library
python scripts/notebook_manager.py add --url "..." --name "..." --description "..." --topics "..."
python scripts/notebook_manager.py list

# Ask
python scripts/ask_question.py --question "..." --notebook-id <id>
python scripts/ask_question.py --questions "q1||q2" --notebook-id <id>

# Sources
python scripts/remote_manager.py add-source --notebook-id <id> --dir ./docs --recursive
python scripts/remote_manager.py sync-sources --notebook-id <id> --dir ./docs --recursive --delete-missing --dry-run


For full command reference with all flags and examples, see references/commands.md.

Weekly Installs
148
Repository
sanjay3290/ai-skills
GitHub Stars
246
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn