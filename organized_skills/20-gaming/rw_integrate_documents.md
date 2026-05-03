---
rating: ⭐⭐⭐
title: rw-integrate-documents
url: https://skills.sh/runwayml/skills/rw-integrate-documents
---

# rw-integrate-documents

skills/runwayml/skills/rw-integrate-documents
rw-integrate-documents
Installation
$ npx skills add https://github.com/runwayml/skills --skill rw-integrate-documents
SKILL.md
Integrate Documents (Knowledge Base)

PREREQUISITE: Run +rw-check-compatibility first. Run +rw-fetch-api-reference to load the latest API reference before integrating. +rw-setup-api-key — API credentials must be configured

USED BY: +rw-integrate-characters — Documents are linked to Avatars to give them domain-specific knowledge

Give your Characters access to domain-specific knowledge. Upload content that your Avatar can reference during conversations for accurate, contextual responses.

When to Use Documents
Use Case	Example Content
Customer support	FAQs, product info, company policies, return procedures
Quizzes & games	Question banks, correct answers, scoring rules
Education	Course material, reference content, learning objectives
Brand experiences	Brand guidelines, messaging, product catalogs
Constraints
Each Avatar supports up to 50,000 tokens of knowledge
Supported formats: plain text and Markdown
More formats planned for future releases
Flow

The flow is: Create a Document → Link it to an Avatar

Step 1: Create a Document
Node.js
import RunwayML from '@runwayml/sdk';

const client = new RunwayML();

const document = await client.documents.create({
  name: 'Product FAQ',
  content: `# Product FAQ

## What is your return policy?
We offer a 30-day return policy for all unused items in original packaging.

## How do I track my order?
Log in to your account and visit the Orders page. You'll find tracking information for all shipped orders.

## Do you offer international shipping?
Yes, we ship to over 50 countries. Shipping costs and delivery times vary by destination.`,
});

console.log('Document created:', document.id);

Python
from runwayml import RunwayML

client = RunwayML()

document = client.documents.create(
    name='Product FAQ',
    content="""# Product FAQ

## What is your return policy?
We offer a 30-day return policy for all unused items in original packaging.

## How do I track my order?
Log in to your account and visit the Orders page.

## Do you offer international shipping?
Yes, we ship to over 50 countries.""",
)

print('Document created:', document.id)

Step 2: Link the Document to an Avatar

Update your Avatar to attach the document. This replaces any existing document attachments — pass all document IDs you want linked.

Node.js
await client.avatars.update(avatarId, {
  documentIds: [document.id],
});

Python
client.avatars.update(
    avatar_id,
    document_ids=[document.id],
)

Multiple Documents

You can link multiple documents to a single avatar (total must stay under 50,000 tokens):

const faq = await client.documents.create({
  name: 'FAQ',
  content: '...',
});

const policies = await client.documents.create({
  name: 'Company Policies',
  content: '...',
});

await client.avatars.update(avatarId, {
  documentIds: [faq.id, policies.id],
});

Step 3: Start a Session

Once documents are linked, the Avatar automatically has access to the knowledge during conversations. Start a session as usual — no additional configuration needed:

const session = await client.realtimeSessions.create({
  model: 'gwm1_avatars',
  avatar: {
    type: 'custom',
    avatarId: avatarId,
  },
});

session = client.realtime_sessions.create(
    model='gwm1_avatars',
    avatar={
        'type': 'custom',
        'avatar_id': avatar_id,
    },
)


See +rw-integrate-characters for the full session creation, polling, and WebRTC flow.

Integration Patterns
Load Documents from Files

Read content from local files and create documents:

import fs from 'fs';
import RunwayML from '@runwayml/sdk';

const client = new RunwayML();

// Read a local markdown file
const content = fs.readFileSync('./knowledge/product-faq.md', 'utf-8');

const document = await client.documents.create({
  name: 'Product FAQ',
  content,
});

from pathlib import Path
from runwayml import RunwayML

client = RunwayML()

content = Path('./knowledge/product-faq.md').read_text()

document = client.documents.create(
    name='Product FAQ',
    content=content,
)

Dynamic Knowledge Updates

Update documents programmatically — useful for syncing with a CMS or database:

// Example: API endpoint to update character knowledge
app.post('/api/avatar/update-knowledge', async (req, res) => {
  const { avatarId, documents } = req.body;

  // Create new documents
  const docIds = [];
  for (const doc of documents) {
    const created = await client.documents.create({
      name: doc.name,
      content: doc.content,
    });
    docIds.push(created.id);
  }

  // Link all documents to the avatar (replaces existing)
  await client.avatars.update(avatarId, {
    documentIds: docIds,
  });

  res.json({ success: true, documentCount: docIds.length });
});

Tips
Use Markdown for structured content — headings help the Avatar navigate the knowledge.
Be concise — stay well under the 50,000 token limit for best retrieval quality.
Organize by topic — multiple focused documents work better than one giant document.
Update regularly — keep knowledge current by re-creating documents when content changes.
Documents can also be managed via the Developer Portal UI.
Weekly Installs
33
Repository
runwayml/skills
GitHub Stars
30
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass