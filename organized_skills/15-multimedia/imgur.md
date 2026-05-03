---
rating: ⭐⭐
title: imgur
url: https://skills.sh/vm0-ai/vm0-skills/imgur
---

# imgur

skills/vm0-ai/vm0-skills/imgur
imgur
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill imgur
SKILL.md
How to Use
Upload Local Image
curl -X POST https://api.imgur.com/3/image -H "Authorization: Client-ID $IMGUR_CLIENT_ID" -F "image=@/path/to/image.png"

Upload from URL
curl -X POST https://api.imgur.com/3/image -H "Authorization: Client-ID $IMGUR_CLIENT_ID" -F "image=https://example.com/image.png" -F "type=url"

Upload Base64
curl -X POST https://api.imgur.com/3/image -H "Authorization: Client-ID $IMGUR_CLIENT_ID" -F "image=$(base64 -i /path/to/image.png)" -F "type=base64"

Optional Parameters
Parameter	Description
title	Image title
description	Image description
name	Filename
curl -X POST https://api.imgur.com/3/image -H "Authorization: Client-ID $IMGUR_CLIENT_ID" -F "image=@screenshot.png" -F "title=My Screenshot" -F "description=Screenshot from my app"

Response
{
  "data": {
  "id": "abc123",
  "link": "https://i.imgur.com/abc123.png",
  "deletehash": "xyz789"
  },
  "success": true,
  "status": 200
}


Key fields:

data.link - Public URL to use in Markdown: ![img](https://i.imgur.com/abc123.png)
data.deletehash - Save this to delete the image later
Delete Image

Replace <your-deletehash> with the deletehash from the upload response:

curl -X DELETE https://api.imgur.com/3/image/<your-deletehash> -H "Authorization: Client-ID $IMGUR_CLIENT_ID"

Rate Limits
~12,500 requests/day
~1,250 uploads/day (uploads cost 10 credits)
Headers show remaining: X-RateLimit-ClientRemaining
Guidelines
Save deletehash: Store it if you need to delete images later
Anonymous uploads: Images are not tied to any account
Supported formats: JPEG, PNG, GIF, APNG, TIFF, BMP, PDF, XCF, WebP
Max file size: 20MB for images, 200MB for GIFs
API Reference
Documentation: https://apidocs.imgur.com/
Register App: https://api.imgur.com/oauth2/addclient
Weekly Installs
101
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