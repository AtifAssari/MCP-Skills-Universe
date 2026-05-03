---
title: changelog
url: https://skills.sh/railwayapp/railway-skills/changelog
---

# changelog

skills/railwayapp/railway-skills/changelog
changelog
Installation
$ npx skills add https://github.com/railwayapp/railway-skills --skill changelog
SKILL.md
Changelog

Railway publishes a weekly product changelog. All changelog data is available as markdown for easy consumption.

Data Sources
Index: all entries

Fetch the full changelog index:

https://railway.com/llms-changelog.md


Returns a list of every changelog entry with this format per entry:

# Railway Product Changelog <Title>
- Title: <title>
- Number: #<4-digit number>
- Link: https://railway.com/changelog/<slug>.md
- Date: <M/D/YYYY>
----------------------------------------


Entries are numbered descending (newest first). The index currently contains 280+ entries spanning 2021 to present.

Individual entry

Every entry link from the index is already an .md URL. Fetch it directly:

https://railway.com/changelog/<slug>.md


Returns full markdown with YAML frontmatter:

---
title: "<title>"
date: <YYYY-MM-DD>
number: <4-digit number>
url: https://railway.com/changelog/<slug>
---


Followed by the full post body (headings, images, links, etc.).

Quick Operations
Get latest changelog entries
Fetch https://railway.com/llms-changelog.md
The first entries are the most recent. Extract the titles, dates, and links.
Read a specific entry
Take the link from the index (already ends in .md)
Fetch it directly to get the full post content
Search for a topic
Fetch the index
Scan entry titles for keywords
Fetch matching entries for full details
Get the N most recent entries
Fetch the index
Take the first N entries
Optionally fetch each one for full content
Routing
Intent	Action
"What's new" / "latest changelog" / "recent changes"	Fetch index, return top 3-5 entries with titles and dates
"Tell me about "	Fetch index, find matching entry by title, fetch that entry's .md URL
"What shipped on "	Fetch index, find entry matching the date, fetch full content
"Summarize changelog #"	Fetch index, find by number, fetch full content
"What's the changelog URL"	Return https://railway.com/changelog (web) or https://railway.com/llms-changelog.md (markdown)
Execution Rules
Always fetch fresh data. The changelog updates weekly (typically Thursdays).
Use WebFetch to retrieve markdown content. Fall back to curl if WebFetch is unavailable.
When summarizing entries, preserve the entry number and date for reference.
Link to the human-readable URL (without .md) when presenting results to users.
For broad questions ("what's new"), return 3-5 recent entries. Don't dump the entire index.
For specific lookups, fetch the full entry content and summarize the relevant sections.
Response Format

When presenting changelog entries:

Title with link to https://railway.com/changelog/<slug> (no .md suffix for user-facing links)
Date and number
Summary of key items when full content is fetched
Weekly Installs
48
Repository
railwayapp/rail…y-skills
GitHub Stars
254
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn