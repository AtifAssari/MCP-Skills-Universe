---
rating: ⭐⭐⭐
title: unity-architecture
url: https://skills.sh/besty0728/unity-skills/unity-architecture
---

# unity-architecture

skills/besty0728/unity-skills/unity-architecture
unity-architecture
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-architecture
SKILL.md
Unity Architecture Advisor

Use this before generating lots of gameplay scripts or when the user asks for a cleaner architecture.

Workflow
Identify scope: prototype, small game, or long-lived project.
Define the core loop and the minimum runtime systems needed.
Recommend the smallest architecture that fits the scope.
Separate:
scene/bootstrap layer
gameplay/domain logic
data/config assets
view/presentation layer
Call out what should stay simple now vs what is worth abstracting.
Output Format

When using this skill, structure the advice as:

Project tier: prototype / small-game / long-lived
Recommended modules: 3-7 modules with one-line responsibilities
Scene/bootstrap plan: where composition and initialization happen
Data ownership: what belongs in scene objects, ScriptableObjects, or pure C# classes
Communication rules: direct refs, interfaces, events, or commands
Performance risks: only the hot paths that matter
Do now / skip now: avoid over-engineering
Default Guidance
Prefer thin MonoBehaviour scripts as composition bridges.
Put reusable gameplay rules in plain C# classes when possible.
Use ScriptableObject for authored config and shared static data, not as a default dump for runtime state.
Keep dependencies explicit. Avoid hidden global state unless the project size clearly justifies a small service layer.
Favor simple module boundaries over framework-heavy architecture.
Guardrails

Mode: Both (Semi-Auto + Full-Auto) — advisory only, no REST skills

Do not start from a giant reusable framework unless the project truly needs it.
Do not add layers just to satisfy textbook SOLID wording.
Prefer a small architecture that can grow, not an impressive one that slows iteration.
Load Related Advisory Modules When Needed
Pattern choice: see ../patterns/SKILL.md
Async / Update / UniTask decisions: see ../async/SKILL.md
Inspector-facing field design: see ../inspector/SKILL.md
Script quality review: see ../scriptdesign/SKILL.md
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