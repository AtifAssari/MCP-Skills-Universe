---
title: wiki-dashboard
url: https://skills.sh/ar9av/obsidian-wiki/wiki-dashboard
---

# wiki-dashboard

skills/ar9av/obsidian-wiki/wiki-dashboard
wiki-dashboard
Installation
$ npx skills add https://github.com/ar9av/obsidian-wiki --skill wiki-dashboard
SKILL.md
Wiki Dashboard — Dynamic Vault Views

You are creating a .base file — an Obsidian Bases definition that turns vault frontmatter into a live, queryable view. The .base format is native to Obsidian 1.8+ and requires no plugins.

Before You Start
Read ~/.obsidian-wiki/config (preferred) or .env (fallback) to get OBSIDIAN_VAULT_PATH
Read $OBSIDIAN_VAULT_PATH/index.md to understand what categories and pages exist
Ask the user what they want to view if not specified — what folder, tag, category, or date range?
What Obsidian Bases Can Do

.base files define database-style views over vault notes. Each file declares:

Which notes to include — filtered by folder, tag, frontmatter property, or combination
Which properties to show — any frontmatter field becomes a column
What view type — table, cards, or list
Sort and group — by any property
Computed columns — formulas using file.* helpers and arithmetic

Embed a .base into any note with ![[MyBase.base]].

Step 1: Understand the Request

Determine:

What to show — all pages in a category? Pages with a specific tag? A project's pages?
What columns matter — title, tags, created, updated, summary, category, project?
View type — table (default), cards (visual), or list (minimal)
Sort order — by updated (default), created, title, or a custom property
Any filters — date range, specific tags, folder scope
Step 2: Generate the .base File

The .base format is YAML. Here are the patterns you'll use:

Basic table — all pages in a category folder
filters:
  - type: folder
    folder: concepts
columns:
  - property: file.name
    title: Page
  - property: tags
    title: Tags
  - property: summary
    title: Summary
  - property: updated
    title: Updated
sort:
  - property: updated
    direction: desc
view: table

Filtered by tag
filters:
  - type: tag
    tag: "#machine-learning"
columns:
  - property: file.name
    title: Page
  - property: category
    title: Category
  - property: summary
    title: Summary
  - property: created
    title: Created
sort:
  - property: created
    direction: desc
view: table

Multi-filter (folder AND tag)
filters:
  operator: and
  conditions:
    - type: folder
      folder: projects
    - type: tag
      tag: "#active"
columns:
  - property: file.name
    title: Project
  - property: summary
    title: Summary
  - property: updated
    title: Last Updated
view: cards

Computed column (days since last update)
columns:
  - property: file.name
    title: Page
  - property: updated
    title: Updated
  - formula: "floor((now() - updated) / 86400000)"
    title: Days Stale
    type: number
sort:
  - formula: "floor((now() - updated) / 86400000)"
    direction: desc
view: table

Filter operators and functions available
file.hasTag("tag") — boolean, true if page has tag
file.inFolder("path") — boolean, true if page is in folder
file.name — the note's filename (without extension)
file.path — full vault-relative path
now() — current timestamp in ms
Arithmetic: +, -, *, /, floor(), ceil()
Comparison: ==, !=, >, <, >=, <=
Step 3: Write the File

Target path: $OBSIDIAN_VAULT_PATH/_meta/<dashboard-name>.base

Use a slug derived from the dashboard's purpose:

"All concepts" → _meta/concepts-index.base
"Recent ingests" → _meta/recent-ingests.base
"Project overview" → _meta/projects-overview.base
"Stale pages" → _meta/stale-pages.base

Create _meta/ if it doesn't exist yet.

Step 4: Embed (optional)

If the user wants the dashboard embedded in an existing note (e.g., index.md or a project overview), add:

## <Dashboard Title>

![[_meta/<dashboard-name>.base]]


Ask the user before modifying an existing note.

Step 5: Update Tracking

log.md — Append:

- [TIMESTAMP] WIKI_DASHBOARD name="<slug>" view=<type> filter="<description>"


No manifest or index update needed — .base files are live queries, not static content pages.

Common Dashboard Recipes

Tell the user about these if they're not sure what to ask for:

Dashboard	What it shows
Content index	All wiki pages grouped by category, sortable by updated date
Entity tracker	All entity pages (people, tools, orgs) with tags and sources
Ingestion log	Pages sorted by created date — see what was added recently
Stale content	Pages not updated in 30+ days — maintenance view
Project overview	All project pages with last-sync date
Tag cloud	Pages grouped by tag — see coverage across topics
Research tracker	All synthesis pages tagged research — shows research history
Quality Checklist
 .base YAML is valid and uses correct field names
 Filter matches the user's intent
 File written to _meta/ with a descriptive slug
 log.md updated
 User told how to embed it (![[_meta/<name>.base]]) and what Obsidian version is required (1.8+)
Weekly Installs
453
Repository
ar9av/obsidian-wiki
GitHub Stars
893
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass