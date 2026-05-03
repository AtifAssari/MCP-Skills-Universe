---
rating: ⭐⭐
title: ai-dev-tools-sync
url: https://skills.sh/duc01226/easyplatform/ai-dev-tools-sync
---

# ai-dev-tools-sync

skills/duc01226/easyplatform/ai-dev-tools-sync
ai-dev-tools-sync
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill ai-dev-tools-sync
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Critical Thinking Mindset — Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence >80% to act. Anti-hallucination: Never present guess as fact — cite sources for every claim, admit uncertainty freely, self-check output for errors, cross-reference independently, stay skeptical of own confidence — certainty without evidence root of all hallucination.

AI Mistake Prevention — Failure modes to avoid on every task:

Check downstream references before deleting. Deleting components causes documentation and code staleness cascades. Map all referencing files before removal.
Verify AI-generated content against actual code. AI hallucinates APIs, class names, and method signatures. Always grep to confirm existence before documenting or referencing.
Trace full dependency chain after edits. Changing a definition misses downstream variables and consumers derived from it. Always trace the full chain.
Trace ALL code paths when verifying correctness. Confirming code exists is not confirming it executes. Always trace early exits, error branches, and conditional skips — not just happy path.
When debugging, ask "whose responsibility?" before fixing. Trace whether bug is in caller (wrong data) or callee (wrong handling). Fix at responsible layer — never patch symptom site.
Assume existing values are intentional — ask WHY before changing. Before changing any constant, limit, flag, or pattern: read comments, check git blame, examine surrounding code.
Verify ALL affected outputs, not just the first. Changes touching multiple stacks require verifying EVERY output. One green check is not all green checks.
Holistic-first debugging — resist nearest-attention trap. When investigating any failure, list EVERY precondition first (config, env vars, DB names, endpoints, DI registrations, data preconditions), then verify each against evidence before forming any code-layer hypothesis.
Surgical changes — apply the diff test. Bug fix: every changed line must trace directly to the bug. Don't restyle or improve adjacent code. Enhancement task: implement improvements AND announce them explicitly.
Surface ambiguity before coding — don't pick silently. If request has multiple interpretations, present each with effort estimate and ask. Never assume all-records, file-based, or more complex path.
Quick Summary

Goal: Synchronize Claude Code and GitHub Copilot configurations to maintain feature parity across both AI dev tools.

Workflow:

Understand — Read current configs (CLAUDE.md, copilot-instructions.md, agents, workflows)
Research — Search for latest features across both platforms
Compare — Identify gaps in skills, prompts, agents, or instructions
Sync — Implement changes in both platforms maintaining compatibility

Key Rules:

Copilot reads .claude/skills/ automatically (backward compatibility)
Both platforms read .github/prompts/*.prompt.md and .github/agents/*.md
Always update both CLAUDE.md and .github/copilot-instructions.md + .github/instructions/*.instructions.md for instruction changes

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

AI Dev Tools Sync

Synchronize Claude Code and GitHub Copilot configurations to maintain feature parity.

When to Use

Activate this skill when:

User asks to update Claude Code or Copilot setup
User wants to add/modify skills, prompts, agents, or instructions
User wants both tools to work similarly
User asks about AI dev tool configuration
Quick Reference
Claude Code	GitHub Copilot	Location
SKILL.md	SKILL.md	.claude/skills/ + .github/skills/
SKILL.md	prompts/*.prompt.md	.claude/skills/ + .github/prompts/
agents/*.md	agents/*.md	.github/agents/ (shared)
workflows/*.md	-	.claude/workflows/
CLAUDE.md	copilot + instructions/	Root + .github/
-	chatmodes/*.chatmode.md	.github/chatmodes/
Sync Process
Step 1: Understand Current Setup

Read these files to understand current configuration:

.claude/workflows/orchestration-protocol.md
.claude/workflows/primary-workflow.md
.github/copilot-instructions.md
.github/instructions/*.instructions.md
.github/AGENTS.md
CLAUDE.md

Step 2: Research Latest Features

Search web for:

"GitHub Copilot features setup 2026"
"GitHub Copilot custom instructions agents skills prompts"
"GitHub Copilot agent mode workspace context"

See references/copilot-features.md for feature catalog.

Step 3: Identify Sync Opportunities

Compare capabilities and identify gaps:

Skills missing in one platform
Inconsistent prompt/instruction behavior
Agent definitions that differ
Step 4: Implement Changes

For each change:

Skills: Create in both .claude/skills/ and .github/skills/
Prompts: Create in both .claude/skills/ and .github/prompts/
Instructions: Update CLAUDE.md + .github/copilot-instructions.md + .github/instructions/*.instructions.md
Agents: Update .github/agents/ (shared by both)
Compatibility Notes
Copilot reads .claude/skills/ automatically (backward compatibility)
Both read .github/prompts/*.prompt.md
Both read .github/agents/*.md
Both read AGENTS.md in root or .github/
Both support path-based instruction files via applyTo in frontmatter
References
Copilot Features Catalog
Sync Patterns
Closing Reminders
MANDATORY IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
MANDATORY IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
MANDATORY IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
MANDATORY IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
MUST ATTENTION apply critical thinking — every claim needs traced proof, confidence >80% to act. Anti-hallucination: never present guess as fact.
MUST ATTENTION apply AI mistake prevention — holistic-first debugging, fix at responsible layer, surface ambiguity before coding, re-read files after compaction.

[TASK-PLANNING] Before acting, analyze task scope and systematically break it into small todo tasks and sub-tasks using TaskCreate.

Weekly Installs
45
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn