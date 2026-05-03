---
rating: ⭐⭐⭐
title: cartog
url: https://skills.sh/jrollin/cartog/cartog
---

# cartog

skills/jrollin/cartog/cartog
cartog
Installation
$ npx skills add https://github.com/jrollin/cartog --skill cartog
SKILL.md
cartog — Code Graph Navigation Skill
Quick Start
Ensure indexed — run the setup script (see Setup below). This is required before any command works.
Explore an unfamiliar codebase — cartog map gives a file tree + top symbols ranked by centrality. Start here when onboarding or orienting.
Search for anything — cartog rag search "your query" is the default entry point. It handles keywords, natural language, and concept queries in a single call.
When to Use

Use cartog before reaching for grep, cat, or file reads when you need to:

Orient in a codebase → cartog map [--tokens N] (start here for unfamiliar projects)
Find code by name, concept, or behavior → cartog rag search "query"
Search project documentation → cartog rag search "query" --kind document
Understand the structure of a file → cartog outline <file>
Find who references a symbol → cartog refs <name> (or --kind calls for just callers)
See what a function calls → cartog callees <name>
Assess refactoring impact → cartog impact <name> --depth 3
Understand class hierarchies → cartog hierarchy <class>
See file dependencies → cartog deps <file>
See what changed recently → cartog changes [--commits N]
How to Run

cartog has two modes — CLI (via Bash) and MCP server. Prefer CLI by default.

Situation	Mode	Why
Single command or simple query	CLI	No server overhead, direct output
Multi-step workflow (e.g. search → refs → impact)	MCP	Warm DB connection, parallel tool calls
Subagent	CLI	MCP tools are only available to the main agent

Do not fall back to grep/glob if MCP tools are missing — use the Bash tool instead.

Rules for both modes:

Run independent cartog commands as parallel tool calls — whether MCP or Bash
Subagents: always use CLI mode via Bash. Skip setup — assume the parent has already indexed

CLI mode: every cartog command in the examples below must be run via a Bash tool call. Do not chain with && or | — use separate Bash calls.

All examples below use CLI syntax. MCP tool names and parameters:

CLI command	MCP tool	Parameters
cartog index .	cartog_index	path, force
cartog search <name>	cartog_search	query, kind?, file?, limit?
cartog rag search "<query>"	cartog_rag_search	query, kind?, limit?
cartog rag index .	cartog_rag_index	path, force
cartog outline <file>	cartog_outline	file
cartog refs <name>	cartog_refs	name, kind?
cartog callees <name>	cartog_callees	name
cartog impact <name>	cartog_impact	name, depth?
cartog hierarchy <class>	cartog_hierarchy	name
cartog deps <file>	cartog_deps	file
cartog changes	cartog_changes	commits?, kind?
cartog stats	cartog_stats	—
cartog doctor	— (CLI only)	—
Setup

Before first use, ensure cartog is installed and indexed.

If the project uses Ollama (check .cartog.toml for [embedding] provider = "ollama"), skip rag setup — models are managed by the Ollama server.

The scripts/ directory is located next to this SKILL.md file. Before running any setup command, look at the absolute path from which this SKILL.md was loaded (visible in your tool call history), take its parent directory, and use that as the scripts root in the bash commands below.

For example: if this file was loaded from /home/user/.claude/skills/cartog/SKILL.md, run:

# Install if missing
command -v cartog || bash "/home/user/.claude/skills/cartog/scripts/install.sh"

# Run the setup script (handles version check + 3 indexing phases)
bash "/home/user/.claude/skills/cartog/scripts/ensure_indexed.sh"


The setup script checks for newer cartog versions (cached, at most once per 24h). If an update is available it prints a notice like:

New cartog version available: X.Y.Z (installed: A.B.C). Update with: bash "/path/to/skill/scripts/install.sh" X.Y.Z


When you see this notice, ask the user if they want to update before continuing. If they agree, run the suggested command, then re-run bash "/path/to/skill/scripts/ensure_indexed.sh".

Search quality tiers

cartog rag search works at three quality levels depending on setup state:

Tier	After	FTS5	Reranker	Vector	Quality
1	cartog index .	Yes	No	No	Keyword matching only
2	+ cartog rag setup	Yes	Yes	No	Keyword + neural reranking
3	+ cartog rag index .	Yes	Yes	Yes	Full hybrid (best)

The setup script runs tier 1+2 blocking, then tier 3 in the background. cartog rag search is usable immediately after tier 2 — vector search becomes available transparently once background embedding completes.

First run: tier 2 downloads ~1.2GB of ONNX models (cached in ~/.cache/cartog/models/). This may take a few minutes — do not abort. Subsequent runs are instant.

Database Location

The index is stored in a SQLite database. cartog resolves the path automatically:

Priority	Source
1	--db <path> flag or CARTOG_DB env var
2	.cartog.toml → [database] path = "..." at git root
3	Auto git-root: DB placed at the root of the current git repository
4	.cartog.db in the current directory (fallback)

For most projects, no configuration is needed — running cartog index . from any subdirectory will place the DB at the git root automatically.

# Override examples
cartog --db /tmp/myproject.db index .
CARTOG_DB=~/.local/share/cartog/proj.db cartog index .

Why cartog Over grep/glob

cartog pre-computes a code graph (symbols + edges) with tree-sitter and stores it in SQLite. Compared to grep/glob:

Fewer tool calls: 1 command vs 3-6 grep/read cycles
Transitive analysis: impact --depth 3 traces callers-of-callers — grep can't do this
Structured results: symbols with types, signatures, and line ranges — not raw text matches
Workflow Rules

Before you grep or read a file to understand structure, query cartog first.

Search routing — pick the right strategy based on the query:

A. Semantic search (cartog rag search "<query>") — default for all searches. Returns code only by default; use --kind document for docs or --kind all for both. Handles keyword matching (FTS5), vector similarity, and cross-encoder reranking in a single call. Works for both natural language and keyword-style queries. Always use ONE call with the full query — never split a query into multiple rag search calls.

cartog rag search "authentication token validation"
cartog rag search "contract management and timesheet signing"
cartog rag search "config"


B. Structural search (cartog search <name>) — use only when you need a symbol name to feed into refs, callees, impact, or hierarchy. These commands require exact symbol names, not search results.

cartog search validate_token
cartog search AuthService --kind class


Routing rules:

Need to find code? → A (rag search) — always
Need a symbol name for refs/callees/impact? → B (search) first, then the structural command
User already gave an exact symbol name? → call refs/callees/impact directly — skip search

When using cartog search to locate a symbol before refs/callees/impact:

Exactly one result → use that symbol name and file, proceed.
Multiple results, same name, different files → add --file <path> to disambiguate.
Multiple results, different names → add --kind <kind> to filter, then re-evaluate.
Never pass an ambiguous name to refs/callees/impact — the result will be wrong.

Use cartog outline <file> instead of cat <file> when you need structure, not content. Then use Read (with offset/limit) for the specific lines you need — this is more efficient than reading entire files.

Before refactoring, run cartog impact <symbol> to see the blast radius.

Only fall back to grep/read when cartog doesn't have what you need (e.g., reading actual implementation logic, string literals, config values).

After making code changes, run cartog index . --no-lsp to quickly update the graph.

Do / Don't

DO:

Use cartog rag search as your default search — it combines FTS5 keyword + vector + reranking in one call
Use cartog search only to get a symbol name for structural commands (refs, callees, impact, hierarchy)
Trust that rag search degrades gracefully — FTS5 works even without vector embeddings

DON'T:

Run cartog search and cartog rag search in parallel for the same query — this wastes a tool call. rag search already includes FTS5 keyword matching internally
Split one query into multiple rag search calls with rephrased variants — one call is enough. The hybrid search (FTS5 + vector + reranker) handles synonyms and related terms internally
Block on RAG embedding at setup — background indexing is fine, rag search works immediately with FTS5 + reranker
Assume rag search requires rag index — it works (at reduced quality) with just cartog index .
Chain multiple cartog CLI commands with && or | — each invocation opens a fresh SQLite connection with full initialization overhead (PRAGMAs, schema checks, cold cache). Run them as separate tool calls instead
Pipe cartog output through grep — cartog already returns focused, structured results. Filtering with grep discards context (line numbers, kinds, file paths) and can break && chains when grep finds no match (exit code 1)
Combine unrelated cartog queries in one bash command — this creates false dependencies and hides failures. See references/query_cookbook.md → "Anti-patterns to avoid" for examples
Commands Reference
Index (build/rebuild)
cartog index .                    # Index current directory (with LSP if available)
cartog index . --no-lsp           # Fast heuristic-only index (~1-4s)
cartog index src/                 # Index specific directory
cartog index . --force            # Re-index all files (ignore cache)


By default, cartog index . auto-detects language servers on PATH and uses them to resolve additional edges. LSP results are persisted in the database — subsequent queries benefit without re-running LSP. Use --no-lsp for fast day-to-day indexing. LSP can be omitted entirely at build time with --no-default-features.

Search (find symbols by partial name)
cartog search parse                          # prefix + substring match
cartog search parse --kind function          # filter by symbol kind
cartog search config --file src/db.rs        # filter to one file
cartog search parse --limit 10               # cap results


Returns symbols ranked: exact match → prefix → substring. Case-insensitive. Max 100 results.

Valid --kind values: function, class, method, variable, import, interface, enum, type-alias, trait, module, document.

RAG Search (hybrid keyword + semantic)
cartog rag search "authentication token validation"
cartog rag search "error handling" --kind function
cartog rag search "database schema setup" --limit 20
cartog rag search "deployment architecture" --kind document


By default, returns code only. Use --kind document for docs or --kind all for both. Uses hybrid retrieval: FTS5 keyword matching + vector KNN, merged via Reciprocal Rank Fusion. When the cross-encoder model is available, results are re-ranked for better precision.

Outline (file structure)
cartog outline src/auth/tokens.py


Output shows symbols with types, signatures, and line ranges — no need to read the file.

Refs (who references this?)
cartog refs validate_token               # all reference types
cartog refs validate_token --kind calls  # only call sites


Available --kind values: calls, imports, inherits, references, raises, implements, type-of.

Callees (what does this call?)
cartog callees authenticate

Impact (transitive blast radius)
cartog impact SessionManager --depth 3


Shows everything that transitively depends on a symbol up to N hops.

Hierarchy (inheritance tree)
cartog hierarchy BaseService

Deps (file imports)
cartog deps src/routes/auth.py

Map (codebase overview)
cartog map                               # default 4000 tokens
cartog map --tokens 2000                 # compact
cartog map --tokens 8000                 # detailed


File tree + top symbols ranked by reference count (centrality). Use at the start of a session for context loading.

Changes (recently modified symbols)
cartog changes                           # last 5 commits + working tree
cartog changes --commits 10              # last 10 commits
cartog changes --kind function           # only functions


Shows symbols affected by recent git changes, grouped by file.

Doctor (environment health check)
cartog doctor                            # check all requirements
cartog --json doctor                     # structured JSON output


Validates git repo, config, database, embedding provider, and reranker. Returns OK / Warn / Error per check and exits with code 1 if any error. Run this when commands fail unexpectedly or after first setup to verify everything is working.

Stats (index summary)
cartog stats

Watch (auto re-index on file changes)
cartog watch .                           # watch current directory
cartog watch . --rag                     # also re-embed symbols (deferred)
cartog watch . --debounce 3 --rag-delay 30  # custom timings


Watch always uses heuristic-only indexing (no LSP) for speed. Previously LSP-resolved edges are preserved in the DB.

Serve (MCP server)
cartog serve                    # MCP server over stdio
cartog serve --watch            # with background file watcher
cartog serve --watch --rag      # watcher + deferred RAG embedding


When an agent calls cartog_index via MCP, LSP servers are started once and kept warm for the session. Subsequent index calls reuse warm servers (~2s instead of a cold 2-15s startup). Background watch re-indexing stays heuristic-only.

Token Budget

Use --tokens N to limit output to approximately N tokens (human-readable only, ignored with --json):

cartog --tokens 500 search validate
cartog --tokens 200 outline src/db.rs
cartog --tokens 1000 changes --commits 10

JSON Output

All commands support --json for structured output:

cartog --json refs validate_token
cartog --json outline src/auth/tokens.py
cartog --json rag search "authentication"

Refactoring Workflow

Before changing any symbol (rename, extract, move, delete):

cartog search <name> — confirm exact symbol name and file
cartog refs <name> — find every usage
cartog impact <name> --depth 3 — transitive blast radius
cartog hierarchy <name> — if it's a class, check subclasses too
Apply changes, then cartog index . --no-lsp to update the graph
Re-run cartog refs <name> to confirm no stale references remain

For the full 3-phase workflow (heuristic → LSP upgrade → verify), see references/query_cookbook.md → "Assess refactoring scope".

Decision Heuristics
I need to...	Use
Orient in an unfamiliar codebase	cartog map (--tokens N for budget control) — start here
Find code by name, concept, or behavior	cartog rag search "query"
Search project documentation	cartog rag search "query" --kind document
Search both code and docs	cartog rag search "query" --kind all
Get a symbol name for structural commands	cartog search <name>
Know what's in a file	cartog outline <file>
Find usages of a function	cartog refs <name> (--kind calls for just callers)
See what a function calls	cartog callees <name>
Check if a change is safe	cartog impact <name> --depth 3
Understand class hierarchy	cartog hierarchy <class>
See file dependencies	cartog deps <file>
See what changed recently	cartog changes (--commits N for more history)
Improve graph precision for a refactoring	cartog index . (with LSP auto-detected)
Fast re-index after code changes	cartog index . --no-lsp
Diagnose why something is broken	cartog doctor
Read actual implementation logic	cat <file> (cartog indexes structure, not content)
Search for string literals / config	grep (cartog doesn't index these)
Nothing from search or rag	Fall back to grep
Limitations
Heuristic resolution is name-based (~25% of edges resolved). With LSP enabled, ~42-81% resolved depending on language. Remaining unresolved edges are mostly calls to external libraries.
Code languages: Python, TypeScript/JavaScript, Rust, Go, Ruby, Java.
Documents: Markdown (.md) — indexed by heading sections for semantic search.
Does not index string literals, comments (except docstrings), or config values.
Method resolution is name-based without LSP — foo.bar() resolves bar, not Foo.bar specifically. LSP resolves to the exact type when a language server is available.
LSP limitations
Default feature: shipped by default. Installs with --no-default-features omit LSP entirely (equivalent to --no-lsp at runtime).
Auto-detected: if language servers are on PATH, they are used automatically during cartog index. Use --no-lsp to skip.
Startup latency: language servers typically reach ready in 2-15s on cold cache. The default ready-timeout is 20s — override via CARTOG_LSP_READY_TIMEOUT_SECS for very large projects. Day-to-day indexing should use --no-lsp.
CLI vs MCP: each cartog index . via Bash spawns and kills LSP servers (cold start). Use cartog serve (MCP mode) for sessions with multiple index calls — it keeps servers warm across tool calls.
Supported servers: rust-analyzer, pyright-langserver, typescript-language-server, gopls, ruby-lsp, solargraph, jdtls. Install hints shown when servers are missing.
External crate edges stay unresolved: LSP resolves definitions within the project. Calls to std/external crates remain unresolved regardless.
RAG search limitations
No substring matching: "valid" does NOT match validate_token. FTS5 is token-based. If rag search returns no results for a known symbol name, fall back to cartog search which supports substring matching.
Graceful degradation: rag search works without rag setup or rag index (FTS5-only). Quality improves with each setup tier (see Search quality tiers above).
Scores are relative: rrf_score and rerank_score values are only meaningful for ranking within a single query — don't compare scores across different queries.
Re-ranking latency: cross-encoder scores all candidates in a single batch ONNX call (up to 50 candidates). Expect ~150-500ms total overhead depending on candidate count.
Auto re-embed: when cartog upgrades its embedding format (e.g., AST-aware chunking), cartog rag index automatically detects the change and re-embeds all symbols. No --force needed.
Weekly Installs
55
Repository
jrollin/cartog
GitHub Stars
3
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn