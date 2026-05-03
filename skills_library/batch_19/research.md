---
title: research
url: https://skills.sh/zpankz/mcp-skillset/research
---

# research

skills/zpankz/mcp-skillset/research
research
Installation
$ npx skills add https://github.com/zpankz/mcp-skillset --skill research
SKILL.md
Research Skill
🎯 Load Full PAI Context

Before starting any task with this skill, load complete PAI context:

read ${PAI_DIR}/.claude/skills/CORE/SKILL.md

This provides access to:

Complete contact list and team members
Stack preferences (TypeScript>Python, bun>npm, uv>pip)
Security rules and repository safety protocols
Response format requirements (structured emoji format)
Voice IDs for agent routing (ElevenLabs)
Personal preferences and operating instructions
When to Use This Skill

This skill activates when the user requests research or information gathering:

"Do research on X"
"Research this topic"
"Find information about X"
"Investigate this subject"
"Analyze trends in X"
"Current events research"
Any comprehensive information gathering request

THREE RESEARCH MODES:

QUICK RESEARCH MODE:

User says "quick research" → Launch 3 agents (1 of each type)
Timeout: 2 minutes | Main Kai waits 2 minutes then synthesizes
Best for: Simple queries, straightforward questions

STANDARD RESEARCH MODE (Default):

Default for most research requests → Launch 9 agents (3 of each type)
Timeout: 3 minutes | Main Kai waits 3 minutes then synthesizes
Best for: Most research needs, comprehensive coverage

EXTENSIVE RESEARCH MODE:

User says "extensive research" → Launch 24 agents (8 of each type)
Use be-creative skill with UltraThink for maximum query diversity
Generate 24 unique, creative research angles
Timeout: 10 minutes | Main Kai waits 10 minutes then synthesizes
Best for: Deep-dive research, multi-domain analysis, comprehensive reports

⏱️ CRITICAL TIMEOUT RULES:

Quick (3 agents): 2 minute timeout
Standard (9 agents): 3 minute timeout
Extensive (24 agents): 10 minute timeout
After timeout, main Kai STOPS WAITING and synthesizes with whatever results are available
Proceed with partial results - don't wait indefinitely for stragglers
How to Execute

Execute the /conduct-research slash command, which handles the complete workflow:

Decomposing research questions into 3-24 sub-questions
Launching up to 24 parallel research agents (perplexity, claude, gemini)
Collecting results in 15-60 seconds (HARD TIMEOUT: 3 minutes max)
Synthesizing findings with confidence levels (even with partial results)
Formatting comprehensive report with source attribution
Available Research Agents
perplexity-researcher: Fast Perplexity API searches (web/current)
claude-researcher: Claude WebSearch with intelligent query decomposition (academic/detailed)
gemini-researcher: Google Gemini multi-perspective research (synthesis)
Speed Benefits
❌ Old approach: Sequential searches → 5-10 minutes
✅ Quick mode: 3 parallel agents → 2 minute timeout
✅ Standard mode: 9 parallel agents → 3 minute timeout
✅ Extensive mode: 24 parallel agents → 10 minute timeout

⏱️ CRITICAL: After timeout, proceed with whatever results are available. DO NOT wait indefinitely for slow agents.

📁 Scratchpad → History Pattern

Working Directory (Scratchpad): ${PAI_DIR}/scratchpad/YYYY-MM-DD-HHMMSS_research-[topic]/

Process:

Scratchpad (Working Files - Temporary):

Create timestamped directory for each research project
Store raw research outputs from all agents
Keep intermediate synthesis notes
Save query decomposition and analysis
Draft reports and iterations

History (Permanent Archive):

Move to ${PAI_DIR}/history/research/YYYY-MM-DD_[topic]/ when complete
Include: README.md, final research report, key data files
Archive for future reference and reuse

Verification (MANDATORY):

Check if hooks captured output to history automatically
If hooks failed, manually save to history
Confirm all files present in history directory

File Structure Example:

Scratchpad (temporary workspace):

${PAI_DIR}/scratchpad/2025-10-26-143022_research-agi-frameworks/
├── raw-outputs/
│   ├── perplexity-001.md
│   ├── claude-001.md
│   └── gemini-001.md
├── synthesis-notes.md
├── query-decomposition.md
└── draft-report.md


History (permanent archive):

${PAI_DIR}/history/research/2025-10-26_agi-frameworks/
├── README.md (research documentation)
├── research-report.md (final comprehensive report)
├── key-findings.md (executive summary)
└── metadata.json (sources, agents used, timestamps)


README.md Template:

# Research: [Topic]

**Date:** YYYY-MM-DD
**Research Mode:** Quick/Standard/Extensive
**Agents Used:** X perplexity, Y claude, Z gemini

## Research Question
[Original question or topic]

## Key Findings
- Finding 1
- Finding 2
- Finding 3

## Methodology
- Query decomposition: [How questions were split]
- Agents deployed: [Which agents, how many]
- Sources consulted: [Number and types]

## Output Files
- research-report.md: Full comprehensive report
- key-findings.md: Executive summary
- metadata.json: Source tracking

## Notes
[Any limitations, gaps, or follow-up needed]

Full Workflow Reference

For complete step-by-step instructions: read ${PAI_DIR}/.claude/commands/conduct-research.md

Weekly Installs
8
Repository
zpankz/mcp-skillset
GitHub Stars
2
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn