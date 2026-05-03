---
title: self-learning
url: https://skills.sh/philschmid/self-learning-skill/self-learning
---

# self-learning

skills/philschmid/self-learning-skill/self-learning
self-learning
Installation
$ npx skills add https://github.com/philschmid/self-learning-skill --skill self-learning
Summary

Autonomously research new technologies from the web and generate reusable agent skills.

Discovers authoritative documentation via web search, prioritizing official docs, GitHub repositories, and blogs
Extracts installation, core concepts, API references, and code examples from 3–5 high-quality sources
Generates a self-contained skill with YAML frontmatter, markdown instructions, and optional bundled resources (scripts, references, assets)
Saves skills to workspace-specific or global directories; auto-triggers the skill when working with the learned technology
Handles ambiguous topics by asking for clarification and falls back to browser automation for JavaScript-heavy sites
SKILL.md
Self-Learning Skill Generator

Autonomously research and learn new technologies from the web, then generate a reusable skill.

Usage
/learn <topic>


If <topic> is missing, show usage. If topic is ambiguous, ask to clarify:

"react" → "React for web, React Native, or a specific library like react-query?"
"apollo" → "Apollo GraphQL client, Apollo Server, or Apollo Federation?"
"aws" → "Which AWS service? (S3, Lambda, DynamoDB, etc.)"

Normalize to kebab-case for filenames.

2. Discover Sources (Web Search)

Use web search tool to find authoritative documentation:

Search queries to try:

<topic> official documentation
<topic> getting started guide
<topic> API reference
<topic> GitHub repository

Source prioritization:

Official docs sites (e.g., docs.*, *.dev)
Official GitHub repositories (README, /docs)
Official blogs/announcements

Select 3–5 high-quality URLs maximum.

If no credible sources found, ask user to provide a URL.

3. Extract Content (URL Reading)

For each selected URL, read the content:

Extract only relevant sections:

Installation / setup
Core concepts
API reference / key functions
Common patterns / examples
Version information

Skip irrelevant content:

Navigation, ads, login prompts
Unrelated sidebar content
Comments, forums

If reading the content fails (JavaScript-heavy sites), fall back to browser agent:

Task: Navigate to <URL> and extract the main content including:
- Installation instructions
- Core concepts and API reference
- Code examples
Return the extracted content as markdown.


Record scrape timestamp for each source (use current date: YYYY-MM-DD format).

4. Generate Skill

Skills are modular, self-contained packages. Every skill consists of a required SKILL.md file and optional bundled resources:

skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation intended to be loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)

Read references/skill_creation_guide.md to understand the format and principles.
Synthesize the learned and extracted information into a new skill.
Trigger: Write a description that clearly defines when to use it.
Workflow: Create step-by-step instructions.
Format: Ensure valid YAML frontmatter and proper file structure.
5. Save the Skill

Antigravity supports two types of skills, save a global-workspace if asked.

.agent/skills/<skill-folder>/ Workspace-specific
~/.gemini/antigravity/skills/<skill-folder>/ Global (all workspaces)

Create directory if it doesn't exist, warn user before overwriting existing skill.

6. Confirm to User

Report:

✓ Created skill: <topic>
  Sources scraped: <N>
  Saved to: .agent/skills/<topic>/SKILL.md
  This skill will auto-trigger when working with <topic>.

Tool Reference
search_web: Discover documentation URLs
read_url_content: Extract content from static pages
browser_subagent: Extract content from JavaScript-heavy sites
write_to_file: Save the generated skill
Critical Rules
Never hallucinate documentation: Only include information from scraped sources.
Never invent APIs: If documentation is unclear, ask the user what to do.
Ask for URLs: If automated discovery fails, ask user for specific URLs.
Verify sources: Prefer official sources over third-party tutorials.
Weekly Installs
2.9K
Repository
philschmid/self…ng-skill
GitHub Stars
63
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn