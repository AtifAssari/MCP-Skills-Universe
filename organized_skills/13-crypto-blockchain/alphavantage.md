---
rating: ⭐⭐⭐
title: alphavantage
url: https://skills.sh/luohy15/financial-skills/alphavantage
---

# alphavantage

skills/luohy15/financial-skills/alphavantage
alphavantage
Installation
$ npx skills add https://github.com/luohy15/financial-skills --skill alphavantage
SKILL.md
Alpha Vantage Skill

Reference documentation for Alpha Vantage API endpoints and functionality.

Setup
Get your free API key at https://www.alphavantage.co/support/#api-key
Set the API key using either method:
Add ALPHAVANTAGE_API_KEY to your .env file in the running directory
Or export ALPHAVANTAGE_API_KEY as an environment variable
# Option 1: Add to .env file in running directory
echo "ALPHAVANTAGE_API_KEY=your_api_key_here" >> .env

# Option 2: Export as environment variable
export ALPHAVANTAGE_API_KEY=your_api_key_here

Usage Guidelines for Agents

When working with Alpha Vantage APIs:

Data Format: Prefer CSV over JSON when both formats are available

CSV is more compact and easier to parse for tabular data
Use datatype=csv parameter in API requests

Response Handling: Always write API responses to files first

Save responses to temporary or data files before processing
Read from files with appropriate limits to avoid context burden
Example: Use Read tool with limit parameter to control data size
Structure
references/ - All API documentation organized by category
references/index.md - Full tree view of all available APIs
Source

Documentation fetched from: https://www.alphavantage.co/documentation

Weekly Installs
14
Repository
luohy15/financial-skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn