---
title: cloudflare-tunnel
url: https://skills.sh/vm0-ai/vm0-skills/cloudflare-tunnel
---

# cloudflare-tunnel

skills/vm0-ai/vm0-skills/cloudflare-tunnel
cloudflare-tunnel
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill cloudflare-tunnel
SKILL.md
Usage
Basic curl Request

Add two headers to authenticate through Cloudflare Access:

curl -s \
  -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET" \
  "https://your-protected-service.example.com/api/endpoint"

With Additional Authentication

Many services require both Cloudflare Access AND their own authentication:

curl -s \
  -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET" \
  -H "Authorization: Bearer $API_TOKEN" \
  "https://your-protected-service.example.com/api/endpoint"

With Basic Auth
curl -s \
  -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET" \
  -u "username:password" \
  "https://your-protected-service.example.com/api/endpoint"

POST Request with JSON Body

Write to /tmp/request.json:

{
  "key": "value"
}


Then run:

curl -s -X POST \
  -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET" \
  -H "Content-Type: application/json" \
  -d @/tmp/request.json \
  "https://your-protected-service.example.com/api/endpoint"

Download File
curl -s -o /tmp/output.file \
  -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET" \
  "https://your-protected-service.example.com/file"

Skip SSL Verification (Self-signed certs)

Add -k flag for services with self-signed certificates:

curl -k -s \
  -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET" \
  "https://your-protected-service.example.com/api/endpoint"

Required Headers
Header	Value	Description
CF-Access-Client-Id	<client-id>.access	Service Token Client ID
CF-Access-Client-Secret	<secret>	Service Token Client Secret
Common Errors
Error	Cause	Solution
403 Forbidden	Invalid or missing headers	Check Client ID and Secret
403 Forbidden	Token not in Access policy	Add token to application's Access policy
401 Unauthorized	Service's own auth failed	Check service-specific credentials
Connection refused	Tunnel not running	Verify cloudflared is running
Tips
Header order doesn't matter - CF headers can be anywhere in the request
Works with any HTTP method - GET, POST, PUT, DELETE, etc.
Combine with other auth - CF Access + Basic Auth, Bearer Token, etc.
Token rotation - Rotate secrets periodically in Zero Trust dashboard
API Reference
Cloudflare Access: https://developers.cloudflare.com/cloudflare-one/identity/service-tokens/
Zero Trust Dashboard: https://one.dash.cloudflare.com/
Weekly Installs
517
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