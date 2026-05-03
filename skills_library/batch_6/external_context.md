---
title: external-context
url: https://skills.sh/yeachan-heo/oh-my-claudecode/external-context
---

# external-context

skills/yeachan-heo/oh-my-claudecode/external-context
external-context
Installation
$ npx skills add https://github.com/yeachan-heo/oh-my-claudecode --skill external-context
SKILL.md
External Context Skill

Fetch external documentation, references, and context for a query. Decomposes into 2-5 facets and spawns parallel document-specialist Claude agents.

Usage
/oh-my-claudecode:external-context <topic or question>

Examples
/oh-my-claudecode:external-context What are the best practices for JWT token rotation in Node.js?
/oh-my-claudecode:external-context Compare Prisma vs Drizzle ORM for PostgreSQL
/oh-my-claudecode:external-context Latest React Server Components patterns and conventions

Protocol
Step 1: Facet Decomposition

Given a query, decompose into 2-5 independent search facets:

## Search Decomposition

**Query:** <original query>

### Facet 1: <facet-name>
- **Search focus:** What to search for
- **Sources:** Official docs, GitHub, blogs, etc.

### Facet 2: <facet-name>
...

Step 2: Parallel Agent Invocation

Fire independent facets in parallel via Task tool:

Task(subagent_type="oh-my-claudecode:document-specialist", model="sonnet", prompt="Search for: <facet 1 description>. Use WebSearch and WebFetch to find official documentation and examples. Cite all sources with URLs.")

Task(subagent_type="oh-my-claudecode:document-specialist", model="sonnet", prompt="Search for: <facet 2 description>. Use WebSearch and WebFetch to find official documentation and examples. Cite all sources with URLs.")


Maximum 5 parallel document-specialist agents.

Step 3: Synthesis Output Format

Present synthesized results in this format:

## External Context: <query>

### Key Findings
1. **<finding>** - Source: [title](url)
2. **<finding>** - Source: [title](url)

### Detailed Results

#### Facet 1: <name>
<aggregated findings with citations>

#### Facet 2: <name>
<aggregated findings with citations>

### Sources
- [Source 1](url)
- [Source 2](url)

Configuration
Maximum 5 parallel document-specialist agents
No magic keyword trigger - explicit invocation only
Weekly Installs
262
Repository
yeachan-heo/oh-…audecode
GitHub Stars
32.3K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn