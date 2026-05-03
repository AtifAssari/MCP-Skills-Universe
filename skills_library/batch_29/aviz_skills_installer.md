---
title: aviz-skills-installer
url: https://skills.sh/aviz85/claude-skills-library/aviz-skills-installer
---

# aviz-skills-installer

skills/aviz85/claude-skills-library/aviz-skills-installer
aviz-skills-installer
Installation
$ npx skills add https://github.com/aviz85/claude-skills-library --skill aviz-skills-installer
SKILL.md
AVIZ Skills Installer

A conversational guide to installing skills from the AVIZ Skills Library.

Important: Fetch Real-Time Data

DO NOT use hardcoded skill lists. Always fetch current data from these sources:

Skills List & Setup Guides: https://aviz.github.io/claude-skills-library/
GitHub Repository: https://github.com/aviz85/claude-skills-library
Individual Skill Pages: https://aviz.github.io/claude-skills-library/skills/{skill-name}.html

Use WebFetch or WebSearch to get the latest available skills and their setup instructions.

Conversational Flow
Step 1: Discover Intent

Ask the user what they want:

See available skills → Fetch from site
Install a specific skill → Proceed to installation
Learn about a skill → Fetch its documentation page
Step 2: Fetch Available Skills

Use WebFetch on https://aviz.github.io/claude-skills-library/ to get the current list of skills.

Step 3: Choose Installation Scope

Ask the user:

Where would you like to install this skill?
1. User-based (~/.claude/skills/) - Personal, available everywhere
2. Project-based (.claude/skills/) - Shared with team via git

Step 4: Install the Skill
# Clone and copy
TEMP=$(mktemp -d)
git clone https://github.com/aviz85/claude-skills-library.git "$TEMP/lib" --depth 1

# For user-based:
mkdir -p ~/.claude/skills
cp -r "$TEMP/lib/skills/SKILL_NAME" ~/.claude/skills/

# For project-based:
mkdir -p .claude/skills
cp -r "$TEMP/lib/skills/SKILL_NAME" .claude/skills/

# Cleanup
rm -rf "$TEMP"

Step 5: Install Dependencies (if needed)
cd DESTINATION/SKILL_NAME/scripts
npm install 2>/dev/null || true

Step 6: Provide Setup Guide

Fetch the skill's documentation page and guide the user through any required configuration:

https://aviz.github.io/claude-skills-library/skills/{skill-name}.html

Conventions for Skill Documentation

Each skill in the library MUST have:

SKILL.md - Main skill file with YAML frontmatter
Setup page on GitHub Pages - At docs/skills/{skill-name}.html

Skills requiring API keys should include:

.env.example file with required variables
Setup instructions on their documentation page
See Also
Library Website: https://aviz.github.io/claude-skills-library/
GitHub Repository: https://github.com/aviz85/claude-skills-library
Weekly Installs
59
Repository
aviz85/claude-s…-library
GitHub Stars
27
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn