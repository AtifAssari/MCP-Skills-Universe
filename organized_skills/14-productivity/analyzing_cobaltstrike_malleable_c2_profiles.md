---
rating: ⭐⭐
title: analyzing-cobaltstrike-malleable-c2-profiles
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-cobaltstrike-malleable-c2-profiles
---

# analyzing-cobaltstrike-malleable-c2-profiles

skills/mukul975/anthropic-cybersecurity-skills/analyzing-cobaltstrike-malleable-c2-profiles
analyzing-cobaltstrike-malleable-c2-profiles
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-cobaltstrike-malleable-c2-profiles
SKILL.md
Analyzing CobaltStrike Malleable C2 Profiles
Overview

Cobalt Strike Malleable C2 profiles are domain-specific language scripts that customize how Beacon communicates with the team server, defining HTTP request/response transformations, sleep intervals, jitter values, user agents, URI paths, and process injection behavior. Threat actors use malleable profiles to disguise C2 traffic as legitimate services (Amazon, Google, Slack). Analyzing these profiles reveals network indicators for detection: URI patterns, HTTP headers, POST/GET transforms, DNS settings, and process injection techniques. The dissect.cobaltstrike library can parse both profile files and extract configurations from beacon payloads, while pyMalleableC2 provides AST-based parsing using Lark grammar for programmatic profile manipulation and validation.

When to Use
When investigating security incidents that require analyzing cobaltstrike malleable c2 profiles
When building detection rules or threat hunting queries for this domain
When SOC analysts need structured procedures for this analysis type
When validating security monitoring coverage for related attack techniques
Prerequisites
Python 3.9+ with dissect.cobaltstrike and/or pyMalleableC2
Sample Malleable C2 profiles (available from public repositories)
Understanding of HTTP protocol and Cobalt Strike beacon communication model
Network monitoring tools (Suricata/Snort) for signature deployment
PCAP analysis tools for traffic validation
Steps
Install libraries: pip install dissect.cobaltstrike or pip install pyMalleableC2
Parse profile with C2Profile.from_path("profile.profile")
Extract HTTP GET/POST block configurations (URIs, headers, parameters)
Identify user agent strings and spoof targets
Extract sleep time, jitter percentage, and DNS beacon settings
Analyze process injection settings (spawn-to, allocation technique)
Generate Suricata/Snort signatures from extracted network indicators
Compare profile against known threat actor profile collections
Extract staging URIs and payload delivery mechanisms
Produce detection report with IOCs and recommended network signatures
Expected Output

A JSON report containing extracted C2 URIs, HTTP headers, user agents, sleep/jitter settings, process injection config, spawned process paths, DNS settings, and generated Suricata-compatible detection rules.

Weekly Installs
45
Repository
mukul975/anthro…y-skills
GitHub Stars
5.9K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail