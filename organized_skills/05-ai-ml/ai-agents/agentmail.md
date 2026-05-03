---
rating: ⭐⭐
title: agentmail
url: https://skills.sh/vm0-ai/vm0-skills/agentmail
---

# agentmail

skills/vm0-ai/vm0-skills/agentmail
agentmail
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill agentmail
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name AGENTMAIL_TOKEN or zero doctor check-connector --url https://api.agentmail.to/v0/inboxes --method POST

Scenarios
1. Customer Support Agent

An AI agent handles inbound support emails automatically.

Create a dedicated inbox for support: POST /v0/inboxes with username: "support"
Register a webhook listening for message.received: POST /v0/webhooks with inbox_ids scoped to the support inbox
When a customer emails support@agentmail.to, the webhook fires with the message payload
Read the full thread for context: GET /v0/inboxes/{inbox-id}/threads/{thread-id}
Generate a response with your LLM, then reply in-thread: POST /v0/inboxes/{inbox-id}/messages/{message-id}/reply
Update labels to track state: PATCH /v0/inboxes/{inbox-id}/messages/{message-id} with add_labels: ["replied"], remove_labels: ["unreplied"]
Periodically check for stale threads: GET /v0/inboxes/{inbox-id}/threads?labels=unreplied to find conversations that still need attention
2. Sales Outreach with Scheduled Follow-ups

An AI agent sends personalized cold emails and manages follow-up sequences.

Create an inbox per sales campaign: POST /v0/inboxes with client_id: "campaign-q1" for idempotency
Send initial outreach: POST /v0/inboxes/{inbox-id}/messages/send with personalized subject/body
Create scheduled follow-up drafts for non-responders: POST /v0/inboxes/{inbox-id}/drafts with send_at set to 3 days later
Register a webhook for message.received to detect replies
When a prospect replies, cancel the scheduled draft: DELETE /v0/inboxes/{inbox-id}/drafts/{draft-id}
Monitor delivery health: GET /v0/metrics?event_types=message.bounced&event_types=message.complained to detect reputation issues early
3. Document Processing Pipeline

An AI agent receives documents via email, processes them, and sends results back.

Create an inbox: POST /v0/inboxes with username: "doc-processor"
Set up a webhook for message.received
When an email arrives with attachments, the webhook payload includes attachment metadata
Download the attachment: GET /v0/inboxes/{inbox-id}/messages/{message-id}/attachments/{attachment-id} → returns a temporary download_url
Download and process the file (OCR, summarization, data extraction, etc.)
Reply with results: POST /v0/inboxes/{inbox-id}/messages/{message-id}/reply including processed output in the body or a new attachment
4. Multi-Agent Team Coordination

Multiple AI agents each have their own inbox, organized by team.

Create a pod for the team: POST /v0/pods with name: "Research Team"
Create an inbox per agent with pod_id: POST /v0/inboxes for each agent (e.g. researcher-1, researcher-2, summarizer)
Set up per-inbox webhooks to route events to each agent's handler: POST /v0/webhooks with inbox_ids scoped per agent
Agents send emails to each other using their @agentmail.to addresses for inter-agent communication
List all inboxes in the pod for oversight: GET /v0/inboxes filtered by pod
5. Human-in-the-Loop Draft Approval

An AI agent drafts emails for human review before sending.

Create a draft with the AI-generated content: POST /v0/inboxes/{inbox-id}/drafts
Notify the human reviewer (via Slack, UI, etc.) with the draft ID
Human reviews the draft: GET /v0/inboxes/{inbox-id}/drafts/{draft-id}
If approved, send the draft: POST /v0/inboxes/{inbox-id}/drafts/{draft-id}/send
If changes needed, update and re-review: PATCH /v0/inboxes/{inbox-id}/drafts/{draft-id} with revised content
If rejected, delete the draft: DELETE /v0/inboxes/{inbox-id}/drafts/{draft-id}
6. Ephemeral Inboxes for One-off Tasks

Create disposable inboxes for short-lived tasks, then clean up.

Create a temporary inbox with client_id tied to the task ID: POST /v0/inboxes with client_id: "task-abc123"
Use the inbox to send/receive emails for this specific task (e.g. verifying an account, requesting info from an external party)
Poll or webhook for responses
When the task is complete, delete the inbox: DELETE /v0/inboxes/{inbox-id} — all associated threads and messages are cleaned up
7. Email Monitoring and Analytics

Track email delivery health across all agent inboxes.

Query delivery metrics over a time range: GET /v0/metrics?start_timestamp=...&end_timestamp=...
Filter by event type to find problems: GET /v0/metrics?event_types=message.bounced&event_types=message.rejected
If bounce rates are high, investigate specific inboxes using GET /v0/inboxes/{inbox-id}/messages?labels=bounced
Set up a webhook for message.bounced and message.complained to get real-time alerts on deliverability issues
8. Inbound Lead Qualification

An AI agent triages inbound emails and routes them appropriately.

Create an inbox as the public-facing entry point: POST /v0/inboxes with username: "hello"
Register a webhook for message.received
When a new email arrives, use your LLM to classify intent (sales inquiry, support request, partnership, spam)
Label the message by category: PATCH /v0/inboxes/{inbox-id}/messages/{message-id} with add_labels: ["sales-lead"]
Send an auto-acknowledgment: POST /v0/inboxes/{inbox-id}/messages/{message-id}/reply
Forward to the right team by sending a new email from a different inbox or notifying via webhook
Review unhandled messages: GET /v0/inboxes/{inbox-id}/messages?labels=needs-review
Inboxes
Create Inbox
curl -s -X POST "https://api.agentmail.to/v0/inboxes" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d '{"username": "my-agent", "display_name": "My Agent"}' | jq .


Create with idempotent client_id (safe to retry without creating duplicates):

curl -s -X POST "https://api.agentmail.to/v0/inboxes" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d '{"username": "my-agent", "display_name": "My Agent", "client_id": "my-agent-inbox"}' | jq .

List Inboxes
curl -s "https://api.agentmail.to/v0/inboxes" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .


With pagination:

curl -s "https://api.agentmail.to/v0/inboxes?limit=10" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Get Inbox
curl -s "https://api.agentmail.to/v0/inboxes/{inbox-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Update Inbox
curl -s -X PATCH "https://api.agentmail.to/v0/inboxes/{inbox-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d '{"display_name": "New Name"}' | jq .

Delete Inbox
curl -s -X DELETE "https://api.agentmail.to/v0/inboxes/{inbox-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN"

Messages
Send Email

Write to /tmp/agentmail_request.json:

{
  "to": ["recipient@example.com"],
  "subject": "Hello from my agent",
  "text": "Plain text body",
  "html": "<p>HTML body</p>"
}


Then run:

curl -s -X POST "https://api.agentmail.to/v0/inboxes/{inbox-id}/messages/send" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .

Send Email with CC/BCC

Write to /tmp/agentmail_request.json:

{
  "to": ["recipient@example.com"],
  "cc": ["cc@example.com"],
  "bcc": ["bcc@example.com"],
  "subject": "Hello",
  "text": "Plain text body",
  "html": "<p>HTML body</p>"
}


Then run:

curl -s -X POST "https://api.agentmail.to/v0/inboxes/{inbox-id}/messages/send" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .

Send Email with Labels

Write to /tmp/agentmail_request.json:

{
  "to": ["recipient@example.com"],
  "subject": "Hello",
  "text": "Plain text body",
  "labels": ["outreach", "onboarding"]
}


Then run:

curl -s -X POST "https://api.agentmail.to/v0/inboxes/{inbox-id}/messages/send" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .

Send Email with Attachment

Write to /tmp/agentmail_request.json:

{
  "to": ["recipient@example.com"],
  "subject": "Report attached",
  "text": "Please find the report attached.",
  "attachments": [
    {
      "filename": "report.txt",
      "content_type": "text/plain",
      "content": "<base64-encoded-content>"
    }
  ]
}


Then run:

curl -s -X POST "https://api.agentmail.to/v0/inboxes/{inbox-id}/messages/send" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .


To base64 encode a file:

base64 -w 0 /path/to/file.pdf

Reply to Message

Write to /tmp/agentmail_request.json:

{
  "text": "Thanks for your message!",
  "html": "<p>Thanks for your message!</p>"
}


Then run:

curl -s -X POST "https://api.agentmail.to/v0/inboxes/{inbox-id}/messages/{message-id}/reply" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .

Reply All

Write to /tmp/agentmail_request.json:

{
  "reply_all": true,
  "text": "Thanks everyone!",
  "html": "<p>Thanks everyone!</p>"
}


Then run:

curl -s -X POST "https://api.agentmail.to/v0/inboxes/{inbox-id}/messages/{message-id}/reply" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .

List Messages
curl -s "https://api.agentmail.to/v0/inboxes/{inbox-id}/messages" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .


With filters:

curl -s "https://api.agentmail.to/v0/inboxes/{inbox-id}/messages?labels=unreplied&limit=10" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Get Message
curl -s "https://api.agentmail.to/v0/inboxes/{inbox-id}/messages/{message-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Update Message Labels

Write to /tmp/agentmail_request.json:

{
  "add_labels": ["replied"],
  "remove_labels": ["unreplied"]
}


Then run:

curl -s -X PATCH "https://api.agentmail.to/v0/inboxes/{inbox-id}/messages/{message-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .

Get Message Attachment
curl -s "https://api.agentmail.to/v0/inboxes/{inbox-id}/messages/{message-id}/attachments/{attachment-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .


Returns a download_url (temporary pre-signed URL) and expires_at. Download the file:

curl -s -o attachment.bin "{download-url}"

Threads
List Threads
curl -s "https://api.agentmail.to/v0/inboxes/{inbox-id}/threads" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .


With filters:

curl -s "https://api.agentmail.to/v0/inboxes/{inbox-id}/threads?labels=unreplied&after=2025-01-01T00:00:00Z&limit=10" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Get Thread

Returns thread with all messages ordered by timestamp ascending:

curl -s "https://api.agentmail.to/v0/inboxes/{inbox-id}/threads/{thread-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Get Thread Attachment
curl -s "https://api.agentmail.to/v0/inboxes/{inbox-id}/threads/{thread-id}/attachments/{attachment-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Delete Thread
curl -s -X DELETE "https://api.agentmail.to/v0/inboxes/{inbox-id}/threads/{thread-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN"

Drafts
Create Draft

Write to /tmp/agentmail_request.json:

{
  "to": ["recipient@example.com"],
  "subject": "Draft email",
  "text": "This is a draft.",
  "html": "<p>This is a draft.</p>"
}


Then run:

curl -s -X POST "https://api.agentmail.to/v0/inboxes/{inbox-id}/drafts" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .

Create Scheduled Draft

Write to /tmp/agentmail_request.json:

{
  "to": ["recipient@example.com"],
  "subject": "Scheduled email",
  "text": "This will be sent later.",
  "send_at": "2025-12-01T10:00:00Z"
}


Then run:

curl -s -X POST "https://api.agentmail.to/v0/inboxes/{inbox-id}/drafts" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .

List Drafts
curl -s "https://api.agentmail.to/v0/inboxes/{inbox-id}/drafts" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Get Draft
curl -s "https://api.agentmail.to/v0/inboxes/{inbox-id}/drafts/{draft-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Update Draft

Write to /tmp/agentmail_request.json:

{
  "subject": "Updated subject",
  "text": "Updated body"
}


Then run:

curl -s -X PATCH "https://api.agentmail.to/v0/inboxes/{inbox-id}/drafts/{draft-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .

Send Draft
curl -s -X POST "https://api.agentmail.to/v0/inboxes/{inbox-id}/drafts/{draft-id}/send" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d '{}' | jq .

Delete Draft
curl -s -X DELETE "https://api.agentmail.to/v0/inboxes/{inbox-id}/drafts/{draft-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN"

Webhooks
Create Webhook

Write to /tmp/agentmail_request.json:

{
  "url": "https://your-server.com/webhooks",
  "event_types": ["message.received", "message.sent", "message.delivered"],
  "client_id": "my-webhook"
}


Then run:

curl -s -X POST "https://api.agentmail.to/v0/webhooks" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .


Supported event types: message.received, message.sent, message.delivered, message.bounced, message.complained, message.rejected, domain.verified

Create Webhook for Specific Inboxes

Write to /tmp/agentmail_request.json:

{
  "url": "https://your-server.com/webhooks",
  "event_types": ["message.received"],
  "inbox_ids": ["{inbox-id-1}", "{inbox-id-2}"],
  "client_id": "inbox-webhook"
}


Then run:

curl -s -X POST "https://api.agentmail.to/v0/webhooks" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .

List Webhooks
curl -s "https://api.agentmail.to/v0/webhooks" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Get Webhook
curl -s "https://api.agentmail.to/v0/webhooks/{webhook-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Update Webhook (Add/Remove Inboxes)

Write to /tmp/agentmail_request.json:

{
  "add_inbox_ids": ["{new-inbox-id}"],
  "remove_inbox_ids": ["{old-inbox-id}"]
}


Then run:

curl -s -X PATCH "https://api.agentmail.to/v0/webhooks/{webhook-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d @/tmp/agentmail_request.json' | jq .

Delete Webhook
curl -s -X DELETE "https://api.agentmail.to/v0/webhooks/{webhook-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN"

Domains
Create Domain
curl -s -X POST "https://api.agentmail.to/v0/domains" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d '{"domain": "yourdomain.com", "feedback_enabled": true}' | jq .


Returns DNS records (TXT, CNAME, MX) that must be added to your DNS provider.

List Domains
curl -s "https://api.agentmail.to/v0/domains" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Get Domain
curl -s "https://api.agentmail.to/v0/domains/{domain-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Verify Domain

Trigger DNS verification after adding records:

curl -s -X POST "https://api.agentmail.to/v0/domains/{domain-id}/verify" --header "Authorization: Bearer $AGENTMAIL_TOKEN"


Domain status values: NOT_STARTED, PENDING, INVALID, FAILED, VERIFYING, VERIFIED

Delete Domain
curl -s -X DELETE "https://api.agentmail.to/v0/domains/{domain-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN"

Pods

Pods are organizational groups for inboxes.

Create Pod
curl -s -X POST "https://api.agentmail.to/v0/pods" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d '{"name": "Support Team", "client_id": "support-pod"}' | jq .

List Pods
curl -s "https://api.agentmail.to/v0/pods" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Get Pod
curl -s "https://api.agentmail.to/v0/pods/{pod-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Delete Pod
curl -s -X DELETE "https://api.agentmail.to/v0/pods/{pod-id}" --header "Authorization: Bearer $AGENTMAIL_TOKEN"

Metrics
Get Delivery Metrics
curl -s "https://api.agentmail.to/v0/metrics?start_timestamp=2025-01-01T00:00:00Z&end_timestamp=2025-12-31T23:59:59Z" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .


Filter by event type:

curl -s "https://api.agentmail.to/v0/metrics?start_timestamp=2025-01-01T00:00:00Z&end_timestamp=2025-12-31T23:59:59Z&event_types=message.sent&event_types=message.bounced" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .


Supported event types: message.sent, message.delivered, message.bounced, message.delayed, message.rejected, message.complained, message.received

API Keys
List API Keys
curl -s "https://api.agentmail.to/v0/api-keys" --header "Authorization: Bearer $AGENTMAIL_TOKEN" | jq .

Create API Key
curl -s -X POST "https://api.agentmail.to/v0/api-keys" --header "Authorization: Bearer $AGENTMAIL_TOKEN" --header "Content-Type: application/json" -d '{"name": "production-key"}' | jq .


The api_key value is only returned once at creation time. Save it immediately.

Delete API Key
curl -s -X DELETE "https://api.agentmail.to/v0/api-keys/{api-key}" --header "Authorization: Bearer $AGENTMAIL_TOKEN"

Webhook Event Payload

When a webhook fires, AgentMail sends a POST request with this JSON payload:

{
  "type": "event",
  "event_type": "message.received",
  "event_id": "unique-event-id",
  "message": {
    "inbox_id": "...",
    "thread_id": "...",
    "message_id": "...",
    "from": "sender@example.com",
    "to": ["your-inbox@agentmail.to"],
    "subject": "Hello",
    "text": "Message body",
    "html": "<p>Message body</p>",
    "attachments": []
  },
  "thread": {
    "thread_id": "...",
    "subject": "Hello",
    "message_count": 1
  }
}


Your endpoint should return HTTP 200 immediately and process the payload asynchronously.

Send Parameters Reference
Parameter	Type	Description
to	string[]	Recipients
cc	string[]	CC recipients
bcc	string[]	BCC recipients
reply_to	string[]	Reply-to addresses
subject	string	Email subject
text	string	Plain text body
html	string	HTML body
labels	string[]	Custom labels
attachments	object[]	Attachments (with filename, content_type, content as base64 or url)
headers	object	Custom email headers
Response Codes
Status	Description
200	Success
202	Accepted (async delete for inboxes, threads)
204	No Content (delete success for webhooks, pods, API keys)
400	Invalid parameters
403	Forbidden (sending not allowed)
404	Resource not found
Guidelines
Always send both text and HTML: Provide both formats for best deliverability across email clients
Use client_id for idempotency: When creating inboxes, webhooks, or drafts, use client_id to prevent duplicates on retries
Use labels for state tracking: Tag messages as unreplied/replied to manage conversation state
Use webhooks over polling: Webhooks are the recommended way to handle incoming emails in production
Custom domains improve deliverability: Set up verified custom domains for production use
Default domain: Without a custom domain, inboxes use @agentmail.to
Webhook response: Return HTTP 200 immediately from webhook endpoints; process payloads asynchronously
API Reference
Documentation: https://docs.agentmail.to
API Reference: https://docs.agentmail.to/api-reference/inboxes/list
Console: https://console.agentmail.to
Quickstart: https://docs.agentmail.to/quickstart
Node.js SDK: https://www.npmjs.com/package/agentmail
Python SDK: pip install agentmail
Weekly Installs
49
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn