---
rating: ⭐⭐
title: pushinator
url: https://skills.sh/vm0-ai/vm0-skills/pushinator
---

# pushinator

skills/vm0-ai/vm0-skills/pushinator
pushinator
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill pushinator
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name PUSHINATOR_TOKEN or zero doctor check-connector --url https://api.pushinator.com/api/v2/notifications/send --method POST

How to Use

Base URL: https://api.pushinator.com

Required headers:

Authorization: Bearer $PUSHINATOR_TOKEN
Content-Type: application/json
1. Send a Push Notification

Send a notification to all subscribers of a channel.

Write to /tmp/pushinator_request.json:

{
  "channel_id": "<your-channel-uuid>",
  "content": "Hello from Pushinator!"
}


Replace <your-channel-uuid> with your actual channel UUID, then run:

curl -s -X POST "https://api.pushinator.com/api/v2/notifications/send" \
  --header "Authorization: Bearer $PUSHINATOR_TOKEN" \
  --header "Content-Type: application/json" \
  -d @/tmp/pushinator_request.json


Response:

{
  "success": true,
  "message": "Notification created and being sent to subscribers"
}

2. Send Deployment Notification

Notify when a deployment completes.

Write to /tmp/pushinator_request.json:

{
  "channel_id": "<your-channel-uuid>",
  "content": "Deployment complete! Project deployed to production."
}


Replace <your-channel-uuid> with your actual channel UUID, then run:

curl -s -X POST "https://api.pushinator.com/api/v2/notifications/send" \
  --header "Authorization: Bearer $PUSHINATOR_TOKEN" \
  --header "Content-Type: application/json" \
  -d @/tmp/pushinator_request.json

3. Send Alert with Emoji

Include emojis for visual distinction.

Write to /tmp/pushinator_request.json:

{
  "channel_id": "<your-channel-uuid>",
  "content": "Build failed! Check the CI logs."
}


Replace <your-channel-uuid> with your actual channel UUID, then run:

curl -s -X POST "https://api.pushinator.com/api/v2/notifications/send" \
  --header "Authorization: Bearer $PUSHINATOR_TOKEN" \
  --header "Content-Type: application/json" \
  -d @/tmp/pushinator_request.json

Request Parameters
Parameter	Type	Required	Description
channel_id	string	Yes	UUID of the notification channel
content	string	Yes	Notification message text
HTTP Status Codes
Code	Description
2xx	Success - notification sent
4xx	Invalid request or missing parameters
5xx	Server error - retry recommended
Guidelines
Keep messages concise: Push notifications have limited display space
Use channels for topics: Create separate channels for different notification types
Rate limiting: Stay within your plan's monthly notification limit
Include context: Make notifications actionable with relevant details
Weekly Installs
73
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass