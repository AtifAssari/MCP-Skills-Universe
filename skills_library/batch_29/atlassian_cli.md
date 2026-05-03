---
title: atlassian-cli
url: https://skills.sh/miguelez11/skills/atlassian-cli
---

# atlassian-cli

skills/miguelez11/skills/atlassian-cli
atlassian-cli
Installation
$ npx skills add https://github.com/miguelez11/skills --skill atlassian-cli
SKILL.md
Atlassian CLI (acli)
Auth
acli auth login          # authenticate (stores credentials globally)
acli jira auth login     # jira-specific login if needed

Jira: View & Search
# View a ticket (default fields: key, type, summary, status, assignee, description)
acli jira workitem view KEY-123
acli jira workitem view KEY-123 --fields '*all'        # all fields
acli jira workitem view KEY-123 --fields summary,comment
acli jira workitem view KEY-123 --json

# Search with JQL
acli jira workitem search --jql "project = TEAM AND status = 'In Progress'"
acli jira workitem search --jql "assignee = '@me' AND sprint in openSprints()"
acli jira workitem search --jql "project = TEAM" --fields "key,summary,status" --paginate
acli jira workitem search --jql "project = TEAM" --limit 20 --json

# List projects
acli jira project list

Jira: Create & Edit
# Create
acli jira workitem create --summary "Fix login bug" --project "TEAM" --type "Bug"
acli jira workitem create --summary "..." --project "PROJ" --type "Story" \
  --assignee "user@example.com" --description "Details here"
acli jira workitem create --editor   # opens $EDITOR for summary + description

# Edit
acli jira workitem edit --key KEY-123 --summary "Updated summary"
acli jira workitem edit --key KEY-123 --assignee "@me"
acli jira workitem edit --key KEY-123 --description "New description" --yes

# Transition status
acli jira workitem transition --key KEY-123 --status "In Progress"
acli jira workitem transition --key KEY-123 --status "Done" --yes

# Delete
acli jira workitem delete --key KEY-123

Jira: Comments
# List comments
acli jira workitem comment list --key KEY-123
acli jira workitem comment list --key KEY-123 --paginate

# Add a comment
acli jira workitem comment create --key KEY-123 --body "Looks good to merge"
acli jira workitem comment create --key KEY-123 --editor   # opens $EDITOR
acli jira workitem comment create --key KEY-123 --body-file comment.txt

Jira: Sprints & Boards
acli jira board search                                   # list boards
acli jira board list-sprints --id <board-id>            # sprints on a board
acli jira sprint list-workitems --id <sprint-id>        # tickets in a sprint

Confluence

Note: acli confluence only supports space-level operations — there is no page viewer. To read a Confluence page (e.g. an ADR), open it in the browser from the space view.

acli confluence space list                   # list all spaces
acli confluence space view --id <space-id>   # view space details
acli confluence space view --id <space-id> --include-all

Tips
Use --json on any command to pipe into jq for scripting
Use --jql with JQL for powerful batch operations (edit/comment/transition multiple tickets)
Common JQL patterns:
assignee = currentUser() — your tickets
sprint in openSprints() AND project = TEAM — active sprint
updated >= -7d AND project = TEAM — recently updated
labels = "adr" — find ADRs by label
Weekly Installs
13
Repository
miguelez11/skills
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass