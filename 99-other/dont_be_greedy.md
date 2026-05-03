---
title: dont-be-greedy
url: https://skills.sh/elliotjlt/claude-skill-potions/dont-be-greedy
---

# dont-be-greedy

skills/elliotjlt/claude-skill-potions/dont-be-greedy
dont-be-greedy
Installation
$ npx skills add https://github.com/elliotjlt/claude-skill-potions --skill dont-be-greedy
SKILL.md
Don't Be Greedy
Instructions
Step 1: Estimate Token Cost

Before loading ANY data file:

python scripts/estimate_size.py "<file_path>"


This returns byte count and estimated token count.

Step 2: Apply Strategy Based on Size
Estimated Tokens	Action
< 10,000	Run quick inspection, load directly
10,000 - 30,000	Run quick inspection, consider filtering
> 30,000	Chunk and summarize before loading
Step 3: Execute Appropriate Workflow
python scripts/quick_inspect.py "<file_path>"


Return stats and load file directly.

python scripts/chunker.py "<file_path>"
python scripts/summarize.py "<chunk_file>"


Return overall summary + per-chunk summaries + safe preview of first rows.

Step 4: Return Structured Output

Always provide:

Overall summary (1-3 paragraphs)
Safe preview (first N rows/lines)
Recommendation for next steps
Chunk information if file was split
NEVER
Load files without running estimate_size.py first
Use cat on unknown or large files
Ask "What would you like me to do with this file?"
Wait for user direction before acting on file uploads
Load raw data exceeding 30k tokens into context
ALWAYS
Run size estimation before any file operation
Chunk files over 30k tokens automatically
Provide a safe preview even for large files
Act immediately when a data file is detected
Be thorough in first response with summary + preview + recommendation
Examples
Example 1: User uploads large CSV

Input: User says "Analyze this sales data" and uploads a 50MB CSV file

Workflow:

Run scripts/estimate_size.py sales.csv → Output: bytes=52428800 (50.0MB) tokens=13107200
Way over 30k tokens. Run scripts/chunker.py sales.csv → Creates 6500+ chunks
Run scripts/summarize.py on representative chunks
Return:
Overall summary of data structure and content
Safe preview showing first 10 rows
Recommendation: "Data contains 1M rows of sales transactions. I've chunked it for processing. Want me to analyze specific columns or date ranges?"
Example 2: User references small JSON config

Input: User asks "Check my config.json for issues"

Workflow:

Run scripts/estimate_size.py config.json → Output: bytes=2048 (2.0KB) tokens=512
Under 10k tokens. Run scripts/quick_inspect.py config.json
Load file directly and analyze
Return: Full analysis with any issues found
Example 3: User uploads medium log file

Input: User uploads a 500KB application.log

Workflow:

Run scripts/estimate_size.py application.log → Output: bytes=512000 (500.0KB) tokens=128000
Over 30k tokens. Run scripts/chunker.py application.log
Summarize chunks focusing on errors and warnings
Return:
Summary of log timespan and key events
Count of errors, warnings, info messages
Safe preview of recent entries
Recommendation for focused analysis
Weekly Installs
8
Repository
elliotjlt/claud…-potions
GitHub Stars
55
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn