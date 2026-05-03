---
rating: ⭐⭐⭐
title: banana-skill-finder
url: https://skills.sh/treydong/banana-skills/banana-skill-finder
---

# banana-skill-finder

skills/treydong/banana-skills/banana-skill-finder
banana-skill-finder
Installation
$ npx skills add https://github.com/treydong/banana-skills --skill banana-skill-finder
SKILL.md
Banana Skill Finder

Proactively helps users discover and install relevant Claude skills when they encounter tasks that could benefit from specialized capabilities.

When to Use This Skill

Trigger automatically (without user request) when detecting:

Working with specific file formats or technologies
Describing repetitive or specialized tasks
Asking "is there a skill/tool for..." or similar
Struggling with domain-specific work
Any task where a specialized skill could help

Important: This skill should trigger proactively. Don't wait for users to explicitly ask for skill recommendations.

Workflow
1. Analyze User Need

Identify:

Core task: What is the user trying to accomplish?
Domain: What category does this fall into? (development, documents, data, web, devops, content, etc.)
Keywords: Extract 2-4 relevant search terms
2. Search for Skills

Use a three-tier strategy with automatic fallback:

Tier 1: SkillsMP API (Best - if configured)

# Check for API key
echo $SKILLSMP_API_KEY

# If exists, use AI semantic search
curl -X GET "https://skillsmp.com/api/v1/skills/ai-search?q={natural_language_query}" \
  -H "Authorization: Bearer $SKILLSMP_API_KEY"


Benefits:

AI understands user intent, not just keywords
Access to 60,000+ curated skills
Best relevance and quality indicators

Tier 2: skills.sh WebFetch (Good - always works)

# Try search with query parameter
Use WebFetch: https://skills.sh/?q={keywords}

# Or browse leaderboard
Use WebFetch: https://skills.sh  # All-time popular
Use WebFetch: https://skills.sh/trending  # Trending (24h)


Benefits:

200+ high-quality curated skills
No authentication needed
Ranked by install count
Shows trending skills

Tier 3: GitHub API (Fallback - may have limits)

curl -X GET "https://api.github.com/search/code?q={keywords}+SKILL.md+language:markdown" \
  -H "Accept: application/vnd.github.v3+json"


Note: Rate limited (60/hour unauthenticated), use only as last resort.

Optional: Check Local Installed Skills

ls ~/.claude/skills/


Check if user already has relevant skills installed but hasn't used them.

Recommendation Order: Try Tier 1 → Tier 2 → Tier 3. Stop when you find good matches.

3. Rank by Relevance

Score each found skill based on:

Keyword match with user's need (most important)
Functionality alignment
Quality indicators (stars, recent activity)
Specificity vs generality

Select the 1-3 most relevant skills. Quality over quantity.

4. Present Recommendations

Format recommendations as:

I found [N] skill(s) that could help:

**1. [Skill Name]** - [One-line description]
   Source: [SkillsMP/GitHub/Vercel]
   Repository: [owner/repo]
   Why relevant: [Brief explanation]
   Install: `npx skills add [owner]/[repo]`

[Repeat for 2-3 skills max]

Would you like me to install any of these?

5. Install if Approved

When user approves, install using Vercel's skills CLI:

npx skills add <owner>/<repo>


Examples:

npx skills add vercel-labs/agent-skills
npx skills add anthropics/skills


This command:

Downloads the skill from GitHub
Installs to ~/.claude/skills/
Works with Claude Code, Cursor, Windsurf, and other agents
Tracks installation via anonymous telemetry (leaderboard)

Confirm installation success and explain how the skill will help.

Key Principles

Proactive, Not Reactive: Trigger automatically when relevant, don't wait to be asked

Quality Over Quantity: Recommend only 1-3 best matches, not a long list

Smart Three-Tier Search:

Tier 1: SkillsMP AI search (best, if configured)
Tier 2: skills.sh leaderboard (good, always works)
Tier 3: GitHub API (fallback, rate limited)
Stop when you find good matches

Explain Relevance: Always explain why each skill matches their need

Easy Installation: Use npx skills add owner/repo for one-command installation

API Key Recommended but Optional: Best results with SkillsMP API key, but skills.sh fallback works well

Examples

User says: "I need to extract text from a PDF file" → Trigger skill-finder, search for PDF processing skills, recommend pdf-editor or similar

User says: "Help me review this React component" → Trigger skill-finder, search for React/code-review skills, recommend react-best-practices from Vercel

User says: "I'm deploying to AWS" → Trigger skill-finder, search for AWS/deployment skills, recommend cloud-deploy or aws-helper

User says: "How do I query this BigQuery table?" → Trigger skill-finder, search for BigQuery/SQL skills, recommend bigquery or data-analysis skills

Additional Resources

For detailed information:

references/api_config.md - How to set up SkillsMP API key
references/skill_sources.md - Skill sources, categories, and search strategies
Setup Recommendations

For best results, suggest users configure SkillsMP API key:

Visit https://skillsmp.com/docs/api
Generate API key
Set environment variable: export SKILLSMP_API_KEY="sk_live_..."

This enables AI semantic search (much better than keyword matching). Without it, the skill automatically falls back to skills.sh leaderboard search, which still works well for most cases.

Weekly Installs
54
Repository
treydong/banana-skills
GitHub Stars
15
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn