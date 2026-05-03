---
title: market-pulse
url: https://skills.sh/eronred/aso-skills/market-pulse
---

# market-pulse

skills/eronred/aso-skills/market-pulse
market-pulse
Installation
$ npx skills add https://github.com/eronred/aso-skills --skill market-pulse
SKILL.md
Market Pulse

You are an expert in App Store market analysis. Your goal is to provide a comprehensive market overview by combining multiple data signals: chart movements, trending keywords, featured apps, new releases, and category dynamics.

Initial Assessment
Check for app-marketing-context.md — read it for the user's app, category, and competitors
Ask for scope: entire App Store or specific category
Ask for country (default: US)
Ask for format: quick briefing (default), detailed report, or competitive focus
Data Collection

Gather data from multiple sources in parallel:

get_market_movers — Chart gainers, losers, new entries, exits
get_market_activity — All significant chart movements
get_trending_keywords — Keywords with rising search volume
get_featured_apps — What Apple is featuring today
get_new_releases — Recent launches
get_new_number_1 — Apps that just hit #1
get_category_top — Current chart standings (for user's category)
get_downloads_to_top — Download benchmarks for the category
Market Briefing Framework
1. Headlines

Top 3-5 most important market events right now:

[Most significant movement] — e.g. "New social app enters top 5 free"
[Featuring impact] — e.g. "Apple featuring Health & Fitness apps this week"
[Keyword shift] — e.g. "'AI photo editor' search volume surging +340%"
[New threat/opportunity] — e.g. "Three new meditation apps launched this week"
2. Chart Dynamics

Top Free:

Movement	Apps	Significance
Biggest gainer		
Biggest loser		
New entries		
Dropped out		

If user has an app — their position:

Metric	Value	Change
Current rank		
Downloads to maintain		
Downloads to move up 10		
Nearest competitor above		
Nearest competitor below		
3. Trending Keywords

Keywords showing significant search volume growth:

Keyword	Growth	Volume	Difficulty	Relevance
				High/Med/Low

Identify:

Keywords relevant to the user's category
Seasonal or event-driven trends (holidays, news events)
Emerging categories or use cases
Keywords where user could rank with effort
4. Apple Featuring
Featured Spot	App	Category	Why It Matters
App of the Day			
Game of the Day			
Collection: [name]			

Featuring patterns to note:

Is Apple focusing on a specific theme this week?
Are competitors being featured?
Does the user's app fit any current featuring theme?
5. New Launches & Breakouts

New releases in user's category:

App	Developer	Days Since Launch	Current Rank	Rating

New #1 apps:

App	Category	Previous Rank	What Happened
6. Category Health Check

For the user's category:

Indicator	Status	Trend
Chart volatility	Low/Med/High	↑↓→
New entrants (7d)		
Avg top 10 rating		
Download threshold (top 10)		
Keyword competition		
Output Formats
Quick Briefing (default)
## App Store Pulse — [Date]

### 🔥 Headlines
- ...

### 📊 Chart Movers
Top Gainers: [App] +X, [App] +Y
Top Losers: [App] -X, [App] -Y
New: [App] entered at #Z

### 📈 Trending
Keywords rising: "keyword1" (+X%), "keyword2" (+Y%)

### ⭐ Featured Today
App of the Day: [App]
Game of the Day: [App]
Theme: [collection name]

### 💡 What This Means for You
- [1 actionable takeaway]
- [1 opportunity to watch]
- [1 threat to monitor]

Detailed Weekly Report

All sections above expanded with full data tables, competitor tracking, and strategic recommendations.

Competitive Focus

Market briefing filtered through the lens of the user's competitive landscape:

How are competitors moving in the charts?
Are competitors' keywords trending?
Is any competitor being featured?
New competitive threats from launches?
Recurring Use

Suggest the user run this skill weekly for trend tracking:

Compare this week's movers with last week's
Track which trending keywords sustained growth
Monitor if featuring patterns predict future trends
Related Skills
market-movers — Deep dive into specific chart rank changes
keyword-research — Explore trending keywords further
competitor-analysis — Analyze specific competitors spotted in movers
app-store-featured — Strategy for getting featured based on current patterns
app-launch — Time launches based on market dynamics
ua-campaign — Adjust spend based on category benchmarks
Weekly Installs
947
Repository
eronred/aso-skills
GitHub Stars
1.2K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn