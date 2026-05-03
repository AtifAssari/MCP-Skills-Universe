---
rating: ⭐⭐
title: youskill-finder
url: https://skills.sh/youware-labs/youskill-finder/youskill-finder
---

# youskill-finder

skills/youware-labs/youskill-finder/youskill-finder
youskill-finder
Installation
$ npx skills add https://github.com/youware-labs/youskill-finder --skill youskill-finder
SKILL.md
YouSkill Finder

Get AI-powered skill recommendations for any open-ended task or scenario.

When to Use

Use this skill when the user:

Asks "how to..." or "how can I..." questions about building or automating something
Describes a scenario or goal without a specific solution in mind
Wants to know what tools/skills exist for a task
Asks for recommendations on approaches to a problem
Needs help with workflow automation, integrations, or AI-assisted tasks

Examples:

"How can I automate code reviews?"
"I want to build a data pipeline from Notion to a database"
"Help me set up automated testing for my project"
"What's the best way to sync data between two services?"
"I need to create a scheduled report generator"
Usage
npx @youware-labs/youskill "<describe the scenario or goal>"


Example:

npx @youware-labs/youskill "I want to automate code reviews with structured feedback"


Note: AI-powered recommendations may take 1-2 minutes to process. If using this command via an AI agent or automated tool, set a higher timeout (3 minutes or more) to avoid premature termination.

Output

Returns curated solutions with:

Title & Description - What the solution does
Trigger Prompt - Ready-to-use prompt to start the workflow
Required Skills - GitHub links to install the skills
Comparison - Trade-offs between different approaches
Rate Limits
Type	Per Hour	Per Day
Anonymous	3	10
Logged in	10	50

Upgrade with npx @youware-labs/youskill login.

Weekly Installs
30
Repository
youware-labs/yo…l-finder
GitHub Stars
3
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn