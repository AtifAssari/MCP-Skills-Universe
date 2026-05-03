---
rating: ⭐⭐
title: google-serper-search
url: https://skills.sh/shuliuzhenhua-sys/google-serper-search/google-serper-search
---

# google-serper-search

skills/shuliuzhenhua-sys/google-serper-search/google-serper-search
google-serper-search
Installation
$ npx skills add https://github.com/shuliuzhenhua-sys/google-serper-search --skill google-serper-search
SKILL.md
Google Serper Search

Use scripts/serper_search.py to call the Serper API and return JSON search results.

Check configuration

Confirm SERPER_API_KEY is available before searching.

Run:

printenv SERPER_API_KEY


If the variable is empty, read references/configuration.md and set it in the current shell or shell profile before continuing.

Run searches

Use:

python3 scripts/serper_search.py "query"


Use filters when the request needs them:

python3 scripts/serper_search.py "query" --type news --gl us --hl en --tbs "past week"


Supported --type values:

search
images
videos
places
maps
reviews
news
shopping
lens
scholar
patents
autocomplete

Aliases:

web -> search
image -> images
img -> images

Supported --tbs shortcuts:

past hour
past 24 hours
past week
past month
past year

Use --gl for country and --hl for language when the request needs regional or language-specific results.

Interpret results

Read references/api_response.md when you need the result schema.

For web and news results, prioritize:

knowledgeGraph
organic
peopleAlsoAsk
relatedSearches

For image results, prioritize:

image title
imageUrl
thumbnailUrl
dimensions
source page
Present the answer

Summarize the most relevant results instead of dumping raw JSON unless the user asks for the raw response.

Include source links in the final answer.

Call out missing configuration or API errors explicitly when the script returns an error field.

Weekly Installs
167
Repository
shuliuzhenhua-s…r-search
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail