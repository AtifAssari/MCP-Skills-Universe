---
rating: ⭐⭐⭐
title: atlassian-mcp
url: https://skills.sh/jeffallan/claude-skills/atlassian-mcp
---

# atlassian-mcp

skills/jeffallan/claude-skills/atlassian-mcp
atlassian-mcp
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill atlassian-mcp
Summary

Jira and Confluence automation via MCP protocol with JQL/CQL queries, ticket management, and sprint workflows.

Supports querying Jira issues with JQL filters, creating and updating tickets with custom fields, and managing sprints and backlogs
Enables searching, creating, and editing Confluence pages using CQL syntax with space and content management
Includes authentication patterns for OAuth 2.0, API tokens, and PAT credentials with permission scope validation
Provides reference guides for server setup, common workflows (issue triage, doc sync, sprint automation), and rate limit handling with pagination
SKILL.md
Atlassian MCP Expert
When to Use This Skill
Querying Jira issues with JQL filters
Searching or creating Confluence pages
Automating sprint workflows and backlog management
Setting up MCP server authentication (OAuth/API tokens)
Syncing meeting notes to Jira tickets
Generating documentation from issue data
Debugging Atlassian API integration issues
Choosing between official vs open-source MCP servers
Core Workflow
Select server - Choose official cloud, open-source, or self-hosted MCP server
Authenticate - Configure OAuth 2.1, API tokens, or PAT credentials
Design queries - Write JQL for Jira, CQL for Confluence; validate with maxResults=1 before full execution
Implement workflow - Build tool calls, handle pagination, error recovery
Verify permissions - Confirm required scopes with a read-only probe before any write or bulk operation
Deploy - Configure IDE integration, test permissions, monitor rate limits
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Server Setup	references/mcp-server-setup.md	Installation, choosing servers, configuration
Jira Operations	references/jira-queries.md	JQL syntax, issue CRUD, sprints, boards, issue linking
Confluence Ops	references/confluence-operations.md	CQL search, page creation, spaces, comments
Authentication	references/authentication-patterns.md	OAuth 2.0, API tokens, permission scopes
Common Workflows	references/common-workflows.md	Issue triage, doc sync, sprint automation
Quick-Start Examples
JQL Query Samples
# Open issues assigned to current user in a sprint
project = PROJ AND status = "In Progress" AND assignee = currentUser() ORDER BY priority DESC

# Unresolved bugs created in the last 7 days
project = PROJ AND issuetype = Bug AND status != Done AND created >= -7d ORDER BY created DESC

# Validate before bulk: test with maxResults=1 first
project = PROJ AND sprint in openSprints() AND status = Open ORDER BY created DESC

CQL Query Samples
# Find pages updated in a specific space recently
space = "ENG" AND type = page AND lastModified >= "2024-01-01" ORDER BY lastModified DESC

# Search page text for a keyword
space = "ENG" AND type = page AND text ~ "deployment runbook"

Minimal MCP Server Configuration
{
  "mcpServers": {
    "atlassian": {
      "command": "npx",
      "args": ["-y", "@sooperset/mcp-atlassian"],
      "env": {
        "JIRA_URL": "https://your-domain.atlassian.net",
        "JIRA_EMAIL": "user@example.com",
        "JIRA_API_TOKEN": "${JIRA_API_TOKEN}",
        "CONFLUENCE_URL": "https://your-domain.atlassian.net/wiki",
        "CONFLUENCE_EMAIL": "user@example.com",
        "CONFLUENCE_API_TOKEN": "${CONFLUENCE_API_TOKEN}"
      }
    }
  }
}


Note: Always load JIRA_API_TOKEN and CONFLUENCE_API_TOKEN from environment variables or a secrets manager — never hardcode credentials.

Constraints
MUST DO
Respect user permissions and workspace access controls
Validate JQL/CQL queries before execution (use maxResults=1 probe first)
Handle rate limits with exponential backoff
Use pagination for large result sets (50-100 items per page)
Implement error recovery for network failures
Log API calls for debugging and audit trails
Test with read-only operations first
Document required permission scopes
Confirm before any write or bulk operation against production data
MUST NOT DO
Hardcode API tokens or OAuth secrets in code
Ignore rate limit headers from Atlassian APIs
Create issues without validating required fields
Skip input sanitization on user-provided query strings
Deploy without testing permission boundaries
Update production data without confirmation prompts
Mix different authentication methods in same session
Expose sensitive issue data in logs or error messages
Output Templates

When implementing Atlassian MCP features, provide:

MCP server configuration (JSON/environment vars)
Query examples (JQL/CQL with explanations)
Tool call implementation with error handling
Authentication setup instructions
Brief explanation of permission requirements

Documentation

Weekly Installs
1.7K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn