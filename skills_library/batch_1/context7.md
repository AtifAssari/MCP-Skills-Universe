---
title: context7
url: https://skills.sh/intellectronica/agent-skills/context7
---

# context7

skills/intellectronica/agent-skills/context7
context7
Installation
$ npx skills add https://github.com/intellectronica/agent-skills --skill context7
Summary

Retrieve current documentation for software libraries and frameworks via the Context7 API.

Two-step workflow: search for a library by name and topic, then fetch documentation using the returned library ID
Supports documentation retrieval across hundreds of libraries (React, Next.js, FastAPI, Axios, and others) with plain-text or JSON response formats
Query parameters accept specific topics for relevance ranking; results include library descriptions and snippet counts
No API key required for basic usage, though rate-limited; plain-text output (type=txt) recommended for readability
SKILL.md
Context7
Overview

This skill enables retrieval of current documentation for software libraries and components by querying the Context7 API via curl. Use it instead of relying on potentially outdated training data.

Workflow
Step 1: Search for the Library

To find the Context7 library ID, query the search endpoint:

curl -s "https://context7.com/api/v2/libs/search?libraryName=LIBRARY_NAME&query=TOPIC" | jq '.results[0]'


Parameters:

libraryName (required): The library name to search for (e.g., "react", "nextjs", "fastapi", "axios")
query (required): A description of the topic for relevance ranking

Response fields:

id: Library identifier for the context endpoint (e.g., /websites/react_dev_reference)
title: Human-readable library name
description: Brief description of the library
totalSnippets: Number of documentation snippets available
Step 2: Fetch Documentation

To retrieve documentation, use the library ID from step 1:

curl -s "https://context7.com/api/v2/context?libraryId=LIBRARY_ID&query=TOPIC&type=txt"


Parameters:

libraryId (required): The library ID from search results
query (required): The specific topic to retrieve documentation for
type (optional): Response format - json (default) or txt (plain text, more readable)
Examples
React hooks documentation
# Find React library ID
curl -s "https://context7.com/api/v2/libs/search?libraryName=react&query=hooks" | jq '.results[0].id'
# Returns: "/websites/react_dev_reference"

# Fetch useState documentation
curl -s "https://context7.com/api/v2/context?libraryId=/websites/react_dev_reference&query=useState&type=txt"

Next.js routing documentation
# Find Next.js library ID
curl -s "https://context7.com/api/v2/libs/search?libraryName=nextjs&query=routing" | jq '.results[0].id'

# Fetch app router documentation
curl -s "https://context7.com/api/v2/context?libraryId=/vercel/next.js&query=app+router&type=txt"

FastAPI dependency injection
# Find FastAPI library ID
curl -s "https://context7.com/api/v2/libs/search?libraryName=fastapi&query=dependencies" | jq '.results[0].id'

# Fetch dependency injection documentation
curl -s "https://context7.com/api/v2/context?libraryId=/fastapi/fastapi&query=dependency+injection&type=txt"

Tips
Use type=txt for more readable output
Use jq to filter and format JSON responses
Be specific with the query parameter to improve relevance ranking
If the first search result is not correct, check additional results in the array
URL-encode query parameters containing spaces (use + or %20)
No API key is required for basic usage (rate-limited)
Weekly Installs
5.8K
Repository
intellectronica…t-skills
GitHub Stars
254
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn