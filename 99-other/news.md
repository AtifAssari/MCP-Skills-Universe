---
title: news
url: https://skills.sh/alsk1992/cloddsbot/news
---

# news

skills/alsk1992/cloddsbot/news
news
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill news
SKILL.md
News Skill

Track news that affects prediction markets and correlate with price movements.

Commands
Recent News
/news
/news trump
/news fed

Market-Specific News
/news for "Trump 2028"

News Alerts
/news alert trump
/news alert "fed rate"

News Sources
Twitter/X Accounts
@polyaborama - Polymarket updates
@Kalshi - Kalshi official
@MetaculusHQ - Metaculus updates
@NateSilver538 - Political analysis
@business - Bloomberg breaking
RSS Feeds
Reuters Politics
AP News
Federal Reserve Press
POLITICO
Correlation Features
Auto-Matching

When news breaks, automatically identify affected markets:

"Trump indicted" → Trump election markets
"Fed signals pause" → Rate cut markets
"Player injured" → Sports markets
Price Impact

Track how news affects market prices:

News timestamp vs price movement
Volume spike detection
Sentiment analysis
Examples

User: "What's moving markets right now?" → Show recent news with correlated market moves

User: "Why did Trump drop 5%?" → Find news from past hour matching "Trump" → Correlate with price action

User: "Alert me to any Fed news" → Create news alert for "fed" OR "fomc" OR "powell"

Output Format
📰 MARKET-MOVING NEWS

🔴 HIGH IMPACT (5 min ago)
Reuters: "Trump hints at not running in 2028"

Affected Markets:
• Trump 2028 (Poly): 47¢ → 42¢ (-10.6%)
• Trump 2024 (Kalshi): 52¢ → 54¢ (+3.8%)
• DeSantis 2028 (Poly): 12¢ → 18¢ (+50%)

Volume Spike: 3.2x normal

──────────────────────────

🟡 MEDIUM IMPACT (23 min ago)
Bloomberg: "Fed officials signal data-dependent approach"

Affected Markets:
• Fed March Cut (Poly): 23¢ → 25¢ (+8.7%)
• Fed May Cut (Kalshi): 45¢ → 47¢ (+4.4%)

Weekly Installs
13
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn