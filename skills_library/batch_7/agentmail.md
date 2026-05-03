---
title: agentmail
url: https://skills.sh/agentmail-to/agentmail-skills/agentmail
---

# agentmail

skills/agentmail-to/agentmail-skills/agentmail
agentmail
Installation
$ npx skills add https://github.com/agentmail-to/agentmail-skills --skill agentmail
Summary

API-first email platform giving AI agents dedicated inboxes with send, receive, and management capabilities.

Supports inbox creation with auto-generated or custom email addresses, message sending/receiving, threaded conversations, and label-based organization
Includes attachment handling via Base64 encoding, draft creation for human approval workflows, and message reply functionality
Offers multi-tenant isolation through pods for SaaS platforms, with idempotent operations using client IDs for safe retries
Provides real-time notifications via webhooks or WebSockets for incoming messages and thread updates
Available in TypeScript/Node.js and Python with identical API surface
SKILL.md
AgentMail SDK

AgentMail is an API-first email platform for AI agents. Install the SDK and initialize the client.

Installation
# TypeScript/Node
npm install agentmail

# Python
pip install agentmail

Setup
import { AgentMailClient } from "agentmail";
const client = new AgentMailClient({ apiKey: "YOUR_API_KEY" });

from agentmail import AgentMail
client = AgentMail(api_key="YOUR_API_KEY")

Inboxes

Create scalable inboxes on-demand. Each inbox has a unique email address.

// Create inbox (auto-generated address)
const autoInbox = await client.inboxes.create();

// Create with custom username and domain
const customInbox = await client.inboxes.create({
  username: "support",
  domain: "yourdomain.com",
});

// List, get, delete
const inboxes = await client.inboxes.list();
const fetchedInbox = await client.inboxes.get("inbox@agentmail.to");
await client.inboxes.delete("inbox@agentmail.to");

# Create inbox (auto-generated address)
inbox = client.inboxes.create()

# Create with custom username and domain
from agentmail.inboxes.types import CreateInboxRequest
inbox = client.inboxes.create(
    request=CreateInboxRequest(username="support", domain="yourdomain.com"),
)

# List, get, delete
inboxes = client.inboxes.list()
inbox = client.inboxes.get(inbox_id="inbox@agentmail.to")
client.inboxes.delete(inbox_id="inbox@agentmail.to")

Messages

Always send both text and html for best deliverability.

// Send message
await client.inboxes.messages.send("agent@agentmail.to", {
  to: "recipient@example.com",
  subject: "Hello",
  text: "Plain text version",
  html: "<p>HTML version</p>",
  labels: ["outreach"],
});

// Reply to message
await client.inboxes.messages.reply("agent@agentmail.to", "msg_123", {
  text: "Thanks for your email!",
});

// List and get messages
const messages = await client.inboxes.messages.list("agent@agentmail.to");
const message = await client.inboxes.messages.get("agent@agentmail.to", "msg_123");

// Update labels
await client.inboxes.messages.update("agent@agentmail.to", "msg_123", {
  addLabels: ["replied"],
  removeLabels: ["unreplied"],
});

# Send message
client.inboxes.messages.send(
    inbox_id="agent@agentmail.to",
    to="recipient@example.com",
    subject="Hello",
    text="Plain text version",
    html="<p>HTML version</p>",
    labels=["outreach"]
)

# Reply to message
client.inboxes.messages.reply(
    inbox_id="agent@agentmail.to",
    message_id="msg_123",
    text="Thanks for your email!"
)

# List and get messages
messages = client.inboxes.messages.list(inbox_id="agent@agentmail.to")
message = client.inboxes.messages.get(inbox_id="agent@agentmail.to", message_id="msg_123")

# Update labels
client.inboxes.messages.update(
    inbox_id="agent@agentmail.to",
    message_id="msg_123",
    add_labels=["replied"],
    remove_labels=["unreplied"]
)

Threads

Threads group related messages in a conversation.

// List threads (with optional label filter)
const threads = await client.inboxes.threads.list("agent@agentmail.to", {
  labels: ["unreplied"],
});

// Get thread details
const thread = await client.inboxes.threads.get("agent@agentmail.to", "thd_123");

// Org-wide thread listing
const allThreads = await client.threads.list();

# List threads (with optional label filter)
threads = client.inboxes.threads.list(inbox_id="agent@agentmail.to", labels=["unreplied"])

# Get thread details
thread = client.inboxes.threads.get(inbox_id="agent@agentmail.to", thread_id="thd_123")

# Org-wide thread listing
all_threads = client.threads.list()

Attachments

Send attachments with Base64 encoding. Retrieve from messages or threads.

// Send with attachment
const content = Buffer.from(fileBytes).toString("base64");
await client.inboxes.messages.send("agent@agentmail.to", {
  to: "recipient@example.com",
  subject: "Report",
  text: "See attached.",
  attachments: [
    { content, filename: "report.pdf", contentType: "application/pdf" },
  ],
});

// Get attachment
const fileData = await client.inboxes.messages.getAttachment(
  "agent@agentmail.to",
  "msg_123",
  "att_456",
);

import base64

# Send with attachment
content = base64.b64encode(file_bytes).decode()
client.inboxes.messages.send(
    inbox_id="agent@agentmail.to",
    to="recipient@example.com",
    subject="Report",
    text="See attached.",
    attachments=[{"content": content, "filename": "report.pdf", "content_type": "application/pdf"}]
)

# Get attachment
file_data = client.inboxes.messages.get_attachment(
    inbox_id="agent@agentmail.to",
    message_id="msg_123",
    attachment_id="att_456"
)

Drafts

Create drafts for human-in-the-loop approval before sending.

// Create draft
const draft = await client.inboxes.drafts.create("agent@agentmail.to", {
  to: "recipient@example.com",
  subject: "Pending approval",
  text: "Draft content",
});

// Send draft (converts to message)
await client.inboxes.drafts.send("agent@agentmail.to", draft.draftId, {});

# Create draft
draft = client.inboxes.drafts.create(
    inbox_id="agent@agentmail.to",
    to="recipient@example.com",
    subject="Pending approval",
    text="Draft content"
)

# Send draft (converts to message)
client.inboxes.drafts.send(inbox_id="agent@agentmail.to", draft_id=draft.draft_id)

Pods

Multi-tenant isolation for SaaS platforms. Each customer gets isolated inboxes.

// Create pod for a customer
const pod = await client.pods.create({ clientId: "customer_123" });

// Create inbox within pod
const inbox = await client.pods.inboxes.create(pod.podId, {});

// List inboxes scoped to pod
const inboxes = await client.pods.inboxes.list(pod.podId);

# Create pod for a customer
pod = client.pods.create(client_id="customer_123")

# Create inbox within pod (pods.inboxes.create accepts flat kwargs)
inbox = client.pods.inboxes.create(pod_id=pod.pod_id)

# List inboxes scoped to pod
inboxes = client.pods.inboxes.list(pod_id=pod.pod_id)

Idempotency

Use clientId for safe retries on create operations.

const inbox = await client.inboxes.create({
  clientId: "unique-idempotency-key",
});
// Retrying with same clientId returns the original inbox, not a duplicate

from agentmail.inboxes.types import CreateInboxRequest

inbox = client.inboxes.create(
    request=CreateInboxRequest(client_id="unique-idempotency-key"),
)
# Retrying with same client_id returns the original inbox, not a duplicate

Real-Time Events

For real-time notifications, see the reference files:

webhooks.md - HTTP-based notifications (requires public URL)
websockets.md - Persistent connection (no public URL needed)
Weekly Installs
1.3K
Repository
agentmail-to/ag…l-skills
GitHub Stars
10
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn