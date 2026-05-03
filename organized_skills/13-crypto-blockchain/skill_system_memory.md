---
rating: ⭐⭐⭐
title: skill-system-memory
url: https://skills.sh/arthur0824hao/skills/skill-system-memory
---

# skill-system-memory

skills/arthur0824hao/skills/skill-system-memory
skill-system-memory
Installation
$ npx skills add https://github.com/arthur0824hao/skills --skill skill-system-memory
SKILL.md
Skill System Memory (PostgreSQL)

Persistent shared memory for all AI agents. PostgreSQL 14+ on Linux or Windows. Memory failures look like intelligence failures — this skill ensures the right memory is retrieved at the right time.

Contract notes:

Module-first: mem.py and MCP tooling are the primary runtime surface.
Plugin optional: OpenCode plugin integration is an adapter layer, not a required dependency.
Prefer project-scoped DB naming: <project>-memory (for example skills-memory).
DB Targeting — Project Isolation

Skills are installed globally but memory is project-scoped. Isolation is at the database level: each project gets its own PostgreSQL database named <project>-memory.

Cross-DB recall is an explicit read-side feature, not a default mode. Search and context reads stay on the current memory DB unless the caller opts in with scope=all or cross_db=true. All write paths remain pinned to the local SKILL_PGDATABASE target.

Search Path Role Architecture (SK-C)

The compatible rollout path is additive:

legacy mode remains DB-per-project via SKILL_PGDATABASE=<project>-memory
shared-DB mode uses an explicit shared DB plus schema isolation
runtime roles are split into admin, connector, and visitor_<identity>

Role model:

admin: migration/init only; creates schemas, grants, and roles
connector: CONNECT-only credential; opens the DB connection and immediately SET ROLEs
visitor_<identity>: daily query role with enforced search_path

Visitor search_path matrix:

visitor_hermes: ep_scope, sk_scope, fd_scope, work_scope, public
visitor_atlas: ep_scope, public
visitor_athena: sk_scope, public
visitor_fd_coder: fd_scope, public
visitor_ep_coder: ep_scope, public
visitor_sk_coder: sk_scope, public
visitor_hephaestion: work_scope, sk_scope, public

Shared-DB mode is explicit and backward-compatible:

SKILL_PGSHARED_DB=<shared-db-name> selects the shared DB
SKILL_PGSCHEMA=<scope-schema> selects the local writable schema
SKILL_PGDATABASE remains valid for legacy DB-per-project mode

Runtime flow in shared-DB mode:

connect as connector
SET ROLE visitor_<identity>
rely on the visitor search_path for scoped queries
allow Hermes-only explicit override for all-scopes audit queries

Shared-DB examples:

# Provision shared DB schemas/roles for SK scope
python3 scripts/mem.py init-project \
  --project-id sk \
  --db-name shared-memory \
  --schema-name sk_scope \
  --shared-db-mode

# Run local SK queries through shared DB scope
SKILL_PGSHARED_DB=shared-memory \
SKILL_PGSCHEMA=sk_scope \
SKILL_VISITOR_ROLE=visitor_sk_coder \
python3 scripts/mem.py search "router policy"

# Hermes explicit all-scopes audit across the shared DB
SKILL_PGSHARED_DB=shared-memory \
SKILL_PGSCHEMA=sk_scope \
SKILL_VISITOR_ROLE=visitor_hermes \
python3 scripts/mem.py search "friction skill-system-comms" --all-scopes

Cross-DB Visibility Contract
visibility=private (default): searchable only inside the DB where the memory lives; legacy rows without visibility read as private
visibility=shared: searchable across configured memory DBs when federation is explicit
visibility=global: searchable across configured memory DBs and eligible for cross-DB auto context injection
Cross-DB results must include source_db
Cross-DB ranking uses normalized fusion (RRF-style), not raw per-DB score comparison
Known DB fan-out targets are configured in config/insight.yaml under memory.cross_db_targets
All mutation paths (store, update, delete, purge) stay local to the active SKILL_PGDATABASE target even when read-side cross-DB federation is enabled
Auto-detection (preferred)

When no env vars are set, the DB name is auto-derived from the project directory name:

Plugin (JS): uses directory passed by OpenCode host → last path segment → <dir>-memory
mem.py CLI: uses script's root directory or cwd → <dir>-memory
MCP server: uses Path.cwd() at startup → <dir>-memory

Do NOT set SKILL_PGDATABASE globally. It overrides auto-detection for ALL projects.

# WRONG — breaks project isolation
export SKILL_PGDATABASE=skills-memory   # every project now hits skills-memory

# RIGHT — let auto-detection work (no env var needed)
cd /path/to/FraudDetect && opencode      # → FraudDetect-memory
cd /path/to/skills && opencode           # → skills-memory

Per-project override (when needed)

If you must override, set SKILL_PGDATABASE at project level, not globally:

In project's .opencode config or launch script
In project's .env file (if your host reads it)
As a prefix to the command: SKILL_PGDATABASE=FraudDetect-memory opencode
Fail-closed policy

If PGDATABASE is set but SKILL_PGDATABASE is not, all entry points refuse to connect. This prevents accidental cross-project memory pollution.

MCP server path for multi-project setups

When skills are globally installed at ~/.agents/skills/, configure MCP with the absolute path to the global install:

{
  "skill-system-memory": {
    "command": "python3",
    "args": ["~/.agents/skills/skill-system-memory/mcp/server.py"]
  }
}


Do NOT use relative paths like skills/skill-system-memory/mcp/server.py — they break in projects that don't have a local skills/ directory.

Quick Start

Database <project>-memory and all functions are created by init.sql in this skill directory. The current supported-now runtime surface covers core memory, typed context reads, the typed evolution ledger, and doctor/compaction support. Session/project/context projection tables and behavior graph refresh remain optional capability-gated surfaces, not unconditional runtime guarantees.

# Linux — replace 'postgres' with your PostgreSQL superuser if different (e.g. your system username)
psql -U postgres -c "CREATE DATABASE <project>-memory;"
psql -U postgres -d <project>-memory -f init.sql

# Windows (adjust path to your psql.exe; replace 'postgres' with your PG superuser if needed)
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -c "CREATE DATABASE <project>-memory;"
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d <project>-memory -f init.sql


Note: If your PostgreSQL installation does not have a postgres role, use your actual PostgreSQL superuser name. On many Linux distros this matches your OS username. You can override at any time by setting PGUSER before running scripts: export PGUSER=your_pg_username (Linux/macOS) or $env:PGUSER = "your_pg_username" (PowerShell).

Verify: SELECT * FROM memory_health_check();

MCP Server (Phase 6.1)

This skill includes an MCP (Model Context Protocol) server that exposes memory operations as agent tools.

MCP Server Setup
# Install dependencies
cd skills/skill-system-memory/mcp
pip install -r requirements.txt

# Verify installation
python server.py --help

# Run with stdio transport (default)
python server.py

# Run with SSE transport (for remote access)
MCP_TRANSPORT=sse MCP_PORT=8000 python server.py

# Or via MCP CLI
mcp dev server.py

MCP Environment Variables
Variable	Default	Description
SKILL_PGDATABASE	<project>-memory	Legacy DB-per-project PostgreSQL database name
SKILL_PGSHARED_DB	(unset)	Shared PostgreSQL database name for search_path mode
SKILL_PGSCHEMA	(unset)	Local writable schema for search_path mode
PGHOST	localhost	PostgreSQL host
PGPORT	5432	PostgreSQL port
PGUSER	(optional)	PostgreSQL user
MCP_TRANSPORT	stdio	Transport mode (stdio or sse)
MCP_PORT	8000	Port for SSE transport
MCP Tools
Tool	Description
memory_search	Search memories by natural language query (hybrid: FTS + trigram + pgvector)
memory_store	Store a new memory with auto-deduplication and local-only write isolation
memory_update	Update selected fields on a local memory row by id with audit logging
memory_delete	Soft-delete a local memory row by id with audit logging
memory_purge	Hard-delete a local memory row only with explicit authorization
memory_auto_match	Auto-match memories against input text + write to .sisyphus/tmp/mem-{session}.md
memory_context	Get user context (soul state, preferences, recent facets)
memory_status	Check memory system health (connection, schema, pgvector)
ingest-close-reports	Parse inbox close reports into structured episodic memory candidates or writes
backfill-embeddings	Backfill missing vector embeddings for existing memories after pgvector repair
myelin_search	Search the myelin affordance registry by intent/context and return only top-k wrappers/reflexes
myelin_get	Fetch one affordance record with full metadata
myelin_validate	Validate one affordance against args and guard rules
debug_diagnose	Run debug-tool diagnosis through the unified MCP server
eda_profile	Run EDA dataset profiling through the unified MCP server
gate_validate	Run gate validation through the unified MCP server
memory_rebuild	Rebuild full agent context after compact or memory loss
MCP Resources
Resource	Description
memory://schema	Memory database schema information
memory://status	Current memory system status
MCP Agent Integration

To use the MCP server with an agent, configure the agent's MCP settings to include:

{
  "mcpServers": {
    "skill-system": {
      "command": "python",
      "args": ["skills/skill-system-memory/mcp/server.py"],
      "env": {
        "SKILL_PGDATABASE": "<project>-memory"
      }
    }
  }
}


Shared-DB MCP example:

{
  "mcpServers": {
    "skill-system": {
      "command": "python",
      "args": ["skills/skill-system-memory/mcp/server.py"],
      "env": {
        "SKILL_PGSHARED_DB": "shared-memory",
        "SKILL_PGSCHEMA": "sk_scope",
        "SKILL_VISITOR_ROLE": "visitor_sk_coder"
      }
    }
  }
}

MCP Tool Examples
# Search memories
mcp_tool: memory_search
args: { "query": "pgvector installation", "limit": 5 }

# Search memories with full content for the returned top-k rows
mcp_tool: memory_search
args: { "query": "pgvector installation", "limit": 5, "mode": "full" }

# Explicit cross-DB search
mcp_tool: memory_search
args: { "query": "reviewer feedback", "cross_db": true, "limit": 5 }

# Hermes all-scopes override in shared-DB mode
mcp_tool: memory_search
args: { "query": "cross-project audit", "all_scopes": true, "limit": 10 }

# Store a memory
mcp_tool: memory_store
args: { "type": "semantic", "category": "troubleshooting", "title": "Fixed pgvector on Windows", "content": "Build steps...", "importance": 8 }

# Update a memory locally
mcp_tool: memory_update
args: { "id": 42, "fields": { "title": "Updated title", "visibility": "shared" } }

# Soft-delete a memory locally
mcp_tool: memory_delete
args: { "id": 42 }

# Hard-delete a memory locally only with explicit authorization
mcp_tool: memory_purge
args: { "id": 42, "hard": true, "authorized": true }

# Auto-match memories (KEY TOOL for near-automatic surfacing)
mcp_tool: memory_auto_match
args: { "text": "I'm seeing an error with database connections", "threshold": 0.8, "limit": 5 }

# Auto-match without hiding low-score candidates
mcp_tool: memory_auto_match
args: { "text": "I'm seeing an error with database connections", "threshold": 0.8, "include_below_threshold": true, "limit": 5, "mode": "full" }

# Get user context
mcp_tool: memory_context
args: { "user": "default" }

# Check system health
mcp_tool: memory_status
args: {}


For existing installations, also run:

psql -U postgres -d <project>-memory -v ON_ERROR_STOP=1 -f migrate-v2-postgres-first.sql

Pure Skill Mode (default)

This skill works without installing any plugin. In pure skill mode:

you manually run scripts when you want (progressive disclosure)
no global OpenCode config is modified automatically
Optional bootstrap (asks + records choices + tries to install)

Notes:

Interactive mode defaults to NOT installing heavy optional components.
Use -InstallAll / --install-all only when you're ready to install everything.

Run the bootstrap script to choose optional components (pgpass, local embeddings, pgvector) and record decisions.

Bootstrap can also optionally install the OpenCode compaction logging plugin (it will copy the plugin into your OpenCode plugins directory).

Windows:

# run from the skill directory
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "scripts\bootstrap.ps1"


Linux/macOS:

# run from the skill directory
bash "scripts/bootstrap.sh"


The selection record is stored at:

~/.config/opencode/skill-system-memory/setup.json

Agent rule:

If this file does not exist, ask the user if they want to enable optional components.
Recommended: run bootstrap with all options enabled (then fix any failures it reports).
Runtime Capability Model

Current live capability classifications are intentionally narrow:

capability	current status	current support surface
core_memory	SUPPORTED_NOW	agent_memories plus store_memory, search_memories, memory_health_check
evolution_ledger	SUPPORTED_NOW	evolution_snapshots plus insert_evolution_snapshot, get_evolution_history
compaction_logging	SUPPORTED_NOW when the repo plugin is synced	local JSONL compaction log plus guarded store_memory(...) writeback
typed_context_reads	SUPPORTED_NOW	get_agent_context, get_soul_state, get_recent_facets, get_user_preferences
runtime_sync_projections	GATED_OPTIONAL	session_summaries, project_summaries, context_rollups only when those tables exist
behavior_refresh_graph	GATED_OPTIONAL	behavior_* refresh only when those tables exist
control_plane_refresh	DEFERRED_UNSUPPORTED	not part of the current user-facing memory runtime

When the durable evolution proposal model is present, doctor also reports:

canonical accepted store: evolution_nodes
canonical rejected store: evolution_rejections
canonical task materialization: evolution_tasks -> agent_tasks
role of agent_memories: searchable summary/backref surface with explicit legacy compatibility rows
approve/reject path status: transaction-safe at the CLI boundary
migration/backfill idempotence: rerun-safe
decision replay status: replay-idempotent by proposal_id
coordination mechanism: advisory lock by proposal + semantic fingerprint on canonical accepted/rejected rows
payload mismatch policy: blocked with no mutation
conflicting terminal policy: blocked with no mutation
task authority model: agent_tasks lifecycle authority, evolution_tasks mapping only

In that state, evolution_snapshots is treated as LEGACY_COMPAT_SURFACE for proposal durability, while remaining active for snapshot/version history.

On Windows, pgvector installation follows the official pgvector instructions (Visual Studio C++ + nmake /F Makefile.win). The bootstrap will attempt to install prerequisites via winget.

Optional automation: compaction logging (OpenCode plugin)

If you want automatic compaction logging, install the OpenCode plugin template shipped with this skill.

Option A (recommended): run bootstrap and choose the plugin option.

Copy plugins/skill-system-memory.js and plugins/runtime_sync.js to ~/.config/opencode/plugins/
Restart OpenCode

Safety / rollback (if OpenCode gets stuck on startup):

Remove or rename ~/.config/opencode/plugins/skill-system-memory.js
Remove or rename ~/.config/opencode/plugins/runtime_sync.js
Restart OpenCode
Check logs:
macOS/Linux: ~/.local/share/opencode/log/
Windows: %USERPROFILE%\.local\share\opencode\log

Plugin behavior notes:

The plugin is designed to be a no-op unless you explicitly enabled it via bootstrap (setup.json sets selected.opencode_plugin=true).
It only attempts a Postgres write if selected.pgpass=true (avoids hanging on auth prompts).
On compaction, it always keeps local JSONL logging and the core store_memory(...) path available when the DB target is valid.
Runtime projection upserts (session_summaries, project_summaries, context_rollups) are capability-gated: if those tables are absent, the plugin skips them with an explicit surfaced reason instead of attempting writes.
Behavior graph refresh into behavior_* tables is also capability-gated and is skipped explicitly when the required tables are absent.

Uninstall:

Remove ~/.config/opencode/plugins/skill-system-memory.js
Remove ~/.config/opencode/plugins/runtime_sync.js
Restart OpenCode
Credentials (psql)

Do NOT hardcode passwords in scripts, skill docs, or config files.

Recommended options for non-interactive psql:

.pgpass / pgpass.conf (recommended)
Linux/macOS: ~/.pgpass (must be chmod 0600 ~/.pgpass or libpq will ignore it)
Windows: %APPDATA%\postgresql\pgpass.conf (example: C:\Users\<you>\AppData\Roaming\postgresql\pgpass.conf)
Format: hostname:port:database:username:password
Docs: https://www.postgresql.org/docs/current/libpq-pgpass.html
PGPASSFILE (optional override): point to a custom location for the password file
PGPASSWORD (not recommended): only for quick local testing; environment variables can leak on some systems
Docs: https://www.postgresql.org/docs/current/libpq-envars.html

Tip: set connection defaults once (per shell) to shorten commands:

export PGHOST=localhost
export PGPORT=5432
export SKILL_PGDATABASE=<project>-memory
export PGUSER=postgres   # change to your PG superuser if postgres role does not exist


Shell copy/paste safety:

Avoid copying inline markdown backticks (e.g. semantic) into your shell. In zsh, backticks are command substitution.
Prefer using the wrapper scripts (scripts/mem.sh, scripts/mem.ps1) or copy from fenced code blocks.
One-time setup helper scripts

This skill ships helper scripts (relative paths):

scripts/setup-pgpass.ps1
scripts/setup-pgpass.sh

OpenCode usage: run them from the skill directory.

Windows run:

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "scripts\setup-pgpass.ps1"


Linux/macOS run:

bash "scripts/setup-pgpass.sh"

Memory Types
Type	Lifespan	Use When
working	24h auto-expire	Current conversation context (requires session_id)
episodic	Permanent + decay	Problem-solving experiences, debugging sessions
semantic	Permanent	Extracted facts, knowledge, patterns
procedural	Permanent	Step-by-step procedures, checklists (importance >= 7)
Core Functions
store_memory(type, category, tags[], title, content, metadata, agent_id, session_id, importance)

Auto-deduplicates by content hash. Duplicate inserts bump access_count and importance_score.

SELECT store_memory(
    'semantic',
    'windows-networking',
    ARRAY['ssh', 'tunnel', 'port-conflict'],
    'SSH Tunnel Port Conflict Resolution',
    'Fix: 1) taskkill /F /IM ssh.exe  2) Use processId not pid  3) Wait 3s',
    '{"os": "Windows 11"}',
    'sisyphus',
    NULL,
    9.0
);

Wrapper: scripts/mem.py (推薦 — parameterized query，無 quoting 問題)

Requirements: pip install psycopg2-binary

# DB 連線狀態 + 記憶總數
python3 scripts/mem.py status

# 搜尋記憶（含特殊字元也安全）
python3 scripts/mem.py search "pgvector windows install" --limit 5
python3 scripts/mem.py search "pgvector windows install" --limit 5 --mode full
python3 scripts/mem.py search "fraud features" --scope project --limit 10
python3 scripts/mem.py search "reviewer feedback" --cross-db --limit 10
python3 scripts/mem.py search "shared debugging notes" --scope all --limit 10

# 跨 5 維度診斷搜尋 (B-015 TKT-001)
python3 scripts/mem.py search "alert file" --diagnostic --limit 10

# Tag 前綴自動展開 (B-015 TKT-003)
python3 scripts/mem.py search "root-cause" --auto-expand

# 儲存記憶（--content flag）
python3 scripts/mem.py store --type semantic --category project --title "pgvector install" --tags "postgres,pgvector,windows" --importance 8 --scope project --content "Steps: ..."
python3 scripts/mem.py store --type semantic --category feedback --title "Reviewer note" --visibility shared --content "Cross-DB searchable note"
python3 scripts/mem.py update 42 --field title="Updated note" --field visibility=shared
python3 scripts/mem.py delete 42
python3 scripts/mem.py purge 42 --hard --authorized

# 儲存記憶（stdin）
printf '%s' "Steps: ..." | python3 scripts/mem.py store semantic project "pgvector install" "postgres,pgvector,windows" 8 --scope session

# 列出 / 匯出 / 壓縮
python3 scripts/mem.py list --scope project --limit 20
python3 scripts/mem.py export --format json --scope global
python3 scripts/mem.py compact --scope project

# session 開頭自動撈出相關記憶
python3 scripts/mem.py context "pgvector ssh tunnel"

# 列出所有已使用的 tags / categories
python3 scripts/mem.py tags
python3 scripts/mem.py categories

# DB 不可用時，將 pending fallback 寫回 DB
python3 scripts/mem.py flush

# 保守升級 visibility（只影響本地 DB）
python3 scripts/mem.py visibility-upgrade --visibility shared --category feedback --dry-run
python3 scripts/mem.py visibility-upgrade --visibility global --tags reviewer,decision


Fallback behavior:

DB 連線失敗時，store 會降級寫入 .memory/pending/*.json，search / context 會讀本地 pending 檔案並印出警告
list / export 也會從 pending fallback 讀取；compact 在 DB 不可用時只印 warning 不崩潰
DB 可連線但 memory schema 缺失時，store 會 warning + no-op，search / context / tags / categories 會回空結果 + warning
flush 會在 DB 恢復後將 .memory/pending/ 內容寫回 PostgreSQL

Scope model:

session (default): 記錄在 metadata.scope=session，並盡量帶上 session_id
project: 記錄在 metadata.scope=project + metadata.project_id=<repo>
global: 記錄在 metadata.scope=global，仍需明確 federated read 才會跨 DB 查詢
search / list / export 不帶 --scope 時，會回傳所有 scope 並在結果中標記來源 scope

Visibility is distinct from scope:

private (default): local DB only
shared: eligible for explicit cross-DB search
global: eligible for explicit cross-DB search and auto context injection

Mutation audit rules:

update writes selected field changes only, in the local DB only
delete is soft-delete only (deleted_at), preserving backward-compatible reads
purge is hard delete and must be explicitly authorized
every mutation writes a memory_audit row with old/new values plus actor metadata

CLI mutation examples:

python3 scripts/mem.py update 42 --field title="Updated note" --field visibility=shared
python3 scripts/mem.py delete 42
python3 scripts/mem.py purge 42 --hard --authorized


memory_audit is the canonical mutation trail for these operations. Each row records:

memory_id
action (update, delete, purge)
old_value
new_value
actor_id
session_id
changed_at

Warning: purge is destructive and bypasses soft-delete recovery. It stays local-only and requires explicit authorization flags; do not use it for routine cleanup.

Known federated read targets are configured in config/insight.yaml:

memory:
  cross_db_targets:
    - Work-memory
    - skills-memory
    - ExperimentPipeline-memory
    - FraudDetect-memory
  cross_db_context_visibility:
    - global


This list controls explicit read fan-out only. Write paths still target the local SKILL_PGDATABASE database even if a caller passes target_db-style data.

Wrapper: scripts/mem.sh / scripts/mem.ps1 (shell fallback)
# 連線狀態
bash "scripts/mem.sh" status

# 搜尋
bash "scripts/mem.sh" search "pgvector windows install" 5

# 儲存 (content via stdin)
printf '%s' "Steps: ..." | bash "scripts/mem.sh" store semantic project "pgvector install" "postgres,pgvector,windows" 8

# 列出 tags / categories
bash "scripts/mem.sh" tags
bash "scripts/mem.sh" categories

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "scripts\mem.ps1" types
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "scripts\mem.ps1" search "pgvector windows install" 5
"Steps: ..." | powershell.exe -NoProfile -ExecutionPolicy Bypass -File "scripts\mem.ps1" store semantic project "pgvector install" "postgres,pgvector,windows" 8

Router Integration (optional)

If you use a Router skill that executes pinned pipelines, it can read a manifest embedded in this SKILL.md.

For portability, the manifest block is fenced as YAML but the content is JSON (valid YAML). The Router parses it.

{
  "schema_version": "2.0",
  "id": "skill-system-memory",
  "version": "1.0.0",
  "capabilities": ["memory-search", "memory-search-cross-db", "memory-role-scope", "memory-store", "memory-update", "memory-delete", "memory-purge", "memory-visibility-upgrade", "memory-list", "memory-compact", "memory-export", "memory-export-md", "memory-flush", "memory-mirror-capture", "memory-reconcile-note-live", "memory-ingest-close-reports", "memory-backfill-embeddings", "myelin-search", "myelin-get", "myelin-validate", "memory-health", "memory-types", "memory-auto-write", "memory-doctor", "plugin-debug", "plugin-eda", "plugin-gate", "memory-rebuild"],
  "effects": ["proc.exec", "db.read", "db.write"],
  "operations": {
    "search": {
      "description": "Search memories by natural language query. Returns ranked results with relevance scores.",
      "input": {
        "query": { "type": "string", "required": true, "description": "Natural language search query" },
        "limit": { "type": "integer", "required": false, "default": 5, "description": "Max results" },
        "scope": { "type": "string", "required": false, "description": "global | project | session filter; all enables explicit cross-DB federation" },
        "cross_db": { "type": "boolean", "required": false, "description": "Explicitly fan out reads across configured memory DBs" },
        "all_scopes": { "type": "boolean", "required": false, "description": "Hermes/admin override to bypass visitor search_path scoping for cross-project audit" }
      },
      "output": {
        "description": "Array of memory matches with local scope labels and cross-DB source attribution when federation is enabled",
        "fields": { "status": "ok | error", "data": "array of {id, title, content, relevance_score, scope, source_db?}" }
      },
      "entrypoints": {
        "unix": ["bash", "scripts/router_mem.sh", "search", "{query}", "{limit}"],
        "windows": ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "scripts\\router_mem.ps1", "search", "{query}", "{limit}"]
      }
    },
    "store": {
      "description": "Store a new memory. Auto-deduplicates by content hash and always writes to the local memory DB.",
      "input": {
        "memory_type": { "type": "string", "required": true, "description": "One of: semantic, episodic, procedural, working" },
        "category": { "type": "string", "required": true, "description": "Category name" },
        "title": { "type": "string", "required": true, "description": "One-line summary" },
        "tags_csv": { "type": "string", "required": true, "description": "Comma-separated tags" },
        "importance": { "type": "integer", "required": true, "description": "1-10 importance score" },
        "scope": { "type": "string", "required": false, "description": "global | project | session" },
        "visibility": { "type": "string", "required": false, "description": "private | shared | global" }
      },
      "output": {
        "description": "Confirmation with stored memory id",
        "fields": { "status": "ok | error", "id": "integer" }
      },
      "entrypoints": {
        "unix": ["bash", "scripts/router_mem.sh", "store", "{memory_type}", "{category}", "{title}", "{tags_csv}", "{importance}"],
        "windows": ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "scripts\\router_mem.ps1", "store", "{memory_type}", "{category}", "{title}", "{tags_csv}", "{importance}"]
      }
    },
    "update": {
      "description": "Update selected fields of a local memory row by id with audit logging.",
      "input": {
        "id": { "type": "integer", "required": true },
        "fields": { "type": "object", "required": true }
      },
      "output": {
        "description": "Update summary",
        "fields": { "status": "ok | error", "id": "integer", "updated_fields": "array" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/mem.py", "update"],
        "windows": ["python", "scripts/mem.py", "update"]
      }
    },
    "delete": {
      "description": "Soft-delete a local memory row by id with audit logging.",
      "input": {
        "id": { "type": "integer", "required": true }
      },
      "output": {
        "description": "Soft-delete summary",
        "fields": { "status": "ok | error", "id": "integer", "deleted_at": "string" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/mem.py", "delete"],
        "windows": ["python", "scripts/mem.py", "delete"]
      }
    },
    "purge": {
      "description": "Hard-delete a local memory row only with explicit authorization.",
      "input": {
        "id": { "type": "integer", "required": true },
        "hard": { "type": "boolean", "required": true },
        "authorized": { "type": "boolean", "required": true }
      },
      "output": {
        "description": "Hard-delete summary",
        "fields": { "status": "ok | error", "id": "integer", "purged": "boolean" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/mem.py", "purge"],
        "windows": ["python", "scripts/mem.py", "purge"]
      }
    },
    "list": {
      "description": "List memories with optional scope/category filters.",
      "input": {
        "scope": { "type": "string", "required": false },
        "category": { "type": "string", "required": false },
        "limit": { "type": "integer", "required": false, "default": 20 }
      },
      "output": {
        "description": "Memory listing with scope labels",
        "fields": { "status": "ok | error", "results": "array" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/mem.py", "list"],
        "windows": ["python", "scripts/mem.py", "list"]
      }
    },
    "compact": {
      "description": "Compact duplicate memories within an optional scope.",
      "input": {
        "scope": { "type": "string", "required": false }
      },
      "output": {
        "description": "Compaction result",
        "fields": { "status": "ok | warn | error", "compacted_count": "integer" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/mem.py", "compact"],
        "windows": ["python", "scripts/mem.py", "compact"]
      }
    },
    "export": {
      "description": "Export memories in json or csv format.",
      "input": {
        "format": { "type": "string", "required": false },
        "scope": { "type": "string", "required": false },
        "limit": { "type": "integer", "required": false, "default": 1000 }
      },
      "output": {
        "description": "Export payload",
        "fields": { "status": "ok | error", "results": "array|string" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/mem.py", "export"],
        "windows": ["python", "scripts/mem.py", "export"]
      }
    },
    "export-md": {
      "description": "Export DB-only memories to markdown files that memory_sync can re-import.",
      "input": {
        "folder": { "type": "string", "required": true, "description": "Target folder for markdown exports" }
      },
      "output": {
        "description": "Markdown export result",
        "fields": { "status": "ok | error", "created": "integer", "skipped": "integer", "folder": "string" }
      },
      "entrypoints": {
        "agent": "Use the memory_export MCP tool from skills/skill-system-memory/mcp/server.py"
      }
    },
    "visibility-upgrade": {
      "description": "Batch-upgrade local memory visibility conservatively by category and/or tag selectors.",
      "input": {
        "visibility": { "type": "string", "required": true, "description": "shared | global | private" },
        "category": { "type": "string", "required": false },
        "tags": { "type": "string", "required": false },
        "dry_run": { "type": "boolean", "required": false, "default": false }
      },
      "output": {
        "description": "Upgrade summary",
        "fields": { "status": "ok | error", "matched": "integer", "updated": "integer" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/mem.py", "visibility-upgrade"],
        "windows": ["python", "scripts/mem.py", "visibility-upgrade"]
      }
    },
    "flush": {
      "description": "Flush local pending fallback files into PostgreSQL when the DB is back.",
      "input": {},
      "output": {
        "description": "Confirmation that pending fallback files were replayed",
        "fields": { "status": "ok | warn | error", "flushed_count": "integer" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/mem.py", "flush"],
        "windows": ["python", "scripts/mem.py", "flush"]
      }
    },
    "mirror-capture": {
      "description": "Mirror changed decision-critical file sections into the selected project memory DB with fail-open behavior.",
      "input": {
        "file": { "type": "string", "required": true, "description": "Changed file path" },
        "content": { "type": "string", "required": false, "description": "New file content" },
        "content_file": { "type": "string", "required": false, "description": "Path containing new file content" },
        "old_content": { "type": "string", "required": false, "description": "Previous file content" },
        "old_content_file": { "type": "string", "required": false, "description": "Path containing previous file content" },
        "config": { "type": "string", "required": false, "description": "Whitelist config path" },
        "pattern": { "type": "string", "required": false, "description": "Additional whitelist glob pattern" },
        "work_root": { "type": "string", "required": false, "description": "Optional root for relative whitelist matching" },
        "db_target": { "type": "string", "required": false, "description": "Explicit project memory DB target" },
        "log_path": { "type": "string", "required": false, "description": "Caller-configurable JSONL log path" },
        "pane": { "type": "string", "required": false, "description": "Origin pane/session metadata" },
        "dry_run": { "type": "boolean", "required": false, "default": false }
      },
      "output": {
        "description": "Mirror result with changed sections, store ids, and fail-open warnings",
        "fields": { "status": "ok | warn | error", "sections": "array", "store_ids": "array", "errors": "array" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/memory_mirror.py", "capture"],
        "windows": ["python", "scripts/memory_mirror.py", "capture"]
      }
    },
    "reconcile-note-live": {
      "description": "Reconcile live note decisions against memory backrefs before compact or close flows.",
      "input": {
        "note_file": { "type": "string", "required": true, "description": "Path to note_live style markdown" },
        "db_target": { "type": "string", "required": false, "description": "Explicit project memory DB target" },
        "log_path": { "type": "string", "required": false, "description": "Caller-configurable JSONL log path" },
        "pane": { "type": "string", "required": false, "description": "Origin pane/session metadata" },
        "dry_run": { "type": "boolean", "required": false, "default": false },
        "strict": { "type": "boolean", "required": false, "default": false },
        "store_missing": { "type": "boolean", "required": false, "default": true }
      },
      "output": {
        "description": "Reconcile result including checked titles, missing backrefs, and auto-store ids",
        "fields": { "status": "ok | warn | error", "checked_titles": "array", "missing_titles": "array", "store_ids": "array" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/memory_mirror.py", "reconcile"],
        "windows": ["python", "scripts/memory_mirror.py", "reconcile"]
      }
    },
    "ingest-close-reports": {
      "description": "Parse milestone close reports from inbox markdown and ingest them into episodic memory with dedup.",
      "input": {
        "inbox": { "type": "string", "required": true, "description": "Path to inbox markdown file" },
        "dry_run": { "type": "boolean", "required": false, "default": false },
        "limit": { "type": "integer", "required": false }
      },
      "output": {
        "description": "Structured candidates, stored ids, and dedup skips",
        "fields": { "status": "ok | error", "candidate_count": "integer", "candidates": "array", "stored_ids": "array", "skipped": "array" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/mem.py", "ingest-close-reports"],
        "windows": ["python", "scripts/mem.py", "ingest-close-reports"]
      }
    },
    "backfill-embeddings": {
      "description": "Backfill missing vector embeddings for existing memories after pgvector repair.",
      "input": {
        "limit": { "type": "integer", "required": false, "default": 50 },
        "model": { "type": "string", "required": false }
      },
      "output": {
        "description": "Updated ids, skipped ids, and provider/model summary",
        "fields": { "status": "ok | error", "updated_count": "integer", "updated_ids": "array", "skipped": "array" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/mem.py", "backfill-embeddings"],
        "windows": ["python", "scripts/mem.py", "backfill-embeddings"]
      }
    },
    "myelin-search": {
      "description": "Search the myelin affordance registry by intent/context and return top-k relevant wrappers/reflexes.",
      "input": {
        "intent": { "type": "string", "required": true, "description": "Intent label such as dispatch, inbox, or EP-status" },
        "context": { "type": "string", "required": false, "description": "Free text or JSON context payload" },
        "limit": { "type": "integer", "required": false, "default": 5 }
      },
      "output": {
        "description": "Ranked affordance results with guard warnings and bridge metadata",
        "fields": { "status": "ok | error", "results": "array", "warnings": "array", "bridge_contract": "object" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/myelin_registry.py", "search", "{intent}"],
        "windows": ["python", "scripts/myelin_registry.py", "search", "{intent}"]
      }
    },
    "myelin-get": {
      "description": "Get one affordance record with full metadata.",
      "input": {
        "id": { "type": "string", "required": true, "description": "Affordance identifier" }
      },
      "output": {
        "description": "Affordance record",
        "fields": { "status": "ok | error", "record": "object" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/myelin_registry.py", "get", "{id}"],
        "windows": ["python", "scripts/myelin_registry.py", "get", "{id}"]
      }
    },
    "myelin-validate": {
      "description": "Validate one affordance against args and guard raw-shell fallbacks.",
      "input": {
        "id": { "type": "string", "required": true },
        "args": { "type": "string", "required": false, "description": "JSON args/context payload" }
      },
      "output": {
        "description": "Validation result",
        "fields": { "status": "ok | error", "valid": "boolean", "warnings": "array", "missing_required_context": "array" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/myelin_registry.py", "validate", "{id}"],
        "windows": ["python", "scripts/myelin_registry.py", "validate", "{id}"]
      }
    },
    "health": {
      "description": "Check memory system health: total count, average importance, stale count.",
      "input": {},
      "output": {
        "description": "Health metrics",
        "fields": { "status": "ok | error", "data": "array of {metric, value, status}" }
      },
      "entrypoints": {
        "unix": ["bash", "scripts/router_mem.sh", "health"],
        "windows": ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "scripts\\router_mem.ps1", "health"]
      }
    },
    "types": {
      "description": "List available memory types and their descriptions.",
      "input": {},
      "output": {
        "description": "Memory type definitions",
        "fields": { "status": "ok | error", "data": "array of {type, lifespan, description}" }
      },
      "entrypoints": {
        "unix": ["bash", "scripts/router_mem.sh", "types"],
        "windows": ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "scripts\\router_mem.ps1", "types"]
      }
    },
    "auto-write": {
      "description": "Procedure template for automatically storing a memory after solving a non-obvious problem.",
      "input": {},
      "output": {
        "description": "Proposed memory fields to store",
        "fields": {"memory_type": "string", "category": "string", "title": "string", "tags_csv": "string", "importance": "integer", "content": "string"}
      },
      "entrypoints": {
        "agent": "Follow scripts/auto-write-template.md"
      }
    },
    "doctor": {
      "description": "Report the current runtime capability map, memory plugin drift, memory DB target, OMO resolution, canonical evolution stores, table/routine readiness, and evolution ledger status.",
      "input": {},
      "output": {
        "description": "Doctor report for the current runtime state",
        "fields": {"status": "ok | warn | error", "doctor_report": "object"}
      },
      "entrypoints": {
        "unix": ["python3", "scripts/runtime_doctor.py", "--format", "json"],
        "windows": ["python", "scripts/runtime_doctor.py", "--format", "json"]
      }
    },
    "debug-diagnose": {
      "description": "Expose skill-system-debug diagnose through the unified MCP server.",
      "input": {
        "symptom": { "type": "string", "required": true },
        "context": { "type": "string", "required": false }
      },
      "output": {
        "description": "Structured diagnosis payload",
        "fields": { "status": "ok | error", "result": "object" }
      },
      "entrypoints": {
        "agent": "Use the debug_diagnose MCP tool from skills/skill-system-memory/mcp/server.py"
      }
    },
    "eda-profile": {
      "description": "Expose skill-system-eda dataset profiling through the unified MCP server.",
      "input": {
        "input_path": { "type": "string", "required": true },
        "sample": { "type": "integer", "required": false },
        "target": { "type": "string", "required": false }
      },
      "output": {
        "description": "EDA profile output",
        "fields": { "status": "ok | error", "profile_path": "string", "report_path": "string" }
      },
      "entrypoints": {
        "agent": "Use the eda_profile MCP tool from skills/skill-system-memory/mcp/server.py"
      }
    },
    "gate-validate": {
      "description": "Expose skill-system-gate validation through the unified MCP server.",
      "input": {
        "rules": { "type": "string", "required": false },
        "artifact_root": { "type": "string", "required": false }
      },
      "output": {
        "description": "Gate validation summary",
        "fields": { "status": "ok | error", "passed": "boolean", "results": "array" }
      },
      "entrypoints": {
        "agent": "Use the gate_validate MCP tool from skills/skill-system-memory/mcp/server.py"
      }
    },
    "rebuild": {
      "description": "Rebuild full agent context after compact or memory loss.",
      "input": {
        "user": { "type": "string", "required": false },
        "recent_limit": { "type": "integer", "required": false }
      },
      "output": {
        "description": "Soul, preferences, recent memories, and pending decisions",
        "fields": { "status": "ok | error", "rebuild_context": "object" }
      },
      "entrypoints": {
        "agent": "Use the memory_rebuild MCP tool from skills/skill-system-memory/mcp/server.py"
      }
    }
  },
  "stdout_contract": {
    "last_line_json": true
  },
  "mcp": {
    "server": {
      "name": "skill-system",
      "description": "Unified skill-system MCP server exposing memory, myelin, debug, eda, gate, and memory_rebuild tools",
      "entrypoint": "python skills/skill-system-memory/mcp/server.py",
      "transport": "stdio",
      "tools": ["memory_search", "memory_store", "memory_auto_match", "memory_context", "memory_status", "memory_sync", "memory_export", "myelin_search", "myelin_get", "myelin_validate", "debug_diagnose", "eda_profile", "gate_validate", "memory_rebuild"],
      "resources": ["memory://schema", "memory://status"]
    }
  }
}


Notes:

The Router expects each step to print last-line JSON.
These Router adapter scripts are separate from mem.sh / mem.ps1 to avoid breaking existing workflows.
Memory Mirror Engine (SK-005)

scripts/memory_mirror.py is the SK-owned fail-open engine for automatic memory mirroring and pre-compact reconciliation.

python3 scripts/memory_mirror.py capture --file Work/note/note_live.md --content-file /tmp/new.md --old-content-file /tmp/old.md --db-target Work-memory --log-path Work/.tkt/memory-mirror.log
python3 scripts/memory_mirror.py reconcile --note-file Work/note/note_live.md --db-target Work-memory --log-path Work/.tkt/memory-mirror.log

Default whitelist lives in memory-mirror-config.yaml
Work-owned wrappers should pass --db-target Work-memory explicitly
Structured log output is JSONL and caller-configurable
Decision-log transaction hardening contract is documented in memory-mirror-contract.md
Close Report Ingestion
./sk mem ingest-close-reports --inbox /share/nas165/arthur0824hao/Work/.tkt/inbox/hermes/inbox.md --dry-run
./sk mem ingest-close-reports --inbox /share/nas165/arthur0824hao/Work/.tkt/inbox/hermes/inbox.md

Purpose: turn milestone close/blocker reports into searchable episodic memory
Dedup: bundle id + actor + timestamp + report status ingest key
Runbook: close-report-ingestion-runbook.md
Vector / Embedding Health

memory_status now treats semantic/vector retrieval as optional capability-gated health:

pgvector_enablement_status: enabled | disabled | unavailable-on-host
pgvector_blocker: exact host/install blocker when unavailable
embedding_dependency_installed: whether the local embedding runtime is present
semantic_search_mode: hybrid-ready | hybrid-schema-no-vectors | vector-installable-but-disabled | fts-trgm-only

FTS + pg_trgm fallback remains the default safe path when pgvector or sentence-transformers is absent.

Semantic retrieval repair commands
SKILL_PGDATABASE=Work-memory python3 scripts/mem.py backfill-embeddings --limit 100
SKILL_PGDATABASE=Work-memory python3 scripts/semantic_smoke.py --db-target Work-memory

mem.py now disables HuggingFace Xet by default when loading sentence-transformers models, to avoid the CAS retry failure that blocked all-MiniLM-L6-v2 cold downloads in the active MCP env.
semantic_smoke.py stores one paraphrased semantic memory and queries it with a non-trivial phrasing to verify the hybrid retrieval path.
Codex MCP transport recovery fallback

If a native MCP session reports Transport closed, use the canonical CLI/scripts outside MCP first:

python3 scripts/mcp_health_probe.py --db-target Work-memory --tool-error "Transport closed"
python3 scripts/mem_work.py status
python3 scripts/mem_work.py search "Hermes inbox triage latest 14:35 Talos Sisyphus Daedalus memory MCP fallback mem.py" --limit 5
python3 scripts/mem_work.py store --type episodic --category scratch --title "transport recovery check" --content "explicit fallback path" --scope project

mem_work.py is a thin wrapper over canonical mem.py
It injects SKILL_PGDATABASE=Work-memory, PGDATABASE=Work-memory, PGHOST=localhost, and PGPORT=5432
Use it for Finch/Wren fallback instead of hand-typing env every time

Recovery rule (fail-closed):

If mcp_health_probe.py returns diagnosis=client_transport_stale, the current client/tool transport cannot be repaired purely server-side.
Do not kill memory MCP processes blindly and do not restart unrelated panes.
Restart only the affected client session/tool transport (operator-approved), then re-verify:
MCP memory_status works again
python3 scripts/mem_work.py status stays healthy
nvidia-smi --query-compute-apps shows no skill-system-memory support context on GPU0
Myelin Registry + ANS Bridge

scripts/myelin_registry.py turns SK MCP into a myelin index / affordance interface.

python3 scripts/myelin_registry.py build --output artifacts/myelin-registry.json
python3 scripts/myelin_registry.py search dispatch --context '{"pane":"dev_coder:SK-coder","message_file":"/tmp/spec.txt"}' --limit 3
python3 scripts/myelin_registry.py get dispatch:hermes-dispatch
python3 scripts/myelin_registry.py validate cli:raw-tmux-sendkeys --args '{"pane":"dev_coder:SK-coder","message":"hi","intent":"dispatch","urgent":false}'

Metadata schema: myelin-registry.schema.yaml
Seeded high-value affordances: myelin-seeds.yaml
ANS event/response contract: ans-myelin-bridge-contract.yaml
Policy: index all affordances, inject only top-k relevant ones by intent/context
Visualize Memories (Markdown export)

If querying PostgreSQL is too inconvenient for daily use, you can export memories into markdown files under ./Memory/ (current directory by default):

bash "<skill-dir>/scripts/sync_memory_to_md.sh" --out-dir "./Memory"


Outputs:

Memory/Long.md (semantic + procedural)
Memory/Procedural.md (procedural only)
Memory/Short.md (friction + compaction-daily + procedural highlights)
Memory/Episodic.md (episodic)

Backups:

Backups are stored under Memory/.backups/ to avoid noisy git status.
Use --no-backup to disable.

The sync script will also create Memory/.gitignore if it doesn't exist (ignores .backups/ and SYNC_STATUS.txt).

Long index:

Memory/Long.md includes an Index section (top categories + tags) to make the export browsable.
search_memories(query, types[], categories[], tags[], agent_id, min_importance, limit)

Hybrid search: full-text (tsvector) + trigram similarity (pg_trgm) + tag filtering. Accepts plain English queries — no tsquery syntax needed. Relevance scoring: text_score * decay * recency * importance.

-- Natural language
SELECT * FROM search_memories('ssh tunnel port conflict', NULL, NULL, NULL, NULL, 7.0, 5);

-- Filter by type + tags
SELECT * FROM search_memories(
    'troubleshooting steps',
    ARRAY['procedural']::memory_type[],
    NULL,
    ARRAY['ssh'],
    NULL, 0.0, 5
);


Returns: id, memory_type, category, title, content, importance_score, relevance_score, match_type Where match_type is one of: fulltext, trigram_title, trigram_content, metadata.

memory_health_check()

Returns: metric | value | status for total_memories, avg_importance, stale_count.

apply_memory_decay()

Decays episodic memories by 0.9999^days_since_access. Run daily.

prune_stale_memories(age_days, max_importance, max_access_count)

Soft-deletes old episodic memories below thresholds. Default: 180 days, importance <= 3, never accessed.

Agent Workflow
Auto-Write Template

After fixing a bug or solving a non-obvious problem, store a memory using the standard template:

Procedure: scripts/auto-write-template.md

最佳實踐：優先使用 mem.py wrapper，避免 shell quoting 與認證問題。 Raw SQL 範例請見 Appendix: Raw SQL。

Before a task
# 自動撈出相關記憶摘要（推薦）
python3 scripts/mem.py context "keywords from user request"

# 或搜尋並手動閱讀
python3 scripts/mem.py search "keywords from user request" 5


If relevant memories found, reference them: "Based on past experience (memory #1)..."

After solving a problem
python3 scripts/mem.py store semantic category-name "One-line problem summary" \
  "tag1,tag2,tag3" 8 --content "Detailed problem + solution"

When delegating to subagents

Include in prompt:

MUST DO FIRST:
  python3 scripts/mem.py context 'relevant keywords'

MUST DO AFTER:
  If you solved something new:
  python3 scripts/mem.py store semantic <category> '<title>' '<tags>' <importance> --content '<solution>'

Check memory system health
python3 scripts/mem.py status

Task Memory Layer (optional)

This skill also ships a minimal task/issue layer inspired by Beads: graph semantics + deterministic "ready work" queries.

Objects:

agent_tasks: tasks (status, priority, assignee)
task_links: typed links (blocks, parent_child, related, etc.)
blocked_tasks_cache: materialized cache to make ready queries fast
task_memory_links: link tasks to memories (agent_memories) for outcomes/notes

Create tasks:

INSERT INTO agent_tasks(title, description, created_by, priority)
VALUES ('Install pgvector', 'Windows build + enable extension', 'user', 1);


Add dependencies:

-- Task 1 blocks task 2
INSERT INTO task_links(from_task_id, to_task_id, link_type)
VALUES (1, 2, 'blocks');

-- Task 2 is parent of task 3 (used for transitive blocking)
INSERT INTO task_links(from_task_id, to_task_id, link_type)
VALUES (2, 3, 'parent_child');


Rebuild blocked cache (usually auto via triggers):

SELECT rebuild_blocked_tasks_cache();


Ready work query:

SELECT id, title, priority
FROM agent_tasks t
WHERE t.deleted_at IS NULL
  AND t.status IN ('open','in_progress')
  AND NOT EXISTS (SELECT 1 FROM blocked_tasks_cache b WHERE b.task_id = t.id)
ORDER BY priority ASC, updated_at ASC
LIMIT 50;


Claim a task (atomic):

SELECT claim_task(2, 'agent-1');


Link a task to a memory:

INSERT INTO task_memory_links(task_id, memory_id, link_type)
VALUES (2, 123, 'outcome');


Optional add-on: conditional_blocks (not implemented yet)

This is intentionally deferred until the core workflow feels solid.
If you need it now, store a condition in task_links.metadata (e.g., { "os": "windows" }) and treat it as documentation.
Wrapper scripts (recommended)

To avoid re-typing SQL, use the wrapper scripts shipped with this skill:

Windows:

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "scripts\tasks.ps1" ready 50
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "scripts\tasks.ps1" create "Install pgvector" 1
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "scripts\tasks.ps1" claim 2 agent-1


Linux/macOS:

bash "scripts/tasks.sh" ready 50
bash "scripts/tasks.sh" create "Install pgvector" 1
bash "scripts/tasks.sh" claim 2 agent-1

Compaction Log (high value)

Compaction can delete context. Treat every compaction as an important event and record it.

If you're using OpenCode, prefer the OpenCode plugin route for automatic compaction logging.

OpenCode plugin (experimental.session.compacting)
Copy plugins/skill-system-memory.js and plugins/runtime_sync.js to ~/.config/opencode/plugins/
Restart OpenCode

It writes local compaction events to:

~/.config/opencode/skill-system-memory/compaction-events.jsonl

And will also attempt a best-effort Postgres store_memory(...) write (requires pgpass).

Verify
SELECT id, title, relevance_score
FROM search_memories('compaction', NULL, NULL, NULL, NULL, 0, 10);


If nothing is inserted, set up .pgpass / pgpass.conf so psql can authenticate without prompting.

Daily Compaction Consolidation

Raw compaction events are noisy. Run a daily consolidation job that turns many compaction events into 1 daily memory.

The consolidation scripts default to the OpenCode plugin event log path.

OpenCode events: ~/.config/opencode/skill-system-memory/compaction-events.jsonl
Output directory: ~/.config/opencode/skill-system-memory/compaction-daily/

Windows run (manual):

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "scripts\consolidate-compactions.ps1"


Linux/macOS run (manual):

bash "scripts/consolidate-compactions.sh"


Scheduling:

Windows Task Scheduler: create a daily task that runs the PowerShell command above
Linux cron example:
# every day at 02:10 UTC
10 2 * * * bash "<skill-dir>/scripts/consolidate-compactions.sh" >/dev/null 2>&1

Friction Log (turn pain into tooling)

Whenever something is annoying, brittle, or fails:

Store an episodic memory with category friction and tags for the tool/OS/error.
If it repeats (2+ times), promote it to procedural memory (importance >= 7) with a checklist.
Update this skill doc when the fix becomes a stable rule/workflow (so every agent learns it).
Schema Overview

agent_memories — General event log. Full-text search, trigram indexes, JSONB metadata, soft-delete. soul_states — One row per user. Structured personality/emotion/buffers JSONB. FK → agent_memories. insight_facets — Per-session facets with structured fields. FK → agent_memories. evolution_snapshots — Versioned evolution records with changes JSONB. FK → agent_memories. Current status: LEGACY_COMPAT_SURFACE for proposal durability, while remaining active for snapshot/version history. user_preferences — Key-value user preferences with confidence scores. memory_links — Graph relationships (references, supersedes, contradicts). working_memory — Ephemeral session context with auto-expire.

Typed table functions (dual-write to both typed table and agent_memories):

upsert_soul_state(user, yaml, personality, emotion, ...) → soul_states
insert_insight_facet(user, session_id, yaml, ...) → insight_facets
insert_evolution_snapshot(user, version_tag, target, ...) → evolution_snapshots
upsert_user_preference(user, key, value, source, confidence) → user_preferences
get_soul_state(user), get_recent_facets(user, limit), get_evolution_history(user, limit), get_user_preferences(user) → typed reads
get_agent_context(user, facet_limit) → aggregated context for plugin injection

There is currently no repo-backed migrate-typed-tables.sql file. Treat legacy typed-table backfill as deferred; do not claim it as a supported migration path.

Optional Postgres-first runtime projection tables (session_summaries, project_summaries, context_rollups, behavior_*) are created by migrate-v2-postgres-first.sql when you explicitly choose to enable that surface.

Key columns: memory_type, category, tags[], title, content, content_hash (auto), metadata (JSONB), importance_score, access_count, relevance_decay, search_vector (auto).

Anti-Patterns
Don't	Do Instead
Store everything	Only store non-obvious solutions
Skip tags	Tag comprehensively: tech, error codes, platform
Use to_tsquery directly	search_memories() handles this via plainto_tsquery
One type for all data	Use correct memory_type per content
Forget importance rating	Rate honestly: 9-10 battle-tested, 5-6 partial
Sharp Edges
Issue	Severity	Mitigation
Chunks lose context	Critical	Store full problem+solution as one unit
Old tech memories	High	apply_memory_decay() daily; prune stale
Duplicate memories	Medium	store_memory() auto-deduplicates by content_hash
No vector search	Info	pg_trgm provides fuzzy matching; pgvector can be added later
Cross-Platform Notes
PostgreSQL 14-18 supported (no partitioning, no GENERATED ALWAYS)
pg_trgm is the only required extension (ships with all PG distributions)
Linux: psql -U postgres -d <project>-memory -f init.sql
Windows: Use full path to psql.exe or add PG bin to PATH
MCP postgres_query: Works for read operations; DDL requires psql
Maintenance
SELECT apply_memory_decay();                         -- daily
SELECT prune_stale_memories(180, 3.0, 0);            -- monthly
DELETE FROM working_memory WHERE expires_at < NOW();  -- daily
SELECT * FROM memory_health_check();                  -- anytime

Optional: pgvector Semantic Search

If pgvector is installed on your PostgreSQL server, init.sql will:

create extension vector (non-fatal if missing)
add agent_memories.embedding vector (variable dimension)
create search_memories_vector(p_embedding, p_embedding_dim, ...)

Notes:

This does NOT generate embeddings. You must populate agent_memories.embedding yourself.
Once embeddings exist, you can do nearest-neighbor search:
-- p_embedding is a pgvector literal; pass it from your app.
-- Optionally filter by dimension (recommended when using multiple models).
SELECT id, title, similarity
FROM search_memories_vector('[0.01, 0.02, ...]'::vector, 768, NULL, NULL, NULL, NULL, 0.0, 10);


Note: variable-dimension vectors cannot be indexed with pgvector indexes. This is a tradeoff to support local models with different embedding sizes.

If pgvector is not installed, everything else still works (fts + pg_trgm).

Embedding Ingestion Pipeline

pgvector search only works after you populate agent_memories.embedding.

This skill ships ingestion scripts (relative paths). Run from the skill directory:

scripts/ingest-embeddings.ps1
scripts/ingest-embeddings.sh

They:

find memories with embedding IS NULL
call an OpenAI-compatible embeddings endpoint (including Ollama)
write vectors into agent_memories.embedding vector

Requirements:

pgvector installed + init.sql applied (so agent_memories.embedding exists)
.pgpass / pgpass.conf configured (so psql -w can write without prompting)
env vars for embedding API:
EMBEDDING_PROVIDER (ollama or openai; default openai)
EMBEDDING_API_KEY (required for openai; optional for ollama)
EMBEDDING_API_URL (default depends on provider)
EMBEDDING_MODEL (default depends on provider)
EMBEDDING_DIMENSIONS (optional; forwarded to the embeddings endpoint when supported)

Windows example:

$env:EMBEDDING_PROVIDER = "ollama"
$env:EMBEDDING_MODEL = "nomic-embed-text"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "scripts\ingest-embeddings.ps1" -Limit 25


Linux/macOS example:

export EMBEDDING_API_KEY=...
export EMBEDDING_MODEL=text-embedding-3-small
bash "scripts/ingest-embeddings.sh"


Scheduling:

run daily (or hourly) after you add new memories
keep Limit small until you trust it

Robustness note:

On Windows, very long SQL strings can be fragile when passed via psql -c. The ingestion script writes per-row updates to a temporary .sql file and runs psql -f to avoid command-line length/quoting edge cases.
Related Skills

systematic-debugging, postgres-pro, postgresql-table-design Shared-DB mode requires runtime role switching:

connect using the connector credential
SET ROLE visitor_<identity> per request
use --all-scopes only for Hermes/admin cross-project audit flows
Weekly Installs
99
Repository
arthur0824hao/skills
GitHub Stars
4
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn