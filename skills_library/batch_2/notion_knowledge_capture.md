---
title: notion-knowledge-capture
url: https://skills.sh/openai/skills/notion-knowledge-capture
---

# notion-knowledge-capture

skills/openai/skills/notion-knowledge-capture
notion-knowledge-capture
Installation
$ npx skills add https://github.com/openai/skills --skill notion-knowledge-capture
Summary

Capture conversations and decisions into structured, linkable Notion pages for wikis, how-tos, FAQs, and decision logs.

Supports six content types: decisions, how-to guides, FAQs, wiki entries, learning notes, and documentation pages, each with dedicated database templates and schemas.
Includes a five-step workflow: define capture purpose, locate the target database, extract and structure content, create or update the Notion page, and link from related hub pages.
Provides reference guides for database schemas, required properties (title, tags, owner, status, dates, relations), and capture patterns with examples.
Requires Notion MCP setup via OAuth; includes troubleshooting steps if the MCP connection fails during page creation or search operations.
SKILL.md
Knowledge Capture

Convert conversations and notes into structured, linkable Notion pages for easy reuse.

Quick start
Clarify what to capture (decision, how-to, FAQ, learning, documentation) and target audience.
Identify the right database/template in reference/ (team wiki, how-to, FAQ, decision log, learning, documentation).
Pull any prior context from Notion with Notion:notion-search → Notion:notion-fetch (existing pages to update/link).
Draft the page with Notion:notion-create-pages using the database’s schema; include summary, context, source links, and tags/owners.
Link from hub pages and related records; update status/owners with Notion:notion-update-page as the source evolves.
Workflow
0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
Add the Notion MCP:
codex mcp add notion --url https://mcp.notion.com/mcp
Enable remote MCP client:
Set [features].rmcp_client = true in config.toml or run codex --enable rmcp_client
Log in with OAuth:
codex mcp login notion

After successful login, the user will have to restart codex. You should finish your answer and tell them so when they try again they can continue with Step 1.

1) Define the capture
Ask purpose, audience, freshness, and whether this is new or an update.
Determine content type: decision, how-to, FAQ, concept/wiki entry, learning/note, documentation page.
2) Locate destination
Pick the correct database using reference/*-database.md guides; confirm required properties (title, tags, owner, status, date, relations).
If multiple candidate databases, ask the user which to use; otherwise, create in the primary wiki/documentation DB.
3) Extract and structure
Extract facts, decisions, actions, and rationale from the conversation.
For decisions, record alternatives, rationale, and outcomes.
For how-tos/docs, capture steps, pre-reqs, links to assets/code, and edge cases.
For FAQs, phrase as Q&A with concise answers and links to deeper docs.
4) Create/update in Notion
Use Notion:notion-create-pages with the correct data_source_id; set properties (title, tags, owner, status, dates, relations).
Use templates in reference/ to structure content (section headers, checklists).
If updating an existing page, fetch then edit via Notion:notion-update-page.
5) Link and surface
Add relations/backlinks to hub pages, related specs/docs, and teams.
Add a short summary/changelog for future readers.
If follow-up tasks exist, create tasks in the relevant database and link them.
References and examples
reference/ — database schemas and templates (e.g., team-wiki-database.md, how-to-guide-database.md, faq-database.md, decision-log-database.md, documentation-database.md, learning-database.md, database-best-practices.md).
examples/ — capture patterns in practice (e.g., decision-capture.md, how-to-guide.md, conversation-to-faq.md).
Weekly Installs
1.0K
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass