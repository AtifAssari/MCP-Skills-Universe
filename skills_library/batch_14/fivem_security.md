---
title: fivem-security
url: https://skills.sh/germanfndez/fiveai-skills/fivem-security
---

# fivem-security

skills/germanfndez/fiveai-skills/fivem-security
fivem-security
Installation
$ npx skills add https://github.com/germanfndez/fiveai-skills --skill fivem-security
SKILL.md
🛡️ FiveM Security & Anti-Exploit Principles

This skill provides architectural guidance for securing FiveM resources against common cheats, unauthorized event triggers, and malicious data manipulation.

Core Philosophy: NEVER TRUST THE CLIENT.

The client is in the hands of the user, which means it can be fully compromised. Every action that affects the game state, economy, or other players MUST be validated on the server.

📂 Core Concepts & Rules

Detailed rules are broken down into specific topics within the rules/ directory:

events.md: How to properly structure and validate RegisterNetEvent / TriggerServerEvent to prevent unauthorized execution.
⚠️ The Golden Rules of FiveM Security
Server Authority: The server dictates the truth. The client only requests actions.
Never Trust Parameters: Always validate arguments sent from the client (e.g., if a client says "give me $50", the server must check if the client earned it, not just blindly accept the amount).
Distance Checks: Always check the distance on the server side before allowing an interaction (e.g., looting, selling, entering a zone).
Rate Limiting: Prevent event spamming by implementing server-side cooldowns or debouncing for critical actions.
Weekly Installs
79
Repository
germanfndez/fiv…i-skills
GitHub Stars
5
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass