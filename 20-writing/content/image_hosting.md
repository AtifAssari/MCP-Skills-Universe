---
title: image-hosting
url: https://skills.sh/img402/skills/image-hosting
---

# image-hosting

skills/img402/skills/image-hosting
image-hosting
Installation
$ npx skills add https://github.com/img402/skills --skill image-hosting
SKILL.md
Image Hosting — img402

Upload an image to img402.dev and get a public URL. No account, no API key, no config.

Quick reference
# Upload (multipart)
curl -s -X POST https://img402.dev/api/free -F image=@/path/to/image.png

# Response
# {"url":"https://i.img402.dev/aBcDeFgHiJ.png","id":"aBcDeFgHiJ","contentType":"image/png","sizeBytes":182400,"expiresAt":"2026-02-17T..."}

Workflow
Get image: Use an existing file, or generate/download one.
Check size: Must be under 1MB. If larger, resize:
sips -Z 1600 /path/to/image.png    # macOS — scale longest edge to 1200px
convert /path/to/image.png -resize 1600x1600 /path/to/image.png  # ImageMagick

Upload:
curl -s -X POST https://img402.dev/api/free -F image=@/path/to/image.png

Use the URL: The url field in the response is a public CDN link. Embed it wherever needed.
Constraints
Max size: 1MB
Retention: 7 days
Formats: PNG, JPEG, GIF, WebP
Rate limit: 1,000 free uploads/day (global)
No auth required
Paid tier

For images that need to persist longer (1 year, 5MB max), use the paid endpoint at $0.01 USDC via x402:

# Step 1: Get an upload token (requires x402 payment)
POST https://img402.dev/api/upload/token
# → {"token": "a1b2c3...", "expiresAt": "..."}

# Step 2: Upload with the token
curl -s -X POST https://img402.dev/api/upload \
  -H "X-Upload-Token: a1b2c3..." \
  -F image=@/path/to/image.png


See https://img402.dev/blog/paying-x402-apis for details on x402 payment.

Weekly Installs
19
Repository
img402/skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass