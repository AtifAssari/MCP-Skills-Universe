---
title: install-skill
url: https://skills.sh/schwepps/skills/install-skill
---

# install-skill

skills/schwepps/skills/install-skill
install-skill
Installation
$ npx skills add https://github.com/schwepps/skills --skill install-skill
SKILL.md
Skill Installer

Automates the installation of new skills into the skills marketplace project. Handles unpacking, marketplace registration, and documentation updates.

When to Use
User has a .skill file in dist/ directory
User asks to "install", "add", "unpack", or "integrate" a skill
User wants to add a new skill to the marketplace
Installation Workflow
Phase 1: Discovery

List available skill packages:

ls -la dist/*.skill


Identify target skill: If user specifies a skill name, use it. Otherwise, list available packages and ask which to install.

Verify package: Check the file exists and is a valid zip archive:

file dist/<skill-name>.skill

Phase 2: Extraction

Preview contents before extracting:

unzip -l dist/<skill-name>.skill


Extract to project root:

unzip -o dist/<skill-name>.skill


Verify extraction:

ls -la <skill-name>/
ls -la <skill-name>/references/

Phase 3: Metadata Extraction

Read SKILL.md frontmatter to extract:

name: Skill identifier (kebab-case)
description: Full description for triggers
metadata.category: Category (seo, music, security, tooling, etc.)
metadata.tags: Comma-separated tags

Parse the frontmatter between --- markers at the top of SKILL.md

Generate short description for marketplace (one line, ~60 chars max)

Phase 4: Marketplace Registration

Update .claude-plugin/marketplace.json:

a. Update the top-level description if needed to include new category

b. Add to plugins array:

{
  "name": "<skill-name>",
  "type": "skill",
  "path": "<skill-name>",
  "description": "<short-description>",
  "category": "<category>",
  "tags": ["tag1", "tag2", ...]
}


c. Add category to categories object if new:

"<category>": {
  "name": "<Category Display Name>",
  "description": "<Category description>",
  "marketplace": "marketplace-<category>.json"
}


Create/update category marketplace (marketplace-<category>.json):

If file doesn't exist, create with template:

{
  "name": "skills-<category>",
  "version": "1.0.0",
  "description": "<Category> skills for Claude Code.",
  "author": "schwepps",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/schwepps/skills.git"
  },
  "plugins": [
    { /* skill entry */ }
  ]
}


If file exists, add skill to plugins array.

Phase 5: Documentation Update

Update README.md:

a. Update header description if new category added

b. Add to "What's Included" table:

| **[<skill-name>](<skill-name>/)** | <short-description> |


c. Add usage examples section if new category:

### <Category>


"Example prompt 1" "Example prompt 2"

d. Add to "Project Structure" tree:

├── <skill-name>/


e. Add to "Browser Download" table:

| <Skill Display Name> | [Download ZIP](https://download-directory.github.io/?url=https://github.com/schwepps/skills/tree/main/<skill-name>) |

Phase 6: Verification

Verify all files updated:

 Skill directory exists with SKILL.md and references/
 marketplace.json contains skill entry
 Category marketplace file exists and contains skill
 README.md updated with skill info

Report summary:

Installed: <skill-name>
Category: <category>
Files: <count> reference files

Updated:
- .claude-plugin/marketplace.json
- .claude-plugin/marketplace-<category>.json
- README.md

Category Mappings
Category	Display Name	Description
seo	SEO & AI Search	Search engine optimization and AI search visibility
music	Music Creation	AI-powered music and audio generation
security	Smart Contract Security	Blockchain and smart contract auditing
tooling	Developer Tools	Automation and development utilities
Error Handling
File not found: List available .skill files in dist/
Invalid package: Check if file is valid zip archive
Missing SKILL.md: Package is malformed, cannot install
Missing frontmatter: Extract what's possible, ask user for missing metadata
Category conflict: Ask user to confirm category assignment
Quick Install Command

For a straightforward installation with a known skill file:

/install-skill <skill-name>


This will:

Unpack dist/<skill-name>.skill
Auto-detect metadata from SKILL.md
Register in all marketplace files
Update README.md
Report completion status
Weekly Installs
28
Repository
schwepps/skills
GitHub Stars
10
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass