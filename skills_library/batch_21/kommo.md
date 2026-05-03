---
title: kommo
url: https://skills.sh/vm0-ai/vm0-skills/kommo
---

# kommo

skills/vm0-ai/vm0-skills/kommo
kommo
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill kommo
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name KOMMO_API_KEY or zero doctor check-connector --url https://your-subdomain.kommo.com/api/v4/leads --method GET

How to Use

All examples below assume you have environment variables set.

The base URL is: https://${KOMMO_SUBDOMAIN}.kommo.com/api/v4

Authentication uses Bearer token in the Authorization header.

Rate limit: Maximum 7 requests per second.

1. List Leads

Get all leads in your account:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/leads" -H "Accept: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" | jq '.["_embedded"]["leads"][] | {id, name, price}'


With filters:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/leads?limit=10&page=1" -H "Accept: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" | jq '.["_embedded"]["leads"]'

2. Get Lead by ID

Get a specific lead:

Replace <your-lead-id> with the actual lead ID:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/leads/<your-lead-id>" -H "Accept: application/json" -H "Authorization: Bearer $KOMMO_API_KEY"

3. Create Lead

Create a new lead:

Write to /tmp/kommo_request.json:

[{
  "name": "New Lead",
  "price": 5000
}]


Then run:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/leads" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" -d @/tmp/kommo_request.json

4. Create Lead with Contact and Company

Create a lead with associated contact and company:

Write to /tmp/kommo_request.json:

[{
  "name": "Lead with Contact",
  "price": 10000,
  "_embedded": {
    "contacts": [{
      "first_name": "John",
      "last_name": "Doe"
    }],
    "companies": [{
      "name": "Acme Corp"
    }]
  }
}]


Then run:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/leads/complex" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" -d @/tmp/kommo_request.json

5. Update Lead

Update an existing lead:

Write to /tmp/kommo_request.json:

{
  "price": 7500,
  "name": "Updated Lead Name"
}


Then run:

Replace <your-lead-id> with the actual lead ID:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/leads/<your-lead-id>" -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" -d @/tmp/kommo_request.json

6. List Contacts

Get all contacts:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/contacts" -H "Accept: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" | jq '.["_embedded"]["contacts"][] | {id, name}'

7. Get Contact by ID

Get a specific contact:

Replace <your-contact-id> with the actual contact ID:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/contacts/<your-contact-id>" -H "Accept: application/json" -H "Authorization: Bearer $KOMMO_API_KEY"

8. Create Contact

Create a new contact:

Write to /tmp/kommo_request.json:

[{
  "first_name": "Jane",
  "last_name": "Smith"
}]


Then run:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/contacts" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" -d @/tmp/kommo_request.json

9. List Companies

Get all companies:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/companies" -H "Accept: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" | jq '.["_embedded"]["companies"][] | {id, name}'

10. Create Company

Create a new company:

Write to /tmp/kommo_request.json:

[{
  "name": "New Company Inc"
}]


Then run:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/companies" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" -d @/tmp/kommo_request.json

11. List Tasks

Get all tasks:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/tasks" -H "Accept: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" | jq '.["_embedded"]["tasks"][] | {id, text, complete_till}'

12. Create Task

Create a new task (use Unix timestamp for complete_till):

Write to /tmp/kommo_request.json:

[{
  "text": "Follow up with client",
  "complete_till": 1735689600,
  "task_type_id": 1
}]


Then run:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/tasks" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" -d @/tmp/kommo_request.json


Task types: 1 = Follow-up, 2 = Meeting

13. List Pipelines

Get all sales pipelines:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/leads/pipelines" -H "Accept: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" | jq '.["_embedded"]["pipelines"][] | {id, name}'

14. Get Pipeline Stages

Get stages for a specific pipeline:

Replace <your-pipeline-id> with the actual pipeline ID:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/leads/pipelines/<your-pipeline-id>" -H "Accept: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" | jq '.["_embedded"]["statuses"][] | {id, name}'

15. Get Account Info

Get account information:

curl -s "https://$KOMMO_SUBDOMAIN.kommo.com/api/v4/account" -H "Accept: application/json" -H "Authorization: Bearer $KOMMO_API_KEY" | jq '{id, name, subdomain, currency}'

Response Format
Lead Response
{
  "id": 12345,
  "name": "Lead Name",
  "price": 5000,
  "responsible_user_id": 123,
  "pipeline_id": 456,
  "status_id": 789
}

Contact Response
{
  "id": 12345,
  "name": "John Doe",
  "first_name": "John",
  "last_name": "Doe"
}

Guidelines
Rate limit: Maximum 7 requests per second, 429 returned if exceeded
Array format: POST requests for creating entities expect an array of objects
Use pagination: Add ?limit=N&page=N for large result sets
Task timestamps: complete_till is Unix timestamp in seconds
If-Modified-Since: Use this header for efficient polling of list endpoints
Weekly Installs
75
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