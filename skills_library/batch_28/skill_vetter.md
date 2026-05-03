---
title: skill-vetter
url: https://skills.sh/maxmilneaus/installer-pack/skill-vetter
---

# skill-vetter

skills/maxmilneaus/installer-pack/skill-vetter
skill-vetter
Installation
$ npx skills add https://github.com/maxmilneaus/installer-pack --skill skill-vetter
SKILL.md
Skill Vetter 🔒

Never install a skill without vetting it first.

When to Use
Before installing any skill from ClawHub, GitHub, or external sources
When evaluating skills shared by other agents
Step 1: Source Check
Where did it come from?
Author known/reputable?
Downloads/stars?
Last updated?
Step 2: Code Review (MANDATORY)

Read ALL files. Reject immediately if you see:

🚨 REJECT:
• curl/wget to unknown URLs
• Sends data to external servers
• Requests credentials/tokens/API keys
• Reads ~/.ssh, ~/.aws, ~/.config without reason
• Accesses MEMORY.md, USER.md, SOUL.md, IDENTITY.md
• base64 decode
• eval()/exec() with external input
• Modifies system files outside workspace
• Installs unlisted packages
• Network calls to IPs instead of domains
• Obfuscated/minified code
• Requests sudo
• Accesses browser cookies/sessions
• Touches credential files

Step 3: Permission Scope
Files read/written?
Commands run?
Network access? To where?
Scope minimal for stated purpose?
Step 4: Risk Classification
Level	Examples	Action
🟢 LOW	Notes, weather, formatting	Basic review, install OK
🟡 MEDIUM	File ops, browser, APIs	Full code review
🔴 HIGH	Credentials, trading, system	Human approval required
⛔ EXTREME	Security configs, root	Do NOT install
Output
SKILL VETTING REPORT
═══════════════════════
Skill: [name] | Source: [origin] | Author: [name] | Version: [ver]
Metrics: [downloads/stars] | Updated: [date] | Files: [count]
Red Flags: [None / list]
Permissions: Files: [list] | Network: [list] | Commands: [list]
Risk: [🟢/🟡/🔴/⛔]
Verdict: [✅ SAFE / ⚠️ CAUTION / ❌ DO NOT INSTALL]
Notes: [observations]
═══════════════════════

Quick Vet (GitHub)
curl -s "https://api.github.com/repos/OWNER/REPO" | jq '{stars: .stargazers_count, forks: .forks_count, updated: .updated_at}'
curl -s "https://api.github.com/repos/OWNER/REPO/contents/skills/SKILL_NAME" | jq '.[].name'

Trust Hierarchy
Official OpenClaw → lower scrutiny (still review)
High-star repos (1000+) → moderate
Known authors → moderate
Unknown sources → maximum
Requesting credentials → human approval always
Completion Checklist
 Source checked
 All files read, red flags checked
 Permission scope assessed
 Risk level assigned
 Verdict delivered

Unchecked = not done.

Paranoia is a feature. 🔒🦀

Credits

Originally by adamb0mbNZ — ClawHub.

Weekly Installs
62
Repository
maxmilneaus/ins…ler-pack
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn