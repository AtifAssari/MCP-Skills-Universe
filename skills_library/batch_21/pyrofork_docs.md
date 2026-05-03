---
title: pyrofork-docs
url: https://skills.sh/edm115/skills/pyrofork-docs
---

# pyrofork-docs

skills/edm115/skills/pyrofork-docs
pyrofork-docs
Installation
$ npx skills add https://github.com/edm115/skills --skill pyrofork-docs
SKILL.md
Pyrofork Documentation Skill

This skill is a reusable, documentation-first operating guide for Pyrofork. Use it to implement features, answer questions, debug issues, and generate correct examples without needing the full docs site.

Core operating rules
Prefer asynchronous usage (async def, await, async with Client(...)) unless a clear sync requirement exists.
Treat Client lifecycle explicitly:
one-shot scripts: async with Client(...)
long-running bots: decorators/handlers + app.run()
Handle API failures explicitly; never swallow broad RPCError without logging/feedback.
For update routing, design filters + groups intentionally (group, propagation control).
Keep session handling safe: never run multiple processes against the same .session file.
Fast task routing

Pick reference files based on task type:

Setup, auth, invocation basics → references/getting-started.md
Handlers, filters, propagation, plugin architecture → references/updates-and-filters.md
Raw API, formatting, storage, proxy, scheduling, performance, test mode → references/advanced-topics.md
Errors, flood waits, session/database/network pitfalls → references/troubleshooting.md
API surface navigation (handlers/decorators/enums/errors/examples) → references/reference-map.md
Complete Topic Guides (full self-contained content from docs/source/topics/*.rst) → references/topics-complete.md
Complete FAQ (full self-contained content from docs/source/faq/*.rst) → references/faq-complete.md
Canonical implementation defaults
Installation:
pip install -U pyrofork
recommended acceleration: pip install -U tgcrypto-pyrofork
Minimum startup shape:
instantiate Client("session_name", api_id=..., api_hash=...) for first auth
after successful auth, session can usually be reused with just Client("session_name")
Flood wait strategy:
catch FloodWait and sleep e.value seconds
Handler registration preference:
ergonomic static code: decorators (@app.on_message(...))
dynamic/runtime behavior: add_handler(...) / remove_handler(...)
Output quality bar when using this skill

When producing Pyrofork code/examples:

Include correct imports (Client, filters, handler classes, errors as needed)
Keep async/sync semantics internally consistent (no mixed await mistakes)
Mention session naming implications when relevant
Mention account model constraints when relevant:
file IDs are account-bound (except sticker IDs)
user/bot both require API ID/hash during initial auth
For troubleshooting answers, provide likely root cause + concrete fix path
Known sharp edges to always account for
Calling .stop(), .restart(), .add_handler(), .remove_handler() from inside a running handler can deadlock unless block=False is used where supported.
Slow or unstable networks often appear as socket/timeout/reset errors.
PEER_ID_INVALID often means wrong id type, not-yet-met peer, or inaccessible chat.
sqlite3.OperationalError: database is locked usually means concurrent access to one session DB.
Reusable response structure for Pyrofork tasks

For implementation/debug requests, respond in this order:

Minimal diagnosis (what class of issue/task this is)
Recommended Pyrofork pattern (async lifecycle + handlers/filters/error model)
Ready-to-run code skeleton
Pitfalls and verification checklist
Scope boundary

This skill covers Pyrofork usage patterns and Telegram MTProto-facing behavior. For third-party voice call libraries (pytgcalls, tgcalls) provide integration guidance only; avoid pretending these APIs are native to Pyrofork.

Weekly Installs
11
Repository
edm115/skills
GitHub Stars
2
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn