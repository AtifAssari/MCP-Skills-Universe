---
title: skywork search
url: https://skills.sh/skyworkai/skywork-skills/skywork-search
---

# skywork search

skills/skyworkai/skywork-skills/Skywork Search
Skywork Search
Installation
$ npx skills add https://github.com/skyworkai/skywork-skills --skill 'Skywork Search'
SKILL.md
Web Search Skill

Search the web for real-time information via the Skywork search API. This skill lets you run up to 3 queries in a single invocation and returns structured results with source URLs and content snippets.

When to use
The user asks you to research a topic or find current information
You need up-to-date facts, statistics, or news to answer a question
Another task (writing a report, creating a PPT, drafting a document) needs web research as a preliminary step
The user explicitly asks to search or look something up
Prerequisites
API Key Configuration (Required First)

This skill requires a SKYWORK_API_KEY to be configured in OpenClaw.

If you don't have an API key yet, please visit: https://skywork.ai

For detailed setup instructions, see: references/apikey-fetch.md

How to use

Run the bundled script from this skill's scripts/ directory:

python3 <skill-path>/scripts/web_search.py "query1" ["query2"] ["query3"]

Pass 1–3 search queries as positional arguments
Results are saved to individual text files in a temporary directory
The script prints the file paths to stdout so you can read them
Crafting good queries

Search quality depends heavily on query phrasing. A few tips:

Be specific: "Tesla Q4 2025 revenue" works better than "Tesla financials"
Use natural language: The API handles full questions well — "What is the current population of Tokyo?" is fine
Split broad topics: If the user wants a comprehensive overview, break it into 2–3 focused queries rather than one vague one
Include time context when relevant: "best Python web frameworks 2026" rather than just "best Python web frameworks"
Reading results

After running the script, read the output files. Each file contains:

query: <the original query>

[result-1] <source URL>
<content snippet>

[result-2] <source URL>
<content snippet>
...


Synthesize the results into a clear answer for the user. Always cite sources when presenting factual information — include the URLs from the results so the user can verify.

Example workflow

User asks: "What are the latest developments in quantum computing?"

Run the search with focused queries:
python3 <skill-path>/scripts/web_search.py \
  "quantum computing breakthroughs 2026" \
  "quantum computing industry news latest"

Read the result files
Synthesize findings into a clear, sourced summary for the user
Limitations
Maximum 3 queries per invocation (the script caps it)
Each query has a 30-second timeout
Results depend on the Skywork search API availability
Weekly Installs
–
Repository
skyworkai/skywork-skills
GitHub Stars
125
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn