---
title: bright-data
url: https://skills.sh/vm0-ai/vm0-skills/bright-data
---

# bright-data

skills/vm0-ai/vm0-skills/bright-data
bright-data
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill bright-data
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name BRIGHTDATA_TOKEN or zero doctor check-connector --url https://api.brightdata.com/datasets/v3/trigger --method POST

Social Media Scraping

Bright Data supports scraping these social media platforms:

Platform	Profiles	Posts	Comments	Reels/Videos
Twitter/X	✅	✅	-	-
Reddit	-	✅	✅	-
YouTube	✅	✅	✅	-
Instagram	✅	✅	✅	✅
TikTok	✅	✅	✅	-
LinkedIn	✅	✅	-	-
How to Use
1. Trigger Scraping (Asynchronous)

Trigger a data collection job and get a snapshot_id for later retrieval.

Write to /tmp/brightdata_request.json:

[
  {"url": "https://twitter.com/username"},
  {"url": "https://twitter.com/username2"}
]


Then run (replace <dataset-id> with your actual dataset ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json


Response:

{
  "snapshot_id": "s_m4x7enmven8djfqak"
}

2. Trigger Scraping (Synchronous)

Get results immediately in the response (for small requests).

Write to /tmp/brightdata_request.json:

[
  {"url": "https://www.reddit.com/r/technology/comments/xxxxx"}
]


Then run (replace <dataset-id> with your actual dataset ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json

3. Monitor Progress

Check the status of a scraping job (replace <snapshot-id> with your actual snapshot ID):

curl -s "https://api.brightdata.com/datasets/v3/progress/<snapshot-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN"


Response:

{
  "snapshot_id": "s_m4x7enmven8djfqak",
  "dataset_id": "gd_xxxxx",
  "status": "running"
}


Status values: running, ready, failed

4. Download Results

Once status is ready, download the collected data (replace <snapshot-id> with your actual snapshot ID):

curl -s "https://api.brightdata.com/datasets/v3/snapshot/<snapshot-id>?format=json" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN"

5. List Snapshots

Get all your snapshots:

curl -s "https://api.brightdata.com/datasets/v3/snapshots" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" | jq '.[] | {snapshot_id, dataset_id, status}'

6. Cancel Snapshot

Cancel a running job (replace <snapshot-id> with your actual snapshot ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/cancel?snapshot_id=<snapshot-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN"

Platform-Specific Examples
Twitter/X - Scrape Profile

Write to /tmp/brightdata_request.json:

[
  {"url": "https://twitter.com/elonmusk"}
]


Then run (replace <dataset-id> with your actual dataset ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json


Returns: x_id, profile_name, biography, is_verified, followers, following, profile_image_link

Twitter/X - Scrape Posts

Write to /tmp/brightdata_request.json:

[
  {"url": "https://twitter.com/username/status/123456789"}
]


Then run (replace <dataset-id> with your actual dataset ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json


Returns: post_id, text, replies, likes, retweets, views, hashtags, media

Reddit - Scrape Subreddit Posts

Write to /tmp/brightdata_request.json:

[
  {"url": "https://www.reddit.com/r/technology", "sort_by": "hot"}
]


Then run (replace <dataset-id> with your actual dataset ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json


Parameters: url, sort_by (new/top/hot)

Returns: post_id, title, description, num_comments, upvotes, date_posted, community

Reddit - Scrape Comments

Write to /tmp/brightdata_request.json:

[
  {"url": "https://www.reddit.com/r/technology/comments/xxxxx/post_title"}
]


Then run (replace <dataset-id> with your actual dataset ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json


Returns: comment_id, user_posted, comment_text, upvotes, replies

YouTube - Scrape Video Info

Write to /tmp/brightdata_request.json:

[
  {"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
]


Then run (replace <dataset-id> with your actual dataset ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json


Returns: title, views, likes, num_comments, video_length, transcript, channel_name

YouTube - Search by Keyword

Write to /tmp/brightdata_request.json:

[
  {"keyword": "artificial intelligence", "num_of_posts": 50}
]


Then run (replace <dataset-id> with your actual dataset ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json

YouTube - Scrape Comments

Write to /tmp/brightdata_request.json:

[
  {"url": "https://www.youtube.com/watch?v=xxxxx", "load_replies": 3}
]


Then run (replace <dataset-id> with your actual dataset ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json


Returns: comment_text, likes, replies, username, date

Instagram - Scrape Profile

Write to /tmp/brightdata_request.json:

[
  {"url": "https://www.instagram.com/username"}
]


Then run (replace <dataset-id> with your actual dataset ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json


Returns: followers, post_count, profile_name, is_verified, biography

Instagram - Scrape Posts

Write to /tmp/brightdata_request.json:

[
  {
    "url": "https://www.instagram.com/username",
    "num_of_posts": 20,
    "start_date": "01-01-2024",
    "end_date": "12-31-2024"
  }
]


Then run (replace <dataset-id> with your actual dataset ID):

curl -s -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json

Account Management
Check Account Status
curl -s "https://api.brightdata.com/status" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN"


Response:

{
  "status": "active",
  "customer": "hl_xxxxxxxx",
  "can_make_requests": true,
  "ip": "x.x.x.x"
}

Get Active Zones
curl -s "https://api.brightdata.com/zone/get_active_zones" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN" | jq '.[] | {name, type}'

Get Bandwidth Usage
curl -s "https://api.brightdata.com/customer/bw" \
  -H "Authorization: Bearer $BRIGHTDATA_TOKEN"

Getting Dataset IDs

To use the scraping features, you need a dataset_id:

Go to Bright Data Control Panel
Create a new Web Scraper dataset or select an existing one
Choose the platform (Twitter, Reddit, YouTube, etc.)
Copy the dataset_id from the dataset settings

Dataset IDs can also be found in the bandwidth usage API response under the data field keys (e.g., v__ds_api_gd_xxxxx where gd_xxxxx is your dataset ID).

Common Parameters
Parameter	Description	Example
url	Target URL to scrape	https://twitter.com/user
keyword	Search keyword	"artificial intelligence"
num_of_posts	Limit number of results	50
start_date	Filter by date (MM-DD-YYYY)	"01-01-2024"
end_date	Filter by date (MM-DD-YYYY)	"12-31-2024"
sort_by	Sort order (Reddit)	new, top, hot
format	Response format	json, csv
Rate Limits
Batch mode: up to 100 concurrent requests
Maximum input size: 1GB per batch
Exceeding limits returns 429 error
Guidelines
Create datasets first: Use the Control Panel to create scraper datasets
Use async for large jobs: Use /trigger for discovery and batch operations
Use sync for small jobs: Use /scrape for single URL quick lookups
Check status before download: Poll /progress until status is ready
Respect rate limits: Don't exceed 100 concurrent requests
Date format: Use MM-DD-YYYY for date parameters
Weekly Installs
86
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn