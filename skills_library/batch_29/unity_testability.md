---
title: unity-testability
url: https://skills.sh/besty0728/unity-skills/unity-testability
---

# unity-testability

skills/besty0728/unity-skills/unity-testability
unity-testability
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-testability
SKILL.md
Unity Testability Advisor

Use this skill when deciding what logic should remain in Unity-facing classes and what should move into pure C# code.

Review Questions
Can the rule/algorithm run without Transform, GameObject, or scene state?
Can config be injected instead of read through static globals?
Can runtime decisions be moved to a plain C# class and called from a thin MonoBehaviour?
Does this need PlayMode coverage, or is EditMode enough?
Output Format
Logic that should move to pure C#
Logic that should stay Unity-facing
Suggested seams/interfaces
Candidate EditMode tests
Candidate PlayMode tests
Guardrails

Mode: Both (Semi-Auto + Full-Auto) — advisory only, no REST skills

Do not force test seams everywhere if the script is tiny and scene-bound.
Prefer a few meaningful seams over abstraction for its own sake.
Weekly Installs
14
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