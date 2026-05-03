---
rating: ⭐⭐
title: smart-skill-maker
url: https://skills.sh/lingkaix/smartworkers/smart-skill-maker
---

# smart-skill-maker

skills/lingkaix/smartworkers/smart-skill-maker
smart-skill-maker
Installation
$ npx skills add https://github.com/lingkaix/smartworkers --skill smart-skill-maker
SKILL.md
Smart Skill Maker

This is the single SmartWorkers skill-authoring entry point.

It uses $skill-creator as the core drafting and improvement engine, then applies the repo's shared conventions from:

skills/general/smart-skill-maker/assets/templates/SKILL.md
skills/general/smart-skill-maker/references/AUTHORING.md
skills/general/smart-skill-maker/scripts/new_skill.sh
Required inputs
Target role and skill name
Whether the task is creating a new skill or improving an existing one
The workspace root path
Whether the source copy already exists under skills/<role>/<skill-name>/
Whether the skill should also include agents/openai.yaml
The worker role the skill belongs to
Workflow

Confirm the workspace authoring prerequisites.

skill-creator should already be installed for Codex.
npx skills should already be available.
The workspace should have a local skills/ folder with skills/AGENTS.md.

Load the canonical SmartWorkers authoring materials.

Use skills/general/smart-skill-maker/assets/templates/SKILL.md as the default scaffold.
Use skills/general/smart-skill-maker/references/AUTHORING.md as the house-style reference.
Keep skills/AGENTS.md short and operational: it should define local apply behavior, not duplicate the full style guide.

Make skills/ the source of truth.

For a new skill, create skills/<role>/<skill-name>/.
Treat <role> as the worker identity and usage scope. A role is not just a tool category; it represents a real worker with related skills and one or more workflows.
Similar capabilities may appear in different roles when the real job, workflow, or acceptance criteria differ. For example, a copy writer and an ads designer may both have image-generation skills, but those skills should still stay role-specific if the worker expectations are different.
For an existing installed skill with no source copy yet, copy .agents/skills/<skill-name>/ into skills/<role>/<skill-name>/ first, using the role that worker should own.
After that point, edit only the source copy in skills/.

Use $skill-creator for the draft or improvement loop.

Let $skill-creator handle generic skill drafting, refinement, and iteration.
Keep SmartWorkers-specific structure here:
routing detail in frontmatter description
safe placeholders in workers.example.jsonc
working files in logs/
final deliverables in artifacts/
reusable helpers in scripts/, assets/, and references/

Apply SmartWorkers conventions before finishing.

Keep name aligned with the skill folder name, and keep that name stable across routine revisions.
Add and maintain a frontmatter metadata.skill_version value so the skill revision is easy to identify without renaming the skill.
Increment metadata.skill_version every time the skill is updated.
Keep the skill body lean and operational.
Keep agents/openai.yaml in sync when present.
Keep documented file references repo-relative; do not hardcode machine-specific absolute filesystem paths.
Avoid secrets and real credentials in skill files.
When the authoring workflow changes, update this skill's assets/, references/, and scripts/ so the installed workflow and the written conventions do not drift apart.

Scaffold safely when a new source folder is needed.

From the repo root:
bash skills/general/smart-skill-maker/scripts/new_skill.sh --role <role> --name <skill-name>
Preview output goes to logs/smart-skill-maker/<timestamp>/<role>/<skill-name>/.
Use --apply only after reviewing the scaffold and making any SmartWorkers-specific adjustments.

Apply the source skill to Codex with npx skills.

From the workspace root, run:
npx skills add -a codex -y ./skills --skill <skill-name>
Use npx skills as the only install/update path into .agents/skills/.
Do not manually patch .agents/skills/<skill-name>/.

Report the result.

Name the source folder under skills/.
Confirm the apply command used.
Confirm the installed Codex copy is now managed by npx skills.
Outputs
Source skill under skills/<role>/<skill-name>/
Installed Codex skill managed under .agents/skills/<skill-name>/
Shared templates and authoring guide under skills/general/smart-skill-maker/
Any working notes or review material under logs/
Definition of done
The source copy exists under skills/<role>/<skill-name>/
The skill follows SmartWorkers conventions
The skill keeps a stable name and an explicit frontmatter metadata.skill_version
metadata.skill_version was incremented for this update
The updated skill has been applied to Codex with npx skills add -a codex -y ./skills --skill <skill-name>
No manual source-of-truth edits were left only inside .agents/skills/
If the authoring workflow changed, the supporting assets/, references/, and scripts/ under skills/general/smart-skill-maker/ were updated too
Safety / quality checklist
Do not treat .agents/skills/ as the editable source of truth.
Do not mix manual copying into .agents/skills/ with npx skills updates.
Do not commit secrets or paste credential values into skill files.
Do not let the installed smart-skill-maker contract drift away from the shared template and authoring guide.
Weekly Installs
21
Repository
lingkaix/smartworkers
First Seen
Mar 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass