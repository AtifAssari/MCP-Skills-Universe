---
title: omni-content-explorer
url: https://skills.sh/exploreomni/omni-agent-skills/omni-content-explorer
---

# omni-content-explorer

skills/exploreomni/omni-agent-skills/omni-content-explorer
omni-content-explorer
Installation
$ npx skills add https://github.com/exploreomni/omni-agent-skills --skill omni-content-explorer
SKILL.md
Omni Content Explorer

Find, browse, and organize Omni content — dashboards, workbooks, and folders — through the Omni CLI.

Prerequisites
# Verify the Omni CLI is installed — if not, ask the user to install it
# See: https://github.com/exploreomni/cli#readme
command -v omni >/dev/null || echo "ERROR: Omni CLI is not installed."

# Show available profiles and select the appropriate one
omni config show
# If multiple profiles exist, ask the user which to use, then switch:
omni config use <profile-name>

Discovering Commands
omni content --help     # Content operations
omni documents --help   # Document operations
omni folders --help     # Folder operations


Tip: Use -o json to force structured output for programmatic parsing, or -o human for readable tables. The default is auto (human in a TTY, JSON when piped).

Browsing Content
List All Content
omni content list

With Counts and Labels
omni content list --include '_count,labels'

Filter and Sort
# By label
omni content list --labels finance,marketing

# By scope
omni content list --scope organization

# Sort by popularity or recency
omni content list --sortfield favorites

omni content list --sortfield updatedAt

Pagination

Responses include pageInfo with cursor-based pagination. Fetch next page:

omni content list --cursor <nextCursor>

Working with Documents
List Documents
omni documents list

# Filter by creator
omni documents list --creatorid <userId>


Each document includes: identifier, name, type, scope, owner, folder, labels, updatedAt, hasDashboard.

Important: Always use the identifier field for API calls, not id. The id field is null for workbook-type documents and will cause silent failures.

Get Document Queries

Retrieve query definitions powering a dashboard's tiles:

omni documents get-queries <identifier>


Useful for understanding what a dashboard computes and re-running queries via omni-query.

Folders
# List
omni folders list

# Create
omni folders create "Q1 Reports" --scope organization

Labels
# List labels
omni labels list

# Add label to document
omni documents add-label <identifier> <labelName>

# Remove label
omni documents remove-label <identifier> <labelName>

Favorites
# Favorite
omni documents add-favorite <identifier>

# Unfavorite
omni documents remove-favorite <identifier>

Dashboard Downloads
# Start download (async)
omni dashboards download <dashboardId> --body '{ "format": "pdf" }'

# Poll job status
omni dashboards download-status <dashboardId> <jobId>


Formats: pdf, png

URL Patterns

Construct direct links to content:

Dashboard: {OMNI_BASE_URL}/dashboards/{identifier}
Workbook:  {OMNI_BASE_URL}/w/{identifier}


The identifier comes from the document's identifier field in API responses. Always provide the user a clickable link after finding content.

Search Patterns

When scanning all documents for field references (e.g., for impact analysis), paginate with cursor and call omni documents get-queries <identifier> for each document. Launch multiple query-fetch calls in parallel for efficiency. For field impact analysis, prefer the content-validator approach in omni-model-explorer.

Docs Reference
Content API · Documents API · Folders API · Labels API · Dashboard Downloads
Related Skills
omni-query — run queries behind dashboards you've found
omni-content-builder — create or update dashboards
omni-embed — embed dashboards you've found in external apps
omni-admin — manage permissions on documents and folders
Weekly Installs
19
Repository
exploreomni/omn…t-skills
GitHub Stars
12
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass