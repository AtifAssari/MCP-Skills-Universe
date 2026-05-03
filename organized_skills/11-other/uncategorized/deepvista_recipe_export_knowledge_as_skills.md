---
rating: ⭐⭐
title: deepvista-recipe-export-knowledge-as-skills
url: https://skills.sh/deepvista-ai/deepvista-cli/deepvista-recipe-export-knowledge-as-skills
---

# deepvista-recipe-export-knowledge-as-skills

skills/deepvista-ai/deepvista-cli/deepvista-recipe-export-knowledge-as-skills
deepvista-recipe-export-knowledge-as-skills
Installation
$ npx skills add https://github.com/deepvista-ai/deepvista-cli --skill deepvista-recipe-export-knowledge-as-skills
SKILL.md
Export Knowledge as Skills

PREREQUISITE: Load the following skill: deepvista-recipe

Export Recipes as SKILL.md files that can be installed in any AI agent (Claude Code, Cursor, OpenCode, and others).

Steps

List all Recipes:

deepvista recipe list


For each Recipe to export, generate the SKILL.md:

deepvista recipe export <recipe_id> --format skill


Save each skill to the agent's skills directory:

mkdir -p ~/.agents/skills/<skill-name>/
# Write the SKILL.md content from the JSON output to that directory


Verify — the skill should now be discoverable by the agent.

Tips
Read-only recipe — only generates files, does not modify Recipes.
This is the Recipe-as-Skill pipeline: author workflows in DeepVista's GUI, export them as installable agent skills so anyone on your team can load them.
The exported SKILL.md includes the full checklist and instructions in a format agents can follow directly.
See Also
deepvista-recipe — Recipe commands
Weekly Installs
27
Repository
deepvista-ai/de…ista-cli
GitHub Stars
5
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass