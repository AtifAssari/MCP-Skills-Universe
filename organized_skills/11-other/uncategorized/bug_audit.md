---
rating: ⭐⭐⭐
title: bug-audit
url: https://skills.sh/abczsl520/bug-audit-skill/bug-audit
---

# bug-audit

skills/abczsl520/bug-audit-skill/bug-audit
bug-audit
Installation
$ npx skills add https://github.com/abczsl520/bug-audit-skill --skill bug-audit
SKILL.md
Bug Audit — Dissect, Then Verify

Do NOT run a generic checklist. Instead: read the code, extract every auditable entity, then exhaustively question each one.

Phase 1: Dissect (10-15 min)

Read all project files. Build 7 tables. These tables ARE the audit — everything found here gets verified in Phase 2.

Table 1: API Endpoints

For every route in server-side code:

| # | Method | Path | Auth? | Params validated? | Precondition | Returns | Attack vector |


For each endpoint, ask:

Can I call this without authentication?
Can I pass 0, negative, NaN, huge numbers, arrays, objects?
Can I skip a prerequisite API and call this directly?
What happens if I call this 100 times per second?
Does the response leak sensitive data (openid, internal IDs, full user objects)?
Table 2: State Machines

For every boolean/enum state variable (isGameOver, battleState, Game.running, phase, mode...):

| # | Variable | Set by | Read by | Init value | Reset when? | Can it leak across lifecycles? |


For each variable, ask:

If the game/session ends, does this get reset?
If I start a new round immediately, will stale state from the previous round affect it?
Are there race conditions between setters?
Table 3: Timers

For every setTimeout/setInterval:

| # | Type | Delay | Created in | Cleared in | What if lifecycle ends before it fires? |


For each timer, ask:

Is the handle stored for cleanup?
If the game ends / user disconnects / page navigates, does this still fire?
If it fires after cleanup, does it reference destroyed objects?
Table 4: Numeric Values

For every user-influenceable number (cost, score, damage, lootValue, kills, quantity...):

| # | Name | Source (client/server/config) | Validated? | Min | Max | What if 0? | What if negative? |


For each value, ask:

Is the server-side cap realistic? (kills cap 200 but max enemies is 50?)
Can the client send a value the server trusts without verification?
Float precision issues? (accumulated math → 290402.0000000001)
Table 5: Data Flows (Critical!)

For every pair of related APIs (buy→use, start→complete, pay→deliver, login→action):

| # | Step 1 API | Step 2 API | Token/link between them? | Can skip Step 1? | Can replay Step 1? |


This is where the biggest bugs hide. For each flow, ask:

Can I call Step 2 without ever calling Step 1? (raid-result without buy)
Can I call Step 1 once but Step 2 many times? (buy once, submit results 10 times)
Is there a one-time token linking them? If not, this is a critical vulnerability.
Can I call Step 1 with cost=0 then Step 2 with high reward?
Table 6: Resource Ledger

For every in-game resource (coins, gems, items, XP, energy...):

| # | Resource | All INFLOWS (APIs/events that add) | All OUTFLOWS (APIs/events that subtract) | Daily limits? | Can any inflow be infinite? |


For each resource, ask:

Is there any inflow without a corresponding cost? (free coins from quest with no cooldown)
Can any outflow go negative? (sell item → coins, but what if coins overflow?)
Are items in safe-box excluded from ALL outflows? (trade, sell, merge, fuse, gift)
Is there a loop? (buy item A → sell for more than cost → repeat)
Table 7: Concurrency Hotspots (TOCTOU)

For every operation that reads-then-writes shared state (balance check→deduct, stock check→reserve, coupon check→redeem):

| # | Operation | Read step | Write step | Atomic? | What if 2 requests hit simultaneously? |


This catches race conditions that single-request testing misses. For each operation, ask:

Is the read-then-write atomic? (SQL UPDATE x=x-1 WHERE x>=1 is atomic; SELECT then UPDATE is NOT)
Can two concurrent requests both pass the check and both execute the write? (double-spend)
Is there a mutex/lock/transaction? If using SQLite, is WAL mode enabled for concurrent reads?
For multi-step flows: can request A be between steps while request B starts the same flow?
Phase 2: Verify (main audit)

Go through every row in every table. For each row, determine:

🔴 Critical: exploitable security hole, data loss, crash
🟡 Medium: logic error, inconsistency, performance issue
🟢 Minor: code quality, edge case, UX issue
✅ OK: verified correct

Output format:

Bug N: [🔴/🟡/🟢] Brief description
- Row: Table X, #Y
- Cause: ...
- Fix: ...
- File: ...


Do NOT stop when you run out of "inspiration". You stop when every row in every table has been verified ✅ or flagged 🔴/🟡/🟢. This is exhaustive, not heuristic.

Phase 3: Red Team / Blue Team

After verifying all tables, switch to adversarial mode. Read references/redblue.md for the full playbook.

Structure

The playbook has 4 parts:

Universal Chains (5) — apply to ALL projects: Auth Bypass, Injection, Rate Abuse, Data Leakage, Concurrency/Race Conditions
Type-Specific Chains — pick sections matching the project:
🎮 Game: Skip-Pay-Collect, Economic Loop, State Manipulation, Anti-Cheat Bypass
📊 Data Tool: Data Access Control, Data Integrity, Scheduled Task Abuse
🔌 API Service: Key/Token Abuse, Upstream Dependency, Response Manipulation
🤖 Bot: Message Injection, Bot State Abuse
🔧 WeChat: OAuth & Identity, WebView Compatibility, H5 Hybrid
📈 Platform: Cross-Service Trust, Multi-Tenant Isolation
Blue Team Defense — for each finding, verify 4 layers: Prevention → Detection → Containment → Recovery
Execution Guide — step-by-step for the auditor
How to Run
From Phase 1 dissection, identify project type(s) — a project can match multiple types
Run ALL 5 Universal Chains
Run type-specific chains matching the project
For each 🔴 finding: verify all 4 Blue Team layers
For each 🟡 finding: verify Layer 1 (Prevention) at minimum
Phase 4: Supplement

After red/blue team, run generic checks as a final safety net. Read references/modules.md and pick sections matching the project:

🔒 Security (S1-S3): CORS, XSS, SQLi, brute force — if project has users
🔐 Crypto (C1): Hardcoded secrets, weak hashing, plaintext storage, insecure random — all projects
📊 Data (D1-D3): Timezone, atomic ops, float precision — if project has DB
⚡ Performance (P1-P2): Memory leaks, hot paths — if project is large/realtime
🎮 Game (G1-G4): State guards, rendering, config — if project is a game
🔧 WeChat (W1-W3): ES6 compat, CDN, debugging — if runs in WeChat WebView
🔌 API (A1-A3): Interface standards, rate limiting — if project is an API service
🤖 Bot (B1): Timeout, dedup, sensitive words — if project is a bot
🚀 Deploy (R1-R2): PM2, nginx, SSL, SDK overwrite — all projects
🧪 Error Handling (E1-E2): Network errors, server errors, graceful degradation — all projects
📱 UX Robustness (U1-U2): Error states, edge case UX — all projects with UI
📦 Supply Chain (SC1): npm audit, dependency vulnerabilities, lockfile integrity — all Node.js projects
📝 Logging (L1): Security event logging, audit trail completeness — all projects with users
Phase 5: Regression + Verify
Check that fixes didn't introduce new bugs
After modular split: verify cross-file variable/function reachability
Live smoke test: homepage 200, key APIs return JSON, login works, core feature functional
Phase 6: Archive

Update project docs with: date, tables built, bugs found/fixed, key pitfalls for next audit.

Key Principles
Tables first, checking second. Building the tables IS the hard work. Once you have them, verification is mechanical.
Exhaustive, not heuristic. Don't stop when you "feel done." Stop when every row is verified.
Think like an attacker. For every API: "How would I exploit this?" For every value: "What if I send garbage?"
Data flows are where critical bugs hide. The link (or lack thereof) between related APIs is the #1 source of exploitable vulnerabilities.
Generic checklists are supplements, not the main event. They catch known patterns; the tables catch project-specific logic bugs.
Reference Files
references/modules.md — Generic audit modules (Security, Crypto, Data, Performance, Game, WeChat, API, Bot, Deploy, Error Handling, UX, Supply Chain, Logging) for Phase 4 supplementary checks.
references/redblue.md — Red team attack chains (universal + 6 project types) and blue team defense verification playbook for Phase 3.
references/pitfalls.md — Real-world pitfall lookup table from 200+ bugs, plus WeChat WebView remote debugging techniques.
Weekly Installs
12
Repository
abczsl520/bug-a…it-skill
GitHub Stars
20
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykFail