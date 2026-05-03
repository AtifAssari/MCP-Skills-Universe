---
rating: ⭐⭐
title: connect-apps
url: https://skills.sh/composiohq/awesome-claude-skills/connect-apps
---

# connect-apps

skills/composiohq/awesome-claude-skills/connect-apps
connect-apps
Installation
$ npx skills add https://github.com/composiohq/awesome-claude-skills --skill connect-apps
Summary

Connect Claude to 1000+ external apps and execute real actions across email, chat, dev tools, and data platforms.

Supports 1000+ integrated apps including Gmail, Slack, GitHub, Notion, Jira, Discord, Airtable, and PostgreSQL
One-time OAuth authorization per app; subsequent commands execute without additional authentication
Composio Tool Router automatically selects the appropriate tool based on your request, then executes the action and returns results
Common workflows include sending emails, creating issues, posting messages, and updating documents across connected services
SKILL.md
Connect Apps

Connect Claude to 1000+ apps. Actually send emails, create issues, post messages - not just generate text about it.

Quick Start
Step 1: Install the Plugin
/plugin install composio-toolrouter

Step 2: Run Setup
/composio-toolrouter:setup


This will:

Ask for your free API key (get one at platform.composio.dev)
Configure Claude's connection to 1000+ apps
Take about 60 seconds
Step 3: Try It!

After setup, restart Claude Code and try:

Send me a test email at YOUR_EMAIL@example.com


If it works, you're connected!

What You Can Do
Ask Claude to...	What happens
"Send email to sarah@acme.com about the launch"	Actually sends the email
"Create GitHub issue: fix login bug"	Creates the issue
"Post to Slack #general: deploy complete"	Posts the message
"Add meeting notes to Notion"	Adds to Notion
Supported Apps

Email: Gmail, Outlook, SendGrid Chat: Slack, Discord, Teams, Telegram Dev: GitHub, GitLab, Jira, Linear Docs: Notion, Google Docs, Confluence Data: Sheets, Airtable, PostgreSQL And 1000+ more...

How It Works
You ask Claude to do something
Composio Tool Router finds the right tool
First time? You'll authorize via OAuth (one-time)
Action executes and returns result
Troubleshooting
"Plugin not found" → Make sure you ran /plugin install composio-toolrouter
"Need to authorize" → Click the OAuth link Claude provides, then say "done"
Action failed → Check you have permissions in the target app
Weekly Installs
1.7K
Repository
composiohq/awes…e-skills
GitHub Stars
57.5K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykWarn