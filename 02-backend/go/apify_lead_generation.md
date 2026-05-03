---
rating: ⭐⭐
title: apify-lead-generation
url: https://skills.sh/apify/agent-skills/apify-lead-generation
---

# apify-lead-generation

skills/apify/agent-skills/apify-lead-generation
apify-lead-generation
Installation
$ npx skills add https://github.com/apify/agent-skills --skill apify-lead-generation
Summary

Multi-platform lead scraping from Google Maps, social media, websites, and search engines.

Supports 16+ Actors covering Google Maps, Instagram, TikTok, Facebook, YouTube, LinkedIn, Google Search, and contact enrichment
Dynamically fetches Actor schemas via mcpc CLI to determine required and optional input parameters before execution
Outputs results as quick chat summaries, CSV, or JSON files with configurable result limits
Requires APIFY_TOKEN in .env file and Node.js 20.6+ for environment variable support
SKILL.md
Lead Generation

Scrape leads from multiple platforms using Apify Actors.

Prerequisites

(No need to check it upfront)

.env file with APIFY_TOKEN
Node.js 20.6+ (for native --env-file support)
mcpc CLI tool: npm install -g @apify/mcpc
Workflow

Copy this checklist and track progress:

Task Progress:
- [ ] Step 1: Determine lead source (select Actor)
- [ ] Step 2: Fetch Actor schema via mcpc
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the lead finder script
- [ ] Step 5: Summarize results

Step 1: Determine Lead Source

Select the appropriate Actor based on user needs:

User Need	Actor ID	Best For
Local businesses	compass/crawler-google-places	Restaurants, gyms, shops
Contact enrichment	vdrmota/contact-info-scraper	Emails, phones from URLs
Instagram profiles	apify/instagram-profile-scraper	Influencer discovery
Instagram posts/comments	apify/instagram-scraper	Posts, comments, hashtags, places
Instagram search	apify/instagram-search-scraper	Places, users, hashtags discovery
TikTok videos/hashtags	clockworks/tiktok-scraper	Comprehensive TikTok data extraction
TikTok hashtags/profiles	clockworks/free-tiktok-scraper	Free TikTok data extractor
TikTok user search	clockworks/tiktok-user-search-scraper	Find users by keywords
TikTok profiles	clockworks/tiktok-profile-scraper	Creator outreach
TikTok followers/following	clockworks/tiktok-followers-scraper	Audience analysis, segmentation
Facebook pages	apify/facebook-pages-scraper	Business contacts
Facebook page contacts	apify/facebook-page-contact-information	Extract emails, phones, addresses
Facebook groups	apify/facebook-groups-scraper	Buying intent signals
Facebook events	apify/facebook-events-scraper	Event networking, partnerships
Google Search	apify/google-search-scraper	Broad lead discovery
YouTube channels	streamers/youtube-scraper	Creator partnerships
Google Maps emails	poidata/google-maps-email-extractor	Direct email extraction
Step 2: Fetch Actor Schema

Fetch the Actor's input schema and details dynamically using mcpc:

export $(grep APIFY_TOKEN .env | xargs) && mcpc --json mcp.apify.com --header "Authorization: Bearer $APIFY_TOKEN" tools-call fetch-actor-details actor:="ACTOR_ID" | jq -r ".content"


Replace ACTOR_ID with the selected Actor (e.g., compass/crawler-google-places).

This returns:

Actor description and README
Required and optional input parameters
Output fields (if available)
Step 3: Ask User Preferences

Before running, ask:

Output format:
Quick answer - Display top few results in chat (no file saved)
CSV - Full export with all fields
JSON - Full export in JSON format
Number of results: Based on character of use case
Step 4: Run the Script

Quick answer (display in chat, no file):

node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'


CSV:

node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.csv \
  --format csv


JSON:

node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.json \
  --format json

Step 5: Summarize Results

After completion, report:

Number of leads found
File location and name
Key fields available
Suggested next steps (filtering, enrichment)
Error Handling

APIFY_TOKEN not found - Ask user to create .env with APIFY_TOKEN=your_token mcpc not found - Ask user to install npm install -g @apify/mcpc Actor not found - Check Actor ID spelling Run FAILED - Ask user to check Apify console link in error output Timeout - Reduce input size or increase --timeout

Weekly Installs
2.8K
Repository
apify/agent-skills
GitHub Stars
2.0K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn