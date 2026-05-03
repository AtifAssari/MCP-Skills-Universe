---
rating: ⭐⭐⭐
title: using-cron
url: https://skills.sh/dtyq/magic/using-cron
---

# using-cron

skills/dtyq/magic/using-cron
using-cron
Installation
$ npx skills add https://github.com/dtyq/magic --skill using-cron
SKILL.md
Scheduled Message Task Management

Manage scheduled message tasks through scripts, supporting create, list, get, update, and delete operations.

Core Capabilities
Create one-time or recurring scheduled message tasks
Query and filter existing scheduled task lists
Get task details
Update task configuration (name, time, enabled status, etc.)
Delete tasks
Quick Start
Typical Workflow
1. Create task (create.py)
   ↓ Get returned schedule_id
2. Query list (list.py) - Optional
   ↓ Confirm task was created
3. Get details (get.py) - Optional
   ↓ View complete task info
4. Update task (update.py) - As needed
5. Delete task (delete.py) - As needed

Available Scripts
create.py - Create Scheduled Task

Create a new scheduled message task.

SYNOPSIS

python scripts/create.py --task-name <name> --message-content <content> --type <type> --time <HH:MM> [OPTIONS]


DESCRIPTION

Create a scheduled message task, supporting one-time execution and daily/weekly/monthly repeat modes.

When to pass --specify-topic 1: Pass 1 only when both hold: (1) the task is recurring (daily_repeat / weekly_repeat / monthly_repeat), and (2) the user intent implies that the next run time or trigger depends on the current or previous run's result (e.g. "run again 3 days after each completion", "next time based on last result"). For one-time tasks or fixed-schedule tasks that do not depend on previous results, omit this option or pass 0.

OPTIONS

Option	Type	Required	Description
--task-name <name>	string	Yes	Task name
--message-content <content>	string	Yes	Message content (same as detail message_content/task_describe)
--type <type>	string	Yes	Schedule type, see table below
--time <HH:MM>	string	Yes	Execution time
--day <value>	string	Conditional	Depends on schedule type, see table below
--deadline <YYYY-MM-DD HH:MM:SS>	string	No	Expiry datetime; format YYYY-MM-DD HH:MM:SS. If only date or unclear format is given, the system will interpret and complete (e.g. to 00:00:00 that day)
--specify-topic <0|1>	integer	No	Whether to specify topic; 0=no, 1=yes; default 0. Pass 1 only when the user intent is a recurring task whose next run depends on the previous run's result; otherwise use default 0

Schedule type --type and --day mapping:

--type	Description	--day
no_repeat	No repeat, one-time execution	Execution date YYYY-MM-DD (required)
daily_repeat	Repeat daily	Not needed
weekly_repeat	Repeat weekly	Day of week 0-6, 0=Sunday (required)
monthly_repeat	Repeat monthly	Day of month 1-31 (required)

OUTPUT

On success: {"id": "<schedule_id>"}

EXAMPLES

python scripts/create.py \
  --task-name "每日早报" \
  --message-content "请生成今日早报" \
  --type daily_repeat \
  --time "9:00"

list.py - Query Task List

Query the scheduled task list with optional filtering.

SYNOPSIS

python scripts/list.py [OPTIONS]


DESCRIPTION

Query all scheduled tasks or filter by conditions, with pagination support. Results are scoped to the current project; project_id is taken from the current session and must not be passed.

OPTIONS

Option	Type	Required	Description
--task-name <name>	string	No	Fuzzy search by task name
--enabled <0|1>	integer	No	1=enabled 0=disabled
--completed <0|1>	integer	No	1=completed 0=not completed
--page <n>	integer	No	Page number, default 1
--page-size <n>	integer	No	Items per page, default 50

OUTPUT

On success: {"total": N, "schedules": [{"id": "...", "task_name": "...", "task_describe": "...", "status": "...", "enabled": 0|1, "time_config": {...}, "deadline": ...}]}. Each item includes: id, task_name, task_describe, status, enabled, time_config, deadline.

EXAMPLES

# 查询全部
python scripts/list.py

# 按条件过滤
python scripts/list.py --task-name "早报" --enabled 1 --completed 0

get.py - Get Task Details

Get the complete details of a specific scheduled task.

SYNOPSIS

python scripts/get.py --id <schedule_id>


DESCRIPTION

Query complete task information by task ID.

OPTIONS

Option	Type	Required	Description
--id <schedule_id>	string	Yes	Task ID

OUTPUT

On success: Returns complete task info including id, task_name, task_describe, message_content, time_config, status, enabled, deadline.

EXAMPLES

python scripts/get.py --id "<schedule_id>"

update.py - Update Task

Update the configuration of a specific scheduled task; only pass fields to be modified.

SYNOPSIS

python scripts/update.py --id <schedule_id> [OPTIONS]


DESCRIPTION

Update scheduled task configuration. Only pass fields to be modified; unspecified fields remain unchanged. --type and --time must be provided together.

OPTIONS

Option	Type	Required	Description
--id <schedule_id>	string	Yes	Task ID
--task-name <name>	string	No	New task name
--message-content <content>	string	No	Message content (same as detail message_content/task_describe)
--type <type>	string	No	Schedule type (must be provided with --time)
--time <HH:MM>	string	No	Execution time (must be provided with --type)
--day <value>	string	No	Date/weekday/day-of-month, depends on --type
--deadline <YYYY-MM-DD HH:MM:SS>	string	No	Expiry datetime; format YYYY-MM-DD HH:MM:SS, auto-completed if only date or unclear
--enabled <0|1>	integer	No	1=enable 0=disable

OUTPUT

On success: {"id": "<schedule_id>"}

EXAMPLES

# 修改任务名称
python scripts/update.py --id "<schedule_id>" --task-name "新名称"

# 修改任务详情
python scripts/update.py --id "<schedule_id>" --message-content "新的任务详情内容"

# 修改调度时间
python scripts/update.py --id "<schedule_id>" --type daily_repeat --time "10:00"

# 修改截止日期
python scripts/update.py --id "<schedule_id>" --deadline "2026-12-31 23:59:59"

# 禁用任务
python scripts/update.py --id "<schedule_id>" --enabled 0

# 重新启用任务
python scripts/update.py --id "<schedule_id>" --enabled 1

delete.py - Delete Task

Delete a specific scheduled task.

SYNOPSIS

python scripts/delete.py --id <schedule_id>


DESCRIPTION

Permanently delete a scheduled task by task ID.

OPTIONS

Option	Type	Required	Description
--id <schedule_id>	string	Yes	Task ID

OUTPUT

On success: {"id": "<schedule_id>"}

EXAMPLES

python scripts/delete.py --id "<schedule_id>"

Usage Examples

In Agent environment, use shell_exec tool to execute scripts:

# 创建任务
shell_exec(
    command='python scripts/create.py --task-name "每日早报" --message-content "请生成今日早报" --type daily_repeat --time "9:00"'
)

# 查询任务列表
shell_exec(
    command="python scripts/list.py"
)

# 获取任务详情
shell_exec(
    command='python scripts/get.py --id "<schedule_id>"'
)

# 更新任务
shell_exec(
    command='python scripts/update.py --id "<schedule_id>" --enabled 0'
)

# 删除任务
shell_exec(
    command='python scripts/delete.py --id "<schedule_id>"'
)

Weekly Installs
13
Repository
dtyq/magic
GitHub Stars
4.8K
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass