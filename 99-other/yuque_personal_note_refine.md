---
title: yuque-personal-note-refine
url: https://skills.sh/yuque/yuque-plugin/yuque-personal-note-refine
---

# yuque-personal-note-refine

skills/yuque/yuque-plugin/yuque-personal-note-refine
yuque-personal-note-refine
Installation
$ npx skills add https://github.com/yuque/yuque-plugin --skill yuque-personal-note-refine
SKILL.md
Note Refine — Restructure & Polish Your Notes

Help the user transform scattered, rough notes into well-structured, deduplicated, and enriched documents. Turn chaos into clarity.

When to Use
User wants to clean up messy notes
User says "帮我整理笔记", "refine my notes", "把这些笔记理一下"
User has accumulated daily captures and wants to consolidate them
User says "这些笔记太乱了", "帮我重新组织一下", "去重整理"
Required MCP Tools

All tools are from the yuque-mcp server:

yuque_search — Find the target notes to refine
yuque_get_doc — Read the full content of notes
yuque_list_repos — List personal repos
yuque_list_docs — List documents in a repo
yuque_create_doc — Create the refined document
yuque_update_doc — Update the original document in place
Workflow
Step 1: Identify the Source Notes

The user may provide:

A specific document to refine
A date range of daily captures to consolidate
A topic keyword to find related scattered notes
Multiple document references to merge

If the user says "整理我最近的笔记":

Tool: yuque_search
Parameters:
  query: "每日捕获"
  type: "doc"


Or for topic-specific notes:

Tool: yuque_search
Parameters:
  query: "<topic keyword>"
  type: "doc"

Step 2: Read All Source Notes

For each identified document:

Tool: yuque_get_doc
Parameters:
  repo_id: "<namespace>"
  doc_id: "<slug>"


Read up to 5-10 source documents. If there are more, prioritize by recency and relevance.

Step 3: Analyze and Plan

Before refining, analyze the raw content:

Identify themes — Group related content by topic
Find duplicates — Flag repeated ideas or information
Spot gaps — Note where information is incomplete
Assess structure — Determine the best organizational approach

Present the analysis to the user:

## 📋 笔记分析

**来源**：X 篇文档，共约 XXXX 字

### 主题分布
- **[主题 1]**：X 条相关记录
- **[主题 2]**：X 条相关记录
- **[主题 3]**：X 条相关记录

### 发现
- 🔄 发现 X 处重复内容
- 🕳️ 发现 X 处信息缺口
- 📊 建议整理为 X 篇主题文档

要按这个方向整理吗？

Step 4: Refine the Notes

Based on user confirmation, perform the refinement:

4a. Single Document Refinement

Restructure one document:

Add clear headings and hierarchy
Remove duplicate content
Improve wording and clarity
Add missing context or transitions
Organize chronological notes into logical structure
4b. Multi-Document Consolidation

Merge multiple notes into themed documents:

Group by topic
Deduplicate across documents
Create a coherent narrative
Preserve attribution (note original dates/sources)

Refined document template:

# [主题标题]

> 整理自 X 篇笔记，时间跨度：YYYY-MM-DD 至 YYYY-MM-DD
> 最后整理：YYYY-MM-DD

---

## 概述

[对这个主题的整体概述，2-3 句话]

---

## [分类 1]

### [子主题 1.1]

[整理后的内容]

### [子主题 1.2]

[整理后的内容]

---

## [分类 2]

### [子主题 2.1]

[整理后的内容]

---

## 待补充

- [ ] [识别出的信息缺口 1]
- [ ] [识别出的信息缺口 2]

---

## 原始来源

- [原文档 1 标题](链接) — YYYY-MM-DD
- [原文档 2 标题](链接) — YYYY-MM-DD

---

> 本文档由 AI 助手整理，原始笔记已保留。

Step 5: Save the Refined Document

Ask the user's preference:

Create new — Save as a new document (recommended for multi-doc consolidation)
Update in place — Replace the original document (for single doc refinement)

For new document:

Tool: yuque_create_doc
Parameters:
  repo_id: "<namespace>"
  title: "[主题标题]"
  body: "<refined content>"
  format: "markdown"


For in-place update:

Tool: yuque_update_doc
Parameters:
  repo_id: "<namespace>"
  doc_id: "<slug>"
  body: "<refined content>"

Step 6: Confirm
✅ 笔记整理完成！

📄 **[[主题标题]](文档链接)**
📚 已保存到：「知识库名称」

### 整理成果
- 📥 输入：X 篇原始笔记，约 XXXX 字
- 📤 输出：1 篇结构化文档，约 XXXX 字
- 🔄 去除重复：X 处
- 🕳️ 标记待补充：X 处

💡 原始笔记已保留，可随时对照。

Guidelines
Always preserve the original notes — refine into a new document by default
Don't discard information during deduplication; merge and enrich instead
Maintain the user's voice and terminology — don't over-formalize casual notes
Flag uncertain interpretations with "【待确认】" markers
For daily captures, suggest a weekly or bi-weekly refinement cadence
If notes span multiple topics, create separate refined documents per topic
Add a "待补充" section for identified gaps — this helps the user know what to add later
Default language is Chinese
Error Handling
Situation	Action
Source notes are too few (<3 items)	Refine what's available; suggest capturing more first
Source notes are too many (>10 docs)	Focus on most recent or ask user to narrow the scope
Content is already well-structured	Tell user honestly; suggest minor improvements only
yuque_update_doc fails	Fall back to creating a new document
Mixed languages in notes	Maintain the dominant language; don't force translation
Weekly Installs
117
Repository
yuque/yuque-plugin
GitHub Stars
71
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass