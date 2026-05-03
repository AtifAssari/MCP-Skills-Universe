---
rating: ⭐⭐⭐
title: earnings-trade-analyzer
url: https://skills.sh/tradermonty/claude-trading-skills/earnings-trade-analyzer
---

# earnings-trade-analyzer

skills/tradermonty/claude-trading-skills/earnings-trade-analyzer
earnings-trade-analyzer
Installation
$ npx skills add https://github.com/tradermonty/claude-trading-skills --skill earnings-trade-analyzer
SKILL.md
Earnings Trade Analyzer - Post-Earnings 5-Factor Scoring

Analyze recent post-earnings stocks using a 5-factor weighted scoring system to identify the strongest earnings reactions for potential momentum trades.

When to Use
User asks for post-earnings trade analysis or earnings gap screening
User wants to find the best recent earnings reactions
User requests earnings momentum scoring or grading
User asks about post-earnings accumulation day (PEAD) candidates
Prerequisites
FMP API key (set FMP_API_KEY environment variable or pass --api-key)
Free tier (250 calls/day) is sufficient for default screening (lookback 2 days, top 20)
Paid tier recommended for larger lookback windows or full screening
Workflow
Step 1: Run the Earnings Trade Analyzer

Execute the analyzer script:

# Default: last 2 days of earnings, top 20 results
python3 skills/earnings-trade-analyzer/scripts/analyze_earnings_trades.py --output-dir reports/

# Custom lookback and market cap filter
python3 skills/earnings-trade-analyzer/scripts/analyze_earnings_trades.py \
  --lookback-days 5 \
  --min-market-cap 1000000000 \
  --top 30 \
  --output-dir reports/

# With entry quality filter
python3 skills/earnings-trade-analyzer/scripts/analyze_earnings_trades.py \
  --apply-entry-filter \
  --output-dir reports/

Step 2: Review Results
Read the generated JSON and Markdown reports
Load references/scoring_methodology.md for scoring interpretation context
Focus on Grade A and B stocks for actionable setups
Step 3: Present Analysis

For each top candidate, present:

Composite score and letter grade (A/B/C/D)
Earnings gap size and direction
Pre-earnings 20-day trend
Volume ratio (20-day vs 60-day average)
Position relative to 200-day and 50-day moving averages
Weakest and strongest scoring components
Step 4: Provide Actionable Guidance

Based on grades:

Grade A (85+): Strong earnings reaction with institutional accumulation - consider entry
Grade B (70-84): Good earnings reaction worth monitoring - wait for pullback or confirmation
Grade C (55-69): Mixed signals - use caution, additional analysis needed
Grade D (<55): Weak setup - avoid or wait for better conditions
Output
earnings_trade_analyzer_YYYY-MM-DD_HHMMSS.json - Structured results with schema_version "1.0"
earnings_trade_analyzer_YYYY-MM-DD_HHMMSS.md - Human-readable report with tables
Resources
references/scoring_methodology.md - 5-factor scoring system, grade thresholds, and entry quality filter rules
Weekly Installs
263
Repository
tradermonty/cla…g-skills
GitHub Stars
1.2K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass