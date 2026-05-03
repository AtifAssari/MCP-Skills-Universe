---
title: skill-advisor
url: https://skills.sh/v5tech/skills/skill-advisor
---

# skill-advisor

skills/v5tech/skills/skill-advisor
skill-advisor
Installation
$ npx skills add https://github.com/v5tech/skills --skill skill-advisor
SKILL.md
Skill Advisor

Search, compare, and install skills correctly to preferred agents.

Determine Operation Type

What does the user want?

Find and install new skills → Follow Installation Workflow
Remove existing skills → Read references/recovery.md
Fix broken installation → Read references/recovery.md
Update skills → Run npx skills check then npx skills update
Installation Workflow

Copy this checklist and track progress:

Skill Installation:
- [ ] Step 1: Search with multiple keywords
- [ ] Step 2: Preview and read SKILL.md
- [ ] Step 3: Compare and categorize (High/Medium/Low)
- [ ] Step 4: Generate install commands (no --all!)
- [ ] Step 5: Verify installation

Step 1: Search Skills

Search with multiple related keywords for better coverage:

npx skills find QUERY
npx skills find RELATED_QUERY

Step 2: Preview and Read SKILL.md

Preview each repository's available skills:

npx skills add owner/repo -g --list


Read actual SKILL.md content at:

https://skills.sh/owner/repo/skill-name


Never rely solely on skill names. Names can be misleading.

Step 3: Compare and Recommend

Evaluate each skill:

Dimension	Weight
Content quality (scripts, references, actionable workflows)	High
Coverage systematics (coherent skill system from same author)	High
Tech stack match	High
Source authority (Official > Org > Individual)	Medium
Maintenance activity	Medium
Function overlap	Medium

Quality criteria:

High: Scripts, detailed references, concrete examples, actionable workflows
Medium: Useful guidance but mostly text-based
Low: Generic content, replaceable by general LLM knowledge

Output format:

## Recommended (Category/Author)
| Skill | Function | Quality | Note |
|-------|----------|---------|------|
| skill-a | Actual function from SKILL.md | High | Why recommended |

## Optional
| Skill | Function | Quality | Note |
|-------|----------|---------|------|
| skill-b | Function from SKILL.md | Medium | Supplements skill-a |

## Not Recommended
| Skill | Function | Quality | Note |
|-------|----------|---------|------|
| skill-c | Function from SKILL.md | Low | Overlaps with skill-a |

Step 4: Generate Install Commands

CRITICAL: Never use --all flag — it overrides --agent and installs to ALL 41 agents.

Rules:

Only generate install commands for High quality skills
Medium quality: list in Optional section, commands provided separately
Low quality: no install commands

Correct pattern:

npx skills add owner/repo -g -s skill1 -s skill2 -a antigravity -a claude-code -a gemini-cli -a opencode -y


Parameters:

Flag	Meaning
-g	Global install (user-level)
-s SKILL	Specify skill (repeat for multiple)
-a AGENT	Target agent (repeat for multiple)
-y	Skip confirmation
-l	List available skills only
--all	DANGER: Installs all skills to all agents

Wrong vs Right:

# WRONG — --all overrides -a, installs to ALL agents
npx skills add expo/skills -g -a claude-code --all

# RIGHT — explicit -s and -a flags
npx skills add expo/skills -g -s xlsx -s pdf -a antigravity -a claude-code -a gemini-cli -a opencode -y

Step 5: Verify Installation
# List installed skills
npx skills ls -g

# Check symlinks exist
ls -la ~/.claude/skills/
ls -la ~/.gemini/skills/
ls -la ~/.gemini/antigravity/skills/
ls -la ~/.config/opencode/skills/

# Verify no unwanted directories
ls ~/.cursor/ ~/.augment/ 2>/dev/null

Default Target Agents
Agent	--agent value	Global Path
Antigravity	antigravity	~/.gemini/antigravity/skills/
Claude Code	claude-code	~/.claude/skills/
Gemini CLI	gemini-cli	~/.gemini/skills/
OpenCode	opencode	~/.config/opencode/skills/

For all 41 supported agents, read references/agents.md.

Common Pitfalls
--all flag: Overrides --agent, installs to 41 agents, creates unwanted directories
Forgetting -g: Installs to project only
Missing -s: May install all skills or prompt interactively
Trusting skill names: Always read SKILL.md content
Example

User request: "Find a skill for processing Excel files"

Response:

## Search
npx skills find excel
npx skills find spreadsheet

## Recommended (expo/skills)
| Skill | Function | Quality | Note |
|-------|----------|---------|------|
| xlsx | Create spreadsheets, analyze data, generate charts | High | Official skill, full-featured |

## Install Command
npx skills add expo/skills -g -s xlsx -a antigravity -a claude-code -a gemini-cli -a opencode -y

## Verify
npx skills ls -g

Weekly Installs
9
Repository
v5tech/skills
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn