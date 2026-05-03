---
title: learn
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/learn
---

# learn

skills/giuseppe-trisciuoglio/developer-kit/learn
learn
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill learn
SKILL.md
Learn

Autonomously analyzes a project's codebase to discover development patterns, conventions, and architectural decisions, then generates project rule files in .claude/rules/ for Claude Code to follow.

Overview

This skill acts as the Orchestrator in a two-agent architecture. It coordinates the overall workflow: gathering project context, delegating deep analysis to the learn-analyst sub-agent, filtering and ranking results, presenting findings to the user, and persisting approved rules to .claude/rules/.

The separation of concerns ensures the analyst operates with a focused forensic prompt while the orchestrator manages user interaction and file persistence.

When to Use

Use this skill when:

User asks to "learn from this project" or "understand project conventions"
User wants to auto-generate .claude/rules/ files from the existing codebase
User asks to "extract project rules" or "discover patterns"
User wants Claude Code to learn the project's coding standards
After joining a new project and wanting to codify existing conventions
Before starting a large feature to ensure Claude follows project patterns

Trigger phrases: "learn from project", "extract rules", "analyze conventions", "discover patterns", "generate project rules", "learn codebase", "auto-generate rules"

Instructions
Phase 1: Project Context Assessment

Before delegating to the analyst, gather high-level project context:

Verify project root: Confirm the current working directory is a project root (has package.json, pom.xml, pyproject.toml, go.mod, .git/, or similar markers)

Check existing rules: Scan for pre-existing rule files to understand what is already documented:

# Check for existing rules
ls -la .claude/rules/ 2>/dev/null || echo "No .claude/rules/ directory found"
cat CLAUDE.md 2>/dev/null || echo "No CLAUDE.md found"
cat AGENTS.md 2>/dev/null || echo "No AGENTS.md found"
ls -la .cursorrules 2>/dev/null || echo "No .cursorrules found"

Assess project size: Get a quick overview of the project scope:
# Quick project overview
find . -maxdepth 1 -type f -name "*.json" -o -name "*.toml" -o -name "*.xml" -o -name "*.gradle*" -o -name "Makefile" -o -name "*.yaml" -o -name "*.yml" | head -20
find . -type f -name "*.ts" -o -name "*.js" -o -name "*.java" -o -name "*.py" -o -name "*.go" -o -name "*.php" | wc -l

Inform the user: Briefly tell the user what you found and that you are about to start analysis:
"I found a [TypeScript/NestJS] project with [N] source files and [M] existing rules. Starting deep analysis..."
Phase 2: Delegate to Analyst Sub-Agent

Invoke the learn-analyst sub-agent to perform the deep codebase analysis.

Use the Task tool to delegate analysis to the learn-analyst agent:

Agent: learn-analyst
Prompt: "Analyze the codebase in the current working directory. Follow your full process: discovery, pattern extraction, classification, and prioritization. Return your findings as a JSON report."
Mode: Run synchronously to receive the JSON report directly

The analyst will return a structured JSON report with classified findings.

Phase 3: Review and Filter Results

Process the analyst's report:

Parse the JSON report returned by the analyst
Validate findings: Ensure each finding has:
A clear title
Evidence from at least 2 files
Impact score ≥ 4 (discard low-impact findings)
Well-formed markdown content
Deduplicate against existing rules: Compare each finding title and content against existing .claude/rules/ files. Skip findings that duplicate existing rules.
Select top 3: From the remaining findings, select the top 3 by impact score. If fewer than 3 remain after filtering, present whatever is left.
If zero findings remain: Inform the user that the project is already well-documented or no significant undocumented patterns were found.
Phase 4: Present to User

Present the filtered findings to the user in a clear, structured format:

I analyzed your codebase and found N patterns worth documenting as project rules:

1. **[RULE]** <Title> (Impact: X/10)
   <One-line explanation>

2. **[RULE]** <Title> (Impact: X/10)
   <One-line explanation>

3. **[RULE]** <Title> (Impact: X/10)
   <One-line explanation>


Then ask the user for confirmation using AskUserQuestion:

Present choices: "Save all N rules", "Let me choose which ones to save", "Cancel — don't save anything"
If the user wants to select individually, present each rule one by one with "Save / Skip" options
Never save automatically — always require explicit user approval
Phase 5: Persist Approved Rules

For each approved rule:

Ensure directory exists:
mkdir -p .claude/rules


Generate the file name: Use the finding's title field converted to kebab-case:

Example: "API Response Envelope Convention" → api-response-envelope-convention.md
Avoid generic names like rule-1.md or learned-pattern.md

Check for conflicts: Before writing, check if a file with the same name already exists:

If it exists, present a diff to the user and ask whether to replace, merge, or skip

Write the rule file: Create the file in .claude/rules/ with the analyst's pre-formatted content

Confirm to user: After saving, list all created files:

✅ Rules saved successfully:

  .claude/rules/api-response-envelope-convention.md
  .claude/rules/feature-based-module-organization.md
  .claude/rules/test-factory-pattern.md

These rules will be automatically applied by Claude Code in future sessions.

Best Practices
Run early in a project: Use this skill when joining a new project to quickly codify conventions
Review before saving: Always verify the generated rules make sense for your project
Iterate: Run the skill periodically as the project evolves — new patterns may emerge
Edit after saving: Generated rules are starting points; refine them to match your exact preferences
Commit rules to git: .claude/rules/ files are project-specific and should be version-controlled so the whole team benefits
Constraints and Warnings
Critical Constraints
Never save without confirmation: Always ask the user before writing any files
Project-local only: Only write to .claude/rules/ in the current project directory, never to global paths
Read-only analysis: The analyst sub-agent must not modify any project files
Evidence-based: Every rule must be backed by concrete evidence from the codebase
No hallucination: Do not invent patterns that are not actually present in the codebase
Respect existing rules: Do not overwrite existing rules without explicit user approval
Keep rules focused: Each rule file should address one specific convention or pattern
Limitations
Large monorepos: Analysis may take longer on very large codebases. The analyst scans representative samples, not every file.
Polyglot projects: In multi-language projects, rules are generated per-language. Ensure the rule title indicates the language scope.
Existing rules conflict: If the project already has comprehensive .claude/rules/, the skill may find few or no new patterns. This is expected.
Dynamic patterns: Some patterns only emerge at runtime (e.g., middleware ordering). This skill focuses on static codebase analysis.
Examples
Example 1: Learning from a NestJS project

User request: "Learn from this project"

Phase 1 — Context assessment:

Found: TypeScript/NestJS project with 142 source files
Existing rules: 0 files in .claude/rules/
Starting deep analysis...


Phase 4 — Presentation:

I analyzed your codebase and found 3 patterns worth documenting as project rules:

1. **[RULE]** Feature-Based Module Organization (Impact: 9/10)
   All modules follow src/modules/<feature>/ with controller, service, dto, entity subdirectories.

2. **[RULE]** DTO Validation Convention (Impact: 8/10)
   All DTOs use class-validator decorators and follow Create/Update naming pattern.

3. **[RULE]** Error Response Envelope (Impact: 7/10)
   All API errors return { statusCode, message, error } consistent envelope format.

Save all 3 rules? [Save all / Let me choose / Cancel]


Phase 5 — Persistence:

✅ Rules saved successfully:

  .claude/rules/feature-based-module-organization.md
  .claude/rules/dto-validation-convention.md
  .claude/rules/error-response-envelope.md

These rules will be automatically applied by Claude Code in future sessions.

Example 2: Project with existing rules

User request: "Discover project patterns"

Phase 1 — Context assessment:

Found: Java/Spring Boot project with 87 source files
Existing rules: 4 files in .claude/rules/
Starting deep analysis...


Phase 3 — After filtering:

The analyst found 6 patterns, but 4 overlap with your existing rules.
After deduplication, 2 new patterns remain:

1. **[RULE]** Repository Method Naming (Impact: 7/10)
   All custom repository methods use findBy/existsBy/countBy prefix convention.

2. **[RULE]** Integration Test Database Strategy (Impact: 6/10)
   Integration tests use @Testcontainers with PostgreSQL and @Sql for fixtures.

Save these 2 rules? [Save all / Let me choose / Cancel]

Weekly Installs
275
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass