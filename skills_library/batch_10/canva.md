---
title: canva
url: https://skills.sh/abgohel/canva-skill/canva
---

# canva

skills/abgohel/canva-skill/canva
canva
Installation
$ npx skills add https://github.com/abgohel/canva-skill --skill canva
SKILL.md
Canva Skill

Create, export, and manage Canva designs via the Connect API.

When to Use
"Create an Instagram post about [topic]"
"Export my Canva design as PNG"
"List my recent designs"
"Create a carousel from these points"
"Upload this image to Canva"
Prerequisites

Create a Canva Integration:

Go to https://www.canva.com/developers/
Create a new integration
Get your Client ID and Client Secret

Set Environment Variables:

export CANVA_CLIENT_ID="your_client_id"
export CANVA_CLIENT_SECRET="your_client_secret"


Authenticate (first time): Run the auth flow to get access tokens (stored in ~/.canva/tokens.json)

API Base URL
https://api.canva.com/rest/v1

Authentication

Canva uses OAuth 2.0. The skill handles token refresh automatically.

# Get access token (stored in ~/.canva/tokens.json)
ACCESS_TOKEN=$(cat ~/.canva/tokens.json | jq -r '.access_token')

Core Operations
List Designs
curl -s "https://api.canva.com/rest/v1/designs" \
  -H "Authorization: Bearer $ACCESS_TOKEN" | jq .

Get Design Details
curl -s "https://api.canva.com/rest/v1/designs/{designId}" \
  -H "Authorization: Bearer $ACCESS_TOKEN" | jq .

Create Design from Template
curl -X POST "https://api.canva.com/rest/v1/autofills" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "brand_template_id": "TEMPLATE_ID",
    "data": {
      "title": {"type": "text", "text": "Your Title"},
      "body": {"type": "text", "text": "Your body text"}
    }
  }'

Export Design
# Start export job
curl -X POST "https://api.canva.com/rest/v1/exports" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "design_id": "DESIGN_ID",
    "format": {"type": "png", "width": 1080, "height": 1080}
  }'

# Check export status
curl -s "https://api.canva.com/rest/v1/exports/{jobId}" \
  -H "Authorization: Bearer $ACCESS_TOKEN" | jq .

Upload Asset
curl -X POST "https://api.canva.com/rest/v1/asset-uploads" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/octet-stream" \
  -H 'Asset-Upload-Metadata: {"name": "my-image.png"}' \
  --data-binary @image.png

List Brand Templates
curl -s "https://api.canva.com/rest/v1/brand-templates" \
  -H "Authorization: Bearer $ACCESS_TOKEN" | jq .

Export Formats
Format	Options
PNG	width, height, lossless
JPG	width, height, quality (1-100)
PDF	standard, print
MP4	(for video designs)
GIF	(for animated designs)
Common Workflows
Create Instagram Post
List brand templates: GET /brand-templates
Find Instagram post template
Autofill with content: POST /autofills
Export as PNG 1080x1080: POST /exports
Download the exported file
Create Carousel
Create multiple designs using autofill
Export each as PNG
Combine for posting
Batch Export
List designs: GET /designs
Loop through and export each
Download all files
Rate Limits
Most endpoints: 100 requests/minute
Upload/Export: 30 requests/minute
Error Handling

Common errors:

401 - Token expired, refresh needed
403 - Missing required scope
429 - Rate limit exceeded
404 - Design/template not found
Scopes Required
design:content:read - Read designs
design:content:write - Create/modify designs
asset:read - Read assets
asset:write - Upload assets
brandtemplate:content:read - Read brand templates
Tips
Use Brand Templates - Pre-designed templates are faster than creating from scratch
Batch Operations - Group exports to avoid rate limits
Cache Template IDs - Store commonly used template IDs locally
Check Job Status - Exports are async; poll until complete
Resources
Canva Connect API Docs
OpenAPI Spec
Starter Kit

Built by Meow 😼 for the Moltbook community 🦞

Weekly Installs
20
Repository
abgohel/canva-skill
GitHub Stars
3
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass