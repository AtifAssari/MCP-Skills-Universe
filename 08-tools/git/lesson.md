---
rating: ⭐⭐
title: lesson
url: https://skills.sh/win4r/memory-lancedb-pro/lesson
---

# lesson

skills/win4r/memory-lancedb-pro/lesson
lesson
Installation
$ npx skills add https://github.com/win4r/memory-lancedb-pro --skill lesson
SKILL.md
Lesson Extraction & Storage

When triggered, extract and store lessons from the recent conversation context.

Steps
Scan recent context — identify the pitfall, bug fix, or key insight just discussed
Store technical layer (category: fact, importance ≥ 0.8):
Pitfall: [symptom]. Cause: [root cause]. Fix: [solution]. Prevention: [how to avoid].

Store principle layer (category: decision, importance ≥ 0.85):
Decision principle ([tag]): [behavioral rule]. Trigger: [when]. Action: [what to do].

Verify — memory_recall with anchor keywords to confirm both entries retrievable
Report — tell Master what was stored (brief summary)
Rules
Keep entries short and atomic (< 500 chars each)
If the lesson also affects a checklist or SKILL.md, update those files too
If no clear lesson is found in recent context, ask Master what to store
Weekly Installs
310
Repository
win4r/memory-lancedb-pro
GitHub Stars
4.3K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass