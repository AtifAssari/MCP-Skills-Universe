---
title: token-efficiency
url: https://skills.sh/nickcrew/claude-ctx-plugin/token-efficiency
---

# token-efficiency

skills/nickcrew/claude-ctx-plugin/token-efficiency
token-efficiency
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill token-efficiency
SKILL.md
Token Efficiency

Compressed communication for limited context windows.

Symbol System
Logic & Flow
Symbol	Meaning
→	leads to, implies
⇒	transforms to
←	rollback
&	and
|	or
»	sequence/then
∴	therefore
∵	because
Status
Symbol	Meaning
✅	complete/pass
❌	failed/error
⚠️	warning
🔄	in progress
⏳	pending
Domains
Symbol	Domain
⚡	performance
🔍	analysis
🛡️	security
🏗️	architecture
Abbreviations
cfg config
impl implementation
deps dependencies
val validation
perf performance
sec security
err error
Examples

Standard:

"The authentication system has a security vulnerability in the user validation function"

Compressed:

auth.js:45 → 🛡️ sec risk in user val()

Standard:

"Build completed, now running tests, then deploying"

Compressed:

build ✅ » test 🔄 » deploy ⏳

When to Use
Context >75% full
Large codebase analysis
Complex multi-step workflows
User requests brevity
Weekly Installs
63
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass