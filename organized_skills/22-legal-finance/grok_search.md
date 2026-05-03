---
rating: ⭐⭐⭐
title: grok-search
url: https://skills.sh/dianel555/dskills/grok-search
---

# grok-search

skills/dianel555/dskills/grok-search
grok-search
Installation
$ npx skills add https://github.com/dianel555/dskills --skill grok-search
SKILL.md
Grok Search

Enhanced web search via Grok API. Standalone CLI only (no MCP dependency).

Execution Methods

Run scripts/groksearch_cli.py via Bash:

# Prerequisites: pip install httpx tenacity
# Environment: GROK_API_URL, GROK_API_KEY

# Web search
python scripts/groksearch_cli.py web_search --query "search terms" [--platform "GitHub"] [--min-results 3] [--max-results 10]

# Fetch webpage
python scripts/groksearch_cli.py web_fetch --url "https://..." [--out file.md]

# Check config
python scripts/groksearch_cli.py get_config_info [--no-test]

# Switch model
python scripts/groksearch_cli.py switch_model --model "grok-2-latest"

# Toggle built-in tools
python scripts/groksearch_cli.py toggle_builtin_tools --action on|off|status [--root /path/to/project]

Tool Routing Policy
Forced Replacement Rules
Scenario	Disabled	Force Use
Web Search	WebSearch	CLI web_search
Web Fetch	WebFetch	CLI web_fetch
Tool Capability Matrix
Tool	Parameters	Output
web_search	query(required), platform/min_results/max_results(optional)	[{title,url,description}]
web_fetch	url(required), out(optional)	Structured Markdown
get_config_info	no_test(optional)	{api_url,status,connection_test}
switch_model	model(required)	{previous_model,current_model}
toggle_builtin_tools	action(on/off/status), root(optional)	{blocked,deny_list}
Search Workflow
Phase 1: Query Construction
Intent Recognition: Broad search → web_search | Deep retrieval → web_fetch
Parameter Optimization: Set platform for specific sources, adjust result counts
Phase 2: Search Execution
Start with web_search for structured summaries
Use web_fetch on key URLs if summaries insufficient
Retry with adjusted query if first round unsatisfactory
Phase 3: Result Synthesis
Cross-reference multiple sources
Must annotate source and date for time-sensitive info
Must include source URLs: Title [<sup>1</sup>](URL)
Error Handling
Error	Recovery
Connection Failure	Run get_config_info, verify API URL/Key
No Results	Broaden search terms
Fetch Timeout	Try alternative sources
Anti-Patterns
Prohibited	Correct
No source citation	Include Source [<sup>1</sup>](URL)
Give up after one failure	Retry at least once
Use built-in WebSearch/WebFetch	Use GrokSearch tools/CLI
Weekly Installs
17
Repository
dianel555/dskills
GitHub Stars
64
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn