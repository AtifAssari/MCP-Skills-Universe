---
title: instagram
url: https://skills.sh/vm0-ai/vm0-skills/instagram
---

# instagram

skills/vm0-ai/vm0-skills/instagram
instagram
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill instagram
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name INSTAGRAM_TOKEN or zero doctor check-connector --url https://graph.facebook.com/v21.0/me --method GET

How to Use

All examples below assume you have already set:

INSTAGRAM_TOKEN
INSTAGRAM_BUSINESS_ACCOUNT_ID

1. Fetch recent media for the account

Fetch the most recent media (photos / videos / Reels) for the account:

curl -s -X GET "https://graph.facebook.com/v21.0/$INSTAGRAM_BUSINESS_ACCOUNT_ID/media?fields=id,caption,media_type,media_url,permalink,timestamp" --header "Authorization: Bearer $INSTAGRAM_TOKEN"


Notes:

Each item in the returned JSON represents a media object
Common fields:
id: media ID (used for details / insights later)
caption: caption text
media_type: IMAGE / VIDEO / CAROUSEL_ALBUM
media_url: direct URL to the media
permalink: Instagram permalink
timestamp: creation time
2. Get details for a single media

If you already have a media id, you can fetch more complete information. Replace <your-media-id> with the id field from the "Get User Media" response (section 1 above):

curl -s -X GET "https://graph.facebook.com/v21.0/<your-media-id>?fields=id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username" --header "Authorization: Bearer $INSTAGRAM_TOKEN"

3. Search media by hashtag

Note: hashtag search requires proper business use cases and permissions as defined by Facebook/Instagram. Refer to the official docs.

This usually involves two steps:

3.1 Get the hashtag ID

Replace <hashtag-name> with any hashtag name you want to search for (without the # symbol), e.g., "travel", "food", "photography":

curl -s -X GET "https://graph.facebook.com/v21.0/ig_hashtag_search?user_id=$INSTAGRAM_BUSINESS_ACCOUNT_ID&q=<hashtag-name>" --header "Authorization: Bearer $INSTAGRAM_TOKEN"


Note the id field in the returned JSON for use in the next step.

3.2 Fetch recent media for the hashtag

Replace <hashtag-id> with the id field from the "Search Hashtag" response (section 3.1 above):

curl -s -X GET "https://graph.facebook.com/v21.0/<hashtag-id>/recent_media?user_id=$INSTAGRAM_BUSINESS_ACCOUNT_ID&fields=id,caption,media_type,media_url,permalink,timestamp" --header "Authorization: Bearer $INSTAGRAM_TOKEN"

4. Publish an image post

Publishing an image post via the Graph API usually requires two steps:

Create a media container
Publish the container to the feed
4.1 Create a media container

Write the request data to /tmp/request.json:

{
  "image_url": "https://example.com/image.jpg",
  "caption": "Hello from Instagram API 👋"
}


Replace https://example.com/image.jpg with any publicly accessible image URL and update the caption text as needed.

curl -s -X POST "https://graph.facebook.com/v21.0/$INSTAGRAM_BUSINESS_ACCOUNT_ID/media" -H "Content-Type: application/json" -d @/tmp/request.json --header "Authorization: Bearer $INSTAGRAM_TOKEN"


The response will contain an id (media container ID), for example:

{
  "id": "1790xxxxxxxxxxxx"
}


Note this ID for use in the next step.

4.2 Publish the media container to the feed

Write the request data to /tmp/request.json:

{
  "creation_id": "<your-creation-id>"
}


Replace <your-creation-id> with the id field from the "Create Media Container" response (section 4.1 above):

curl -s -X POST "https://graph.facebook.com/v21.0/$INSTAGRAM_BUSINESS_ACCOUNT_ID/media_publish" -H "Content-Type: application/json" -d @/tmp/request.json --header "Authorization: Bearer $INSTAGRAM_TOKEN"


If successful, the response will contain the final media id:

{
  "id": "1791yyyyyyyyyyyy"
}


You can then use the "Get details for a single media" command to fetch its permalink.

5. Common errors and troubleshooting
Permissions / OAuth errors
Typical error message: (#10) Application does not have permission for this action
Check:
Whether the app has been reviewed / approved
Whether the required Instagram permissions are enabled
Whether INSTAGRAM_TOKEN is a valid long-lived token
Unsupported account type
Most Graph API features require Business / Creator accounts
Make sure the Instagram account type is correct and linked to a Facebook Page
Rate limits
Too many requests in a short period may hit rate limits; add delays for bulk operations
Guidelines
Do not log tokens: INSTAGRAM_TOKEN is sensitive; avoid printing it in logs or chat transcripts
Validate curl commands in a test environment first: confirm flows before wiring them into automation / agents
Keep API version up to date: periodically check Facebook docs and update the v21.0 version in URLs to the latest
Use placeholder text for IDs: all examples use placeholder text like <your-media-id> instead of shell variables in URLs to avoid dependencies and make examples self-contained
Weekly Installs
272
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn