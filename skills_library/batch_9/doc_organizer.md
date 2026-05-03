---
title: doc-organizer
url: https://skills.sh/s-hiraoku/synapse-a2a/doc-organizer
---

# doc-organizer

skills/s-hiraoku/synapse-a2a/doc-organizer
doc-organizer
Installation
$ npx skills add https://github.com/s-hiraoku/synapse-a2a --skill doc-organizer
SKILL.md
Doc Organizer

Reorganize scattered documentation into a clear, maintainable structure with a single source of truth for every topic.

Workflow
Audit -- Inventory all docs and classify their topics.
Plan -- Propose restructuring (moves, merges, deletions). Present the plan for confirmation.
Execute -- Apply the changes.
Verify -- Cross-check links, terminology, and completeness.
1) Documentation Audit

Scan the repository for documentation files:

**/*.md, **/*.rst, **/*.txt in root, docs/, guides/, references/
Inline doc comments in config files (YAML, TOML, JSON)

For each file, record:

Primary topic and subtopics covered
Last meaningful update (git log)
Overlap with other files (flag duplicates)
References to code that may have changed (staleness candidates)

Output: a summary table of all docs with topic, location, staleness risk, and duplicate flag.

2) Structure Optimization

Canonical locations:

Content type	Location
Project overview, quickstart	README.md
How-to guides, tutorials	guides/
Architecture, deep-dives	docs/
API/CLI reference specs	references/ or docs/reference/
Per-feature notes	colocated with feature code

Propose a move plan as a table: current path -> target path -> action (move/merge/delete/keep). Present the plan and wait for user confirmation before executing.

3) Deduplication
Identify content repeated across multiple files.
Choose one canonical location; replace duplicates with a short summary and a link.
Prefer the more detailed version as the canonical source.
4) Terminology Normalization
Extract key terms from docs (project name variants, feature names, abbreviations).
Flag inconsistencies (e.g., "config" vs "configuration", "setup" vs "set up").
Apply the project's preferred terminology uniformly.
5) Navigation Improvement
Add or update a table of contents in long documents (>100 lines).
Add cross-links between related docs.
Ensure README.md links to all top-level guide and reference docs.
Create an index page (docs/README.md or docs/index.md) if multiple docs exist without one.
6) Staleness Detection

Compare documentation claims against the current implementation:

CLI flags/options mentioned in docs vs actual --help output or arg parser code.
Config keys documented vs keys in schema/defaults.
API endpoints documented vs route definitions.

Flag mismatches as "needs update" with the specific discrepancy.

Verification Checklist
 No broken internal links (relative paths resolve correctly)
 No orphaned docs (every doc reachable from README or index)
 Terminology consistent across all files
 Examples match current CLI/API behavior
 Duplicate content eliminated (single source of truth per topic)
Weekly Installs
11
Repository
s-hiraoku/synapse-a2a
GitHub Stars
4
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass