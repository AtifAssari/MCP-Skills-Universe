---
title: codebase-context
url: https://skills.sh/zcy22606/codebase-context/codebase-context
---

# codebase-context

skills/zcy22606/codebase-context/codebase-context
codebase-context
Installation
$ npx skills add https://github.com/zcy22606/codebase-context --skill codebase-context
SKILL.md
Project AI Init

Analyze a project codebase from scratch and generate agent-friendly context files, enabling all AI coding tools (Claude Code, Kiro, Cursor, GitHub Copilot, Codex, OpenCode, Trae) to quickly understand the project and produce high-quality work.

Execution Modes

When the Skill starts, first select an execution mode. Use the userInput tool to present clickable options. Choose the best fit based on time budget and project needs:

{
  "question": "🚀 Select execution mode:",
  "options": [
    {
      "title": "⚡ Quick Mode (~5 min)",
      "description": "Generate CLAUDE.md only — make AI usable immediately. Best for: quick trial, personal projects, time-constrained"
    },
    {
      "title": "📋 Standard Mode (~30 min)",
      "description": "Generate CLAUDE.md + architecture docs + tech stack docs + AI tool configs. Best for: team projects, multi-tool support",
      "recommended": true
    },
    {
      "title": "🔬 Full Mode (~1-2 hours)",
      "description": "Deep analysis of every module/page, generate complete documentation. Best for: large projects, precise context needed"
    }
  ]
}

Mode Comparison
	⚡ Quick	📋 Standard	🔬 Full
Estimated Time	~5 min	~30 min	~1-2 hours
Generated Content	CLAUDE.md only	CLAUDE.md + docs/ + AI tool configs	All + per-module/page docs
Best For	Quick trial, personal projects	Team projects, multi-tool support	Large projects, precise context
Deep Analysis	❌	Lists modules/pages	✅ Interactive deep-dive
Tool-Specific Configs	❌	✅	✅
Validation Phase	❌	✅ (optional)	✅ (optional)
Mode × Phase Execution Matrix
Phase	⚡ Quick	📋 Standard	🔬 Full
0 Mode & Language Selection	✅	✅	✅
1 Basic Info Collection	✅	✅	✅
1.5 Resource Discovery	✅	✅	✅
2 Interactive Discovery	✅ (lite)	✅	✅
3 Schema + API Analysis	❌	✅	✅
4 Backend Module Deep Analysis	❌	❌ (list only)	✅ (interactive)
5 Frontend Page Analysis	❌	❌ (list only)	✅ (interactive)
6 Generate Common Files	✅ (CLAUDE.md only)	✅ (all)	✅ (all + module/page docs)
7 Tool-Specific Configs	❌	✅	✅
8 Output Summary	✅	✅	✅
9 Validation Phase	❌	✅ (optional)	✅ (optional)

💡 Recommendation: If the user is unsure, suggest 📋 Standard Mode — but always wait for explicit user confirmation. Never auto-select.

Quick Start
Select execution mode: Choose ⚡ Quick / 📋 Standard / 🔬 Full based on time budget
Select output language: Choose the language for generated files
Determine project type: Scan directory structure, identify frontend/backend/fullstack/monorepo
Collect basic info: Read config files, extract tech stack
Confirm team tools: Ask which AI tools the team uses (Claude Code / Kiro / Cursor / GitHub Copilot / Codex / OpenCode / Trae)
Deep analysis: Analyze backend by module, frontend by page route (Standard lists only, Full dives deep)
Generate common files: CLAUDE.md + module docs + page docs + architecture docs + tech stack docs + PR/Issue templates (Quick generates CLAUDE.md only)
Generate tool-specific configs: Generate dedicated rule/steering/rules files for each AI tool (Quick skips this)
Human review: Sections marked TODO need team input
Core Principles
90% of AI code quality depends on the context it receives
Treat frontend and backend differently: backend focuses on module responsibilities/business rules/state machines; frontend focuses on page routes/component trees/interaction flows
Shared layer is globally visible: utility methods, shared components, API conventions go into CLAUDE.md
One analysis benefits all AI tools (standard Markdown, not tied to any specific tool)
After human review, commit to repo as shared AI context infrastructure for the team
Interactive Discovery

Before analysis, confirm the following:

Project basics:

What kind of project is this? (Web app, API service, CLI tool, library)
Primary language and framework?
Team size? (Solo, small team, large team)

Business context:

Who are the users? What problem does it solve?
What are the core business flows?
Which modules/pages are the most complex?

Existing conventions:

Does the team have coding style guides?
Any API design conventions?
Any "unwritten rules" the AI should know?

AI tool usage:

Which AI coding tools does the team use?
Tool-specific config files will be generated for each selected tool

Use the userInput tool to present tool selection with toggleable options:

{
  "question": "🔧 Select AI coding tools your team uses. Configs will be generated for selected tools.\n\n(The current tool is pre-selected. Toggle additional tools your team needs.)",
  "options": [
    {
      "title": "Select tools to configure",
      "subOptionsLabel": "AI Coding Tools",
      "subOptions": [
        { "title": "Claude Code", "description": ".claude/rules/, commands/, settings.json, .claudeignore" },
        { "title": "Kiro", "description": ".kiro/steering/ rule files (always-load + conditional-load)" },
        { "title": "Cursor", "description": ".cursor/rules/ .mdc files with glob path matching" },
        { "title": "GitHub Copilot", "description": ".github/copilot-instructions.md single-file instructions" },
        { "title": "Codex", "description": "AGENTS.md instruction files (root + per-directory)" },
        { "title": "OpenCode", "description": ".opencode/instructions.md project instructions" },
        { "title": "Trae", "description": ".trae/rules/ rule files with YAML frontmatter" }
      ]
    }
  ]
}

Configuration Decision Tree
Start — Scan directory structure
│
├─ 1. Has packages/ or apps/ directory
│  └─ Monorepo → List sub-projects, user selects, analyze each (re-run detection per sub-project)
│
├─ 2. Root directory .md files > 50%, no src/ or app/ directory
│  └─ Docs/Knowledge Base → Run document structure analysis (directory hierarchy + naming conventions + navigation files)
│
├─ 3. Has bin/ directory, or package.json has bin field, or CLI entry file exists (cli.ts/cli.py/main.go)
│  └─ CLI Tool → Run command structure analysis (entry point + subcommands + argument definitions)
│
├─ 4. Has src/index.* entry + package.json has main/exports field, no page directory
│  └─ Library/SDK → Run API surface analysis (public interfaces + type definitions + example code)
│
├─ 5. Has Dockerfile + service entry (e.g. main.ts/app.py/main.go), no frontend page directory
│  └─ Microservice → Run service interface analysis (routes + health checks + config management + inter-service communication)
│
├─ 5.5 Has IaC config files (.tf, cdk.json, Pulumi.yaml, ansible.cfg, main.bicep, Chart.yaml, CloudFormation template)
│  └─ Infrastructure → Detect single/multi-project structure, run IaC analysis per project
│     ├─ Single project → Analyze directly (modules, workspaces, resources)
│     └─ Multi-project → List projects, analyze each independently, map shared modules
│
├─ 7. Has app/ or pages/ page directory, no service/controller layer
│  └─ Frontend Only → Run frontend analysis (page routes + shared layer)
│
├─ 8. Has service/controller layer, no page directory
│  └─ Backend Only → Run backend analysis (feature modules)
│
├─ 9. Has both page directory and service/controller layer
│  └─ Fullstack → Run both frontend + backend analysis
│
└─ 10. None of the above match
   └─ Generic Project → Use basic analysis strategy


💡 Priority note: Match from top to bottom by number, stop on first match. Monorepo has highest priority (sub-projects are recursively detected), docs/knowledge base is second (to avoid misclassification).

See references/non-web-project-analysis.md for detailed analysis strategies for non-web project types.

Generated Configurations
Common Files (Shared Across All Tools)
File	Purpose	When Generated
CLAUDE.md	Agent rule file (includes shared layer)	Always
docs/architecture.md	Architecture overview + module/page index	Recommended
docs/modules/{name}.md	Backend module business logic docs	Backend/fullstack projects, one per module
docs/pages/{name}.md	Frontend page business logic docs	Frontend/fullstack projects, one per page
docs/tech-stack.md	Tech stack & coding standards	Recommended
.github/PULL_REQUEST_TEMPLATE.md	PR template	Recommended
.github/ISSUE_TEMPLATE/	Issue templates	Optional
AI Tool-Specific Configurations
Tool	Generated Files	Description
Claude Code	.claude/rules/, .claude/commands/, .claude/settings.json, .claudeignore	Path-level rules + slash commands + permission config + file ignore rules
Kiro	.kiro/steering/product.md, tech.md, structure.md, conventions.md, api.md, frontend.md	Steering rule files, supports always-load and conditional-load
Cursor	.cursor/rules/project.mdc, frontend.mdc, backend.mdc, testing.mdc	.mdc rule files with glob path matching
GitHub Copilot	.github/copilot-instructions.md	Single-file global instructions (condensed)
Codex	AGENTS.md (root), per-directory AGENTS.md	OpenAI Codex instruction files, supports hierarchical inheritance, subdirectory rules override root rules
OpenCode	.opencode/instructions.md	Project-level instruction file, pure Markdown format
Trae	.trae/rules/project.md, frontend.md, backend.md	Rule files with YAML frontmatter controlling load conditions

See references/tool-specific-configs.md.

Workflow
Phase 0: Mode & Language Selection (mandatory, never skip)

⛔ Mandatory interaction: Under all circumstances, you must present the following options and wait for the user's explicit reply before proceeding. Never auto-select a default mode. Never decide for the user based on project characteristics.

Use the userInput tool to present clickable mode options:

{
  "question": "🚀 Select execution mode:",
  "options": [
    {
      "title": "⚡ Quick Mode (~5 min)",
      "description": "Generate CLAUDE.md only — make AI usable immediately. Best for: quick trial, personal projects, time-constrained"
    },
    {
      "title": "📋 Standard Mode (~30 min)",
      "description": "Generate CLAUDE.md + architecture docs + tech stack docs + AI tool configs. Best for: team projects, multi-tool support",
      "recommended": true
    },
    {
      "title": "🔬 Full Mode (~1-2 hours)",
      "description": "Deep analysis of every module/page, generate complete documentation. Best for: large projects, precise context needed"
    }
  ]
}


After user selects an option, record the mode selection.

Then use the userInput tool to present clickable language options:

{
  "question": "🌐 Select output language for generated files:",
  "options": [
    {
      "title": "English",
      "description": "Generate all output files in English"
    },
    {
      "title": "中文 (Chinese)",
      "description": "Generate all output files in Chinese"
    },
    {
      "title": "日本語 (Japanese)",
      "description": "Generate all output files in Japanese"
    },
    {
      "title": "Auto-detect",
      "description": "Follow the project's primary language"
    }
  ]
}


💡 This language selection affects only the generated output files (CLAUDE.md, docs/, steering, etc.). The Skill instructions themselves remain in English.

After user confirms both selections, proceed to Phase 1.

Phase 1: Basic Info Collection ⚡📋🔬

Read project config files and extract tech stack info:

File	Extracted Info
package.json	Project name, scripts, dependencies, framework detection
pyproject.toml / requirements.txt	Python dependencies
go.mod / Cargo.toml	Go/Rust dependencies
tsconfig.json	TypeScript configuration
.eslintrc* / .prettierrc*	Code style rules
README.md	Project description, business context
.env.example	Environment variable list (read names only, never read values)
Phase 1.5: Resource Discovery ⚡📋🔬

Before generating any files, check whether AI config files already exist in the target project. Based on detection results, the user can choose to incrementally update, skip existing files, or regenerate everything.

This Phase runs in all modes (⚡ Quick / 📋 Standard / 🔬 Full).

1. Check Existing Config Files

Scan whether the following files/directories already exist in the target project:

Path	Type	Description
CLAUDE.md	File	Universal agent rule file
.claude/rules/	Directory	Claude Code path-level rules
.claude/commands/	Directory	Claude Code slash commands
.claude/settings.json	File	Claude Code permission config
.claudeignore	File	Claude Code ignore file
.kiro/steering/	Directory	Kiro steering rule files
.cursor/rules/	Directory	Cursor rule files
.github/copilot-instructions.md	File	GitHub Copilot global instructions
AGENTS.md	File	Codex root-level instructions
.opencode/instructions.md	File	OpenCode project instructions
.trae/rules/	Directory	Trae rule files
docs/architecture.md	File	Architecture doc
docs/modules/	Directory	Backend module docs
docs/pages/	Directory	Frontend page docs
docs/tech-stack.md	File	Tech stack doc

For existing files, read content and record file size (word count); for existing directories, record file count and file name list.

2. Present Discovery Results

Show the user what was found:

🔍 Detected existing AI configurations:

✅ CLAUDE.md (1,234 words)
✅ .kiro/steering/ (4 files: product.md, tech.md, structure.md, conventions.md)
✅ docs/architecture.md (856 words)
❌ .claude/rules/ (not found)
❌ .claude/commands/ (not found)
❌ .claude/settings.json (not found)
❌ .claudeignore (not found)
❌ .cursor/rules/ (not found)
❌ .github/copilot-instructions.md (not found)
❌ AGENTS.md (not found)
❌ .opencode/instructions.md (not found)
❌ .trae/rules/ (not found)
❌ docs/modules/ (not found)
❌ docs/pages/ (not found)
❌ docs/tech-stack.md (not found)


If no config files exist at all, skip the user choice step and proceed directly to Phase 2.

3. User Chooses Handling Strategy

When existing config files are detected, ask the user:

Choose handling strategy:

1️⃣ Incremental Update — merge new analysis into existing files
   ✅ Preserves manually edited content
   ✅ Adds missing sections
   ✅ Updates outdated info (e.g. dependency versions)
   ⚠️ Requires human review of merge results

2️⃣ Skip Existing — only generate files that don't exist (default)
   ✅ Does not modify any existing files
   ✅ Safest option
   ⚠️ Existing files may lack newly analyzed info

3️⃣ Regenerate All — back up existing files, then regenerate from scratch
   ✅ Get the latest, most complete configs
   ⚠️ Overwrites manually edited content (existing files backed up to .ai-init-backup/)


Execution logic per option:

Incremental Update: Perform section-level merge on existing files (preserve user edits, add missing sections, update outdated info); generate missing files normally
Skip Existing: Keep current behavior — don't touch existing files, only generate missing ones
Regenerate All: Back up existing files to .ai-init-backup/{timestamp}/, then generate everything from scratch

💡 The user can also choose different strategies for different files (e.g. "incrementally update CLAUDE.md, regenerate the rest").

See references/incremental-update-strategy.md for detailed merge rules, conflict handling, and backup strategy.

Phase 2: Directory Structure Analysis + Project Type Detection ⚡📋🔬

Scan root directory and first-level subdirectories, identify architecture patterns and determine project type.

⚡ Quick Mode: Use lite interaction, reduce confirmation questions, quickly determine project type.

See references/directory-patterns.md.

Phase 3: Code Style Sampling 📋🔬

⚡ Quick Mode skips this Phase.

Randomly read 3-5 source files from the primary language (excluding tests and configs) to infer coding conventions.

See references/code-style-sampling.md.

Phase 4: Backend Module Deep Analysis 🔬 (backend/fullstack projects only)

⚡ Quick Mode skips this Phase. 📋 Standard Mode: List module names only, no deep-dive. 🔬 Full Mode: Interactive per-module deep analysis.

Infer business module list from service/controller/model directories
Present module list to user, ask which to analyze in depth (Full Mode)
Read core files per module, extract business rules, state machines, flows, dependencies (Full Mode)
Split complex modules (service > 800 lines or 3+ sub-domains) into multiple docs (Full Mode)

See references/backend-analysis.md.

🏗️ Infrastructure projects: Phase 4 is replaced by IaC-specific analysis: single/multi-project detection → per-project module parsing → workspace detection → resource inventory extraction → optional cloud CLI query. See infrastructure-analysis.md.

Phase 5: Frontend Page Route & Component Analysis 🔬 (frontend/fullstack projects only)

⚡ Quick Mode skips this Phase. 📋 Standard Mode: List page routes only, no deep-dive. 🔬 Full Mode: Interactive per-page deep analysis.

Infer page route tree from route directories
Present page list to user, ask which to analyze in depth (Full Mode)
Read entry files and sub-components per page, extract component tree, state management, interaction flows (Full Mode)
Scan shared layer: UI components, business components, utility methods, API layer, global state (Full Mode)
Split complex pages (5+ independent functional areas) into multiple docs (Full Mode)

See references/frontend-analysis.md.

Phase 6: Generate Context Files ⚡📋🔬

⚡ Quick Mode: Generate CLAUDE.md only, skip docs/, PR/Issue templates, etc. 📋 Standard Mode: Generate CLAUDE.md + docs/ + PR/Issue templates. 🔬 Full Mode: Generate everything, including per-module/per-page detailed docs.

🌐 Language: Generate all output content in the language selected by the user in Phase 0.

1. CLAUDE.md (always generated)

Contains: Tech Stack, Project Structure, Commands, Code Conventions, Architecture Decisions, Important Context (module/page overview + key business rules), Common Utilities & Shared Components, API Layer Conventions, Do NOT, Environment Variables.

See assets/CLAUDE.md.template.

2. docs/architecture.md (recommended)

Contains: System architecture diagram, backend module index, frontend page index, Data Flow, Database Schema, API Structure, External Services.

See assets/architecture.md.template.

3. docs/modules/{name}.md (backend module docs)

One doc per backend module, containing: responsibilities, core files, entities, state machines, business rules, flows, dependencies, third-party integrations, error handling, common pitfalls.

See assets/module.md.template.

4. docs/pages/{name}.md (frontend page docs)

One doc per frontend page, containing: responsibilities, route, component tree, state management, data fetching, interaction flows, shared component dependencies, common pitfalls.

See assets/page.md.template.

5. docs/tech-stack.md (recommended)

See assets/tech-stack.md.template.

6. PR/Issue Templates (recommended)

See assets/pr-template.md and assets/issue-templates/.

Phase 7: Generate AI Tool-Specific Configs 📋🔬

⚡ Quick Mode skips this Phase.

⛔ Mandatory interaction: Before generating any tool-specific configs, you MUST present the tool selection interface below and wait for the user's explicit confirmation. Never skip this step. Never auto-select all tools.

Step 1: Detect current running environment. Identify which AI coding tool is currently executing this Skill (e.g., if running inside Kiro, the current tool is "Kiro"; if running inside Cursor, the current tool is "Cursor"). Only the detected current tool should be pre-selected by default.

Step 2: Present tool selection. Use the userInput tool with the following parameters:

{
  "question": "🔧 Select AI coding tools your team uses. Configs will be generated for selected tools.\n\n(The current tool is pre-selected. Toggle additional tools your team needs.)",
  "options": [
    {
      "title": "Select tools to configure",
      "subOptionsLabel": "AI Coding Tools",
      "subOptions": [
        { "title": "Claude Code", "description": ".claude/rules/, commands/, settings.json, .claudeignore" },
        { "title": "Kiro", "description": ".kiro/steering/ rule files (always-load + conditional-load)" },
        { "title": "Cursor", "description": ".cursor/rules/ .mdc files with glob path matching" },
        { "title": "GitHub Copilot", "description": ".github/copilot-instructions.md single-file instructions" },
        { "title": "Codex", "description": "AGENTS.md instruction files (root + per-directory)" },
        { "title": "OpenCode", "description": ".opencode/instructions.md project instructions" },
        { "title": "Trae", "description": ".trae/rules/ rule files with YAML frontmatter" }
      ]
    }
  ]
}


Step 3: Process user selection.

Parse the user's response to determine which tools were selected.
If no tools were selected: Prompt the user that at least one tool must be selected before continuing. Re-present the tool selection interface.
If one or more tools were selected: Record the selected tool list and proceed to generate configs only for the selected tools.

Step 4: Generate configs. Based on the confirmed selection, split and generate tool-specific config files from CLAUDE.md and analysis results. Only generate configs for tools the user selected — skip all unselected tools.

🌐 Language: Generate all tool-specific config content in the language selected by the user in Phase 0.

Claude Code (if team uses it)

Generate the complete Claude Code configuration system, including path-level rules, slash commands, permission config, and file ignore rules.

1. .claude/rules/ — Path-Level Rules

Split from CLAUDE.md to generate path-level rule files:

frontend.md — Frontend components, shared components, state management rules
backend.md — Backend API, error handling, database rules
testing.md — Test organization, naming, pattern rules

See assets/claude-rules/.

2. .claude/commands/ — Slash Commands

Generate Claude Code slash commands. Each .md file auto-registers as a /command-name command.

Generation steps:

Copy assets/claude-commands/commit.md.template → .claude/commands/commit.md
Copy assets/claude-commands/review.md.template → .claude/commands/review.md
Customize:
Read package.json scripts, integrate common script commands into commit/review workflows
Monorepo projects: add scope suggestion list (sub-package names) to commit.md
If project has specific commit conventions (e.g. JIRA ticket prefix), add to commit.md conventions section
Suggest user add custom commands as needed (e.g. deploy.md, migrate.md)

Generated files:

commit.md — Git commit workflow (analyze git diff --staged → generate Conventional Commits message → execute commit)
review.md — Code review workflow (code quality → security → performance → test coverage → project conventions, output by 🔴🟡🟢 severity)

See assets/claude-commands/.

3. .claude/settings.json — Permission Config

Generate Claude Code permission config controlling what AI can and cannot do.

Generation steps:

Start from assets/claude-settings.json.template
Detect package manager (npm/pnpm/yarn/bun), replace command prefixes
Read package.json scripts, add project-defined scripts to allow list
Detect project toolchain (Docker → docker compose *, Prisma → npx prisma *, Python → python *)
Security audit: ensure dangerous commands in deny list (rm -rf, npm publish, git push --force, curl|bash, sudo) don't appear in allow list
Output final .claude/settings.json

See assets/claude-settings.json.template.

4. .claudeignore — File Ignore Rules

Generate .claudeignore in project root (alongside .gitignore) to prevent AI from accessing sensitive info or wasting context on irrelevant files.

Generation steps (three-layer overlay):

Layer 1 — .gitignore base: Read project's .gitignore (if exists), reuse its ignore rules
Layer 2 — AI tool default ignore patterns: Load from assets/claudeignore.template (env vars, keys/certs, large binaries, build artifacts, local databases, etc.)
Layer 3 — Project-specific sensitive files: Detected by scan_project.py (.env*, *.pem, *.key, filenames containing secret/credential, etc.)
Merge and deduplicate, ensure .env.example is not ignored (add !.env.example negation rule)
Detect large resource directories (e.g. public/images/, static/assets/), suggest ignoring if large
Output .claudeignore with categorized comments

⚠️ If .claudeignore already exists, skip generation and notify user.

See assets/claudeignore.template.

See references/tool-specific-configs.md for detailed format specifications.

Kiro (if team uses it)

Generate .kiro/steering/ directory with steering files, supporting always-load and conditional-load:

product.md — Product overview, business module summary, key business rules (always-load)
tech.md — Tech stack, commands, key dependencies (always-load)
structure.md — Project structure, architecture decisions, module/page index (always-load)
conventions.md — Coding conventions, Do NOT rules (always-load)
api.md — API conventions (conditional-load: matches API-related files)
frontend.md — Shared components, utility methods, frontend conventions (conditional-load: matches frontend files)

Steering files reference detailed docs via #[[file:docs/modules/xxx.md]], keeping themselves lightweight.

See assets/kiro-steering/.

Cursor (if team uses it)

Generate .cursor/rules/ directory with .mdc rule files supporting glob path matching:

project.mdc — Global rules (alwaysApply: true)
frontend.mdc — Frontend rules (glob matches **/*.tsx etc.)
backend.mdc — Backend rules (glob matches **/services/** etc.)
testing.mdc — Testing rules (glob matches **/*.test.* etc.)

See assets/cursor-rules/.

GitHub Copilot (if team uses it)

Generate .github/copilot-instructions.md single-file global instructions, condensed from CLAUDE.md (Copilot has a smaller context window, content must be concise).

See assets/copilot-instructions.md.template.

Codex (if team uses it)

Generate Codex instruction files from CLAUDE.md analysis results.

1. AGENTS.md — Root-Level Instructions

Create a root-level AGENTS.md file containing:

Project overview and tech stack summary
Global coding conventions and standards
Architecture guidelines
Key constraints and forbidden patterns
2. Per-Directory AGENTS.md (optional)

If the project has distinct modules (e.g., src/, tests/, docs/), generate subdirectory-level AGENTS.md files:

src/AGENTS.md — Source code conventions, import rules, component patterns
tests/AGENTS.md — Testing conventions, framework usage, coverage requirements

Hierarchy rule: Subdirectory AGENTS.md rules override/supplement root-level rules. Keep subdirectory files focused on directory-specific concerns.

OpenCode (if team uses it)

Generate OpenCode project instructions from CLAUDE.md analysis results.

1. .opencode/instructions.md — Project Instructions

Create a single project instruction file containing:

Project overview and purpose
Tech stack and key dependencies
Coding conventions and standards
Architecture patterns and guidelines
Forbidden patterns and common pitfalls

Format: Pure Markdown, single file. Keep concise and focused on actionable instructions.

Trae (if team uses it)

Generate Trae rule files from CLAUDE.md analysis results.

1. .trae/rules/project.md — Global Rules

Create a global rule file with YAML frontmatter:

---
description: "Project-wide coding standards and conventions"
globs: "**/*"
alwaysApply: true
---


Content: Project overview, tech stack, global coding conventions, architecture guidelines.

2. .trae/rules/frontend.md — Frontend Rules (if applicable)
---
description: "Frontend development rules"
globs: "src/components/**,src/pages/**,src/app/**"
alwaysApply: false
---


Content: Component patterns, state management, styling conventions, accessibility rules.

3. .trae/rules/backend.md — Backend Rules (if applicable)
---
description: "Backend development rules"
globs: "src/api/**,src/server/**,src/services/**"
alwaysApply: false
---


Content: API patterns, database conventions, error handling, security rules.

Format: Markdown with YAML frontmatter. Supports glob path matching for conditional loading (similar to Cursor's .mdc format).

Phase 8: Output Summary & Review ⚡📋🔬

Output generated file list, tech stack summary, module/page counts, TODO list requiring human input.

Phase 9: Validation Phase 📋🔬 (optional)

⚡ Quick Mode skips this Phase. 📋🔬 Standard and Full Mode optionally execute, default is skip.

After Phase 8 output summary, optionally run validation to have AI attempt a simple task to verify generated configs work.

1. Ask User Whether to Validate
Run config validation? AI will attempt a simple task to verify generated configs are effective. (yes/skip)

Default: skip


If user chooses skip or presses enter, skip Phase 9 and finish.

2. Choose Validation Method
Choose validation method:

1️⃣ Script Validation — Run validate_output.py to check file completeness
   Checks CLAUDE.md required sections, TODO markers, Markdown link validity

2️⃣ AI Task Validation — Have AI attempt a simple code task
   Add a simple function in an analyzed module/page, verify AI correctly references docs and follows conventions

3️⃣ Run Both

3. Execute Validation

Script Validation (option 1️⃣ or 3️⃣):

Run the output validation script:

python scripts/validate_output.py


The script checks: CLAUDE.md existence and required sections, TODO marker count, Markdown internal link validity, docs/ directory structure completeness.

AI Task Validation (option 2️⃣ or 3️⃣):

Select one analyzed module/page as validation target
AI attempts a simple code task (e.g. add a utility function to a service, add a helper component to a page)
After the task, check whether AI:
✅ Correctly referenced business rules from the relevant module/page doc
✅ Followed coding conventions from CLAUDE.md Code Conventions
✅ Respected prohibitions from CLAUDE.md Do NOT
✅ Used shared utilities/components documented in Common Utilities
4. Output Results and Improvement Suggestions

Summarize validation results by pass/warning/failure:

📋 Validation Results:

✅ AI correctly referenced business rules from module docs
✅ AI followed naming conventions from Code Conventions
⚠️ AI did not reference utility methods from Common Utilities
❌ AI violated a prohibition from Do NOT

Suggested improvements:
- Add usage examples for utility methods in CLAUDE.md Common Utilities section
- Add more specific prohibition scenarios in Do NOT section


If validation reveals config gaps:

Point out which config file and section needs improvement
Give specific improvement suggestions
If issues are severe, suggest manual review

If all validations pass:

🎉 Validation passed! AI can correctly understand project context and follow coding conventions.
Generated config files are ready to commit to the repository.

Output Structure

Fullstack project (team uses Claude Code + Kiro + Cursor + Codex):

project/
├── CLAUDE.md                              ← Universal agent rule file
├── AGENTS.md                              ← Codex root-level instructions
├── docs/
│   ├── architecture.md                    ← Architecture overview + index
│   ├── tech-stack.md                      ← Tech stack doc
│   ├── modules/                           ← Backend module docs
│   │   ├── auth.md
│   │   ├── course.md
│   │   └── payment-core.md
│   └── pages/                             ← Frontend page docs
│       ├── home.md
│       ├── course-detail.md
│       └── dashboard.md
├── .claude/                               ← Claude Code specific
│   ├── settings.json                      ← Permission config (allow/deny)
│   ├── rules/
│   │   ├── frontend.md
│   │   ├── backend.md
│   │   └── testing.md
│   └── commands/
│       ├── commit.md                      ← /commit slash command
│       └── review.md                      ← /review slash command
├── .claudeignore                          ← Claude Code file ignore rules (alongside .gitignore)
├── .kiro/                                 ← Kiro specific
│   └── steering/
│       ├── product.md
│       ├── tech.md
│       ├── structure.md
│       ├── conventions.md
│       ├── api.md                         ← Conditional load
│       └── frontend.md                    ← Conditional load
├── .cursor/                               ← Cursor specific
│   └── rules/
│       ├── project.mdc                    ← alwaysApply
│       ├── frontend.mdc                   ← glob match
│       ├── backend.mdc                    ← glob match
│       └── testing.mdc                    ← glob match
├── .opencode/                             ← OpenCode specific (if used)
│   └── instructions.md                    ← Project-level instructions
├── .trae/                                 ← Trae specific (if used)
│   └── rules/
│       ├── project.md                     ← Global rules (alwaysApply)
│       ├── frontend.md                    ← Frontend rules (glob match)
│       └── backend.md                     ← Backend rules (glob match)
└── .github/
    ├── copilot-instructions.md            ← Copilot specific (if used)
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/


Note: Only generate tool-specific configs for tools the team actually uses.

Safety Rules
Read-only analysis, never modify code — Only generate new files, never modify existing project code
Never read sensitive data — .env reads variable names only, never values; never read key files
Mark uncertain parts — Info that cannot be inferred is marked TODO: please fill in, never guess
Never overwrite existing files — If target file exists, skip and notify user
Universal format — Generate standard Markdown, not dependent on any specific AI tool's proprietary format
Reference Materials
Reference	When to Read
directory-patterns.md	Directory structure recognition & project type detection
non-web-project-analysis.md	Non-web project (docs/knowledge base, CLI tool, library/SDK, microservice) analysis strategies
code-style-sampling.md	Code style sampling strategy
backend-analysis.md	Backend module deep analysis methods
frontend-analysis.md	Frontend page route & component analysis methods
tool-specific-configs.md	AI tool-specific config file generation guide
incremental-update-strategy.md	Phase 1.5 Resource Discovery: incremental update strategy, merge rules, conflict handling, backup strategy
infrastructure-analysis.md	Infrastructure/IaC project analysis: multi-project detection, workspace analysis, cloud CLI resource query
Templates
Common Templates
Template	Purpose
CLAUDE.md.template	Agent rule file template
architecture.md.template	Architecture doc template
module.md.template	Backend module doc template
page.md.template	Frontend page doc template
tech-stack.md.template	Tech stack doc template
pr-template.md	PR template
issue-templates/	Issue templates
infrastructure.md.template	Infrastructure/IaC project doc template
AI Tool-Specific Templates
Template	Tool	Purpose
claude-rules/	Claude Code	.claude/rules/ path-level rule templates
claude-commands/	Claude Code	.claude/commands/ slash command templates (commit.md, review.md)
claude-settings.json.template	Claude Code	.claude/settings.json permission config template
claudeignore.template	Claude Code	.claudeignore file ignore rule template
kiro-steering/	Kiro	.kiro/steering/ steering file templates
cursor-rules/	Cursor	.cursor/rules/ .mdc rule templates
copilot-instructions.md.template	GitHub Copilot	Global instructions template
Supported Project Types
Project Type	Detection Criteria	Analysis Strategy	Support Level	Reference
Next.js / React Fullstack	Has both page directory and service/controller layer	Analyze frontend + backend simultaneously	⭐⭐⭐⭐⭐	frontend-analysis.md, backend-analysis.md
Frontend Only (Vite/CRA/Vue)	Has app/ or pages/ page directory, no service/controller layer	Page routes + shared layer	⭐⭐⭐⭐⭐	frontend-analysis.md
Node.js Backend (Express/Fastify/NestJS)	Has service/controller layer, no page directory	Module analysis	⭐⭐⭐⭐⭐	backend-analysis.md
Python (Django/FastAPI/Flask)	Has service/controller layer, no page directory	Backend analysis	⭐⭐⭐⭐	backend-analysis.md
Go / Rust	Has service/controller layer, no page directory	Basic backend analysis	⭐⭐⭐	backend-analysis.md
Monorepo	Has packages/ or apps/ directory	Per-sub-project analysis	⭐⭐⭐⭐	directory-patterns.md
React Native	Has screens/ directory + React Native dependency	Analyze by screens	⭐⭐⭐⭐	frontend-analysis.md
Docs/Knowledge Base	Root .md files > 50%, no src//app/ directory	Document structure analysis (directory hierarchy + naming conventions + navigation files + content format)	⭐⭐⭐⭐	non-web-project-analysis.md
CLI Tool	Has bin/ directory or package.json has bin field or CLI entry file exists	Command structure analysis (entry + subcommands + arguments + output format)	⭐⭐⭐⭐	non-web-project-analysis.md
Library/SDK	Has src/index.* entry + package.json has main/exports, no page directory	API surface analysis (public interfaces + type definitions + version compatibility + release flow)	⭐⭐⭐⭐	non-web-project-analysis.md
Microservice	Has Dockerfile + service entry, no frontend page directory	Service interface analysis (routes + health checks + config management + inter-service communication)	⭐⭐⭐⭐	non-web-project-analysis.md
Infrastructure/IaC	Has .tf files, cdk.json, Pulumi.yaml, ansible.cfg, main.bicep, Chart.yaml, or CloudFormation templates	Single/multi-project structure detection → per-project IaC analysis (modules, workspaces, resources, cloud CLI query)	⭐⭐⭐⭐	infrastructure-analysis.md, non-web-project-analysis.md
Weekly Installs
16
Repository
zcy22606/codeba…-context
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass