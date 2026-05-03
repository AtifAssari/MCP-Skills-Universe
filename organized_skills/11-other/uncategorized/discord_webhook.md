---
rating: ⭐⭐
title: discord-webhook
url: https://skills.sh/vm0-ai/vm0-skills/discord-webhook
---

# discord-webhook

skills/vm0-ai/vm0-skills/discord-webhook
discord-webhook
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill discord-webhook
SKILL.md
How to Use

All examples below assume you have DISCORD_WEBHOOK_URL set.

1. Send Simple Message

Write to /tmp/discord_webhook_request.json:

{
  "content": "Hello from webhook!"
}


Then run:

curl -s -X POST "$DISCORD_WEBHOOK_URL" -H "Content-Type: application/json" -d @/tmp/discord_webhook_request.json

2. Send with Custom Username and Avatar

Write to /tmp/discord_webhook_request.json:

{
  "content": "Alert!",
  "username": "Alert Bot",
  "avatar_url": "https://i.imgur.com/4M34hi2.png"
}


Then run:

curl -s -X POST "$DISCORD_WEBHOOK_URL" -H "Content-Type: application/json" -d @/tmp/discord_webhook_request.json

3. Send Rich Embed

Write to /tmp/discord_webhook_request.json:

{
  "embeds": [
    {
      "title": "Deployment Complete",
      "description": "Version 1.2.3 deployed to production",
      "color": 5763719,
      "fields": [
        {
          "name": "Environment",
          "value": "Production",
          "inline": true
        },
        {
          "name": "Status",
          "value": "Success",
          "inline": true
        }
      ],
      "timestamp": "2025-01-01T12:00:00.000Z"
    }
  ]
}


Then run:

curl -s -X POST "$DISCORD_WEBHOOK_URL" -H "Content-Type: application/json" -d @/tmp/discord_webhook_request.json


Common colors (decimal):

Green: 5763719
Red: 15548997
Blue: 5793266
Yellow: 16776960
Orange: 16744192
4. Send Error Alert

Write to /tmp/discord_webhook_request.json:

{
  "embeds": [
    {
      "title": "Error Alert",
      "description": "Database connection failed",
      "color": 15548997,
      "fields": [
        {
          "name": "Service",
          "value": "api-server"
        },
        {
          "name": "Error",
          "value": "Connection timeout"
        }
      ],
      "footer": {
        "text": "Monitor"
      }
    }
  ]
}


Then run:

curl -s -X POST "$DISCORD_WEBHOOK_URL" -H "Content-Type: application/json" -d @/tmp/discord_webhook_request.json

5. Send File Attachment

Write to /tmp/discord_webhook_payload.json:

{
  "content": "Screenshot attached"
}


Then run:

curl -s -X POST "$DISCORD_WEBHOOK_URL" -F "file1=@screenshot.png" -F 'payload_json=@/tmp/discord_webhook_payload.json'

6. Send Multiple Files

Write to /tmp/discord_webhook_payload.json:

{
  "content": "Log files attached"
}


Then run:

curl -s -X POST "$DISCORD_WEBHOOK_URL" -F "file1=@error.log" -F "file2=@debug.log" -F 'payload_json=@/tmp/discord_webhook_payload.json'

7. Send Multiple Embeds

Write to /tmp/discord_webhook_request.json:

{
  "embeds": [
    {
      "title": "Build Started",
      "color": 16776960
    },
    {
      "title": "Tests Passed",
      "color": 5763719
    },
    {
      "title": "Deployed",
      "color": 5793266
    }
  ]
}


Then run:

curl -s -X POST "$DISCORD_WEBHOOK_URL" -H "Content-Type: application/json" -d @/tmp/discord_webhook_request.json

8. Send with Mention

Write to /tmp/discord_webhook_request.json:

{
  "content": "<@<your-user-id>> Check this out!",
  "allowed_mentions": {
    "users": ["<your-user-id>"]
  }
}


Then run:

curl -s -X POST "$DISCORD_WEBHOOK_URL" -H "Content-Type: application/json" -d @/tmp/discord_webhook_request.json


Replace <your-user-id> with the actual Discord user ID.

9. Send Silent Message (No Notification)

Write to /tmp/discord_webhook_request.json:

{
  "content": "Silent update",
  "flags": 4096
}


Then run:

curl -s -X POST "$DISCORD_WEBHOOK_URL" -H "Content-Type: application/json" -d @/tmp/discord_webhook_request.json

10. CI/CD Pipeline Notification

Write to /tmp/discord_webhook_request.json:

{
  "username": "GitHub Actions",
  "embeds": [
    {
      "title": "Pipeline Status",
      "color": 5763719,
      "fields": [
        {
          "name": "Repository",
          "value": "myorg/myrepo",
          "inline": true
        },
        {
          "name": "Branch",
          "value": "main",
          "inline": true
        },
        {
          "name": "Commit",
          "value": "abc1234",
          "inline": true
        },
        {
          "name": "Status",
          "value": "Success"
        }
      ],
      "timestamp": "2025-01-01T12:00:00.000Z"
    }
  ]
}


Then run:

curl -s -X POST "$DISCORD_WEBHOOK_URL" -H "Content-Type: application/json" -d @/tmp/discord_webhook_request.json

Embed Structure
{
  "title": "Title text",
  "description": "Description text",
  "url": "https://example.com",
  "color": 5763719,
  "fields": [
  {"name": "Field 1", "value": "Value 1", "inline": true}
  ],
  "author": {"name": "Author", "icon_url": "https://..."},
  "footer": {"text": "Footer text"},
  "thumbnail": {"url": "https://..."},
  "image": {"url": "https://..."},
  "timestamp": "2025-01-01T12:00:00.000Z"
}

Guidelines
Rate limits: 30 requests per 60 seconds per webhook
Message limit: 2000 characters for content
Embed limits: Max 10 embeds, 6000 total characters
File limits: Max 8MB per file (50MB with Nitro boost)
Security: Treat webhook URLs like passwords
Weekly Installs
205
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass