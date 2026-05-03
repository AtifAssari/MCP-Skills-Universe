---
rating: ⭐⭐⭐
title: skywork excel
url: https://skills.sh/skyworkai/skywork-skills/skywork-excel
---

# skywork excel

skills/skyworkai/skywork-skills/Skywork Excel
Skywork Excel
Installation
$ npx skills add https://github.com/skyworkai/skywork-skills --skill 'Skywork Excel'
SKILL.md
Excel Generator

Generate professional Excel files and data analysis reports using the Skywork Excel backend service.

Prerequisites
API Key Configuration (Required First)

This skill requires a SKYWORK_API_KEY to be configured in OpenClaw.

If you don't have an API key yet, please visit: https://skywork.ai

For detailed setup instructions, see: references/apikey-fetch.md

🚫 CRITICAL: Pass Query As-Is, Do NOT Read User Files
NEVER use the read tool on user-provided files (Excel, PDF, CSV, images, etc.). Pass file paths via --files and let the backend handle reading.
Do NOT rewrite, expand, or reinterpret the user's query. Pass it as-is. The backend agent has its own understanding capabilities.
Only two modifications are allowed:
Time info: For time-sensitive queries, prepend current time: [Current time: 2026-03-14] User request: ...
File paths: Replace absolute paths with filenames only (e.g., /Users/xxx/report.xlsx → report.xlsx)
Workflow

Excel tasks take 5-25 minutes. Run the script in background and poll the log every 60 seconds.

Step 1: Start Task
EXCEL_LOG=/tmp/excel_$(date +%s).log

python3 scripts/excel_api_client.py "user's query" \
  --files "/path/to/file1.xlsx" "/path/to/file2.pdf" \
  --language zh-CN \
  --log-path "$EXCEL_LOG" \
  > /dev/null 2>&1 &

echo "Task started. Log: $EXCEL_LOG"

--files: Upload user-provided files (Excel, CSV, PDF, Image). Omit if no files.
--language: zh-CN (default) or en-US — match the user's language.
--session <id>: For follow-up tasks — see Multi-Turn Sessions.
Step 2: Monitor Progress

Execution pattern (required):

Run the Step 1 start command in background and note the EXCEL_LOG path from the output.
Then execute the Step 2 monitor command separately every 60 seconds (do not use a while loop).
$EXCEL_LOG does not persist between exec calls — Step 2 MUST recover the path (see monitor command below).

Rules — no exceptions:

Poll every 60 seconds by calling exec tool repeatedly. Do NOT use a while loop.
Show only the last TASK PROGRESS UPDATE block. Do not output full log (tail -50, etc.) or summarize/interpret it.
Never restart the task. The agent handles errors internally and auto-recovers.
Ignore transient errors in the log (❌, Missing parameter, heartbeat pings, etc.) — the agent retries automatically.
Use heartbeat as liveness signal: check heartbeat lines every poll to confirm the task is still running, but do NOT output raw heartbeat lines to the user.

Every 60 seconds, run:

# Recover log path: use the path printed by Step 1, or find the most recent log
EXCEL_LOG=$(ls -t /tmp/excel_*.log 2>/dev/null | head -1)
if [ -z "$EXCEL_LOG" ] || [ ! -f "$EXCEL_LOG" ]; then
  echo "ERROR: Log not found. Ensure Step 1 ran with --log-path."; exit 1
fi
sleep 60
echo "=== Progress Update ==="
grep -A8 "TASK PROGRESS UPDATE" "$EXCEL_LOG" | tail -10
grep -E "\[HEARTBEAT\]" "$EXCEL_LOG" | tail -1
grep -E "\[DONE\]|All done" "$EXCEL_LOG" | tail -1

What to report to user

CRITICAL: Output ONLY the current status. Do NOT repeat or accumulate previous status messages. Each update should be a single, fresh line.

After each log read, output ONLY ONE LINE showing the current status:

[Main stage] | [current action] | Elapsed: Xs


Example (output only this single line, nothing else):

Data Processing | Generating charts | Elapsed: 120s

Progress contains	Main stage
"读取" / "read" / "load"	Loading data
"分析" / "analysis"	Data analysis
"图表" / "chart" / "visualization"	Generating charts
"Excel" / "xlsx"	Creating Excel file
"HTML" / "报告" / "report"	Generating report
"保存" / "save" / "output"	Saving output

Stop polling when log contains [DONE] or ✅ All done! → read final output:

tail -30 "$EXCEL_LOG"

If NOT done → report progress to user, then call exec again after 60 seconds with the same monitor command.
Repeat until done — keep calling exec every 60 seconds until [DONE] or All done appears.
Do NOT stop after a single poll.
Step 3: Deliver Result

After completion, provide the user with both:

OSS download URL — cloud link for sharing (show as a clickable hyperlink)
Local file path — absolute path on their machine

Example reply:

✅ Report generated!

📥 Download: https://picture-search.skywork.ai/skills/upload/2026-03-14/xxx.xlsx
💾 Local: /Users/xxx/.openclaw/workspace/report.xlsx


Do NOT use sandbox:// or [filename](sandbox://...) format — these are not clickable. If oss_url is unavailable, provide the local path only.

Multi-Turn Sessions

To continue a previous task, use --session with the ID printed at the end of the previous run:

# First turn — no --session needed; session ID is printed at end
python3 scripts/excel_api_client.py "Create a sales report" \
  --language zh-CN --log-path "$EXCEL_LOG" > /dev/null 2>&1 &
# Output: 💡 To continue this conversation, use: --session abc123def456

# Follow-up turn — add --session
python3 scripts/excel_api_client.py "Add a pie chart" \
  --session abc123def456 \
  --language zh-CN --log-path "$EXCEL_LOG" > /dev/null 2>&1 &


When to use --session: User says "continue", "modify", "add a chart", "change colors", "based on the previous...", or references prior output.

⛔ Without --session, the agent starts fresh and loses all previous context.

Error Handling
Error	Solution
Unauthorized (401)	SKYWORK_API_KEY is missing, invalid, or expired — set or rotate the key in OpenClaw skill env
Connection timeout	Use --timeout 1500 for complex tasks (default: 900s)
Agent produces wrong output	Be more specific; use multi-turn to refine iteratively
Insufficient benefit	See below
When benefit is insufficient

Script output may show: Insufficient benefit. Please upgrade your account at {url}

Reply in the user's language:

Convey: "Sorry, Excel/report generation failed. This skill requires upgrading your Skywork membership."
Format: One short sentence + [Upgrade now →](url) (or equivalent in user's language)
URL: Extract from the at https://... part of the log output
Security Notes
Never commit SKYWORK_API_KEY to version control
Set the key in OpenClaw skill env or as an environment variable
Tokens expire — the client will auto-refresh when needed
Weekly Installs
–
Repository
skyworkai/skywork-skills
GitHub Stars
125
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn