---
title: github-deep-research
url: https://skills.sh/bytedance/deer-flow/github-deep-research
---

# github-deep-research

skills/bytedance/deer-flow/github-deep-research
github-deep-research
Installation
$ npx skills add https://github.com/bytedance/deer-flow --skill github-deep-research
Summary

Comprehensive GitHub repository analysis through multi-round research combining API data, web search, and structured reporting.

Executes four research rounds: GitHub API extraction, discovery searches, deep investigation with web fetching, and timeline analysis from commits and issues
Produces structured markdown reports with executive summaries, chronological timelines, metrics tables, and Mermaid diagrams for architecture and comparisons
Implements source prioritization (official docs first, then technical blogs, news, community discussions) with confidence scoring for each claim
Includes built-in citation tracking, competitive analysis capabilities, and balanced strengths/weaknesses assessment across all findings
SKILL.md
GitHub Deep Research Skill

Multi-round research combining GitHub API, web_search, web_fetch to produce comprehensive markdown reports.

Research Workflow
Round 1: GitHub API
Round 2: Discovery
Round 3: Deep Investigation
Round 4: Deep Dive
Core Methodology
Query Strategy

Broad to Narrow: Start with GitHub API, then general queries, refine based on findings.

Round 1: GitHub API
Round 2: "{topic} overview"
Round 3: "{topic} architecture", "{topic} vs alternatives"
Round 4: "{topic} issues", "{topic} roadmap", "site:github.com {topic}"


Source Prioritization:

Official docs/repos (highest weight)
Technical blogs (Medium, Dev.to)
News articles (verified outlets)
Community discussions (Reddit, HN)
Social media (lowest weight, for sentiment)
Research Rounds

Round 1 - GitHub API Directly execute scripts/github_api.py without read_file():

python /path/to/skill/scripts/github_api.py <owner> <repo> summary
python /path/to/skill/scripts/github_api.py <owner> <repo> readme
python /path/to/skill/scripts/github_api.py <owner> <repo> tree


Available commands (the last argument of github_api.py):

summary
info
readme
tree
languages
contributors
commits
issues
prs
releases

Round 2 - Discovery (3-5 web_search)

Get overview and identify key terms
Find official website/repo
Identify main players/competitors

Round 3 - Deep Investigation (5-10 web_search + web_fetch)

Technical architecture details
Timeline of key events
Community sentiment
Use web_fetch on valuable URLs for full content

Round 4 - Deep Dive

Analyze commit history for timeline
Review issues/PRs for feature evolution
Check contributor activity
Report Structure

Follow template in assets/report_template.md:

Metadata Block - Date, confidence level, subject
Executive Summary - 2-3 sentence overview with key metrics
Chronological Timeline - Phased breakdown with dates
Key Analysis Sections - Topic-specific deep dives
Metrics & Comparisons - Tables, growth charts
Strengths & Weaknesses - Balanced assessment
Sources - Categorized references
Confidence Assessment - Claims by confidence level
Methodology - Research approach used
Mermaid Diagrams

Include diagrams where helpful:

Timeline (Gantt):

gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    section Phase 1
    Development    :2025-01-01, 2025-03-01
    section Phase 2
    Launch         :2025-03-01, 2025-04-01


Architecture (Flowchart):

flowchart TD
    A[User] --> B[Coordinator]
    B --> C[Planner]
    C --> D[Research Team]
    D --> E[Reporter]


Comparison (Pie/Bar):

pie title Market Share
    "Project A" : 45
    "Project B" : 30
    "Others" : 25

Confidence Scoring

Assign confidence based on source quality:

Confidence	Criteria
High (90%+)	Official docs, GitHub data, multiple corroborating sources
Medium (70-89%)	Single reliable source, recent articles
Low (50-69%)	Social media, unverified claims, outdated info
Output

Save report as: research_{topic}_{YYYYMMDD}.md

Formatting Rules
Chinese content: Use full-width punctuation（，。：；！？）
Technical terms: Provide Wiki/doc URL on first mention
Tables: Use for metrics, comparisons
Code blocks: For technical examples
Mermaid: For architecture, timelines, flows
Best Practices
Start with official sources - Repo, docs, company blog
Verify dates from commits/PRs - More reliable than articles
Triangulate claims - 2+ independent sources
Note conflicting info - Don't hide contradictions
Distinguish fact vs opinion - Label speculation clearly
CRITICAL: Always include inline citations - Use [citation:Title](URL) format immediately after each claim from external sources
Extract URLs from search results - web_search returns {title, url, snippet} - always use the URL field
Update as you go - Don't wait until end to synthesize
Citation Examples

Good - With inline citations:

The project gained 10,000 stars within 3 months of launch [citation:GitHub Stats](https://github.com/owner/repo).
The architecture uses LangGraph for workflow orchestration [citation:LangGraph Docs](https://langchain.com/langgraph).


Bad - Without citations:

The project gained 10,000 stars within 3 months of launch.
The architecture uses LangGraph for workflow orchestration.

Weekly Installs
1.0K
Repository
bytedance/deer-flow
GitHub Stars
64.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn