---
title: solo-swarm
url: https://skills.sh/fortunto2/solo-factory/solo-swarm
---

# solo-swarm

skills/fortunto2/solo-factory/solo-swarm
solo-swarm
Installation
$ npx skills add https://github.com/fortunto2/solo-factory --skill solo-swarm
SKILL.md
/swarm

Create an agent team to research "$ARGUMENTS" from multiple perspectives in parallel.

Team Structure

Spawn 3 teammates, each with a distinct research focus:

1. Market Researcher

Focus: competitors, market size, pricing models, business models.

Search for direct and indirect competitors
Find market reports with TAM/SAM/SOM figures
Analyze pricing strategies and monetization
Identify market gaps and opportunities
Check Product Hunt, G2, Capterra for existing products
2. User Researcher

Focus: pain points, user sentiment, feature requests.

Search Reddit for user discussions (site:reddit.com <query> via WebSearch, or MCP web_search if available)
Search Hacker News for tech community opinions (site:news.ycombinator.com)
If MCP session_search available: check if this idea was researched before in past sessions
Find app reviews and ratings
Extract direct user quotes about frustrations
Identify unmet needs and feature requests
3. Technical Analyst

Focus: feasibility, tech stack, existing solutions, implementation complexity.

Search GitHub for open-source alternatives (site:github.com <query>)
Evaluate tech stack options
If MCP project_info available: check existing projects for reusable code
If MCP codegraph_explain available: get architecture overview of similar existing projects
If MCP codegraph_query available: find shared packages across projects
If MCP project_code_search available: search for reusable patterns, services, infrastructure across existing projects
Assess implementation complexity and timeline
Search Backends

Teammates should use available search tools:

WebSearch (built-in) — broad discovery, market reports, always available
WebFetch — scrape specific URLs for details, always available
MCP web_search (if available) — additional search with engine routing
MCP kb_search (if available) — search local knowledge base for related research

Domain filtering: use site:github.com, site:reddit.com etc. for targeted results.

Coordination
Each teammate writes findings to a shared task list
Require plan approval before teammates start deep research
After all complete, synthesize findings into research.md
Use the research.md format from /research skill
Output

After team completes, the lead should:

Synthesize findings from all 3 teammates
Write research.md to docs/ in the current project directory
Provide GO / NO-GO / PIVOT recommendation
Suggest next step: /validate <idea>
Common Issues
Agent team not available

Cause: CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS env var not set. Fix: Ensure .claude/settings.json has "env": {"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"}.

Teammates produce overlapping findings

Cause: Research areas not clearly separated. Fix: Each teammate has a distinct focus (market/users/tech). The lead synthesizes and deduplicates findings.

Web search returns limited results

Cause: No additional search backends configured. Fix: Teammates fall back to WebSearch (built-in) which is always available. For richer results with engine routing (Reddit, GitHub, YouTube), set up SearXNG (private, self-hosted, free) and configure solograph MCP.

Weekly Installs
32
Repository
fortunto2/solo-factory
GitHub Stars
15
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn