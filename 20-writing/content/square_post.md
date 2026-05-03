---
rating: ⭐⭐
title: square-post
url: https://skills.sh/binance/binance-skills-hub/square-post
---

# square-post

skills/binance/binance-skills-hub/square-post
square-post
Installation
$ npx skills add https://github.com/binance/binance-skills-hub --skill square-post
Summary

Post text content to Binance Square with API key authentication and error handling.

Supports pure text posts with hashtag support; constructs shareable post URLs on success
Requires X-Square-OpenAPI-Key header authentication; agent prompts for missing credentials before attempting posts
Handles 20+ error codes including sensitive content detection, daily post limits, identity verification requirements, and account bans
Agent optimizes raw user input for readability and requests confirmation before posting; never displays full API keys in output
SKILL.md
Square Post Skill
Overview

Post text content to Binance Square.

API: Add Content
Method: POST

URL:

https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add


Request Headers:

Header	Required	Description
X-Square-OpenAPI-Key	Yes	Square OpenAPI Key
Content-Type	Yes	application/json
clienttype	Yes	binanceSkill

Request Body:

Field	Type	Required	Description
bodyTextOnly	string	Yes	Post content text
Example Request
curl -X POST 'https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add' \
  -H 'X-Square-OpenAPI-Key: your_api_key' \
  -H 'Content-Type: application/json' \
  -H 'clienttype: binanceSkill' \
  -d '{
    "bodyTextOnly": "BTC looking bullish today!"
  }'

Response Example
{
  "code": "000000",
  "message": null,
  "data": {
    "id": "content_id_here"
  }
}

Response Fields
Field	Type	Description
code	string	"000000" = success
message	string	Error message (null on success)
data.id	string	Created content ID
Post URL Format

On success, construct the post URL:

https://www.binance.com/square/post/{id}


Example: If data.id is 298177291743282, the post URL is:

https://www.binance.com/square/post/298177291743282

Error Handling
Code	Description
000000	Success
10004	Network error. Please try again
10005	Only allowed for users who have completed identity verification
10007	Feature unavailable
20002	Detected sensitive words
20013	Content length is limited
20020	Publishing empty content is not supported
20022	Detected sensitive words (with risk segments)
20041	Potential security risk with the URL
30004	User not found
30008	Banned for violating platform guidelines
220003	API Key not found
220004	API Key expired
220009	Daily post limit exceeded for OpenAPI
220010	Unsupported content type
220011	Content body must not be empty
2000001	Account permanently blocked from posting
2000002	Device permanently blocked from posting
Authentication
Required Header
Header	Required	Description
X-Square-OpenAPI-Key	Yes	API key for Square posting
Security
Never Display Full Keys

When showing credentials to users:

X-Square-OpenAPI-Key: Show first 5 + last 4 characters: abc12...xyz9
Listing Accounts

When listing accounts, show names and description only — never full keys:

Accounts:
* default (Default account for Square posting)

Agent Behavior
Check key before API calls: Verify that X-Square-OpenAPI-Key is configured and not the placeholder your_api_key
Prompt for key if missing: If key is not configured, ask user to provide their API Key first
Prompt for content if missing: If user triggers posting but doesn't provide specific content, ask what they want to post
Never display full keys: Only show first 5 + last 4 characters (e.g., abc12...xyz9)
Store provided keys: When user provides a new key, update the Accounts section in this file
Optimize content before posting:
Polish user's raw input for better readability
Do NOT auto-add hashtags (#xxx) during optimization — keep any hashtags the user wrote, but never add new ones
Show optimized content and ask user to choose: use optimized version or post original text
Return post URL on success: After successful post, return the URL https://www.binance.com/square/post/{id}
Handle missing id: If code is 000000 but data.id is empty or missing, inform user that post may have succeeded but URL is unavailable, suggest checking Square page manually
Notes
Only pure text posts are supported currently
Check daily post limit to avoid 220009 error
Weekly Installs
3.1K
Repository
binance/binance…ills-hub
GitHub Stars
801
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail