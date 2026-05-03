---
title: find-skills
url: https://skills.sh/bytedance/deer-flow/find-skills
---

# find-skills

skills/bytedance/deer-flow/find-skills
find-skills
Originally fromvercel-labs/skills
Installation
$ npx skills add https://github.com/bytedance/deer-flow --skill find-skills
Summary

Discover and install specialized agent skills from the open ecosystem when users need extended capabilities.

Searches the skills directory using npx skills find [query] to match user requests against available skills across domains like React, testing, DevOps, design, and documentation
Presents matching skills with installation commands and links to skills.sh for detailed documentation
Installs selected skills globally using the install-skill.sh script, automatically linking them to the project
Activates when users ask "how do I do X," "find a skill for X," or express interest in extending agent capabilities with specialized tools or workflows
SKILL.md
Find Skills

This skill helps you discover and install skills from the open agent skills ecosystem.

When to Use This Skill

Use this skill when the user:

Asks "how do I do X" where X might be a common task with an existing skill
Says "find a skill for X" or "is there a skill for X"
Asks "can you do X" where X is a specialized capability
Expresses interest in extending agent capabilities
Wants to search for tools, templates, or workflows
Mentions they wish they had help with a specific domain (design, testing, deployment, etc.)
What is the Skills CLI?

The Skills CLI (npx skills) is the package manager for the open agent skills ecosystem. Skills are modular packages that extend agent capabilities with specialized knowledge, workflows, and tools.

Key commands:

npx skills find [query] - Search for skills interactively or by keyword
npx skills check - Check for skill updates
npx skills update - Update all installed skills

Browse skills at: https://skills.sh/

How to Help Users Find Skills
Step 1: Understand What They Need

When a user asks for help with something, identify:

The domain (e.g., React, testing, design, deployment)
The specific task (e.g., writing tests, creating animations, reviewing PRs)
Whether this is a common enough task that a skill likely exists
Step 2: Search for Skills

Run the find command with a relevant query:

npx skills find [query]


For example:

User asks "how do I make my React app faster?" → npx skills find react performance
User asks "can you help me with PR reviews?" → npx skills find pr review
User asks "I need to create a changelog" → npx skills find changelog

The command will return results like:

Install with bash /path/to/skill/scripts/install-skill.sh vercel-labs/agent-skills@vercel-react-best-practices

vercel-labs/agent-skills@vercel-react-best-practices
└ https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices

Step 3: Present Options to the User

When you find relevant skills, present them to the user with:

The skill name and what it does
The install command they can run
A link to learn more at skills.sh

Example response:

I found a skill that might help! The "vercel-react-best-practices" skill provides
React and Next.js performance optimization guidelines from Vercel Engineering.

To install it:
bash /path/to/skill/scripts/install-skill.sh vercel-labs/agent-skills@vercel-react-best-practices

Learn more: https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices

Step 4: Install the Skill

If the user wants to proceed, use the install-skill.sh script to install the skill and automatically link it to the project:

bash /path/to/skill/scripts/install-skill.sh <owner/repo@skill-name>


For example, if the user wants to install vercel-react-best-practices:

bash /path/to/skill/scripts/install-skill.sh vercel-labs/agent-skills@vercel-react-best-practices


The script will install the skill globally to skills/custom/

Common Skill Categories

When searching, consider these common categories:

Category	Example Queries
Web Development	react, nextjs, typescript, css, tailwind
Testing	testing, jest, playwright, e2e
DevOps	deploy, docker, kubernetes, ci-cd
Documentation	docs, readme, changelog, api-docs
Code Quality	review, lint, refactor, best-practices
Design	ui, ux, design-system, accessibility
Productivity	workflow, automation, git
Tips for Effective Searches
Use specific keywords: "react testing" is better than just "testing"
Try alternative terms: If "deploy" doesn't work, try "deployment" or "ci-cd"
Check popular sources: Many skills come from vercel-labs/agent-skills or ComposioHQ/awesome-claude-skills
When No Skills Are Found

If no relevant skills exist:

Acknowledge that no existing skill was found
Offer to help with the task directly using your general capabilities
Suggest the user could create their own skill with npx skills init

Example:

I searched for skills related to "xyz" but didn't find any matches.
I can still help you with this task directly! Would you like me to proceed?

If this is something you do often, you could create your own skill:
npx skills init my-xyz-skill

Weekly Installs
1.1K
Repository
bytedance/deer-flow
GitHub Stars
64.5K
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykWarn