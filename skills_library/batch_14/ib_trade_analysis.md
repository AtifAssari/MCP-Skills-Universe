---
title: ib_trade-analysis
url: https://skills.sh/crtvrffnrt/skills/ib_trade-analysis
---

# ib_trade-analysis

skills/crtvrffnrt/skills/ib_trade-analysis
ib_trade-analysis
Installation
$ npx skills add https://github.com/crtvrffnrt/skills --skill ib_trade-analysis
SKILL.md
Skill: ib_trade-analysis
Purpose

This skill generates a high-conviction, 8-day directional forecast score (-100 to +100) for a curated universe of AI infrastructure and platform stocks. It fuses OSINT intelligence with recent price structure and relative strength.

Core Mandates
Asymmetric Probability Only: Do not trade "good" stocks. Trade when the next 8-day probability distribution is asymmetric and catalyst-driven.
AI-Supercycle Focus: Prioritize GPU/accelerator stack (NVDA, AMD), foundry (TSM), and hyperscalers (MSFT, GOOG, AMZN).
8-Day Window: All forecasts and trades are designed for a 24-hour to 8-day horizon.
1. Forecast Engine (Score: -100 to +100)

Every Monday (U.S. Open), generate a score based on these weights:

50% OSINT Catalyst: Measure the strength of recent AI-related news, capex changes, supply chain wins, or regulatory headwinds.
25% Price Structure (8-Day): Analyze only the last 8 trading days. Focus on higher highs/lows, daily closes, and volume.
15% Relative Strength: Compare the stock against the NASDAQ-100 and its sector peers.
10% Event/Risk: Factor in earnings, conferences, and macro shocks.
2. Universe Tiers
Tier A (Momentum): NVDA, TSM, AVGO, MU, AMD, ORCL (Primary longs).
Tier B (Platforms): MSFT, GOOG, AMZN (Tactical longs/shorts).
Tier C (Special Sit): INTC, ASML (High uncertainty/tactical).
3. Directional Bias Rules
Long Bias: Score >= +35, OSINT > 0. (Strongest deployment if Score >= +60).
Short Bias: Score <= -35, OSINT < 0. (Strongest conviction if Score <= -60).
No Trade: Score between -34 and +34.
4. Instrument Selection Guidance
Long Stock: Bullish conviction + direct exposure desired.
Short Stock: Bearish conviction + defined catalyst.
Options Spreads: Bullish/Bearish conviction + high volatility or defined risk requirement.
Cash-Secured Puts: Neutral-to-Bullish + desired entry at lower levels.
5. Entry & Exit Logic
Entry: Breakout continuation or bullish pullbacks (for Longs). Failed rallies or breakdowns (for Shorts).
Time Exit: Close or reassess after 8 trading days.
Thesis Exit: Exit immediately if the OSINT flow invalidates the original catalyst.
Price Exit: Stop loss (4-6% for stock), profit-taking (40-60% of max spread value).
6. Target Forecast Output (JSON/YAML)

Every analysis must produce:

ticker: Stock symbol.
forecast_score: Numerical score (-100 to +100).
catalyst_summary: Concise description of the driving news/event.
price_structure: bullish, bearish, or neutral.
relative_strength: strong, weak, or neutral.
recommended_action: long_stock, bull_call_spread, short_stock, no_trade, etc.
conviction: high, medium, or low.
Weekly Installs
8
Repository
crtvrffnrt/skills
First Seen
Mar 14, 2026