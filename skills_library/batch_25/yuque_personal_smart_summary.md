---
title: yuque-personal-smart-summary
url: https://skills.sh/yuque/yuque-plugin/yuque-personal-smart-summary
---

# yuque-personal-smart-summary

skills/yuque/yuque-plugin/yuque-personal-smart-summary
yuque-personal-smart-summary
Installation
$ npx skills add https://github.com/yuque/yuque-plugin --skill yuque-personal-smart-summary
SKILL.md
Smart Summary — Yuque Knowledge Base & Document Summarization

Generate intelligent summaries for an entire knowledge base or a set of documents, helping users quickly understand content landscape, key themes, and important insights.

When to Use
User wants an overview of a knowledge base
User says "帮我总结一下这个知识库", "summarize my repo", "这个库里都有什么"
User wants a summary of multiple related documents
User says "帮我做个知识盘点", "generate a project summary from my docs"
User wants periodic knowledge review
Required MCP Tools

All tools are from the yuque-mcp server:

yuque_list_repos — List personal knowledge bases
yuque_get_repo_toc — Get the table of contents of a knowledge base
yuque_get_doc — Read full document content
yuque_search — Search documents by keyword (for topic-based summaries)
Workflow
Step 1: Identify Scope

Determine what the user wants summarized:

Option A: Entire knowledge base

Tool: yuque_list_repos
Parameters:
  type: "user"


Then let the user pick a repo, or use the one they specified.

Option B: Specific topic across repos

Tool: yuque_search
Parameters:
  query: "<topic keywords>"
  type: "doc"


Option C: User specifies exact documents Proceed directly to reading them.

Step 2: Get Document List

For a knowledge base summary, get the table of contents:

Tool: yuque_get_repo_toc
Parameters:
  repo_id: "<namespace>"


This gives you the full structure — titles, hierarchy, and document slugs.

Step 3: Sample and Read Documents

For large knowledge bases (>20 docs), use a sampling strategy:

Read all documents if ≤10 docs
Sample strategically if >10 docs:
Read the top-level / introductory documents first
Pick 2-3 documents from each major section
Prioritize recently updated documents
Read up to 10-15 documents total
Tool: yuque_get_doc
Parameters:
  repo_id: "<namespace>"
  doc_id: "<slug>"

Step 4: Analyze and Categorize

As you read, track:

Main themes — What topics are covered
Content types — Tutorials, references, notes, specs, etc.
Coverage depth — Which areas are well-documented vs sparse
Freshness — How recently content was updated
Connections — How documents relate to each other
Step 5: Generate Summary

Compose the summary in the following format:

## 📚 知识库摘要：「知识库名称」

### 概览
- **文档总数**：X 篇
- **最近更新**：YYYY-MM-DD
- **主要语言**：中文/英文/混合

---

### 🗂️ 内容结构

知识库包含以下主要板块：

1. **[板块名称]**（X 篇文档）
   - [简要描述这个板块的内容]
   - 代表文档：[文档标题](链接)

2. **[板块名称]**（X 篇文档）
   - [简要描述]
   - 代表文档：[文档标题](链接)

3. **[板块名称]**（X 篇文档）
   - [简要描述]
   - 代表文档：[文档标题](链接)

---

### 🔑 核心要点

从整个知识库中提炼的关键信息：

1. **[要点 1]**：[2-3 句话概括]
2. **[要点 2]**：[2-3 句话概括]
3. **[要点 3]**：[2-3 句话概括]
4. **[要点 4]**：[2-3 句话概括]
5. **[要点 5]**：[2-3 句话概括]

---

### 📊 知识库健康度

| 指标 | 状态 |
|------|------|
| 内容覆盖 | [全面/有缺口/待补充] |
| 更新频率 | [活跃/一般/较少更新] |
| 结构清晰度 | [清晰/一般/需要整理] |
| 文档质量 | [高/中/参差不齐] |

---

### 💡 建议

- [建议 1：如"XX 板块内容较少，建议补充"]
- [建议 2：如"部分文档超过 6 个月未更新，建议检查时效性"]
- [建议 3：如"建议添加一篇总览文档串联各板块"]

Step 6: Multi-Document Summary (Alternative)

If summarizing specific documents rather than a whole repo:

## 📄 文档摘要

### 文档列表
| # | 标题 | 知识库 | 更新时间 |
|---|------|--------|----------|
| 1 | [标题](链接) | 「库名」 | YYYY-MM-DD |
| 2 | [标题](链接) | 「库名」 | YYYY-MM-DD |

### 综合摘要

[3-5 段话，综合所有文档的核心内容，突出共同主题和关键信息]

### 各文档要点

#### 1. [文档标题]
- [要点 1]
- [要点 2]
- [要点 3]

#### 2. [文档标题]
- [要点 1]
- [要点 2]
- [要点 3]

### 文档间关联
- [文档 A 和文档 B 在 XX 方面互相补充]
- [文档 C 是文档 A 的深入展开]

Guidelines
Always answer in the same language the user used (Chinese or English)
For large knowledge bases, be upfront about sampling: "知识库共有 X 篇文档，我抽样阅读了 Y 篇进行分析"
Focus on actionable insights, not just listing document titles
Highlight gaps and opportunities — what's missing is as valuable as what's there
Include document links so users can dive deeper into any topic
This skill summarizes personal repos — for team repos, use the corresponding skill in the yuque-group plugin
Error Handling
Situation	Action
yuque_list_repos returns empty	Ask user for the exact repo name or ID
yuque_get_repo_toc returns empty	Inform user the knowledge base appears to be empty
yuque_get_doc fails (404)	Skip this doc, note it may have been deleted
yuque_get_doc fails (403)	Tell user they may lack permission to access this doc
API timeout	Retry once, then inform user of connectivity issue
Knowledge base has >50 docs	Sample 10-15 docs, clearly state the sampling approach
Weekly Installs
188
Repository
yuque/yuque-plugin
GitHub Stars
71
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn