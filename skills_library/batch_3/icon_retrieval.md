---
title: icon-retrieval
url: https://skills.sh/antvis/chart-visualization-skills/icon-retrieval
---

# icon-retrieval

skills/antvis/chart-visualization-skills/icon-retrieval
icon-retrieval
Installation
$ npx skills add https://github.com/antvis/chart-visualization-skills --skill icon-retrieval
SKILL.md
Icon Search

Use the icon HTTP API directly with curl.

API
Search Endpoint
Method: GET
URL: https://lab.weavefox.cn/api/v1/infographic/icon
Query params:
text (required): search keyword, e.g. "data analysis"
topK (optional): number of icons to fetch (1-20), default 5

Example:

curl -sS -L --max-time 20 "https://lab.weavefox.cn/api/v1/infographic/icon?text=document&topK=5"


Typical response:

{
  "success": true,
  "data": [
    "https://example.com/icon1.svg",
    "https://example.com/icon2.svg"
  ]
}

Retrieve SVG Content
curl -sS -L --max-time 20 "https://example.com/icon1.svg"

Workflow
Determine the icon concept keyword (for example: security, document, data).
Search icon URLs using the API endpoint.
Use curl to fetch the SVG content of selected URLs.
Use SVG directly in pages, diagrams, or infographic materials.
Notes
Use URL encoding for special characters in text.
topK range is 1–20; if omitted, the service returns up to 5 results.
For network issues, retry with a smaller topK or verify endpoint accessibility.
Weekly Installs
676
Repository
antvis/chart-vi…n-skills
GitHub Stars
269
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn