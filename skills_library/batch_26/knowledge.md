---
title: knowledge
url: https://skills.sh/boshu2/agentops/knowledge
---

# knowledge

skills/boshu2/agentops/knowledge
knowledge
Installation
$ npx skills add https://github.com/boshu2/agentops --skill knowledge
SKILL.md
Knowledge Skill

YOU MUST EXECUTE THIS WORKFLOW. Do not just describe it.

Find and retrieve knowledge from past work.

Execution Steps

Given /knowledge <query>:

Step 1: Search with ao CLI (if available)
ao search "<query>" --limit 10 2>/dev/null


If results found, read the relevant files.

Step 2: Search .agents/ Directory
# Search learnings
grep -r "<query>" .agents/learnings/ 2>/dev/null | head -10

# Search patterns
grep -r "<query>" .agents/patterns/ 2>/dev/null | head -10

# Search research
grep -r "<query>" .agents/research/ 2>/dev/null | head -10

# Search retros
grep -r "<query>" .agents/retros/ 2>/dev/null | head -10

Step 3: Search Plans
# Local plans
grep -r "<query>" .agents/plans/ 2>/dev/null | head -10

# Global plans
grep -r "<query>" ~/.claude/plans/ 2>/dev/null | head -10

Step 3.5: Search Global Patterns
# Global patterns (cross-repo knowledge)
grep -r "<query>" ~/.claude/patterns/ 2>/dev/null | head -10


Global patterns contain knowledge promoted from any repository via /learn --global. These are high-confidence, cross-project learnings.

Step 3.6: Search Global Learnings
# Global learnings (cross-repo abstracted knowledge)
grep -r "<query>" ~/.agents/learnings/ 2>/dev/null | head -10


Global learnings are abstracted, transferable insights promoted from repo-specific learnings via /learn --promote or classified as cross-cutting by /retro.

Step 3.7: Search Global Patterns (new location)
# Global patterns (new location, cross-repo)
grep -r "<query>" ~/.agents/patterns/ 2>/dev/null | head -10

Step 4: Use Semantic Search (if MCP available)
Tool: mcp__smart-connections-work__lookup
Parameters:
  query: "<query>"
  limit: 10

Step 5: Read Relevant Files

For each match found, use the Read tool to get full content.

Step 6: Synthesize Results

Combine findings into a coherent response:

What do we know about this topic?
What learnings are relevant?
What patterns apply?
What past decisions were made?
Step 7: Report to User

Present the knowledge found:

Summary of findings
Key learnings (with IDs)
Relevant patterns
Links to source files
Confidence level (how much we know)
Knowledge Locations
Type	Location	Format
Learnings	.agents/learnings/	Markdown
Patterns	.agents/patterns/	Markdown
Research	.agents/research/	Markdown
Retros	.agents/retros/	Markdown
Plans	.agents/plans/	Markdown
Global Plans	~/.claude/plans/	Markdown
Global Learnings	~/.agents/learnings/	Cross-repo abstracted learnings
Global Patterns	~/.agents/patterns/	Cross-repo reusable patterns
Legacy Patterns	~/.claude/patterns/	Read-only fallback (deprecated for writes)
Key Rules
Search multiple locations - knowledge may be scattered
Use ao CLI first - semantic search is better
Fall back to grep - if ao not available
Read full files - don't just report matches
Synthesize - combine findings into useful answer
Example Queries
/knowledge authentication    # Find auth-related learnings
/knowledge "rate limiting"   # Find rate limit patterns
/knowledge kubernetes        # Find K8s knowledge
/knowledge "what do we know about caching"

Examples
Finding Past Learnings

User says: /knowledge "error handling patterns"

What happens:

Agent tries ao search "error handling patterns", finds 3 matches
Agent searches .agents/learnings/ with grep, finds 5 additional matches
Agent searches .agents/patterns/ for related patterns, finds 2 matches
Agent reads all matched files using Read tool
Agent synthesizes findings into coherent response
Agent reports: "We have 5 learnings about error handling: L1 (always wrap errors), L3 (use typed errors), L12 (log before returning), L15 (context propagation), L22 (retry with backoff)"
Agent provides links to source files and confidence level: high (multiple confirmations)

Result: Complete knowledge synthesis with 5 specific learnings and 2 related patterns, all with source citations.

Querying Without ao CLI

User says: /knowledge "database migrations"

What happens:

Agent tries ao search, command not found
Agent falls back to grep search across .agents/ directories
Agent finds 2 matches in learnings, 1 in research, 0 in patterns
Agent reads matched files
Agent synthesizes: "Limited knowledge found. L8 recommends using transaction-wrapped migrations. Research doc from 2026-01-20 analyzed migration tools."
Agent reports medium confidence (only 2 sources)

Result: Knowledge found despite missing ao CLI, with appropriate confidence level based on source count.

Troubleshooting
Problem	Cause	Solution
No results found	Query too specific or knowledge not yet captured	Broaden search terms. Try synonyms. Check if topic was covered in recent work but retro not yet run. Suggest running /retro to extract recent learnings.
Too many results (overwhelming)	Very broad query term	Narrow query with more specific terms. Filter by date: search only recent learnings. Use semantic search (ao CLI) for better ranking if available.
Results lack context	Grep matches found but files don't address query	Read full files, not just matching lines. Synthesize from surrounding context. May need to trace back to original research with /trace.
Confidence level unclear	Mixed or contradictory sources	Report conflicting information explicitly. Note which sources agree/disagree. Suggest running /research to investigate further if critical.
Weekly Installs
167
Repository
boshu2/agentops
GitHub Stars
323
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass