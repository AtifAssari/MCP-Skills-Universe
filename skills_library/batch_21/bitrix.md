---
title: bitrix
url: https://skills.sh/vm0-ai/vm0-skills/bitrix
---

# bitrix

skills/vm0-ai/vm0-skills/bitrix
bitrix
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill bitrix
SKILL.md
How to Use

All examples assume BITRIX_WEBHOOK_URL is set to your webhook base URL.

1. Get Current User

Get information about the authenticated user:

curl -s -X GET "$BITRIX_WEBHOOK_URL/user.current.json"


Response:

{
  "result": {
  "ID": "1",
  "NAME": "John",
  "LAST_NAME": "Doe",
  "EMAIL": "john@example.com"
  }
}

2. List Users

Get a list of users in the workspace:

curl -s -X GET "$BITRIX_WEBHOOK_URL/user.get.json" | jq '.result[] | {ID, NAME, LAST_NAME, EMAIL}'

CRM - Leads
3. Create a Lead

Write to /tmp/bitrix_request.json:

{
  "fields": {
    "TITLE": "New Lead from API",
    "NAME": "John",
    "LAST_NAME": "Doe",
    "PHONE": [{"VALUE": "+1234567890", "VALUE_TYPE": "WORK"}],
    "EMAIL": [{"VALUE": "john@example.com", "VALUE_TYPE": "WORK"}]
  }
}


Then run:

curl -s -X POST "$BITRIX_WEBHOOK_URL/crm.lead.add.json" --header "Content-Type: application/json" -d @/tmp/bitrix_request.json


Response:

{
  "result": 123
}

4. Get a Lead

Replace <your-lead-id> with the actual lead ID:

curl -s -X GET "$BITRIX_WEBHOOK_URL/crm.lead.get.json?id=<your-lead-id>"

5. List Leads
curl -s -X GET "$BITRIX_WEBHOOK_URL/crm.lead.list.json" | jq '.result[] | {ID, TITLE, STATUS_ID}'


With filter:

Write to /tmp/bitrix_request.json:

{
  "filter": {"STATUS_ID": "NEW"},
  "select": ["ID", "TITLE", "NAME", "PHONE"]
}


Then run:

curl -s -X POST "$BITRIX_WEBHOOK_URL/crm.lead.list.json" --header "Content-Type: application/json" -d @/tmp/bitrix_request.json

6. Update a Lead

Write to /tmp/bitrix_request.json:

{
  "id": 123,
  "fields": {
    "STATUS_ID": "IN_PROCESS",
    "COMMENTS": "Updated via API"
  }
}


Then run:

curl -s -X POST "$BITRIX_WEBHOOK_URL/crm.lead.update.json" --header "Content-Type: application/json" -d @/tmp/bitrix_request.json

7. Delete a Lead

Replace <your-lead-id> with the actual lead ID:

curl -s -X GET "$BITRIX_WEBHOOK_URL/crm.lead.delete.json?id=<your-lead-id>"

CRM - Contacts
8. Create a Contact

Write to /tmp/bitrix_request.json:

{
  "fields": {
    "NAME": "Jane",
    "LAST_NAME": "Smith",
    "PHONE": [{"VALUE": "+1987654321", "VALUE_TYPE": "MOBILE"}],
    "EMAIL": [{"VALUE": "jane@example.com", "VALUE_TYPE": "WORK"}]
  }
}


Then run:

curl -s -X POST "$BITRIX_WEBHOOK_URL/crm.contact.add.json" --header "Content-Type: application/json" -d @/tmp/bitrix_request.json

9. List Contacts
curl -s -X GET "$BITRIX_WEBHOOK_URL/crm.contact.list.json" | jq '.result[] | {ID, NAME, LAST_NAME}'

CRM - Deals
10. Create a Deal

Write to /tmp/bitrix_request.json:

{
  "fields": {
    "TITLE": "New Deal from API",
    "STAGE_ID": "NEW",
    "OPPORTUNITY": 5000,
    "CURRENCY_ID": "USD"
  }
}


Then run:

curl -s -X POST "$BITRIX_WEBHOOK_URL/crm.deal.add.json" --header "Content-Type: application/json" -d @/tmp/bitrix_request.json

11. List Deals
curl -s -X GET "$BITRIX_WEBHOOK_URL/crm.deal.list.json" | jq '.result[] | {ID, TITLE, STAGE_ID, OPPORTUNITY}'

12. Update Deal Stage

Write to /tmp/bitrix_request.json:

{
  "id": 456,
  "fields": {
    "STAGE_ID": "WON"
  }
}


Then run:

curl -s -X POST "$BITRIX_WEBHOOK_URL/crm.deal.update.json" --header "Content-Type: application/json" -d @/tmp/bitrix_request.json

Tasks
13. Create a Task

Write to /tmp/bitrix_request.json:

{
  "fields": {
    "TITLE": "New Task from API",
    "DESCRIPTION": "Task description here",
    "RESPONSIBLE_ID": 1,
    "DEADLINE": "2025-12-31"
  }
}


Then run:

curl -s -X POST "$BITRIX_WEBHOOK_URL/tasks.task.add.json" --header "Content-Type: application/json" -d @/tmp/bitrix_request.json

14. List Tasks
curl -s -X GET "$BITRIX_WEBHOOK_URL/tasks.task.list.json" | jq '.result.tasks[] | {id, title, status}'

15. Complete a Task

Replace <your-task-id> with the actual task ID:

curl -s -X GET "$BITRIX_WEBHOOK_URL/tasks.task.complete.json?taskId=<your-task-id>"

Get Field Definitions

Get available fields for any entity:

# Lead fields
curl -s -X GET "$BITRIX_WEBHOOK_URL/crm.lead.fields.json"

# Contact fields
curl -s -X GET "$BITRIX_WEBHOOK_URL/crm.contact.fields.json"

# Deal fields
curl -s -X GET "$BITRIX_WEBHOOK_URL/crm.deal.fields.json"

Common Parameters
Parameter	Description
filter	Filter results (e.g., {"STATUS_ID": "NEW"})
select	Fields to return (e.g., ["ID", "TITLE"])
order	Sort order (e.g., {"ID": "DESC"})
start	Pagination offset
Guidelines
Keep webhook secret: Never expose your webhook URL publicly
Use POST for complex queries: Filters and field selections work better with POST
Check field names: Use *.fields.json methods to get valid field names
Rate limits: Bitrix24 has rate limits; add delays for bulk operations
Pagination: Results are paginated; use start parameter for large datasets
Weekly Installs
136
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