---
title: gemini
url: https://skills.sh/johnlindquist/claude/gemini
---

# gemini

skills/johnlindquist/claude/gemini
gemini
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill gemini
SKILL.md
Gemini AI Assistant

Leverage Google's Gemini Pro model with its 1M context window for research, analysis, and reasoning tasks.

Prerequisites

Install the Gemini CLI:

pip install google-generativeai


Set your API key:

export GEMINI_API_KEY=your_api_key


Get an API key at: https://makersuite.google.com/app/apikey

CLI Reference
Basic Usage
# Simple question
gemini -m pro "Your question here"

# With text output (no markdown)
gemini -m pro -o text "Your question"

# Disable extensions for programmatic use
gemini -m pro -o text -e "" "Your question"

# Pipe content as stdin
echo "content to analyze" | gemini -m pro -o text -e "" "Summarize this"
cat file.txt | gemini -m pro -o text -e "" "Analyze this code"

Common Operations
Research

Deep research with critical analysis:

gemini -m pro -o text -e "" "You are an expert research analyst. Research: [topic]. Provide specific facts, distinguish opinions from facts, note uncertainties, and give actionable insights."

Summarization
cat document.txt | gemini -m pro -o text -e "" "Summarize this content, focusing on: [focus area]"

Code Analysis
cat code.ts | gemini -m pro -o text -e "" "Analyze this code and answer: [question]"

Web Search with Synthesis
gemini -m pro -o text -e "" "Search and synthesize: [query]. Include specific facts, dates, and distinguish confirmed from speculative information."

Fact-Checking
gemini -m pro -o text -e "" "Fact-check this claim: [claim]. State true/false/partial, cite sources, note context."

Step-by-Step Reasoning
gemini -m pro -o text -e "" "Think through this problem step by step: [problem]. Constraints: [constraints]. Provide reasoning and conclusion."

Data Extraction
cat content.txt | gemini -m pro -o text -e "" "Extract [what to extract] from this content. Format as [json/list/table]."

News Lookup
gemini -m pro -o text -e "" "Latest news about: [topic] from [timeframe]. Summarize important developments."

Prompt Templates
Research Prompt
You are an expert research analyst. Your goal is to provide genuinely useful, accurate research.

RESEARCH OBJECTIVE: [topic]

QUALITY STANDARDS:
- Be specific and concrete, not vague
- Distinguish between facts, expert opinions, and speculation
- Note when information is uncertain, contested, or evolving
- Identify what's NOT known or what gaps exist
- Provide actionable insights, not just information

Analysis Prompt
Analyze the following and provide:
1. Key findings
2. Implications
3. Recommendations
4. Uncertainties or gaps

Content: [content]

Best Practices
Use -o text -e "" for programmatic usage to get clean output
Pipe large content via stdin rather than command line args
Be specific in prompts - vague questions get vague answers
Ask for structure - request lists, tables, or JSON for parseable output
Request citations when accuracy matters
Set timeouts for long operations (gemini can take 30-120s)
Error Handling
Error	Solution
"command not found"	Install: pip install google-generativeai
"API key" / "unauthorized"	Set GEMINI_API_KEY environment variable
"rate limit" / "quota"	Wait and retry, or check quota at Google Cloud Console
Timeout	Break into smaller queries or increase timeout
Weekly Installs
27
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn