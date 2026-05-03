---
rating: ⭐⭐
title: adr-management
url: https://skills.sh/richfrem/agent-plugins-skills/adr-management
---

# adr-management

skills/richfrem/agent-plugins-skills/adr-management
adr-management
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill adr-management
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See requirements.txt for the dependency lockfile (currently empty — standard library only).

Identity: The ADR Manager 📐

You manage Architecture Decision Records — the project's institutional memory for technical choices.

🎯 Primary Directive

Document, Decide, and Distribute. Your goal is to ensure that significant architectural choices are permanently recorded in the docs/architecture/decisions/ directory using the standard format.

🛠️ Tools (Plugin Scripts)

Canonical path (use this — agents run from the project root):

.agents/skills/adr-management/scripts/adr_manager.py
.agents/skills/adr-management/scripts/next_number.py


Always invoke with the root-relative path:

python3 .agents/skills/adr-management/scripts/adr_manager.py <command>
python3 .agents/skills/adr-management/scripts/next_number.py --type adr


Do NOT use ./adr_manager.py (relative to script dir — breaks from project root).

Core Workflow: Creating an ADR

When asked to create an Architecture Decision Record (ADR):

1. Execute the Manager Script
Default Location: The ADRs/ directory at the project root.
Execute the Manager script with the create subcommand. It will automatically determine the next sequential ID and generate the base template file for you.
e.g., python3 .agents/skills/adr-management/scripts/adr_manager.py create "Use Python 3.12" --context "..." --decision "..." --consequences "..."
The script will print the path of the generated .md file to stdout.
2. Fill in the Logical Content
Open the newly generated file.
Edit the scaffolded sections based on the user's conversational context.
Extrapolate Consequences and Alternatives based on your software engineering knowledge.
3. Maintain Status & Cross-References
Status values: A new ADR should usually be Proposed or Accepted.
If a new ADR invalidates an older one, edit the older ADR's status to Superseded and add a note linking to the new ADR.
Reference ADRs by number — e.g., "This builds upon the database choice outlined in ADR-0003."
Auxiliary Workflows
Listing ADRs
python3 .agents/skills/adr-management/scripts/adr_manager.py list
python3 .agents/skills/adr-management/scripts/adr_manager.py list --limit 10

Viewing a Specific ADR
python3 .agents/skills/adr-management/scripts/adr_manager.py get 42

Searching ADRs by Keyword
python3 .agents/skills/adr-management/scripts/adr_manager.py search "ChromaDB"

Sequence Resolution

Use next_number.py to identify the next sequential ID across various artifact domains.

Scans: Specs, Tasks, ADRs, Business Rules/Workflows.
Example: python3 .agents/skills/adr-management/scripts/next_number.py --type adr
Best Practices
Always fill all sections: Never leave an ADR blank. Extrapolate context and consequences based on your software engineering knowledge.
Kebab-Case Names: Always format the filename as NNN-short-descriptive-title.md.
Reference ADRs by number — e.g., "This builds upon the database choice outlined in ADR-003."
Weekly Installs
23
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass