---
title: vc-info
url: https://skills.sh/mnfst/vc-info/vc-info
---

# vc-info

skills/mnfst/vc-info/vc-info
vc-info
Installation
$ npx skills add https://github.com/mnfst/vc-info --skill vc-info
SKILL.md
VC Info

Produce a concise VC firm briefing from web research. Max 2 search rounds.

Research

Round 1 — run all in parallel:

{name} venture capital fund size AUM overview
{name} VC portfolio companies investments
{name} venture capital partners team
{name} VC investment thesis verticals
site:crunchbase.com/organization {name}
site:linkedin.com {name} venture capital partners
Fetch the firm's website homepage, /team, /portfolio, and /about pages

Round 2 (only if critical gaps): Max 3 targeted follow-ups for missing fund size, partner LinkedIn URLs, or portfolio data.

Rules
Never fabricate. Write "Not disclosed" for missing fields.
Use search snippets when sites block fetching (LinkedIn, Crunchbase).
LinkedIn links: Extract actual linkedin.com/in/... URLs from search results. Never guess. Omit if not found.
Cross-reference fund size across 2+ sources when possible.
Prefer sources from last 12 months.
List at least 5 portfolio companies, prioritizing well-known ones.
Include all GPs and MDs; limit other team to notable members.
Output

Read references/template.md for the exact output structure. Sections:

TLDR — 2-3 sentences + key facts table
Thesis & Focus — philosophy, sweet spot, geo, what they look for
Team — background + LinkedIn
Funds — table of funds with year, size, status
Portfolio — table with vertical, stage, status
Access & Process — how to get in, speed, founder-friendliness
Value Add & Reputation — beyond capital + founder sentiment
Recent Activity — latest fund, deals, exits
Quick Take — best fit / skip if

Keep sentences short. No filler. If data unavailable, say so.

Edge Cases
Micro VC / solo GP: Single partner, smaller portfolio, may lack fund history.
Corporate VC: Note parent company, strategic vs financial, strings attached.
Multi-stage / mega fund: Clarify which stage team is relevant.
Angel group / syndicate: Note if formal fund or deal-by-deal.
Not found: Tell the user directly.
Weekly Installs
13
Repository
mnfst/vc-info
GitHub Stars
4
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn