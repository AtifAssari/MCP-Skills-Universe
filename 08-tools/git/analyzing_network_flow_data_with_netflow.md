---
title: analyzing-network-flow-data-with-netflow
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-network-flow-data-with-netflow
---

# analyzing-network-flow-data-with-netflow

skills/mukul975/anthropic-cybersecurity-skills/analyzing-network-flow-data-with-netflow
analyzing-network-flow-data-with-netflow
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-network-flow-data-with-netflow
SKILL.md
Analyzing Network Flow Data with Netflow
When to Use
When investigating security incidents that require analyzing network flow data with netflow
When building detection rules or threat hunting queries for this domain
When SOC analysts need structured procedures for this analysis type
When validating security monitoring coverage for related attack techniques
Prerequisites
Familiarity with network security concepts and tools
Access to a test or lab environment for safe execution
Python 3.8+ with required dependencies installed
Appropriate authorization for any testing activities
Instructions
Install dependencies: pip install netflow
Collect NetFlow/IPFIX data from routers or use the built-in collector: python -m netflow.collector -p 9995
Parse captured flow data using netflow.parse_packet().
Analyze flows for:
Port scanning: single source to many destinations on same port
Data exfiltration: high byte-count outbound flows to unusual destinations
C2 beaconing: periodic connections with consistent intervals
Volumetric anomalies: traffic spikes beyond baseline thresholds
Generate a prioritized findings report.
python scripts/agent.py --flow-file captured_flows.json --output netflow_report.json

Examples
Parse NetFlow v9 Packet
import netflow
data, _ = netflow.parse_packet(raw_bytes, templates={})
for flow in data.flows:
    print(flow.IPV4_SRC_ADDR, flow.IPV4_DST_ADDR, flow.IN_BYTES)

Weekly Installs
47
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