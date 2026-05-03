---
title: google-spaces-updates
url: https://skills.sh/jezweb/claude-skills/google-spaces-updates
---

# google-spaces-updates

skills/jezweb/claude-skills/google-spaces-updates
google-spaces-updates
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill google-spaces-updates
Summary

Post team updates to Google Chat Spaces with git context and deployment notifications.

Reads webhook URL and team config from .claude/settings.json; includes setup command to initialize per project
Supports five message types: deployment, bugfix, feature complete, question, and custom updates with appropriate templates
Automatically gathers git context (recent commits, branch, changed files) to enrich messages
Proactively suggests posting updates after significant work, pushes to main, or when team input is needed
SKILL.md
Google Spaces Updates

Status: Production Ready Last Updated: 2026-01-09

Post updates to a team Google Chat Space via webhook.

Quick Start
1. Setup (first time per project)

Run /google-spaces-updates setup or manually create .claude/settings.json:

{
  "project": {
    "name": "my-project",
    "repo": "github.com/org/my-project"
  },
  "team": {
    "chat_webhook": "https://chat.googleapis.com/v1/spaces/SPACE_ID/messages?key=KEY&token=TOKEN",
    "members": ["Deepinder", "Joshua", "Raquel"]
  }
}

2. Post an update
"Post deployment update to team"
"Tell the team about the new feature"
"Ask the team about the auth approach"

How It Works
Step 1: Check for project settings

Look for .claude/settings.json in the current project directory:

cat .claude/settings.json 2>/dev/null || echo "NOT_FOUND"


If NOT_FOUND, ask the user:

"This project doesn't have Google Spaces configured. Would you like me to set it up? I'll need the webhook URL for your team's Google Space."

Then create the file using the template in templates/settings-template.json.

Step 2: Determine update type

Based on the command or context, determine the update type:

Type	When to use
deployment	After pushing to production/staging, deploying to Vercel/etc
bugfix	After fixing a bug, especially one reported by team
feature	After completing a feature that's ready for review/use
question	When blocked or need team input on a decision
custom	For anything else
Step 3: Gather context

Collect relevant information to include:

# Recent commits (for context)
git log --oneline -3 2>/dev/null

# Current branch
git branch --show-current 2>/dev/null

# Changed files (if recent changes)
git diff --name-only HEAD~1 2>/dev/null | head -10


Also use context from the conversation:

What was just completed
Any preview/production URLs
Relevant file paths
Who might need to know
Step 4: Format the message

Use the appropriate template from templates/ directory.

Key formatting rules for Google Chat:

Use *bold* for emphasis (not markdown bold)
Use _italic_ for secondary text
Newlines work as expected
Keep messages concise but informative
Include actionable links when relevant
Step 5: Post to webhook
curl -X POST "WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"text": "MESSAGE_HERE"}'


Replace:

WEBHOOK_URL with value from .claude/settings.json → team.chat_webhook
MESSAGE_HERE with the formatted message (escape quotes properly)
Step 6: Confirm to user

After posting, tell the user:

"Posted update to team chat: [brief summary of what was posted]"

Message Templates
Deployment
🚀 *Deployed: [PROJECT_NAME]*

[WHAT_CHANGED - 1-2 sentences]

• Branch: `[BRANCH]`
• Commit: `[COMMIT_HASH]`
[• Preview: URL (if applicable)]
[• Production: URL (if applicable)]

_Posted by [USER] via Claude Code_

Bug Fix
🐛 *Bug Fixed: [PROJECT_NAME]*

*Problem:* [What was broken]
*Solution:* [How it was fixed]
*Files:* [Key files changed]

[• Commit: `[COMMIT_HASH]`]

_Please verify if you reported this issue._

Feature Complete
✨ *Feature Complete: [PROJECT_NAME]*

*[FEATURE_NAME]*

[DESCRIPTION - what it does, 1-2 sentences]

[• Demo: URL]
[• Files: key files]

_Ready for review/testing._

Question
❓ *Question: [PROJECT_NAME]*

[QUESTION - clear and specific]

*Context:*
[Relevant background - what you're working on, what you've tried]

*Options considered:*
1. [Option A]
2. [Option B]

_@[PERSON] - would appreciate your input_

Custom
📢 *Update: [PROJECT_NAME]*

[MESSAGE]

_Posted by [USER] via Claude Code_

Setup Command

When user runs /google-spaces-updates setup:

Ask for the Google Spaces webhook URL
Ask for project name (or detect from package.json/repo)
Ask for team members (optional)
Create .claude/settings.json using the template
Add .claude/ to .gitignore if not already there
Confirm setup is complete
Proactive Suggestions

Suggest posting an update when:

User says "done", "finished", "completed" after significant work
After a git push to main/master/production
User mentions team members by name
User seems blocked and might benefit from team input

Ask: "Would you like me to post an update to the team about this?"

When NOT to Use
Minor refactors, typo fixes
WIP commits that aren't ready for review
Internal debugging/testing
Anything that would just be noise
Getting a Webhook URL
Open Google Chat
Navigate to your Space
Click Space name → Apps & integrations → Webhooks
Click Add webhook
Name it (e.g., "Claude Code Updates")
Copy the webhook URL

The URL format: https://chat.googleapis.com/v1/spaces/SPACE_ID/messages?key=KEY&token=TOKEN

Security: Keep webhook URLs private. Add .claude/settings.json to .gitignore.

Weekly Installs
305
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail