---
title: goodqunbot
url: https://skills.sh/imgoodbai/goodable/goodqunbot
---

# goodqunbot

skills/imgoodbai/goodable/goodqunbot
goodqunbot
Installation
$ npx skills add https://github.com/imgoodbai/goodable --skill goodqunbot
SKILL.md
微信消息助手 (WeChat Message Assistant)

This skill enables AI to interact with WeChat directly through AI chat, providing two core capabilities: retrieving recent messages and sending messages to contacts or groups.

Platform Requirements
OS: Windows 10/11 only
WeChat: WeChat PC client must be installed, running, and logged in
Python: Python 3.11+ (automatically handled by Goodable)
Core Capabilities
1. Retrieve Recent Messages

Fetch the last 10-15 messages from any WeChat contact or group chat.

What you can ask:

Get the last 15 messages from "张三"
Show me recent messages from "Product Team" group
Retrieve messages from "李四", last 10 only


What AI will do:

Opens the specified chat in WeChat
Retrieves the requested number of messages (default: 15, max: 100)
Returns messages with timestamp, sender, and content
Formats as structured JSON for easy parsing
2. Send Messages

Send a text message to any WeChat contact or group chat.

What you can ask:

Send "Meeting at 3pm" to "张三"
Message "Product Team" group: "Release notes updated"
Tell "李四": "Please review the document"


What AI will do:

Opens the specified chat in WeChat
Sends the message content
Confirms successful delivery
How to Use
Prerequisites

Before using this skill, ensure:

WeChat PC client is running
You are logged into your WeChat account
The contact/group name you specify exists in your WeChat
Example Usage

Scenario 1: Check messages from a colleague

User: "帮我看一下张三最近给我发了什么消息"
AI: [Runs get_messages.py script]
AI: "张三最近的5条消息：
1. [2024-01-28 10:30] 张三: 会议资料已发送
2. [2024-01-28 11:00] 张三: 请查收
..."


Scenario 2: Send a message

User: "给产品群发个消息：今天下午3点开会"
AI: [Runs send_message.py script]
AI: "消息已成功发送到产品群"

Instructions for AI

When the user requests WeChat message operations:

1. Retrieve Messages

Run the get_messages.py script:

python scripts/get_messages.py "<Contact/Group Name>" [count]


Parameters:

Contact/Group Name: Exact name as shown in WeChat (required)
count: Number of recent messages to retrieve (optional, default: 15, max: 100)

Output Format: The script returns JSON with message details:

[
  {
    "time": "2024-01-28 10:30:45",
    "sender": "张三",
    "content": "会议资料已发送",
    "type": "text"
  }
]


IMPORTANT - Output Formatting for User: After successfully retrieving messages, you MUST format them in a clean, readable way. DO NOT show raw JSON to the user.

For 5 or fewer messages - Use a numbered list:

📨 **张三** 的最近消息：

1. [2024-01-28 10:30] 张三: 会议资料已发送
2. [2024-01-28 11:00] 张三: 请查收
3. [2024-01-28 14:30] 你: 好的，已收到


Tips:

Always include contact/group name in the header
Keep timestamps concise (remove date if same day)
Group consecutive messages from same sender when appropriate
Highlight important information if user asks for summary

Error Handling:

If WeChat is not running: "WeChat PC client is not running or not logged in"
If contact not found: "Contact or group 'xxx' not found"
Parse the error and provide user-friendly explanation in Chinese
2. Send Messages

Run the send_message.py script:

python scripts/send_message.py "<Contact/Group Name>" "<Message Content>"


Parameters:

Contact/Group Name: Exact name as shown in WeChat (required)
Message Content: Text message to send (required, cannot be empty)

Output:

Success: "Message sent successfully to 'xxx'"
Failure: Error message with details

Important Notes:

Always enclose contact names and message content in quotes
Contact names must match exactly as shown in WeChat
For group chats, use the full group name
Only text messages are supported (no images/files/emojis)
3. Best Practices

Name Matching:

Ask user to confirm the exact contact/group name if unsure
Suggest checking WeChat contact list for correct spelling
Chinese names are case-sensitive and must match exactly

Error Recovery:

If "WeChat not found" error: Ask user to start WeChat and log in
If "Contact not found" error: Ask user to verify the name
If script fails: Check if Python environment is properly set up

User Experience:

Summarize retrieved messages in a readable format
Confirm before sending messages if content seems important
Provide context about what happened after each operation
Technical Details
Script Locations
skills/goodqunbot/
├── SKILL.md                    # This file
├── scripts/
│   ├── get_messages.py         # Retrieve messages
│   └── send_message.py         # Send messages
└── wxauto_lib/                 # WeChat automation library (pyc bytecode)

Implementation

Both scripts use the wxauto library (RPA-based WeChat automation):

get_messages.py:

Initializes WeChat instance
Opens specified chat with wx.ChatWith(who)
Retrieves all messages with wx.GetAllMessage(savepic=False, savefile=False)
Returns recent N messages as JSON

send_message.py:

Initializes WeChat instance
Sends message with wx.SendMsg(msg=message, who=who, clear=True)
Returns success/failure status
Limitations
Platform: Windows only (wxauto uses Windows API)
Message Types: Text only (no images, files, or rich media)
Rate Limits: May be subject to WeChat's anti-spam mechanisms
Accuracy: Contact name must match exactly (case-sensitive)
State Dependency: Requires WeChat PC client to be running and logged in
Troubleshooting
Issue	Solution
"WeChat window not found"	Start WeChat PC client and log in
"Contact not found"	Verify exact contact/group name in WeChat
Script timeout	Check if WeChat is responding, restart if frozen
Import error	Ensure wxauto_lib directory exists in goodqunbot
Permission error	Run with appropriate user permissions on Windows
Privacy & Security
Local Only: All operations are local, no data sent to external servers
Read-Only Access: get_messages.py only reads, doesn't modify chat history
User Control: send_message.py only sends when explicitly requested
No Logging: Messages are not stored or logged by the scripts
Compliance: Use responsibly and comply with WeChat Terms of Service
Related Features

This skill complements the GoodQunBot App (template.json), which provides:

Web UI for browsing all groups
AI-powered chat summaries
Data visualization (activity charts, word clouds)
Member management and business opportunity discovery

Skill vs App:

Skill Mode: Quick AI-driven message operations in chat
App Mode: Full-featured web interface for comprehensive chat management
Both modes share the same wxauto library and work independently
Weekly Installs
13
Repository
imgoodbai/goodable
GitHub Stars
173
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn