---
title: db-investigator
url: https://skills.sh/191341025/self-evolving-skill/db-investigator
---

# db-investigator

skills/191341025/self-evolving-skill/db-investigator
db-investigator
Installation
$ npx skills add https://github.com/191341025/self-evolving-skill --skill db-investigator
SKILL.md
Tool Selection
Need	Tool
Data investigation (counts, WHERE, GROUP BY, JOIN)	db_query.py
Table structure (DDL, columns, indexes, sample rows)	fetch_structure.py --tables
SP/Function source code	fetch_structure.py --procedures
Database overview (list all objects)	fetch_index.py

Decision flow: Data question → db_query.py. Structure → fetch_structure.py. Don't know what exists → fetch_index.py.

Tool experience: When a query pattern or parameter combination proves especially effective (or a pitfall is discovered), note it in the relevant references/ file alongside the query template or investigation flow.

Initialization

On first use or new environment, run: python $S/decay_engine.py init

Creates references/ directory + _index.md template + db_config.ini template
Idempotent: safe to re-run, skips existing files
After init: edit db_config.ini with database credentials before any queries
Precondition Check

AI must verify before ANY investigation:

Check if $S/db_config.ini exists
If missing → tell user: "Run python .claude/skills/db-investigator/scripts/setup.py to configure database connection"
Do NOT attempt any database queries without valid configuration
Check if references/_index.md exists
If missing → run: python $S/decay_engine.py init
Domain Knowledge System
Selective Loading Protocol

Domain knowledge lives in references/ as a topic-based structure:

Always read references/_index.md first — lightweight routing table
Identify task-relevant entities (table names like t_employee, SP names like sp_settle, column names — technical identifiers only, NOT Chinese descriptions)
Run: python $S/decay_engine.py search --path $S/../references/ --entities "<names>" --level TRUST
Load only matched files; for VERIFY entries, flag for opportunistic verification
REVALIDATE entries: verify with tools BEFORE using
If no entities identified or search returns empty → fall back to topic-based file selection from _index.md
Knowledge Governance Protocol

Before modifying any knowledge file, pass all five gates in order:

Gate 1 — VALUE: Is this domain knowledge?
  Pure operational output (e.g., "query ran successfully", "export done") → REJECT
  Domain fact, relationship, data characteristic, or pattern → PROCEED
  (Let Gate 4 decay handle freshness — data_snapshot decays in ~14 days automatically)

Gate 2 — ALIGNMENT: Contradicts existing knowledge?
  1. Extract entity names from new knowledge — must be technical identifiers (table names like t_employee, SP names, column names) that match <!-- entities: --> tags; NOT Chinese business descriptions
  2. Run: python $S/decay_engine.py search --path $S/../references/ --entities "<names>"
  3. For each match: compare new knowledge with the existing entry
     - Full contradiction → CORRECT existing entry (feedback --result failure on old)
     - Partial overlap → MERGE or keep both (note differences)
     - No contradiction → proceed
  4. If no search results → proceed to Gate 3

Gate 3 — REDUNDANCY: Already captured (possibly different wording)?
  1. Use search results from Gate 2 (same entity matches)
  2. For each match: is the new knowledge semantically equivalent?
     - Same fact, different wording → SKIP (do not add)
     - Same entity, different fact → proceed (not redundant)
  3. If no matches or no redundancy → proceed to Gate 4

Gate 4 — FRESHNESS (write): Assign decay metadata + entities
  → Classify type: schema | business_rule | tool_experience |
                    query_pattern | data_range | data_snapshot
  → Extract entity names as technical identifiers (table/SP/column names)
  → Write both tags:
    <!-- decay: type=<type> confirmed=<YYYY-MM-DD> C0=1.0 -->
    <!-- entities: <entity1>, <entity2> -->
  → High-decay types (data_range/data_snapshot): prefer rejection

Gate 4 — FRESHNESS (read): On-demand confidence scan
  → Run: python $S/decay_engine.py scan --file <topic_file>
  → TRUST: use directly, no mention of confidence
  → VERIFY: use but flag for opportunistic verification
  → REVALIDATE: verify with tools BEFORE using

Gate 4 — FRESHNESS (feedback): After operations using knowledge
  Hard signals (weight=1.0, default):
    → SQL execution success/failure involving known columns/tables
    → Structure query match/mismatch with known schema
    → Numeric comparison within/outside ±5% of recorded value
    Command: python $S/decay_engine.py feedback --file $S/../references/<f> --line <n> --result success|failure

  Soft signals (weight=0.3):
    → Gate 2 ALIGNMENT correction (β+0.3 on corrected entry)
    → Empty result on enum/status value query:
      - Value came from existing knowledge → soft FAILURE (knowledge may be wrong)
      - Value was user-supplied and NOT in known enum → soft SUCCESS (confirms completeness)
      - Value source unclear → do NOT record feedback
    → User explicit confirmation of result correctness
    Command: python $S/decay_engine.py feedback --file $S/../references/<f> --line <n> --result success|failure --weight 0.3

  No clear outcome → do NOT record feedback

  After REVALIDATE passes:
    python $S/decay_engine.py reset --file $S/../references/<f> --line <n>

Decay boundary rules:
  → Never auto-delete entries even if C→0; deletion requires user confirmation
  → Confidence resets only via reset command after tool-verified revalidation
  → If REVALIDATE finds contradiction → Gate 2 (ALIGNMENT) takes priority

Gate 5 — PLACEMENT: Which topic file? Which memory tier?
  Structure knowledge → schema_map.md
  Business rules → business_rules.md
  Reusable SQL → query_patterns.md
  Multi-step investigation procedure → investigation_flows.md
  New topic needed → only if 3+ related facts justify a new file
  Update _index.md if new file created OR existing file's scope changed significantly


Default outcome is NO CHANGE for Gates 2-5 (deduplication, redundancy). But Gate 1 should pass most domain facts through — freshness is managed by Gate 4's decay model, not by upfront rejection.

Human Entry Points
Human injection: When user explicitly shares domain knowledge
  (signals: "记住", "注意这个", "这个要记下来", "remember this")
  → Treat as knowledge candidate
  → Run Gate 1-3 (VALUE / ALIGNMENT / REDUNDANCY) as normal
  → If all pass:
    python $S/decay_engine.py inject --type <t> --content "<c>" --target <f> --entities "<e1>,<e2>"
  → If any gate fails: explain why to user, do not write

Human correction: When user indicates existing knowledge is wrong
  (signals: "这个变了", "这条不对", "这个规则已经废弃了")
  → Identify the knowledge entry in references/
  → Run: python $S/decay_engine.py invalidate --file $S/../references/<f> --line <n>
  → Immediately treat as REVALIDATE: verify with tools before further use

Scaling Rules
Single topic file exceeds ~80 lines → split into sub-topics
Total topic files exceed 8 → review for consolidation
_index.md must stay under 40 lines (pure routing, no detail)
Active check: After each knowledge write, verify the target file's line count; if approaching 80, plan the split before next write
Post-Investigation Checkpoint

Execute after EVERY investigation, before moving on. Non-negotiable.

Feedback: If references/ knowledge was loaded and used during this investigation:
Query confirmed the knowledge → feedback --result success
Query contradicted the knowledge → feedback --result failure
No clear signal → skip (do NOT force feedback)
Capture: Gate 1 — is any finding domain knowledge?
Pure operational output (e.g., "query ran", "export done") → stop here
Domain fact, relationship, data characteristic, or pattern → run full Gates 2-5 (Knowledge Governance Protocol)
Default is no action. But this evaluation must still happen — it takes seconds and is the only mechanism through which this skill evolves.
Commands
S=".claude/skills/db-investigator/scripts"

# Database tools
python $S/db_query.py --sql "<SELECT>" --database <db> [--limit N]
python $S/fetch_structure.py --tables <t>[,t2] [--sample N] [--database <db>]
python $S/fetch_structure.py --procedures <sp>[,sp2] [--database <db>]
python $S/fetch_index.py [--database <db>]

# Initialization
python $S/decay_engine.py init

# Knowledge lifecycle
python $S/decay_engine.py scan --file $S/../references/<topic_file>
python $S/decay_engine.py scan --path $S/../references/
python $S/decay_engine.py search --path $S/../references/ --entities "<names>" [--level TRUST|VERIFY|REVALIDATE]
python $S/decay_engine.py search --path $S/../references/ [--min-confidence 0.8]
python $S/decay_engine.py feedback --file $S/../references/<f> --line <n> --result success|failure [--weight 0.3]
python $S/decay_engine.py reset --file $S/../references/<f> --line <n>
python $S/decay_engine.py inject --type <t> --content "<c>" --target <f> [--entities "<e1>,<e2>"]
python $S/decay_engine.py invalidate --file $S/../references/<f> --line <n>

Constraints
Read-only enforced: db_query.py whitelist-validates SQL (SELECT/SHOW/DESCRIBE/EXPLAIN only)
Write operations: Generate SQL and present to user for manual execution
No credentials in output: never print db_config.ini content
Timeout: connect_timeout=10s, read_timeout=30s; retry once or narrow scope
Cached schemas: db_schemas/ has previously fetched structures — check before re-fetching
Weekly Installs
12
Repository
191341025/self-…ng-skill
GitHub Stars
19
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass