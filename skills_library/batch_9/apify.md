---
title: apify
url: https://skills.sh/vm0-ai/vm0-skills/apify
---

# apify

skills/vm0-ai/vm0-skills/apify
apify
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill apify
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name APIFY_TOKEN or zero doctor check-connector --url https://api.apify.com/v2/acts/apify~web-scraper/runs --method POST

How to Use
1. Run an Actor (Async)

Start an Actor run asynchronously:

Write to /tmp/apify_request.json:

{
  "startUrls": [{"url": "https://example.com"}],
  "maxPagesPerCrawl": 10,
  "pageFunction": "async function pageFunction(context) { const { request, log, jQuery } = context; const $ = jQuery; const title = $(\"title\").text(); return { url: request.url, title }; }"
}


Then run:

curl -s -X POST "https://api.apify.com/v2/acts/apify~web-scraper/runs" --header "Authorization: Bearer $APIFY_TOKEN" --header "Content-Type: application/json" -d @/tmp/apify_request.json


Response contains id (run ID) and defaultDatasetId for fetching results.

2. Run Actor Synchronously

Wait for completion and get results directly (max 5 min):

Write to /tmp/apify_request.json:

{
  "startUrls": [{"url": "https://news.ycombinator.com"}],
  "maxPagesPerCrawl": 1,
  "pageFunction": "async function pageFunction(context) { const { request, log, jQuery } = context; const $ = jQuery; const title = $(\"title\").text(); return { url: request.url, title }; }"
}


Then run:

curl -s -X POST "https://api.apify.com/v2/acts/apify~web-scraper/run-sync-get-dataset-items" --header "Authorization: Bearer $APIFY_TOKEN" --header "Content-Type: application/json" -d @/tmp/apify_request.json

3. Check Run Status

⚠️ Important: The {runId} below is a placeholder - replace it with the actual run ID from your async run response (found in .data.id). See the complete workflow example below.

Poll the run status:

# Replace {runId} with actual ID like "HG7ML7M8z78YcAPEB"
curl -s "https://api.apify.com/v2/actor-runs/{runId}" --header "Authorization: Bearer $APIFY_TOKEN" | jq -r '.data.status'


Complete workflow example (capture run ID and check status):

Write to /tmp/apify_request.json:

{
  "startUrls": [{"url": "https://example.com"}],
  "maxPagesPerCrawl": 10
}


Then run:

# Step 1: Start an async run and capture the run ID
RUN_ID=$(curl -s -X POST "https://api.apify.com/v2/acts/apify~web-scraper/runs" --header "Authorization: Bearer $APIFY_TOKEN" --header "Content-Type: application/json" -d @/tmp/apify_request.json | jq -r '.data.id')

# Step 2: Check the run status
curl -s "https://api.apify.com/v2/actor-runs/${RUN_ID}" --header "Authorization: Bearer $APIFY_TOKEN" | jq '.data.status'


Statuses: READY, RUNNING, SUCCEEDED, FAILED, ABORTED, TIMED-OUT

4. Get Dataset Items

⚠️ Important: The {datasetId} below is a placeholder - do not use it literally! You must replace it with the actual dataset ID from your run response (found in .data.defaultDatasetId). See the complete workflow example below for how to capture and use the real ID.

Fetch results from a completed run:

# Replace {datasetId} with actual ID like "WkzbQMuFYuamGv3YF"
curl -s "https://api.apify.com/v2/datasets/{datasetId}/items" --header "Authorization: Bearer $APIFY_TOKEN"


Complete workflow example (run async, wait, and fetch results):

Write to /tmp/apify_request.json:

{
  "startUrls": [{"url": "https://example.com"}],
  "maxPagesPerCrawl": 10
}


Then run:

# Step 1: Start async run and capture IDs
RESPONSE=$(curl -s -X POST "https://api.apify.com/v2/acts/apify~web-scraper/runs" --header "Authorization: Bearer $APIFY_TOKEN" --header "Content-Type: application/json" -d @/tmp/apify_request.json)

RUN_ID=$(echo "$RESPONSE" | jq -r '.data.id')
DATASET_ID=$(echo "$RESPONSE" | jq -r '.data.defaultDatasetId')

# Step 2: Wait for completion (poll status)
while true; do
  STATUS=$(curl -s "https://api.apify.com/v2/actor-runs/${RUN_ID}" --header "Authorization: Bearer $APIFY_TOKEN" | jq -r '.data.status')
  echo "Status: $STATUS"
  [[ "$STATUS" == "SUCCEEDED" ]] && break
  [[ "$STATUS" == "FAILED" || "$STATUS" == "ABORTED" ]] && exit 1
  sleep 5
done

# Step 3: Fetch the dataset items
curl -s "https://api.apify.com/v2/datasets/${DATASET_ID}/items" --header "Authorization: Bearer $APIFY_TOKEN"


With pagination:

# Replace {datasetId} with actual ID
curl -s "https://api.apify.com/v2/datasets/{datasetId}/items?limit=100&offset=0" --header "Authorization: Bearer $APIFY_TOKEN"

5. Popular Actors
Google Search Scraper

Write to /tmp/apify_request.json:

{
  "queries": "web scraping tools",
  "maxPagesPerQuery": 1,
  "resultsPerPage": 10
}


Then run:

curl -s -X POST "https://api.apify.com/v2/acts/apify~google-search-scraper/run-sync-get-dataset-items?timeout=120" --header "Authorization: Bearer $APIFY_TOKEN" --header "Content-Type: application/json" -d @/tmp/apify_request.json

Website Content Crawler

Write to /tmp/apify_request.json:

{
  "startUrls": [{"url": "https://docs.example.com"}],
  "maxCrawlPages": 10,
  "crawlerType": "cheerio"
}


Then run:

curl -s -X POST "https://api.apify.com/v2/acts/apify~website-content-crawler/run-sync-get-dataset-items?timeout=300" --header "Authorization: Bearer $APIFY_TOKEN" --header "Content-Type: application/json" -d @/tmp/apify_request.json

Instagram Scraper

Write to /tmp/apify_request.json:

{
  "directUrls": ["https://www.instagram.com/apaborotnikov/"],
  "resultsType": "posts",
  "resultsLimit": 10
}


Then run:

curl -s -X POST "https://api.apify.com/v2/acts/apify~instagram-scraper/runs" --header "Authorization: Bearer $APIFY_TOKEN" --header "Content-Type: application/json" -d @/tmp/apify_request.json

Amazon Product Scraper

Write to /tmp/apify_request.json:

{
  "categoryOrProductUrls": [{"url": "https://www.amazon.com/dp/B0BSHF7WHW"}],
  "maxItemsPerStartUrl": 1
}


Then run:

curl -s -X POST "https://api.apify.com/v2/acts/junglee~amazon-crawler/runs" --header "Authorization: Bearer $APIFY_TOKEN" --header "Content-Type: application/json" -d @/tmp/apify_request.json

6. List Your Runs

Get recent Actor runs:

curl -s "https://api.apify.com/v2/actor-runs?limit=10&desc=true" --header "Authorization: Bearer $APIFY_TOKEN" | jq '.data.items[] | {id, actId, status, startedAt}'

7. Abort a Run

⚠️ Important: The {runId} below is a placeholder - replace it with the actual run ID. See the complete workflow example below.

Stop a running Actor:

# Replace {runId} with actual ID like "HG7ML7M8z78YcAPEB"
curl -s -X POST "https://api.apify.com/v2/actor-runs/{runId}/abort" --header "Authorization: Bearer $APIFY_TOKEN"


Complete workflow example (start a run and abort it):

Write to /tmp/apify_request.json:

{
  "startUrls": [{"url": "https://example.com"}],
  "maxPagesPerCrawl": 100
}


Then run:

# Step 1: Start an async run and capture the run ID
RUN_ID=$(curl -s -X POST "https://api.apify.com/v2/acts/apify~web-scraper/runs" --header "Authorization: Bearer $APIFY_TOKEN" --header "Content-Type: application/json" -d @/tmp/apify_request.json | jq -r '.data.id')

echo "Started run: $RUN_ID"

# Step 2: Abort the run
curl -s -X POST "https://api.apify.com/v2/actor-runs/${RUN_ID}/abort" --header "Authorization: Bearer $APIFY_TOKEN"

8. List Available Actors

Browse public Actors:

curl -s "https://api.apify.com/v2/store?limit=20&category=ECOMMERCE" --header "Authorization: Bearer $APIFY_TOKEN" | jq '.data.items[] | {name, username, title}'

Popular Actors Reference
Actor ID	Description
apify/web-scraper	General web scraper
apify/website-content-crawler	Crawl entire websites
apify/google-search-scraper	Google search results
apify/instagram-scraper	Instagram posts/profiles
junglee/amazon-crawler	Amazon products
apify/twitter-scraper	Twitter/X posts
apify/youtube-scraper	YouTube videos
apify/linkedin-scraper	LinkedIn profiles
lukaskrivka/google-maps	Google Maps places

Find more at: https://apify.com/store

Run Options
Parameter	Type	Description
timeout	number	Run timeout in seconds
memory	number	Memory in MB (128, 256, 512, 1024, 2048, 4096)
maxItems	number	Max items to return (for sync endpoints)
build	string	Actor build tag (default: "latest")
waitForFinish	number	Wait time in seconds (for async runs)
Response Format

Run object:

{
  "data": {
  "id": "HG7ML7M8z78YcAPEB",
  "actId": "HDSasDasz78YcAPEB",
  "status": "SUCCEEDED",
  "startedAt": "2024-01-01T00:00:00.000Z",
  "finishedAt": "2024-01-01T00:01:00.000Z",
  "defaultDatasetId": "WkzbQMuFYuamGv3YF",
  "defaultKeyValueStoreId": "tbhFDFDh78YcAPEB"
  }
}

Guidelines
Sync vs Async: Use run-sync-get-dataset-items for quick tasks (<5 min), async for longer jobs
Rate Limits: 250,000 requests/min globally, 400/sec per resource
Memory: Higher memory = faster execution but more credits
Timeouts: Default varies by Actor; set explicit timeout for sync calls
Pagination: Use limit and offset for large datasets
Actor Input: Each Actor has different input schema - check Actor's page for details
Credits: Check usage at https://console.apify.com/billing
Weekly Installs
304
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