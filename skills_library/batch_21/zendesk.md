---
title: zendesk
url: https://skills.sh/vm0-ai/vm0-skills/zendesk
---

# zendesk

skills/vm0-ai/vm0-skills/zendesk
zendesk
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill zendesk
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name ZENDESK_API_TOKEN or zero doctor check-connector --url https://your-subdomain.zendesk.com/api/v2/tickets.json --method GET

How to Use

All examples assume environment variables are set.

Base URL: https://{subdomain}.zendesk.com/api/v2/

Authentication: API Token via -u flag

-u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN"


Note: The -u flag automatically handles Base64 encoding for you.

Core APIs
1. List Tickets

Get all tickets (paginated):

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" | jq '.tickets[] | {id, subject, status, priority}


With pagination:

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets.json?page=1&per_page=50" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN"

2. Get Ticket

Retrieve a specific ticket:

TICKET_ID="123"

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets/${TICKET_ID}.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN"

3. Create Ticket

Create a new support ticket:

Write to /tmp/zendesk_request.json:

{
  "ticket": {
    "subject": "My printer is on fire!",
    "comment": {
      "body": "The smoke is very colorful."
    },
    "priority": "urgent"
  }
}


Then run:

curl -s -X POST "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json


Create ticket with more details:

Write to /tmp/zendesk_request.json:

{
  "ticket": {
    "subject": "Need help with account",
    "comment": {
      "body": "I cannot access my account settings."
    },
    "priority": "high",
    "status": "open",
    "type": "problem",
    "tags": ["account", "access"]
  }
}


Then run:

curl -s -X POST "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

4. Update Ticket

Update an existing ticket:

TICKET_ID="123"


Write to /tmp/zendesk_request.json:

{
  "ticket": {
    "status": "solved",
    "comment": {
      "body": "Issue has been resolved. Thank you!",
      "public": true
    }
  }
}


Then run:

curl -s -X PUT "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets/${TICKET_ID}.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json


Change priority and assignee:

TICKET_ID="123"
ASSIGNEE_ID="456"


Write to /tmp/zendesk_request.json:

{
  "ticket": {
    "priority": "high",
    "assignee_id": ASSIGNEE_ID_PLACEHOLDER
  }
}


Then run:

sed -i '' "s/ASSIGNEE_ID_PLACEHOLDER/${ASSIGNEE_ID}/" /tmp/zendesk_request.json

curl -s -X PUT "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets/${TICKET_ID}.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

5. Delete Ticket

Permanently delete a ticket:

TICKET_ID="123"

curl -s -X DELETE "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets/${TICKET_ID}.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN"

6. Create Multiple Tickets

Bulk create tickets:

Write to /tmp/zendesk_request.json:

{
  "tickets": [
    {
      "subject": "Ticket 1",
      "comment": {
        "body": "First ticket"
      }
    },
    {
      "subject": "Ticket 2",
      "comment": {
        "body": "Second ticket"
      }
    }
  ]
}


Then run:

curl -s -X POST "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets/create_many.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

7. List Users

Get all users:

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/users.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" | jq '.users[] | {id, name, email, role}

8. Get Current User

Get authenticated user details:

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/users/me.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN"

9. Create User

Create an end-user:

Write to /tmp/zendesk_request.json:

{
  "user": {
    "name": "John Customer",
    "email": "john@example.com",
    "role": "end-user"
  }
}


Then run:

curl -s -X POST "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/users.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json


Create an agent:

Write to /tmp/zendesk_request.json:

{
  "user": {
    "name": "Jane Agent",
    "email": "jane@company.com",
    "role": "agent"
  }
}


Then run:

curl -s -X POST "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/users.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

10. Update User

Update user information:

USER_ID="456"


Write to /tmp/zendesk_request.json:

{
  "user": {
    "name": "Updated Name",
    "phone": "+1234567890"
  }
}


Then run:

curl -s -X PUT "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/users/${USER_ID}.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

11. Search Users

Search for users by query:

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/users/search.json?query=john" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" | jq '.users[] | {id, name, email}

12. List Organizations

Get all organizations:

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/organizations.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" | jq '.organizations[] | {id, name, domain_names}

13. Create Organization

Create a new organization:

Write to /tmp/zendesk_request.json:

{
  "organization": {
    "name": "Acme Inc",
    "domain_names": ["acme.com", "acmeinc.com"],
    "details": "Important customer"
  }
}


Then run:

curl -s -X POST "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/organizations.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

14. Update Organization

Update organization details:

ORG_ID="789"


Write to /tmp/zendesk_request.json:

{
  "organization": {
    "name": "Acme Corporation",
    "notes": "Premium customer since 2020"
  }
}


Then run:

curl -s -X PUT "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/organizations/${ORG_ID}.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

15. List Groups

Get all agent groups:

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/groups.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" | jq '.groups[] | {id, name}

16. Create Group

Create a new agent group:

Write to /tmp/zendesk_request.json:

{
  "group": {
    "name": "Support Team"
  }
}


Then run:

curl -s -X POST "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/groups.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

17. Search API

Search for open tickets:

Write to /tmp/zendesk_query.txt:

type:ticket status:open

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/search.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -G --data-urlencode "query@/tmp/zendesk_query.txt" | jq '.results[] | {id, subject, status}


Search for high priority tickets:

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/search.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -G --data-urlencode "query@/tmp/zendesk_query.txt" | jq '.results[]


Search tickets with keywords:

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/search.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -G --data-urlencode "query@/tmp/zendesk_query.txt" | jq '.results[]


Search users by email domain:

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/search.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -G --data-urlencode "query@/tmp/zendesk_query.txt" | jq '.results[]

18. Get Ticket Comments

List all comments on a ticket:

TICKET_ID="123"

curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets/${TICKET_ID}/comments.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" | jq '.comments[] | {id, body, author_id, public}

19. Assign Ticket to Group

Assign a ticket to a group:

TICKET_ID="123"
GROUP_ID="456"


Write to /tmp/zendesk_request.json:

{
  "ticket": {
    "group_id": GROUP_ID_PLACEHOLDER
  }
}


Then run:

sed -i '' "s/GROUP_ID_PLACEHOLDER/${GROUP_ID}/" /tmp/zendesk_request.json

curl -s -X PUT "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets/${TICKET_ID}.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

20. Bulk Update Tickets

Update multiple tickets at once:

Write to /tmp/zendesk_request.json:

{
  "ticket": {
    "status": "solved"
  }
}


Then run:

curl -s -X PUT "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets/update_many.json?ids=123,124,125" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

Common Workflows
Create Ticket and Assign to Agent

Write to /tmp/zendesk_request.json:

{
  "ticket": {
    "subject": "New issue",
    "comment": {
      "body": "Need help"
    }
  }
}


Then run:

# Create ticket
TICKET_RESPONSE=$(curl -s -X POST "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json)

TICKET_ID=$(echo $TICKET_RESPONSE | jq -r '.ticket.id')

# Assign to agent
ASSIGNEE_ID="789"


Write to /tmp/zendesk_request.json:

{
  "ticket": {
    "assignee_id": ASSIGNEE_ID_PLACEHOLDER,
    "status": "open"
  }
}


Then run:

sed -i '' "s/ASSIGNEE_ID_PLACEHOLDER/${ASSIGNEE_ID}/" /tmp/zendesk_request.json

curl -s -X PUT "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets/${TICKET_ID}.json" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

Find and Close Old Tickets
# Search for old open tickets (30+ days)
OLD_TICKETS="$(curl -s "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/search.json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -G --data-urlencode "query@/tmp/zendesk_query.txt" | jq -r '.results[].id' | paste -sd "," -)"


Write to /tmp/zendesk_request.json:

{
  "ticket": {
    "status": "closed"
  }
}


Then run:

# Bulk close them
curl -s -X PUT "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets/update_many.json?ids=${OLD_TICKETS}" -H "Content-Type: application/json" -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" -d @/tmp/zendesk_request.json

Search Query Syntax
Ticket Search Operators
type:ticket - Search tickets only
status:open - Filter by status (open, pending, solved, closed)
priority:high - Filter by priority (low, normal, high, urgent)
assignee:name - Find tickets assigned to specific agent
group:name - Find tickets in specific group
tags:keyword - Search by tag
created>2024-01-01 - Created after date
created<30 - Created in last 30 days
"exact phrase" - Search exact text
User Search Operators
type:user - Search users only
role:agent - Filter by role (end-user, agent, admin)
email:*@domain.com - Search by email domain
name:john - Search by name
Combining Operators

Use spaces for AND logic:

query=type:ticket status:open priority:high

Rate Limits
Plan	Requests/Minute
Team	200
Growth	400
Professional	400
Enterprise	700
Enterprise Plus	2,500

Special Limits:

Update Ticket: 30 updates per 10 minutes per user per ticket
Account-wide ceiling: 100,000 requests/minute
Rate Limit Headers
X-Rate-Limit: 700                    # Your account's limit
X-Rate-Limit-Remaining: 685          # Requests remaining
Retry-After: 45                      # Seconds to wait if exceeded

Handling Rate Limits
# Use curl retry flags
curl "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/tickets.json" \
  -u "$ZENDESK_EMAIL/token:$ZENDESK_API_TOKEN" \
  --retry 3 --retry-delay 5

Guidelines
Enable API token access first: In Admin Center, ensure Token Access is enabled before using tokens
Always use HTTPS: TLS 1.2+ required
Monitor rate limits: Check X-Rate-Limit-Remaining header
Use bulk operations: create_many, update_many endpoints save API calls
Implement exponential backoff: Honor Retry-After header on 429 responses
Paginate large datasets: Default limit is 100, max per_page is 100
Secure your tokens: Store in environment variables, never in code
Use specific searches: Narrow queries with filters to reduce response size
Verify with reliable endpoints: Use /tickets.json or /users.json to test tokens (not /users/me.json)
Status values: open, pending, hold, solved, closed
Priority values: low, normal, high, urgent
User roles: end-user, agent, admin (need agent or admin role for API access)
Ticket types: problem, incident, question, task
Authentication format: email/token:api_token (curl -u handles encoding)
New workspaces: Fresh Zendesk accounts come with sample tickets for testing
API Reference
Main Documentation: https://developer.zendesk.com/api-reference/
Tickets API: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/
Users API: https://developer.zendesk.com/api-reference/ticketing/users/users/
Organizations API: https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/
Groups API: https://developer.zendesk.com/api-reference/ticketing/groups/groups/
Search API: https://developer.zendesk.com/documentation/ticketing/using-the-zendesk-api/searching-with-the-zendesk-api/
Rate Limits: https://developer.zendesk.com/api-reference/introduction/rate-limits/
Authentication: https://developer.zendesk.com/api-reference/introduction/security-and-auth/
Admin Center: https://www.zendesk.com/admin/
Weekly Installs
67
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