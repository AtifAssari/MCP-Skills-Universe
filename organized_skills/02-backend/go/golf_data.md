---
rating: ⭐⭐⭐
title: golf-data
url: https://skills.sh/machina-sports/sports-skills/golf-data
---

# golf-data

skills/machina-sports/sports-skills/golf-data
golf-data
Installation
$ npx skills add https://github.com/machina-sports/sports-skills --skill golf-data
SKILL.md
Golf Data (PGA / LPGA / DP World Tour)

Before writing queries, consult references/api-reference.md for endpoints, player IDs, and score formats.

Setup

Before first use, check if the CLI is available:

which sports-skills || pip install sports-skills


If pip install fails with a Python version error, the package requires Python 3.10+. Find a compatible Python:

python3 --version  # check version
# If < 3.10, try: python3.12 -m pip install sports-skills
# On macOS with Homebrew: /opt/homebrew/bin/python3.12 -m pip install sports-skills


No API keys required.

Quick Start

Prefer the CLI — it avoids Python import path issues:

sports-skills golf get_leaderboard --tour=pga
sports-skills golf get_schedule --tour=pga --year=2026
sports-skills golf get_news --tour=pga

CRITICAL: Before Any Query

CRITICAL: Before calling any data endpoint, verify:

The tour parameter is specified (pga, lpga, or eur) — there is no default tour.
Player IDs are obtained from get_leaderboard results or ESPN golf URLs — never guessed.
Important: Golf is Not a Team Sport
Tournaments, not games: Each event is a multi-day tournament (typically 4 rounds, Thu–Sun).
Individual athletes: The leaderboard has 72–147 individual golfers, not 2 teams.
Score relative to par: Scores are strings like "-17", "E" (even), "+2" — not point totals.
One event per week: Unlike team sports, golf has one tournament per week per tour.
No standings endpoint: FedEx Cup standings are not available via this API.
The tour Parameter

Most commands require --tour=pga, --tour=lpga, or --tour=eur:

PGA: PGA Tour (men's professional golf)
LPGA: LPGA Tour (women's professional golf)
EUR: DP World Tour (formerly European Tour)

If the user doesn't specify, default to pga. If they say "women's golf" or "LPGA", use lpga. If they mention the European Tour or DP World Tour, use eur.

Commands
Command	Description
get_leaderboard	Current tournament leaderboard with all golfer scores
get_schedule	Full season tournament schedule
get_player_info	Individual golfer profile
get_player_overview	Detailed overview with season stats, rankings, recent results
get_scorecard	Hole-by-hole scorecard for a golfer
get_news	Golf news articles

See references/api-reference.md for full parameter lists and return shapes.

Examples

Example 1: Current leaderboard User says: "What's the PGA leaderboard right now?" Actions:

Call get_leaderboard(tour="pga") Result: Current tournament leaderboard sorted by position with each golfer's score and round-by-round breakdown

Example 2: Season schedule User says: "Show me the LPGA schedule for 2026" Actions:

Call get_schedule(tour="lpga", year=2026) Result: Full LPGA tournament calendar with names, dates, and venues

Example 3: Golfer profile User says: "Tell me about Scottie Scheffler" Actions:

Call get_player_info(player_id="9478", tour="pga") Result: Scheffler's profile with age, nationality, height/weight, turned pro year

Example 4: Upcoming major User says: "When is the Masters this year?" Actions:

Derive year from currentDate
Call get_schedule(tour="pga", year=<derived_year>)
Search results for "Masters Tournament" Result: Masters date, course (Augusta National), and tournament ID

Example 5: Player scorecard User says: "Show me Scottie Scheffler's scorecard" Actions:

Call get_scorecard(tour="pga", player_id="9478") Result: Hole-by-hole scores for each completed round with strokes and score-to-par

Example 6: Player season form User says: "How has Rory McIlroy been playing this season?" Actions:

Call get_player_overview(player_id="3470", tour="pga") Result: Season stats (scoring average, earnings, wins, top-10s), world ranking, and recent results
Commands that DO NOT exist — never call these
get_tournament_results — does not exist. Use get_leaderboard for current/recent tournament scores.
get_rankings — does not exist. FedEx Cup/world rankings are not available via this API. Use get_player_overview for individual rankings.
get_odds / get_betting_odds — not available. For prediction market odds, use the polymarket or kalshi skill.
search_player — does not exist. Use get_leaderboard to find player IDs from the current field.

If a command is not listed in the Commands table above, it does not exist.

Error Handling

When a command fails, do not surface raw errors to the user. Instead:

If no active tournament, tell the user and suggest checking the schedule
If a player ID is wrong, suggest using get_leaderboard to find current player IDs
Only report failure with a clean message after exhausting alternatives
Troubleshooting

Error: sports-skills command not found Cause: Package not installed Solution: Run pip install sports-skills

Error: No active tournament on leaderboard Cause: Golf tournaments run Thursday–Sunday; between events the leaderboard may show no active tournament Solution: Call get_schedule(tour="pga") to find the next upcoming event

Error: Limited round data — scores are empty Cause: Before a tournament starts, round scores will be empty. During the tournament, only completed rounds have scores. Solution: Check get_leaderboard for tournament status and current round; wait for rounds to complete

Error: Player not found by ID Cause: Player ID is incorrect or the player is not in the current tournament field Solution: Get player IDs from get_leaderboard results, or look up ESPN golf URLs (espn.com/golf/player/_/id/<id>/player-name)

Weekly Installs
169
Repository
machina-sports/…s-skills
GitHub Stars
90
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn