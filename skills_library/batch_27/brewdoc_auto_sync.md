---
title: brewdoc:auto-sync
url: https://skills.sh/kochetkov-ma/claude-brewcode/brewdoc:auto-sync
---

# brewdoc:auto-sync

skills/kochetkov-ma/claude-brewcode/brewdoc:auto-sync
brewdoc:auto-sync
Installation
$ npx skills add https://github.com/kochetkov-ma/claude-brewcode --skill brewdoc:auto-sync
SKILL.md
Auto-Sync
Mode Detection

EXECUTE using Bash tool (args: $ARGUMENTS):

bash "${CLAUDE_SKILL_DIR}/scripts/detect-mode.sh" $ARGUMENTS


Parse output: MODE|ARG|FLAGS. If exit code non-zero → report error, EXIT.

Mode	Trigger	Scope
STATUS	status	Report INDEX state → EXIT
INIT	init <path>	Tag file + add to INDEX → EXIT
GLOBAL	global	~/.claude/** (excludes managed dirs)
PROJECT	empty	.claude/** (excludes managed dirs)
FILE	file path	Single file
FOLDER	folder path	All .md in folder

Managed directories (excluded from auto-scan, explicit path required):

rules/ — sync via /brewdoc:auto-sync .claude/rules
agents/ — sync via /brewdoc:auto-sync .claude/agents
skills/ — sync via /brewdoc:auto-sync .claude/skills
INDEX Format
{"p":"skills/auth/SKILL.md","t":"skill","u":"2026-02-05","pr":"default"}

Field	Description
p	Relative path
t	Type: skill/agent/rule/config/doc
u	Last sync date (YYYY-MM-DD)
pr	Protocol: default/override

Paths: Project .claude/auto-sync/INDEX.jsonl | Global ~/.claude/auto-sync/INDEX.jsonl

Frontmatter Fields

Required (3):

auto-sync: enabled
auto-sync-date: 2026-02-05
auto-sync-type: skill


Optional override (multiline YAML):

auto-sync-override: |
  sources: src/**/*.ts, .claude/agents/*.md
  focus: API endpoints, error handling
  preserve: ## User Notes, ## Custom Config

Override Field

When auto-sync-override: present in frontmatter → INDEX gets pr: "override".

Stored in frontmatter only — never in document body.

Read INDEX.jsonl, verify indexed files exist
Find all .md files in scope
Compare indexed vs found → identify non-indexed
Detect type for non-indexed (discover.sh typed) — output: TYPE|PATH per line
Output report: Indexed (path, type, protocol, last sync, stale), Non-Indexed (path, detected type, reason), Summary (counts)
EXIT

Input: init <path>

Read <path> — if NOT found → error, EXIT
If has auto-sync: enabled → "Already tagged", EXIT
Detect type via discover.sh
Add frontmatter: auto-sync: enabled, auto-sync-date: {today}, auto-sync-type: {type}
Check frontmatter auto-sync-override: → set pr: override|default
Add to INDEX.jsonl
Output: path, type, protocol; EXIT
Sync Mode (PROJECT/GLOBAL/FILE/FOLDER)
Phase 1: Setup INDEX

EXECUTE using Bash tool:

SCOPE="project"  # or "global"
INDEX_DIR=".claude/auto-sync"
[ "$SCOPE" = "global" ] && INDEX_DIR="$HOME/.claude/auto-sync"
mkdir -p "$INDEX_DIR" && INDEX_FILE="$INDEX_DIR/INDEX.jsonl" && touch "$INDEX_FILE"
echo "INDEX=$INDEX_FILE"

Phase 2: Discover + Queue (load config: INTERVAL_DAYS, PARALLEL_AGENTS from .claude/tasks/cfg/brewdoc.config.json)
Find tagged files — EXECUTE using Bash tool:
bash "${CLAUDE_SKILL_DIR}/scripts/discover.sh" "$SCOPE_PATH" typed


Output: TYPE|PATH per line (types: skill, agent, rule, config, doc). Capped at MAX_FILES (default 50).

For each file not in INDEX → auto-add:

Read file, use type from discover output
If no frontmatter → add auto-sync: enabled, auto-sync-date, auto-sync-type
Check <auto-sync-override> → set pr
Add to INDEX (index-ops.sh add)

Find stale entries — EXECUTE using Bash tool:

bash "${CLAUDE_SKILL_DIR}/scripts/index-ops.sh" stale "$INDEX_FILE" "$INTERVAL_DAYS"

Queue: new + stale files
Phase 3: Process + Report

Launch bd-auto-sync-processor agents (max PARALLEL_AGENTS batches, model="sonnet"):

Task(subagent_type="brewdoc:bd-auto-sync-processor",
     prompt="PATH: {path} | TYPE: {type} | FLAGS: {flags}")


Context: BD_PLUGIN_ROOT is injected into agent prompt by pre-task.mjs hook.

For each result:

If status = updated or unchanged → update INDEX u to today (index-ops.sh update)
If status = error → log to Errors table, do NOT update INDEX (file remains stale for retry)

Output report:

## Auto-Sync Complete

| Metric | Count |
|--------|-------|
| Discovered | {N} |
| Queued (stale/new) | {N} |
| Updated | {N} |
| Unchanged | {N} |
| Errors | {N} |

### Updated
| Path | Type | Changes |
|------|------|---------|

### Errors
| Path | Error |
|------|-------|

Error Handling
Error	Action
INDEX corrupt	Rebuild from discovery
File not found	Skip, add to errors
Agent timeout	Retry once
No tagged files	Report "0 found"
/brewdoc:doc called	"Use /brewdoc:auto-sync"
Weekly Installs
14
Repository
kochetkov-ma/cl…brewcode
GitHub Stars
25
First Seen
Mar 2, 2026