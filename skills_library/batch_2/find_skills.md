---
title: find-skills
url: https://skills.sh/site/skills.volces.com/find-skills
---

# find-skills

skills/skills.volces.com/find-skills
find-skills
$ npx skills add https://skills.volces.com/skills/clawhub/breckengan
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
npx skills add <package> - Install a skill from GitHub or other sources
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

Install with npx skills add <owner/repo@skill>

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
npx skills add vercel-labs/agent-skills@vercel-react-best-practices

Learn more: https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices

Step 4: Offer to Install

If the user wants to proceed, you can install the skill for them:

npx skills add <owner/repo@skill> -g -y


The -g flag installs globally (user-level) and -y skips confirmation prompts.

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
1.3K
Source
skills.volces.c…eckengan
First Seen
Mar 19, 2026
Security Audits
SocketPass