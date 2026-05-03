---
rating: ⭐⭐⭐
title: voltagent-docs-bundle
url: https://skills.sh/voltagent/skills/voltagent-docs-bundle
---

# voltagent-docs-bundle

skills/voltagent/skills/voltagent-docs-bundle
voltagent-docs-bundle
Installation
$ npx skills add https://github.com/voltagent/skills --skill voltagent-docs-bundle
SKILL.md
VoltAgent Embedded Docs Lookup

Look up VoltAgent docs embedded in node_modules/@voltagent/core/docs. This bundle mirrors the website docs plus additional doc sets, so it is safe to use for version-matched answers.

Where the Docs Live
node_modules/@voltagent/core/docs/
|-- actions.md
|-- agents/
|-- api/
|-- blog/
|-- community/
|-- deployment-docs/
|-- deployment.md
|-- evals.md
|-- evaluation-docs/
|-- getting-started/
|-- guardrails/
|-- integrations/
|-- models-docs/
|-- observability/
|-- observability-platform/
|-- prompt-engineering-docs/
|-- rag/
|-- recipes/
|-- repo-docs/
|-- site-examples/
|-- tools/
|-- triggers.md
|-- troubleshooting/
|-- ui/
|-- utils/
`-- workflows/


If you are inside the VoltAgent monorepo, the same content exists at:

packages/core/docs/

Lookup Flow
List available sections:
ls node_modules/@voltagent/core/docs

Search for a topic:
rg -n "workflow" node_modules/@voltagent/core/docs -g"*.md"

Read the file:
cat node_modules/@voltagent/core/docs/workflows/overview.md

Quick Commands
# List docs
ls node_modules/@voltagent/core/docs

# Find a keyword
rg -n "memory" node_modules/@voltagent/core/docs -g"*.md"

# Open a section
cat node_modules/@voltagent/core/docs/getting-started/quick-start.md

Why This Works
Docs are bundled with the installed version
Avoids web drift and outdated content
Covers the full doc surface (guides, recipes, platform docs)
Weekly Installs
226
Repository
voltagent/skills
GitHub Stars
12
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass