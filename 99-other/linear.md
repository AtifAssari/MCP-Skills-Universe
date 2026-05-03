---
title: linear
url: https://skills.sh/odysseus0/symphony/linear
---

# linear

skills/odysseus0/symphony/linear
linear
Installation
$ npx skills add https://github.com/odysseus0/symphony --skill linear
SKILL.md
Linear GraphQL

All Linear operations go through the linear_graphql client tool exposed by Symphony's app server. It handles auth automatically.

{
  "query": "query or mutation document",
  "variables": { "optional": "graphql variables" }
}


One operation per tool call. A top-level errors array means the operation failed even if the tool call completed.

Workpad

Maintain a local workpad.md in your workspace. Edit freely (zero API cost), then sync to Linear at milestones — plan finalized, implementation done, validation complete. Do not sync after every small change.

First sync — create the comment, save the ID:

mutation CreateComment($issueId: String!, $body: String!) {
  commentCreate(input: { issueId: $issueId, body: $body }) {
    success
    comment { id }
  }
}


Write the returned comment.id to .workpad-id so subsequent syncs can update.

Subsequent syncs — read .workpad-id, update in place:

mutation UpdateComment($id: String!, $body: String!) {
  commentUpdate(id: $id, input: { body: $body }) { success }
}

Query an issue

The orchestrator injects issue context (identifier, title, description, state, labels, URL) into your prompt at startup. You usually do not need to re-read.

When you do, use the narrowest lookup for what you have:

# By ticket key (e.g. MT-686)
query($key: String!) {
  issue(id: $key) {
    id identifier title url description
    state { id name type }
    project { id name }
  }
}


For comments and attachments:

query($id: String!) {
  issue(id: $id) {
    comments(first: 50) { nodes { id body user { name } createdAt } }
    attachments(first: 20) { nodes { url title sourceType } }
  }
}

State transitions

Fetch team states first, then move with the exact stateId:

query($id: String!) {
  issue(id: $id) {
    team { states { nodes { id name } } }
  }
}

mutation($id: String!, $stateId: String!) {
  issueUpdate(id: $id, input: { stateId: $stateId }) {
    success
    issue { state { name } }
  }
}

Attach a PR or URL
# GitHub PR (preferred for PRs)
mutation($issueId: String!, $url: String!, $title: String) {
  attachmentLinkGitHubPR(issueId: $issueId, url: $url, title: $title, linkKind: links) {
    success
  }
}

# Plain URL
mutation($issueId: String!, $url: String!, $title: String) {
  attachmentLinkURL(issueId: $issueId, url: $url, title: $title) {
    success
  }
}

File upload

Three steps:

Get upload URL:
mutation($filename: String!, $contentType: String!, $size: Int!) {
  fileUpload(filename: $filename, contentType: $contentType, size: $size, makePublic: true) {
    success
    uploadFile { uploadUrl assetUrl headers { key value } }
  }
}

PUT file bytes to uploadUrl with the returned headers (use curl).
Embed assetUrl in comments/workpad as ![description](url).
Issue creation

Resolve project slug to IDs first:

query($slug: String!) {
  projects(filter: { slugId: { eq: $slug } }) {
    nodes { id teams { nodes { id key states { nodes { id name } } } } }
  }
}


Then create:

mutation($input: IssueCreateInput!) {
  issueCreate(input: $input) {
    success
    issue { identifier url }
  }
}


$input fields: title, teamId, projectId, and optionally description, priority (0–4), stateId. For relations, follow up with:

mutation($input: IssueRelationCreateInput!) {
  issueRelationCreate(input: $input) { success }
}


Input: issueId, relatedIssueId, type (blocks or related).

Rules
No introspection. Never use __type or __schema queries. They return the entire Linear schema (~200K chars) and waste the context window. Every pattern you need is documented above.
Keep queries narrowly scoped — ask only for fields you need.
Sync the workpad at milestones, not after every change.
For state transitions, always fetch team states first — never hardcode state IDs.
Prefer attachmentLinkGitHubPR over generic URL attachment for GitHub PRs.
Weekly Installs
171
Repository
odysseus0/symphony
GitHub Stars
62
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass