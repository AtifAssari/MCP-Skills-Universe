---
rating: ⭐⭐
title: unity-async
url: https://skills.sh/besty0728/unity-skills/unity-async
---

# unity-async

skills/besty0728/unity-skills/unity-async
unity-async
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-async
SKILL.md
Unity Async Strategy

Use this skill when the user is deciding how runtime work should be scheduled or cleaned up.

Guardrails

Mode: Both (Semi-Auto + Full-Auto) — advisory only, no REST skills

Do not recommend UniTask just because it looks more advanced than coroutine.
Prefer the simplest scheduling model that fits the use case.
Decision Ladder
First ask whether the task needs per-frame work at all.
If not, prefer events, callbacks, or explicit method calls.
If a short Unity-bound sequence is needed, prefer coroutine.
Recommend UniTask only when:
the project already uses it, or
the user explicitly wants it and accepts the dependency.
Use Update only for true continuous simulation, polling, or input loops that cannot be event-driven.
Specific Guidance
Avoid many unrelated Update methods if a more event-driven flow works.
Cache references used in hot paths.
Always define lifecycle ownership:
who starts the work
who cancels or stops it
when it is cleaned up
In MonoBehaviour, prefer OnEnable / OnDisable / OnDestroy for subscribe-unsubscribe symmetry.
Use IDisposable mainly for pure C# lifetimes, temporary subscriptions, or scope-based cleanup helpers, not as a cargo-cult replacement for Unity lifecycle methods.
Output Format
Recommended scheduling model
Why it fits
Lifecycle / cancellation owner
Hot-path risks
Why the heavier alternative is unnecessary, if applicable
Weekly Installs
12
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