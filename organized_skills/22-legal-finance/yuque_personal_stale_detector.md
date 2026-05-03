---
rating: ⭐⭐⭐
title: yuque-personal-stale-detector
url: https://skills.sh/yuque/yuque-plugin/yuque-personal-stale-detector
---

# yuque-personal-stale-detector

skills/yuque/yuque-plugin/yuque-personal-stale-detector
yuque-personal-stale-detector
Installation
$ npx skills add https://github.com/yuque/yuque-plugin --skill yuque-personal-stale-detector
SKILL.md
Stale Detector — Yuque Knowledge Base Freshness Check

Scan your Yuque knowledge bases to detect documents that haven't been updated for a long time and may contain outdated information, helping you maintain a healthy and accurate knowledge base.

When to Use
User wants to find outdated documents in their knowledge base
User says "检查一下哪些文档过期了", "find stale docs", "我的知识库有哪些需要更新"
User wants to do periodic knowledge base maintenance
User says "帮我做个知识库健康检查", "哪些文档很久没更新了"
Required MCP Tools

All tools are from the yuque-mcp server:

yuque_list_repos — List personal knowledge bases
yuque_get_repo_toc — Get the table of contents with document metadata
yuque_get_doc — Read document content to check for staleness signals
Workflow
Step 1: Select Knowledge Base

If the user specifies a repo, use it directly. Otherwise, list available repos:

Tool: yuque_list_repos
Parameters:
  type: "user"


Let the user pick which repo(s) to scan, or scan all if requested.

Step 2: Get Document List with Metadata

For each repo, get the table of contents:

Tool: yuque_get_repo_toc
Parameters:
  repo_id: "<namespace>"


Extract from each document entry:

title — Document title
slug — Document identifier
updated_at — Last update timestamp
created_at — Creation timestamp
Step 3: Classify Documents by Freshness

Calculate the age of each document (days since last update) and classify:

Category	Age	Emoji
🟢 新鲜 (Fresh)	< 90 days	Recently updated, likely current
🟡 老化 (Aging)	90-180 days	May need review
🟠 陈旧 (Stale)	180-365 days	Likely needs update
🔴 过期 (Expired)	> 365 days	High risk of outdated content
Step 4: Deep Scan Suspicious Documents (Optional)

For documents classified as 🟠 or 🔴, optionally read their content to check for additional staleness signals:

Tool: yuque_get_doc
Parameters:
  repo_id: "<namespace>"
  doc_id: "<slug>"


Look for:

Version references — Mentions of specific software versions that may be outdated
Date references — Hardcoded dates like "2023年计划", "Q1 目标"
Broken patterns — References to tools, APIs, or processes that may have changed
Temporal language — "目前", "最近", "即将" that imply time-sensitive content

Limit deep scanning to 5-10 documents to avoid excessive API calls.

Step 5: Generate Report
## 🔍 知识库健康检查报告

### 📚 扫描范围
- **知识库**：「知识库名称」
- **文档总数**：X 篇
- **扫描时间**：YYYY-MM-DD

---

### 📊 整体健康度

| 状态 | 数量 | 占比 |
|------|------|------|
| 🟢 新鲜（<90天） | X 篇 | XX% |
| 🟡 老化（90-180天） | X 篇 | XX% |
| 🟠 陈旧（180-365天） | X 篇 | XX% |
| 🔴 过期（>365天） | X 篇 | XX% |

**健康评分：X/10**

---

### 🔴 需要立即关注（过期文档）

| # | 文档标题 | 最后更新 | 已过天数 | 风险说明 |
|---|----------|----------|----------|----------|
| 1 | [标题](链接) | YYYY-MM-DD | X 天 | [如：包含版本号引用] |
| 2 | [标题](链接) | YYYY-MM-DD | X 天 | [如：含有时间敏感内容] |

### 🟠 建议检查（陈旧文档）

| # | 文档标题 | 最后更新 | 已过天数 |
|---|----------|----------|----------|
| 1 | [标题](链接) | YYYY-MM-DD | X 天 |
| 2 | [标题](链接) | YYYY-MM-DD | X 天 |

### 🟡 可以关注（老化文档）

[列出文档标题和更新时间，简要列表即可]

---

### 💡 维护建议

1. **优先处理**：[具体建议，如"XX 文档引用了 v2.x 版本，当前已是 v4.x"]
2. **批量更新**：[如"XX 板块的 X 篇文档都超过半年未更新，建议集中审查"]
3. **考虑归档**：[如"XX 文档可能已不再适用，建议归档或标记为历史文档"]
4. **定期检查**：建议每 [月/季度] 运行一次过期检测，保持知识库健康

---

### 📈 趋势观察

- **最活跃板块**：[哪个板块更新最频繁]
- **最冷门板块**：[哪个板块最久没动过]
- **更新模式**：[如"大部分更新集中在工作日"，"XX 板块有周期性更新"]

Guidelines
Always answer in the same language the user used (Chinese or English)
Be helpful, not alarming — old documents aren't necessarily bad (some content is evergreen)
Distinguish between time-sensitive content (API docs, process guides) and evergreen content (principles, tutorials)
Provide actionable suggestions — don't just list stale docs, suggest what to do about them
When deep scanning, highlight specific outdated references (version numbers, dates, deprecated tools)
This skill scans personal repos — for team repos, use the corresponding skill in the yuque-group plugin
Error Handling
Situation	Action
yuque_list_repos returns empty	Ask user for the exact repo name or ID
yuque_get_repo_toc returns empty	Inform user the knowledge base appears to be empty
yuque_get_doc fails (404)	Note the document may have been deleted (itself a finding!)
yuque_get_doc fails (403)	Tell user they may lack permission to access this doc
API timeout	Retry once, then inform user of connectivity issue
All documents are fresh	Congratulate the user on maintaining a healthy knowledge base!
Knowledge base has >100 docs	Use metadata-only analysis (skip deep scan), offer to deep scan specific sections
Weekly Installs
111
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