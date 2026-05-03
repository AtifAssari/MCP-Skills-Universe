---
title: jira
url: https://skills.sh/89jobrien/steve/jira
---

# jira

skills/89jobrien/steve/jira
jira
Installation
$ npx skills add https://github.com/89jobrien/steve --skill jira
SKILL.md
Jira Integration Skill

This skill enables direct interaction with Jira Cloud via REST API v3 and JQL queries.

Prerequisites

Set these environment variables (or in .env file):

JIRA_DOMAIN=company.atlassian.net
JIRA_EMAIL=user@company.com
JIRA_API_TOKEN=your-api-token


Generate API tokens at: https://id.atlassian.com/manage-profile/security/api-tokens

Core Workflows
1. Get Issue Details

To retrieve issue information:

python scripts/jira_api.py GET /issue/PROJ-123


With specific fields:

python scripts/jira_api.py GET "/issue/PROJ-123?fields=summary,status,assignee"

2. Search with JQL

To search issues using JQL:

python scripts/jira_api.py GET /search --query "jql=project=AOP AND status='In Progress'&maxResults=20"


Common JQL patterns - see references/jql-reference.md:

My open issues: assignee = currentUser() AND resolution = Unresolved
Recent updates: updated >= -1d ORDER BY updated DESC
Sprint work: sprint in openSprints() AND assignee = currentUser()
3. Create Issue

To create a new issue, use ADF format for description (see references/adf-format.md):

python scripts/jira_api.py POST /issue --data '{
  "fields": {
    "project": { "key": "PROJ" },
    "issuetype": { "name": "Task" },
    "summary": "Issue title",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [{ "type": "text", "text": "Description here" }]
        }
      ]
    }
  }
}'

4. Update Issue

To update fields on an existing issue:

python scripts/jira_api.py PUT /issue/PROJ-123 --data '{
  "fields": {
    "summary": "Updated title",
    "labels": ["label1", "label2"]
  }
}'

5. Add Comment

To add a comment (requires ADF format):

python scripts/jira_api.py POST /issue/PROJ-123/comment --data '{
  "body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [{ "type": "text", "text": "Comment text here" }]
      }
    ]
  }
}'

6. Transition Issue Status

First, get available transitions:

python scripts/jira_api.py GET /issue/PROJ-123/transitions


Then transition to new status:

python scripts/jira_api.py POST /issue/PROJ-123/transitions --data '{
  "transition": { "id": "21" }
}'

7. Assign Issue

To assign an issue:

# Get user account ID first
python scripts/jira_api.py GET "/user/search?query=username"

# Then assign
python scripts/jira_api.py PUT /issue/PROJ-123/assignee --data '{
  "accountId": "user-account-id"
}'


To unassign:

python scripts/jira_api.py PUT /issue/PROJ-123/assignee --data '{"accountId": null}'

Direct curl Usage

For quick operations without the helper script:

JIRA_DOMAIN="company.atlassian.net"
AUTH=$(echo -n "$JIRA_EMAIL:$JIRA_API_TOKEN" | base64)

curl -s "https://$JIRA_DOMAIN/rest/api/3/issue/PROJ-123" \
  -H "Authorization: Basic $AUTH" \
  -H "Content-Type: application/json"

Reference Files
references/api-endpoints.md - Complete REST API v3 endpoint reference
references/jql-reference.md - JQL operators, functions, fields, and patterns
references/adf-format.md - Atlassian Document Format for rich text fields
Common Patterns
Bulk Operations

To get multiple issues efficiently:

python scripts/jira_api.py GET /search --query "jql=key in (PROJ-1,PROJ-2,PROJ-3)"

Get Project Info

To list projects or get project details:

python scripts/jira_api.py GET /project
python scripts/jira_api.py GET /project/PROJ

Get Available Issue Types
python scripts/jira_api.py GET "/project/PROJ?expand=issueTypes"

Error Handling

Common error codes:

400: Bad request - check JSON syntax and field names
401: Unauthorized - verify credentials
403: Forbidden - check user permissions
404: Not found - verify issue key exists
429: Rate limited - wait and retry

For field validation errors, Jira returns detailed error messages indicating which fields are invalid.

Weekly Installs
18
Repository
89jobrien/steve
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass