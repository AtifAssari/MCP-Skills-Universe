---
title: jira
url: https://skills.sh/vimkim/my-cubrid-skills/jira
---

# jira

skills/vimkim/my-cubrid-skills/jira
jira
Installation
$ npx skills add https://github.com/vimkim/my-cubrid-skills --skill jira
SKILL.md

Look up CUBRID JIRA issue context.

Given a JIRA ticket ID (e.g., CBRD-25123), fetch the issue details from the CUBRID JIRA REST API and present a comprehensive summary. The argument is the ticket ID.

If no ticket ID is provided, ask for one.

$ARGUMENTS

Steps:

First, verify the uv executable exists in PATH by running which uv. If it does not exist, halt immediately and tell the user: "Error: uv is not installed or not in PATH. Install it first: https://docs.astral.sh/uv/getting-started/installation/"

Use the Bash tool to run:

cubrid-jira-search TICKET_ID

Present the output to the user as-is. The command searches local cache first and fetches from JIRA if missing, outputting readable markdown.
If the command fails, inform the user that the JIRA instance may be unreachable or cubrid-jira-search is not installed (uv tool install cubrid-jira-fetcher).
Weekly Installs
9
Repository
vimkim/my-cubrid-skills
GitHub Stars
2
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn