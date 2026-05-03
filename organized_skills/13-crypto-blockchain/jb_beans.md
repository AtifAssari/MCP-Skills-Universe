---
rating: ⭐⭐⭐
title: jb-beans
url: https://skills.sh/bjesuiter/skills/jb-beans
---

# jb-beans

skills/bjesuiter/skills/jb-beans
jb-beans
Installation
$ npx skills add https://github.com/bjesuiter/skills --skill jb-beans
SKILL.md
beans - Flat-File Issue Tracker

Use beans to track work as markdown files alongside a project.

First step for agents

Before starting work in a beans-enabled project, run:

beans prime


Read and follow its output. It may define project-specific workflow rules, issue types, statuses, and expectations for how agents should create/update beans.

Why beans?
Flat files — issues live as markdown in .beans/
Git-friendly — changes can be reviewed and committed like code
Agent-friendly — supports --json, structured relationships, and context priming
Portable — no server or database required
Installation
# Via Homebrew
brew install hmans/beans/beans

# Via Go
go install github.com/hmans/beans@latest

Setup
# Initialize beans in the current project
beans init

# Validate config and bean graph
beans check

# Show installed version
beans version

Global flags

Most commands support these global flags:

--config <path>       # Use a specific .beans.yml
--beans-path <path>   # Override the data directory
--json                # Use structured machine-readable output where supported


For agent workflows, prefer --json whenever you plan to parse output.

Core workflow
# 1. Inspect project-specific guidance
beans prime

# 2. Find existing work
beans list --json --ready
beans list --json -S "login"

# 3. Create work if needed
beans create --json "Add login screen" -t feature -s todo -d "Build the initial login UI"

# 4. Start work
beans update --json <id> -s in-progress

# 5. Keep the bean current while working
beans update --json <id> --body-append "## Notes\n\nStarted implementation"

# 6. Finish work
beans update --json <id> -s completed --body-append "## Summary of Changes\n\nImplemented the feature and validated behavior."

Issue model
Types

Current CLI-supported types:

milestone
epic
bug
feature
task
Statuses

Current CLI-supported statuses:

in-progress
todo
draft
completed
scrapped
Priorities

Current CLI-supported priorities:

critical
high
normal
low
deferred
Core commands
Prime the agent context
beans prime


Outputs instructions for AI coding agents, often including:

required workflow rules
project-specific types/statuses
command usage preferences
when to create, complete, or archive beans

Always check this first in beans-enabled repos.

Create beans
# Minimal
beans create "Implement user login" -t feature

# Agent-friendly
beans create --json "Fix auth race" -t bug -s in-progress -p high -d "Repro under parallel refresh"

# With tags
beans create --json "Refactor API client" -t task --tag tech-debt --tag networking

# With relationships
beans create --json "Add billing UI" -t feature --parent <epic-id>
beans create --json "Ship migration" -t task --blocked-by <other-id>
beans create --json "Unblock deploy" -t task --blocking <other-id>

# Read body from stdin or file
printf 'Implementation notes' | beans create "Document rollout" -t task -d -
beans create "Import fixtures" -t task --body-file notes.md


Useful flags:

-t, --type
-s, --status
-p, --priority
-d, --body
--body-file
--tag
--parent
--blocking
--blocked-by
--prefix
--json
List beans
# List everything
beans list
beans list --json

# Ready to start
beans list --json --ready

# Filter by status/type/tag/priority
beans list --json -s todo -t bug
beans list --json --tag urgent
beans list --json -p high

# Search
beans list --json -S "login"
beans list --json -S 'title:login'
beans list --json -S 'body:authentication'
beans list --json -S '"user login"'
beans list --json -S 'login~'

# Relationship filters
beans list --json --parent <id>
beans list --json --has-parent
beans list --json --no-parent
beans list --json --has-blocking
beans list --json --no-blocking
beans list --json --is-blocked

# Other output modes
beans list --json --full
beans list --quiet
beans list --sort updated


Notes:

--ready excludes blocked, in-progress, completed, scrapped, and draft beans.
--quiet outputs only IDs, one per line.
Search uses Bleve query syntax.
Show bean details
beans show <id>
beans show <id> <id2>
beans show --json <id>
beans show --body-only <id>
beans show --raw <id>
beans show --etag-only <id>


Use --etag-only when doing optimistic locking with updates.

Update beans
# Status/title/type/priority
beans update --json <id> -s in-progress
beans update --json <id> --title "New title"
beans update --json <id> -t feature -p high

# Tags
beans update --json <id> --tag urgent --tag auth
beans update --json <id> --remove-tag urgent

# Relationships
beans update --json <id> --parent <epic-id>
beans update --json <id> --remove-parent
beans update --json <id> --blocked-by <other-id>
beans update --json <id> --remove-blocked-by <other-id>
beans update --json <id> --blocking <other-id>
beans update --json <id> --remove-blocking <other-id>

# Replace body entirely
beans update --json <id> -d "Updated body"
beans update --json <id> --body-file notes.md

# Append to body
beans update --json <id> --body-append "## Notes\n\nExtra context"
printf '## Summary\n\nDone.' | beans update --json <id> --body-append -

# Exact single replacement in body
beans update --json <id> \
  --body-replace-old "- [ ] Add tests" \
  --body-replace-new "- [x] Add tests"

# Combine metadata + body edits
beans update --json <id> \
  -s completed \
  --body-append "## Summary of Changes\n\nImplemented and verified."

Concurrency-safe updates
ETAG=$(beans show <id> --etag-only)
beans update --json <id> --if-match "$ETAG" -s in-progress


Use --if-match to avoid overwriting concurrent edits.

Delete beans
beans delete <id>
beans delete <id> <id2>
beans delete --json <id>     # implies --force
beans delete -f <id>


If other beans reference the target, beans warns and removes those references after confirmation. -f skips prompts and warnings.

Archive completed work
beans archive
beans archive --json


Moves all completed and scrapped beans into .beans/archive/.

Archive only when appropriate for the project workflow or when the user asks. Archived beans are preserved for project memory and remain visible in queries.

Validate configuration and integrity
beans check
beans check --json
beans check --fix


Checks for:

config errors
broken links
self-links
circular dependencies

--fix can repair broken links and self-links automatically.

Generate roadmaps
beans roadmap
beans roadmap --json
beans roadmap --include-done
beans roadmap --status todo
beans roadmap --no-status completed
beans roadmap --link-prefix https://example.com/beans/
beans roadmap --no-links


Use this for milestone/epic rollups and markdown planning views.

Query with GraphQL
# The command is beans graphql; beans query is an alias
beans graphql '{ beans { id title status } }'
beans graphql --json '{ bean(id: "abc") { title body } }'
beans graphql -v '{"id":"abc"}' 'query GetBean($id: ID!) { bean(id: $id) { title } }'
beans graphql --schema


Examples:

# Actionable work
beans graphql --json '{ beans(filter: { excludeStatus: ["completed", "scrapped"], isBlocked: false }) { id title status type } }'

# High priority bugs
beans graphql --json '{ beans(filter: { type: ["bug"], priority: ["critical", "high"] }) { id title } }'

# Traverse relationships
beans graphql --json '{ bean(id: "abc") { title parent { title } children { id title status } blockedBy { id title } } }'

TUI
beans tui


Current CLI help indicates this has moved to beans-tui. Do not rely on beans tui for real workflows unless the separate beans-tui tool is installed/configured.

Relationships

Beans support structured relationships:

Parent: hierarchy like milestone → epic → feature → task
Blocking: this bean blocks another bean
Blocked-by: this bean is blocked by another bean

Examples:

beans update --json child-1 --parent epic-1
beans update --json task-2 --blocked-by task-1
beans update --json infra-1 --blocking release-1

Recommended agent usage patterns
Always prefer JSON when parsing
beans list --json --ready
beans show --json <id>
beans create --json "Title" -t task
beans update --json <id> -s in-progress

Keep bean bodies current

Use body content for:

checklists
implementation notes
reproduction steps
summaries of changes
reasons for scrapping work
Make narrow body replacements

When updating checklists or notes, use exact replacement instead of rewriting the whole body when possible:

beans update <id> \
  --body-replace-old "- [ ] Ship release" \
  --body-replace-new "- [x] Ship release"

Prefer relationships over ad-hoc text

Use --parent, --blocking, and --blocked-by instead of only mentioning dependencies in freeform notes.

Integration notes
OpenCode

The beans prime output can be injected into agent context via an OpenCode plugin.

Codex / Pi / Claude Code

At minimum, add a rule to project instructions like:

Before starting work in this repo, run `beans prime` and follow its output.

Tips
Run beans prime first in beans-enabled projects
Use --json for agent-readable output
Use beans version, not beans --version
Use beans graphql for advanced filtering and relationship traversal
Treat beans tui as deprecated/moved unless beans-tui is available
Use beans check after large edits or relationship changes
Links
GitHub: https://github.com/hmans/beans
Documentation: https://github.com/hmans/beans#readme
Weekly Installs
13
Repository
bjesuiter/skills
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass