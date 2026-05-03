---
title: feishu-doc
url: https://skills.sh/m1heng/clawdbot-feishu/feishu-doc
---

# feishu-doc

skills/m1heng/clawdbot-feishu/feishu-doc
feishu-doc
Installation
$ npx skills add https://github.com/m1heng/clawdbot-feishu --skill feishu-doc
Summary

Read, write, and manage comments in Feishu documents with markdown support and block-level operations.

Supports full document lifecycle: read plain text, write/append markdown content, create new documents, and manage individual blocks (get, update, delete)
Comment operations include listing document and block-level comments, retrieving single comments, and creating global comments with pagination support
Structured content (tables, images, code blocks) accessible via list_blocks action; markdown tables not supported in write operations
Atomic create_and_write action recommended for new documents to avoid separate API calls; folder placement supported via folder_token
SKILL.md
Feishu Document Tool

Single tool feishu_doc with action parameter for all document operations including comment management.

Token Extraction

From URL https://xxx.feishu.cn/docx/ABC123def → doc_token = ABC123def From URL https://xxx.feishu.cn/docs/doccn123c → doc_token = doccn123c

Actions
Read Document
{ "action": "read", "doc_token": "ABC123def" }


Returns: title, plain text content, block statistics. Check hint field - if present, structured content (tables, images) exists that requires list_blocks.

Write Document (Replace All)
{ "action": "write", "doc_token": "ABC123def", "content": "# Title\n\nMarkdown content..." }


Replaces entire document with markdown content. Supports: headings, lists, code blocks, quotes, links, images (![](url) auto-uploaded), bold/italic/strikethrough.

Limitation: Markdown tables are NOT supported.

Create + Write (Atomic, Recommended)
{
  "action": "create_and_write",
  "title": "New Document",
  "content": "# Title\n\nMarkdown content..."
}


With folder:

{
  "action": "create_and_write",
  "title": "New Document",
  "content": "# Title\n\nMarkdown content...",
  "folder_token": "fldcnXXX"
}


Creates the document and writes content in one call. Prefer this over separate create + write.

Append Content
{ "action": "append", "doc_token": "ABC123def", "content": "Additional content" }


Appends markdown to end of document.

Create Document
{ "action": "create", "title": "New Document" }


With folder:

{ "action": "create", "title": "New Document", "folder_token": "fldcnXXX" }


Creates an empty document (title only).

List Blocks
{ "action": "list_blocks", "doc_token": "ABC123def" }


Returns full block data including tables, images. Use this to read structured content.

Get Single Block
{ "action": "get_block", "doc_token": "ABC123def", "block_id": "doxcnXXX" }

Update Block Text
{ "action": "update_block", "doc_token": "ABC123def", "block_id": "doxcnXXX", "content": "New text" }

Delete Block
{ "action": "delete_block", "doc_token": "ABC123def", "block_id": "doxcnXXX" }

List Comments
{ "action": "list_comments", "doc_token": "ABC123def", "page_size": 50 }


Returns all comments for the document. Use page_token for pagination. Comments include is_whole field to distinguish between whole-document comments (true) and block-level comments (false).

Get Single Comment
{ "action": "get_comment", "doc_token": "ABC123def", "comment_id": "comment_xxx" }

Create Comment
{ "action": "create_comment", "doc_token": "ABC123def", "content": "Comment text" }

List Comment Replies
{ "action": "list_comment_replies", "doc_token": "ABC123def", "comment_id": "comment_xxx", "page_size": 50 }


page_size should be a positive integer. If omitted, tool defaults to 50.

Comment Write Scope

Current tool provides documented comment write action create_comment (global comment creation). For replies, use list_comment_replies for retrieval; the reply creation endpoint is not exposed in current SDK surface.

Reading Workflow
Start with action: "read" - get plain text + statistics
Check block_types in response for Table, Image, Code, etc.
If structured content exists, use action: "list_blocks" for full data
Configuration
channels:
  feishu:
    tools:
      doc: true  # default: true


Note: feishu_wiki depends on this tool - wiki page content is read/written via feishu_doc.

Permissions

Required: docx:document, docx:document:readonly, docx:document.block:convert, drive:drive

For comment operations:

Read comments: docx:document.comment:read
Write comments: docx:document.comment (optional, for create_comment)
Weekly Installs
1.8K
Repository
m1heng/clawdbot-feishu
GitHub Stars
4.3K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn