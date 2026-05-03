---
rating: ⭐⭐
title: free-apis-catalog
url: https://skills.sh/jamditis/claude-skills-journalism/free-apis-catalog
---

# free-apis-catalog

skills/jamditis/claude-skills-journalism/free-apis-catalog
free-apis-catalog
Installation
$ npx skills add https://github.com/jamditis/claude-skills-journalism --skill free-apis-catalog
SKILL.md
Free public APIs catalog

A curated list of 1000+ free, legal public APIs organized by category. Many require no auth.

Quick reference by category
Finance and crypto

CoinGecko, CoinCap, Alpha Vantage, Open Exchange Rates, FRED (Federal Reserve Economic Data)

News and media

NewsAPI, GNews, TheNewsAPI, MediaStack, New York Times API

Headlines, RSS, aggregators, real-time sentiment
Weather and geolocation
Open-Meteo — fully free, no API key required
OpenWeatherMap, WeatherAPI, Visual Crossing
Temperature, precipitation, forecasts, historical data for any coordinates
Sports

API-Football, TheSportsDB, PandaScore, ESPN API

Results, team form, player stats, historical league data
ML and text analysis

Hugging Face Inference API, Cohere

Classification, sentiment, summarization, embeddings — pre-trained models
Entertainment

TMDB (movies/TV), RAWG (games), MusicBrainz (music)

Charts, ratings, metadata
Also available (in the full catalog)

Politics, law, health, science, transport, government open data

Evaluating APIs from the catalog
Field	What to check
Auth	"No" = no registration needed
CORS	Matters for browser frontend, irrelevant for backend scripts
Limits	Most free APIs have daily caps — usually enough for personal tools
Weekend project ideas
News alerts: NewsAPI + keyword filter + Telegram bot (2-3 hours)
Sentiment signal: News feed + Hugging Face sentiment model + score -1 to +1
Weather dashboard: Open-Meteo + historical data + forecast for target city
Sports aggregator: Team form, injuries, home advantage in one view
Usage tip

For any new project needing external data: check this catalog first before assuming you need a paid API. Feed the full list to an agent and ask what's useful for the specific task — it will find connections you'd miss manually.

Attribution

Based on "1000+ Free APIs That Will Replace Your Paid Subscriptions" by @qwerty on X (Mar 10, 2026). Original thread catalogs free public APIs across finance, news, weather, sports, ML, entertainment, and more, with evaluation criteria and build ideas.

Weekly Installs
56
Repository
jamditis/claude…urnalism
GitHub Stars
179
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass