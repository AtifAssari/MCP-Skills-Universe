---
rating: ⭐⭐⭐
title: skillsmp api
url: https://skills.sh/kevintsai1202/skillmp-api/skillsmp-api
---

# skillsmp api

skills/kevintsai1202/skillmp-api/SkillsMP API
SkillsMP API
Installation
$ npx skills add https://github.com/kevintsai1202/skillmp-api --skill 'SkillsMP API'
SKILL.md
SkillsMP API Skill

This skill provides search functionality for the SkillsMP skill marketplace, supporting both keyword search and AI semantic search.

Prerequisites
Python 3.8 or higher
requests library (pip install requests)
SkillsMP API Key from skillsmp.com/settings/api
Installation

First-time setup requires installing the requests library:

pip install requests


[!NOTE] This step only needs to be run once. Python's requests library is the only external dependency required.

API Key Configuration
Check if API Key is configured

Before running any search script, check if .env file exists:

# Check if .env exists
test -f .env && echo "Configured" || echo "Not configured"

Setup API Key

Option 1: Using setup script (Recommended)

python scripts/setup.py <API_KEY>


Option 2: Create .env file directly

Create a .env file with the following content:

SKILLSMP_API_KEY=sk_live_skillsmp_xxxxxxxxxx


[!TIP] Get your API Key from SkillsMP API Settings

Features
1. Keyword Search

Search the skill library using keywords.

Usage:

python scripts/search.py "<keyword>" [page] [per_page] [sort]


Parameters:

Parameter	Required	Description
keyword	✓	Search keyword
page		Page number, default: 1
per_page		Items per page, default: 20, max: 100
sort		stars or recent

Examples:

# Basic search
python scripts/search.py "SEO"

# With pagination and sorting
python scripts/search.py "web scraper" 1 10 stars

2. AI Semantic Search

Use AI-powered semantic search (Cloudflare AI).

Usage:

python scripts/ai_search.py "<query>"


Parameters:

Parameter	Required	Description
query	✓	Natural language query

Examples:

python scripts/ai_search.py "How to create a web scraper"
python scripts/ai_search.py "skills for building REST APIs"

3. Install Helper

Search skills and get installation command suggestions.

Usage:

python scripts/install_helper.py "<keyword>" [limit]


Parameters:

Parameter	Required	Description
keyword	✓	Skill keyword to search
limit		Number of results to show, default: 5

Examples:

python scripts/install_helper.py "spring boot"
python scripts/install_helper.py "react" 10


Output includes:

Skill name, author, stars, description
GitHub search link to find the repository
Installation command instructions
Skill Installation

This skill integrates with add-skill CLI to install skills directly from Git repositories.

Supported Agents
Agent	Identifier	Global Skills Directory
Antigravity	antigravity	~/.gemini/antigravity/skills/
Claude Code	claude-code	~/.claude/skills/
Cursor	cursor	.cursor/skills/
Codex	codex	.codex/skills/
OpenCode	opencode	.opencode/skills/
GitHub Copilot	github-copilot	.github/copilot/skills/
Roo Code	roo	.roo/skills/
Install Command References

The add-skill tool installs skills from any Git repository.

Install specific skill to global scope (User-level):

npx add-skill <owner>/<repo> --skill "<skill-name>" -g -a antigravity -y


Install ALL skills from a repo:

npx add-skill <owner>/<repo> -g -a antigravity -y


Install to project scope (Local):

npx add-skill <owner>/<repo> --skill "<skill-name>" -a antigravity -y


List available skills in a repo:

npx add-skill <owner>/<repo> --list

Complete Installation Workflow

Search for skills Use the helper script to find the repository and skill name:

python scripts/install_helper.py "spring boot"


Verify repository content List all skills available in the repository:

npx add-skill <owner>/<repo> --list


Install the skill Choose one of the installation commands above. For most cases, use the Global Install:

npx add-skill <owner>/<repo> --skill "<skill-name>" -g -a antigravity -y


Verify Installation Check if the skill files are created in the agent's skill directory.

Response Format

Success Response:

{
  "success": true,
  "data": {
    "skills": [...]
  }
}


Error Response:

{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error message"
  }
}

Agent Workflow

When a user requests SkillsMP search functionality:

Check if .env exists

If exists → Run search script directly
If not → Guide user through setup

Guide user to get API Key

Direct user to https://skillsmp.com/settings/api
Ask user to provide the API Key

Configure API Key

Use setup.py script or create .env file
Verify setup before running search

[!CAUTION] The .env file contains sensitive information and is excluded from Git. Never share or expose your API Key publicly.

Weekly Installs
–
Repository
kevintsai1202/s…llmp-api
GitHub Stars
6
First Seen
–
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail