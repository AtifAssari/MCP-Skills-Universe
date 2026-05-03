---
title: slack-webhook
url: https://skills.sh/vm0-ai/vm0-skills/slack-webhook
---

# slack-webhook

skills/vm0-ai/vm0-skills/slack-webhook
slack-webhook
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill slack-webhook
SKILL.md
Usage
Simple Message

Write to /tmp/slack_request.json:

{
  "text": "Hello, world."
}


Then run:

curl -X POST $SLACK_WEBHOOK_URL -H "Content-type: application/json" -d @/tmp/slack_request.json

With Formatting

Write to /tmp/slack_request.json:

{
  "text": "*Bold* and _italic_ text"
}


Then run:

curl -X POST $SLACK_WEBHOOK_URL -H "Content-type: application/json" -d @/tmp/slack_request.json

With Link

Write to /tmp/slack_request.json:

{
  "text": "Check <https://example.com|this link>"
}


Then run:

curl -X POST $SLACK_WEBHOOK_URL -H "Content-type: application/json" -d @/tmp/slack_request.json

With Blocks (Rich Layout)

Write to /tmp/slack_request.json:

{
  "text": "New review submitted",
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Danny left the following review:"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "<https://example.com|Overlook Hotel>\n:star:\nDoors had too many axe holes."
      }
    }
  ]
}


Then run:

curl -X POST $SLACK_WEBHOOK_URL -H "Content-type: application/json" -d @/tmp/slack_request.json

With Fields

Write to /tmp/slack_request.json:

{
  "text": "Deployment status",
  "blocks": [
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*Environment:*\nProduction"
        },
        {
          "type": "mrkdwn",
          "text": "*Status:*\nSuccess"
        }
      ]
    }
  ]
}


Then run:

curl -X POST $SLACK_WEBHOOK_URL -H "Content-type: application/json" -d @/tmp/slack_request.json

Message Formatting
Syntax	Result
*bold*	bold
_italic_	italic
~strike~	strike
`code`	code
\n	newline
<URL|text>	hyperlink
:emoji:	emoji
Shell Escaping

Messages with ! may fail due to shell history expansion. Use heredoc:

curl -s -X POST $SLACK_WEBHOOK_URL -H "Content-type: application/json" -d @- << 'EOF'
{"text":"Deploy completed! :rocket:"}
EOF

Response

Success: ok (HTTP 200)

Errors:

invalid_payload - Malformed JSON
no_text - Missing text field
no_service - Webhook disabled or invalid
channel_not_found - Channel deleted
channel_is_archived - Channel archived
action_prohibited - Admin restriction
Limitations
One webhook = one channel only
Cannot override username or icon (set in app config)
Send only (no reading messages)
Cannot delete messages after posting
Rate limit: 1 message/second

For full API access, use the slack skill with Bot Token.

API Reference
Webhooks Guide: https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks
Block Kit Builder: https://app.slack.com/block-kit-builder
Message Formatting: https://docs.slack.dev/messaging/formatting-message-text
Weekly Installs
91
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass