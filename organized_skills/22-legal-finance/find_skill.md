---
rating: ⭐⭐
title: find-skill
url: https://skills.sh/dtyq/magic/find-skill
---

# find-skill

skills/dtyq/magic/find-skill
find-skill
Installation
$ npx skills add https://github.com/dtyq/magic --skill find-skill
SKILL.md
Search and Install Skills
Search Priority

Always search in this order and stop as soon as a match is found:

My skill library (already owned, ready to use)
Platform skill market (published by platform, can be added then installed)
skillhub (external community, last resort fallback)
platform-search — Search Within Platform (Run First)

Searches both "my skill library" and the "platform skill market" simultaneously, returning JSON. Always run this before trying skillhub.

Result fields:

my_skills: In your skill library
market: Available in the platform skill market
shell_exec(
    cwd='<find-skill-absolute-path>',
    command="python scripts/search.py --keyword \"<keyword>\""
)


If found in my_skills, install with install-platform-me; if found in market, install with install-platform-market; then load with read_skills. Use the code field from search results as the argument:

shell_exec(
    command="skillhub install-platform-me <code>"
)

shell_exec(
    command="skillhub install-platform-market <code>"
)

read_skills(skill_names=["<skill-name>"])

skillhub — External Search (Fallback Only)

Only use skillhub if the platform search above returns no useful results.

Important: Never pass the cwd parameter when calling shell_exec for any skillhub command. The system automatically uses the project root as the working directory to ensure skills are installed to the correct location. Specifying cwd manually will cause skills to be installed to the wrong path.

search — Search for Skills

Keyword / natural language search, returns up to 20 results by default.

shell_exec(
    command="skillhub search \"react best practices\""
)

install — Install a Skill

The slug comes from the slug field in search results. After installation, use read_skills to load the skill — the parameter is the name field value in the skill's SKILL.md.

shell_exec(
    command="skillhub install <slug>"
)

read_skills(skill_names=["<skill-name>"])

upgrade — Upgrade Installed Skills

Upgrade all installed skills to their latest versions.

shell_exec(
    command="skillhub upgrade"
)


Upgrade a specific skill:

shell_exec(
    command="skillhub upgrade <slug>"
)

list — List Installed Skills

List all currently installed skills and their versions.

shell_exec(
    command="skillhub list"
)

install-github — Install a Skill from GitHub

Supports a full repository or a subdirectory inside a repository. After installation, use read_skills to load it.

Install from a full repository:

shell_exec(
    command="skillhub install-github https://github.com/<owner>/<repo>"
)


Install from a subdirectory:

shell_exec(
    command="skillhub install-github https://github.com/<owner>/<repo>/tree/<branch>/<path/to/skill>"
)

read_skills(skill_names=["<skill-name>"])

remove — Remove an Installed Skill
shell_exec(
    command="skillhub remove <skill-name>"
)

Weekly Installs
16
Repository
dtyq/magic
GitHub Stars
4.8K
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn