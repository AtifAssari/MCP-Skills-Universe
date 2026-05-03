---
rating: ⭐⭐⭐
title: openclaw-help
url: https://skills.sh/wghust/stark-skills/openclaw-help
---

# openclaw-help

skills/wghust/stark-skills/openclaw-help
openclaw-help
Installation
$ npx skills add https://github.com/wghust/stark-skills --skill openclaw-help
SKILL.md
openclaw-help Skill

Language: Respond in the same language as the user (中文提问则中文回答).

Answer OpenClaw usage questions using the bundled reference (橙皮书 extracts) and official docs (docs.openclaw.ai). When the two conflict, prefer official docs. When neither suffices, trigger WebSearch.

Reference is derived from OpenClaw橙皮书 v1.2.0; for latest details, prefer docs.openclaw.ai.

Knowledge Sources
1. Embedded Reference (bundled)
Path: reference.md (sibling to SKILL.md in the openclaw-help skill directory)
Content: FAQ, Command Cheat Sheet, Resources, Architecture, Deployment, Channels, Skills, Model providers, Security
Retrieval: Grep reference.md → Read matching regions
2. Official Docs (Remote)
Base: https://docs.openclaw.ai
Getting Started: https://docs.openclaw.ai/start/getting-started
Doc Index: https://docs.openclaw.ai/llms.txt (discover channels, cli, install pages)
Retrieval: WebFetch to fetch relevant pages
3. Alignment Rule
On conflict (e.g., Node version, command syntax): prefer official docs
Install / quick start / commands: MUST reference official docs in the answer
Execution Flow
Step 0 · Trigger Check

Activate when user asks about OpenClaw usage: deployment, channel integration, configuration, errors, Skills, 养虾, etc.

Step 1 · Retrieve from Reference
Extract 2–5 keywords from the user question (e.g., 部署, Telegram, Skills, openclaw doctor, FAQ)
Grep reference.md in the skill directory for those keywords
Read matching regions with context (e.g., ±50 lines)
If no hits or content insufficient → treat as "reference no cover"

Query → Section mapping (优先 Read 对应段落以快速获取完整回答):

查询示例	reference 段落
国内云、阿里云、腾讯云、百度、火山、华为、扣子、一键部署	## 国内云厂商一键部署
xxx 接入、Telegram/Discord/飞书/钉钉/QQ/WhatsApp	## Channels 渠道 及对应子节
首次配置、gateway.auth、openclaw doctor、backup	### 首次配置 Initial Configuration
远程访问、Tailscale、SSH 端口转发	### 远程访问 Remote Access
Step 2 · Retrieve from Official Docs

Use WebFetch (or mcp_web_fetch) to fetch relevant docs pages:

Question Type	Fetch
Install / quick start	https://docs.openclaw.ai/start/getting-started
Channel (Telegram, Discord, etc.)	https://docs.openclaw.ai/channels/telegram.md (or corresponding channel)
CLI command (doctor, gateway, etc.)	https://docs.openclaw.ai/cli/doctor.md (or corresponding cli page)
General	Check https://docs.openclaw.ai/llms.txt for page URLs

If WebFetch fails → continue with reference or fallback; note network issue.

Step 3 · Synthesize Answer
Found In	Action
Both reference and official docs	Synthesize from both; prefer official docs on version/command details
Reference only	Answer from reference; add "建议同时查阅 [官方文档链接] 以确认最新版本"
Official docs only	Answer from official docs
Neither	Proceed to Step 4 (WebSearch fallback)
Step 4 · WebSearch Fallback

When neither reference nor official docs has sufficient content:

Invoke WebSearch with the user question (and OpenClaw-related refinements)
Organize answer from search results
Note: "Reference 与官方文档未覆盖，以下来自网络搜索"
Reference Attribution
From reference: Cite section (e.g., "据 reference 渠道章节…")
From official docs: Include docs.openclaw.ai link (e.g., https://docs.openclaw.ai/start/getting-started)
From web search: Note "Reference 与官方文档未覆盖，以下来自网络搜索"
Examples
Example A — Telegram 接入 (Chinese)

Input: "OpenClaw 如何接入 Telegram？"

Actions:

Grep reference.md for "Telegram"
WebFetch https://docs.openclaw.ai/channels/telegram.md
Synthesize from both; prefer official docs on setup steps
Cite reference Channels section and link to docs.openclaw.ai/channels/telegram
Example B — openclaw doctor (Chinese)

Input: "openclaw doctor 是干什么的？"

Actions:

Grep reference.md for "doctor" or "诊断"
WebFetch https://docs.openclaw.ai/cli/doctor.md
Synthesize; prefer official docs on command flags
Example C — Quick start (官方文档为主)

Input: "OpenClaw 快速开始怎么装？"

Actions:

WebFetch https://docs.openclaw.ai/start/getting-started (primary)
Optional: Grep reference.md for "安装"
Answer primarily from official docs; add reference background if relevant
Example D — ClawHub Skill 安全 (Reference FAQ)

Input: "ClawHub Skill 安全吗？"

Actions:

Grep reference.md for "ClawHub" or "安全"
WebFetch docs if relevant; reference FAQ Q9 likely sufficient
Cite reference FAQ section
Example E — Fallback

Input: Question not covered by reference or official docs

Actions:

WebSearch
Organize answer; note "Reference 与官方文档未覆盖，以下来自网络搜索"
Error Handling
Situation	Action
WebFetch fails (network)	Proceed with reference; note "官方文档暂时不可达，建议稍后查阅 docs.openclaw.ai"
Grep returns no hits in reference	Rely on official docs or WebSearch
reference.md not found	Use official docs and WebSearch
Conflict between sources	Prefer official docs
Weekly Installs
8
Repository
wghust/stark-skills
GitHub Stars
4
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn