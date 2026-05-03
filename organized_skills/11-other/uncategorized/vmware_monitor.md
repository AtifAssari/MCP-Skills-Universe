---
rating: ⭐⭐
title: vmware-monitor
url: https://skills.sh/zw008/vmware-monitor/vmware-monitor
---

# vmware-monitor

skills/zw008/vmware-monitor/vmware-monitor
vmware-monitor
Installation
$ npx skills add https://github.com/zw008/vmware-monitor --skill vmware-monitor
SKILL.md
VMware Monitor (Read-Only)

Disclaimer: This is a community-maintained open-source project and is not affiliated with, endorsed by, or sponsored by VMware, Inc. or Broadcom Inc. "VMware" and "vSphere" are trademarks of Broadcom. Source code is publicly auditable at github.com/zw008/VMware-Monitor under the MIT license.

Read-only VMware vCenter/ESXi monitoring — 8 MCP tools, zero destructive code.

Code-level safety: This skill contains NO power, create, delete, snapshot, or modify operations. Not disabled — they don't exist in the codebase. Companion skills: vmware-aiops (VM lifecycle), vmware-storage (iSCSI/vSAN), vmware-vks (Tanzu Kubernetes), vmware-nsx (NSX networking), vmware-nsx-security (DFW/firewall), vmware-aria (metrics/alerts/capacity), vmware-avi (AVI/ALB/AKO). | vmware-pilot (workflow orchestration) | vmware-policy (audit/policy)

What This Skill Does
Category	Capabilities
Inventory	List VMs, ESXi hosts, datastores, clusters
Health	Active alarms, recent events (filter by severity/time)
VM Details	CPU, memory, disks, NICs, snapshots, guest OS, IP
Scanning	Scheduled alarm/log scanning with Slack/Discord webhooks
Quick Install
uv tool install vmware-monitor
vmware-monitor doctor

When to Use This Skill
List or search VMs, hosts, datastores, clusters
Check active alarms or recent events
Get detailed info about a specific VM
Set up scheduled monitoring with webhook alerts
Any read-only VMware query where safety is paramount
Alarm/Event Output: suggested_actions Field

get_alarms and get_events results include a suggested_actions list. Each item is a ready-to-use hint pointing to the correct companion skill and tool:

{
  "alarm_name": "VM CPU Ready High",
  "entity_name": "prod-db-01",
  "suggested_actions": [
    "vmware-aiops: acknowledge_vcenter_alarm(entity_name='prod-db-01', alarm_name='VM CPU Ready High')",
    "vmware-aiops: reset_vcenter_alarm(entity_name='prod-db-01', alarm_name='VM CPU Ready High')"
  ]
}


AI agents (especially smaller local models) can read these hints directly to determine which skill and tool to call next, without needing to reason about skill routing themselves.

Use companion skills for:

Power on/off, deploy, clone, migrate --> vmware-aiops
iSCSI, vSAN, datastore management --> vmware-storage
Tanzu Kubernetes clusters --> vmware-vks
Load balancing, AVI/ALB, AKO, Ingress --> vmware-avi
Related Skills — Skill Routing
User Intent	Recommended Skill
Read-only vSphere monitoring, zero risk	vmware-monitor ← this skill
Storage: iSCSI, vSAN, datastores	vmware-storage
VM lifecycle, deployment, guest ops	vmware-aiops
Tanzu Kubernetes (vSphere 8.x+)	vmware-vks
NSX networking: segments, gateways, NAT	vmware-nsx
NSX security: DFW rules, security groups	vmware-nsx-security
Aria Ops: metrics, alerts, capacity planning	vmware-aria
Multi-step workflows with approval	vmware-pilot
Load balancer, AVI, ALB, AKO, Ingress	vmware-avi (uv tool install vmware-avi)
Audit log query	vmware-policy (vmware-audit CLI)
Common Workflows
Daily Health Check
Check alarms --> vmware-monitor health alarms --target prod-vcenter
Review recent events --> vmware-monitor health events --hours 24 --severity warning
List hosts --> vmware-monitor inventory hosts --> check connection state and memory usage
If connection fails --> run vmware-monitor doctor to diagnose config/network issues
Investigate a Specific VM
Find the VM --> vmware-monitor inventory vms --power-state poweredOff
Get details --> vmware-monitor vm info problem-vm
Check related events --> vmware-monitor health events --hours 48
If VM not found --> verify VM name with vmware-monitor inventory vms --limit 100 or check target with --target <other-vcenter>
Set Up Continuous Monitoring
Configure webhook in ~/.vmware-monitor/config.yaml
Start daemon --> vmware-monitor daemon start
Daemon scans every 15 min, sends alerts to Slack/Discord
Usage Mode
Scenario	Recommended	Why
Local/small models (Ollama, Qwen)	CLI	~2K tokens vs ~8K for MCP
Cloud models (Claude, GPT-4o)	Either	MCP gives structured JSON I/O
Automated pipelines	MCP	Type-safe parameters, structured output
MCP Tools (8 — all read-only)
Tool	Description
list_virtual_machines	List VMs with filtering (power state, sort, limit)
list_esxi_hosts	ESXi hosts with CPU, memory, version, uptime
list_all_datastores	Datastores with capacity, free space, type
list_all_clusters	Clusters with host count, DRS/HA status
get_alarms	All active/triggered alarms — includes suggested_actions remediation hints
get_events	Recent events filtered by severity and time — includes suggested_actions hints
vm_info	Detailed VM info (CPU, memory, disks, NICs, snapshots)

All tools are read-only. No tool can modify, create, or delete any resource.

CLI Quick Reference
vmware-monitor inventory vms [--target <t>] [--limit 20] [--power-state poweredOn]
vmware-monitor inventory hosts [--target <t>]
vmware-monitor inventory datastores [--target <t>]
vmware-monitor inventory clusters [--target <t>]
vmware-monitor health alarms [--target <t>]
vmware-monitor health events [--hours 24] [--severity warning]
vmware-monitor vm info <vm-name> [--target <t>]
vmware-monitor scan now [--target <t>]
vmware-monitor daemon start|stop|status
vmware-monitor doctor [--skip-auth]


Full CLI reference: see references/cli-reference.md

Troubleshooting
Alarms returns empty but vCenter shows alarms

The get_alarms tool queries triggered alarms at the root folder level. Some alarms are entity-specific — try checking events instead: get_events --hours 1 --severity info.

"Connection refused" error
Run vmware-monitor doctor to diagnose
Verify target hostname/IP and port (443) in config.yaml
For self-signed certs: set disableSslCertValidation: true
Events returns too many results

Use severity filter: --severity warning (default) filters out info-level events. Use --hours 4 to narrow time range.

VM info shows "guest_os: unknown"

VMware Tools not installed or not running in the guest. Install/start VMware Tools for guest OS detection, IP address, and guest family info.

Doctor passes but commands fail with timeout

vCenter may be under heavy load. Try targeting a specific ESXi host directly instead of vCenter, or increase connection timeout in config.yaml.

Setup
uv tool install vmware-monitor
mkdir -p ~/.vmware-monitor
vmware-monitor init
chmod 600 ~/.vmware-monitor/.env  # if using webhooks


All tools are automatically audited via vmware-policy. Audit logs: vmware-audit log --last 20

Full setup guide, security details, and AI platform compatibility: see references/setup-guide.md

Audit & Safety

All operations are automatically audited via vmware-policy (@vmware_tool decorator):

Every tool call logged to ~/.vmware/audit.db (SQLite, framework-agnostic)
Policy rules enforced via ~/.vmware/rules.yaml (deny rules, maintenance windows, risk levels)
Risk classification: each tool tagged as low/medium/high/critical
View recent operations: vmware-audit log --last 20
View denied operations: vmware-audit log --status denied

vmware-policy is automatically installed as a dependency — no manual setup needed.

License

MIT — github.com/zw008/VMware-Monitor

Weekly Installs
24
Repository
zw008/vmware-monitor
GitHub Stars
7
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail