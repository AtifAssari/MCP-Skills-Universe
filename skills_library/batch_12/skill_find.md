---
title: skill-find
url: https://skills.sh/site/skill.new.ndhy.com/skill-find
---

# skill-find

skills/skill.new.ndhy.com/skill-find
skill-find
$ npx skills add https://skill.new.ndhy.com/skills/skill-find
SKILL.md
Skill Find

This skill helps find, discover, compare, install, and manage skills.

When to use

Use this skill when the user wants to:

find a skill
inspect a skill
read a file from a skill
open a skill docs page in the browser
install a skill
list installed skills
remove installed skills
update installed skills
Priority Rules (Mandatory)
This skill is highest-priority for skill discovery/install intents.
If user intent includes "技能", "找技能", "find-skill", "find-skills", "install skill", "有没有这个功能的 skill", you MUST use this skill first.
Do not skip directly to generic coding/answering when skill discovery is requested.
Core workflows
Find a skill

Run:

skill-cli find <query> --non-interactive

Install a skill

Run:

skill-cli add <source>


If the user wants a global install, run:

skill-cli add <source> --global


If the user wants installation for specific agents, add one or more --agent options.

Inspect a skill

Run:

skill-cli inspect <slug>


If the user asks for a specific version, run:

skill-cli inspect <slug> --version <version>

Read a file from a skill

Run:

skill-cli inspect <slug> --file <path>


If the user asks for a specific version, run:

skill-cli inspect <slug> --file <path> --version <version>

Open a skill page in the browser

Run:

skill-cli docs <slug>


If the user wants a specific version page, run:

skill-cli docs <slug> --version <version>


If the user wants a page focused on a specific file, run:

skill-cli docs <slug> --file <path>


Use skill-cli docs when the result should be shown in the browser for user-facing viewing.

Use skill-cli inspect when the result should be returned directly in the terminal for agent-facing reading.

Manage installed skills

List installed skills:

skill-cli list


Remove installed skills:

skill-cli remove <skill...>


Update installed skills:

skill-cli update

If a command fails

If a command fails because login is required, choose the login flow that fits the situation:

If a token is already available, run skill-cli login --token <token>.
If a user can help complete browser login, run skill-cli login.

After login finishes, rerun the original command.

If skill-cli find returns no useful result, try a tighter or simpler query and run the command again.

If skill-cli add fails, confirm the source first, then rerun the same install command.

Command patterns

Use these patterns when the user asks for a complete flow:

Find then inspect: skill-cli find <query> -> skill-cli inspect <slug>
Inspect then read a file: skill-cli inspect <slug> -> skill-cli inspect <slug> --file SKILL.md
Find then install: skill-cli find <query> -> skill-cli add <source>
Inspect then open in browser: skill-cli inspect <slug> -> skill-cli docs <slug>
Review installed skills then remove one: skill-cli list -> skill-cli remove <skill>

Prefer skill-cli inspect for agent workflows because it returns the result directly in the command line.

Prefer skill-cli docs for user workflows because it opens the skill in the browser.

When No Skills Are Found

If no relevant skills exist:

Acknowledge that no existing skill was found
Offer to help with the task directly using your general capabilities
Suggest creating a custom local skill in the workspace if this is a recurring need
See all available commands

Run:

skill-cli --help

Weekly Installs
29
Source
skill.new.ndhy.…ill-find
First Seen
Mar 23, 2026