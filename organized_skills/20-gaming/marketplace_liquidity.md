---
rating: ⭐⭐
title: marketplace-liquidity
url: https://skills.sh/refoundai/lenny-skills/marketplace-liquidity
---

# marketplace-liquidity

skills/refoundai/lenny-skills/marketplace-liquidity
marketplace-liquidity
Installation
$ npx skills add https://github.com/refoundai/lenny-skills --skill marketplace-liquidity
Summary

Framework for diagnosing and fixing supply-demand imbalances in two-sided marketplaces.

Guides you through understanding your marketplace type, identifying whether you're supply-constrained or demand-constrained, and defining fill rate as your core liquidity metric
Emphasizes that liquidity is fundamentally about reliability: how often buyers find what they want and sellers find buyers
Highlights the "whac-a-mole" nature of marketplace management, requiring constant rebalancing of supply and demand across geographies and segments
Flags common mistakes like growing both sides equally, ignoring local fragmentation, and expanding before achieving density in a single market
SKILL.md
Marketplace Liquidity Management

Help the user build and manage marketplace liquidity using frameworks from 4 product leaders.

How to Help

When the user asks for help with marketplace liquidity:

Understand the marketplace type - Ask about their supply/demand dynamics, how fragmented the market is, and whether needs are uniform or heterogeneous
Diagnose the constraint - Determine if they're supply-constrained, demand-constrained, or facing a matching problem
Define liquidity metrics - Help them establish clear measures of marketplace reliability and fill rates
Design interventions - Guide them on where to focus to improve liquidity (geographic focus, supply acquisition, demand generation, matching quality)
Core Principles
Liquidity is how marketplaces win

Benjamin Lauzier: "Liquidity is how marketplaces win. It's this measure of your ability to match buyers and sellers efficiently." Focus on the core metric of how reliably you can connect supply with demand. This is the foundational metric that determines marketplace success or failure.

Liquidity = reliability of the marketplace

Dan Hockenmaier: "How reliable is the marketplace? If the consumer is looking for something or supplier is looking to sell something, how often can they do that thing they're trying to do?" Define liquidity as fill rate - the percentage of times buyers find what they want and sellers find buyers. Make this your number one metric.

Marketplace management is whac-a-mole

Ramesh Johari: "Marketplaces are a little bit like a game of whac-a-mole... a lot of marketplace management is moving attention and inventory around." Expect constant rebalancing between supply and demand across different segments and geographies. Build systems to reallocate attention and inventory dynamically.

No supply without demand, no demand without supply

Tim Holley: "If you've got supply without demand, then you don't really have a marketplace. If you've got demand and no supply to meet it, then you also don't have a marketplace." Watch for the "graduation problem" where successful sellers leave the platform. Use data to guide supply toward areas of unmet demand.

Questions to Help Users
"How do you define liquidity for your marketplace? What's your fill rate?"
"Are you currently supply-constrained or demand-constrained? Does this vary by geography or category?"
"How fragmented are the needs in your marketplace - are they uniform or highly heterogeneous?"
"What happens when you add more supply? Does it immediately get absorbed by demand?"
"Are you seeing a 'graduation problem' where successful suppliers leave your platform?"
Common Mistakes to Flag
Growing both sides equally - Usually one side is the constraint. Focus resources on the bottleneck
Ignoring geographic/category fragmentation - National liquidity metrics can hide severe local imbalances
Not measuring fill rate - Without a clear liquidity metric, you can't manage toward it
Over-expanding before reaching local density - It's better to be highly liquid in one market than illiquid across many
Deep Dive

For all 4 insights from 4 guests, see references/guest-insights.md

Related Skills
Measuring Product-Market Fit
Designing Growth Loops
Pricing Strategy
Retention & Engagement
Weekly Installs
980
Repository
refoundai/lenny-skills
GitHub Stars
744
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass