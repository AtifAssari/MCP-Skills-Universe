---
title: linear
url: https://skills.sh/vm0-ai/vm0-skills/linear
---

# linear

skills/vm0-ai/vm0-skills/linear
linear
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill linear
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name LINEAR_TOKEN or zero doctor check-connector --url https://api.linear.app/graphql --method POST

How to Use

All examples below assume you have LINEAR_TOKEN set.

Base URL: https://api.linear.app/graphql

Linear uses GraphQL for all API operations. Queries retrieve data, mutations modify data.

1. List Teams

Get all teams in your workspace:

Write to /tmp/linear_request.json:

{
  "query": "{ teams { nodes { id name key } } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.teams.nodes'


Save a team ID for subsequent queries.

2. List Issues for a Team

Get issues from a specific team. Replace <your-team-id> with the actual team ID:

Write to /tmp/linear_request.json:

{
  "query": "{ team(id: \"<your-team-id>\") { issues { nodes { id identifier title state { name } assignee { name } } } } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.team.issues.nodes'

3. Get Issue by Identifier

Fetch a specific issue by its identifier (e.g., ENG-123):

Write to /tmp/linear_request.json:

{
  "query": "{ issue(id: \"ENG-123\") { id identifier title description state { name } priority assignee { name } createdAt } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.issue'

4. Search Issues

Search issues with filters:

Write to /tmp/linear_request.json:

{
  "query": "{ issues(filter: { state: { name: { eq: \"In Progress\" } } }, first: 10) { nodes { id identifier title assignee { name } } } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.issues.nodes'

5. Create Issue

Create a new issue in a team. Replace <your-team-id> with the actual team ID:

Write to /tmp/linear_request.json:

{
  "query": "mutation { issueCreate(input: { title: \"Bug: Login button not working\", description: \"Users report the login button is unresponsive on mobile.\", teamId: \"<your-team-id>\" }) { success issue { id identifier title url } } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.issueCreate'

6. Create Issue with Priority and Labels

Create an issue with additional properties. Replace <your-team-id> and <your-label-id> with actual IDs:

Write to /tmp/linear_request.json:

{
  "query": "mutation { issueCreate(input: { title: \"High priority task\", teamId: \"<your-team-id>\", priority: 1, labelIds: [\"<your-label-id>\"] }) { success issue { id identifier title priority } } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.issueCreate'


Priority values: 0 (No priority), 1 (Urgent), 2 (High), 3 (Medium), 4 (Low)

7. Update Issue

Update an existing issue. Replace <your-issue-id> with the actual issue ID:

Write to /tmp/linear_request.json:

{
  "query": "mutation { issueUpdate(id: \"<your-issue-id>\", input: { title: \"Updated title\", priority: 2 }) { success issue { id identifier title priority } } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.issueUpdate'

8. Change Issue State

Move an issue to a different state (e.g., "Done"). Replace <your-issue-id> and <your-state-id> with actual IDs:

Write to /tmp/linear_request.json:

{
  "query": "mutation { issueUpdate(id: \"<your-issue-id>\", input: { stateId: \"<your-state-id>\" }) { success issue { id identifier state { name } } } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.issueUpdate'

9. List Workflow States

Get available states for a team. Replace <your-team-id> with the actual team ID:

Write to /tmp/linear_request.json:

{
  "query": "{ team(id: \"<your-team-id>\") { states { nodes { id name type } } } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.team.states.nodes'

10. Add Comment to Issue

Add a comment to an existing issue. Replace <your-issue-id> with the actual issue ID:

Write to /tmp/linear_request.json:

{
  "query": "mutation { commentCreate(input: { issueId: \"<your-issue-id>\", body: \"This is a comment from the API.\" }) { success comment { id body createdAt } } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.commentCreate'

11. List Projects

Get all projects in the workspace:

Write to /tmp/linear_request.json:

{
  "query": "{ projects { nodes { id name state progress targetDate } } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.projects.nodes'

12. Get Current User

Get information about the authenticated user:

Write to /tmp/linear_request.json:

{
  "query": "{ viewer { id name email admin } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.viewer'

13. List Labels

Get available labels for a team. Replace <your-team-id> with the actual team ID:

Write to /tmp/linear_request.json:

{
  "query": "{ team(id: \"<your-team-id>\") { labels { nodes { id name color } } } }"
}


Then run:

curl -s -X POST "https://api.linear.app/graphql" -H "Content-Type: application/json" -H "Authorization: $LINEAR_TOKEN" -d @/tmp/linear_request.json | jq '.data.team.labels.nodes'

Finding IDs

To find IDs for teams, issues, projects, etc.:

Open Linear app
Press Cmd/Ctrl + K to open command menu
Type "Copy model UUID"
Select the entity to copy its ID

Or use the queries above to list entities and extract their IDs.

Guidelines
Use GraphQL variables: For production, use variables instead of string interpolation for better security
Handle pagination: Use first, after, last, before for paginated results
Check for errors: GraphQL returns 200 even with errors; always check the errors array
Rate limiting: Implement backoff if you receive rate limit errors
Batch operations: Combine multiple queries in one request when possible
Issue identifiers: You can use either UUID or readable identifier (e.g., ENG-123) for most queries
Weekly Installs
64
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass