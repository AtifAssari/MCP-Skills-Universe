---
title: feishu-integration
url: https://skills.sh/etzhang/openclaw-skills/feishu-integration
---

# feishu-integration

skills/etzhang/openclaw-skills/feishu-integration
feishu-integration
Installation
$ npx skills add https://github.com/etzhang/openclaw-skills --skill feishu-integration
SKILL.md
Feishu Integration

OpenClaw 与飞书（Feishu/Lark）的集成技能，支持文档管理、文件夹操作和权限查询。

Features
📄 文档管理 - 创建、读取、更新、删除飞书文档
📁 文件夹操作 - 列出文档和子文件夹
🔐 权限查询 - 查询应用权限范围
✍️ 内容编辑 - 追加、更新、删除文档块
📋 块操作 - 获取和操作文档结构
Available Tools
Tool	Description
feishu_doc_read	读取文档纯文本内容和元数据
feishu_doc_create	创建新空白文档
feishu_doc_write	写入Markdown内容（覆盖）
feishu_doc_append	追加Markdown内容到末尾
feishu_doc_update_block	更新特定块的文本内容
feishu_doc_delete_block	删除特定块
feishu_doc_list_blocks	列出文档所有块（获取结构）
feishu_doc_get_block	获取特定块的详细内容
feishu_folder_list	列出文件夹中的文档和子文件夹
feishu_app_scopes	列出当前应用权限范围
Setup
1. Create Feishu App
Go to Feishu Open Platform
Create a new application
Get App ID and App Secret
Enable required permissions:
docx:document - Document read/write
docx:folder - Folder access
approval:instance - Approval (optional)
2. Configure Credentials

Create .env file in the skill directory:

# Feishu App Credentials
FEISHU_APP_ID=your_app_id_here
FEISHU_APP_SECRET=your_app_secret_here

# Optional: Custom API endpoint
FEISHU_API_BASE_URL=https://open.feishu.cn/open-apis


Or set environment variables:

export FEISHU_APP_ID="your_app_id"
export FEISHU_APP_SECRET="your_app_secret"

3. Install Dependencies
cd feishu-integration
pip install -r requirements.txt  # If needed

Usage
Create a New Document
from openclaw.tools import feishu_doc_create

result = feishu_doc_create(
    folder_token="optional_parent_folder_token",
    title="My New Document"
)
doc_token = result.doc_token

Read Document Content
from openclaw.tools import feishu_doc_read

result = feishu_doc_read(
    doc_token="your_document_token"
)
# Returns: plain text content and metadata

Write Content
from openclaw.tools import feishu_doc_write

feishu_doc_write(
    doc_token="your_document_token",
    content="# Hello World\n\nThis is a **Feishu** document!"
)

Append Content
from openclaw.tools import feishu_doc_append

feishu_doc_append(
    doc_token="your_document_token",
    content="## Additional Section\n\nMore content here."
)

Update a Block
from openclaw.tools import feishu_doc_update_block

feishu_doc_update_block(
    doc_token="your_document_token",
    block_id="block_id_from_list_blocks",
    content="Updated text content"
)

List Document Blocks
from openclaw.tools import feishu_doc_list_blocks

result = feishu_doc_list_blocks(
    doc_token="your_document_token"
)
# Returns: list of all blocks with their IDs

List Folder Contents
from openclaw.tools import feishu_folder_list

result = feishu_folder_list(
    folder_token="your_folder_token"
)
# Returns: documents and subfolders in the folder

Check App Permissions
from openclaw.tools import feishu_app_scopes

result = feishu_app_scopes()
# Returns: list of available permissions/scopes

Document Structure

Feishu documents are block-based. Common block types:

paragraph - 文本段落
heading1 - 一级标题
heading2 - 二级标题
heading3 - 三级标题
bullet - 无序列表
ordered - 有序列表
code - 代码块
quote - 引用
table - 表格
image - 图片
Best Practices

Security First

Never commit .env or credentials
Use .gitignore to exclude sensitive files
Rotate app secrets periodically

Error Handling

Check result for success status
Handle rate limits gracefully
Log errors for debugging

Content Format

Use Markdown for content
Note: Tables not supported in write/append
Use blocks API for complex structures

Rate Limits

Respect Feishu API rate limits
Implement backoff for retries
Cache frequently accessed data
Example Workflow
# Create a meeting notes document
from openclaw.tools import (
    feishu_doc_create,
    feishu_doc_write,
    feishu_doc_append
)

# 1. Create new document
doc = feishu_doc_create(title="Meeting Notes - 2024-01-15")

# 2. Write initial content
feishu_doc_write(
    doc_token=doc.doc_token,
    content="# Team Meeting\n\n## Attendees\n- Alice\n- Bob\n- Charlie\n\n## Agenda\n1. Project updates\n2. Q1 planning"
)

# 3. Append action items
feishu_doc_append(
    doc_token=doc.doc_token,
    content="## Action Items\n- [ ] Review PR #123 (Alice)\n- [ ] Update documentation (Bob)"
)

print(f"Document created: https://example.feishu.cn/docx/{doc.doc_token}")

Troubleshooting
"App not found" Error
Verify App ID and Secret are correct
Check app is published (not in draft mode)
"Permission denied" Error
Check required permissions are enabled
Verify tenant-level consent if needed
"Rate limit exceeded" Error
Implement exponential backoff
Reduce API call frequency
Document not updating
Check block_id is valid
Ensure content format is correct
Verify document hasn't been deleted
Resources
Feishu Open Platform Docs
Document API Reference
App Creation Guide
License

MIT

Weekly Installs
8
Repository
etzhang/openclaw-skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass