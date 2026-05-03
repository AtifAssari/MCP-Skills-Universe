---
title: skill-share
url: https://skills.sh/composiohq/awesome-claude-skills/skill-share
---

# skill-share

skills/composiohq/awesome-claude-skills/skill-share
skill-share
Installation
$ npx skills add https://github.com/composiohq/awesome-claude-skills --skill skill-share
Summary

Create and automatically share new Claude skills with your team via Slack.

Generates properly structured skill directories with standardized SKILL.md templates, metadata, and organized subdirectories (scripts/, references/, assets/)
Validates skill format, naming conventions, and metadata completeness before packaging
Creates distributable zip files and automatically posts skill summaries to designated Slack channels using Rube integration
Enforces hyphen-case naming and YAML frontmatter standards for consistency across your skill library
SKILL.md
When to use this skill

Use this skill when you need to:

Create new Claude skills with proper structure and metadata
Generate skill packages ready for distribution
Automatically share created skills on Slack channels for team visibility
Validate skill structure before sharing
Package and distribute skills to your team

Also use this skill when:

User says he wants to create/share his skill

This skill is ideal for:

Creating skills as part of team workflows
Building internal tools that need skill creation + team notification
Automating the skill development pipeline
Collaborative skill creation with team notifications
Key Features
1. Skill Creation
Creates properly structured skill directories with SKILL.md
Generates standardized scripts/, references/, and assets/ directories
Auto-generates YAML frontmatter with required metadata
Enforces naming conventions (hyphen-case)
2. Skill Validation
Validates SKILL.md format and required fields
Checks naming conventions
Ensures metadata completeness before packaging
3. Skill Packaging
Creates distributable zip files
Includes all skill assets and documentation
Runs validation automatically before packaging
4. Slack Integration via Rube
Automatically sends created skill information to designated Slack channels
Shares skill metadata (name, description, link)
Posts skill summary for team discovery
Provides direct links to skill files
How It Works
Initialization: Provide skill name and description
Creation: Skill directory is created with proper structure
Validation: Skill metadata is validated for correctness
Packaging: Skill is packaged into a distributable format
Slack Notification: Skill details are posted to your team's Slack channel
Example Usage
When you ask Claude to create a skill called "pdf-analyzer":
1. Creates /skill-pdf-analyzer/ with SKILL.md template
2. Generates structured directories (scripts/, references/, assets/)
3. Validates the skill structure
4. Packages the skill as a zip file
5. Posts to Slack: "New Skill Created: pdf-analyzer - Advanced PDF analysis and extraction capabilities"

Integration with Rube

This skill leverages Rube for:

SLACK_SEND_MESSAGE: Posts skill information to team channels
SLACK_POST_MESSAGE_WITH_BLOCKS: Shares rich formatted skill metadata
SLACK_FIND_CHANNELS: Discovers target channels for skill announcements
Requirements
Slack workspace connection via Rube
Write access to skill creation directory
Python 3.7+ for skill creation scripts
Target Slack channel for skill notifications
Weekly Installs
1.6K
Repository
composiohq/awes…e-skills
GitHub Stars
57.5K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass