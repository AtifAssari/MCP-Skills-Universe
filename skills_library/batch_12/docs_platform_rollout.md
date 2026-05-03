---
title: docs-platform-rollout
url: https://skills.sh/dhananjaypawar26/docs-platform-rollout/docs-platform-rollout
---

# docs-platform-rollout

skills/dhananjaypawar26/docs-platform-rollout/docs-platform-rollout
docs-platform-rollout
Installation
$ npx skills add https://github.com/dhananjaypawar26/docs-platform-rollout --skill docs-platform-rollout
SKILL.md
Docs Platform Rollout

Use this skill when the user wants complete documentation setup in one run.

Scope

This skill is self-contained and ships the implementation details it needs in references/.

Bundled references:

references/project-docs-bootstrap.SKILL.md
references/docs-docusaurus-vercel.SKILL.md
references/skills-usage-and-vercel-deployment.md
How to load references

Read the references in this order before making changes:

references/project-docs-bootstrap.SKILL.md
references/docs-docusaurus-vercel.SKILL.md
references/skills-usage-and-vercel-deployment.md only when deployment or reuse guidance is needed
Workflow order
Use references/project-docs-bootstrap.SKILL.md to create or standardize the docs/ structure and baseline content.
Use references/docs-docusaurus-vercel.SKILL.md to publish docs with Docusaurus and configure Vercel deployment.
Validate local docs build and list deployment steps.
Inputs to confirm
Project/repo name
Branch strategy (auto deploy or manual production promotion)
Desired docs route (/docs or /)
Vercel root strategy (repo root or website)
Required outputs
Production-ready docs/ structure with governance metadata.
website/ Docusaurus site consuming root docs.
vercel.json aligned to root-directory strategy.
Root npm scripts for docs dev/build/serve.
Validation result from local docs build.
Acceptance criteria
Docs structure exists and is internally consistent.
npm --prefix website run build succeeds.
Sidebar renders all configured sections.
Vercel deployment config is explicit and reproducible.
The skill can be copied alone into another repo under .agents/skills/docs-platform-rollout/ and still be usable.
Failure handling
If docs build fails, fix MDX/sidebar/routes before finishing.
If Vercel setup fails, provide exact fallback mode (Mode A or Mode B) and branch/deploy instructions.
Weekly Installs
36
Repository
dhananjaypawar2…-rollout
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass