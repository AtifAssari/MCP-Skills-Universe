---
rating: ⭐⭐⭐
title: cloudflare-troubleshooting
url: https://skills.sh/daymade/claude-code-skills/cloudflare-troubleshooting
---

# cloudflare-troubleshooting

skills/daymade/claude-code-skills/cloudflare-troubleshooting
cloudflare-troubleshooting
Installation
$ npx skills add https://github.com/daymade/claude-code-skills --skill cloudflare-troubleshooting
SKILL.md
Cloudflare Troubleshooting
Core Principle

Investigate with evidence, not assumptions. Always query Cloudflare API to examine actual configuration before diagnosing issues. The skill's value is the systematic investigation methodology, not predetermined solutions.

Investigation Methodology
1. Gather Credentials

Request from user:

Domain name
Cloudflare account email
Cloudflare Global API Key (or API Token)

Global API Key location: Cloudflare Dashboard → My Profile → API Tokens → View Global API Key

2. Get Zone Information

First step for any Cloudflare troubleshooting - obtain the zone ID:

curl -s -X GET "https://api.cloudflare.com/client/v4/zones?name=<domain>" \
  -H "X-Auth-Email: <email>" \
  -H "X-Auth-Key: <api_key>" | jq '.'


Extract zone_id from result[0].id for subsequent API calls.

3. Investigate Systematically

For each issue, gather evidence before making conclusions. Use Cloudflare API to inspect:

Current configuration state
Recent changes (if audit log available)
Related settings that might interact
Common Investigation Patterns
Redirect Loops (ERR_TOO_MANY_REDIRECTS)

Evidence gathering sequence:

Check SSL/TLS mode:

curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/ssl" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"


Look for: result.value - tells current SSL mode

Check Always Use HTTPS setting:

curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/always_use_https" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"


Check Page Rules for redirects:

curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/pagerules" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"


Look for: forwarding_url or always_use_https actions

Test origin server directly (if possible):

curl -I -H "Host: <domain>" https://<origin_ip>


Diagnosis logic:

SSL mode "flexible" + origin enforces HTTPS = redirect loop
Multiple redirect rules can conflict
Check browser vs curl behavior differences

Fix:

curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/ssl" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key" \
  -H "Content-Type: application/json" \
  --data '{"value":"full"}'


Purge cache after fix:

curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key" \
  -d '{"purge_everything":true}'

DNS Issues

Evidence gathering:

List DNS records:

curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"


Check external DNS resolution:

dig <domain>
dig @8.8.8.8 <domain>


Check DNSSEC status:

curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"


Look for:

Missing A/AAAA/CNAME records
Incorrect proxy status (proxied vs DNS-only)
TTL values
Conflicting records
SSL Certificate Errors

Evidence gathering:

Check SSL certificate status:

curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/ssl/certificate_packs" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"


Check origin certificate (if using Full Strict):

openssl s_client -connect <origin_ip>:443 -servername <domain>


Check SSL settings:

Minimum TLS version
TLS 1.3 status
Opportunistic Encryption

Common issues:

Error 526: SSL mode is "strict" but origin cert invalid
Error 525: SSL handshake failure at origin
Provisioning delay: Wait 15-30 minutes for Universal SSL
Origin Server Errors (502/503/504)

Evidence gathering:

Check if origin is reachable:

curl -I -H "Host: <domain>" https://<origin_ip>


Check DNS records point to correct origin:

curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"


Review load balancer config (if applicable):

curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"


Check firewall rules:

curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"

Learning New APIs

When encountering issues not covered above, consult Cloudflare API documentation:

Browse API reference: https://developers.cloudflare.com/api/
Search for relevant endpoints using issue keywords
Check API schema to understand available operations
Test with GET requests first to understand data structure
Make changes with PATCH/POST after confirming approach

Pattern for exploring new APIs:

# List available settings for a zone
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"

API Reference Overview

Consult references/api_overview.md for:

Common endpoints organized by category
Request/response schemas
Authentication patterns
Rate limits and error handling

Consult references/ssl_modes.md for:

Detailed SSL/TLS mode explanations
Platform compatibility
Security implications

Consult references/common_issues.md for:

Issue patterns and symptoms
Investigation checklists
Platform-specific notes
Best Practices
Evidence-Based Investigation
Query before assuming - Use API to check actual state
Gather multiple data points - Cross-reference settings
Check related configurations - Settings often interact
Verify externally - Use dig/curl to confirm
Test incrementally - One change at a time
API Usage
Parse JSON responses - Use jq or python for readability
Check success field - "success": true/false in responses
Handle errors gracefully - Read errors array in responses
Respect rate limits - Cloudflare API has limits
Use appropriate methods:
GET: Retrieve information
PATCH: Update settings
POST: Create resources / trigger actions
DELETE: Remove resources
Making Changes
Gather evidence first - Understand current state
Identify root cause - Don't guess
Apply targeted fix - Change only what's needed
Purge cache if needed - Especially for SSL/redirect changes
Verify fix - Re-query API to confirm
Inform user of wait times:
Edge server propagation: 30-60 seconds
DNS propagation: Up to 48 hours
Browser cache: Requires manual clear
Security
Never log API keys in output
Warn if user shares credentials in public context
Recommend API Tokens with scoped permissions over Global API Key
Use read-only operations for investigation
Workflow Template
1. Gather: domain, email, API key
2. Get zone_id via zones API
3. Investigate:
   - Query relevant APIs for evidence
   - Check multiple related settings
   - Verify with external tools (dig, curl)
4. Analyze evidence to determine root cause
5. Apply fix via appropriate API endpoint
6. Purge cache if configuration change affects delivery
7. Verify fix via API query and external testing
8. Inform user of resolution and any required actions

Example: Complete Investigation

When user reports "site shows ERR_TOO_MANY_REDIRECTS":

# 1. Get zone ID
curl -s -X GET "https://api.cloudflare.com/client/v4/zones?name=example.com" \
  -H "X-Auth-Email: user@example.com" \
  -H "X-Auth-Key: abc123" | jq '.result[0].id'

# 2. Check SSL mode (primary suspect for redirect loops)
curl -s -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/settings/ssl" \
  -H "X-Auth-Email: user@example.com" \
  -H "X-Auth-Key: abc123" | jq '.result.value'

# If returns "flexible" and origin is GitHub Pages/Netlify/Vercel:

# 3. Fix by changing to "full"
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/ZONE_ID/settings/ssl" \
  -H "X-Auth-Email: user@example.com" \
  -H "X-Auth-Key: abc123" \
  -H "Content-Type: application/json" \
  --data '{"value":"full"}'

# 4. Purge cache
curl -X POST "https://api.cloudflare.com/client/v4/zones/ZONE_ID/purge_cache" \
  -H "X-Auth-Email: user@example.com" \
  -H "X-Auth-Key: abc123" \
  -d '{"purge_everything":true}'

# 5. Inform user: Wait 60 seconds, clear browser cache, retry

When Scripts Are Useful

The bundled scripts (scripts/check_cloudflare_config.py, scripts/fix_ssl_mode.py) serve as:

Reference implementations of investigation patterns
Quick diagnostic tools when Python is available
Examples of programmatic API usage

However, prefer direct API calls via Bash/curl for flexibility and transparency. Scripts should not limit capability - use them when convenient, but use raw API calls when needed for:

Unfamiliar scenarios
Edge cases
Learning/debugging
Operations not covered by scripts

The investigation methodology and API knowledge is the core skill, not the scripts.

Weekly Installs
257
Repository
daymade/claude-…e-skills
GitHub Stars
968
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail