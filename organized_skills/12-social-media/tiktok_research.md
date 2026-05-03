---
rating: ⭐⭐⭐
title: tiktok-research
url: https://skills.sh/bradautomates/head-of-content/tiktok-research
---

# tiktok-research

skills/bradautomates/head-of-content/tiktok-research
tiktok-research
Installation
$ npx skills add https://github.com/bradautomates/head-of-content --skill tiktok-research
Summary

Identify high-performing TikTok videos, extract viral hooks, and generate actionable content insights.

Fetches videos from tracked accounts using Apify's TikTok Scraper, then applies statistical outlier detection to surface top performers
Analyzes the top 5 outlier videos with AI to extract hook techniques, content structure, retention patterns, and CTA strategies
Generates structured markdown reports ranking videos by engagement, mapping content patterns, and synthesizing replicable formulas for your own content
Requires Apify and Gemini API credentials, plus a pre-configured list of TikTok accounts to monitor
SKILL.md
TikTok Research

Research high-performing TikTok videos, identify outliers, and analyze top video content for hooks and structure.

Prerequisites
APIFY_TOKEN environment variable or in .env
GEMINI_API_KEY environment variable or in .env
apify-client and google-genai Python packages
Accounts configured in .claude/context/tiktok-accounts.md

Verify setup:

python3 -c "
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
from apify_client import ApifyClient
from google import genai
assert os.environ.get('APIFY_TOKEN'), 'APIFY_TOKEN not set'
assert os.environ.get('GEMINI_API_KEY'), 'GEMINI_API_KEY not set'
" && echo "Prerequisites OK"

Workflow
1. Create Run Folder
RUN_FOLDER="tiktok-research/$(date +%Y-%m-%d_%H%M%S)" && mkdir -p "$RUN_FOLDER" && echo "$RUN_FOLDER"

2. Fetch Content
python3 .claude/skills/tiktok-research/scripts/fetch_tiktok.py \
  --days 30 \
  --limit 50 \
  --sorting latest \
  --output {RUN_FOLDER}/raw.json


Parameters:

--days: Days back to search (default: 30)
--limit: Max videos per account (default: 50)
--sorting: "latest", "popular", or "oldest" (default: latest)
--usernames: Override accounts file with specific usernames
3. Identify Outliers
python3 .claude/skills/tiktok-research/scripts/analyze_posts.py \
  --input {RUN_FOLDER}/raw.json \
  --output {RUN_FOLDER}/outliers.json \
  --threshold 2.0


Output JSON contains:

total_videos: Number of videos analyzed
outlier_count: Number of outliers found
topics: Top hashtags, sounds, and keywords
accounts: List of accounts analyzed
outliers: Array of outlier videos with engagement metrics
4. Analyze Top Videos with AI
python3 .claude/skills/video-content-analyzer/scripts/analyze_videos.py \
  --input {RUN_FOLDER}/outliers.json \
  --output {RUN_FOLDER}/video-analysis.json \
  --platform tiktok \
  --max-videos 5


Extracts from each video:

Hook technique and replicable formula
Content structure and sections
Retention techniques
CTA strategy

See the video-content-analyzer skill for full output schema and hook/format types.

5. Generate Report

Read {RUN_FOLDER}/outliers.json and {RUN_FOLDER}/video-analysis.json, then generate {RUN_FOLDER}/report.md.

Report Structure:

# TikTok Research Report

Generated: {date}

## Top Performing Hooks

Ranked by engagement. Use these formulas for your content.

### Hook 1: {technique} - @{username}
- **Opening**: "{opening_line}"
- **Why it works**: {attention_grab}
- **Replicable Formula**: {replicable_formula}
- **Engagement**: {diggCount} likes, {commentCount} comments, {playCount} views
- [Watch Video]({webVideoUrl})

[Repeat for each analyzed video]

## Content Structure Patterns

| Video | Format | Pacing | Key Retention Techniques |
|-------|--------|--------|--------------------------|
| @username | {format} | {pacing} | {techniques} |

## CTA Strategies

| Video | CTA Type | CTA Text | Placement |
|-------|----------|----------|-----------|
| @username | {type} | "{cta_text}" | {placement} |

## All Outliers

| Rank | Username | Likes | Comments | Shares | Views | Engagement Rate |
|------|----------|-------|----------|--------|-------|-----------------|
[List all outliers with metrics and links]

## Trending Topics

### Top Hashtags
[From outliers.json topics.hashtags]

### Top Sounds
[From outliers.json topics.sounds]

### Top Keywords
[From outliers.json topics.keywords]

## Actionable Takeaways

[Synthesize patterns into 4-6 specific recommendations]

## Accounts Analyzed
[List accounts]


Focus on actionable insights. The "Top Performing Hooks" section with replicable formulas should be prominent.

Quick Reference

Full pipeline:

RUN_FOLDER="tiktok-research/$(date +%Y-%m-%d_%H%M%S)" && mkdir -p "$RUN_FOLDER" && \
python3 .claude/skills/tiktok-research/scripts/fetch_tiktok.py -o "$RUN_FOLDER/raw.json" && \
python3 .claude/skills/tiktok-research/scripts/analyze_posts.py -i "$RUN_FOLDER/raw.json" -o "$RUN_FOLDER/outliers.json" && \
python3 .claude/skills/video-content-analyzer/scripts/analyze_videos.py -i "$RUN_FOLDER/outliers.json" -o "$RUN_FOLDER/video-analysis.json" -p tiktok


Then read both JSON files and generate the report.

Engagement Metrics

Engagement Score: likes + (3 x comments) + (2 x shares) + (2 x saves) + (0.05 x views)

Outlier Detection: Videos with engagement rate > mean + (threshold x std_dev)

Engagement Rate: (score / followers) x 100

TikTok-Specific Fields
diggCount: Likes/hearts
shareCount: Shares
playCount: Video views
commentCount: Comments
collectCount: Saves/bookmarks
authorFollowers: Creator's follower count
musicName: Sound used in video
musicOriginal: Whether sound is original
Weekly Installs
672
Repository
bradautomates/h…-content
GitHub Stars
86
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn