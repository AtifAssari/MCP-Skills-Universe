---
title: footballbin-predictions
url: https://skills.sh/davila7/claude-code-templates/footballbin-predictions
---

# footballbin-predictions

skills/davila7/claude-code-templates/footballbin-predictions
footballbin-predictions
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill footballbin-predictions
SKILL.md
FootballBin Match Predictions

Get AI-powered predictions for Premier League and Champions League matches via the FootballBin MCP API.

Quick Start

Run scripts/footballbin.sh with the following commands:

Get current matchweek predictions
scripts/footballbin.sh predictions premier_league
scripts/footballbin.sh predictions champions_league

Get specific matchweek
scripts/footballbin.sh predictions premier_league 27

Filter by team
scripts/footballbin.sh predictions premier_league --home arsenal
scripts/footballbin.sh predictions premier_league --away liverpool
scripts/footballbin.sh predictions premier_league --home chelsea --away wolves

List available tools
scripts/footballbin.sh tools

Supported Leagues
Input	League
premier_league, epl, pl, prem	Premier League
champions_league, ucl, cl	Champions League
Supported Team Aliases

Common aliases work: united (Man Utd), city (Man City), spurs (Tottenham), wolves (Wolverhampton), gunners (Arsenal), reds (Liverpool), blues (Chelsea), villa (Aston Villa), forest (Nottingham Forest), palace (Crystal Palace), barca (Barcelona), real (Real Madrid), bayern (Bayern Munich), psg (PSG), juve (Juventus), inter (Inter Milan), bvb (Dortmund), atleti (Atletico Madrid).

Response Data

Each match prediction includes:

Half-time score (e.g., "1:0")
Full-time score (e.g., "2:1")
Next goal scorer (e.g., "Home,Salah")
Corner count (e.g., "7:4")
Key players with form-based reasoning
External Endpoints
URL	Data Sent	Purpose
https://ru7m5svay1.execute-api.eu-central-1.amazonaws.com/prod/mcp	League, matchweek, team filters	Fetch match predictions
Security & Privacy
No API key required (public endpoint, rate-limited)
No user data collected or stored
Read-only: only fetches prediction data
No secrets or environment variables needed
Links
iOS App: https://apps.apple.com/app/footballbin/id6757111871
Android App: https://play.google.com/store/apps/details?id=com.achan.footballbinandroid
Weekly Installs
109
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass