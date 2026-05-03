---
rating: ⭐⭐⭐
title: workflow-creator
url: https://skills.sh/nicepkg/ai-workflow/workflow-creator
---

# workflow-creator

skills/nicepkg/ai-workflow/workflow-creator
workflow-creator
Installation
$ npx skills add https://github.com/nicepkg/ai-workflow --skill workflow-creator
SKILL.md
Workflow Creator

Create complete workflow directories with curated skills downloaded from GitHub.

Workflow Creation Process
Step 1: Create directory structure

Run scripts/create_workflow.py to initialize:

python scripts/create_workflow.py <workflow-name> --path <output-dir>


Creates (with multi-AI tool support):

workflows/<workflow-name>-workflow/
├── README.md          # User documentation (English)
├── README_cn.md       # User documentation (Chinese)
├── AGENTS.md          # AI context (auto-loaded)
├── .claude/
│   ├── settings.json
│   └── skills/        # Skills go here (primary storage)
├── .codex/
│   └── skills -> ../.claude/skills
├── .cursor/
│   └── skills -> ../.claude/skills
├── .opencode/
│   └── skill -> ../.claude/skills
├── .agents/
│   └── skills -> ../.claude/skills
├── .kilocode/
│   └── skills -> ../.claude/skills
├── .roo/
│   └── skills -> ../.claude/skills
├── .goose/
│   └── skills -> ../.claude/skills
├── .gemini/
│   └── skills -> ../.claude/skills
├── .agent/
│   └── skills -> ../.claude/skills
├── .github/
│   └── skills -> ../.claude/skills
├── skills -> .claude/skills
├── .factory/
│   └── skills -> ../.claude/skills
└── .windsurf/
    └── skills -> ../.claude/skills


Symlinks enable all AI tools to use the same skills from .claude/skills/.

Step 2: Select and download skills
Use the Skill Sources section below to find relevant skills
Download each skill using scripts/download_skill.py:
python scripts/download_skill.py <repo-url> <skill-path> --output workflows/<workflow-name>/.claude/skills/


Examples:

# Official Anthropic skills
python scripts/download_skill.py https://github.com/anthropics/skills skills/docx --output ./workflows/media-workflow/.claude/skills/

# Community skills (root level)
python scripts/download_skill.py https://github.com/gked2121/claude-skills social-repurposer --output ./workflows/media-workflow/.claude/skills/

Step 3: Generate README.md (English)

CRITICAL: Follow the exact format from workflows/marketing-pro-workflow/README.md

Required structure:

<div align="center">

# 📋 Workflow Name

### **Your AI-Powered [Domain] Team**

[← Back to AI Workflow](../../README.md)

[简体中文](./README_cn.md) | English

</div>

---

## 🎯 Who Is This For?
- **Role 1** - Use case
- **Role 2** - Use case

---

## ⚡ Quick Install
[Install commands]

---

## 📦 Skills Included (N)

### 0️⃣ Stage Name
| Skill | What It Does |
|:------|:-------------|
| `skill-name` | Description |

### 1️⃣ Next Stage
...

---

## 🔄 Complete Pipeline (N Stages)
[ASCII tree diagram]

---

## 💡 Example Workflows
[Multiple scenario examples with numbered prompts]

---

## 🔗 Skill Combinations
[Table with Goal → Skill Chain]

---

## 📄 License
MIT © [nicepkg](https://github.com/nicepkg)


Use assets/templates/README.template.md as reference.

Step 4: Generate README_cn.md (Chinese)

Create Chinese version with:

Same structure as English README
Professional Chinese terminology
Link back to ../../README_cn.md
Step 5: Generate AGENTS.md

Write AI instructions covering:

Workflow overview with pipeline diagram
Available skills grouped by stage
Skill usage guidelines (when to use each)
Recommended sequences for common tasks
Output standards
Quality gates between phases

Important: AGENTS.md is auto-loaded by Claude Code. Keep it concise (<500 lines) and focused on actionable instructions.

Use assets/templates/AGENTS.template.md as reference.

Step 6: Update project README

After creating a workflow in the ai-workflow project, update:

README.md (English):

Add new workflow to the workflow table
Add skills list under <details> section
Update skill count (e.g., "150+ skills")

README_cn.md (Chinese):

Same updates in Chinese
Link to README_cn.md in workflow folder
Skill Sources
A. Skill Aggregators & Directories (for discovering skills)
Name	Type	Scale	Best For
Skillhub Awesome Skills	GitHub curated list	1000+ skills	Top skills by category, well-organized
Skillhub.club	Online directory	1000+	Web UI for browsing by category
SkillsMP	Marketplace	63,000+	Mass search with filters (category/popularity/author)
agent-skills.md	Online directory	Large	Install commands included (pnpm dlx add-skill ...)
Claude Skills Hub	Online directory	Medium	Product-style browsing, good for inspiration
MCP Market Skills	Online store	Medium	Product pages with About/FAQ, content creator friendly
Skills Directory	Online directory	Medium	Copy SKILL.md directly, good structure
Smithery Skills	Skill directory	Medium	Includes expected_output.json, tool-oriented
Awesome Claude Skills (ComposioHQ)	GitHub awesome list	High stars	Ecosystem resources, comprehensive
Awesome Claude Skills (travisvn)	GitHub awesome list	5k+ stars	Second perspective, prevents single-source bias
Awesome Agent Skills	GitHub multi-agent list	1k+ stars	Covers Claude/Codex/Copilot/VSCode
B. Production-Ready Skill Repositories (for bulk import)
Repository	Focus	Best For
alirezarezvani/claude-skills	Multi-role skill packs	Content Creator suite (brand voice, SEO, platform frameworks)
gked2121/claude-skills	Production workflows	Clear workflow examples (Podcast→Content→Social→SEO)
sickn33/antigravity-awesome-skills	Skill registry	Organized by role (skills/content-creator)
Microck/ordinary-claude-skills	600+ skills collection	skill-navigator, SEO clustering, email optimization
synapz-org/marketing-ops-hub	Marketing orchestration	Multi-skill coordination patterns
m2ai-portfolio/claude-skills	Creator/Growth suite	IG caption, YouTube script, tweet thread, blog outline
pluginagentmarketplace/custom-plugin-product-manager	Product Manager suite	user-research, roadmap, requirements, analytics
lyndonkl/claude	Decision frameworks	prioritization, forecasting, stakeholder mapping
jamesrochabrun/skills	Mixed professional	prd-generator, technical-launch-planner
britt/claude-code-skills	Writing & specs	writing-product-specs, writing-user-stories
troykelly/codex-skills	Workflow management	work-intake, milestone-management
escarti/agentDevPrompts	Feature lifecycle	feature-planning, feature-implementing
aj-geddes/useful-ai-prompts	Sprint & agile	agile-sprint-planning, requirements-gathering
daffy0208/ai-dev-standards	Multi-role standards	customer-feedback-analyzer, go-to-market-planner
C. Search Strategy

When the above sources lack needed skills:

GitHub Search: "claude" "skills" "SKILL.md" <topic>
agent-skills.md Search: Browse by tags at https://agent-skills.md/tags
SkillsMP Search: Filter by category at https://skillsmp.com
Validate: Check SKILL.md has valid YAML frontmatter with name and description
D. Download Commands
# From GitHub repository
python scripts/download_skill.py https://github.com/<owner>/<repo> <skill-path> --output workflows/<workflow-name>/.claude/skills/

# Example: Download from alirezarezvani
python scripts/download_skill.py https://github.com/alirezarezvani/claude-skills skills/content-creator --output ./workflows/content-creator-workflow/.claude/skills/

# Example: Download from pluginagentmarketplace
python scripts/download_skill.py https://github.com/pluginagentmarketplace/custom-plugin-product-manager skills/user-research --output ./workflows/product-manager-workflow/.claude/skills/

Output Checklist

After workflow creation, verify:

 .claude/skills/ contains downloaded skill folders
 Each skill folder has SKILL.md
 All symlinks work (.codex/skills, .cursor/skills, .opencode/skill, .agents/skills, .kilocode/skills, .roo/skills, .goose/skills, .gemini/skills, .agent/skills, .github/skills, skills, .factory/skills, .windsurf/skills)
 README.md follows standard format with all sections
 README_cn.md created with Chinese translation
 AGENTS.md provides clear AI instructions (<500 lines)
 settings.json exists in .claude/
 Project README.md updated with new workflow
 Project README_cn.md updated with new workflow
 Skill counts updated in both README files
Weekly Installs
247
Repository
nicepkg/ai-workflow
GitHub Stars
176
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn