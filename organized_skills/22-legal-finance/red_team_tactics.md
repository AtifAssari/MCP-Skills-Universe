---
rating: ⭐⭐
title: red-team-tactics
url: https://skills.sh/sickn33/antigravity-awesome-skills/red-team-tactics
---

# red-team-tactics

skills/sickn33/antigravity-awesome-skills/red-team-tactics
red-team-tactics
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill red-team-tactics
Summary

Red team simulation framework based on MITRE ATT&CK phases and adversary tactics.

Covers 12 attack phases from reconnaissance through impact, with objectives and techniques for each stage
Includes specific guidance for privilege escalation, defense evasion, lateral movement, and Active Directory attacks on Windows and Linux targets
Provides reconnaissance principles, initial access vectors, credential harvesting methods, and C2 operational security practices
Emphasizes detection evasion techniques, reporting requirements, and ethical boundaries to ensure scoped, non-destructive simulations
SKILL.md

AUTHORIZED USE ONLY: Use this skill only for authorized security assessments, defensive validation, or controlled educational environments.

Red Team Tactics

Adversary simulation principles based on MITRE ATT&CK framework.

1. MITRE ATT&CK Phases
Attack Lifecycle
RECONNAISSANCE → INITIAL ACCESS → EXECUTION → PERSISTENCE
       ↓              ↓              ↓            ↓
   PRIVILEGE ESC → DEFENSE EVASION → CRED ACCESS → DISCOVERY
       ↓              ↓              ↓            ↓
LATERAL MOVEMENT → COLLECTION → C2 → EXFILTRATION → IMPACT

Phase Objectives
Phase	Objective
Recon	Map attack surface
Initial Access	Get first foothold
Execution	Run code on target
Persistence	Survive reboots
Privilege Escalation	Get admin/root
Defense Evasion	Avoid detection
Credential Access	Harvest credentials
Discovery	Map internal network
Lateral Movement	Spread to other systems
Collection	Gather target data
C2	Maintain command channel
Exfiltration	Extract data
2. Reconnaissance Principles
Passive vs Active
Type	Trade-off
Passive	No target contact, limited info
Active	Direct contact, more detection risk
Information Targets
Category	Value
Technology stack	Attack vector selection
Employee info	Social engineering
Network ranges	Scanning scope
Third parties	Supply chain attack
3. Initial Access Vectors
Selection Criteria
Vector	When to Use
Phishing	Human target, email access
Public exploits	Vulnerable services exposed
Valid credentials	Leaked or cracked
Supply chain	Third-party access
4. Privilege Escalation Principles
Windows Targets
Check	Opportunity
Unquoted service paths	Write to path
Weak service permissions	Modify service
Token privileges	Abuse SeDebug, etc.
Stored credentials	Harvest
Linux Targets
Check	Opportunity
SUID binaries	Execute as owner
Sudo misconfiguration	Command execution
Kernel vulnerabilities	Kernel exploits
Cron jobs	Writable scripts
5. Defense Evasion Principles
Key Techniques
Technique	Purpose
LOLBins	Use legitimate tools
Obfuscation	Hide malicious code
Timestomping	Hide file modifications
Log clearing	Remove evidence
Operational Security
Work during business hours
Mimic legitimate traffic patterns
Use encrypted channels
Blend with normal behavior
6. Lateral Movement Principles
Credential Types
Type	Use
Password	Standard auth
Hash	Pass-the-hash
Ticket	Pass-the-ticket
Certificate	Certificate auth
Movement Paths
Admin shares
Remote services (RDP, SSH, WinRM)
Exploitation of internal services
7. Active Directory Attacks
Attack Categories
Attack	Target
Kerberoasting	Service account passwords
AS-REP Roasting	Accounts without pre-auth
DCSync	Domain credentials
Golden Ticket	Persistent domain access
8. Reporting Principles
Attack Narrative

Document the full attack chain:

How initial access was gained
What techniques were used
What objectives were achieved
Where detection failed
Detection Gaps

For each successful technique:

What should have detected it?
Why didn't detection work?
How to improve detection
9. Ethical Boundaries
Always
Stay within scope
Minimize impact
Report immediately if real threat found
Document all actions
Never
Destroy production data
Cause denial of service (unless scoped)
Access beyond proof of concept
Retain sensitive data
10. Anti-Patterns
❌ Don't	✅ Do
Rush to exploitation	Follow methodology
Cause damage	Minimize impact
Skip reporting	Document everything
Ignore scope	Stay within boundaries

Remember: Red team simulates attackers to improve defenses, not to cause harm.

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
548
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail