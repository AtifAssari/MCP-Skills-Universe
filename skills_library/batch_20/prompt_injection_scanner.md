---
title: prompt-injection-scanner
url: https://skills.sh/jorgealves/agent_skills/prompt-injection-scanner
---

# prompt-injection-scanner

skills/jorgealves/agent_skills/prompt-injection-scanner
prompt-injection-scanner
Installation
$ npx skills add https://github.com/jorgealves/agent_skills --skill prompt-injection-scanner
SKILL.md
Prompt Injection Scanner
Purpose and Intent

The prompt-injection-scanner is a security tool specifically for the AI agent era. It identifies weak points in agent instructions where a malicious user could potentially "hijack" the agent's behavior by inserting conflicting instructions into input fields.

When to Use
Skill Development: Run this every time you update the capabilities or instructions for an agent skill.
Pre-deployment Security Review: Essential before making an agent accessible to untrusted users.
Continuous Security Auditing: Periodically scan all skills as new injection patterns are discovered.
When NOT to Use
Standard Code Auditing: Use the secret-leak-detector for credentials; this is specifically for "instruction-level" security.
Input and Output Examples
Input
skill_path: "./agent-skills/data-processor/SKILL.md"

Output

A structured report highlighting parts of the instructions that are susceptible to prompt hijacking, along with concrete mitigation strategies.

Error Conditions and Edge Cases
Missing Instructions: If a skill defines tools but provides no behavioral instructions, the scanner will flag this as a risk.
Complex Logic: Highly conditional instructions can be difficult to model and may result in false positives or negatives.
Security and Data-Handling Considerations
Metadata Focus: Only scans instructions; does not touch private user data.
Local Analysis: Recommended to run locally within the development environment.
Weekly Installs
134
Repository
jorgealves/agent_skills
GitHub Stars
1
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass