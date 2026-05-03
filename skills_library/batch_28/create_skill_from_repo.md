---
title: create-skill-from-repo
url: https://skills.sh/hairyf/skills/create-skill-from-repo
---

# create-skill-from-repo

skills/hairyf/skills/create-skill-from-repo
create-skill-from-repo
Installation
$ npx skills add https://github.com/hairyf/skills --skill create-skill-from-repo
SKILL.md
Create Skills from Repo

Use this workflow to quickly ingest a framework or project's logic and documentation into the local environment. This is triggered when a user provides a <repo-url> and a <skills-name> for which no local skill yet exists.

🎯 Objectives
Source Persistence: Keep the original repo in sources/ for traceability and future updates.
Knowledge Distillation: Convert dense documentation into agent-optimized references/*.md (focusing on Usage and Why over Installation).
Automatic Registration: Ensure the new skill is immediately discoverable via AGENTS.md.
🛠 Prerequisites
Validation: Ensure <repo-url> is valid and <skills-name> uses kebab-case.
Environment: Verify git access and identify the project root.
🔄 Workflow
Step 1: Source Synchronization
Define the destination: sources/<submodule>.
Sync Logic:
Primary: git submodule add <repo-url> sources/<submodule>
Fallback: If the workspace is not a git repo, use git clone --depth 1 <repo-url> sources/<submodule>
Maintenance: If the directory exists but is empty, run git submodule update --init.
Step 2: Identify Knowledge Base
Locate Source Root: Scan sources/<submodule>/ for docs/, wiki/, README.md, or packages/*/docs/.
Filtering Strategy:
✅ Include: API references, core concepts, design patterns, best practices.
❌ Exclude: Installation guides (irrelevant to the Agent), contributing logs, sponsorship info, or marketing fluff.
Step 3: Modular Skill Generation

Target Structure: skills/<skills-name>/[SKILL.md, GENERATION.md, references/]

references/*.md Guidelines:
Atomicity: One concept per file.
Naming: {category}-{concept}.md (e.g., core-reactivity.md).
Content: Must include a Frontmatter, a brief description, high-quality Code Snippets, and source URLs.
SKILL.md Indexing:
Create a central entry point with tables categorizing references into Core, Features, and Advanced.
GENERATION.md Metadata:
Record the Git SHA, source path, and generation date for future diffing.
Step 4: The Coverage Loop
Review: Compare the Source Root navigation tree against the generated references/.
Supplement: If major modules (e.g., Middleware, Auth, Error Handling) are missing, repeat Step 3 for those specific modules.
Exit Condition: Stop once the primary API surface and architectural pillars are covered. Do not get bogged down in edge cases.
Step 5: Integration & Handover
**Update AGENTS.md**: Locate AGENTS.md in the project root (create it if missing).
Inject Skill Entry:
### <skills-name>
- **Location**: `skills/<skills-name>/`
- **Description**: [Short description from SKILL.md]


Completion Report: Summarize the output for the user (e.g., "Generated 15 reference files covering Core and Advanced modules").
💡 Key Principles
Agent-Centric Writing: Write for an AI audience. Prioritize technical accuracy and code examples over prose.
Kebab-Case: Strictly use kebab-case for all directory and filenames.
Path Formatting: Always use forward slashes (/) for cross-platform compatibility.
Incremental Readiness: The sources/ clone should remain so that git diff can be used later to spot documentation changes.
📚 References
Topic	Description	Reference
Coverage Criteria	Definitions of "major modules" and stop conditions	coverage-loop
Style Guide	Detailed writing style for reference files	style-guide

Would you like me to simulate a run of this skill using a specific repository URL to show you the expected output?

Weekly Installs
217
Repository
hairyf/skills
GitHub Stars
15
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn