---
title: recall
url: https://skills.sh/parcadei/continuous-claude-v3/recall
---

# recall

skills/parcadei/continuous-claude-v3/recall
recall
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill recall
SKILL.md
Recall - Semantic Memory Retrieval

Query the memory system for relevant learnings from past sessions.

Usage
/recall <query>

Examples
/recall hook development patterns
/recall wizard installation
/recall TypeScript errors

What It Does
Runs semantic search against stored learnings (PostgreSQL + BGE embeddings)
Returns top 5 results with full content
Shows learning type, confidence, and session context
Execution

When this skill is invoked, run:

cd $CLAUDE_OPC_DIR && PYTHONPATH=. uv run python scripts/core/recall_learnings.py --query "<ARGS>" --k 5


Where <ARGS> is the query provided by the user.

Output Format

Present results as:

## Memory Recall: "<query>"

### 1. [TYPE] (confidence: high, id: abc123)
<full content>

### 2. [TYPE] (confidence: medium, id: def456)
<full content>

Options

The user can specify options after the query:

--k N - Return N results (default: 5)
--vector-only - Use pure vector search (higher precision)
--text-only - Use text search only (faster)

Example: /recall hook patterns --k 10 --vector-only

Weekly Installs
302
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail