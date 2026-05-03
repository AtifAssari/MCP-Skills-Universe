---
title: sessions-to-blog
url: https://skills.sh/jmerta/codex-skills/sessions-to-blog
---

# sessions-to-blog

skills/jmerta/codex-skills/sessions-to-blog
sessions-to-blog
Installation
$ npx skills add https://github.com/jmerta/codex-skills --skill sessions-to-blog
SKILL.md
Sessions To Blog
Overview

Create publishable MDX blog posts from sessions/articles session logs with consistent voice, structure, and internal links, aligned to project standards.

Workflow

Resolve project standards and output location

Find the project's MDX article standards and output location (check repo docs, AGENTS, README, or content guidelines).
If standards or location are not found, ask the user before drafting.

Clarify scope and output

Ask for date range, audience, and desired length if not provided.
Use the language of the user's prompts in the logs; confirm if mixed or unclear.

Gather source entries

Read the relevant sessions/articles/YYYY-MM-DD.md blocks for the selected dates.
Extract: intent, actions, artifacts, decisions, progress, open questions, and any file paths.

Plan the post

Build a short outline using the template in references/examples.md.
Select 3 to 7 key highlights; prioritize user intent and outcomes.

Draft in the defined style

Follow references/style-and-structure.md.
Keep facts grounded in the logs; mark uncertainty explicitly.

Apply internal linking rules

Follow references/linking-rules.md for links to source logs, files, and related posts.

QA pass

Check for missing sources, broken links, and inconsistent tense.
Ensure the post is readable without the raw logs.
References
references/style-and-structure.md for voice, tone, structure, and language rules.
references/linking-rules.md for internal links and citation conventions.
references/examples.md for input and output examples and a lightweight template.
Weekly Installs
20
Repository
jmerta/codex-skills
GitHub Stars
126
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass