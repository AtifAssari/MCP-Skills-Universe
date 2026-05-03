---
title: exchange-rate
url: https://skills.sh/qverisai/open-qveris-skills/exchange-rate
---

# exchange-rate

skills/qverisai/open-qveris-skills/exchange-rate
exchange-rate
Installation
$ npx skills add https://github.com/qverisai/open-qveris-skills --skill exchange-rate
SKILL.md
Exchange Rate

Real-time currency exchange rate and conversion using QVeris tools.

What This Skill Does

Exchange Rate provides:

Rate lookup – Current exchange rate between two currencies (e.g. USD/EUR, CNY/JPY).
Amount conversion – Convert an amount from one currency to another at current rates.

Supported via QVeris: forex and common fiat pairs; optional historical date for rate/conversion when the tool supports it.

Key Advantages
Uses only QVeris API: search for tools by capability, then execute; no hardcoded provider list.
Fallback across providers (e.g. Alpha Vantage, Twelve Data) when one fails or is unavailable.
Same credential as other skills: QVERIS_API_KEY only.
Read-only, no side effects; suitable for travel, trade, and reporting.
Core Workflow
Parse user intent: rate (from_currency, to_currency) or convert (from_currency, to_currency, amount).
Search QVeris for tools: e.g. "currency exchange rate real-time", "currency conversion".
Rank results by success_rate, latency, and parameter fit (rate vs conversion).
Build request parameters: for rate use from_currency/to_currency or symbol (e.g. EUR/USD); for conversion add amount.
Execute chosen tool with 5s timeout; on failure try next candidate.
Return formatted rate and/or converted amount (markdown or JSON).
Command Surface

Primary script: scripts/exchange_rate.mjs

Get rate only:
node scripts/exchange_rate.mjs rate --from USD --to EUR
node scripts/exchange_rate.mjs rate --from CNY --to USD
Convert amount:
node scripts/exchange_rate.mjs convert --from USD --to JPY --amount 1000
node scripts/exchange_rate.mjs convert --from EUR --to GBP --amount 500

Optional: --date YYYY-MM-DD for historical rate/conversion when the tool supports it; --format json for machine-readable output.

Safety and Disclosure
Uses only QVERIS_API_KEY; no other secrets.
Calls only QVeris over HTTPS; no package install or arbitrary commands.
Output is for reference only; not financial or contractual advice.
Weekly Installs
73
Repository
qverisai/open-q…s-skills
GitHub Stars
17
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass