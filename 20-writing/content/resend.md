---
title: resend
url: https://skills.sh/vm0-ai/vm0-skills/resend
---

# resend

skills/vm0-ai/vm0-skills/resend
resend
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill resend
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name RESEND_TOKEN or zero doctor check-connector --url https://api.resend.com/emails --method POST

Emails
Send Email

Write to /tmp/resend_request.json:

{
  "from": "Acme <onboarding@resend.dev>",
  "to": ["<your-recipient-email>"],
  "subject": "<your-subject>",
  "html": "<p><your-html-content></p>"
}


Then run:

curl -s -X POST "https://api.resend.com/emails" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Send Email with Plain Text

Write to /tmp/resend_request.json:

{
  "from": "Acme <onboarding@resend.dev>",
  "to": ["<your-recipient-email>"],
  "subject": "<your-subject>",
  "text": "<your-plain-text-content>"
}


Then run:

curl -s -X POST "https://api.resend.com/emails" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Send Email with CC/BCC

Write to /tmp/resend_request.json:

{
  "from": "Acme <onboarding@resend.dev>",
  "to": ["<your-recipient-email>"],
  "cc": ["<your-cc-email>"],
  "bcc": ["<your-bcc-email>"],
  "subject": "<your-subject>",
  "html": "<p><your-html-content></p>"
}


Then run:

curl -s -X POST "https://api.resend.com/emails" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Send Email with Reply-To

Write to /tmp/resend_request.json:

{
  "from": "Acme <onboarding@resend.dev>",
  "to": ["<your-recipient-email>"],
  "reply_to": "<your-reply-to-email>",
  "subject": "<your-subject>",
  "html": "<p><your-html-content></p>"
}


Then run:

curl -s -X POST "https://api.resend.com/emails" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Send Scheduled Email

Schedule email using natural language or ISO 8601 format:

Write to /tmp/resend_request.json:

{
  "from": "Acme <onboarding@resend.dev>",
  "to": ["<your-recipient-email>"],
  "subject": "<your-subject>",
  "html": "<p><your-html-content></p>",
  "scheduled_at": "in 1 hour"
}


Then run:

curl -s -X POST "https://api.resend.com/emails" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Send Batch Emails

Send up to 100 emails in a single request:

Write to /tmp/resend_request.json:

[
  {
    "from": "Acme <onboarding@resend.dev>",
    "to": ["<your-recipient-1>"],
    "subject": "Hello 1",
    "html": "<p>Email 1</p>"
  },
  {
    "from": "Acme <onboarding@resend.dev>",
    "to": ["<your-recipient-2>"],
    "subject": "Hello 2",
    "html": "<p>Email 2</p>"
  }
]


Then run:

curl -s -X POST "https://api.resend.com/emails/batch" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Retrieve Email
curl -s "https://api.resend.com/emails/<your-email-id>" --header "Authorization: Bearer $RESEND_TOKEN"

List Sent Emails
curl -s "https://api.resend.com/emails" --header "Authorization: Bearer $RESEND_TOKEN"

Cancel Scheduled Email
curl -s -X POST "https://api.resend.com/emails/<your-email-id>/cancel" --header "Authorization: Bearer $RESEND_TOKEN"

Contacts
Create Contact

Write to /tmp/resend_request.json:

{
  "email": "<your-contact-email>",
  "first_name": "<your-first-name>",
  "last_name": "<your-last-name>",
  "unsubscribed": false
}


Then run:

curl -s -X POST "https://api.resend.com/contacts" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Create Contact with Custom Properties

Write to /tmp/resend_request.json:

{
  "email": "<your-contact-email>",
  "first_name": "<your-first-name>",
  "last_name": "<your-last-name>",
  "properties": {
    "company": "<your-company-name>",
    "role": "<your-role>"
  }
}


Then run:

curl -s -X POST "https://api.resend.com/contacts" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Retrieve Contact
curl -s "https://api.resend.com/contacts/<your-contact-id>" --header "Authorization: Bearer $RESEND_TOKEN"

List Contacts
curl -s "https://api.resend.com/contacts" --header "Authorization: Bearer $RESEND_TOKEN"

List Contacts with Pagination
curl -s "https://api.resend.com/contacts?limit=50" --header "Authorization: Bearer $RESEND_TOKEN"

Update Contact

Write to /tmp/resend_request.json:

{
  "first_name": "<your-new-first-name>",
  "unsubscribed": true
}


Then run:

curl -s -X PATCH "https://api.resend.com/contacts/<your-contact-id>" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Delete Contact
curl -s -X DELETE "https://api.resend.com/contacts/<your-contact-id>" --header "Authorization: Bearer $RESEND_TOKEN"

Domains
List Domains
curl -s "https://api.resend.com/domains" --header "Authorization: Bearer $RESEND_TOKEN"

Retrieve Domain
curl -s "https://api.resend.com/domains/<your-domain-id>" --header "Authorization: Bearer $RESEND_TOKEN"

Create Domain

Write to /tmp/resend_request.json:

{
  "name": "<your-domain-name>"
}


Then run:

curl -s -X POST "https://api.resend.com/domains" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Verify Domain
curl -s -X POST "https://api.resend.com/domains/<your-domain-id>/verify" --header "Authorization: Bearer $RESEND_TOKEN"

Delete Domain
curl -s -X DELETE "https://api.resend.com/domains/<your-domain-id>" --header "Authorization: Bearer $RESEND_TOKEN"

API Keys
List API Keys
curl -s "https://api.resend.com/api-keys" --header "Authorization: Bearer $RESEND_TOKEN"

Create API Key

Write to /tmp/resend_request.json:

{
  "name": "<your-key-name>"
}


Then run:

curl -s -X POST "https://api.resend.com/api-keys" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Create API Key with Permissions

Write to /tmp/resend_request.json:

{
  "name": "<your-key-name>",
  "permission": "sending_access"
}


Then run:

curl -s -X POST "https://api.resend.com/api-keys" --header "Authorization: Bearer $RESEND_TOKEN" --header "Content-Type: application/json" -d @/tmp/resend_request.json

Delete API Key
curl -s -X DELETE "https://api.resend.com/api-keys/<your-api-key-id>" --header "Authorization: Bearer $RESEND_TOKEN"

Email Parameters Reference
Parameter	Type	Description
from	string	Sender email (required). Format: "Name <email@domain.com>"
to	string[]	Recipients (required). Max 50 addresses
subject	string	Email subject (required)
html	string	HTML content
text	string	Plain text content
cc	string[]	CC recipients
bcc	string[]	BCC recipients
reply_to	string	Reply-to address
scheduled_at	string	Schedule time (ISO 8601 or natural language)
tags	array	Custom tags for tracking
attachments	array	File attachments (max 40MB total)
Response Codes
Status	Description
200	Success
400	Invalid parameters
401	Missing API key
403	Invalid API key
404	Resource not found
429	Rate limit exceeded (2 req/sec)
5xx	Server error
Guidelines
Rate Limits: Default is 2 requests per second; implement backoff for 429 errors
Sender Domain: Use verified domains for production; onboarding@resend.dev for testing
Batch Emails: Use /emails/batch for sending to multiple recipients efficiently
Idempotency: Use Idempotency-Key header to prevent duplicate sends
Scheduling: Use natural language (in 1 hour) or ISO 8601 format for scheduled_at
API Reference
Documentation: https://resend.com/docs/api-reference/introduction
Dashboard: https://resend.com/overview
API Keys: https://resend.com/api-keys
Domains: https://resend.com/domains
Weekly Installs
71
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass