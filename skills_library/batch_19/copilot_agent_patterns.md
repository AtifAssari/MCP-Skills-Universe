---
title: copilot-agent-patterns
url: https://skills.sh/hack23/riksdagsmonitor/copilot-agent-patterns
---

# copilot-agent-patterns

skills/hack23/riksdagsmonitor/copilot-agent-patterns
copilot-agent-patterns
Installation
$ npx skills add https://github.com/hack23/riksdagsmonitor --skill copilot-agent-patterns
SKILL.md
Copilot Agent Patterns Skill
🔴 AI FIRST Quality Principle

Apply the AI FIRST principle: never accept first-pass quality. Minimum 2 iterations. Read all output, improve every section. No shortcuts.

Purpose

Provides proven patterns for designing, implementing, and orchestrating GitHub Copilot custom agents.

Agent Design Patterns
Specialist Agent Pattern
Focused on single domain expertise
Minimal tool set (view, edit, create, shell, search_code)
Clear scope boundaries (MUST/MUST NOT)
Skills integration references
Orchestrator Agent Pattern
Broad tool access (tools: ["*"])
Creates and assigns GitHub issues
Delegates to specialist agents
Tracks progress and quality
YAML Frontmatter Standards
name: agent-name               # Lowercase, hyphen-separated
description: Brief expertise   # Max 200 characters
tools: ["tool1", "tool2"]     # Minimal set for non-meta agents

Collaboration Patterns
Sequential: Task agent → creates issues → assigns specialists
Parallel: Multiple specialists work on different scopes simultaneously
Stacked PRs: Foundation PR → Implementation PR → Polish PR (using base_ref)
Agent Boundaries
Each agent respects its expertise area
Delegates outside its scope
References skills library constantly
Follows ISMS policies automatically
Copilot Coding Agent Tools
assign_copilot_to_issue — with base_ref and custom_instructions
create_pull_request_with_copilot — with base_ref and custom_agent
get_copilot_job_status — for tracking progress
Best Practices
Focus on expertise area
Complete work autonomously when possible
Test changes thoroughly
Document decisions
Only ask when genuinely ambiguous
Related Policies
Secure Development Policy
🔗 Integration with agentic workflows & analysis artifacts

This skill is consumed by the 11 agentic news workflows in .github/workflows/news-*.md. The authoritative contract lives in .github/prompts/README.md; this skill supplies domain expertise on top of that contract.

Analysis product → ai-driven-analysis-guide.md + every template in analysis/templates/.
Required before any article: 9 core artifacts (14 for Tier-C) in analysis/daily/$ARTICLE_DATE/$SUBFOLDER/; 05-analysis-gate.md is the single blocking gate.
gh-aw v0.69.3 docs: abridged · complete · blog series.
Weekly Installs
20
Repository
hack23/riksdagsmonitor
GitHub Stars
7
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass