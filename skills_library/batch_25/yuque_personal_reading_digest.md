---
title: yuque-personal-reading-digest
url: https://skills.sh/yuque/yuque-plugin/yuque-personal-reading-digest
---

# yuque-personal-reading-digest

skills/yuque/yuque-plugin/yuque-personal-reading-digest
yuque-personal-reading-digest
Installation
$ npx skills add https://github.com/yuque/yuque-plugin --skill yuque-personal-reading-digest
SKILL.md
Reading Digest — Document Summarization & Reading Notes

Help the user quickly distill a Yuque document into a structured reading digest with key takeaways, core arguments, and actionable insights.

When to Use
User wants a summary of a long Yuque document
User says "帮我总结这篇文档", "summarize this doc", "生成阅读摘要"
User wants to extract key points from an article for future reference
User says "这篇文章讲了什么", "帮我提炼要点"
Required MCP Tools

All tools are from the yuque-mcp server:

yuque_search — Find the target document by keyword
yuque_get_doc — Read the full document content
yuque_list_repos — List personal repos to find the save target
yuque_create_doc — Save the reading digest as a new document
Workflow
Step 1: Locate the Document

The user may provide:

A document title or keyword
A direct Yuque document URL
A repo + doc reference

If the user provides a keyword or title:

Tool: yuque_search
Parameters:
  query: "<keyword>"
  type: "doc"


If the user provides a URL or specific reference, extract the repo_id and doc_id directly.

Step 2: Read the Document
Tool: yuque_get_doc
Parameters:
  repo_id: "<namespace>"
  doc_id: "<slug>"


If the document is very long, note the total length and proceed with the full content.

Step 3: Generate the Reading Digest

Analyze the document and produce a structured digest:

# 📖 阅读摘要：[文档标题]

> **原文**：[文档标题](文档链接)
> **作者**：[作者]
> **阅读日期**：YYYY-MM-DD
> **预计阅读时间**：约 X 分钟

---

## 🎯 一句话总结

[用一句话概括文档的核心观点或目的]

---

## 📌 关键要点

1. **[要点 1]**：[简要说明]
2. **[要点 2]**：[简要说明]
3. **[要点 3]**：[简要说明]
4. **[要点 4]**：[简要说明]
5. **[要点 5]**：[简要说明]

---

## 🧠 核心论点与逻辑

[梳理文档的核心论证逻辑，2-3 段]

---

## 💡 启发与思考

- [这篇文档对我的启发 1]
- [这篇文档对我的启发 2]
- [可以应用到的场景]

---

## 📝 原文金句

> [摘录文档中值得记住的精彩段落 1]

> [摘录文档中值得记住的精彩段落 2]

---

## 🔗 相关延伸

- [可以进一步阅读的方向 1]
- [可以进一步阅读的方向 2]

---

> 本摘要由 AI 助手生成，建议结合原文阅读。

Step 4: Review with User

Present the digest to the user and ask:

"摘要是否准确？有需要调整的地方吗？"
"要保存到你的语雀知识库吗？"
Step 5: (Optional) Save to Yuque

If the user wants to save:

Tool: yuque_list_repos
Parameters:
  type: "user"


Find or ask for the target repo (often "阅读笔记" or "读书摘要").

Tool: yuque_create_doc
Parameters:
  repo_id: "<namespace>"
  title: "📖 阅读摘要：[原文标题]"
  body: "<formatted digest>"
  format: "markdown"

Step 6: Confirm
✅ 阅读摘要已生成并保存！

📄 **[📖 阅读摘要：原文标题](文档链接)**
📚 已归档到：「知识库名称」

### 摘要概览
- 提炼了 X 个关键要点
- 摘录了 X 条原文金句
- 生成了 X 个延伸阅读方向

Guidelines
Preserve the author's original intent — don't distort or over-simplify
Key points should be specific and actionable, not vague generalizations
Include direct quotes from the original for important claims
The "启发与思考" section should be personalized — relate to the user's context if known
Default language is Chinese; match the original document's language
For very long documents (>5000 words), consider breaking the digest into sections matching the original structure
Error Handling
Situation	Action
yuque_search returns no results	Ask user for the exact document URL or repo/slug
yuque_get_doc fails (404)	Document may have been deleted; inform user
yuque_get_doc fails (403)	User may lack permission; suggest checking access
Document is very short (<200 words)	Generate a brief summary instead of full digest template
Document is non-text (slides, spreadsheet)	Inform user this skill works best with text documents
Weekly Installs
199
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