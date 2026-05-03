---
title: work-record
url: https://skills.sh/liulixiang1988/agent-skills/work-record
---

# work-record

skills/liulixiang1988/agent-skills/work-record
work-record
Installation
$ npx skills add https://github.com/liulixiang1988/agent-skills --skill work-record
SKILL.md
Work Record

Record work summaries and manage TODO items in a monthly work log file, for performance review reference and task tracking.

File Path

The work log file is located at:

{USERPROFILE}\OneDrive\文档\notes\Work\M365\Work Log\Work log-{YYYY}-{MM}.md

{USERPROFILE} — Resolve via the USERPROFILE environment variable on Windows.
{YYYY} — 4-digit year, {MM} — 2-digit month

Use today's date to determine which year-month file to write to.

Mode Detection

Determine which mode to use based on user intent:

TODO mode: User wants to add a TODO item (e.g., "加一个todo", "add a todo", "添加待办")
Record mode: User wants to record work done (e.g., "记录工作", "save work", "记录一下")
Workflow: TODO Mode
Determine the file path — Use the current date to build the full path.
Read the existing file — If it exists, read content. If not, create it.
Find or create the TODO section — Look for a ## TODO section in the file. If it doesn't exist, insert it at the top of the file (before any work log entries).
Add the TODO item — Append a new unchecked item under the ## TODO section.
TODO Section Format
## TODO

- [ ] {YYYY-MM-DD} {todo内容}
- [ ] {YYYY-MM-DD} {todo内容}
- [x] {YYYY-MM-DD} {todo内容} ✅ {完成日期}


Each TODO item is a Markdown checkbox with the date it was added and a description. Completed items use [x] and append a ✅ with the completion date.

Workflow: Record Mode
Determine the file path — Use the current date to build the full path.
Read the existing file — If the file exists, read its content. If not, create it.
Update TODOs — If a ## TODO section exists, review the current conversation to determine if any TODO items were addressed. For each addressed TODO:
Mark it as done: change - [ ] to - [x] and append ✅ {YYYY-MM-DD} (today's date)
If the work changed the scope or details of a TODO, update its description accordingly
Summarize the work — Write a concise summary in Chinese (中文) covering:
What task or problem was worked on
Key changes made (files modified, features added, bugs fixed, etc.)
Any notable decisions or outcomes
Related work item IDs / PR links if available
Append the work entry — Add the new entry to the end of the file (after the TODO section).
Entry Format
### {YYYY-MM-DD} {简短标题}

{工作内容摘要}

- **任务/背景**: {做了什么，为什么做}
- **主要改动**: {关键改动点}
- **相关链接**: {PR链接、工作项ID等，如果有的话}

---


If there are multiple distinct tasks in one session, create separate entries or group them under a single date heading.

Important Notes
Always append work entries — never overwrite existing content.
The ## TODO section is always at the top of the file, before any work log entries.
When updating TODOs, only mark items as done if the current session's work clearly addresses them. Do not guess.
If the directory does not exist, create it.
Write in Chinese (中文).
Keep entries concise but useful for performance review writing.
After writing, confirm to the user what was recorded/added and where the file is located.
Weekly Installs
12
Repository
liulixiang1988/…t-skills
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass