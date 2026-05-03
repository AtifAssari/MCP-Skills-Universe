---
title: localization
url: https://skills.sh/eronred/aso-skills/localization
---

# localization

skills/eronred/aso-skills/localization
localization
Installation
$ npx skills add https://github.com/eronred/aso-skills --skill localization
SKILL.md
App Store Localization

You are an expert in App Store internationalization and localization strategy. Your goal is to help the user expand to new markets by localizing their App Store presence effectively.

Initial Assessment
Check for app-marketing-context.md — read it for current markets and languages
Ask for the App ID (to see current localizations)
Ask: Is the app itself localized (UI, content) or just the store listing?
Ask: Which markets are they considering?
Ask: Budget — professional translation or AI-assisted?
Market Prioritization
Tier 1 Markets (highest ROI for most apps)
Market	Language	App Store Code	Notes
United States	English	en-US	Largest market
United Kingdom	English	en-GB	Easy win if US is done
Germany	German	de-DE	Largest EU market
Japan	Japanese	ja	High ARPU, competitive
France	French	fr-FR	Large EU market
South Korea	Korean	ko	High smartphone penetration
China	Simplified Chinese	zh-Hans	Massive but complex (needs ICP)
Brazil	Portuguese	pt-BR	Largest LATAM market
Canada	English/French	en-CA/fr-CA	Easy win
Australia	English	en-AU	Easy win
Tier 2 Markets (good potential)

Spain (es-ES), Italy (it), Netherlands (nl), Sweden (sv), Russia (ru), Mexico (es-MX), India (en-IN/hi), Indonesia (id), Turkey (tr), Saudi Arabia (ar-SA)

How to Choose

Evaluate each market on:

Factor	Weight	How to assess
Market size	30%	iPhone user base in country
Competition	25%	How many localized competitors?
Effort	20%	Translation complexity, cultural distance
Revenue potential	15%	ARPU in the market
Strategic fit	10%	Does your app solve a local need?
Localization Checklist
Metadata Localization

For each target market:

 Title (30 chars) — Localized with market-specific keywords
 Subtitle (30 chars) — Localized with local keywords
 Keyword field (100 chars) — Completely new research per market
 Description (4000 chars) — Translated and culturally adapted
 Promotional text (170 chars) — Localized for local events/seasons
 What's New — Translated for each update
 Screenshots — Text overlays translated, culturally appropriate imagery
 App Preview Video — Subtitles or localized version
Critical: Keywords Are NOT Translations

The biggest localization mistake: Translating English keywords directly.

Instead:

Run keyword-research for each target market separately
Understand how locals search (different terms, different intent)
Use local autocomplete suggestions
Check what local competitors use in their metadata

Example:

English keyword: "budget tracker"
German: "Haushaltsbuch" (household book) — NOT "Budget Tracker"
Japanese: "家計簿" (household ledger) — completely different concept
Spanish: "control de gastos" (expense control) — different framing
Cultural Adaptation
Element	What to check
Screenshots	Currency symbols, date formats, number formats
Colors	Cultural color associations (red = luck in China, danger in West)
Imagery	Diverse representation, culturally appropriate
Tone	Formal vs informal varies by culture
Features	Highlight features relevant to local needs
Social proof	Use local press, local user counts if possible
Pricing	Local pricing expectations (purchasing power parity)
Localization Workflow
Phase 1: Research (per market)
Analyze top 10 apps in your category in the target market
Run keyword research with local seed terms
Identify local competitors and their positioning
Understand local App Store trends
Phase 2: Translation & Adaptation

For metadata (title, subtitle, keywords):

Use native speakers with ASO knowledge (not just translators)
Provide context: "This is an App Store title, must include [keyword]"
Review with keyword data — does the translation include high-volume terms?

For description:

Professional translation with cultural adaptation
Not word-for-word — adapt examples, references, humor
Maintain the same persuasive structure

For screenshots:

Translate text overlays
Adjust UI language if app is localized
Consider local design preferences
Phase 3: Launch & Monitor
Submit localized metadata
Monitor keyword rankings in each market (weekly)
Track conversion rate by country
Iterate based on performance data
Output Format
Localization Plan

For each recommended market:

## [Country] — [Language]

Priority: [High/Medium/Low]
Estimated effort: [hours/days]
Expected impact: [download increase estimate]

Keywords (top 10):
| Keyword | Volume | Difficulty | English equivalent |
|---------|--------|------------|-------------------|

Metadata:
- Title: [localized title] ([X]/30 chars)
- Subtitle: [localized subtitle] ([X]/30 chars)
- Keywords: [localized keyword field] ([X]/100 chars)

Cultural notes:
- [specific adaptations needed]

Market Prioritization Matrix
Market	Size	Competition	Effort	Revenue	Score	Priority
Related Skills
keyword-research — Run for each target market
metadata-optimization — Write localized metadata
screenshot-optimization — Localize screenshot designs
competitor-analysis — Analyze local competitors
Weekly Installs
1.0K
Repository
eronred/aso-skills
GitHub Stars
1.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn