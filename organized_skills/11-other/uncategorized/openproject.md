---
rating: ⭐⭐⭐
title: openproject
url: https://skills.sh/hoangvantuan/claude-plugin/openproject
---

# openproject

skills/hoangvantuan/claude-plugin/openproject
openproject
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill openproject
SKILL.md
OpenProject CLI

Single-command interface for OpenProject. All operations via op.py.

Quick Start
# From skill directory:
cd skills/openproject

# 1. First time: init config (only once per project)
uv run python op.py init 13

# 2. Check status
uv run python op.py status

# 3. Start working
uv run python op.py wp list --status open

Setup
cd skills/openproject
uv sync


Configure .env:

OPENPROJECT_URL=https://your-instance.com
OPENPROJECT_API_KEY=your-api-key


API key from: OpenProject → My Account → Access Tokens

CLI Commands

All commands: cd skills/openproject && uv run python op.py <command>

System
Command	Description
status	Check connection + config status
init <project_id>	Init config for project (once)
config	Show full config (types, statuses, members, custom fields)
Work Packages (wp)
Command	Description
wp list [options]	List work packages
wp get <id>	Get single work package
wp create --subject "..." [options]	Create work package
wp update <id> [options]	Update work package
wp delete <id>	Delete work package
wp comment <id> --message "..."	Add comment
wp activities <id>	List activities/comments
wp relations <id>	List WP relations
wp add-relation <from> <to> --type blocks	Create relation
wp del-relation <relation_id>	Delete relation
wp schema --type-id N	Get form schema

wp list filters: --status open|closed|all|"name" --type "Task" --assignee "name" --parent N --project N --limit N

wp create/update: --subject --type --status --priority --assignee --responsible --description --parent --version --start-date --due-date --estimated-hours --done --cf "key=val"

relation types: relates|blocks|blocked|precedes|follows|duplicates|includes|partof|requires

Time Tracking (time)
Command	Description
time log <wp_id> --hours N	Log time entry
time list [options]	List time entries
time today	Today's entries for current user
time get <id>	Get time entry
time update <id> [options]	Update time entry
time delete <id>	Delete time entry
time activities	List activity types

time log: --hours N (required) --comment "..." --date YYYY-MM-DD --activity N

time list: --wp N --user "name" --date --from-date --to-date --limit N

time update: --hours N --comment "..." --date --wp N --activity N

Projects (project)
Command	Description
project list	List all projects
project get <id>	Get project
project create --name "..."	Create project
project update <id> [options]	Update project
project delete <id>	Delete project
project versions [--id N]	List versions
project categories [--id N]	List categories

project create: --name --identifier --description --parent N --public

Notifications (notif)
Command	Description
notif list [--unread] [--reason X]	List notifications
notif count	Unread count
notif read <id>	Mark as read
notif unread <id>	Mark as unread
notif read-all	Mark all read

notif reasons: mentioned|assigned|watched|responsible|commented|created|prioritized|scheduled

Users (user)
Command	Description
user list	List all users
user get <id>	Get user
user me	Current user info
Lookups (from config cache)
Command	Description
members	Project members (name + user_id)
types	WP types (Task, Bug, etc.)
statuses	All statuses
priorities	All priorities
Examples
# List open tasks assigned to Hung NB
uv run python op.py wp list --status open --assignee "Hung NB" --type Task

# Create a bug
uv run python op.py wp create --subject "Login page broken" --type Bug --priority High

# Update status and assignee
uv run python op.py wp update 675 --status "In progress" --assignee "Hung NB"

# Add comment to WP
uv run python op.py wp comment 675 --message "Fixed in commit abc123"

# Create a relation: WP 100 blocks WP 200
uv run python op.py wp add-relation 100 200 --type blocks

# Log 2.5 hours
uv run python op.py time log 675 --hours 2.5 --comment "Fixed login bug"

# Get today's logged time
uv run python op.py time today

# Time entries for date range
uv run python op.py time list --from-date 2026-02-01 --to-date 2026-02-28 --user "Tuan HV"

# Check unread notifications
uv run python op.py notif count

# List unread notifications
uv run python op.py notif list --unread --limit 10

# Get current user
uv run python op.py user me

# List project versions
uv run python op.py project versions

Output Format

All commands output JSON. Example:

{"count": 2, "work_packages": [{"id": 675, "subject": "Login page", "type": "Bug", "status": "In progress"}]}

⚠️ Important Notes
Name resolution uses config cache. Refresh with: uv run python op.py init <project_id>
Custom fields are project/type specific. Use op.py config to see available ones.
op.py auto-loads .env — no manual load_dotenv() needed.
Advanced: Python API

For complex operations not covered by CLI, use Python packages directly:

uv run python -c "
from openproject_work_packages import list_work_packages
for wp in list_work_packages(project_id=13):
    print(wp['subject'])
"


Sub-package docs:

Package	SKILL.md
openproject_core	openproject-core/SKILL.md
openproject_projects	openproject-projects/SKILL.md
openproject_work_packages	openproject-work-packages/SKILL.md
openproject_time	openproject-time/SKILL.md
openproject_users	openproject-users/SKILL.md
openproject_documents	openproject-documents/SKILL.md
openproject_queries	openproject-queries/SKILL.md
openproject_notifications	openproject-notifications/SKILL.md
openproject_admin	openproject-admin/SKILL.md
Python API Gotchas
list_* functions return generators → use list(...) to convert
Time hours is ISO 8601 duration (e.g., PT1H30M) → use parse_duration()
update_work_package() auto-fetches lockVersion if not provided
get_schema() requires both project_id AND type_id
Weekly Installs
20
Repository
hoangvantuan/cl…e-plugin
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn