---
title: yuque-personal-daily-capture
url: https://skills.sh/yuque/yuque-plugin/yuque-personal-daily-capture
---

# yuque-personal-daily-capture

skills/yuque/yuque-plugin/yuque-personal-daily-capture
yuque-personal-daily-capture
Installation
$ npx skills add https://github.com/yuque/yuque-plugin --skill yuque-personal-daily-capture
SKILL.md
Daily Capture — Quick Idea & Note Capture to Yuque

Help the user quickly capture ideas, thoughts, meeting insights, reading annotations, and any fleeting information into their personal Yuque knowledge base with minimal friction.

When to Use
User wants to quickly jot down an idea or thought
User says "记一下", "帮我记录", "capture this", "写个笔记"
User shares a fleeting thought, inspiration, or meeting insight
User says "这个想法先记下来", "随手记", "快速记录"
Required MCP Tools

All tools are from the yuque-mcp server:

yuque_list_repos — List personal repos to find the capture target
yuque_search — (Optional) Find today's capture doc if appending
yuque_list_docs — (Optional) Check if today's daily note exists
yuque_create_doc — Create a new capture document
yuque_update_doc — Append to an existing capture document
Workflow
Step 1: Receive the Capture

The user's input can be:

A raw idea or thought (1-2 sentences)
A longer note with context
A quote or snippet from something they read
A meeting insight or action item
A mix of the above

Classify the capture type:

Type	Icon	Example
💡 想法/灵感	💡	"突然想到可以用 Redis 做缓存"
📝 笔记	📝	"今天学到 Go 的 context 用法..."
📖 阅读批注	📖	"这篇文章提到的观点很有意思..."
🎯 待办/行动	🎯	"记得下周跟进 API 设计评审"
💬 会议灵感	💬	"会上讨论到的架构方案值得深入..."
🔗 链接/资源	🔗	"这个工具不错：https://..."
Step 2: Determine Capture Strategy

Two strategies based on user preference:

Strategy A: Daily Note (Default)

Append to today's daily capture document. If it doesn't exist, create one.

Strategy B: Standalone Note

Create a separate document for this capture (for longer or topic-specific notes).

If the user's input is short (< 100 words), default to Strategy A. If longer or clearly a standalone topic, use Strategy B. Ask if unclear.

Step 3A: Daily Note — Append Mode

Check if today's daily note exists:

Tool: yuque_search
Parameters:
  query: "每日捕获 YYYY-MM-DD"
  type: "doc"


If found, append to it:

Tool: yuque_update_doc
Parameters:
  repo_id: "<namespace>"
  doc_id: "<slug>"
  body: "<existing content>\n\n---\n\n### [HH:MM] [类型图标] [简短标题]\n\n[捕获内容]\n"


If not found, create today's daily note:

Tool: yuque_create_doc
Parameters:
  repo_id: "<namespace>"
  title: "📥 每日捕获 YYYY-MM-DD"
  body: "<daily note template with first capture>"
  format: "markdown"


Daily note template:

# 📥 每日捕获 YYYY-MM-DD

> 今日碎片化记录，定期整理归档。

---

### [HH:MM] [类型图标] [简短标题]

[捕获内容]

[标签：#tag1 #tag2]

Step 3B: Standalone Note
Tool: yuque_list_repos
Parameters:
  type: "user"

Tool: yuque_create_doc
Parameters:
  repo_id: "<namespace>"
  title: "[类型图标] [标题]"
  body: "<formatted note>"
  format: "markdown"

Step 4: Confirm

For daily note append:

✅ 已捕获！

[类型图标] **[简短标题]** → 已追加到「📥 每日捕获 YYYY-MM-DD」

💡 今日已捕获 X 条记录。


For standalone note:

✅ 笔记已创建！

📄 **[[类型图标] 标题](文档链接)**
📚 已保存到：「知识库名称」

Guidelines
Speed is everything — minimize questions, maximize capture
If the user just throws a sentence at you, capture it immediately; don't ask for clarification
Auto-generate a short title from the content if the user doesn't provide one
Add relevant tags based on content analysis (e.g., #技术, #产品, #灵感)
Keep the formatting lightweight — this is a quick capture, not a polished document
Default to daily note append mode for short captures
Suggest periodic review: "你的每日捕获已经积累了不少，要整理一下吗？" (link to note-refine skill)
Default language is Chinese
Error Handling
Situation	Action
No capture repo found	Ask user which repo to use, or suggest creating a "随手记" repo
yuque_update_doc fails	Fall back to creating a new standalone note
yuque_search can't find today's note	Create a new daily note document
User input is ambiguous	Capture as-is with 📝 type; don't over-classify
Very long input (>500 words)	Switch to standalone note strategy automatically
Weekly Installs
166
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