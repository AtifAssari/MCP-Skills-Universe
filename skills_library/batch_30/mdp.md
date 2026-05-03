---
title: mdp
url: https://skills.sh/varunpandey0502/markdown-projects/mdp
---

# mdp

skills/varunpandey0502/markdown-projects/mdp
mdp
Installation
$ npx skills add https://github.com/varunpandey0502/markdown-projects --skill mdp
SKILL.md
mdp — Markdown Project Management

A file-based project management CLI. Projects live in .mdp/ directories containing markdown files with YAML frontmatter.

IMPORTANT: On first use

When you start working with an existing project, immediately read .mdp/settings.json to learn the project's valid statuses, types, labels, and priorities, and read .mdp/project.md for project identity, health, and instructions. Do not guess or assume defaults — the config is the source of truth. Statuses are grouped by category (e.g., completed, started), and only the name field within each status is used in commands.

Installation
bun install -g github:varunpandey0502/markdown-projects


See INSTALL.md for details.

Quick start
mdp project create -p . --preset software
mdp issue create -p . -t "Fix login bug" --type bug --priority High
mdp issue list -p .
mdp issue update -p . --id ISS-1 -s "In Progress"

Project structure
.mdp/
├── settings.json          # Schema config: statuses, priorities, labels, types (committed)
├── project.md             # Project identity: title, description, instructions, health, log (committed)
├── issues/                # Flat directory of issue folders
│   └── ISS-1-add-auth/
│       └── ISS-1-add-auth.md
├── milestones/            # Flat directory of milestone folders
│   └── M-1-v1-release/
│       └── M-1-v1-release.md
├── docs/                  # Documentation
└── templates/             # Issue/milestone templates

Configuration

Schema config is stored in .mdp/settings.json with entity-scoped objects:

{
  "issues": {
    "prefix": "ISS",
    "statuses": {
      "triage": [], "backlog": [...], "unstarted": [...],
      "started": [...], "completed": [...], "canceled": []
    },
    "priorities": [...], "labels": [...], "types": [...]
  },
  "milestones": {
    "prefix": "M",
    "statuses": {
      "backlog": [], "planned": [...], "in_progress": [...],
      "completed": [...], "canceled": []
    },
    "priorities": [...], "labels": [...]
  }
}


Project identity is stored in .mdp/project.md with YAML frontmatter:

---
title: My Project
description: Optional one-line project description
instructions: Optional free-text guidance for LLMs and collaborators
health: on-track
log: []
createdAt: 2025-01-01T00:00:00.000Z
updatedAt: 2025-01-01T00:00:00.000Z
---


Statuses are grouped by status category (lifecycle stage). Each category maps to an array of { name, description } status objects. The system uses categories (not status names) to determine completion, overdue detection, etc.

Issues and milestones have independent statuses, priorities, and labels.

At runtime, .mdp/settings.json is the sole source of truth for schema config — no merge layers.

At project creation: preset (built-in or custom from ~/.mdp/settings.json) → CLI flag overrides → written to settings.json.

Custom presets and default preferences (default preset, output format) are stored in ~/.mdp/settings.json.

Global options

Every command accepts: -p <path> (project path), -f json|table (output format), -q (quiet), -V (verbose).

All output is JSON: { "ok": true, "data": {...} } or { "ok": false, "error": {...} }.

Commands
Project management
mdp project create -p <path> [--preset <name>] [-F|--force] [--with-templates] [--no-with-templates] [--issue-prefix <prefix>] [--milestone-prefix <prefix>] [--tags <tags>] [--title <title>] [--description <desc>] [--instructions <text>] — Create a new project (presets: software, marketing, design, product, social-media, generic)
mdp project get -p <path> [--no-include-content] — Get project identity, health, log, and body
mdp project settings -p <path> — Show project schema settings
mdp project stats -p <path> — Project statistics
mdp project fix -p <path> [--dry-run] — Fix folder structure to match frontmatter
Project log

Manage log entries on the project (stored in .mdp/project.md):

mdp project log add -p <path> -b "message" [--author <name>] [--health on-track|at-risk|off-track] [--dry-run]
mdp project log list -p <path>
mdp project log get -p <path> --index <n>
mdp project log update -p <path> --index <n> [-b <body>] [--author <name>] [--health <health>] [--dry-run]
mdp project log delete -p <path> --index <n> [--dry-run]
Project registry

Manage projects in ~/.mdp/settings.json:

mdp project list [--tag <tag>] — List registered projects (includes tagDescriptions in output)
mdp project add <path> [--tags <tags>]
mdp project remove <path>
mdp project tag <path> --add <tags> | --remove <tags> — Tags added via --add are auto-created globally
Tags

Manage tags globally via mdp tag:

mdp tag list — List all tags with descriptions and project counts
mdp tag add <tag> [-d "description"] — Create a tag (description defaults to "")
mdp tag update <tag> -d "description" — Update a tag's description
mdp tag remove <tag> [--force] — Remove a tag; --force to also strip from projects
Issues
Create
mdp issue create -p <path> -t "Title" [options]

Option	Description
-t, --title <title>	Issue title (required)
--type <type>	Issue type (config-driven)
-s, --status <status>	Initial status (default: first status in config)
--priority <priority>	Priority level (default: null)
-l, --labels <labels>	Comma-separated labels
-a, --assignee <assignee>	Assignee identifier
-m, --milestone <milestone>	Milestone ID
-e, --estimate <estimate>	Effort points (positive integer)
--spent <spent>	Actual effort spent
--due-date <date>	Due date (YYYY-MM-DD)
--blocked-by <ids>	Comma-separated issue IDs
--parent <id>	Parent issue ID
--related-to <ids>	Comma-separated issue IDs
--checklist <items>	Comma-separated checklist items
-d, --description <desc>	Short description
-c, --content <content>	Full markdown body (or - for stdin)
--template <name>	Template name from .mdp/templates/
--dry-run	Preview without creating
List
mdp issue list -p <path> [options]

Option	Description
-s, --status <statuses>	Comma-separated status filter
--type <types>	Comma-separated type filter
--priority <priority>	Priority filter
-l, --labels <labels>	Comma-separated labels filter
-a, --assignee <assignee>	Filter by assignee (none for unassigned)
-m, --milestone <milestone>	Filter by milestone ID (none for unassigned)
--blocked <bool>	true for blocked only, false for unblocked
--parent <id>	Filter by parent issue ID (none for top-level)
--created-after <date>	Created after date (YYYY-MM-DD)
--created-before <date>	Created before date (YYYY-MM-DD)
--due-before <date>	Due before date (YYYY-MM-DD)
--due-after <date>	Due after date (YYYY-MM-DD)
--sort <field>	Sort: id, title, status, priority, type, created, updated, estimate, spent, dueDate (default: id)
--order <order>	Sort order: asc, desc (default: asc)
Get
mdp issue get -p <path> --id <id> [--no-include-content]

Update
mdp issue update -p <path> --id <id> [options]

Option	Description
-t, --title <title>	New title
--type <type>	New type
-s, --status <status>	New status
--priority <priority>	New priority
-a, --assignee <assignee>	Set assignee (none to clear)
-m, --milestone <milestone>	Set milestone (none to clear)
-e, --estimate <estimate>	Set estimate (none to clear)
--spent <spent>	Set spent (none to clear)
--due-date <date>	Set due date (none to clear)
--parent <id>	Set parent issue (none to clear)
-l, --labels <labels>	Set labels (replaces all)
--add-labels <labels>	Add labels
--remove-labels <labels>	Remove labels
--blocked-by <ids>	Set blockedBy (replaces all)
--add-blocked-by <ids>	Add to blockedBy (with cycle detection)
--remove-blocked-by <ids>	Remove from blockedBy
--related-to <ids>	Set relatedTo (replaces all)
--add-related-to <ids>	Add to relatedTo
--remove-related-to <ids>	Remove from relatedTo
--add-checklist <items>	Add checklist items
--remove-checklist <items>	Remove checklist items by text
--check <items>	Check items by text
--uncheck <items>	Uncheck items by text
-c, --content <content>	Replace markdown body
--dry-run	Preview without writing
Delete
mdp issue delete -p <path> --id <id> [--dry-run]


Cleans up blockedBy, relatedTo, and parent references in other issues.

Log

Manage log entries on an issue.

mdp issue log add -p <path> --id <id> -b "message" [--author <name>] [--dry-run]
mdp issue log list -p <path> --id <id>
mdp issue log get -p <path> --id <id> --index <n>
mdp issue log update -p <path> --id <id> --index <n> [--author <a>] [-b <body>] [--dry-run]
mdp issue log delete -p <path> --id <id> --index <n> [--dry-run]

Batch create

Create multiple issues at once by piping a JSON array via stdin. Processes items sequentially; continues on error and reports per-item success/failure.

echo '<json-array>' | mdp issue batch-create -p <path> [--dry-run]


Input: JSON array of issue objects. Required field: title. All other fields match issue create options (type, status, priority, labels, assignee, milestone, estimate, spent, dueDate, blockedBy, parent, relatedTo, checklist, description, content, template). Array fields (labels, blockedBy, etc.) accept string[].

Output:

{
  "ok": true,
  "data": {
    "total": 3, "succeeded": 2, "failed": 1,
    "results": [
      { "ok": true, "data": { "id": "ISS-4", "title": "...", "filePath": "..." } },
      { "ok": false, "error": { "code": "INVALID_STATUS", "message": "...", "index": 2 } }
    ]
  }
}


Exits with code 1 if any item failed.

Batch update

Update multiple issues at once by piping a JSON array via stdin. Processes items sequentially; continues on error and reports per-item success/failure. In-memory state is refreshed after each successful update for accurate cycle detection.

echo '<json-array>' | mdp issue batch-update -p <path> [--dry-run]


Input: JSON array of update objects. Required field: id. All other fields match issue update options (title, type, status, priority, labels, addLabels, removeLabels, assignee, milestone, estimate, spent, dueDate, blockedBy, addBlockedBy, removeBlockedBy, parent, relatedTo, addRelatedTo, removeRelatedTo, addChecklist, removeChecklist, check, uncheck, content). Array fields accept string[].

Output: Same envelope format as batch-create, with changes and filePath per item.

Exits with code 1 if any item failed.

Milestones
Create
mdp milestone create -p <path> -t "Title" [options]

Option	Description
-t, --title <title>	Milestone title (required)
-s, --status <status>	Initial status (default: first status in config)
--priority <priority>	Priority level (default: null)
-l, --labels <labels>	Comma-separated labels
--start-date <date>	Start date (YYYY-MM-DD)
--due-date <date>	Due date (YYYY-MM-DD)
--checklist <items>	Comma-separated checklist items
-d, --description <desc>	Short description
-c, --content <content>	Full markdown body
--template <name>	Template name from .mdp/templates/
--dry-run	Preview without creating
List
mdp milestone list -p <path> [options]

Option	Description
-s, --status <statuses>	Comma-separated status filter
--priority <priority>	Priority filter
-l, --labels <labels>	Comma-separated labels filter
--overdue <bool>	true for overdue only, false for not overdue
--sort <field>	Sort: id, title, status, priority, created, updated, dueDate, completion (default: id)
--order <order>	Sort order: asc, desc (default: asc)
Get
mdp milestone get -p <path> --id <id> [--no-include-content]

Update
mdp milestone update -p <path> --id <id> [options]

Option	Description
-t, --title <title>	New title
-s, --status <status>	New status
--priority <priority>	New priority
--start-date <date>	Set start date (none to clear)
--due-date <date>	Set due date (none to clear)
-l, --labels <labels>	Set labels (replaces all)
--add-labels <labels>	Add labels
--remove-labels <labels>	Remove labels
--add-checklist <items>	Add checklist items
--remove-checklist <items>	Remove checklist items by text
--check <items>	Check items by text
--uncheck <items>	Uncheck items by text
-c, --content <content>	Replace markdown body
--dry-run	Preview without writing
Delete
mdp milestone delete -p <path> --id <id> [--dry-run]


Clears milestone reference from all assigned issues.

Progress
mdp milestone progress -p <path> --id <id>


Returns completion percentage, issue counts by status, and list of assigned issues.

Log

Manage log entries on a milestone.

mdp milestone log add -p <path> --id <id> -b "message" [--author <name>] [--dry-run]
mdp milestone log list -p <path> --id <id>
mdp milestone log get -p <path> --id <id> --index <n>
mdp milestone log update -p <path> --id <id> --index <n> [--author <a>] [-b <body>] [--dry-run]
mdp milestone log delete -p <path> --id <id> --index <n> [--dry-run]

Search
mdp search -p <path> -q "query text" [--limit <n>]


Searches project, issues, and milestones by text content using BM25 ranking. Returns matched fields with snippets. Use --entity project to search only the project file.

Workflow recommendations
Start with mdp project create -p . --preset software to set up a project
Create issues with mdp issue create — use --type and --labels for organization
For bulk operations, use mdp issue batch-create and mdp issue batch-update with JSON arrays piped via stdin
Move issues through statuses with mdp issue update --id ISS-1 -s "In Progress"
Group work into milestones, then track with mdp milestone progress
Use mdp issue list with filters to find relevant issues

See WORKFLOWS.md for detailed workflow patterns.

References
INSTALL.md — Installation guide
WORKFLOWS.md — Detailed workflow patterns
PROJECTS.md — Project commands reference
ISSUES.md — Issue commands reference
MILESTONES.md — Milestone commands reference
PROJECT-CONFIG.md — Project configuration reference
GLOBAL-CONFIG.md — Global configuration reference
Weekly Installs
9
Repository
varunpandey0502…projects
First Seen
Feb 3, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass