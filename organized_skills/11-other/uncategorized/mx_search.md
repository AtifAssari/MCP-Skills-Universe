---
rating: ⭐⭐
title: mx-search
url: https://skills.sh/site/skills.volces.com/mx-search
---

# mx-search

skills/skills.volces.com/mx_search
mx_search
$ npx skills add https://skills.volces.com/skills/clawhub/xpmars
SKILL.md
妙想资讯搜索 Skill (mx_search)
Overview

This skill provides a safe way to query the Meixiang financial search service for news, announcements, research reports, policy documents, trading rules, specific events, impact analyses, and any other external data needed for finance‑related queries. It ensures the results come from authoritative sources and are current.

Prerequisites
Obtain an API key from the Meixiang Skills page.
Set the API key in the environment variable MX_APIKEY.
export MX_APIKEY="your_api_key_here"

Ensure curl is available on the system (default on macOS).
Usage

When the user asks a finance‑related question, follow these steps:

Construct the query string based on the user's request.
Execute the POST request to the Meixiang endpoint:
curl -X POST \
  --location 'https://mkapi2.dfcfs.com/finskillshub/api/claw/news-search' \
  --header 'Content-Type: application/json' \
  --header "apikey:${MX_APIKEY}" \
  --data '{"query":"<YOUR_QUERY_HERE>"}'

Parse the JSON response. Important fields include:
title: concise headline of the information.
secuList: list of related securities (code, name, type).
trunk: main text or structured data block.
Present the information to the user in a readable format, optionally highlighting the securities involved.
Example

User query: "立讯精密的资讯"

Command executed:

curl -X POST --location 'https://mkapi2.dfcfs.com/finskillshub/api/claw/news-search' \
  --header 'Content-Type: application/json' \
  --header 'apikey:${MX_APIKEY}' \
  --data '{"query":"立讯精密的资讯"}'


Sample response excerpt:

{
  "title": "立讯精密最新研报",
  "secuList": [{"secuCode":"002475","secuName":"立讯精密","secuType":"股票"}],
  "trunk": "...report content..."
}


Formatted reply to user:

标题: 立讯精密最新研报
关联证券: 002475 立讯精密 (股票)
内容摘要: ... (provide concise summary from trunk)
Saving Results (optional)

If the user wants to keep the result, you can save the raw JSON to a file in the current work directory:

curl ... > mx_search_result.json


Then inform the user of the file path.

When Not to Use

Do not use this skill for non‑financial queries, or when the user explicitly asks for opinion‑based answers without needing source data.

References
Meixiang API documentation (internal).
Example queries table (see above).
Weekly Installs
42
Source
skills.volces.c…b/xpmars
First Seen
10 days ago