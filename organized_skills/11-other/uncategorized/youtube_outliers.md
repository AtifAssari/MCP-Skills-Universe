---
rating: ⭐⭐⭐
title: youtube-outliers
url: https://skills.sh/aiagentwithdhruv/skills/youtube-outliers
---

# youtube-outliers

skills/aiagentwithdhruv/skills/youtube-outliers
youtube-outliers
Installation
$ npx skills add https://github.com/aiagentwithdhruv/skills --skill youtube-outliers
SKILL.md
YouTube Outlier Detection
Goal

Find high-performing videos in your niche for competitive intelligence and content inspiration.

Scripts
./scripts/scrape_youtube_outliers.py - Scrape and score outliers
./scripts/update_transcripts.py - Fetch transcripts for existing outliers
Usage
# Default run
python3 ./scripts/scrape_youtube_outliers.py

# Custom parameters
python3 ./scripts/scrape_youtube_outliers.py \
  --keywords "AI automation,AI agents" \
  --days 30 \
  --min_score 1.5 \
  --limit 50

How It Works
Searches YouTube for keywords
Calculates outlier score (views / channel average)
Applies recency boost
Fetches transcripts
Generates Claude summaries
Saves to Google Sheet
Output

Google Sheet with:

Outlier Score, Views, Duration
Title, Video Link, Channel
Thumbnail, Summary, Transcript
Publish Date
vs Cross-Niche Outliers
youtube_outliers: Your core niche (daily monitoring)
cross-niche-outliers: Adjacent niches (weekly inspiration)
Environment
APIFY_API_TOKEN=your_token
ANTHROPIC_API_KEY=your_key

Schema
Inputs
Name	Type	Required	Description
keywords	string	No	Comma-separated keywords (default: niche keywords)
days	integer	No	Lookback period in days (default: 30)
min_score	float	No	Minimum outlier score (default: 1.5)
limit	integer	No	Max results (default: 50)
Outputs
Name	Type	Description
sheet_url	string	Google Sheet with outlier videos
Credentials
Name	Source
APIFY_API_TOKEN	.env
ANTHROPIC_API_KEY	.env
Composable With

Skills that chain well with this one: title-variants, recreate-thumbnails, cross-niche-outliers

Cost

Apify credits + Claude API

Weekly Installs
19
Repository
aiagentwithdhruv/skills
GitHub Stars
9
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn