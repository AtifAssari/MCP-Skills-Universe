---
title: session-wrap
url: https://skills.sh/leonsong09/session-wrap/session-wrap
---

# session-wrap

skills/leonsong09/session-wrap/session-wrap
session-wrap
Installation
$ npx skills add https://github.com/leonsong09/session-wrap --skill session-wrap
SKILL.md
Session Wrap Skill
Overview

Use this skill to close out the current coding session in a way that is easy to resume later. Focus on what was actually finished, what is still open, what was learned, and what should happen next.

Core Rules
Scope is the current session unless the user explicitly asks for a broader range.
Prioritize outcomes, decisions, learnings, and follow-up actions over process chatter.
Do not output a chronological 流水账.
Do not claim work is completed unless there is evidence in the session, git status, or validation output.
If the user asks to write files, commit, or update docs, summarize first and then confirm the action.
Workflow
Step 1: Confirm scope

Default to the current session. If the user already gave a clear wrap-up request, do not ask extra questions.

Clarify only when needed:

current session only or also include earlier sessions
whether to include commit advice
whether to produce a handoff note or just a chat summary
Step 2: Inspect the working tree

Collect the minimum evidence needed to summarize the session accurately.

Recommended commands:

git status --short
git diff --stat
git log --oneline -n 10


If the repository state is not available, say so explicitly and continue with the session evidence you do have.

Step 3: Summarize completed work

Summarize by workstream instead of by timestamp.

Preferred structure:

本次完成
关键决策
涉及文件 / 模块
已做验证

If there were no meaningful code changes, say that clearly instead of inventing成果.

Step 4: Extract learnings and open items

Capture the parts that matter for the next session:

new findings
mistakes avoided or lessons learned
known risks
unfinished tasks
blockers or dependencies

Keep this section concise and operational.

Step 5: Offer next actions and commit guidance

When relevant, finish with:

suggested next steps
whether a commit is appropriate now
a possible commit message direction
whether additional verification is still needed

Do not auto-commit. Recommend commit timing only when there is enough evidence.

Recommended Output Shape
## 本次会话总结

### 已完成
- ...

### 关键决策
- ...

### 涉及文件 / 模块
- ...

### 验证情况
- 已验证：...
- 未验证：...

### 经验与风险
- ...

### 下一步建议
- ...

When to Use
用户说“总结会话”
用户说“收尾”或“会话收尾”
当前会话已经完成一段明确工作，需要压缩成可复用总结
需要为下一次继续工作准备 handoff
When Not to Use
用户要的是“今天所有会话”的汇总，而不是当前会话
用户要的是纯 commit 日报
当前会话几乎没有实际工作内容，只是简单问答

In those cases, prefer a daily summary or research-note style skill instead.

Quality Checklist

Before responding, verify:

 Summary is scoped to the current session unless user asked otherwise
 Completed work is grouped by workstream, not by timeline
 Validation is reported honestly
 Risks and unfinished items are explicit
 No fake completion, fake commit readiness, or fake verification claims
Weekly Installs
12
Repository
leonsong09/session-wrap
GitHub Stars
8
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass