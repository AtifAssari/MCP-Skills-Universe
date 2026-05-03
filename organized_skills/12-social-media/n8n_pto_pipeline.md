---
rating: ⭐⭐
title: n8n-pto-pipeline
url: https://skills.sh/datadrivenconstruction/ddc_skills_for_ai_agents_in_construction/n8n-pto-pipeline
---

# n8n-pto-pipeline

skills/datadrivenconstruction/ddc_skills_for_ai_agents_in_construction/n8n-pto-pipeline
n8n-pto-pipeline
Installation
$ npx skills add https://github.com/datadrivenconstruction/ddc_skills_for_ai_agents_in_construction --skill n8n-pto-pipeline
SKILL.md
n8n PTO-Foreman Pipeline
Business Case
Problem Statement

Daily work planning in construction involves:

Manual task distribution from PTO (engineering) to field crews
Paper-based or phone-based task assignment
No systematic tracking of task completion
Delayed reporting and status updates
Solution

Automated n8n pipeline connecting Google Sheets task lists with Telegram bots for real-time task distribution and status collection.

Business Value
Real-time distribution - Tasks delivered automatically at 8:00 AM
Digital tracking - All assignments and statuses in one table
Mobile-first - Foremen use familiar Telegram interface
No app installation - Works with any phone with Telegram
Technical Implementation
Architecture
┌─────────────────┐    ┌─────────────┐    ┌─────────────────┐
│  Google Sheets  │───>│  n8n        │───>│  Telegram Bot   │
│  (Task List)    │    │  Pipeline   │    │  (To Foreman)   │
└─────────────────┘    └─────────────┘    └─────────────────┘
        ▲                     │                    │
        │                     │                    ▼
        │              ┌──────┴──────┐      ┌───────────┐
        └──────────────│   Status    │<─────│  Foreman  │
                       │   Update    │      │  Response │
                       └─────────────┘      └───────────┘

n8n Pipeline Components
1. Morning Trigger (8:00 AM)
{
  "nodes": [
    {
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "parameters": {
        "rule": {
          "interval": [
            {"field": "hours", "hoursInterval": 24}
          ]
        },
        "triggerTimes": {"item": [{"hour": 8, "minute": 0}]}
      }
    }
  ]
}

2. Get Tasks from Google Sheets
{
  "name": "Get Today Tasks",
  "type": "n8n-nodes-base.googleSheets",
  "parameters": {
    "operation": "read",
    "sheetId": "YOUR_SHEET_ID",
    "range": "Tasks!A:F",
    "options": {}
  }
}

3. Filter Tasks by Foreman
// Filter tasks for specific foreman based on chat_id
const chatId = $node["Telegram Trigger"].json["message"]["chat"]["id"];
const tasks = $input.all();

return tasks.filter(task =>
  task.json.foreman_chat_id === chatId.toString()
);

4. Format and Send via Telegram
// Format task message
const tasks = $input.all();
let message = "📋 *Задачи на сегодня:*\n\n";

tasks.forEach((task, index) => {
  message += `*${index + 1}. ${task.json.task_name}*\n`;
  message += `   📍 Участок: ${task.json.location}\n`;
  message += `   ⏰ Срок: ${task.json.deadline}\n`;
  message += `   📝 ${task.json.description}\n\n`;
});

message += "\n_Ответьте на это сообщение статусом:_\n";
message += "✅ выполнил\n❌ не выполнил + причина";

return [{json: {message}}];

5. Status Update Handler
// Parse foreman response and update status
const message = $node["Telegram Trigger"].json["message"]["text"];
const replyTo = $node["Telegram Trigger"].json["message"]["reply_to_message"];

let status = "в работе";
let comment = "";

if (message.toLowerCase().includes("выполнил")) {
  status = "выполнено";
} else if (message.toLowerCase().includes("не выполнил")) {
  status = "не выполнено";
  comment = message.replace(/не выполнил/i, "").trim();
}

return [{
  json: {
    task_id: replyTo.message_id,
    status: status,
    comment: comment,
    updated_at: new Date().toISOString()
  }
}];

Google Sheets Structure

Tasks Sheet:

Column	Description
task_id	Unique task identifier
task_name	Task title
description	Detailed description
location	Work location
deadline	Due date/time
foreman_chat_id	Telegram chat ID of assigned foreman
status	Current status
comment	Foreman comment

Foremen Sheet:

Column	Description
name	Foreman name
chat_id	Telegram chat ID
registered_at	Registration timestamp
Telegram Bot Setup
Create bot via @BotFather
Get bot token
Configure webhook in n8n
For local testing, use n8n tunnel:
npx n8n --tunnel

Usage Flow
For PTO Engineer:
Open Google Sheets task list
Add tasks with foreman assignments
System automatically sends at 8:00 AM
For Foreman:
Receive tasks via Telegram bot
Reply to task message with status
System updates Google Sheets automatically
For Manager:
View real-time status in Google Sheets
Generate reports from historical data
Analyze completion rates by foreman/location
Deployment Options
Local (Testing)
npx n8n --tunnel

Cloud VPS (Production)
Hostinger n8n: ~$5/month
Amvera Cloud: ~170 RUB/month
timeweb: ~590 RUB/month
Extensions
Add photo attachments for completed work
Integrate with PostgreSQL for complex queries
Add reminder notifications
Generate daily/weekly reports
Connect to project management systems
Resources
Source: DDC Telegram Community discussions
Template: Available in DDC GitHub repository
Weekly Installs
17
Repository
datadrivenconst…truction
GitHub Stars
114
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn