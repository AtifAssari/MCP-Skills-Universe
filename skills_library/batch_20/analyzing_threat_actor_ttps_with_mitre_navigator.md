---
title: analyzing-threat-actor-ttps-with-mitre-navigator
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-threat-actor-ttps-with-mitre-navigator
---

# analyzing-threat-actor-ttps-with-mitre-navigator

skills/mukul975/anthropic-cybersecurity-skills/analyzing-threat-actor-ttps-with-mitre-navigator
analyzing-threat-actor-ttps-with-mitre-navigator
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-threat-actor-ttps-with-mitre-navigator
SKILL.md
Analyzing Threat Actor TTPs with MITRE Navigator
Overview

The MITRE ATT&CK Navigator is a web application for annotating and visualizing ATT&CK matrices. Combined with the attackcti Python library (which queries ATT&CK STIX data via TAXII), analysts can programmatically generate Navigator layer files mapping specific threat group TTPs, compare multiple groups, and assess detection coverage gaps against known adversaries.

When to Use
When investigating security incidents that require analyzing threat actor ttps with mitre navigator
When building detection rules or threat hunting queries for this domain
When SOC analysts need structured procedures for this analysis type
When validating security monitoring coverage for related attack techniques
Prerequisites
Python 3.8+ with attackcti and stix2 libraries installed
MITRE ATT&CK Navigator (web UI or local instance)
Understanding of STIX 2.1 objects and relationships
Steps
Query ATT&CK STIX data for target threat group using attackcti
Extract techniques associated with the group via STIX relationships
Generate ATT&CK Navigator layer JSON with technique annotations
Overlay detection coverage to identify gaps
Export layer for team review and defensive planning
Expected Output
{
  "name": "APT29 TTPs",
  "domain": "enterprise-attack",
  "techniques": [
    {"techniqueID": "T1566.001", "score": 1, "comment": "Spearphishing Attachment"},
    {"techniqueID": "T1059.001", "score": 1, "comment": "PowerShell"}
  ]
}

Weekly Installs
37
Repository
mukul975/anthro…y-skills
GitHub Stars
5.9K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass