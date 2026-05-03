---
title: storyclaw-x2c-publish
url: https://skills.sh/storyclaw-official/talenthub/storyclaw-x2c-publish
---

# storyclaw-x2c-publish

skills/storyclaw-official/talenthub/storyclaw-x2c-publish
storyclaw-x2c-publish
Installation
$ npx skills add https://github.com/storyclaw-official/talenthub --skill storyclaw-x2c-publish
SKILL.md
X2C Publish - Distribution & Wallet API

Publish video content to the X2C platform and manage digital assets.

Critical Rules
Complete ALL workflow steps in order — never skip steps
Always add timeout to curl commands: -m 60
NEVER retry failed requests — report error and ask user
Check project status before publishing to avoid duplicates
Cover URL must be an image (jpg/png/webp), never a video URL
Multi-User Support

Store API key in credentials/{USER_ID}.json:

{
  "x2cApiKey": "x2c_sk_xxx"
}


Set USER_ID env var when calling. OpenClaw passes it automatically from chat context.

Or set X2C_API_KEY env var, or configure via skills."x2c-publish".env.X2C_API_KEY in ~/.openclaw/openclaw.json.

Distribution Workflow
1. distribution/categories → Get categories
2. distribution/upload-url → Get S3 presigned upload URLs
3. Upload files to S3 via HTTP PUT
4. distribution/publish → Submit with public_url from Step 3
5. distribution/query → Check review status
6. distribution/add-episodes → Add more episodes
7. distribution/list → List all projects


Two ways to provide videos:

S3 Upload — use upload-url workflow for local files
External URL — use existing video URLs directly in publish
API Endpoint

All requests go to the X2C Open API. The base URL is configured via X2C_API_BASE_URL env var or defaults to the production endpoint.

Headers:

Content-Type: application/json
X-API-Key: <your_x2c_api_key>
Get Categories
curl -m 60 -X POST "$X2C_API_BASE_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $X2C_API_KEY" \
  -d '{"action": "distribution/categories", "lang": "zh-CN"}'

Get Upload URLs
curl -m 60 -X POST "$X2C_API_BASE_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $X2C_API_KEY" \
  -d '{
    "action": "distribution/upload-url",
    "files": [
      {"file_type": "cover", "file_name": "cover.jpg", "content_type": "image/jpeg"},
      {"file_type": "video", "file_name": "ep1.mp4", "content_type": "video/mp4"}
    ]
  }'


Response includes upload_url, upload_headers, and public_url.

Upload to S3

Use the upload_url and upload_headers from the previous response:

curl -X PUT "<upload_url>" \
  -H "Content-Type: image/jpeg" \
  <additional headers from upload_headers> \
  --data-binary @cover.jpg

Publish Project
curl -m 60 -X POST "$X2C_API_BASE_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $X2C_API_KEY" \
  -d '{
    "action": "distribution/publish",
    "title": "My Drama",
    "description": "A story about...",
    "category_id": "uuid",
    "cover_url": "https://...",
    "video_urls": ["https://..."],
    "enable_prediction": false
  }'

Param	Required	Description
title	Yes	Project name (max 100 chars)
description	Yes	Synopsis (max 2000 chars)
category_id	Yes	Category UUID
cover_url	Yes	Cover image URL
video_urls	Yes	Array of video URLs (1-10)
enable_prediction	No	Enable prediction market
Query Status
curl -m 60 -X POST "$X2C_API_BASE_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $X2C_API_KEY" \
  -d '{"action": "distribution/query", "project_id": "uuid"}'


Status values: draft, pending_review, approved, rejected

Add Episodes
curl -m 60 -X POST "$X2C_API_BASE_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $X2C_API_KEY" \
  -d '{
    "action": "distribution/add-episodes",
    "project_id": "uuid",
    "video_urls": ["https://..."]
  }'

List Projects
curl -m 60 -X POST "$X2C_API_BASE_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $X2C_API_KEY" \
  -d '{"action": "distribution/list", "page": 1, "page_size": 20, "status": "approved"}'

Wallet API (Asset Management)
Get Balance
curl -m 60 -X POST "$X2C_API_BASE_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $X2C_API_KEY" \
  -d '{"action": "wallet/balance"}'


Returns: credits, x2c_wallet_balance, x2c_pending_claim, x2c_pending_release, usdc_balance, wallet_address.

Claim X2C
curl -m 60 -X POST "$X2C_API_BASE_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $X2C_API_KEY" \
  -d '{"action": "wallet/claim-x2c", "amount": 50.0}'

Swap X2C to USDC
curl -m 60 -X POST "$X2C_API_BASE_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $X2C_API_KEY" \
  -d '{"action": "wallet/swap-x2c", "amount": 100.0}'

Withdraw USDC
curl -m 60 -X POST "$X2C_API_BASE_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $X2C_API_KEY" \
  -d '{"action": "wallet/withdraw-usdc", "amount": 10.0, "to_address": "SolanaAddress..."}'

Transaction History
curl -m 60 -X POST "$X2C_API_BASE_URL" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $X2C_API_KEY" \
  -d '{"action": "wallet/transactions", "page": 1, "page_size": 20, "type": "all"}'


Types: earnings (mining, distribution, referral, etc.), purchases (consume, swap, withdrawal, etc.), or all.

Weekly Installs
48
Repository
storyclaw-offic…alenthub
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn