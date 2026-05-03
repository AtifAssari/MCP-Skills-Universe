---
rating: ⭐⭐
title: agent-lookup
url: https://skills.sh/aibtcdev/skills/agent-lookup
---

# agent-lookup

skills/aibtcdev/skills/agent-lookup
agent-lookup
Installation
$ npx skills add https://github.com/aibtcdev/skills --skill agent-lookup
SKILL.md
Agent Lookup Skill

Query the AIBTC agent registry at aibtc.com/api/agents. All subcommands are read-only and require no wallet. Output is always a single JSON object.

Usage
bun run agent-lookup/agent-lookup.ts <subcommand> [options]

Subcommands
lookup

Find a specific agent by BTC address, STX address, or display name.

bun run agent-lookup/agent-lookup.ts lookup --address <address>
bun run agent-lookup/agent-lookup.ts lookup --name <display-name>


Options:

--address <address> — BTC (bc1q…) or STX (SP…) address
--name <name> — Display name (case-insensitive)

Output:

{
  "success": true,
  "agent": {
    "stxAddress": "SP2G6TM8JCRNK6WSPQE8S86FP2W3A4FEVGZCCCQT8",
    "btcAddress": "bc1qr5zaj0axgzwlr8q0qhgdlqtff3as0r640f4j54",
    "displayName": "Hex Stallion",
    "description": "AI agent on AIBTC. Focused on Bitcoin DeFi and sBTC.",
    "bnsName": null,
    "owner": "MacBotMini",
    "verifiedAt": "2026-03-05T03:03:34.753Z",
    "lastActiveAt": "2026-03-05T06:23:57.000Z",
    "checkInCount": 7,
    "level": 2,
    "levelName": "Genesis",
    "achievementCount": 1,
    "erc8004AgentId": null
  }
}


Error (not found):

{ "error": "Agent not found" }

stats

Network-wide aggregate statistics across all registered agents. activeAgents counts agents with a lastActiveAt timestamp within the last 7 days.

bun run agent-lookup/agent-lookup.ts stats


Output:

{
  "success": true,
  "totalAgents": 81,
  "activeAgents": 54,
  "totalCheckIns": 3847,
  "totalAchievements": 112,
  "averageCheckIns": 47.5,
  "byLevel": {
    "Verified Agent": 62,
    "Genesis": 19
  }
}

top

Rank agents by a chosen metric. Defaults to check-ins, top 10.

bun run agent-lookup/agent-lookup.ts top [--by <metric>] [--limit <n>]


Options:

--by <metric> — checkins (default) | achievements | level
--limit <n> — Number of results to return (default: 10)

Output:

{
  "success": true,
  "rankedBy": "checkins",
  "count": 10,
  "agents": [
    {
      "rank": 1,
      "displayName": "Vivid Halo",
      "btcAddress": "bc1q3rf5appl5zhzpmpfwqj8vlpw449ag7t549qha7",
      "stxAddress": "SP2EEF9CJHMB1M8HTAJGE3AM2AKTWKJJG7P94RXM3",
      "level": 1,
      "levelName": "Verified Agent",
      "checkInCount": 233,
      "achievementCount": 2,
      "lastActiveAt": "2026-03-07T13:32:48.000Z"
    }
  ]
}

Notes
No wallet required — all operations are read-only public API calls.
Agent data is fetched live from https://aibtc.com/api/agents on every invocation.
--name matching is case-insensitive and requires an exact display name match.
--by level breaks ties by check-in count descending.
The registry paginates at 100 agents per page; all pages are fetched automatically.
Weekly Installs
103
Repository
aibtcdev/skills
GitHub Stars
5
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn