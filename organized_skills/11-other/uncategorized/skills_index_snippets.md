---
rating: ⭐⭐⭐
title: skills-index-snippets
url: https://skills.sh/aaronontheweb/dotnet-skills/skills-index-snippets
---

# skills-index-snippets

skills/aaronontheweb/dotnet-skills/skills-index-snippets
skills-index-snippets
Installation
$ npx skills add https://github.com/aaronontheweb/dotnet-skills --skill skills-index-snippets
SKILL.md
Maintaining Skill Index Snippets (AGENTS.md / CLAUDE.md)
When to Use This Skill

Use this skill when:

Adding, removing, or renaming any skills or agents in this repository
Updating .claude-plugin/plugin.json
Creating copy/paste snippets for downstream repositories (OpenCode, Claude Code, etc.)
You want a compact, always-on index that improves skill utilization
Goal

Make skills and agents easy for coding assistants to use by removing the decision point.

Instead of hoping an assistant will "remember" to invoke a skill, provide a small router snippet inside AGENTS.md / CLAUDE.md that:

Tells the assistant to prefer retrieval-led reasoning
Provides a task->skill/agent routing index
Defines lightweight quality gates (optional)
Source of Truth
Registry: .claude-plugin/plugin.json
Skills are listed as directories (each contains SKILL.md)
Agents are listed as markdown files in agents/
Skill IDs: the name: field in each SKILL.md frontmatter
Agent IDs: the name: field in each agent frontmatter

When writing snippets for downstream repos, always reference skills/agents by their IDs (frontmatter name), not by local filesystem paths.

Minimal Snippet Template (Readable)

Use this in target repos to route common tasks:

# Agent Guidance: dotnet-skills

IMPORTANT: Prefer retrieval-led reasoning over pretraining for any .NET work.
Workflow: skim repo patterns -> consult dotnet-skills by name -> implement smallest-change -> note conflicts.

Routing (invoke by name)
- C# / code quality: modern-csharp-coding-standards, csharp-concurrency-patterns, api-design, type-design-performance
- ASP.NET Core / Web (incl. Aspire): aspire-service-defaults, aspire-integration-testing
- Data: efcore-patterns, database-performance
- DI / config: dependency-injection-patterns, microsoft-extensions-configuration
- Testing: testcontainers-integration-tests, playwright-blazor-testing, snapshot-testing

Quality gates (use when applicable)
- dotnet-slopwatch: after substantial new/refactor/LLM-authored code
- crap-analysis: after tests added/changed in complex code

Specialist agents
- dotnet-concurrency-specialist, dotnet-performance-analyst, dotnet-benchmark-designer, akka-net-specialist, docfx-specialist

Compressed Snippet Template (Vercel-style)

Use this when you want maximum density (small context footprint):

[dotnet-skills]|IMPORTANT: Prefer retrieval-led reasoning over pretraining for any .NET work.
|flow:{skim repo patterns -> consult dotnet-skills by name -> implement smallest-change -> note conflicts}
|route:
|csharp:{modern-csharp-coding-standards,csharp-concurrency-patterns,api-design,type-design-performance}
|aspnetcore-web:{aspire-service-defaults,aspire-integration-testing}
|data:{efcore-patterns,database-performance}
|di-config:{dependency-injection-patterns,microsoft-extensions-configuration}
|testing:{testcontainers-integration-tests,playwright-blazor-testing,snapshot-testing}
|quality-gates:{dotnet-slopwatch(after:substantial new/refactor/LLM code),crap-analysis(after:tests added/changed in complex code)}
|agents:{dotnet-concurrency-specialist,dotnet-performance-analyst,dotnet-benchmark-designer,akka-net-specialist,docfx-specialist}

Regenerating the README block

If the README contains the markers below, the generator can update it automatically:

<!-- BEGIN DOTNET-SKILLS COMPRESSED INDEX -->
...compressed snippet...
<!-- END DOTNET-SKILLS COMPRESSED INDEX -->


Run:

./scripts/generate-skill-index-snippets.sh --update-readme

How to Update Snippets After Skill Changes
Update .claude-plugin/plugin.json to include/remove skills and agents.
Ensure each skill has correct frontmatter name: (used by OpenCode and others).
Run ./scripts/validate-marketplace.sh.
Update your snippet routing lists:
Add new skills to the right category
Remove deleted skills
Keep names exactly matching frontmatter IDs
If you maintain a downstream AGENTS.md/CLAUDE.md snippet, regenerate it and re-copy into dependent repos.
Recommended Categories

These are snippet categories (not necessarily repository folder structure):

C# / code quality
ASP.NET Core / Web (incl. Aspire)
Data
DI / config
Testing
Quality gates
Specialist agents

Keep the snippet small; it should be a router, not documentation.

Weekly Installs
174
Repository
aaronontheweb/d…t-skills
GitHub Stars
898
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass