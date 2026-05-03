---
title: unity-inspector
url: https://skills.sh/besty0728/unity-skills/unity-inspector
---

# unity-inspector

skills/besty0728/unity-skills/unity-inspector
unity-inspector
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-inspector
SKILL.md
Unity Inspector Design

Use this skill when scripts need to be easier to author, configure, and review in the Inspector.

Guardrails

Mode: Both (Semi-Auto + Full-Auto) — advisory only, no REST skills

Prefer [SerializeField] private over unnecessary public fields.
Do not over-decorate with attributes when simple naming suffices.
Default Rules
Use [Header], [Tooltip], [Space], [Range], [Min], [TextArea] when they clarify authoring intent.
Use [RequireComponent] for mandatory sibling dependencies.
Use [CreateAssetMenu] for config/data assets that designers should create directly.
Use OnValidate only for lightweight editor-time validation and normalization.
Use SerializeReference only when polymorphic serialized data is genuinely needed.
Inspector Quality Checklist
Are defaults safe?
Are required references obvious?
Are fields grouped by responsibility?
Are tuning values constrained?
Are debug-only fields separated from authoring fields?
Will another person understand this script from the Inspector alone?
Output Format
Field exposure strategy
Recommended attributes
Validation rules
Authoring UX improvements
Over-design to avoid
Weekly Installs
13
Repository
besty0728/unity-skills
GitHub Stars
894
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass