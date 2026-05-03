---
title: skill-lookup
url: https://skills.sh/f/awesome-chatgpt-prompts/skill-lookup
---

# skill-lookup

skills/f/awesome-chatgpt-prompts/skill-lookup
skill-lookup
Installation
$ npx skills add https://github.com/f/awesome-chatgpt-prompts --skill skill-lookup
Summary

Search, retrieve, and install reusable Agent Skills from the prompts.chat registry.

Provides two core MCP tools: search_skills for keyword-based discovery with optional category and tag filtering, and get_skill to fetch complete skill packages including SKILL.md, documentation, and helper scripts
Handles the full installation workflow: search results presentation, skill retrieval, file organization into .claude/skills/{slug}/, and verification of successful setup
Supports filtering by category (e.g., "coding", "automation") and tags to narrow skill discovery
Returns skill metadata including title, description, author, file inventory, and category/tag information to help developers evaluate before installing
SKILL.md
Workflow
Search for skills matching the user's request using search_skills
Present results with title, description, author, and file list
If the user picks a skill, retrieve it with get_skill to get all files
Install by saving files to .claude/skills/{slug}/ and verify the SKILL.md exists
Confirm installation and explain what the skill does and when it activates
Example
search_skills({"query": "code review", "limit": 5, "category": "coding"})
get_skill({"id": "abc123"})

Available Tools

Use these prompts.chat MCP tools:

search_skills - Search for skills by keyword
get_skill - Get a specific skill by ID with all its files
How to Search for Skills

Call search_skills with:

query: The search keywords from the user's request
limit: Number of results (default 10, max 50)
category: Filter by category slug (e.g., "coding", "automation")
tag: Filter by tag slug

Present results showing:

Title and description
Author name
File list (SKILL.md, reference docs, scripts)
Category and tags
Link to the skill
How to Get a Skill

Call get_skill with:

id: The skill ID

Returns the skill metadata and all file contents:

SKILL.md (main instructions)
Reference documentation
Helper scripts
Configuration files
How to Install a Skill

When the user asks to install a skill:

Call get_skill to retrieve all files
Create the directory .claude/skills/{slug}/
Save each file to the appropriate location:
SKILL.md → .claude/skills/{slug}/SKILL.md
Other files → .claude/skills/{slug}/{filename}
Read back SKILL.md to verify the frontmatter is intact
Guidelines
Always search before suggesting the user create their own skill
Present search results in a readable format with file counts
When installing, confirm the skill was saved successfully
Explain what the skill does and when it activates
Weekly Installs
1.5K
Repository
f/awesome-chatg…-prompts
GitHub Stars
161.4K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn