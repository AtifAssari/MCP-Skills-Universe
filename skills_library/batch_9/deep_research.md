---
title: deep-research
url: https://skills.sh/sanjay3290/ai-skills/deep-research
---

# deep-research

skills/sanjay3290/ai-skills/deep-research
deep-research
Installation
$ npx skills add https://github.com/sanjay3290/ai-skills --skill deep-research
SKILL.md
Gemini Deep Research Skill

Run autonomous research tasks that plan, search, read, and synthesize information into comprehensive reports.

Requirements
Python 3.8+
httpx: pip install -r requirements.txt
GEMINI_API_KEY environment variable
Setup
Get a Gemini API key from Google AI Studio
Set the environment variable:
export GEMINI_API_KEY=your-api-key-here

Or create a .env file in the skill directory.
Usage
Start a research task
python3 scripts/research.py --query "Research the history of Kubernetes"

With structured output format
python3 scripts/research.py --query "Compare Python web frameworks" \
  --format "1. Executive Summary\n2. Comparison Table\n3. Recommendations"

Stream progress in real-time
python3 scripts/research.py --query "Analyze EV battery market" --stream

Start without waiting
python3 scripts/research.py --query "Research topic" --no-wait

Check status of running research
python3 scripts/research.py --status <interaction_id>

Wait for completion
python3 scripts/research.py --wait <interaction_id>

Continue from previous research
python3 scripts/research.py --query "Elaborate on point 2" --continue <interaction_id>

List recent research
python3 scripts/research.py --list

Output Formats
Default: Human-readable markdown report
JSON (--json): Structured data for programmatic use
Raw (--raw): Unprocessed API response
Cost & Time
Metric	Value
Time	2-10 minutes per task
Cost	$2-5 per task (varies by complexity)
Token usage	~250k-900k input, ~60k-80k output
Best Use Cases
Market analysis and competitive landscaping
Technical literature reviews
Due diligence research
Historical research and timelines
Comparative analysis (frameworks, products, technologies)
Workflow
User requests research → Run --query "..."
Inform user of estimated time (2-10 minutes)
Monitor with --stream or poll with --status
Return formatted results
Use --continue for follow-up questions
Exit Codes
0: Success
1: Error (API error, config issue, timeout)
130: Cancelled by user (Ctrl+C)
Weekly Installs
279
Repository
sanjay3290/ai-skills
GitHub Stars
246
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn