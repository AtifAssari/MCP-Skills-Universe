---
rating: ⭐⭐⭐
title: twenty
url: https://skills.sh/vm0-ai/vm0-skills/twenty
---

# twenty

skills/vm0-ai/vm0-skills/twenty
twenty
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill twenty
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name TWENTY_TOKEN or zero doctor check-connector --url https://api.twenty.com/rest/companies --method GET

How to Use
1. List Companies
curl -s -X GET "https://api.twenty.com/rest/companies" --header "Authorization: Bearer $TWENTY_TOKEN" | jq '.data.companies[:3]'


With pagination:

curl -s -X GET "https://api.twenty.com/rest/companies?limit=10&offset=0" --header "Authorization: Bearer $TWENTY_TOKEN" | jq '.data.companies'

2. Create a Company

Write to /tmp/twenty_request.json:

{
  "name": "Acme Corp",
  "domainName": "acme.com",
  "address": "123 Main St, San Francisco, CA"
}


Then run:

curl -s -X POST "https://api.twenty.com/rest/companies" --header "Authorization: Bearer $TWENTY_TOKEN" --header "Content-Type: application/json" -d @/tmp/twenty_request.json

3. List People (Contacts)
curl -s -X GET "https://api.twenty.com/rest/people" --header "Authorization: Bearer $TWENTY_TOKEN" | jq '.data.people[:3]'

4. Create a Person

Write to /tmp/twenty_request.json:

{
  "name": {
    "firstName": "John",
    "lastName": "Doe"
  },
  "email": "john@example.com",
  "phone": "+1234567890"
}


Then run:

curl -s -X POST "https://api.twenty.com/rest/people" --header "Authorization: Bearer $TWENTY_TOKEN" --header "Content-Type: application/json" -d @/tmp/twenty_request.json

5. Get a Specific Record

Note: Replace {companyId} and {personId} with actual IDs obtained from the "List Companies" or "List People" endpoints above (look for the id field in the response).

# Get company by ID
curl -s -X GET "https://api.twenty.com/rest/companies/{companyId}" --header "Authorization: Bearer $TWENTY_TOKEN"

# Get person by ID
curl -s -X GET "https://api.twenty.com/rest/people/{personId}" --header "Authorization: Bearer $TWENTY_TOKEN"

6. Update a Record

Note: Replace {companyId} with an actual company ID from the "List Companies" endpoint above.

Write to /tmp/twenty_request.json:

{
  "name": "Acme Corporation",
  "employees": 500
}


Then run:

curl -s -X PATCH "https://api.twenty.com/rest/companies/{companyId}" --header "Authorization: Bearer $TWENTY_TOKEN" --header "Content-Type: application/json" -d @/tmp/twenty_request.json

7. Delete a Record

Note: Replace {companyId} with an actual company ID from the "List Companies" endpoint above.

curl -s -X DELETE "https://api.twenty.com/rest/companies/{companyId}" --header "Authorization: Bearer $TWENTY_TOKEN"

8. List Notes
curl -s -X GET "https://api.twenty.com/rest/notes" --header "Authorization: Bearer $TWENTY_TOKEN" | jq '.data.notes[:3]'

9. Create a Note

Write to /tmp/twenty_request.json:

{
  "title": "Meeting Notes",
  "body": "Discussed Q1 roadmap and budget allocation."
}


Then run:

curl -s -X POST "https://api.twenty.com/rest/notes" --header "Authorization: Bearer $TWENTY_TOKEN" --header "Content-Type: application/json" -d @/tmp/twenty_request.json

10. List Tasks
curl -s -X GET "https://api.twenty.com/rest/tasks" --header "Authorization: Bearer $TWENTY_TOKEN" | jq '.data.tasks[:3]'

11. Create a Task

Write to /tmp/twenty_request.json:

{
  "title": "Follow up with client",
  "dueAt": "2025-01-15T10:00:00Z",
  "status": "TODO"
}


Then run:

curl -s -X POST "https://api.twenty.com/rest/tasks" --header "Authorization: Bearer $TWENTY_TOKEN" --header "Content-Type: application/json" -d @/tmp/twenty_request.json

12. Get Metadata (Object Schema)

List all object types and their fields:

curl -s -X GET "https://api.twenty.com/rest/metadata/objects" --header "Authorization: Bearer $TWENTY_TOKEN" | jq '.data.objects[] | {name: .nameSingular, fields: [.fields[].name]}'


Get metadata for a specific object:

curl -s -X GET "https://api.twenty.com/rest/metadata/objects/companies" --header "Authorization: Bearer $TWENTY_TOKEN"

13. GraphQL Query

Write to /tmp/twenty_request.json:

{
  "query": "query { companies(first: 5) { edges { node { id name domainName } } } }"
}


Then run:

curl -s -X POST "https://api.twenty.com/graphql" --header "Authorization: Bearer $TWENTY_TOKEN" --header "Content-Type: application/json" -d @/tmp/twenty_request.json | jq '.data.companies.edges'

API Endpoints
Category	Endpoint	Description
Core Objects	/rest/companies	Manage companies
	/rest/people	Manage contacts
	/rest/opportunities	Manage deals/opportunities
	/rest/notes	Manage notes
	/rest/tasks	Manage tasks
	/rest/activities	Activity timeline
Metadata	/rest/metadata/objects	List all object schemas
	/rest/metadata/objects/{name}	Get specific object schema
	/rest/metadata/picklists	Get dropdown field options
GraphQL	/graphql	GraphQL endpoint
Query Parameters
Parameter	Description
limit	Number of records to return (default: 20)
offset	Number of records to skip
filter	Filter conditions (JSON)
orderBy	Sort order

Example with filters:

curl -s -X GET "https://api.twenty.com/rest/companies?filter={\"name\":{\"like\":\"%Acme%\"}}" --header "Authorization: Bearer $TWENTY_TOKEN" | jq '.data.companies'

Response Format
{
  "data": {
  "companies": [
  {
  "id": "uuid",
  "name": "Company Name",
  "domainName": "example.com",
  "createdAt": "2025-01-01T00:00:00Z",
  "updatedAt": "2025-01-01T00:00:00Z"
  }
  ]
  },
  "pageInfo": {
  "hasNextPage": true,
  "endCursor": "cursor-string"
  }
}

Guidelines
API Playground: Test API calls at Settings → APIs & Webhooks in the Twenty app
Rate Limits: Cloud has rate limits; self-hosted has no limits
GraphQL: Use GraphQL for complex queries with relationships
REST: Use REST for simple CRUD operations
Custom Objects: Twenty supports custom objects; use metadata API to discover schema
Webhooks: Set up webhooks at Settings → APIs & Webhooks for real-time events
Resources
API Docs: https://docs.twenty.com/developers/api-and-webhooks/api
Webhooks: https://docs.twenty.com/developers/api-and-webhooks/webhooks
GitHub: https://github.com/twentyhq/twenty
Discord: https://discord.gg/cx5n4Jzs57
Weekly Installs
95
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