---
rating: ⭐⭐⭐
title: parallel-agents
url: https://skills.sh/sickn33/antigravity-awesome-skills/parallel-agents
---

# parallel-agents

skills/sickn33/antigravity-awesome-skills/parallel-agents
parallel-agents
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill parallel-agents
Summary

Coordinate multiple specialized agents for complex tasks requiring diverse expertise domains.

Includes 17 pre-built agents covering security, backend, frontend, testing, DevOps, database, mobile, API design, debugging, documentation, performance, planning, SEO, and game development
Supports three orchestration patterns: comprehensive analysis (discovery through synthesis), feature review (domain-specific agents plus testing), and security audits (auditor plus penetration tester)
Agents share context within a single session, enabling sequential workflows where findings from one agent inform the next
Built-in synthesis protocol consolidates findings into prioritized recommendations with action items across all participating agents
SKILL.md
Native Parallel Agents

Orchestration through Claude Code's built-in Agent Tool

Overview

This skill enables coordinating multiple specialized agents through Claude Code's native agent system. Unlike external scripts, this approach keeps all orchestration within Claude's control.

When to Use Orchestration

✅ Good for:

Complex tasks requiring multiple expertise domains
Code analysis from security, performance, and quality perspectives
Comprehensive reviews (architecture + security + testing)
Feature implementation needing backend + frontend + database work

❌ Not for:

Simple, single-domain tasks
Quick fixes or small changes
Tasks where one agent suffices
Native Agent Invocation
Single Agent
Use the security-auditor agent to review authentication

Sequential Chain
First, use the explorer-agent to discover project structure.
Then, use the backend-specialist to review API endpoints.
Finally, use the test-engineer to identify test gaps.

With Context Passing
Use the frontend-specialist to analyze React components.
Based on those findings, have the test-engineer generate component tests.

Resume Previous Work
Resume agent [agentId] and continue with additional requirements.

Orchestration Patterns
Pattern 1: Comprehensive Analysis
Agents: explorer-agent → [domain-agents] → synthesis

1. explorer-agent: Map codebase structure
2. security-auditor: Security posture
3. backend-specialist: API quality
4. frontend-specialist: UI/UX patterns
5. test-engineer: Test coverage
6. Synthesize all findings

Pattern 2: Feature Review
Agents: affected-domain-agents → test-engineer

1. Identify affected domains (backend? frontend? both?)
2. Invoke relevant domain agents
3. test-engineer verifies changes
4. Synthesize recommendations

Pattern 3: Security Audit
Agents: security-auditor → penetration-tester → synthesis

1. security-auditor: Configuration and code review
2. penetration-tester: Active vulnerability testing
3. Synthesize with prioritized remediation

Available Agents
Agent	Expertise	Trigger Phrases
orchestrator	Coordination	"comprehensive", "multi-perspective"
security-auditor	Security	"security", "auth", "vulnerabilities"
penetration-tester	Security Testing	"pentest", "red team", "exploit"
backend-specialist	Backend	"API", "server", "Node.js", "Express"
frontend-specialist	Frontend	"React", "UI", "components", "Next.js"
test-engineer	Testing	"tests", "coverage", "TDD"
devops-engineer	DevOps	"deploy", "CI/CD", "infrastructure"
database-architect	Database	"schema", "Prisma", "migrations"
mobile-developer	Mobile	"React Native", "Flutter", "mobile"
api-designer	API Design	"REST", "GraphQL", "OpenAPI"
debugger	Debugging	"bug", "error", "not working"
explorer-agent	Discovery	"explore", "map", "structure"
documentation-writer	Documentation	"write docs", "create README", "generate API docs"
performance-optimizer	Performance	"slow", "optimize", "profiling"
project-planner	Planning	"plan", "roadmap", "milestones"
seo-specialist	SEO	"SEO", "meta tags", "search ranking"
game-developer	Game Development	"game", "Unity", "Godot", "Phaser"
Claude Code Built-in Agents

These work alongside custom agents:

Agent	Model	Purpose
Explore	Haiku	Fast read-only codebase search
Plan	Sonnet	Research during plan mode
General-purpose	Sonnet	Complex multi-step modifications

Use Explore for quick searches, custom agents for domain expertise.

Synthesis Protocol

After all agents complete, synthesize:

## Orchestration Synthesis

### Task Summary
[What was accomplished]

### Agent Contributions
| Agent | Finding |
|-------|---------|
| security-auditor | Found X |
| backend-specialist | Identified Y |

### Consolidated Recommendations
1. **Critical**: [Issue from Agent A]
2. **Important**: [Issue from Agent B]
3. **Nice-to-have**: [Enhancement from Agent C]

### Action Items
- [ ] Fix critical security issue
- [ ] Refactor API endpoint
- [ ] Add missing tests

Best Practices
Available agents - 17 specialized agents can be orchestrated
Logical order - Discovery → Analysis → Implementation → Testing
Share context - Pass relevant findings to subsequent agents
Single synthesis - One unified report, not separate outputs
Verify changes - Always include test-engineer for code modifications
Key Benefits
✅ Single session - All agents share context
✅ AI-controlled - Claude orchestrates autonomously
✅ Native integration - Works with built-in Explore, Plan agents
✅ Resume support - Can continue previous agent work
✅ Context passing - Findings flow between agents
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
483
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass