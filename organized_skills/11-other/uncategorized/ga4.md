---
rating: ⭐⭐
title: ga4
url: https://skills.sh/jdrhyne/agent-skills/ga4
---

# ga4

skills/jdrhyne/agent-skills/ga4
ga4
Installation
$ npx skills add https://github.com/jdrhyne/agent-skills --skill ga4
SKILL.md
GA4 - Google Analytics 4 Data API

Query GA4 properties for analytics data: page views, sessions, users, traffic sources, conversions, and more.

Setup (one-time)
Enable Google Analytics Data API: https://console.cloud.google.com/apis/library/analyticsdata.googleapis.com
Create OAuth credentials or use existing Google Cloud project
Set environment variables:
GA4_PROPERTY_ID - Your GA4 property ID (numeric, e.g., "123456789")
GOOGLE_CLIENT_ID - OAuth client ID
GOOGLE_CLIENT_SECRET - OAuth client secret
GOOGLE_REFRESH_TOKEN - OAuth refresh token (from initial auth flow)
Common Queries
Top Pages (by pageviews)
python3 scripts/ga4_query.py --metric screenPageViews --dimension pagePath --limit 30

Top Pages with Sessions & Users
python3 scripts/ga4_query.py --metrics screenPageViews,sessions,totalUsers --dimension pagePath --limit 20

Traffic Sources
python3 scripts/ga4_query.py --metric sessions --dimension sessionSource --limit 20

Landing Pages
python3 scripts/ga4_query.py --metric sessions --dimension landingPage --limit 30

Custom Date Range
python3 scripts/ga4_query.py --metric sessions --dimension pagePath --start 2026-01-01 --end 2026-01-15

Filter by Page Path
python3 scripts/ga4_query.py --metric screenPageViews --dimension pagePath --filter "pagePath=~/blog/"

Available Metrics

Common metrics: screenPageViews, sessions, totalUsers, newUsers, activeUsers, bounceRate, averageSessionDuration, conversions, eventCount

Available Dimensions

Common dimensions: pagePath, pageTitle, landingPage, sessionSource, sessionMedium, sessionCampaignName, country, city, deviceCategory, browser, date

Output Formats

Default: Table format Add --json for JSON output Add --csv for CSV output

Weekly Installs
143
Repository
jdrhyne/agent-skills
GitHub Stars
232
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass